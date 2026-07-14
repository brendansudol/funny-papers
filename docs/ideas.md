# funny-papers — Ideas & Near-Term Backlog

Candidate next steps for the project, gathered 2026-07-03. Nothing here is committed work — it's a menu. Roughly ordered by leverage within each section. See [papers/MANIFEST.md](../papers/MANIFEST.md), [papers/ANALYSIS.md](../papers/ANALYSIS.md), and [data/MANIFEST.md](../data/MANIFEST.md) for what already exists.

## Done (for context)

- ✅ Paper library: 111/116 guide entries with distributable PDF + full-text Markdown; restricted-source mode and local primary sources for T1, T2, T4, and Suls's half of T5; T3 remains unavailable (`papers/`)
- ✅ Dataset library: 39 of 53 artifacts vendored, ~9.4GB (`data/`)
- ✅ Structured extracts + one-pagers + cross-paper analysis (`papers/extracts/`, `papers/summaries/`, `papers/ANALYSIS.md`)
- ✅ Reflowable EPUB reader editions: field guide alone or the guide plus all 115 available public summaries, with canonical ordering, restricted-source safeguards, and EPUBCheck validation (`scripts/build_ebook.py`)
- ✅ Evidence-strength profiles + synthesis support/counterevidence/confidence map ([papers/EVIDENCE.md](../papers/EVIDENCE.md))
- ✅ Guide-vs-paper evidence certification: all 111 converted entries audited across two passes (796 claims; all 14 fixes applied), plus a stratified 26-extract substantive spot check ([papers/DISCREPANCIES.md](../papers/DISCREPANCIES.md))
- ✅ Restricted theory extraction: scoped gpt-5.5 conversion and extraction completed for T1, T2, T4, and Suls's half of T5, with complete-source and direct-claim quality checks; all four remain outside the certification totals pending an independent audit.
- ✅ Git + GitHub: public repo at https://github.com/brendansudol/funny-papers. `data/` is gitignored (~9.4GB, rebuilds from `data/datasets.json` via the scripts); distributable `papers/pdfs/` is versioned; restricted `papers/private/` and secrets stay ignored.
- ✅ Docs: [README.md](../README.md) (front door), [AGENTS.md](../AGENTS.md) (agent ops guide; imported by `CLAUDE.md`), [docs/query-cookbook.md](query-cookbook.md) (verified jq/python recipes over catalogs + extracts)

## Housekeeping (cheap, do soon)

- **Certify restricted theory extracts** — independently audit the T1, T2, T4, and partial-T5 derived extracts before folding them into guide certification. T5 remains explicitly partial until Oring is consulted; T3 remains an acquisition gap.
- **BibTeX file** (`papers/papers.bib`) — generate from `papers.json` + extracts (extracts have verified author lists). Cheap; useful the moment any writing happens.
- **Figure images for visual-humor papers** — transcriptions have `[Figure: …]` placeholders; rerun pdf-to-md with `--keep-images` for the few papers where the figure *is* the content (HumorDB, YesBut, PixelHumor, cartoon papers).

## Make the library more usable

- **RAG / semantic search index** — chunk + embed the ~1,880 markdown pages (and/or one-pagers) for "ask the library a question, get paper+page citations." Local and simple (sqlite + embeddings). The extracts make good metadata filters (task, dataset, theory).
- **Citation lineage graph** — extract each paper's references, map who-cites-whom among the 116 entries, and render the lineages the guide describes in prose (Hessel → caption-preferences → HumorBench; Crowd Score → HumorRank). Could output a Mermaid/DOT graph into the repo or an Artifact page.
- **Library browser page** — a single searchable HTML page (Artifact or local file) over the catalog: filter by task/theory/dataset/model, click through to one-pagers. Mostly a `build_*.py` script over existing JSON. Natural extension: publish it (plus summaries/manifests) via GitHub Pages since the repo is already public.
- **Claude Code project skill / MCP server over the library** — wrap the cookbook queries + full-text grep + summary lookup as a skill or local MCP server, so any future session (here or in other repos) can ask the library questions without rediscovering the layout.

## Keep it alive

