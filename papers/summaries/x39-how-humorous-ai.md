# How humorous is AI? Exploring ChatGPT’s role in humor generation and human-AI interaction

**Yi Cao, Jiahao Cao, Yubo Hou, Li-Jun Ji** — Computers in Human Behavior Reports 20:100807 · Guide entry Part 5 (four-study HCI evaluation) (Part 5 - Situated Humor)

[paper page](https://www.sciencedirect.com/science/article/pii/S2451958825002222) · [local PDF](../pdfs/x39-how-humorous-ai.pdf) · [full markdown](../md/x39-how-humorous-ai/x39-how-humorous-ai.md) · [extract](../extracts/x39-how-humorous-ai.json)

## TL;DR
This paper reports four preregistered experiments on GPT-4o’s humor generation and use in human-AI interaction. GPT-4o beat humans on sentence-based humor and negative-context humor coping, but humans beat GPT-4o on image-caption humor; in conflict scenarios, AI assistance helped people, although pure AI responses were rated best.

## Problem & Motivation
The authors ask whether AI can produce humor that rivals humans and whether it can help people use humor in socially difficult situations. They focus on humor generation, humor coping, and interpersonal conflict, arguing that humor is not only about being funny but also about being effective, socially appropriate, and emotionally useful. They also examine Martin et al.’s four humor styles: affiliative, self-enhancing, aggressive, and self-defeating.

## Approach
The paper evaluates OpenAI’s ChatGPT using GPT-4o, described as the August 2024 version, via the ChatGPT web platform. Study 1 compares human and GPT-4o humor in image-caption and sentence-completion tasks. Study 2 compares human and GPT-4o humor coping in positive and negative contexts and has experts classify humor styles. Study 3 asks humans and GPT-4o to rate GPT-4o-generated examples of the four humor styles in a negative context. Study 4 tests whether GPT-4o helps people craft humorous responses to a workplace conflict.

## Data & Experimental Setup
Study 1 used 100 Prolific participants and 100 GPT-4o-simulated participants; 112 American university students rated outputs, with each caption or sentence rated by 14 raters. Study 2 used 97 human participants and 97 GPT-4o-simulated participants; 104 student raters judged funniness, two psychology experts coded humor type, and 40 student raters judged effectiveness in the negative context. Study 3 generated 100 GPT-4o responses per humor type, randomly selected 10 per type, and had 400 humans plus GPT-4o rate funniness, likability, and effectiveness. Study 4 had 200 senders create workplace-conflict responses, with 107 assigned to AI assistance and 93 to control; 350 recipients later evaluated 60 selected responses.

## Results
In Study 1, the group-by-task interaction was significant, F(1, 198) = 90.33, p < .001, ηp² = .31. Humans beat GPT-4o on image captions, M = 3.88 vs 3.24, but GPT-4o beat humans on sentence humor, M = 4.03 vs 3.57. In Study 2, GPT-4o was funnier than humans in positive contexts, M = 4.08 vs 3.60, and especially negative contexts, M = 4.21 vs 3.27. GPT-4o’s negative-context humor was also more effective, M=4.29 vs 3.80, F(1, 192)=15.45, p<.001. Experts coded GPT-4o’s negative-context humor as almost entirely self-enhancing: 96/97 and 97/97 across the two coders. In Study 3, human raters rated self-enhancing humor highest: funny M=4.91, likable M=5.06, effective M=5.37. In Study 4, AI-assisted senders rated their responses higher than controls on funniness, likability, effectiveness, and relief; for funniness, M = 4.28 vs 3.54.

## Takeaways
- GPT-4o is strongest where humor is text-based and context-sensitive.
- Human visual humor generation remains stronger in this study.
- For negative situations, GPT-4o converges on self-enhancing humor, which humans also rate as most effective.
- AI assistance can improve people’s confidence in their humorous conflict responses, but pure AI responses may be more polished than hybrid ones.
- Humor-system evaluations should measure effectiveness and relief, not only funniness.

## Limitations & Caveats
The findings are for GPT-4o only and may not generalize to other or newer models. The work is mostly in English and U.S. samples, and the authors note possible North American cultural bias. The studies cover text and images, but not audio or video cues such as tone, facial expression, or gesture. Inference details such as temperature, token limits, and exact model snapshot are not reported.
