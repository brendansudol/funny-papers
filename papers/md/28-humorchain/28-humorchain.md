<!-- Transcribed from 28-humorchain.pdf -->



<!-- page 0001 -->

arXiv:2511.21732v2 [cs.CL] 24 Mar 2026

# HUMORCHAIN: Theory-Guided Multi-Stage Reasoning for Interpretable Multimodal Humor Generation

Jiajun Zhang<sup>* †</sup>  
Peking University  
Beijing, China  
jzhang3439-c@my.cityu.edu.hk

Shijia Luo<sup>* †</sup>  
Ocean University of China  
Qingdao, China  
luoshijia@stu.ouc.edu.cn

Ruikang Zhang<sup>*</sup>  
Peking University  
Beijing, China  
2300018416@stu.pku.edu.cn

Qi Su<sup>‡</sup>  
Peking University  
Beijing, China  
sukia@pku.edu.cn

## Abstract

Humor, as both a creative human activity and a social binding mechanism, has long posed a major challenge for AI generation. Although producing humor requires complex cognitive reasoning and social understanding, theories of humor suggest that it follows learnable patterns and structures, making it theoretically possible for generative models to acquire them implicitly. In recent years, multimodal humor has become a prevalent form of online communication, especially among Gen Z, highlighting the need for AI systems capable of integrating visual understanding with humorous language generation. However, existing data-driven approaches lack explicit modeling or theoretical grounding of humor, often producing literal descriptions that fail to capture its underlying cognitive mechanisms, resulting in the generated image descriptions that are fluent but lack genuine humor or cognitive depth. To address this limitation, we propose HUMORCHAIN (HUmor-guided Multi-step Orchestrated Reasoning Chain for Image Captioning), a theory-guided multi-stage reasoning framework. It integrates visual semantic parsing, humor- and psychology-based reasoning, and a fine-tuned discriminator for humor evaluation, forming an interpretable and controllable cognitive reasoning chain. To the best of our knowledge, this is the first work to explicitly embed cognitive structures from humor theories into multimodal humor generation, enabling a structured reasoning process from visual understanding to humor creation. Experiments on Meme-Image-No-Text, Oogiri-GO, and OxfordTVG-HIC datasets show that HUMORCHAIN outperforms state-of-the-art baselines in human humor preference, Elo/BT scores, and semantic diversity, demonstrating that theory-driven structured reasoning enables large language models to generate humor aligned with human perception.

## 1. Introduction

Humor is a fundamental component of human communication, yet its inherent subjectivity and creative nature make it a persistent challenge for artificial intelligence [16, 17]. Although recent multimodal generative models have achieved impressive progress in tasks such as image captioning [1], producing fluent and semantically coherent descriptions, they remain limited when the objective extends beyond factual depiction to creative humor generation. This shift reveals fundamental gaps in their reasoning capabilities and their capacity to capture the nuanced cognitive mechanisms underlying humor. Understanding these limitations requires examining what humor generation actually entails in a multimodal setting.

In such settings, generating humor involves not only linguistic fluency but also the perception of visual cues, the recognition of cognitive incongruity, and the engagement of affective responses [20]. Current models, however, lack the reasoning capacity to support these processes, leading to outputs with limited humorous effect and insufficient cognitive-affective grounding. Nonetheless, humor creation is not arbitrary: classical theoretical frameworks—such as Incongruity–Resolution Theory, Benign Violation Theory, and Superiority Theory—show that humor follows systematic and learnable structures [9, 13, 24, 35], suggesting that generative models may be capable of implicitly internaliz-

<sup>*</sup>Equal contribution.  
<sup>†</sup>Work done during internship at Peking University.  
<sup>‡</sup>Corresponding Author.



<!-- page 0002 -->

[Figure: Simplified flowchart and comparison examples. Flowchart labels include “Simplified flowchart”, “Image”, “Humor Theory”, “Large Language Model”, “object_analogy”, “emotion_analogy”, “contrast_irony”, “absurdity”, “Manual Annotation”, “Fine-tuning”, “Based on Qwen3-VL-4B-Instruct”, “Humor Discriminator”, “Yes!”, “NO!”, and “Output a humorous title”. Legend: “Not Funny”, “Funny”, “Hilarious”, “ChatGPT 5”, “HUMORCHAIN (Ours)”. Example panels are labeled “object_analogy”, “emotion_analogy”, “contrast_irony”, and “absurdity”, with visible captions such as “The socket did its best.”, “My schedule for Monday...”, “Convertible pickup: when the bed needs more sunshine.”, “It’s like stubbornly enduring baldness while still trying to act cool”, “Ultraman’s awkward prom photo with a scaly date”, “Just like me at the annual meeting where I was drinking with the boss.”, “Not much hair, but a lot of sense of ceremony.”, “Dry your hopes.”, “You there—who ate the last s’more?”, “Welcome to freely express your opinions. Go ahead, you first.”, “Bone Appétit: Chew Chef at Work”, “The weight loss plan will start tomorrow.”, “Cupid goes tactical: love at first scope.”, “The KPI for love is too difficult to achieve.”, “The front wheel went first.”, and “The front wheel is in the braking position”.]

Figure 1. Comparison between HUMORCHAIN and ChatGPT-5 on humorous image captioning.

ing these paradigms.

Building on this insight, we propose an innovative framework—**HUMORCHAIN** (HUmor-guided Multi-step Orchestrated Reasoning Chain for Image Captioning). By integrating established humor and psychological theories [9, 13, 24, 35, 36, 45], we design a theory-guided multi-stage reasoning framework. Specifically, the framework first identifies visual cues and potential humor triggers within an image, then applies corresponding humor theories and generation strategies according to image type, thereby producing captions consistent with the cognitive mechanisms of humor perception, as shown in Figure 1.

Given the inherently subjective nature of humor evaluation, traditional automated metrics struggle to accurately assess generation quality. To address this issue, we introduce a human-preference-guided humor discrimination mechanism. We fine-tune the Qwen3-VL-4B-Instruct model [43] using instruction tuning and attach a classification head to construct a humor discriminator capable of reliably determining whether a generated caption is humorous, thereby forming a closed-loop feedback system with the generation module.

Extensive experiments on the Meme-Image-No-Text, Oogiri-GO [47], and OxfordTVG-HIC [20] datasets show that HUMORCHAIN substantially outperforms existing baselines in human humor preference, Elo/BT scores, and semantic diversity. These results further confirm that integrating humor theory can effectively enhance the ability of large language models to generate humor that aligns with human perception.

Our main contributions are threefold:

1. We propose **HUMORCHAIN** that systematically integrates humor and psychological theories into multimodal generation, realizing theory-driven structured humor reasoning.
2. We design a human-preference-guided humor discriminator, forming a closed-loop “generate–evaluate–refine” optimization framework that significantly improves humor quality and stability.
3. We construct a human-annotated humor preference dataset containing over 5,000 image–caption pairs, advancing evaluation and modeling in humor generation.

## 2. Related Work

### 2.1. Humorous Image Captioning and Multimodal Reasoning

Current research on humorous image captioning mainly follows two directions: data-driven and strategy-oriented approaches. Data-driven models rely heavily on large-scale corpora, such as the OxfordTVG-HIC dataset [20], which contains 2.9 million image-text pairs with humor ratings and emotional annotations, and MemeCraft [37], which



<!-- page 0003 -->

performs large-scale training for visual-humor alignment. However, these methods suffer from strong data dependence and tend to inherit the distributional biases of their training data, resulting in limited stylistic diversity.

Strategy-oriented research focuses on optimizing generation logic. Early unimodal methods (e.g., MemeBot [31]) use text template generation, overlooking humor-relevant visual cues. More recent multimodal approaches (e.g., XMeCap [6]) integrate image segmentation and visual feature extraction, optimizing modality alignment and generation quality via supervised fine-tuning and reinforcement learning. However, their reliance on fixed prompt templates restricts dynamic reasoning and deep humor understanding. The CLoT model [47] introduces “Leap-of-Thought” creative thinking to enhance novelty and surprise, partially improving stylistic diversity, but its outputs still fall short of producing coherent and genuinely humorous content with consistent overall quality. Some methods have focused on humor theories. For example, OxfordTVG-HIC [20] employs humor theories to evaluate generated titles. However, existing work lacks exploration of their integration into the generation process, leaving their contribution to humor generation underexplored.

Multimodal Large Language Models (MLLMs) have made notable progress in vision-language integration. Early research established foundational architectures, training strategies, and evaluation protocols [41, 44]. Subsequent models extended these foundations to support complex multimodal reasoning tasks such as image captioning, visual question answering, and cross-modal generation [11, 22, 32]. Building on this progress, generalization has further improved through few-shot adaptation, visual prompting, and modality expansion [10, 14, 21, 25]. Parallel lines of research explore interpretability, structured reasoning, and cross-modal transfer learning [4, 7, 15, 26, 33, 42], thereby broadening the applicability of MLLMs to creative generation, situational understanding, and knowledge discovery.

Among the reasoning techniques empowered by MLLMs, Chain-of-Thought (CoT) stands out by enhancing step-by-step reasoning that improves interpretability [18, 38, 39]. In humor generation, Chen et al. proposed the text-based Chain-of-Humor (CoH), which generates humorous sentences through concept extraction and conflict insertion [6]. Most existing multimodal studies, however, follow a shallow pipeline from visual description to joke generation [12, 40], constrained by the lack of humor-theoretic guidance and inadequate modeling of visual cues.

## 2.2. Humor Theory

Humor is grounded in four foundational cognitive and psychological theories:

**Incongruity–Resolution Theory** is the dominant paradigm in contemporary humor studies [29]. From a cognitive perspective, it defines humor as the perception and subsequent resolution of incongruity between conceptual elements [27, 30]. The humorous experience therefore unfolds in two stages: the individual first perceives an inconsistency, then cognitively reconstructs its internal logic to achieve resolution [35]. Building on this, Attardo and Raskin proposed the Script-based Semantic Theory of Humor (SSTH) and later the General Theory of Verbal Humor (GTVH), significantly enhancing explanatory power [2].

**Benign Violation Theory**, proposed by McGraw and Warren [24], defines humor as the result of a “benign breach” of norms. It posits that humor arises only when two conditions are met simultaneously: (1) violation—a mild transgression of social or cognitive expectations—and (2) benignity—contextual cues mitigating the perceived harm. The dynamic balance between these dimensions determines the strength of the humorous effect.

**Superiority Theory**, originating from Hobbes [13], conceptualizes laughter as a psychological response to the sudden awareness of one’s superiority. Its limitations lie in its narrow explanatory range (failing to capture all humor types) and neglect of incongruity as a core feature [5]. Contemporary research has expanded its scope by incorporating nonhuman targets and self-deprecating humor, broadening its applicability.

