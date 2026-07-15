# funny-papers

A research library on **humor and large language models**: a curated field guide covering 116 works (humor theory from 1900 through LLM-era papers up to July 2026), plus the full text of nearly every paper, the datasets they released, structured per-paper extracts, and cross-paper analysis built on top.

The goal: everything needed to deeply understand the field — and eventually build and evaluate humor systems — in one place, reproducibly.

## Start here

| If you want to… | Go to |
| --- | --- |
| Read the field, curated and in order | [humor-and-llms-field-guide.md](humor-and-llms-field-guide.md) |
| Read on an e-reader | Download the [Field Guide EPUB](dist/humor-and-llms-field-guide.epub) or [Complete Edition EPUB](dist/humor-and-llms-complete.epub) |
| Browse the paper library (source / full text where distributable / summary links) | [papers/MANIFEST.md](papers/MANIFEST.md) |
| Compare papers — who evaluated on what, which theories, which models | [papers/ANALYSIS.md](papers/ANALYSIS.md) |
| Audit evidence strength, human grounding, budgets, and synthesis confidence | [papers/EVIDENCE.md](papers/EVIDENCE.md) |
| Inspect guide and extract certification results | [papers/DISCREPANCIES.md](papers/DISCREPANCIES.md) |
| Read a one-page summary of a specific paper | `papers/summaries/<key>.md` |
| See what datasets exist and what's vendored locally | [data/MANIFEST.md](data/MANIFEST.md) |
| Query the library programmatically | [docs/query-cookbook.md](docs/query-cookbook.md) |
| See what might get built next | [docs/ideas.md](docs/ideas.md) |

## What's inside

- **The field guide** — [humor-and-llms-field-guide.md](humor-and-llms-field-guide.md), a curated bibliography of 116 entries organized into theory foundations plus nine parts (explanation, generation, multimodal, evaluation, situated/live humor, safety, cross-cultural, datasets, surveys). Each entry notes method, dataset, and key findings. Across two primary-text passes, all 111 converted entries and 796 checkable claims have been audited; methods, fixes, and the stratified extract check are documented in [papers/DISCREPANCIES.md](papers/DISCREPANCIES.md).
- **Paper library** (`papers/`) — 111 of 116 entries have distributable PDFs and vision-transcribed Markdown full text. Four additional theory entries (T1, T2, T4, and the Suls half of T5) are cataloged as restricted primary sources: publisher links and derived analysis may be public, but their PDFs and full-text derivatives are not. Public extracts and summaries are available for all four consulted restricted sources. T3 remains unavailable; Oring's half of T5 remains pending.
  - `papers/papers.json` — machine-readable catalog and **source of truth** (publication/source version, check and retrieval dates, PDF provenance, sha256, page counts)
  - `papers/pdfs/<key>.pdf` · `papers/md/<key>/<key>.md` — the documents themselves
  - `papers/extracts/<key>.json` — structured extract per paper (tasks, datasets, models, theories, headline numbers, and evidence profile)
  - `papers/summaries/<key>.md` — one-page summaries
  - `papers/ANALYSIS.md` — cross-paper matrices generated from the extracts
  - `papers/EVIDENCE.md` — human samples, judge dependence, selection/budget/provenance, contamination risk, and synthesis claim confidence
- **Dataset library** (`data/`) — 53 datasets cataloged in `data/datasets.json`; 39 public artifacts vendored locally (~9.4 GB, gitignored — rebuilds from the catalog with one script). Includes HumorBench (with autograder), the New Yorker caption-ranking corpus (250M+ votes), Oogiri-GO, ExPUNations, PunEval, HumorDB, both YesBut lineages, MultiPun, TIC-TALK, MWAHAHA, SMILE-Next, and more.
- **Pipeline scripts** (`scripts/`) — everything above is built by small, resumable, idempotent Python scripts (see below).

## Repo layout

```
humor-and-llms-field-guide.md   # the curated guide — the root document
AGENTS.md                       # canonical operational guide for coding agents
CLAUDE.md                       # Claude Code import shim for AGENTS.md
docs/
  ebook-release-notes.md        # contents, caveats, and checksums for the EPUBs
  ideas.md                      # candidate next steps (a menu, not a plan)
  query-cookbook.md             # jq/python recipes over the catalogs & extracts
assets/
  ebook.css                     # reflowable, e-ink-friendly EPUB styling
papers/
  papers.json                   # paper catalog (source of truth)
  MANIFEST.md                   # human-readable index (generated)
  ANALYSIS.md                   # cross-paper comparison views (generated)
  EVIDENCE.md                   # evidence profiles + synthesis claims (generated)
  synthesis_claims.json         # curated support/counterevidence map
  DISCREPANCIES.md              # guide-vs-paper verification report
  pdfs/ md/ extracts/ summaries/ runs/ review/
  private/                      # local restricted sources/derivatives (gitignored)
data/
  datasets.json                 # dataset catalog (source of truth)
  MANIFEST.md                   # human-readable index (generated)
  <key>/                        # vendored datasets (gitignored, ~9.4 GB)
scripts/                        # the pipelines (all resumable/idempotent)
dist/                           # versioned, generated EPUB reader editions
```

