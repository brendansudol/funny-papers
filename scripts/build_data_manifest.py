#!/usr/bin/env python3
"""Generate data/MANIFEST.md from data/datasets.json (+ papers/papers.json for cross-refs).

Idempotent; run any time to refresh.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASETS_PATH = ROOT / "data" / "datasets.json"
PAPERS_PATH = ROOT / "papers" / "papers.json"
MANIFEST_PATH = ROOT / "data" / "MANIFEST.md"

STATUS_LABELS = {
    "downloaded": "",
    "pending": "not yet downloaded",
    "too_large": "over size cap, not vendored",
    "gated": "gated (login/agreement required)",
    "request": "by request from authors",
    "failed": "download FAILED",
    "unavailable": "no public release",
}


def md_escape(text: str) -> str:
    return str(text).replace("|", "\\|")


def main() -> int:
    catalog = json.loads(DATASETS_PATH.read_text(encoding="utf-8"))
    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    papers_by_key = {p["key"]: p for p in papers}

    datasets = catalog["datasets"]
    counts: dict[str, int] = {}
    total_mb = 0.0
    for entry in datasets:
        counts[entry.get("status", "?")] = counts.get(entry.get("status", "?"), 0) + 1
        total_mb += entry.get("disk_mb") or 0

    lines: list[str] = []
    lines.append("# Dataset Library Manifest")
    lines.append("")
    lines.append(
        f"Public datasets released by papers in "
        f"[humor-and-llms-field-guide.md](../humor-and-llms-field-guide.md). "
        f"Regenerated {date.today().isoformat()} by `scripts/build_data_manifest.py` "
        f"from [datasets.json](datasets.json) (machine-readable source of truth). "
        f"Sibling library: [papers/MANIFEST.md](../papers/MANIFEST.md)."
    )
    lines.append("")
    summary = ", ".join(
        f"{n} {STATUS_LABELS.get(s) or s}" for s, n in sorted(counts.items())
    )
    lines.append(
        f"**{len(datasets)} datasets**: {summary}. ~{total_mb / 1024:.1f} GB on disk."
    )
    lines.append("")
    lines.append(
        "Layout: each dataset lives in `data/<key>/`, exactly as published "
        "(shallow git clone, HuggingFace snapshot, or direct download — see "
        "`fetch method`). Re-run `scripts/download_datasets.py` after editing "
        "datasets.json; it skips anything already present."
    )
    lines.append("")
    lines.append("| Dataset | From paper(s) | Contents | Fetch | License | Size | Local | Notes |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")

    for entry in datasets:
        key = entry["key"]
        name_cell = f"[{md_escape(entry['name'])}]({entry['source_url']})" if entry.get("source_url") else md_escape(entry["name"])

        refs = []
        for paper_key in entry.get("paper_keys", []):
            paper = papers_by_key.get(paper_key)
            if paper:
                refs.append(
                    f"[{md_escape(paper['ref'])}](../papers/md/{paper_key}/{paper_key}.md)"
                    if paper.get("status") == "converted"
                    else md_escape(paper["ref"])
                )
        papers_cell = ", ".join(refs) if refs else "—"

        local_cell = f"`{entry['local_path']}/`" if entry.get("local_path") else "—"
        size_mb = entry.get("disk_mb")
        if size_mb is None:
            size_cell = entry.get("approx_size") or "?"
        elif size_mb >= 1024:
            size_cell = f"{size_mb / 1024:.1f} GB"
        else:
            size_cell = f"{size_mb:.0f} MB"

        note_bits = []
        status_label = STATUS_LABELS.get(entry.get("status"), entry.get("status"))
        if status_label:
            note_bits.append(f"**{status_label}**")
        for field in ("note", "note_auto"):
            if entry.get(field):
                note_bits.append(entry[field])
        lines.append(
            "| "
            + " | ".join(
                [
                    name_cell,
                    papers_cell,
                    md_escape(entry.get("contents", "")),
                    entry.get("method", "?"),
                    md_escape(entry.get("license") or "?"),
                    size_cell,
                    local_cell,
                    md_escape(" ".join(note_bits)),
                ]
            )
            + " |"
        )

    lines.append("")
    MANIFEST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
