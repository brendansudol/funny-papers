<!-- guide claims for 13-humorgen-persona-distillation (#13) -->

### 13. [HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation](https://arxiv.org/abs/2604.09629)
Ajayi & Mitra — **2026** (arXiv:2604.09629) · `preprint` `method` `dataset`
- **Method:** Mixture-of-Thought with six cognitive personas (Absurdist, Cynic, …) grounded in humor theory; distilled data fine-tunes a 7B student; tests DPO and offline group-relative RL (O-GRPO). Evaluated on SemEval-2026 Task 1 (MWAHAHA, #57) headlines and Humor Transfer Bench.
- **Findings:** 7B models beat larger instruct baselines; two notable null results — neither DPO nor O-GRPO beat plain SFT (data quality > optimization), and distilling the teacher's *reasoning traces* usually hurts ("the explainer trap"). Also reports that fine-tuning on stand-up transcripts *regressed* text-native humor (performance humor ≠ written humor).
- **Disclosure:** Companion paper to HumorRank (#35), by the same authors.
