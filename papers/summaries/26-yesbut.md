# YesBut: A High-Quality Annotated Multimodal Dataset for evaluating Satire Comprehension capability of Vision-Language Models

**Abhilash Nandy, Yash Agarwal, Ashish Patwa, Millon Madhur Das, Aman Bansal, Ankit Raj, Pawan Goyal, Niloy Ganguly** — EMNLP 2024 · Guide entry #26 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2409.13592) · [local PDF](../pdfs/26-yesbut.pdf) · [full markdown](../md/26-yesbut/26-yesbut.md) · [extract](../extracts/26-yesbut.json) · [dataset: YesBut (V1)](../../data/yesbut/) · [dataset: YesBut V2](../../data/yesbut-v2/)

## TL;DR
The paper introduces YesBut, a multimodal benchmark for satire comprehension in two-panel images, and evaluates five vision-language models on detection, explanation, and completion tasks. The central result is that current models remain weak: no model exceeds 60 on detection accuracy or F1, and the best completion accuracy is only 61.81.

## Problem & Motivation
The authors study whether VL models can understand satirical images that combine a normal scenario with a conflicting or ironic scenario. This requires recognizing objects and text, relating entities across two sub-images, and using commonsense and social reasoning. The paper argues that prior multimodal humor and satire work has not simultaneously evaluated detection, understanding, and comprehension of satirical situations in images.

## Approach
YesBut is built through a four-stage pipeline. The authors first manually collect 283 satirical images from the X handle @_yesbut_ with consent. Five annotators then write a left-sub-image description, right-sub-image description, and overall punchline description, and label features such as text presence, whether sub-images are connected, and annotation difficulty. To expand style diversity, the authors use DALL-E 3 to generate 2D stick-figure and 3D stick-figure sub-images from the annotated descriptions, combine generated and original sub-images, and manually label the resulting images as satirical or non-satirical.

The benchmark defines three tasks: Satirical Image Detection, a binary classification over all images; Satirical Image Understanding, where models describe sub-images and answer “Why is this image funny/satirical?”; and Satirical Image Completion, where a model selects one of two candidate sub-images to complete a funny or satirical pair.

## Data & Experimental Setup
The final YesBut dataset has 2,547 images: 1,084 satirical and 1,463 non-satirical. It spans colorized sketches, 2D stick figures, and 3D stick figures. Compared with MemeCap and MET-Meme, YesBut has 53% images without content text, 100% images with sub-images, and 88.89% with multiple artistic styles. The authors evaluate LLaVA, Kosmos-2, MiniGPT4, GPT4 using `gpt-4-vision-preview`, and Gemini Pro Vision. Detection and completion use zero-shot and zero-shot CoT prompts; understanding uses zero-shot generation. The authors avoid in-context learning to test models without exemplar support.

## Results
For detection, Kosmos-2 with zero-shot CoT has the best TEST ACC. at 56.97, while Kosmos-2 zero-shot has the best F1 SCORE at 59.71. GPT4 zero-shot is next-best on detection accuracy at 55.44, so the top accuracy margin is 1.53 points. CoT improves detection accuracy in only 2/5 models and F1 in only 1/5 models.

For understanding, all normalized average metric values are below 0.4. On the WHYFUNNY prompt, Gemini reaches the best Average Score reported in Table 6, 0.3227. Human evaluation shows a large gap: best model scores are 60.00 for Correctness, 56.67 for Appropriate Length, 46.67 for Visual Completeness, and 56.67 for Faithfulness, versus human scores of 100.00, 100.00, 80.00, and 93.33.

For completion, Gemini is best with 61.11 zero-shot accuracy and 61.81 zero-shot CoT accuracy. On 119 real satirical photographs, GPT4 leads with Detection 93.27 and Understanding 46.22, but every model stays below 50% on Understanding.

## Takeaways
- YesBut stresses visual-social reasoning rather than only text-based humor recognition.
- Multiple styles and missing text make the benchmark hard for current VL models.
- Zero-shot CoT is not reliably helpful for satire detection.
- Automatic and human evaluations both show substantial room for improvement in satire explanation.

## Limitations & Caveats
The authors note that annotations involve background knowledge and remain subjective despite manual review. The work is English-only, and the authors plan to extend it to other languages.
