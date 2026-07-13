# Humor as a window into generative AI bias

**Roger Saumure, Julian De Freitas, Stefano Puntoni** — Scientific Reports 15:1326 · Guide entry Part 6 (bias under humorization) (Part 6 - Safety, Harm & Boundaries)

[paper page](https://doi.org/10.1038/s41598-024-83384-6) · [local PDF](../pdfs/x27-genai-humor-bias.pdf) · [full markdown](../md/x27-genai-humor-bias/x27-genai-humor-bias.md) · [extract](../extracts/x27-genai-humor-bias.json)

## TL;DR
This preregistered audit tests whether asking ChatGPT to make generated images funnier changes who appears in those images. Across 600 images from 150 prompts, humorization increased representation of older, high body weight, and visually impaired people, while decreasing representation of racial minority and female subjects.

## Problem & Motivation
The paper studies the intersection of generative AI image production, bias, and humor. The authors argue that humor can normalize derogatory stereotypes, especially when it is interpreted as punching down at groups that already face prejudice. Because consumer AI systems combine language models and image generators, the paper asks whether the interaction between GPT-4 and DALL-E3 creates biased humorous images when users request funnier versions.

## Approach
Two research assistants generated images in ChatGPT from 150 prompts describing a human carrying out an action, then asked the system to make each image funnier. The authors also asked GPT-4 what prompt it used to generate each image, yielding internal textual descriptors. Separately, hypothesis-blind research assistants coded images for race, gender, eyesight, bodyweight, and age. The analysis used equal-weighted and severity-weighted omnibus bias measures plus trait-specific regressions comparing original versus funnier images.

## Data & Experimental Setup
The main audit contains 600 images: 150 original images per research assistant and 150 funnier versions per research assistant. Images with non-human entities or more than one human were excluded, and traits that were not discernible were excluded only for that trait measure. The paper also analyzes 600 internal prompts. A Prolific pretest with N = 300 supplied severity weights, and a preregistered Prolific study with N = 100 measured perceived political sensitivity of different kinds of bias.

## Results
The equal-weighted omnibus analysis found bias toward stereotyping: M = 0.39, SE = 0.05, t(264) = 7.25, 95% CI [0.286, 0.499], p < 0.001, d = 0.45. The severity-weighted version also found bias: M = 0.09, SE = 0.01, t(264) = 8.65, 95% CI [0.0729, 0.116], p < 0.001, d = 0.531.

Trait-specific regressions showed significant increases for age (β = 2.93, p < 0.001), bodyweight (β = 0.095, p < 0.001), and eyesight (β = 2.83, p < 0.001). Race and gender moved in the opposite direction: race β = -1.32, p = 0.011; gender β = -0.88, p = 0.022. Participants rated race and gender bias as more politically sensitive than age, bodyweight, or eyesight bias, M = 80.00 vs. M = 61.20. An additional image analysis found a political sensitivity × image version interaction, β = 3.67, SE = 0.42, z = 8.79, p < 0.001. Internal prompt analysis found evidence of language-side bias only for eyesight: χ²(1) = 34.04, p < 0.001, with glasses appearing 17.74% vs. 2.26%.

## Takeaways
- Humorization can surface bias dimensions that standard race/gender audits may miss.
- Bias moved in opposite directions for politically sensitive and less politically sensitive traits.
- Image outputs, not just LLM text prompts, need direct auditing.
- Original images were already skewed, including 0% high body weight and 9.80% female individuals.

## Limitations & Caveats
The authors state that causes are difficult to determine. The political-sensitivity image analysis was not preregistered. The study does not test downstream attitude effects, other AI models, other languages, or whether visual style changes such as colorfulness and cartoon-like rendering systematically amplify stereotypes.
