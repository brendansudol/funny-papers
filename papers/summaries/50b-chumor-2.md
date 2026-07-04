# Chumor 2.0: Towards Benchmarking Chinese Humor Understanding

**Ruiqi He, Yushu He, Longju Bai, Jiarui Liu, Zhenjie Sun, Zenghao Tang, He Wang, Hanchen Xia, Rada Mihalcea, Naihao Deng** — ACL Findings 2025 (arXiv:2412.17729) · Guide entry #50 (2.0) (Part 7 - Cross-Cultural & Translation)

[paper page](https://arxiv.org/abs/2412.17729) · [local PDF](../pdfs/50b-chumor-2.pdf) · [full markdown](../md/50b-chumor-2/50b-chumor-2.md) · [extract](../extracts/50b-chumor-2.json)

## TL;DR
The paper introduces Chumor, a Chinese humor explanation benchmark built from Ruo Zhi Ba jokes. Ten Chinese-capable LLMs are tested on judging whether an explanation fully explains a joke; the best LLM accuracy is 60.3%, far below the human score of 78.3%.

## Problem & Motivation
Most humor datasets and evaluations are English-centered, while Chinese humor often depends on cultural references, homophones, character forms, parsing ambiguity, and cross-lingual sound play. The authors argue that humor explanation is harder than merely detecting humor because it requires identifying why a joke works. They target Ruo Zhi Ba, a Chinese Reddit-like forum known for intellectually challenging and culturally specific jokes.

## Approach
Chumor frames humor understanding as a binary explanation classification task. Given a joke and an explanation, the model must choose whether the explanation “fully explain[s] the joke” or “partially/does not explain” it. GPT-4o and ERNIE4-turbo first generate explanations for collected jokes, and five native Chinese-speaking authors annotate the generated explanations by majority vote. The paper also categorizes jokes into six types: cultural, situational, pun-based, homophonic, glyph-based, and cross-lingual.

## Data & Experimental Setup
The dataset is sourced from RZB “Best Annual Threads” from 2018 to 2021 and the “Moderator’s Recommendation” section. After cleaning, removing duplicates, and manually filtering forum-management, offensive, incomplete, and non-humor/philosophical posts, Chumor contains 3,339 instances; the paper states 1,454 are good explanations and 1,887 are bad explanations. The authors evaluate Yi-34B, Nemotron70B, Athene70B, Qwen2.5-72B, Mistral123B, Gemini1.5-pro, GLM-4plus, GPT-4 Turbo, GPT-4o, and ERNIE4-turbo using direct prompting and chain-of-thought prompting. Metrics are accuracy, FPR, FNR, and MCC. A separate human study uses three native Chinese speakers on 200 examples. A case study compares human-written explanations against GPT-4o and ERNIE4-turbo explanations for 1,951 jokes, with six native Chinese-speaking college students doing A/B preference annotation.

## Results
All LLMs struggle: reported accuracies range from 44.6% to 60.3%. ERNIE4-turbo and Gemini1.5-pro reach the highest accuracy, 60.3%, only about ten points above the random baseline and 18.0 points below human accuracy of 78.3%. The best LLM MCC is 0.29, versus human MCC of 0.60. CoT does not reliably help: ERNIE4-turbo drops from 60.3% to 45.2%, Mistral123B from 55.6% to 51.2%, GPT-4o from 51.9% to 50.6%, and GPT-4 Turbo from 52.3% to 51.3%; eight of ten LLMs have lower MCC under CoT. In the preference study, Figure 4 reports human explanations beating GPT-4o 59.9% of the time and ERNIE4-turbo 53.7% of the time, while LLM wins are 2.2% and 2.9%.

## Takeaways
- Chinese humor explanation is a hard benchmark even for advanced LLMs.
- Direct prompting can outperform CoT when models lack the underlying humor understanding.
- Builders should test by joke mechanism, not only aggregate accuracy, because failures differ across cultural, pun, homophone, glyph, parsing, and cross-lingual cases.
- Human explanations remain much higher quality than GPT-4o and ERNIE4-turbo explanations in this setup.

## Limitations & Caveats
The paper could not evaluate all possible LLMs because of budget and API limits. Humor preference is subjective, with 61.4% average agreement in the A/B study. The authors filtered offensive content but warn that some jokes may still offend and recommend culturally sensitive use.
