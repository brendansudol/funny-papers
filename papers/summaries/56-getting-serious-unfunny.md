# Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models

**Zachary Horvitz, Jingru Chen, Rahul Aditya, Harshvardhan Srivastava, Robert West, Zhou Yu, Kathleen McKeown** — ACL 2024 · Guide entry #56 (Part 8 - Datasets & Shared Tasks)

[paper page](https://arxiv.org/abs/2403.00794) · [local PDF](../pdfs/56-getting-serious-unfunny.pdf) · [full markdown](../md/56-getting-serious-unfunny/56-getting-serious-unfunny.md) · [extract](../extracts/56-getting-serious-unfunny.json) · [dataset: Getting Serious with LLMs (unfun pairs)](../../data/getting-serious/) · [dataset: Unfun.me database dumps](../../data/unfun-me/)

## TL;DR
The paper tests whether LLMs can create aligned humor/non-humor datasets by editing jokes to remove the humor, rather than trying to write jokes from scratch. GPT-4 is the best synthetic Unfun generator: classifiers trained on its unfuns reach 76.5 (0.2) with MISTRAL and 69.9 (0.5) with ROBERTA, only ΔMistral = -3.8% and ΔRoBERTa = -2.8% below human-edited Unfun training data.

## Problem & Motivation
Humor detection remains difficult partly because datasets rarely pair a humorous text with a closely matched non-humorous counterpart. Human-authored aligned datasets such as Unfun are useful but limited in size and scope. The authors exploit an asymmetry: LLMs may be weak joke writers but still good at making an existing joke serious.

## Approach
The main method prompts LLMs with few-shot examples of humorous text mapped to serious text, asking them to “unfun” new jokes while preserving wording where possible. The paper also tests the reverse direction, editing serious headlines into satire, to compare unfunning with humor generation. A lightweight ROBERTA-SWAP baseline replaces k = 3 surprising low-probability tokens with RoBERTa’s highest-probability alternatives. For English-Hindi tweets, GPT-4 generates unfuns and then filters outputs it still classifies as humorous.

## Data & Experimental Setup
For English satire, the authors use the February 2, 2023 Unfun database backup: 11,831 valid pairs, with a high-quality subset of 867 pairs split into prompt, dev, and test shards. After filtering to one unfun per satire headline, they use 3,882 training unfuns, 186 dev unfuns, and 375 test unfuns, plus corresponding satirical headlines and 3,882 real news headlines as a baseline. Models evaluated include GPT-4, GPT-3.5-TURBO, MISTRAL-7B, MISTRAL-7B-INSTRUCT, ROBERTA-BASE, ROBERTA-SWAP, and HING-ROBERTA. Human evaluation used 10 native-English-speaking university students for Unfun and three bilingual Hindi-English annotators for English-Hindi.

## Results
On Unfun automatic evaluation, Human Players remain best overall at 80.3 (0.5) MISTRAL accuracy and 72.7 (0.4) ROBERTA accuracy. GPT-4 is the best synthetic unfun source, with 76.5 (0.2) and 69.9 (0.5), beating the real-news baseline of 66.3 (0.2) and 64.1 (0.2). In human evaluation, GPT-3.5 and GPT-4 unfuns were rated real 51% and 49% of the time, versus 33% for Human Players, while being similarly unfunny. Humor generation was weaker: The Onion reached 68% / 24% Slightly Funny / Funny, compared with GPT-3.5 at 54% / 8% and GPT-4 at 45% / 10%. For English-Hindi tweets, GPT-4 unfuns had Humor 16.0% and Coherence 93.6%; GPT-4 filtering reduced Humor to 3.6% with Coherence 89.3%. Classifiers trained only on the original English-Hindi dataset reached just 22.6 (3.7) on human-vetted unfuns; using 50% synthetic unfuns raised this to 57.7 (6.0) but lowered original-dataset balanced accuracy from 67.9 (0.9) to 62.1 (0.6).

## Takeaways
- Editing humor away is currently more reliable than generating humor.
- Aligned synthetic unfuns are much stronger negative examples than unrelated real news headlines.
- Human evaluation matters: LLM unfuns can look more like real news than crowd-worker unfuns.
- Synthetic unfuns can expose brittle humor classifiers that rely on superficial cues.

## Limitations & Caveats
The study covers only English satirical headlines and code-mixed English-Hindi tweets. Humor judgments are subjective: only 48% of previously humorous English-Hindi tweets were rated humorous by the paper’s annotators. Human Unfun players were incentivized to minimize edits, which may disadvantage them in some comparisons. Data contamination is a concern for Unfun, though overlap checks found only small numbers of matches.
