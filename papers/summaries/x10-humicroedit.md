# SemEval-2020 Task 7: Assessing Humor in Edited News Headlines

**Nabil Hossain, John Krumm, Michael Gamon, Henry Kautz** — SemEval-2020 · Guide entry Part 8 (pre-LLM anchor) (Part 8 - Datasets & Shared Tasks)

[paper page](https://aclanthology.org/2020.semeval-1.7/) · [local PDF](../pdfs/x10-humicroedit.pdf) · [full markdown](../md/x10-humicroedit/x10-humicroedit.md) · [extract](../extracts/x10-humicroedit.json) · [dataset: Humicroedit + FunLines (SemEval-2020 Task 7)](../../data/humicroedit-funlines/)

## TL;DR
This paper is the overview of SemEval-2020 Task 7, a shared task on assessing humor in edited news headlines. It provides a benchmark for predicting 0-3 funniness ratings and for choosing the funnier of two edited headlines; the best system, Hitachi, achieved 0.49725 RMSE on Subtask 1 and 67.43% accuracy on Subtask 2.

## Problem & Motivation
Most prior humor datasets treated humor as binary, but the authors argue that humor varies in intensity and that systems need to estimate degree of funniness. They focus on news headlines with micro-edits because a single-word substitution creates a localized humorous effect in a short context. The shared task is intended to unify computational humor research around common data, metrics, and comparisons.

## Approach
The benchmark has two subtasks. Subtask 1 is regression: given the original and edited headline, estimate the edited headline’s mean funniness on a 0-3 scale. Subtask 2 is classification: given two edited versions of the same original headline, predict which one is funnier. Subtask 1 is evaluated with RMSE. Subtask 2 is evaluated with accuracy, plus an auxiliary reward metric that weights correct and incorrect predictions by the absolute funniness difference between the two headlines.

## Data & Experimental Setup
The task uses the Humicroedit data, containing about 5,000 original headlines and 15,095 edited headlines. Original headlines came from Reddit r/worldnews and r/politics, were published between 01/2017 and 05/2018, were 4-20 words long, and were sampled from 25 major English news sources. Qualified Mechanical Turk editors replaced one verb, noun, or entity with a single word to make the headline funny. Five judges rated each edited headline from 0 to 3, and the mean rating is the target. The task also provided FunLines as extra training data: 8,248 annotated headlines. Subtask 1 used 9,653 train, 8,248 FunLines train, 2,420 dev, and 3,025 test examples. Subtask 2 used 9,382 train, 1,959 FunLines train, 2,356 dev, and 2,961 test examples.

## Results
The task attracted 48 teams for Subtask 1 and 31 for Subtask 2. Hitachi won both: 0.49725 RMSE for Subtask 1, described as a 13.5% improvement over BASELINE, and 67.43% accuracy for Subtask 2, a 17.93 percentage-point increase over BASELINE, with reward 0.2988. The best official benchmark was RoBERTa: 0.52207 RMSE for Subtask 1 and 0.6495 accuracy / 0.2541 reward for Subtask 2. The paper reports that contextual BERT and RoBERTa embeddings outperformed the context-independent GloVe CBOW benchmark. Aggregate analysis found minimum regression error around funniness 1.0, larger errors at the extremes, and easier pairwise classification when the funniness gap was larger.

## Takeaways
- Shared humor tasks can attract substantial participation and enable direct comparison across approaches.
- Pre-trained language models and large ensembles were the strongest approaches in this benchmark.
- Subtask 2 can often be solved by scoring each headline with a Subtask 1 regressor and ranking the scores.
- Incongruity, approximated with GloVe distance between original and replacement words, correlated with easier pairwise humor ranking.
- Systems still fail on cases requiring world knowledge, cultural references, sarcasm, negative sentiment, and common sense.

## Limitations & Caveats
Humor ratings are subjective, and some examples had low judge agreement. The funniness distribution is non-uniform, with fewer extreme examples. The paper notes dataset quirks, including Trump-related bias, and says FunLines ratings may not be calibrated with the main task data because they used different judges.
