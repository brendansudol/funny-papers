# “So You Think You’re Funny?”: Rating the Humour Quotient in Standup Comedy

**Anirudh Mittal, Pranav Jeevan, Prerak Gandhi, Diptesh Kanojia, Pushpak Bhattacharyya** — EMNLP 2021 · Guide entry Part 5 (laughter-and-performance anchor) (Part 5 - Situated & Live Humor)

[paper page](https://aclanthology.org/2021.emnlp-main.789/) · [local PDF](../pdfs/x24-open-mic-humor-quotient.pdf) · [full markdown](../md/x24-open-mic-humor-quotient/x24-open-mic-humor-quotient.md) · [extract](../extracts/x24-open-mic-humor-quotient.json) · [dataset: Open Mic humor quotient dataset](../../data/open-mic-humor-quotient/)

## TL;DR
This paper introduces the Open Mic humor quotient dataset, a multimodal English stand-up comedy dataset rated on a five-point scale using detected audience laughter. Its central result is that a multimodal model using RoBERTa-large textual features reaches 0.813 QWK against the paper’s automated scoring mechanism, while the laughter-based scores average 0.595 QWK against human annotators.

## Problem & Motivation
The paper argues that rating humour is difficult because humour is subjective, culturally dependent, and often interpreted differently by different people. Human annotation is also costly and may not provide an objective measure. Stand-up comedy offers a natural signal: live audience laughter. The authors use that signal to create an automatically scored dataset and to train models that predict a clip’s “funniness” without relying on laughter being present at inference time.

## Approach
The scoring method detects audience-laughter intervals in each clip, sums their durations, and divides by the clip duration to remove the bias that longer clips might contain more jokes. The resulting normalized laughter score is mapped to a 0–4 Likert-scale rating using thresholds based on the mean and standard deviation of all scores. Before model training, audience laughter is muted so the system cannot simply use laughter as a shortcut. Audio features and textual embeddings are processed through separate Bi-LSTM pathways, concatenated, and classified into one of five rating classes.

## Data & Experimental Setup
The paper gathers 36 English stand-up comedy shows from 32 comedians and segments them into 927 roughly two-minute clips. It also adds 128 roughly two-minute TED talk clips as “unfunny” samples. Table 1 totals 1055 clips across ratings 0–4: 233 rated 4, 185 rated 3, 256 rated 2, 253 rated 1, and 128 rated 0. The train-test split is 70-30. Three annotators, aged 21–33, rated clips based solely on audience laughter feedback. Textual features include GloVe, BERT-base, BERT-large, DistilBERT, RoBERTa-base, RoBERTa-large, and XLM; audio features include MFCCs, RMS energy, and spectrogram features.

## Results
Human inter-annotator agreement is reported as average pairwise Cohen’s Kappa 0.634, Fleiss’ Kappa 0.632, and Krippendorff’s alpha 0.632. The automated scoring mechanism agrees with human annotators at QWK 0.659 for Human A, 0.562 for Human B, 0.563 for Human C, and 0.595 on average. Against the scoring mechanism, GloVe reaches QWK 0.691, BERT-base 0.722, BERT-large 0.796, DistilBERT 0.721, RoBERTa-base 0.775, RoBERTa-large 0.813, and XLM 0.714. RoBERTa-large is best and is reported as improving by 12% points over the GloVe baseline. In an ablation, audio-based features score 0.66 QWK, beating text-based features at 0.48 QWK.

## Takeaways
- Audience laughter can serve as a scalable supervision signal for stand-up humour rating, not just binary humour detection.
- Muting laughter before feature extraction is essential if the target system must score clips without audience feedback.
- For this task, delivery-related audio cues matter strongly: audio-only features outperform text-only features in the ablation.
- Larger contextual text models help; RoBERTa-large and BERT-large are the strongest reported textual-feature settings.
- Intermediate humour levels are hardest, with mistakes concentrated around adjacent classes such as 2/3 and 3/4.

## Limitations & Caveats
The paper uses only three human annotators and plans more annotation in future work. The data is English and centered on stand-up comedy, with TED talks used as non-funny speech. The model struggles with sarcasm, irony, dark humour, and subtle comparisons. The paper also contains a size inconsistency: one sentence says 519 clips, while Table 1 and later discussion refer to 1055 clips/cases.
