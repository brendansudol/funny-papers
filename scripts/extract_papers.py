#!/usr/bin/env python3
"""Structured extraction over transcribed public and restricted papers.

For each converted paper in papers/papers.json, sends the full markdown
transcription to an OpenAI model with a strict JSON schema and writes:

  papers/extracts/<key>.json   - structured extract (the comparison database)
  papers/summaries/<key>.md    - one-page summary (metadata header generated
                                 here; body written by the model in the same
                                 API call as the extract)

Resumable: papers with an existing extract are skipped unless --force.
Restricted sources require ``--include-restricted`` and never expose local
PDF/Markdown links or private paths. Book-length sources use complete,
catalog-defined page units, private chapter caches, and a final synthesis pass;
the script never truncates source text.

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

try:
    from evidence_schema import EVIDENCE_INSTRUCTIONS, EVIDENCE_PROFILE_SCHEMA
    from extraction_planning import (
        expected_page_count,
        format_page_spec,
        missing_page_files,
        plan_chapter_inputs,
        validate_chapter_units,
    )
    from paper_sources import (
        access_notice,
        chapter_cache_dir,
        is_restricted,
        paper_md_path,
        paper_pages_dir,
        paper_pdf_path,
        public_source_links,
    )
except ModuleNotFoundError:  # Imported as scripts.extract_papers in tests/tools.
    from scripts.evidence_schema import EVIDENCE_INSTRUCTIONS, EVIDENCE_PROFILE_SCHEMA
    from scripts.extraction_planning import (
        expected_page_count,
        format_page_spec,
        missing_page_files,
        plan_chapter_inputs,
        validate_chapter_units,
    )
    from scripts.paper_sources import (
        access_notice,
        chapter_cache_dir,
        is_restricted,
        paper_md_path,
        paper_pages_dir,
        paper_pdf_path,
        public_source_links,
    )

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "papers" / "papers.json"
DATASETS_PATH = ROOT / "data" / "datasets.json"
EXTRACTS_DIR = ROOT / "papers" / "extracts"
SUMMARIES_DIR = ROOT / "papers" / "summaries"

MODEL = "gpt-5.5"
REASONING_EFFORT = "high"  # gpt-5.5 default is "medium" when omitted
MAX_CHARS = 250_000  # per source unit; exceeding it is an error, never truncation
MAX_SYNTHESIS_CHARS = 500_000  # structured chapter records, not raw full text
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
        "evidence_profile": EVIDENCE_PROFILE_SCHEMA,
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
        "evidence_profile", "headline_results", "key_findings", "limitations", "safety_ethics_notes",
        "artifacts", "one_pager_markdown",
    ],
}

CHAPTER_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "summary": {
            "type": "string",
            "description": "A source-grounded summary of this unit, including its role in the work",
        },
        "research_questions": {"type": "array", "items": {"type": "string"}},
        "tasks": {"type": "array", "items": {"type": "string"}},
        "humor_domains": {"type": "array", "items": {"type": "string"}},
        "modalities": {"type": "array", "items": {"type": "string"}},
        "languages": {"type": "array", "items": {"type": "string"}},
        "datasets_and_artifacts": {"type": "array", "items": {"type": "string"}},
        "models_and_systems": {"type": "array", "items": {"type": "string"}},
        "methods_and_theories": {"type": "array", "items": {"type": "string"}},
        "evaluation_and_evidence": {"type": "array", "items": {"type": "string"}},
        "quantitative_results": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "finding": {"type": "string"},
                    "value": {"type": ["string", "null"]},
                    "context": {"type": "string"},
                    "source_pages": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["finding", "value", "context", "source_pages"],
            },
        },
        "key_findings": {"type": "array", "items": {"type": "string"}},
        "limitations": {"type": "array", "items": {"type": "string"}},
        "safety_ethics_notes": {"type": ["string", "null"]},
        "coverage_notes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Ambiguities, OCR problems, cross-references, or qualifications the synthesis pass must preserve",
        },
    },
    "required": [
        "summary",
        "research_questions",
        "tasks",
        "humor_domains",
        "modalities",
        "languages",
        "datasets_and_artifacts",
        "models_and_systems",
        "methods_and_theories",
        "evaluation_and_evidence",
        "quantitative_results",
        "key_findings",
        "limitations",
        "safety_ethics_notes",
        "coverage_notes",
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

""" + EVIDENCE_INSTRUCTIONS + """

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

CHAPTER_SYSTEM_PROMPT = """You are performing the first pass of a complete long-document extraction.

