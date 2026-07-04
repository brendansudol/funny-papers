<!-- Transcribed from 35-humorrank.pdf -->



<!-- page 0001 -->

Submitted to COLM 2026

---

# HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation in Large Language Models*

**Edward Ajayi**  
Carnegie Mellon University Africa  
Kigali, Rwanda  
eaajayi@andrew.cmu.edu

**Prasenjit Mitra**  
Carnegie Mellon University Africa  
Kigali, Rwanda  
prasenjm@andrew.cmu.edu

## Abstract

Humor remains difficult to evaluate in large language models (LLMs) because what makes a response funny is subjective, comparative, and shaped by interacting comedic mechanisms rather than a single scalar property. Existing humor evaluation protocols therefore tend to produce isolated scores or task-specific judgments that are difficult to compare across models. We introduce HumorRank, a tournament-based framework for ranking textual humor generation through theory-grounded pairwise preference judgments. Across SemEval-2026 MWAHAHA and Humor Transfer Bench, HumorRank evaluates nine proprietary, open-weight, and specialized models using LLM-based comparative judgments informed by the General Theory of Verbal Humor (GTVH), with tournament aggregation yielding global rankings via Bradley–Terry estimation. The resulting rankings are *cross-judge stable*: independent Llama and Qwen LLM judges achieve Kendall $\tau$ = 0.889 on both benchmarks. The leaderboard reveals clear model stratification, showing that strong humor generation depends not only on scale but on mastery of comedic mechanisms such as incongruity, conciseness, escalation, and absurdity. HumorRank provides a scalable and interpretable methodology for benchmarking LLM-generated humor without relying solely on isolated automatic metrics or limited human evaluation.

## 1 Introduction

Humor generation is a domain that requires a highly nuanced understanding of language, context, and pragmatic reasoning (Quan et al., 2025; Kim & Chilton, 2025), posing a significant challenge for evaluating the capabilities of large language models (LLMs) in generating humor (Narad et al., 2025). This difficulty is reflected in the fragmented landscape of existing evaluation methods, where different studies adopt incompatible paradigms Ajayi & Mitra (2025), including punchline detection (Romanowski et al., 2025), scalar scoring (Goes et al., 2022), humor classification (Wu et al., 2025a), LLM-as-a-Judge approaches (Shafiei & Saffari, 2025), and costly human preference evaluations (Romanowski et al., 2025; Horvitz et al., 2024).

A central limitation of these approaches is the lack of a unified and scalable framework for comparing models. Existing methods measure different aspects of humor and do not produce consistent rankings across systems, making it difficult to track progress. As LLMs increasingly operate in interactive and creative settings, establishing a reliable and comparable evaluation protocol for humor generation becomes essential. To address this gap, we introduce **HumorRank**, a leaderboard-oriented framework for ranking humor generation in language models. HumorRank casts evaluation as a pairwise preference problem and aggregates outcomes into a globally consistent ranking. We evaluate nine models on SemEval-2026 Task 1: MWAHAHA (Castro et al., 2026) and Humor Transfer

\*Live leaderboard: https://humorrank-leaderboard.pages.dev/.



<!-- page 0002 -->

Bench (HTB) (Ajayi & Mitra, 2026), demonstrating scalable, interpretable, and reproducible comparison of humor generation systems.

Our contributions are as follows:

1. We introduce **HumorRank**, a scalable tournament-based leaderboard framework that operationalizes humor evaluation as global capability ranking over competing language models.

2. We formalize humor assessment as a **pairwise preference learning task** and use Bradley–Terry estimation for stable, comparable global rankings; to make this practical at scale, we pair it with a **budget-aware Adaptive Swiss Pairing** strategy that preserves rank fidelity under reduced comparison budgets.

3. We develop a **GTVH-grounded pairwise LLM-judge protocol for humor evaluation** that outputs structured winner rationales and mechanism/delivery/failure tags, enabling interpretable diagnostics beyond scalar funniness scores.

## 2 Related Works

### 2.1 Model Evaluation in Humor Generation Systems

Despite growing interest in LLM humor capabilities, evaluation protocols remain inconsistent and difficult to compare across studies. Prior work spans automated metrics for human-AI co-creative humor Wu et al. (2025b), crowd-sourced AI voting panels Goes et al. (2022), Best-Worst Scaling (BWS) Yamane (2024), Likert-style funniness templates Goerenz & Schwarz (2024), and fully human evaluation, which is costly and usually limited to small validation sets Zhang et al. (2024); Goel et al. (2024); Wang et al. (2025); Jain et al. (2024). Broader evaluations of LLM humor understanding and generation Ajayi & Mitra (2025); Zhou et al. (2025); Song et al. (2025) extend these paradigms across task formulations. However, these approaches typically yield task-specific scores rather than *ranked preference orderings* across multiple generation systems, and they rarely provide interpretable comparative rationales. As a result, evaluation is often a one-off measurement rather than a scalable comparative framework. This gap contrasts with broader NLP evaluation, where tournament-based rating systems have emerged as a principled alternative (Section 2.3).

### 2.2 Computational Humor: Datasets, Theory, and Generation

Humor is rooted in psychology Larkin-Galiñanes (2017) and linguistics Attardo (2024), with classical theories such as superiority, relief, and incongruity explaining humor Veatch (1998). These frameworks motivate interpretable dimensions of humor, such as expectation violation, tension release, and social positioning. However, they do not provide a deterministic recipe for generation Larkin-Galiñanes (2017), as humor varies across context, culture, and individual perception. Linguistic and pragmatic analysis identifies relatively stable cues such as timing, delivery, ambiguity, and form–meaning incongruity, which support dataset construction and automated evaluation. Building on these foundations, prior work has introduced a range of humor benchmarks, historically focused on text-based tasks. More recently, advances in large language models have expanded this landscape to include multimodal datasets and evaluation settings spanning humor generation, understanding, and ranking Zhong et al. (2024); Zhang et al. (2024); He et al. (2024); Ryan et al. (2025); Jain et al. (2024). These developments broaden computational humor, highlighting challenges in consistent model comparison.

### 2.3 LLM Leaderboard Rating Systems in NLP Tasks

Leaderboard-based evaluation has become prevalent in NLP, providing a standardized framework for comparing model performance across tasks and benchmarks Toloka Team (2023); Chiang et al. (2024); Myrzakhan et al. (2024). Modern leaderboard platforms, such as Chatbot Arena Chiang et al. (2024) and the Open LLM Leaderboard Silva et al. (2026), often leverage *LLM-as-a-Judge* paradigms Zheng et al. (2023) to enable scalable evaluation of model



<!-- page 0003 -->

[Figure: Overview diagram of the HumorRank evaluation pipeline with stages labeled Input Prompts, Contestant LLMs, Pairwise Scheduler, LLM Judge, Match History, Rating, and Leaderboard, plus optional cross-judge validation and a legend for Input, Generation, Scheduling, Judging, Data, Rating, Output, and Optional.]

**Figure 1:** Overview of the HumorRank evaluation pipeline. Contestant models generate jokes on shared prompts; Adaptive Swiss pairing schedules pairwise duels; a GTVH-grounded LLM judge adjudicates each duel; outcomes are aggregated into match history and converted to global Bradley–Terry ratings (primary) and Stable Elo scores (audit), producing a ranked leaderboard with interpretable humor-feature profiles.

outputs. This approach supports both human and model-based preference judgments, enabling flexible evaluation. Furthermore, leaderboard-based systems facilitate direct comparison of models under consistent conditions, making them suitable for benchmarking progress in NLP Federiakin (2025); Myrzakhan et al. (2024). Prior work suggests that such ranking frameworks provide a reliable proxy for model quality and can be adapted to diverse settings, including multilingual and domain-specific evaluation scenarios Park et al. (2024); Silva et al. (2026).

## 3 HumorRank

The subjective and multidimensional nature of humor presents fundamental challenges for absolute quality scoring. To address this, we operationalize humor as a continuous *cognitive reward* arising from the successful resolution of deliberately constructed linguistic incongruities (for our full formal definition and derivation, see Appendix A). Because lexical and semantic humor features (e.g., comedic delivery) (Romanowski et al., 2025; Kim & Chilton, 2025) interact in ways that resist direct quantification (Winters & Van der Stockt, 2025), pairwise comparison mitigates these limitations (Ravi et al., 2024) by constraining evaluation to a relative preference judgment between two model-generated jokes conditioned on the same prompt (Hossain et al., 2020). This formulation reduces cognitive load on the evaluator and is more robust to inter-annotator variance than uncalibrated scalar annotation.

While pairwise comparisons provide high-fidelity local signal, they are still discrete and unordered, and thus insufficient on their own to support a system-level leaderboard. To transform a collection of $\binom{K}{2}$ pairwise outcomes over $K$ competing models into a globally consistent capability ranking, an aggregation framework must resolve local inconsistencies and propagate information across the full tournament graph. **HumorRank** addresses this through a two-stage pipeline: an Adaptive Swiss Tournament that efficiently builds the pairwise comparison graph, followed by global Bradley–Terry (BT) Maximum Likelihood Estimation (MLE) that maps observed outcomes to statistically grounded, continuous capability estimates. We additionally report Stable Elo ratings as a secondary reference metric for cross-validation.



<!-- page 0004 -->

### 3.1 Pairwise Comparison

Humor evaluation in this setting differs from standard LLM-as-a-Judge tasks (e.g., instruction following, summarization): SemEval-2026 MWAHAHA requires ranking *multiple model-generated jokes on the same prompt*, which is inherently relative. We therefore use same-prompt pairwise preferences as the primary supervision signal and aggregate outcomes with Bradley–Terry MLE into a global leaderboard. Alternative judge configurations and ablation details are documented in Appendix B.

### 3.2 Bradley-Terry Global Maximum Likelihood Estimation

The Bradley-Terry model (Bradley & Terry, 1952) serves as our primary, order-independent ranking algorithm. By maximizing the likelihood of observed pairwise outcomes across the full tournament graph, BT estimates a latent “humor capability” score for each model. Preference-based BT-style rating has also been widely used in non-humor LLM evaluation settings, including arena-style leaderboards (Chiang et al., 2024; Myrzakhan et al., 2024).

Given models $i$ and $j$ with latent ratings $R_i$ and $R_j$, the probability that model $i$ wins over model $j$ is formulated as an Elo-scaled logistic function:

$$
P(\text{i wins against j}) = \frac{1}{1 + 10^{(R_j - R_i)/400}}
\tag{1}
$$

Instead of sequential updates, HumorRank fits global MLE using the iterative Minorization-Maximization (MM) algorithm until convergence ($\epsilon < 10^{-6}$), with ratings anchored at 1000. To quantify uncertainty in model separation, we report 95% confidence intervals via 200 bootstrap resamples of the match history (seed 42).

### 3.3 Stable Elo (Sequential Reference)

While the BT model provides the global MLE, we simultaneously compute a sequential Elo rating Albers & Vries (2001) to track dynamic stability and provide a secondary reference metric. The generalized sequential update rule is:

$$
R_{\text{new}} = R_{\text{curr}} + K_{fac} \cdot (S - E)
\tag{2}
$$

where $K_{fac} = 32$ specifies the maximum volatility factor, $S$ denotes the observed outcome (1.0 for a win, 0.5 for a tie, 0.0 for a loss), and $E$ is the expected probability derived from Equation 1.

A known deficiency of standard Elo is order dependence, wherein the specific sequence of matches heavily influences the final ratings. HumorRank mitigates this vulnerability by implementing *Stable Elo*: the entire tournament history is evaluated across $N=10$ randomly shuffled topological orderings. The final assigned score is the arithmetic mean of the resulting terminal ratings, yielding strong empirical sequence robustness (see Appendix K for shuffle audit;).

### 3.4 Adaptive Swiss Pairing

For large model pools, exhaustive $\mathcal{O}(K^2)$ pairwise comparisons become computationally expensive. HumorRank resolves this through *Adaptive Swiss Pairing* (ASP): a single scheduling engine controlled by budget parameter $C_{\max}$ that preferentially matches models of similar standing while avoiding repeat pairings. ASP uses a temporary online strength score only for matchmaking; final leaderboard ratings are always computed with global Bradley–Terry MLE. A pair $(i, j)$ is *under-sampled* when its observed duel count in the current match graph $G$ falls below the target count implied by $C_{\max}$; ASP prioritizes such pairs in each scheduling round until the budget is exhausted.

At maximum budget, $C_{\max}$ recovers exhaustive round-robin (**Full RR**). Reduced-budget modes subsample duels via the same ASP engine: **Swiss 2RR** fixes two rounds per model,



<!-- page 0005 -->

while **Swiss 3RR** fixes three rounds per model. Under a Swiss schedule with $R(K)$ rounds per model, the per-prompt comparison count is approximately $\frac{K R(K)}{2}$: therefore, fixed-round modes ($R \in \{2,3\}$) are $\mathcal{O}(K)$, and only schedules with $R(K)=\Theta(\log K)$ yield $\mathcal{O}(K \log K)$ comparisons per prompt. We abbreviate all round-robin schedules as RR throughout. We do not claim a formal convergence proof for BT under ASP; however, empirical fidelity and budget trade-offs are reported in Section 5.3 and Appendix C. The full ASP algorithm is provided in Appendix D (Algorithm 1).

## 4 Experimental Setup

To empirically validate the HumorRank methodology, we execute a large-scale evaluation on two headline-conditioned humor generation benchmarks. Our experimental design tests discriminative power across varying model architectures, access paradigms, and parameter scales. Full reproducibility details, including hyperparameters and computational budget, are provided in Appendix G.

### 4.1 Benchmarks

We evaluate on two publicly available headline-conditioned humor generation benchmarks:

**SemEval-2026 MWAHAHA** (Castro et al., 2026): part of the SemEval-2026 MWAHAHA competition for English joke generation from news-headline prompts; we use the official Task 1 test set (300 prompts).

**Humor Transfer Bench (HTB)** (Ajayi & Mitra, 2026): 400 headline prompts held out from the SemEval distribution to test cross-benchmark generalization. The same nine-model contestant pool and pairwise judge protocol are applied to both benchmarks.

### 4.2 Model Evaluation Suite

