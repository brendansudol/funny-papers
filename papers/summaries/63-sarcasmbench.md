# SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding

**Yazhou Zhang, Chunwang Zou, Zheng Lian, Prayag Tiwari, Jing Qin** — arXiv:2408.11319 · Guide entry #63 (Adjacent - Sarcasm & Humor Styles)

[paper page](https://arxiv.org/abs/2408.11319) · [local PDF](../pdfs/63-sarcasmbench.pdf) · [full markdown](../md/63-sarcasmbench/63-sarcasmbench.md) · [extract](../extracts/63-sarcasmbench.json)

## TL;DR
SarcasmBench evaluates whether LLMs have really mastered sarcasm understanding. Across six text sarcasm datasets and three prompting strategies, the central result is negative: current prompting-based LLMs underperform supervised PLM sarcasm baselines, although GPT-4 Turbo is the strongest LLM and few-shot IO prompting helps.

## Problem & Motivation
The paper challenges the claim that LLMs have largely solved fast, intuitive “System I” NLP tasks. Sarcasm is treated as harder than ordinary sentiment classification because the literal wording can conflict with the speaker’s real intention. The main research question is: “Have LLMs really made significant progress in understanding sarcasm?” The authors also examine whether few-shot examples, chain-of-thought prompting, and multi-modal inputs improve sarcasm understanding.

## Approach
The paper builds SarcasmBench, an evaluation framework for sarcasm detection with LLMs. Sarcasm detection is reformulated as a conditional generative classification task: given an instruction and an input text, the model must output only “sarcastic” or “non-sarcastic.” Three prompting strategies are evaluated: zero-shot IO prompting, few-shot IO prompting, and few-shot CoT prompting. For few-shot settings, the paper samples k similar demonstrations from the training set using KNN search. The same test labels are used to evaluate LLM outputs against supervised baselines.

## Data & Experimental Setup
The main text evaluation uses six benchmark datasets: IAC-V1, IAC-V2, Ghosh, iSarcasmEval, Riloff, and SemEval 2018 Task 3. The compared systems include traditional DLMs such as TextCNN, LSTM, Bi-LSTM, and AT-LSTM; PLMs such as BERT, RoBERTa, DeBERT, XLNet, and DC-Net-RoBERTa; and eleven LLMs including Baichuan 2-7B, ChatGLM 2-6B/3-6B, LLaMA 2-7B/3-8B, Mistral-7B, Qwen 1.5-7B/2-7B, ChatGPT, GPT-4 Turbo, and Claude-3-haiku. Metrics are accuracy, precision, recall, and F1, averaged over five random seeds. A separate multi-modal section evaluates MMSD and CMMA with Retrieval-LLaVA 1.5, GPT-4V, Wenxin 4, and Qwen-VL-Plus.

## Results
In zero-shot IO, PLMs outperform traditional DLMs: RoBERTa reaches average F1 71.3 and DC-Net-RoBERTa 71.5, while Bi-LSTM and AT-LSTM score 66.7 and 65.3. GPT-4 Turbo is the best LLM, with zero-shot F1 scores of 78.7 on IAC-V1, 76.6 on IAC-V2, 39.8 on iSarcasmEval, 33.3 on Riloff, 76.5 on SemEval Task 3, and 82.2 on Ghosh. The paper reports that GPT-4 outperforms other LLMs by an average improvement of 14.0%↑.

Few-shot IO is the best prompting strategy overall, with an average improvement of 4.5%↑ over zero-shot IO and few-shot CoT. GPT-4’s iSarcasmEval F1 increases from 39.8 to 52.3, reported as a 31.4% improvement. However, CoT hurts: GPT-4 drops from 68.4 average F1 with IO prompting to 64.7 with CoT, Mistral from 55.8 to 47.5, and Qwen 2 from 53.1 to 39.7. In multi-modal evaluation, Retrieval-LLaVA 1.5 reaches MMSD F1 89.4, while Qwen-VL-Plus has the best CMMA F1 among reported multi-modal LLMs at 56.1.

## Takeaways
- Do not assume general LLM strength transfers to sarcasm detection; supervised PLMs still remain strong baselines.
- GPT-4 Turbo is the clearest LLM leader, but its performance varies sharply by dataset.
- Few-shot IO prompting is more reliable than CoT for sarcasm classification.
- More demonstrations are not always better: GPT-4 peaks at 2-shot with F1 67.5 in the demonstration-count study.
- Sarcasm evaluation should include error analysis, because category imbalance and sarcastic examples drive many failures.

## Limitations & Caveats
The paper only tests standard prompting and CoT, leaving tree-based or graphical prompting for future work. It also does not deeply analyze how model performance varies across different sarcasm contexts, which the authors identify as an important future direction.
