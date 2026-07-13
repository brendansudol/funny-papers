<!-- guide claims for 57-mwahaha (#57) -->

### 57. [SemEval-2026 Task 1: MWAHAHA — Models Write Automatic Humor And Humans Annotate](https://aclanthology.org/2026.semeval-1.454/)
Castro, Chiruzzo, Góngora, Deng, Rahili, Sastre, Rosá, Amoroso, Rey, Moncecchi, Meaney, Prada & Mihalcea — **SemEval-2026** · `workshop` `shared task` `dataset` `benchmark`
- **Method:** The first general-purpose humor-generation shared task: constrained short jokes in English, Spanish, and Chinese plus GIF caption/punchline tasks, ranked by pairwise human preference and Elo. It drew 309 registrants, 37 final teams, and 12,936 non-skip judgments.
- **Findings:** A simple zero-shot Gemini 2.5 Flash baseline tied for first in every subtask; most elaborate multi-stage systems only marginally surpassed it with overlapping confidence intervals. Per-item agreement was low (Fleiss' κ=.15), while split-half system rankings were reasonably stable (mean Spearman ρ=.79). There was no human-written baseline, so the apparent performance ceiling is not a human-parity result.
- **Why it matters:** The released prompts, evaluation data, and leaderboards make it the likely generation anchor that SemEval-2017 Task 7 became for puns. It is also the strongest current warning against inferring from many separate method papers that scaffolding or theory grounding reliably beats a well-prompted frontier baseline.
