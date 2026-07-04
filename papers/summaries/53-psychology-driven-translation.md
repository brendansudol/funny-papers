# Psychology-Driven Enhancement of Humour Translation

**Yuchen Su, Yonghua Zhu, Yang Chen, Diana Benavides Prado, Michael Witbrock** — arXiv:2507.09259 · Guide entry #53 (Part 7 - Cross-Cultural & Translation)

[paper page](https://arxiv.org/abs/2507.09259) · [local PDF](../pdfs/53-psychology-driven-translation.pdf) · [full markdown](../md/53-psychology-driven-translation/53-psychology-driven-translation.md) · [extract](../extracts/53-psychology-driven-translation.json)

## TL;DR
The paper proposes Humour Decomposition Mechanism (HDM), a Chain-of-Thought prompting method for translating jokes by first analyzing the humour, then translating the analysis, then regenerating the joke in the target language. On English-to-Chinese Short Jokes, the paper reports average gains of 7.75% in humour, 2.81% in fluency, and 6.13% in coherence; the best Table 1 system is GPT4-Turbo + HDM with SQM-H 70.54, SQM-F 99.45, and SQM-C 97.73.

## Problem & Motivation
The paper argues that ordinary LLM translation is often too literal for humour. Jokes depend on cultural context, wordplay, metaphor, and hidden punchlines, so direct translation can lose the intended comic effect. The authors also focus on linguistic interference: translated text may sound non-standard, less fluent, or less coherent because it follows the source-language structure too closely.

## Approach
HDM replaces one-step translation with three prompted stages. In humour decomposition, the LLM analyzes the source joke and extracts intrinsic knowledge. In the translation module, that analysis is translated into the target language. In humour composition, the LLM generates a target-language joke from the translated analysis. The paper then adds a humour-theory prompt inspired by Toplyn: each joke is decomposed into topic, angle, and punchline, where the punchline is the surprise at the end.

## Data & Experimental Setup
The main experiment randomly selects 500 samples from the Short Jokes Dataset and translates from English to Chinese. The evaluated backbones are Gemini1.5-Pro, Yi-Large, GPT3.5-Turbo, and GPT4-Turbo, compared with direct model translation plus DUAL-REFLECT and MAPS baselines. Evaluation uses GEMBA, a GPT4-based automatic metric: GEMBA-SQM scores 0–100, and GEMBA-STARS scores one to five stars for humour, fluency, and coherence. Results are averaged over three runs, and invalid LLM outputs are omitted. Generality tests use 100 samples per dataset/language, including Question-Answer Jokes, SemEval-2021, English-to-Spanish, English-to-German, and open-source models.

## Results
HDM is best in Table 1 for every closed-source backbone and every reported metric. For GPT4-Turbo, HDM scores SQM-H 70.54 versus MAPS 59.34, a +11.20 gain; SQM-F 99.45 versus 95.12, a +4.33 gain; and SQM-C 97.73 versus 88.62, a +9.11 gain. The paper specifically states that GPT4-Turbo’s humour improves by an average of 11.2%. Across other datasets, HDM improves by at least 1.84% in humour, 1.7% in fluency, and 2.15% in coherence. For Yi-Large English-to-German, the reported gains are 2.75% humour, 3.25% fluency, and 3% coherence. Open-source results are mixed: Qwen2.5-14B-Instruct improves from 51.60/91.40/86.00 to 61.80/97.40/91.35 on SQM-H/F/C, but Qwen2.5-0.5B-Instruct drops in SQM-H from 39.80 to 28.70.

## Takeaways
- For humour translation systems, translating an explanation of the joke before regenerating the joke can outperform direct translation.
- Topic-angle-punchline decomposition helps most when embedded inside the full HDM pipeline.
- Evaluation should separately measure humour, fluency, and coherence because a fluent translation may still lose the joke.
- Small open-source models may not have enough capacity for reliable humour decomposition and recomposition.

## Limitations & Caveats
The study uses only English source datasets and only Chinese, Spanish, and German as target languages. It has no human evaluation, relying instead on GPT4-based GEMBA metrics. The method is not systematically tested across humour types, and the error analysis shows failures on pronunciation-based and culturally specific puns such as “Fleece Navidad.”
