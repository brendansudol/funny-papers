# Pun Generation with Surprise

**He He, Nanyun Peng, Percy Liang** — NAACL 2019 · Guide entry Part 2 (learned-generation anchor) (Part 2 - Generating Jokes)

[paper page](https://aclanthology.org/N19-1172/) · [local PDF](../pdfs/x16-pun-generation-surprise.pdf) · [full markdown](../md/x16-pun-generation-surprise/x16-pun-generation-surprise.md) · [extract](../extracts/x16-pun-generation-surprise.json)

## TL;DR
The paper proposes an unsupervised method for generating homophonic puns from non-humorous text, given a pun word and an alternative homophone. Its central idea is local-global surprisal: a good pun word should be unexpected in its immediate context but supported by the wider sentence. The best system, SURGEN, reaches 31.4% success in human evaluation, compared with 9.2% for an adapted NEURALJOINTDECODER baseline and 78.9% for expert-written puns.

## Problem & Motivation
The task is to generate a pun sentence containing only the pun word, while evoking both the pun word and an alternative homophone, such as dyed and died. The authors argue that supervised generation is inappropriate because there is no large pun corpus and because mimicry conflicts with novelty. They also argue that ambiguity alone is insufficient: a pun must create surprise and then support resolution.

## Approach
The paper defines local-global surprisal using a language-model probability ratio between the pun word and the alternative word. Local surprisal measures the immediate context around the pun word; global surprisal measures the whole sentence. The desired pattern is that the pun word is more surprising locally than globally.

For generation, the authors build SURGEN, a retrieve-and-edit system. It retrieves BookCorpus sentences containing the alternative word, swaps the alternative word for the pun word, and inserts a topic word related to the pun word near the beginning of the sentence. Topic words come from a distant skip-gram model trained on sentence-level word co-occurrence, and replacements are filtered using WordNet path similarity for type consistency. A smoother variation uses a sequence-to-sequence model to rewrite neighboring words around the inserted topic.

## Data & Experimental Setup
The authors use the SemEval-2017 Task 7 pun dataset, which contains 1099 human-written puns annotated with pun words and alternative words, taking 219 for development. BookCorpus supplies the generic corpus for retrieval and for training system components, and a neural language model trained on WikiText-103 supplies probabilities for surprisal and unusualness.

For metric analysis, they collect AMT funniness ratings for 130 sentences: 33 puns, 33 swap-puns, and 64 non-puns. They also analyze the KAO dataset with 141 puns and 257 non-puns. For generation, they evaluate 150 pun/alternative word pairs. AMT workers rate success, funniness, and grammaticality; each generated sentence receives 5 ratings.

## Results
For puns versus non-puns, local-global surprisal has Spearman correlations of 0.46 on SEMEVAL and 0.58 on KAO, with p=0.00 for both. For puns versus swap-puns, it reaches 0.48 with p=0.00, while ambiguity, distinctiveness, and unusualness are not significant there.

In generation, SURGEN has the best automatic-system success rate: 31.4%, beating NEURALJOINTDECODER at 9.2% by 22.2 percentage points and retrieval at 4.6% by 26.8 points. It also beats RETRIEVE+SWAP at 27.0% and RETRIEVE+SWAP+TOPIC+SMOOTHER at 28.8%. Its funniness score is 1.7, tied with the smoother variation, versus 1.4 for NEURALJOINTDECODER and 3.0 for human puns. Grammar shows a tradeoff: retrieval scores 3.9, human puns 3.8, SURGEN 3.0, and NEURALJOINTDECODER 2.6. Pairwise, SURGEN beats NEURALJOINTDECODER on funniness in 56.7% of cases and loses in 25.3%.

## Takeaways
- Surprise matters: replacing the pun word with the alternative word creates ambiguous but less funny swap-puns.
- Retrieve-and-edit is more effective here than neural joint decoding conditioned on two meanings.
- Adding topic support improves pun success but can damage grammaticality.
- Automatic metrics can help detect puns, but they do not reliably rank quality within puns.

## Limitations & Caveats
SURGEN is still far below expert-written puns: 31.4% success versus 78.9%. The authors report failures from weak local association, pun words not fitting the seed sentence, bad or unrelated topic words, grammatical errors, and missing seed or topic candidates. They also state that language models conflate creativity with nonsense, making direct optimization difficult.
