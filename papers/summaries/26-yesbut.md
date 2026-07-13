# YesBut: A High-Quality Annotated Multimodal Dataset for evaluating Satire Comprehension capability of Vision-Language Models

**Abhilash Nandy, Yash Agarwal, Ashish Patwa, Millon Madhur Das, Aman Bansal, Ankit Raj, Pawan Goyal, Niloy Ganguly** — EMNLP 2024 · Guide entry #26 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2409.13592) · [local PDF](../pdfs/26-yesbut.pdf) · [full markdown](../md/26-yesbut/26-yesbut.md) · [extract](../extracts/26-yesbut.json) · [dataset: YesBut-Satire (Nandy et al.)](../../data/yesbut/)

## TL;DR
The paper introduces YesBut, a multimodal satire benchmark built from two-panel Yes/But images and augmented with DALL-E 3-generated stick-figure variants. Five VL models—LLaVA, Kosmos-2, MiniGPT4, GPT4, and Gemini—perform poorly in zero-shot settings: best detection accuracy is 56.97, best detection F1 is 59.71, and best completion accuracy is 61.81.

## Problem & Motivation
The authors ask whether current Vision-Language Models can understand satire in images, not just recognize objects or answer standard visual questions. YesBut images contain two sub-images: a normal scenario and a conflicting, ironic, or funny scenario. The task often requires reading any embedded text, recognizing objects, relating the two halves, and using commonsense knowledge to infer the punchline.

## Approach
The paper proposes three tasks. Satirical Image Detection asks the model to output whether a full image is satirical. Satirical Image Understanding asks the model to describe sub-images and answer why the image is funny or satirical. Satirical Image Completion gives one half of an image and two candidate halves, requiring the model to choose the option that makes the pair satirical.

## Data & Experimental Setup
YesBut contains 2,547 images: 1,084 satirical and 1,463 non-satirical. The pipeline starts with 283 satirical images manually downloaded from the X handle @_yesbut_ with consent. Five annotators write left, right, and overall descriptions, plus metadata. DALL-E 3 then generates 2D and 3D stick-figure sub-images from those descriptions; a graduate student labels generated combinations, adding 302 satirical and 547 non-satirical images in Stage 3 and 499 satirical and 916 non-satirical images in Stage 4. The authors evaluate LLaVA, Kosmos-2, MiniGPT4, gpt-4-vision-preview, and Gemini Pro Vision in zero-shot and zero-shot CoT settings. Understanding is scored with BLEU, ROUGE-L, METEOR, BERTScore, Polos, and a 30-image human evaluation by 3 lab students.

## Results
Detection remains weak: Kosmos-2 zero-shot CoT has the best test accuracy, 56.97, while Kosmos-2 zero-shot has the best F1 Score, 59.71. CoT improves detection accuracy for only 2/5 models and F1 for only 1/5. For understanding with the WHYFUNNY prompt, Gemini is best by Average Score at Stage 2, Stage 3, and Stage 4, with 0.3227, 0.321, and 0.3227. Human evaluation shows the best model still trails human-written descriptions by 40, 43.33, 33.33, and 36.66 points on Correctness, Appropriate Length, Visual Completeness, and Faithfulness. Completion is also difficult: Gemini is best with 61.11 in zero-shot and 61.81 in zero-shot CoT. On 119 real satirical photographs, GPT4 is best with 93.27 detection accuracy and 46.22 understanding accuracy; all models score below 50% on understanding.

## Takeaways
- YesBut is designed to test satire comprehension, not merely captioning or object recognition.
- Mixed artistic styles, absent text, and two-panel visual relations make the benchmark hard for current VL models.
- Automatic metrics and human evaluation agree that model explanations often miss the satirical point.
- CoT is not a reliable fix: it helps some completion results but not detection overall.

## Limitations & Caveats
The authors note that satire annotation is subjective because it depends on background knowledge. The work is English-only. Reporting gaps include missing API inference dates, decoding settings, exact open-source checkpoints, blind-status details, and decontamination checks for public social-media source images.
