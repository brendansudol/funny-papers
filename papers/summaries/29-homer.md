# ON THE WINGS OF IMAGINATION: CONFLICTING SCRIPT-BASED MULTI-ROLE FRAMEWORK FOR HUMOR CAPTION GENERATION

**Wenbo Shang, Yuxi Sun, Jing Ma, Xin Huang** — ICLR 2026 · Guide entry #29 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2602.06423) · [local PDF](../pdfs/29-homer.pdf) · [full markdown](../md/29-homer/29-homer.md) · [extract](../extracts/29-homer.json)

## TL;DR
HOMER is a GTVH-based, multi-role LLM framework for generating funny captions for images. Its main result is that, with GPT-4o, it reports average improvements over seven baselines of 8.62% on pass@1, 6.48% on pass@3, and 5.91% on pass@5 across two New Yorker cartoon benchmarks.

## Problem & Motivation
The paper targets multimodal humor caption generation: given an image, generate a relevant and funny caption. The authors argue that existing LLM approaches rely on generic prompting, reasoning chains, self-improvement, or task-specific tuning, and therefore often capture surface humor but lack explicit humor logic, creativity, and interpretability. HOMER is motivated by the General Theory of Verbal Humor, especially script opposition, so that captions are grounded in a recognizable conflict rather than only in free-form LLM generation.

## Approach
HOMER decomposes captioning into three LLM-based roles. The conflicting-script extractor first produces a situation description D and identifies script oppositions C in the image. The hierarchical imaginator then selects candidate humor targets from local and global views and builds imagination trees T_im: LLM free associations form backbone chains, while top-k joke retrieval expands them with humor-related concepts. HOMER-pruning keeps retrieved entities using a score H that combines relevance-opposition, humor-frequency, and POS-diversity. Finally, the caption generator samples a conflict script, target, and imagination path, then generates a caption conditioned on GTVH knowledge resources: situation, script opposition, target, narrative strategy, and language.

## Data & Experimental Setup
The main evaluation uses two New Yorker cartoon datasets. Humor in AI has 365 cartoons, average 6,044 captions, and three ranking groups: #Top10, #200-#209, and #1000-#1009. Electronic sheep has 679 cartoons, average 6 captions, and two groups formed from pairwise rankings: High-Humor and Low-Humor. The humor retrieval database is built from 11 public humor corpora and contains 335,570 jokes after filtering and deduplication. The paper compares HOMER against CoT, few-shot, self-consistency, HumorousAI, LoL, Phunny, and CLoT using GPT-4o, Claude-4, Qwen-VL (7B), and LLaVA-1.5 (7B). GPT-5 is the primary judge; pass@1, pass@3, and pass@5 are averaged over five trials.

## Results
With GPT-4o on Humor in AI, HOMER reaches Top10 pass@1/3/5 of 66.41/83.70/89.18, #200-209 of 73.40/88.38/92.57, and #1000-1009 of 76.32/90.50/94.19. On Electronic sheep with GPT-4o, it scores 75.53/89.21/92.10 for High-Humor and 79.45/91.48/93.81 for Low-Humor. Human evaluation also favors HOMER: 3.54 ± 0.59 on Humor in AI and 3.31 ± 0.85 on Electronic sheep, both the highest reported means. GPT-5 is selected as evaluator because it has the best ranking accuracy: 73.5% on Humor in AI and 70.0% on Electronic sheep. On a public ImgFlip meme dataset, HOMER reports 83.33 pass@1, 96.67 pass@3, and 98.86 pass@5.

## Takeaways
- Explicit script opposition gives LLM caption generation a controllable humor logic.
- The full combination of image, situation description, conflict scripts, and imagination trees is strongest in ablations.
- Joke retrieval is useful, but pruning matters; relevance, frequency, and POS-diversity all contribute.
- Builders of humor systems should evaluate both funniness and diversity; HOMER reports 3-gram diversity 0.98 and NLI Diversity 91.5% on Humor in AI.
- LLM-as-judge results are backed by human ratings and correlation checks, but human humor remains subjective.

## Limitations & Caveats
The paper states that HOMER struggles with purely formal or inherently non-humorous images where script opposition is hard to detect. It also notes subjectivity in humor evaluation, with Cohen's kappa κ = 0.49. Retrieval must be balanced: too few jokes limits imagination, while too many introduce noise. The full model uses seven LLM calls per output, including three imaginator calls.