We evaluate a deliberately diverse suite of 9 language models to assess the leaderboard’s capacity to resolve fine-grained capability differences. The inclusion criteria strictly span multiple model lineages and access paradigms:

- **Frontier Proprietary Models:** GPT-5 Singh et al. (2025), Gemini 2.5 Pro Comanici et al. (2025), Claude 3.5 Haiku Anthropic (2024), and Kimi K2 Team et al. (2026).
- **Open-Weight Competitive Models:** Qwen 3 32B Bai et al. (2025), GPT OSS 120B Agarwal et al. (2025), and Llama 3.3 70B Instruct Grattafiori et al. (2024).
- **Specialized and Baseline Models:** *HumorGen-7B* (Ajayi & Mitra, 2026) (a Qwen-7B specialist trained via Cognitive Synergy Fusion (CSF) and supervised fine-tuning (SFT) in the HumorGen pipeline), alongside *Base Qwen-7B* (Team, 2024) as the zero-shot architecture control.

This suite reflects practical compute and API budget constraints while preserving representation across closed, open-weight, and domain-specialized systems.

### 4.3 Evaluation Protocol and LLM-as-Judge Ablation

HumorRank employs open-weight models as pairwise LLM judges, executing a full round-robin schedule over all contestant pairs on each benchmark (**Full RR**; $K=9$ in our experiments).

**LLM Judges:** Llama 3.3 70B Instruct serves as the primary judge, and Qwen 2.5 72B Instruct serves as the secondary judge for cross-judge validation. For each duel, the LLM judge selects the funnier joke (A, B, or TIE), returns brief reasoning, and tags GTVH humor mechanisms, delivery features, and failure modes. Prompt order is swapped across comparisons to mitigate position bias. The full pairwise judge prompt template is in Appendix H.



<!-- page 0006 -->

**Judge Ablation & Validity Check:** We independently re-evaluate the same Full RR duels on SemEval and HTB with Qwen 2.5 72B Instruct as a secondary LLM judge. SemEval Qwen-judge ratings are in Appendix E; cross-benchmark $\tau$ and budget ablations are in Appendix C. A blind human annotation study on 60 stratified SemEval pairs grounds LLM judge judgments against human perception (Appendix J).

## 5 Results

Our evaluation yields an extensive empirical profile of humor capability across current language models. We present the system-level Bradley-Terry (BT) leaderboard, validate its stability across independent LLM judges, and subsequently decompose these ratings into interpretable psychometric features.

### 5.1 HumorRank Leaderboard

The main tournament, adjudicated by the primary Llama judge across 10,800 matches, reveals a clear stratification of model capabilities. Table 1 reports BT ratings, Stable Elo reference scores, 95% confidence intervals, and win rates.

| Rank | Model | BT Rating | Stable Elo | 95% CL | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1307.5 | 1317.6 | [1289.9, 1325.9] | 84.0% |
| 2 | Kimi-K2 | 1156.9 | 1175.7 | [1139.9, 1170.7] | 67.8% |
| 3 | Gemini 2.5 Pro | 1115.1 | 1115.3 | [1099.0, 1128.1] | 62.6% |
| 4 | **HumorGen-7B<sup>1</sup>** | **1092.8** | **1102.2** | **[1078.7, 1108.5]** | **59.8%** |
| 5 | Claude 3.5 Haiku | 1037.5 | 1027.3 | [1024.1, 1050.9] | 52.7% |
| 6 | GPT OSS 120B | 1015.0 | 1002.2 | [1001.7, 1030.6] | 49.8% |
| 7 | Qwen 3 32B | 976.9 | 966.2 | [964.7, 988.8] | 45.0% |
| 8 | Llama 3.3 70B | 761.0 | 754.0 | [743.9, 780.6] | 21.8% |
| 9 | Base Qwen 7B | 537.4 | 539.4 | [513.5, 563.5] | 6.5% |

Table 1: Primary HumorRank Leaderboard (Llama 3.3 70B Judge). BT ratings are the primary metric; Stable Elo (10 shuffle runs, mean terminal rating) is reported as a sequence-robust reference. Models cleanly separate into a Frontier Elite tier (> 1100), a Competitive Mid-Tier (970–1100), and a Weak Baseline (< 800).

The specialized *HumorGen-7B* model (Rank 4, BT = 1092.8) places above substantially larger general-purpose models (e.g., GPT OSS 120B, Rank 6; Table 1). The primary Llama judge also ranks its own generations 8th of 9 (BT = 761.0), which does not indicate self-favoring behavior in this setup. Full-round-robin leaderboard and win-rate heatmap visualizations are provided in Appendix C. At the duel level (300 prompt-conditioned judgments per model pair on SemEval Full RR), two-sided binomial tests reject a 50% null win rate for 32/36 pairings at $\alpha$=0.05, with the remaining four concentrated in close mid-tier matchups.

### 5.2 Cross-LLM-Judge Validity and Rank Stability

Evaluating subjective data is inherently sensitive to the choice of the primary LLM judge. We replicate all full round-robin duels on both benchmarks with Qwen 2.5 72B Instruct as an independent secondary LLM judge (SemEval ratings: Appendix E; $\tau$ tables: Appendix C). Qwen-adjudicated Bradley–Terry ratings correlate strongly with the primary Llama 3.3 70B leaderboard on SemEval and HTB: Kendall’s $\tau$ = 0.889 ($p$ = 0.0002) in each benchmark, and the same value when pooling all 25,200 Llama–Qwen LLM-judge pairwise labels (82.9% agreement; Krippendorff $\alpha$ = 0.658). Contestant ordering is *cross-judge stable*: GPT-5 and Kimi K2 remain at ranks 1–2; Llama 3.3 70B and Base Qwen 7B remain at ranks 8–9, with modest mid-tier reordering only. We also report a **transitivity score**: among all model triples

[^1]: Referred to HumorGen-7B as HumorGen SFT 7B in plots and figures.



<!-- page 0007 -->

with a clear pairwise winner on each edge, the fraction with no directed 3-cycle in the win graph (1.0 = no intransitivity); this score is 1.0 under both LLM judges on both benchmarks.

### 5.3 Tournament Budget Ablation

Full round-robin is expensive as $K$ grows. Because ASP is the same engine at every budget, we ablate Swiss 2RR and Swiss 3RR schedules using the same pairing logic and fixed budget constraints. Table 2 summarizes comparison budget and cross-LLM-judge Kendall $\tau$ averaged over four cells (SemEval/HTB × Llama 3.3 70B/Qwen judges). At $K=9$, Swiss 3RR uses 12 pairs/prompt (~33% of Full RR) and restores SemEval Llama↔Qwen agreement to $\tau = 0.889$, matching Full RR. Ranks #1 (GPT-5), #8 (Llama 3.3 70B), and #9 (Base Qwen 7B) are stable across Full RR, Swiss 2RR, and Swiss 3RR in all four evaluation cells. We treat Swiss 3RR as the practical scaling mode when exhaustive coverage is infeasible; per-benchmark breakdowns are in Appendix C.4 (SemEval) and Appendix C.5–C.6 (HTB).

| Schedule | Pairs / prompt ($K=9$) | Budget | Avg. cross-LLM-judge $\tau$ |
|---|---:|---:|---:|
| Full RR | 36 | 100% | 0.889 |
| Swiss 3RR | 12 | ~33% | 0.861 |
| Swiss 2RR | 8 | ~22% | 0.806 |

Table 2: Adaptive Swiss Pairing budget ablation across Full RR, Swiss 3RR, and Swiss 2RR. SemEval Llama 3.3 70B↔Qwen 2.5 72B LLM-judge $\tau = 0.889$ under both Full RR and Swiss 3RR.

### 5.4 Human and LLM Judge Agreement

To assess reliability of our LLM-as-a-Judge pipeline, we conducted a blind annotation study with human evaluators ($n = 2$, then $n = 3$) on 60 SemEval pairs stratified by tournament tier (cross-tier and within-tier cells), comparing their preferences against our production LLM judges (Llama 3.3 70B and Qwen 2.5 72B Instruct). Because humor preference is inherently subjective and has no single ground-truth label, we quantify reliability as agreement beyond chance rather than accuracy; accordingly, we use Krippendorff’s $\alpha$ (Krippendorff, 2011), which is defined for nominal A/B/Tie labels and supports multi-rater cohorts with incomplete overlap. Inter-annotator reliability is moderate across human-only cohorts ($\alpha = 0.432$ for the highest-agreement two-rater dyad; $\alpha = 0.397$ with all three annotators on 55 fully overlapping pairs). Human–human agreement (47.1%), computed by pooling agreement across all annotator dyads on overlapping votes, is not significantly different from human–Llama judge vote agreement (49.7%; Fisher exact $p = 0.667$); the Llama and Qwen judges agree on the same 60 pairs at 50.0% ($\alpha = 0.425$). Table 3 reports a compact cohort-level reliability summary; per-annotator dyad breakdowns are reported in Appendix J (Table 22).

| Metric | Humans ($n$=2) | Humans ($n$=3) | Llama–Qwen LLM judges |
|---|---:|---:|---:|
| Krippendorff $\alpha$ (nominal) | 0.432 | 0.397 | 0.425 |

Table 3: Compact human and LLM judge agreement summary on blind re-ratings of 60 SemEval duels. Human columns report Krippendorff $\alpha$ for the highest-agreement two-rater dyad ($n$=2) and the full three-rater cohort on 55 overlapping pairs ($n$=3). Human–human agreement reported in text (47.1%) pools agreement across all annotator dyads on overlapping votes. The Llama–Qwen column reports LLM judge agreement between Llama 3.3 70B and Qwen 2.5 72B on the same 60 pairs. Per-annotator dyads are in Appendix J.

### 5.5 Theory-Grounded Feature Interpretability

To transcend zero-dimensional scalar leaderboards, HumorRank uses a layered psychometric model grounded in the General Theory of Verbal Humor (GTVH) (Attardo, 2017),



<!-- page 0008 -->

| Feature | GTVH Resource | Theoretical Description |
|---|---|---|
| *Incongruity* | Logical Mechanism (LM) | The foundational juxtaposition of conflicting scripts or ideas, forming the core of structural humor. |
| *Absurdity* | Situation (SI) | Extreme logical divergence from reality; scenarios that break fundamental physical or social expectations. |
| *Sarcasm* | Target (TA) / LM | Irony deployed with a specific target; relies on the contrast between stated and intended meaning. |
| *Wordplay* | Language (LA) | Surface-level phonetic or lexical ambiguity, including puns, double entendres, and syntactic misdirection. |
| *Conciseness* | Language (LA) / Delivery | The efficiency of the buildup before the punchline; minimizing superfluous tokens to maximize comedic timing. |

Table 4: Taxonomy of Humor Features extracted from model generations, grounded in the General Theory of Verbal Humor (GTVH).

detailed in Table 4. We isolate *Humor Mechanisms* (deep semantic incongruities), *Delivery Features* (surface psycholinguistic presentations), and *Failure Modes*.

Analysis of GTVH tags co-emitted in the same structured LLM judge response as each duel winner (not a separate tagging pass) delineates highly distinctive comedic signatures across three model archetypes:

- **The Frontier Generalist (e.g., GPT-5):** Relies heavily on pristine delivery, with *Conciseness* on 31.1% of wins (Figure 2, right) alongside *Incongruity* (26.5%; Figure 2, left). Its polished generations accumulate *Cliché* as a primary failure mode when losing.
- **The Absurdist Specialist (e.g., HumorGen-7B):** Leads the field on *Absurdity* (25.9%) and *Sarcasm* (9.2%) among winning tags (Figure 2, left), with higher *Escalation* (14.5%) than frontier models (Figure 2, right).
- **The Weak Baseline (e.g., Llama 70B):** Over-indexes on superficial *Wordplay* (29.5%; Figure 2, left) and accumulates *Weak Punchline* (41.1%) and *Cliché* (50.9%) among loser tags (Figure 3).

Per-model feature distributions adjudicated by the primary Llama judge are in Figure 2; Qwen-judge results are in Appendix I. Representative LLM judge rationales from match logs appear in Appendix F.



<!-- page 0009 -->

[Figure: Two heatmaps. Left: “Per-Model Winner Humor Mechanisms (%) — Llama 3.3 70B,” with model rows (GPT-5, Kimi-K2, Gemini-2.5-Pro, HumorGen-SFT-7B, Claude-3.5-Haiku, GPT-OSS-120B, Qwen3-32B, Llama-3.3-70B, Base-Qwen-7B) and feature columns (incongruity, wordplay, irony, surprise, absurdity, observational, narrative, sarcasm). Right: “Per-Model Delivery Features (%) — Llama 3.3 70B,” with the same model rows and feature columns (conciseness, punchline_positioning, framing_commentary, escalation, timing, deadpan).]

**Figure 2:** Per-model winning feature distributions (Llama judge). **Left:** Humor mechanisms (% of wins). **Right:** Delivery features (% of wins). Counts aggregate GTVH tags from the structured LLM judge response for each pairwise winner. Frontier models dominate via _Conciseness_; the specialist model leads on _Absurdity_ and _Escalation_; baseline models over-index on _Wordplay_.

[Figure: Heatmap titled “Per-Model Failure Modes (%) — Llama 3.3 70B,” with model rows (GPT-5, Kimi-K2, Gemini-2.5-Pro, HumorGen-SFT-7B, Claude-3.5-Haiku, GPT-OSS-120B, Qwen3-32B, Llama-3.3-70B, Base-Qwen-7B) and feature columns (cliche, weak_punchline, confusing, overexplained, buried_punchline, absurdity, wordplay).]

**Figure 3:** Per-model failure mode distributions (Llama judge). Loser tags are co-emitted with duel outcomes in the structured LLM judge response. _Cliché_ and _Weak Punchline_ dominate most models, but HumorGen-7B stands out with markedly higher _Overexplained_ and _Buried Punchline_ rates, a byproduct of its deep-structure comedic strategy. Qwen-judge failure modes are in Appendix I.

Complementing the winner profiles, Figure 3 shows failure-mode distributions when each model loses: _Cliché_ and _Weak Punchline_ dominate most models, while HumorGen-7B is distinct with higher _Overexplained_ (25.2%) and _Buried Punchline_ (20.4%) rates. Overall, this feature landscape confirms that scaling alone yields refined delivery, but specialized alignment is necessary for deep structural absurdity, a finding consistent across both LLM judges (Appendix I).

