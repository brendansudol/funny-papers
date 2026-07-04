# One Does Not Simply Meme Alone: Evaluating Co-Creativity Between LLMs and Humans in the Generation of Humor

**Zhikun Wu, Thomas Weber, Florian Müller** — IUI 2025 · Guide entry #21 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2501.11433) · [local PDF](../pdfs/21-meme-co-creativity.pdf) · [full markdown](../md/21-meme-co-creativity/21-meme-co-creativity.md) · [extract](../extracts/21-meme-co-creativity.json)

## TL;DR
This paper studies whether GPT-4o can act as a co-creative partner for generating humorous internet memes. LLM assistance made participants produce more ideas and feel less effort, but human-AI collaboration did not improve meme quality; on average, AI-only memes were rated higher for humor, creativity, and shareability.

## Problem & Motivation
Prior work has examined LLM creativity in domains such as poetry, narratives, music, and art, but the paper argues that humor remains underexplored as a co-creative setting. Memes are a useful test case because they combine text and image, depend on cultural context, and are judged not only by whether they are funny but also by whether they feel creative and worth sharing.

## Approach
The authors ran a between-subject user study with human-only meme creation, human-AI meme creation, and AI-only meme creation. Human participants created captions for popular meme templates on constrained topics: work, food, and sports. In the collaboration condition, participants could chat with GPT-4o through a conversational interface during ideation. For the AI-only condition, GPT-4o was prompted to “generate 20 meme captions for this <image> about the topic of <topic>.” A second online survey then rated the generated memes.

## Data & Experimental Setup
For meme creation, 124 Prolific participants were recruited and 26 were excluded for not completing the task, leaving 98 usable participants from 30 countries. Participants had good English skills and prior experience with an LLM interface. Each participant worked on three image-topic combinations, spent at least four and at most five minutes ideating per image, selected three favorite ideas, and then added captions to the meme template. The study produced 882 favorite ideas across the human-involved conditions; 415 baseline ideas and 441 collaborative ideas were usable. After curation, the authors retained 335 human-only images and 307 human-AI images. One meme template was excluded because too many outputs were unusable. For rating, the authors sampled 150 images per condition. The rating study recruited N=100 participants, of whom 98 completed the task, each rating at least 50 images on humor, creativity, and shareability.

## Results
Participants created an average of 6.1 ideas (sd: 3.2). LLM-supported users generated significantly more ideas than baseline users: Mann-Whitney-U tests reported W = 12652, p < 0.001 for absolute count and W = 1519.5, p < 0.001 for average number of ideas. Overall Raw TLX workload did not differ significantly (t = -0.955, df = 88.811, p = 0.342), but the effort subscale was lower with LLM support (W = 755, p = 0.027). LLM users also reported lower ownership for “The generated captions are my ideas” (W = 562, p < 0.001).

For meme quality, generation condition significantly affected ratings across all topics: Funny F = 6.971, p = 0.001; Creative F = 5.793, p = 0.003; Shareable χ² = 11.761, p = 0.003. Pairwise comparisons showed AI-only memes were rated more positively than human-involved memes, except that shareability between cooperative and pure AI creation was not significant. Human-AI collaboration was not significantly different from human-only creation on any of the three dimensions. Topic analysis showed the significant differences came mainly from work memes: Funny F = 7.1, p = 0.001; Creative χ² = 11.22, p = 0.004; Shareable χ² = 8.470, p = 0.014.

## Takeaways
- LLMs can increase humorous ideation volume without increasing overall workload.
- More ideas did not translate into better rated memes when humans used AI assistance.
- AI-only generation produced broadly appealing memes on average in this study.
- Human involvement still mattered among top examples: human memes led in humor, while human-AI memes stood out in creativity and shareability.
- Designers of humor tools should support iteration, curation, and ownership, not just caption generation.

## Limitations & Caveats
The study measured only short-term use in a single session. Many participants did not deeply collaborate with the LLM: less than half interacted with it multiple times, and only six had more than eight interactions. The open-ended chat interface may not have guided iterative refinement well. Humor is culturally and socially dependent, but the study did not collect detailed demographic information such as ethnicity or language proficiency, limiting analysis of audience-specific humor preferences.
