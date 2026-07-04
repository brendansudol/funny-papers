# Can Language Models Laugh at YouTube Short-form Videos?

**Dayoon Ko, Sangho Lee, Gunhee Kim** — EMNLP 2023 · Guide entry Part 3 (video humor) (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2310.14159) · [local PDF](../pdfs/x06-exfuntube.pdf) · [full markdown](../md/x06-exfuntube/x06-exfuntube.md) · [extract](../extracts/x06-exfuntube.json) · [dataset: ExFunTube](../../data/exfuntube/)

## TL;DR
The paper introduces ExFunTube, a dataset of 10,136 user-generated short-form YouTube videos with timestamps and text explanations for funny moments. It also proposes a zero-shot video-to-text prompting method that improves humor explanation by LLMs; GPT-3.5 with prompting reaches mean SentBERT 0.602, mean ROSCOE (RA) 0.817, and human rating 0.523, but remains below Gold explanations at 0.792.

## Problem & Motivation
Prior video humor datasets mainly come from constrained domains such as TED speeches or sitcoms and often provide only binary funny/unfunny labels. The authors argue that binary labels do not show whether a model understands why a video is funny, especially when humor depends on both what is said and what is seen. ExFunTube is designed to test explanation of general multimodal humor in short-form user-generated videos.

## Approach
The dataset pipeline starts from videos shared on the r/youtubehaiku subreddit. A GPT-3.5-based filtering process keeps videos where visual information contributes to humor: it generates a video caption and transcript, checks whether GPT-3.5 can find funny utterances with and without the caption, and compares GPT-3.5 explanations with and without visual information using SentBERT similarity. The final method for model prompting converts each video into text: visual segments are captioned using BLIP-2 and InternVideo, speech is transcribed with Whisper and speaker-separated with ChatGPT, and sound tags are added. These components are arranged chronologically and passed to LLMs to generate explanations.

## Data & Experimental Setup
The authors initially crawl 220K videos and collect 21K high-quality multimodal humorous videos before manual safety filtering removes about 50%, leaving 10,136 videos. AMT workers annotate up to three funny moments per video with start/end timestamps and explanations, yielding 11,166 explanations averaging 44.3 words; 9,222 videos have one funny moment, 798 have two, and 116 have three. Experiments compare text-only T5 Large, BART Large, and GPT-3.5 text-davinci-003; MAF; VideoChat-Text; and the same LLMs with the proposed prompting. Finetuned models use five-fold cross-validation. Evaluation uses SentBERT, ROSCOE (RA), a QD-DETR moment-localization rationale quality score, and AMT human evaluation on 100 videos.

## Results
GPT-3.5 with prompting is the strongest generated system overall. It achieves mean SentBERT 0.602 versus 0.529 for text-only GPT-3.5, 0.541 for MAF, and 0.539 for VideoChat-Text. It reaches mean ROSCOE (RA) 0.817 versus 0.772 for text-only GPT-3.5. For rationale quality, GPT-3.5 improves from 18.8 to 5.5 at IoU @0.3 and from 22.5 to 9.3 at IoU @0.5, where lower is better. Human ratings also improve: GPT-3.5 with prompting scores 0.523 versus 0.385 for text-only GPT-3.5, while Gold explanations score 0.792. Ablation confirms multimodality: GPT-3.5 with all visual, speech, and sound inputs scores 0.602 SentBERT and 0.817 ROSCOE, compared with 0.512/0.778 without visual, 0.497/0.763 without speech, and 0.574/0.801 without sound.

## Takeaways
- Humor explanation is a stricter test than binary humor detection for short-form videos.
- Text-only transcripts are insufficient for this dataset; visual and audio context both matter.
- Converting multimodal evidence into structured text can outperform an end-to-end multimodal baseline on this task.
- Prompting helps especially for visually grounded humor categories such as Clownish humor, Visual gags, and Slapsticks.
- The gap to Gold explanations shows that video humor explanation remains unsolved.

## Limitations & Caveats
The dataset distributes URLs rather than videos because of copyright. The method depends on existing zero-shot models and uses text as the bridge between modalities. Sound timing is not modeled, although timing can be important for humor. Humor and explanations are subjective, and worker recruitment from AU, CA, GB, NZ, and US may introduce cultural and geographic bias.
