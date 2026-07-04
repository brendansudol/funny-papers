# ExPUNations: Augmenting Puns with Keywords and Explanations

**Jiao Sun, Anjali Narayan-Chen, Shereen Oraby, Alessandra Cervone, Tagyoung Chung, Jing Huang, Yang Liu, Nanyun Peng** — EMNLP 2022 · Guide entry #7 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2210.13513) · [local PDF](../pdfs/07-expunations.pdf) · [full markdown](../md/07-expunations/07-expunations.md) · [extract](../extracts/07-expunations.json) · [dataset: ExPUNations (ExPun)](../../data/expunations/) · [dataset: SemEval-2017 Task 7 puns](../../data/semeval2017-task7-puns/)

## TL;DR
This paper introduces ExPUN, an augmentation of SemEval 2017 Task 7 puns with human annotations for funniness, joke keywords, and natural-language explanations. Its clearest quantitative result is in generation: T5PT+FT trained with ExPUN human keywords reaches a 77.0% human-rated pun success rate, higher than AmbiPun's 51.0% despite AmbiPun's stronger word incorporation.

## Problem & Motivation
Existing humor datasets often give only sparse binary labels such as joke/not-joke or pun/not-pun. The authors argue that this is not enough to test whether models understand why something is funny or can generate novel humor. Puns are a difficult test case because they depend on lexical-semantic ambiguity, phonological similarity, commonsense knowledge, and subjective human judgments.

## Approach
The paper builds ExPUN by adding six annotation fields to samples from SemEval 2017 Task 7: whether the text is understandable, offensive/inappropriate, intended as a joke, a 1-5 funniness rating, a concise natural-language explanation, and sparse joke keyword phrases copied from the text. It then proposes two tasks enabled by these annotations: pun explanation, evaluated through explanation-augmented joke classification, and keyword-conditioned pun generation, where a model must generate a new pun from keywords, a pun word, an alternate pun word, and optionally word-sense annotations.

## Data & Experimental Setup
The dataset contains 1,999 sampled texts: 834 heterographic puns, 1,074 homographic puns, and 91 non-puns. A team of 10 full-time annotators produced 5 annotations per sample after pilot calibration. ExPUN contains 6,650 explanations, averaging 3.33 explanations per sample, 31.67 tokens per explanation, and 2.01 sentences per explanation. For pun classification, the split is 1,699/100/200 train/dev/test; train contains 1,299 jokes and 400 non-jokes. For keyword-conditioned generation, the paper uses 1,482 samples with both ExPUN keywords and SemEval pun-sense annotations, reserving 100 for test. Models include BERT-base, RoBERTa-base, DeBERTa-base, T5-base, ELV, AmbiPun, T5FT, and T5PT+FT.

## Results
Annotation agreement reflects the subjectivity of humor. Joke intent has κ = 0.58 and ρ = 0.32; funniness has κ = 0.41 and ρ = 0.30. Textual keyword annotations agree much more than explanations: keywords score BLEU 0.58 and METEOR 0.74, while explanations score BLEU 0.18 and METEOR 0.30. In classification, the paper reports that gold explanations improve accuracy, sampled negative explanations improve it further, generated explanations do not help at test time, and ELV improves accuracy but often produces non-fluent explanations. In generation, ExPUN-keyword T5PT+FT achieves 77.0% success with word incorporation p_w = 93.0, K = 80.2, both = 83.5. AmbiPun has better incorporation with ExPUN keywords—99.0, 92.1, and 94.4—but only 51.0% success. T5PT+FT also benefits from human keywords: 77.0% success with ExPUN keywords versus 54.0% with RAKE keywords.

## Takeaways
- Human-written explanations can help humor classification, but current generated explanations are not yet good enough to provide the same benefit.
- Sparse human-selected keywords are useful control inputs for pun generation and outperform automatically extracted RAKE keywords in human success rate.
- Word incorporation is not sufficient: AmbiPun copies/incorporates inputs well but is less successful as judged by humans.
- Evaluation of humor systems should include human judgments, not only lexical or incorporation metrics.

## Limitations & Caveats
The work covers only puns, not humor broadly. Humor judgments remain subjective. The authors note that pretrained generation models may produce biased or sensitive content, and this framework does not yet explicitly address that risk.
