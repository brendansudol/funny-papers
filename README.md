# funny-papers

A research library on **humor and large language models**: a curated field guide covering ~86 works (humor theory from 1900 through LLM-era papers up to 2026), plus the full text of nearly every paper, the datasets they released, structured per-paper extracts, and cross-paper analysis built on top.

The goal: everything needed to deeply understand the field — and eventually build and evaluate humor systems — in one place, reproducibly.

## Start here

| If you want to… | Go to |
| --- | --- |
| Read the field, curated and in order | [humor-and-llms-field-guide.md](humor-and-llms-field-guide.md) |
| Browse the paper library (per-paper PDF / full text / summary links) | [papers/MANIFEST.md](papers/MANIFEST.md) |
| Compare papers — who evaluated on what, which theories, which models | [papers/ANALYSIS.md](papers/ANALYSIS.md) |
| Read a one-page summary of a specific paper | `papers/summaries/<key>.md` |
| See what datasets exist and what's vendored locally | [data/MANIFEST.md](data/MANIFEST.md) |
| Query the library programmatically | [docs/query-cookbook.md](docs/query-cookbook.md) |
| See what might get built next | [docs/ideas.md](docs/ideas.md) |

## What's inside

- **The field guide** — [humor-and-llms-field-guide.md](humor-and-llms-field-guide.md), a curated bibliography of ~86 entries organized into theory foundations plus nine parts (explanation, generation, multimodal, evaluation, situated/live humor, safety, cross-cultural, datasets, surveys). Each entry notes method, dataset, and key findings. Every factual claim in it was checked against the papers' full text (see [papers/DISCREPANCIES.md](papers/DISCREPANCIES.md)).
- **Paper library** (`papers/`) — 80 of 86 entries with downloaded PDFs and vision-transcribed Markdown full text. The 6 missing are books/paywalled theory works with no open PDF.
  - `papers/papers.json` — machine-readable catalog and **source of truth** (statuses, PDF provenance, sha256, page counts)
  - `papers/pdfs/<key>.pdf` · `papers/md/<key>/<key>.md` — the documents themselves
  - `papers/extracts/<key>.json` — structured extract per paper (tasks, datasets used with roles, models evaluated, theories operationalized, headline numbers)
  - `papers/summaries/<key>.md` — one-page summaries
  - `papers/ANALYSIS.md` — cross-paper matrices generated from the extracts
- **Dataset library** (`data/`) — 34 datasets cataloged in `data/datasets.json`; 26 public ones vendored locally (~8.8 GB, gitignored — rebuilds from the catalog with one script). Includes HumorBench (with autograder), the New Yorker caption-ranking corpus (250M+ votes), Oogiri-GO, ExPUNations, PunEval, HumorDB, YesBut, and more.
- **Pipeline scripts** (`scripts/`) — everything above is built by small, resumable, idempotent Python scripts (see below).

## Repo layout

```
humor-and-llms-field-guide.md   # the curated guide — the root document
CLAUDE.md                       # operational guide for coding agents
docs/
  ideas.md                      # candidate next steps (a menu, not a plan)
  query-cookbook.md             # jq/python recipes over the catalogs & extracts
papers/
  papers.json                   # paper catalog (source of truth)
  MANIFEST.md                   # human-readable index (generated)
  ANALYSIS.md                   # cross-paper comparison views (generated)
  DISCREPANCIES.md              # guide-vs-paper verification report
  pdfs/ md/ extracts/ summaries/ runs/ review/
data/
  datasets.json                 # dataset catalog (source of truth)
  MANIFEST.md                   # human-readable index (generated)
  <key>/                        # vendored datasets (gitignored, ~8.8 GB)
scripts/                        # the pipelines (all resumable/idempotent)
```

## Rebuilding from a fresh clone

PDFs, markdown, extracts, and summaries are all versioned — a clone gives you the complete paper library as-is. Only the datasets (~8.8 GB) are gitignored and need rebuilding:

```bash
python3 -m venv .venv && .venv/bin/pip install huggingface_hub
.venv/bin/python scripts/download_datasets.py     # vendors the 26 public datasets
python3 scripts/build_data_manifest.py            # refresh data/MANIFEST.md
```

Datasets are fetched exactly as published (shallow git clone, HuggingFace snapshot, or direct download) with a 2 GB per-dataset size cap; a few are gated or request-only — `data/MANIFEST.md` documents each one's status.

## The pipelines

Three stages, each resumable and safe to re-run:

1. **Download** — `scripts/download_papers.py` walks `papers.json`, tries each entry's `pdf_candidates` in order, verifies the result looks like the right paper, and records provenance. (A handful of bot-walled publishers required downloading manually in a browser.)
2. **Convert** — `scripts/convert_papers.py` transcribes each PDF to Markdown page-by-page using a vision LLM (via the sibling [`pdf-to-md`](https://github.com/brendansudol/pdf-to-md) tool; requires an `OPENAI_API_KEY`). Resumes mid-paper.
3. **Extract & analyze** — `scripts/extract_papers.py` sends each full text to gpt-5.5 (high reasoning effort, strict JSON-schema output) producing the structured extract and one-pager in a single call; `scripts/build_analysis.py` then regenerates the cross-paper views.

`scripts/build_manifest.py` and `scripts/build_data_manifest.py` regenerate the human-readable indexes from the catalogs at any time.

## Trust & caveats

- **Markdown full texts are LLM vision transcriptions** of the PDFs — high quality but not authoritative; figures appear as `[Figure: …]` placeholders. Cite the PDF/original.
- **Extracts and summaries are LLM-generated** from those transcriptions. The *guide's* claims were adversarially verified against the full texts (~540 claims checked, 8 discrepancies found and fixed — see [papers/DISCREPANCIES.md](papers/DISCREPANCIES.md)); the extracts themselves have not yet had their own verification pass.
- **Copyright stays with the original authors/publishers.** PDFs are open-access or author-hosted copies vendored for personal research; datasets keep their original licenses (recorded per-entry in `data/datasets.json`).
