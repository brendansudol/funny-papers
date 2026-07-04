# Who Laughs with Whom? Disentangling Influential Factors in Humor Preferences across User Clusters and LLMs

**Soichiro Murakami, Hidetaka Kamigaito, Hiroya Takamura, Manabu Okumura** — arXiv:2601.03103 · Guide entry #36 (Part 4 - Evaluation Methodology)

[paper page](https://arxiv.org/abs/2601.03103) · [local PDF](../pdfs/36-who-laughs-with-whom.pdf) · [full markdown](../md/36-who-laughs-with-whom/36-who-laughs-with-whom.md) · [extract](../extracts/36-who-laughs-with-whom.json)

## TL;DR
This paper studies whose humor preferences LLMs resemble in Japanese text-based Oogiri, rather than comparing models only to an averaged human score. It clusters 276 active users by voting history, estimates cluster-specific Bradley-Terry-Luce factor weights, and finds that LLMs differ from overall users but can align with particular clusters; for example, GPT-5.1 and Claude correlate with C0 at 0.57 and 0.52, while correlations with all users are negative.

## Problem & Motivation
Humor judgments are subjective and culturally dependent, so averaging ratings across users can hide meaningful preference differences. Prior Oogiri work compared LLMs against aggregated human preferences, but did not show whether LLMs match any subset of users. This paper asks what different user clusters prefer, whether LLMs resemble specific clusters, and whether persona prompting can steer an LLM toward a cluster’s preferences.

## Approach
The authors extend an existing Japanese Oogiri-Corpus with user-level voting histories. Each user is represented as a sparse vector of votes over responses, reweighted with TF-IDF, reduced to 100 dimensions with truncated SVD, normalized, and clustered with K-means. For each prompt-response pair, they compute 45 linguistic features and 11 GPT-5.1-labeled humor strategy labels such as `wordplay`, `black_joke_satire`, `incongruity`, `self_reference`, and `mini_story`. Continuous features are binned into categorical factors, and a Bradley-Terry-Luce model estimates how strongly each factor is associated with winning pairwise vote comparisons. The same factor analysis is applied to LLM selections of the funniest response.

## Data & Experimental Setup
The source Oogiri-Corpus contains 908 prompts and 82,536 responses from Oogiri Sogo. After crawling user IDs and filtering to active users with at least 100 votes, the analytical dataset contains 908 prompts, 14,389 responses, and 57,751 votes from 276 users, with 35.6 users per prompt on average. For LLM preference collection, prompts with fewer than five responses are excluded, yielding 897 unique prompts and 14,352 responses. The models evaluated are Gemini 3 Pro, GPT-5.1, and Claude Sonnet 4.5. Seven persona settings are tested: `no_persona`, `{male,female}_20`, `{male,female}_45`, and `{male,female}_65`. Humor-strategy label quality is checked on 110 instances; 94 out of 110 (85.5%) are judged correct.

## Results
K-means yields K = 7 clusters, selected using the elbow method and silhouette scores; the silhouette score is low, s = 0.025. Despite weak separation, clusters show distinct preferences. C0’s top factors are `parentheses` (+0.60), `dialogue` (+0.49), and `sentences-many` (+0.36), while its bottom factors include `self_reference` (-0.61). C5 strongly favors `slang` (+0.65), while C6 strongly disfavors `ending-ellipsis` (-0.83). Cluster correlations also vary: C0 and C3 correlate at 0.41, while C0 and C6 correlate at -0.39.

LLMs do not match overall human preferences: correlations with all users are GPT-5.1: -0.22, Gemini: -0.36, and Claude: -0.26. However, LLMs can resemble specific clusters; GPT-5.1 and Claude correlate with C0 at 0.57 and 0.52. Persona prompting can increase alignment: for Gemini 3 Pro, correlation with C0 rises from 0.39 under `no_persona` to 0.63 under `female_45`, and correlation with C3 rises from 0.10 to 0.34 under `male_20`.

## Takeaways
- Humor evaluation should report cluster- or user-level alignment, not only agreement with an averaged human score.
- BTL factor weights make preference differences interpretable, showing which linguistic and humor-strategy features each group favors or rejects.
- LLMs may look misaligned with “humans overall” while still matching particular user clusters.
- Persona prompting can shift humor preferences, but the paper reports that the effect varies by model, persona, and cluster.

## Limitations & Caveats
The study is limited to Japanese text-based Oogiri and three LLMs. The factor set excludes many social and cultural variables, true rater demographics are unknown, and filtering to users with at least 100 votes may not generalize to less active users. Sparse voting data and missingness may affect clustering, and the strategy-label evaluation uses one author on 110 instances.
