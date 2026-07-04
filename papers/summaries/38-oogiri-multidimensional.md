# Assessing the Capabilities of LLMs in Humor: A Multi-dimensional Analysis of Oogiri Generation and Evaluation

**Ritsu Sakabe, Hwichan Kim, Tosho Hirasawa, Mamoru Komachi** — AAAI 2026 · Guide entry #38 (Part 4 - Evaluation Methodology)

[paper page](https://arxiv.org/abs/2511.09133) · [local PDF](../pdfs/38-oogiri-multidimensional.pdf) · [full markdown](../md/38-oogiri-multidimensional/38-oogiri-multidimensional.md) · [extract](../extracts/38-oogiri-multidimensional.json)

## TL;DR
This paper evaluates whether state-of-the-art LLMs can generate and judge Japanese Oogiri humor using a new six-dimensional annotation setup. The main result is that LLMs generate responses between low- and mid-tier human performance, while their evaluations align poorly with humans: Claude Sonnet 4 has the best Overall Funniness correlation, but only 0.266.

## Problem & Motivation
Prior LLM humor evaluations often reduce humor to a single “funny/not funny” or overall score. The authors argue that this misses important differences in humor sensibility between humans and LLMs. They focus on Oogiri, a Japanese improvisational comedy format where a participant answers a topic with a humorous punchline, and ask two questions: whether LLMs can produce responses humans find funny, and whether LLMs can judge humorous responses the way humans do.

## Approach
The paper builds a multi-dimensional evaluation framework with six 0–4 axes: Novelty, Clarity, Relevance, Intelligence, Empathy, and Overall Funniness. GPT-4.1, Gemini 2.5 Pro, and Claude Sonnet 4 are prompted in Japanese to generate one funny answer per Oogiri topic. The same three models are then used as LLM judges, evaluating topic–response pairs with the same rubric given to humans.

## Data & Experimental Setup
The source data comes from Oogiri-GO and a newly collected Oogiri-Chaya dataset. After filtering, Oogiri-GO contributes 1,329 topics, and Oogiri-Chaya contributes 551 topics. From these, the authors select 200 topics, split into 100 text-based and 100 image-based topics. For each topic, they evaluate eight response types: human High, Mid, and Low vote tiers; an Unrelated response; a serious GPT-4.1 response; and humorous responses from GPT-4.1, Gemini 2.5 Pro, and Claude Sonnet 4. Human annotation is done through Lancers, with four native Japanese speakers rating each response.

## Results
For generation, Gemini 2.5 Pro is the strongest LLM by human Overall Funniness, scoring 1.803, ahead of GPT-4.1 at 1.621 and Claude Sonnet 4 at 1.504. However, Gemini remains below the human Mid tier at 1.913 by 0.110, while exceeding the human Low tier at 1.232 by 0.571. The paper identifies Empathy as the main gap: human High responses score 2.615 on Empathy, compared with 2.053 for Gemini 2.5 Pro, 1.858 for GPT-4.1, and 1.830 for Claude Sonnet 4.

For evaluation, human–LLM agreement is weak. Overall Funniness Spearman correlations are 0.224 for GPT-4.1, 0.169 for Gemini 2.5 Pro, and 0.266 for Claude Sonnet 4. The accuracy for correctly ordering High, Mid, and Low human responses is only 50.9 %, 51.9 %, and 54.1 %, respectively. LLM judges also overrate Unrelated responses: humans give them 0.681 Overall Funniness, while GPT-4.1 gives 2.411, Gemini 2.5 Pro gives 3.291, and Claude Sonnet 4 gives 2.183.

## Takeaways
- Human-like humor generation requires more than novelty and relevance; the paper finds Empathy is a key missing dimension.
- LLM-as-judge is unreliable for Oogiri Overall Funniness, even with a detailed rubric.
- LLMs show positivity bias toward weak or irrelevant answers and self-preference toward LLM-generated answers.
- Builders of humor systems should evaluate multiple dimensions, not only aggregate funniness.

## Limitations & Caveats
The study is scoped to Japanese Oogiri and to 200 final topics. It evaluates only GPT-4.1, Gemini 2.5 Pro, and Claude Sonnet 4 with default generation settings. The authors also note that Bokete/Oogiri-GO vote counts may contain first-mover and conformity biases, motivating the inclusion of Oogiri-Chaya.
