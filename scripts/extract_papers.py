#!/usr/bin/env python3
"""Structured extraction over every transcribed paper.

For each converted paper in papers/papers.json, sends the full markdown
transcription to an OpenAI model with a strict JSON schema and writes:

  papers/extracts/<key>.json   - structured extract (the comparison database)
  papers/summaries/<key>.md    - one-page summary (metadata header generated
                                 here; body written by the model in the same
                                 API call as the extract)

Resumable: papers with an existing extract are skipped unless --force.

Run with the pdf-to-md venv (has the openai package + .env API key):
  /Users/bren/Documents/code/pdf-to-md/.venv/bin/python scripts/extract_papers.py [--only KEY] [--force] [--workers N]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "papers" / "papers.json"
DATASETS_PATH = ROOT / "data" / "datasets.json"
EXTRACTS_DIR = ROOT / "papers" / "extracts"
SUMMARIES_DIR = ROOT / "papers" / "summaries"

# Reuse pdf-to-md's .env loader so OPENAI_API_KEY is available.
sys.path.insert(0, "/Users/bren/Documents/code/pdf-to-md")
from pdf_to_md import load_default_env_files  # noqa: E402

MODEL = "gpt-5.5"
REASONING_EFFORT = "high"  # gpt-5.5 default is "medium" when omitted
MAX_CHARS = 250_000
REQUEST_TIMEOUT = 600
MAX_RETRIES = 4

HUMOR_THEORIES = [
    "SSTH (script opposition)",
    "GTVH",
    "incongruity-resolution",
    "appropriate incongruity",
    "benign violation",
    "superiority",
    "relief",
    "surprise theory",
    "frame-shifting / conceptual blending",
    "humor styles (Martin HSQ)",
    "other",
    "none",
]

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "title": {"type": "string", "description": "Exact paper title"},
        "authors": {"type": "array", "items": {"type": "string"}},
        "year": {"type": ["integer", "null"]},
        "venue": {"type": ["string", "null"], "description": "Venue as stated in the paper itself"},
        "paper_types": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["benchmark", "dataset", "method", "evaluation-study", "survey", "position", "HCI-study", "theory", "system", "shared-task"],
            },
        },
        "research_questions": {"type": "array", "items": {"type": "string"}},
        "tasks": {
            "type": "array",
            "description": "Humor-related tasks studied, e.g. 'humor explanation', 'pun generation', 'caption ranking', 'humor detection', 'joke translation'",
            "items": {"type": "string"},
        },
        "humor_domains": {
            "type": "array",
            "description": "e.g. puns, one-liners, cartoon captions, memes, comics, stand-up, Oogiri, news headlines, conversational humor, satire, sarcasm",
            "items": {"type": "string"},
        },
        "modalities": {
            "type": "array",
            "items": {"type": "string", "enum": ["text", "image", "video", "audio"]},
        },
        "languages": {"type": "array", "items": {"type": "string"}},
        "datasets_used": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string", "description": "Canonical dataset name; if it matches a known dataset from the provided list, use exactly that name"},
                    "role": {"type": "string", "enum": ["introduced", "evaluated-on", "trained-on", "source-material", "analyzed"]},
                    "size": {"type": ["string", "null"], "description": "Size as stated, e.g. '2,589 puns'"},
                },
                "required": ["name", "role", "size"],
            },
        },
        "models_evaluated": {
            "type": "array",
            "description": "Canonical model names actually run/evaluated in the paper (not merely cited), e.g. 'GPT-4o', 'Claude 3.5 Sonnet', 'LLaVA-1.5-13B'",
            "items": {"type": "string"},
        },
        "methods_proposed": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string"},
                    "summary": {"type": "string", "description": "1-2 sentence description"},
                },
                "required": ["name", "summary"],
            },
        },
        "humor_theories": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "theory": {"type": "string", "enum": HUMOR_THEORIES},
                    "usage": {"type": "string", "enum": ["operationalized", "grounding/motivation", "cited-in-passing"]},
                    "detail": {"type": ["string", "null"]},
                },
                "required": ["theory", "usage", "detail"],
            },
        },
        "evaluation_methods": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "type": {"type": "string", "enum": ["human-eval", "LLM-as-judge", "automatic-metric", "live-audience", "crowd-votes", "expert-annotation"]},
                    "detail": {"type": "string"},
                },
                "required": ["type", "detail"],
            },
        },
        "headline_results": {
            "type": "array",
            "description": "The paper's most important quantitative results, with exact numbers",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "finding": {"type": "string", "description": "One sentence stating the result"},
                    "metric": {"type": ["string", "null"]},
                    "value": {"type": ["string", "null"], "description": "Exact number/range as stated"},
                    "dataset": {"type": ["string", "null"]},
                    "best_system": {"type": ["string", "null"], "description": "Which model/system achieved it"},
                },
                "required": ["finding", "metric", "value", "dataset", "best_system"],
            },
        },
        "key_findings": {
            "type": "array",
            "description": "3-6 takeaways, each one sentence, grounded in the paper",
            "items": {"type": "string"},
        },
        "limitations": {"type": "array", "items": {"type": "string"}},
        "safety_ethics_notes": {"type": ["string", "null"]},
        "artifacts": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "code_url": {"type": ["string", "null"]},
                "data_url": {"type": ["string", "null"]},
                "other": {"type": ["string", "null"]},
            },
            "required": ["code_url", "data_url", "other"],
        },
        "one_pager_markdown": {
            "type": "string",
            "description": "The one-page summary body in Markdown (see instructions)",
        },
    },
    "required": [
        "title", "authors", "year", "venue", "paper_types", "research_questions",
        "tasks", "humor_domains", "modalities", "languages", "datasets_used",
        "models_evaluated", "methods_proposed", "humor_theories", "evaluation_methods",
        "headline_results", "key_findings", "limitations", "safety_ethics_notes",
        "artifacts", "one_pager_markdown",
    ],
}

SYSTEM_PROMPT = """You are a meticulous research analyst building a comparison database over humor-and-LLMs papers.

