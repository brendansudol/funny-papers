# Does Reasoning Kill the Joke? Long-Context Humor Understanding in Hindi

**Kaveri Anuranjana, Navya Shrivastava, Atharv Johar, Rishabh Sabharwal, Gautam Ranka, Aryan Lunawat, Punit Rathore, Radhika Mamidi** — C3NLP 2026 · Guide entry Part 7 (long-context Hindi) (Part 7 - Cross-Cultural & Translation)

[paper page](https://aclanthology.org/2026.c3nlp-1.14/) · [local PDF](../pdfs/x30-hins.pdf) · [full markdown](../md/x30-hins/x30-hins.md) · [extract](../extracts/x30-hins.json)

## TL;DR
The paper introduces HinS, a Hindi long-context conversational humor benchmark built from humorous video clips, and evaluates LLMs on explaining why audiences laughed. The main result is that Hindi humor reasoning remains largely unsolved: Gemini-2.0-Flash leads automatic metrics with BLEU 0.0566 and BERTScore 0.8075, while manual evaluation of Sarvam-M-24B reaches only 26.25% accuracy.

## Problem & Motivation
Prior humor benchmarks are heavily English-centered and often test simpler detection tasks rather than explanations. The authors argue that conversational humor is a pragmatic, culture-grounded task, so it is a useful probe of linguistic equity: whether models maintain performance across languages and societies. Hindi is especially under-served for explanation-oriented humor understanding, even though prior Hindi work has studied related areas such as sarcasm, memes, and binary humor classification.

## Approach
HinS converts humorous Hindi video clips into text-based inputs for LLM evaluation. The pipeline extracts time-aligned dialogue transcripts, generates dense scene descriptions for visual context using a frontier captioning model, and extracts audio features. The main task is explanation generation: given the transcript and scene description, the model must explain why the audience laughed. The paper also analyzes lexical diversity using Type-Token Ratio to identify rambling or hallucinated outputs that standard quality metrics may miss.

## Data & Experimental Setup
HinS contains 1,046 instances from 44 videos and 9,531 video segments, with an average of 23.7 clips per video and 9.11 segments per clip. The data comes from Indian sitcoms and stand-up comedy; 676 instances, approximately 64.5%, are Creative Commons licensed, and 370 clips, approximately 35.4%, are under standard copyright restrictions. Ground-truth explanations were automatically generated and then checked by native Hindi-speaking university students: among 200 randomly selected samples, 86.65% were correct, with IAA 0.68.

The main benchmark evaluates Qwen-2.5-7B, Qwen-3-7B, Sarvam-M-24B, Gemma-3-27B, Llama-3.1-70B, and Gemini-2.0-Flash. Additional analyses include DeepSeek-R1-0528, Gemma-3-27B, and Gemini-2.0-Flash on 150 random SMILE versus HinS samples, plus qualitative error analysis with Llama-3.1-8B and Llama-3.1-70B.

## Results
Gemini-2.0-Flash is the strongest system in Table 2: BLEU 0.0566, METEOR 0.2869, ROUGE-1/2/L 0.31 / 0.10 / 0.24, and BERTScore 0.8075. Llama-3.1-70B follows on BLEU and METEOR with 0.0523 and 0.2334, while Qwen-2.5-7B scores BERTScore 0.7828. Sarvam-M-24B is competitive with Llama-3.1-70B despite being Indic-specialized and smaller: BLEU 0.0471 versus 0.0523, METEOR 0.2274 versus 0.2334, and BERTScore 0.7890 versus 0.7910.

English-to-Hindi comparison shows a consistent gap. DeepSeek-R1-0528 has the largest reported decline: BLEU drops 38.3%, from 0.1138 to 0.0702, and BERTScore drops from 0.8239 to 0.7958. Context length analysis finds a peak at 250–750 words, lower performance below 250 words, and degradation beyond 750 words. Human evaluation is harsher than automatic metrics: Sarvam-M-24B achieves only 26.25% accuracy on 80 explanations.

## Takeaways
- Hindi conversational humor is not solved by current LLMs, including large and Indic-focused models.
- Larger models help, but scale alone produces limited gains on pragmatic humor reasoning.
- Indic pretraining matters: Sarvam-M-24B competes with much larger generalist models.
- Automatic metrics can be misleading; human evaluation and diversity diagnostics are important.
- Long context is not always better: useful context peaks at 250–750 words, while excessive context adds noise.

## Limitations & Caveats
The benchmark uses transcripts and generated scene descriptions rather than raw multimodal inputs, so it loses prosody, timing, facial expressions, and detailed actions. Cultural evaluation is subjective, and the paper notes that culture and language effects are intertwined. The reported metrics are aggregate scores and do not isolate humor mechanisms such as sarcasm, allusion, or fallacious reasoning.
