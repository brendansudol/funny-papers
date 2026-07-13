# Assessing the Potential of LLM-assisted Annotation for Corpus Pragmatics: The Case of Humor

**Antonio Bianco, Nicola Brocca, Davide Garassino** — Corpus Pragmatics 10:33 · Guide entry Part 1 (corpus-pragmatics annotation) (Part 1 - Explaining & Understanding Jokes)

[paper page](https://link.springer.com/article/10.1007/s41701-026-00235-7) · [local PDF](../pdfs/x40-corpus-pragmatics.pdf) · [full markdown](../md/x40-corpus-pragmatics/x40-corpus-pragmatics.md) · [extract](../extracts/x40-corpus-pragmatics.json) · [dataset: Corpus-pragmatics humor annotations](../../data/corpus-pragmatics-humor/)

## TL;DR
The paper evaluates whether GPT-4o and LLaMA-3.3-70B-Instruct can assist corpus-pragmatics annotation of humor in Italian political tweets. The main result is a split: GPT-4o slightly exceeds the novice human annotator on binary humor detection (κ = 0.75; AC1 = 0.87), but both LLMs fall well below the novice on classifying humor functions.

## Problem & Motivation
Corpus pragmatics needs annotated data for context-dependent phenomena, but manual annotation is slow, expensive, and sensitive to annotator disagreement. Humor is especially difficult because it depends on script opposition, context, cultural knowledge, and pragmatic inference. The paper asks whether LLMs can serve as research assistants for annotating humor and its communicative functions in a corpus of Italian political discourse on X.

## Approach
The study uses Semantic Script Theory and the General Theory of Verbal Humor to define humor through overlapping and opposed scripts. It also defines five humor functions for political tweets: Self-deprecating, Aggressive, Affiliative, Defensive, and (Self-)Enhancing humor, plus NA for uncertainty. Two humans and two LLMs annotate the data: EXP, an expert Italian PhD student in humor and political discourse; NOV, an Italian Master’s student in Linguistics with no prior humor-studies expertise; GPT-4o; and LLaMA-3.3-70B-Instruct. Agreement with EXP is measured using Cohen’s kappa and Gwet’s AC1.

## Data & Experimental Setup
The source corpus contains 7,552 tweets posted by 38 Italian politicians during the 2022 election campaign, from 25 August to 25 September 2022. For Task 1, the authors select 200 tweets: 90 humorous and 110 non-humorous according to EXP. For Task 2, the 90 humorous tweets are labeled for their main communicative function. LLM prompting is few-shot: prompts include definitions and examples not included in the target dataset. For Task 1, the 200 target tweets are sent in batches of ten; Task 2 uses a similar but more complex prompt design. LLaMA-3.3 is accessed through the Hugging Face web interface; the paper does not report exact model snapshots, inference dates, or sampling settings.

## Results
For humor detection, all systems show substantial agreement with EXP. GPT-4o performs best: κ = 0.75 (z = 10.6, p < .001) and AC1 = 0.87 (SE = 0.05, p < .001). NOV is close behind with κ = 0.72 and AC1 = 0.86, while LLaMA-3.3 scores κ = 0.66 and AC1 = 0.83. For humor functions, performance drops. NOV reaches κ = 0.62 and AC1 = 0.83, but GPT-4o reaches only κ = 0.37 and AC1 = 0.70, and LLaMA-3.3 κ = 0.33 and AC1 = 0.69. The function distribution is highly skewed: Aggressive = 71, Affiliative = 12, Defensive = 1, Self-deprecating = 4, and (Self-)Enhancing = 2; χ²(4) = 199.22, p < .0001.

## Takeaways
- LLMs can be useful for first-pass binary humor detection in political tweets.
- GPT-4o can reach novice-level, and in this study slightly better-than-novice, agreement for humor detection.
- Humor-function annotation remains much harder and still favors human interpretation.
- Error analysis suggests that LLMs rely on surface cues such as emojis, punctuation, quotation marks, and dysphemistic vocabulary.
- Builders of humor annotation systems should treat LLMs as support tools, not replacements for expert pragmatic judgment.

## Limitations & Caveats
The study lacks a true gold standard based on multiple expert annotators and consensus, so F1 scores are not reported. The sample is small, monolingual, and limited to Italian political tweets; the function labels are highly imbalanced. The paper also notes that single tweets often lack the social and interactional context needed for humor interpretation, and future work should add co-text and multimodal material such as images and GIFs.
