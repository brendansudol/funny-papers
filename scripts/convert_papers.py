#!/usr/bin/env python3
"""Convert every downloaded paper PDF to Markdown via the pdf-to-md tool.

Reads papers/papers.json, runs pdf-to-md on each entry with status
"downloaded", and updates the catalog (status -> "converted", md_path)
as each paper finishes. Safe to re-run: already-converted papers are
skipped, and partially-converted papers resume page-by-page thanks to
pdf-to-md's --resume flag.

Concurrency: PAPER_WORKERS papers at a time, each transcribing
PAGE_WORKERS pages concurrently.

Run with any python3:
  python3 scripts/convert_papers.py            # convert everything pending
  python3 scripts/convert_papers.py --only KEY # convert one paper
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "papers" / "papers.json"
MD_DIR = ROOT / "papers" / "md"
RUNS_DIR = ROOT / "papers" / "runs"

PDF_TO_MD_DIR = Path("/Users/bren/Documents/code/pdf-to-md")
VENV_PYTHON = PDF_TO_MD_DIR / ".venv" / "bin" / "python"
PDF_TO_MD = PDF_TO_MD_DIR / "pdf_to_md.py"

PAPER_WORKERS = 2
PAGE_WORKERS = 3
REQUEST_TIMEOUT = 240

catalog_lock = threading.Lock()


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def save_paper_update(key: str, **fields) -> None:
    """Re-read, update one entry, write back (under lock, so progress survives kills)."""
    with catalog_lock:
        catalog = load_catalog()
        for paper in catalog["papers"]:
            if paper["key"] == key:
                paper.update(fields)
                break
        CATALOG_PATH.write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )


def already_converted(paper: dict) -> bool:
    key = paper["key"]
    combined = MD_DIR / key / f"{key}.md"
    if not combined.exists() or combined.stat().st_size == 0:
        return False
    expected = paper.get("page_count")
    if expected:
        pages = len(list((MD_DIR / key / "pages").glob("page_*.md")))
        return pages >= expected
    return True


def convert(paper: dict) -> tuple[str, bool, str]:
    key = paper["key"]
    pdf_path = ROOT / paper["pdf_path"]
    out_dir = MD_DIR / key
    progress_path = RUNS_DIR / f"{key}.progress.jsonl"

    cmd = [
        str(VENV_PYTHON),
        str(PDF_TO_MD),
        str(pdf_path),
        "-o",
        str(out_dir),
        "--workers",
        str(PAGE_WORKERS),
        "--resume",
        "--quiet",
        "--json",
        "--request-timeout",
        str(REQUEST_TIMEOUT),
        "--progress-jsonl",
        str(progress_path),
    ]

    started = time.time()
    print(f"[{key}] converting {paper.get('page_count', '?')} pages...", flush=True)
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(PDF_TO_MD_DIR)
    )
    elapsed = int(time.time() - started)

    summary = None
    if proc.stdout.strip():
        try:
            summary = json.loads(proc.stdout.strip().splitlines()[-1])
        except json.JSONDecodeError:
            pass

    if proc.returncode == 0 and summary and summary.get("ok"):
        combined = out_dir / f"{pdf_path.stem}.md"
        save_paper_update(
            key,
            status="converted",
            md_path=str(combined.relative_to(ROOT)),
            md_pages_dir=str((out_dir / "pages").relative_to(ROOT)),
            md_page_files=summary.get("page_files"),
            md_model=summary.get("model"),
            converted_seconds=elapsed,
        )
        print(
            f"[{key}] done in {elapsed}s ({summary.get('page_files')} pages)",
            flush=True,
        )
        return key, True, ""

    error = (proc.stderr or proc.stdout or "unknown error").strip()[-2000:]
    save_paper_update(key, status="convert_failed", convert_error=error)
    print(f"[{key}] FAILED after {elapsed}s: {error[:200]}", flush=True)
    return key, False, error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Convert only this paper key")
    args = parser.parse_args()

    MD_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    catalog = load_catalog()
    todo = []
    for paper in catalog["papers"]:
        if args.only and paper["key"] != args.only:
            continue
        if paper.get("status") not in ("downloaded", "convert_failed", "converted"):
            continue
        if already_converted(paper):
            if paper.get("status") != "converted":
                save_paper_update(paper["key"], status="converted")
            continue
        todo.append(paper)

    total_pages = sum(p.get("page_count", 0) for p in todo)
    print(
        f"Converting {len(todo)} papers (~{total_pages} pages), "
        f"{PAPER_WORKERS} papers x {PAGE_WORKERS} page-workers",
        flush=True,
    )

    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=PAPER_WORKERS) as executor:
        futures = {executor.submit(convert, paper): paper["key"] for paper in todo}
        for future in as_completed(futures):
            key, ok, _error = future.result()
            if not ok:
                failures.append(key)

    print(f"\nFinished: {len(todo) - len(failures)} converted, {len(failures)} failed")
    if failures:
        print("Failed keys: " + ", ".join(failures))

    # Regenerate the human-readable manifest from the final catalog state.
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_manifest.py")], check=False
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
