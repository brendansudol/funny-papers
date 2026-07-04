<!-- guide claims for 10-joke-master-pun-curriculum (#10) -->

### 10. [Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM](https://aclanthology.org/2024.findings-acl.51/)
Chen, Yang, Hu, Chen, Lan, Cai, Zhuang, Lin, Lu & Zhou — **Findings of ACL 2024** · `peer-reviewed` `method` `dataset`
- **Method:** Multi-stage curriculum *preference* learning with an improved DPO to jointly optimize pun-structure and humor preferences (multi-objective alignment).
- **Dataset:** ChinesePun (2.1k annotated puns); evaluated on Chinese + English (SemEval) benchmarks.
- **Findings:** Significantly beats baselines on both languages; the most relevant recent pun-*generation* paper. (Pre-LLM pun-generation context: AmbiPun, Context-Situated Pun Generation, and "A Unified Framework for Pun Generation with Humor Principles," all EMNLP 2022; for a novelty-controlled test of pun comprehension *and* generation, see Phunny, #8.)
