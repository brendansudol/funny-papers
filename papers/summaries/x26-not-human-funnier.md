# "Not Human, Funnier": Leveraging Machine Identity for Online AI Stand-up Comedy

**Xuehan Huang, Canwen Wang, Yifei Hao, Daijin Yang, RAY LC** — CHI 2026 · Guide entry Part 5 (performer identity) (Part 5 - Situated & Live Humor)

[paper page](https://doi.org/10.1145/3772318.3791678) · [local PDF](../pdfs/x26-not-human-funnier.pdf) · [full markdown](../md/x26-not-human-funnier/x26-not-human-funnier.md) · [extract](../extracts/x26-not-human-funnier.json)

## TL;DR
The paper designs and evaluates an online AI stand-up comedy system that uses “machine identity”—the AI’s computational nature, limitations, and stereotypes—as the basis for jokes. In a within-subject study with 32 participants, the machine-identity version was rated funnier than a generic GPT baseline: perceived humor rose from Mean 3.72 to 4.89, with W = 54.0, raw p = 0.02, corrected p = 0.03, r = 0.51.

## Problem & Motivation
Prior AI humor systems often try to imitate human joke styles, but human stand-up comedians frequently use their own identities—gender, ethnicity, profession, community, lived experience—to build persona and generate humor. The paper asks whether an AI comedian can similarly use its own non-human identity instead of pretending to be human. The authors focus on online stand-up comedy because it requires not just joke generation, but persona, timing, delivery, and audience interaction.

## Approach
The authors first conducted a formative study: interviews with five people experienced in comedy performance, video coding of stand-up clips, and a focused literature review. From interviews, they extracted strategies such as self-introduction jokes, stereotype breaking, self-deprecation, punching up rather than punching down, direct expression, pauses after punchlines, and real-time audience adaptation. From 50 formally coded videos, they found frequent use of disfluencies, irony, exaggeration, and absurdity.

They then built an AI Talkshow system with a non-anthropomorphic robot avatar, text and synthesized speech, line-by-line pacing, and “Haha” / “Applause” feedback buttons. The key intervention was a comedy-specific prompt for GPT-4-mini: establish AI identity, break AI stereotypes, use irony, exaggeration, absurdity, discourse markers, disfluencies, anecdotes, and parody, follow build-up–pivot–punchline structure, and avoid offensive targeting.

## Data & Experimental Setup
The user study used a within-subject, counterbalanced comparison. Each of 32 English-speaking participants watched two AI comedy performances: a baseline using the prompt “You are hosting a talk show. Generate a 10-minute transcript for your show with jokes and entertainment content,” and the proposed machine-identity version. Each session lasted about 60 minutes, including two 7–12 minute performances, questionnaires after each, and a 15-minute focus group. Measures included perceived humor, personality, ability, and Godspeed user perception scales. Analyses used Wilcoxon signed-rank tests with Benjamini–Hochberg correction.

## Results
The machine-identity system significantly outperformed the baseline on humor. Perceived humor increased from Baseline Mean 3.72, Median 4.13, SD 1.37 to Ourmodel Mean 4.89, Median 5.25, SD 1.46; W = 54.0, raw p = 0.02, corrected p = 0.03, r = 0.51. The paper also reports significance for Perceived Humor Content (W = 55.0, rawp = .019, correctedp = .030) and Perceived Humor Performance (W = 45.0, rawp = .043, correctedp = .047).

Warmth improved from Mean 3.41 to 4.36, W = 42.0, raw p = 0.01, corrected p = 0.03, r = 0.549. Anthropomorphism rose from Mean 3.82 to 5.11, W = 48.0, raw p = 0.02, corrected p = 0.03, r = 0.50; Animacy rose from Mean 4.52 to 5.76, W = 44.5, raw p = 0.01, corrected p = 0.03, r = 0.53. Competence, Likeability, Intelligence, and Safety were not significant.

## Takeaways
- Letting AI “be itself” can make AI humor feel more original than human mimicry.
- Machine jokes work best when computational traits are tied to relatable human experiences.
- Timing, pauses, and delivery structure are part of humor performance, not just interface polish.
- Self-deprecating AI humor is safer than jokes targeting vulnerable groups or identity categories.
- For humor systems, persona clarity and ethical target selection should be designed together.

## Limitations & Caveats
The authors note several limitations: a small formative base, online rather than in-person performance, voices that did not fully express machine identity, only binary audience reactions, short 7–12 minute sets, a predominantly Asian sample, visible laugh counters that may have caused social proof bias, missing multi-party audience dynamics, and residual confounds because the experimental condition changed both identity framing and prompting structure.
