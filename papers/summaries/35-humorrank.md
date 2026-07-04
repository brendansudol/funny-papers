# HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation in Large Language Models

**Edward Ajayi, Prasenjit Mitra** — arXiv:2604.19786 · Guide entry #35 (Part 4 - Evaluation Methodology)

[paper page](https://arxiv.org/abs/2604.19786) · [local PDF](../pdfs/35-humorrank.pdf) · [full markdown](../md/35-humorrank/35-humorrank.md) · [extract](../extracts/35-humorrank.json)

## TL;DR
HumorRank is a tournament-based framework for ranking LLMs on headline-conditioned joke generation. It evaluates nine models on SemEval-2026 MWAHAHA and Humor Transfer Bench using pairwise LLM judges, Bradley–Terry ratings, and GTVH feature tags. The central result is strong cross-judge stability: independent Llama 3.3 70B and Qwen 2.5 72B judges achieve Kendall τ = 0.889 on both benchmarks.

## Problem & Motivation
Humor evaluation is hard because funniness is subjective, comparative, and driven by interacting mechanisms rather than a single scalar property. The paper argues that existing approaches—absolute scores, punchline detection, classification, scalar funniness rubrics, or small human preference studies—produce isolated or task-specific measurements that do not support consistent model comparison. HumorRank reframes evaluation as a leaderboard problem: given multiple models generating jokes for the same prompt, which model is preferred more often across a tournament?

## Approach
Each contestant model generates a joke for the same headline prompt. HumorRank then schedules same-prompt pairwise duels and asks an LLM judge to choose A, B, or TIE, with brief reasoning plus structured tags for winner humor mechanisms, winner delivery features, and loser failure modes. The protocol is grounded in GTVH and uses tags such as incongruity, wordplay, absurdity, sarcasm, conciseness, escalation, cliché, and weak_punchline. Pairwise outcomes are aggregated with Bradley–Terry maximum likelihood estimation; Stable Elo over 10 shuffled orderings is reported as an audit metric. Adaptive Swiss Pairing is proposed to reduce comparison cost while preserving ranking fidelity.

## Data & Experimental Setup
The paper evaluates two English headline-conditioned humor benchmarks: SemEval-2026 Task 1 MWAHAHA data, using the official 300-prompt test set, and Humor Transfer Bench, using 400 held-out headline prompts. The nine contestant models are GPT-5, Kimi K2, Gemini 2.5 Pro, HumorGen-7B, Claude 3.5 Haiku, GPT OSS 120B, Qwen 3 32B, Llama 3.3 70B, and Base Qwen 7B. Llama 3.3 70B Instruct is the primary judge; Qwen 2.5 72B Instruct is the validation judge. Full round-robin uses 36 pairs per prompt: 10,800 SemEval judgments and 14,400 HTB judgments per judge.

## Results
On SemEval with the Llama judge, GPT-5 ranks first with BT 1307.5 and 84.0% win rate. It beats Kimi-K2, ranked second at BT 1156.9, by 150.6 BT points. HumorGen-7B ranks fourth at BT 1092.8, above GPT OSS 120B at BT 1015.0 by 77.8 points, despite being much smaller. On HTB with the Llama judge, GPT-5 remains first at BT 1314.7, Kimi K2 is second at 1242.0, and HumorGen-7B ranks third at 1097.7.

Cross-judge agreement is the key validation result: Llama and Qwen leaderboards have Kendall τ = 0.889 on both SemEval and HTB, and pooled Llama–Qwen labels show 82.9% agreement with Krippendorff α = 0.658. Budget ablation shows Full RR averages τ = 0.889; Swiss 3RR uses 12 pairs/prompt (~33% budget) and averages τ = 0.861; Swiss 2RR uses 8 pairs/prompt (~22%) and averages τ = 0.806. Human evaluation on 60 SemEval pairs gives human-only α = 0.432 for the best two-rater dyad and Llama–Qwen α = 0.425.

## Takeaways
- Pairwise preference is more discriminative than absolute humor scoring in this setting.
- GPT-5 is the strongest evaluated model, but HumorGen-7B is competitive with larger general-purpose systems.
- Swiss 3RR is the paper’s recommended reduced-budget mode when full round-robin is too expensive.
- Feature tags make the leaderboard diagnostic: frontier models emphasize conciseness, while HumorGen-7B emphasizes absurdity and escalation.
- LLM-as-judge results should be validated across judges and, where possible, against human preferences.

## Limitations & Caveats
The study is English-only, evaluates only nine models, and covers headline-conditioned text rather than interactive or multimodal humor. LLM judges may encode cultural and stylistic bias, and GTVH tags were not separately human-audited. The human study is small, and Adaptive Swiss Pairing has empirical support but no formal convergence proof.
