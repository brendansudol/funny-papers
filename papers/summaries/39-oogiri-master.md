# OOGIRI-MASTER: Benchmarking Humor Understanding via Oogiri

**Soichiro Murakami, Hidetaka Kamigaito, Hiroya Takamura, Manabu Okumura** — arXiv:2512.21494 · Guide entry #39 (Part 4 - Evaluation Methodology)

[paper page](https://arxiv.org/abs/2512.21494) · [local PDF](../pdfs/39-oogiri-master.pdf) · [full markdown](../md/39-oogiri-master/39-oogiri-master.md) · [extract](../extracts/39-oogiri-master.json) · [dataset: Oogiri-Master dataset builder](../../data/oogiri-master-builder/)

## TL;DR
The paper introduces OOGIRI-CORPUS, a Japanese text-to-text Oogiri dataset, and OOGIRI-MASTER, a 600-item benchmark for judging Oogiri humor. Its strongest benchmark result is GPT-5 with insight-augmented prompting at 70.7% average accuracy, improving over GPT-5’s 67.6% baseline and exceeding the 68.7% human baseline.

## Problem & Motivation
The paper treats Oogiri, a Japanese creative response game, as a testbed for human-like humor understanding in LLMs. Existing Oogiri resources are described as limited because they can expose popularity signals during rating and often provide few candidate responses per prompt. The authors ask what makes Oogiri responses funny to humans and argue that reliable analysis requires many candidate responses per prompt, independent voting, and objective metrics for comparing funniness judgments.

## Approach
The study has three parts. First, it builds OOGIRI-CORPUS from Oogiri Sogo, a public Japanese Oogiri competition platform where vote counts are not displayed during voting. Second, it analyzes linguistic features that distinguish high-rated from low-rated responses, using top-three responses per prompt as high-rated and bottom-three responses as low-rated. Features include basic surface measures, semantic distance, NLI probabilities, surprisal, nPMI, and eight GPT-5-scored higher-order features such as ambiguity exploitation, benign violation, incongruity resolution, metaphor use, and perspective shift. Third, it defines OOGIRI-MASTER with four relative MCQA tasks and one absolute funny/not-funny classification task, and tests baseline versus insight-augmented prompts.

## Data & Experimental Setup
The authors crawled 2,165 prompts from Oogiri Sogo and filtered out prompts with fewer than 100 total votes, leaving 908 prompts. OOGIRI-CORPUS contains 82,536 prompt–response pairs, with 95.9 responses and 171.6 votes per prompt on average. The feature analysis uses 5,448 responses: 908 prompts × 6 responses. OOGIRI-MASTER contains 600 items: 400 MCQA items across four relative-judgment tasks and 200 binary-classification items. Models include gpt-oss-20b, DeepSeek-R1-14b, DeepSeek-R1-14b_ja, LLM-jp-3.1-13b_ja, Claude-Opus-4, Gemini-2.5-Pro, and GPT-5. API model results are averaged over three trials with temperature zero. Human performance is measured with 21 Yahoo! Crowdsourcing workers per item after attention checks.

## Results
High-rated responses were shorter than low-rated ones: length High 14.12 vs Low 16.40, Cohen’s d -0.28. Higher-order features showed the strongest effects: perspective shift High 2.40 vs Low 1.87, d 0.50; ambiguity exploitation High 2.10 vs Low 1.61, d 0.42; incongruity resolution High 3.71 vs Low 3.35, d 0.36. With the baseline prompt, Claude-Opus-4 and humans tied at 68.7% average accuracy, followed by GPT-5 at 67.6%. With insight-augmented prompting, GPT-5 reached 70.7%, a +3.1 point gain over its baseline and 2.0 points above the human baseline. Feature prompting hurt some models, including Claude-Opus-4, which dropped from 68.7% to 59.2%. Continued Japanese pretraining helped DeepSeek-R1: DeepSeek-R1-14b_ja improved over DeepSeek-R1-14b from 41.3% to 44.6% in the baseline setting and from 41.4% to 46.0% with features.

## Takeaways
- Humor judgments benefited most from higher-order cues such as perspective shift, ambiguity, and incongruity resolution, but simple features like brevity were also useful.
- Feature-augmented prompts can improve strong models, but may cause weaker models to over-rely on heuristics.
- Asking GPT-5 to consult features only when uncertain produced the best reported average accuracy, 70.7%.
- Japanese continued pretraining improved performance on this Japanese cultural humor benchmark.

## Limitations & Caveats
The benchmark is limited to Japanese text-to-text Oogiri and does not cover generation, explanation, or multimodal Oogiri variants. Some features, such as character-type ratios, are Japanese-specific. The authors also note a possible demographic mismatch between crowdworkers and Oogiri-platform users.
