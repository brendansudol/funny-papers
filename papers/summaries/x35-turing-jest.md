# Turing Jest: Distributional Semantics and One-Line Jokes

**Sean Trott, Drew E. Walker, Samuel M. Taylor, Seana Coulson** — Cognitive Science 49(5):e70066 · Guide entry Part 1 (Turing Jest) (Part 1 - Explaining & Understanding Jokes)

[paper page](https://onlinelibrary.wiley.com/doi/full/10.1111/cogs.70066) · [local PDF](../pdfs/x35-turing-jest.pdf) · [full markdown](../md/x35-turing-jest/x35-turing-jest.md) · [extract](../extracts/x35-turing-jest.json) · [dataset: Turing Jest stimuli and responses](../../data/turing-jest/)

## TL;DR
The paper asks whether distributional language statistics alone can support one-line joke detection, appreciation, and comprehension. GPT-3 text-davinci-002 and several open-source LLMs performed above chance, but humans remained better overall, especially at understanding joke entailments.

## Problem & Motivation
The authors use humor as a test case for the distributional semantic hypothesis: can a system trained only on linguistic input acquire capacities that seem to require incongruity resolution, frame-shifting, pragmatic reasoning, world knowledge, or Theory of Mind? They focus on one-line jokes because these short verbal materials often hinge on a sentence-final word that forces reinterpretation. A human benchmark is central to the design, because above-chance model performance alone would not show human parity.

## Approach
The paper adapts 400 sentences from Coulson and Lovett (2004): 80 Expected sentences, 160 Joke sentences, and 160 Straight nonfunny counterparts. It runs three tasks. In humor detection, participants and LLMs decide whether each sentence is a joke. In humor appreciation, they rate funniness on a 1–5 scale. In humor comprehension, they judge whether a follow-up probe is entailed by the original sentence. LLM detection and comprehension are scored from log odds comparing p("Yes") to p("No"); LLM funniness is the 1–5 response with highest probability. The paper also analyzes final-word surprisal as a cue.

## Data & Experimental Setup
Study 1 used 167 UCSD native-English-speaking participants; 14 failed attention checks and were excluded. Each participant saw 120 sentences and gave joke/nonjoke judgments plus funniness ratings. Study 2 used 160 Prolific native-English-speaking participants, all passing attention checks, each judging 60 comprehension probes.

The main LLM was GPT-3 text-davinci-002 via the OpenAI Python API, selected because it was not trained with RLHF. Open-source models were run through HuggingFace inference endpoints: Llama-3-8B, Llama-3-70B, and Mixtral 8×7B; Mixtral 8–22B is listed in methods but not reported in detail in the main results. The paper also uses a range of GPT-3 models for preliminary surprisal estimates.

## Results
For Study 1 joke detection, humans were most accurate overall: Human 81.4%, GPT-3 67.5%, Llama-3-70B 70%, Llama-3-8B 67.8%, and Mixtral 8×7B 62%. For joke versus straight controls, F1 scores were Human 0.81, Mixtral8-7B 0.8, Llama3-70B 0.76, Llama3-8B 0.59, and GPT-3 0.36. GPT-3 had high precision but low recall: 0.9 precision, 0.23 recall.

For appreciation, GPT-3 rated jokes funnier than nonjokes and its funniness ratings correlated with average human ratings, Pearson r = .47. In leave-one-annotator-out comparisons, human agreement averaged Pearson r = .58, SD = 0.17, and Spearman rho = 0.56, SD = 0.17; GPT-3 versus the human average reached Pearson r = .52 and Spearman rho = 0.6. The open-source LLM funniness ratings were uncorrelated with human ratings.

For Study 2 comprehension, humans beat GPT-3 overall: 89.5% versus 84.2%. The crucial gap was for jokes: humans scored 84.7% and GPT-3 scored 69.4%; for nonjokes, humans scored 91.9% and GPT-3 scored 94.2%. Llama-3-70B reached 75% on jokes, above GPT-3 but still below humans.

## Takeaways
- Distributional statistics are enough for above-chance one-line joke detection and some joke comprehension.
- Human-level joke understanding is not reached, especially for entailments of jokes.
- Final-word surprisal matters: both humans and LLMs are more likely to treat surprising nonjokes as jokes.
- GPT-3’s funniness ratings are unusually human-like compared with the tested open-source models.
- Humor benchmarks should include human baselines and comprehension tests, not only joke classification.

## Limitations & Caveats
The materials are only one-liners, so results may not generalize to puns, stand-up, conversational humor, or other genres. The model set is limited, exact snapshots and inference dates are not reported, and prompt sensitivity remains a concern. Data leakage is possible because the jokes were previously published and partly web-sourced, though the authors argue the comprehension probes and answers were unlikely to be in training data. The tasks test cognitive judgments, not emotional laughter or arousal.
