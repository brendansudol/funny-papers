<!-- guide claims for 04-pun-unintended (#4) -->

### 4. [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://arxiv.org/abs/2509.12158)
Zangari, Marcuzzo, Albarelli, Pilehvar & Camacho-Collados — **EMNLP 2025** · `peer-reviewed` `benchmark`
- **Method:** Reformulates pun benchmarks (e.g., swap the pun word for a random one); semi-structured rationales; 7 LLMs + RoBERTa; temp 0; human eval.
- **Dataset:** PunEval (2,589, cleaned SemEval-2017 Task 7) + a JOKER subset (632 puns / 632 non-puns).
- **Findings:** Subtle edits that destroy the pun still get labeled puns — structure-matching, not comprehension; documents "regressive sycophancy." The sharpest "understanding is an illusion" result.
