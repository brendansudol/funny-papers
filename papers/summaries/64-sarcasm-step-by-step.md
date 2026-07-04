# Is Sarcasm Detection A Step-by-Step Reasoning Process in Large Language Models?

**Ben Yao, Yazhou Zhang, Qiuchi Li, Jing Qin** — AAAI 2025 · Guide entry #64 (Adjacent - Sarcasm & Humor Styles)

[paper page](https://arxiv.org/abs/2407.12725) · [local PDF](../pdfs/64-sarcasm-step-by-step.pdf) · [full markdown](../md/64-sarcasm-step-by-step/64-sarcasm-step-by-step.md) · [extract](../extracts/64-sarcasm-step-by-step.json)

## TL;DR
This paper asks whether LLM sarcasm detection should be treated as a step-by-step reasoning problem. It proposes SarcasmCue, a framework with two sequential cue methods and two non-sequential cue methods; the strongest result is that non-sequential ToC greatly helps smaller open-source LLMs, reaching 65.24 Avg. of F1 on Llama 3-8B and 68.39 on Qwen 2-7B.

## Problem & Motivation
Chain-of-thought prompting improves LLMs on tasks such as mathematical and commonsense reasoning, where intermediate steps are natural. The paper argues that sarcasm is different: sarcasm judgment often combines linguistic, contextual, and emotional cues holistically, and sarcasm does not necessarily follow formal logical structures. The explicit research question is: “Is human sarcasm detection a step-by-step reasoning process?”

## Approach
SarcasmCue contains four cue-based methods. Chain of Contradiction (CoC) is linear: identify surface sentiment, infer true intention, and classify sarcasm when they do not align. Graph of Cues (GoC) builds a graph over ten predefined cues: four linguistic cues, three contextual cues, and three emotional cues; an LLM evaluator selects useful cues through voting until it has sufficient confidence. Bagging of Cues (BoC) is non-sequential: it samples multiple cue subsets, asks the LLM to predict from each subset, and aggregates by majority vote. Tensor of Cues (ToC) is also non-sequential: it extracts linguistic, contextual, and emotional cues, fuses their hidden-layer embeddings with a tensor product, prepends the fused representation to the prompt, freezes the LLM, and trains only the fully connected layers.

## Data & Experimental Setup
The main sarcasm experiments use IAC-V1, IAC-V2, SemEval 2018 Task 3, and MUStARD. Table 5 reports train/dev/test sizes of 1,595/80/320 for IAC-V1, 5,216/262/1,042 for IAC-V2, 3,634/200/784 for SemEval 2018, and 552/-/138 for MUStARD. The paper evaluates GPT-4o, Claude 3.5 Sonnet, Llama 3-8B, and Qwen 2-7B, with additional scale experiments on Qwen 2-1.5B, Qwen 2-72B, and Llama 3-70B. Metrics are Accuracy and Macro-F1; the reported tables give mean performance over 5 runs.

## Results
On GPT-4o, CoC reaches 70.73 Avg. of F1, compared with the best baseline ToT at 67.88, reported as a 4.2% improvement. On Claude 3.5 Sonnet, CoC reaches 74.74, beating the best baseline IO at 73.26 by 2.0%. On Llama 3-8B, ToC reaches 65.24, beating ToT at 50.31 by 29.7%. On Qwen 2-7B, ToC reaches 68.39, beating IO at 43.22 by 58.2%. For humor detection, using GPT-4o, BoC obtains the best Avg. of F1 at 67.48 across CMMA and UR-FUNNY-V2.

## Takeaways
- Cue design matters: predefined sarcasm cues outperform freestyle prompting baselines.
- Stronger LLMs benefit from CoC and GoC, but smaller LLMs benefit most from ToC.
- Sarcasm detection is not clearly proven to be step-by-step; the smaller-model results support non-sequential cue fusion.
- For builders of humor systems, testing both sequential reasoning prompts and non-sequential cue aggregation is important.
- Ablations show linguistic, contextual, and emotional cues all contribute.

## Limitations & Caveats
The paper notes that SarcasmCue uses only three cue types and may miss other useful signals. ToC requires model-internal access and supervised training, so it is not implemented for GPT-4o or Claude 3.5 Sonnet. The MUStARD experiments use only textual information, and the case study says highly ambiguous examples may need extra context or combined methods.