- **arXiv watcher** — weekly scheduled job (Claude Code `/schedule` routine): query arXiv for new humor+LLM papers, filter against `papers.json`, propose new entries in the guide's format. The guide was revised July 2026 and the field moves monthly.
- **Venue-status checker** — periodic pass over `preprint`-tagged entries to see if they've since landed at a venue (the guide's compilation note explicitly flags this drift). The discrepancy check found one already (#19 → IASDR 2025).
- **Dataset gap watch** — recheck the blocked datasets occasionally: MaMe-Re (paper still has a placeholder URL), github.com/SDS-NLP/Oogiri-Eval (404 as of July 2026), MemeReaCon release, and the anonymized HinS OSF link once it has a stable public project URL.
- **One-time unblocks (user action needed):** MULAI (contact authors for an individual license), CHEESE! (request the full ORTOLANG corpus), Chumor 2.0 (accept HF click-through + `hf auth login`), D-HUMOR (sign the authors' data-use agreement), CAH rounds data (email mail@cardsagainsthumanity.com), workplace-humor dataset (email authors — anonymous repo expired).

## Build the actual bot

- **Eval harness first** — Part 4's core lesson: measurement drives everything. Use randomized, source-blind **human pairwise preference** as the criterion measure, with target-audience metadata, ties/skips, position reversal, repeated items, and uncertainty over system rankings. Multi-dimensional human ratings (#38's Novelty/Clarity/Relevance/Intelligence/Empathy axes) should diagnose *why* preferences differ. Only after measuring agreement and bias on that target sample should an LLM judge be calibrated as a screening surrogate; report its human correlation, position/length/self-preference biases, and rank stability (Does Bigger Mean Funnier?; #34; #54; #57). Vendored data to seed it: caption-ranking (250M votes), Phunny, Jester, rJokes, Oogiri-GO, and MWAHAHA.
- **Reproduction runs** — before building anything new, reproduce 1–2 headline numbers with a current model using vendored data + code (HumorBench has its autograder in `data/humorbench/`; PunEval has splits + perturbations). Validates the harness and gives baselines.
- **Contamination audit for eval data** — before trusting eval numbers, check which vendored benchmarks are plausibly in current models' training data (rJokes and SemEval puns almost certainly are; Phunny was built specifically with contamination controls — start from its methodology). Determines which datasets can anchor the harness honestly.
- **Generation experiments** — compare structured approaches without presuming the winner: script-opposition control (HOMER, #29), persona diversity (HumorGen's six cognitive personas, #13), generate–evaluate–revise loops (#15, #16), and leap-of-thought (CLoT, #11). Hold the base model, prompt information, output/token budget, and best-of-*N* budget fixed, include the simple MWAHAHA-style frontier baseline, and use blind human evaluation.
- **Theory-grounded joke schema** — operationalize GTVH's six Knowledge Resources as a generation/annotation schema. HOMER and HumorRank both show that it is an engineerable vocabulary; treat it as a useful control surface, not a complete theory of what people find funny.
- **Safety guardrails from day one** — Part 6 findings: engagement-maximizing humor amplifies harm (#47), humor is a jailbreak vector (#49), over-filtering flattens edge (#41). Use benign-violation theory (T6) as one diagnostic lens alongside target, identity, power, relationship, and audience uptake.

## Analysis ideas (cheap, high-interest)

- **Cross-paper contradiction/agreement mining** — the extracts make it cheap to ask "where do papers disagree?" (e.g., #2 "not funny" vs #31 "funnier than laypeople"; the guide's Synthesis 1 explains it as task-format dependence — test that framing against all 111 extracts).
- **Auto-generated reading paths** — cluster papers by extract fields (task × theory × modality) and compare against the guide's hand-written reading paths; differences are interesting either way.
- **Field timeline / trends view** — papers by year × task × model generation from the extracts: watch the 2023→2026 shift (detection → explanation → generation → evaluation methodology), which theories rise/fall, when each frontier model shows up in evals. One `build_*.py` script + a chart or two.

## Pipeline polish (only if it starts to matter)

- **`--provider claude` path in extract_papers.py** — Anthropic SDK + Message Batches (50% off) + structured outputs; blocked on an `ANTHROPIC_API_KEY` on this machine. gpt-5.5 at `reasoning: high` is the current standard.
- **`reasoning.summary` logging** — currently skipped; only worth it if we want to audit extraction reasoning.
- **Fetch-on-demand for the big datasets** — jmhessel caption corpus (7.9GB), OxfordTVG-HIC, Harm-or-Humor drive folder; add only when an experiment needs them.
