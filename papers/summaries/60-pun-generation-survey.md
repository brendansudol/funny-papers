# A Survey of Pun Generation: Datasets, Evaluations and Methodologies

**Yuchen Su, Yonghua Zhu, Ruofan Wang, Zijian Huang, Diana Benavides-Prado, Michael Witbrock** — Findings of EMNLP 2025 · Guide entry #60 (Part 9 - Surveys & Resources)

[paper page](https://aclanthology.org/2025.findings-emnlp.389/) · [local PDF](../pdfs/60-pun-generation-survey.pdf) · [full markdown](../md/60-pun-generation-survey/60-pun-generation-survey.md) · [extract](../extracts/60-pun-generation-survey.json)

## TL;DR
This paper is a survey of pun generation, covering datasets, methodologies, and evaluation strategies across text and visual puns. Its main contribution is an organized taxonomy: datasets are grouped as generic, derived, and human-annotated; methods are grouped into conventional systems, classic DNNs, PLM fine-tuning, PLM prompting, and visual-language models.

## Problem & Motivation
Pun generation is a creative NLG task that requires producing humorous text with double or multiple meanings while preserving fluency, coherence, and contextual appropriateness. The authors argue that, despite decades of work on puns, no dedicated survey had systematically reviewed pun generation datasets, methods, and evaluation. They position the survey as a guide for researchers working on puns, especially as the field shifts from template systems and neural networks toward large language models and multimodal models.

## Approach
The paper first defines four pun categories: homophonic, heterographic, homographic, and visual puns. It then reviews datasets, methods, and evaluation metrics. The method taxonomy follows technological development: early conventional/template systems such as JAPE, STANDUP, T-PEG, and PAUL BOT; classic DNN approaches using LSTM, ON-LSTM, Seq2Seq, and GAN-style methods; PLM fine-tuning with models such as T5, GPT-2, BERT, LLaMA2-7B, and Baichuan2-7B in prior work; prompting-based LLM work; and preliminary visual-language-model studies.

## Data & Experimental Setup
This is a non-empirical survey: it does not run models or collect new human judgments. The authors searched for “pun research,” “computational humour,” and “pun dataset” on arXiv and Google Scholar, initially identifying “around 150 publications,” filtering to “approximately 30 papers” focused on pun generation, and then applying forward and backward snowballing. The dataset review includes generic corpora such as Wikipedia, BookCorpus, C4, The Pile, and Dakshina, plus pun-specific resources. Table 4 lists, among others, SemEval with 2,878 items, ExPUNations with 1,999, CUP with 2,396, ChinesePun with 2,106, Pun Rebus Art with 1,011, and UNPIE with 1,000.

## Results
The paper reports no new benchmark scores. Its results are survey findings: early datasets were often domain-specific, such as Paron from advertisements with 3,850 items and Church with 373 items; SemEval is described as the first expert-annotated pun dataset and a widely referenced resource; recent datasets expand toward explanations, context, Chinese puns, and multimodal or multilingual puns. For evaluation, the survey lists automatic metrics including ambiguity, distinctiveness, surprisal, unusualness, Dist-1 & Dist-2, perplexity, and structure success. Human evaluation metrics include success, funniness, fluency, informativeness, coherence, and readability.

## Takeaways
- Pun generation systems must balance ambiguity, humour, fluency, and contextual fit; no single automatic metric captures all of these.
- Human evaluation remains essential, but evaluator background and cultural knowledge matter and are often underreported.
- LLMs show promise, especially with prompting and contextual information, but the survey notes limits in creativity and humour.
- English text puns dominate existing work; multilingual and multimodal pun generation are major open areas.
- Visual puns are underdeveloped as a generation task, despite emerging datasets and vision-language studies.

## Limitations & Caveats
The authors state that some work may have been missed because search terms vary. They also note limited coverage of pun categories such as recursive puns and antanaclasis, and acknowledge that fast-moving research means the survey cannot cover all historical work or the latest advances. Because this is a survey, it provides taxonomy and synthesis rather than directly comparable experimental results.
