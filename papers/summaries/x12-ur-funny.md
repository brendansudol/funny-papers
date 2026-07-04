# UR-FUNNY: A Multimodal Language Dataset for Understanding Humor

**Md Kamrul Hasan, Wasifur Rahman, Amir Zadeh, Jianyuan Zhong, Md Iftekhar Tanveer, Louis-Philippe Morency, Mohammed (Ehsan) Hoque** — EMNLP 2019 · Guide entry Part 8 (pre-LLM anchor) (Part 8 - Datasets & Shared Tasks)

[paper page](https://aclanthology.org/D19-1211/) · [local PDF](../pdfs/x12-ur-funny.pdf) · [full markdown](../md/x12-ur-funny/x12-ur-funny.md) · [extract](../extracts/x12-ur-funny.json) · [dataset: UR-FUNNY (repo)](../../data/ur-funny/)

## TL;DR
UR-FUNNY introduces a multimodal humor detection dataset built from TED talks, with transcript text, acoustic features, and visual facial features aligned around context and punchline. The best baseline, C-MFN using text, acoustic, and visual modalities, reaches 65.23% accuracy, well below the reported human performance of 82.5%.

## Problem & Motivation
The paper argues that humor in face-to-face communication is not only textual: speakers use words, gestures, facial behavior, and prosodic cues. Prior humor detection datasets in NLP were mostly text-only, or at most included audio, and often used negative samples from different domains. The authors target a more realistic setting: decide whether a sequence of sentences in a speech, including the build-up and punchline, will trigger immediate audience laughter.

## Approach
The dataset is constructed from TED talks. The authors use TED transcript laughter markers as the indicator of humor: the sentence immediately before a laughter marker is treated as the punchline, and preceding sentences up to the previous laughter marker or video start are treated as context. Negative samples are chosen at random intervals from the same videos, with the last sentence not followed by laughter. Forced alignment provides word-level timing so text, visual, and acoustic streams can be aligned.

The paper also proposes Contextual Memory Fusion Network, or C-MFN, as a baseline. It first encodes each modality in the context with LSTMs, fuses multimodal context using a self-attention encoder, and uses these context representations to initialize a Memory Fusion Network that models the punchline.

## Data & Experimental Setup
UR-FUNNY contains 1,866 videos from 1,741 speakers across 417 topics. It has 16,514 segments total: 8,257 humor instances and 8,257 non-humor instances. Total duration is 90.23 hours, with 965,573 words and 63,727 sentences. The average instance lasts 19.67 seconds, with 14.7 seconds of context and 4.97 seconds of punchline.

The standard folds are speaker independent: train has 5,306 humor and 5,292 non-humor instances, validation has 1,313 and 1,313, and test has 1,638 and 1,652. Text features use GloVe. Acoustic features are 81 COVAREP features. Visual features are OpenFace facial Action Units and facial shape parameters. Experiments compare C-MFN, punchline-only C-MFN (P), context-only C-MFN (C), and a Random Forest baseline across modality settings: T, A+V, T+A, T+V, and T+A+V.

## Results
The best result is C-MFN with all three modalities, at 65.23% accuracy. This beats the strongest Random Forest result, 57.78%, by 7.45 percentage points, and the cited prior unimodal punchline/text result of 58.9% by 6.33 points.

Both punchline and context matter. With T+A+V, full C-MFN scores 65.23%, punchline-only C-MFN (P) scores 64.47%, and context-only C-MFN (C) scores 58.45%. Thus full context-plus-punchline modeling beats punchline-only by 0.76 points and context-only by 6.78 points.

Modalities also matter. Full C-MFN scores 64.44 with text alone, 57.99 with acoustic plus visual, 64.47 with text plus acoustic, 64.22 with text plus visual, and 65.23 with all three. Human performance is reported as 82.5%, with annotators agreeing 84% of times.

## Takeaways
- Treating humor as multimodal improves results: the best setting uses text, acoustic, and visual features together.
- Punchlines carry the strongest signal, but context still helps.
- Speaker-independent splits are important because the dataset has many speakers and aims to avoid overfitting to identity or communication style.
- A large gap remains between the best model and human performance, so UR-FUNNY is meant as a challenging benchmark.

## Limitations & Caveats
The labels are based on audience laughter markers, so the task is laughter prediction rather than a broader manually judged humor label. TED camera work changes frequently, and the paper notes that the speaker’s face was the only consistently available visual source. Human performance was estimated from only 100 humor and 100 non-humor cases with two annotators.
