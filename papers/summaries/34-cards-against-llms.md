# Cards Against LLMs: Benchmarking Humor Alignment in Large Language Models

**Yousra Fettach, Guillaume Bied, Hannu Toivonen, Tijl De Bie** — CHum 2026 · Guide entry #34 (Part 4 - Evaluation Methodology)

[paper page](https://aclanthology.org/2026.chum-1.4/) · [local PDF](../pdfs/34-cards-against-llms.pdf) · [full markdown](../md/34-cards-against-llms/34-cards-against-llms.md) · [extract](../extracts/34-cards-against-llms.json) · [dataset: Cards Against LLMs (code)](../../data/cards-against-llms/)

## TL;DR
This paper benchmarks whether five frontier LLMs choose the same Cards Against Humanity punchlines that human players chose. All models beat the 10% random baseline, but human alignment is only 13.4%–17.9%, and models agree with one another far more than with humans.

## Problem & Motivation
Humor is culturally embedded, socially sensitive, and hard to formalize. The authors argue that what an LLM finds funny reveals more than task capability: it reflects cultural knowledge, social boundaries, and alignment choices. Cards Against Humanity provides a structured test because each round has a black-card prompt and ten white-card responses, but the winning choice depends on contextual, often transgressive humor judgment.

## Approach
The task is discrete preference selection. For each CAH round, a model receives the black card and ten candidate white cards and must return the single funniest card. Each round is run twice with a different random ordering of the white cards to measure stability and position bias. The paper evaluates human–LLM alignment with exact-match accuracy against the human player’s chosen card, examines demographic subgroup accuracy, measures intra-model consistency and inter-model agreement, tests position bias with chi-square tests, analyzes topic preferences, and fits conditional logistic surrogate models using only card position and white-card topic flags.

## Data & Experimental Setup
The raw CAH Lab Gameplay Dataset contains 148,497 past games, 501 unique black prompt cards, and 2074 white punchline cards. After filtering out rounds completed in fewer than 10 seconds, over 120 seconds, or marked as skipped, the authors obtained 107,562 unique rounds and sampled 4,947 rounds. With two replicates, this yielded 9,894 records; 282 were excluded because at least one model abstained or produced an unparseable response, leaving 9,612 valid records. The models were GPT-5.2, Gemini 3 Flash, Claude Opus 4.5, Grok 4, and DeepSeek-V3.2, queried through APIs at temperature 0.8. A demographic analysis used 824 players with non-missing IDs. White cards were labeled with 15 topics using Mixtral 8x7B.

## Results
Human–LLM alignment was low: GPT 13.4%, Gemini 16.5%, Claude 17.9%, DeepSeek 15.0%, and Grok 17.0%, versus a 10% random baseline. Claude was best, but still below the card popularity baseline at 19.11% and the boosted-tree ensemble at 19.77%. Intra-model consistency was much higher: GPT 49.5%, Gemini 59.9%, Claude 59.8%, DeepSeek 44.9%, and Grok 63.3%. Inter-model agreement ranged from 21.4% to 44.9%, exceeding the 13%–18% human-alignment range. All models had significant position bias: GPT χ²=356, Gemini χ²=282, Claude χ²=678, DeepSeek χ²=1851, and Grok χ²=658, all p<0.001. Topic analysis showed Gemini, DeepSeek, Claude, and Grok chose bodily humor in 31% to 40% of answers versus 21% for humans, and sexual themes in 29% to 38% versus 24% for humans. Surrogate models using only position and topic reached round-level accuracies of 0.171 for GPT, 0.339 for Gemini, 0.244 for Claude, 0.351 for DeepSeek, and 0.361 for Grok.

## Takeaways
- Beating random choice does not imply human-like humor judgment; the best LLM remains below simple human-choice baselines.
- LLMs appear to share a stable, partially common humor profile that is more aligned with other LLMs than with human CAH players.
- Position order and broad content categories can explain a substantial share of choices, so humor benchmarks should control for option-order artifacts.
- Topic preferences matter: models over-select bodily and sexual cards and under-select politics/society and identity/demographic cards relative to humans.

## Limitations & Caveats
The dataset has only one human choice per round, so inter-rater agreement is unavailable. The study uses two replicates, one temperature setting, and a predominantly Western, self-selected CAH player population. Topic labels are LLM-generated, and four of the five evaluated models are developed primarily in Western contexts.