You will receive exactly one catalog-defined page unit from a paper or book. Extract only what that unit states. Page boundaries are marked as <!-- source-page-NNNN -->. Preserve exact numbers, distinguish the author's claims from cited claims, and attach physical source-page numbers to quantitative results. Capture qualifications and cross-references needed by a later whole-work synthesis. Do not infer what unprovided chapters contain, do not write a final paper summary, and use empty arrays/nulls rather than padding."""

SYNTHESIS_SYSTEM_PROMPT = SYSTEM_PROMPT.replace(
    "You will receive the full Markdown transcription of one paper (transcribed page-by-page from the PDF; there may be minor OCR artifacts).",
    "You will receive source-grounded structured records covering every physical page of one paper or book. Synthesize across all records; do not treat any individual chapter as the whole work.",
) + "\n\nParaphrase source prose. Do not reproduce extended passages from the work."


def load_known_datasets() -> list[str]:
    if not DATASETS_PATH.exists():
        return []
    catalog = json.loads(DATASETS_PATH.read_text(encoding="utf-8"))
    return sorted({d["name"] for d in catalog["datasets"]})


def load_default_env_files() -> None:
    """Use the required sibling project's environment loader for paid runs."""
    sys.path.insert(0, "/Users/bren/Documents/code/pdf-to-md")
    from pdf_to_md import load_default_env_files as load  # type: ignore

    load()


def build_client():
    from openai import OpenAI

    return OpenAI()


