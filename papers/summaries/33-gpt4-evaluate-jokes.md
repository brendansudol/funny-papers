# Is GPT-4 Good Enough to Evaluate Jokes?

**Fabricio Goes, Piotr Sawicki, Marek Grześ, Dan Brown, Marco Volpe** — ICCC 2023 · Guide entry #33 (Part 4 - Evaluation Methodology)

[paper page](https://computationalcreativity.net/iccc23/papers/ICCC-2023_paper_89.pdf) · [local PDF](../pdfs/33-gpt4-evaluate-jokes.pdf) · [full markdown](../md/33-gpt4-evaluate-jokes/33-gpt4-evaluate-jokes.md) · [extract](../extracts/33-gpt4-evaluate-jokes.json)

## TL;DR
This paper tests whether GPT-4 can evaluate joke funniness similarly to humans. Its central methodological choice is to compare rankings of jokes, not raw 1-to-5 scores. The best condition is a reusable system description generated from 200 scored examples, but its correlation with human rankings is still weak: between 0.16 and 0.31.

## Problem & Motivation
Humor evaluation is expensive when it depends on human judges, and creative systems need scalable ways to assess generated artifacts. The authors ask whether GPT-4 can act as a joke evaluator whose rankings resemble human funniness judgments. They focus on rankings because raw score scales can differ between humans and models; what matters here is whether GPT-4 orders jokes similarly to people.

## Approach
The paper evaluates GPT-4 under 7 system descriptions: no description (NONE), a naive “humour expert” role (HE), four humor-style roles from Martin et al. (2003)—affiliative (AH), self-enhancing (SE), aggressive (AG), and self-defeating (SD)—and a proposed suggested description (SG). SG is created by a many-shot prompt containing 200 jokes and their average scores, asking GPT-4 to produce a system description that would help match those scores. The generated description says the evaluator prefers wordplay, puns, light-hearted jokes, clever twists, and subtle wit, and dislikes offensive or inappropriate content.

The authors also test 5 instruction levels: baseline (BS), only examples (OEXA), only explanations (OEXP), examples plus explanations (EXP_EXA), and examples plus explanations with extra examples (EXP_EXA_EXT). GPT-4 is configured with temperature(0), top P(1), frequency penalty(0), and presence penalty(0).

## Data & Experimental Setup
The study uses 1500 jokes from the Sun et al. (2022) dataset, with human annotations including funniness. The paper says that dataset was originally extracted from SemEval 2017 Task 7, and the authors merge the selected jokes with the original joke text. For each of the 35 combinations of 7 system descriptions and 5 instruction levels, they randomly select 10 samples of 5 jokes. This totals 1750 joke evaluations, with the same joke allowed to appear more than once. Human and GPT-4 scores are converted into rankings, and rankings are compared with Spearman rank correlation.

## Results
Across system descriptions, the suggested description (SG) produces the most positive correlation with human rankings. The paper reports that the correlation remains weak, “between 0.16 and 0.31.” Aggressive humour (AG) and affiliative humour (AH) show very weak positive correlation. Self-enhancing humour (SE), self-defeating humour (SD), the humour expert role (HE), and no description (NONE) show no correlation because their intervals intersect zero.

Across instruction levels, the baseline prompt without detailed instructions already shows positive correlation. Only EXP_EXA_EXT improves the average coefficients above the baseline. OEXA, OEXP, and EXP_EXA reduce the average coefficients. The authors explain this by noting that 10% of jokes were rated in the [2.2-2.4] range covered by the extra examples, while only one joke scored more than 3 by human evaluators, making score-3 and score-5 examples less useful.

## Takeaways
- Many-shot generation of a reusable evaluator persona is more promising than simple roles such as “humour expert.”
- Ranking-based evaluation is useful when model and human score scales may not align.
- More instructions are not automatically better; examples must match the dataset’s score distribution.
- GPT-4 shows some alignment with human joke rankings, but the alignment is weak.

## Limitations & Caveats
The study tests only GPT-4 and only this 1500-joke setup. The best reported correlations are weak. GPT-4’s 8192-token restriction limits how many examples can be used in many-shot prompts, and temperature 0 does not guarantee deterministic behavior.
