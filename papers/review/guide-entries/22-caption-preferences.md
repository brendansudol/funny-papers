<!-- guide claims for 22-caption-preferences (#22) -->

### 22. [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://arxiv.org/abs/2406.10522)
Zhang, Jain, Guo, Chen, Zhou, Suresh, Wagenmaker, Sievert, Rogers, Jamieson et al. — **NeurIPS 2024 (D&B)** · `peer-reviewed` `dataset` `benchmark`
- **Method:** A very large-scale cartoon-caption *preference* dataset and benchmark for ranking/generation, built from New Yorker contest crowd votes, with GPT-4 and human-judgment ranking metrics.
- **Dataset:** 365 contests (numbers 530–895), 2.2M+ captions, and 250M+ human ratings (funny / somewhat funny / unfunny) collected over ~8 years via the NEXT multi-armed-bandit crowdsourcing platform.
- **Findings:** The major large-scale resource extending Hessel's line. Headline results: SFT *hurts* the generation task, RLHF and DPO **underperform** on this creative objective, and even GPT-4 and Claude still **trail top human contestants** at producing winning captions — a sobering scale-isn't-enough result, given a quarter-billion ratings. (The same group later builds HumorBench, #3, to isolate comprehension from preference.)
