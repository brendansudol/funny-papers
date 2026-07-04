# Pun Unintended: LLMs and the Illusion of Humor Understanding

**Alessandro Zangari, Matteo Marcuzzo, Andrea Albarelli, Mohammad Taher Pilehvar, Jose Camacho-Collados** — EMNLP 2025 · Guide entry #4 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2509.12158) · [local PDF](../pdfs/04-pun-unintended.pdf) · [full markdown](../md/04-pun-unintended/04-pun-unintended.md) · [extract](../extracts/04-pun-unintended.json) · [dataset: PunEval + PunnyPattern + PunBreak + NAP](../../data/puneval/) · [dataset: SemEval-2017 Task 7 puns](../../data/semeval2017-task7-puns/)

## TL;DR
This paper tests whether strong LLM pun-detection scores reflect real understanding or surface shortcuts. It introduces/refines English pun datasets and shows that LLMs do well on standard benchmarks but fail badly when puns are subtly altered or non-puns retain familiar pun templates; the conclusion reports > 0.83 average accuracy on existing benchmarks but drops of −15% on PunnyPattern and −50% on PunBreak.

## Problem & Motivation
Puns rely on polysemy, phonetic similarity, and contextual support for two meanings. Prior work often used the SemEval pun dataset and focused on binary classification or free-text explanations, which can hide memorization, leakage, or shallow pattern matching. The authors ask whether recent LLMs can detect puns robustly and whether their explanations identify the actual pun mechanism.

## Approach
The paper evaluates seven instruction-tuned or reasoning LLMs: GPT-4o, Qwen2.5, Llama3.3, Gemini2.0, Mistral3, DeepSeek-R1, and DeepSeek-R1-Distill-Llama-70B, plus a fine-tuned RoBERTa-large baseline. Prompts range from zero-shot and few-shot yes/no detection to semi-structured rationales that require the pun word, alternative word, and optionally both senses. Explanation quality is measured automatically with Pun Pair Agreement (PPA), then manually analyzed for context, pun-pair, word-sense, and sense-similarity errors.

## Data & Experimental Setup
The authors create PunEval by correcting the Xu et al. refined SemEval data, yielding 2,589 samples split into 1,071 train, 1,341 test, and 177 validation samples. They also use the English JOKER subset with 632 puns and 632 single-word-substitution non-puns. NAP adds 128 newly collected puns and 128 rephrased non-puns. PunnyPattern contains 1,200 examples built around six frequent pun templates, with equal puns and non-puns. PunBreak contains 1,100 examples, including 200 original puns and 800 altered non-puns produced through homophone, random, pun-synonym, and alternative-synonym substitutions, plus 100 random non-pun controls.

## Results
On main detection, GPT-4o is strongest: 86.9 ± 0.8 F1 on NAP and 83.3 ± 0.4 on JOKER with the W prompt, and 93.0 ± 0.3 on PunEval with R+W+S. RoBERTa-large scores 92.5 ± 0.3 on PunEval but only 64.0 ± 0.1 on NAP and 65.7 ± 0.1 on JOKER, suggesting dataset artifacts. On PunnyPattern, average precision drops by 16-23% and F1 by 4-13%; GPT-4o reaches F1 83.1 with precision 79.7 and recall 88.1. PunBreak is much harder: GPT-4o with W gets only 32.5 ± 2.3 accuracy on homophone substitutions and 37.3 ± 4.1 on pun-word synonyms, while still scoring 99.0 ± 0.0 on random-sentence controls. For rationales, GPT-4o averages around 1.5/2 PPA, while R1 reaches 1.7 on PunEval W+S. Manual analysis finds R1 has the fewest errors: 87 total, versus 111 for Llama3.3 and 128 for GPT-4o.

## Takeaways
- High pun-detection scores can be inflated by recurring templates and dataset structure.
- Robust humor evaluation needs adversarial non-puns that preserve surface cues.
- Asking for rationales can improve detection, but correct labels can still come from wrong reasoning.
- Builders should test context support and phonetic/orthographic fit, not just binary humor labels.

## Limitations & Caveats
The new datasets were not comprehensively validated by language experts, and pun perception is subjective. Some examples may be contaminated through online exposure or contain accidental puns. The study is English-only, and prompts were not optimized separately for each model.
