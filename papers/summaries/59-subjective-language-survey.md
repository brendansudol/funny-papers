# Large Language Models for Subjective Language Understanding: A Survey

**Changhao Song, Yazhou Zhang, Hui Gao, Ben Yao, Peng Zhang** — arXiv:2508.07959 · Guide entry #59 (Part 9 - Surveys & Resources)

[paper page](https://arxiv.org/abs/2508.07959) · [local PDF](../pdfs/59-subjective-language-survey.pdf) · [full markdown](../md/59-subjective-language-survey/59-subjective-language-survey.md) · [extract](../extracts/59-subjective-language-survey.json)

## TL;DR
This survey defines “subjective language understanding” as LLM-based interpretation of language that expresses feelings, opinions, figurative meaning, intent, or aesthetic judgment. It covers eight tasks and synthesizes “over 200 recent papers”; its central conclusion is that LLMs help through prompting, world knowledge, explanations, and multimodality, but sarcasm, humor, metaphor, and aesthetics remain especially difficult.

## Problem & Motivation
Human communication is full of sentiment, emotion, sarcasm, humor, metaphor, stance, intent, and aesthetic preference. These phenomena are not reducible to literal facts: they depend on context, speaker intent, culture, shared knowledge, and sometimes theory-of-mind-style inference. The survey argues that older task-specific NLP systems handled these phenomena separately and generalized poorly, while LLMs offer a possible unified route through in-context learning, instruction following, broad pretraining knowledge, and natural-language reasoning.

## Approach
The paper is a literature survey, not a new benchmark or model paper. It first defines subjective language from linguistic and cognitive perspectives, then reviews LLM foundations and current prompting, supervised fine-tuning, and reasoning-based approaches. It surveys task definitions, datasets, methods, and open challenges for eight areas: sentiment analysis, emotion recognition, sarcasm detection, humor detection, stance detection, metaphor recognition, intent detection, and aesthetics identification. It also compares tasks and argues for unified, multi-task subjective-language modeling.

## Data & Experimental Setup
There is no original experimental setup. Instead, the paper catalogs many resources. Examples include IMDb with “50k balanced reviews,” Sentiment140 with “1.6M tweets,” Twitter US Airline Sentiment with “14,160 tweets,” GoEmotions as a “58k-comment Reddit corpus,” and EmpatheticDialogues with “32 emotions.” For humor and related figurative language, it discusses resources such as Kaggle short jokes, Pun of the Day, rJokes corpus, UR-FUNNY, Humicroedit + FunLines (SemEval-2020 Task 7), HaHackathon (SemEval-2021 Task 7), CHumor 1.0, Chumor 2.0, HumorBench, HumorDB, MHSDB, and YesBut. For metaphor, it highlights VUA/VUAMC, TroFi with “3k sentences for 50 target verbs,” MOH-X with “647 verb instances,” MUNCH with “over 10,000” apt and “1,500” inapt paraphrases, and CMDAG with “28K” Chinese literary sentences.

## Results
Because the paper is a survey, it does not report new accuracy, F1, or win-rate results of its own, and it does not provide exact margins for most cross-paper comparisons. Its quantitative claims are mainly scope and resource facts: it reviews “over 200 recent papers,” covers “eight” tasks, and situates LLMs such as GPT-3 at “175B” parameters, PaLM at “540B,” and Megatron-Turing NLG at “530B.” The comparative findings are qualitative: GPT-4 is described as strongest among LLMs in some sarcasm benchmarks but still behind supervised PLMs; Chumor studies find SOTA LLMs only slightly above chance; HumorDB finds vision-language models above chance but below humans.

## Takeaways
- Treat humor, sarcasm, metaphor, and aesthetics as stress tests for real subjective understanding, not solved classification problems.
- Prompting is useful for quick baselines, but task-aligned fine-tuning, retrieval, structured reasoning, and multimodal fusion are often needed for robustness.
- Humor systems need culturally grounded and context-rich evaluation, including funniness, offensiveness, appropriateness, and explanation quality.
- Unified subjective-language models are promising, but require multi-task data and careful handling of negative transfer.

## Limitations & Caveats
The paper itself does not run experiments, so its claims depend on the comparability and reliability of surveyed work. It repeatedly notes open problems: ambiguous labels, cultural variation, dataset bias, privacy, safety, hallucinated explanations, computational cost, and lack of standardized benchmarks that evaluate both the “what” and the “why” of subjective judgments.
