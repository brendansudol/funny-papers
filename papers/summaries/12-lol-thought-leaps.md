# INNOVATIVE THINKING, INFINITE HUMOR: HUMOR RESEARCH OF LARGE LANGUAGE MODELS THROUGH STRUCTURED THOUGHT LEAPS

**Han Wang, Yilin Zhao, Dian Li, Xiaohan Wang, Gang Liu, Xuguang Lan, Hui Wang** — ICLR 2025 · Guide entry #12 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2410.10370) · [local PDF](../pdfs/12-lol-thought-leaps.pdf) · [full markdown](../md/12-lol-thought-leaps/12-lol-thought-leaps.md) · [extract](../extracts/12-lol-thought-leaps.json)

## TL;DR
LoL is a two-stage method for improving LLM humor reasoning: first train humor judgment and understanding with structured instruction data, then improve generation with online DPO preference learning and GPT-4o-generated rationales. The main result is broad improvement on humor judgment: the paper reports average accuracy gains of 4.55% and 5.91% over LLAMA3-70B and GPT-4o on English benchmarks, and 16.22% over GPT-4o on Chinese benchmarks.

## Problem & Motivation
The paper argues that humor generation is hard because it requires multi-hop reasoning over sparse and often implicit associations. Prior work such as CLoT trains mostly on question-answer endpoints and may learn surface creative patterns rather than the reasoning path. The authors frame humor reasoning as a knowledge-graph problem: entities from the question and answer must be connected through correlation entities and causal relations that explain why the answer is funny. Their goal is to make those hidden links more explicit during training.

## Approach
LoL has two training stages. In supervised fine-tuning, the authors convert human-voted humor data into judgment-oriented tasks: selecting the funnier answer, ranking answers, rewriting a non-humorous answer into a humorous one, and a teacher-student loop where GPT-4o agents simulate feedback, revision, and backtracking. They also propose Automatic Instruction Expansion (AIE), a three-agent process with a generator, imaginator, and selector/critic that expands seed conversations with richer background knowledge while rejecting shifts away from the joke’s core idea.

The second stage is Guided Explorative Self-Improvement Tuning (GESIT). A frozen copy of the SFT model judges sampled answer pairs, while the trainable model is optimized with DPO. GPT-4o supplies rationales for online-generated positive and negative responses, and training mixes data with and without rationales at a 1:1 ratio.

## Data & Experimental Setup
The paper uses Oogiri-GO, HaHackathon (SemEval-2021 Task 7), Humicroedit + FunLines (SemEval-2020 Task 7), and Chinese Community Data including Ruozhiba. Oogiri-GO is split with 95% for training and 5% for testing. The main judgment evaluations are 2T1, 2T1(hard), 3T1, and 4T1 choice questions. LoL is mainly validated on QWEN1.5-32B-Chat with LoRA on 8 A100 GPUs: 6 SFT epochs at learning rate 3e-4, then 3 DPO epochs at 2e-4. The paper also evaluates DAT creativity scores and runs a human study on 200 Ruozhiba validation questions, collecting 15 valid questionnaires and 3000 votes.

## Results
On English benchmarks, OURS-32B scores 96.58 on SemEval 2021 2T1, 57.45 on 2T1(hard), 48.06 on 3T1, 35.90 on 4T1, 64.57 on SemEval 2020 2T1, and 97.20 on Oogiri-GO 2T1. GPT-4o is best only on SemEval 2021 2T1(hard), with 60.77. On Chinese benchmarks, OURS-32B reaches 90.95 on 2T1 and 69.97 on 2T1(hard), compared with GPT-4o at 64.98 and 63.49. On Ruozhiba 2T1, LoL scores 95.35, above QwQ at 90.80 and GPT-4o at 76.40.

Ablations show the training components matter. On English ablation, ALL+AIE(DIET) reaches 97.20 on Oogiri-GO-en 2T1 versus 68.01 for QWEN1.5-32B, and 45.46 on SemEval 2021 3T1 versus 35.38. On Chinese ablation, +AIE(DIET) reaches 90.34 on 2T1 versus 52.71 for QWEN1.5-32B.

## Takeaways
- Pairwise humor judgment is central: LoL uses selection and ranking rather than a single noisy humor score.
- Rationale-rich preference learning is used to connect humorous answers back to causal logic.
- AIE is intended to broaden associations without letting the joke drift off-topic.
- For humor-system builders, the paper suggests training judgment, explanation/rationale structure, and generation together rather than treating generation alone as the task.

## Limitations & Caveats
The authors emphasize humor subjectivity and note that unified scoring can be noisy. Their failure cases show uneven creativity, partly attributed to variation in the training data, and some human-preferred answers beat LoL. The paper reports strong human preference for LoL but does not state exact win-rate percentages in the text transcription.
