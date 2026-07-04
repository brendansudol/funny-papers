# Harm or Humor: A Multimodal, Multilingual Benchmark for Overt and Covert Harmful Humor

**Ahmed Sharshar, Hosam Elgendy, Yasser Rohaim, Saad El Dine Ahmed, Yuxia Wang** — arXiv:2603.17759 · Guide entry #48 (Part 6 - Safety, Harm & Boundaries)

[paper page](https://arxiv.org/abs/2603.17759) · [local PDF](../pdfs/48-harm-or-humor.pdf) · [full markdown](../md/48-harm-or-humor/48-harm-or-humor.md) · [extract](../extracts/48-harm-or-humor.json)

## TL;DR
The paper introduces Harm or Humor, a manually curated benchmark for detecting harmful humor across 3,000 text jokes, 6,005 image memes, and 1,202 video clips in English, Arabic, and universal language-independent settings. The central result is that closed-source models lead, but all systems struggle with implicit, culturally grounded harm, especially in Arabic.

## Problem & Motivation
Dark humor can hide harmful meanings behind jokes, memes, or videos, making safety evaluation harder than ordinary toxicity detection. The authors argue that prior benchmarks are biased toward text or static media, mostly English, and rarely label implicit harm that requires cultural or semantic reasoning. Their goal is to test whether current LLMs, VLMs, and video LLMs understand when a joke crosses from safe humor into harmful humor, including covert cases where the offensive meaning is not on the surface.

## Approach
The benchmark labels every item as Safe or Harmful. Harmful items are further divided into Explicit, where toxicity is overt, and Implicit, where harm requires semantic inference or cultural context. Seven volunteer annotators labeled the full dataset independently, and majority vote produced the gold labels. The authors evaluate models with one prompt per modality and frame the model task as binary Harmful vs. Safe classification. They report Accuracy, Macro-F1, and recall for the Implicit and Explicit harmful subsets.

## Data & Experimental Setup
The dataset contains 3,000 text jokes: 2,000 English and 1,000 Arabic. It contains 6,005 images: 3,701 English and 2,304 Arabic. It also contains 1,202 videos: 317 Arabic, 533 English, and 352 Universal, with mean duration 14 seconds and range 6s–62s. Sources include public online repositories, forums, Reddit/X material, Wikimedia Commons, Vimeo, MemeDroid, and D-HUMOR. Inter-annotator agreement was high but lower for video: Harmful/Safe κ was 0.87 for text, 0.84 for images, and 0.81 for videos; Explicit/Implicit κ was 0.81, 0.78, and 0.74.

## Results
On text, GPT-5.2 was best: English Acc 90.3 and F1 90.2; Arabic Acc 83.4 and F1 83.1. It beat Gemini 2.5 Pro on English text F1 by 5.7 points and on Arabic text F1 by 1.3 points. On images, GPT-5.2 led English with Acc 74.7 and F1 72.0, while Gemini 2.5 Pro led Arabic with Acc 70.2 and F1 70.1. The English image implicit/explicit gap was large for GPT-5.2: Imp 49.7 vs Exp 88.5. On videos, GPT-5 Pro had the best overall Acc 69.4 and F1 80.2, only 0.7 F1 ahead of Gemini 2.5 Pro at 79.5. Gemini 2.5 Pro had the best Arabic and English video F1 scores, 78.4 and 85.2, and the highest Imp and Exp recalls, 66.7 and 76.1. The best open-source video model, Qwen2.5-Omni, reached F1 60.5, trailing GPT-5 Pro by 19.7 points.

## Takeaways
- Harmful-humor evaluation should separate explicit toxicity from implicit harm; models often miss the latter.
- Arabic humor exposes major gaps in dialectal, OCR, and culturally grounded reasoning.
- Accuracy alone can hide dangerous failures because some open-source VLMs predict “safe” while missing harmful cases.
- Closed-source models currently dominate, especially for multimodal and video safety evaluation.
- Older or more engineered models may outperform newer releases on corner cases: Gemini 2.5 Pro consistently beat Gemini 3 Pro here.

## Limitations & Caveats
The benchmark covers only English, Arabic, and universal visual content, and the Arabic subset is smaller than the English subset. Humor judgments remain subjective despite guidelines and majority voting. The dataset lacks fine-grained harm-type labels, limiting diagnostic analysis by racism, violence, sexual content, religion, disability, or related categories. Video evaluation depends heavily on proprietary systems because open-source models still struggle to integrate visual, temporal, OCR, and audio cues.
