#!/usr/bin/env python3
"""Convert downloaded paper PDFs to Markdown via the pdf-to-md tool.

Reads papers/papers.json, runs pdf-to-md on each entry with status
"downloaded", and updates the catalog (status -> "converted", md_path)
as each paper finishes. Safe to re-run: already-converted papers are
skipped, and partially-converted papers resume page-by-page thanks to
pdf-to-md's --resume flag.

Restricted sources are excluded unless ``--include-restricted`` is supplied.
Their PDFs, Markdown, page files, manifests, and logs remain below the
gitignored ``papers/private/<key>/`` tree, and their catalog status remains
``restricted``.

Concurrency: PAPER_WORKERS papers at a time, each transcribing
PAGE_WORKERS pages concurrently.

Run with any python3:
  python3 scripts/convert_papers.py            # convert everything pending
  python3 scripts/convert_papers.py --only KEY # convert one paper
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from paper_sources import (
        conversion_progress_path,
        is_restricted,
        paper_md_dir,
        paper_md_path,
        paper_pages_dir,
        paper_pdf_path,
    )
except ModuleNotFoundError:  # Imported as scripts.convert_papers in tests/tools.
    from scripts.paper_sources import (
        conversion_progress_path,
        is_restricted,
        paper_md_dir,
        paper_md_path,
        paper_pages_dir,
        paper_pdf_path,
    )

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
SERIALIZED_RESPONSE_PREFIXES = ("Response(", "ChatCompletion(")
PAGE_FILE_RE = re.compile(r"page_(\d+)\.md$")


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


def invalid_page_files(paper: dict) -> list[Path]:
    """Find page outputs that accidentally contain a serialized SDK response."""
    invalid: list[Path] = []
    for path in paper_pages_dir(ROOT, paper).glob("page_*.md"):
        text = path.read_text(encoding="utf-8", errors="replace").lstrip()
        if text.startswith(SERIALIZED_RESPONSE_PREFIXES):
            invalid.append(path)
    return sorted(invalid)


def discard_invalid_page_outputs(paper: dict) -> list[int]:
    """Remove corrupt pages and their manifest rows before a resumed conversion."""
    paths = invalid_page_files(paper)
    page_numbers = {
        int(match.group(1))
        for path in paths
        if (match := PAGE_FILE_RE.search(path.name)) is not None
    }
    if not page_numbers:
        return []

    for path in paths:
        path.unlink()

    out_dir = paper_md_dir(ROOT, paper)
    manifest_path = out_dir / "manifest.jsonl"
    if manifest_path.exists():
        kept: list[str] = []
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                kept.append(line)
                continue
            if record.get("page") not in page_numbers:
                kept.append(line)
        manifest_path.write_text(
            "\n".join(kept) + ("\n" if kept else ""), encoding="utf-8"
        )

    combined = paper_md_path(ROOT, paper)
    if combined.exists():
        combined.unlink()
    return sorted(page_numbers)


def already_converted(paper: dict) -> bool:
    combined = paper_md_path(ROOT, paper)
    if not combined.exists() or combined.stat().st_size == 0:
        return False
    if invalid_page_files(paper):
        return False
    expected = (
        paper.get("restricted_source", {}).get("page_count")
        if is_restricted(paper)
        else paper.get("page_count")
    )
    if expected:
        pages = len(list(paper_pages_dir(ROOT, paper).glob("page_*.md")))
        return pages >= expected
    return True


def convert(paper: dict) -> tuple[str, bool, str]:
    key = paper["key"]
    pdf_path = paper_pdf_path(ROOT, paper)
    out_dir = paper_md_dir(ROOT, paper)
    progress_path = conversion_progress_path(ROOT, paper)
    out_dir.mkdir(parents=True, exist_ok=True)
    progress_path.parent.mkdir(parents=True, exist_ok=True)

    invalid_pages = discard_invalid_page_outputs(paper)
    if invalid_pages:
        print(
            f"[{key}] retrying {len(invalid_pages)} invalid page outputs: "
            + ", ".join(str(page) for page in invalid_pages),
            flush=True,
        )

    if not pdf_path.exists():
        error = f"source PDF not found: {pdf_path}"
        print(f"[{key}] FAILED: {error}", flush=True)
        return key, False, error

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
        invalid_after_conversion = invalid_page_files(paper)
        if invalid_after_conversion:
            pages = ", ".join(
                match.group(1)
                for path in invalid_after_conversion
                if (match := PAGE_FILE_RE.search(path.name)) is not None
            )
            error = f"serialized SDK response found in converted page(s): {pages}"
            if not is_restricted(paper):
                save_paper_update(key, status="convert_failed", convert_error=error)
            print(f"[{key}] FAILED after {elapsed}s: {error}", flush=True)
            return key, False, error

        generated = out_dir / f"{pdf_path.stem}.md"
        combined = paper_md_path(ROOT, paper)
        if generated != combined:
            generated.replace(combined)
        if not is_restricted(paper):
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
    if not is_restricted(paper):
        save_paper_update(key, status="convert_failed", convert_error=error)
    print(f"[{key}] FAILED after {elapsed}s: {error[:200]}", flush=True)
    return key, False, error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Convert only this paper key")
    parser.add_argument(
        "--include-restricted",
        action="store_true",
        help="Explicitly allow restricted sources; all outputs stay under papers/private/",
    )
    args = parser.parse_args()

    MD_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    catalog = load_catalog()
    if args.only:
        selected = next(
            (paper for paper in catalog["papers"] if paper["key"] == args.only),
            None,
        )
        if selected is None:
            parser.error(f"unknown paper key: {args.only}")
        if is_restricted(selected) and not args.include_restricted:
            parser.error("restricted sources require --include-restricted")
    if args.include_restricted and not args.only:
        parser.error("paid restricted conversion requires a scoped --only KEY")

    todo = []
    for paper in catalog["papers"]:
        if args.only and paper["key"] != args.only:
            continue
        if is_restricted(paper):
            if not args.include_restricted:
                continue
            if already_converted(paper):
                continue
            todo.append(paper)
            continue
        if paper.get("status") not in ("downloaded", "convert_failed", "converted"):
            continue
        if already_converted(paper):
            if paper.get("status") != "converted":
                save_paper_update(paper["key"], status="converted")
            continue
        todo.append(paper)

    total_pages = sum(
        p.get("restricted_source", {}).get("page_count", p.get("page_count", 0))
        for p in todo
    )
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
