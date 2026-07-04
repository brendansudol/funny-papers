# Computational Humor Modeling: A Survey on the State of the Art

**Jens Lemmens, Victor De Marez** — ACM Computing Surveys 58(7):177 · Guide entry #62 (Part 9 - Surveys & Resources)

[paper page](https://dl.acm.org/doi/10.1145/3778357) · [local PDF](../pdfs/62-humor-modeling-survey.pdf) · [full markdown](../md/62-humor-modeling-survey/62-humor-modeling-survey.md) · [extract](../extracts/62-humor-modeling-survey.json)

## TL;DR
This is a broad survey of recent computational humor modeling across datasets, shared tasks, detection, generation, annotation/evaluation, and explainability. Its central finding is that the field has broadened beyond English text, but remains skewed toward joke datasets and lacks a shared evaluation framework for humor generation.

## Problem & Motivation
Humor is framed as an AI-complete problem because it requires world knowledge, semantic reasoning, linguistic understanding, and sensitivity to social context. Earlier surveys identified recurring gaps: weak evaluation methods, limited use of humor theory, overreliance on English jokes, and insufficient attention to multimodality. This paper asks how those gaps have changed in recent work, focusing on methods since 2022 and datasets/shared tasks from January 2020 onward.

## Approach
The authors search Google Scholar, Semantic Scholar, ACL Anthology, ACM Computing Surveys, IEEE Xplore, and the European Journal of Humor Research using humor- and AI-related keywords, plus backward and forward citation search. A decision tree filters for recent computational humor modeling papers, with limited exceptions for non-peer-reviewed work that provides patented systems or shared code/data with novel experiments. The survey classifies work by task, modality, language, humor genre, model type, evaluation, and relationship to humor theory.

## Data & Experimental Setup
The paper analyzes 39 humor datasets from 2020–2024 and groups them into jokes, performance humor, and conversational humor. It also reviews shared tasks including SemEval-2020 Task 7, HaHackathon (SemEval-2021 Task 7), HAHA@IberLEF 2021, HUHU@IberLEF 2023, CLEF 2024 JOKER, and MuSe 2024. Modalities include text, image, video, and audio; languages include English, Spanish, Chinese, French, Hindi, Portuguese, Arabic, Telugu, German, Russian, English-Urdu, English-Hindi, Japanese, and multilingual settings.

## Results
Dataset coverage is imbalanced: 26 out of 39 datasets contain jokes, while only 2 of the 39 contain conversational humor. This contrasts with cited daily humor proportions of 70% conversational humor, 17% performance humor, and 11% jokes. Multimodality has improved: 20 out of 39 datasets are multimodal. Shared-task results illustrate both progress and difficulty: the SemEval-2020 Task 7 winner achieved RMSE 0.497 and accuracy 0.674, while HaHackathon top-10 systems exceeded F1-score>0.96 for humor intention detection but only reached around 0.50–0.55 RMSE for humor rating and 0.62–0.63 F1-score for offensiveness. In the New Yorker Caption Contest benchmark, few-shot GPT-4 reached 85% caption matching accuracy and 73% caption ranking accuracy, below human figures of 94% and 87%.

## Takeaways
- Builders should not treat “humor” as a single text classification problem: genre, modality, culture, and task change the problem.
- Humor generation evaluation is not comparable across papers; the authors argue for multidimensional evaluation of mechanism diversity, appropriateness, and originality.
- LLMs are central to generation, but results are prompt-dependent and originality remains a problem.
- Detection remains methodologically diverse; older feature-based or hybrid models can still be useful, especially for testing humor theories.
- Explainability work often reveals reliance on superficial cues such as punctuation, formatting, or offensiveness rather than robust humor understanding.

## Limitations & Caveats
The survey excludes work focused specifically on irony and sarcasm, limits model papers mostly to 2022 onward, and only selectively includes non-peer-reviewed work. Its conclusions are therefore a scoped snapshot of a fast-moving field rather than an exhaustive history of computational humor.
