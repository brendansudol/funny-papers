# StandUp4AI: A New Multilingual Dataset for Humor Detection in Stand-up Comedy Videos

**Valentin Barriere, Nahuel Gomez, Leo Hemamou, Sofia Callejas, Brian Ravenet** — arXiv:2505.18903 · Guide entry #44 (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2505.18903) · [local PDF](../pdfs/44-standup4ai.pdf) · [full markdown](../md/44-standup4ai/44-standup4ai.md) · [extract](../extracts/44-standup4ai.json) · [dataset: StandUp4AI](../../data/standup4ai/)

## TL;DR
StandUp4AI introduces a multilingual stand-up comedy video dataset for humor and laughter detection, covering seven languages and 334.2 hours of performances. The paper’s strongest empirical result is that its ASR-based laughter enhancement improves manually evaluated laughter detection from F1 0.51 with the Omine et al. (2024) off-the-shelf model to F1 0.58 with filtered candidates at IoU threshold 0.2.

## Problem & Motivation
Most video humor detection work treats humor as sequence classification, usually detecting a punchline at the end of a segment. The authors argue that this misses how stand-up and conversational humor work: multiple laughs can occur inside one sentence, and tags after punchlines can keep laughter going. They therefore frame laughter prediction as word-level sequence labeling, where a model continuously predicts when audience laughter should occur.

## Approach
The paper contributes both a dataset and a data-cleaning method. StandUp4AI is built from online stand-up videos, with transcripts produced using Whisper and WhisperX and laughter initially detected using the Omine et al. (2024) model. The authors observe complementary ASR timestamp errors around laughter: Whisper often merges laughter duration with the following word, while WhisperX often merges it with the previous word. Their method finds intersections between the two transcripts to insert candidate laughter segments, then filters candidates with a Random Forest classifier using acoustic features.

For humor modeling, each word receives a binary label indicating whether laughter occurs right after it or continues through it. Fine-tuned xlm-roberta-base sequence labelers are trained under multilingual and monolingual settings.

## Data & Experimental Setup
StandUp4AI contains 3,617 videos, 334.2 hours, 2,887,402 words, and 128,194 laughter labels. The seven languages are English, Spanish, Italian, Hungarian, Czech, French, and Portuguese. The manually annotated test set contains 70 videos, 10 per language, with laughter timestamps annotated at 0.1 seconds using Audacity and manually checked ASR outputs.

For candidate laughter validation, the authors annotated 376 candidates from 50 videos; 208 were real laughter events missed by the off-the-shelf detector. The Random Forest used acoustic features extracted with librosa. Sequence labelers used a maximum sequence length of 512, a stride of 128, Adam, 10 epochs, and learning rate 1e − 5.

## Results
The Random Forest candidate laughter classifier achieved Laughter precision 0.89, recall 0.81, and F1 0.85; macro precision, recall, and F1 were 0.84, 0.84, and 0.83. On the manually annotated test set with IoU threshold 0.2, Omine et al. (2024) scored precision 0.68, recall 0.41, and F1 0.51. Using all candidates scored F1 0.56, and filtered candidates scored precision 0.70, recall 0.49, and F1 0.58.

For word-level sequence labeling against manual annotations, the multilingual enhanced model reached the best average F1, 42.4. The multilingual raw model averaged 42.2, while monolingual enhanced models averaged 39.4. On the automatic test set, multilingual enhanced again led with Avg. F1 28.7, compared with 27.9 for monolingual enhanced and 26.9 for monolingual raw.

## Takeaways
- Modeling stand-up humor as word-level laughter prediction better matches repeated laughs and post-punchline tags than end-of-sequence classification.
- ASR errors can be useful signals: combining Whisper and WhisperX timestamps uncovered missed laughter candidates.
- Multilingual training was stronger than monolingual training in the reported baselines.
- The dataset includes multimodal resources, but the first baselines are intentionally text-only.

## Limitations & Caveats
The current humor detection experiments are unimodal text baselines. The paper does not model laughter intensity, cites remaining ASR-error issues for dialects, slang, and vulgarity, and notes that YouTube videos may disappear. The authors release metadata and annotations, not the video or audio content.
