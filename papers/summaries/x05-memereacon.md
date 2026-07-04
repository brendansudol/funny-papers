# MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models

**Zhengyi Zhao, Shubo Zhang, Yuxi Zhang, Yifan Zhang, Yanxi Zhao, Zezhong Wang, Huimin Wang, Yutian Zhao, Bin Liang, Yefeng Zheng, Binyang Li, Kam-Fai Wong, Xian Wu** — EMNLP 2025 · Guide entry Part 3 (also in this section) (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2505.17433) · [local PDF](../pdfs/x05-memereacon.pdf) · [full markdown](../md/x05-memereacon/x05-memereacon.md) · [extract](../extracts/x05-memereacon.json)

## TL;DR
MemeReaCon is a benchmark for testing whether large vision-language models understand memes in their original Reddit context: image, post text, and community comment. The main result is a sharp gap between surface classification and deeper explanation: Gemini-2.5-pro leads with 83.21% CMI-C accuracy but only 44.86% ROUGE-L for generating the poster’s intent.

## Problem & Motivation
The paper argues that meme meaning depends on where and why a meme is posted. The same image can mean different things in r/ProgrammerHumor and a generic meme subreddit because the post title, community norms, and comments change the intended interpretation. Prior meme work often treats memes as isolated images, focusing on harmfulness detection or standalone explanation. This leaves an evaluation gap: models may recognize image/text content but fail to explain why a meme was used in a particular social context.

## Approach
The authors introduce MemeReaCon, built around five annotation dimensions. Context-Meme Interplay labels whether the context explains the meme or the meme enhances the context. Meme Types label structure: Pure Meme, Text-in-Meme, Text-out-Meme, Comics, or Combination. Comment Stance and Affective Consistence labels whether a comment supports, denies, or extends the post, and whether its literal affect matches its intended meaning. Post Connection asks for key logical/thematic links among context, meme, and comments. Post Intent captures the poster’s purpose.

The benchmark supports four tasks: Context-Meme Interplay Classification, Comment Stance and Affective Consistent Classification, Post Connection Generation, and Post Intent Generation. The paper also proposes Context Relevance Score, using BERTScore relevance with a 0.7 threshold to quantify how well responses integrate post text, image, and comments.

## Data & Experimental Setup
The dataset contains 1,565 annotated instances from five English Reddit communities: r/meme(s) 690 (44.1%), r/ProgrammerHumor 352 (22.5%), r/BritishMemes 256 (16.4%), and r/RelationshipMemes 267 (17.1%). The initial pool had over 3,000 candidates; deleted/broken posts, too-short contexts, and non-meme images were filtered.

Six English-speaking Ph.D. annotators were trained, each instance received 3 annotations, and disagreements were resolved by majority vote or a senior annotator. Fleiss’ Kappa was CMI 0.86, MT 0.88, CSAC 0.75, PC 0.79, and PI 0.81. Models were evaluated zero-shot: Qwen2.5 and Flamingo as unimodal baselines; LLaVA-OneVision, Phi-4-MM, InternVL3, Qwen2.5-VL, and Qwen2.5-Omni as VLMs; QvQ, GPT-4o, Grok-3, Claude-3.7, and Gemini-2.5-pro as reasoning models.

## Results
Gemini-2.5-pro is best on every main task: 83.21% / 82.86% accuracy/macro-F1 on CMI-C, 71.28% / 59.42% on CSAC-C, 66.89% / 60.38% BERTScore/ROUGE-L on PC-G, and 52.34% / 44.86% on PI-G. It beats Claude-3.7 by 2.24 points on CMI-C accuracy, 2.89 points on CSAC-C accuracy, 3.24 ROUGE-L points on PC-G, and 4.55 ROUGE-L points on PI-G.

For Qwen2.5-Omni, self-consistency improves CMI-C accuracy from 68.86 to 73.42 and PI-G BERTScore from 30.43 to 36.28. CRS also favors reasoning models: Gemini-2.5-pro scores 0.68 and Claude-3.7 scores 0.64.

## Takeaways
- Contextual meme evaluation needs post text and comments, not just the image.
- Classification scores can overstate meme understanding; intent generation remains difficult.
- Specialized and cultural communities expose knowledge gaps.
- Builders should test whether systems connect visual details to communicative purpose, not only whether they describe the image.

## Limitations & Caveats
The authors note that post-connection annotations can be subjective and less consistently specified. Meme interpretation also depends on annotator background knowledge. The dataset is limited to English Reddit communities and may not represent other platforms or cultures.
