# Pun2Pun: Benchmarking LLMs on Textual-Visual Chinese-English Pun Translation via Pragmatics Model and Linguistic Reasoning

**Yiran Rex Ma, Shan Huang, Yuting Xu, Ziyu Zhou, Yuanxi Wei** — ACL 2025 SRW · Guide entry #52 (Part 7 - Cross-Cultural & Translation)

[paper page](https://aclanthology.org/2025.acl-srw.23/) · [local PDF](../pdfs/52-pun2pun.pdf) · [full markdown](../md/52-pun2pun/52-pun2pun.md) · [extract](../extracts/52-pun2pun.json) · [dataset: Pun2Pun](../../data/pun2pun/)

## TL;DR
Pun2Pun introduces a Chinese-English benchmark for translating textual and visual puns while preserving wordplay and humor. The strongest textual translation result is deepseek-v3/CVO on English puns, with Hit 43.16/47.02 for homophonic/homographic cases, but overall performance remains modest, especially for visual puns.

## Problem & Motivation
Pun translation is difficult because puns rely on language-specific sound, spelling, meaning, and culture. The paper focuses on Chinese-English translation, a distant language pair where pun transfer is often treated as nearly impossible. Existing computational work covers detection, generation, and closer language pairs more than Chinese-English pun translation, and the authors argue that language-specific reasoning remains underexplored in current LLM evaluation.

## Approach
The paper builds Pun2Pun with progressive subtasks. For text, the tasks are Classification, Locating, Decomposition, and Translation. For visual puns, the tasks are Classification, Decomposition, Appreciation, and Translation. The proposed translation strategy adapts Constant-Variable Optimization: identify source constants SM1, SM2, and SPM; enumerate target variables TM1, TM2, and TPM; reconstruct a target-language pun; and optimize overlap. The Ovl metric scores hit translations using weights 0.25 for structure preservation, 0.25 for contextual reconstruction, and 0.50 for pragmatic retention.

## Data & Experimental Setup
Pun2Pun contains 5.5k textual examples across Chinese and English plus 1k caption-embedded images. The final textual split includes Chinese textual 1154 phonic and 1490 graphic examples, and English textual 1197 phonic and 1661 graphic examples. The visual split includes Chinese visual 426 phonic and 74 graphic examples, and English visual 155 phonic and 349 graphic examples. Textual models include gpt-4o, o1-mini, deepseek-v3, deepseek-r1, qwen-vl-max, qwq-32b-preview, and claude-3.5-sonnet; visual models include gpt-4o, o3-mini, qwen-vl-max, qvq-72b-preview, and claude-3.5-sonnet. Strategies are Vanilla, 1-Shot, and CVO.

## Results
Textual metrics are reported in homophonic/homographic order. On English textual translation, deepseek-v3/CVO reached Hit 43.16/47.02, improving over deepseek-v3/Vanilla 10.94/15.41 by +32.22/+31.61 points. On Chinese textual translation, deepseek-r1/CVO had the best Hit, 26.31/24.73, compared with deepseek-r1/Vanilla 23.89/22.21. For visual translation, metrics are English/Chinese: gpt-4o/1-Shot achieved the best English Hit, 23.34, while claude-3.5-sonnet/1-Shot achieved the best Chinese Hit, 17.80, and the best Ovl, 40.21/23.66. The paper also reports that hit rates rarely exceed 40% for textual puns and 20% for visual puns.

## Takeaways
- Pun understanding is not the main bottleneck; translation is.
- CVO can help strong models, but it can also over-abstract and hurt outputs.
- Homophonic puns are generally harder to translate than homographic puns.
- Successful translations often require semantic divergence from the source.
- Switching between homophonic and homographic mechanisms can be a useful adaptation strategy.

## Limitations & Caveats
The benchmark lacks inter-rater reliability measurements and gold reference translations. Main quantitative evaluation relies heavily on gpt-4o-mini as an LLM judge, and the authors state that scores should be interpreted cautiously. The study focuses on Chinese-English, primarily large/proprietary models, relatively simple prompting comparisons, and isolated puns rather than broader discourse contexts.
