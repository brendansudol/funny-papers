#!/usr/bin/env python3
"""Add methodological evidence profiles to existing paper extracts.

This is separate from extract_papers.py so the library can backfill evidence
metadata without regenerating the existing extracts or one-page summaries.

Run with the pdf-to-md venv:
  /Users/bren/Documents/code/pdf-to-md/.venv/bin/python scripts/enrich_evidence.py [--only KEY] [--force] [--workers N]
"""

from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from evidence_schema import EVIDENCE_INSTRUCTIONS, EVIDENCE_PROFILE_SCHEMA

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "papers" / "papers.json"
EXTRACTS_DIR = ROOT / "papers" / "extracts"

sys.path.insert(0, "/Users/bren/Documents/code/pdf-to-md")
from pdf_to_md import load_default_env_files  # noqa: E402

MODEL = "gpt-5.5"
REASONING_EFFORT = "high"
MAX_CHARS = 250_000
REQUEST_TIMEOUT = 600
MAX_RETRIES = 4

RESPONSE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {"evidence_profile": EVIDENCE_PROFILE_SCHEMA},
    "required": ["evidence_profile"],
}

SYSTEM_PROMPT = f"""You are a meticulous research-methods analyst auditing evidence in humor-and-AI papers.

Extract only study-design facts supported by the supplied paper. The existing extract is a navigation aid, not an authority; resolve conflicts in favor of the full paper. Use null and explicit reporting gaps instead of guessing. The contamination-risk level is the sole analyst assessment and must have a transparent basis.

{EVIDENCE_INSTRUCTIONS}"""


def build_client():
    from openai import OpenAI

    return OpenAI()


def call_model(client, paper: dict, extract: dict, markdown: str) -> dict:
    user_content = (
        f"PAPER IDENTITY: {paper['ref']} / {paper['key']} / {paper['title']}\n\n"
        f"EXISTING STRUCTURED EXTRACT:\n{json.dumps(extract, ensure_ascii=False)}\n\n"
        f"FULL PAPER MARKDOWN:\n\n{markdown}"
    )
    last_error = None
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
                        "name": "evidence_profile",
                        "schema": RESPONSE_SCHEMA,
                        "strict": True,
                    }
                },
                timeout=REQUEST_TIMEOUT,
            )
            return json.loads(response.output_text)["evidence_profile"]
        except Exception as exc:
            last_error = exc
            if attempt < MAX_RETRIES - 1:
                sleep_seconds = min(60, 5 * 2**attempt)
                print(
                    f"  retry {attempt + 1}: {str(exc)[:120]} (sleep {sleep_seconds}s)",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(sleep_seconds)
    raise RuntimeError(f"Evidence enrichment failed after {MAX_RETRIES} attempts") from last_error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Enrich only this paper key")
    parser.add_argument("--force", action="store_true", help="Replace an existing evidence profile")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    load_default_env_files()
    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    todo = []
    for paper in papers:
        if paper.get("status") != "converted":
            continue
        if args.only and paper["key"] != args.only:
            continue
        extract_path = EXTRACTS_DIR / f"{paper['key']}.json"
        extract = json.loads(extract_path.read_text(encoding="utf-8"))
        if not args.force and extract.get("evidence_profile"):
            continue
        todo.append((paper, extract_path, extract))

    print(
        f"Enriching {len(todo)} evidence profiles with {args.workers} workers "
        f"(model {MODEL}, reasoning {REASONING_EFFORT})",
        flush=True,
    )
    client_state = threading.local()

    def get_client():
        if getattr(client_state, "client", None) is None:
            client_state.client = build_client()
        return client_state.client

    def process(item) -> tuple[str, bool, str]:
        paper, extract_path, extract = item
        key = paper["key"]
        markdown = (ROOT / paper["md_path"]).read_text(encoding="utf-8")
        if len(markdown) > MAX_CHARS:
            markdown = markdown[:MAX_CHARS]
        started = time.time()
        try:
            profile = call_model(get_client(), paper, extract, markdown)
            extract["evidence_enriched_at"] = time.strftime("%Y-%m-%d")
            extract["evidence_extraction_model"] = MODEL
            extract["evidence_extraction_reasoning_effort"] = REASONING_EFFORT
            extract["evidence_profile"] = profile
            temp_path = extract_path.with_suffix(".json.tmp")
            temp_path.write_text(
                json.dumps(extract, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            temp_path.replace(extract_path)
        except Exception as exc:
            print(f"[{key}] FAILED: {str(exc)[:200]}", flush=True)
            return key, False, str(exc)[:500]
        print(f"[{key}] ok in {int(time.time() - started)}s", flush=True)
        return key, True, ""

    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(process, item) for item in todo]
        for future in as_completed(futures):
            key, ok, _ = future.result()
            if not ok:
                failures.append(key)

    print(f"\nDone: {len(todo) - len(failures)} enriched, {len(failures)} failed")
    if failures:
        print("Failed: " + ", ".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
