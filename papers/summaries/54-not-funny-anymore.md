# Not Funny Anymore: LLM Judges Confuse Literal Similarity for Humor in Translated Jokes

**Fabricio Rivera, Rohit Pochugari, Tessa Chan, Devansh Katakwar, Kevin Zhu, Michael Saxon** — LM4UC @ AAAI 2026 · Guide entry #54 (Part 7 - Cross-Cultural & Translation)

[paper page](https://openreview.net/forum?id=fdrM652upk) · [local PDF](../pdfs/54-not-funny-anymore.pdf) · [full markdown](../md/54-not-funny-anymore/54-not-funny-anymore.md) · [extract](../extracts/54-not-funny-anymore.json)

## TL;DR
This paper studies whether LLMs can judge whether humor is preserved in reference-free joke translation. Using 7 LLMs, 3 prompting strategies, and human Likert annotations on 162 English-to-Chinese and 76 English-to-Hindi joke pairs, it finds that LLM judges are badly misaligned with humans: strict agreement is often near or below the 20% random baseline, and the best strict score in Table 1 is only 23.5. The central explanation is that LLM judges confuse literal similarity with successful humor preservation.

## Problem & Motivation
Humor translation is hard because jokes often rely on puns, wordplay, idioms, cultural references, timing, and surprise rather than literal sentence meaning. Standard MT metrics such as BLEURT and COMET are designed for general adequacy and fluency, and reference-based evaluation can reward similarity to a gold translation rather than preservation of the comedic effect. The paper asks whether large language models can reliably evaluate cross-lingual humor preservation without a reference translation, based only on the source joke and candidate translation.

## Approach
The authors build a reference-free LLM-as-a-Judge framework. Each model receives the English source joke and translated joke and outputs a single 1–5 humor-preservation score. They test vanilla, chain-of-thought, and self-consistency prompts, all explicitly telling models to prioritize humor preservation over surface lexical similarity.

They also propose a token-level semantic alignment diagnostic for literalness. Source and target tokens are embedded with `xlm-r-100langs-bert-base-nli-stsb-mean-tokens`, aligned with an orthogonal Procrustes transformation, matched with the Hungarian algorithm, and scored by mean token-level cosine similarity. Higher scores indicate translations that more closely follow the source wording and structure.

## Data & Experimental Setup
The dataset is built from jokes sampled from the Kaggle short-jokes dataset. The paper reports 162 jokes translated into Mandarin using GPT-4o-mini and 76 English-to-Hindi joke pairs. Four bilingual native speakers annotated Mandarin translations, and three annotators annotated Hindi translations. Ratings used a five-point Likert scale for semantic preservation of humor. The paper reports Krippendorff’s α of 0.776 for Mandarin and “0.776 (change number)” for Hindi.

The evaluated judges are `claude-sonnet-4-5-20250929`, `gpt-4o`, `gemini-2.5-flash-lite`, `Qwen3-235B-A22B-Instruct-2507-tput`, `Llama-4-Maverick-17B-128E-Instruct-FP8`, `Mistral-7B-Instruct-v0.3`, and `DeepSeek-V3.1`.

## Results
Strict agreement is poor. Table 1’s best single strict accuracy is Gemini with self-consistency at 23.5, only slightly above the 20% random baseline for a five-point scale. Average strict accuracies by model range from 9.1 for OpenAI to 15.8 for Gemini. The paper states that Spearman and Pearson correlations are low, mostly between −0.15 and 0.27.

For ±1 accuracy and MAE, Mistral with vanilla prompting performs best in Table 3, with ±1 Accuracy of 61.5 and MAE of 1.31. In binary classification metrics, Mistral vanilla has the highest accuracy at 75.8, but F1 remains low at 29.1. Error analysis shows that LLM scores rise with literalness: models give higher scores to more word-for-word translations, even when humans judge that the joke’s wordplay or idiom no longer works.

## Takeaways
- Do not assume LLM judges can evaluate translated humor just because they perform well on general MT evaluation.
- Prompting with chain-of-thought or self-consistency does not fix the core misalignment.
- Literal semantic similarity is a confounder: LLM judges often reward faithful wording instead of preserved comedic effect.
- Builders of humor-translation metrics should explicitly model or control for literalness.
- Pun- and idiom-heavy translations are especially risky for automatic judging.

## Limitations & Caveats
The paper lists a small dataset size, synthetic GPT-4o-mini translations, mostly short one-liners, heavy reliance on wordplay and puns, and restriction to current SoTA LLMs. Its Limitations section also states the dataset is English-to-Chinese only, although the methodology and abstract report an additional 76 English-to-Hindi pairs.