**Relief Theory**, first proposed by Freud and later elaborated by Spencer [9, 34], diverges from the others by focusing on humor’s function. It interprets humor as a psychological release mechanism—a safe outlet for repressed emotions constrained by social norms. Spencer further argued that laughter serves as the discharge of surplus nervous energy, triggered by tension between cognitive expectation and external stimuli.

In summary, these four foundational theories reveal humor’s cognitive architecture and psychological dynamics from complementary perspectives. Taken together, they provide the conceptual basis for embedding humor cognition into multimodal generative models and constructing interpretable reasoning frameworks for humor production.

## 3. HUMORCHAIN Framework

### 3.1. Theory-Guided Multi-Stage Reasoning Framework

The core challenge of humorous image captioning lies in operationalizing abstract humor theories into executable structured reasoning procedures. HUMORCHAIN tackles this challenge through a multi-stage LLM reasoning framework that systematically integrates humor-theoretic and psychological mechanisms into each reasoning step.

Building upon the cognitive mechanisms outlined in classical humor theories, HUMORCHAIN formalizes humor generation as a sequential reasoning chain. The model first detects incongruous information in the visual domain (corresponding to Incongruity–Resolution Theory [35]),



<!-- page 0004 -->

[Figure: Flowchart of the proposed HUMORCHAIN framework. Visible labels include: “Input image”; “Image Description” with “main subjects”, “state/emotions”, “scene”, “actions”, “texts(if readable)”, “significant details”; “The language model generates judgments for images” with “incongruity_for_humor”, “has_human_or_animal_or_cartoon”, “plausibility”, “reasons supporting the above judgments”; “Identify the main character in the picture” with “Human beings?”, “Animals?”, “Cartoon characters?”; decision boxes “Determine whether the picture is humorous”, “Determine whether the picture is Plausible”, “Determine whether it is compliant” with “Group / Personal attacks”, “hatred/discrimination”, “humiliation”; outputs “Object_analogy”, “Emotion_analogy”, “Contrast_irony”, “Absurdity”; “HumorDiscriminate a humor discriminator based on Qwen3-VL-4B-Instruct and fine-tuned with Lora”; “Output the humorous title of this image”.]

Figure 2. Workflow of the proposed **HUMORCHAIN** framework.

then introduces irony or self-deprecation to stimulate emotional engagement (Superiority Theory [13]), or intentionally violates norms in a controlled manner (Benign Violation Theory [24]). Finally, the model achieves affective release through linguistic expression (Relief Theory [9, 34]), as shown in Figure 2. This mapping transforms humor theories into a multimodal reasoning architecture, granting the humor generation process explicit cognitive logic and theoretical interpretability.

HUMORCHAIN decomposes the humor generation process into multiple stages, each assigned a specific cognitive task to systematically progress from visual perception to humorous caption creation. Following Yu’s (2021) classification of image macro memes [45], the framework adapts and generalizes the categories into four humor generation strategies:

1. **Absurdity:** Rooted in evolutionary psychology, studies (e.g., Varela et al. [36]) show that humans prioritize processing of action and emotional information in living entities. Thus, captions should primarily focus on the emotional or behavioral states of people, animals, or characters in the image. According to Incongruity–Resolution Theory, humor arises when viewers perceive an incongruity and subsequently resolve it through reinterpretation. A caption providing explanations can help individuals resolve incongruities, thereby creating humor. Therefore, for images with obvious incongruent elements, humor can be generated by producing personified descriptions based on incongruity and absurdity, or by imagining subsequent scenarios around the incongruent points (e.g., speculating “what might happen next”).

2. **Contrast_irony:** When visual incongruity is not explicitly present, humor can be induced through semantic contrast or irony. Based on Incongruity Theory, captions can intentionally oppose the core sentiment or behavior depicted in the image, creating an absurd reversal. Alternatively, irony can be constructed under Superiority Theory, where the combination of caption and image produces an ironic effect. Benign Violation Theory constrains this process: the semantic “violation” intensity must stay within a safe emotional boundary—breaking norms enough to evoke mild discomfort but avoiding genuine offense—thereby producing pleasure through simultaneous perception of “violation” and “safety.”

3. **Emotion_analogy:** For images already containing humorous or emotionally charged elements, the model performs cognitive reconstruction and emotional release based on Incongruity–Resolution and Relief Theories. It identifies emotional tension or implicit humor in the visual content, analogizes it with human psychological responses in similar situations, and generates empathetic humorous expressions. The tension relief through contrast and analogy yields both cognitive insight and emotional satisfaction.

4. **Object_analogy:** For images dominated by inanimate objects, where direct emotional or behavioral inference is difficult, the model employs object analogy, combining Superiority and Relief Theories. It extracts salient physical or contextual features and maps them to human life events or mental states (e.g., “a messy desk” → “my brain before a deadline”), evoking self-deprecating or relatable humor that simultaneously expresses stress and releases it.

To ensure safety, HUMORCHAIN incorporates a compliance detection module to filter group or personal attacks, hate speech, or humiliating expressions (including metaphorical references). When a violation is detected, the system triggers an automatic rewriting process.

Finally, the framework employs a Humor Discriminator to perform binary classification (“humorous” vs. “non-humorous”) on generated image-caption pairs. When an output is judged as non-humorous, the system feeds back into the rewriting stage and optimizes generation strategies through controlled semantic perturbations. The discriminator’s design and training are detailed in subsection 3.2. An end-to-end implementation example of the entire HUMORCHAIN reasoning pipeline is presented in Fig. 3

### 3.2. Humor Discriminator: Dataset and Training

To align generated humorous captions with human preferences, we developed a lightweight humor discriminator based on Qwen3-VL-4B-Instruct [43], fine-tuned via LoRA



<!-- page 0005 -->

[Figure: End-to-end HUMORCHAIN flow diagram. Readable labels include “Input image”; “Image Description” with fields “Main subjects,” “State/emotions,” “Scene,” “Actions,” “Texts(if readable),” and “Significant details”; “Judgments for images” with “has_human_or_animal_or_cartoon: TRUE,” “incongruity_for_humor: False,” and “plausibility: implausible”; decision boxes for identifying the main character, determining whether the picture is humorous, determining whether the picture is incongruity, and determining whether it is compliant; theory boxes “Object_analogy,” “Emotion_analogy,” “Contrast irony,” and “Absurdity”; “humor discriminator”; and output “Output a humorous title: ‘The KPI for love is too difficult to achieve.’” Red arrows show the selected path and black dashed arrows show other possibilities.]

Figure 3. End-to-end example of the proposed HUMORCHAIN framework. Given an input image, HUMORCHAIN first performs visual entity recognition and determines that the scene contains a person. It then evaluates whether the image exhibits humorous characteristics, concluding that it is not humorous. Next, the system assesses the plausibility of the scene and judges it as implausible. Based on this judgment, HUMORCHAIN activates the Absurdity reasoning pathway, guided by Incongruity–Resolution Theory, to generate a corresponding humorous caption that aligns with this type of humor. The red arrow indicates the path through which the caption is generated, while the black dashed arrows represent other possibilities.

using a small, high-quality, human-labeled dataset. The discriminator performs binary classification on image–caption pairs (“humorous” vs. “non-humorous”). If a caption is classified as non-humorous, the system automatically triggers a rewriting mechanism to improve alignment with desirable humor traits.

### 3.2.1. Dataset Construction

We curated a benchmark of humorous images and generated multiple candidate captions using the HUMORCHAIN framework. Each image–caption pair was independently annotated by five annotators following detailed guidelines. We defined a pair as humorous if at least two annotators labeled it as “humorous”; otherwise, it was labeled as “non-humorous”. This lenient threshold was chosen to retain diverse humorous expressions while filtering out clearly non-humorous cases. This human annotation process incorporates human preference, which not only establishes a high-quality benchmark for humor discrimination but also effectively mitigates the inherent biases introduced during the operation of the prompt framework in the humor generation pipeline.

### 3.2.2. Training Process

The model was fine-tuned with LoRA using humor-aware prompts to activate implicit reasoning. Initial supervised fine-tuning enabled binary humor prediction, but this approach was inflexible. To address this, we added a classification head that outputs continuous humor probabilities, allowing adjustable thresholds for acceptance. Setting the threshold to 0.66 provided an optimal balance between precision and regeneration cost.

### 3.2.3. Retry Limit and Fallback Strategy

To ensure the efficiency and reliability of the closed-loop optimization, we set a 5-retry limit for the generation-evaluation-refine cycle, and failed cases default to the discriminator’s top-rated candidate. This enhanced architecture improves precision and stability, enabling HUMORCHAIN to generate captions better aligned with human perception.

## 4. Experiments

Through systematic experiments, we evaluate HUMORCHAIN from multiple dimensions: we assess its performance in humorous image captioning; examine whether integrating humor theory with few-shot learning or knowledge-transfer reasoning enhances humor generation; and investigate the contributions of the fine-tuned humor discriminator to the overall pipeline. Specifically, we use GPT-5-2025-08-07 as the backbone reasoning model in our



<!-- page 0006 -->

experiments.

## 4.1. Experiment 1: Pipeline Comparison and Dataset Design

Table 1. Pairwise comparisons for humorous image captioning.

| Pair ID | Comparison Objective |
|---|---|
| A vs B | Evaluate the benefit of few-shot prompting for humor captioning. |
| A vs C | Assess the impact of introducing humor theory. |
| B vs D | Explore the effect of combining theory with few-shot prompting. |
| C vs E | Analyze the gain from CoT + theory-guided humorous image captioning. |
| D vs F | Analyze the gain from combining CoT + theory-guided approach with few-shot prompting. |
| E vs F | Compare the contribution of few-shot prompting within theory-guided + CoT framework. |
| I vs A | Compare the overall improvement of HUMORCHAIN over the baseline. |
| I vs F | Analyze the differences between HUMORCHAIN and CoT-guided methods. |
| I vs G | Analyze the performance differences between HUMORCHAIN and CLoT. |
| I vs H | Evaluate the performance of HUMORCHAIN under OxfordTVG-HIC dataset conditions. |
| J vs A | Quantify the performance gain of theory-guided reasoning (without discriminator) over zero-shot baseline. |
| J vs F | Verify the superiority of pure theory-guided multi-stage reasoning over CoT-fused baselines (without discriminator). |
| J vs G | Compare the theory-guided framework (without discriminator) with the external CLoT model for humor generation. |
| J vs H | Evaluate the performance of HUMORCHAIN under OxfordTVG-HIC dataset conditions. |
| I vs J | Highlight the performance improvement brought by the discriminator and retry loop in HUMORCHAIN. |