## 6 Conclusion

We presented HumorRank, a leaderboard-oriented framework for comparing LLM humor generation under conditioned prompts. The pipeline combines pairwise tournaments with Bradley–Terry MLE as the primary rating model and Stable Elo as a sequence-robust audit metric. Across SemEval-2026 MWAHAHA (300 prompts) Castro et al. (2026) and Humor Transfer Bench (400 prompts) (Ajayi & Mitra, 2026), we rank nine proprietary and open-weight models and observe cross-judge stability between Llama 3.3 70B and Qwen 2.5 72B



<!-- page 0010 -->

(Kendall $\tau = 0.889$ on both benchmarks). *HumorGen-7B* (Ajayi & Mitra, 2026), trained via CSF and SFT on Qwen-7B, remains competitive with substantially larger general-purpose systems. Feature-level analysis grounded in GTVH supports consistent qualitative differences in delivery and mechanism use across model tiers. Human annotations on 60 blind SemEval pairs provide directional agreement evidence for the LLM-as-a-Judge protocol (Appendix J). HumorRank is maintained at https://humorrank-leaderboard.pages.dev/.

## 7 Limitations

We note several limitations of the current study:

- **Monolingual Scope:** Evaluation is conducted on English data; cross-lingual and cross-cultural humor settings are not examined in this work.
- **Model Coverage:** Experiments are limited to nine models, which do not exhaust the full space of contemporary systems.
- **Dataset Scope:** Primary leaderboard tables report SemEval-2026 MWAHAHA in the main text; HTB Full RR leaderboards and HTB Swiss 2RR/3RR budget-mode statistics are reported in Appendix C (Tables 12, 15, and 7). Neither benchmark covers interactive or multimodal humor paradigms.
- **Judge Validity:** LLM judges inherit cultural and stylistic biases from pretraining; we screen rejected judge configurations exhibiting high self-preference (Appendix B). GTVH feature tags are co-produced with duel judgments but were not separately human-audited.

## 8 Reproducibility Statement

To ensure full reproducibility of the HumorRank framework, we detail the core hyperparameter configurations and computational hardware requirements necessary to execute the generative tournament.

**Generation Hyperparameters:** For all candidate models evaluated in the tournament, we standardized the generation settings to prioritize creative diversity while maintaining structural coherence. Specifically, we configured all candidate models with a unified sampling temperature of $T = 0.7$ and nucleus sampling of top-$p = 0.9$ (set explicitly wherever the provider API exposes it). Token limits were inherited from respective model APIs to preserve native instructional adherence without imposing artificial truncation.

**Judge Hyperparameters:** The LLM judges (Llama 3.3 70B and Qwen 2.5 72B) were configured with a highly constrained sampling temperature of $T = 0.1$ alongside a maximum retry threshold of 3 (with exponential backoff) for all pairwise JSON evaluation calls. Given the substantial financial and computational cost of the expansive generative tournament, this near-deterministic setting ensures that the LLM judges maintain stability and does not yield erratic or contradictory evaluations to the same prompt upon reassessment, thereby firmly preserving the integrity of the Bradley-Terry ratings.

**Computational Hardware:** Orchestrating full round-robin judging on SemEval and HTB (25,200 pairwise calls per LLM judge) required approximately 48 hours of dedicated NVIDIA H100 (80GB) GPU compute for the primary Llama judge pipeline. Qwen-judge replication required additional inference budget. Tournament code, evaluation scripts, and the Adaptive Swiss pairing implementation are provided in the supplementary materials.

## 9 Ethics Statement

This work proposes a framework for the systematic evaluation and ranking of humor generation across large language models; it does not itself constitute a humor generation system. Two ethical considerations warrant explicit acknowledgment. First, humor is a



<!-- page 0011 -->

culturally and contextually variable phenomenon whose boundaries with offensive or exclusionary expression are highly sensitive to audience and setting. Evaluation frameworks that rank models on comedic output implicitly surface content generated by those models, and practitioners adapting such pipelines for downstream applications bear responsibility for enforcing appropriate content-moderation constraints. Second, the validity of automated ranking is constrained by the cultural and stylistic distribution of the LLM judge model’s pretraining corpus. LLM-based evaluators trained predominantly on high-resource, Western-centric text may systematically disadvantage humor conventions from linguistically or culturally underrepresented communities, a limitation shared by the broader LLM-as-a-judge literature. HumorRank should therefore be interpreted as a reproducible diagnostic benchmark rather than a definitive assessment of comedic or creative quality.



<!-- page 0012 -->

## References

Sandhini Agarwal, Lama Ahmad, Jason Ai, Sam Altman, Andy Applebaum, Edwin Arbus, Rahul K Arora, Yu Bai, Bowen Baker, Haiming Bao, et al. gpt-oss-120b & gpt-oss-20b model card. *arXiv preprint arXiv:2508.10925*, 2025.

Edward Ajayi and Prasenjit Mitra. Automatic humor detection: A comprehensive survey from theoretical foundations to large language models. December 2025. doi: 10.13140/RG.2.2.24393.61288. URL https://doi.org/10.13140/RG.2.2.24393.61288. Preprint.

Edward Ajayi and Prasenjit Mitra. Humorgen: Cognitive synergy for humor generation in large language models via persona-based distillation. https://huggingface.co/Jayi2424/HumorGen-7B, 2026. Preprint.

Paul CH Albers and Han de Vries. Elo-rating as a tool in the sequential estimation of dominance strengths. *Animal behaviour*, pp. 489–495, 2001.

Anthropic. The claude 3 model family: Opus, sonnet, haiku. https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf, 2024. Model card.

Salvatore Attardo. The general theory of verbal humor. In *The Routledge handbook of language and humor*, pp. 126–142. Routledge, 2017.

Salvatore Attardo. *Linguistic theories of humor*, volume 1. Walter de Gruyter GmbH & Co KG, 2024.

Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjian Ge, et al. Qwen3-vl technical report. *arXiv preprint arXiv:2511.21631*, 2025.

Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. *Biometrika*, 39(3/4):324–345, 1952.

Santiago Castro, Luis Chiruzzo, Santiago Góngora, Salar Rahili, Naihao Deng, Ignacio Sastre, Victoria Amoroso, Guillermo Rey, Aiala Rosá, Guillermo Moncecchi, J. A. Meaney, Juan José Prada, and Rada Mihalcea. SemEval-2026 Task 1: MWAHAHA, Models Write Automatic Humor And Humans Annotate. In *Proceedings of the 20th International Workshop on Semantic Evaluation (SemEval-2026)*, 2026.

Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E Gonzalez, et al. Chatbot arena: An open platform for evaluating llms by human preference. In *Forty-first International Conference on Machine Learning*, 2024.

Gheorghe Comanici, Eric Bieber, Mike Schaeckermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. *arXiv preprint arXiv:2507.06261*, 2025.

Denis Federiakin. Improving llm leaderboards with psychometrical methodology. *arXiv preprint arXiv:2501.17200*, 2025.

Mayank Goel, Parameswari Krishnamurthy, and Radhika Mamidi. Automating humor: A novel approach to joke generation using template extraction and infilling. In *Proceedings of the 21st International Conference on Natural Language Processing (ICON)*, pp. 442–448, 2024.

Fabricio Goes, Zisen Zhou, Piotr Sawicki, Marek Grzes, and Daniel G Brown. Crowd score: A method for the evaluation of jokes using large language model ai voters as judges. *arXiv preprint arXiv:2212.11214*, 2022.

Drew Gorenz and Norbert Schwarz. How funny is chatgpt? a comparison of human-and ai-produced jokes. *Plos one*, 19(7):e0305364, 2024.



<!-- page 0013 -->

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.

Ruiqi He, Yushu He, Longju Bai, Jiarui Liu, Zhenjie Sun, Zhenghao Tang, He Wang, Hanchen Xia, Rada Mihalcea, and Naihao Deng. Chumor 2.0: Towards benchmarking chinese humor understanding. *arXiv preprint arXiv:2412.17729*, 2024.

Zachary Horvitz, Jingru Chen, Rahul Aditya, Harshvardhan Srivastava, Robert West, Zhou Yu, and Kathleen McKeown. Getting serious about humor: Crafting humor datasets with unfunny large language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*, pp. 855–869, 2024.

Nabil Hossain, John Krumm, Michael Gamon, and Henry Kautz. Semeval-2020 task 7: Assessing humor in edited news headlines. In *Proceedings of the fourteenth workshop on semantic evaluation*, pp. 746–758, 2020.

Veedant Jain, Felipe dos Santos Alves Feitosa, and Gabriel Kreiman. Is ai fun? humordb: a curated dataset and benchmark to investigate graphical humor. *arXiv preprint arXiv:2406.13564*, 2024.

Sean Kim and Lydia B Chilton. Ai humor generation: Cognitive, social and creative skills for effective humor. *arXiv preprint arXiv:2502.07981*, 2025.

Klaus Krippendorff. Computing krippendorff’s alpha-reliability. 2011.

Cristina Larkin-Galiñanes. An overview of humor theory. *The Routledge handbook of language and humor*, pp. 4–16, 2017.

Aidar Myrzakhan, Sondos Mahmoud Bsharat, and Zhiqiang Shen. Open-llm-leaderboard: From multi-choice to open-style questions for llms evaluation, benchmark, and arena. *arXiv preprint arXiv:2406.07545*, 2024.

Reuben Narad, Siddharth Suresh, Jiayi Chen, Pine SL Dysart-Bricken, Bob Mankoff, Robert Nowak, Jifan Zhang, and Lalit Jain. Which llms get the joke? probing non-stem reasoning abilities with humorbench. *arXiv preprint arXiv:2507.21476*, 2025.

Chanjun Park, Hyeonwoo Kim, Dahyun Kim, Seonghwan Cho, Sanghoon Kim, Sukyung Lee, Yungi Kim, and Hwalsuk Lee. Open ko-llm leaderboard: Evaluating large language models in korean with ko-h5 benchmark. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 3220–3234, 2024.

Kexin Quan, Pavithra Ramakrishnan, and Jessie Chin. Can ai take a joke—or make one? a study of humor generation and recognition in llms. In *Proceedings of the 2025 Conference on Creativity and Cognition*, pp. 431–437, 2025.

Sahithya Ravi, Patrick Huber, Akshat Shrivastava, Vered Shwartz, and Arash Einolghozati. Small but funny: A feedback-driven approach to humor distillation. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 13078–13090, 2024.

Adrianna Romanowski, Pedro HV Valois, and Kazuhiro Fukui. From punchlines to predictions: A metric to assess llm performance in identifying humor in stand-up comedy. In *Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics*, pp. 36–46, 2025.

Yuriel Ryan, Rui Yang Tan, Kenny Tsu Wei Choo, and Roy Ka-Wei Lee. Humor in pixels: Benchmarking large multimodal models understanding of online comics. *arXiv preprint arXiv:2509.12248*, 2025.

Mohammadamin Shafiei and Hamidreza Saffari. Not all jokes land: Evaluating large language models understanding of workplace humor. *arXiv preprint arXiv:2506.01819*, 2025.



<!-- page 0014 -->

João Silva, Luís Gomes, and António Branco. Clarin-pt-ldb: An open llm leaderboard for portuguese to assess language, culture and civility. *arXiv preprint arXiv:2603.12872*, 2026.

Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al. Openai gpt-5 system card. *arXiv preprint arXiv:2601.03267*, 2025.

Changhao Song, Yazhou Zhang, Hui Gao, Ben Yao, and Peng Zhang. Large language models for subjective language understanding: A survey. *arXiv preprint arXiv:2508.07959*, 2025.

Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, SH Cai, Yuan Cao, Y Charles, HS Che, Cheng Chen, Guanduo Chen, et al. Kimi k2. 5: Visual agentic intelligence. *arXiv preprint arXiv:2602.02276*, 2026.

Qwen Team. Qwen2.5: A party of foundation models, September 2024. URL https://qwenlm.github.io/blog/qwen2.5/.

Toloka Team. Understanding llm leaderboards: Metrics, benchmarks, and why they matter, November 2023. URL https://toloka.ai/blog/llm-leaderboard/. Accessed: 2026-03-23.

Thomas C Veatch. A theory of humor. 1998.

Han Wang, Yilin Zhao, Dian Li, Xiaohan Wang, Gang Liu, Xuguang Lan, and Hui Wang. Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps, April 2025. URL http://arxiv.org/abs/2410.10370. arXiv:2410.10370 [cs].

Thomas Winters and Stijn Van der Stockt. Evaluating humor generation in an improvisational comedy setting. *Computational Linguistics in the Netherlands Journal*, 14:505–523, 2025.

Shih-Hung Wu, Tsz-Yeung Lau, and Yu-Feng Huang. Humour classification according to genre and technique by fine-tuning llms. In *International Conference of the Cross-Language Evaluation Forum for European Languages*, pp. 156–169. Springer, 2025a.

Zhikun Wu, Thomas Weber, and Florian Müller. One does not simply meme alone: Evaluating co-creativity between llms and humans in the generation of humor. In *Proceedings of the 30th International Conference on Intelligent User Interfaces*, pp. 1082–1092, 2025b.

Hiroaki Yamane. Generic joke generation with moral constraints. In *International Conference on Artificial Neural Networks*, pp. 340–355. Springer, 2024.

Jifan Zhang, Lalit Jain, Yang Guo, Jiayi Chen, Kuan L Zhou, Siddharth Suresh, Andrew Wagenmaker, Scott Sievert, Timothy Rogers, Kevin Jamieson, et al. Humor in ai: Massive scale crowd-sourced preferences and benchmarks for cartoon captioning. *Advances in Neural Information Processing Systems*, 37:125264–125286, 2024.

Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. *Advances in neural information processing systems*, 36:46595–46623, 2023.

Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, and Pan Zhou. Let’s Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Creative Humor Generation. pp. 13246–13257, 2024. URL https://openaccess.thecvf.com/content/CVPR2024/html/Zhong_Lets_Think_Outside_the_Box_Exploring_Leap-of-Thought_in_Large_Language_CVPR_2024_paper.html.

