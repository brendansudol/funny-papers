<!-- guide claims for 65-humour-style-recognition (#65) -->

### 65. [A Two-Model Approach for Humour Style Recognition](https://arxiv.org/abs/2410.12842)
Kenneth, Khosmood & Edalat — **2024** · `preprint` `method` — Classifies text into the four Martin humor styles (see HSQ, Theory); ~+11.6% F1 on affiliative. Styles recur as generation conditions and judge personas (cf. Crowd Score #32).

---

## Synthesis: recurring themes

1. **Performance is task-format-dependent, not a fixed ladder.** As a rough pattern, forced-choice recognition/ranking is easiest to score, explanation reveals mechanism failures, and generation looks strong in constrained short-form settings but degrades with novelty, context, audience calibration, and live performance. "Recognition ≫ explanation ≫ origination" is a heuristic, not a law (contrast #2 with Gorenz & Schwarz #31) — though the paired Oogiri results show the gradient cleanly inside a single format (near-human understanding in #39 vs. low-to-mid-tier generation in #38).
2. **Humor competence fragments across joke types.** Transfer between humor types is real but partial and asymmetric (#40); models fail on genuinely novel instances of even simple pun schemas (#8); and no model reliably explains all four joke types in #5. "Humor" is many skills wearing one name — one reason the mechanism × medium × audience × context lens (point 8) is needed at all.
3. **Explanation is harder to fake than detection — but not foolproof.** Models can rationalize non-jokes or produce plausible post-hoc explanations (#2), so explanation is a *better* probe, not a perfect one (#1, #3, #58).
4. **"Understanding" is fragile.** Subtle perturbations break apparent comprehension — structure-matching over meaning (#4, #8, MemeReaCon).
5. **STEM reasoning only partly transfers — and where it does, it helps *comprehension*, not generation.** Reasoning gains carry over to cartoon-caption explanation (#3) but not to knowledge-heavy topical jokes or pun nuance (#5). This is the flip side of point 6: reasoning helps a model *get* a joke more than *make* one.
6. **Generic linear CoT is the wrong tool for generation.** Successful systems use structured creative search, script opposition, persona diversity, retrieval, or generate–evaluate–revise loops (#11–#20, #28, #29) — a lesson already visible in pre-LLM template systems (Part 2 foundations note): structure can be mechanized, brilliance can't.
7. **Data and scaffolding beat optimization tricks.** Quality data and skill/feedback pipelines outperform RLHF-style alignment (#13's twin null results; #14; #15; and #22, where SFT/RLHF/DPO underperform even with 250M ratings).
8. **Humor = mechanism × medium × audience × context.** Funniness is rarely one scalar; audiences cluster (#36), settings differ (#45, #46), and culture reshapes the joke (#30, #50–#55). Per benign violation + distance (T6), the *same* stimulus is funny or not depending on the rater's norm commitments and psychological distance — so any evaluator must fix or model the audience. Evaluation choices (#31–#40) drive the headline.
9. **Visual humor is harder than text humor.** Wider human gaps; models miss the humor-critical region or fail to integrate panels; world knowledge is the bottleneck (#24–#27) — and when humor must be read from *motion* without language, everything drops further (v-HUB, Part 3).
10. **Safety cuts both ways.** Filtering flattens comedic edge (#41), yet engagement-seeking humor amplifies harm (#47) and humor is a jailbreak vector (#49); benign violation (T6) is the knife-edge.

## Reading paths
- **Start:** Who's Laughing Now? (#58) → Hessel et al. (#1) → Inside Jokes (T3) + GTVH (T2).
- **Understanding:** HumorBench (#3) → Pun Unintended (#4) → Phunny (#8) → Comparing Apples to Oranges (#5) → ExPUNations (#7) → IRS / Cartoon Captionist (#24).
- **Generation:** CLoT (#11) → Small But Funny (#15) → HumorGen (#13) → Kim & Chilton (#14) → HOMER (#29); then A Robot Walks into a Bar (#41) for the human reality check.
- **Multimodal:** HumorDB (#25) → YesBut (#26) → Humor in AI (#22) → IRS (#24) → BottleHumor (#27) → HOMER (#29).
- **Evaluation/"are they funny?":** Jentzsch & Kersting (#2) vs. Gorenz & Schwarz (#31) → Crowd Score (#32) → Is GPT-4 Good Enough (#33) → Cards Against LLMs (#34) → HumorRank (#35) → Oogiri multi-dimensional (#38) → Oogiri-Master (#39) → Who Laughs with Whom (#36).
- **Generalization across humor types:** Phunny (#8) → One Joke to Rule them All (#40).
- **Live/situated:** Theater Stage as Laboratory (#43) → Improvised Theatre deployment (#42) → StandUp4AI (#44) → Not All Jokes Land (#45).
- **Theory:** SSTH (T1) → GTVH (T2) → incongruity-resolution / appropriate incongruity (T5) → benign violation + distance (T6) → Inside Jokes (T3).

---

*Compilation note:* entries were checked against primary sources where available; entries that lead with an arXiv ID rather than an author line are those whose authorship could not be confirmed against the primary source, and HUMORCHAIN's CVPR 2026 venue is taken from the CVF citation (the CVF page blocks automated fetching). Fast-moving 2025–26 preprint and workshop items may change venue or status, and tags marked `preprint` may since have appeared in a reviewed venue.
