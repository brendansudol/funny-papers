<!-- guide claims for 08-phunny (#8) -->

### 8. ["What do you call a dog that is incontrovertibly true? Dogma": Testing LLM Generalization through Humor (Phunny)](https://aclanthology.org/2025.acl-long.1117/)
Cocchieri, Ragazzi, Italiani, Tagliavini & Moro — **ACL 2025** · `peer-reviewed` `benchmark` `dataset`
- **Method:** A pun-based question-answering benchmark manually curated for *novelty* to minimize data contamination; three tasks over a fixed structural schema — pun comprehension, resolution, and generation — plus a detailed error analysis.
- **Dataset:** Phunny (novel, human-written structured puns).
- **Findings:** Most LLMs struggle to generalize even on structurally simple tasks, consistently underperforming the human baseline. The natural complement to Pun Unintended (#4): that paper shows models fooled by *corrupted familiar* puns; Phunny asks whether they can handle *genuinely novel* ones at all. Together they bracket the memorization question.
