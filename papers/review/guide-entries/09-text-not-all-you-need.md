<!-- guide claims for 09-text-not-all-you-need (#9) -->

### 9. [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](https://arxiv.org/abs/2412.05315)
Ashwin Baluja — **CHum 2025** · `workshop` `method`
- **Method:** Presents the LLM with both the text and a TTS-generated *spoken* form of a joke for phonetic/timing cues; CoT prompting where the reasoning doubles as explanation.
- **Dataset:** Existing pun datasets, zero/few-shot.
- **Findings:** Multimodal (text+audio) prompting beats text-only on pun understanding/explanation — some "understanding" failures are really modality limits (puns live in sound).

---

## Part 2 — Generating Jokes

Throughline: **generic linear chain-of-thought is poorly matched to humor generation; successful systems use structured creative search, script opposition, persona diversity, retrieval, or generate–evaluate–revise loops.** That umbrella covers CLoT, LoL, HumorGen, HOMER, HUMORCHAIN, Witscript, Jokeasy, and Multi-Agent Comedy Club alike.

**Pre-LLM foundations (historical grounding).** Computational humor long predates LLMs. Template-and-schema systems generated puns and riddles — Binsted & Ritchie's [**JAPE**](https://arxiv.org/abs/cmp-lg/9406022) ("An implemented model of punning riddles," AAAI 1994) and its successor **STANDUP** (Ritchie et al. 2007) used WordNet plus pronunciation dictionaries; **HAHAcronym** (Stock & Strapparava 2005) produced humorous acronyms; and Mihalcea & Strapparava's "Making Computers Laugh" (HLT/EMNLP 2005) pioneered humor *recognition*. Their lasting lesson — conceded by the authors themselves (schoolchildren reportedly called JAPE's output "pathetic") — anchors this bibliography's synthesis: structure can be mechanized, but mechanized structure alone yields weak humor.
