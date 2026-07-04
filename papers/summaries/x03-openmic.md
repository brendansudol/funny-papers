# OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System

**Yuyang Wu, Hanzhong Cao, Jianhao Chen, Yufei Li** — arXiv:2601.08288 · Guide entry Part 2 (also in this cluster) (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2601.08288) · [local PDF](../pdfs/x03-openmic.pdf) · [full markdown](../md/x03-openmic/x03-openmic.md) · [extract](../extracts/x03-openmic.json)

## TL;DR
OpenMic is an AutoGen-based multi-agent system for Chinese stand-up generation: it turns a user topic into a 3–5 minute stage-ready script and then a narrated comedy video. Its main empirical claim is that low-temperature generation with RAG best preserves retrieved comedic material; in Table 1, JW+Tem0.1 scores 82.5 Persona, 88.0 Reactivity, 95.5 Humor, 93.0 Narrative, and 97.5 Coherence.

## Problem & Motivation
The paper argues that Chinese stand-up is harder than plain text generation because it requires culturally grounded humor, delayed punchlines, callbacks, timing, spoken delivery, and stage cues. Existing Chinese humor datasets such as CFunSet are described as useful for humor understanding and short-form generation tasks, but misaligned with long-form 3–5 minute stand-up. The authors also report that strong single models can fail stylistically: GPT-5.2 can become didactic or “preachy,” while DeepSeek can produce sparse and uneven jokes.

## Approach
OpenMic decomposes stand-up creation into five agents. AudienceAnalyzer builds a persona card and taboo list. ComedyDirector creates subtopics and a structure plan with hooks, bits, callbacks, and closing tags. JokeWriter drafts spoken Chinese stand-up. PerformanceCoach adds DSL cues such as pauses, emphasis, pace changes, applause, and laughter. QualityController gates the result with PASS or REVISION feedback.

The system uses a shared blackboard for persistent structured state and a separate Secret Blackboard inside the RAG subsystem. Its RAG pipeline retrieves candidates from an integrated comedic corpus, uses an LLM Candidate Scorer to filter for comedic potential, and uses an LLM Punchline Selector to distill retrieved jokes into writing materials. The authors also fine-tune a JokeWriter with QLoRA and completion-only loss to focus on assistant responses rather than prompt text.

## Data & Experimental Setup
The retrieval corpus combines short-form setups and punchlines from the CFUN repository and material produced by a Crosstalk-to-Talkshow Pipeline that converts traditional crosstalk scripts into narrative talk-show observations. Fine-tuning uses an LLM-processed Talkshow dataset formatted with the Qwen-2.5 chat template. Table 2 lists QLoRA settings: Base Model Qwen-2.5-3B-Instruct, 4-bit NF4 quantization, LoRA rank 16, LoRA alpha 32, dropout 0.05, learning rate 2 × 10^-4, Paged AdamW 32-bit, per-device batch size 2, gradient accumulation 4, and 1 epoch.

Evaluation uses `Grok-4-1-fast-reasoning` as an LLM judge with a senior executive producer persona. Scores cover Persona Fidelity, Humor Mechanics, Interactive Reactivity, Contextual Coherence, and Narrative Arc, with weights 30%, 25%, 20%, 15%, and 10%.

## Results
Across temperature settings, Table 1 reports: JW+Tem0.1 = 82.5 Persona, 88.0 Reactivity, 95.5 Humor, 93.0 Narrative, 97.5 Coherence; JW+Tem0.3 = 88.5, 15.0, 96.0, 93.0, 97.5; JW+Tem0.5 = 82.5, 15.0, 96.5, 93.0, 98.5; JW+Tem0.7 = 92.5, 45.0, 96.0, 98.5, 97.0; JW+Tem0.9 = 85.0, 25.0, 92.0, 94.0, 96.0. The paper’s interpretation is that T = 0.1 plus a large RAG corpus gives the best overall behavior because it maximizes focus on retrieved comedic building blocks. It also reports that the hardest dual-failure case occurs in ~30% of round-1 attempts but drops to <5% by round 3.

## Takeaways
- Treat long-form stand-up as a production pipeline, not a single prompt.
- RAG is used here as creative grounding, but the paper argues raw retrieval needs LLM scoring and refinement.
- Lower temperature helps the JokeWriter assemble retrieved materials rather than hallucinate disconnected humor.
- Delivery markup matters: the output is designed for performance, not just reading.

## Limitations & Caveats
The paper emphasizes that humor evaluation is subjective, culturally grounded, context-dependent, and delivery-sensitive. The reported evaluation is LLM-as-a-judge rather than human or live-audience evaluation, and the temperature analysis is described as having high variance.
