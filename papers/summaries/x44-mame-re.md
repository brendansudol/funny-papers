# Memes-as-Replies: Can Models Select Humorous Manga Panel Responses?

**Ryosuke Kohita, Seiichiro Yoshioka** — arXiv:2602.15842v1 · Guide entry Part 5 (memes as conversational actions) (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2602.15842) · [local PDF](../pdfs/x44-mame-re.pdf) · [full markdown](../md/x44-mame-re/x44-mame-re.md) · [extract](../extracts/x44-mame-re.json)

## TL;DR
This paper introduces Meme Reply Selection: given a social media post, choose the funniest manga-panel meme reply. It also introduces MaMe-Re, a Japanese benchmark with 100,000 context–meme pairs and 500,000 crowd annotations. GPT-5 with panel descriptions is the best reported system, but only narrowly beats the best text-embedding baseline on Score@1: 0.325 versus 0.320.

## Problem & Motivation
The paper argues that memes are often used as conversational actions, not just static artifacts. Their humor depends on the interaction between a post and a reply image: a manga panel can become funny when recontextualized in a new situation. Existing meme work mostly studies intrinsic meme properties, while dialogue-media selection often emphasizes semantic relevance. The authors therefore define a task that evaluates whether models can select a contextually humorous visual reply rather than merely a relevant one.

## Approach
The authors formalize Meme Reply Selection as choosing the meme with the highest funniness score for a context. They define Score@1 as the average human reference funniness score of the selected meme. They compare two main method families. `sim-select` embeds the context and memes and selects the highest cosine-similarity candidate. `pref-select` prompts an LLM to choose the funniest candidate from a multiple-choice list. They also test retrieve-and-rerank, controlled candidate sets with one clearly funny meme, and candidate pools with varying semantic similarity.

## Data & Experimental Setup
MaMe-Re contains 250 GPT-4.1-generated synthetic social media contexts and 400 openly licensed manga panels from Black Jack ni Yoroshiku, all in Japanese. Exhaustive pairing creates 100,000 context–meme pairs. Each pair receives five binary funny/not funny annotations from Yahoo! Crowdsourcing, yielding 500,000 annotations from 2,325 unique annotators. The final score is the proportion of annotators judging a pair funny. Overall Fleiss’ κ is -0.022, but 20.4% of pairs have unanimous agreement and another 21.8% have high agreement.

## Results
In Exp1, GPT-5 with descriptions achieves Score@1 0.325 (±0.014) and CHR 0.052 (±0.016). The best similarity model, Sarashina-Text-Emb without descriptions, reaches Score@1 0.320 (±0.022), while random is 0.255 (±0.001). Visual information does not help consistently: Jina-CLIP-Multi-Emb scores 0.282, EvoVLM-VLM-Emb scores 0.263, and descriptions often slightly reduce performance. In Exp2, oracle reranking over retrieved candidates reaches 0.48 at k=4 and 0.55 at k=8, but LLM rerankers remain near or below the 0.320 standalone embedding baseline. In Exp3, GPT-5 scores 0.46, 0.41, and 0.37 for k=4, 8, and 12 when the funny candidate is clearly distinguishable. In Exp4, high candidate similarity reduces performance; for GPT-OSS at k=4, Score drops from 0.457 to 0.385.

## Takeaways
- Contextual humor selection is not solved by semantic relevance alone.
- LLMs show advantages on social cues such as exaggeration, irony, and persona, but the gains are small.
- Current models struggle to use visual information for active humorous reply selection.
- Retrieve-and-rerank needs stronger rerankers that can distinguish subtle differences in wit among plausible candidates.
- Benchmarks should test hard negative candidates, not only obvious funny-vs-unfunny choices.

## Limitations & Caveats
The benchmark is limited to Japanese manga from one source and synthetic contexts. The binary annotation scheme is simple, humor is highly subjective, and no annotator demographics were collected. Human baseline details in Exp3 are underreported, and the work studies selection rather than real-world generation or deployment.
