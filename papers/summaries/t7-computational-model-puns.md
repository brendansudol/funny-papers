# A Computational Model of Linguistic Humor in Puns

**Justine T. Kao, Roger Levy, Noah D. Goodman** — Cognitive Science 40(5):1270-1285 · Guide entry T7 (Theory Foundations)

[paper page](https://doi.org/10.1111/cogs.12269) · [local PDF](../pdfs/t7-computational-model-puns.pdf) · [full markdown](../md/t7-computational-model-puns/t7-computational-model-puns.md) · [extract](../extracts/t7-computational-model-puns.json)

## TL;DR
This paper proposes a computational account of why phonetic puns are funny, based on two information-theoretic measures derived from a noisy-channel model of sentence understanding. Across 435 English sentences, both ambiguity and distinctiveness distinguished puns from non-puns, and distinctiveness predicted fine-grained funniness within 145 puns (r = .28, p < .001).

## Problem & Motivation
The paper targets a gap between humor theory and computational modeling. Incongruity theories claim that humor often involves multiple incompatible meanings, but the authors argue that these ideas need precise, testable measures. Puns are used as a controlled test case because a phonetic ambiguity, such as “hare” versus “hair,” can map one sentence surface form onto two possible meanings. The key question is not merely whether a sentence contains an ambiguous word, but whether both meanings are contextually plausible and whether different parts of the sentence support each meaning.

## Approach
The authors propose a simple probabilistic model of sentence processing. A sentence has a latent meaning m, approximated by either the observed ambiguous word or its homophone/near homophone. Each content word is either semantically relevant to that meaning or generated as noise from an n-gram process. From this model they derive two measures. Ambiguity is the entropy of P(m|w), so it is high when both meanings are similarly likely. Distinctiveness is the symmetrized Kullback-Leibler divergence between the distributions over relevant words under each meaning, so it is high when each interpretation is supported by a different subset of words.

## Data & Experimental Setup
The study uses 435 English sentences: 65 identical-homophone puns, 130 corresponding non-pun sentences, 80 near-homophone puns, and 160 corresponding non-pun sentences. Puns came from “Pun of the Day” and additional generated homophone puns; non-puns came from Heinle’s Newbury House Dictionary of American English. Funniness ratings were collected on Amazon Mechanical Turk on a 1–7 scale: 100 participants rated the 195 identical-homophone sentences and 160 participants rated the 240 near-homophone sentences, with non-native English speakers removed. To estimate semantic relatedness, participants also rated 1,460 word pairs for identical-homophone sentences and 2,056 word pairs for near-homophone sentences. Google N-grams and Google Web unigrams supplied language statistics.

## Results
Identical and near-homophone puns did not differ significantly in funniness (t(130.91) = 0.13, p = .896), ambiguity (t(137.80) = 1.13, p = .261), or distinctiveness (t(134.91) = -0.61, p = .543), so the authors collapsed across them. Puns scored higher than non-puns on ambiguity (t(159.48) = 7.89, p < .0001) and distinctiveness (t(248.99) = 6.11, p < .0001). A regression using both measures predicted averaged funniness ratings with F(2, 432) = 74.07, R^2 = 0.25, p < .0001; coefficients were 1.915 for ambiguity and 0.264 for distinctiveness, both p < .0001. Within the 145 puns, ambiguity did not correlate with funniness (r = .03, p = .697), but distinctiveness did (r = .28, p < .001). Puns in the top distinctiveness quartile were funnier than lower-quartile puns (t(90.15) = 3.41, p < .001).

## Takeaways
- Ambiguity helps separate puns from ordinary sentences with ambiguous words.
- Distinctiveness matters for ranking which puns are funnier.
- Humor systems should model not only multiple meanings, but also which context words support each meaning.
- The method gives interpretable support sets that can function like lightweight pun explanations.

## Limitations & Caveats
The scope is narrow: written English phonetic puns, not spoken humor, dialogue, discourse, or complex jokes. Sentence meaning is approximated by homophone meanings, and semantic relatedness is supplied by human ratings rather than learned automatically. The authors note that richer models may need pragmatics, background knowledge, time-course processing, and script-level representations.
