# D-HUMOR: Dark Humor Understanding via Multimodal Open-ended Reasoning - A Benchmark Dataset and Method

**Sai Kartheek Reddy Kasu, Mohammad Zia Ur Rehman, Shahid Shafi Dar, Rishi Bharat Junghare, Dhanvin Sanjay Namboodiri, Nagendra Kumar** — ICDM 2025 · Guide entry Part 6 (dark-humor resource) (Part 6 - Safety, Harm & Boundaries)

[paper page](https://arxiv.org/abs/2509.06771) · [local PDF](../pdfs/x29-d-humor.pdf) · [full markdown](../md/x29-d-humor/x29-d-humor.md) · [extract](../extracts/x29-d-humor.json)

## TL;DR
The paper introduces D-HUMOR, a benchmark of 4,379 Reddit memes annotated for dark humor, target category, and three-level intensity. It also proposes a reasoning-augmented multimodal model, TCRNet, that fuses OCR text, image features, and self-refined VLM explanations. The strongest result is that TCRNet reaches 75.00% dark humor detection accuracy and 62.72% intensity prediction accuracy, with ablations showing that removing reasoning sharply hurts performance.

## Problem & Motivation
Dark humor in memes is hard to model because the joke often depends on sensitive topics, implicit social context, and the interaction between image and text. The paper argues that existing work mostly studies related styles such as sarcasm, irony, satire, or cynicism separately, while dark humor can combine them in a single instance. The authors state that, to the best of their knowledge, there was no multimodal dark humor dataset, limiting work on content moderation and multimodal humor understanding.

## Approach
The method first uses Qwen-2.5-7B to generate a structured explanation for each meme with six fields: Meme Summary, Implied Joke, Narrative Structure, Emotional Effect, Dark Attributes, and Target. A Role-Reversal Self-Loop then prompts the model to act as the meme’s original author and critique/refine the explanation for a maximum of 5 epochs; the paper says explanations typically stabilize by approximately 3 epochs.

For classification, the system encodes OCR text with BERT, reasoning with S-BERT, and images with ViT. TCRNet applies pairwise scaled dot-product attention across text-image, text-reasoning, and image-reasoning streams, average-pools the attended outputs, concatenates them into a 2,304-dimensional vector, and predicts dark humor presence, target, and intensity.

## Data & Experimental Setup
All memes were collected from Reddit via the Reddit API, with OCR used to extract embedded text. After manual duplicate removal, the corpus contains 4,379 multimodal memes. The train/test split is 3,503/876 memes. In training, 1,577 are dark humor and 1,926 are non-dark humor; in testing, 397 are dark humor and 479 are non-dark humor.

Dark humor memes are further labeled for target: Gender/Sex-Related Topics, Mental Health, Disability, Race/Ethnicity, Violence/Death, and Other. Intensity is Mild (1), Moderate (2), or Severe (3). Annotation used three trained undergraduate annotators, expert supervision, a 100-meme gold seed set, and final adjudication. Fleiss’ Kappa was 70.29 for dark humor, 72.13 for target, and 58.57 for intensity.

## Results
TCRNet is best for dark humor detection, with 75.00% Accuracy, 73.55 Macro-F1, and 74.13 Weighted-F1. The next-best dark humor accuracy is Llama-3.2-3b-it with OCR Text + Structured Explanation at 73.39%.

For target identification, the best system is Distil-BERT with OCR Text + Structured Explanation: 66.41 Accuracy, 62.53 Macro-F1, and 66.07 Weighted-F1. This improves over OCR-only Distil-BERT target Macro-F1 from 55.98 to 62.53.

For intensity prediction, TCRNet is best with 62.72 Accuracy, 49.71 Macro-F1, 60.74 Weighted-F1, and 38.63 Pearson correlation. Removing explanations from TCRNet drops Target Identification Macro-F1 from 60.54 to 35.11 and Dark Humor Weighted-F1 from 74.13 to 67.31.

## Takeaways
- Structured explanations add useful context beyond raw OCR text, especially for target and intensity.
- Image-only models underperform text-only models, but multimodal fusion with reasoning performs best overall.
- Zero-shot VLMs are not enough for this benchmark without task-specific adaptation.
- Builders of humor systems should evaluate not only humor presence but also target and severity for sensitive content.

## Limitations & Caveats
The authors state that the dataset is skewed toward Gender/Sex-Related Topics. They also note that distinguishing clean humor from dark humor can never be fully objective. The dataset contains offensive material, is intended only for academic research, and access requires a data usage agreement.
