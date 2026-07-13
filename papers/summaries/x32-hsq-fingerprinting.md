# Fingerprinting LLMs through Survey Item Factor Correlation: A Case Study on Humor Style Questionnaire

**Simon Münker** — EMNLP 2025 · Guide entry Adjacent (construct-validity caution) (Adjacent - Sarcasm & Humor Styles)

[paper page](https://aclanthology.org/2025.emnlp-main.13/) · [local PDF](../pdfs/x32-hsq-fingerprinting.pdf) · [full markdown](../md/x32-hsq-fingerprinting/x32-hsq-fingerprinting.md) · [extract](../extracts/x32-hsq-fingerprinting.json)

## TL;DR
The paper introduces a correlation-based “fingerprint” for comparing how LLMs and humans organize psychological questionnaire items, using the 32-item Humor Style Questionnaire as a case study. The central result is that human subsamples are highly consistent with one another, with cosine similarities from 0.776 to 0.891 (averaging 0.823), while LLM-human similarities are near zero, averaging only 0.026.

## Problem & Motivation
LLMs are increasingly used with psychological instruments, but surface-level plausible answers do not show whether models represent psychological constructs in human-like ways. The paper argues that population-level factor covariance patterns may be more stable and revealing than individual raw scores. Humor styles are used as a low-risk psychological domain with an established four-factor structure: Affiliative, Self-enhancing, Aggressive, and Self-defeating humor.

## Approach
For each model and baseline, the author collects HSQ responses and computes a 32 × 32 Pearson item-correlation matrix. The upper triangle of each matrix, excluding the diagonal, becomes a 496-element fingerprint. Fingerprints are compared using cosine similarity. The paper also runs exploratory graph analysis with graphical LASSO, EBIC model selection, and Walktrap community detection, plus Cronbach’s alpha for the four HSQ dimensions.

## Data & Experimental Setup
The main experiment evaluates six open-weight LLMs: Llama 3.1 8B, Llama 3.3 70B, Mistral 7B, Mistral 123B, Qwen 2.5 7B, and Qwen 2.5 72B. Each model produces 1000 independent 32-item HSQ response sets. The prompt asks for a 1–5 Likert response only, and the main setting includes a five-question sliding window of prior questions and answers. Baselines include Random 1000 synthetic response sets, Human Items 1,000 synthetic response sets preserving item-level human means and standard deviations, and Human Full with 1071 human HSQ responses from Martin et al. (2003). An ablation removes the context window.

## Results
The strongest contrast is human consistency versus LLM divergence. Ten human subsamples of n = 100 have similarities from 0.776 to 0.891, averaging 0.823. Human-to-LLM similarity averages only 0.026; against Human Full, LLMs average 0.049, with the best single score being Qwen 2.5 7B at 0.164. Within-family similarities in the context setting are modest: Mistral 7B/123B is 0.044 and Qwen 2.5 7B/72B is 0.034. Some cross-family pairs are higher, including Qwen 2.5 7B with Llama 3.3 70B at 0.085 and Qwen 2.5 72B with Llama 3.1 8B at 0.082. Removing context sharply reduces alignment: Qwen 2.5 7B to Human Full falls from 0.164 to 0.004, and the highest no-context Human Full similarity is only 0.011. EGA recovers the human four-factor structure, but LLMs produce 2-8 communities that do not align clearly with HSQ theory. Cronbach’s alpha is high for Human Full (0.841, 0.820, 0.790, 0.815) but substantially lower for all LLMs.

## Takeaways
- Plausible questionnaire answers are not evidence of human-like psychological construct representation.
- Correlation fingerprints can reveal representational gaps that raw scores or output quality may hide.
- Context helps LLMs produce more coherent questionnaire patterns, but not enough to recover human HSQ structure.
- Bigger models are not consistently more reliable or more human-like on this task.
- Anyone using LLMs as human simulacra in humor or psychology studies should validate construct structure, not just answer plausibility.

## Limitations & Caveats
The models may have seen HSQ items during training. Results use one psychological instrument and may not generalize beyond humor styles. Prompting, generation settings, local implementations, and the chosen sliding-window context strategy may affect the fingerprints. The study also excludes OpenAI and Anthropic models.
