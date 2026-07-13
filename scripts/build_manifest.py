#!/usr/bin/env python3
"""Generate papers/MANIFEST.md from papers/papers.json.

Idempotent; run any time to refresh the human-readable index.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "papers" / "papers.json"
MANIFEST_PATH = ROOT / "papers" / "MANIFEST.md"

STATUS_LABELS = {
    "converted": "converted",
    "downloaded": "PDF only (conversion pending)",
    "convert_failed": "PDF only (conversion FAILED)",
    "download_failed": "needs manual download",
    "pending": "not yet downloaded",
    "unavailable": "no open PDF",
}


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    papers = catalog["papers"]

    counts: dict[str, int] = {}
    for paper in papers:
        counts[paper.get("status", "?")] = counts.get(paper.get("status", "?"), 0) + 1

    # Preserve catalog order within sections; sections in first-seen order.
    sections: dict[str, list[dict]] = {}
    for paper in papers:
        sections.setdefault(paper["section"], []).append(paper)

    lines: list[str] = []
    lines.append("# Paper Library Manifest")
    lines.append("")
    lines.append(
        f"Companion library for [humor-and-llms-field-guide.md](../humor-and-llms-field-guide.md). "
        f"Regenerated {date.today().isoformat()} by `scripts/build_manifest.py` "
        f"from [papers.json](papers.json) (the machine-readable source of truth)."
    )
    lines.append("")
    total = len(papers)
    lines.append(
        f"**{total} entries**: "
        + ", ".join(f"{n} {STATUS_LABELS.get(s, s)}" for s, n in sorted(counts.items()))
        + "."
    )
    lines.append("")
    lines.append("Layout:")
    lines.append("")
    lines.append("- `papers/pdfs/<key>.pdf` — downloaded paper PDFs")
    lines.append(
        "- `papers/md/<key>/<key>.md` — combined Markdown transcription "
        "(per-page files in `papers/md/<key>/pages/`, per-page API usage in "
        "`papers/md/<key>/manifest.jsonl`)"
    )
    lines.append("- `papers/runs/<key>.progress.jsonl` — conversion progress logs")
    lines.append(
        "- `papers/extracts/<key>.json` — structured extract (tasks, datasets, "
        "models, theories, headline numbers); `papers/summaries/<key>.md` — "
        "one-page summary; cross-paper views in [ANALYSIS.md](ANALYSIS.md)"
    )
    lines.append("")
    lines.append(
        "Pipeline: `scripts/download_papers.py` -> `scripts/convert_papers.py` "
        "(uses `../pdf-to-md`) -> `scripts/build_manifest.py`. All steps are "
        "resumable; to add a missing paper, drop the PDF into `papers/pdfs/` "
        "with the right key and rerun the last two steps."
    )
    lines.append("")

    for section, entries in sections.items():
        lines.append(f"## {section}")
        lines.append("")
        lines.append("| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for paper in entries:
            key = paper["key"]
            title = md_escape(paper["title"])
            if paper.get("page_url"):
                title_cell = f"[{title}]({paper['page_url']})"
            else:
                title_cell = title

            if paper.get("pdf_path"):
                pages = paper.get("page_count")
                label = f"pdf ({pages}p)" if pages else "pdf"
                pdf_cell = f"[{label}](pdfs/{key}.pdf)"
            else:
                pdf_cell = "—"

            if paper.get("status") == "converted" and paper.get("md_path"):
                md_cell = f"[md](md/{key}/{key}.md)"
            else:
                md_cell = "—"

            if (ROOT / "papers" / "summaries" / f"{key}.md").exists():
                summary_cell = f"[1-pager](summaries/{key}.md)"
            else:
                summary_cell = "—"

            note_bits = []
            status = paper.get("status")
            if status != "converted":
                note_bits.append(STATUS_LABELS.get(status, status))
            if paper.get("note"):
                note_bits.append(paper["note"])
            if paper.get("source_version"):
                source_pin = f"Source pin: {paper['source_version']}"
                if paper.get("source_checked"):
                    source_pin += f"; checked {paper['source_checked']}"
                if paper.get("pdf_retrieved_at"):
                    source_pin += f"; PDF retrieved {paper['pdf_retrieved_at']}"
                note_bits.append(source_pin + ".")
            notes_cell = md_escape(" ".join(note_bits)) if note_bits else ""

            lines.append(
                f"| {md_escape(paper['ref'])} | {title_cell} | {paper.get('year', '')} "
                f"| {md_escape(str(paper.get('venue', '')))} | {pdf_cell} | {md_cell} | {summary_cell} | {notes_cell} |"
            )
        lines.append("")

    missing = [
        p
        for p in papers
        if p.get("status") in ("unavailable", "download_failed", "pending")
    ]
    if missing:
        lines.append("## Not in the library (and why)")
        lines.append("")
        for paper in missing:
            reason = paper.get("note") or STATUS_LABELS.get(paper.get("status"), "")
            lines.append(f"- **{paper['ref']} — {md_escape(paper['title'])}**: {reason}")
        lines.append("")

    MANIFEST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
