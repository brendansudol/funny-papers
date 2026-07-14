# "Cheese!": a corpus of face-to-face French interactions. A case study for analyzing smiling and conversational humor

**Béatrice Priego-Valverde, Brigitte Bigi, Mary Amoyal** — LREC 2020 · Guide entry Part 5 (smiling, uptake, and failed humor) (Part 5 - Situated & Live Humor)

[paper page](https://aclanthology.org/2020.lrec-1.59/) · [local PDF](../pdfs/x42-cheese.pdf) · [full markdown](../md/x42-cheese/x42-cheese.md) · [extract](../extracts/x42-cheese.json)

## TL;DR
This paper presents CHEESE!, a multimodal corpus of 11 French face-to-face dyadic conversations designed for studying smiling and conversational humor. Its exploratory analysis of two interactions finds that smiling, especially mean smile intensity, often marks humor, but the data do not show that simply smiling prevents humor from failing.

## Problem & Motivation
The authors aim to provide a high-quality French audio-video corpus for analyzing conversation, non-verbal behavior, and humor. CHEESE! was designed to support cross-cultural comparison with American English work on smiling during humorous productions, but this paper focuses on presenting the French corpus and demonstrating what kinds of analyses it enables. The central empirical questions are whether smiling frames or marks humor, and whether smiling affects the success or failure of conversational humor.

## Approach
The corpus contains dyadic interactions recorded in a soundproof room with separated headset microphones and two front-facing cameras. Participants first read canned jokes to each other and then conversed freely. For annotation, the authors used SPPAS to segment Inter-Pausal Units and generate time-aligned token, phoneme, syllable and activity tiers; MarsaTag generated POS-related annotations. Orthographic transcription was manual and verified. Smiles in two interactions were manually annotated in ELAN using the Smiling Intensity Scale, with 400 ms intervals rated from 0 (neutral face) to 4 (laughter). Humor was manually annotated in Praat; conversational humor items were labeled successful unless negative reactions occurred: acknowledged but answered seriously, ignored, or explicitly rejected.

## Data & Experimental Setup
CHEESE! consists of 11 mixed and non-mixed French face-to-face interactions, around 15 minutes each, with 22 native-French Linguistics students aged 20 to 40. Five interactions had enriched annotations at publication time. Two interactions, MA_PC and JS_CL, were manually annotated for smiling and humor. The smile annotations cover 2,610 smile intensities in MA_PC and 2,475 in JS_CL; double coding yielded Cohen’s Kappa 0.87 and 0.89. The five annotated dialogues contain 2,130 different words and 20,201 word occurrences.

## Results
Humorous production lasted 2.6 min in MA_PC out of 17.4 min, versus 7.03 min in JS_CL out of 16.5 min. Humor-item counts varied by participant: MA 23 (1.3/min), PC 32 (1.8/min), JS 39 (2.36/min), and CL 53 (3.2/min). Mean smile intensity was higher in humorous than non-humorous sequences for MA (2,26 vs 1,3), PC (2,13 vs 1,12), and JS (2,05 vs 1,43), but identical for CL (1,5 vs 1,5). Smiling was the most frequent facial behavior during humor production. Failed humor was less frequent than successful humor: MA 4/19, PC 13/19, JS 7/32, CL 5/48. However, smiles also occurred frequently in failed humor, so smile presence alone did not predict success. Mean smile intensity was higher for successful than failed humor for PC, JS, and CL, but MA showed the opposite pattern.

## Takeaways
- CHEESE! is useful for multimodal analysis of French conversational humor, especially because it combines speech, video, transcription, and smile-intensity annotation.
- Smiling appears more central than laughter as a visible marker of humor in these interactions.
- For humor systems or annotation schemes, binary smile presence may be too coarse; smile intensity may carry more useful information.
- Success/failure of humor cannot be inferred from smile presence alone in this small study.

## Limitations & Caveats
The exploratory analysis uses only two interactions and four participants. Humor annotation was done by one author, without reported reliability. The paper reports descriptive statistics only, and the authors caution that possible gender and topic effects require analysis of the full corpus.