**Data Sources** This study utilizes three categories of datasets to facilitate both internal and external comparative analyses. For all internal methods (A–F), the Meme-Image-No-Text dataset is employed to ensure a consistent evaluation setting for images. For cross-model comparisons, two external evaluation sets are constructed: Oogiri-GO (Group G) [47] and OxfordTVG-HIC (Group H) [20], with captions generated in parallel by HUMORCHAIN and the respective external systems. Detailed dataset configurations are provided in Appendix F.

A total of nine generation methods (A–I) were designed to systematically test different strategies for humor captioning, as shown in Table 2. Groups A–F are internal baselines developed in this study, while G (CLoT) and H (OxfordTVG-HIC) serve as external comparison models. I (Ours) corresponds to HUMORCHAIN, integrating theory-guided multi-stage reasoning and discriminator-based feedback.

**Experimental Design and Evaluation Metrics** Given the subjectivity of humorous image captioning, we adopt a complementary two-stage evaluation strategy, comprising Pairwise Comparison and Single-Title Evaluation. Detailed annotator instructions are provided in the Appendix H.

**(1) Pairwise Comparison** To systematically assess the relative performance of diverse generation strategies, ten comparison groups were constructed to cover all key variable combinations, as summarized in Table 1. Four metrics were derived from annotator judgments. Win Rate and Hard Win Rate quantify the proportion of preferred captions, with Hard Win Rate excluding ties. Significance tests assess the reliability of these differences. Additionally, the Bradley–Terry and Arena Elo [8] models are used to derive relative rankings.

**(2) Single-Caption Evaluation** Annotators independently rate each caption, using a binary label to assess its humor performance. In addition, we compute a series of automated metrics: Distinct-1/2 for lexical diversity [19], BERTScore for semantic similarity [46], CLIPScore [28] for visual–semantic alignment and incongruity, and Embedding Average (EA) and Greedy Matching (GM) [23] for sentence- and word-level semantic relevance. Together, these complementary metrics form a comprehensive evaluation framework for assessing models’ humor generation capabilities.

## 4.2. Experiment 2: Evaluation of the Humor Discriminator

**Comparison Before and After Fine-Tuning** We evaluated three discriminator variants on the validation set using identical, officially recommended generation parameters: 1) Baseline (un-tuned), 2) LoRA (binary classifier), 3) LoRA + Classifier Head (threshold = 0.66). This experiment demonstrates how humor dataset fine-tuning improves alignment with human preferences and shows the added flexibility from a trained classification head. We analyze confusion matrices and key metrics for each model.

**Impact on the Overall Pipeline** To assess the discriminator’s effect on pipeline performance, we compare the ratio of captions labeled as humorous in the fine-tuned dataset with the precision of LoRA + Classifier Head after integration. This directly reflects the discriminator’s impact on output quality. Confusion matrix metrics are also used to estimate the retry mechanism’s effect on inference cost.

**Comparison with Other Large Models** To further validate the fine-tuned discriminator’s advantages, we evaluate several larger closed-source LLMs on humor detection, including Gemini-2.5-Flash, GPT-4-1, and Claude-3-5-Haiku-20241022, using recommended parameters. As these models do not support training a classification head, we use a unified 0/1 binary classification with structured outputs. Metrics from Section 4.2 are used to ensure consistency in comparison.

# 5. Results and Discussion

## 5.1. Pairwise Comparison Analysis

As shown in Table 3 and Table 4, across all nine experimental configurations (A–J), the proposed HUMORCHAIN (Method I) achieves the best overall performance. In cross-model evaluations, HUMORCHAIN consistently outperforms CLoT (Group G) [47] and OxfordTVG-HIC (Group H) [20]. Notably, the ablation model J (without discriminator) also outperforms most baselines, validating the core



<!-- page 0007 -->

Table 2. Experimental method configurations (A–I) for humorous image captioning.

| Group | Strategy | Description |
|---|---|---|
| A | Zero-shot | Direct image captioning without examples or theoretical cues. |
| B | Few-shot | Incorporates example-based prompting with humor-style mimicry. |
| C | Rule-Based | References the four theories of humor (e.g., incongruity, violation). |
| D | Few-shot + Rule-Based | Combines examples with theoretical references to achieve structured prompts. |
| E | Rule-Guided + CoT | Adds Chain-of-Thought reasoning to theory-guided captioning. |
| F | Few-shot + Rule-Guided + CoT | Combines all strategies without explicit multi-stage orchestration. |
| G | External CLoT (SYSU) | Sun Yat-sen University’s CLoT model [47]. |
| H | External OxfordTVG-HIC | Oxford University dataset based on humor-labeled caption pairs [20]. |
| I (Ours) | Theory-Guided Multi-Stage Reasoning | Proposed HUMORCHAIN framework integrating cognitive humor theory, staged reasoning, and humor discrimination feedback. |
| J | Theory-Guided Multi-Stage Reasoning (without discriminator) | Proposed HUMORCHAIN framework with the humor discriminator and retry loop ablated, only retaining cognitive humor theory and staged reasoning. |

contribution of humor theory guidance. These results indicate HUMORCHAIN’s robustness in humorous caption generation.

Table 3. Pairwise win rate and significance analysis for humorous image captioning methods.

| Comparison | Total | Win Rate A | Win Rate B |
|---|---:|---:|---:|
| A vs B | 300 | 0.495 | 0.505 |
| A vs C | 300 | 0.502 | 0.498 |
| B vs D | 300 | 0.492 | 0.508 |
| C vs E | 300 | 0.465 | 0.535 |
| D vs F | 300 | 0.523 | 0.477 |
| E vs F | 300 | 0.482 | 0.518 |
| J vs A | 300 | 0.850 | 0.150 |
| J vs F | 300 | 0.830 | 0.170 |
| J vs G | 300 | 0.626 | 0.374 |
| J vs H | 300 | 0.788 | 0.212 |
| I vs A | 300 | 0.695 | 0.305 |
| I vs F | 300 | 0.680 | 0.320 |
| I vs G | 794 | 0.683 | 0.317 |
| I vs H | 1007 | 0.860 | 0.140 |
| I vs J | 300 | 0.745 | 0.255 |

In the comparison between A and I, the results show that explicit multi-stage reasoning and humor-mechanism modeling provide a substantial advantage in humor generation. The comparison between F and I further demonstrates that HUMORCHAIN markedly outperforms CoT-based approaches in both stability and humor coherence, underscoring that effective humor generation benefits not only from explicit knowledge but also from cognitive modeling embedded in the reasoning processes.

In cross-model and cross-dataset evaluations, HUMORCHAIN achieves consistently higher humor win rates in both I-vs-G and I-vs-H, indicating that Method I (Ours) maintains robust and stable humor performance across diverse conditions.

Regarding the Arena Elo (Elo) and Bradley–Terry (BT) scores (Table 4), Method I achieves the highest values on both metrics. The results further reveal a general trend in which model performance improves with increasing prompt complexity and reasoning depth. The A–C groups indicate that single-strategy enhancements yield limited gains, while implicit chain-of-thought methods (E, F) provide moderate improvements yet remain inferior to I (Ours). External models G (CLoT) and H (OxfordTVG-HIC) obtain comparatively lower scores. Overall, the global statistics reinforce HUMORCHAIN’s robustness and consistent superiority across diverse generation strategies.

Table 4. Global ranking metrics for humorous image captioning frameworks. Arena Elo and Bradley–Terry (BT) scores are calculated from all human comparison results.

| Framework | Elo | BT |
|---|---:|---:|
| I (Ours) | 1554.60 | 3.57 |
| F (Few-shot + CoT + Rule-Guided) | 1528.84 | 1.00 |
| E (CoT + Rule-Guided) | 1526.46 | 0.88 |
| D (Few-shot + Rule-Based) | 1505.43 | 0.73 |
| C (Rule-Based) | 1504.45 | 0.54 |
| A (Zero-shot) | 1498.09 | 0.52 |
| B (Few-shot) | 1495.05 | 0.46 |
| H (OxfordTVG-HIC) | 1467.40 | 0.55 |
| G (CLoT) | 1464.06 | 0.74 |

## 5.2. Single-Title Evaluation

Combining human humor ratings with multidimensional automated metrics, a comprehensive assessment of humor quality, lexical diversity, and semantic distinctiveness was conducted (Table 5). I (Ours) (0.810) significantly outperforms all baselines, while combined strategies (D, E, F) show similar performance within the 0.38–0.40 range, indicating limited gains from integrating implicit reasoning and few-shot prompting. The external model G (0.195) performs notably worse, reflecting restricted humor generation.

Across automated metrics, I (Ours) achieves the best CLIPScore, EA-Rev, and BERT Cross Score, demonstrating stronger contrast, unexpectedness, and semantic creativity in image–text relations, consistent with incongruity-based humor mechanisms. Although G shows higher GM-Rev, suggesting more novel word usage, the overall trends are consistent: HUMORCHAIN enhances incongruity and creativity while maintaining visual–semantic relevance, achieving the strongest performance along the “unexpectedness–humor” dimension.

## 5.3. Evaluation of the Humor Discriminator

**Comparison Before and After Fine-Tuning**

Fine-tuning with LoRA and adding a classification head both lead to substantial improvements in key metrics such as accuracy and precision (see Table 6). These enhancements demonstrate that the model’s humor detection capability is significantly strengthened through targeted training and threshold adjustment.



<!-- page 0008 -->

Table 5. Single-Title Evaluation results for humorous image captioning. Metrics include human humor score, CLIPScore, Embedding Average (EA-Rev), Greedy Matching (GM-Rev), Distinct-1/2, and BERT Cross Score.

| Framework | Humor Mean | CLIPScore | EA-Rev | GM-Rev | Distinct-1 | Distinct-2 | BERT Cross Score |
|---|---:|---:|---:|---:|---:|---:|---:|
| A (Zero-shot) | 0.412 | 0.630 | 0.567 | 0.458 | 0.804 | 0.988 | 0.837 |
| B (Few-shot) | 0.418 | 0.630 | 0.560 | 0.458 | 0.757 | 0.966 | 0.833 |
| C (Rule-Based) | 0.362 | 0.630 | 0.578 | 0.463 | 0.795 | 0.980 | 0.837 |
| D (Few-shot + Rule-Based) | 0.394 | 0.626 | 0.609 | 0.470 | 0.728 | 0.965 | 0.836 |
| E (CoT + Rule-Guided) | 0.382 | 0.629 | 0.557 | 0.457 | 0.750 | 0.965 | 0.838 |
| F (Few-shot + CoT + Rule-Guided) | 0.398 | 0.625 | 0.622 | 0.466 | 0.720 | 0.937 | 0.837 |
| G (CLoT) | 0.195 | 0.636 | 0.731 | 0.546 | 0.377 | 0.725 | 0.836 |
| I (Ours) | 0.810 | 0.618 | 0.765 | 0.521 | 0.808 | 0.965 | 0.832 |

Table 6. Humor discriminator precision performance comparison.

