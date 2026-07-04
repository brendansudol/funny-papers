# Humor Mechanics: Advancing Humor Generation with Multistep Reasoning

**Alexey Tikhonov, Pavel Shtykovskiy** — ICCC 2024 · Guide entry #16 (Part 2 - Generating Jokes)

[paper page](https://computationalcreativity.net/iccc24/papers/ICCC24_paper_128.pdf) · [local PDF](../pdfs/16-humor-mechanics-multistep.pdf) · [full markdown](../md/16-humor-mechanics-multistep/16-humor-mechanics-multistep.md) · [extract](../extracts/16-humor-mechanics-multistep.json)

## TL;DR
This paper proposes a GPT-4-based multi-step pipeline for generating English one-liner jokes. It first infers a humor-generation policy from highly ranked human one-liners, then brainstorms and refines associations for a topic before generating jokes. In human evaluation, the full pipeline achieved the best average funniness, 2.72, versus 2.56 for zero-shot GPT-4 and 2.38 for a cleaned Reddit joke subsample; its strongest result is improved novelty, with the text reporting 17.6% known jokes and 82.4% previously unknown jokes.

## Problem & Motivation
The authors argue that direct LLM prompting tends to produce memorized or standard jokes, while genuine humor generation requires combining distant associations and applying joke-construction principles. They focus narrowly on one-liners: short, self-contained jokes of one or two sentences. Rather than hand-coding a humor theory, they test whether GPT-4 can infer a usable humor policy from examples and whether a creative-problem-solving-style association process can improve joke generation.

## Approach
The method has two main parts. First, the authors create a seed set of high-quality jokes by taking 100 random one-liners from the “16000 OneLiners” dataset, collecting pairwise human rankings with ten assessors per pair, and keeping the top 30 jokes. GPT-4 decomposes each joke into humorous building blocks, then distills the decompositions into a humor-generation policy prompt.

Second, Algorithm 1 generates jokes from a topic. A topic is randomly selected from the top 10,000 most frequent English words after filtering profanity, stopwords, and words shorter than four letters. GPT-4 generates 20 associations, expands them, refines them into at most six stronger association items, and finally writes 7-10 one-liners using the topic, refined associations, and humor policy.

## Data & Experimental Setup
The authors evaluate five generation schemes: zero-shot GPT-4, no-assoc, assoc-v1, assoc-v2, and full. Table 2 reports 100 zero-shot examples, 120 examples for each other generated condition, and 156 cleaned positive Reddit jokes from ReJ. Each text was labeled on ScaleAI by at least five native English-speaking annotators. Labels covered understandability, offensiveness, whether the text is a joke, whether the annotator had heard it before, funniness on a 1-5 scale, and an explanation.

## Results
The full method had the best Funniness score, 2.72, compared with 2.56 for zero-shot, 2.66 for no-assoc, 2.67 for assoc-v1, 2.55 for assoc-v2, and 2.38 for reddit. It also had the highest Understandable score, 93%, versus 88% for zero-shot and no-assoc, 91% for assoc-v1, 90% for assoc-v2, and 84% for reddit. On IsJoke, full tied zero-shot at 84%, ahead of reddit at 72%.

Novelty was the clearest gain. Table 2 gives Known as 27% for zero-shot, 24% for no-assoc, 19% for assoc-v1, 20% for assoc-v2, 18% for full, and 27% for reddit; the text further reports 17.6% known and 82.4% previously unknown for the proposed method. Mann-Whitney U p-values for known scores were 0.0008% for full vs zero-shot GPT-4, 0.46% for full vs no-assoc, and 0.002% for full vs reddit. Funniness significance was weaker: full vs zero-shot had p=6.89% on averaged scores and p=2.93% on all scores.

## Takeaways
- Multi-step prompting can improve both joke quality and novelty over direct GPT-4 prompting.
- Association mining appears important; the authors state that the policy alone is insufficient to improve zero-shot quality significantly.
- Human evaluation is essential because automatic humor assessment remains unreliable and humor is subjective.
- Novelty should be measured explicitly, since zero-shot GPT-4 produced many jokes annotators had heard before.
- Better funniness came with a cost: full had 11% Offensive, higher than assoc-v2 at 7% and assoc-v1 at 8%.

## Limitations & Caveats
The sample sizes are small, and the authors warn that some differences are near the border of significance. Novelty is based on annotator memory, so true novelty may be lower. The study covers only English one-liners, annotator cultural backgrounds were unavailable, and high-quality jokes with funniness in {4,5} were described as negligible.
