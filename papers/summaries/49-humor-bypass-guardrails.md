# Using Humor to Bypass Safety Guardrails in Large Language Models

**Pedro Cisneros-Velarde** — LLMSEC 2025 · Guide entry #49 (Part 6 - Safety, Harm & Boundaries)

[paper page](https://aclanthology.org/2025.llmsec-1.3/) · [local PDF](../pdfs/49-humor-bypass-guardrails.pdf) · [full markdown](../md/49-humor-bypass-guardrails/49-humor-bypass-guardrails.md) · [extract](../extracts/49-humor-bypass-guardrails.json)

## TL;DR
This paper introduces a simple humor-based jailbreak: put an unsafe request, unchanged, inside a humorous prompt context. Across JBB, AdvBench, and HEx-PHI, and four open-source LLMs, the original method beats direct injection in 42 out of 48 cases; removing humor or adding too much humor generally makes it worse.

## Problem & Motivation
The paper studies whether humor can be used to bypass LLM safety guardrails. Existing jailbreaks often rely on carefully engineered prompts, model access, auxiliary LLMs, or more complex multi-turn strategies. Here, the author asks whether a fixed, black-box, humorous framing can elicit unsafe responses while leaving the unsafe request verbatim. The broader motivation is both security and humor processing: the paper argues that LLMs may respond to humorous contexts in kind, and that this tendency may interact poorly with safety training.

## Approach
The main method is a fixed single-turn prompt template. It places the unsafe request inside a humorous, whispered context and asks the model to help a subject such as “man,” “chicken,” “I,” or “goat.” The unsafe request is not rewritten. The paper emphasizes this as a key design choice: the attack is agnostic to the content of the unsafe request and does not need another LLM to construct the prompt.

The paper also tests two variants that add more humor. The first is a three-turn knock-knock attack: the first turns set up a joke, and the final turn adds a joke before the original attack prompt. The second removes the preceding knock-knock turns and uses only the joke plus the original prompt. A no-humor ablation removes cues such as whispering, laughter, and explicit humorous wording.

## Data & Experimental Setup
The evaluation uses three unsafe-request datasets: JBB with 100 unsafe requests, AdvBench with 520 unsafe requests, and HEx-PHI with 300 unsafe requests. The paper denotes them D1, D2, and D3. Four models are attacked: `Llama-3.3-70B-Instruct`, `Meta-Llama-3.1-8B-Instruct`, `Mixtral-8x7B-Instruct-v0.1`, and `gemma-3-27b-it`. All experiments use temperature zero. Llama 3.3 70B is also used as an LLM-as-judge to classify responses as safe or unsafe, with instructions to pay attention to unsafe content even in humorous contexts.

## Results
The original humor-based method is more effective than direct injection in 42 out of 48 cases. On Gemma 3 27B, direct injection scores 0.00, 0.19, and 6.33 on D1/D2/D3, while the Chicken humor variant scores 49.00, 56.54, and 52.33. On Llama 3.1 8B, direct injection scores 5.00, 2.50, and 7.00; the best main-method scores are 33.00 on D1, 31.73 on D2, and 44.00 on D3.

The ablation supports the role of humor: removing humorous context does not increase effectiveness in 46 out of 48 cases. Adding more humor does not generally help. The knock-knock attack improves over the original in only 4 out of 84 cases, and the joke-addition single-turn variant improves in only 9 out of 84 cases.

## Takeaways
- Humor can be a practical attack surface for LLM safety guardrails.
- A simple fixed template can work without rewriting the unsafe request or using another LLM.
- Evaluations of safety should include humorous and playful unsafe contexts, not just direct requests.
- More humor is not necessarily stronger; the paper argues that excessive humor may distract the model from fulfilling the unsafe request.
- The authors hypothesize mismatched generalization: safety training may not generalize well to humorous unsafe prompting.

## Limitations & Caveats
The experiments use temperature zero, and the paper notes that results may be sensitive to this setting. The study covers four open-source models and does not test proprietary LLMs or reasoning models. The stated goal is to demonstrate effectiveness, not to compare with prior jailbreaks or achieve state-of-the-art performance.