| Model | Precision |
|---|---:|
| Baseline | 0.523 |
| LoRA | 0.636 |
| LoRA + Classifier (thr = 0.66) | **0.670** |

**Impact on Pipeline Performance**

As shown in Table 7, introducing the discriminator significantly increases the proportion of humorous outputs and overall caption quality, while maintaining a reasonable inference cost. The improved precision means users are much more likely to receive genuinely humorous outputs, representing a substantial gain in user experience. The retry mechanism ensures users receive high-quality captions, and parallel generation can further optimize efficiency.

Table 7. Impact of the humor discriminator on pipeline output quality and inference cost.

| Metric | Before Discriminator | After Discriminator (LoRA + Classifier) |
|---|---:|---:|
| Proportion of Humorous Outputs | 45.1% | **67.0%** |
| Acceptance Rate (Positive Pred.) | – | 36.5% |
| Avg. Generations per Accepted Caption | – | 2.74× |
| Precision Improvement △ | – | **+22%** |

**Comparison with Other LLMs**

As shown in Table 8, closed-source LLMs tend to overestimate humor, resulting in low precision. This means that simply integrating a larger or closed-source LLM does not effectively improve output quality. In contrast, our fine-tuned discriminator provides substantial gains in both accuracy and efficiency, highlighting its essential role in the pipeline.

Table 8. Comparison of humor detection performance across LLMs.

| Model | TP | TN | FP | FN | Positive Rate (%) | Precision |
|---|---:|---:|---:|---:|---:|---:|
| Gemini-2.5-Flash | 119 | 9 | 137 | 1 | 96.2 | 0.465 |
| GPT-4.1 | 111 | 23 | 123 | 9 | 87.9 | 0.474 |
| Claude-3.5-Haiku-20241022 | 116 | 10 | 136 | 4 | 94.7 | 0.460 |
| Qwen3-VL-4B-Instruct<br>(LoRA + Cls) | 65 | 114 | 32 | 55 | **36.5** | **0.670** |

## 5.4. Summary and Discussion

Our experiments show that relying solely on zero-shot prompting, few-shot prompting, theory-guided prompts, or chain-of-thought reasoning does not substantially improve humorous caption generation. HUMORCHAIN’s explicit multi-stage reasoning pipeline integrates core mechanisms from humor studies and psychology—such as incongruity, creativity, and cognitive consistency—into the generation process, enabling the model to produce more diverse and unexpected humorous content than traditional approaches.

In addition, the fine-tuned discriminator plays a crucial role in filtering and optimizing outputs, significantly increasing the proportion of captions perceived as humorous (from 45% to 67%). This targeted discrimination step ensures that generated captions better align with human humor perception and expectations.

These results confirm that integrating structured reasoning and targeted discrimination is essential for generating high-quality humorous content.

## 6. Conclusion

Grounded in humor and psychological theories, HUMORCHAIN integrates multi-stage reasoning with a targeted discriminator to provide a structured and interpretable framework for humor generation. The reasoning pipeline explicitly translates core mechanisms from humor and psychological theories into actionable steps, driving creative and diverse output, while the discriminator ensures quality and alignment with human expectations.

Experiments demonstrate that HUMORCHAIN achieves consistent improvements over mainstream methods, particularly in interpretability and reasoning transparency. Its parameterized theoretical components and lightweight adaptation module also show promising potential for cross-lingual and cross-cultural transfer, enabling personalized, culture-aware, and context-aware generation. Beyond humor, the theory-driven, structured reasoning paradigm offers a universal approach for creative language tasks, such as satire and metaphor, and a general direction for multimodal generation with less data and greater control. HUMORCHAIN’s contribution lies in its theory-driven approach to structured reasoning and generation. While our framework demonstrates strong performance and improved interpretability, future work will focus on expanding its applicability to broader creative language tasks and addressing challenges in subjective evaluation and cultural adaptation.



<!-- page 0009 -->

## References

[1] Huda Diab Abdulgaliil and Otman A Basir. Next-generation image captioning: A survey of methodologies and emerging challenges from transformers to multimodal large language models. *Natural Language Processing Journal*, page 100159, 2025. 1

[2] Salvatore Attardo and Victor Raskin. Script theory revis(it)ed: Joke similarity and joke representation model. 1991. 3

[3] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, Wenbin Ge, Zhifang Guo, Qidong Huang, Jie Huang, Fei Huang, Binyuan Hui, Shutong Jiang, Zhaohai Li, Mingsheng Li, Mei Li, Kaixin Li, Zicheng Lin, Junyang Lin, Xuejing Liu, Jiawei Liu, Chenglong Liu, Yang Liu, Dayiheng Liu, Shixuan Liu, Dunjie Lu, Ruilin Luo, Chenxu Lv, Rui Men, Lingchen Meng, Xuancheng Ren, Xingzhang Ren, Sibo Song, Yuchong Sun, Jun Tang, Jianhong Tu, Jianqiang Wan, Peng Wang, Pengfei Wang, Qiuyue Wang, Yuxuan Wang, Tianbao Xie, Yiheng Xu, Haiyang Xu, Jin Xu, Zhibo Yang, Mingkun Yang, Jianxin Yang, An Yang, Bowen Yu, Fei Zhang, Hang Zhang, Xi Zhang, Bo Zheng, Humen Zhong, Jingren Zhou, Fan Zhou, Jing Zhou, Yuanzhi Zhu, and Ke Zhu. Qwen3-vl technical report, 2025. 2

[4] Davide Caffagni, Federico Cocchi, Luca Barsellotti, Nicholas Moratelli, Sara Sarto, Lorenzo Baraldi, Lorenzo Baraldi, Marcella Cornia, and Rita Cucchiara. The revolution of multimodal large language models: A survey, 2024. 3

[5] Hui Cai and Xing Yin. A review of western humor theories. *Foreign Language Research*, 2005. in Chinese. 3

[6] Yuyan Chen, Songzhou Yan, Zhihong Zhu, Zhixu Li, and Yanghua Xiao. Xmemecap: Meme caption generation with sub-image adaptability. In *Proceedings of the 32nd ACM International Conference on Multimedia*, pages 3352–3361, 2024. 3

[7] Can Cui, Yunsheng Ma, Xu Cao, Wenqian Ye, Yang Zhou, Kaizhao Liang, Jintai Chen, Juanwu Lu, Zichong Yang, Kuei-Da Liao, Tianren Gao, Erlong Li, Kun Tang, Zhipeng Cao, Tong Zhou, Ao Liu, Xinrui Yan, Shuqi Mei, Jianguo Cao, Ziran Wang, and Chao Zheng. A survey on multimodal large language models for autonomous driving, 2023. 3

[8] Arpad E Elo and Sam Sloan. The rating of chessplayers: Past and present. *(No Title)*, 1978. 6

[9] Sigmund Freud. *Jokes and their relation to the unconscious*. WW Norton & Company, 1960. 1, 2, 3, 4

[10] Yuncheng Guo and Xiaodong Gu. Mmrl: Multi-modal representation learning for vision-language models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 25015–25025, 2025. 3

[11] Longzhen Han, Awes Mubarak, Almas Baimagambetov, Nikolaos Polatidis, and Thar Baker. Multimodal large language models: A survey. *arXiv preprint arXiv:2506.10016*, 2025. 3

[12] Md Kamrul Hasan, Wasifur Rahman, AmirAli Bagher Zadeh, Jianyuan Zhong, Md Iftekhar Tanveer, Louis-Philippe Morency, and Mohammed Ehsan Hoque. Ur-funny: A multimodal language dataset for understanding humor. In *Proceedings of the 2019 conference on empirical methods in natural language processing and the 9th international joint conference on natural language processing (EMNLP-IJCNLP)*, pages 2046–2056, 2019. 3

[13] David Heyd. The place of laughter in hobbes’s theory of emotions. *Journal of the History of Ideas*, pages 285–295, 1982. 1, 2, 3, 4

[14] Jiaxing Huang and Jingyi Zhang. A survey on evaluation of multimodal large language models, 2024. 3

[15] Yizhang Jin, Jian Li, Yexin Liu, Tianjun Gu, Kai Wu, Zhengkai Jiang, Muyang He, Bo Zhao, Xin Tan, Zhenye Gan, Yabiao Wang, Chengjie Wang, and Lizhuang Ma. Efficient multimodal large language models: A survey, 2024. 3

[16] Antonios Kalloniatis and Panagiotis Adamidis. Computational humor recognition: a systematic literature review. *Artificial Intelligence Review*, 58(2):43, 2024. 1

[17] Sean Kim and Lydia B Chilton. Ai humor generation: Cognitive, social and creative skills for effective humor. *arXiv preprint arXiv:2502.07981*, 2025. 1

[18] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. *Advances in neural information processing systems*, 35:22199–22213, 2022. 3

[19] Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, and William B Dolan. A diversity-promoting objective function for neural conversation models. In *Proceedings of the 2016 conference of the North American chapter of the association for computational linguistics: human language technologies*, pages 110–119, 2016. 6

[20] Runjia Li, Shuyang Sun, Mohamed Elhoseiny, and Philip Torr. Oxfordtvg-hic: Can machine make humorous captions from images? In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 20293–20303, 2023. 1, 2, 3, 6, 7

[21] Zongxia Li, Xiyang Wu, Hongyang Du, Fuxiao Liu, Huy Nghiem, and Guangyao Shi. A survey of state of the art large vision language models: Alignment, benchmark, evaluations and challenges. *arXiv preprint arXiv:2501.02189*, 2025. 3

[22] Chia Xin Liang, Pu Tian, Caitlyn Heqi Yin, Yao Yua, Wei An-Hou, Li Ming, Tianyang Wang, Ziqian Bi, and Ming Liu. A comprehensive survey and guide to multimodal large language models in vision-language tasks. *arXiv preprint arXiv:2411.06284*, 2024. 3

[23] Chia-Wei Liu, Ryan Lowe, Iulian Vlad Serban, Mike Noseworthy, Laurent Charlin, and Joelle Pineau. How not to evaluate your dialogue system: An empirical study of unsupervised evaluation metrics for dialogue response generation. In *Proceedings of the 2016 conference on empirical methods in natural language processing*, pages 2122–2132, 2016. 6

[24] A Peter McGraw and Caleb Warren. Benign violations: Making immoral behavior funny. *Psychological science*, 21(8):1141–1149, 2010. 1, 2, 3, 4

[25] Chancharik Mitra, Brandon Huang, Tianning Chai, Zhiqiu Lin, Assaf Arbelle, Rogerio Feris, Leonid Karlinsky, Trevor Darrell, Deva Ramanan, and Roei Herzig. Enhancing few-shot vision-language classification with large multimodal model features, 2025. 3



<!-- page 0010 -->

