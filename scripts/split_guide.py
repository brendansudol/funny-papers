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
    "x02-comic": "**Performance-oriented multi-agent systems:**",
    "x03-openmic": "**Performance-oriented multi-agent systems:**",
    "x04-pixelhumor": "**Related comics datasets:**",
    "x05-memereacon": "**Related comics datasets:**",
    "x06-exfuntube": "**Video humor:**",
    "x07-vhub": "**Video humor:**",
    "x09-hahackathon": "**HaHackathon",
    "x10-humicroedit": "**Humicroedit & FunLines",
    "x11-rjokes-last-laugh": "**rJokes**",
    "x12-ur-funny": "**UR-FUNNY**",
    "x13-redefining-humor-data": "**Humor data as social interaction:**",
    "x16-pun-generation-surprise": "**Pun Generation with Surprise**",
    "x17-context-satirical-news": "**Context-Driven Satirical News Generation**",
    "x18-yodalib": "**YodaLib**",
    "x19-unpie": "**Visual-pun disambiguation:**",
    "x20-does-bigger-funnier": "**Judge-validity stress test:**",
    "x21-joke-space-originality": "**Originality beyond funniness:**",
    "x22-humor-word-embeddings": "**Earlier audience-modeling anchors:**",
    "x23-eigentaste-jester": "[**Eigentaste / Jester**]",
    "x24-open-mic-humor-quotient": "**Audience laughter as a signal:**",
    "x25-tic-talk": "**Timing as multimodal data:**",
    "x26-not-human-funnier": "**Performer identity as material:**",
    "x27-genai-humor-bias": "**Bias introduced by",
    "x28-counterfactual-unfairness": "**Relational fairness under identity swaps:**",
    "x29-d-humor": "**Dark-humor resource:**",
    "x30-hins": "**Long context in Hindi:**",
    "x31-clef-joker-2024": "**Shared-task ecosystem:**",
    "x32-hsq-fingerprinting": "**Construct-validity caution:**",
    "x33-yesbut-juxtaposition": "**YesBut-Juxtaposition (Hu et al.):**",
    "x34-yesbut-v2": "**YesBut V2 (Hu et al.):**",
    "x35-turing-jest": "**Turing Jest:**",
    "x36-ironic-melting-pot": "**Human-evaluation reporting audit:**",
    "x37-improv-comedy-setting": "**Live AI–human improv comparison:**",
    "x38-multipun": "**Adversarial multimodal-pun tests:**",
    "x39-how-humorous-ai": "**Humor in social interaction:**",
    "x40-corpus-pragmatics": "**Pragmatic-function annotation:**",
    "x41-mulai": "**Dyadic laughter and participant perception:**",
    "x42-cheese": "**Smiling, uptake, and failed humor:**",
    "x43-smile-next": "**Real-world laughter tasks for LLMs:**",
    "x44-mame-re": "**Memes as conversational actions:**",
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
        # Stop at a new section/subsection or a separately cataloged compact
        # entry that happens to sit between numbered entries.
        block = re.split(r"\n## ", block, maxsplit=1)[0]
        block = re.split(r"\n### (?!T?\d+\. )", block, maxsplit=1)[0]
        compact_starts = []
        for anchor in set(ANCHORS.values()):
            anchor_pos = block.find(anchor)
            if anchor_pos <= 0:
                continue
            paragraph_start = block.rfind("\n\n", 0, anchor_pos)
            compact_starts.append(paragraph_start if paragraph_start >= 0 else anchor_pos)
        if compact_starts:
            block = block[: min(compact_starts)]
        block = block.strip()
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
