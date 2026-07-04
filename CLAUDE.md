# CLAUDE.md — operational guide for this repo

A research library on humor + LLMs: a curated field guide (`humor-and-llms-field-guide.md`), full-text paper library (`papers/`), dataset library (`data/`), and structured extracts/analysis, all built by the scripts in `scripts/`. See [README.md](README.md) for the tour; this file is the how-not-to-break-it guide.

## Source-of-truth rules (most important)

- `papers/papers.json` and `data/datasets.json` are the **canonical catalogs**. Scripts update them in place.
- `papers/MANIFEST.md`, `papers/ANALYSIS.md`, and `data/MANIFEST.md` are **generated — never hand-edit**. After changing a catalog, extracts, or summaries, regenerate:
  - `python3 scripts/build_manifest.py` (papers manifest)
  - `python3 scripts/build_analysis.py` (cross-paper analysis)
  - `python3 scripts/build_data_manifest.py` (data manifest)
- The field guide, `papers/DISCREPANCIES.md`, `README.md`, and `docs/` (ideas, cookbook) are hand-written — edit directly.
- If a paper's guide entry changes (venue, status, title), sync `papers.json` and regenerate the manifest.

## Which Python for which script

| Script | Interpreter | Why |
| --- | --- | --- |
| `download_papers.py`, `extract_papers.py` | `/Users/bren/Documents/code/pdf-to-md/.venv/bin/python` | needs pymupdf/openai + reuses pdf-to-md's `.env` loader (`OPENAI_API_KEY`) |
| `convert_papers.py` | any `python3` | shells out to pdf-to-md with its own venv |
| `download_datasets.py` | `.venv/bin/python` (this repo's venv) | has `huggingface_hub` |
| `build_*.py`, `split_guide.py` | any `python3` | stdlib only |

All pipeline scripts are **resumable and idempotent** — safe to re-run; they skip work already done. `extract_papers.py` skips existing extracts unless `--force`; `convert_papers.py` resumes page-by-page; most support `--only KEY`.

## Conventions

- **Paper keys**: `NN-short-slug` for numbered guide entries (`03-humorbench`), `tN-…` for theory entries, `xNN-…` for unnumbered "also in this section" / pre-LLM anchor items. Dataset keys are plain slugs (`humorbench`, `oogiri-go`).
- **Dataset names in extracts** are normalized against the `name` fields in `data/datasets.json` — that's what makes ANALYSIS.md cross-references cohere. If you add a dataset, keep the name in extracts identical to the catalog name.
- **Extraction model standard**: OpenAI `gpt-5.5` with `reasoning={"effort": "high"}` and strict JSON-schema structured outputs (user's explicit choice). Stick with OpenAI for pipelines — there is **no ANTHROPIC_API_KEY on this machine**; Claude subagents (via this harness) are the option for judgment-heavy review passes instead.
- Paper statuses: `converted` / `downloaded` / `unavailable` / (`download_failed`, `convert_failed`, `pending`). Dataset statuses: `downloaded` / `too_large` / `gated` / `request` / `unavailable` / `pending` / `failed`.

## Gotchas learned the hard way

- **Bot-walled PDFs** (ACM, OpenReview, MDPI have been hit): scripted download fails; ask the user to download in a browser and drop the file at `papers/pdfs/<key>.pdf`, then re-run convert + manifest.
- **Git pushes are large** (`papers/pdfs/` is ~277 MB and versioned by design). `http.postBuffer=524288000` is already set in local git config; keep it if re-cloning.
- **git-lfs is not installed** — git-cloned datasets leave LFS pointer stubs; `download_datasets.py` detects and notes this in the catalog. Don't "fix" stubs by installing LFS without checking sizes first (2 GB cap).
- `.gitignore` keeps `data/*` out except `datasets.json` + `MANIFEST.md`; `.env` (has `OPENAI_API_KEY`) and `.venv/` are ignored. Don't commit dataset payloads.
- Guide markdown quirks: entries are `### N. [Title](url)` blocks; some works are covered inside paragraph anchors, not numbered headers — `scripts/split_guide.py` has the anchor map.

## Where things live

- Idea backlog: [docs/ideas.md](docs/ideas.md) — the canonical menu of next steps. Update it there (mark items done, add new ones) rather than inventing parallel TODO docs.
- Query recipes over catalogs/extracts: [docs/query-cookbook.md](docs/query-cookbook.md).
- Guide-verification artifacts: `papers/review/` (per-paper guide entries, discrepancy JSON) + `papers/DISCREPANCIES.md`.
- Conversion logs / API usage: `papers/runs/<key>.progress.jsonl`, `papers/md/<key>/manifest.jsonl`.