[26] Ivona Najdenkoska, Xiantong Zhen, and Marcel Worring. Meta learning to bridge vision and language models for multimodal few-shot learning. *arXiv preprint arXiv:2302.14794*, 2023. 3

[27] Jerry Palmer. *Taking humour seriously*. Routledge, 2003. 3

[28] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In *International conference on machine learning*, pages 8748–8763. PmLR, 2021. 6

[29] Victor Raskin. Semantic theory of humor. In *Semantic mechanisms of humor*, pages 99–147. Springer, 1985. 3

[30] Graeme Ritchie. *The linguistic analysis of jokes*. Routledge, 2004. 3

[31] Aadhavan Sadasivam, Kausic Gunasekar, Hasan Davulcu, and Yezhou Yang. Memebot: Towards automatic image meme generation. *arXiv preprint arXiv:2004.14571*, 2020. 3

[32] Shezheng Song, Xiaopeng Li, Shasha Li, Shan Zhao, Jie Yu, Jun Ma, Xiaoguang Mao, and Weimin Zhang. How to bridge the gap between modalities: A comprehensive survey on multimodal large language model. *arXiv preprint arXiv:2311.07594*, 2023. 3

[33] Shezheng Song, Xiaopeng Li, Shasha Li, Shan Zhao, Jie Yu, Jun Ma, Xiaoguang Mao, Weimin Zhang, and Meng Wang. How to bridge the gap between modalities: Survey on multimodal large language model. *IEEE Transactions on Knowledge and Data Engineering*, 2025. 3

[34] Herbert Spencer and Herbert Spencer. *The principles of psychology*. Williams and Norgate London, 1870. 3, 4

[35] Jerry M Suls. A two-stage model for the appreciation of jokes and cartoons: An information-processing analysis. *The psychology of humor: Theoretical perspectives and empirical issues*, 1:81–100, 1972. 1, 2, 3

[36] Victor PL Varela, Alice Towler, Richard I Kemp, and David White. Looking at faces in the wild. *Scientific Reports*, 13(1):783, 2023. 2, 4

[37] Han Wang and Roy Ka-Wei Lee. Memecraft: Contextual and stance-driven multimodal meme generation. In *Proceedings of the ACM Web Conference 2024*, pages 4642–4652, 2024. 2

[38] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022. 3

[39] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022. 3

[40] Orion Weller and Kevin Seppi. Humor detection: A transformer gets the last laugh. *arXiv preprint arXiv:1909.00252*, 2019. 3

[41] Jiayang Wu, Wensheng Gan, Zefeng Chen, Shicheng Wan, and Philip S Yu. Multimodal large language models: A survey. In *2023 IEEE International Conference on Big Data (BigData)*, pages 2247–2256. IEEE, 2023. 3

[42] Junda Wu, Hanjia Lyu, Yu Xia, Zhehao Zhang, Joe Barrow, Ishita Kumar, Mehrnoosh Mirtaheri, Hongjie Chen, Ryan A. Rossi, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, Jiuxiang Gu, Nesreen K. Ahmed, Yu Wang, Xiang Chen, Hanieh Deilamsalehy, Namyong Park, Sungchul Kim, Huanrui Yang, Subrata Mitra, Zhengmian Hu, Nedim Lipka, Dang Nguyen, Yue Zhao, Jiebo Luo, and Julian McAuley. Personalized multimodal large language models: A survey, 2024. 3

[43] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. *arXiv preprint arXiv:2505.09388*, 2025. 2, 4

[44] Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. A survey on multimodal large language models. *National Science Review*, 11(12):nwae403, 2024. 3

[45] Francisco Yus. Incongruity-resolution humorous strategies in image macro memes. *Internet Pragmatics*, 4(1):131–149, 2021. 2, 4

[46] T Zhang, V Kishore, F Wu, KQ Weinberger, and Y Artzi. Bertscore: Evaluating text generation with bert. iclr 2020. *arXiv preprint arXiv:1904.09675*, 2020. 6

[47] Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, and Pan Zhou. Let’s think outside the box: Exploring leap-of-thought in large language models with creative humor generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 13246–13257, 2024. 2, 3, 6, 7



<!-- page 0011 -->

# HUMORCHAIN: Theory-Guided Multi-Stage Reasoning for Interpretable Multimodal Humor Generation

## Supplementary Material

## A. Limitations

Although HUMORCHAIN is grounded in four foundational humor theories—Incongruity–Resolution, Benign Violation, Superiority, and Relief—its theoretical coverage remains incomplete. More recent frameworks and multidisciplinary perspectives have not yet been systematically integrated, and certain forms of humor (e.g., culturally embedded irony or reference-dependent implicit jokes) may therefore be underrepresented or insufficiently captured. However, the modular design of our Theory-Guided Multi-Stage Reasoning Framework enables us to incorporate new generation strategies with only modification of generation prompts, which highlights the flexibility of our framework. In future works, we plan to incorporate and compare additional humor theories to further strengthen the theoretical grounding of the reasoning module and to more comprehensively cover diverse humor phenomena. Humor theory-guided reasoning is inherently unable to cover all humor phenomena exhaustively, which also reflects the inherent limitation of theory-guided Chain-of-Thought reasoning; future practical deployment will therefore focus on balancing the comprehensiveness of humor theory integration and the computational complexity of the reasoning system.

Moreover, humor is inherently subjective: even for the same joke or image caption, differences in cultural background, linguistic experience, and personal preference can lead to markedly different perceptions of funniness. Although we employ pairwise comparisons and binary annotations to approximate consensus-style labels and train the discriminator accordingly, the current framework remains biased toward captions that appeal to the majority rather than modeling individual humor preferences in a fine-grained manner. Future work will explore the integration of personalization signals and user modeling to better capture such subjective variability.

## B. Validation of Selected Humor Theories

We validate the four adopted humor theories (Incongruity–Resolution, Benign Violation, Superiority, Relief) via quantitative analysis of 100 OxfordTVG-HIC samples, finding they apply to 86% of cases (72% with a single dominant theory), verifying their universality for multimodal humor. Statistical analysis of 25% of our generated captions shows the four corresponding generation strategies distribute as: Absurdity (26.9%), Contrast Irony (22.6%), Emotion Analogy (29.2%), Object Analogy (21.2%)—no over-reliance on a single strategy, and strategy selection has no significant correlation with humor quality.

## C. Analysis of Failure Cases

To provide intuitive insights into the limitations of our framework, we present representative failure cases in Figure 4. As observed from the failure cases, the underperformance primarily stems from two core issues: 1) inadequate image descriptions that fail to capture key contextual cues or emotional nuances critical for humor construction; 2) non-incongruous images lacking direct semantic-humor links, where the visual content itself provides limited basis for triggering humorous associations. These observations inspire future exploration of more sophisticated humor mechanisms in cross-modal or weak-semantic connection settings.

[Figure: Representative failure cases with three input images on the left and generated/ground-truth captions on the right. Readable text: “PowerPoint assassin vibes / License to Nerd”; “Safety First / Bond? No, Bob.”; “gt: I got it as a memento of my resignation!”; “Like my optimism on caffeine / Sky, hold my scarf!”; “Living my best fall / Missed the bus!”; “gt: A spectacular jump! And from the warp... a mid-ocean roll!”; “Peak productivity, obviously / Pit stop on a lunch break”; “Big meeting today / Pit stop panic—like me parallel parking.”; “gt: Mm-hmm. I’ll buy it.”]

Figure 4. Representative failure cases. Left: Input images; Right: Humorous captions generated by HUMORCHAIN (top lines) and the bolded ground truth (GT) captions from the dataset (bottom line), where GTs are more contextually aligned and humorous.

## D. On the Robustness of HUMORCHAIN

Although the multi-stage architecture of HUMORCHAIN can in principle propagate early misjudgments to downstream stages, we argue that such structural error accumulation is, to a large extent, controllable and acceptable within our framework. In practice, many failure cases originate from images that are inherently ambiguous, for which multiple, equally plausible interpretations exist. To handle these cases, HUMORCHAIN does not strictly adhere to a single deterministic reasoning pipeline. Instead, it leverages the fine-tuned humor discriminator to evaluate the generated image–caption pairs; when a caption is predicted as non-humorous, the system rolls back to the intermediate decision stage, revisits the choice of reasoning path, and regenerates captions along an alternative route. This iterative “Generate–Evaluate–Revise” loop effectively serves as a form of structural regularization: it enables



<!-- page 0012 -->

the model to escape locally inconsistent reasoning trajectories and reduces the impact of early-stage errors on the final output. Although this mechanism does not completely eliminate all forms of error propagation, our experimental results indicate that, in the context of humorous image captioning, it substantially alleviates the practical consequences of structural error accumulation. We further verified the framework’s robustness with two experiments (n=100 each). First, paraphrased prompts without the discriminator yield win rates of 0.725 (vs. A) and 0.475 (vs. J), confirming prompt stability. Second, on Qwen3-VL-235B-A22B-Instruct [3], J outperforms A with a 0.74 win rate, validating our backbone-agnostic design.

### E. Comparison of Generated Humorous Titles by Different Strategies

To further demonstrate the advantages of HUMORCHAIN in generating humorous titles for real-world images and facilitate a clearer assessment of its stylistic characteristics and performance strengths, we present qualitative comparisons across multiple generation strategies with images across diverse visual contexts. Table 9 summarizes methodological configurations for all evaluated approaches.

[Figure: small image of a cat among penguins, with candidate humorous titles listed.]

- **A** Undercover housecat infiltrates penguin committee.
- **B** Undercover kitty infiltrates the penguin colony.
- **C** Purr-guin reporting for fish duty.
- **D** I thought “penguin suit” was a membership requirement.
- **E** Tuxedo cat takes the penguin dress code way too literally.
- **F** When the tuxedo cat crashes a tuxedo convention.
- **G** My cat is not happy about the penguin's company
- **I** First day at a new school.

[Figure: small image of soccer players falling on a field, with candidate humorous titles listed.]

- **A** When gravity joins the starting lineup.
- **B** New formation: 4-4-fall.
- **C** Synchronized falling: World Cup edition.
- **D** Coach said fall back; they took it literally.
- **E** When a gentle pat triggers a season-ending flop.
- **F** Minimal contact, maximum theater.
- **G** I was at the 2008 Beijing Olympics, and I have to say, the Nigerians are pretty tough.
- **I** Group Project Chaos.

[Figure: cartoon face inside a target/crosshair, with candidate humorous titles listed.]

- **A** Targeted Ads Take Things Personally.
- **B** When the selfie app adds terrifying autofocus.
- **C** Autofocus thinks my face is a bullseye.
- **D** When the camera’s autofocus has trust issues.
- **E** When the eye test escalates to boss battle.
- **F** When the eye exam escalates quickly.
- **G** I'm not sure if I should go to the doctor or just keep taking the pills.
- **I** When the pop quiz picks you.

