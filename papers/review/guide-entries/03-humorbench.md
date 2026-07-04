<!-- guide claims for 03-humorbench (#3) -->

### 3. [Which LLMs Get the Joke? Probing Non-STEM Reasoning Abilities with HumorBench](https://arxiv.org/abs/2507.21476)
Narad, Suresh, Chen, Dysart-Bricken, Mankoff, Nowak, Zhang & Jain — **2025** (arXiv:2507.21476) · `preprint` `benchmark`
- **Method:** Open-ended *explanation*: given a cartoon description + caption, articulate the joke; graded by LLM-judge against a rubric of discrete verifiable "elements."
- **Dataset:** ≈300 expert-annotated cartoon–caption pairs from the New Yorker Caption Contest (top-3 finalists) and Cartoonstock.
- **Findings:** STEM-reasoning ability transfers to humor comprehension; STEM-only-trained models still do well; test-time "thinking" budgets give mixed gains; on the harder HumorBench-hard subset, no current LLM exceeds 60%. Best recent pick for explanation specifically.
- **Lineage:** From the same UW / UW–Madison group behind the NeurIPS caption-preference dataset (#22), with Bob Mankoff — former New Yorker cartoon editor — as co-author; deliberately isolates objective comprehension from subjective preference alignment.
