#!/usr/bin/env python3
"""Download every paper PDF listed in papers/papers.json.

For each pending entry, tries pdf_candidates in order, keeps the first
response that looks like a real PDF, and (when a `verify` phrase is set)
checks the phrase appears in the first pages' extracted text. A verify
miss is recorded as verify_ok=false but the file is kept, since scanned
PDFs may have no text layer.

Updates papers.json in place with status / pdf_path / pdf_source /
page_count. Safe to re-run; already-downloaded files are skipped.

Run with the pdf-to-md venv python (needs pymupdf):
  /Users/bren/Documents/code/pdf-to-md/.venv/bin/python scripts/download_papers.py
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "papers" / "papers.json"
PDF_DIR = ROOT / "papers" / "pdfs"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
MIN_PDF_BYTES = 10_000


def fetch(url: str, timeout: float = 90.0) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,application/octet-stream,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def pdf_info(data: bytes, verify_phrase: str | None) -> tuple[int, bool | None]:
    """Return (page_count, verify_ok). verify_ok is None when no phrase given."""
    with fitz.open(stream=data, filetype="pdf") as doc:
        page_count = len(doc)
        if verify_phrase is None:
            return page_count, None
        text = "".join(doc[i].get_text() for i in range(min(3, page_count))).lower()
    return page_count, verify_phrase.lower() in text


def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    downloaded = cached = failed = unavailable = 0
    failures: list[str] = []

    for paper in catalog["papers"]:
        key = paper["key"]
        candidates = paper.get("pdf_candidates") or []
        if not candidates:
            unavailable += 1
            continue

        dest = PDF_DIR / f"{key}.pdf"
        if dest.exists() and dest.stat().st_size >= MIN_PDF_BYTES:
            if paper.get("status") == "pending":
                paper["status"] = "downloaded"
            paper.setdefault("pdf_path", str(dest.relative_to(ROOT)))
            cached += 1
            continue

        success = False
        for url in candidates:
            try:
                data = fetch(url)
            except Exception as exc:
                print(f"[{key}] FETCH FAIL {url} -> {exc}", file=sys.stderr)
                continue

            if not data.startswith(b"%PDF") or len(data) < MIN_PDF_BYTES:
                print(
                    f"[{key}] NOT A PDF ({len(data)} bytes) {url}",
                    file=sys.stderr,
                )
                continue

            try:
                page_count, verify_ok = pdf_info(data, paper.get("verify"))
            except Exception as exc:
                print(f"[{key}] UNREADABLE PDF {url} -> {exc}", file=sys.stderr)
                continue

            dest.write_bytes(data)
            paper["status"] = "downloaded"
            paper["pdf_path"] = str(dest.relative_to(ROOT))
            paper["pdf_source"] = url
            paper["pdf_bytes"] = len(data)
            paper["pdf_sha256"] = hashlib.sha256(data).hexdigest()
            paper["pdf_retrieved_at"] = date.today().isoformat()
            paper["page_count"] = page_count
            if verify_ok is not None:
                paper["verify_ok"] = verify_ok
            flag = "" if verify_ok in (True, None) else "  [VERIFY MISS]"
            print(f"[{key}] ok  {page_count}p  {len(data) // 1024} KB  <- {url}{flag}")
            success = True
            break

        if success:
            downloaded += 1
        else:
            paper["status"] = "download_failed"
            failed += 1
            failures.append(key)

        time.sleep(1.0)

    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(
        f"\nDownloaded {downloaded}, already present {cached}, "
        f"failed {failed}, unavailable (no source) {unavailable}"
    )
    if failures:
        print("Failed keys: " + ", ".join(failures))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
