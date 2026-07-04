# Let’s Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Creative Humor Generation

**Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, Pan Zhou** — CVPR 2024 · Guide entry #11 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2312.02439) · [local PDF](../pdfs/11-clot-leap-of-thought.pdf) · [full markdown](../md/11-clot-leap-of-thought/11-clot-leap-of-thought.md) · [extract](../extracts/11-clot-leap-of-thought.json) · [dataset: Oogiri-GO](../../data/oogiri-go/)

## TL;DR
The paper studies “Leap-of-Thought” (LoT)—non-sequential associative thinking—through Oogiri-style humor generation, where models must produce unexpected and funny responses to images, text, or both. It introduces Oogiri-GO, a 134,148-sample multilingual/multimodal Oogiri dataset, and proposes Creative Leap-of-Thought (CLoT). The main result is that Qwen-VL+CLoT improves over Qwen-VL by Avg. 42.7 (+9.1) on IT2T, 40.5 (+10.4) on I2T, and 38.5 (+8.2) on T2T.

## Problem & Motivation
Chain-of-Thought helps LLMs reason step by step, but the authors argue that creative problem solving often needs abrupt associative jumps rather than sequential reasoning. Oogiri is used as the testbed because players respond to images, text, or image-text prompts with surprising humorous answers. The paper asks whether current LLMs have this LoT ability and whether training can improve it.

## Approach
CLoT has two stages. First, Associable Instruction Tuning converts Oogiri-GO into generation, selection, and ranking instructions; some generation prompts include a noun condition from the target response, while others leave the condition empty to encourage freer association. Second, Explorative Self-Refinement asks the tuned model to generate candidates under weakly-associated conditions sampled from a noun set or left empty, rank them, select the best, and retrain on selected high-quality generated data. At inference, CLoT generates multiple candidates, ranks them, and selects from the top-2.

## Data & Experimental Setup
Oogiri-GO contains 89,744 I2T, 34,072 T2T, and 10,332 IT2T samples in English, Chinese, and Japanese; 95% are used for training and 5% for testing. 77.95% have human preference annotations from likes. Raw data came from Bokete, Twitter, and Weibo, then underwent Qwen-VL safety screening and manual screening. Evaluation uses choice questions (2T1, 3T1, 4T1, 5T2) with accuracy, ranking questions with NDCG, a user study with 154 valid questionnaires and 2772 votes, plus CGG and DAT creativity tests.

## Results
On multilingual multimodal Oogiri, Qwen-VL+AIT already improves Qwen-VL, but Qwen-VL+CLoT is stronger: Avg. 42.7 (+9.1) on IT2T, 40.5 (+10.4) on I2T, and 38.5 (+8.2) on T2T. With CogVLM-17B, CLoT reaches I2T Avg. 51.6 (+21.7) and T2T Avg. 48.3 (+16.4). On English T2T, CogVLM-17B+CLoT scores Avg. 44.2 and Qwen-VL+CLoT 43.4, above GPT-3.5 at 36.0 and GPT-4 at 32.0. In the user study, Qwen-VL+CLoT receives 42.0% average votes, versus GPT4v at 16.4%, Qwen-VL+AIT at 15.0%, Qwen-VL at 9.7%, Qwen-VL+CoT at 8.9%, and MiniGPT-v2 at 8.0%.

## Takeaways
- Prompting alone, including CoT, CoT-SC, and “let’s think outside the box,” is not enough to elicit strong LoT behavior.
- Training models to both generate and discriminate creative responses matters for humor systems.
- Weakly-associated conditions are central: they push models toward remote associations rather than literal captions.
- Oogiri-style evaluation combines generation, selection, ranking, and human preference, making it richer than only asking for jokes.

## Limitations & Caveats
Humor is subjective, and translations may not preserve all cultural meaning. Oogiri-GO lacks English IT2T data because that format is rare online and harder to create. Multi-round self-refinement did not significantly improve results without more diverse creative data or condition nouns, and LoRA-style tuning may cause partial forgetting.