## Rebuilding from a fresh clone

Distributable PDFs and Markdown, plus public extracts and summaries, are versioned. Restricted sources and all of their full-text derivatives are deliberately absent from a clone. Dataset payloads (~9.4 GB) are also gitignored and can be rebuilt:

```bash
python3 -m venv .venv && .venv/bin/pip install huggingface_hub
.venv/bin/python scripts/download_datasets.py     # vendors the available public artifacts
python3 scripts/build_data_manifest.py            # refresh data/MANIFEST.md
```

Datasets are fetched exactly as published (shallow git clone, HuggingFace snapshot, or direct download) with a 2 GB per-dataset size cap; a few are gated or request-only — `data/MANIFEST.md` documents each one's status.

## The pipelines

Three stages, each resumable and safe to re-run:

1. **Download** — `scripts/download_papers.py` walks `papers.json`, tries each distributable entry's `pdf_candidates` in order, verifies the result looks like the right paper, and records provenance. Restricted entries are always skipped.
2. **Convert** — `scripts/convert_papers.py` transcribes each PDF to Markdown page-by-page using a vision LLM (via the sibling [`pdf-to-md`](https://github.com/brendansudol/pdf-to-md) tool; requires an `OPENAI_API_KEY`). Resumes mid-paper. Restricted conversion requires both `--only KEY` and `--include-restricted`; every output stays under gitignored `papers/private/<key>/`.
3. **Extract & analyze** — `scripts/extract_papers.py` uses gpt-5.5 (high reasoning effort, strict JSON-schema output) to produce the structured extract, evidence profile, and one-pager. Sources up to 250,000 characters use one pass. Longer books use explicit, complete page units, resumable private chapter extracts, and a final synthesis pass; oversized input without a complete unit plan fails instead of being truncated. `--dry-run` validates the plan without loading credentials or making model calls. Restricted extraction also requires scoped `--only KEY --include-restricted`. `scripts/enrich_evidence.py` backfills profiles for single-pass sources without rewriting summaries; `scripts/build_analysis.py` and `scripts/build_evidence.py` regenerate cross-paper views.

`scripts/build_manifest.py` and `scripts/build_data_manifest.py` regenerate the human-readable indexes from the catalogs at any time.

## Building the e-reader editions

The ebook builder creates reflowable EPUB 3 files from the public, versioned
library. It never includes PDFs, full-text Markdown, extracts, private sources,
or pipeline logs. Summary order and source links come from `papers/papers.json`;
restricted entries retain their public access notices and official publisher
links.

Install [Pandoc](https://pandoc.org/installing.html) and, for standards
validation, [EPUBCheck](https://www.w3.org/publishing/epubcheck/). On macOS with
Homebrew:

```bash
brew install pandoc epubcheck
```

Then build either reader edition—or both by omitting `--edition`:

```bash
python3 scripts/build_ebook.py --edition guide
python3 scripts/build_ebook.py --edition complete
python3 scripts/build_ebook.py --require-epubcheck
```

Outputs are written to the versioned [Field Guide
EPUB](dist/humor-and-llms-field-guide.epub) and [Complete Edition
EPUB](dist/humor-and-llms-complete.epub), so readers can download them without
installing the build tools. The guide edition is designed for a continuous
first read. The complete edition adds all 115 available paper summaries,
grouped by field-guide section with a nested table of contents. See the [ebook
release notes](docs/ebook-release-notes.md) for coverage, caveats, and
checksums. Send either EPUB to a Kindle with [Amazon's Send to
Kindle](https://www.amazon.com/sendtokindle). The local build is deterministic
for unchanged sources and makes no network or paid model calls.

## Trust & caveats

- **Markdown full texts are LLM vision transcriptions** of the PDFs — high quality but not authoritative; figures appear as `[Figure: …]` placeholders. Cite the PDF/original.
- **Extracts and summaries are LLM-generated** from those transcriptions. All 111 converted guide entries have now received a separate primary-text claim audit across two passes (796 claims checked, 14 discrepancies found and fixed). A stratified 26-extract sample (23.4%) received substantive field-level checks and passed; the other 85 extracts received source-presence, current-hash, and non-truncation checks only. This was an independent pipeline pass by another AI model, not a human replication or sentence-by-sentence certification. See [papers/DISCREPANCIES.md](papers/DISCREPANCIES.md) and [papers/review/certification.json](papers/review/certification.json).
- **Restricted additions are not yet evidence-certified.** T1, T2, T4, and Suls's half of T5 now have derived extracts and initial direct-source quality checks, but not the separate independent audit required for certification. The existing certification totals therefore continue to cover the 111 distributed/converted entries only. T5 currently covers Suls (1972), not Oring's appropriate-incongruity account.
- **Copyright stays with the original authors/publishers.** Versioned PDFs are open-access or author-hosted copies. Restricted primary texts are consulted locally and not distributed; their public summaries link to official publisher pages. Datasets keep their original licenses (recorded per-entry in `data/datasets.json`).
