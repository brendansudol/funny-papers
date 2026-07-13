# SemEval-2026 Task 1: MWAHAHA, Models Write Automatic Humor And Humans Annotate

**Santiago Castro, Luis Chiruzzo, Santiago Góngora, Salar Rahili, Naihao Deng, Ignacio Sastre, Victoria Amoroso, Guillermo Rey, Aiala Rosá, Guillermo Moncecchi, J. A. Meaney, Juan José Prada, Rada Mihalcea** — SemEval-2026 · Guide entry #57 (Part 8 - Datasets & Shared Tasks)

[paper page](https://aclanthology.org/2026.semeval-1.454/) · [local PDF](../pdfs/57-mwahaha.pdf) · [full markdown](../md/57-mwahaha/57-mwahaha.md) · [extract](../extracts/57-mwahaha.json) · [dataset: SemEval-2026 Task 1 MWAHAHA data](../../data/mwahaha-semeval2026/)

## TL;DR
MWAHAHA is the SemEval-2026 shared task on general-purpose humor generation: systems write constrained short jokes in English, Spanish, and Chinese and humorous GIF captions or punchlines in English. The main result is a strong null finding: a simple Gemini 2.5 Flash zero-shot baseline tied for first place in every subtask, while elaborate pipelines only marginally surpassed it within overlapping confidence intervals.

## Problem & Motivation
Prior humor shared tasks focused mostly on understanding: detection, rating, puns, offense, or edited headlines. This task targets humor generation directly, where reference-based metrics are especially weak because many valid jokes can be produced for the same prompt and funniness is subjective. The organizers therefore designed matched constraints so systems are compared on the same rare word pair, news headline, GIF, or GIF-plus-prompt rather than benefiting from easier topics.

## Approach
Subtask A asks for text jokes under either a word-inclusion constraint or a news-headline constraint, in English, Spanish, and Chinese. Subtask B is multimodal and English-only: B1 asks for a humorous caption for a GIF, and B2 asks for a short punchline completing a blank in a text prompt paired with a GIF. Evaluation follows a Chatbot Arena-style protocol: humans see two outputs for the same prompt and vote for the funnier one, tie, or skip. Non-skip votes are fit with a Bradley–Terry model to produce Elo-style ratings, with 1,000 bootstrap resamples for 95% confidence intervals.

## Data & Experimental Setup
The organizers released no training data, only development and test sets. Subtask A development data had 1 200 rows for English and Spanish and 1 000 for Chinese; test data had 300 rows per language, each with 275 new headlines and 25 rare word combinations. B1 released 1 100 development GIFs and 300 test GIFs. B2 released 500 development GIF-and-prompt pairs and 300 test pairs. The task drew 309 registered users and 37 final-phase teams. Final evaluation collected 12 936 non-skip votes, including 10 707 from paid Prolific annotators and 2 229 from volunteers.

## Results
Per-item agreement was low, as expected for humor: pooled agreement was 46.8%, with Fleiss’ κ = 0.15 and Krippendorff’s α = 0.17. But aggregate rankings were stable: split-half Spearman correlations were 0.79 in English, 0.90 in Spanish, 0.79 in Chinese, 0.90 in B1, and 0.59 in B2, for mean 0.79. In A-en, nine systems tied for first, led by the baseline at 1081 Elo. In A-es, RAGthoven scored 1182 and the baseline 1140, both tied for first. In A-zh, UIR_CIS led with 1120 while the baseline scored 1053 and remained tied for first. In B1, praveenjoshi007 scored 1140 and the baseline 1124; in B2, UIR_CIS scored 1065 and the baseline 1022, again tied for first.

## Takeaways
- Strong frontier LLM prompting is a hard baseline for humor generation.
- Generate-then-rank was common among top systems, suggesting selection matters at least as much as generation.
- SSTH, BVT, and GTVH helped some systems structure prompts, but the paper found no consistent advantage for theory grounding.
- Multilingual humor remains uneven; Chinese was difficult because homophonic wordplay is central.
- RL and preference optimization for humor were fragile, with reports of reward hacking, instability, and noisy synthetic preferences.

## Limitations & Caveats
The task had no human-written joke baseline, so the apparent leaderboard ceiling is hard to interpret. The annotator pools were demographically limited and self-selected in part. The constraints reduce but do not eliminate memorization risk, and the benchmark covers only three text languages plus English multimodal humor.