[Figure: small image of a dog on a beach, with candidate humorous titles listed.]

- **A** Baywatch: Mossy Dog Edition.
- **B** Seadog on shore leave, reconsidering life choices.
- **C** Mossy beach dog, waiting for the tide to fetch.
- **D** Beach lifeguard took doggy paddle too literally.
- **E** Beach day, but the mascot brought snow boots.
- **F** Beach day, but the lifeguard is a confused shag rug.
- **G** A dog in a costume standing on the beach
- **I** When your Zoom background glitches IRL.



<!-- page 0013 -->

Table 9. Experimental method configurations (A–I) for humorous image captioning.

| Group | Strategy | Description |
|---|---|---|
| A | Zero-shot | Direct image captioning without examples or theoretical cues. |
| B | Few-shot | Incorporates example-based prompting with humor-style mimicry. |
| C | Rule-Based | References the four theories of humor (e.g., incongruity, violation). |
| D | Few-shot + Rule-Based | Combines examples with theoretical references to achieve structured prompts. |
| E | Rule-Guided + CoT | Adds Chain-of-Thought reasoning to theory-guided captioning. |
| F | Few-shot + Rule-Guided + CoT | Combines all strategies without explicit multi-stage orchestration. |
| G | External CLoT (SYSU) | Sun Yat-sen University’s CLoT model [47]. |
| I (Ours) | Theory-Guided Multi-Stage Reasoning | Proposed HUMORCHAIN framework integrating cognitive humor theory, staged reasoning, and humor discrimination feedback. |

