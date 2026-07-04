# Chumor 1.0: A Truly Funny and Challenging Chinese Humor Understanding Dataset from Ruo Zhi Ba

**Ruiqi He, Yushu He, Longju Bai, Jiarui Liu, Zhenjie Sun, Zenghao Tang, He Wang, Hanchen Xia, Naihao Deng** — arXiv:2406.12754 · Guide entry #50 (Part 7 - Cross-Cultural & Translation)

[paper page](https://arxiv.org/abs/2406.12754) · [local PDF](../pdfs/50-chumor.pdf) · [full markdown](../md/50-chumor/50-chumor.md) · [extract](../extracts/50-chumor.json)

## TL;DR
Chumor is a Chinese humor understanding dataset built from Ruo Zhi Ba jokes, with 1,951 manually annotated explanations. In A/B preference tests, native Chinese speakers strongly preferred human explanations over GPT-4o and ERNIE Bot: human explanations won 59.9% vs GPT-4o’s 2.2%, and 53.7% vs ERNIE Bot’s 2.9%.

## Problem & Motivation
Most humor datasets and evaluations discussed by the paper focus on English, leaving culturally specific non-English humor underrepresented. The authors target Chinese Internet humor from Ruo Zhi Ba, a Chinese Reddit-like platform for intellectually challenging jokes. They argue that these jokes require cultural knowledge, linguistic flexibility, and reasoning over puns, pronunciation, character forms, and context, making them useful for evaluating LLM humor understanding.

## Approach
The authors construct Chumor from Ruo Zhi Ba “Best Annual Threads” between 2018 and 2021 plus all threads in the “Moderator’s Recommendation” section. They clean placeholder content such as “.”, “!”, “0”, and “RT,” repair truncated titles using full content, and remove duplicates. One author then manually writes explanations and filters out posts that are not funny, are about forum management or rules, contain excessively offensive content, are incomplete, or are more philosophical than humorous.

For model evaluation, the authors prompt GPT-4o and ERNIE Bot zero-shot in Chinese: “请用两句话解释这个笑话的幽默之处:\n[Joke]” (“Please explain the joke in two sentences:\n[Joke]”). Human and LLM explanations are compared via randomized A/B tests.

## Data & Experimental Setup
Chumor contains 1,951 jokes. The explanations average 78 Chinese characters per joke and total 151,730 Chinese characters. Six college students who are native Chinese speakers and grew up in China annotate preferences between a human explanation and one LLM explanation. Each joke receives three preference annotations; the authors take majority vote, and if all annotators disagree, assign “Undecided.” The reported agreement rate is 61.39% in the main text; Appendix C reports 61.92% for GPT-4o, 60.86% for ERNIE Bot, and 61.38% combined.

## Results
Against GPT-4o, human explanations win 59.9% of cases, ties are 31.8%, GPT-4o wins 2.2%, and 6.2% are undecided. Thus, human wins exceed GPT-4o wins by 57.7 percentage points. Against ERNIE Bot, human explanations win 53.7%, ties are 38%, ERNIE Bot wins 2.9%, and 5.3% are undecided; human wins exceed ERNIE Bot wins by 50.8 percentage points.

A 200-example error analysis shows GPT-4o has higher cultural unawareness than ERNIE Bot: 29.5 vs 10.5. Other reported frequencies include insufficient contextual understanding at 22 for GPT-4o and 26 for ERNIE Bot, pun-based humor at 15.5 and 19.5, hallucination at 9.5 and 2, homophonic humor at 5 and 4.5, character-based humor at 2.5 and 3, parsing error at 1.5 and 0.5, and cross-lingual humor at 0.5 and 1.

Appendix F tests GPT-4o as a preference annotator. GPT-4o chooses human explanations 20.9% of the time, ties 6.6%, and its own explanations 72.6%, a distribution the authors say differs significantly from human preference.

## Takeaways
- Chinese humor explanation remains difficult for SOTA LLMs, especially when jokes rely on culture, pronunciation, parsing ambiguity, or Chinese character forms.
- Human evaluation is crucial here; GPT-4o’s self-favoring preference behavior makes it unreliable as a standalone judge.
- Builders of humor systems should test culturally specific cases rather than relying only on English benchmarks.
- Error analysis should distinguish cultural failure, pun failure, hallucination, and over-refusal, because they imply different model weaknesses.

## Limitations & Caveats
The preference study is not large-scale because it was time-consuming and required native Chinese speakers. Humor is subjective, and the authors encourage larger future preference datasets. The paper evaluates only GPT-4o and ERNIE Bot, not open-source LLMs. Although excessively offensive content was filtered, some jokes may still be offensive depending on audience and cultural context.
