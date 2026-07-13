# Does Bigger Mean Funnier? Evaluating Humor Generation Across the Qwen3 Model Family

**Jatin Agrawal, Radhika Mamidi** — CHum 2026 · Guide entry Part 4 (judge-validity stress test) (Part 4 - Evaluation Methodology)

[paper page](https://aclanthology.org/2026.chum-1.7/) · [local PDF](../pdfs/x20-does-bigger-funnier.pdf) · [full markdown](../md/x20-does-bigger-funnier/x20-does-bigger-funnier.md) · [extract](../extracts/x20-does-bigger-funnier.json) · [dataset: Qwen3 humor parameter ablation data](../../data/does-bigger-funnier/)

## TL;DR
This paper tests whether larger Qwen3 models generate funnier jokes by running a controlled within-family ablation from 8B to 235B parameters. DeepSeek-V3.2 as an automated judge gives a perfect monotonic scaling result, but human annotators find no significant aggregate difference; only the 22 high-agreement themes show a significant human preference for Qwen3-235B-A22B (p = 0.039).

## Problem & Motivation
Scaling laws show predictable gains for language modeling, but it is unclear whether those gains transfer to creative humor generation. Humor depends on timing, world knowledge, pragmatic inference, and subjective taste. The paper asks both whether “bigger means funnier” within one model family and whether LLM-as-a-judge evaluation is reliable for a subjective task where human agreement is expected to be low.

## Approach
The authors evaluate five instruction-tuned Qwen3 models: dense 8B, 14B, and 32B models, plus MoE 30A3 and 235A22 variants. Each model writes one short joke for each of 50 everyday themes using the same prompt, max_tokens=128, and /no_think enabled to suppress reasoning. Automated evaluation uses DeepSeek-V3.2 for pairwise comparisons in both presentation orders, with Bradley-Terry aggregation. Human evaluation is blinded and ranks three models—32B, 30A3, and 235A22—on 40 themes.

## Data & Experimental Setup
The dataset contains 50 everyday humor themes spanning technology, social interactions, workplace life, and domestic situations, while avoiding culturally sensitive or likely offensive topics. Automated judging compares all 10 model pairs per theme in both orderings, producing 999 comparisons because one API timeout removed one planned comparison. Human evaluation uses two independent groups of six annotators; for each theme, three anonymized jokes appear in random order for 60 seconds and annotators rank them from funniest to least funny, yielding 240 total rankings.

## Results
The LLM judge reports monotonic scaling: win rates are 33.5% for 8B, 49.2% for 14B, 51.6% for 30A3, 54.6% for 32B, and 61.0% for 235A22, with Spearman ρ = 1.0, p < 0.001. However, it also shows major artifacts: Position A wins 73.5% of comparisons (χ² = 215.9, p < 0.001), and the longer joke wins 62.2% of the time when lengths differ (binomial p < 0.0001). Humans show no significant aggregate model difference: 235A22 has mean rank 1.900 and 40.8% first-place rankings, but the Friedman test is χ² = 3.73, p = 0.155, with Krippendorff’s α = 0.098. On 22 high-agreement themes, results become significant: 235A22 mean rank 1.833, 32B 2.023, 30A3 2.144; Friedman χ² = 6.47, p = 0.039, and 235A22 beats 30A3 by Wilcoxon W = 3404, p = 0.020.

## Takeaways
- LLM judges can overstate clean scaling trends on subjective humor tasks.
- Human judgments suggest a “quality floor”: many model jokes are structurally competent but indistinguishable.
- Scaling benefits appear when themes produce distinguishable jokes, especially through stronger incongruity and punchlines.
- Positional and length bias must be measured before relying on LLM-as-a-judge results for creative generation.
- Dense versus MoE differences remain suggestive, not conclusive.

## Limitations & Caveats
Each model generated only one joke per theme, the dataset is small, and only one automated judge was tested. Human evaluation covered only three of five models and had low agreement. Disabling reasoning isolates generation but excludes deliberative inference. The paper also cannot determine whether jokes are novel or memorized, and originality was not separately scored.
