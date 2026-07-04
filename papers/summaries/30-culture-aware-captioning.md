# Culture-Aware Humorous Captioning: Multimodal Humor Generation across Cultural Contexts

**Run Xu, Lu Li, Rongzhao Zhang, Jie Xu** — arXiv:2604.18091 · Guide entry #30 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2604.18091) · [local PDF](../pdfs/30-culture-aware-captioning.pdf) · [full markdown](../md/30-culture-aware-captioning/30-culture-aware-captioning.md) · [extract](../extracts/30-culture-aware-captioning.json)

## TL;DR
This paper defines culture-aware humorous captioning: generating a short funny caption from an image while conditioning on an explicit Eastern or Western cultural context. Its main technical result is that CuHAlign achieves the best Contextual Fit scores in both settings, raising Qwen3-VL-8B-Instruct from 5.49 to 6.63 in Western context and from 5.22 to 6.30 in Eastern context.

## Problem & Motivation
The paper argues that humorous image captioning requires more than literal visual description: a caption must connect visual cues with implicit meaning, novelty, and a punchline. Culture adds another constraint because the same image can activate different shared experiences and associative pathways across audiences. Existing multimodal humor work mostly optimizes funniness or specificity under implicit social assumptions, while culture-aware LLM work is largely text-only. The authors therefore treat cultural context as a condition that should shape humor construction, not as a surface style tag.

## Approach
The proposed method, CuHAlign, uses Qwen3-VL-8B with LoRA in three stages. Stage 1 performs supervised fine-tuning on 3,000 Western-context image-text samples to establish output format, instruction following, and basic humorous captioning behavior. Stage 2 applies judge-based GRPO: for each sample, the policy generates K = 8 rollouts, an LLM judge ranks them together with a reference caption, and rewards are based on rank relative to the reference. This stage includes a Degradation-aware Prototype Repulsion Constraint, which penalizes outputs whose representation is too close to prototype vectors for annotated degradation directions. Stage 3 adapts to Eastern context with 1,000 image-text pairs: 50% new Eastern-context images, 30% Eastern captions for shared training-pool images, and 20% Western replay to reduce forgetting.

## Data & Experimental Setup
Raw images are collected from CLoT and filtered for visual richness and reinterpretability, yielding 5,000 images. The split is image-disjoint: 3,500 train, 500 dev, and 1,000 benchmark images. The benchmark has symmetric Western and Eastern references. Western experiments use English prompts, evaluation prompts, and outputs; Eastern experiments use Chinese prompts, evaluation prompts, and outputs. Evaluation uses six 10-point dimensions: Image Relevance, Contextual Fit, Semantic Richness, Reasonableness, Humor, and Creativity. A fixed 20% of test samples is scored by humans and 80% by an LLM judge.

## Results
CuHAlign's core gain is Contextual Fit. In Table 2, it scores CF 6.63 under Western context and 6.30 under Eastern context, the best CF in both settings. Compared with Qwen3-VL-8B-Instruct, this is an increase from 5.49 to 6.63 and from 5.22 to 6.30. CuHAlign's overall averages are 6.63 Western and 6.66 Eastern; GPT-4o has higher overall averages in the same table, 6.76 and 6.75, so CuHAlign's headline advantage is cultural fit rather than top Avg. across all baselines. Explicit context matters: CuHAlign's no-context CF is 5.21, rising to 6.63 Western and 6.30 Eastern; Qwen3-VL-8B-Instruct rises from 3.97 to 5.49 and 5.22. Ablations show Western CF moving 5.49 → 6.13 → 6.59 → 6.62 → 6.63 across base, SFT, GRPO, degradation constraint, and full model. Judge validation finds GPT-5.1 highest in all four settings, with agreement 68.2, 77.3, 71.6, and 79.2.

## Takeaways
- Evaluate culture-aware humor separately from generic funniness; CF changes the ranking story.
- Explicit cultural prompts help, but alignment is needed to make the model use them reliably.
- GRPO provides the largest alignment gain; low-resource cultural adaptation is crucial for Eastern-context performance.
- Hybrid human/LLM evaluation is scalable but still weak on ambiguous fine-grained comparisons.

## Limitations & Caveats
The authors explicitly note that Chinese-for-Eastern and English-for-Western may confound language effects with cultural effects. The Eastern/Western split is coarse and not an exhaustive culture model. The benchmark references are anchors, not a complete set of valid captions. Automatic judging is more reliable for clear quality gaps than for close caption pairs.
