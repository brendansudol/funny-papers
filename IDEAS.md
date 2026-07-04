# funny-papers — Ideas & Near-Term Backlog

Candidate next steps for the project, gathered 2026-07-03. Nothing here is committed work — it's a menu. Roughly ordered by leverage within each section. See [papers/MANIFEST.md](papers/MANIFEST.md), [papers/ANALYSIS.md](papers/ANALYSIS.md), and [data/MANIFEST.md](data/MANIFEST.md) for what already exists.

## Done (for context)

- ✅ Paper library: 80/86 guide entries with PDF + full-text markdown (`papers/`)
- ✅ Dataset library: 26 of 34 public datasets vendored, ~8.8GB (`data/`)
- ✅ Structured extracts + one-pagers + cross-paper analysis (`papers/extracts/`, `papers/summaries/`, `papers/ANALYSIS.md`)
- ✅ Guide-vs-paper discrepancy check; all 8 fixes applied ([papers/DISCREPANCIES.md](papers/DISCREPANCIES.md))
- ✅ Git + GitHub: public repo at https://github.com/brendansudol/funny-papers. `data/` is gitignored (~8.8GB, rebuilds from `data/datasets.json` via the scripts); `papers/pdfs/` is versioned. Secrets stay in `.env` (ignored).

## Housekeeping (cheap, do soon)

- **BibTeX file** (`papers/papers.bib`) — generate from `papers.json` + extracts (extracts have verified author lists). Cheap; useful the moment any writing happens.
- **Figure images for visual-humor papers** — transcriptions have `[Figure: …]` placeholders; rerun pdf-to-md with `--keep-images` for the few papers where the figure *is* the content (HumorDB, YesBut, PixelHumor, cartoon papers).

## Make the library more usable

- **RAG / semantic search index** — chunk + embed the ~1,400 markdown pages (and/or one-pagers) for "ask the library a question, get paper+page citations." Local and simple (sqlite + embeddings). The extracts make good metadata filters (task, dataset, theory).
- **Citation lineage graph** — extract each paper's references, map who-cites-whom among the 86 entries, and render the lineages the guide describes in prose (Hessel → caption-preferences → HumorBench; Crowd Score → HumorRank). Could output a Mermaid/DOT graph into the repo or an Artifact page.
- **Library browser page** — a single searchable HTML page (Artifact or local file) over the catalog: filter by task/theory/dataset/model, click through to one-pagers. Mostly a `build_*.py` script over existing JSON.
- **Query examples doc** — a short cookbook of `jq`/python one-liners against `papers/extracts/*.json` ("which papers evaluate on X", "all headline results mentioning GPT-4o").

## Keep it alive

- **arXiv watcher** — weekly scheduled job (Claude Code `/schedule` routine): query arXiv for new humor+LLM papers, filter against `papers.json`, propose new entries in the guide's format. The guide is compiled June 2026 and the field moves monthly.
- **Venue-status checker** — periodic pass over `preprint`-tagged entries to see if they've since landed at a venue (the guide's compilation note explicitly flags this drift). The discrepancy check found one already (#19 → IASDR 2025).
- **Dataset gap watch** — recheck the blocked datasets occasionally: github.com/SDS-NLP/Oogiri-Eval (404 as of July 2026), MWAHAHA post-competition data in the organizers' repo, MemeReaCon release.
- **One-time unblocks (user action needed):** Chumor 2.0 (accept HF click-through + `hf auth login`), MWAHAHA (free Codabench account), CAH rounds data (email mail@cardsagainsthumanity.com), workplace-humor dataset (email authors — anonymous repo expired).

## Build the actual bot

- **Eval harness first** — Part 4's core lesson: measurement drives everything. Concretely: pairwise/tournament LLM judging (HumorRank-style, GTVH-grounded rubric) + multi-dimensional scoring (#38's Novelty/Clarity/Relevance/Intelligence/Empathy axes, noting LLM judges over-weight Novelty vs. human Empathy). Vendored data to seed it: caption-ranking (250M votes), Phunny, rJokes, Oogiri-GO.
- **Reproduction runs** — before building anything new, reproduce 1–2 headline numbers with a current model using vendored data + code (HumorBench has its autograder in `data/humorbench/`; PunEval has splits + perturbations). Validates the harness and gives baselines.
- **Generation experiments** — the guide's synthesis says generic CoT loses to structured approaches. Implementable from the extracts/full texts: script-opposition control (HOMER, #29), persona diversity (HumorGen's six cognitive personas, #13), generate–evaluate–revise loops (#15, #16), leap-of-thought (CLoT, #11). Each is a small pipeline testable against the eval harness.
- **Theory-grounded joke schema** — operationalize GTVH's six Knowledge Resources as a generation/annotation schema (the guide calls GTVH "the most engineerable theory"; HOMER and HumorRank both operationalize it).
- **Safety guardrails from day one** — Part 6 findings: engagement-maximizing humor amplifies harm (#47), humor is a jailbreak vector (#49), over-filtering flattens edge (#41). Benign-violation theory (T6) as the design frame for the boundary.

## Analysis ideas (cheap, high-interest)

- **Cross-paper contradiction/agreement mining** — the extracts make it cheap to ask "where do papers disagree?" (e.g., #2 "not funny" vs #31 "funnier than laypeople"; the guide's Synthesis 1 explains it as task-format dependence — test that framing against all 80 extracts).
- **Extract spot-verification pass** — the discrepancy check validated the *guide*; a sampled Opus pass over extracts themselves (numbers vs. transcription) would certify the comparison database for downstream use.
- **Auto-generated reading paths** — cluster papers by extract fields (task × theory × modality) and compare against the guide's hand-written reading paths; differences are interesting either way.

## Pipeline polish (only if it starts to matter)

- **`--provider claude` path in extract_papers.py** — Anthropic SDK + Message Batches (50% off) + structured outputs; blocked on an `ANTHROPIC_API_KEY` on this machine. gpt-5.5 at `reasoning: high` is the current standard.
- **`reasoning.summary` logging** — currently skipped; only worth it if we want to audit extraction reasoning.
- **Fetch-on-demand for the big datasets** — jmhessel caption corpus (7.9GB), OxfordTVG-HIC, Harm-or-Humor drive folder; add only when an experiment needs them.
