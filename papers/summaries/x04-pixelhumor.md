# Humor in Pixels: Benchmarking Large Multimodal Models Understanding of Online Comics

**Yuriel Ryan, Rui Yang Tan, Kenny Tsu Wei Choo, Roy Ka-Wei Lee** — EMNLP Findings 2025 · Guide entry Part 3 (also in this section) (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2509.12248) · [local PDF](../pdfs/x04-pixelhumor.pdf) · [full markdown](../md/x04-pixelhumor/x04-pixelhumor.md) · [extract](../extracts/x04-pixelhumor.json) · [dataset: PixelHumor](../../data/pixelhumor/)

## TL;DR
PixelHumor is a benchmark of 2,800 annotated multi-panel online comics for testing LMM humor understanding across identification, classification, interpretation, and sequence recognition. The headline result is that models can say “this is humorous” almost perfectly, but fail on deeper reasoning: best panel sequencing accuracy is only 0.645, and human explanations are preferred in 48 (68.6%) of 70 samples.

## Problem & Motivation
The paper argues that humor comprehension requires social, contextual, linguistic, and visual reasoning, yet current Large Multimodal Models have not been systematically evaluated on multi-panel comic humor. Prior humor datasets often focus on text-only jokes, single images, memes, or caption ranking, and do not jointly test narrative order, modality attribution, and humor explanation. PixelHumor targets comics because their humor often depends on a setup, a punchline, and the interaction of visual and textual cues.

## Approach
The authors introduce PixelHumor and a four-task evaluation framework. Humor identification includes humor presence, sound-effect contribution, punchline panel, and whether text, visuals, or both drive the humor. Humor classification uses eight styles: Comparison, Personification, Exaggeration, Pun, Sarcasm, Silliness, Surprise, and Dark. Humor interpretation asks models to explain the joke in natural language. Sequence recognition asks models to reconstruct panel order and identify panel text.

## Data & Experimental Setup
PixelHumor contains 2,800 comics from Cyanide and Happiness, Peanuts, Garfield, XKCD, PhD Comics, They Can Talk, and Saturday Morning Breakfast Cereal. Eight undergraduate annotators aged 18 to 25 were trained over two weeks; comics were annotated in pairs, disagreements occurred in 15% of cases, and a third annotator resolved them by majority vote. Overall agreement was 0.872 and Krippendorff’s Alpha was 0.556. The dataset is primarily English and Western. The evaluated models are GPT-4o, Gemini-1.5-Pro, Qwen2-VL-72B, Gemma3-27B, LLaVA-OneVision-7B-SI, and Qwen2-VL-7B, all run zero-shot with temperature 0.

## Results
Humor presence is easy but misleading: Gemini-1.5-Pro, Qwen2-VL-72B, and Gemma3-27B reach F1 = 0.984, with only eight misclassified comics each, but only 33 comics are non-humorous. On harder identification subtasks, GPT-4o is best: sound-effect F1 = 0.821, panel contribution F1 = 0.765, and modality contribution F1 = 0.626; on modality contribution it beats Gemini-1.5-Pro by 0.013. Humor classification remains weak: GPT-4o leads with weighted F1 = 0.499, ahead of Gemini-1.5-Pro by 0.019 and Gemma3-27B by 0.034. For interpretation, GPT-4o has the best mean Likert score, 5.801, but human-written explanations are still chosen in 48 (68.6%) of 70 preference-study samples. For sequence recognition, Gemini-1.5-Pro has the best panel accuracy, 0.645, beating GPT-4o by 0.031; GPT-4o has the best text accuracy, 0.326, with WER = 0.230 and CER = 0.241.

## Takeaways
- Do not use binary humor presence alone as evidence of humor understanding; label imbalance can make the task look solved.
- Multi-panel sequencing and punchline localization are much harder than detecting that a comic is intended to be funny.
- GPT-4o and Gemini-1.5-Pro generally outperform open-source models, but even they rely on heuristics and struggle with longer narratives.
- Human explanations better integrate text and visuals than model explanations, which often become generic or hallucinated.
- Builders of humor systems need stronger cross-modal fusion and narrative tracking, not only better visual recognition.

## Limitations & Caveats
PixelHumor covers static image-text comics, not video, animation, or audio humor. It is primarily English and Western, so cross-cultural generalizability is limited. Humor is subjective despite training and guidelines, and copyright constraints mean the dataset is released as URLs and metadata rather than redistributed images.
