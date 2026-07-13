# “I See What You Did There”: Can Large Vision-Language Models Understand Multimodal Puns?

**Naen Xu, Jiayi Sheng, Changjiang Li, Chunyi Zhou, Yuyuan Li, Tianyu Du, Jun Wang, Zhihui Fu, Jinbao Li, Shouling Ji** — ACL 2026 · Guide entry Part 3 (MultiPun) (Part 3 - Multimodal & Visual Humor)

[paper page](https://aclanthology.org/2026.acl-long.444/) · [local PDF](../pdfs/x38-multipun.pdf) · [full markdown](../md/x38-multipun/x38-multipun.md) · [extract](../extracts/x38-multipun.json) · [dataset: MultiPun](../../data/multipun/)

## TL;DR
The paper introduces MULTIPUN, an English image-plus-text benchmark for multimodal puns with 445 genuine puns and 890 adversarial non-puns. Across 11 VLMs, models often recognize real puns but fail to reject non-puns; the paper reports that Pun-CoT and Pun-Tuning improve F1 scores by an average of 16.5%.

## Problem & Motivation
Multimodal puns require linking a visual literal object with a textual or contextual second meaning, such as pears behaving like a romantic pair. Existing work is mostly text-only or positive-only, so a model can appear good by saying that every playful scene is a pun. The paper asks whether VLMs can detect, localize, and explain multimodal puns against adversarial non-puns, and whether prompting or fine-tuning can improve this ability.

## Approach
The authors construct MULTIPUN from homophonic and homographic pun tuples. They use CMU Pronouncing Dictionary and WordNet to identify candidate word/sense pairs, GPT-4o to generate captions, image descriptions, and interpretations, and GPT-image-1 to generate images. Two negative variants are created for each pun: Explicative Substitution, which removes ambiguity by replacing the pun word with an explicit meaning, and Random Substitution, which replaces the object with an unrelated concrete noun. The evaluation suite has detection, localization, and explanation tasks, each asked in biased-to-pun and biased-to-non-pun forms. Two improvement methods are proposed: Pun-CoT, a structured prompt with visual grounding, lexical anchoring, and cross-modal verification; and Pun-Tuning, fine-tuning on positives, negatives, and both prompt biases.

## Data & Experimental Setup
MULTIPUN has 194 homophonic and 251 homographic positive samples, plus 445 Explicative Substitution and 445 Random Substitution negatives, for 1,335 total samples. Three graduate-student annotators verified samples; retention required at least 2 of 3 acceptances, and Fleiss’ Kappa was 0.78. The paper evaluates GPT-5.1, GPT-4o, Gemini-3-Pro, Claude Sonnet 4.5, Qwen3-VL variants, LLaVA-v1.6-Vicuna-13B, Llama-4-Scout-17B, and GLM-4.1V-9B-Thinking. Metrics include TPR, TNR, F1, prompt-bias deltas, Cohen’s Kappa, mention ratio, and LLM-judge Win/Tie/Loss comparisons for explanations.

## Results
The central failure is false positives on non-puns. For homophonic detection, Qwen3-VL-30B-A3B-Instruct reaches TPR 0.990 but TNR only 0.018. Closed models also have low detection TNRs: the paper says GPT-5.1, GPT-4o, Gemini-3-Pro, and Claude-Sonnet-4.5 are mostly below 0.38. GPT-5.1 is strongest on explanation-task F1, with 0.804 on homophonic and 0.757 on homographic puns. Prompt bias is severe for some open models: LLaVA-v1.6-Vicuna-13B has homophonic detection ΔTPR -0.923 and ΔTNR +0.933. Pun-CoT raises Qwen3-VL-8B-Thinking homophonic explanation F1 from 0.595 to 0.807 and TNR from 0.387 to 0.776. Pun-Tuning raises LLaVA-v1.6-Vicuna-13B F1 from 0.057 to 0.640 on homophonic puns and 0.051 to 0.617 on homographic puns.

## Takeaways
- Include adversarial non-puns; positive-only pun tests overestimate understanding.
- Ask reverse or bias-controlled prompts to expose sycophancy and prompt dependence.
- Explanation prompts can improve non-pun rejection, but explanation quality remains hard.
- Homophonic alternative-word recovery is a bottleneck.
- Structured grounding and fine-tuning on negatives both help reduce forced pun interpretations.

## Limitations & Caveats
MULTIPUN is English-only and synthetic. The explanation-quality comparison depends on an unnamed advanced LLM judge, with no reported human validation. API inference dates and decoding settings are not reported. The paper also contains an inconsistency: it says fine-tuning is limited to three open-source models, while Table 4 reports Pun-Tuning results for four models.
