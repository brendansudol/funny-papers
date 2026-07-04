#!/usr/bin/env python3
"""Generate papers/ANALYSIS.md — cross-paper comparison views built from
papers/extracts/*.json.

Views:
  1. Datasets x papers (who introduced / evaluated on what)
  2. Models x papers (which models were actually run where)
  3. Humor theories x papers (operationalized vs motivation)
  4. Tasks x papers
  5. Headline results table (per dataset where possible)

Idempotent; rerun after extract_papers.py.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACTS_DIR = ROOT / "papers" / "extracts"
PAPERS_PATH = ROOT / "papers" / "papers.json"
ANALYSIS_PATH = ROOT / "papers" / "ANALYSIS.md"

MIN_GROUP = 2  # only show dataset/model/task rows shared by >= this many papers


def md_escape(text: str) -> str:
    return str(text).replace("|", "\\|")


def paper_link(extract: dict) -> str:
    key = extract["key"]
    return f"[{md_escape(extract['ref'])}](summaries/{key}.md)"


def normalize_model(name: str) -> str:
    """Light canonicalization so e.g. 'GPT-4o (2024-08-06)' and 'gpt-4o' group together."""
    base = name.strip()
    base = re.sub(r"\s*\((?:20\d\d[-.\d]*|v[\d.]+|[\d-]+)\)$", "", base)
    return base


def main() -> int:
    extracts = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(EXTRACTS_DIR.glob("*.json"))
    ]
    if not extracts:
        print("No extracts found; run extract_papers.py first.")
        return 1

    lines: list[str] = []
    lines.append("# Cross-Paper Analysis")
    lines.append("")
    lines.append(
        f"Comparison views over {len(extracts)} paper extracts. Regenerated "
        f"{date.today().isoformat()} by `scripts/build_analysis.py` from "
        f"[extracts/](extracts/) (full-text-grounded, one JSON per paper). "
        f"One-page summaries: [summaries/](summaries/). "
        f"Rows shared by fewer than {MIN_GROUP} papers are omitted from the "
        f"matrix views (see per-paper extracts for the long tail)."
    )
    lines.append("")

    # ---- 1. Datasets x papers ----
    dataset_rows: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for e in extracts:
        for ds in e.get("datasets_used", []):
            dataset_rows[ds["name"]][ds["role"]].append(e)
    lines.append("## Datasets × papers")
    lines.append("")
    lines.append("| Dataset | Introduced by | Evaluated on by | Trained on by | Source/analyzed by |")
    lines.append("| --- | --- | --- | --- | --- |")
    for name, roles in sorted(
        dataset_rows.items(),
        key=lambda kv: -sum(len(v) for v in kv[1].values()),
    ):
        total = sum(len(v) for v in roles.values())
        if total < MIN_GROUP:
            continue
        def cell(*keys):
            papers = [p for k in keys for p in roles.get(k, [])]
            return ", ".join(paper_link(p) for p in papers) or "—"
        lines.append(
            f"| {md_escape(name)} | {cell('introduced')} | {cell('evaluated-on')} "
            f"| {cell('trained-on')} | {cell('source-material', 'analyzed')} |"
        )
    lines.append("")

    # ---- 2. Models x papers ----
    model_rows: dict[str, list] = defaultdict(list)
    for e in extracts:
        for m in set(normalize_model(m) for m in e.get("models_evaluated", [])):
            model_rows[m].append(e)
    lines.append("## Models × papers (models actually run)")
    lines.append("")
    lines.append("| Model | Papers evaluating it |")
    lines.append("| --- | --- |")
    for model, papers in sorted(model_rows.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        if len(papers) < MIN_GROUP:
            continue
        lines.append(f"| {md_escape(model)} | {', '.join(paper_link(p) for p in papers)} |")
    lines.append("")

    # ---- 3. Humor theories x papers ----
    theory_rows: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for e in extracts:
        for t in e.get("humor_theories", []):
            if t["theory"] == "none":
                continue
            theory_rows[t["theory"]][t["usage"]].append(e)
    lines.append("## Humor theories × papers")
    lines.append("")
    lines.append("| Theory | Operationalized by | Grounding/motivation for | Cited in passing by |")
    lines.append("| --- | --- | --- | --- |")
    for theory, usages in sorted(
        theory_rows.items(), key=lambda kv: -sum(len(v) for v in kv[1].values())
    ):
        def tcell(key):
            return ", ".join(paper_link(p) for p in usages.get(key, [])) or "—"
        lines.append(
            f"| {md_escape(theory)} | {tcell('operationalized')} "
            f"| {tcell('grounding/motivation')} | {tcell('cited-in-passing')} |"
        )
    lines.append("")

    # ---- 4. Tasks x papers ----
    task_rows: dict[str, list] = defaultdict(list)
    for e in extracts:
        for t in set(t.strip().lower() for t in e.get("tasks", [])):
            task_rows[t].append(e)
    lines.append("## Tasks × papers")
    lines.append("")
    lines.append("| Task | Papers |")
    lines.append("| --- | --- |")
    for task, papers in sorted(task_rows.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(papers) < MIN_GROUP:
            continue
        lines.append(f"| {md_escape(task)} | {', '.join(paper_link(p) for p in papers)} |")
    lines.append("")

    # ---- 5. Headline results ----
    lines.append("## Headline results")
    lines.append("")
    lines.append(
        "Every extracted headline number, grouped by paper (see each extract "
        "for full context)."
    )
    lines.append("")
    lines.append("| Paper | Finding | Metric | Value | Dataset | Best system |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for e in extracts:
        for r in e.get("headline_results", []):
            lines.append(
                f"| {paper_link(e)} | {md_escape(r['finding'])} "
                f"| {md_escape(r.get('metric') or '—')} | {md_escape(r.get('value') or '—')} "
                f"| {md_escape(r.get('dataset') or '—')} | {md_escape(r.get('best_system') or '—')} |"
            )
    lines.append("")

    ANALYSIS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {ANALYSIS_PATH} ({len(extracts)} extracts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
