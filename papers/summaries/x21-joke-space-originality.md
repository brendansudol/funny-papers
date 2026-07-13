# Navigating the Joke Space: Towards Automated Originality Assessment of AI-Generated Humor

**Ori Amir, Huyen Dieu Ngo, Joe Toplyn, Kevin P. Hickerson** — CHum 2026 · Guide entry Part 4 (originality beyond funniness) (Part 4 - Evaluation Methodology)

[paper page](https://aclanthology.org/2026.chum-1.8/) · [local PDF](../pdfs/x21-joke-space-originality.pdf) · [full markdown](../md/x21-joke-space-originality/x21-joke-space-originality.md) · [extract](../extracts/x21-joke-space-originality.json) · [dataset: One Million Reddit Jokes](../../data/one-million-reddit-jokes/)

## TL;DR
This paper proposes automated measures for rating the originality of AI-generated jokes by extracting “topic handles” and checking how rare or semantically distant their combinations are in a large joke corpus. The strongest individual measures correlated with professional comedians’ originality ratings at ρ = .372 and ρ = .369, and a Lasso composite reached ρ = .401 in 10-fold cross-validation, about 82% of the estimated human-rating reliability ceiling.

## Problem & Motivation
LLMs can generate jokes, but it is unclear whether those jokes are genuinely original rather than reworded or recombined versions of existing humor. The paper argues that surface plagiarism detection is insufficient because jokes can share an underlying premise while differing in wording. Building on the General Theory of Verbal Humor, it treats a joke’s core identity as its script opposition and logical mechanism, approximated computationally by “topic handles”: key nouns or noun phrases whose pairing drives the joke.

## Approach
The method extracts topic handles from each joke with GPT-5.4, decomposes multi-word handles when needed, enumerates all handle pairs, and scores the most original pair. Three PMI variants measure how rarely handle pairs co-occur in a reference corpus: exact raw PMI, semantic-cluster PMI using 15 K-means clusters, and decomposed PMI over component words. Two embedding measures use all-mpnet-base-v2: Concept Distance Max, the largest 1 − cosine distance among handle pairs, and Corpus Novelty, defined as 1 minus the maximum cosine similarity between the full joke and any reference-corpus joke retrieved with FAISS. A Lasso composite combines the strongest signals.

## Data & Experimental Setup
The reference corpus is the SocialGrep One Million Reddit Jokes dataset, described as one million English jokes from joke subreddits. The paper generated 400 OpenAI API jokes: 200 from GPT-4o and 200 from GPT-5.4, using prompts that varied style across absurdist, satirical, dry wit, wordplay, and observational humor. It also used 80 JEST benchmark items: 60 Witscript-generated jokes and 20 GPT-5.1 non-humor items. Three professional comedians rated 80 jokes from each source on 0–3 originality and 0–3 funniness scales.

## Results
JEST jokes were rated most original: M = 2.48 (SD = 0.45), versus GPT-4o M = 2.09 (SD = 0.48) and GPT-5.4 M = 1.92 (SD = 0.55), with H(2) = 45.80, p < .001. Funniness did not differ significantly across sources: H(2) = 4.74, p = .094. Originality and funniness correlated positively for JEST (ρ = .554), negatively for GPT-4o (ρ = -.247), and weakly positively for GPT-5.4 (ρ = .239).

All automated measures significantly predicted human originality. Corpus Novelty led with ρ = .372, followed closely by Concept Distance Max at ρ = .369. PMI measures were weaker but significant: Raw Max ρ = .231, Decomposed Max ρ = .232, and Cluster Max ρ = .248. None significantly correlated with funniness (all p > .08). The Lasso composite used Corpus Novelty (51%), Concept Distance Max (43%), and PMI Decomposed Max (6%), producing in-sample ρ = .417, 10-fold cross-validated ρ = .401, and LOO ρ = .388.

## Takeaways
- Originality can be estimated with corpus novelty and handle-pair semantic distance, not just human judgment.
- The measures appear specific to originality, since they did not predict funniness.
- Combining full-text novelty, handle distance, and PMI gives a modest gain over individual measures.
- Systems that optimize for recognizable humor may also reproduce familiar joke patterns.

## Limitations & Caveats
The approach assumes jokes can be reduced to extractable handles, which may not hold for all humor. The reference corpus is only Reddit jokes, not all human humor or LLM training data. Human originality ratings are an imperfect target: pooled originality agreement was low, with κ = .187 and mean pairwise ρ = .240. Composite analyses also excluded jokes missing required handle-pair measures.
