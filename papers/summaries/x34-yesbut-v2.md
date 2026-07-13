# When ‘YES’ Meets ‘BUT’: Can Large Models Comprehend Contradictory Humor Through Comparative Reasoning?

**Tuo Liang, Zhe Hu, Jing Li, Hao Zhang, Yiren Lu, Yunlai Zhou, Yiran Qiao, Disheng Liu, Jeirui Peng, Jing Ma, Yu Yin** — arXiv:2503.23137 · Guide entry Part 3 (Hu YesBut V2) (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2503.23137) · [local PDF](../pdfs/x34-yesbut-v2.pdf) · [full markdown](../md/x34-yesbut-v2/x34-yesbut-v2.md) · [extract](../extracts/x34-yesbut-v2.json) · [dataset: YesBut V2-Juxtaposition (Hu et al.)](../../data/yesbut-v2/)

## TL;DR
This paper introduces YESBUT (V2), a benchmark of 1,262 juxtaposed comic images designed to test whether large models understand humor created by contradictions between panels. Across four tasks, even the strongest VLMs trail humans substantially: on 50 comics, humans score 91.3 on symbolism and 97.5 on title matching, compared with GPT-4o at 80.4/80.6 and LLaVA-Next-13B at 70.4/66.9.

## Problem & Motivation
The paper argues that comics require more than object recognition: readers must compare panels, identify contradictory narrative elements, and use social or cultural knowledge to infer the joke or message. Prior humor benchmarks often emphasize single images or captions, while this work targets multi-panel juxtaposition where the “Yes” panel sets an expectation and the “But” panel subverts it.

## Approach
YESBUT (V2) annotates each comic with a literal description, an explicit contradiction, an underlying symbolism/message, a title, social knowledge, linguistic context, text-presence metadata, and panel bounding boxes. The authors define four tasks: Literal Description Writing, Explicit Contradiction Generation, Underlying Symbolism Selection, and Title Matching. Annotation uses a progressive human-AI pipeline: GPT-4 drafts structured annotations and distractors, then human annotators refine, verify, cross-check, adjudicate, and an author reviews final labels.

## Data & Experimental Setup
The benchmark contains 1,262 comics; Table 1 reports 1,262 literal descriptions, 1,262 explicit contradictions, 5,048 symbolism options, 5,048 title options, 3,407 social-knowledge annotations, and 1,262 linguistic-context annotations. The dataset includes English, Chinese, and Russian examples; 58% of comics contain embedded text and 86% require social knowledge. The evaluation covers VLMs including GPT-4o, GPT-4-Vision-Turbo, Qwen2-VL, LLaVA-OneVision, LLaVA-Next, LLaVA-1.5, and CogVLM2, plus LLMs such as GPT-4, DeepSeek-R1-70B, Llama3, and Qwen2.5 using VLM-generated captions. Generation tasks are scored with BERT Score, ROUGE-2, GPT-based scoring, and human evaluation; MCQ tasks use accuracy.

## Results
GPT-4o is best on literal description with BERT 88.96, R-2 63.13, and GPT 3.96. For contradiction generation, GPT-4o leads on BERT 87.85 and GPT 3.72, while Qwen2-VL-72B leads ROUGE-2 with 60.07. On deep reasoning, GPT-4o is best for symbolism at 80.38%, and Qwen2-VL-72B is best for title matching at 81.25%. Humans outperform models on the 50-comic baseline, scoring 91.3 and 97.5. Text-only finetuning improves LLaVA-Next-7B symbolism from 59.35 to 67.91 and LLaVA-Next-13B from 70.36 to 75.25. Adding social knowledge improves or maintains performance across tested VLMs.

## Takeaways
- Evaluating humor in comics should test comparison, contradiction, and social knowledge, not just caption quality.
- Strong surface descriptions are necessary but not sufficient; flawed self-descriptions can hurt downstream reasoning.
- Splitting panels into separate images generally does not help current multi-image VLMs.
- Social-knowledge retrieval or explicit knowledge injection is a promising path for humor understanding.
- Text-only synthetic finetuning can improve deep reasoning without new paired image-text training data.

## Limitations & Caveats
The paper reports inconsistencies in dataset and annotator counts across sections, and human evaluations are small. Public social-media source images create possible contamination risk, but no decontamination test is reported. Many open-source checkpoint, inference-date, token-budget, and invalid MCQ parsing details are not provided.
