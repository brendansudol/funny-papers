# Evaluating Humor Generation in an Improvisational Comedy Setting

**Thomas Winters, Stijn Van der Stockt** — Computational Linguistics in the Netherlands Journal 14 · Guide entry Part 5 (live improv evaluation) (Part 5 - Situated Humor)

[paper page](https://www.clinjournal.org/clinj/article/view/214) · [local PDF](../pdfs/x37-improv-comedy-setting.pdf) · [full markdown](../md/x37-improv-comedy-setting/x37-improv-comedy-setting.md) · [extract](../extracts/x37-improv-comedy-setting.json)

## TL;DR
This paper evaluates GPT-4 humor generation in a live Dutch improvisational comedy show, comparing AI-generated jokes with jokes improvised by three professional comedians under the same audience suggestions. Human jokes were preferred slightly more often (34.6% vs. 29.7%, with 35.7% ties), but GPT-4 produced several standout jokes, including the top-rated joke and 6 of the top 10 jokes by average rating.

## Problem & Motivation
Humor generation is hard to evaluate because humor is subjective, delivery matters, and human baselines are often unfairly polished. The authors argue that comparing raw AI jokes with curated jokes from comedians, joke books, or online repositories underestimates AI systems and fails to account for live performance. They therefore move evaluation into an improvisational setting where humans and GPT-4 must produce jokes on the spot from the same prompts.

## Approach
The study uses three “Scenes from a Hat”-style improv games: “Worst Slogan for X,” “If X is the Answer, What is the Question?”, and “Sex with Me is Like X.” For each game, the authors prepared a GPT-4 prompt with few-shot chain-of-thought examples. During the live show, an audience suggestion was inserted into the relevant prompt, GPT-4 generated multiple candidate jokes, and an offstage assistant selected jokes to show on a screen. Comedians then performed both their own improvised joke and a GPT-4 joke, while trying to make AI jokes sound as if they had been created on the spot.

## Data & Experimental Setup
The performance was recorded for the Belgian TV show “Ze Zeggen Dat.” Three professional Dutch improvisational comedians participated. There were three games, three rounds per game, and nine audience suggestions total. Each comedian performed one human-created and one GPT-4-generated joke per round, yielding 54 jokes evenly split between human and AI sources. A live studio audience of 40 people, unaware that some jokes were AI-generated, rated all jokes after the performance on a four-point scale: Bad (1), Okay (2), Good (3), Amazing (4). This produced 2,160 ratings. Audience members also selected their favorite joke of the whole performance. The resulting dataset is released as `zzd-impro`.

## Results
In pairwise comparisons for the same comedian and suggestion, audience members preferred human jokes 34.6% of the time, GPT-4 jokes 29.7% of the time, and rated both equally 35.7% of the time. Human jokes had a slightly higher mean score: 2.67 versus 2.59. The difference was statistically significant but small: W = 108207.5, p = 0.0317, Cohen’s d = 0.161. Agreement among audience members was low, with Fleiss’ Kappa κ = 0.0858 and Krippendorff’s alpha α = 0.129. GPT-4 nevertheless produced strong peaks: 6 of the top 10 jokes by average rating were GPT-4-generated, and the highest-rated joke scored 3.88 and received 18 of 40 best-joke votes.

## Takeaways
- Live improv is a useful evaluation setting because it matches human and AI time constraints better than curated joke datasets.
- GPT-4 did not clearly beat professional comedians, but it was close enough to be practically competitive.
- Best-of-N human selection and comedian delivery can turn GPT-4 into a strong creative collaborator.
- Humor evaluation remains noisy: low agreement means aggregate numbers should be treated cautiously.
- Builders of humor systems should evaluate performed jokes, not only written text, when delivery is part of the intended use.

## Limitations & Caveats
The study uses one live performance, 40 audience members, three comedians, and Dutch-language humor only. The four-point scale is positively skewed. AI jokes were filtered by an assistant and comedians and sometimes adapted before delivery, so the results evaluate a human-AI performance pipeline rather than raw GPT-4 output. Order randomization was imperfect because GPT-4 generation introduced delays.
