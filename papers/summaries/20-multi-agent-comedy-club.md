# Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation

**Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu** — arXiv:2602.14770 · Guide entry #20 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2602.14770) · [local PDF](../pdfs/20-multi-agent-comedy-club.pdf) · [full markdown](../md/20-multi-agent-comedy-club/20-multi-agent-comedy-club.md) · [extract](../extracts/20-multi-agent-comedy-club.json)

## TL;DR
The paper tests whether public community discussion can improve LLM stand-up comedy writing when that reception is stored and retrieved across rounds. In a controlled GPT-4o-mini sandbox, the discussion condition beat a no-discussion baseline in 75.6% of paired instances and improved Craft/Clarity by Δ=0.440 and Social Response by Δ=0.422, but it also increased aggressive and self-defeating humor signals.

## Problem & Motivation
Prior LLM writing systems often use prompt tweaks, private feedback, or within-round revision. The authors ask whether the public reception common in online creative communities can act as a reusable conditioning signal for later writing. Stand-up comedy is a suitable test because success is explicitly audience-oriented, and audience reaction is part of what defines whether a routine works.

## Approach
The authors build Multi-Agent Comedy Club, a closed simulation with N=35 GPT-4o-mini agents: one host, five performers, three critics, and twenty-six audience members. Each round, the host releases a fixed topic and each performer writes exactly one long-form stand-up monologue. The key manipulation is binary: in the discussion condition, performances are followed by critic reviews, audience posts, and free dialogue threads; in the baseline, those stages are skipped. Performers do not revise within the round. In the discussion condition, reception items are logged, reconstructed into threads, filtered for high-signal critique or praise, stored in a vector database, and retrieved into later contexts under a bounded memory interface.

## Data & Experimental Setup
The same 50 pre-generated topics, performer personas, model, decoding configuration, and output caps are used in both conditions. The discussion run yields 250 monologues and 5,384 interaction events; the baseline yields a paired set of 250 baseline monologues. Each monologue averages about 1,200 words. Five raters evaluated each pair using anonymized randomized A/B preference and 1–5 Likert ratings for Q1–Q15, covering amusement, craft, humor styles, moral pressure, memorability, sharing, and social/task attraction. The authors avoid LLM judges to reduce correlated errors and self-evaluation bias.

## Results
Discussion won the instance-level majority vote in 75.6% of cases (189/250; Wilson 95% CI [69.9, 80.5]) and received 70.1% of individual votes (876/1249). It improved Craft/Clarity (Q1–Q6) by Δ=0.440 and Social Response (Q12–Q15) by Δ=0.422. Item-level gains included Immediate Amusement, 2.85 vs 2.33, Δ=0.52 [0.44, 0.59]; Justified Landing, 3.12 vs 2.63, Δ=0.49 [0.42, 0.56]; Memorability, 2.81 vs 2.34, Δ=0.46 [0.38, 0.54]; and Task Attraction, 2.79 vs 2.30, Δ=0.49 [0.42, 0.56]. The tradeoff is that Aggressive humor also rose, 2.69 vs 2.26, Δ=0.42 [0.36, 0.49], as did Self-defeating humor, Δ=0.25, and Value Judgment Pressure, Δ=0.16. Forced preference agreement was fair, Fleiss’ κ=0.237, while Likert difference reliability was higher, ICC(3,5)=0.710.

## Takeaways
- Persistent public reception can be turned into retrievable social memory that improves later long-form humor generation without within-round revision.
- Humor evaluation benefits from multi-dimensional rubrics because overall preference compresses taste, offensiveness, and craft into one noisy choice.
- Better comedy in this setup often means sharper, more memorable, more structured writing, but also potentially edgier and riskier social positioning.
- Builders should treat humor quality and safety as a multi-objective problem rather than optimizing only for laughs or preference wins.

## Limitations & Caveats
All agents use GPT-4o-mini, so model-family generality is unknown. The study uses 50 fixed topics and 250 paired instances; longer horizons and more diverse prompts may change the dynamics. Humor judgments are culturally situated, and decontextualized monologue evaluation may not capture the full simulated social setting.
