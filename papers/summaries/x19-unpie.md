# Can visual language models resolve textual ambiguity with visual cues? Let visual puns tell you!

**Jiwan Chung, Seungwon Lim, Jaehyun Jeon, Seungbeen Lee, Youngjae Yu** — EMNLP 2024 · Guide entry Part 3 (controlled cross-modal anchor) (Part 3 - Multimodal & Visual Humor)

[paper page](https://aclanthology.org/2024.emnlp-main.144/) · [local PDF](../pdfs/x19-unpie.pdf) · [full markdown](../md/x19-unpie/x19-unpie.md) · [extract](../extracts/x19-unpie.json) · [dataset: UNPIE (Understanding Pun with Image Explanations)](../../data/unpie/)

## TL;DR
The paper introduces UNPIE, a 1,000-item multimodal multilingual benchmark for testing whether models use images to resolve ambiguity in puns. Across pun grounding, disambiguation, and reconstruction, visual context improves performance, with the strongest reconstruction system, GPT-4 with images, reaching All Correct (%) of 57.9 for De→En, 55.9 for Fr→En, and 61.3 for Ko→En.

## Problem & Motivation
The authors frame the work around multimodal literacy: the ability to actively combine text and visual information when text is ambiguous. Puns are chosen because they are intrinsically ambiguous and often become clearer when paired with visual explanations. The goal is not just to test whether a model can process an image, but whether it uses the image to resolve lexical ambiguity in text.

## Approach
UNPIE defines three tasks. Pun grounding asks a model to identify the word or phrase that creates the pun in an English sentence, optionally with a pun explanation image. Pun disambiguation gives an English pun and a disambiguator image showing one meaning, and asks the model to translate the sentence into German, French, or Korean in a way aligned with that image. Pun reconstruction gives an ambiguity-free non-English translation plus a pun explanation image and asks the model to reconstruct an English sentence containing the original pun.

## Data & Experimental Setup
The benchmark starts from SemEval-2017 Task 7 puns: from 2,878 English pun sentences, the authors select 500 homographic and 500 heterographic puns. Each item receives one DALL-E 3-generated pun explanation image showing both meanings and two LAION 2B-retrieved disambiguator images, one for each meaning. Human annotators translate each pun into German, French, and Korean, making the translation meaning-specific rather than preserving English ambiguity. Models include Vicuna, GPT-4, Qwen-VL, LLaVA, Socratic Models using BLIP-2 captions, and LLaVA-MMT fine-tuned on Multi30k.

## Results
In pun grounding, images improved every multimodal variant. Qwen-VL had the largest gains: homographic exact match rose from 43.8 to 63.6 (↑ 19.8), and heterographic from 57.8 to 70.8 (↑ 13.0). GPT-4 was already strong text-only at 95.4/92.0 and improved to 97.6/94.0 with images.

For pun disambiguation, GPT-4 as a Socratic Model with image captions was best: All accuracy was 71.4 for En→De, 72.9 for En→Fr, and 65.8 for En→Ko. LLaVA-MMT did not reliably help; for example, it scored 65.7 on En→De All versus 68.0 for zero-shot LLaVA.

Pun reconstruction was hardest and showed the clearest need for images. GPT-4 with images achieved All Correct (%) of 57.9 for De→En (↑13.7), 55.9 for Fr→En (↑3.6), and 61.3 for Ko→En (↑9.0). Bleu-4 and METEOR did not show a clear trend for pun correctness.

## Takeaways
- Visual context helps most when the task forces ambiguity resolution rather than simple phrase identification.
- Strong language understanding remains crucial: GPT-4 with captions beats monolithic VLMs on disambiguation.
- Standard multimodal machine translation fine-tuning on Multi30k does not teach the visual dependence needed for UNPIE.
- Evaluating pun reconstruction needs meaning-aware judgment; surface text metrics are inadequate.

## Limitations & Caveats
UNPIE is built from English puns, so it mainly captures English-specific ambiguity. Its 1,000 examples are not enough for a training split suitable for fine-tuning. Generated images differ somewhat from natural pun images, and the dataset may retain subtle cultural biases or stereotypes from source humor.
