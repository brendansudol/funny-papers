# Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM

**Yang Chen, Chong Yang, Tu Hu, Xinhao Chen, Man Lan, Li Cai, Xinling Zhuang, Xuan Lin, Xin Lu, Aiming Zhou** — Findings of ACL 2024 · Guide entry #10 (Part 2 - Generating Jokes)

[paper page](https://aclanthology.org/2024.findings-acl.51/) · [local PDF](../pdfs/10-joke-master-pun-curriculum.pdf) · [full markdown](../md/10-joke-master-pun-curriculum/10-joke-master-pun-curriculum.md) · [extract](../extracts/10-joke-master-pun-curriculum.json) · [dataset: ChinesePun](../../data/chinesepun/)

## TL;DR
The paper proposes PGCL, a multi-stage curriculum preference learning framework for making LLMs generate puns that satisfy both structure constraints and humor preferences. It also introduces ChinesePun, a Chinese pun generation dataset. The main result is that PGCL reaches 44.00% Pun Succ. on ChinesePun and 56.00% on SemEval, improving over the best baselines by 16% and 22% respectively.

## Problem & Motivation
Pun generation requires a model to satisfy two goals at once: use the required pun word structure and produce a sentence that is actually humorous. The paper argues that directly applying preference learning such as DPO is inefficient because the available pun datasets are relatively small and the model must align to both structure and humor simultaneously. Prior pun generation work focused mainly on smaller models and English datasets, especially SemEval 2017 Task 7. The authors aim to improve LLM pun generation and test whether the approach works in both English and Chinese.

## Approach
PGCL uses a two-stage curriculum. In stage 1, the model learns structure preference with DPO: the labeled pun is the positive sample, and generated outputs that fail the required structure are used as negative samples. Structure requirements differ by pun type and language: for English homographic and Chinese homographic puns, the pun word must appear; for English homophonic puns, the pun word must appear without the alternative word; for Chinese homophonic puns, both words must appear.

In stage 2, the model learns humor preference. To reduce catastrophic forgetting of structure, the authors propose Improved Humor DPO, a triplet loss using positive puns, “rumination” samples from the stage-1 model that satisfy structure, and negative samples that lack humor and structure. The intended ranking is positive > rumination > negative.

## Data & Experimental Setup
The paper introduces ChinesePun, with 1,049 homophonic puns, 1,057 homographic puns, and 187,315 words in total. Three postgraduate annotators revised ChatGPT pre-annotations; Fleiss’ kappa on 150 instances is κ = 0.68. Experiments use ChinesePun and SemEval-2017 Task 7 puns. ChinesePun is split into 1684 train and 422 test samples; SemEval is split into 1918 train and 478 test samples.

Baselines include AmbiPun, ChatGPT using gpt-3.5-turbo, LLaMA2-7B for English, Baichuan2-7B for Chinese, and SFT/DPO variants. Human evaluation samples 50 pun word pairs and reports humor A/B-test against ChatGPT and Pun Succ.

## Results
On ChinesePun, PGCL obtains 44.00% Pun Succ., versus the best baseline ChatGPT at 28.00%, a 16% improvement. It wins 64.00% and loses 22.00% in humor A/B-test against ChatGPT, with 89.10% Structure Succ. On SemEval, PGCL obtains 56.00% Pun Succ., versus the best baseline ChatGPT at 34.00%, a 22% improvement. It wins 68.00% and loses 14.00% against ChatGPT, with 98.95% Structure Succ. The paired t-test reports significance at p < 0.05.

Ablations show the triplet loss matters: without Improved Humor DPO, ChinesePun Structure Succ. drops from 89.10 to 80.46 and Pun Succ. from 44.00 to 38.00; on SemEval, Structure Succ. drops from 98.95 to 91.64 and Pun Succ. from 56.00 to 46.00.

## Takeaways
- Treat pun generation as multi-objective alignment: structure and humor should be optimized separately.
- DPO is more effective than instruction tuning for the preference targets studied here.
- A structure-first, humor-second curriculum gives the strongest humor results while mostly preserving structure.
- Triplet preference data can reduce forgetting when later alignment stages might overwrite earlier capabilities.
- ChatGPT remains strong in diversity metrics, but lower in pun success.

## Limitations & Caveats
The authors explicitly limit the work to pun generation, a niche humor task. They state that the method still fails to recognize humor’s subjective nature, including variation from personal backgrounds and contextual subtleties. Human evaluation uses 50 sampled pun word pairs and has moderate IAA: 0.47 for humor capability and 0.58 for pun success.
