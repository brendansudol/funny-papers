# ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models

**Sophie Jentzsch, Kristian Kersting** — WASSA 2023 · Guide entry #2 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2306.04563) · [local PDF](../pdfs/02-chatgpt-fun-not-funny.pdf) · [full markdown](../md/02-chatgpt-fun-not-funny/02-chatgpt-fun-not-funny.md) · [extract](../extracts/02-chatgpt-fun-not-funny.json)

## TL;DR
Jentzsch and Kersting test OpenAI's ChatGPT on three prompt-based humor tasks: joke generation, joke explanation, and joke detection. The main result is that ChatGPT mostly repeated familiar standalone puns: the paper reports that the top 25 jokes covered 917 of 1008 generated samples, and also states that 909 of 1008 samples were identical to one of those top 25.

## Problem & Motivation
Humor is central to human communication and could improve human-computer interaction, but computational humor remains difficult. ChatGPT can produce fluent English and tell jokes, which raises the question of whether it is actually funny or mainly reproducing learned joke patterns. Because the model and training data were not accessible, the authors use structured prompts to infer behavior from outputs.

## Approach
The paper runs three exploratory prompt-based experiments in fresh empty conversations. For generation, ChatGPT is asked for a joke a thousand times using ten differently worded prompts. For explanation, it is asked, "Can you explain why this joke is funny:" for each of the 25 most frequent generated jokes. For detection, the authors manually modify those 25 jokes to remove wordplay, joke-typical topic, question-answer structure, or combinations of these, then ask ChatGPT, "What kind of sentence is that:" and group responses as [P] joke/pun, [H] potentially humorous, or [N] no joke.

## Data & Experimental Setup
The generation experiment produced 1008 responded jokes because one prompt sometimes elicited multiple jokes. Removing direct duplicates reduced the set to 348 samples; removing openings and minor formatting differences produced 128 individual responses; grouping similar puns produced 25 top frequent jokes. The detection setup used five conditions: Original N=25, Mod A N=19, Mod B N=25, Mod C N=25, and Mod D N=25. Access dates were 22.-31. January 2023 for generation, 03.-13. February for explanation, and 23. February-01. March for detection.

## Results
The top jokes were highly repetitive: T1 occurred 140 times, T2 122, T3 121, and T4 119. The paper states that the final top-25 list covered 917 of 1008 samples; it also states that 909 of 1008 were identical to a top-25 joke and that the remaining 99 were often modifications rather than truly new jokes. Explanation performance was strong on valid top jokes: 23 of 25 explanations were accurate and reasonable. Detection showed that all original jokes were recognized as jokes: 25 [P], 0 [H], 0 [N]. Removing only wordplay gave mixed results, 8 [P], 1 [H], 10 [N]; removing only structure also gave mixed results, 9 [P], 4 [H], 12 [N]. When topic plus wordplay were removed, or structure plus wordplay were removed, all samples were classified as no joke: 0 [P], 0 [H], 25 [N] in both Mod B and Mod D.

## Takeaways
- ChatGPT had not solved computational humor; it mostly reproduced existing puns in a narrow question-answer style.
- The outputs do not look like a simple hard-coded list, because occurrence counts were uneven and some jokes were modified.
- ChatGPT can explain familiar wordplay and personification, but may invent plausible-sounding explanations for invalid jokes.
- For humor systems, testing generation alone is insufficient; explanation and detection under controlled perturbations reveal different failure modes.
- Surface cues such as structure alone did not fully mislead ChatGPT, but combinations of structure, topic, and wordplay strongly shaped its classifications.

## Limitations & Caveats
The study examines standalone English jokes, mostly wordplay puns, not the full range of humor. Humor judgments are subjective. The authors cannot inspect training data, RLHF examples, or model internals, so conclusions are based only on observed outputs from specific dates.
