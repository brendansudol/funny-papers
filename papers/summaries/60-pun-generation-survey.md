# A Survey of Pun Generation: Datasets, Evaluations and Methodologies

**Yuchen Su, Yonghua Zhu, Ruofan Wang, Zijian Huang, Diana Benavides-Prado, Michael Witbrock** — arXiv:2507.04793 · Guide entry #60 (Part 9 - Surveys & Resources)

[paper page](https://arxiv.org/abs/2507.04793) · [local PDF](../pdfs/60-pun-generation-survey.pdf) · [full markdown](../md/60-pun-generation-survey/60-pun-generation-survey.md) · [extract](../extracts/60-pun-generation-survey.json)

## TL;DR
This paper is a survey of pun generation, covering pun categories, datasets, methods, evaluation metrics, challenges, and future directions. Its central contribution is a structured map of the field rather than a new benchmark: the authors identify around 150 publications, filter to approximately 30 pun-generation papers, and show that research has moved from templates to DNNs, PLMs, prompting, and early visual-language work while still being constrained by datasets and evaluation.

## Problem & Motivation
Pun generation is framed as a creative NLG task: a system must produce humour or double meanings while preserving coherence and contextual appropriateness. The authors argue that, although pun generation has been studied for decades, there was no dedicated survey focused specifically on this area. Prior surveys covered broader humour generation or other creative writing tasks, but did not systematically review pun datasets, methods, and LLM-era work.

## Approach
The survey first defines four pun categories: homophonic, heterographic, homographic, and visual puns. It then organizes datasets into generic datasets, derived datasets, and human-annotated datasets. Methods are grouped by technological timeline: conventional template/rule systems, classic DNNs, fine-tuned pre-trained language models, prompting of PLMs/LLMs, and visual-language models. Evaluation is summarized as automatic metrics and human evaluation metrics.

## Data & Experimental Setup
This is not an experimental paper and does not run models or produce a new leaderboard. The authors collect relevant literature by searching “pun research”, “computational humour”, and “pun dataset” on arXiv and Google Scholar, finding around 150 publications, filtering to approximately 30 pun-generation papers, and then applying forward and backward snowballing. Dataset coverage includes generic corpora such as Wikipedia, BookCorpus, C4, The Pile, and Dakshina, plus pun datasets such as Paron, Church, Pun-Yang, Pun-Kao, SemEval-2017 Task 7 puns, ExPUNations, CUP, ChinesePun, Pun Rebus Art, and UNPIE.

## Results
Because the paper is a survey, no system beats another in new experiments. The main quantitative results are descriptive. Table 4 lists Paron with 3,850 puns, SemEval with 2,878 puns, SemEval-P with 1,607, and SemEval-G with 1,271. Later human-annotated resources include ExPUNations with 1,999 items and CUP with 2,396. ChinesePun contains 2,106 items, split into ChinesePun-P with 1,049 and ChinesePun-G with 1,057. Multimodal/multilingual resources include Pun Rebus Art with 1,011 and UNPIE with 1,000.

## Takeaways
- Pun generation research is still heavily English- and text-centered.
- SemEval-2017 Task 7 puns is treated as a central expert-annotated dataset for later work.
- PLMs and LLMs have expanded generation approaches, but the survey reports that LLMs still have limitations in creative and humorous pun generation.
- Evaluation remains unsettled: automatic metrics cover ambiguity, distinctiveness, surprisal, unusualness, diversity, perplexity, and structural success, while human evaluation covers success, funniness, fluency, informativeness, coherence, and readability.
- For builders of humor systems, the paper points to multilingual generation, multimodal puns, and better prompting as major open directions.

## Limitations & Caveats
The authors state that some works may have been missed because search keywords vary. They also note limited coverage of pun categories such as recursive puns and antanaclasis, and acknowledge that rapid progress means the survey cannot cover the full historical scope or all latest advances. The appendix adds that automatic metrics can miss semantic diversity and logical consistency, while human evaluation is culturally subjective and often underreports annotator background.
