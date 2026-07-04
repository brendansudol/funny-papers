# Re-defining Humor Data Objects for AI Humor Research

**Anna Arnett, Bang Nguyen, Meng Jiang** — arXiv:2605.25171 · Guide entry Part 8 (also) (Part 8 - Datasets & Shared Tasks)

[paper page](https://arxiv.org/abs/2605.25171) · [local PDF](../pdfs/x13-redefining-humor-data.pdf) · [full markdown](../md/x13-redefining-humor-data/x13-redefining-humor-data.md) · [extract](../extracts/x13-redefining-humor-data.json)

## TL;DR
This paper argues that AI humor datasets should not treat humor as only present or absent in a text. It defines a humor reasoning data object around social interaction and shows that a revised GPT-4o mini prompt improves explanation quality from 17 / 31 acceptable outputs to 27 / 31 on the same manually reviewed examples, then scales generation to 307 explanation examples.

## Problem & Motivation
Most existing AI humor work represents an item as a text plus a binary humor label. The authors argue that this misses the social structure of humor: a teller makes a humorous attempt in context, a receiver reacts, and that reaction can be explained. Failed humor may also require a recovery response. The paper’s goal is to create a richer data object that supports humor reasoning, not just humor detection.

## Approach
The proposed humor object is a quintuple (C, X; Y, R; Z): C is social dialogue or context, X is the teller’s humorous attempt, Y is the receiver reaction where 1 means humorous and 0 otherwise, R is the receiver’s explanation for the reaction, and Z is the teller’s recovery response after failure, with ‘n/a’ when Y = 1. The preliminary work focuses on generating R. The authors first used a prompt asking GPT-4o mini for reasoning steps, a causal flow chart, a one-sentence explanation, and a hallucination flag. After manual error analysis, they revised the prompt to first judge whether the text alone supports the explanation and to flag missing context, possible multimodal dependence, transcription errors, alignment problems, and related data-quality issues.

## Data & Experimental Setup
The source material came especially from SMILE (TED+sitcoms), using local textual context C, candidate humorous utterance or punchline X, speaker information, and observed reaction Y. Because the sources were often multimodal, the transcript sometimes lacked visual cues, gestures, timing, delivery, or earlier setup. Both prompts were evaluated on the same 31 manually reviewed examples. Outputs were judged acceptable or unacceptable according to whether they matched the authors’ interpretation of the transcript. After a pilot inspection for valid JSON, grounded reasoning, and hallucination avoidance, the revised prompt was used to generate 307 explanation examples.

## Results
Prompt 1 produced 17 / 31 acceptable outputs and 14 / 31 incorrect outputs. The 14 errors broke down into 7 due to incomplete context, 2 due to named entities not being properly explained, and 5 due to multimodality. Prompt 2, using the same GPT-4o mini checkpoint, produced 27 / 31 correctly labeled outputs and 4 / 31 errors. That is 10 more correct outputs than Prompt 1 on the same set, while incorrect outputs dropped from 14 / 31 to 4 / 31. The remaining Prompt 2 errors were narrower: 1 missing-context case and 3 likely multimodal-dependence cases. The authors also report that automatic prompt optimization using DSPy/GEPA did not improve performance beyond manual prompt adjustment in their setup.

## Takeaways
- Humor explanation systems need to decide when the available transcript is insufficient, rather than always forcing an explanation.
- Data-quality flags for missing context, multimodal dependence, transcription errors, and alignment issues are central for humor data built from live or audiovisual sources.
- Manual failure analysis directly improved prompt design and mattered more than automatic prompt optimization in this preliminary setup.
- The 307 generated examples are positioned as a foundation for data synthesis, data augmentation, and future humor understanding models.

## Limitations & Caveats
The manual evaluation set is small, with only 31 examples. The 307-example dataset is not a final gold-standard resource and still needs systematic evaluation by case type. The work focuses on receiver explanations R, while recovery responses Z remain future work. The paper also has not yet shown that the generated explanations improve downstream humor detection, generation, or appropriateness modeling.
