# Which LLMs Get the Joke? Probing Non-STEM Reasoning Abilities with HumorBench

**Reuben Narad, Siddharth Suresh, Jiayi Chen, Pine S.L. Dysart-Bricken, Bob Mankoff, Robert Nowak, Jifan Zhang, Lalit Jain** — arXiv:2507.21476 · Guide entry #3 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2507.21476) · [local PDF](../pdfs/03-humorbench.pdf) · [full markdown](../md/03-humorbench/03-humorbench.md) · [extract](../extracts/03-humorbench.json) · [dataset: HumorBench](../../data/humorbench/)

## TL;DR
HumorBench is a benchmark for testing whether LLMs can explain sophisticated cartoon-caption jokes by identifying objective joke elements rather than matching audience funniness preferences. The best main result is OpenAI o3 at 87.5% accuracy on HumorBench, but on the 100-element HumorBench-Hard subset the best model, o3, reaches only 59.85%.

## Problem & Motivation
Existing reasoning benchmarks in mathematics, science, and programming are increasingly saturated, so the paper proposes humor comprehension as a non-STEM reasoning probe. The authors argue that understanding cartoon-caption humor requires forming and testing connections among visual concepts, captions, cultural references, wordplay, and implications. Prior New Yorker Caption Contest benchmarks can mix two capabilities: understanding the intended joke and aligning with subjective audience preferences. HumorBench is designed to isolate the first capability by grading explanations against factual, objective joke components.

## Approach
Each example consists of a detailed textual cartoon description, a caption, and one to three hand-written “element” annotations. An element is a short, verifiable statement that captures a necessary objective part of the joke, such as a pun, reference, implication, or dual meaning. Models are prompted to explain the joke in under 200 words. A GPT-4o autograder then checks whether the explanation explicitly covers each anticipated element. The authors refined annotations iteratively by generating sample explanations, grading each element ten times, and revising or removing elements with more than 30% autograder disagreement until fewer than 5% triggered inconsistency flags.

## Data & Experimental Setup
HumorBench contains approximately 300 unique cartoon-caption pairs from the New Yorker Caption Contest and Cartoonstock.com and 499 high-quality unique element annotations. NYCC captions were drawn from publicly available datasets and restricted to top-3 finalists; Cartoonstock examples used original captions. The benchmark is text-only: the visual cartoon is represented by a detailed neutral description. The authors validated the GPT-4o autograder on 300 human expert judgments over explanations from GPT-4o, Gemini 2.5 Pro, and Claude 3.7 Sonnet. They benchmarked frontier, open-source, and reasoning models, with temperature set to 1 where possible and external tool calling deactivated. Outputs were truncated to the last 1000 tokens for length control.

## Results
The GPT-4o autograder achieved 92.00% overall accuracy on the 300 human-labeled judgments, with 14.79% FPR and 6.51% FNR; the authors therefore treat benchmark scores as upper bounds. On the main benchmark, o3 led with 87.5% accuracy, while Gemini 2.5 Pro, Claude 3.7 Sonnet, and DeepSeek R1 achieved approximately 80%. Reasoning variants improved over base models: DeepSeek R1 scored 79.8% versus DeepSeek V3 at 72.2%, and Claude 3.7 Sonnet with a 1024-token thinking budget scored 83.6% versus base Claude 3.7 Sonnet at 80.4%. HumorBench correlated with other reasoning benchmarks: GPQA Diamond 0.736 (p = 0.024), ARC-AGI 0.650 (p = 0.058), ARC-AGI without o-series 0.943 (p = 0.005), and LM Arena ELO 0.714 (p = 0.071). On HumorBench-Hard, o3 reached 59.85%; Qwen/Qwen2.5-72B-Instruct-Turbo scored 26.83%.

## Takeaways
- Objective element rubrics make open-ended humor explanation automatically gradable while reducing dependence on subjective funniness preferences.
- STEM reasoning progress appears to transfer to humor: HumorBench rankings correlate strongly with GPQA Diamond and especially ARC-AGI without o-series models.
- STEM-only reasoning-trained models, including DeepSeek R1 Zero and Phi-4 Reasoning Plus, outperform their base versions, suggesting abstract reasoning skills help humor comprehension.
- More test-time compute is not uniformly helpful: Qwen Plus and o-series models improved with more reasoning effort, but Claude 3.7 Sonnet worsened beyond the 1024-token thinking budget.
- Hard examples are not explained simply by broad categories: wordplay was under-represented in the hard subset by -5.4%, while cultural references and toxic or shocking humor were nearly evenly represented.

## Limitations & Caveats
HumorBench removes vision by using textual descriptions, so it does not test recognition of visual cues. The autograder is lenient, making reported scores optimistic. Some annotations may still contain errors or subjective interpretations, and 499 unique elements limit fine-grained statistical analysis.
