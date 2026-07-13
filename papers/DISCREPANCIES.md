# Guide-vs-Paper Discrepancy Check

> **Status: all 8 fixes below were applied to the guide on 2026-07-03** (guide text edited; papers.json metadata synced for #19 and #25). The "guide says" quotes preserve the pre-fix wording.

Fact-check of every entry in [humor-and-llms-field-guide.md](../humor-and-llms-field-guide.md) against the full-text transcriptions in `papers/md/`. Run 2026-07-03 by 16 Claude Opus 4.8 agents (5 papers each); every reported discrepancy is backed by a verbatim quote from the transcription. Machine-readable results: [review/discrepancies.json](review/discrepancies.json).

**Scope at the time of the audit (2026-07-03):** the original 80 transcribed papers and ~540 factual claims (authors, venues, dataset sizes, quantitative results, findings characterizations). Editorial opinions, reading advice, and cross-paper lineage claims were excluded. The six entries then lacking a paper included theory books T1–T5 and the not-yet-published MWAHAHA overview; MWAHAHA and 18 additional works were added to the library on 2026-07-11 and are outside this historical audit.

## Verdict

**74 of 80 entries fully confirmed. 8 discrepancies in 6 entries: 2 major, 6 minor.** Every headline number spot-checked in the guide — 62%/94% and 84.5% (#1), 75.6% and Δ=0.440/0.422 (#20), p≈0.053 (#14), Kendall τ≈0.89 (#35), ~50% (#37), 2–3% (#50), 62.94%/50.12% (#55), +1.88–4.05% (#40), ~+11.6% (#65) — matches the papers.

## Major discrepancies

### 1. #51 CFunModel — task list partly misattributed
- **Guide says:** "multi-task across crosstalk generation, recognition, type/level classification, and punchline detection"
- **Paper says:** CFunModel's tasks are Crosstalk Response Selection, Humor Recognition, Joke Generation/Continuation, Humor Explanation, and Crosstalk Generation. "Humor type classification, humor level classification, and punchline detection" appear only in Related Work as tasks proposed by Chen et al. (2024a) — a different paper.
- **Evidence:** [page_0002.md](md/51-cfunmodel/pages/page_0002.md), [page_0003.md](md/51-cfunmodel/pages/page_0003.md) (Table 1)
- **Suggested fix:** "multi-task across crosstalk response selection, humor recognition, joke generation/continuation, humor explanation, and crosstalk generation"

### 2. #19 Jokeasy — publication status understated
- **Guide says:** "Ge et al. — **2026** · `preprint`"
- **Paper says:** "Accepted at IASDR 2025. This is the author-accepted version." The guide's `preprint` tag and 2026 date reflect the arXiv posting, but the paper self-identifies as peer-reviewed (IASDR 2025).
- **Evidence:** [page_0001.md](md/19-jokeasy/pages/page_0001.md)
- **Suggested fix:** "Ge et al. — **IASDR 2025** (arXiv 2026) · `peer-reviewed` `HCI study`" — note this one *upgrades* the paper's status.

## Minor discrepancies

| Entry | Guide says | Paper says | Evidence |
| --- | --- | --- | --- |
| #1 Hessel et al. | "Thousands of cartoons with finalist captions" | 704 cartoons; the *captions* number in the thousands (2.7K high-quality) | [page_0004](md/01-androids-electric-sheep/pages/page_0004.md), [page_0016](md/01-androids-electric-sheep/pages/page_0016.md) |
| #51 CFunSet | "20k+ jokes incl. Tieba JokeBar" | CFunSet is 160k+ entries; 20k+ is only the Tieba-JokeBar subset | [page_0001](md/51-cfunmodel/pages/page_0001.md) |
| #25 HumorDB | Title "Is AI Fun? HumorDB: A Curated Dataset…" | Transcribed (ICCV camera-ready) title is "HumorDB: Can AI understand graphical humor?" — arXiv-vs-camera-ready retitle | [page_0001](md/25-humordb/pages/page_0001.md) |
| v-HUB (Part 3) | Authors "Shi, Li, Zhao et al." | No author named "Li" among the nine authors; first three are Shi, Zhao, Zhou | [x07-vhub](md/x07-vhub/x07-vhub.md) |
| JAPE (Part 2) | "used WordNet plus pronunciation dictionaries" | The 1994 JAPE paper uses a hand-built homonym base from an American-English homophone list; WordNet/pronunciation dictionaries belong to successor STANDUP | [page_0004](md/x01-jape/pages/page_0004.md) |
| JAPE (Part 2) | "schoolchildren reportedly called JAPE's output 'pathetic'" | The "jokes, but pathetic ones" verdict came from the study's 14 adult judges; schoolchildren are mentioned only as future work | [page_0005](md/x01-jape/pages/page_0005.md) |

## Systematic notes (not discrepancies)

- **Venue tags are mostly unverifiable from the PDFs themselves**: many transcriptions are arXiv versions that don't self-state their accepted venue (e.g. #4 EMNLP 2025, #27 ACL Findings 2025, #28 CVPR 2026, #47 EACL 2026). None are contradicted; the guide's own compilation note already flags that preprint/venue statuses may shift. Exceptions confirmed in-paper: #8 ACL 2025, #12 ICLR 2025, #29 ICLR 2026, #38 AAAI 2026, #46 C&C 2025, #61 LaTeCH-CLfL 2020, #62 ACM CSUR 58(7):177.
- **#26 YesBut V2** (1,262 multilingual images) is a separate later release by a different team; the V1 paper neither confirms nor contradicts it (our dataset catalog vendors both).
- **#55 nuance**: baseline GPT (41.06%) actually *underperforms* NMT on humor retention; the guide's "GPT-based translation significantly beats NMT" is the paper's own abstract framing and the guide correctly centers GPT-Ex — not flagged.
- **#6 title**: the transcription's page-1 header reads "reward" (OCR artifact); the body confirms "reword" as in the guide.
