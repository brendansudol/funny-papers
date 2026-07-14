# SMILE-Next: Teaching Large Language Models to Detect, Classify, and Reason about Laughter

**Lee Jung-Mok, Kim Sung-Bin, Joohyun Chang, Lee Hyun, Tae-Hyun Oh** — ACL 2026 · Guide entry Part 5 (real-world laughter benchmark) (Part 5 - Situated & Live Humor)

[paper page](https://aclanthology.org/2026.acl-long.2023/) · [local PDF](../pdfs/x43-smile-next.pdf) · [full markdown](../md/x43-smile-next/x43-smile-next.md) · [extract](../extracts/x43-smile-next.json)

## TL;DR
SMILE-Next introduces a real-world multimodal laughter-understanding dataset and a laughter-specialized LLM framework for detection, type classification, and reasoning. The core result is that text-only LLMs using textualized multimodal cues outperform raw audio-visual and visual LLM baselines, with best SMILE-Next scores including detection F1 0.9675, type-classification F1 0.8067, and reasoning SentBERT 0.7907.

## Problem & Motivation
Prior laughter and humor work often focuses on narrow tasks such as humor detection, humor intensity, or constrained explanation settings. The authors argue that real laughter in human interaction is broader: it can be mirthful, polite, sarcastic, awkward, socially bonding, or tension-reducing. Understanding it requires more than detecting an audio event; a system must identify whether laughter occurs, classify what kind of laughter it is, and explain why it happened in context.

## Approach
The paper contributes SMILE-Next and a laughter expert LLM. Instead of feeding raw video directly to an LLM, the method converts multimodal evidence into text: utterances, acoustic features, facial action units, video captions, and speaker relationship information. The authors then fine-tune LLMs on these textualized cues. Two training components are proposed: Laughter-specific Self-Instruct, which uses GPT-4 to synthesize additional laughter-centered instruction data, and Mixture-of-Laugh-Experts (MoLE), a LoRA-based soft-routed expert architecture with three task-specific experts.

## Data & Experimental Setup
SMILE-Next contains 3,590 video clips and 6,386 question–answer pairs: 2,384 for laughter detection, 1,957 for laughter type classification, and 2,045 for laughter reasoning. Sources include TED Talks, sitcoms, YouTube videos, dyadic conversations, talk shows, and movies. GPT-4 generated pseudo-reasoning labels, which AMT annotators verified or corrected; AMT workers also labeled laughter types, with three annotators per instance and Fleiss’ Kappa 0.42195. The paper evaluates MiniCPM-o-v2.6, Qwen2.5-Omni-7B, Qwen2.5-VL, Video-LLaVA, Vicuna-v1.5-7B, LLaMA3, and Qwen2.5. Metrics are F1/accuracy for classification tasks and BLEU4, METEOR, ROUGE_L, and SentBERT for reasoning.

## Results
On SMILE-Next detection, Vicuna-v1.5 achieved F1 0.9675 and accuracy 0.9696; LLaMA3 tied the accuracy at 0.9696. On type classification, LLaMA3 was best with F1 0.8067 and accuracy 0.8425, compared with the strongest visual baseline Video-LLaVA at F1 0.7589 and accuracy 0.7912. For reasoning, LLaMA3 led BLEU4 and METEOR with 0.2427 and 0.2328, while Vicuna-v1.5 led ROUGE_L and SentBERT with 0.4191 and 0.7907. Human preference also favored the proposed LLM: against V-LLM it won 55.7% vs 37.4%, and against AV-LLM it won 69.0% vs 26.2%. Using full multimodal cues instead of transcripts alone improved Qwen2.5 detection F1 from 0.8613 to 0.9629 and type F1 from 0.4019 to 0.7094. MoLE added only +19 ms overall latency, from 1494 ms to 1513 ms.

## Takeaways
- Textualizing multimodal cues is central to the paper’s gains.
- Laughter evaluation should go beyond binary detection to include type and explanation.
- Synthetic laughter-specific instructions help broaden scenario coverage.
- Task-specialized LoRA experts can improve multi-task laughter modeling with small latency overhead.
- Human preference results support the automatic-metric conclusion that textualized cues improve reasoning quality.

## Limitations & Caveats
The dataset is primarily English and may underrepresent culturally specific laughter, rare cases, nuanced social norms, and complex group interactions. Human preference participant counts and decoding settings are not reported. Reasoning labels depend partly on GPT-4 pseudo-labels, although they are human-verified. The model still confuses mirthful and polite laughter and can over-interpret facial or acoustic cues.
