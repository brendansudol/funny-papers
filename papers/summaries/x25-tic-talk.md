# Timing In stand-up Comedy: Text, Audio, Laughter, Kinesics (TIC-TALK): Pipeline and Database for the Multimodal Study of Comedic Timing

**Yaelle Zribi, Florian Cafiero, Vincent Lépinay, Chahan Vidal-Gorène** — CHum 2026 · Guide entry Part 5 (timing as multimodal data) (Part 5 - Situated & Live Humor)

[paper page](https://aclanthology.org/2026.chum-1.2/) · [local PDF](../pdfs/x25-tic-talk.pdf) · [full markdown](../md/x25-tic-talk/x25-tic-talk.md) · [extract](../extracts/x25-tic-talk.json) · [dataset: TIC-TALK](../../data/tic-talk/)

## TL;DR
TIC-TALK is a multimodal resource and pipeline for studying stand-up comedy timing across 90 professionally filmed Netflix specials. It aligns 5,416 topic segments with detected laughter, shot labels, and pose-derived movement signals, and the strongest descriptive result is that topic-level kinetic energy negatively correlates with laughter rate (r = -0.75, N = 24).

## Problem & Motivation
The paper argues that computational humor work has focused heavily on verbal content, while stand-up comedy depends on timing, embodied delivery, editing, and audience response. The authors define comedic timing as short-lag coordination across text, gesture, and audience response in live delivery. Their goal is not to model jokes fully, but to make timing, gesture, and laughter measurable at corpus scale.

## Approach
The pipeline processes each modality at its own temporal resolution. Subtitles are segmented into time blocks, embedded with all-MiniLM-L6-v2, and modeled with BERTopic; 60 s blocks receive topic IDs and retain 384-dimensional embeddings. Audio is processed with Whisper-AT at a 0.8 s stride to detect contiguous laughter events with labels and confidence scores. Video is processed at 1 fps with a fine-tuned YOLOv8-cls shot classifier and YOLOv8s-pose for 17-joint keypoints on full-body frames. From raw keypoints, the paper computes arm spread, kinetic energy, and trunk lean, then aligns streams by hierarchical temporal containment rather than resampling.

## Data & Experimental Setup
TIC-TALK contains derived annotations for 90 stand-up performances from 2015–2024. The average runtime per show is 63 min, for a total of ≈94 h. The unified dataset has 5,416 topic segments, 322,973 video frames at 1 fps, and full-body pose coverage for 22% of frames. The shot classifier was trained on 594 manually annotated frames and validated on 128 held-out samples. The predictive benchmark samples 285,916 non-laughter anchor points at 1 s steps; positives are anchors where a new laughter event begins in the next 2 s. Shows are split by group into 62 train, 14 validation, and 14 test shows.

## Results
The shot classifier reached average F1 = 0.91. In the descriptive use case, mean laughter coverage was 17.8% with ≈1.2 events/10 s. Kinetic energy was the strongest cross-modal correlate of laughter rate, with Pearson r = -0.75 across 24 topics. High-laughter topics included body/dress/boobs (0.253), baby/abortion (0.248), food/want/chef (0.230), and romantic relationships (0.222), while indian/trump/india scored 0.141 and iceland/icelandic 0.085. Close-up proportion correlated weakly with laughter rate (r = +0.28, N = 24). In onset prediction, history-only achieved AUROC = 0.643 and AUPRC = 0.275. The full text + vision + history system was best with AUROC = 0.647, AUPRC = 0.277, F1 = 0.342, precision = 0.248, and recall = 0.553, only +0.004 AUROC over history-only. Its AUPRC was above the random baseline of 0.170, a 1.6× lift.

## Takeaways
- For humor-system builders, audience laughter history is a strong baseline: it explains most short-horizon predictability in this setup.
- Text and vision add only small gains at 60 s topical granularity, but text + vision beats either alone.
- Pose-derived stillness may be an important signal, but the paper treats the result as correlational rather than causal.
- Camera framing matters analytically because professionally edited specials mix performance with montage.

## Limitations & Caveats
The corpus is restricted to Netflix specials and therefore reflects platform selection and professional editing conventions. Topic blocks do not model setups, punchlines, callbacks, or joke structure. The main correlations may be confounded by performer style, mobility, filming choices, and an artefactual topic. The released data exclude audio, images, and video, providing only derived annotations.
