# “A good pun is its own reword”: Can Large Language Models Understand Puns?

**Zhijun Xu, Siyu Yuan, Lingjie Chen, Deqing Yang** — EMNLP 2024 · Guide entry #6 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://aclanthology.org/2024.emnlp-main.657/) · [local PDF](../pdfs/06-good-pun-own-reword.pdf) · [full markdown](../md/06-good-pun-own-reword/06-good-pun-own-reword.md) · [extract](../extracts/06-good-pun-own-reword.json) · [dataset: SemEval-2017 Task 7 puns](../../data/semeval2017-task7-puns/)

## TL;DR
This paper systematically evaluates eight LLMs on English pun recognition, pun explanation, and pun generation using homographic and heterographic puns. GPT-4-Turbo and Claude-3-Opus are strong in recognition and explanation, but generated puns remain less successful and less funny than human puns; GPT-4-Turbo’s constrained homographic generation reaches Success 0.670 versus Human pun 0.860.

## Problem & Motivation
Puns are a controlled form of linguistic humor because they rely on double meanings of the same word or similar-sounding words. Prior work trained task-specific models for recognizing, explaining, or generating puns, but the paper argues that LLM pun understanding had not been systematically evaluated. The authors focus on whether LLMs can detect puns, explain the underlying wordplay, and create new puns rather than merely producing plausible joke-like text.

## Approach
The evaluation covers three tasks. Pun recognition asks models to classify text as pun or non-pun, using paired prompts biased toward either “pun” or “non-pun” to test confidence and consistency. Pun explanation uses Chain-of-Thought-style responses and checks whether explanations mention the pun word, alternative word, pun sense, and alternative sense. Pun generation is tested in two modes: free generation from the pun pair alone and constrained generation from the pun pair plus contextual words. The authors add Overlap to estimate copying from human puns and define Strict Success as successful generation with overlap < 0.5.

## Data & Experimental Setup
The dataset combines SemEval-2017 Task 7 puns with ExPUNations (ExPun), filtered so each pun has text, pun pair, human explanation, and keyword set. The Hom-Dataset has 10 hom-pun examples, 10 non-pun examples, 810 hom-pun test items, and 633 non-pun test items. The Het-Dataset has 10 het-pun examples, 10 non-pun examples, 647 het-pun test items, and 499 non-pun test items. The evaluated models are Llama2-7B-Chat, Vicuna-7B, Mistral-7B, OpenChat-7B, Gemini-Pro, GPT-3.5-Turbo, Claude-3-Opus, and GPT-4-Turbo. Human evaluation uses three trained English-major undergraduates; punchline-check agreement is Fleiss’s κ = 0.87. GPT-4 is also used for pairwise explanation comparison and reaches 88.3% consistency with annotators on sampled data.

## Results
For enhanced-prompt recognition, GPT-4-Turbo is best: on homographic puns it gets TPR 0.988, TNR 0.758, and κ 0.962; on heterographic puns it gets TPR 0.961, TNR 0.796, and κ 0.959. Prompt definitions and examples improve consistency and non-pun recognition, although TNR stays lower than TPR.

In punchline checks, GPT-4-Turbo scores 0.98 / 0.98 / 0.96 / 0.93 on homographic w_p / w_a / S_p / S_a, compared with Human 0.95 / 0.95 / 0.95 / 0.95. For heterographic puns, GPT-4-Turbo scores 0.96 / 0.90 / 0.93 / 0.85, below Human 0.97 / 0.97 / 0.94 / 0.93 on the hidden alternative word and sense.

For constrained generation, GPT-4-Turbo reaches homographic Success 0.670 and Funny 2.584, below Human 0.860 and 3.268. On heterographic generation, Claude-3-Opus reaches Success 0.610 and Funny 2.348; GPT-4-Turbo gets Success 0.600 and Funny 2.348; Human puns score 0.840 and 3.229.

## Takeaways
- Recognition is easier than explanation or generation, but prompt bias can substantially change outputs.
- Heterographic puns are especially hard because the alternative word is absent and must be recovered phonetically.
- Contextual words help LLMs generate better puns, but they also increase copying risk.
- Builders should explicitly discourage “lazy pun generation,” where models use both words separately instead of fusing meanings.

## Limitations & Caveats
The evaluation is English-only. Overlap is only a rough originality measure because LLM training data are not public. Human humor judgments are subjective, and the authors note that public pun datasets may contain socially harmful or toxic language.
