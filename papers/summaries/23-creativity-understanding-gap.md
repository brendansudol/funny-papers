# Bridging the Creativity Understanding Gap: Small-Scale Human Alignment Enables Expert-Level Humor Ranking in LLMs

**Kuan Lok Zhou, Jiayi Chen, Siddharth Suresh, Reuben Narad, Timothy T. Rogers, Lalit K Jain, Robert D Nowak, Bob Mankoff, Jifan Zhang** — EMNLP Findings 2025 · Guide entry #23 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2502.20356) · [local PDF](../pdfs/23-creativity-understanding-gap.pdf) · [full markdown](../md/23-creativity-understanding-gap/23-creativity-understanding-gap.md) · [extract](../extracts/23-creativity-understanding-gap.json)

## TL;DR
This paper revisits New Yorker Cartoon Caption Contest humor ranking and decomposes the problem into visual understanding, humor reasoning, and alignment with crowd preferences. The key result is that supervised fine-tuning of GPT-4o on a small set of crowd preference pairs, with o1-preview explanations, reaches 82.4±1.2% accuracy on the 10vs1000 task, up from 67.3±1.5% for GPT-4o prompting and above the expert average of 78±2.6%.

## Problem & Motivation
Prior work showed a gap between LLMs and humans on choosing the funnier of two New Yorker cartoon captions. The authors argue that this gap mixes three problems: the model must understand the cartoon image, reason about why each caption is funny, and match the preferences of the New Yorker voting crowd. They also use the task to argue that creative AI systems need human preference data, because creative domains lack verifiable rewards and depend on subgroup-specific taste.

## Approach
The system first improves cartoon descriptions. GPT-4o-generated descriptions are checked by humans, corrected when needed, and paired with “canny” and “uncanny” descriptions. Second, the authors generate caption-level humor explanations with GPT-4o and o1-preview, then feed those explanations into ranking prompts. Third, they compare persona-based prompting against supervised fine-tuning. Persona prompts try to simulate likely contest audiences, while fine-tuning directly trains GPT-4o to choose the crowd-preferred caption.

## Data & Experimental Setup
The introduced working dataset covers 379 contests from #510 to #889, with 20 constructed caption pairs per contest and a random split of 279 training cartoons and 100 test cartoons. Training uses 5,580 pairwise comparisons: for each training cartoon, 10 pairs compare ranks 1–10 against 1000–1009, and 10 pairs compare ranks 30–39 against 300–309. Five-shot in-context examples are sampled from the training set. Human evaluation uses five renowned experts on 50 test contests, with two caption pairs each.

## Results
Description quality mattered: 23.5% (89/379) of GPT-4o descriptions had errors, and refined descriptions improved GPT-4o prompting from 70% to 73% and finetuned performance from 81.3% to 82.4%. In explanation experiments, o1-preview explanations improved GPT-4o ranking to 76%, compared with 73% for no explanation and 71% for GPT-4o explanations. Persona prompting was limited: the best GPT-4o persona, Female Lawyer, reached 76.5% on a size 200 subset, versus 73.5 for the empty baseline. The strongest method was GPT-4o SFT w/ Expl., with 82.4±1.2% on 10vs1000 and 63.2±1.5% on 30vs300. This beat GPT-4o prompting by 15.1 points on 10vs1000 and 9.3 points on 30vs300. It also exceeded expert average accuracy on both tasks, though it remained below the best expert on 10vs1000.

## Takeaways
- Correct visual annotations and good explanations help, but do not close the humor preference gap alone.
- Persona prompts are a weak substitute for real preference data in this setting.
- Small-scale supervised fine-tuning on crowd preferences can move an LLM from below-human to expert-level ranking accuracy.
- Builders of humor systems should evaluate alignment to a target audience, not only generic joke reasoning.

## Limitations & Caveats
The work is limited to New Yorker cartoon captions and pairwise ranking, so results may not generalize to other humor types or generation. The labels reflect a specific audience’s subjective taste. The paper also warns that humor may be offensive and states that the current framework does not explicitly detect or mitigate offensive content.
