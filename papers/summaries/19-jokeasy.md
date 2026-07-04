# Jokeasy: Exploring Human-AI Collaboration in Thematic Joke Generation

**Yate Ge, Lin Tian, Chiqian Xu, Luyao Xu, Meiying Li, Yuanda Hu, Weiwei Guo** — arXiv:2602.09496 · Guide entry #19 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2602.09496) · [local PDF](../pdfs/19-jokeasy.pdf) · [full markdown](../md/19-jokeasy/19-jokeasy.md) · [extract](../extracts/19-jokeasy.json)

## TL;DR
Jokeasy is a search-enabled visual co-writing prototype for thematic joke generation. In a qualitative study with 13 hobbyists and 5 experts, most participants preferred Jokeasy to a search-enabled conversational baseline: 13 / 18 favoured Jokeasy. The central result is that real-time web material plus a structured visual workflow enriched ideation and preserved author agency, but users wanted finer search control, tighter chat–canvas integration, and more flexible visual editing.

## Problem & Motivation
The paper focuses on thematic jokes: jokes built around a specific topic, current event, anecdote, or cultural reference. The authors argue that this writing process depends on fresh material, audience relevance, and a setup-punchline structure. Ordinary LLM chat interfaces can generate humor, but they rely on static model knowledge and often provide little control over how topical material is found, selected, and transformed into jokes. The paper asks how a search-enabled LLM agent and a human writer can collaborate without overwhelming the writer or reducing creative agency.

## Approach
Jokeasy gives the LLM agent two roles: material scout and prototype writer. The system first helps the user specify a theme, audience, style, and requirements in a Topic Ideation Panel. It then derives three inspiration themes, expands search keywords, queries the web, and distills retrieved material into editable inspiration blocks. These blocks populate inspiration pools inside joke maps, each containing a provisional joke title and draft joke. Selecting a block opens the Echo Assistant, which shows source material and an echo summary explaining how the block might resonate with the intended audience. Users can edit, delete, manually add, or AI-add inspiration blocks, add or remove joke maps, and regenerate joke drafts.

## Data & Experimental Setup
The front end is a Figma widget plugin; the back end uses Node.js. The LLM is moonshot-v1-auto, with temperature set to 0.3, and search is implemented using the Tavily API. The study recruited 18 participants: 13 general users and 5 experts. Expert users included comedians with over five stand-up performance experiences, plus an HCI specialist and an AI researcher. Participants used both Jokeasy and a baseline conversational system in counter-balanced order. The baseline used the same LLM and search capabilities but lacked Jokeasy’s staged workflow and visual co-creation interface. All participants were native Chinese speakers, and LLM outputs were configured in Chinese.

## Results
Jokeasy beat the baseline in stated preference: 13 / 18 participants favoured Jokeasy. Eight participants said the agent reliably matched their intentions or sparked new ideas. Fourteen participants praised the visual canvas for structured clarity, often comparing it to a mind map. All five experts saw value in pairing an LLM with live search for humor that references current events, and 4 / 5 experts felt the non-linear canvas fit joke-writing practice. However, some users still felt the conversational baseline gave a stronger sense of collaboration, and experts said final judgment must remain with human creators.

## Takeaways
- Search-grounded joke tools should make source material traceable, not just generate punchlines.
- Inspiration blocks gave users a controllable unit for selecting, editing, and remixing topical material.
- Visual structure helped novices organize joke creation, but experts wanted more flexible mid-stage editing.
- Chat and canvas interaction should be combined: chat supports spontaneous riffing, while the canvas records decisions and evidence.
- Retrieval quality matters for humor; overly broad or weakly related sources can dilute specificity and authenticity.

## Limitations & Caveats
The prototype supports early-stage thematic joke creation, not full stand-up script development. Its simplified web search sometimes produced broad or insufficiently specific results. The sample size was modest, so the findings are not broadly generalizable. The authors also note that the system’s general-purpose design may have limited insights for specialized professional comedy workflows.
