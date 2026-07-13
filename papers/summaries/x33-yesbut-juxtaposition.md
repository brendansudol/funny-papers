# Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions

**Zhe Hu, Tuo Liang, Jing Li, Yiren Lu, Yunlai Zhou, Yiran Qiao, Jing Ma, Yu Yin** — NeurIPS 2024 (Oral) · Guide entry Part 3 (Hu YesBut lineage) (Part 3 - Multimodal & Visual Humor)

[paper page](https://proceedings.neurips.cc/paper_files/paper/2024/hash/540a6eefb60428c8547a27253f9a2a59-Abstract-Conference.html) · [local PDF](../pdfs/x33-yesbut-juxtaposition.pdf) · [full markdown](../md/x33-yesbut-juxtaposition/x33-yesbut-juxtaposition.md) · [extract](../extracts/x33-yesbut-juxtaposition.json) · [dataset: YesBut-Juxtaposition (Hu et al.)](../../data/yesbut-juxtaposition/)

## TL;DR
The paper introduces YESBUT, a benchmark of 348 two-panel captionless comics where humor comes from juxtaposed contradictory narratives. It tests whether large vision-language and language models can move from literal comic description to contradiction explanation, philosophy selection, and title matching. The strongest reported results are still far from solved: Claude-3 reaches 84.10% on philosophy selection, while LLaVA-1.6-34B reaches only 63.31% on title matching.

## Problem & Motivation
The authors argue that comics with juxtaposition require more than object recognition or ordinary captioning. A reader must understand two panels together, identify a contradiction, and infer the social or philosophical point being satirized. This is framed as nonlinear narrative reasoning involving human norms, cultural context, and subtle social cues. The paper asks whether recent commercial and open-source VLMs and LLMs can handle this kind of visual humor.

## Approach
YESBUT contains one image per sample plus four annotated components: a literal description, a contradiction explanation, an underlying philosophy, and a title. The benchmark defines four tasks: literal description writing, contradiction generation, underlying philosophy selection from four options, and title matching from four options. Annotation uses a progressive human-AI pipeline: GPT-4 drafts components and hard negatives, then eight human judges modify, verify, and cross-check them; one author later reviews each sample.

## Data & Experimental Setup
The dataset has 348 comics, primarily from Anton Gudim’s “YES, BUT” series, scraped from Twitter and Pinterest after deduplication, filtering comics with more than two panels, and removing inappropriate or offensive content. The paper reports 348 literal descriptions with average length 80 words, 348 contradictions with average length 31 words, 1,392 philosophy options with average length 24 words, and 1,392 title options with average length 6 words.

The evaluated VLMs include GPT-4, Claude-3, LLaVA-1.6 variants, LLaVA-1.5-13B, InstructBLIP, CogVLM, Qwen-VL-Chat, and mPLUG-Owl2. The evaluated LLMs are ChatGPT, Llama-3-8B-Instruct, and Mistral-7B-Instruct, using LLaVA-1.6-13B descriptions as inputs. Generation tasks use BERTScore recall, ROUGE-2 recall, and GPT-based 1-to-5 scoring with gpt-3.5-turbo-0125. MCQ tasks use accuracy. Three human judges also rate 30 random samples.

## Results
GPT-4 is strongest on literal description, scoring 88.32 BERTScore recall, 87.46 ROUGE-2 recall, and 3.76 GPT score. For contradiction generation, GPT-4 has 83.21 ROUGE-2 and 4.03 GPT score, while ChatGPT has the best BERTScore recall at 87.78.

For deep reasoning, Claude-3 leads philosophy selection with 84.10%, beating GPT-4’s 82.76% by 1.34 points. LLaVA-1.6-34B leads title matching with 63.31%, beating GPT-4’s 60.25% by 3.06 points. Human evaluation also ranks GPT-4 highest: literal Correctness 3.75, Completeness 3.86, Faithfulness 3.53; contradiction Correctness 3.1 and Faithfulness 3.22.

Oracle literal descriptions strongly help. For Llama3-8B, philosophy accuracy rises from 72.1 to 89.3 and title accuracy from 49.7 to 73.5. However, adding VLM-generated descriptions can hurt: LLaVA-1.6-13B title accuracy drops from 55.08 to 48.76 with its predicted description.

## Takeaways
- Evaluating comic humor needs tasks beyond captioning; contradiction and title abstraction expose deeper reasoning gaps.
- Strong literal image understanding is a prerequisite for deeper humor interpretation.
- Oracle text helps both LLMs and VLMs, showing that current visual narrative understanding is a bottleneck.
- Decomposing VLM reasoning with noisy generated descriptions is not automatically beneficial.
- Builders should track hallucination, visual misinterpretation, and wrong panel-relationship reasoning, not just answer accuracy.

## Limitations & Caveats
The dataset is small and comic interpretation remains subjective despite cross-verification. The benchmark focuses on visual humor through juxtaposition and does not cover all comic or humor types. The source comics are public social media images, and the paper does not report decontamination checks. Exact inference dates, token budgets, and full open-source checkpoint details are not reported.
