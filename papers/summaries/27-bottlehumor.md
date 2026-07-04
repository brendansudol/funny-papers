# BOTTLEHUMOR: Self-Informed Humor Explanation using the Information Bottleneck Principle

**EunJeong Hwang, Peter West, Vered Shwartz** — Findings of ACL 2025 · Guide entry #27 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2502.18331) · [local PDF](../pdfs/27-bottlehumor.pdf) · [full markdown](../md/27-bottlehumor/27-bottlehumor.md) · [extract](../extracts/27-bottlehumor.json)

## TL;DR
BOTTLEHUMOR is an unsupervised prompting method for multimodal humor explanation that elicits image descriptions, implications, and candidate explanations, then selects useful implications with an information-bottleneck objective. Across models, it improves F1 over the best of zero-shot and CoT by 4.2 points on MemeCap, 1.6 on NewYorker, and 2.1 on Yes-But, with GPT-4o + BOTTLEHUMOR reaching the best Avg. F1 of $56.7_{1.1}$.

## Problem & Motivation
Multimodal humor in memes, cartoons, and YesBut images often depends on connecting visual details with text and background knowledge, including commonsense, cultural references, social norms, and unexpected contrasts. Prior multimodal humor datasets ask models to generate free-text explanations, but this is hard to evaluate because explanations are open-ended and humor is subjective. The paper argues that models need not only better reasoning chains, but a way to identify which elicited knowledge is relevant rather than redundant or distracting.

## Approach
BOTTLEHUMOR first asks a VLM to generate up to five literal image-description sentences. It then generates “implications”: concise commonsense or social connections between the image, caption, and descriptions. At each hop, it also generates candidate explanations. The key selection step uses the information bottleneck principle: an implication should be non-redundant with existing inputs, measured by maximum cosine similarity, and relevant to candidate explanations, measured by cross-entropy with a length penalty. The paper uses Qwen2-1.5B for cross-entropy, $\alpha = 0.7$, $H = 2$ hops, and $k = 3$ reasoning chains.

The paper also proposes an LLM-based evaluation metric. References and predictions are decomposed into atomic facts, Gemini-Flash-1.5 checks whether facts are conveyed, and the paper reports precision, recall, and macro-F1.

## Data & Experimental Setup
Experiments use 100 sampled test instances from each of MemeCap, NewYorker, and YesBut, repeated with three random seeds. The tested VLMs are GPT-4o, Gemini 1.5 Flash-8B, Qwen2-VL-7B-Instruct, and Phi-3.5-Vision-Instruct. Baselines are zero-shot, CoT, self-refine with a critic, and self-refine without a critic; baseline temperature is 0.8. The LLM evaluator uses Gemini-Flash-1.5 with temperature 0.2.

## Results
On GPT-4o, BOTTLEHUMOR improves F1 over zero-shot from $48.1_{2.8}$ to $51.5_{0.3}$ on MemeCap, $53.9_{1.9}$ to $58.2_{0.5}$ on NewYorker, and $58.0_{5.5}$ to $60.4_{2.6}$ on YesBut. Compared with self-refine baselines, BOTTLEHUMOR improves average F1 by 2.8, 2.0, and 3.3 points on MemeCap, NewYorker, and YesBut. CoT generally hurts performance; the paper says it often produces generic explanations and loses focus.

The IB ablation supports the selection objective: for GPT4o, Cosine+CE reaches Precision/Recall/F1 of 81.6/37.6/51.5, beating Cosine-only F1 46.7 and CE-only F1 49.2. The proposed metric also aligns with humans: LLM-human agreement is 77.1% ($\kappa$ = 54.1), similar to human-human agreement of 75.4% ($\kappa$ = 50.8).

## Takeaways
- Eliciting extra world knowledge helps humor explanation most when the method also filters for relevance and non-redundancy.
- Recall gains are central: BOTTLEHUMOR adds missing explanatory details while keeping precision comparable.
- Plain CoT is not a safe default for humor explanation because it can make outputs generic.
- Self-refinement without new knowledge is much less useful than implication-guided refinement.
- Builders should watch for noisy implications: error analysis attributes 81.2% of negative cases to dilution of focus and 18.7% to irrelevant information.

## Limitations & Caveats
Humor is subjective, and references may miss valid alternative readings. Atomic-fact evaluation can miss explanation-level nuance. BOTTLEHUMOR is also costlier than direct prompting, using up to 20 calls per sample; the paper estimates 100 samples cost up to $4–5 USD with GPT-4o and up to $1 USD with Gemini-Flash-1.5-8B.