[Figure: Example caption comparison for an image of a damaged/ruined McDonald’s-like scene. A: “Grand Reopening: Now Serving McRubble.” B: “Now serving: McRubble with fries.” C: “Now serving deconstructed Happy Meals.” D: “Grand reopening: minimalist edition.” E: “McDonald's introduces open-air dining.” F: “Now serving rubble with a smile.” G: “The clown is a 100% employee.” I: “Cheerful while layoffs happen.”]

[Figure: Example caption comparison for an image of a child in striped pants kicking a ball. A: “Wind-up complete: ball deeply concerned.” B: “Kickoff, but make it dramatic.” C: “Karate warmup for a three-pointer.” D: “Penalty kick, wrong ball, right attitude.” E: “Coach said any ball—challenge accepted.” F: “Bend It Like Shaq.” G: “A boy in striped pants kicking a ball” I: “Future MVP, Today’s Trip Hazard”]

## F. Data sources

**Evaluation of the Theory-Guided Multi-Stage Reasoning Framework.** The datasets in this study are sourced from three different sources, aiming to support both internal method comparisons and external benchmark evaluations:

• **Primary Dataset – Meme-Image-No-Text:** Used for all internal comparisons (Methods A–F). This dataset consists of humor-related images without textual interference, covering diverse visual scenes. All images were manually screened to ensure neutrality and minimize cultural ambiguity, ensuring fair and consistent evaluation.

• **External Dataset 1 – Oogiri-GO:** Used for direct comparison with the CLoT model (Group G) [47]. We randomly sample images from its publicly available Oogiri-GO dataset. Captions for these images are generated separately by HUMORCHAIN and CLoT, forming the Method I (Ours) vs. Group G (CLoT) comparison group, along with independent per-caption scoring data.

• **External Dataset 2 – OxfordTVG-HIC:** Used to evaluate cross-cultural robustness (Group H) [20]. Since the official Oxford implementation was not publicly released, we generated new captions using HUMORCHAIN on randomly sampled images and compared them against existing humorous captions from OxfordTVG-HIC.

**Training of the Humor Discriminator.** We generate titles for images sourced from the aforementioned datasets with the Theory-Guided Multi-Stage Reasoning Framework, and randomly sample picture-title pairs for human annotation. For details of human annotations and datasets, see H and I.

## G. Token Consumption and Computational Cost Statistics

Table 10 reports the token consumption and cost without the discriminator module, calculated based on the official token pricing of the backbone model (GPT-5-2025-08-07) with 100 samples.

## H. Volunteer Annotation Guidelines

We provide standardized instructions for volunteers participating in the humor caption evaluation study. The goal is to ensure consistent and high-quality annotations across all evaluators.

### H.1. Task Overview

Two types of annotation tasks are included:

1. **Pairwise Comparison:** Volunteers are presented with the same image and two captions generated by different models. They must determine which caption is funnier or indicate a tie.

2. **Single-Title Evaluation:** Volunteers are presented with an image and a single caption, and must provide a binary judgment of whether it is humorous (1) or not humorous (0).



<!-- page 0014 -->

Table 10. Average I/O Token Consumption and Cost for Caption Generation Methods (n=100).

| Method | Avg. Input Tokens | Avg. Output Tokens | Avg. Cost ($) |
|---|---:|---:|---:|
| A (Zero-shot) | 398.15 | 16.65 | 0.0007 |
| B (Few-shot) | 492.00 | 16.40 | 0.0008 |
| C (Rule-Based) | 500.00 | 17.60 | 0.0008 |
| D (Few-shot + Rule-Based) | 619.00 | 16.75 | 0.0009 |
| E (Rule-Guided + CoT) | 377.00 | 683.00 | 0.0073 |
| F (Few-shot + Rule-Guided + CoT) | 438.00 | 686.00 | 0.0074 |
| HUMORCHAIN (without discriminator) | 2344.00 | 529.00 | 0.0082 |

## H.2. Definition of Humor (Reference Only)

In this study, “humor” refers broadly to any linguistic expression that elicits mild amusement, surprise, or a sense of wit. Humor may arise from:

- **Incongruity:** contrast or violation of expectation;
- **Benign Violation:** mild and non-harmful rule breaking;
- **Superiority:** self-deprecation or a mild sense of advantage;
- **Relief:** emotional release or tension resolution.

Annotators are not required to master these theories but may find them helpful as conceptual references.

## H.3. Pairwise Comparison Guidelines

For each sample, volunteers will see:

- the same image, and
- two captions, labeled A and B.

Annotators must choose one of the following options:

- **A is funnier** — Caption A is clearly funnier than B, with stronger contrast, more clever expression, makes you more amused, and **feels more like a natural human joke**;
- **B is funnier** — Caption B meets the same criteria above;
- **TIE** — Both captions are humorous and similar in quality;
- **Both Not Funny** — Neither caption is humorous.

**Evaluation Criteria**

- Each decision should reflect your genuine subjective impression.
- “Both Not Funny” applies when neither caption reaches your minimum threshold of humor.

**Avoid the Following**

- Do not attempt to keep scores “balanced” across tasks.
- Do not be influenced by earlier tasks or other annotators.

## H.4. Single-Title Evaluation Guidelines

For each sample, annotators see an image and one caption, and must assign:

**1 = Humorous, 0 = Not Humorous**

**Choose 1 (Humorous) when the caption:**

- feels amusing, lighthearted, surprising, or incongruous;
- evokes mild emotional reactions (e.g., smiling, a sense of wit);
- exhibits clear humorous logic (e.g., reversal, misunderstanding, analogy, exaggeration);
- **resembles a natural human joke and does not feel awkward or forced.**

**Choose 0 (Not Humorous) when the caption:**

- is purely descriptive with no attempt at humor;
- contains no contrast, wit, or playful intent;
- is confusing or incoherent such that humor cannot be perceived;
- feels unnatural, awkward, or far from how humans typically express humor.

## H.5. Annotation Protocol and Conduct

1. Carefully read this guideline document before starting the evaluation.
2. Complete all judgments independently, without discussing answers with others.
3. If a sample is difficult to judge, make your best subjective decision and move on; you may revisit later if needed.
4. Do not allow others’ opinions to affect your rating.
5. Cultural or personal differences in humor are expected; simply annotate according to your own interpretation.

## H.6. Post-Evaluation Discussion

After all annotations are completed, a group discussion may be held to gather feedback regarding:

- the clarity of task rules,
- the presence of ambiguous samples,
- possible improvements to the annotation process.

This discussion is for refinement only and must not alter previously submitted judgments.

## H.7. Summary

- Humor is subjective; your genuine impression is the primary criterion.
- Treat each evaluation independently.
- A caption that feels like a natural human joke is more likely to be humorous.



<!-- page 0015 -->

## I. Fine-Tuning Dataset Statistics

The humor preference dataset contains a total of 5,320 image–caption pairs, with 2,511 positive samples and 2,809 negative samples. The training set includes 5,054 samples (2,391 positive, 2,663 negative), and the validation set contains 266 samples (120 positive, 146 negative).

## J. Technical Details on Fine-Tuning and Classification Head Training

### J.1. LoRA Parameter Settings

For LoRA fine-tuning, the following parameters are used:

- `dtype: torch.bfloat16`
- `r: 8`
- `lora_alpha: 32`
- `target_modules: ["q_proj", "k_proj", "v_proj","o_proj","qkv","proj"]`
- `lora_dropout: 0.05`
- `bias: "none"`

### J.2. SFT Stage LoRA Fine-Tuning

Supervised fine-tuning (SFT) with LoRA uses the following settings:

- `dtype: torch.bfloat16`
- `BATCH_SIZE: 1`
- `GRAD_ACCUM: 8`
- `EPOCHS: 3`
- `LR: 2e-4`

### J.3. Classifier Head Structure and Training

The RoBERTa-like classifier is trained with:

- `dtype: torch.bfloat16`
- `BATCH_SIZE: 16`
- `GRAD_ACCUM: 1`
- `EPOCHS: 3`
- `LR: 5e-4`

The classifier head structure is as follows (input: EOS hidden state):

    self.norm = nn.LayerNorm(self.hidden_size)
    self.classifier = nn.Sequential(
        nn.Dropout(0.1),
        nn.Linear(self.hidden_size,
            self.hidden_size),
        nn.Tanh(),
        nn.Dropout(0.1),
        nn.Linear(self.hidden_size, 1)
    )

## K. Generation Parameters

### K.1. Theory-Guided Multi-Stage Reasoning Framework (GPT-5-2025-08-07)

- A. Image Description  
  – temperature: 0.2  
  – max_tokens: 4000
- B. Strategy Judgment  
  – temperature: 0.1  
  – max_tokens: 4000
- C1. Object Analogy  
  – temperature: 0.9  
  – max_tokens: 4000
- C2. Absurdity  
  – temperature: 0.8  
  – max_tokens: 4000
- C3. Contrast Irony  
  – temperature: 0.9  
  – max_tokens: 4000
- C4. Emotion Analogy  
  – temperature: 0.85  
  – max_tokens: 4000
- D. Safety Classifier  
  – temperature: 0.1  
  – max_tokens: 4000

### K.2. Humor Discriminator (Qwen3-VL-4B-Instruct)

- `greedy: false`
- `seed: 3407`
- `top_p: 0.8`
- `top_k: 20`
- `temperature: 0.7`
- `repetition_penalty: 1.0`
- `presence_penalty: 1.5`
- `out_seq_length: 32768`

## L. Prompts

### L.1. Theory-Guided Multi-Stage Reasoning Framework

#### L.1.1. Stage 1: Image Description

You are an image describer.

1. **Objective**  
Please objectively and thoroughly describe the visible content of the image.

2. **Scope**  
- Main subjects  
- State/emotions  
- Scene  
- Actions  
- Text (if clearly readable)  
- Significant details

#### L.1.2. Stage 2: Strategy Judgment

You are an evaluator of ”reasonableness and humorous incongruity points”.



<!-- page 0016 -->

Make judgments based only on the given textual description, without introducing external image information or fabricating details.

1. **Task**  
Please assess plausibility (real–world possibility/commonality) as follows:

- common: The situation is entirely reasonable with no particular oddities.
- plausible: Overall reasonable, though not everyday, it is possible in real life without violating common sense or physical laws.
- rare: Very uncommon or unusual, but might happen under extreme/special conditions.
- implausible: Impossible or violates objective laws.

2. **Outputs**  
Also, provide the following:

- plausibility: Values: common | plausible | rare | implausible
- incongruity_for_humor: Whether there is obvious incongruity/discord/semantic conflict/personification that could cause humor. Values: true | false
- has_human_or_animal_or_cartoon: Whether the description contains people, animals, or cartoon characters (including comic/animation characters/dolls with anthropomorphic traits). Values: true | false
- reasons: A concise list of 2–5 reasons supporting the above judgments, each <= 20 words

3. **Few-shot Examples (flat list)**  
FEWSHOT EXAMPLES:

- Example 1: Hotpot in Office -> Rare but possible, and humorous incongruity; contains humans  
user: ”Description: Employees are projecting a PowerPoint in a meeting room, while a hotpot is being cooked in the middle of the meeting table surrounded by ingredients.”  
assistant.plausibility: ”rare”  
assistant.incongruity_for_humor: true  
assistant.has_human_or_animal_or_cartoon: true  
assistant.reasons:  
- ”Office setting misused for cooking”  
- ”Food and electronics create contrast”  
- ”Presence of ’employees’ as characters”

- Example 2: Samurai Scanning QR Code in Subway -> Rare, humorous incongruity (mismatch of time/space); contains humans  
user: ”Description: A samurai in ancient armor scans a QR code at a modern subway entrance.”  
assistant.plausibility: ”implausible”  
assistant.incongruity_for_humor: true  
assistant.has_human_or_animal_or_cartoon: true  
assistant.reasons:  
- ”Contrast between ancient armor and modern facilities”  
- ”Time/space mismatch creates dramatic effect”  
- ”Samurai as a human character”

- Example 3: Waiter Serving Food in a Regular Restaurant -> Common, no humor incongruity; contains humans  
user: ”Description: In a regular restaurant, a waiter walks toward a table carrying food, with bright lighting and customers chatting.”  
assistant.plausibility: ”common”  
assistant.incongruity_for_humor: false  
assistant.has_human_or_animal_or_cartoon: true  
assistant.reasons:  
- ”Scene behavior is consistent with common sense”  
- ”Waiter and customers are human characters”



<!-- page 0017 -->

- Example 4: Only Landscape Without Living Beings -> Reasonable, no humor; no humans/animals/cartoon characters  
user: "Description: The mountains are golden under the sunset, and the tranquil lake reflects the sky, with no people or animals."  
assistant.plausibility: "common"  
assistant.incongruity_for_humor: false  
assistant.has-human_or_animal_or_cartoon: false  
assistant.reasons:  
- "Pure landscape description is common"  
- "Clearly states no people or animals"

- Example 5: Fashion Show with Exaggerated Outfits -> Reasonable, usually not humorous incongruity; contains humans  
user: "Description: Models on the runway at a fashion show wearing exaggerated outfits and headgear, walking in front of lights and an audience."  
assistant.plausibility: "common"  
assistant.incongruity_for_humor: false  
assistant.has-human_or_animal_or_cartoon: true  
assistant.reasons:  
- "Exaggeration is a conventional expression in this setting"  
- "Model as the human character"

### L.1.3. Stage 3A: Object Analogy

OBJECT_ANALOGY_SYSTEM:  
"You are an English 'Object Analogy' sarcastic title generator.  
Generate a very short, colloquial title based on the textual information from step1/step2, with a slight sense of sarcasm or self-deprecation.  
Key requirements (must adhere to these):  
- Do not restate the objects, scenes, or details in the image, and do not explain the origin or reason.  
- Just write the conclusion of the analogy, like something that comes to mind first.  
- You may use simple structures like 'just like...' or 'like...'; you may also provide the conclusion directly.  
- Output only one sentence, no need for 'Title:', no emojis, no unnecessary punctuation or explanations.  
- The tone can be mild or sharp; avoid personal attacks or group degradation.  
- If step2 points out any incongruity, reflect awkwardness/conflict in the tone, but still do not restate the image.  
- Preferably between 3-8 words, and not exceeding 20 words."

OBJECT_ANALOGY_FEWSHOT (flat list; output title only):

- Example: Object -> Person (Box full of fried chicken -> Brain only thinking about food)  
user.step1: "A box filled with fried chicken, chicken pieces piled to the edge."  
user.step2.plausibility: "common"  
user.step2.incongruity_for_humor: true  
user.step2.reasons:  
- "Stacked quantity triggers analogy, fried chicken is a common food"  
user.analogy_strategy: "to-persona"  
user.tone: "mild"  
user.domain_hint: "workplace"  
assistant: "At work, all I can think about is food"

- Example: Object -> Person (Tangled earphone wires -> Tangled thoughts)  
user.step1: "A tangled mess of earphone wires, the cable worn."  
user.step2.plausibility: "common"  
user.step2.incongruity_for_humor: true  
user.step2.reasons:  
- "Tangled = Blocked = Tangled thoughts, analogy to a chaotic"



<!-- page 0018 -->

mind”
user.analogy_strategy: ”to-persona”
user.tone: ”mild”
user.domain_hint: ”studies”
assistant: ”My brain circuitry”

– Example: Object -> Event (Empty
  wallet -> End of the month feel)
user.step1: ”An open wallet that’s
  nearly empty, with only a few
  scattered coins.”
user.step2.plausibility: ”common”
user.step2.incongruity_for_humor:
  true
user.step2.reasons:
  – ”Empty = Lack = End-of-month
    anxiety, analogy to a wallet at
    month’s end”
user.analogy_strategy: ”to-event”
user.tone: ”mild”
user.domain_hint: ”spending”
assistant: ”End of the month”

**L.1.4. Stage 3B: Absurdity**

TITLE_SYSTEM:  
You are the ’Humorous Image Title
  Generator.’ Your sole task: Generate
  a humorous English title based on
  the provided information.

Available Information:  
– Key image details (overview/subjects/
  text_in_image or free-form text
  description)  
– Analysis of scene plausibility and
  incongruities (plausibility,
  incongruity_for_humor, reasons)

Core Objectives (prioritize the most
  prominent point):  
– Capture the ’most striking
  incongruity/contrast’ and craft the
  caption around it.  
– Prioritize personifying the entity
  causing the incongruity; secondarily
  , the entity directly interacting
  with it; only use a narrator/
  bystander perspective if neither
  fits.

Caption Requirements:  
– Personified, colloquial, short
  phrases resembling an ’immediate
  reaction.’  
– 3–8 characters ideal, max 20
  characters.  
– Directly address the action or
  contrast with mild humor/irony.  
– May reasonably imagine ’the next step
  after the incongruity’ for humorous
  exaggeration, but must not
  contradict visible facts in the
  image (quantity/posture/position/
  color, etc.).

Output Specifications (Strictly Adhere)
:  
– Output only one line of English title
  .  
– No explanations, analysis, prefixes/
  suffixes, quotation marks, numbering
  , tags, emojis, or Markdown.  
– Do not ask users questions or request
  additional information.  
– Avoid unnecessary spaces; common
  punctuation for expression is
  permitted.

Self-Check Checklist (internal review
  before generation, not output):  
– Did I select the most prominent
  incongruity/contrast as the focal
  point?  
– Does the title revolve around this
  single contrast without restating
  factual details?  
– Did I avoid verifiable specifics or
  content contradicting the image?  
– Is the word count between 3/\
  textendash 20 words, colloquial and
  rhythmic?

TITLE_FEWSHOT (flat list; output title
  only):

– Example: Seagull in convenience store
  ; perspective = seagull  
user.step1.overview: ”A white seagull
  stands on the tiled floor near
  the entrance of a convenience
  store, with shelves and automatic
  glass doors in the background.”  
user.step1.subjects:  
  – label: ”Seagull”  
    actions_or_states: [”standing”, ”
      holding a chip bag”]



<!-- page 0019 -->

facial_expression: ””  
user.step1.text_in_image: []  
user.step2.plausibility: ”rare”  
user.step2.incongruity_for_humor:  
&nbsp;&nbsp;&nbsp;&nbsp;true  
user.step2.reasons:  
&nbsp;&nbsp;&nbsp;&nbsp;- ”Shopping space is a human  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activity domain”  
&nbsp;&nbsp;&nbsp;&nbsp;- ”A wild seagull entering and  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eating is a misplaced use”  
&nbsp;&nbsp;&nbsp;&nbsp;- ”Animal anthropomorphism creating  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a supermarket shopping contrast  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;”  
user.perspective: ”seagull”  
assistant: ”Chips taste better than  
&nbsp;&nbsp;&nbsp;&nbsp;fish”

- Example: Hotpot in meeting room;  
&nbsp;&nbsp;&nbsp;&nbsp;perspective = narrator  
user.step1.overview: ”In the meeting  
&nbsp;&nbsp;&nbsp;&nbsp;room, a PPT is projected, and a  
&nbsp;&nbsp;&nbsp;&nbsp;hotpot is being cooked in the  
&nbsp;&nbsp;&nbsp;&nbsp;middle of the conference table,  
&nbsp;&nbsp;&nbsp;&nbsp;surrounded by ingredients and  
&nbsp;&nbsp;&nbsp;&nbsp;laptops.”  
user.step1.subjects:  
&nbsp;&nbsp;&nbsp;&nbsp;- label: ”Employee”  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;actions_or_states: [”giving a PPT  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;presentation”]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facial_expression: ””  
user.step1.text_in_image: []  
user.step2.plausibility: ”rare”  
user.step2.incongruity_for_humor:  
&nbsp;&nbsp;&nbsp;&nbsp;true  
user.step2.reasons:  
&nbsp;&nbsp;&nbsp;&nbsp;- ”Office setting is misused for  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cooking”  
&nbsp;&nbsp;&nbsp;&nbsp;- ”Food placed next to electronic  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;devices creates a discordant  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;effect”  
user.perspective: ”narrator”  
assistant: ”This meeting’s more  
&nbsp;&nbsp;&nbsp;&nbsp;exciting in the pot”

#### L.1.5. Stage 3C: Contrast Irony

HUMOR_TITLE_SYSTEM_CONTRAST_IRONY:  
”You are an English satirical ’title  
&nbsp;&nbsp;&nbsp;&nbsp;generator.’ Based on the textual key  
&nbsp;&nbsp;&nbsp;&nbsp;information from the image (step1/  
&nbsp;&nbsp;&nbsp;&nbsp;step2), you will first conceptualize  
&nbsp;&nbsp;&nbsp;&nbsp;a ’minimal event/story’ in your  
&nbsp;&nbsp;&nbsp;&nbsp;mind, then generate an English title  
&nbsp;&nbsp;&nbsp;&nbsp;with as few words as possible,  
&nbsp;&nbsp;&nbsp;&nbsp;forming a natural and smooth sense  
&nbsp;&nbsp;&nbsp;&nbsp;of irony and humor.

Generation strategy (randomly pick one  
&nbsp;&nbsp;&nbsp;&nbsp;or based on input specification):  
A. Direct contrast (contrast): The  
&nbsp;&nbsp;&nbsp;&nbsp;literal meaning of the title forms  
&nbsp;&nbsp;&nbsp;&nbsp;an absurd contrast or opposition to  
&nbsp;&nbsp;&nbsp;&nbsp;the core emotion/action in the image  
&nbsp;&nbsp;&nbsp;&nbsp;.  
B. Situational irony (irony): The title  
&nbsp;&nbsp;&nbsp;&nbsp;creates an ironic effect when  
&nbsp;&nbsp;&nbsp;&nbsp;combined with the image (appears  
&nbsp;&nbsp;&nbsp;&nbsp;comforting/positive but is actually  
&nbsp;&nbsp;&nbsp;&nbsp;ironic).

Writing guidelines:  
- First, based on the image, ’  
&nbsp;&nbsp;&nbsp;&nbsp;reasonably invent a minimal event/  
&nbsp;&nbsp;&nbsp;&nbsp;story’ (only common-sense extension)  
&nbsp;&nbsp;&nbsp;&nbsp;, and then use the fewest words  
&nbsp;&nbsp;&nbsp;&nbsp;possible to form the title, making  
&nbsp;&nbsp;&nbsp;&nbsp;the irony more natural and smooth.  
- Focus on the most prominent action/  
&nbsp;&nbsp;&nbsp;&nbsp;expression/state; instinctive ’first  
&nbsp;&nbsp;&nbsp;&nbsp;reaction,’ allowing for mild  
&nbsp;&nbsp;&nbsp;&nbsp;exaggeration or inner-monologue  
&nbsp;&nbsp;&nbsp;&nbsp;style short phrases.  
- Only common-sense associations,  
&nbsp;&nbsp;&nbsp;&nbsp;without contradicting the  
&nbsp;&nbsp;&nbsp;&nbsp;description; avoid using profanity  
&nbsp;&nbsp;&nbsp;&nbsp;or offensive expressions.  
- 3–8 words preferred, no more than 20  
&nbsp;&nbsp;&nbsp;&nbsp;words.  
Output: Only output one title sentence  
&nbsp;&nbsp;&nbsp;&nbsp;.”

HUMOR_TITLE_FEWSHOT_CONTRAST_IRONY (  
&nbsp;&nbsp;&nbsp;&nbsp;flat list; output title only):

- Example: Strategy = A_contrast  
user.step1: ”A woman is crying with  
&nbsp;&nbsp;&nbsp;&nbsp;her hands over her face, her  
&nbsp;&nbsp;&nbsp;&nbsp;shoulders shaking, and her eyes  
&nbsp;&nbsp;&nbsp;&nbsp;are red.”  
user.step2.plausibility: ”common”  
user.step2.incongruity_for_humor:  
&nbsp;&nbsp;&nbsp;&nbsp;true  
user.step2.reasons:  
&nbsp;&nbsp;&nbsp;&nbsp;- ”Strong negative emotions, easily  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;creating contrast through  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;absurdity”  
user.strategy: ”A_contrast”



<!-- page 0020 -->

assistant: "I'm hungry, but I already  
brushed my teeth"

- Example: Strategy = B_irony  
user.step1: "A group of medical staff  
in white coats smiles at the  
camera, holding medical  
instruments."  
user.step2.plausibility: "common"  
user.step2.incongruity_for_humor:  
true  
user.step2.reasons:  
- "The professional context and  
patient experience can form  
irony"  
user.strategy: "B_irony"  
assistant: "This won't hurt"

### L.1.6. Stage 3D: Emotion Analogy

HUMOR_TITLE_SYSTEM_EMOTION:  
"You are an English title generator.  
Please generate an English title  
based on the following information:  
- Key information from the image (  
structured or free-form text)  
- Analysis of the expression, action,  
state, and emotion of the characters  
/animals/cartoons  
Requirements:  
- Draw an analogy to a human reaction  
in a similar situation to create  
incongruity and contrast.  
- First-reaction short sentences, may  
include mild humor/contrast-based  
jokes; very minimal inner-monologue  
style short phrases are allowed.  
- Common-sense associations are fine;  
avoid contradicting the description;  
do not use profanity or offensive  
expressions.  
- 3-8 words preferred, no more than 20  
words.  
Output: Only output one title sentence  
."

HUMOR_TITLE_FEWSHOT_EMOTION (flat list;  
output title only):

- Example: Dog with blank stare  
user.step1: "A little dog with its  
mouth wide open and a blank stare  
."  
user.step2.plausibility: "common"  
user.step2.incongruity_for_humor:  
false  
user.step2.reasons:  
- "Expression matches tiredness/  
blankness"  
assistant: "I don't want to study!"

- Example: Child writing nervously  
user.step1: "A child is writing,  
looking nervous, with their mouth  
wide open."  
user.step2.plausibility: "common"  
user.step2.incongruity_for_humor:  
false  
user.step2.reasons:  
- "Student rushing through homework  
, expression is tense"  
assistant: "Oh no, I forgot the  
deadline!"

### L.1.7. Stage 4: Safety Classifier

SAFETY_SYSTEM_PROMPT:  
"You are a safety classifier for short  
humorous English image captions.

Your job is to detect whether a given  
English caption contains any of the  
following:  
- group attacks: insults or demeaning  
content toward groups based on  
ethnicity, nationality, religion,  
gender,  
sexual orientation, disability, etc.;  
- personal attacks: targeted insults or  
demeaning expressions toward an  
individual;  
- hate speech: slurs or content that  
promotes hatred, exclusion, or  
dehumanization of protected groups;  
- humiliating or demeaning expressions,  
including metaphorical references.

For each input caption, respond with a  
STRICT JSON object in the following  
format:

{  
"compliant": true or false,  
"violation_categories": [  
"group_attack" | "personal_attack",  
| "hate_speech" | "humiliation"  
| "other"  
],



<!-- page 0021 -->

"explanation": "short natural language explanation (<= 50 words)"
}

Guidelines:  
- If the caption is fully safe (no problematic content), set "compliant" to true, use an empty list for "violation_categories", and keep the explanation concise (you may simply say it is safe).  
- If there is any problematic content, set "compliant" to false and include 1–3 relevant categories in "violation_categories", with a brief explanation.  
- Do NOT include any text outside the JSON object."

### L.2. Humor Discriminator

# Humor Judgment: General Theory of Verbal Humor (GTVH)

You are a reliable and insightful expert in humor theory. Your task is to judge whether a given title is humorous for a provided image, using the General Theory of Verbal Humor (GTVH) as your main analytical framework.

## GTVH Framework

GTVH proposes that humor arises from the interplay of six key "Knowledge Resources" (KRs). For each input, analyze the following resources and determine whether any of them contribute to humor, using the classic humor theories as guidance:

1. **Script Opposition**  
   - *Definition*: The presence of two conflicting or contrasting scripts (interpretations, scenarios, or expectations) within the image–title pair.  
   - *Related Theories*:  
     - **Incongruity Theory**: Humor from violated expectations or illogical contrasts.  
     - **Script-based Semantic Theory of Humor (SSTH)**: Humor from overlapping scripts or schemas that are compatible yet opposite.  
     - **Cognitive Insight Theory**: Humor from sudden realizations, hidden connections, double meanings, or unexpected twists.  
   - *Analysis*: Does the title create a contrast, surprise, or double meaning with the image? Is there a moment of insight or script switch?

2. **Logical Mechanism**  
   - *Definition*: The technique or reasoning that connects the scripts and delivers the humor (e.g., exaggeration, reversal, wordplay).  
   - *Related Theories*:  
     - **Cognitive Insight Theory**: Humor from sudden realization or clever connections.  
     - **General wit or cleverness**: Humor from puns, wordplay, or creative associations.  
   - *Analysis*: Does the title use clever logic, wordplay, or a twist to create humor?

3. **Situation**  
   - *Definition*: The context, background, or scenario depicted in the image and referenced by the title.  
   - *Related Theories*:  
     - **Relief Theory**: Humor from releasing tension or repressed emotions in a given situation.  
     - **Benign Violation Theory**: Humor from breaking norms or expectations in a harmless way.  
   - *Analysis*: Does the situation involve tension, taboo, or a harmless violation that could be funny?

4. **Target**  
   - *Definition*: The subject or object of the humor (who or what is being laughed at).



<!-- page 0022 -->

- *Related Theories*:
  - **Superiority Theory**: Humor from feeling superior to others mistakes or weaknesses.
  - *Analysis*: Is the humor directed at someone’s error, misfortune, or foolishness?

5. **Narrative Strategy**
- *Definition*: The way the humor is delivered (e.g., as a riddle, pun, or straightforward statement).
- *Analysis*: Does the delivery style enhance the humorous effect?

6. **Language**
- *Definition*: The specific wording, phrasing, or linguistic devices used in the title.
- *Analysis*: Does the language itself (e.g., puns, rhymes, ambiguity) contribute to humor?

## Instructions

- For each Knowledge Resource, analyze whether it contributes to humor in the given image-title pair, using the relevant theories above or other general factors.
- If any resource, through these mechanisms, creates a humorous effect, judge the title as humorous.
- If the title contains general wit or cleverness without fitting a specific theory, eliciting humor according to common human experience, also judge it as humorous.
- Output ONLY a single JSON object with exactly one field: "humorous". Set its value to 1 if the title is humorous, or 0 if not.

**Example Output:**

{"humorous": 1}

**Adhere exactly to the JSON schema and content rules above. Do not output anything else.**
