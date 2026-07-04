# Who’s Laughing Now? An Overview of Computational Humour Generation and Explanation

**Tyler Loakman, William Thorne, Chenghua Lin** — INLG 2025 · Guide entry #58 (Part 9 - Surveys & Resources)

[paper page](https://arxiv.org/abs/2509.21175) · [local PDF](../pdfs/58-whos-laughing-now.pdf) · [full markdown](../md/58-whos-laughing-now/58-whos-laughing-now.md) · [extract](../extracts/58-whos-laughing-now.json)

## TL;DR
This paper surveys computational humour generation and explanation, arguing that humour is an underused but demanding test of LLM verbal reasoning, pragmatics, cultural knowledge, and phonetic understanding. Its central conclusion is that work beyond puns remains sparse and that current systems still fall short of human capabilities, especially for heterographic puns, long-form incongruity, topical jokes, and multimodal humour.

## Problem & Motivation
The authors argue that humour processing should matter more in NLP because humour requires exactly the kinds of reasoning that many current benchmarks underemphasize: common sense, cultural reference, pragmatic inference, phonetics, and the ability to infer what is not explicitly said. They contrast this with recent benchmark suites used for systems such as Kimi K2 and Grok4, where nine cited benchmarks focus on STEM or structured reasoning, while only Tau2 touches communicative competence. Humour is also subjective and ethically ambiguous, so it raises practical issues for generation and explanation systems.

## Approach
The paper is a literature survey organized around two generative tasks: humour generation and humour explanation. Generation is divided into pun generation—homographic, heterographic, and combined approaches—and non-pun humour such as set-up/punchline jokes, satirical headlines, hyperbole, and tongue twisters. Explanation is divided into classification-based explanation, such as pun interpretation or humour-technique classification, and natural language explanation for jokes, cartoons, and memes. The paper grounds the discussion in humour theories, especially incongruity and benign violation, while also summarizing relief and superiority theories.

## Data & Experimental Setup
The paper runs no new experiments. It reviews prior datasets and tasks, including ChinesePun, CUP, SemEval-2017 Task 7 puns, CLEF 2024 JOKER Task 2, the New Yorker Cartoon Caption Contest, MEMECAP with 6.3K memes, MeSum with 13K+ memes, MemeIntent with 950 samples, MEMEMQA, the Internet Meme Knowledge Graph with 2 million edges, and MultiBully. It also uses joke examples from Loakman et al. (2025b), covering homographic puns, heterographic puns, non-topical jokes, and topical jokes.

## Results
The survey reports several key numbers from prior work. AMBiPUN achieved a 52% success rate in human evaluation for homographic pun generation. CLEF 2024 JOKER Task 2 received 54 submissions for humour classification by genre and technique. Baluja (2025) found that giving Gemini 1.5 speech audio alongside text led to approximately a 2.5% to 4% improvement in joke-explanation performance. For New Yorker visual jokes, access to visual information improved explanations in 84.7% of cases by human preference judgments, but human-authored explanations were still preferred in 68% of instances over model explanations.

## Takeaways
- Treat humour explanation as a stronger test of understanding than detection alone, because coherent explanation is less likely to arise by accident.
- Do not evaluate humour only on puns: topical, contextual, multimodal, and long-form humour expose different weaknesses.
- Phonetic information matters; text-only LLMs struggle with heterographic puns and other pronunciation-dependent humour.
- Multimodal prompting can help, but human explanations remain better in the cited visual-joke results.
- Builders of humour systems should consider demographic awareness, human-in-the-loop workshopping, and intent-aware explanation rather than unrestricted joke generation.

## Limitations & Caveats
The authors state that the paper prioritizes breadth over detailed technical analysis of each surveyed method. They also note that some relevant work may have been missed. The survey does not deeply cover automatic metrics, human evaluation paradigms, available datasets, or humour detection approaches, and it provides no new empirical benchmark or model evaluation.
