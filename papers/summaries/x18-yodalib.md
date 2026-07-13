# “Judge me by my size (noun), do you?” YodaLib: A Demographic-Aware Humor Generation Framework

**Aparna Garimella, Carmen Banea, Nabil Hossain, Rada Mihalcea** — COLING 2020 · Guide entry Part 2 (learned-generation anchor) (Part 2 - Generating Jokes)

[paper page](https://aclanthology.org/2020.coling-main.253/) · [local PDF](../pdfs/x18-yodalib.pdf) · [full markdown](../md/x18-yodalib/x18-yodalib.md) · [extract](../extracts/x18-yodalib.json)

## TL;DR
YodaLib is a BERT-based framework for generating funny Mad Lib-style stories tailored to a target location, India or the United States. Its strongest result is that Yoda_US receives the best TOP3 mean funniness grades: 2.03 from IN judges and 1.77 from US judges, outperforming human FreeText completions, a generic MLM baseline, and the reported Libitum score of 1.51.

## Problem & Motivation
Humor is subjective, and the paper argues that demographic differences affect how humor is produced and judged. The authors study Mad Libs-style humor generation, where funny stories are created by filling blanks with prompted word types. Their goal is to generate coherent and funny stories automatically while accounting for the target audience’s location.

## Approach
YodaLib has three stages. First, a location-biased BERT_base masked language model proposes blank-filling candidates after further training on Indian and US blog posts. Second, FunnyBERT, a BERT sentence-pair classifier, ranks filled-in sentences by whether they are funny transformations of the masked originals. Third, story completion selects funny sentence transformations while also considering coherence, estimated using cosine similarity over location-specific BERT sentence embeddings. Candidate selection keeps the highest ranking k = 10,000 words, then uses top n = 100 candidates during left-to-right filling; story completion advances the top N = 100 stories.

## Data & Experimental Setup
The authors use Fun Libs from Hossain et al. (2017), discard 4 of the 50 stories because their themes cater to a US audience, and replace them with 4 new stories. AMT annotation has selected judges and players: 50 US and 43 IN judges are selected from 60 and 100 candidates, and 30 IN and 26 US players are selected from 80 and 60 turkers. Stories are filled by 3 players from each country and judged by 5 judges from the same country, with opposite-country judgements for test stories. The location-biased language model is trained on 35K blogs and 17M tokens for IN, and 33K blogs and 12M tokens for US. FunnyBERT datasets contain TRAIN funny/not funny counts of IN 566/130 and US 574/122, VALIDATION counts of IN 173/49 and US 193/29, and TEST counts of IN 137/94 and US 210/21.

## Results
FunnyBERT validation accuracy is 84.39 for IN and 88.60* for US, versus a 50% majority vote baseline. In story generation, Yoda_US is best. For IN judges in TOP3, it scores 2.03, compared with Yoda_IN 1.94, FT_US 1.57, FT_IN 1.17, and MLM 0.70. For US judges in TOP3, it scores 1.77, compared with Yoda_IN 1.56, FT_US 1.41, FT_IN 1.39, and MLM 0.68. In TOP10, Yoda_US scores 1.70 for IN judges and 1.48 for US judges, while MLM scores 0.91 and 0.84. YodaLib also beats Libitum’s reported 1.51 in the closest TOP3 setting. YodaLib outperforms FreeText for 28 and 23 stories, with average gains of 0.79 and 0.46 for IN judges, and 0.17 and 0.37 for US judges, for IN- and US-generated stories respectively.

## Takeaways
- Location matters: US-slanted humor is preferred by both IN and US judges in this setup.
- A generic MLM is a weak humor generator because it favors plausible, coherent words rather than surprise.
- Coherence helps humans write strong humor, but YodaLib mostly succeeds through incongruity and deviation.
- IN judges appear more lenient, while US judges appear more coherence-sensitive.

## Limitations & Caveats
The study only covers location, and only IN and US. The story set is limited to 50 Fun Lib-style stories. The authors state that YodaLib still struggles to generate coherent humor like skilled humans, and future work should expand to more stories, more demographics, and better models of textual humor coherence.
