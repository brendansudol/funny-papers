# Grounded Satirical Generation with RAG

**Oona Itkonen, Yuxin Su, Linyao Du, Ona De Gibert** — arXiv:2605.10853 · Guide entry #18 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2605.10853) · [local PDF](../pdfs/18-grounded-satire-rag.pdf) · [full markdown](../md/18-grounded-satire-rag/18-grounded-satire-rag.md) · [extract](../extracts/18-grounded-satire-rag.json)

## TL;DR
This paper presents a RAG pipeline for generating satirical dictionary definitions grounded in current Finnish news from Yle. Human annotators rated the outputs as more political than funny: humor averaged M=1.98, SD=1.06, while political relevance averaged M=2.53, SD=1.55. RAG and topic-based word selection improved political relevance but not humor; LLM judges correlated well with humans on politics, especially Aya-Expanse-8B with ρ=0.826, but poorly on humor.

## Problem & Motivation
The paper targets satire generation, which the authors frame as especially difficult because satire depends on shared social, political, historical, cultural, and regional context. They adopt the Cambridge Dictionary definition of satire as humorous criticism that makes a political point, so they evaluate generated satire on two dimensions: funny and political. The work focuses on the Finnish context and asks whether culturally grounded news retrieval can help LLMs generate better satirical definitions.

## Approach
The proposed pipeline scrapes English-language news from the Finnish broadcaster Yle, filters articles by timestamp and sentiment, identifies current topics, retrieves relevant snippets, and uses an LLM to write satirical dictionary definitions. Articles older than 30 days are not processed further. Sentiment analysis uses NLP-Town/bert-base-multilingual-uncased-sentiment, with the stated goal of filtering overly negative or sensitive news to avoid offensive or disturbing output.

For candidate words, the system embeds articles with paraphrase-multilingual-MiniLM-L12-v2, applies UMAP, and uses BERTopic to cluster news into topics and extract salient keywords. Retrieval embeds articles with all-MiniLM-L6-v2, returns up to 3 snippets per input, filters similarities below 0.1, and includes timestamp, category, and title. Generation uses meta-llama/Meta-Llama-3-8B-Instruct via Ollama, prompted as the editor of a “Satirical Dictionary” and restricted to under 50 words.

## Data & Experimental Setup
For evaluation, the authors generated definitions for 50 words: 25 from news topics and 25 randomly selected English words. Each word received two definitions, one with RAG and one without RAG, yielding 100 definitions. The evaluation news articles were scraped on March 3, 2026.

Six human annotators rated all 100 shuffled definitions blindly. Three annotators were Finnish and three were from other cultural backgrounds. Each definition was scored from 1 to 5 for Q1, “Is it funny?”, and Q2, “Is it political?”. The same rubric was also given to five LLM judges: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, Aya-Expanse-8B, and EuroLLM-9B-Instruct.

## Results
Human ratings showed weak humor performance: funny M=1.98, SD=1.06, with 40% of annotations receiving score 1. Political relevance was higher and more varied: M=2.53, SD=1.55.

Inter-annotator agreement was low for humor and higher for politics: overall Krippendorff’s α was 0.070 for humor and 0.514 for politics. Finnish annotators had α=0.053 for humor and 0.646 for politics; international annotators had α=0.183 for humor and 0.490 for politics. Finnish vs. international ratings showed no statistically significant differences, p>0.1.

Topic-modeled words did not improve humor, p=0.758, but improved political relevance, p<0.001. RAG likewise did not yield a statistically significant humor gain, p=.05, but improved political relevance, p<.001.

For LLM-as-judge, all models correlated poorly with humans on humor. Aya-Expanse-8B was best overall, with humor ρ=0.199* [0.005, 0.373] and political ρ=0.826** [0.758, 0.872]. The next political correlations were Llama-3.1-8B-Instruct at 0.756, Mistral-7B-Instruct-v0.3 at 0.751, Qwen2.5-7B-Instruct at 0.688, and EuroLLM-9B-Instruct at 0.663.

## Takeaways
- Grounding satire in news helps political relevance more than humor.
- Topic-based word selection is useful if the goal is topicality, not necessarily funniness.
- RAG should not be assumed to make generated humor funnier when the retrieved source material is not humorous.
- LLM judges may be usable for political relevance judgments, but not for subjective humor judgments.
- Human evaluation remains necessary and difficult for satire.

## Limitations & Caveats
The pipeline is limited to English-language Yle news in the Finnish context. The authors call for additional languages, additional sources, and alternative evaluation methods. Agreement for humor was very low, and even political agreement fell below commonly used thresholds for strong reliability.
