# Learning to Think Like a Cartoon Captionist: Incongruity–Resolution Supervision for Multimodal Humor Understanding

**Hatice Merve Vural, Doga Kukul, Ege Erdem Ozlu, Demir Ekin Arikan, Bob Mankoff, Erkut Erdem, Aykut Erdem** — arXiv:2604.15210 · Guide entry #24 (Part 3 - Multimodal & Visual Humor)

[paper page](https://arxiv.org/abs/2604.15210) · [local PDF](../pdfs/24-irs-cartoon-captionist.pdf) · [full markdown](../md/24-irs-cartoon-captionist/24-irs-cartoon-captionist.md) · [extract](../extracts/24-irs-cartoon-captionist.json)

## TL;DR
The paper introduces Incongruity-Resolution Supervision (IRS), a training framework for multimodal cartoon-caption humor understanding. IRS supervises models to identify visual incongruities, resolve them into humorous interpretations, and align choices with human preferences; its best model, IRS-72B, reaches 76.10% accuracy on NYCC ranking, beating all model baselines in that column.

## Problem & Motivation
Most work on the New Yorker Cartoon Caption Contest treats humor understanding as selecting or ranking captions, without teaching models the reasoning process that makes a caption funny. The authors argue that cartoon humor requires a structured path: recognize a mismatch in the visual scene, construct a coherent reinterpretation, and decide which caption resolves the tension best. NYCC is used because it connects images, crowd captions, expert curation, and audience preferences.

## Approach
IRS has three stages. Incongruity Modeling performs continual pretraining on captionist discussions, editorial analyses, caption-writing guides, books, and general text to adapt the model to humor-related discourse. Resolution Modeling trains on captionist reasoning traces generated from Hessel et al. annotations using DeepSeek-R1, then rephrased with GPT-4o into concise, image-grounded commentary. Preference Alignment uses GRPO with four rewards: accuracy, output format, visual perception, and style. The visual and style rewards are judged by Qwen2.5-7B-Instruct and are applied only when the answer is correct.

## Data & Experimental Setup
The main evaluation uses NYCC-based matching and ranking from Hessel et al. (2023), plus Zhou et al. (2025) 10-vs-1000 and 30-vs-300 ranking splits. Models include DeepSeek-R1 on text annotations, closed multimodal baselines o3 and o4-mini, open multimodal reasoning models, Qwen2.5-VL backbones at 7B/32B/72B, and IRS versions of those backbones. Human baselines include an expert captionist and 21 non-expert participants. Zero-shot transfer is tested on YesBut Philosophy/Title and DeepEval humorous-subset DeepSemantics, Description, and Title tasks.

## Results
IRS improves over the corresponding Qwen2.5-VL base models at every scale. At 7B, IRS scores 59.67, 64.42, 56.29, and 53.14 versus the base model’s 42.67, 55.06, 50.57, and 47.99. IRS-72B scores 69.33 on matching and 76.10 on ranking; the 76.10 ranking result exceeds o3’s 62.85 and o4-mini’s 62.59. o3 remains strongest on matching at 83.33. In ablations, the full 7B IRS pipeline is strongest overall; Resolution Modeling is the main contributor, while Incongruity Modeling alone can hurt but helps when combined with RM. On YesBut, IRS-7B improves from 43.19 to 74.90 on Philosophy and from 29.11 to 63.32 on Title. On DeepEval, it improves from 10.34 to 54.43, 24.13 to 100.00, and 34.48 to 63.18.

## Takeaways
- Supervising humor reasoning structure is more effective than relying on scale alone for open-weight models.
- Captionist-style traces help models connect visual details, incongruity, speaker roles, and caption choice.
- Visual grounding and style rewards matter most for ranking-style humor judgments.
- Strong matching performance still depends heavily on perception; closed models retain an advantage there.
- Zero-shot gains suggest IRS learns reusable visual humor reasoning patterns.

## Limitations & Caveats
The model still makes visual perception errors on stylized cartoons, and these errors cascade into wrong caption choices. Cultural grounding is brittle, especially for pop-culture references. The work is centered on Anglophone, U.S.-centric NYCC humor, and humor judgments remain subjective. Some training sources are copyrighted and cannot be directly released.
