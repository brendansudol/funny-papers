# One Joke to Rule them All? On the (Im)possibility of Generalizing Humor Detection

**Mor Turgeman, Chen Shani, Dafna Shahaf** — CHum 2026 · Guide entry #40 (Part 4 - Evaluation Methodology)

[paper page](https://aclanthology.org/2026.chum-1.1/) · [local PDF](../pdfs/40-one-joke-to-rule-them-all.pdf) · [full markdown](../md/40-one-joke-to-rule-them-all/40-one-joke-to-rule-them-all.md) · [extract](../extracts/40-one-joke-to-rule-them-all.json)

## TL;DR
This paper asks whether LLMs fine-tuned for one humor type can detect humor in new, unseen humor types. Across four short-form English text datasets, transfer is possible but asymmetric: Mistral reaches up to 75% accuracy on an unseen dataset, and Dad Jokes is the best source for transfer but the hardest target.

## Problem & Motivation
Computational humor research often splits humor into narrow tasks such as puns, sarcasm, cartoons, memes, or specific joke formats. The authors ask whether this fragmentation is necessary: if an LLM learns one kind of humor, does that competence transfer to another kind? This matters because new humor forms continually emerge online, and robust systems should capture transferable humor mechanisms rather than only dataset-specific cues.

## Approach
The paper evaluates transfer learning across four humor datasets using three setups. In single-dataset training, a model is fine-tuned on one dataset and tested on all four. In double-dataset training, it is trained on each pair of datasets and tested on all four. In triple-dataset training, it is trained on three datasets and evaluated on the held-out fourth. All training sets contain 5,000 balanced examples, so diversity changes without increasing total training size. The authors use instruction fine-tuning with LoRA for LLaMA-2-7B and Mistral-7B.

## Data & Experimental Setup
The datasets are Amazon Questions, One Liners, Sarcasm Headlines, and Reddit Dad Jokes. The original dataset sizes are 19K records for Amazon, 32K one-liner sentences, 28K headlines, and Reddit posts from r/dadjokes. For experiments, each dataset is downsampled to 6,250 balanced examples with an 80%/2%/18% train/validation/test split. Reddit Dad Jokes originally has only positive examples, so the authors use GPT-4 Turbo to minimally edit jokes into non-humorous versions; in a manual review of 3,000 outputs, 2.63% failed to maintain style or content, and no examples retained the punchline. Zero-shot accuracy for the base models is only 40% to 56%, supporting the need for fine-tuning.

## Results
Single-dataset training shows partial transfer. Mistral trained on Amazon reaches 75 accuracy on Headlines and 72 on One Liners, while training on Headlines transfers back to Amazon and One Liners at 65 and 62. Dad Jokes is highly asymmetric: training on it gives 68-71 transfer accuracy for Mistral, but models trained on other datasets reach only 51-62 on Dad Jokes. In double-dataset training, Amazon + Dad Jokes generalizes best, with Mistral scoring 74 on both held-out Headlines and One Liners. Triple-dataset training confirms Dad Jokes is hardest to transfer to, with average accuracy of 56%, while Headlines and One Liners average 70.5% and 71.5%. Increasing diversity improves transfer: LLaMA-2 gains 3.02 points from single to double training and 4.05 from single to triple; Mistral gains 2.02 and 1.88. In-domain performance drops only 0.49 points for Mistral and 1.76 for LLaMA-2 when in-domain data is reduced to 33%.

## Takeaways
- Humor transfer is real but uneven; success depends on source-target relations.
- Dad Jokes is the strongest transfer source, possibly because its generated negatives force models to identify humor rather than superficial style.
- More diverse humor training data generally helps, but most gains come from moving beyond one dataset.
- Mistral generalizes better than LLaMA-2, though both show similar transfer patterns.
- Builders of humor detectors should prioritize dataset diversity, not just in-domain size.

## Limitations & Caveats
The study covers only binary classification of short-form English text and excludes funniness ratings, explanations, dialogue, memes, videos, and other modalities. It uses only four datasets and two models. Dataset-to-humor-style mappings are approximate, and the GPT-generated Dad Jokes negatives may introduce artifacts shaped by a stronger LLM’s understanding of humor.
