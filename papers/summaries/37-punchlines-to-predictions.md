# From Punchlines to Predictions: A Metric to Assess LLM Performance in Identifying Humor in Stand-Up Comedy

**Adrianna Romanowski, Pedro H. V. Valois, Kazuhiro Fukui** — CMCL 2025 · Guide entry #37 (Part 4 - Evaluation Methodology)

[paper page](https://arxiv.org/abs/2504.09049) · [local PDF](../pdfs/37-punchlines-to-predictions.pdf) · [full markdown](../md/37-punchlines-to-predictions/37-punchlines-to-predictions.md) · [extract](../extracts/37-punchlines-to-predictions.json)

## TL;DR
This paper proposes a metric for scoring how well LLMs identify humorous punchlines in stand-up comedy transcripts. The metric compares model-extracted quotes with laughter-derived ground truth using fuzzy string matching, sentence embeddings, or subspace similarity. On 51 Open Mic transcripts, the best reported embedding score is DeepSeek-V3 at 51.6%, while humans score 40.7% under the fuzzy module.

## Problem & Motivation
The paper argues that humor detection remains difficult for AI because humor depends on subjectivity, context, irony, sarcasm, and cultural nuance. Prior humor-detection work often uses binary classification on standalone jokes or other short humorous texts, but the authors focus on stand-up comedy because it contains narrative set-ups and punchlines with immediate audience feedback. Their goal is not just to classify a sentence as funny, but to evaluate whether an LLM can extract the lines from a transcript that correspond to moments where an audience laughed.

## Approach
The proposed humor detection metric prompts a model to extract humorous quotes from a stand-up transcript, then compares the model’s list with ground-truth quotes. Ground truth is created from audio and transcript data: a laughter detection model extracts laughter timestamps, and forced alignment maps transcript sentences to laughter time frames.

The metric has three alternative scoring modules. The fuzzy string matching module uses Levenshtein-based text similarity and averages the best match for each ground-truth quote, with an overgeneration penalty using alpha = 0.1. The vector embedding module uses Sentence Transformers to compare semantic similarity rather than exact wording. The subspace similarity module applies PCA to sets of feature vectors from multiple prompt variations and scores alignment between model-output and ground-truth subspaces.

## Data & Experimental Setup
The experiments use the Open Mic dataset, which provides stand-up performance audio and transcripts. The authors randomly selected 51 transcripts with an average word length of 270 words and length of 106 seconds. Models were prompted in a zero-shot setting, primarily with: “Extract the key humorous lines and punchlines for this stand-up comedy transcript...”

The evaluated models include Gemma 2b-it, Gemma 2 9b-it, Phi 3-Mini 3.8b-it, Llama 3.1 8B Instruct, ChatGPT-4o, Claude 3.5 Sonnet, and DeepSeek-V3. The paper also studies prompt engineering and runs a human evaluation with 11 naive raters on 6 transcripts.

## Results
Table 1 shows that DeepSeek-V3 has the highest embedding score, 51.6%, ahead of Claude 3.5 Sonnet at 46.9%. ChatGPT-4o has the highest fuzzy score among the leading models, 48.9%, which is 2.9 points above DeepSeek-V3’s 46% fuzzy score, but ChatGPT-4o drops to 25.4% on the embedding module. The highest subspace score is Gemma 2b-it at 55.7%.

Humans score 40.7% against the ground truth using fuzzy string matching, so ChatGPT-4o, Claude 3.5 Sonnet, and DeepSeek-V3 outperform humans under that metric. Human-human agreement is much higher: Percentage Agreement averages 86.7% across the 6 transcripts. Human-machine agreement averages 59.9%, with Gemma 2b-instruct and Gemma 2 9b-instruct highest at 68.8%, and ChatGPT-4o lowest at 28.7%.

Prompt engineering mostly fails to improve results. For Gemma 2b-instruct, Prompt 2 reaches 31.2% versus the original 30.1%, but personas, humor-type preferences, comedian personas, and demographic prompts generally do not help.

## Takeaways
- Stand-up humor detection remains difficult even for leading LLMs; the best reported scores are only around the 50% range.
- Different scoring modules reveal different behavior: lexical matching and semantic similarity can disagree strongly.
- High metric performance does not imply high agreement with human raters, as shown by ChatGPT-4o.
- Prompt personas and demographic framing should not be assumed to improve humor detection.
- Laughter-derived ground truth gives an audience-based target, but it is still noisy and performance-specific.

## Limitations & Caveats
The ground truth assumes that the sentence before laughter is the humorous quote, which can misattribute jokes. The laughter detector uses a minimum laughter length of 0.2 seconds and probability threshold of 0.5, and it does not measure laughter magnitude. The evaluation is text-based, so it omits tone, timing, delivery, and body language. Human raters were all aged 20 to 30 years, which may limit diversity of humor interpretations.
