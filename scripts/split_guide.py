#!/usr/bin/env python3
"""Split humor-and-llms-field-guide.md into per-paper claim files for the
guide-vs-paper discrepancy check.

Writes papers/review/guide-entries/<key>.md for every converted paper in
papers/papers.json. Numbered entries (#N, T-N) are extracted by header;
'also in this section' items by anchor phrase (paragraph containing it).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "humor-and-llms-field-guide.md"
PAPERS = ROOT / "papers" / "papers.json"
OUT_DIR = ROOT / "papers" / "review" / "guide-entries"

# Keys whose guide text is not a numbered "### N." block: anchor phrase whose
# containing paragraph (to the next blank line) is the entry.
ANCHORS = {
    "x15-minsky-jokes": "Marvin Minsky, \"Jokes and the Logic",
    "x01-jape": "**Pre-LLM foundations (historical grounding).**",
    "x02-comic": "**Also in this cluster (2026):**",
    "x03-openmic": "**Also in this cluster (2026):**",
    "x04-pixelhumor": "**Also in this section:**",
    "x05-memereacon": "**Also in this section:**",
    "x06-exfuntube": "**Video humor:**",
    "x07-vhub": "**Video humor:**",
    "x09-hahackathon": "**HaHackathon",
    "x10-humicroedit": "**Humicroedit & FunLines",
    "x11-rjokes-last-laugh": "**rJokes**",
    "x12-ur-funny": "**UR-FUNNY**",
    "x13-redefining-humor-data": "**Also:** [Re-defining Humor Data Objects",
}
# Keys covered by another entry's numbered block.
ALIASES = {
    "x08-can-ai-make-us-laugh": "#17",
    "50b-chumor-2": "#50",
}


def numbered_blocks(text: str) -> dict[str, str]:
    """Map '#1'/'T1' style refs to their '### ' block text."""
    blocks: dict[str, str] = {}
    pattern = re.compile(r"^### (T?\d+)\. ", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        # Trim trailing sub-headers (e.g. '### Pun / wordplay generation')
        block = re.split(r"\n### [^\d]", block)[0].strip()
        ref = match.group(1)
        blocks["#" + ref if not ref.startswith("T") else ref] = block
    return blocks


def paragraph_containing(text: str, anchor: str) -> str | None:
    index = text.find(anchor)
    if index == -1:
        return None
    start = text.rfind("\n\n", 0, index) + 2
    end = text.find("\n\n", index)
    return text[start:end if end != -1 else len(text)].strip()


def main() -> int:
    text = GUIDE.read_text(encoding="utf-8")
    papers = json.loads(PAPERS.read_text(encoding="utf-8"))["papers"]
    blocks = numbered_blocks(text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    written, missed = 0, []
    for paper in papers:
        if paper.get("status") != "converted":
            continue
        key, ref = paper["key"], paper["ref"]
        entry = None
        if key in ANCHORS:
            entry = paragraph_containing(text, ANCHORS[key])
        elif key in ALIASES:
            entry = blocks.get(ALIASES[key])
            if entry:
                entry = (
                    f"(This paper is described inside the guide's {ALIASES[key]} "
                    f"entry — check only the claims about THIS paper.)\n\n" + entry
                )
        else:
            entry = blocks.get(ref.split(" ")[0])
        if entry is None:
            missed.append(key)
            continue
        (OUT_DIR / f"{key}.md").write_text(
            f"<!-- guide claims for {key} ({ref}) -->\n\n{entry}\n", encoding="utf-8"
        )
        written += 1

    print(f"wrote {written} entry files; missed: {missed or 'none'}")
    return 1 if missed else 0


if __name__ == "__main__":
    raise SystemExit(main())
