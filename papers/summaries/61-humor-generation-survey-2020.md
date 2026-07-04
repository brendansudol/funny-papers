# A Survey on Approaches to Computational Humor Generation

**Miriam Amin, Manuel Burghardt** — LaTeCH-CLfL 2020 · Guide entry #61 (Part 9 - Surveys & Resources)

[paper page](https://aclanthology.org/2020.latechclfl-1.4/) · [local PDF](../pdfs/61-humor-generation-survey-2020.pdf) · [full markdown](../md/61-humor-generation-survey-2020/61-humor-generation-survey-2020.md) · [extract](../extracts/61-humor-generation-survey-2020.json)

## TL;DR
This survey reviews text-based computational humor generation systems for jokes and short humorous texts, grouping them into neural and template-based approaches. Its central result is a trade-off: no surveyed system reaches the highest rank in both humorousness and complexity; neural systems get H=3, C=1, while the best template systems get H=1 but lower complexity ranks.

## Problem & Motivation
The paper addresses a longstanding gap in computational humor generation: many systems have been proposed since the early 1990s, but no system has generated jokes like humans, and the field lacks a standardized basis for comparing systems. The authors focus only on verbal/textual humor, not visual humor. They argue that comparison should consider linguistic humor theories because jokes typically rely on incongruity between two interpretations, scripts, or frames and on some form of resolution.

## Approach
The survey first separates systems into neural and template-based generators. The neural group includes Yang and Sheng’s current-affair joke generator, trained with an LSTM RNN, and Yu et al.’s neural pun generator using joint and highlight models. The larger template-based group is subdivided by how systems select variables for templates: ontologies and lexicons, quantitative measures such as frequency and co-occurrence, or hybrid combinations. The paper proposes two comparison criteria: humorousness, meaning whether output is identifiable as a joke or humorous text, and complexity, meaning variety in syntax, lexical choices, and joke mechanisms.

## Data & Experimental Setup
The paper does not run new generation experiments. Instead, it analyzes published systems and examples. It discusses resources used by those systems, including a dataset of 7,699 Conan O’Brien jokes and news data for Yang and Sheng; the Wikipedia text corpus for Yu et al.; WordNet, ConceptNet, UniSyn, and the CMU pronouncing dictionary for several template systems; Google n-gram data for quantitative systems; and an SMS Corpus for lexical replacement humor. The authors rank 12 systems in Table 1 on humorousness (H) and complexity (C) using a 1–3 scale where 1 is stated as the highest rank.

## Results
The clearest finding is that no system achieves the top rank on both criteria. The two neural systems, current affair joke generation and homographic pun generation, are assigned H=3, C=1: they are judged highly complex but not humorous. Several template-based systems receive H=1: LIBJOG; JAPE and STANDUP; Hong and Ong’s question-answer joke patterns; Labutov and Lipson’s ConceptNet circuits; and Petrović and Matthews’ humorous analogy generator. These therefore beat the neural systems by two rank levels on humorousness, but their complexity values are C=2 or C=3. Middle-ranked systems include HAHAcronym, Japanese Standup, PUNDA, the ambiguous compound generator, and the humorous SMS generator, all at H=2, C=2. One concrete system-level number reported is that Hong and Ong’s T-PEG extracted 39 templates, of which 27 (69 %) were found usable.

## Takeaways
- Template constraints help produce identifiable jokes, but restrict diversity.
- Neural generators offer more lexical and syntactic freedom, but the surveyed examples fail as jokes.
- Evaluation practices are weak: most prior work relies on human Likert ratings of individual outputs, and sample selection is often unclear.
- Builders of humor systems should not evaluate only best examples; random outputs and system-level diversity matter.
- The authors recommend more explicit use of linguistic humor theories, especially the surprise disambiguation model and SSTH.

## Limitations & Caveats
The survey’s own ranking is qualitative and has no computable metric. The authors note that they could only judge published examples, usually 3–5 per system, and those examples may have been manually filtered. The paper excludes non-textual humor and does not run the surveyed systems itself.
