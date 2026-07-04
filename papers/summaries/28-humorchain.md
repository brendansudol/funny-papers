# HUMORCHAIN: Theory-Guided Multi-Stage Reasoning for Interpretable Multimodal Humor Generation

**Jiajun Zhang, Shijia Luo, Ruikang Zhang, Qi Su** — CVPR 2026 · Guide entry #28 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2511.21732) · [local PDF](../pdfs/28-humorchain.pdf) · [full markdown](../md/28-humorchain/28-humorchain.md) · [extract](../extracts/28-humorchain.json)

## TL;DR
HUMORCHAIN is a theory-guided, multi-stage framework for generating humorous English image captions. It uses GPT-5-2025-08-07 for staged reasoning and a fine-tuned Qwen3-VL-4B-Instruct discriminator for generate–evaluate–revise feedback. Its strongest reported result is a human Humor Mean of 0.810, far above the next listed baseline value of 0.418.

## Problem & Motivation
The paper argues that current multimodal captioning systems can describe images fluently but often fail to produce captions with genuine humorous effect. The authors frame multimodal humor as requiring visual cue recognition, incongruity detection, social safety, and affective response. Their goal is to make humorous image captioning more interpretable and controllable by explicitly embedding humor and psychology theories into the generation process rather than relying only on data-driven prompting.

## Approach
HUMORCHAIN decomposes captioning into stages. First, the system describes the image: main subjects, states or emotions, scene, actions, readable text, and significant details. Second, it judges plausibility, whether there is humorous incongruity, and whether humans, animals, or cartoon characters are present. Third, it selects one of four strategies: Absurdity, Contrast_irony, Emotion_analogy, or Object_analogy. These are mapped to Incongruity–Resolution, Benign Violation, Superiority, and Relief theories. A safety classifier checks for group attacks, personal attacks, hate speech, and humiliation. A Qwen3-VL-4B-Instruct humor discriminator fine-tuned with LoRA and a classifier head then accepts or rejects the caption; rejected captions trigger rewriting, with a 5-retry limit and fallback to the top-rated candidate.

## Data & Experimental Setup
Internal comparisons A–F use Meme-Image-No-Text. External comparisons use Oogiri-GO for CLoT and OxfordTVG-HIC for existing humorous captions; OxfordTVG-HIC is described as containing 2.9 million image-text pairs with humor ratings and emotional annotations. The authors also introduce a human-annotated humor preference dataset of 5,320 image–caption pairs: 2,511 positive and 2,809 negative. Its training split has 5,054 samples, and validation has 266 samples. Human evaluation includes pairwise comparisons and binary single-title labels. Automatic metrics include Distinct-1/2, CLIPScore, BERT Cross Score, EA-Rev, and GM-Rev.

## Results
In pairwise evaluation, HUMORCHAIN beat zero-shot A with 0.695 vs 0.305 and beat Few-shot + CoT + Rule-Guided F with 0.680 vs 0.320. Against external systems, it beat CLoT on Oogiri-GO with 0.683 vs 0.317 over 794 comparisons and OxfordTVG-HIC captions with 0.860 vs 0.140 over 1007 comparisons. Global ranking also favored HUMORCHAIN: Elo 1554.60 and BT 3.57, ahead of F at Elo 1528.84 and BT 1.00. In single-title evaluation, HUMORCHAIN reached Humor Mean 0.810; the listed baselines range from 0.195 for CLoT to 0.418 for Few-shot. The discriminator improved precision from Baseline 0.523 to LoRA 0.636 and LoRA + Classifier 0.670. In the full pipeline, humorous outputs rose from 45.1% to 67.0%, with Acceptance Rate 36.5% and Avg. Generations per Accepted Caption 2.74×.

## Takeaways
- Explicit staged reasoning outperformed merely adding few-shot examples, rules, or CoT.
- The discriminator mattered: HUMORCHAIN beat its no-discriminator ablation J with 0.745 vs 0.255.
- Larger closed-source LLMs were poor humor filters in this setup, with precision 0.465, 0.474, and 0.460.
- Builders of humor systems should evaluate with human preference and not rely only on caption fluency or generic multimodal ability.

## Limitations & Caveats
The paper states that its theory coverage is incomplete and may miss culturally embedded irony or reference-dependent jokes. Humor labels reflect majority preference rather than individual taste. Failure cases come from inadequate image descriptions and images with weak or absent humor-linked incongruity.
