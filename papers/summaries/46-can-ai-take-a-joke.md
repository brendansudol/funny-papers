# Can AI Take a Joke—Or Make One? A Study of Humor Generation and Recognition in LLMs

**Kexin Quan, Pavithra Ramakrishnan, Jessie Chin** — Creativity & Cognition 2025 · Guide entry #46 (Part 5 - Situated & Live Humor)

[paper page](https://dl.acm.org/doi/10.1145/3698061.3734388) · [local PDF](../pdfs/46-can-ai-take-a-joke.pdf) · [full markdown](../md/46-can-ai-take-a-joke/46-can-ai-take-a-joke.md) · [extract](../extracts/46-can-ai-take-a-joke.json)

## TL;DR
This paper evaluates whether GPT-4o, Gemini 1.5, and LLaMA3.3 can generate and recognize humor in emotionally sensitive, support-oriented conversations. It introduces two small datasets and finds GPT-4o strongest for generation tone and humor-style fit, while recognition remains modest: GPT-4o reaches μ = 0.65 for humor classification, and LLaMA3 leads role classification at μ = 0.60.

## Problem & Motivation
Humor can build rapport, ease tension, and support emotional connection, but it can also fail badly when timing, role, or emotional context is misread. The paper focuses on supportive settings such as counseling, peer support, mental health chatbots, and tutoring, where humor must be not only fluent but also appropriate. The central question is whether current LLMs can produce and interpret humor with enough pragmatic and relational sensitivity for these contexts.

## Approach
The authors compare ChatGPT/GPT-4o, Gemini 1.5, and Meta LLaMA3.3 using two complementary tasks. For generation, models are prompted to write short statements incorporating three keywords and matching a specified humor style. Human raters then judge whether the intended style is recognizable and whether the statement is emotionally appropriate and funny. For recognition, each model classifies human-written supportive statements by humor style and by speaker role, distinguishing Counselor from Friend.

## Data & Experimental Setup
The Humor Generation Dataset contains 60 AI-generated statements, with 20 from each LLM. The paper describes prompts combining three contextual keywords with humor styles; the reported generation results focus on Affiliative, Self-Defeating, and No Joke categories, while Table 1 also shows examples involving Wordplay/Puns and Dry Humor. Two independent human raters labeled generated statements blind to the original prompt and rated appropriateness and humor strength on 5-point Likert scales. The Humor Recognition Dataset contains 20 human-authored responses crafted by a researcher to simulate emotionally sensitive scenarios, varying by speaker role and humor condition.

## Results
For generation style alignment, ChatGPT performs best on clear categories: No Joke reaches μ = 1.00, σ = 0.00, and Self-Defeating reaches μ = 0.93, σ = 0.051. Gemini is moderate on Self-Defeating with μ = 0.71, σ = 0.00 and No Joke with μ = 0.60, σ = 0.00, but weak on Affiliative humor with μ = 0.13, σ = 0.129. LLaMA3 is reported at μ = 0.50, σ = 0.257 for Affiliative style alignment.

On emotional appropriateness, ChatGPT again leads, especially for Affiliative responses with μ = 4.35, σ = 0.13 and No Joke with μ = 4.13, σ = 1.24. Gemini has moderate appropriateness for Affiliative with μ = 3.82, σ = 0.44 and Self-Defeating with μ = 3.57, σ = 0.57. LLaMA3 is lower for No Joke, at μ = 2.93, σ = 0.46. For humor strength, Affiliative humor is rated funniest overall, with both ChatGPT and LLaMA3 at μ = 3.66.

For recognition, ChatGPT leads humor classification at μ = 0.65, compared with Gemini 1.5 and LLaMA3 at μ = 0.60. LLaMA3 leads speaker-role classification at μ = 0.60, while ChatGPT and Gemini 1.5 each score μ = 0.55.

## Takeaways
- Fluent humor generation is not the same as emotionally appropriate humor.
- GPT-4o shows the strongest balance of style alignment and emotional fit in this study.
- Affiliative humor remains difficult because it depends on subtle social connection.
- Role sensitivity is a bottleneck: models blur Counselor and Friend even with clean inputs.
- Builders of support-oriented humor systems should treat LLM output as draft material requiring human judgment.

## Limitations & Caveats
The datasets are small and narrow in scope. The rater pool is small and homogeneous, which may introduce subjective bias and reduce annotation reliability. The study uses static single-turn statements, not real multi-turn interactions where humor timing, repair, and user perception evolve over time.
