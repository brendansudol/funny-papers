# COMIC: Agentic Sketch Comedy Generation

**Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman, Steve Seitz** — arXiv:2603.11048 · Guide entry Part 2 (also in this cluster) (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2603.11048) · [local PDF](../pdfs/x02-comic.pdf) · [full markdown](../md/x02-comic/x02-comic.md) · [extract](../extracts/x02-comic.json)

## TL;DR
COMIC is a fully automated multi-agent system for generating 1–2 minute sketch-comedy videos from character portraits, voices, text descriptions, and backgrounds. Its main result is that COMIC scored highest in human-rated funniness among tested systems, with 3.45 versus Sora 2 at 2.73, Veo 3.1 at 2.32, VGoT at 1.18, and MovieAgent at 1.27.

## Problem & Motivation
The paper asks whether AI can reliably be funny, not just occasionally produce a good joke after many tries. Sketch comedy requires three hard pieces at once: finding a comedic premise, writing a funny script with payoff, and rendering a coherent multi-shot video with stable characters and backgrounds. The authors argue that a fixed scalar reward is ill-suited to humor because humor is subjective, context-dependent, and stylistically diverse.

## Approach
COMIC models a production studio with agents for writing, criticism, editing, scene direction, rendering, and voice generation. A central contribution is viewer-aligned LLM critics: the system generates diverse critic personas, then selects those whose pairwise preferences best match engagement tiers from real YouTube comedy sketches. Script generation uses multiple isolated islands, each with its own critic committee; scripts compete in round-robin pairwise tournaments, and only losing scripts are revised using critic feedback. Rendering uses script-conditioned video critics, storyboards, shot-level iterative refinement, history tournaments to avoid over-refinement, and final tournaments across complete video realizations.

## Data & Experimental Setup
For critic alignment, the authors collected 4,940 data points from five YouTube sketch comedy channels: Foil Arms & Hog, Key & Peele, SNL, Studio C, and Viva La Dirt League. They normalized view counts by fitting per-channel logistic growth models, then extracted 30 data points from each of 5 channels and 3 engagement tiers, giving 450 total data points split into in-context, validation, and test sets. The base COMIC configuration uses 3 islands, 3 scripts per island, 3 critics per island, 2 scene directions, and 1 rendering critic. Human evaluation compared COMIC with Veo 3.1, Sora 2, VGoT, and MovieAgent using 22 responses per method, 110 total responses, and 7-point Likert ratings.

## Results
Task-Wise Best critic selection outperformed Mean Critic and Single Best on validation, reaching 0.64 average accuracy for Top vs. Middle and 0.83 for Top vs. Bottom. On held-out scripts, it remained best with 0.578 and 0.716. In human evaluation, COMIC led on Funniness (3.45), Watch More (3.09), vs. Human (3.05), Script (3.32), and Narrative (4.50). Sora 2 and Veo 3.1 remained higher on Realism and Consistency. Automated video evaluation also favored COMIC, with win rates of 0.440 under Single Best and 0.390 under Channel-Wise Best. In the no-critics ablation, raters preferred COMIC by 62% vs 38% for funniness and 100% for consistency.

## Takeaways
- Humor evaluation worked best when critics were selected for specific comparison tasks and channels.
- Iterative competition mattered: critic-free generation was consistently weaker.
- Multi-island search helps preserve specialized comedic styles rather than forcing one global objective.
- For humor systems, script and narrative quality can outweigh raw visual realism in viewer preference.

## Limitations & Caveats
The method is computationally expensive despite parallelizable structure. YouTube view counts are a noisy proxy for humor because clickbait and algorithmic promotion can affect popularity. The system does not yet incorporate sound effects, and the authors identify attribution and originality measurement for internet-derived corpora as future work.