def call_json_response(
    client,
    *,
    system_prompt: str,
    user_content: str,
    schema: dict,
    schema_name: str,
) -> dict:
    """Call the configured model with retries and one strict JSON schema."""
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            response = client.responses.create(
                model=MODEL,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                reasoning={"effort": REASONING_EFFORT},
                text={
                    "format": {
                        "type": "json_schema",
                        "name": schema_name,
                        "schema": schema,
                        "strict": True,
                    }
                },
                timeout=REQUEST_TIMEOUT,
            )
            return json.loads(response.output_text)
        except Exception as exc:
            last_error = exc
            if attempt < MAX_RETRIES - 1:
                sleep_seconds = min(60, 5 * 2**attempt)
                print(
                    f"  retry {attempt + 1} after error: {str(exc)[:120]} "
                    f"(sleep {sleep_seconds}s)",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(sleep_seconds)
    raise RuntimeError(f"{schema_name} failed after {MAX_RETRIES} attempts") from last_error


def call_model(client, paper: dict, markdown: str, known_datasets: list[str]) -> dict:
    source_scope = paper.get("extraction", {}).get("source_scope", "complete paper")
    pending = [
        source.get("label", "publisher source")
        for source in paper.get("official_sources", [])
        if source.get("consulted") is False
    ]
    pending_note = (
        "\nUNCONSULTED CATALOG SOURCES (do not claim coverage or findings from these): "
        + "; ".join(pending)
        if pending
        else ""
    )
    user_content = (
        f"Paper identity (from library catalog): ref {paper['ref']}, "
        f"\"{paper['title']}\" ({paper.get('venue', '')}, {paper.get('year', '')}).\n"
        f"CONSULTED SOURCE SCOPE: {source_scope}.{pending_note}\n\n"
        f"KNOWN DATASETS (use these exact names when they match): {', '.join(known_datasets)}\n\n"
        f"FULL PAPER MARKDOWN:\n\n{markdown}"
    )
    return call_json_response(
        client,
        system_prompt=SYSTEM_PROMPT,
        user_content=user_content,
        schema=SCHEMA,
        schema_name="paper_extract",
    )


def call_chapter_model(
    client,
    paper: dict,
    unit: dict,
    known_datasets: list[str],
) -> dict:
    user_content = chapter_user_content(paper, unit, known_datasets)
    return call_json_response(
        client,
        system_prompt=CHAPTER_SYSTEM_PROMPT,
        user_content=user_content,
        schema=CHAPTER_SCHEMA,
        schema_name="chapter_extract",
    )


def chapter_user_content(
    paper: dict,
    unit: dict,
    known_datasets: list[str],
) -> str:
    return (
        f"WORK IDENTITY: {paper['ref']} / {paper['key']} / {paper['title']}\n"
        f"UNIT: {unit['title']} (physical source pages {unit['page_spec']})\n"
        f"KNOWN DATASETS (use exact names when they match): {', '.join(known_datasets)}\n\n"
        f"UNIT MARKDOWN:\n\n{unit['markdown']}"
    )


def call_synthesis_model(
    client,
    paper: dict,
    chapter_records: list[dict],
    known_datasets: list[str],
) -> dict:
    serialized = json.dumps(chapter_records, ensure_ascii=False)
    if len(serialized) > MAX_SYNTHESIS_CHARS:
        raise ValueError(
            f"{paper['key']} chapter records total {len(serialized):,} characters; "
            "add a hierarchical synthesis stage instead of truncating them"
        )
    source_scope = paper.get("extraction", {}).get("source_scope", "complete work")
    pending = [
        source.get("label", "publisher source")
        for source in paper.get("official_sources", [])
        if source.get("consulted") is False
    ]
    pending_note = (
        "\nUNCONSULTED CATALOG SOURCES (do not claim coverage or findings from these): "
        + "; ".join(pending)
        if pending
        else ""
    )
    user_content = (
        f"Paper identity (from library catalog): ref {paper['ref']}, "
        f"\"{paper['title']}\" ({paper.get('venue', '')}, {paper.get('year', '')}).\n"
        f"CONSULTED SOURCE SCOPE: {source_scope}.{pending_note}\n\n"
        f"KNOWN DATASETS (use these exact names when they match): {', '.join(known_datasets)}\n\n"
        "COMPLETE ORDERED UNIT RECORDS:\n\n"
        f"{serialized}"
    )
    return call_json_response(
        client,
        system_prompt=SYNTHESIS_SYSTEM_PROMPT,
        user_content=user_content,
        schema=SCHEMA,
        schema_name="paper_synthesis",
    )


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value_sha256(value) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_json_atomic(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def chapter_cache_signature(
    paper: dict,
    source_hash: str,
    unit: dict,
    known_datasets: list[str],
) -> dict[str, object]:
    request_contract = {
        "system_prompt": CHAPTER_SYSTEM_PROMPT,
        "user_content": chapter_user_content(paper, unit, known_datasets),
        "schema": CHAPTER_SCHEMA,
        "schema_name": "chapter_extract",
    }
    return {
        "source_md_sha256": source_hash,
        "extraction_config_sha256": value_sha256(paper.get("extraction", {})),
        "chapter_request_sha256": value_sha256(request_contract),
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "unit_id": unit["id"],
        "source_pages": unit["page_spec"],
        "source_characters": unit["char_count"],
    }


def load_or_extract_chapter(
    client,
    paper: dict,
    unit: dict,
    known_datasets: list[str],
    source_hash: str,
    force: bool,
) -> dict:
    cache_path = chapter_cache_dir(ROOT, paper) / f"{unit['id']}.json"
    signature = chapter_cache_signature(
        paper,
        source_hash,
        unit,
        known_datasets,
    )
    if cache_path.exists() and not force:
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            cached = None
        if (
            isinstance(cached, dict)
            and cached.get("provenance") == signature
            and isinstance(cached.get("analysis"), dict)
        ):
            print(f"[{paper['key']}] cached {unit['id']}", flush=True)
            return cached["analysis"]

    print(
        f"[{paper['key']}] extracting {unit['id']} "
        f"(pages {unit['page_spec']}, {unit['char_count']:,} chars)",
        flush=True,
    )
    analysis = call_chapter_model(client, paper, unit, known_datasets)
    write_json_atomic(
        cache_path,
        {
            "provenance": signature,
            "extracted_at": time.strftime("%Y-%m-%d"),
            "unit": {
                "id": unit["id"],
                "parent_id": unit["parent_id"],
                "title": unit["title"],
                "source_pages": unit["page_spec"],
            },
            "analysis": analysis,
        },
    )
    return analysis


def extract_document(
    client,
    paper: dict,
    known_datasets: list[str],
    force_chapters: bool,
) -> tuple[dict, str, dict]:
    md_path = paper_md_path(ROOT, paper)
    if not md_path.is_file():
        raise FileNotFoundError(
            f"{paper['key']} has no complete transcription; run convert_papers.py first"
        )
    source_hash = file_sha256(md_path)
    strategy = paper.get("extraction", {}).get("strategy", "single")

    if strategy == "single":
        markdown = md_path.read_text(encoding="utf-8")
        if len(markdown) > MAX_CHARS:
            raise ValueError(
                f"{paper['key']} has {len(markdown):,} characters, above the "
                f"{MAX_CHARS:,}-character single-pass limit; configure complete chapter units"
            )
        extract = call_model(client, paper, markdown, known_datasets)
        page_count = expected_page_count(paper)
        coverage = {
            "strategy": "single-pass",
            "source_scope": paper.get("extraction", {}).get(
                "source_scope", "complete paper"
            ),
            "source_page_count": page_count,
            "covered_page_count": page_count,
            "source_characters": len(markdown),
            "complete_for_consulted_scope": True,
        }
        return extract, source_hash, coverage

    if strategy != "chapters":
        raise ValueError(f"{paper['key']} has unknown extraction strategy {strategy!r}")
    if not is_restricted(paper):
        raise ValueError(
            f"{paper['key']} chapter caches require restricted/private source mode"
        )

    units = plan_chapter_inputs(paper, paper_pages_dir(ROOT, paper), MAX_CHARS)
    chapter_records = []
    for unit in units:
        analysis = load_or_extract_chapter(
            client,
            paper,
            unit,
            known_datasets,
            source_hash,
            force_chapters,
        )
        chapter_records.append(
            {
                "unit_id": unit["id"],
                "parent_unit_id": unit["parent_id"],
                "unit_title": unit["title"],
                "physical_source_pages": unit["page_spec"],
                "analysis": analysis,
            }
        )
    extract = call_synthesis_model(client, paper, chapter_records, known_datasets)
    page_count = expected_page_count(paper)
    coverage = {
        "strategy": "chapter-extraction-plus-synthesis",
        "source_scope": paper.get("extraction", {}).get(
            "source_scope", "complete work"
        ),
        "source_page_count": page_count,
        "covered_page_count": sum(len(unit["pages"]) for unit in units),
        "complete_for_consulted_scope": True,
        "units": [
            {
                "id": unit["id"],
                "title": unit["title"],
                "source_pages": unit["page_spec"],
                "source_characters": unit["char_count"],
            }
            for unit in units
        ],
    }
    return extract, source_hash, coverage


def summary_header(paper: dict, extract: dict, datasets_by_paper: dict) -> str:
    lines = [f"# {extract['title']}"]
    authors = ", ".join(extract["authors"]) if extract["authors"] else paper.get("authors", "")
    lines.append("")
    lines.append(f"**{authors}** — {paper.get('venue', '')} · Guide entry {paper['ref']} ({paper['section']})")
    lines.append("")
    links = []
    if is_restricted(paper):
        for source in public_source_links(paper):
            label = str(source["label"])
            if source.get("consulted") is True:
                label += " (consulted)"
            elif source.get("consulted") is False:
                label += " (not yet consulted)"
            links.append(f"[{label}]({source['url']})")
    else:
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
    if is_restricted(paper):
        lines.append(access_notice(paper))
        lines.append("")
    return "\n".join(lines)


def public_source_metadata(paper: dict, source_hash: str, coverage: dict) -> dict:
    metadata = {
        "source_access": "restricted" if is_restricted(paper) else "distributed",
        "source_md_sha256": source_hash,
        "source_truncated": False,
        "extraction_coverage": coverage,
    }
    if is_restricted(paper):
        metadata.update(
            {
                "source_notice": access_notice(paper),
                "source_official_sources": public_source_links(paper),
                "catalog_entry_source_coverage_complete": not any(
                    source.get("consulted") is False
                    for source in paper.get("official_sources", [])
                ),
            }
        )
    else:
        metadata["source_md"] = paper["md_path"]
    return metadata


def dry_run_plan(paper: dict) -> dict:
    strategy = paper.get("extraction", {}).get("strategy", "single")
    md_path = paper_md_path(ROOT, paper)
    plan = {
        "key": paper["key"],
        "access": "restricted" if is_restricted(paper) else "distributed",
        "strategy": strategy,
        "source_pdf_present": paper_pdf_path(ROOT, paper).is_file(),
        "transcription_present": md_path.is_file(),
    }
    if strategy == "single":
        if not md_path.is_file():
            plan["status"] = "awaiting-conversion"
            return plan
        char_count = len(md_path.read_text(encoding="utf-8"))
        plan["source_characters"] = char_count
        if char_count > MAX_CHARS:
            plan["status"] = "blocked"
            plan["error"] = (
                f"source exceeds {MAX_CHARS:,} characters and needs chapter units"
            )
        else:
            plan["status"] = "ready"
        return plan

    if strategy != "chapters":
        raise ValueError(f"unknown extraction strategy {strategy!r}")
    configured = validate_chapter_units(paper)
    plan["configured_units"] = [
        {
            "id": unit["id"],
            "title": unit["title"],
            "source_pages": format_page_spec(unit["pages"]),
        }
        for unit in configured
    ]
    page_count = expected_page_count(paper)
    assert page_count is not None
    missing = missing_page_files(paper_pages_dir(ROOT, paper), page_count)
    if not md_path.is_file() or missing:
        plan["status"] = "awaiting-conversion"
        plan["missing_page_transcriptions"] = len(missing)
        return plan
    planned = plan_chapter_inputs(paper, paper_pages_dir(ROOT, paper), MAX_CHARS)
    plan["status"] = "ready"
    plan["planned_units"] = [
        {
            "id": unit["id"],
            "title": unit["title"],
            "source_pages": unit["page_spec"],
            "source_characters": unit["char_count"],
        }
        for unit in planned
    ]
    return plan


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Extract only this paper key")
    parser.add_argument("--force", action="store_true", help="Re-extract even if output exists")
    parser.add_argument(
        "--force-chapters",
        action="store_true",
        help="Re-extract private chapter caches as well as the final output",
    )
    parser.add_argument(
        "--include-restricted",
        action="store_true",
        help="Explicitly allow a restricted source; private intermediates stay ignored",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print extraction plans without loading credentials or calling a model",
    )
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    selected = next((paper for paper in papers if paper["key"] == args.only), None)
    if args.only and selected is None:
        parser.error(f"unknown paper key: {args.only}")
    if selected and is_restricted(selected) and not args.include_restricted:
        parser.error("restricted sources require --include-restricted")
    if args.include_restricted and not args.only and not args.dry_run:
        parser.error("paid restricted extraction requires a scoped --only KEY")

    eligible = []
    for paper in papers:
        if args.only and paper["key"] != args.only:
            continue
        if paper.get("status") == "converted":
            eligible.append(paper)
        elif is_restricted(paper) and args.include_restricted:
            eligible.append(paper)

    if args.dry_run:
        plans = []
        failed = False
        for paper in eligible:
            try:
                plan = dry_run_plan(paper)
            except Exception as exc:
                plan = {
                    "key": paper["key"],
                    "status": "invalid",
                    "error": str(exc),
                }
            failed = failed or plan["status"] in {"blocked", "invalid"}
            plans.append(plan)
        print(json.dumps({"model_calls": 0, "plans": plans}, indent=2))
        return 1 if failed else 0

    EXTRACTS_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    force_output = args.force or args.force_chapters
    todo = [
        paper
        for paper in eligible
        if force_output or not (EXTRACTS_DIR / f"{paper['key']}.json").exists()
    ]
    print(
        f"Extracting {len(todo)} papers with {args.workers} workers (model {MODEL})",
        flush=True,
    )
    if not todo:
        return 0

    load_default_env_files()
    known_datasets = load_known_datasets()

    datasets_by_paper: dict[str, list[dict]] = {}
    if DATASETS_PATH.exists():
        for ds in json.loads(DATASETS_PATH.read_text(encoding="utf-8"))["datasets"]:
            for pk in ds.get("paper_keys", []):
                datasets_by_paper.setdefault(pk, []).append(ds)

    client_state = threading.local()

    def get_client():
        if getattr(client_state, "client", None) is None:
            client_state.client = build_client()
        return client_state.client

    def process(paper: dict) -> tuple[str, bool, str]:
        key = paper["key"]
        started = time.time()
        try:
            extract, source_hash, coverage = extract_document(
                get_client(), paper, known_datasets, args.force_chapters
            )
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
            **public_source_metadata(paper, source_hash, coverage),
            **extract,
        }
        write_json_atomic(EXTRACTS_DIR / f"{key}.json", record)
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
