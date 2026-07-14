<!-- guide claims for 06-good-pun-own-reword (#6) -->

### 6. ["A good pun is its own reword": Can Large Language Models Understand Puns?](https://aclanthology.org/2024.emnlp-main.657/)
Xu, Yuan, Chen & Yang — **EMNLP 2024** · `peer-reviewed`
- **Method:** Pun recognition, explanation, and generation with new metrics designed for in-context learning; dual-biased prompts whose "reason" doubles as the explanation; fine-grained punchline checks.
- **Dataset:** SemEval-2017 Task 7 + the ExPun corpus (hom/het/non-puns); 8 LLMs (7B open models through GPT-4-Turbo, Claude-3-Opus).
- **Findings:** Lower true-negative than true-positive rate (non-puns that resemble puns fool models); identifies the "lazy pun generation" pattern (both senses jammed into one line); strong models still do respectably.