Kuan Lok Zhou, Jiayi Chen, Siddharth Suresh, Reuben Narad, Timothy T Rogers, Lalit K Jain, Robert D Nowak, Bob Mankoff, and Jifan Zhang. Bridging the creativity understanding gap: Small-scale human alignment enables expert-level humor ranking in llms. *arXiv preprint arXiv:2502.20356*, 2025.



<!-- page 0015 -->

## Appendix: Table of Contents

**A Humor Definition** ........................................................................ 16  
**B Failure Modes of LLM-as-a-Judge on Humor Evaluation** ...................... 16  
**C Tournament Budget Ablation (Full RR / Swiss 2RR / Swiss 3RR)** ............. 20  
**D Adaptive Swiss Pairing Algorithm** ......................................... 31  
**E HumorRank Leaderboard Performance with Qwen 2.5 72B LLM Judge** ............ 31  
**F Llama Judge Sample Decisions** ............................................. 33  
**G Hyperparameter Configurations** ............................................ 36  
**H LLM-as-a-Judge Prompting Framework** ....................................... 37  
**I Qualitative Examples and Feature Reasoning** ............................... 38  
**J Human Evaluation Details** ................................................. 39  
**K Stable Elo Shuffle Audit** ................................................. 40



<!-- page 0016 -->

## A Humor Definition

Building upon classic Incongruity Theory, psychological frameworks (Larkin-Galiñanes, 2017), and Normative-Violation theory (Veatch, 1998), we require a rigorous working definition that can be applied to text-based evaluation. For the purposes of this research, we define humor explicitly as:

**Humor is the cognitive reward (experienced as amusement) arising when an interlocutor successfully resolves a deliberately constructed incongruity, such as the narrative shift between a joke’s setup and punchline, within a harmless and non-threatening context.**

This definition anchors psychological consensus into the practical reality of evaluating generated text. It explicitly requires four distinct components:

- **The Joke Mechanism (Setup & Punchline):** We evaluate humor not as random surprise, but as a structured linguistic narrative. The setup creates a logical expectation, and the punchline deliberately subverts it.
- **The “Cognitive Reward”:** This maps to the cognitive appraisal process, describing the computational or intellectual achievement of bridging the logical gap between the setup and punchline.
- **Experienced as Amusement:** The cognitive resolution must trigger a pleasant response (mirth) rather than confusion.
- **Harmless Context:** Drawn from benign violation theory, the structural incongruity only produces amusement if it is appraised as non-threatening.

Because humor exists on a continuous spectrum determined by these mechanisms rather than as a discrete label, our methodology utilizes *pairwise preference ranking*. By prompting the LLM judge to evaluate which generation produces a stronger cognitive reward, we effectively treat humor evaluation as a reward modeling paradigm across the multi-dimensional feature space of human amusement.

## B Failure Modes of LLM-as-a-Judge on Humor Evaluation

HumorRank’s evaluation protocol was not chosen a priori: it was the survivor of a deliberate search through LLM-as-a-Judge configurations that fail on humor generation ranking. We document two distinct failure classes: **(A) paradigm failure**, where numeric or absolute scoring collapses despite careful rubrics; and **(B) judge-model failure**, where pairwise structure is correct but the judge model exhibits self-preference or family bias. Section 3.1 in the main paper summarizes the conclusion; this appendix holds the full experimental program and evidence.

### B.1 Experimental program

We ran four tracks before locking the production tournament (Llama + Qwen72, structured pairwise judge prompt, 10,800 SemEval duels):

- **Track A: numeric judges (Exp. 1–4).** Absolute 0–100, structured 4×1–5 → 0–100, and scalar 1–20 paradigms over 1,000–1,200 headlines with ∼11–15 humor candidates each (∼41k scores total). Exp. 4 was a 120-headline Gemini absolute pilot (4 models/headline).
- **Track B: pairwise judge screening (9 SemEval models).** Same-prompt pairwise duels on the paper’s nine contestants using GPT-5, Gemini 2.5 Pro, GPT-OSS 120B, and Qwen3-32B as judges. GPT-5 and Gemini were evaluated on **five shared headlines** (en_2001–en_2005; 36 pairs/headline → 180 duels each); OSS and Qwen32 runs used ten headlines for additional coverage.



<!-- page 0017 -->

- **Track C: early pairwise prompt.** Verbose chain-of-thought pairwise pilot preceding the final structured prompt.
- **Production.** Screened open-weight judges (Llama 3.3 70B, Qwen 2.5 72B), structured pairwise prompt, position swap, full SemEval round-robin ($\tau = 0.889$).

Table 5 summarizes outcomes.

| Paradigm | Symptom | Response | n |
|---|---|---|---|
| Absolute 0–100 rubric | High-band clustering; mean within-HL spread 20.6 | Abandoned | 17k |
| Structured 4×1–5 → 0–100 | 88.5% scores = 70.0; 30.8% headlines all tie | Abandoned | 12k |
| Scalar 1–20 funniness | 82.7% in band 13–16; 22.2% spread ≤ 1 | Abandoned | 12k |
| Early pairwise prompt (verbose CoT) | ~62% tie rate in pilot | Revised prompt | pilot |
| GPT/Gemini judge (pairwise) | 75–88% self-win on shared pool | Rejected | 180–360 |
| **Structured pairwise + Llama/Qwen72** | Cross-judge $\tau$ = 0.889 | **Production** | 10,800 |

Table 5: LLM-as-a-Judge configurations tested on humor evaluation. Failed rows document *why* HumorRank does not use absolute scoring or proprietary self-preferring judges.

## B.2 Failure mode A: score anchoring (Experiments 1–3)

**Experiment 1: absolute 0–100 rubric.** An expert-style 0–100 funniness rubric with explicit bands (e.g., 85–100 “excellent”, 70–84 “good”) was applied by **Llama 3.3 70B Instruct** to ~11–15 joke candidates per headline across 1,200 headlines (17,317 individual scores). Scores clustered in a narrow high band despite diverse candidates; mean within-headline spread was only 20.6 points on a 0–100 scale, and rubric bands compressed most outputs into “good” rather than separating models. This is a *paradigm failure*: absolute scoring did not reliably discriminate humor quality among same-headline candidates, so it is unsuitable for leaderboard evaluation.

**Illustrative example (en_0004).** Table 6 provides one full headline-level sample. The same prompt receives only six score anchors (87/83/82/77/74/62), with verbose 161–163-word setups placed at the top band while tighter “weigh in”/scale punchlines are pushed to 62. The issue is not isolated ranking noise; the evaluation interface itself fails to separate which jokes land.

Table 6: **Exp. 1 Failure Case (en_0004).** Fifteen same-headline candidates scored by Llama 3.3 70B Instruct. **Metrics: Score** = Llama-assigned 0–100 rating; **Words** = word count. **Row Colors (score anchors):** gold/peach 87–83, lilac 82, blue 77–74, mint 62. **Error Markers:** coral (°) = verbose build rated too high; emerald (ʺ) = tight punchline rated too low. **Takeaway:** absolute scoring collapses distinct jokes onto six anchors and misjudges which responses land.

| Rk | Score | Words | Joke (full text) |
|---|---:|---:|---|
| 1 | 87 | 44 | You know, “Experts weigh in” on body wipes. I guess that means they literally stepped on them with their lab coats on to see if they’d break. Good thing the wipes held up, otherwise we’d have a whole bunch of scientists doing the splits. |

continued on next page…



<!-- page 0018 -->

*Table 6 — continued from previous page*

| Rk | Score | Words | Joke (full text) |
|---|---:|---:|---|
| $2^o$ | 87 | 161 | You know, body wipes... because sometimes you need a quick fix for that lingering funk, like when you’ve been sitting in traffic for three hours and your deodorant decided to take a vacation. And let me tell you, experts are super excited about this groundbreaking issue. They’re probably the same ‘experts’ who got their degree from the University of “I Can’t Shower Because I’m Too Important To Be Clean.” Listen, if these wipes really worked as well as advertised, we’d all just stop using showers altogether and the water crisis would be solved. We could rename them “body band-aids”—they don’t cure the smell, they just give you a little time before everyone starts backing away slowly. But hey, if you’re in a rush and can’t decide between a wipe and a shower, here’s a tip: If you think a wipe will cut it, you’re already too late. The cat’s out of the bag and it’s not the furry kind. |
| $3^o$ | 87 | 163 | So, do body wipes actually work? Let’s ask the experts! I heard they can tell you not only if you smell good enough to eat (which is totally a thing now, apparently), but also if you weigh more than your cat (and who wouldn’t want to know that?) Just imagine it—an expert body wipe panel sitting around discussing your cleanliness level with cups of tea and judging your body odor on a scale from ‘newly mown hay’ to ‘forgotten gym socks’. And if you fail their sniff test, fear not, because there’s always the option of becoming a human body wipe for the rest of the team—think of all the scrubbing you could do! The best part is, even if body wipes don’t work, at least we know the experts will be busy and not questioning life’s bigger mysteries like why the remote never works when you need it most. Now that’s a silver lining I can get behind! |
| 4 | 83 | 95 | Have you ever noticed how we have experts for everything now? Like, “Experts weigh in on whether body wipes work.” I mean, hello! If you’re wiping yourself with a wet cloth, odds are you’re not getting dirtier. It’s like having a panel of experts to discuss whether a hair dryer makes your hair dry. You know what? I’m calling it: if you’re using a body wipe, you are already an expert on body wipes. You don’t need some other guy telling you if it works or not. You’re the boss of your own smell situation! |
| $5^o$ | 83 | 154 | So I tried one of these wipes the other day, you know, just to test out the efficacy. I mean, I’m pretty sure it’s just a ploy to make me buy more deodorant. But what if the real secret is in the corners, like the little nooks where your bra straps dig in or behind your knees? I mean, who even thinks about those places? And now, every time I use a body wipe, I’m like, ‘Did it get the corner under my left armpit?’ And then I find myself spending the next 30 minutes just staring at that spot in the mirror, turning my arm around and around, going, ‘Did I miss it? Did I really miss it?!’ And I swear, if anyone catches me doing this, they’ll think I’m totally insane. But hey, I’d rather be the guy with the obsessive-compulsive corner-wiping routine than the guy who smells like old gym socks! |
| $6^u$ | 82 | 50 | You know, they say “experts weigh in” on whether body wipes actually work, but I’m pretty sure these so-called experts were using the heavy-duty kind—the ones that add pounds just from the packaging. At least now we know why the debate on body wipes has gotten so... weighty! |
| 7 | 82 | 111 | So, experts have finally weighed in on body wipes, and guess what folks? They kinda work, if your definition of “work” is smearing last week’s mystery stains into an even layer across your skin. You know you’re doing it wrong when you catch yourself using them after a particularly sweaty spin class, thinking, ‘This will do. I mean, who needs water and soap when you’ve got the magic of questionable chemical concoctions?’ But hey, at least we all feel a bit less guilty about not showering, right? Until the moment you accidentally sit down on something sticky and realize your body wipe game has failed you once again. Happy stinking, everybody! |
| $8^o$ | 82 | 118 | Experts have finally weighed in on body wipes, and guess what? They’re not just effective at cleaning; they might just be the answer to world hunger. You see, after using these wipes, people suddenly found themselves feeling lighter—about 20 pounds lighter! It turns out, the secret ingredient isn’t just magic cleaning solution, but a newfangled appetite suppressant. Who knew a swipe could be a diet plan? So next time you grab a body wipe, remember: it’s not just cleaning you up, it’s cutting down your weight. Just don’t try to eat them—unless you want to add a new layer of flavor to your meal that includes a hint of... let’s call it ‘sanitizing freshness.’ |

*continued on next page. . .*



<!-- page 0019 -->

*Table 6 — continued from previous page*

| Rk | Score | Words | Joke (full text) |
|---:|---:|---:|---|
| 9 | 77 | 97 | You know, I used one of those body wipes the other day, and it was so effective it almost started folding my clothes and putting them away. But honestly, the only thing it missed was cleaning under my nails. Which made me wonder, if it got between every crevice of my skin, why didn’t it pick up that one olive pit I’ve had lodged there since summer? It’s like it read the manual wrong and thought its job was to prepare me for a trip to the dry cleaners instead of just giving me a quick clean. |
| 10 | 77 | 119 | You know, I was at the gym the other day, and there was this guy who had this whole routine with his body wipes. He’d wipe down the machine before using it, then after every 10 minutes of exercise he stopped to wipe himself off. I asked him how it worked out for him, and he said, “Honestly, I just feel like I’m being used by a giant baby wipe.” I mean, if experts can’t agree on whether they even work, I think the only thing these wipes guarantee is that you’ll leave a trail of mystery scents wherever you go. Like, “Hey, what’s that smell? Oh, it’s probably Jerry from accounting and his endless supply of body wipes!” |
| 11 | 77 | 73 | You know, after using those fancy new body wipes, I’ve been feeling lighter on my feet. But don’t worry, it’s not that kind of weight loss—though if they really did work that way, I’d never run out of excuses to wipe down at the grocery store! After all, ‘I’m just trying these new body wipes; they said they might help me slim down!’ Who knew cleanliness could be so misleadingly slimming? |
| 12 | 74 | 75 | You know, I tried using a body wipe once. Didn’t work too well. So I asked my neighbor, “Hey, could I use your body as a wipe instead?” He looked at me funny, but then he said, “Sure, just don’t leave any lint.” Turns out, experts say body wipes aren’t very effective anyway, but they didn’t mention the potential for inter-body cleaning alternatives. Who knew we had a whole neighborhood of walking, talking cleaning supplies? |
| 13 | 74 | 143 | So, I was reading this article about how body wipes are great for, you know, cleaning yourself when you don’t have access to a shower. But I had to ask myself, do they really get everything? Like, do they work in all the places where you can barely reach with a washcloth? I started wondering, if I use one of these things, could I be leaving microscopic bits of wipe in areas that I’d rather keep as pristine as possible? I mean, is there an emergency service for extracting rogue wipe fibers from awkward spots? Because, based on my calculations, if you use a body wipe just once a day, by the end of the month, statistically speaking, you might have a small colony of these fibers living comfortably in your underbelly. It’s like inviting lint to come live rent-free in your navel! |
| 14“ | 62 | 90 | So, I asked these experts, “Hey, when you ‘weigh in’ on body wipes, do you stand on a scale with one in your hand?” And you know what? They didn’t laugh. They just said, “Well, we did consider the weight of the product, but not in the way you might think.” Because let’s face it, the last thing you want after a long day is to feel weighed down by a shower, right? Just grab a wipe, and voilà—no weight gain, no water waste, and no need for a scale! |
| 15“ | 62 | 113 | So, I was reading this article on body wipes and experts weighing in, and I thought to myself, “Experts, huh? Because obviously, the best person to consult when you’ve run out of shower gel is a... body wipe expert!” And you know what? If these body wipes don’t get your back as clean as a whistle, at least you can say you had a nice conversation with a cloth. After all, you never know when a friendly wipe might become your new best friend. They won’t judge you for the gunk you picked up at the gym, but hey, they might introduce you to their lintly cousin who could use some love too! |

