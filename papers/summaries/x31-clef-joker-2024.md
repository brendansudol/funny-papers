# Overview of the CLEF 2024 JOKER Task 3: Translate puns from English to French

**Liana Ermakova, Anne-Gwenn Bosser, Tristan Miller, Adam Jatowt** — CLEF 2024 Working Notes, CEUR-WS Vol. 3740 · Guide entry Part 7 (shared-task ecosystem) (Part 7 - Cross-Cultural & Translation)

[paper page](https://ceur-ws.org/Vol-3740/#paper-167) · [local PDF](../pdfs/x31-clef-joker-2024.pdf) · [full markdown](../md/x31-clef-joker-2024/x31-clef-joker-2024.md) · [extract](../extracts/x31-clef-joker-2024.json)

## TL;DR
This paper is the overview of CLEF 2024 JOKER Task 3, a shared task on translating English puns into French while preserving wordplay. Ten teams submitted 20 official English-to-French runs, and one additional team submitted three English-to-Spanish open-task runs. On the French test set, Arampatzis_GoogleTranslate was best by automatic metrics, with BLEU 65.23 and BERT Score F₁ 91.85%, but pun-specific analysis shows that wordplay preservation remains very weak.

## Problem & Motivation
Puns exploit multiple meanings or similar sounds, so literal translation often destroys the joke or makes the text nonsensical. The task asks systems to preserve, as much as possible, both the form and meaning of the original wordplay, corresponding to Delabastita’s pun→pun strategy. The paper motivates the task with prior CLEF 2023 results: the highest manually evaluated success rate for translations preserving both form and sense was only 6% for French and 18% for Spanish.

## Approach
The paper reports the shared-task setup, participant approaches, and evaluation. Systems included commercial translation engines, LLM prompting, and neural translation models. The authors evaluate with BLEU, BERT Score, and an additional pun-location analysis: a generated French translation is marked as containing a location if it includes at least one exact word or phrase annotated as carrying multiple meanings in the corresponding reference translations.

## Data & Experimental Setup
The Task 3 training data has 1,405 English wordplay instances and 5,838 professional French translations; the maximum number of references per English pun is 29, and 72% have multiple references. The 2024 extension introduced 376 new distinct source texts with 832 French reference translations by professional French native-speaker translators. The official French test evaluation reports results over 376 distinct English texts and 832 references. For the location analysis, the authors use CLEF 2023 JOKER Task 2 annotations: 5,838 French translations of 1,405 English puns with 4,355 distinct locations. For Spanish, Olga’s three runs are compared on 215 English puns with 644 Spanish references.

## Results
On the French test set, Arampatzis_GoogleTranslate led BLEU with 65.23, ahead of Tomislav&Rowan_MarianMTModel and Arampatzis_MarianMT at 58.85, a difference of 6.38 BLEU. It also led BERT Score F₁ with 91.85%, narrowly ahead of Frane_TranslationModel at 91.77%. On the training data, fine-tuning changed the picture: UAms_Marian_ft achieved BLEU 68.56, while UAms_T5-base_ft scored 59.93; however, T5 led BERT Score F₁ with 83.80% versus 82.28% for Marian. Pun-location overlap was much lower than the general metrics suggest. UAmS_Marian_ft had the best overlap, 317/1,405 translations or 23%; UAmS_T5-base_ft had 179/1,405 or 13%; Google Translate had 141/1,405 or 10%. The paper summarizes that fine-tuned models reached at most 23%, while non-fine-tuned models used pun-location words in only 11% of cases.

## Takeaways
- Strong BLEU or BERT Score does not imply that a pun survived translation.
- Commercial MT, especially Google Translate, was strongest on the French test set by automatic metrics.
- Fine-tuning on the JOKER data helped on the training set and improved pun-location overlap.
- Evaluation for wordplay translation needs pun-aware measures, not only standard MT metrics.

## Limitations & Caveats
The test-set pun-location overlap is very small: only 13 distinct locations for 8 unique English puns overlap with the 2024 test data, so those results are not entirely interpretable. The location metric uses exact string matches only. Some submissions are partial, and no new Spanish references were created in 2024.
