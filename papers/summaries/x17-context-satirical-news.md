# Context-Driven Satirical Headline Generation

**Zachary Horvitz, Nam Do, Michael L. Littman** — Fig-Lang 2020 · Guide entry Part 2 (learned-generation anchor) (Part 2 - Generating Jokes)

[paper page](https://aclanthology.org/2020.figlang-1.5/) · [local PDF](../pdfs/x17-context-satirical-news.pdf) · [full markdown](../md/x17-context-satirical-news/x17-context-satirical-news.md) · [extract](../extracts/x17-context-satirical-news.json)

## TL;DR
The paper builds a context-driven system for generating The Onion-style satirical headlines by pairing real satirical headlines with retrieved real-world context from CNN and Wikipedia, then fine-tuning BERTSum summarization models to generate the headline from that context. In human evaluation, the best generated system was D-Context with 9.4% of headlines rated funny, outperforming Satire GPT-2 at 6.9% and News GPT-2 at 2.4%, though still far below Onion (Gold) at 38.2%.

## Problem & Motivation
The authors argue that satirical news depends on more than surface wordplay: understanding a headline often requires knowing entities, events, relationships, and cultural context. Prior computational humor work emphasized puns, sarcasm, or small curated headline-editing datasets. This paper instead treats satire generation as a conditional generation problem: given a real-world context, generate a humorous satirical headline.

## Approach
For each Onion headline, the system retrieves the first sentence of the original satirical article, extracts named entities with SpaCy NER, queries CNN.com for contemporaneous news and Wikipedia for entity paragraphs, ranks the retrieved material, and builds a synthetic context document. The generation task is then to map this approximated context to the original satirical headline. The authors fine-tune BERTSum, a pretrained abstractive summarization architecture, in three variants: Encoder-Weighted-Context (E-Context), Abstractive-Context (A-Context), and Decoder-Weighted-Context (D-Context). They compare against context-free GPT-2 large baselines trained on satirical headlines or real news headlines.

## Data & Experimental Setup
The introduced dataset contains more than 15K satirical headlines paired with ranked contextual information; the paper states that documents were retrieved for 15199 Onion headlines. Synthetic documents used the first four sentences from the top two CNN articles and the top three remaining ranked documents, trimmed to approximately 512 tokens. Satire models used an 85-15 train-test split. GPT-2 baselines were fine-tuned on the paper’s satire corpus and on roughly 10K real news headlines from the Unfun.me corpus; another Unfun.me model trained on 2758 unfunned-satirical pairs was excluded from the main table.

Human annotators on Amazon Mechanical Turk judged 750 headlines per model for coherence, whether they sounded like The Onion, and funniness, with three annotations per headline and majority labels. Retrieval quality was separately evaluated by 62 annotators over 1500 headlines.

## Results
Onion (Gold) scored 99.5% coherence, 86.6% Onion, 38.2% funny, and 38.4% F|C. Among generated systems, D-Context had the best Funny score at 9.4%, compared with E-Context at 8.7%, A-Context at 8.8 %, Satire GPT-2 at 6.9%, and News GPT-2 at 2.4%. E-Context had the highest F|C among generated systems at 10.8%, slightly above D-Context at 10.4% and A-Context at 10.3%.

The retrieval evaluation found that for the top five retrieved documents, at least one annotator saw a relevant document for 99.0% of headlines, and a majority did so for 80.7%. In normalized Jaccard context-similarity, the context models scored D-Context 6.2, E-Context 6.7, and A-Context 6.0, above Onion at 5.0 but below the pretrained Summarizer at 9.9.

## Takeaways
- Conditioning on retrieved real-world context improved human-rated funniness over context-free satire GPT-2 in this setup.
- Summarization architectures are useful for topical humor because they encode source context before decoding a headline.
- Human funny rates remain low, so success is relative rather than human-level.
- Retrieval quality matters: the pipeline is mostly useful but not uniformly relevant.
- The generated headlines often mimic satirical news register, introduce incongruity, and reuse contextual entities.

## Limitations & Caveats
The best model’s 9.4% funny score is far below Onion’s 38.2%. The retrieval pipeline is imperfect, and the authors note that Transformer latent spaces are difficult to analyze. Sensitivity analysis suggests stronger dependence on entity changes than on adjectives or negations. The excluded Unfun.me model produced only 2.5% funny generations and 64% duplicates, indicating data size and overlap problems.
