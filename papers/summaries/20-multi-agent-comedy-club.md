# Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation

**Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu** — Findings of ACL 2026 · Guide entry #20 (Part 2 - Generating Jokes)

[paper page](https://aclanthology.org/2026.findings-acl.145/) · [local PDF](../pdfs/20-multi-agent-comedy-club.pdf) · [full markdown](../md/20-multi-agent-comedy-club/20-multi-agent-comedy-club.md) · [extract](../extracts/20-multi-agent-comedy-club.json)

## TL;DR
This paper tests whether public community discussion can improve LLM stand-up comedy writing when stored as retrievable social memory. In a 50-round GPT-4o-mini sandbox, discussion-enabled monologues beat a no-discussion baseline in 75.6% of human majority preferences and improved Craft/Clarity by Δ=0.440 and Social Response by Δ=0.422, but also increased aggressive and self-defeating humor.

## Problem & Motivation
Prior LLM writing work often uses prompts, private self-critique, or localized feedback. The authors ask whether a more public signal—broadcast community reception like comments, critiques, and audience discussion—can condition later creative writing. Humor is the test case because stand-up success is audience-oriented and depends on reception, timing, social framing, and risk.

## Approach
The authors build Multi-Agent Comedy Club, a controlled text-only sandbox with 35 GPT-4o-mini agents: one host, five performers, three critics, and twenty-six audience members. In every round, the host releases the same topic to both conditions and each performer writes exactly one monologue with no within-round revision. The intervention is binary: the baseline logs performances and moves on, while the discussion condition adds critic reviews, audience posts, and threaded free dialogue. High-signal reception is written into a vector-store social memory and later retrieved into performer context using similarity, importance, and recency. This isolates cross-round public reception as the intended mechanism.

## Data & Experimental Setup
The sandbox runs 50 fixed topics. The discussion condition yields 250 monologues and a trace with 5,384 interaction events; the baseline yields 250 paired monologues from the same performers and topics. Each monologue averages about 1,200 words. Five dedicated human raters evaluated all paired outputs. For each pair, they saw the topic and two anonymized randomized texts, chose an overall A/B preference (Q0), and rated both texts on Q1–Q15 1–5 Likert items covering amusement, craft, humor styles, moral pressure, memorability, share willingness, and social/task attraction. The paper avoids LLM judges for main quality evaluation, but uses GPT-5.1 at temperature 0 for a secondary audit of discussion-message failures.

## Results
Discussion won 75.6% of instance-level majority votes (189/250; Wilson 95% CI [69.9, 80.5]) and 70.1% of individual votes (876/1249). The main aggregate gains were Craft/Clarity (Q1–Q6) Δ=0.440 and Social Response (Q12–Q15) Δ=0.422. Item-level gains include Immediate Amusement: 2.85 vs. 2.33, Δ=0.52 [0.44, 0.59]; Justified Landing: 3.12 vs. 2.63, Δ=0.49 [0.42, 0.56]; and Task Attraction: 2.79 vs. 2.30, Δ=0.49 [0.42, 0.56]. Risk-related dimensions also rose: Aggressive humor Δ=0.42 [0.36, 0.49], Self-defeating humor Δ=0.25 [0.20, 0.30], and Value Judgment Pressure Δ=0.16 [0.12, 0.19]. Benefit and Safety were weakly correlated (Spearman ρ = -0.046, p = 0.472); 57/250 instances (22.8%) were “win–win,” and 6/250 (2.4%) were Pareto-efficient.

## Takeaways
- Persistent public feedback can be made into a usable conditioning signal for long-form humor generation.
- The strongest improvements come from craft and social impact, not merely from higher forced preference.
- Community feedback may push models toward sharper, edgier, and sometimes riskier comedic styles.
- Multi-dimensional human rubrics are more diagnostic than one binary funniness/preference vote; Q0 Fleiss’ κ was 0.237, while Δ mean Q1–Q15 ICC(3,5) was 0.710.
- Builders should treat reception memory as multi-objective: optimize quality while monitoring style, moral pressure, and moderation risks.

## Limitations & Caveats
The whole simulation uses GPT-4o-mini, so results may not generalize to Claude, Llama, Gemini, or other scales. The study uses only 50 fixed topics and five raters, with limited demographic reporting. There is no human-written comedy baseline. Several reproducibility details are missing, including model snapshots, exact decoding parameters, embedding model, and cost/model-call counts.
