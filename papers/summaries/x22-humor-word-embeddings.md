# Humor in Word Embeddings: Cockamamie Gobbledegook for Nincompoops

**Limor Gultchin, Genevieve Patterson, Nancy Baym, Nathaniel Swinger, Adam Tauman Kalai** — ICML 2019 · Guide entry Part 4 (audience-modeling anchor) (Part 4 - Evaluation Methodology)

[paper page](https://proceedings.mlr.press/v97/gultchin19a.html) · [local PDF](../pdfs/x22-humor-word-embeddings.pdf) · [full markdown](../md/x22-humor-word-embeddings/x22-humor-word-embeddings.md) · [extract](../extracts/x22-humor-word-embeddings.json) · [dataset: Cockamamie Gobbledegook single-word humor data](../../data/humor-word-embeddings/)

## TL;DR
This paper shows that single-word humor correlates with simple linear directions in standard word embeddings. On the Engelthaler-Hill 4,997-word humor norms, web-trained embeddings reached cross-validated Pearson correlations up to 0.730 ± 0.002, and individual “sense-of-humor” vectors predicted held-out personal preferences with 68.2% success in the normal know-your-audience test.

## Problem & Motivation
The paper asks whether humor, often treated as too subjective for NLP, has simpler structure at the level of individual words. It builds on prior evidence that people consistently rate some words as funnier than others, while emphasizing that aggregate ratings alone cannot explain why people disagree. The authors use word embeddings as a testbed because embeddings are known to encode many semantic properties as linear directions.

## Approach
The first method is a “humor vector”: a least-squares linear regression from 300-dimensional word embeddings to mean word-humor ratings. The paper then defines six theory-motivated humor features—humorous sound, juxtaposition, colloquiality, insults, sexual connotation, and scatological connotation—and tests whether embeddings predict them. Finally, each participant’s sense of humor is represented as the average vector of words they rated funny, enabling clustering and pairwise prediction of unseen preferences.

## Data & Experimental Setup
The authors use the Engelthaler-Hill Dataset: 4,997 single English words, each rated by approximately 35 raters on a 1-5 humor scale. They also introduce a public crowdsourced dataset, starting with 120,000 lower-case words and phrases from GNEWS, filtering to 8,120 words, then to 216 highly humorous words rated by 1,678 U.S.-based raters. A separate annotation study labels 1,500 words for the six humor features, with at least 8 raters per feature/word pair. The evaluated embeddings are GNEWS, WebSubword, WebFast, and WebGlove, all 300-dimensional.

## Results
On Engelthaler-Hill ratings, GNEWS achieved 0.721 correlation without cross-validation and 0.675 ± 0.003 with 10-fold cross-validation. WebSubword achieved 0.767 and 0.729 ± 0.002; WebFast achieved 0.767 and 0.730 ± 0.002; WebGlove achieved 0.768 and 0.730 ± 0.002. For feature prediction, GNEWS predicted colloquial words and insults with correlations greater than 0.5, while juxtaposition was only slightly greater than 0.2; WebSubword predicted all features better than GNEWS except colloquiality and reached correlations equal or greater than 0.4 for five of six features. In the know-your-audience test, success rates were 78.1% for the easy version, 68.2% for the normal version, and 65.0% when only five training words were used. Clustering humor vectors yielded demographic differences: Cluster 1 was 70.3% female, Cluster 5 was 35.2% female, Cluster 3 had mean age 42.3, and Cluster 5 had mean age 34.7, with reported p-value < 10^{-6} for the significant differences.

## Takeaways
- Single-word humor is partly encoded in off-the-shelf word embeddings as linear structure.
- Individual humor preferences can be modeled from only a handful of liked words and can generalize to unrated words.
- Humor evaluation should account for audience differences, not only aggregate funniness.
- Theory-based humor features are useful diagnostics for understanding what an embedding-based humor model captures.

## Limitations & Caveats
The Engelthaler-Hill data is aggregate-only and limited in coverage. The new data is English, mainly U.S.-based, and restricted to lower-case alphabetic strings and phrases. The authors also note that the 216-word rating design introduces noise because initial random word order affects later comparisons, and that embeddings should be complemented by phonotactic, morphological, and orthographic analyses.
