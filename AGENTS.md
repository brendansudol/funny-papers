# AGENTS.md - operational guide for this repo

This repository is a research library on humor and LLMs: a curated field
guide (`humor-and-llms-field-guide.md`), a full-text paper library (`papers/`),
a dataset library (`data/`), and structured extracts and analysis built by the
scripts in `scripts/`. See `README.md` for the project tour. This file records
the operational rules that are easy for an agent to miss.

## Sources of truth and generated files

- `papers/papers.json` and `data/datasets.json` are the canonical catalogs.
- `papers/MANIFEST.md`, `papers/ANALYSIS.md`, `papers/EVIDENCE.md`,
  `data/MANIFEST.md`, and `papers/review/guide-entries/` are generated. Never
  hand-edit them.
- The field guide, `papers/synthesis_claims.json`,
  `papers/DISCREPANCIES.md`, `README.md`, and `docs/` are hand-written.
- `papers/extracts/` and `papers/summaries/` are pipeline outputs. Prefer
  re-extraction or evidence enrichment; make a manual correction only when it
  is grounded in the primary paper and preserves provenance metadata.
- Restricted primary sources and all full-text derivatives live under
  gitignored `papers/private/<key>/`. Never copy their PDFs, Markdown, page
  files, manifests, chapter caches, or run logs into a public/versioned path.
  Public summaries may link only to the official publisher pages recorded in
  the catalog and must carry the restricted-source notice.
- If a guide entry changes bibliographic facts such as title, venue, or
  publication status, synchronize `papers/papers.json` and regenerate the
  affected views.

## Change and validation matrix

- After changing the field guide, run `python3 scripts/split_guide.py`. If a
  compact entry label changes, update `ANCHORS` in that script in the same
  change.
- After changing `papers/papers.json`, run
  `python3 scripts/build_manifest.py`.
- After changing extracts or normalization logic, run
  `python3 scripts/build_analysis.py` and
  `python3 scripts/build_evidence.py`.
- After changing `papers/synthesis_claims.json`, run
  `python3 scripts/build_evidence.py`.
- After changing `data/datasets.json`, run
  `python3 scripts/build_data_manifest.py`.
- Run `python3 -m unittest discover -s tests -v` after substantive changes.
  Some tests deliberately encode catalog and claim cardinalities; update those
  expectations only when entries or claims were intentionally added or
  removed, never merely to silence a failure.

## Python environments and expensive operations

| Script | Interpreter | Notes |
| --- | --- | --- |
| `download_papers.py`, `extract_papers.py`, `enrich_evidence.py` | `/Users/bren/Documents/code/pdf-to-md/.venv/bin/python` | Provides PyMuPDF/OpenAI and the sibling project's `.env` loader |
| `convert_papers.py` | any `python3` | Shells out to the sibling `pdf-to-md` venv |
| `download_datasets.py` | `.venv/bin/python` | Requires `huggingface_hub` |
| `build_*.py`, `split_guide.py` | any `python3` | Standard-library-only local builds |

- The paper pipeline currently depends on the sibling checkout at
  `/Users/bren/Documents/code/pdf-to-md`. Check that path before running it;
  do not silently substitute another converter, provider, or model.
- Build scripts, the guide splitter, and tests are local and cheap. Paper
  conversion, extraction, and evidence enrichment use paid model calls;
  downloads use the network, and dataset downloads may be multi-gigabyte.
- Use `--only KEY` where supported. Do not start an unscoped paid or large
  download run unless the task explicitly requires it.
- Restricted conversion and extraction additionally require the explicit
  `--include-restricted` flag. This is a privacy guard, not authorization to
  run a paid operation.
- Pipeline scripts are resumable and idempotent, but that is not permission to
  trigger expensive work unnecessarily. `extract_papers.py` skips existing
  extracts unless `--force`; `convert_papers.py` resumes page by page.

## Data and analysis conventions

- Paper keys use `NN-short-slug` for numbered guide entries, `tN-...` for
  theory entries, and `xNN-...` for unnumbered or historical-anchor entries.
  Dataset keys are plain slugs.
- Dataset names in extracts must match the `name` fields in
  `data/datasets.json`; these names drive cross-references in the analysis.
- Model and task aggregation is owned by the alias and normalization logic in
  `scripts/build_analysis.py`. Keep extract values faithful and add
  defensible aliases plus tests instead of bulk-rewriting extracts merely to
  merge matrix rows. Do not collapse narrower tasks such as pun generation
  into a broader category without a substantive reason.
- The extraction standard is OpenAI `gpt-5.5` with
  `reasoning={"effort": "high"}` and strict JSON-schema outputs. A model or
  provider change must be explicit and recorded, not an incidental fallback.
- Evidence profiles distinguish participants from observations, human from
  LLM judges, single-sample from best-of-N selection, exact model/version/date,
  inference budget, human baselines, contamination risk, and LLM-judge
  dependence. Use `enrich_evidence.py` to backfill them without regenerating
  summaries.
- Paper statuses are `converted`, `downloaded`, `restricted`, `unavailable`,
  `download_failed`, `convert_failed`, or `pending`. Dataset statuses are
  `downloaded`, `too_large`, `gated`, `request`, `unavailable`, `pending`, or
  `failed`.

## Research integrity

- Treat compilations, search results, extracts, and summaries as navigation
  aids. Verify bibliographic metadata and substantive guide claims against the
  primary paper or archival record.
- Preserve study-design qualifications when summarizing results, especially
  judge population, candidate-selection budget, model version/date, human
  baseline, contamination risk, and dependence on an LLM judge.
- Do not turn a nonsignificant difference into an equivalence or human-parity
  claim. Keep conclusions scoped to the tested task, stimuli, population, and
  protocol.

## Repository gotchas

- Bot-walled distributable PDFs from ACM, OpenReview, and MDPI may require a
  browser download. Put a verified file at `papers/pdfs/<key>.pdf`, then rerun
  the relevant catalog, conversion, and build steps. Restricted sources go
  only to `papers/private/<key>/source.pdf` and use the explicit opt-in path.
- PDFs are versioned by design, so pushes can be large. Do not remove them or
  introduce Git LFS without an explicit repository-level decision.
- Git LFS is not installed. Dataset clones may contain pointer stubs;
  `download_datasets.py` detects and records them. Check size before changing
  that behavior because the downloader has a 2 GB per-dataset cap.
- `.gitignore` excludes dataset payloads under `data/` except the catalog and
  manifest. `.env` and `.venv/` are also ignored. Never commit credentials or
  dataset payloads.
- The worktree may contain large, intentional batches of pipeline output.
  Preserve pre-existing changes and never revert unrelated files while
  completing a narrower task.

## Repository map

- `docs/ideas.md`: canonical backlog and next-step menu; do not create a
  parallel TODO document.
- `docs/query-cookbook.md`: verified catalog and extract queries.
- `papers/review/` and `papers/DISCREPANCIES.md`: guide-verification artifacts.
- `papers/runs/<key>.progress.jsonl` and `papers/md/<key>/manifest.jsonl`:
  conversion logs and API usage.
