# HumorDB: Can AI understand graphical humor?

**Vedaant V Jain, Felipe dos Santos Alves Feitosa, Gabriel Kreiman** — ICCV 2025 · Guide entry #25 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2406.13564) · [local PDF](../pdfs/25-humordb.pdf) · [full markdown](../md/25-humordb/25-humordb.md) · [extract](../extracts/25-humordb.json) · [dataset: HumorDB](../../data/humordb/)

## TL;DR
HumorDB is a curated benchmark for purely visual, graphical humor, built around 3,542 images and 1,271 minimally contrastive funny/not-funny pairs. The paper finds that current models are above chance but still below humans on Binary and especially Comparison tasks; the best Range-task model is LLaVA(words fine-tuned), with RMSE 1.68 ± 0.28 on testAllSet and 1.66 ± 0.31 on testOnlyPairs.

## Problem & Motivation
The paper treats graphical humor as a test of scene understanding: a system must detect objects, relations, intentions, prior knowledge, and incongruities rather than merely label objects. Existing humor resources are described as often text-focused, multimodal rather than purely visual, insufficiently diverse, or lacking rigorous controls. HumorDB is designed to isolate the visual element that makes an image funny.

## Approach
The authors collected images through Google Search API scraping with manual curation and generated additional images using DALL-E and MidJourney. They removed explicit/offensive material and cases where humor relied on embedded text. The key design is a set of minimally contrastive pairs: an original humorous image and a modified version where the humor-inducing object or cue is removed or altered using Photoshop or AI inpainting. Both versions received subtle enhancements to reduce editing-artifact confounds.

## Data & Experimental Setup
The final dataset contains 3,542 images: 36% photos, 35% Photoshopped real-life photos, 14% cartoons, 5% sketches, and 10% AI-generated images. It is balanced into 1,771 funny and 1,771 not funny images, with train/validation/test splits of 2,136 / 703 / 706 images; testOnlyPairs contains 600 paired images. The main text reports 650 online participants; the appendix lists 850 initial participants before exclusions. Each final image received 6–8 Binary or Range ratings or 4–6 comparisons. Models evaluated include DINOv2 Large, ViT-Large/Huge, SwinV2-Large, ConvNeXt-Large, ViTG-14, ResNet152, BLIP, LLaVA, GPT-4o, and Gemini 1.5-002 Flash.

## Results
Human ratings confirmed that modifications reduced humor: originals were rated funnier than modified counterparts in 86.4% of pairs. Human self-reliability was 84.2 ± 13.3% for Binary repeats, rho = 0.89 for Range repeats, and 91.3 ± 14.8% for Comparison repeats. On Range, LLaVA(words fine-tuned) had the lowest RMSE: 1.68 ± 0.28 on testAllSet, 0.02 lower than LLaVA(fine-tuned) at 1.70 ± 0.22 and 0.08 lower than ViTG-14 at 1.76 ± 0.08. On testOnlyPairs it scored 1.66 ± 0.31, 0.03 lower than LLaVA(fine-tuned). Binary and Comparison accuracies are shown graphically; the text reports all models above 50% chance but below humans, with Comparison harder. On the external non-funny control set, not-funny classifications were ViT-G14 81%, LLaVA FT 80%, SwinV2 76%, ViTHuge 71%, and DinoV2 62%. Gemini explanations were rated best by humans: Why Funny 4.1 ± 0.6 and Accuracy 4.24 ± 0.47.

## Takeaways
- Minimal pairs are crucial: model performance drops on paired images, exposing reliance on superficial cues.
- Human keyword supervision helped: LLaVA(words fine-tuned) was the best Range-task model.
- Sketches remain difficult: Table 6 shows near-chance sketch performance, e.g. GPT-4o 50 and Gemini-Flash 53.
- Good classification is not the same as understanding: attention maps often missed the humor-critical region.

## Limitations & Caveats
The dataset could be larger, but expansion requires more editing, curation, and annotation. Humor is culturally dependent; participants were 54.0% from the United States and skewed younger. Majority votes and average ratings do not capture personalized humor preferences. Some internet images may have appeared in large-model training data, and the paper notes GPT-4o’s 10% original-only improvement as a warning sign.
