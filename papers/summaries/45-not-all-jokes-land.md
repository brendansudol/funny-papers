# Not All Jokes Land: Evaluating Large Language Models’ Understanding of Workplace Humor

**Mohammadamin Shafiei, Hamidreza Saffari** — arXiv:2506.01819 · Guide entry #45 (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2506.01819) · [local PDF](../pdfs/45-not-all-jokes-land.pdf) · [full markdown](../md/45-not-all-jokes-land/45-not-all-jokes-land.md) · [extract](../extracts/45-not-all-jokes-land.json)

## TL;DR
The paper introduces the first dataset focused on appropriateness of humor in professional industrial settings and evaluates five LLMs on classifying workplace jokes as Offensive, Mildly Inappropriate, Neutral, or Wholesome. The strongest holdout result is Claude 3.5 Sonnet on the GPT-4o-generated subset with weighted average F1-score 0.73, but offensive humor remains difficult, with average F1-scores of 0.32 and 0.26 across the two subsets.

## Problem & Motivation
LLMs are increasingly used for automated writing, email drafting, workplace social media, and agentic simulations of human interaction. In those settings, an AI system may generate or react to humor, but workplace humor is highly context-dependent: it can build rapport when used well and create misunderstanding or credibility problems when misused. The authors argue that existing computational humor work does not evaluate whether LLMs understand the appropriateness of professional, industry-specific humor.

## Approach
The paper builds a text dataset of humorous workplace sentences. Each item includes a sentence, an appropriateness label, an industry-specific context, a humor type, and a short explanation. The four appropriateness labels are Offensive, Mildly Inappropriate, Neutral, and Wholesome. The seven humor types are Irony, Hyperbole, Self-deprecation, Metaphorical Humor, Situational Humor, Positive Humor, and Cultural Reference Humor.

## Data & Experimental Setup
Claude 3.5 Sonnet and GPT-4o generated an initial 340 samples, 170 from each model. Two experienced annotators reviewed the generated material and removed irrelevant, repetitive, or nonsensical items, reducing the dataset to 304 samples. The final split contains 156 Claude-generated samples and 148 GPT-4o-generated samples. Appropriateness counts are 57 Offensive, 76 Mildly Inappropriate, 84 Neutral, and 87 Wholesome. The dataset covers 138 industry-specific contexts.

The authors evaluate GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Flash, Llama-3.2-1B-Instruct, and Qwen2.5-72B-Instruct. GPT-4o and Claude 3.5 Sonnet are tested only on the subset they did not generate. All experiments use temperature zero, and responses were collected in November 2024.

## Results
On the Claude-generated subset, GPT-4o has the best weighted average F1-score at 0.60, ahead of Llama-3.2-1B-Instruct at 0.58 by 0.02, Qwen2.5-72B-Instruct at 0.54 by 0.06, and Gemini 1.5 Flash at 0.48 by 0.12. On the GPT-4o-generated subset, Claude 3.5 Sonnet is strongest with weighted average F1-score 0.73, ahead of Llama at 0.52 by 0.21, Gemini at 0.41 by 0.32, and Qwen at 0.34 by 0.39.

The paper reports lower average weighted F1 on the GPT-4o-generated subset, 0.50, than on the Claude-generated subset, 0.55, suggesting the GPT-4o subset is more nuanced or context-specific. Wholesome is the easiest category on average, with F1 0.84 on the Claude subset and 0.83 on the GPT-4o subset. Offensive is much weaker, with average F1 0.32 and 0.26. In the Llama humor-type analysis, Irony and Hyperbole have the top weighted average F1-scores, both 0.60, while Cultural Reference Humor has 0.41 and only 0.07 F1 for Offensive.

## Takeaways
- Workplace humor appropriateness is not solved by current LLMs, even with explicit label definitions.
- Offensive humor involving cultural or national references is especially risky for automated workplace writing systems.
- Evaluations should separate appropriateness levels; high Wholesome performance can mask weak Offensive performance.
- Humor type matters: Llama’s results vary substantially across Irony, Hyperbole, Self-deprecation, and Cultural Reference Humor.

## Limitations & Caveats
The dataset contains only 304 samples. The humor-type taxonomy is limited; sarcasm is grouped under Irony. Both annotators are male, so the authors removed samples with gender references. The paper also notes that using LLMs to generate the examples may introduce model or prompt biases and may not match humor selected by human experts.
