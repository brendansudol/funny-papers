# Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor

**Ashwin Baluja** — CHum 2025 · Guide entry #9 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://arxiv.org/abs/2412.05315) · [local PDF](../pdfs/09-text-not-all-you-need.pdf) · [full markdown](../md/09-text-not-all-you-need/09-text-not-all-you-need.md) · [extract](../extracts/09-text-not-all-you-need.json)

## TL;DR
This paper tests a simple way to improve LLM humor understanding: give the model both the joke text and a TTS-generated spoken version of the same joke. Using Gemini-1.5-Flash for generation and GPT-4o as an LLM judge, multimodal prompting improves explanation quality over text-only prompting on SemEval, Context-Situated Puns, and ExplainTheJoke.

## Problem & Motivation
The paper argues that humor, especially puns, often depends on information that text-only LLMs may not represent well: phonetic ambiguity, rhythm, timing, and spoken cues. Puns are the central motivation because they rely on homographs and heterographs, where multiple meanings or similar sounds are essential to the joke. Prior work has studied LLM humor classification and text prompting, but this paper asks whether a lightweight multimodal prompt can help without training a new model.

## Approach
The method converts each text joke into audio using OpenAI’s tts-1-hd. Gemini-1.5-Flash then receives a prompt containing task definitions, instructions, six few-shot examples with chain-of-thought-style reasoning, the input text, and the generated audio. The model outputs a parsable JSON explanation and choice indicating whether the text is a pun or non-pun.

The paper tests two multimodal designs: separate text-only and audio-only explanation processes followed by aggregation, and a single prompt containing both text and audio. The single combined prompt performed better and is used for the main experiments. Prompts instruct the LLM not to mention that it received multiple modalities, because the reference explanations do not discuss modality.

## Data & Experimental Setup
Three datasets are evaluated. SemEval-2017 Task 7 puns contains “810 & 647 puns (homographic & heterographic), and 1077 non-puns,” with human annotations and human sentence-form explanations. Context-Situated Puns contains “821 & 1739 puns (homographic & heterographic)” with pun-word annotations but no human explanations. ExplainTheJoke contains “350 jokes” with variable-quality paragraph explanations.

Gemini-1.5-Flash generates explanations. GPT-4o judges explanation quality through pairwise comparison. To address positional bias, each comparison is run twice with swapped ordering, and win rates are averaged. For SemEval, model explanations are compared against human explanations. For Context-Situated Puns and ExplainTheJoke, text-only and multimodal outputs are compared directly.

## Results
On SemEval heterographs, the baseline achieved 47.76 Win % and 5.64 Tie %, while the audio condition achieved 51.74 Win % and 4.56 Tie %. On SemEval homographs, the baseline achieved 68.89 Win % and 8.40 Tie %, while audio achieved 72.59 Win % and 6.36 Tie %.

On Context-Situated Puns, audio also won more often in direct comparison. For heterographs, baseline Win % was 33.87, audio Win % was 36.49, and Tie % was 29.65. For homographs, baseline Win % was 35.08, audio Win % was 36.85, and Tie % was 28.08.

On ExplainTheJoke, baseline Win % was 12.81, audio Win % was 15.44, and Tie % was 71.75. The ablation shows that audio-only prompting is much weaker: 25.50 heterograph and 55.86 homograph Model Win %, compared with 51.74 and 72.59 for the full system.

## Takeaways
- Audio is useful as a supplement to text, not a replacement.
- TTS-generated speech can improve pun explanation, especially where phonetic ambiguity matters.
- Gains also appear on broader jokes from ExplainTheJoke, suggesting audio may convey cues beyond homophones.
- Prompt design matters substantially; the combined audio-text prompt beat the separate aggregation strategy.
- LLM-as-judge evaluation should control for positional bias, as this paper does with swapped comparisons.

## Limitations & Caveats
The method is prompt-sensitive and required tuning. The TTS audio does not fully capture human timing, cadence, rhythm, or richer delivery cues. The evaluation relies on GPT-4o judging rather than human assessment, and the paper recommends future human evaluations or stronger judge models. The ethics statement also warns that joke explanations may reproduce offensive stereotypes or harmful content.
