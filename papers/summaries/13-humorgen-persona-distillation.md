# HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation

**Edward Ajayi, Prasenjit Mitra** — arXiv:2604.09629 · Guide entry #13 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2604.09629) · [local PDF](../pdfs/13-humorgen-persona-distillation.pdf) · [full markdown](../md/13-humorgen-persona-distillation/13-humorgen-persona-distillation.md) · [extract](../extracts/13-humorgen-persona-distillation.json)

## TL;DR
The paper proposes a Cognitive Synergy Framework (CSF) for humor generation: six theory-grounded personas generate diverse joke candidates, which are ranked and distilled into 7B HumorGen models. The main result is that HumorGen-SFT-7B ranks 3rd on HTB under the Llama judge with BT 1128.14, ahead of Gemini-2.5-Pro (1059.07), GPT-OSS-120B (1048.19), and Qwen3-32B (990.44), while DPO and O-GRPO do not improve reliably over SFT.

## Problem & Motivation
The authors argue that standard next-token prediction pushes LLMs toward predictable completions, which conflicts with the surprise and incongruity needed for comedy. Prior humor generation work often focuses on reasoning prompts or specific joke types, while the authors want a broader data-curation method that captures multiple cognitive styles of humor and transfers beyond headline prompts.

## Approach
CSF uses Mixture-of-Thought generation with six cognitive personas: Neurotic, Cynic, Observer, Wordsmith, Optimist, and Absurdist. Each is mapped to a humor theory or mechanism, such as Relief Theory, Superiority Theory, Incongruity, linguistic ambiguity, or Benign Violation. For each input, the system generates 24 candidates (4 per persona × 6 personas), ranks them with pairwise LLM judging and Elo/Bradley-Terry scores, and uses the best candidates for supervised fine-tuning. The paper then tests DPO, O-GRPO, and a Think/CSD variant that trains on reasoning traces plus jokes.

## Data & Experimental Setup
Training starts from the official SemEval 2026 Task 1 MWAHAHA experimental set: 1,200 news headlines and word-pair prompts. Kimi-K2 and Qwen 2.5-32B-Instruct generate about 28,800 candidates, judged by Llama 3.3-70B-Instruct. The authors build SFT data with N = 12,000 top-10 candidates, DPO data with N = 6,000 top-vs-bottom pairs, and O-GRPO data using all 24 candidates per prompt. Evaluation uses the first 50 headlines from the SemEval test set and the new Humor Transfer Bench (HTB), 400 prompts across eight domains. Main automated evaluations compare 15 models with Llama 3.3-70B and Qwen 2.5-72B judges.

## Results
On HTB with the Llama judge, GPT-5 leads at BT 1336.18 and Kimi-K2 is second at 1259.98, but HumorGen-SFT-7B is 3rd at 1128.14 and HumorGen-DPO-7B is 4th at 1123.72. SFT is 69.07 BT above Gemini-2.5-Pro and 79.95 above GPT-OSS-120B. On SemEval with the Llama judge, HumorGen-SFT-7B scores 1140.37 and DPO scores 1135.25, ahead of GPT-OSS-120B at 1049.99 and Qwen3-32B at 1023.18. Under the Qwen judge on SemEval, DPO reaches 1202.76 and SFT 1193.81, both above Gemini-2.5-Pro at 1144.23. Cross-judge agreement is high: Kendall tau = 0.8667 on HTB and 0.8286 on SemEval. Preference alignment is not a clear win: HTB Llama has SFT 1128.14 vs DPO 1123.72, with overlapping confidence intervals; O-GRPO trails at 1071.13. Human evaluation reports 31.7% unanimous agreement, Krippendorff’s α = 0.425, and LLM-human consensus of 58.3%.

## Takeaways
- Curated humor data mattered more than model size in these experiments.
- DPO did not consistently improve over strong CSF-based SFT.
- O-GRPO’s offline advantage weighting underperformed, partly linked to median advantage = −0.479.
- Reasoning traces often hurt judged funniness by encouraging over-explanation.
- Stand-up data was not automatically useful: 998 Shaun Eli jokes reduced BT from 1083.9 to 653.1.

## Limitations & Caveats
The study is English-only, text-only, and limited to SemEval-MWAHAHA plus HTB. Human evaluation is small (N = 3, 60 pairs), and model coverage is limited by compute. The authors also note risks of offensive or culturally insensitive generated humor.
