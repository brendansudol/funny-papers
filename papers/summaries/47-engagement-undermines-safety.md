# Engagement Undermines Safety: How Stereotypes and Toxicity Shape Humor in Language Models

**Atharvan Dogra, Soumya Suvra Ghosal, Ameet Deshpande, Ashwin Kalyan, Dinesh Manocha** — EACL 2026 · Guide entry #47 (Part 6 - Safety, Harm & Boundaries)

[paper page](https://arxiv.org/abs/2510.18454) · [local PDF](../pdfs/47-engagement-undermines-safety.pdf) · [full markdown](../md/47-engagement-undermines-safety/47-engagement-undermines-safety.md) · [extract](../extracts/47-engagement-undermines-safety.json)

## TL;DR
This paper uses humor generation as a safety testbed and asks whether LLM humor pipelines reward stereotypes and toxicity. Across six open-source models, comedian-persona prompting increases harmful generations, and both a trained humor regressor and an LLM rater score more stereotypical or toxic jokes as funnier.

## Problem & Motivation
LLMs are increasingly used as creative writing assistants and engagement systems, including for jokes and witty remarks. The paper argues that humor is a risky setting because stereotypes or toxic cues can act as shortcuts to surprise and engagement. The central concern is a “Bias Amplification Loop”: generators may produce harmful humor, and evaluators optimized for funniness may reward it, pushing single-objective humor pipelines toward unsafe content.

## Approach
The authors start from r/Jokes setups, remove punchlines, filter setups to be non-stereotypical, and ask models to complete the jokes. They compare a base prompt with a persona prompt that instructs the model to “Speak exactly like” one of 50 prominent comedians from Pantheon 2.0. For each generated joke, they measure humor, stereotypicality, toxicity, and incongruity. Humor is measured with a retrained Weller and Seppi-style regressor and with a 3-point LLM ordinal rater. Stereotypes are measured with an ALBERT-v2 stereotype classifier and LLM ratings; toxicity is measured with HateBERT-ToxiGen and LLM ratings. Incongruity is operationalized through token-level uncertainty and surprisal over punchlines.

## Data & Experimental Setup
The main data source is the r/Jokes corpus, described as over 550,000 jokes with setups, punchlines, and upvote counts. After filtering, the authors sample 10,000 neutral joke bodies as prompts. Six models generate completions: OLMo-2-1124-7B-Instruct, OLMo-2-1124-13B-Instruct, OLMo-2-0325-32B-Instruct, Meta-Llama-3.1-8B-Instruct, Ministral-8B-Instruct-2410, and Mistral-Small-24B-Instruct-2501. Each prompt yields 5 completions in both base and persona conditions, producing approximately 15 Million generations. The paper also evaluates an external satire-generation subset from Horvitz et al. (2024), using human funniness labels.

## Results
Persona prompting increases harm. Classifier-based mean stereotype rate rises from 54.91₁.₅₁ to 59.11₃.₆₇, and classifier-based toxicity rises from 70.92₁.₆₇ to 75.78₄.₀₇. LLM-eval toxicity also rises from 34.62₄.₇₃ to 39.35₅.₅₁.

Harmful jokes score funnier. Mean humor score increases across stereotype levels: Not Stereotypical 0.834, Subtle Stereotypical 0.869, Strong Stereotypical 0.891. It also increases across toxicity levels: Not Toxic 0.844, Mild Toxic 0.863, Severe Toxic 0.900. In LLM humor labels, Strong Stereotypical outputs are 80.9% Hilarious, while Mild Toxicity is 90.5% Hilarious and Severe Toxicity is 83.0% Hilarious. Correlations are positive: stereotype vs. humor ρ ≈ +0.10, toxicity vs. humor ρ ≈ +0.21, and stereotype vs. toxicity ρ ≈ +0.26, all with p ≪ 0.001.

The satire task supports the pattern: ChatGPT-3.5 stereotype rate rises from 8.54 to 18.29, GPT-4 from 8.51 to 13.83, and Mistral-Inst. from 9.09 to 18.18.

## Takeaways
- Single-objective “maximize funniness” pipelines can select for harmful content.
- Persona or role prompting can make humor generations edgier and less safe.
- Humor evaluators trained on community preference signals may encode harmful taste biases.
- Safety evaluation for humor should jointly track funniness, stereotypes, toxicity, and incongruity rather than reporting humor alone.

## Limitations & Caveats
The results depend heavily on r/Jokes and Reddit upvote-derived humor signals. The study focuses on six open-source models, while proprietary or newer systems may differ. The stereotype detector uses broad categories, so finer cultural stereotypes may be missed. The authors also note that other evaluation setups, including multimodal or human-in-the-loop systems, could reveal different patterns.
