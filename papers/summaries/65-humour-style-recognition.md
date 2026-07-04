# A Two-Model Approach for Humour Style Recognition

**Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat** — arXiv:2410.12842 · Guide entry #65 (Adjacent - Sarcasm & Humor Styles)

[paper page](https://arxiv.org/abs/2410.12842) · [local PDF](../pdfs/65-humour-style-recognition.pdf) · [full markdown](../md/65-humour-style-recognition/65-humour-style-recognition.md) · [extract](../extracts/65-humour-style-recognition.json)

## TL;DR
The paper introduces an English text dataset of 1,463 instances for recognising four humour styles—self-enhancing, self-deprecating, affiliative, and aggressive—plus neutral text. Its main result is that a two-model pipeline improves average f1-score from 70.52 to 75.43 across 14 tested models, with the largest gain for affiliative humour: +11.61% f1-score and 14/14 models improving.

## Problem & Motivation
The authors argue that computational humour work has focused mostly on humour detection, laughter, and generation, while humour style recognition remains underdeveloped despite its links to psychological well-being. Following Martin et al. (2003), they treat affiliative and self-enhancing humour as beneficial styles and aggressive and self-deprecating humour as potentially harmful styles. The paper aims to fill two gaps: the lack of a dedicated dataset for the four humour styles and the lack of baseline models for recognising them in text.

## Approach
The paper evaluates a single-model setup and proposes a two-model setup. The single-model approach trains one classifier to predict five labels: self-enhancing, self-deprecating, affiliative, aggressive, and neutral. The two-model approach first trains a four-class classifier for self-enhancing, self-deprecating, neutral, and a combined affiliative/aggressive class; a second binary classifier then separates affiliative from aggressive humour. This design is motivated by the observation that single models often misclassify affiliative humour as aggressive.

## Data & Experimental Setup
The new Humour Styles Dataset contains 1,463 text instances: 298 self-enhancing, 265 self-deprecating, 250 affiliative, 318 aggressive, and 332 neutral, with text lengths from 4 to 229 words. Sources include 983 jokes from online sites, 280 non-humorous ColBERT instances, and 200 Short Text Corpus instances consisting of 150 jokes and 50 non-jokes. Six Ph.D. annotators labelled the 200 Short Text Corpus instances; Fleiss’ Kappa was 0.2651 and 0.2841 for the two 100-sample sets. For 14 no-majority cases, Chat-GPT, Claude, Microsoft Copilot, and HuggingChat were added as labelers.

Experiments used an 80/20 train/test split with seed 100 and 5-fold cross-validation. The 14 tested systems were Naive Bayes; Random Forest and XGBoost with six embeddings each (BGE, GTE, UAE, MRL, ALI, MUL); and DistilBERT. Metrics were accuracy, precision, recall, and f1-score, with Wilcoxon signed-rank tests comparing approaches.

## Results
For the five-class single-model setup, the best Table 4 result was ALI + XGBoost with 77.8% accuracy and 77.3% f1-score. Single models struggled most on affiliative humour: class f1-scores ranged from 39.2% to 64.9%.

As individual submodels, MUL + XGBoost was best for four-class classification with 85.3% accuracy and 85.1% macro-mean f1-score, while ALI + XGBoost was best for binary affiliative/aggressive classification with 80.0% accuracy and 80.0% f1-score. Combining these produced the best two-model result: 78.0% f1-score and 77.8% accuracy.

Across all 14 models, the two-model approach improved average precision from 72.23 to 77.01 (+4.79), recall from 71.66 to 75.29 (+3.63), f1-score from 70.52 to 75.43 (+4.91), and accuracy from 71.83 to 75.25 (+3.42). Affiliative f1-score improved by 11.61% with p-value 0.0001; aggressive humour was the exception, with average difference -1.65 and p-value 0.1189.

## Takeaways
- Treating affiliative and aggressive humour as a hard pair and separating them in a second stage is useful for this dataset.
- Overall best-score gains are modest, but average gains across models are consistent and statistically supported for most metrics.
- Builders of humour classifiers should report per-style scores; overall accuracy hides weak affiliative performance.
- Annotation remains difficult: even trained annotators produced only fair agreement.

## Limitations & Caveats
The dataset is relatively small, English-centric, and partly sourced from websites that often correspond to only one humour type, creating possible source-style confounds. The task is subjective, as shown by low Fleiss’ Kappa and annotation disagreements. The work is text-only and does not test multilingual, multimodal, personalised, or generative humour-style systems.