You will receive the full Markdown transcription of one paper (transcribed page-by-page from the PDF; there may be minor OCR artifacts). Extract ONLY what the paper itself states — no outside knowledge, no speculation. Rules:

- Exact numbers: report metrics/values verbatim (e.g. "84.5%", "Kendall tau 0.89"). Never round or invent.
- Empty arrays / nulls when the paper genuinely lacks a field. Do not pad.
- datasets_used: every dataset the paper introduces, trains on, evaluates on, or draws material from. If a name matches one in the KNOWN DATASETS list you are given, use exactly that canonical name.
- models_evaluated: only models actually run in experiments; use canonical public names.
- humor_theories: only theories the paper actually engages with; "operationalized" means the theory shapes the method/annotation scheme, not just the intro.
- headline_results: 2-6 rows covering the paper's most load-bearing numbers.

one_pager_markdown: write a ~400-650 word single-page summary a researcher could read instead of the paper. Use exactly these section headers (## level):
## TL;DR
(2-3 sentences: what the paper does and the single most important result)
## Problem & Motivation
## Approach
## Data & Experimental Setup
## Results
(specific numbers; what beat what by how much)
## Takeaways
(bulleted; include what this means for anyone building or evaluating humor systems)
## Limitations & Caveats

Do NOT include the paper title as a heading (the header is added by tooling). Write plainly and concretely; every claim grounded in the paper. Do not use the word "delve"."""


def load_known_datasets() -> list[str]:
    if not DATASETS_PATH.exists():
        return []
    catalog = json.loads(DATASETS_PATH.read_text(encoding="utf-8"))
    return sorted({d["name"] for d in catalog["datasets"]})


def build_client():
    from openai import OpenAI

    return OpenAI()


def call_model(client, paper: dict, markdown: str, known_datasets: list[str]) -> dict:
    user_content = (
        f"Paper identity (from library catalog): ref {paper['ref']}, "
        f"\"{paper['title']}\" ({paper.get('venue', '')}, {paper.get('year', '')}).\n\n"
        f"KNOWN DATASETS (use these exact names when they match): {', '.join(known_datasets)}\n\n"
        f"FULL PAPER MARKDOWN:\n\n{markdown}"
    )
    last_err = None
    for attempt in range(MAX_RETRIES):
        try:
            response = client.responses.create(
                model=MODEL,
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_content},
                ],
                reasoning={"effort": REASONING_EFFORT},
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "paper_extract",
                        "schema": SCHEMA,
                        "strict": True,
                    }
                },
                timeout=REQUEST_TIMEOUT,
            )
            return json.loads(response.output_text)
        except Exception as exc:
            last_err = exc
            if attempt < MAX_RETRIES - 1:
                sleep_s = min(60, 5 * 2**attempt)
                print(f"  retry {attempt + 1} after error: {str(exc)[:120]} (sleep {sleep_s}s)", file=sys.stderr)
                time.sleep(sleep_s)
    raise RuntimeError(f"Extraction failed after {MAX_RETRIES} attempts") from last_err


def summary_header(paper: dict, extract: dict, datasets_by_paper: dict) -> str:
    lines = [f"# {extract['title']}"]
    authors = ", ".join(extract["authors"]) if extract["authors"] else paper.get("authors", "")
    lines.append("")
    lines.append(f"**{authors}** — {paper.get('venue', '')} · Guide entry {paper['ref']} ({paper['section']})")
    lines.append("")
    links = []
    if paper.get("page_url"):
        links.append(f"[paper page]({paper['page_url']})")
    links.append(f"[local PDF](../pdfs/{paper['key']}.pdf)")
    links.append(f"[full markdown](../md/{paper['key']}/{paper['key']}.md)")
    links.append(f"[extract](../extracts/{paper['key']}.json)")
    for ds in datasets_by_paper.get(paper["key"], []):
        if ds.get("local_path"):
            links.append(f"[dataset: {ds['name']}](../../{ds['local_path']}/)")
    lines.append(" · ".join(links))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Extract only this paper key")
    parser.add_argument("--force", action="store_true", help="Re-extract even if output exists")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    load_default_env_files()
    EXTRACTS_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)

    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    known_datasets = load_known_datasets()

    datasets_by_paper: dict[str, list[dict]] = {}
    if DATASETS_PATH.exists():
        for ds in json.loads(DATASETS_PATH.read_text(encoding="utf-8"))["datasets"]:
            for pk in ds.get("paper_keys", []):
                datasets_by_paper.setdefault(pk, []).append(ds)

    todo = []
    for paper in papers:
        if args.only and paper["key"] != args.only:
            continue
        if paper.get("status") != "converted":
            continue
        if not args.force and (EXTRACTS_DIR / f"{paper['key']}.json").exists():
            continue
        todo.append(paper)

    print(f"Extracting {len(todo)} papers with {args.workers} workers (model {MODEL})", flush=True)

    client_state = threading.local()

    def get_client():
        if getattr(client_state, "client", None) is None:
            client_state.client = build_client()
        return client_state.client

    def process(paper: dict) -> tuple[str, bool, str]:
        key = paper["key"]
        md_path = ROOT / paper["md_path"]
        markdown = md_path.read_text(encoding="utf-8")
        truncated = False
        if len(markdown) > MAX_CHARS:
            markdown = markdown[:MAX_CHARS]
            truncated = True
        started = time.time()
        try:
            extract = call_model(get_client(), paper, markdown, known_datasets)
        except Exception as exc:
            print(f"[{key}] FAILED: {str(exc)[:200]}", flush=True)
            return key, False, str(exc)[:500]

        one_pager = extract.pop("one_pager_markdown")
        record = {
            "key": key,
            "ref": paper["ref"],
            "section": paper["section"],
            "extracted_at": time.strftime("%Y-%m-%d"),
            "extraction_model": MODEL,
            "extraction_reasoning_effort": REASONING_EFFORT,
            "source_md": paper["md_path"],
            "source_md_sha256": hashlib.sha256(
                md_path.read_bytes()
            ).hexdigest(),
            "source_truncated": truncated,
            **extract,
        }
        (EXTRACTS_DIR / f"{key}.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (SUMMARIES_DIR / f"{key}.md").write_text(
            summary_header(paper, extract, datasets_by_paper) + "\n" + one_pager.strip() + "\n",
            encoding="utf-8",
        )
        print(f"[{key}] ok in {int(time.time() - started)}s", flush=True)
        return key, True, ""

    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(process, paper) for paper in todo]
        for future in as_completed(futures):
            key, ok, _ = future.result()
            if not ok:
                failures.append(key)

    print(f"\nDone: {len(todo) - len(failures)} extracted, {len(failures)} failed")
    if failures:
        print("Failed: " + ", ".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