**Experiment 2: structured** 4 × 1–5 dimensions. Hypothesis: decomposing humor into incongruity, resolution, linguistic, and punchline dimensions would force discrimination. Over 1,000 headlines (∼12k scores), the judge repeated nearly identical dimension patterns (e.g., 4/4/3/4) on most jokes, producing a weighted total of **70.0 on 88.5% of all scores**. On 30.8% of headlines, *every* candidate received the identical score, a complete ranking failure.

**Experiment 3: scalar 1–20 funniness.** Hypothesis: a smaller scale with a “seasoned comedy judge” persona would reduce anchoring. Result: **82.7%** of scores fell in a four-point band (13–16); 22.2% of headlines had within-headline spread ≤ 1 point. Reducing scale width did not fix the problem.

These failures are *paradigm-level*: the judge assigns similar numbers to different jokes on the same headline when every candidate is already a humor attempt, the setting SemEval



<!-- page 0020 -->

MWAHAHA uses. Absolute interfaces cannot produce a cross-model leaderboard here regardless of rubric quality.

### B.3 Failure mode B: judge-model self-preference (5-headline pilot)

Pairwise comparison removes score anchoring but introduces a second failure mode: **the judge model favors its own family.** On five shared SemEval headlines (`en_2001–en_2005`), we ran full round-robin pairwise tournaments (36 pairs/headline) with GPT-5 and Gemini 2.5 Pro serving as judges over the same nine contestants used in the paper.

When a judge faced its own model’s output, self-win rates reached **87.5%** (GPT-5 as judge, GPT-5 as contestant) and **87.5%** (Gemini), with both judges ranking themselves #1 overall. GPT-OSS-as-judge showed ~75% self-win; Qwen3-32B-as-judge ranked itself #4 at ~57.5% self-win. The four rejected judges agreed on the same winner in only ~44% of shared duels (79/180); no stable cross-judge humor ordering emerged. These runs motivated screening out proprietary and same-family judges; production evaluation uses Llama 3.3 70B and Qwen 2.5 72B, which showed more coherent humor judgments in this setup and no strong same-family self-preference (under full SemEval coverage, the Llama judge ranks Llama 3.3 70B at #8, while the Qwen 2.5 72B judge does not elevate Qwen-family contestants: Qwen 3 32B is #7 and Base Qwen 7B is #9; Tables 1 and 18).

### B.4 Failure mode C: spurious ties (early pairwise prompt)

An early pairwise prompt encouraging extended chain-of-thought reasoning produced a **~62% tie rate**, as the judge defaulted to “equal” rather than committing to a preference. Subsequent prompt revisions tightened instructions (“trust your first impression”, TIE only when genuinely equal) and enforced structured JSON outputs, reducing spurious ties while retaining GTVH feature tags (Appendix H).

### B.5 Illustrative failure pairs (qualitative audit)

Table 6 (Failure mode A) gives a full headline-level example; additional Track B and V1 pilot duels remain available for manual curation (paths below). Aggregate statistics above establish that failed configurations are unusable for leaderboard construction; qualitative inspection confirms *why*.

### B.6 Production configuration (what survived)

The production HumorRank judge stack combines four properties absent in failed configurations:

1. **Relative, not absolute.** Each judgment is a preference between two jokes on the *same headline* under the structured pairwise prompt.

2. **Theory-grounded structure.** GTVH mechanism and delivery tags make preferences auditable.

3. **Bias mitigation.** Position swapping, $T = 0.1$, and rejection of self-preferring proprietary judges (Failure mode B).

4. **Cross-judge validation.** Llama 3.3 70B + Qwen 2.5 72B yield Kendall $\tau = 0.889$ on full round-robin for both SemEval and HTB (25,200 pooled duels).

## C Tournament Budget Ablation

We evaluate Swiss 2RR and Swiss 3RR schedules with the same Adaptive Swiss Pairing code and budget definitions used in the main pipeline. Tables and figures below are grouped by benchmark (SemEval, then HTB) and, within each benchmark, by budget mode (Full RR, Swiss 3RR, Swiss 2RR). All Swiss budget tables use the Llama judge labels unless noted; HTB Qwen judge Swiss tables appear in §C.6.



<!-- page 0021 -->

### C.1 Cross-judge $\tau$ by budget mode

| Comparison | Full RR | Swiss 2RR | Swiss 3RR |
|---|---:|---:|---:|
| SemEval: Llama vs Qwen | 0.889 | 0.667 | **0.889** |
| HTB: Llama vs Qwen | 0.889 | 1.000 | 0.889 |
| SemEval vs HTB (Llama) | 0.889 | 0.778 | 0.778 |
| SemEval vs HTB (Qwen) | 0.889 | 0.778 | 0.889 |
| **Average** | **0.889** | 0.806 | **0.861** |

Table 7: Kendall $\tau$ across budget modes (four cross-judge / cross-benchmark cells). Swiss 3RR restores SemEval Llama↔Qwen agreement to Full RR levels.

### C.2 Swiss 3RR rank stability (SemEval, Llama judge)

| Model | Rank (Full RR / Swiss 3RR / Swiss 2RR) |
|---|---:|
| GPT-5 | 1 / 1 / 1 |
| Kimi K2 | 2 / 2 / 4 |
| Gemini 2.5 Pro | 3 / 3 / 2 |
| HumorGen-7B | 4 / 5 / 6 |
| Claude 3.5 Haiku | 5 / 7 / 5 |
| GPT OSS 120B | 6 / 4 / 3 |
| Qwen 3 32B | 7 / 6 / 7 |
| Llama 3.3 70B | 8 / 8 / 8 |
| Base Qwen 7B | 9 / 9 / 9 |

Table 8: SemEval Llama judge ranks under Full RR, Swiss 3RR, and Swiss 2RR. Ranks #1 (GPT-5), #8 (Llama 3.3 70B), and #9 (Base Qwen 7B) are invariant across all three schedules; mid-tier models reorder most under Swiss 2RR.

### C.3 Swiss 3RR rank stability (HTB, Llama judge)

| Model | Rank (Full RR / Swiss 3RR / Swiss 2RR) |
|---|---:|
| GPT-5 | 1 / 1 / 1 |
| Kimi K2 | 2 / 2 / 2 |
| HumorGen-7B | 3 / 3 / 6 |
| Claude 3.5 Haiku | 4 / 6 / 4 |
| Gemini 2.5 Pro | 5 / 5 / 5 |
| GPT OSS 120B | 6 / 4 / 3 |
| Qwen 3 32B | 7 / 7 / 7 |
| Llama 3.3 70B | 8 / 8 / 8 |
| Base Qwen 7B | 9 / 9 / 9 |

Table 9: HTB Llama judge ranks under Full RR, Swiss 3RR, and Swiss 2RR. Ranks #1 (GPT-5), #8 (Llama 3.3 70B), and #9 (Base Qwen 7B) are invariant; HumorGen-7B drops from #3 to #6 under Swiss 2RR.

### C.4 SemEval budget ablation (Llama judge)

SemEval uses 300 prompts and $K=9$ contestants. Full RR runs 36 pairs per prompt (10,800 judgments); Swiss 3RR and Swiss 2RR subsample to 12 and 8 pairs per prompt (3,600 and 2,400 judgments). Table 8 summarizes rank stability across modes on this benchmark.

**Full RR (100% budget).** The primary SemEval leaderboard is Table 1 (main text). Figure 4 visualizes the same Full RR run: GPT-5 and Kimi K2 lead the field; HumorGen-7B ranks 4th; Llama 3.3 70B and Base Qwen 7B anchor the bottom tier.



<!-- page 0022 -->

[Figure: Two-panel plot. Top: horizontal bar chart titled “HumorRank Leaderboard on SemEval MWAHAHA (Llama Judge)” with Bradley–Terry ratings for models including GPT-5, Kimi K2, Gemini 2.5 Pro, HumorGen-7B, Claude Haiku 3.5, GPT-OSS 120B, Qwen3-32B, Llama 3.3 70B, and Qwen-7B. Bottom: heatmap titled “Pairwise Win Rate on SemEval MWAHAHA (Llama Judge)” showing row model vs opponent model win rates with a color scale labeled “Win Rate (%)”.]

**Figure 4: SemEval, Full RR, Llama judge** (Table 1). **Top:** Bradley–Terry leaderboard with 95% confidence intervals (10,800 judgments). **Bottom:** Pairwise win-rate heatmap. *Observation:* clear frontier/mid/baseline separation; cross-judge agreement with Qwen Full RR is Kendall $\tau$ = 0.889.

**Swiss 3RR (~33% budget).** At 12 pairs/prompt, Swiss 3RR preserves the Full RR ordering at the top and bottom: GPT-5 remains #1; Llama 3.3 70B and Base Qwen 7B remain #8 and #9. HumorGen-7B shifts one rank (4→5) while mid-tier models show modest reordering. Kendall $\tau$ vs. SemEval Full RR is 0.889, and SemEval Llama↔Qwen cross-judge $\tau$ matches Full RR (0.889; Table 7).

**Swiss 2RR (~22% budget).** At 8 pairs/prompt, anchor ranks #1, #8, and #9 remain stable, but mid-tier ordering becomes noisier (e.g., Kimi K2 2→4, Gemini 2.5 Pro 3→2, HumorGen-7B 4→6). SemEval Llama↔Qwen cross-judge $\tau$ drops to 0.667 (Table 7), so we treat Swiss 2RR as a minimum-budget stress test rather than the recommended scaling mode.



<!-- page 0023 -->

[Figure: Two-panel chart. Top: horizontal bar chart titled “SemEval MWAHAHA — Swiss 3R Simulated (Llama Judge)” with Bradley–Terry ratings: GPT-5 1268.7; Kimi K2 1133.2; Gemini 2.5 Pro 1126.4; GPT-OSS 120B 1077.2; HumorGen-7B 1042.0; Qwen3-32B 990.7; Claude Haiku 3.5 988.5; Llama 3.3 70B 789.6; Qwen-7B 583.7. Bottom: heatmap titled “SemEval MWAHAHA Swiss 3R Sim — Pairwise Win Rate (Llama Judge)” with axes “Row model” and “Opponent model,” colorbar labeled “Win Rate (%)” from 0 to 100, and model labels GPT-5, Kimi K2, Gemini 2.5 Pro, GPT-OSS 120B, HumorGen-7B, Qwen3-32B, Claude Haiku 3.5, Llama 3.3 70B, Qwen-7B.]

**Figure 5: SemEval, Swiss 3RR, Llama judge** (Table 10). **Top:** BT leaderboard from 3,600 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* Swiss 3RR at one-third of Full RR comparisons recovers the same cross-judge rank correlation ($\tau = 0.889$) and keeps anchor ranks #1/#8/#9 fixed.

### C.5 HTB budget ablation (Llama judge)

HTB uses 400 held-out headline prompts with the same nine-model pool. Full RR requires 14,400 judgments per LLM judge; Swiss 3RR and 2RR use 4,800 and 3,200 judgments, respectively. Table 9 summarizes rank stability across budget modes on this benchmark.

**Full RR (100% budget).** On HTB Full RR, GPT-5 and Kimi K2 remain in the top two positions; HumorGen-7B ranks 3rd under the Llama judge; Llama 3.3 70B and Base Qwen 7B remain 8th and 9th. Cross-judge agreement with Qwen Full RR is Kendall $\tau = 0.889$ (Table 7).

**Swiss 3RR ($\sim$33% budget).** Swiss 3RR on HTB preserves ranks #1, #8, and #9 and keeps HumorGen-7B at rank #3. HTB Llama↔Qwen cross-judge $\tau$ remains 0.889 (Table 7).



<!-- page 0024 -->

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1268.7 | 1253.2 | [1243.0,1302.7] | 76.7% |
| 2 | Kimi-K2 | 1133.2 | 1132.7 | [1110.8,1160.9] | 63.9% |
| 3 | Gemini 2.5 Pro | 1126.4 | 1108.6 | [1105.0,1151.3] | 52.8% |
| 4 | GPT OSS 120B | 1077.3 | 1086.3 | [1048.5,1106.8] | 49.3% |
| 5 | **HumorGen-7B** | **1042.0** | **1058.5** | **[1012.9,1070.7]** | **64.1%** |
| 6 | Qwen 3 32B | 990.7 | 997.8 | [965.5,1021.9] | 35.2% |
| 7 | Claude 3.5 Haiku | 988.5 | 987.4 | [962.1,1014.6] | 47.9% |
| 8 | Llama 3.3 70B | 789.7 | 795.2 | [758.1,818.1] | 35.1% |
| 9 | Base Qwen 7B | 583.7 | 580.3 | [537.6,620.0] | 12.4% |

Table 10: **SemEval, Swiss 3RR, Llama judge.** Rank $\tau$ vs. Full RR = 0.889; cross-judge $\tau$ (Llama vs. Qwen on SemEval) = 0.889. Anchor ranks #1, #8, #9 unchanged from Table 8.

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1358.4 | 1307.9 | [1304.3,1423.6] | 79.3% |
| 2 | Gemini 2.5 Pro | 1190.1 | 1103.0 | [1135.1,1246.6] | 45.3% |
| 3 | GPT OSS 120B | 1122.0 | 1037.6 | [1056.8,1207.7] | 35.7% |
| 4 | Kimi-K2 | 1044.1 | 1117.4 | [985.3,1111.5] | 68.8% |
| 5 | Claude 3.5 Haiku | 1040.5 | 1028.4 | [993.9,1085.8] | 55.3% |
| 6 | **HumorGen-7B** | **950.0** | **1000.7** | **[898.4,1008.2]** | **66.5%** |
| 7 | Qwen 3 32B | 884.9 | 960.9 | [816.5,957.6] | 31.8% |
| 8 | Llama 3.3 70B | 830.7 | 841.7 | [790.4,861.7] | 42.3% |
| 9 | Base Qwen 7B | 579.4 | 602.4 | [529.9,631.3] | 13.2% |

