# Jokes or Gibberish? Humor Retention in Translation with Neural Machine Translation vs. Large Language Model

**Mondheera Pituxcoosuvarn, Yohei Murakami** — Digital (MDPI) 5(4):49 · Guide entry #55 (Part 7 - Cross-Cultural & Translation)

[paper page](https://www.mdpi.com/2673-6470/5/4/49) · [local PDF](../pdfs/55-jokes-or-gibberish.pdf) · [full markdown](../md/55-jokes-or-gibberish/55-jokes-or-gibberish.md) · [extract](../extracts/55-jokes-or-gibberish.json)

## TL;DR
This paper evaluates humor retention when translating 850 English jokes into Thai using Google Translate and GPT-4o with three prompting strategies. The main result is that the explanation-enhanced prompt, GPT-Ex, achieved the highest joke retention rate at 62.94%, significantly above MT’s 50.12% (ΔJ = +12.82 percentage points, p = 9.40 × 10^{-11}); baseline GPT was worse than MT at 41.06%.

## Problem & Motivation
Humor translation is difficult because jokes often depend on wordplay, double meanings, cultural context, idioms, and pragmatic cues. Standard translation metrics such as BLEU and COMET do not directly measure whether a translated joke is still recognized and understood as funny. The study therefore asks how well MT, GPT, GPT-P, and GPT-Ex preserve humor in English-to-Thai translation, and what kinds of humor-loss patterns appear in machine-translated jokes.

## Approach
The authors compare four translation approaches. MT is Google Translate via the deep_translator Python package. Baseline GPT uses GPT-4o with a professional-translator prompt. GPT-P adds humor-preservation instructions, telling the model to adapt wordplay, puns, and cultural references naturally for Thai speakers without explaining the joke. GPT-Ex uses the same humor-preservation strategy but adds an explanation in parentheses when needed to clarify wordplay, double meanings, or cultural references.

## Data & Experimental Setup
The study uses 850 English jokes randomly selected from the Humorous Jokes Dataset on Kaggle, drawn from online sources including Twitter, Textfiles.com, FunnyShortJokes.com, LaughFactory.com, and OneLineFun.com. Jokes were manually assigned multi-label joke types: Wordplay (n = 413), Idioms (n = 24), Cultural Reference (n = 203), Irony (n = 224), Dark (n = 177), Absurd (n = 28), and Other (n = 47). Three Thai-native annotators labeled each translation as J, N, X, or XJ. Final labels used majority vote, with consensus or blinded adjudication for 1–1–1 splits. Reported agreement was Fleiss’κ = 0.6536 and 78.57% simple agreement.

## Results
Overall retention was GPT-Ex 62.94%, GPT-P 54.12%, MT 50.12%, and GPT 41.06%. Against MT, baseline GPT significantly decreased retention by −9.06 percentage points (127:204, p = 1.19 × 10^{-8}). GPT-P was +4.00 percentage points over MT but not significant at α = 0.05 (206:172, p = 0.0649). GPT-Ex significantly beat MT by +12.82 percentage points (270:161, p = 9.40 × 10^{-11}). By joke type, GPT-Ex gains over MT were significant for Wordplay, Cultural Reference, Irony, and Dark Humor. Wordplay improved from GPT’s 32.20% to GPT-Ex’s 59.81% (+27.61 percentage points), with MT vs. GPT-Ex p = 3.5 × 10^{-8}.

## Takeaways
- Humor-aware prompting helps, but explanations helped most in this setup.
- Baseline GPT-4o translation can remove joke structure and underperform Google Translate.
- Anyone evaluating humor translation should use human labels for joke recognition and comprehension, not only general translation metrics.
- Small joke-type strata can show large numerical effects that are not statistically reliable.

## Limitations & Caveats
The annotation did not include explicit joke-difficulty ratings or calibrated difficulty examples. Idioms and Absurd Humor had small sample sizes, so those stratified findings are exploratory. The study is limited to English-to-Thai text jokes, and the source dataset may contain offensive content.
