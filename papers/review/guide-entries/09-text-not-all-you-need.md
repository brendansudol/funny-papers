<!-- guide claims for 09-text-not-all-you-need (#9) -->

### 9. [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](https://arxiv.org/abs/2412.05315)
Ashwin Baluja — **CHum 2025** · `workshop` `method`
- **Method:** Presents the LLM with both the text and a TTS-generated *spoken* form of a joke for phonetic/timing cues; CoT prompting where the reasoning doubles as explanation.
- **Dataset:** Existing pun datasets, zero/few-shot.
- **Findings:** Multimodal (text+audio) prompting beats text-only on pun understanding/explanation — some "understanding" failures are really modality limits (puns live in sound).
