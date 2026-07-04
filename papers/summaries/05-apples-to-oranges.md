# Comparing Apples to Oranges: A Dataset & Analysis of LLM Humour Understanding from Traditional Puns to Topical Jokes

**Tyler Loakman, William Thorne, Chenghua Lin** — EMNLP Findings 2025 · Guide entry #5 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2507.13335) · [local PDF](../pdfs/05-apples-to-oranges.pdf) · [full markdown](../md/05-apples-to-oranges/05-apples-to-oranges.md) · [extract](../extracts/05-apples-to-oranges.json) · [dataset: Comparing Apples to Oranges jokes](../../data/apples-to-oranges-jokes/)

## TL;DR
This paper introduces a 600-joke benchmark for testing whether LLMs can explain humour across four forms: homographic puns, heterographic puns, non-topical Reddit jokes, and topical Reddit jokes. Across 4800 zero-shot explanations from 8 LLMs, the main result is that no tested model reliably explains all joke types, and topical humour plus heterographic puns expose clear weaknesses.

## Problem & Motivation
Most computational humour work has focused on detection or on short pun-based jokes. The authors argue that this narrow focus misses much of everyday humour, especially internet and topical jokes that depend on social context, pop culture, news, and real-world entities. The paper asks whether joke format affects LLM explanation ability and whether findings from pun-heavy humour research generalise to the jokes people encounter online.

## Approach
The authors curate a balanced dataset and write a human reference explanation for every joke. Models are prompted zero-shot with: “Explain the following joke (presented in square brackets) in approximately 100 words.” Explanations are scored on two 0–5 criteria: accuracy, meaning whether the explanation is correct and avoids hallucinated interpretations; and completeness, meaning whether it covers the relevant elements needed to understand the humour. A “good” explanation is one scoring at least 4 on both criteria.

## Data & Experimental Setup
The dataset contains 600 English jokes: 150 homographic puns, 150 heterographic puns, 150 non-topical Reddit jokes, and 150 topical Reddit jokes. The pun subsets come from SemEval-2017 Task 7 puns; the Reddit subsets come from rJokes corpus. Topical Reddit jokes were selected using r/Jokes scores, named-entity filtering, and manual verification. The paper evaluates GPT-4o, GPT-4o Mini, Gemini 1.5 Pro, Gemini 1.5 Flash, Llama 3.1 8B, Llama 3.1 70B, DeepSeek-R1-Distill-Llama-8B, and DeepSeek-R1-Distill-Llama-70B. One author rated all 4800 explanations; 320 were re-annotated by 2 third-party annotators. Qwen2.5-72B-Instruct was also used as an LLM judge, and automatic metrics were computed against the human references.

## Results
GPT-4o consistently outperformed the other systems, while Llama 70B outperformed most models except GPT-4o. GPT-4o Mini beat Gemini Pro in some cases, including accuracy on homographic jokes and both accuracy and completeness for non-topical and topical jokes. The DeepSeek-R1 reasoning models did not outperform the non-reasoning models; R1 8B was the worst-performing model.

Logistic regression showed a strong size effect: larger variants were more likely to produce good explanations (β = 1.707, p < 0.001). Joke type also mattered: homographic jokes were easiest (β = 0.583, p < 0.001), while non-topical jokes (β = -0.511, p < 0.001) and topical jokes (β = -0.574, p < 0.001) were harder; pseudo R² = 0.138. Automatic metrics followed the same broad pattern: topical jokes scored SacreBLEU 7.09 and ROUGE-L 0.23, compared with homographic jokes at SacreBLEU 10.15 and ROUGE-L 0.28. Human reliability checks gave α = .574 for accuracy and α = .553 for completeness; Qwen judge agreement was α = .565 and α = .519.

## Takeaways
- Evaluating only puns overstates LLM humour understanding.
- Heterographic puns are difficult because phonetic similarity is not explicit in text tokens.
- Topical jokes require retrieval or recall of unstated real-world knowledge.
- Larger models help, but scale alone does not solve humour explanation.
- Completeness is a key failure mode: models often identify part of a joke but omit essential context.

## Limitations & Caveats
The benchmark has 600 jokes, which is small but enables manual reference-writing and evaluation. The jokes come from existing sources and may have appeared in model training data, although the authors argue explanations are much less likely to be present. Most scoring was done by one author, with third-party and LLM-judge checks. The dataset does not test very recent topical humour, and many joke formats remain outside its four-way categorisation.
