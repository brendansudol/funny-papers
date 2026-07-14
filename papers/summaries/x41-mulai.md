# Introducing MULAI: A Multimodal Database of Laughter during Dyadic Interactions

**Michel-Pierre Jansen, Khiet P. Truong, Deniece S. Nazareth, Dirk K.J. Heylen** — LREC 2020 · Guide entry Part 5 (dyadic laughter and participant perception) (Part 5 - Situated & Live Humor)

[paper page](https://aclanthology.org/2020.lrec-1.534/) · [local PDF](../pdfs/x41-mulai.pdf) · [full markdown](../md/x41-mulai/x41-mulai.md) · [extract](../extracts/x41-mulai.json)

## TL;DR
MULAI is a multimodal database of laughter in dyadic human-human interactions, created to study conversational and humour-related laughter with social context. Its preliminary analysis finds that laughter acoustics do not correlate with participants’ own humour self-ratings, but some acoustic properties do correlate with how humorous their conversation partners perceive them to be.

## Problem & Motivation
The paper argues that existing laughter databases often lack the social context, modalities, and annotation consistency needed to study functionally different forms of social laughter. Many laughter datasets use posed laughter, stimulus-induced laughter, or limited modalities, whereas MULAI targets naturally interactive dyads and includes participant perceptions of humour. The authors emphasize that interlocutors may be better positioned than third-party annotators to judge humour because they understand the interaction context.

## Approach
The authors collected dyadic interactions across several task settings: a survival task, a make-the-other-laugh task, and a joke-telling task. Participants wore microphones, cameras, and Shimmer sensors capturing inertial movement, ECG, and GSR. After each task, participants rated both their own humorousness and their partner’s humorousness on five-point Likert scales. Laughter bouts, speech-laughs, and laughter-related respirations were annotated in Praat using elements of a prior laughter annotation scheme, and duration, mean pitch, and mean intensity were extracted from laughter bouts.

## Data & Experimental Setup
The database includes 13 sessions and 26 consenting participants, after 6 of 32 participants were excluded for not consenting to database inclusion. Participants had age M = 24, SD = 2.3; 14 were male and 12 female; a majority were Dutch (N=17), and all spoke English. MULAI contains 357 minutes of recorded video-, audio-, and physiological streams. The annotated part spans 134 minutes and includes 601 annotated laughter bouts, 168 annotated speech-laughs, and 538 laughter related events. The preliminary analysis excludes speech-laughter and focuses on laughter bouts from the make-the-other-laugh and joke-telling tasks.

## Results
Self-rated humour and partner-perceived humour were not significantly correlated in conversational tasks (ρ = 0.03, p = 0.527), but were significantly positively correlated in joke-telling tasks (ρ = 0.22, p<.001). In linear mixed models, duration, pitch, and intensity did not significantly predict humour self-ratings in either task. For partner ratings, conversational laughter pitch was significant (β = 0.0010, p = 0.0239) and intensity was significant (β = 0.0234, p = 0.0002). In joke-telling, duration was a significant negative predictor (β = -0.0675, p = 0.0413), while intensity was a significant positive predictor (β = 0.0163, p = 0.0226).

## Takeaways
- Perceived humour in interaction is not captured by self-ratings alone; partner ratings behave differently.
- Acoustic intensity is the most consistent reported correlate of partner-perceived humour across task settings.
- The relationship between laughter acoustics and humour perception appears task dependent.
- MULAI is useful for researchers studying social laughter, multimodal expression, physiological responses, and personality-linked differences in laughter.

## Limitations & Caveats
The reported significant correlations are small, and the authors note that unexplored factors such as joke content or laugh-elicitation strategy may matter more. Speech-laughter is excluded from the preliminary analysis. The paper does not report inter-annotator agreement or the number of laughter annotators. Several resources are planned for future work, including transcripts, strategy annotations, pair familiarity, survival-task annotations, and function/context labels for individual laughs.
