<!-- guide claims for 54-not-funny-anymore (#54) -->

### 54. [Not Funny Anymore: LLM Judges Confuse Literal Similarity for Humor in Translated Jokes](https://openreview.net/forum?id=fdrM652upk)
Rivera, Pochugari, Chan, Katakwar, Zhu & Saxon (Algoverse AI / Andrews Univ. / Univ. of Washington) — **LM4UC @ AAAI 2026 workshop** (OpenReview) · `workshop` `dataset` `method`
- **Method:** Reference-free humor-translation *evaluation* — LLM-as-judge rates how well a joke's humor survives translation, vs. human 5-point Likert ratings; introduces a correlation-based "literalness" metric in a multilingual embedding space (Procrustes-aligned token embeddings) to diagnose failures.
- **Dataset:** 162 English→Chinese and 76 English→Hindi joke pairs with human annotations; 7 LLM judges × prompting strategies (vanilla / CoT / self-consistency).
- **Findings:** Judges struggle (strict agreement near or below the 20% random baseline), and the failure is driven by an **over-literal bias** — models reward word-for-word fidelity over preserved comedic effect. A sharp caution for LLM-as-judge on creative cross-lingual tasks.