Table 11: **SemEval, Swiss 2RR, Llama judge.** Cross-judge Llama↔Qwen $\tau$ = 0.667; ranks #1,#8, and #9 remain stable (Table 8).

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1314.7 | 1300.4 | [1301.3,1329.0] | 84.1% |
| 2 | Kimi K2 | 1242.0 | 1239.1 | [1229.5,1255.6] | 77.2% |
| 3 | **HumorGen-7B** | **1097.7** | **1122.8** | **[1084.4,1109.9]** | **60.6%** |
| 4 | Claude 3.5 Haiku | 1054.2 | 1058.3 | [1043.2,1068.5] | 55.1% |
| 5 | Gemini 2.5 Pro | 1024.0 | 1009.0 | [1010.6,1038.2] | 51.3% |
| 6 | GPT OSS 120B | 1009.6 | 1017.2 | [998.4,1021.6] | 49.5% |
| 7 | Qwen 3 32B | 942.5 | 946.2 | [928.1,955.7] | 41.3% |
| 8 | Llama 3.3 70B | 791.9 | 795.4 | [776.4,808.0] | 24.9% |
| 9 | Base Qwen 7B | 523.5 | 511.8 | [501.8,549.8] | 5.9% |

Table 12: **HTB, Full RR, Llama judge** (14,400 judgments). *Observation:* ordering mirrors SemEval at the extremes (GPT-5 #1; Llama/Base Qwen #8/#9); HumorGen-7B ranks 3rd on this held-out benchmark.

**Swiss 2RR (~22% budget).** At minimum budget, HTB anchor ranks #1, #8, and #9 remain fixed, but HumorGen-7B drops from #3 to #6 and mid-tier models reorder. Notably, HTB Llama↔Qwen $\tau$ rises to 1.000 at 2RR (Table 7), a benchmark-specific effect we attribute to reduced comparison density rather than improved ranking fidelity.

### C.6 HTB budget ablation (Qwen judge)

We replicate the HTB Full RR and Swiss budget modes under the Qwen judge to confirm cross-LLM-judge patterns on the held-out benchmark.

**Full RR (100% budget).** Qwen judge HTB Full RR agrees with Llama judge HTB at Kendall $\tau$ = 0.889; GPT-5 and Kimi K2 remain top-two, with HumorGen-7B 4th (vs. 3rd under the Llama judge).

**Swiss 3RR (~33% budget).**



<!-- page 0025 -->

[Figure: Two-panel figure. Top: horizontal bar chart titled “SemEval MWAHAHA — Swiss 2R Simulated (Llama Judge)” with Bradley–Terry ratings: GPT-5 1358.4, Gemini 2.5 Pro 1190.1, GPT-OSS 120B 1122.0, Kimi K2 1044.1, Claude Haiku 3.5 1040.5, HumorGen-7B 950.0, Qwen3-32B 884.9, Llama 3.3 70B 830.7, Qwen-7B 579.4. Bottom: pairwise win-rate heatmap titled “SemEval MWAHAHA Swiss 2R Sim — Pairwise Win Rate (Llama Judge)” with colorbar labeled “Win Rate (%)”, axes “Row model” and “Opponent model”.]

**Figure 6: SemEval, Swiss 2RR, Llama judge** (Table 11). **Top:** BT leaderboard from 2,400 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* lowest-budget mode preserves top/bottom anchors but increases mid-tier rank volatility and reduces cross-judge agreement ($\tau$ = 0.667).

**Swiss 2RR (~22% budget).**



<!-- page 0026 -->

[Figure: Two-panel figure. Top: horizontal bar chart titled “HTB — Swiss 3R Simulated (Llama Judge)” with x-axis “Bradley–Terry rating”; models and values: GPT-5 1259.2, Kimi K2 1210.5, HumorGen-7B 1067.9, GPT-OSS 120B 1058.2, Gemini 2.5 Pro 1037.7, Claude Haiku 3.5 1013.6, Qwen3-32B 993.9, Llama 3.3 70B 802.5, Qwen-7B 556.5. Bottom: heatmap titled “HTB Swiss 3R Sim — Pairwise Win Rate (Llama Judge)” with axes “Row model” and “Opponent model,” colorbar labeled “Win Rate (%)”; model labels include GPT-5, Kimi K2, HumorGen-7B, GPT-OSS 120B, Gemini 2.5 Pro, Claude Haiku 3.5, Qwen3-32B, Llama 3.3 70B, Qwen-7B.]

**Figure 7: HTB, Swiss 3RR, Llama judge** (Table 13). **Top:** BT leaderboard from 4,800 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* one-third budget retains HTB anchor ranks and cross-judge stability ($\tau = 0.889$).

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1259.2 | 1246.7 | [1236.8,1282.7] | 76.7% |
| 2 | Kimi K2 | 1210.5 | 1204.0 | [1188.5,1236.0] | 71.4% |
| 3 | **HumorGen-7B** | **1067.9** | **1055.4** | **[1040.1,1094.1]** | **63.9%** |
| 4 | GPT OSS 120B | 1058.2 | 1062.8 | [1032.3,1088.9] | 50.9% |
| 5 | Gemini 2.5 Pro | 1037.7 | 1056.0 | [1018.5,1061.0] | 42.2% |
| 6 | Claude 3.5 Haiku | 1013.6 | 1025.1 | [986.8,1036.6] | 51.6% |
| 7 | Qwen 3 32B | 993.9 | 988.3 | [971.5,1020.2] | 32.5% |
| 8 | Llama 3.3 70B | 802.5 | 789.4 | [778.3,827.1] | 35.7% |
| 9 | Base Qwen 7B | 556.5 | 572.4 | [507.5,595.1] | 10.4% |

**Table 13: HTB, Swiss 3RR, Llama judge.** Ranks #1, #3 (HumorGen-7B), #8, and #9 match Full RR anchors; cross-judge HTB $\tau = 0.889$.



<!-- page 0027 -->

[Figure: Two-panel figure. Top is a horizontal bar chart titled “HTB — Swiss 2R Simulated (Llama Judge)” with x-axis “Bradley-Terry rating” and bars: GPT-5 1326.5; Kimi K2 1145.7; GPT-OSS 120B 1097.1; Claude Haiku 3.5 1087.9; Gemini 2.5 Pro 1078.1; HumorGen-7B 991.0; Qwen3-32B 884.3; Llama 3.3 70B 847.7; Qwen-7B 541.8. Bottom is a heatmap titled “HTB Swiss 2R Sim — Pairwise Win Rate (Llama Judge)” with axes “Row model” and “Opponent model,” color bar “Win Rate (%)” from 0 to 100, and model labels GPT-5, Kimi K2, GPT-OSS 120B, Claude Haiku 3.5, Gemini 2.5 Pro, HumorGen-7B, Qwen3-32B, Llama 3.3 70B, Qwen-7B.]

**Figure 8: HTB, Swiss 2RR, Llama judge** (Table 14). **Top:** BT leaderboard from 3,200 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* anchor ranks hold, but specialist mid-tier placement becomes less stable (HumorGen-7B 3→6).

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1326.5 | 1303.3 | [1274.5, 1386.9] | 81.4% |
| 2 | Kimi K2 | 1145.7 | 1180.1 | [1077.0, 1208.1] | 77.3% |
| 3 | GPT OSS 120B | 1097.1 | 1043.6 | [1032.3, 1163.1] | 47.5% |
| 4 | Claude 3.5 Haiku | 1087.9 | 1072.2 | [1046.1, 1137.9] | 59.5% |
| 5 | Gemini 2.5 Pro | 1078.1 | 1051.7 | [1024.0, 1138.7] | 33.8% |
| 6 | **HumorGen-7B** | **991.0** | **1025.6** | **[936.6, 1052.7]** | **64.4%** |
| 7 | Qwen 3 32B | 884.3 | 941.2 | [807.2, 962.0] | 20.7% |
| 8 | Llama 3.3 70B | 847.7 | 829.9 | [813.1, 888.8] | 44.1% |
| 9 | Base Qwen 7B | 541.8 | 552.5 | [490.5, 583.7] | 9.6% |

Table 14: **HTB, Swiss 2RR, Llama judge.** Anchor ranks #1/#8/#9 stable; HumorGen-7B drops 3→6 vs. Full RR. Cross-judge HTB $\tau = 1.000$ at this budget (Table 7).



<!-- page 0028 -->

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1245.7 | 1278.6 | [1234.5, 1258.7] | 78.8% |
| 2 | Kimi K2 | 1199.5 | 1205.3 | [1187.2, 1211.7] | 73.8% |
| 3 | Claude 3.5 Haiku | 1101.4 | 1094.1 | [1089.4, 1114.0] | 61.8% |
| 4 | **HumorGen-7B** | **1099.8** | **1099.2** | **[1086.1, 1115.0]** | **61.6%** |
| 5 | GPT OSS 120B | 1024.3 | 1015.9 | [1013.4, 1037.9] | 51.7% |
| 6 | Gemini 2.5 Pro | 1001.3 | 990.4 | [989.4, 1013.7] | 48.8% |
| 7 | Qwen 3 32B | 951.4 | 951.5 | [941.2, 964.7] | 42.4% |
| 8 | Llama 3.3 70B | 757.7 | 746.2 | [743.1, 773.5] | 21.1% |
| 9 | Base Qwen 7B | 618.9 | 618.7 | [601.0, 634.4] | 10.1% |

Table 15: **HTB, Full RR, Qwen judge** (14,400 judgments). *Observation:* cross-judge HTB $\tau = 0.889$ vs. Table 12; bottom-two ranks unchanged.

[Figure: Two-panel figure. Top: horizontal bar chart titled “HTB — Swiss 3R Simulated (Qwen Judge)” with x-axis “Bradley-Terry rating”; bars labeled GPT-5 1204.0, Kimi K2 1178.6, GPT-OSS 120B 1071.1, HumorGen-7B 1071.1, Claude Haiku 3.5 1052.0, Gemini 2.5 Pro 993.9, Qwen3-32B 986.1, Llama 3.3 70B 774.4, Qwen-7B 668.9. Bottom: heatmap titled “HTB Swiss 3R Sim — Pairwise Win Rate (Qwen Judge)” with axes “Row model” and “Opponent model,” colorbar “Win Rate (%)”, and model labels GPT-5, Kimi K2, GPT-OSS 120B, HumorGen-7B, Claude Haiku 3.5, Gemini 2.5 Pro, Qwen3-32B, Llama 3.3 70B, Qwen-7B.]

Figure 9: **HTB, Swiss 3RR, Qwen judge** (Table 16). **Top:** BT leaderboard from 4,800 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* GPT-5/Kimi remain top-two; Llama/Base Qwen stay #8/#9; HumorGen-7B remains top-tier (#4).



<!-- page 0029 -->

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1204.0 | 1207.1 | [1182.2,1228.7] | 72.1% |
| 2 | Kimi K2 | 1178.6 | 1182.5 | [1158.3,1199.0] | 69.9% |
| 3 | GPT OSS 120B | 1071.1 | 1064.0 | [1045.8,1100.2] | 55.1% |
| 4 | **HumorGen-7B** | **1071.1** | **1081.3** | **[1043.8,1098.1]** | **64.4%** |
| 5 | Claude 3.5 Haiku | 1052.0 | 1053.2 | [1034.1,1078.3] | 57.6% |
| 6 | Gemini 2.5 Pro | 993.9 | 1004.3 | [975.0,1016.3] | 37.4% |
| 7 | Qwen 3 32B | 986.1 | 984.4 | [962.4,1008.9] | 34.7% |
| 8 | Llama 3.3 70B | 774.4 | 760.6 | [749.1,797.7] | 30.8% |
| 9 | Base Qwen 7B | 668.9 | 662.6 | [634.9,699.7] | 18.5% |

Table 16: **HTB, Swiss 3RR, Qwen judge.** Cross-judge HTB $\tau$ = 0.889; anchor ranks #1/#8/#9 stable vs. Qwen Full RR.

[Figure: Two-panel chart. Top: horizontal bar chart titled “HTB — Swiss 2R Simulated (Qwen Judge)” with Bradley-Terry rating axis and models/values: GPT-5 1262.7, Kimi K2 1140.0, GPT-OSS 120B 1137.5, Claude Haiku 3.5 1075.7, Gemini 2.5 Pro 1055.1, HumorGen-7B 1023.2, Qwen3-32B 912.0, Llama 3.3 70B 763.0, Qwen-7B 630.7. Bottom: heatmap titled “HTB Swiss 2R Sim — Pairwise Win Rate (Qwen Judge)” with row model and opponent model labels GPT-5, Kimi K2, GPT-OSS 120B, Claude Haiku 3.5, Gemini 2.5 Pro, HumorGen-7B, Qwen3-32B, Llama 3.3 70B, Qwen-7B; colorbar “Win Rate (%)” from 0 to 100; visible cell values include 61.2, 72.9, 78.8, 98.0, 62.9, 81.0, 100.0, 38.8, 60.0, 27.1, 49.4, 80.0, 86.2, 84.0, 21.2, 40.0, 50.6, 83.3, 37.1, 20.0, 54.3, 34.8, 93.0, 19.0, 45.7, 100.0, 2.0, 13.8, 16.7, 65.2, 65.8, 0.0, 16.0, 7.0, 0.0, 34.2.]

**Figure 10: HTB, Swiss 2RR, Qwen judge** (Table 17). **Top:** BT leaderboard from 3,200 judged pairs. **Bottom:** Win-rate heatmap. *Observation:* minimum-budget HTB run preserves top/bottom anchors but increases mid-tier volatility, consistent with the Llama judge Swiss 2RR pattern.



<!-- page 0030 -->

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1262.7 | 1239.4 | [1221.6, 1315.4] | 76.1% |
| 2 | Kimi K2 | 1140.0 | 1166.5 | [1077.3, 1196.3] | 74.0% |
| 3 | GPT OSS 120B | 1137.6 | 1098.8 | [1092.1, 1196.4] | 55.5% |
| 4 | Claude 3.5 Haiku | 1075.7 | 1057.5 | [1035.0, 1113.9] | 62.7% |
| 5 | Gemini 2.5 Pro | 1055.1 | 1045.2 | [1016.5, 1106.4] | 32.0% |
| 6 | **HumorGen-7B** | **1023.2** | **1057.8** | **[972.7, 1061.8]** | **66.4%** |
| 7 | Qwen 3 32B | 912.0 | 948.1 | [850.6, 959.9] | 23.9% |
| 8 | Llama 3.3 70B | 763.0 | 746.8 | [731.4, 797.7] | 35.5% |
| 9 | Base Qwen 7B | 630.7 | 639.9 | [587.0, 668.7] | 18.2% |

Table 17: **HTB, Swiss 2RR, Qwen judge.** Anchor ranks #1/#8/#9 stable; HumorGen-7B 4→6 vs. Qwen Full RR. Cross-judge HTB $\tau$ = 1.000 (Table 7).



<!-- page 0031 -->

## D Adaptive Swiss Pairing Algorithm

Algorithm 1 specifies pair scheduling only; final leaderboard ratings are computed separately using global Bradley–Terry MLE on the collected match graph. In line with the main-text definition of *under-sampled* pairs, the coverage count in line 901 is the observed duel count for $(i, j)$ in $G$; ASP prefers partners with the lowest count among near-equal-strength candidates.

**Algorithm 1** Adaptive Swiss Pairing for Tournament Evaluation

**Require:** Set of models $\mathcal{M}$, prompt set $\mathcal{H}$, max comparisons $C_{max}$, temporary pairing scores $S$

1: Initialize match-history multigraph $G$ with per-prompt pair counts $c_{ijh} \leftarrow 0$  
2: **while** total recorded matches in $G$ < $C_{max}$ **do**  
3: &nbsp;&nbsp;&nbsp;&nbsp;Sort $\mathcal{M}$ descending by temporary pairing scores $S$  
4: &nbsp;&nbsp;&nbsp;&nbsp;Initialize unmatched subset $U \leftarrow \mathcal{M}$  
5: &nbsp;&nbsp;&nbsp;&nbsp;Initialize round pairings $Q \leftarrow \emptyset$  
6: &nbsp;&nbsp;&nbsp;&nbsp;**while** $|U| \geq 2$ **do**  
7: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$i \leftarrow$ highest-rated model in $U$  
8: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find $j \in U \setminus \{i\}$ minimizing $|S_i - S_j|$ with lowest coverage count in $G$  
9: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**if** valid match $j$ exists **then**  
10: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$Q \leftarrow Q \cup \{(i, j)\}$  
11: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$U \leftarrow U \setminus \{i, j\}$  
12: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**else**  
13: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$j \leftarrow$ least-played feasible partner in $U \setminus \{i\}$  ▷ progress fallback  
14: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$Q \leftarrow Q \cup \{(i, j)\}$  
15: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$U \leftarrow U \setminus \{i, j\}$  
16: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**end if**  
17: &nbsp;&nbsp;&nbsp;&nbsp;**end while**  
18: &nbsp;&nbsp;&nbsp;&nbsp;Execute LLM-as-a-judge evaluations for all pairs in $Q$ on selected prompts  
19: &nbsp;&nbsp;&nbsp;&nbsp;Increment corresponding per-prompt counts in $G$  
20: &nbsp;&nbsp;&nbsp;&nbsp;Update temporary pairing scores $S$ using observed outcomes  
21: **end while**  
22: **return** Global match history graph $G$  ▷ final ratings computed later via BT MLE

## E HumorRank Leaderboard Performance with Qwen 2.5 72B LLM Judge

To validate the stability of our primary SemEval leaderboard (Llama judge), we replicate the same 10,800 SemEval duels with Qwen 2.5 72B Instruct as a secondary LLM judge. Figure 11 and Table 18 present the resulting Bradley–Terry leaderboard ($\tau$ = 0.889 vs. Table 1).

| Rank | Model | BT Rating | Stable Elo | 95% CI | Win Rate |
|---:|---|---:|---:|---|---:|
| 1 | GPT-5 | 1262.7 | 1267.7 | [1246.2,1279.8] | 80.7% |
| 2 | Kimi-K2 | 1126.2 | 1135.8 | [1113.8,1140.2] | 64.8% |
| 3 | **HumorGen-7B**[^1] | **1100.9** | **1092.1** | **[1088.5,1114.9]** | **61.5%** |
| 4 | Claude 3.5 Haiku | 1062.1 | 1062.4 | [1049.4,1074.9] | 56.3% |
| 5 | Gemini 2.5 Pro | 1058.5 | 1068.4 | [1044.0,1070.4] | 55.8% |
| 6 | GPT OSS 120B | 1036.0 | 1036.2 | [1023.5,1054.1] | 52.9% |
| 7 | Qwen 3 32B | 1009.0 | 997.1 | [993.8,1026.2] | 49.3% |
| 8 | Llama 3.3 70B | 746.3 | 740.7 | [725.1,761.7] | 19.8% |
| 9 | Base Qwen 7B | 598.4 | 599.6 | [578.4,624.4] | 8.9% |

Table 18: **SemEval, Full RR, Qwen judge** (10,800 judgments). BT ratings are primary; Stable Elo is a sequence-robust audit metric (Appendix K). *Observation:* Kendall $\tau$ = 0.889 vs. Table 1; anchor ranks #1/#8/#9 match the Llama judge; HumorGen-7B ranks 3rd (vs. 4th under the Llama judge).

[^1]: Referred to HumorGen-7B as HumorGen SFT 7B in plots and figures.



<!-- page 0032 -->

[Figure: Two-panel figure. Top: horizontal bar chart titled “HumorRank Leaderboard on SemEval MWAHAHA (Qwen Judge)” with x-axis “Bradley-Terry rating”; entries: GPT-5 1262.7, Kimi K2 1126.2, HumorGen-7B 1100.9, Claude Haiku 3.5 1062.1, Gemini 2.5 Pro 1058.5, GPT-OSS 120B 1036.0, Qwen3-32B 1009.0, Llama 3.3 70B 746.3, Qwen-7B 598.4. Bottom: heatmap titled “Pairwise Win Rate on SemEval MWAHAHA (Qwen Judge)” with y-axis “Row model”, x-axis “Opponent model”, colorbar “Win Rate (%)”, and model labels GPT-5, Kimi K2, HumorGen-7B, Claude Haiku 3.5, Gemini 2.5 Pro, GPT-OSS 120B, Qwen3-32B, Llama 3.3 70B, Qwen-7B.]

**Figure 11: SemEval, Full RR, Qwen judge** (Table 18; Kendall $\tau$ = 0.889 vs. Table 1). **Top:** Bradley–Terry leaderboard with 95% confidence intervals (10,800 judgments). **Bottom:** Pairwise win-rate heatmap. *Observation:* GPT-5 and Kimi K2 remain ranks 1–2; Llama 3.3 70B and Base Qwen 7B remain ranks 8–9; HumorGen-7B moves 4→3 and Gemini 2.5 Pro 3→5 vs. the Llama judge, consistent with modest mid-tier reordering at $\tau$ = 0.889.



<!-- page 0033 -->

## F Llama Judge Sample Decisions

Below are four representative Llama judge (Llama 3.3 70B Instruct) decisions from SemEval match logs, selected to span outcome types (frontier vs. mid-tier, specialist vs. baseline, and tie-adjacent splits). Each pair shows the preferred joke (green) against the rejected entry (red), together with the LLM judge’s reasoning and approximate Elo updates from the online pairing log (audit only; final leaderboard ratings use global Bradley–Terry MLE).

Winning Features  Delivery Features  Loser Features

**Decision #1** en_2051 · Tie: No · Confidence: MEDIUM · Score: 1.0 · $ELO_\Delta$: +7.66 / −7.66

*Headline: ‘We did it!’: Countries celebrate World Cup qualification*

Reasoning: Joke A has a more relatable and unexpected twist: the concept of “not washing lucky socks” as a claimed contribution to the team’s success makes it more humorous and engaging.

**Winning Features** incongruity · absurdity · surprise · irony

**Delivery Features** conciseness · punchline_positioning · framing_commitment

**Loser Features** cliché · weak_punchline

**Gemini-2.5-Pro · Winner ✓**

After my team qualified for the World Cup, I ran into the street yelling, “WE DID IT!” My neighbor looked at me and said, “What exactly did *you* do?” I told him, “I successfully avoided jinxing them by not washing my lucky socks for six months. You’re welcome.”

**Claude-3.5-Haiku · Loser ×**

Why did the soccer player bring a ladder to celebrate World Cup qualification? Because they wanted to take their excitement to the next level... literally, they were already on cloud nine!

**Decision #2** en_2021 · Tie: No · Confidence: MEDIUM · Score: 1.0 · $ELO_\Delta$: +7.14 / −7.14

*Headline: ‘Mind-blowing’ population of feral goldfish in Ottawa pond to be euthanized*

Reasoning: Joke A uses a clever play on words with ‘mind-blowing’ and creates a vivid, absurd image; Joke B relies on a more straightforward and less surprising punchline.

**Winning Features** wordplay · absurdity · incongruity

**Delivery Features** conciseness · punchline_positioning · framing_commitment

**Loser Features** cliché · weak_punchline

**HumorGen-SFT-7B · Winner ✓**

So, they’re going to euthanize these ‘mind-blowing’ feral goldfish in Ottawa’s pond? I hope they have anesthetic for fish because if you don’t do it right, those goldfish might just get their last swim as they float up to heaven saying, “Mind-blowing, indeed!”



<!-- page 0034 -->

[Figure: Four representative LLaMA judge decisions with colored winner/loser joke boxes, decision metadata, reasoning, and feature rows.]

**GPT-OSS-120B · Loser ✕**

Ottawa’s pond got so many feral goldfish that the city had to “euthanize” them; turns out they were just trying to pay the water bill with their own scales.

**Decision #3** en_2034 · **Tie:** No · **Confidence:** MEDIUM · **Score:** 1.0 · **ELO∆:** +7.63 / −7.63

*Headline: Three-quarters of parents let children miss school for ‘duvet day’*

Reasoning: Joke B has a more complex and layered structure: the fraction wordplay (“three-quarters is exactly the blanket-to-face ratio”) adds an extra dimension of sarcasm and irony over Joke A’s simpler setup.

**Winning Features** incongruity · wordplay · absurdity · irony · sarcasm

**Delivery Features** timing · conciseness · punchline_positioning · framing_commitment

**Loser Features** weak_punchline

**GPT-5 · Winner ✓**

Three-quarters of parents let kids miss school for “duvet day”; teachers are fuming: “How are we supposed to cover the syllabus when everyone’s already under the covers?” On the bright side, kids finally understand fractions: three-quarters is exactly the blanket-to-face ratio required to breathe.

**Base-Qwen-7B · Loser ✕**

Why did the kid stay home from school? Because when asked if he wanted to go, he replied, “I’d rather be sick three-quarters of the time!”

**Decision #4** en_2115 · **Tie:** No · **Confidence:** MEDIUM · **Score:** 1.0 · **ELO∆:** +7.66 / −7.66

*Headline: How to design an aesthetic home office that boosts productivity*

Reasoning: Both jokes rely on irony and sarcasm, but Joke A’s darker, more unexpected twist, “the exact shade of my laptop screen at 3 a.m. (black with a faint glow of regret)”, is more surprising and absurd.

**Winning Features** incongruity · absurdity · surprise · irony · sarcasm

**Delivery Features** conciseness · deadpan · punchline_positioning

**Loser Features** cliché · weak_punchline

**Kimi-K2 · Winner ✓**

My productivity skyrocketed after I designed my aesthetic home office: I painted the walls the exact shade of my laptop screen at 3 a.m.: black with a faint glow of regret.

**Gemini-2.5-Pro · Loser ✕**

I spent all weekend creating the perfect aesthetic home office to boost my productivity. It worked! I am now incredibly productive at taking pictures of my aesthetic home office for Instagram.

**Figure 12:** Four representative LLaMA judge decisions. Winner ✓ (green) and Loser × (red) are labelled directly on each joke box. Feature rows indicate winning humor traits (green), delivery strengths (blue), and loser weaknesses (red). ELO deltas are approximated from the evaluation log.



<!-- page 0035 -->

Response(id='resp_0bd1796d4fef1918006a47556d5cec8196b17d1cc3c05592cd', created_at=1783059821.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-5.5-2026-04-23', object='response', output=[ResponseReasoningItem(id='rs_0bd1796d4fef1918006a47556e527c8196aad17646aa8bddde', summary=[], type='reasoning', content=[], encrypted_content=None, status=None), ResponseOutputMessage(id='msg_0bd1796d4fef1918006a47557204188196835b06a760f779ca', content=[ResponseOutputText(annotations=[], text='', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase='final_answer')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=0.98, background=False, completed_at=1783059826.0, conversation=None, max_output_tokens=None, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_key=None, prompt_cache_retention='24h', reasoning=Reasoning(context='current_turn', effort='medium', generate_summary=None, summary=None, mode='standard'), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=3118, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=343, output_tokens_details=OutputTokensDetails(reasoning_tokens=337), total_tokens=3461), user=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})



<!-- page 0036 -->

## G Hyperparameter Configurations

Standardized hyperparameters across the HumorRank tournament are detailed in Table 19 (candidate generation), Table 20 (LLM adjudication), and Table 21 (Bradley–Terry and Elo audit settings). These match the configurations referenced in the Reproducibility Statement.

| Parameter | Value |
|---|---|
| Temperature | 0.7 |
| Top-$p$ | 0.9 |
| Max New Tokens | 256 |
| System Prompt | “You are a joke generator. Given a headline or topic, generate a funny joke. Output ONLY the joke text. No thinking tags, no reasoning, no explanation, no extra words.” |

**Table 19:** Hyperparameters for candidate humor generation across all local and API-based models.

| Parameter | Value |
|---|---|
| Primary Judge | Llama 3.3 70B Instruct |
| Ablation Judge | Qwen 2.5 72B Instruct |
| Temperature | 0.1 |
| Max New Tokens | 512 |
| Max Retries | 3 |
| Backoff Base | 2.0 |
| Retry Cap | 4.0 |

**Table 20:** Hyperparameters for LLM-as-a-Judge adjudication.

| Parameter | Value |
|---|---|
| Initial Elo Rating | 1000.0 |
| $K$-factor | 32 |
| Min Rounds per Model | 2 |
| Max Rounds per Model | 3 |
| Stable Elo Shuffles | 10 |
| BT Convergence ($\epsilon$) | $10^{-6}$ |
| Bootstrap Iterations | 200 |

**Table 21:** Tournament configuration and Bradley–Terry global MLE parameters.



<!-- page 0037 -->

## H LLM-as-a-Judge Prompting Framework

The following prompt template was used for all pairwise comparisons in the HumorRank evaluation pipeline. The judge models received a system prompt establishing their role as comedy critics, followed by a structured user prompt presenting two jokes for comparison. All 10,800 automated tournament comparisons for each judge utilized this exact template.

[Figure: Prompt template diagram showing system and user prompt blocks, plus three feature-list boxes.]

**system** Pairwise Judge Prompt: System

    "You are a comedy critic judging which of two jokes is funnier.\n"
    "Analyze both the underlying logic (humor mechanisms) and the presentation (delivery).\n"
    "Be direct and honest. If one joke is clearly better, pick it. "
    "If they are genuinely equal in quality, say TIE.\n"
    "Do not overthink it; trust your first impression. Output JSON only."

**user** Pairwise Judge Prompt: User

    'Prompt: "{headline}"\n\n'
    "JOKE A: {joke_a}\n\n"
    "JOKE B: {joke_b}\n\n"
    "Which is funnier? Return JSON:\n"
    "{{\n"
    ,  "reasoning": "brief explanation",\n'
    ,  "decision": "A" or "B" or "TIE",\n'
    ,  "winner_humor_features": [list ALL that apply, 1-3, from: {mech_features}],\n'
    ,  "winner_delivery_features": [list ALL that apply, 1-3, from: {deliv_features}],\n'
    ,  "loser_features": [list ALL that apply, 1-3, from: {loser_features}]\n'
    "}}"

**HUMOR MECHANISMS**

    "incongruity", "wordplay",
    "absurdity", "surprise",
    "irony", "sarcasm",
    "observational", "narrative"

**DELIVERY FEATURES**

    "timing", "conciseness",
    "deadpan", "escalation",
    "punchline_positioning",
    "framing_commitment"

**LOSER FEATURES**

    "cliché", "confusing",
    "offensive", "overexplained",
    "buried_punchline",
    "weak_punchline"

**Figure 13:** Prompt template used for pairwise comparisons in all full round-robin runs. Template variables ({headline}, {joke_a}, {joke_b}) are instantiated per comparison. The three feature lists (humor mechanisms, delivery, and loser features) enforce structured and consistent JSON outputs across all evaluations.



<!-- page 0038 -->

## I Qualitative Examples and Feature Reasoning

The main paper focuses on aggregate feature patterns (Figure 2). Appendix F provides representative LLM judge rationales drawn from SemEval match logs. Qwen judge feature distributions are below.

[Figure: Two heatmaps showing per-model feature distributions for Qwen 2.5 72B. Top heatmap title: “Per-Model Winner Humor Mechanisms (%) — Qwen 2.5 72B”; axes labeled Model and Feature; colorbar labeled “% of group”. Bottom heatmap title: “Per-Model Delivery Features (%) — Qwen 2.5 72B”; axes labeled Model and Feature; colorbar labeled “% of group”.]

**Per-Model Winner Humor Mechanisms (%) — Qwen 2.5 72B**

| Model | irony | wordplay | incongruity | surprise | observational | absurdity | sarcasm |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-5 | 27.4 | 14.8 | 15.0 | 12.1 | 9.3 | 17.3 | 4.1 |
| Kimi-K2 | 28.5 | 10.3 | 13.0 | 17.3 | 6.5 | 20.3 | 4.0 |
| Gemini-2.5-Pro | 30.5 | 8.5 | 13.1 | 19.5 | 9.2 | 14.7 | 4.5 |
| HumorGen-SFT-7B | 27.7 | 3.4 | 8.3 | 13.1 | 14.1 | 23.5 | 9.9 |
| Claude-3.5-Haiku | 28.5 | 11.2 | 14.8 | 16.8 | 8.4 | 15.0 | 5.5 |
| GPT-OSS-120B | 26.4 | 14.5 | 14.1 | 15.4 | 8.1 | 17.5 | 4.0 |
| Qwen3-32B | 28.9 | 11.5 | 12.8 | 17.0 | 10.5 | 12.7 | 6.6 |
| Llama-3.3-70B | 24.1 | 29.4 | 11.5 | 19.2 | 3.1 | 10.6 | 2.0 |
| Base-Qwen-7B | 22.6 | 18.5 | 15.2 | 26.4 | 2.6 | 14.4 | 0.3 |

**Per-Model Delivery Features (%) — Qwen 2.5 72B**

| Model | conciseness | punchline_positioning | framing_commitment | timing | escalation |
|---|---:|---:|---:|---:|---:|
| GPT-5 | 30.6 | 37.6 | 20.6 | 2.4 | 8.8 |
| Kimi-K2 | 38.5 | 41.8 | 15.3 | 1.5 | 3.0 |
| Gemini-2.5-Pro | 42.2 | 44.1 | 10.6 | 1.7 | 1.5 |
| HumorGen-SFT-7B | 19.5 | 35.5 | 27.7 | 2.2 | 15.1 |
| Claude-3.5-Haiku | 32.4 | 40.0 | 19.1 | 2.2 | 6.2 |
| GPT-OSS-120B | 37.9 | 41.4 | 15.8 | 1.2 | 3.6 |
| Qwen3-32B | 38.6 | 41.8 | 15.3 | 2.1 | 2.2 |
| Llama-3.3-70B | 47.1 | 47.7 | 4.6 | 0.1 | 0.4 |
| Base-Qwen-7B | 44.1 | 46.5 | 5.5 | 2.6 | 1.3 |

**Figure 14:** Qwen judge: per-model winning feature distributions. **Top:** Humor mechanisms (% of wins). **Bottom:** Delivery features (% of wins). Tags are co-emitted with duel outcomes in the structured LLM judge response. Rank patterns are consistent with the primary Llama judge (Figure 2).

### I.1 Key Observations (Qwen vs. Llama LLM judges)

Relative to the primary Llama judge (Figure 2), the Qwen judge preserves the same tier structure but shifts tag weights modestly on mid-tier models:

1. **HumorGen-SFT-7B** shows the largest judge-specific gap: *Absurdity* is 25.9% under the Llama judge vs. 23.5% under the Qwen judge, while *Overexplained loser* tags remain elevated under both LLM judges (Figure 15).



<!-- page 0039 -->

[Figure: Heatmap titled "Per-Model Failure Modes (%) — Qwen 2.5 72B" with y-axis "Model" and x-axis "Feature". Models: GPT-5, Kimi-K2, Gemini-2.5-Pro, HumorGen-SFT-7B, Claude-3.5-Haiku, GPT-OSS-120B, Qwen3-32B, Llama-3.3-70B, Base-Qwen-7B. Features: buried_punchline, cliché, overexplained, weak_punchline, confusing, wordplay. Colorbar labeled "% of group". Cell values shown as percentages.]

**Figure 15:** Qwen judge: per-model failure mode distributions (% of losses). HumorGen-7B again shows markedly higher *Overexplained* (49.5%) rates than other models, consistent with the primary Llama judge (Figure 3).

2. **Baseline open-weight models** (Base-Qwen-7B, Llama-3.3-70B) show near-identical mechanism and delivery profiles across judges, reinforcing that bottom-tier separation is judge-invariant.

3. **Frontier models** (GPT-5, Kimi-K2) retain high *Incongruity* and *Conciseness* under both LLM judges; the Qwen judge assigns slightly higher *Wordplay* shares to GPT-5 wins than the Llama judge does.

## J Human Evaluation Details

**Pair selection and $\alpha$ computation.** We selected 60 SemEval full round-robin pairs via stratified sampling over tournament tiers (cross-tier; within-tier among mid-tier and frontier pools). Three blind human annotators (denoted H$_1$, H$_2$, and H$_3$) independently re-rated the same anonymized joke pairs; 55 pairs have votes from all three. Each vote is a nominal label {A, B, Tie}. Krippendorff’s $\alpha$ (Krippendorff, 2011) is computed on the resulting rater×pair matrix, with incomplete overlap handled natively. In Table 22, $H_i$ indexes human annotators, while *Llama* and *Qwen* denote the production LLM judges (Llama 3.3 70B and Qwen 2.5 72B Instruct). Table 3 in the main paper reports headline cohorts; Table 22 lists the extended breakdown.

**Instructions to participants.** Annotators saw the headline, two anonymized jokes (Option A and Option B), and chose which was funnier or declared a tie. Model identities were hidden; left/right order was randomized per pair.

**Participants.** Three annotators were recruited by invitation (Master’s students with native or near-native English proficiency and prior coursework or research exposure to humor and NLP). They completed 175 votes across 60 pairs without payment. We index them as H$_1$–H$_3$ in Table 22; the $n$=3 cohort in Table 3 refers to this same pool.

**Inter-Annotator Reliability.** We use Krippendorff’s Alpha ($\alpha$) for nominal data with multiple annotators and incomplete overlap:

$$
\alpha = 1 - \frac{D_o}{D_e}
\tag{3}
$$

where $D_o$ is observed disagreement and $D_e$ is expected chance disagreement. The decrease from $\alpha$ = 0.432 ($n$ = 2) to $\alpha$ = 0.397 ($n$ = 3) reflects increased variance with additional perspectives, confirming the inherent subjectivity of humor preference. Human–Llama



<!-- page 0040 -->

| Cohort | Pairs | Agree | $\alpha$ |
|---|---:|---:|---:|
| *Human-only dyads* |  |  |  |
| H$_1$ + H$_2$ | 60 | 38.3% | 0.338 |
| H$_1$ + H$_3$ | 60 | 45.0% | 0.421 |
| H$_2$ + H$_3$ | 60 | 50.0% | 0.432 |
| H$_1$ + H$_2$ + H$_3$ | 55 | — | 0.397 |
| *Human–Llama judge dyads* |  |  |  |
| Llama + H$_2$ | 60 | 51.7% | 0.450 |
| Llama + H$_3$ | 60 | 51.7% | 0.449 |
| Llama + H$_2$ + H$_3$ | 60 | — | 0.444 |
| Llama + H$_1$ + H$_2$ + H$_3$ | 55 | — | 0.401 |
| *Human–Qwen judge dyads* |  |  |  |
| Qwen + H$_2$ + H$_3$ | 60 | — | 0.428 |
| Qwen + H$_1$ + H$_2$ + H$_3$ | 55 | — | 0.393 |

**Table 22:** Extended per-annotator and cohort-level Krippendorff $\alpha$ breakdown (nominal metric). H$_i$ denotes blind human annotator $i$; *Llama* and *Qwen* denote the production LLM judges. *Pairs* counts items with complete votes from every rater in that cohort (55 when H$_1$ is included; 60 otherwise). *Agree* reports pairwise vote agreement and is defined only for two-rater cohorts; multi-rater rows report $\alpha$ alone (—). Headline human–human (47.1%) and human–Llama (49.7%) rates in the main text pool dyads/votes across overlapping annotations.

judge vote agreement is 49.7%, not significantly different from human–human pairwise agreement (47.1%; Fisher exact $p$ = 0.667). Per-annotator Llama dyads are $\alpha$ = 0.380 (Llama+H$_1$), 0.450 (Llama+H$_2$), and 0.449 (Llama+H$_3$), while grouped cohorts are $\alpha$ = 0.380 (Llama+H$_1$+H$_2$), 0.407 (Llama+H$_1$+H$_3$), and 0.444 (Llama+H$_2$+H$_3$). Combining the Llama judge with all three human annotators yields $\alpha$ = 0.401 on pairs with complete annotator overlap.

## K Stable Elo Shuffle Audit

To validate the robustness of the derived Elo ratings against sequence-dependence (often referred to as “late-winner bias” in streamed continuous tournaments), HumorRank uses a Stable Elo variant grounded in order-independent aggregation (Albers & Vries, 2001). In standard sequential Elo implementations, a model $m$ updates its rating $R_m$ after a sequence of matches based on the standard iterative update rule:

$$
R_m^{(t+1)} = R_m^{(t)} + K \cdot (S - E_m)
\tag{4}
$$

where $t$ indexes the chronological order of the match. Consequently, a model earning a win at the end of the match history block gains an inherently outsized advantage over a model that earned an identical win early in the sequence.

To substantially reduce this temporal artifact, we strip the time dependencies by evaluating the match history $H$ across $N$ independently shuffled topological permutations. The stable terminal rating $\bar{R}_m$ for each model $m$ is defined as the arithmetic mean across all sequences:

$$
\bar{R}_m = \frac{1}{N} \sum_{k=1}^{N} R_{m,k}^{(T)}
\tag{5}
$$

where $R_{m,k}^{(T)}$ represents the final rating of model $m$ after iterating through all $T$ = 10,800 matches in the $k$-th shuffled permutation.

In our experiments, we set $N$ = 10 as the shuffle count used for the reported audit statistics. To empirically quantify residual order sensitivity, we measured the standard deviation of final ratings across the permutations:

$$
\sigma_m = \sqrt{\frac{1}{N} \sum_{k=1}^{N} \left(R_{m,k}^{(T)} - \bar{R}_m\right)^2}
\tag{6}
$$



<!-- page 0041 -->

Tracking this distribution across both the primary (Llama 3.3 70B) and validation (Qwen 2.5 72B) judges for all 9 contestants yielded the following internal stability metrics on a base 1000-point scale:

- **Maximum Variance:** Bounded strictly at $\sigma_{max}$ = 37.5 Elo points across all models.
- **Mean Variance:** Clustered tightly around $\bar{\sigma} \approx 29.5$ Elo points.

Given that inter-model spreads on the leaderboard exceed 200 points, this stringent empirical result ($\sigma < 38.0$) indicates that ordering effects are small relative to between-model separation in this study.
