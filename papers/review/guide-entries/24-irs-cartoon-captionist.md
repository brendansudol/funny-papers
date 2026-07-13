<!-- guide claims for 24-irs-cartoon-captionist (#24) -->

### 24. [Learning to Think Like a Cartoon Captionist: Incongruity-Resolution Supervision for Multimodal Humor Understanding](https://arxiv.org/abs/2604.15210)
Vural et al. — **2026** · `preprint` `method`
- **Method:** IRS (Incongruity-Resolution Supervision) decomposes visual humor understanding into three learnable stages — *incongruity modeling* (spotting the visual mismatch), *resolution modeling* (constructing a coherent reinterpretation), and *preference alignment* (scoring candidate interpretations against human judgments) — supervising the *intermediate reasoning trace*, not just the answer (continual pretraining → SFT on captionist-style traces → alignment with humor judgments).
- **Dataset:** New Yorker Cartoon Caption Contest (matching/ranking).
- **Findings:** Grounded explicitly in incongruity-resolution theory (T5), script opposition (T2), and frame-shifting (Coulson). It creates a direct bridge between humor theory and the cartoon-caption benchmark line by operationalizing "why is this funny?" as an explicit, learnable reasoning process rather than black-box ranking.
