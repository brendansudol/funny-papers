# Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning

**Jifan Zhang, Lalit Jain, Yang Guo, Jiayi Chen, Kuan Lok Zhou, Siddharth Suresh, Andrew Wagenmaker, Scott Sievert, Timothy Rogers, Kevin Jamieson, Robert Mankoff, Robert Nowak** — NeurIPS 2024 (D&B) · Guide entry #22 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2406.10522) · [local PDF](../pdfs/22-caption-preferences.pdf) · [full markdown](../md/22-caption-preferences/22-caption-preferences.md) · [extract](../extracts/22-caption-preferences.json) · [dataset: New Yorker caption ranking (Humor in AI)](../../data/newyorker-caption-ranking/)

## TL;DR
This paper releases a massive multimodal preference dataset from The New Yorker cartoon caption contest and proposes a benchmark for funny caption generation. The central result is that current models can be funny but still lag top humans under human judgment: workers preferred Claude-3-Opus over Human Top 10 captions only 35.4% of the time, and the expert only 1.6%.

## Problem & Motivation
Humorous captioning is a difficult alignment and creativity problem because it combines visual understanding, cultural reference, concision, reasoning, and subjective reader preference. The authors use The New Yorker weekly cartoon caption contest as a high-volume real-world testbed where human submissions are already judged by large crowds.

## Approach
The paper introduces a dataset of cartoons, captions, and ratings, then builds HumorousAI, a benchmark where a model generates ten captions for a held-out cartoon. Those ten are compared with four groups of past human entries: ranked #1-10, #200-209, #1000-1009, and median. The authors propose two group-based evaluation modes: Overall, choosing the funnier group as a whole, and Best Pick, choosing the best caption in each group and comparing those. They also test SFT, RLHF/PPO, DPO, and Best-of-N sampling on open models.

## Data & Experimental Setup
The released dataset covers 365 contests and 365 cartoons, with over 2.2M captions and 284,183,913 ratings. Ratings are collected through a bandit-driven crowd system with labels funny, somewhat funny, and unfunny. For generation experiments, the paper holds out 91 contests. Text-only models receive cartoon descriptions, locations, and entities; multimodal models receive images. Evaluated generators include LLaVA, Mistral-7B variants, GPT-3.5 Turbo, GPT-4o, GPT-4o Vision, and Claude-3-Opus.

## Results
Group evaluation is more reliable than pairwise evaluation for GPT judges. GPT4-Turbo with Hessel et al. descriptions reaches 77.5±2.96 ranking accuracy in Overall group comparison, versus 67±3.33 for the best pairwise setting, a 10.5 point gain. The human expert still reaches 94.28±2.79.

Under GPT-based Overall evaluation, Claude-3-Opus is strongest, with win rates of 54.40, 70.88, 81.87, and 88.46 against Top 10, #200-#209, #1000-#1009, and median human groups. Under human evaluation against Human Top 10, however, Claude is preferred only 35.4% by workers and 1.6% by the expert. For Mistral, DPO improves Best Pick over 0-shot from 1.65 to 10.44 against Top 10 and from 12.64 to 30.22 against median. BoN improves Overall over 0-shot from 8.79 to 16.48 against #200-#209, from 11.54 to 21.43 against #1000-#1009, and from 25.82 to 35.71 against median.

## Takeaways
- Evaluate humor in groups, not only pairwise; it materially improves LLM-judge reliability.
- Expert human judgment remains a much higher bar than GPT-based or crowd-worker judgments.
- Multimodal access did not guarantee better captioning; the paper finds vision integration can hurt.
- SFT can reduce humor quality, while DPO and BoN help in different ways.
- Reward-model gains under PPO do not necessarily translate into funnier captions.

## Limitations & Caveats
The benchmark is New Yorker-specific and reflects its audience, editorial filtering, and style. GPT-based judges require calibration and remain below the expert. The authors also flag humor-offensiveness tradeoffs as unresolved future work.
