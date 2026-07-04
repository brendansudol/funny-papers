<!-- guide claims for 35-humorrank (#35) -->

### 35. [HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation](https://arxiv.org/abs/2604.19786)
Ajayi & Mitra — **2026** (arXiv:2604.19786) · `preprint` `benchmark` `method`
- **Method:** Pairwise, GTVH-grounded LLM judgments aggregated via Adaptive Swiss tournament + Bradley–Terry into global rankings; 9 models on SemEval-2026 MWAHAHA (#57) + Humor Transfer Bench.
- **Findings:** Cross-judge stable (Llama/Qwen judges agree, Kendall τ≈0.89); strong humor depends on mastery of mechanisms (incongruity, conciseness, escalation, absurdity), not just scale. Pairwise/tournament is often more plausible than absolute funniness scores.
- **Disclosure:** Same authors as HumorGen (#13), and the leaderboard ranks their own HumorGen-7B 4th, above models an order of magnitude larger — consistent with, but not independent of, the "mechanisms over scale" headline. (One counter-signal to judge self-preference worries: the Llama judge ranks its own generations 8th of 9.)
