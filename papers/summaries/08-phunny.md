# “What do you call a dog that is incontrovertibly true? Dogma”: Testing LLM Generalization through Humor

**Alessio Cocchieri, Luca Ragazzi, Paolo Italiani, Giuseppe Tagliavini, Gianluca Moro** — ACL 2025 · Guide entry #8 (Part 1 - Explaining & Understanding Jokes)

[paper page](https://aclanthology.org/2025.acl-long.1117/) · [local PDF](../pdfs/08-phunny.pdf) · [full markdown](../md/08-phunny/08-phunny.md) · [extract](../extracts/08-phunny.json) · [dataset: Phunny](../../data/phunny/)

## TL;DR
The paper introduces PHUNNY, a benchmark of 350 manually crafted English structured puns designed to test whether LLMs generalize in a humor-based QA setting rather than relying on memorized content. Across comprehension, resolution, and generation, most LLMs fall below humans on core generalization behavior, especially rejecting misleading non-puns; o3-mini is the strongest model, reaching 93.9 ACC on resolution and 93.5 constrained-generation ACC, but it scores only 4.7 MPA on misleading pun comprehension.

## Problem & Motivation
The authors use humor as a controlled test of linguistic generalization. Their target format is simple: “What do you call a X that Y? XZ,” where the answer is a real word that starts with the subject X but is not a derivative or compound. This isolates a single-step morpho-semantic transformation, such as “dog” to “dogma,” while still requiring context, word meaning, and wordplay. The central question is whether LLMs can handle novel creative language in the way humans can.

## Approach
PHUNNY is built around structured puns represented as triplets ⟨X, Y, XZ⟩. The authors manually design each pun, then check for data contamination by retrieving the top-10 DuckDuckGo results for each complete pun and asking Gemini-1.5-Flash whether the pun appears in the retrieved web pages. This removes 20 contaminated entries. The benchmark defines three macro-tasks: Comprehension, where models explain whether a coherent or misleading pun works; Resolution, where models produce the missing punchline; and Generation, where models create new puns in either Free or Constrained settings.

## Data & Experimental Setup
The final dataset contains 350 hand-crafted puns. For comprehension, the authors evaluate 1,050 inputs: 350 coherent puns, 350 semantically similar misleading swaps, and 350 semantically dissimilar misleading swaps. Resolution uses the 350 coherent puns. Free generation asks for 50 puns, while constrained generation fixes the subject using 104 unique subjects from the dataset. The evaluated models are GPT-4o, GPT-4o-mini, o3-mini, Gemini-2.0-Flash, Gemini-2.0-Flash-Thinking, LLaMA-3.1-8B, LLaMA-3.3-70B, Phi-3.5, and Phi-4-14B. Human baselines come from 60 English-fluent volunteers.

## Results
On coherent comprehension, o3-mini is the best LLM with CPA 78.3, but humans score 87.9. On misleading comprehension, LLMs fail badly: Phi-3.5 has the highest LLM MPA at 47.7, while o3-mini scores only 4.7 and humans reach 90.9. In resolution, o3-mini leads with ACC 93.9, VPA 98.0, and EWA 99.1, above the human ACC of 85.7. In constrained generation, o3-mini reaches 93.5 ACC, above humans at 88.7. In free generation, o3-mini reaches 100.0 ACC but has limited diversity, with C_S 38.0 and C_A 52.0; humans score 92.8 ACC with much higher creativity, C_S 82.3 and C_A 95.2.

## Takeaways
- PHUNNY exposes a sharp gap between recognizing real puns and rejecting fake ones.
- Strong reasoning models can solve many resolution and constrained-generation cases, but may over-justify misleading inputs.
- Accuracy alone is insufficient for humor generation; diversity measures reveal that humans remain more flexible.
- Common LLM errors include missing the required prefix, producing derivative answers, and inventing nonexistent words.
- CoT prompting helps larger open models more than smaller ones.

## Limitations & Caveats
The benchmark is English-only, manually crafted, and restricted to suffix-addition puns with noun or adjective answers. It excludes verbs, prefix-based puns, and other joke formats. The authors also note that future work should use contaminated web-mined puns for more targeted data-leakage analysis.
