# Small But Funny: A Feedback-Driven Approach to Humor Distillation

**Sahithya Ravi, Patrick Huber, Akshat Shrivastava, Aditya Sagar, Ahmed Aly, Vered Shwartz, Arash Einolghozati** — ACL 2024 · Guide entry #15 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2402.18113) · [local PDF](../pdfs/15-small-but-funny.pdf) · [full markdown](../md/15-small-but-funny/15-small-but-funny.md) · [extract](../extracts/15-small-but-funny.json)

## TL;DR
This paper studies whether humor generation can be distilled from a large teacher LLM into a smaller model using not only imitation, but also feedback. Llama2-70B generates humorous paraphrases and then critiques BART-large student outputs; the best variant, BART-BRIO-DPO, reaches WTR_llama2 = 65 and WTR_GPT4 = 56 against the teacher, versus BART-FT at 28 and 30.

## Problem & Motivation
The task is conditional humor generation: given a literal text, generate a humorous paraphrase that broadly preserves the meaning. The authors argue that imitation-only distillation is insufficient for creative tasks because small models may overfit to the teacher’s surface style without learning what makes outputs funny. Chain-of-thought distillation is also less natural here because, as the paper states, it is difficult to come up with a recipe for a joke.

## Approach
The proposed framework has two phases. In the imitation phase, Llama2-70B acts as a teacher and generates N = 3 humorous paraphrases per literal input; BART-large is fine-tuned on the resulting literal-humorous pairs. In the critique phase, the fine-tuned student generates k = 6 candidates, the authors choose a diverse pair using maximum pairwise n-gram-based edit distance, and Llama2-70B acts as a critic. The critic uses Multiple Choice Prompting to choose the better paraphrase based on humor, human-likeness, and faithfulness to the input. The feedback is incorporated using BRIO, DPO, or a combined BRIO-DPO variant. To mitigate known critic biases, training pairs are filtered to have length ratios between 0.8 and 1.2, and evaluation averages both presentation orders.

## Data & Experimental Setup
Literal inputs come from EmpatheticDialogues: 12,000 training sentences are sampled, and Llama2-70B generates 36,000 literal-humorous text pairs. The authors also sample 1,000 sentences from validation and test sets and 100 test samples for human evaluation. For out-of-distribution evaluation, they use 500 literal inputs from Samsum. Teacher generation uses the 70B chat version of Llama 2 with temperature 0.8 and top_p = 1. Student outputs use BART-large with beam search and 5 beams. Automatic evaluation uses Win Tie Rate against the teacher with either Llama2-70B or GPT-4 as critic.

## Results
In main automatic evaluation, BART-BRIO-DPO is strongest: WTR_GPT4 = 56 and WTR_llama2 = 65. This beats BART-FT at 30 and 28, BART-SD at 35 and 36, BART-BRIO at 48 and 53, and BART-DPO at 52 and 60. On the 500-example Samsum OOD set, BART-BRIO-DPO scores WTR_llama2 = 49, compared with BART-FT = 34, BART-BRIO = 42, and BART-DPO = 47. The critic study shows MCP WTR has Ag-H = 76, Ag-C = 59, PB = 15, and LB = 20, while cloze WTR has Ag-H = 57 and Ag-C = 47. In Table 4, more frequent feedback helps: BART-BRIO with 12K data rises from 43 at 1/10 epochs feedback to 56 at 2/10 and 66 at 10/10.

## Takeaways
- Feedback is much more effective than imitation alone for this humor-generation distillation setup.
- DPO and BRIO both help; combining them is best in the main in-distribution automatic evaluation.
- LLM critics can be useful for humor feedback, but their length and position biases must be measured and mitigated.
- Simply adding more imitation data is not enough: BART-BRIO with 12K examples beats BART-FT with 36K examples in Table 4.

## Limitations & Caveats
Humor is subjective and culturally variable, and the paper observes North America-centered celebrity and event references. LLM feedback can propagate model and evaluation biases into the student. More frequent feedback also increases teacher communication cost, and length bias can make student outputs much longer without filtering.
