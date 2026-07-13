<!-- guide claims for 01-androids-electric-sheep (#1) -->

### 1. [Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest](https://arxiv.org/abs/2209.06293)
Hessel, Marasović, Hwang, Lee, Da, Zellers, Mankoff & Choi — **ACL 2023** · `peer-reviewed` `benchmark`
- **Method:** Three tasks on New Yorker cartoons — caption/cartoon matching, quality ranking, and explanation generation.
- **Dataset:** 704 cartoons with thousands of finalist captions (2.7K high-quality); explanations annotated with required world knowledge.
- **Findings:** The foundational benchmark; models trail humans on all three tasks, widest on explanation. Concretely: the best from-pixels model hit 62% on 5-way matching vs. 94% for humans, GPT-4 (5-shot) reached 84.5% on matching *given human-written scene descriptions* — and even then, human-authored explanations were preferred head-to-head over GPT-4's in more than two-thirds of cases. Everything downstream builds on it.
