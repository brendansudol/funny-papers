# Do Androids Laugh at Electric Sheep? Humor “Understanding” Benchmarks from The New Yorker Caption Contest

**Jack Hessel, Ana Marasović, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, Yejin Choi** — ACL 2023 · Guide entry #1 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2209.06293) · [local PDF](../pdfs/01-androids-electric-sheep.pdf) · [full markdown](../md/01-androids-electric-sheep/01-androids-electric-sheep.md) · [extract](../extracts/01-androids-electric-sheep.json)

## TL;DR
This paper builds a benchmark suite from The New Yorker Cartoon Caption Contest to test whether models can match captions to cartoons, rank caption quality, and explain why a caption is funny. The central result is that models make progress but remain below humans: the best From Pixels matching model scores 62.3 vs. 94.0 for humans, and human explanations beat 5-shot GPT-4 in 67.7% of pairwise judgments.

## Problem & Motivation
The authors argue that generating jokes is not the same as understanding humor. New Yorker captions are difficult because the image-caption relation is often indirect, depends on unusual visual situations, and can require cultural or world knowledge. A model may recognize that a caption is relevant to an image but still fail to judge which caption is funnier or explain the joke.

## Approach
The benchmark has three tasks. Matching is a 5-way multiple-choice task where one caption truly corresponds to the cartoon and the distractors are finalists from other contests. Quality ranking asks which of two captions for the same cartoon is higher quality: a finalist/high-quality caption or an “okay” non-finalist. Explanation generation asks models to produce a free-text explanation of why a caption fits the cartoon and is funny.

The paper evaluates two settings. In From Pixels, models receive only the cartoon image at test time. In From Description, models receive human-authored annotations: scene location, literal description, unusual/uncanny elements, and relevant Wikipedia entities. The authors also test an OFA-Huge → T5 pipeline where OFA predicts those descriptions from pixels and a language model uses them.

## Data & Experimental Setup
The corpus covers 14 years of weekly contests and 704 cartoons. It combines roughly 250 contests from Jain et al. (2020), with 1.5M unique captions and over 114M ratings, plus contests #1–#507 from Shahaf et al. (2015) and Radev et al. (2016), with 2M unique captions. The released benchmark includes 2.7K high quality captions and 651 human-created joke explanations. Task sizes are 1.6K / 538 / 538 for matching, 1.6K / 523 / 523 for quality ranking, and 391 / 130 / 130 for explanation. Models include CLIP, OFA-Huge, T5-Large, T5-11B, GPT-3, GPT-3.5, and GPT-4.

## Results
For From Pixels matching, fine-tuned CLIP ViT-L/14@336px is best at 62.3 accuracy, 31.7 points below the human estimate of 94.0. In From Description matching, GPT-4 (5-shot) reaches 84.5, beating T5-11B at 70.8 by 13.7 points and fine-tuned GPT-3 at 75.1 by 9.4 points, but still below humans by 9.5 points.

For quality ranking, GPT-4 (5-shot) has the best CrowdAcc at 73.3, while humans reach 83.7. Fine-tuned GPT-3 has the best NYAcc at 69.8, above the human estimate of 64.6. For explanations, T5-11B with image information beats caption-only T5-11B in 84.7% of cases, and From Description T5-11B beats OFA → T5-11B in 74.6%, showing that visual recognition is a bottleneck. GPT-4 (5-shot) beats GPT-3 (5-shot) in 93.0% of explanation comparisons, but human explanations still beat GPT-4 in 67.7%.

## Takeaways
- Evaluating humor needs more than binary humor detection; relevance, preference, and explanation probe different abilities.
- Human-written visual descriptions substantially help language models, but they do not close the gap.
- Caption-only baselines are weaker, so image-caption interaction matters.
- Automatic overlap metrics for explanations are less reliable than human pairwise judgments in this setting.
- Builders of humor systems should treat visual understanding and world-knowledge grounding as major failure points.

## Limitations & Caveats
The benchmark covers a narrow English-language, New Yorker-specific style of humor. Quality labels reflect average preferences, not objective funniness or individual taste. The explanation references were largely written by one author. The corpus may contain offensive jokes, though the authors removed a handful targeting protected classes.
