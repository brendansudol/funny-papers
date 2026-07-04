<!-- Transcribed from x05-memereacon.pdf -->



<!-- page 0001 -->

# MemeReaCon: Probing Contextual Meme Understanding in Large Vision-Language Models

Zhengyi Zhao<sup>1</sup>, Shubo Zhang<sup>2</sup>, Yuxi Zhang<sup>2</sup>, Yanxi Zhao<sup>2</sup>, Yifan Zhang<sup>2</sup>,  
Zezhong Wang<sup>1</sup>, Huimin Wang<sup>3</sup>, Yutian Zhao<sup>3</sup>, Bin Liang<sup>1</sup>, Yefeng Zheng<sup>4</sup>,  
Binyang Li<sup>2</sup>, Kam-Fai Wong<sup>1</sup>, Xian Wu<sup>3,*</sup>,

<sup>1</sup> The Chinese University of Hong Kong <sup>2</sup> University of International Relations  
<sup>3</sup> Jarvis Research Center, Tencent YouTu Lab <sup>4</sup> Westlake University  
`zyzhao@se.cuhk.edu.hk`

## Abstract

Memes have emerged as a popular form of multimodal online communication, where their interpretation heavily depends on the specific context in which they appear. Current approaches predominantly focus on isolated meme analysis, either for harmful content detection or standalone interpretation, overlooking a fundamental challenge: the same meme can express different intents depending on its conversational context. This oversight creates an evaluation gap: although humans intuitively recognize how context shapes meme interpretation, Large Vision Language Models (LVLMs) can hardly understand context-dependent meme intent. To address this critical limitation, we introduce MemeReaCon, a novel benchmark specifically designed to evaluate how LVLMs understand memes in their original context. We collected memes from five different Reddit communities, keeping each meme’s image, the post text, and user comments together. We carefully labeled how the text and meme work together, what the poster intended, how the meme is structured, and how the community responded. Our tests with leading LVLMs show a clear weakness: models either fail to interpret critical information in the contexts, or overly focus on visual details while overlooking communicative purpose. MemeReaCon thus serves both as a diagnostic tool exposing current limitations and as a challenging benchmark to drive development toward more sophisticated LVLMs of the context-aware understanding.

[Figure: Two Reddit-style post cards. Left: r/ProgrammerHumor; “Post Title: andTheyNeverBoxAndUnbox”; meme text “YOUR OUTIE UNDERSTANDS THE DIFFERENCE / BETWEEN STACK AND HEAP.”; “Post Intent: Self-mocking about knowing these programming skills”. Right: r/memes; “Post Title: My mom said not to my clothes”; same meme; “Post Intent: Self-mocking about I often have an untidy pile of clothes”.]

Figure 1: Demo illustrating how a single meme’s interpretation changes across different contextual settings. Meme here literally indicates *you know the difference between “Stack” and “Heap”*. The “Stack” and “Heap” mean specific terms in programmer community, but can mean condition of an item in general talk.

## 1 Introduction

Memes are “amateur media artifacts, extensively remixed and recirculated by different participants on social media networks” (Milner, 2012) that have become a key part of how people communicate online. These combinations of images and text derive meaning not just from their content, but from their contextual placement: where they appear, why they are shared, and how communities respond to them. A meme posted in a programmer joke forum carries a fundamentally different meaning than the same meme shared in a generic community, as illustrated in Figure 1. While humans naturally process these contextual distinctions, developing computational models that can achieve similar understanding remains a significant challenge (Wang et al., 2024).

Current meme-focused research has largely pursued two distinct paths, neither fully capturing the contextual richness of memes in real online communication. The first approach centers on detecting harmful or toxic meme content (Sharma et al., 2022; Hee et al., 2023; Huang et al., 2024). While crucial for content moderation systems, this research typically leverages context primarily as a classifier for harmfulness rather than for comprehensive meaning interpretation. The second research direction tackles isolated meme understanding through tasks like caption generation (Hwang and Shwartz, 2023), intent description (Park et al., 2024), and role explanation (Sharma et al., 2023). Despite their value, these efforts examine memes

*Corresponding author.



<!-- page 0002 -->

divorced from their original context, separating them from post text, creator intent, and community reactions that collectively shape their contextual meaning.

This decontextualization creates a fundamental evaluation gap: we lack methods to assess whether LVLMs can understand why particular memes are selected for specific communicative situations. As Park et al. (2024) observed, people create memes “with an intent to perform some action”. The same meme template can convey radically different meanings depending on its accompanying post title, community norms, or ongoing conversation thread (Lin et al., 2024). Without incorporating these contextual elements, we cannot effectively measure LVLMs’ capacity to process memes as humans naturally do in online environments.

To address these limitations, we developed **MemeReaCon:** Meme Reasoning in Context, a comprehensive benchmark specifically designed to evaluate LVLMs’ ability to understand memes within their original contexts. We constructed MemeReaCon using content from five diverse Reddit communities, encompassing varied topics, styles, and community norms. Each example preserves three critical contextual elements: the meme image itself, the complete post text, and the top-rated community comments that reveal collective interpretation. Beyond mere data collection, our benchmark includes detailed annotations that enable targeted analysis of specific contextual understanding dimensions.

Through MemeReaCon, we investigate two fundamental questions about current LVLM limitations: (1) To what extent do models understand the meme? (2) To what extent does the post context affect models’ understanding of meme?

Our extensive evaluation of leading LVLMs reveals a persistent weakness in contextual integration. Models frequently fail to establish meaningful connections between memes and their context, **either fail to interpret critical information in the contexts, or overly focus on visual details while overlooking communicative purpose.** Detailed error analysis reveals that models are sensitive to context type, such that models often fail in culturally dominant contexts rather than giving specific tags or communities. Our work makes following contributions:

- To our knowledge, we firstly identify how the post context and meme work together: post context mainly explains the meme, or the meme illustrates points made in the context. This helps us to evaluate models whether understand different ways people use memes to communicate.
- We propose a novel benchmark, MemeReaCon, for meme understanding that maintains the essential relationship between meme images, post, and community reception, enabling the first systematic evaluation of how well LVLMs interpret memes as they actually function in online environments.
- We conduct comprehensive evaluation, revealing contextual-insensitive limitations in current LVLMs to connect multimodal elements for contextual interpretation.

## 2 Related Works

**Meme Classification.** The detection of harmful memes has emerged as a significant research area, supported by extensive benchmark datasets (Kiela et al., 2019; Pramanick et al., 2021a; Lin et al., 2024) and community initiatives such as Facebook’s Hateful Memes Challenge (Kiela et al., 2020). Research in this domain has evolved along several trajectories. Early approaches employed two-stream architectures that separately encode textual and visual features before applying attention mechanisms and multimodal fusion techniques for classification (Kiela et al., 2019; Suryawanshi et al., 2020; Pramanick et al., 2021b). A parallel line of work has focused on fine-tuning pre-trained multimodal models specifically for harmful content detection (Lippe et al., 2020; Velioglu and Rose, 2020; Hee et al., 2022, 2023). Both methods are conducted on multiple harmful categories such as trolling (Suryawanshi et al., 2020), hateful (Kiela et al., 2020), anti-semitism (Chandra et al., 2021), misogynous (Fersini et al., 2022), and anti-vaccinationism (Knuutila et al., 2024).

**Meme Explanation.** Another stream of research focuses on understanding memes as standalone units. Tasks include generating textual explanations (Sharma et al., 2023) or captions for memes (Hwang and Shwartz, 2023), classifying their sentiment or evoked emotions (Hee et al., 2023), identifying depicted entities (Sharma et al., 2023), or explaining their underlying humor (Sharma et al., 2022). These studies typically operate on decontextualized memes, removing them from the original posts and discussions where their meaning is



<!-- page 0003 -->

| Dataset | Task Type | Post Context | Comments | Size |
|---|---|---:|---:|---:|
| MultiOFF (Suryawanshi et al., 2020) | classify: meme hatefulness | ✘ | ✘ | 743 |
| HatefulMemes (Kiela et al., 2020) | classify: meme hatefulness | ✘ | ✘ | 10k |
| Jewtocracy (Chandra et al., 2021) | classify: meme hatefulness | ✘ | ✘ | 6,611 |
| HarMeme (Pramanick et al., 2021a) | classify: meme hatefulness/target | ✘ | ✘ | 3,544 |
| MAMI (Fersini et al., 2022) | classify: meme hatefulness | ✘ | ✘ | 15k |
| FigMemes (Liu et al., 2022) | classify: meme political opinion | ✘ | ✘ | 5,141 |
| HVVMemes (Sharma et al., 2022) | classify: meme character role | ✘ | ✘ | 7k |
| GOAT (Lin et al., 2024) | classify: meme hatefulness | ✘ | ✘ | 6,626 |
| HatReD (Hee et al., 2023) | explain: meme | ✘ | ✘ | 3,228 |
| ExHVV (Sharma et al., 2023) | explain: meme | ✘ | ✘ | 4,680 |
| MemeCap (Hwang and Shwartz, 2023) | explain: meme + metaphors | ✔ | ✘ | 6,387 |
| MemeIntent (Park et al., 2024) | explain: metaphors | ✔ | ✘ | 950 |
| **MemeReaCon (ours)** | **classify: meme + post + comment type/affection**<br>**explain: meme + metaphors + post + post intents** | ✔ | ✔ | **1,565** |

Table 1: Comparisons with other related meme benchmarks.

shaped and negotiated. This methodological choice inherently limits the ability to assess if models grasp the social function of the meme (i.e., why it was used **there**).

**MemeReaCon’s Position.** Table 1 shows related meme benchmarks. MemeReaCon occupies a unique position by being the first benchmark, to our knowledge, specifically constructed to evaluate the fine-grained contextual reasoning required to understand memes as they are used in online posts. It mandates the integration of the meme image and the full original post text. Its detailed annotations concerning the context-meme relationship, meme structure, and comment interactions enable a more nuanced analysis of LVLM capabilities and failures than previously possible.

## 3 Constructing the MemeReaCon Benchmark

The central goal of MemeReaCon is to provide a robust resource for evaluating the contextual reasoning capabilities of LVLMs when interpreting memes. Achieving this requires a dataset that is not only large and diverse but also curated about the interplay between a meme and its surrounding textual context. The construction process is detailed below.

### 3.1 Data Collection

To capture authentic meme usage patterns within varied contexts, we selected Reddit[^1] as our primary data source. Reddit hosts a vast number of communities with distinct topics and communication styles, making it an ideal ecosystem for observing how the same meme template might be interpreted differently across contexts. We specifically chose five diverse, high-activity, English subreddits to ensure broad coverage:

- **r/memes** and **r/meme**: Two large, general-purpose communities offering a baseline of popular meme formats and topics.
- **r/ProgrammerHumor**: A niche community focused on technology and programmer-specific context and humor.
- **r/BritishMemes**: A culturally specific community, requiring understanding of UK-related references, stereotypes, and events.
- **r/RelationshipMemes**: A social community centered on dating and interpersonal dynamics, often involving nuanced emotional expression.

This curated selection ensures variability in the types of contextual information (general knowledge, technical terms, cultural references, and social cues) required for successful interpretation.

We collected publicly available posts submitted between January 2022 and May 2025 using the Python Reddit API Wrapper. Our initial query targeted posts containing: (i) a textual title, (ii) an associated meme image, and (iii) the top-rated comments to filter out posts with community interaction. This initial pool contained over 3,000 potential candidates.

### 3.2 Filtering for Quality and Contextual Relevance

The raw data required careful filtering to isolate instances suitable for evaluating contextual reasoning. Our multi-stage filtering process aimed

[^1]: https://www.reddit.com



<!-- page 0004 -->

[Figure: Two-part illustrative panel. Top titled “Context-Meme Interplay Types” with examples labeled “(I) Context Explain Meme” and “(II) Meme Enhance Context”; visible post titles include “Indeed, we only demand sth adore us” and “when you finish all the levels in a game in one night and now you have nothing to live for”. Bottom titled “Meme Types” with examples labeled “(a) Pure Meme”, “(b) Text-in-Meme”, “(c) Text-out-Meme”, “(d) Comics”, and “(e) Combination”.]

Figure 2: Cases of each annotation scheme. Top-side (I) and (II) represent the label of Context-Meme Interplay (CMI). Bottom-side (a) to (e) show the label of Meme Composition (MC).

to maximize data quality and ensure that each instance contained sufficient context for meaningful analysis.

Firstly, we removed posts that were deleted (by user or admin), associated with suspended accounts, or contained broken image links. This step ensured the integrity and reproducibility of the dataset instances. Approximately 24% of the initial pool was removed here.

Besides, to ensure presence of textual context accompanying the meme. We filtered out posts with very short context (fewer than 3 words[^2]), as these often lack the necessary linguistic cues to establish a specific context beyond the meme image itself. This step removed roughly 18% of the remaining posts, focusing the dataset on instances where textual context is explicitly provided.

While sourcing from meme-centric subreddits increases the likelihood of collecting actual memes, we implemented a verification step during annotation. Annotators removed non-meme images (e.g., selfie, advertisements) (in approximately 8% of filtered posts).

Then, for comments, we selected the single highest-voted, non-deleted comment (excluding bot comments) as a proxy for the dominant community reaction or interpretation. To ensure the comment provided substantive feedback, we required a minimum length of 3 words. Posts lacking such a comment were also included noted as [none].

Each resulting instance was structured to include the meme image, the post title, the post body (marked empty if absent), and the selected top comment text. All usernames were anonymized to protect user privacy.

### 3.3 Annotation Scheme

The annotation scheme is designed specifically to target the reasoning processes involved in understanding a meme within its post context. We developed labels that move beyond simple classification to capture the nuances of the context-meme connection and its intent. Our scheme includes five key dimensions:

• **Context-Meme Interplay (CMI):** to directly addresses the question: how does the context relate to the meme (shown in Figure 2 (I) and (II))?

– *Context Explain Meme (CEM):* The text is essential for understanding the meme’s relevance or specific meaning.  
– *Meme Enhance Context (MEC):* The text establishes a point, and the meme serves to illustrate, emphasize, or add humor/emotion.

• **Meme Types (MT):** to understand how information is distributed in meme (shown in Figure 2 (a) to (e)).

– *Pure Meme:* Visuals carry the primary load.  
– *Text-in-Meme:* Embedded text is integral.  
– *Text-out-Meme:* Post title/body acts as the primary caption for a reusable template.

[^2]: Some of contexts were internet-cultural abbreviations containing less than 3 words. We include these strong-cultural abbreviations too.



<!-- page 0005 -->

[Figure: Two pie charts. Left chart titled “Distribution across Communities” with slices labeled r/ProgrammerHumor 22.5%, r/BritishMeme 16.4%, r/RelationshipMeme 17.1%, r/meme(s) 44.1%. Right chart titled “Distribution of Meme Types” with slices labeled Pure Meme 13.9%, Combination 5.8%, Comics 11.2%, Text-out-Meme 15.8%, Text-in-Meme 53.3%.]

Figure 3: Statistics of our MemeReaCon. Our MemeReaCon benchmark comprises 1,565 annotated instances collected from five diverse subreddits. Detailed statistics can be found in Appendix B.

[Figure: Example meme with text “Me looking at code that I wrote yesterday:” above a multi-panel reaction image. Annotation panel text includes: “Post Context: whatWasThat”; “Comment: check your record with Cursor”; “CMI: Context Explain Meme”; “MT: Text-out-Meme”; “CSAC: Extension,Consistent”; “Post Connection: (1) Programmers often find themselves in a situation where they cannot understand the code they wrote yesterday today. (2) Cursor-like AI can help programmers write code through conversation. (3) Today’s AI makes it possible for programmers to write code without knowing what code they have written.”; “Post Intent: Self-mocking the daily work of programmers.”]

Figure 4: Example of a meme in MemeReaCon.

– *Comics*: Multi-panel narrative structure.  
– *Combination*: Multi-type figures are combined together to perform the unitary meaning.

• **Comment Stance and Affective Consistence (CSAC):** stance to assess the relationship between the top comment and the post. Affective consistence to assess the affection of a comment between its literal and its intended meaning.

(1) From stance-level:  
– *Support*: Agrees with or reinforces the post.  
– *Deny*: Disagrees with or challenges the post.  
– *Extension*: Builds upon the post.  

(2) From affection-level:  
– *Consistent*: Same to its intent affection.  
– *Inconsistent*: Different from its literal one to perform a sarcastic or complain.

• **Post Connection (PC):** to capture the logical or thematic linkages among the post context, meme, and comments, provided in key points that identify the specific connections between elements.

• **Post Intent (PI):** to identify the author’s purpose for creating and sharing the post, such as humor, experience sharing, and complaint.

**Annotation Process and Quality Control.** Figure 4 shows an example of our MemeReaCon<sup>3</sup>. Ensuring high-quality annotations was prominent. We recruited and trained 6 annotators (English-speaking Ph.D. students familiar with internet culture) using detailed guidelines and iteratively trained on 200 samples. The main annotation was conducted via a customized web interface displaying all components. To maximize reliability, each instance was independently annotated by 3 annotators. Disagreements were resolved by majority vote. For the rare cases of complete disagreement (3 unique labels for an instance), a senior annotator determined based on the guidelines and discussion. We calculated inter-annotator agreement (IAA) using Fleiss’ Kappa ($\kappa$) on a held-out set of 500 instances annotated by all 6 annotators prior to the main task. The achieved agreement was substantial: CMI ($\kappa$ = 0.86), MT ($\kappa$ = 0.88), CSAC ($\kappa$ = 0.75), PC ($\kappa$ = 0.79), and PI ($\kappa$ = 0.81), indicating the robustness and clarity of our annotation scheme and process.

### 3.4 Dataset Statistics

The final MemeReaCon benchmark comprises 1,565 annotated instances collected from five diverse subreddits. Figure 3 provides statistics of our MemeReaCon. Detailed statistics can be found in Appendix B.

## 4 Experiments

Our experiments with MemeReaCon are designed to address two key research questions: (1) to what extent do models understand the meme? (2) to what extent does the post affect models’ understanding of meme?

<sup>3</sup>More cases are shown in Appendix A.



<!-- page 0006 -->

## 4.1 Experimental Setup

**Models Evaluated.** We evaluated 10 diverse state-of-the-art models spanning three architectural paradigms, alongside two unimodal baselines to establish comparative foundations:

- **Unimodal Baselines:** Qwen2.5 (Yang et al., 2024) (text-only) and Flamingo (Alayrac et al., 2022) (image-only) establish performance boundaries for single-modality reasoning.
- **Vision-Language Models (VLM):** LLaVA-OneVision-7B (Li et al., 2024), Phi-4-MM-5.6B (Abdin et al., 2024), Qwen2.5-VL-7B (Bai et al., 2025), Qwen2.5-Omni-7B (Xu et al., 2025), and InternVL3-8B (Chen et al., 2024) represent approaches where vision and language capabilities are jointly trained.
- **Vision Reasoning Models (VRM):** QvQ-72B (Qwen, 2024), GPT-4o (Hurst et al., 2024), Grok3 (xAI, 2025), Claude-3.7-sonnet-thinking (Anthropic, 2025), and Gemini-2.5-Pro (DeepMind, 2025) integrate advanced reasoning mechanisms atop vision-language foundations, representing the current frontier.

**Evaluation Settings.** All evaluations were conducted in a zero-shot setting with no fine-tuning. For classification tasks, we report accuracy and macro F1-score to account for class imbalance. For generative tasks, we use BERTScore (B-S) (Zhang et al., 2020) and ROUGE-L (R-L) to evaluate semantic and lexical similarity.

**Tasks.** We designed four primary tasks of increasing complexity to systematically probe different dimensions of contextual meme understanding.

It is important to note the role of the **Meme Types (MT)** annotation. While MT is a crucial dimension for understanding the structural properties of memes, we do not define a direct classification task for it. Instead, MT serves as an analytical lens through which we evaluate model performance on the other defined tasks. This allows for a fine-grained analysis of how different meme structures impact a model’s ability.

The four primary evaluation tasks are:

- **Context-Meme Interplay Classification (CMI-C):** Given the post context and the meme, models must classify the relationship as either *Context Explain Meme (CEM)* or *Meme Enhance Context (MEC)*. This task evaluates the model’s basic understanding of how textual context and visual meme content depend on each other.
- **Comment Stance and Affective Consistent Classification (CSAC-C):** This is a two-part classification task. Given the original post (context + meme) and a top-level comment, models must: (1) determine the comment’s stance towards the post (*Support, Deny,* or *Extension*), and (2) identify whether the comment’s literal affection is *Consistent* or *Inconsistent* with its intended meaning. This task probes deeper social reasoning capabilities, including the ability to understand agreement, disagreement, and nuanced expressions like sarcasm.
- **Post Connection Generation (PC-G):** Given the post context, the meme, and a set of relevant comments, models are required to generate a free-form text. This text should explain the key logical or thematic connections linking these elements. This generative task evaluates the model’s overall understanding and its ability to articulate the reasoning chain.
- **Post Intent Generation (PI-G):** Based on all available evidence (post context, meme, and comments), models must generate the original poster’s communicative intent (e.g., humor, complaint). This task assesses the model’s ability to understand the overall purpose of the multimodal post.

These tasks are designed to progressively challenge models, moving from classifying direct relationships (CMI-C) to understanding complex social cues (CSAC-C), generating coherent explanations (PC-G), and inferring high-level intent (PI-G). Together, they provide a comprehensive benchmark for evaluating contextual reasoning abilities in the domain of internet memes. Detailed implementations can be found in Appendix C.

## 4.2 Overall Performance Comparison

Table 2 presents a comprehensive performance evaluation of various models on our MemeReaCon benchmark. Our analysis reveals critical insights into current LVLM capabilities and limitations in understanding social media posts with memes.

**Surface-level Understanding vs. Deep Comprehension.** While models demonstrate reasonable proficiency on simpler classification tasks (CMI-C, CSAC-C), their performance deteriorates substantially on generative tasks requiring deeper



<!-- page 0007 -->

| Model | CMI-C Acc (%) | CMI-C MacF1 (%) | CSAC-C Acc (%) | CSAC-C MacF1 (%) | PC-G B-S (%) | PC-G R-L (%) | PI-G B-S (%) | PI-G R-L (%) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| *Unimodal Baselines* |  |  |  |  |  |  |  |  |
| Qwen2.5 | 54.83 | 53.92 | 59.27 | 41.24 | 46.48 | 46.37 | 22.63 | 17.82 |
| Flamingo | 52.14 | 51.58 | 31.73 | 22.79 | 25.42 | 18.13 | 9.31 | 8.47 |
| *Vision-Language Models (VLM)* |  |  |  |  |  |  |  |  |
| LLaVA-One Vision | 56.32 | 55.76 | 38.91 | 29.08 | 20.19 | 22.53 | 12.68 | 10.91 |
| Phi-4-MM | 58.47 | 58.12 | 42.34 | 32.61 | 26.92 | 28.39 | 15.52 | 13.26 |
| InternVL3 | 64.72 | 64.18 | 49.53 | 38.41 | 37.23 | 38.92 | 25.63 | 20.43 |
| Qwen2.5-VL | 61.43 | 60.97 | 46.15 | 35.83 | 33.74 | 31.27 | 19.76 | 16.04 |
| Qwen2.5-Omni | 68.86 | 68.47 | 54.32 | 42.13 | 43.04 | 44.79 | 30.43 | 24.18 |
| Qwen2.5-Omni w/ CoT | 71.35 | 70.96 | 57.68 | 44.72 | 47.19 | 48.23 | 33.76 | 26.95 |
| Qwen2.5-Omni w/ SC | 73.42 | 73.09 | 60.17 | 46.89 | 49.87 | 50.42 | 36.28 | 29.37 |
| *Vision Reasoning Models (VRM)* |  |  |  |  |  |  |  |  |
| gpt-4o | 72.48 | 71.96 | 58.76 | 46.53 | 57.82 | 48.47 | 34.94 | 28.37 |
| QvQ | 75.29 | 74.87 | 62.61 | 49.74 | 60.13 | 51.25 | 39.52 | 32.64 |
| Grok-3 | 78.36 | 78.09 | 65.73 | 53.21 | 62.29 | 54.03 | 43.19 | 36.47 |
| Claude-3.7 | 80.97 | 80.56 | 68.39 | 55.93 | 64.48 | 57.14 | 47.59 | 40.31 |
| Gemini-2.5-pro | **83.21** | **82.86** | **71.28** | **59.42** | **66.89** | **60.38** | **52.34** | **44.86** |

Table 2: Performance comparison across model architectures on MemeReaCon tasks. **Bold** indicates the best performance.

[Figure: Bar chart of Context Relevance Score by model category with dashed “Average CRS” line. Legend includes Unimodal Baselines, Vision-Language Models (VLM), and Vision Reasoning Models (VRM). Bars labeled with scores including Qwen2.5 0.41, Flamingo 0.38, LLaVA-OneVis. 0.43, InternVL3 0.46, Phi-4-MM 0.52, Qwen2.5-VL 0.49, Qwen2.5-Omni 0.51, Omni w/ CoT 0.53, Omni w/ SC 0.53, gpt-4o 0.50, QvQ 0.53, Grok-3 0.45, Claude-3.7 0.64, Gemini-2.5-pro 0.68. Y-axis label: Context Relevance Score.]

Figure 5: Context relevance scores across model categories, measuring how effectively models integrate information from multiple contextual sources.

post comprehension (PC-G, PI-G). Even the top-performing Gemini-2.5-pro shows a big drop from classification (83.21% accuracy on CMI-C) to generative tasks (60.38% ROUGE-L on PC-G, 44.86% on PI-G). This performance cliff indicates that current models can identify superficial relationships between text and images but struggle to synthesize holistic interpretations that capture the post’s communicative intent and social context. The low PI-G scores particularly suggest that current models still fall short in understanding the nuanced social dynamics embedded in meme-based communication.

When applying Chain-of-Thought (CoT) and Self-Consistency (SC) techniques to Qwen2.5-Omni, we observe modest improvements across all tasks. However, these enhancements are more for classification tasks (+4.56% on CMI-C with SC) and less impactful for generative tasks (+3.85% on BERTScore on PI-G). This suggests that while structured reasoning approaches can help models better classify relationships, they offer limited benefits for the deeper contextual integration needed to understand post meaning and intent.

**Post Components Integration Challenge.** To quantitatively assess models’ ability to integrate information across modalities and contextual elements, we introduce the Context Relevance Score



<!-- page 0008 -->

[Figure: Composite illustration of error cases. Top row shows a meme reading “Me looking at code that I wrote yesterday:” with panels comparing “Generated” and “Golden” analyses and an “Error Analysis: (Context)” box. Bottom row shows a Reddit gun violence comic meme with text including “Gun Violence is Wrong!”, “We Agree. Please Stop Shooting Us!”, and “Well Not All Guns are Bad!”, with “Generated” and “Golden” analyses and an “Error Analysis: (Culture)” box.]

Figure 6: Illustration of some cases in error. The green text indicates the correct answer. The red text indicates the wrong answer.

(CRS), defined as:

$$
\mathrm{CRS} = \frac{1}{N} \sum_{i=1}^{N} w_i \cdot \mathrm{Rel}(r_i, \{c_j\}_{j=1}^{M}), \tag{1}
$$

where $N$ is the number of evaluation samples, $r_i$ is the model’s response for sample $i$, $\{c_j\}_{j=1}^{M}$ represents the $M$ contextual elements (post text, image, comments) for sample $i$, $\mathrm{Rel}(\cdot)$ measures the semantic relevance between the response and all contextual elements (computed using BERTScore with a threshold of 0.7 for relevance), and $w_i$ is a difficulty weight based on the number of contextual elements requiring integration. CRS ranges from 0 to 1, with higher scores indicating better cross-contextual integration.

Our CRS analysis reveals significant gaps in contextual integration capabilities. As shown in Figure 5, VRMs achieve higher CRS values compared to VLMs. But the best models struggle with fully integrating information across modalities and contextual elements. This finding aligns with the poor performance on PC-G and PI-G tasks, confirming that contextual integration represents a fundamental bottleneck in current architectures. We show more analysis of performance in different communities (D.1), meme structure (D.2), meme text-density (D.3), comment affection (D.4), and modality contribution (D.5).

### 4.3 Error Analysis

To gain deeper insights into how post context influences meme interpretation, we conducted a systematic error analysis across all evaluated models. This analysis reveals critical limitations in current models when processing contextually embedded memes and highlights failure patterns that occur at the intersection of visual humor and social context.

We categorized errors into four distinct patterns that emerged consistently across models: context error, visual error, semantic error, and cultural error. Appendix E shows detailed definition of these patterns and distributions of error types across models. Figure 6 shows the selected error cases. More cases can be found in Appendix F.

## 5 Conclusion

In this paper, we introduced MemeReaCon, a novel benchmark that addresses a critical gap in meme understanding research by preserving the post context for meme interpretation. Our findings revealed significant limitations in current LVLMs to integrate contextual information when explaining memes, with models often failing to establish meaningful connections between visual content and surrounding context or overlooking communicative purpose in favor of surface-level visual analysis. Besides, by identifying the dual relationship patterns between memes and their contexts, we provided a framework for evaluating how well models understand the diverse communicative functions



<!-- page 0009 -->

of memes in online environments. This work not only highlights the context-insensitive limitations of current models but also establishes a foundation for future to more accurately capture how humans naturally process and interpret memes within their original discourse contexts.

## Limitations

Our work, while comprehensive, is subject to certain limitations, primarily concerning the nuances of annotation when dealing with complex connections and intents and the inherent subjectivity in meme interpretation. First, regarding the annotation of post connections, we observed that the explicit post connections was less consistent across annotations in some cases. This suggests a challenge in achieving widespread mutual agreement on a precise methodology for connecting posters’ context meaning with the meme meanings. Even when annotators possess the general knowledge to understand the meme’s overall message, a shared, systematic approach to deconstructing and codifying the specific metaphorical knowledge embedded in the memes may not be uniformly applied. Second, the interpretation of memes is deeply dependent on annotator’s background knowledge, encompassing cultural, social, and contextual understanding, which inherently varies among annotators.

## Ethics Statement

The development of this benchmark for contextual meme understanding was guided by a commitment to responsible research practices. We have taken several steps to address potential ethical considerations related to data collection, annotation, and the potential impact of our work.

**Data Collection and Provenance.** The data for this benchmark was collected from Reddit, a publicly accessible platform, using its official Application Programming Interface (API). Our data collection adhered to Reddit’s API terms of service. We focused on collecting posts that included both textual context and a meme image. To protect the privacy of Reddit users, all usernames and any other personally identifiable information (PII) were removed from the collected data. The dataset primarily consists of content that users have chosen to share publicly. We acknowledge that internet memes can sometimes contain sensitive or controversial themes.

**Annotation Process and Annotator Considerations.** The annotation of the collected data was performed by 6 Ph.D. students, all of whom are proficient English speakers and have a good understanding of internet culture and memes. Annotators were recruited from our research institution. Prior to commencing the annotation task, all annotators were provided with detailed guidelines and training on the annotation scheme to ensure consistency and quality. They were made aware of the research objectives and how their contributions would be used.

Recognizing that prolonged exposure to online content can sometimes be taxing, and that memes can vary widely in their subject matter, annotators were instructed that they could skip any specific data instance they felt uncomfortable annotating, without any penalty. The annotation tasks were designed to be objective, focusing on the relationship between context, meme, and comments. The PhD students involved in annotation were part of the broader research effort and their contribution is acknowledged; this work formed part of their research activities.

We paid $0.19 for each data annotation. The annotators were compensated with an average hourly wage of $14.82, which is comparable to the local minimum wage. We did not collect any personal information from annotators without their permission.

## References

Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael Harrison, Russell J Hewett, Mojan Javaheripi, Piero Kauffmann, and et al. 2024. Phi-4 technical report. *arXiv preprint arXiv:2412.08905.*

Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, and et al. 2022. Flamingo: a visual language model for few-shot learning. *Advances in neural information processing systems*, 35:23716–23736.

Anthropic. 2025. Claude 3.7 sonnet and claude code. *https://www.anthropic.com/news/claude-3-7-sonnet.*

Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, and et al. 2025. Qwen2.5-vl technical report. *arXiv preprint arXiv:2502.13923.*



<!-- page 0010 -->

Mohit Chandra, Dheeraj Pailla, Himanshu Bhatia, Aadilmehdi Sanchawala, Manish Gupta, Manish Shrivastava, and Ponnurangam Kumaraguru. 2021. “subverting the jewtocracy”: Online antisemitism detection using multimodal deep learning. In *Proceedings of the 13th ACM Web Science Conference 2021*, pages 148–157.

Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, and et al. 2024. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 24185–24198.

Google DeepMind. 2025. Gemini 2.5 pro: Best for coding and complex prompts. *https://deepmind.google/technologies/gemini/pro/*.

Elisabetta Fersini, Francesca Gasparini, Giulia Rizzi, Aurora Saibene, Berta Chulvi, Paolo Rosso, Alyssa Lees, and Jeffrey Sorensen. 2022. Semeval-2022 task 5: Multimedia automatic misogyny identification. In *Proceedings of the 16th International Workshop on Semantic Evaluation (SemEval-2022)*, pages 533–549.

Ming Shan Hee, Wen-Haw Chong, and Roy Ka-Wei Lee. 2023. Decoding the underlying meaning of multimodal hateful memes. In *Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence*, pages 5995–6003.

Ming Shan Hee, Roy Ka-Wei Lee, and Wen-Haw Chong. 2022. On explaining multimodal hateful meme detection models. In *Proceedings of the ACM Web Conference 2022*, pages 3651–3655.

Jianzhao Huang, Hongzhan Lin, Liu Ziyan, Ziyang Luo, Guang Chen, and Jing Ma. 2024. Towards low-resource harmful meme detection with lmm agents. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, pages 2269–2293.

Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, and et al. 2024. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*.

EunJeong Hwang and Vered Shwartz. 2023. Meme-cap: A dataset for captioning and interpreting memes. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 1433–1445.

Douwe Kiela, Suvrat Bhooshan, Hamed Firooz, Ethan Perez, and Davide Testuggine. 2019. Supervised multimodal bitransformers for classifying images and text. *arXiv preprint arXiv:1909.02950*.

Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide Testuggine. 2020. The hateful memes challenge: Detecting hate speech in multimodal memes. *Advances in neural information processing systems*, 33:2611–2624.

Aleksi Knuutila, Anna George, Jonathan Bright, Anna George, and Philip Howard. 2024. The spread of anti-vaccination memes on facebook. In *Multidisciplinary International Symposium on Disinformation in Open Online Media*, pages 86–100. Springer.

Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Peiyuan Zhang, Yanwei Li, Ziwei Liu, and et al. 2024. Llava-onevision: Easy visual task transfer. *arXiv preprint arXiv:2408.03326*.

Hongzhan Lin, Ziyang Luo, Bo Wang, Ruichao Yang, and Jing Ma. 2024. Goat-bench: Safety insights to large multimodal models through meme-based social abuse. *Preprint*, arXiv:2401.01523.

Phillip Lippe, Nithin Holla, Shantanu Chandra, Santhosh Rajamanickam, Georgios Antoniou, Ekaterina Shutova, and Helen Yannakoudakis. 2020. A multimodal framework for the detection of hateful memes. *arXiv preprint arXiv:2012.12871*.

Chen Liu, Gregor Geigle, Robin Krebs, and Iryna Gurevych. 2022. Figmemes: A dataset for figurative language identification in politically-opinionated memes. In *Proceedings of the 2022 conference on empirical methods in natural language processing*, pages 7069–7086.

Ryan M Milner. 2012. The world made meme: Discourse and identity in participatory media.

Jeongsik Park, Khoi PN Nguyen, Terrence Li, Suyeh Shrestha, Megan Kim Vu, Jerry Yining Wang, and Vincent Ng. 2024. Memeintent: Benchmarking intent description generation for memes. In *Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue*, pages 631–643.

Shraman Pramanick, Dimitar Dimitrov, Rituparna Mukherjee, Shivam Sharma, Md Shad Akhtar, Preslav Nakov, and Tanmoy Chakraborty. 2021a. Detecting harmful memes and their targets. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*, pages 2783–2796.

Shraman Pramanick, Shivam Sharma, Dimitar Dimitrov, Md Shad Akhtar, Preslav Nakov, and Tanmoy Chakraborty. 2021b. Momenta: A multimodal framework for detecting harmful memes and their targets. In *Findings of the Association for Computational Linguistics: EMNLP 2021*, pages 4439–4455.

Qwen. 2024. Qvq: To see the world with wisdom. *https://qwenlm.github.io/blog/qvq-72b-preview/*.

Shivam Sharma, Siddhant Agarwal, Tharun Suresh, Preslav Nakov, Md Shad Akhtar, and Tanmoy



<!-- page 0011 -->

Chakraborty. 2023. What do you meme? generating explanations for visual semantic role labelling in memes. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 37, pages 9763–9771.

Shivam Sharma, Tharun Suresh, Atharva Kulkarni, Himanshi Mathur, Preslav Nakov, Md Shad Akhtar, and Tanmoy Chakraborty. 2022. Findings of the constraint 2022 shared task on detecting the hero, the villain, and the victim in memes. In *Proceedings of the Workshop on Combating Online Hostile Posts in Regional Languages during Emergency Situations*, pages 1–11.

Shardul Suryawanshi, Bharathi Raja Chakravarthi, Mihael Arcan, and Paul Buitelaar. 2020. Multimodal meme dataset (multioff) for identifying offensive content in image and text. In *Proceedings of the second workshop on trolling, aggression and cyberbullying*, pages 32–41.

Riza Velioglu and Jewgeni Rose. 2020. Detecting hate speech in memes using multimodal deep learning approaches: Prize-winning solution to hateful memes challenge. *arXiv preprint arXiv:2012.12975*.

Bingbing Wang, Shijue Huang, Bin Liang, Geng Tu, Min Yang, and Ruifeng Xu. 2024. What do they “meme”? a metaphor-aware multi-modal multi-task framework for fine-grained meme understanding. *Knowledge-Based Systems*, 294:111778.

xAI. 2025. Grok 3: The age of reasoning agents. *https://x.ai*.

Jin Xu, Zhifang Guo, Jinzheng He, Hangrui Hu, Ting He, Shuai Bai, Keqin Chen, Jialin Wang, Yang Fan, Kai Dang, and et al. 2025. Qwen2.5-omni technical report. *arXiv preprint arXiv:2503.20215*.

An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, and et al. 2024. Qwen2 technical report. *CoRR*.

Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. 2020. Bertscore: Evaluating text generation with BERT. In *8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020*. OpenReview.net.

## A More Cases

Figure 7, 8, and 9 shows more examples from our proposed MemeReaCon.

## B Statistics of MemeReaCon

Tables 3, 5, and 4 provide comprehensive statistics about our dataset, including distributions across different categories, cross-category relationships, and textual characteristics.

## C Detailed Implementations

This section details the specific prompts and implementation procedures for each task in our MemeReaCon benchmark. The tasks are designed to systematically evaluate models’ abilities to understand contextual memes across different dimensions of complexity. All inferences are conducted through vLLM framework or Huggingface Transformers framework. For BERTScore, we use `microsoft/deberta-xlarge-mnli` as embedding model.

### C.1 Context-Meme Interplay Classification (CMI-C)

This fundamental task evaluates whether models can identify the primary relationship between the context (post text) and the meme image.

**Task Description:** Models must classify the relationship into one of two categories: (1) Context Explain Meme (CEM): The textual context provides necessary information to understand the meme. (2) Meme Enhance Context (MEC): The meme adds additional meaning or humor to the textual context.

**Implementation Details:** (1) **Unimodal Baselines:** For text-only models, we provide detailed descriptions of the meme images. We summarize the descriptions using gpt-4o model via OpenAI API. For image-only models, we render the post text onto the image as a composite manually. (2) **VLM Models:** Receive both the post text and meme image directly through their respective modality inputs. (3) **VRM Models:** Receive the same inputs as VLM models but are additionally instructed to explain their reasoning before providing the final classification.

The prompt is shown in Table 6.

### C.2 Comment Stance and Affective Consistence Classification (CSAC-C)

This dual-aspect task evaluates models’ abilities to analyze social dynamics in comments related to meme posts.

**Task Description:** Models must: (1) Determine the stance of a comment relative to the original post (support, deny, or extension). (2) Detect whether the comment’s literal meaning matches its intended meaning (consistent and inconsistent).

**Implementation Details:**



<!-- page 0012 -->

[Figure: Examples of meme posts and corresponding annotations. Readable text follows.]

**Panel 1 meme:** Book cover: “HOW TO FIT INTO SOCIETY WHEN YOU’RE AN ALIEN FROM AN ALTERNATE UNIVERSE”

**Post Context:** How does one 'fit in'  
**Comment:** Zuckerberg refuses it.

**CMI:** Context Explain Meme  
**MT:** Pure Meme  
**CSAC:** Deny,Inconsistent

**Post Connection:**  
(1) Literally translated as "How to fit into society when you are an alien from an alternative universe"  
(2) People generally don't know how to fit into society as they were an alien.  
(3) Offensively imply Zuckerberg doesn't know how to fit into society.

**Post Intent:**  
Self-mocking fit into society is hard and needed to be a task

**Panel 2 meme:** “THE MOMENT YOU WAKE UP” / “AND REALIZE ITS MONDAY”

**Post Context:** And you realize there are many more to come  
**Comment:** True

**CMI:** Context Explain Meme  
**MT:** Text-In-Meme  
**CSAC:** Support,Consistent

**Post Connection:**  
(1) The prototype of "Monday Trauma" is derived from the classic line "I hate Mondays" in the American comic "Garfield".  
(2) Monday generally means starting work.  
(3) Author implies not prefer working for this and future.

**Post Intent:**  
Complain about needing to work again

**Panel 3 meme:** “Me looking at code that I wrote yesterday:”

**Post Context:** whatWasThat  
**Comment:** check your record with Cursor

**CMI:** Context Explain Meme  
**MT:** Text-out-Meme  
**CSAC:** Extension,Consistent

**Post Connection:**  
(1) Programmers often find themselves in a situation where they cannot understand the code they wrote yesterday today.  
(2) Cursor-like AI can help programmers write code through conversation.  
(3) Today's AI makes it possible for programmers to write code without knowing what code they have written.

**Post Intent:**  
Self-mocking the daily work of programmers.

**Panel 4 meme:** “Error on line 265”

**Post Context:** compilerBeLikeImGonnaMakeYourLifeMiserable  
**Comment:** Clear your build caches, people! Ten times out of nine, these happen because the IDE or the toolchain is catching an old version of your code so the line numbers are no longer valid.

**CMI:** Context Explain Meme  
**MT:** Comic  
**CSAC:** Extension,Consistent

**Post Connection:**  
(1) A programmer find there should not have an error at the compiler indicated line.  
(2) The error line is space line.  
(3) Author makes the joke about personating compiler.  
(4) Clear caches can always help.

**Post Intent:**  
To complain about compiler's misjudge.

Figure 7: Examples of our proposed MemeReaCon (1/3).

[Figure: Examples of meme posts and corresponding annotations. Readable text follows.]

**Panel 1 meme:** “Town in Northern England starter pack” with labels including “Factory that’s been derelict since 1979”, “Museum about the Good Old Days”, “Terrible football team”, “Obesity crisis”, “Is that Chernobyl?”, and “World’s deadliest pub”.

**Post Context:** Northern England  
**Comment:** Definitely not just northern england

**CMI:** Context Explain Meme  
**MT:** Combination  
**CSAC:** Deny,Inconsistent

**Post Connection:**  
(1) Meme shows stereotype of common elements shown in Northern England.  
(2) Comment implies not just northern but all place in England have the same situation.

**Post Intent:**  
Make laugh about stereotype about northern England.

**Panel 2 meme:** “HOW TEACHERS FEEL PLAYING ‘NOT LIKE US’ BECAUSE THE KIDS LIKE RAP” / “HOW DO YOU DO, FELLOW KIDS?”

**Post Context:** Had a teacher play "top 20 trending rap songs" and it was a bunch of tiktok sounds be like:  
**Comment:** Okay kids, time to learn about Aerosmith and Run DMC.

**CMI:** Meme Enhance Context  
**MT:** Text-In-Meme  
**CSAC:** Support,Consistent

**Post Connection:**  
(1) Meme implies that the teacher is confused when hearing the students play the works of rappers  
(2) Post implies the students feel same to the teacher.  
(3) Post implies different musical groups having contrast taste and refuse to accept others.

**Post Intent:**  
Show the experience about musical taste.

**Panel 3 meme:** “Me and rest of the crew looking at the time clock to finish our shift only for a group of randos entering the shop and demanding an order at the last minute:”

**Post Context:** group looks like trouble so we just continue the work  
**Comment:** and the order will be literally every single thing on the menu

**CMI:** Meme Enhance Context  
**MT:** Text-out-Meme  
**CSAC:** Extension,Consistent

**Post Connection:**  
(1) Literally says: "Me and rest of the crew looking at the time clock to finish our shift only for a group of randos entering the shop and demanding an order at the last minute.  
(2) Post complain they continue the work cause new customers come in.  
(3) Comment implies they general put heavy workload to cashers on purpose.

**Post Intent:**  
Complain about the continue working situation.

**Panel 4 meme:** Image of a man in front of a conspiracy board.

**Post Context:** I misunderstood that word a couple of times when I first started to learn Lithuanian  
**Comment:** I bet you will be encountered this again and again

**CMI:** Meme Enhance Context  
**MT:** Pure Meme  
**CSAC:** Support,Consistent

**Post Connection:**  
(1) Lithuanian has a lot of ambiguity words too hard to learn.  
(2) Comment implies when you learn further about Lithuanian, there are more ambiguity you will face.

**Post Intent:**  
Self-mocking the hard to learn Lithuanian ambiguity words.

Figure 8: Examples of our proposed MemeReaCon (2/3).

- **Unimodal Baselines:** Similar adaptations as in the CMI-C task, with comment text included.

- **VLM Models:** Process the entire post-meme-comment triple as a unified input.

- **VRM Models:** Are additionally prompted to consider social and cultural contexts that might influence interpretation of stance and affection.

**Evaluation Metrics:** Accuracy and macro F1-score for the combined classification task with the following matrix (Table 7):

The prompt is shown in Table 8.



<!-- page 0013 -->

[Figure: A grid of four MemeReaCon examples, each pairing a meme image with an annotation box. Visible text includes:

- Meme image labels: “WATCHING A SENIOR DEV”, “GRACEFULLY AND CONFIDENTLY”, “DIVE INTO”, “LEGACY CODE”.  
  Annotation box:  
  **Post Context:** iMetMyFirstJobAfterGraduationAndStartToReviewTheGroup CodeAndDocumentsBeLike  
  **Comment:** Of course I know him ...  
  **CMI:** Meme Enhance Context  
  **MT:** Comic  
  **CSAC:** Extension,Consistent  
  **Post Connection:**  
  (1) Meme shows a senior developer dive into pit named legacy code.  
  (2) Post shows the experience about first job starting with review code and documents.  
  (3) Post implies reviewing code and documents is disaster.  
  **Post Intent:** Show the experience about disaster reviewing legacy group code and documents.

- Meme image text: “When you fix a bug, have no idea what you are doing, but now everything works” and subtitle “[The work is mysterious and important]”.  
  Annotation box:  
  **Post Context:** itsWorkingNoIdeaWhy  
  **Comment:** At least you got that work life balance  
  **CMI:** Context Explain Meme  
  **MT:** Text-out-Meme  
  **CSAC:** Support,Inconsistent  
  **Post Connection:**  
  (1) Meme shows If the code works but you don't know why, don't change it.  
  (2) Post implies don't delve into the underlying principles of the code, just comfort yourself that it works then everything will be solved.  
  (3) Comment implies they actually don't have WLB.  
  **Post Intent:** Show experience about coding working but no idea why.

- Bell-curve meme with readable text including “It has to have all the features!!”, “Make it simple”, and quote text beneath the curve.  
  Annotation box:  
  **Post Context:** asSimpleAsPossible  
  **Comment:** Of all the bell curve memes I've ever seen posted on this sub, this is the one that I most felt in my bones.  
  **CMI:** Meme Enhance Context  
  **MT:** Combination  
  **CSAC:** Support,Consistent  
  **Post Connection:**  
  (1) Ordinary programmers will write complex code and bring themselves pain and trouble.  
  (2) Voltaire was quoted, emphasizing the development of human intelligence from simplicity to complexity and back to simplicity.  
  **Post Intent:** Humorously express that when people face complex needs, returning to a simple way of thinking is often a more effective solution

- Photo of people holding a banner reading “listening to each other's favorite songs is a date”.  
  Annotation box:  
  **Post Context:** Do you agree?  
  **Comment:** Yess! It's like sharing the soundtrack to your soul.  
  **CMI:** Meme Enhance Context  
  **MT:** Pure Meme  
  **CSAC:** Support,Consistent  
  **Post Connection:**  
  (1) Presents an unconventional yet charming view of a date activity.  
  (2) Highlights the significance of shared musical experiences in bonding.  
  **Post Intent:** To show a POV of dating through music.]

Figure 9: Examples of our proposed MemeReaCon (3/3).

| Category | Total (%) | r/meme(s) | r/ProgrammerHumor | r/BritishMemes | r/RelationshipMemes |
|---|---:|---:|---:|---:|---:|
| **Overall Distribution** | **1565 (100%)** | **690 (44.1%)** | **352 (22.5%)** | **256 (16.4%)** | **267 (17.1%)** |
| **Context-Meme Interplay (CMI)** |  |  |  |  |  |
| Context Explains Meme | 796 (50.9%) | 339 (49.1%) | 187 (53.1%) | 126 (49.2%) | 144 (53.9%) |
| Meme Enhances Context | 769 (49.1%) | 351 (50.9%) | 165 (46.9%) | 130 (50.8%) | 123 (46.1%) |
| **Meme Types (MT)** |  |  |  |  |  |
| Pure Meme | 218 (13.9%) | 101 (14.6%) | 32 (9.1%) | 49 (19.1%) | 36 (13.5%) |
| Text-in-Meme | 834 (53.3%) | 365 (52.9%) | 189 (53.7%) | 133 (52.0%) | 147 (55.1%) |
| Text-out-Meme | 247 (15.8%) | 117 (17.0%) | 57 (16.2%) | 36 (14.1%) | 37 (13.9%) |
| Comics | 175 (11.2%) | 68 (9.9%) | 52 (14.8%) | 24 (9.4%) | 31 (11.6%) |
| Combination | 91 (5.8%) | 39 (5.6%) | 22 (6.3%) | 14 (5.5%) | 16 (6.0%) |
| **Comment Stance (CS)** |  |  |  |  |  |
| Support | 732 (46.8%) | 326 (47.2%) | 162 (46.0%) | 118 (46.1%) | 126 (47.2%) |
| Denial | 248 (15.8%) | 109 (15.8%) | 55 (15.6%) | 41 (16.0%) | 43 (16.1%) |
| Extension | 585 (37.4%) | 255 (37.0%) | 135 (38.4%) | 97 (37.9%) | 98 (36.7%) |
| **Comment Affection (CA)** |  |  |  |  |  |
| Consistent | 1194 (76.3%) | 526 (76.2%) | 267 (75.9%) | 196 (76.6%) | 205 (76.8%) |
| Inconsistent | 371 (23.7%) | 164 (23.8%) | 85 (24.1%) | 60 (23.4%) | 62 (23.2%) |

Table 3: Comprehensive statistics of the MemeReaCon Benchmark Dataset showing distribution of all annotation categories across subreddits. Percentages in the “Total Count” column represent proportion of each category within its group, while percentages in subreddit columns show the distribution within that subreddit.

### C.3 Post Connections Generation (PC-G)

This generative task evaluates models’ abilities to articulate the relationships between all elements of a meme post.

**Task Description:** Models must generate a free-form explanation that demonstrates understanding of how the post text, meme image, and comments interrelate.

**Implementation Details:** All models receive adapted inputs as described in previous tasks. The prompt is shown in Table 9.



<!-- page 0014 -->

<table>
  <thead>
    <tr>
      <th rowspan="2">Category</th>
      <th colspan="2">Post Type</th>
      <th colspan="2">Comment Stance</th>
      <th colspan="2">Comment Affection</th>
    </tr>
    <tr>
      <th>CEM</th>
      <th>MEC</th>
      <th>Support</th>
      <th>Deny/Ext.</th>
      <th>Consist.</th>
      <th>Inconsist.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pure Meme</td>
      <td>103 (47.2%)</td>
      <td>115 (52.8%)</td>
      <td>97 (44.5%)</td>
      <td>121 (55.5%)</td>
      <td>167 (76.6%)</td>
      <td>51 (23.4%)</td>
    </tr>
    <tr>
      <td>Text-in-Meme</td>
      <td>431 (51.7%)</td>
      <td>403 (48.3%)</td>
      <td>397 (47.6%)</td>
      <td>437 (52.4%)</td>
      <td>637 (76.4%)</td>
      <td>197 (23.6%)</td>
    </tr>
    <tr>
      <td>Text-out-Meme</td>
      <td>128 (51.8%)</td>
      <td>119 (48.2%)</td>
      <td>118 (47.8%)</td>
      <td>129 (52.2%)</td>
      <td>189 (76.5%)</td>
      <td>58 (23.5%)</td>
    </tr>
    <tr>
      <td>Comics</td>
      <td>87 (49.7%)</td>
      <td>88 (50.3%)</td>
      <td>79 (45.1%)</td>
      <td>96 (54.9%)</td>
      <td>133 (76.0%)</td>
      <td>42 (24.0%)</td>
    </tr>
    <tr>
      <td>Combination</td>
      <td>47 (51.6%)</td>
      <td>44 (48.4%)</td>
      <td>41 (45.1%)</td>
      <td>50 (54.9%)</td>
      <td>68 (74.7%)</td>
      <td>23 (25.3%)</td>
    </tr>
  </tbody>
</table>

Table 4: Cross-category distributions showing how different annotation dimensions relate to each other. Percentages represent row proportions.

<table>
  <thead>
    <tr>
      <th rowspan="2">Text</th>
      <th colspan="3">Word Count</th>
      <th colspan="3">Token Count</th>
    </tr>
    <tr>
      <th>Avg.</th>
      <th>Max</th>
      <th>Min</th>
      <th>Avg.</th>
      <th>Max</th>
      <th>Min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Post Title</td>
      <td>7.8</td>
      <td>24</td>
      <td>3</td>
      <td>10.3</td>
      <td>54</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Meme Text</td>
      <td>14.3</td>
      <td>68</td>
      <td>3</td>
      <td>19.1</td>
      <td>91</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Top Comment</td>
      <td>16.5</td>
      <td>89</td>
      <td>4</td>
      <td>21.7</td>
      <td>112</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Connection</td>
      <td>75.4</td>
      <td>231</td>
      <td>25</td>
      <td>80.4</td>
      <td>246</td>
      <td>32</td>
    </tr>
    <tr>
      <td>Post Intent</td>
      <td>16.8</td>
      <td>92</td>
      <td>11</td>
      <td>22.9</td>
      <td>103</td>
      <td>14</td>
    </tr>
  </tbody>
</table>

Table 5: Text length statistics across different components of the MemeReaCon dataset. Measurements include both word count and tokenization using the Qwen2.5-32b-instruct tokenizer for consistent evaluation.

### C.4 Post Intent Generation (PI-G)

This advanced task tests models’ abilities to infer the implicit communicative intent behind meme posts.

**Task Description:** Models must identify the poster’s likely intent, and generate with free-form sentence to show the specific author’s intent.

**Implementation Details:** All models receive adapted inputs as described in previous tasks. The prompt is shown in Table 10.

## D Further Analysis Experiments

### D.1 Community-Specific Performance Analysis

Understanding how models perform across different online communities provides critical insights into their ability to comprehend diverse social contexts. We analyze model performance across five popular subreddits to assess how community-specific knowledge affects contextual understanding capabilities.

Table 11 reveals a consistent and significant performance drop across all models when processing content from specialized communities. All evaluated models perform substantially worse on r/ProgrammerHumor (requiring technical knowledge) and r/BritishMemes (requiring cultural context) compared to general meme communities. Interestingly, we observe that the performance gap between specialized and general communities widens as task complexity increases. For the generative PI-G task requiring deeper contextual reasoning, performance degradation is more severe than for the classification-based CMI-C task. This suggests that specialized knowledge gaps compound when models must perform multi-step reasoning, revealing a fundamental limitation in current contextual understanding capabilities.

The consistent performance differential across community types persists regardless of model scale or architecture, indicating that current pre-training approaches may not adequately capture the specialized knowledge and cultural contexts necessary for understanding community-specific content. This finding challenges the assumption that scaling alone can solve contextual understanding problems, suggesting that targeted approaches to incorporate domain-specific knowledge may be necessary for developing models with robust cross-community understanding capabilities.

### D.2 Meme Structure Performance Analysis

The structural configuration of memes significantly impacts model comprehension, revealing important insights about how LVLMs process multimodal content. Table 12 shows performance across five distinct meme structures: pure meme (PM), Text-in-Meme (TIM), Text-out-Meme (TOM), comics (Comic), and combination (Comb).

Our analysis reveals a consistent pattern where Vision Reasoning Models (VRMs) substantially outperform standard Vision-Language Models (VLMs) across all structural configurations, with an average performance gap of 10-15%. This gap



<!-- page 0015 -->

<table>
<tr>
<td>

<strong>For VLM and VRM models</strong><br>
Given this social media post with text and an image meme:

Post text: &lt;post text&gt;<br>
&lt;Meme image is provided&gt;

Analyze the relationship between the post text and the meme image. Determine which of the following is true:<br>
A. The post text primarily explains or provides context needed to understand the meme image (CEM).<br>
B. The meme image primarily enhances, illustrates, or adds humor to the post text (MEC).

Select only A or B.

<strong>For text-only models</strong><br>
Given this social media post with text and an image meme:

Post text: &lt;post text&gt;<br>
Meme description: &lt;meme description&gt;

Analyze the relationship between the post text and the meme image. Determine which of the following is true:<br>
A. The post text primarily explains or provides context needed to understand the meme image (CEM).<br>
B. The meme image primarily enhances, illustrates, or adds humor to the post text (MEC).

Select only A or B.

<strong>For image-only models</strong><br>
&lt;Meme image and post text are provided as a composite image&gt;

Analyze this social media post. Determine which relation is true:<br>
A. Context Explain Meme (CEM)<br>
B. Meme Enhance Context (MEC)<br>
Select only A or B.

</td>
</tr>
</table>

Table 6: Prompt for Context-Meme Interplay task.

|  | Support | Deny | Extension |
|---|---|---|---|
| **Consistent** | Support | Deny | Extension |
| **Inconsistent** | Deny | Support | Extension |

Table 7: Real comments type matrix to show both literal meaning and intended meaning.

widens most dramatically for Text-in-Meme (TIM, $\Delta = 14.87\%$), suggesting that VRMs possess superior capabilities for integrating visual and textual elements when they spatially overlap. Interestingly, all models struggle most with comic formats and combination formats (Comb), which require tracking narrative flow across sequential images and understanding relationships between multiple visual elements.

The performance hierarchy (TIM > TOM > PM > Comic > Comb) across model types indicates that current architectures find it easier to process memes where text and image are tightly integrated in a single visual space, compared to formats requiring sequential reasoning or cross-referencing between multiple visual elements. This finding highlights a critical limitation in current LVLMs: while they can effectively process localized multimodal information, they struggle with distributed multimodal reasoning tasks that more closely resemble how humans process complex social media content. The substantial performance degradation on combined formats (12.89% below TIM for VRMs) demonstrates that even state-of-the-art models have not yet bridged the gap between processing isolated multimodal elements and understanding holistic multimodal narratives.

### D.3 Meme Text-Density Analysis

Memes exhibit significant variation in text density, ranging from image-dominant formats with minimal text to text-heavy variants where the visual component serves primarily as a backdrop. This variability presents unique challenges for multimodal understanding. To systematically investigate how text density affects model performance, we categorized memes in our dataset into three distinct groups: low-text (0-10 words), medium-text (11-30 words), and high-text (>30 words). This analysis specifically focuses on the Post Intent Prediction (PI-G) task, as this requires comprehensive integration of visual and textual elements.

As illustrated in Figure 10, the performance gap between high-text and low-text memes narrows sig-



<!-- page 0016 -->

**For VLM and VRM models**  
Analyze this social media interaction:

Post text: \<post text>  
\<Meme image is provided>  
Comments: \<comment>

Part 1 - Stance Analysis: Determine the stance of the comment toward the post:  
A. Support (the comment agrees with or reinforces the post)  
B. Deny (the comment disagrees with or contradicts the post)  
C. Extension (the comment adds information without clearly agreeing or disagreeing)

Part 2 - Affection Analysis: Determine whether:  
A. Consistent (the comment means exactly what it says)  
B. Inconsistent (the comment uses irony, sarcasm, or other figurative language)

Provide your answer as two letters, one for each part (e.g., "A, B").

**For text-only models**  
Analyze this social media interaction:

Post text: \<post text>  
Meme description: \<meme description>  
Comments: \<comment>

Part 1 - Stance Analysis: Determine the stance of the comment toward the post:  
A. Support (the comment agrees with or reinforces the post)  
B. Deny (the comment disagrees with or contradicts the post)  
C. Extension (the comment adds information without clearly agreeing or disagreeing)

Part 2 - Affection Analysis: Determine whether:  
A. Consistent (the comment means exactly what it says)  
B. Inconsistent (the comment uses irony, sarcasm, or other figurative language)

Provide your answer as two letters, one for each part (e.g., "A, B").

**For image-only models**  
\<Meme image, post text, and comments are provided as a composite image>

Analyze this interaction. Determine:  
1. Comment stance: A. Support, B. Deny, C. Extension  
2. Comment tone: A. Consistent, B. Inconsistent  
Answer with two letters (e.g., "A, B").

Table 8: Prompt for Comment Stance + Affection task.

[Figure: Two bar charts. Left chart titled “Performance Gap by Model” with y-axis “ROUGE-L Score Gap (High-Text minus Low-Text)” and legend “Unimodal Text”, “Unimodal Image”, “VLM”, “VRM”. Bars labeled Qwen2.5 17.1, Flamingo -4.9, LLaVA-OneVis 6.9, Phi-4-MM 7.1, Qwen2.5-VL 7.6, Qwen2.5-Omni 7.4, InternVL3 7.4, QvQ 5.7, gpt-4o 5.1, Grok3 5.0, Claude-3.7-sonnet 4.8, Gemini-2.5-Pro 4.9. Right chart titled “Average Gap” with bars Unimodal 6.1, VLM 7.3, VRM 5.1.]

Figure 10: Performance gap between high-text and low-text memes across model categories. Positive values indicate better performance on high-text memes. The gap narrows significantly for Vision Reasoning Models, demonstrating their superior cross-modal integration capabilities.

nificantly as model sophistication increases. While VLMs show an average ROUGE-L performance



<!-- page 0017 -->

<table>
<tr>
<td>
<strong>For VLM and VRM models</strong><br>
Analyze this social media post and its comments:<br><br>

Post text: &lt;post text&gt;<br>
&lt;Meme image is provided&gt;<br>
Comments: &lt;comment&gt;<br><br>

Explain in 3-5 sentences how the following elements connect and interact:<br>
1. The relationship between the post text and the meme image<br>
2. How the comments respond to the post’s message<br>
3. Whether the post achieves its apparent communicative purpose<br><br>

Be specific about how visual and textual elements work together to create meaning.<br><br>

<strong>For text-only models</strong><br>
Analyze this social media post and its comments:<br><br>

Post text: &lt;post text&gt;<br>
Meme description: &lt;meme description&gt;<br>
Comments: &lt;comment&gt;<br><br>

Explain in 3-5 sentences how the following elements connect and interact:<br>
1. The relationship between the post text and the meme image<br>
2. How the comments respond to the post’s message<br>
3. Whether the post achieves its apparent communicative purpose<br><br>

Be specific about how visual and textual elements work together to create meaning.<br><br>

<strong>For image-only models</strong><br>
&lt;Meme image, post text, and comments are provided as a composite image&gt;<br><br>

Explain how the text, image, and comments in this post connect. Focus on:<br>
1. Text-image relationship<br>
2. Comment responses<br>
3. Post effectiveness<br>
(3-5 sentences)
</td>
</tr>
</table>

Table 9: Prompt for Post Connection task.

difference of 7.3 points between high-text and low-text memes, this gap shrinks to just 4.7 points for VRMs. Claude-3.7-sonnet exhibits the smallest gap at 4.8 points, suggesting that advanced reasoning mechanisms enable more balanced processing of multimodal content regardless of text-image ratio. This finding has significant implications for meme understanding systems, indicating that sophisticated reasoning capabilities, rather than simply larger model size, are crucial for handling the diverse spectrum of meme formats encountered in real-world social media.

### D.4 Comment Affection Analysis

Social media conversations often involve complex dynamics where comments may support, deny, or extend the original post while conveying affective meanings that can be inconsistent with their literal content. This section explores how these comment characteristics influence models’ ability to understand the relationship between posts and memes.

We designed experiments to analyze how models’ performance varies across different comment types (support, deny, extension) and affection patterns (consistent vs. inconsistent). Consistent affection occurs when the literal meaning aligns with the intended sentiment (e.g., sincere praise), while inconsistent affection involves misalignment (e.g., sarcastic “praise” that actually criticizes). We present data to models under three conditions: (1) without comments, (2) with consistent-affection comments, and (3) with inconsistent-affection comments. For each condition, we evaluated performance on the Post Intent Prediction (PI-G) task, which requires inferring the poster’s communicative intent.

As shown in Table 13, both Gemini-2.5-pro and Qwen2.5-VL models experience a substantial performance disparity between consistent and inconsistent affection scenarios. When presented with comments whose affective meaning contradicts their literal content (inconsistent affection), even leading Vision Reasoning Models (VRMs) suffer performance drops of 20-25 percentage points com-



<!-- page 0018 -->

**For VLM and VRM models**  
Analyze this social media post with its meme and comments:

Post text: \<post text>  
\<Meme image is provided>  
Comments: \<comment>

Based on all available evidence, what was the poster’s primary communicative intent?  
The intent means the purpose, aim, or goal behind an action, statement, or piece of communication.  
It represents what a person or entity intends to convey or achieve.  
Provide your answer as a brief sentence.

**For text-only models**  
Analyze this social media post with its meme and comments:

Post text: \<post text>  
Meme description: \<meme description>  
Comments: \<comment>

Based on all available evidence, what was the poster’s primary communicative intent?  
The intent means the purpose, aim, or goal behind an action, statement, or piece of communication.  
It represents what a person or entity intends to convey or achieve.  
Provide your answer as a brief sentence.

**For image-only models**  
\<Meme image, post text, and comments are provided as a composite image>

What was the poster’s primary communicative intent?  
The intent means the purpose, aim, or goal behind an action, statement, or piece of communication.  
It represents what a person or entity intends to convey or achieve.  
Provide your answer as a brief sentence.

Table 10: Prompt for Post Intent Prediction task.

| Model | r/memes | r/meme | r/ProgrammerHumor | r/BritishMemes | r/RelationshipMemes |
|---|---:|---:|---:|---:|---:|
| *CMI-C Task (Accuracy %)* |  |  |  |  |  |
| Qwen2.5-VL | 64.57 | 65.12 | 53.28 | 58.76 | 65.79 |
| InternVL3 | 61.32 | 63.46 | 51.43 | 57.21 | 62.94 |
| Gemini-2.5-pro | 85.72 | 86.19 | 72.33 | 77.83 | 88.03 |
| Max △ | 24.40 | 22.73 | 20.90 | 20.62 | 25.09 |
| *PI-G Task (ROUGE-L %)* |  |  |  |  |  |
| Qwen2.5-VL | 18.34 | 19.07 | 12.52 | 14.79 | 17.63 |
| InternVL3 | 15.87 | 16.92 | 10.28 | 12.44 | 15.97 |
| Gemini-2.5-pro | 45.41 | 46.13 | 35.04 | 39.54 | 45.59 |
| Max △ | 29.54 | 29.21 | 24.76 | 27.10 | 29.62 |

Table 11: Performance across subreddits for representative models. Best and worst performance for each model are highlighted. Max △ shows the gap between highest and lowest performing models.

pared to consistent affection scenarios. This gap, which we term the “Context-Affection Gap,” is most pronounced in deny comments with inconsistent affection (e.g., sarcastic agreement that actually contradicts). For instance, Gemini-2.5-Pro achieves 76.1% accuracy with consistent denial comments but only 52.0% with inconsistent denial comments.

This finding suggests that current LVLMs struggle with communication where literal meaning diverges from intended meaning. The narrower gap observed in VRMs compared to VLMs indicates that advanced reasoning models are hurt more by providing opposite points of view.

**D.5 Modality Contribution Analysis**

To investigate how different elements of posts contribute to model understanding, we conducted systematic ablation experiments by removing or replacing key components. Table 14 shows perfor-



<!-- page 0019 -->

| Model Type | PM | TIM | TOM | Comic | Comb |
|---|---:|---:|---:|---:|---:|
| Qwen-VL | 58.73 | 64.92 | 60.37 | 54.68 | 52.94 |
| InternVL3 | 65.28 | 71.43 | 67.58 | 59.76 | 59.05 |
| VLMs (avg) | 58.42 | 65.31 | 60.73 | 55.14 | 52.87 |
| VRMs (avg) | 68.73 | 80.18 | 73.42 | 64.52 | 65.76 |
| Δ* | 10.31 | 14.87 | 12.69 | 9.38 | 12.89 |

Table 12: Impact of meme structural configuration on PC-G task performance. PM: Pure Memes without text overlay; TIM: Text-in-Meme; TOM: Text-out-Meme; Comic: comic format; Comb: Multiple images combination. Δ* indicates average performance gap between VRMs and VLMs.

mance changes when manipulating either textual context or visual elements.

Our findings reveal several interesting patterns. First, image removal causes dramatically larger performance drops than text removal, with PC-G task performance declining by 34.28% for Qwen2.5-VL compared to just 12.13% when text is removed. This suggests that memes serve as the primary information carrier in these multimodal posts, even for the “Meme to enhance context” setting. Second, models perform better with mismatched components than with missing ones: random text produces smaller drops (7.57% for Qwen2.5-VL on PC-G) than no text (12.13%). This indicates models use whatever context is available to create meaning, even when connections are tenuous.

Most surprisingly, we find that smaller models like Qwen2.5-VL show greater sensitivity to modality manipulation than larger ones like Gemini-2.5-Pro. When presented with random images, Qwen2.5-VL’s performance drops by 31.84% on PC-G tasks, while Gemini-2.5-Pro decreases by only 12.04%. This suggests that reasoning models develop more robust internal representations that can partially recover from contextual mismatches, effectively “filtering out” irrelevant information. These findings highlight a critical gap in current models: while they can process multimodal inputs, they struggle to determine which elements should be contextually emphasized or disregarded, which is a fundamental aspect of human social media consumption that remains challenging for LVLMs.

## E Error Analysis Description and Performance

We categorized errors into four distinct patterns that emerged consistently across models (Figure 11). The distribution of these errors varies significantly

[Figure: Bar chart showing distribution of error types across model categories. Y-axis: “Percentage of Errors (%)”. X-axis groups: Unimodal, VLM, VRM. Legend: Context, Visual, Semantic, Cultural. Values shown include Unimodal: 52.3, 8.7, 23.4, 15.6; VLM: 41.7, 28.4, 19.3, 10.6; VRM: 22.5, 24.8, 32.9, 19.8.]

Figure 11: Distribution of error types across model categories when interpreting memes in context. Vision Reasoning Models (VRMs) make fewer context-neglect errors but struggle more with contextual conflicts than Vision-Language Models (VLMs).

between model architectures, revealing fundamental differences in contextual processing capabilities. The four primary error patterns we identified are:

- **Context:** Models process the meme in isolation, disregarding crucial context from the post text or comments. This was most prevalent in VLMs (41.7%) and less common in VRMs (22.5%), suggesting that reasoning-enhanced architectures better incorporate textual context.

- **Visual:** Models overemphasize visually important but contextually irrelevant image elements. This error occurred when models focused on character objects rather than the socially relevant aspects indicated by the post.

- **Semantic:** Initially correct interpretations gradually go wrong as response length increases. Notably, this was highest among VRMs (32.9%), suggesting that more powerful generative capabilities sometimes lead to unfocused elaboration.

- **Cultural:** Models fail to recognize community-specific references, slang, or humor conventions. This affects all model classes but was most pronounced in VRMs (19.8%), possibly due to their attempts at more complex reasoning about unfamiliar cultural elements.

## F More Error Cases

We show more error cases covering each error type in Figure 12 and 13.



<!-- page 0020 -->

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th rowspan="2">No Comments</th>
<th colspan="3">Consistent Affection</th>
<th colspan="3">Inconsistent Affection</th>
</tr>
<tr>
<th>Support</th>
<th>Deny</th>
<th>Extend</th>
<th>Support</th>
<th>Deny</th>
<th>Extend</th>
</tr>
</thead>
<tbody>
<tr>
<td>Qwen2.5-VL</td>
<td>66.2</td>
<td>62.3</td>
<td>58.7</td>
<td>55.2</td>
<td>40.1</td>
<td>37.2</td>
<td>43.8</td>
</tr>
<tr>
<td>Gemini-2.5-Pro</td>
<td>83.2</td>
<td>82.7</td>
<td>76.1</td>
<td>73.8</td>
<td>58.2</td>
<td>52.0</td>
<td>61.3</td>
</tr>
</tbody>
</table>

Table 13: Model performance on Post Intent Prediction (PI-G) task with different comment types and affection patterns. Results show ROUGE-L (%).

<table>
<thead>
<tr>
<th rowspan="2">Settings</th>
<th colspan="2">PC-G</th>
<th colspan="2">PI-G</th>
<th colspan="2">PC-G</th>
<th colspan="2">PI-G</th>
</tr>
<tr>
<th>R-L (%)</th>
<th>△</th>
<th>R-L (%)</th>
<th>△</th>
<th>R-L (%)</th>
<th>△</th>
<th>R-L (%)</th>
<th>△</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td colspan="4"><strong><em>Qwen2.5-VL</em></strong></td>
<td colspan="4"><strong><em>Gemini-2.5-Pro</em></strong></td>
</tr>
<tr>
<td>Original</td>
<td>60.38</td>
<td>-</td>
<td>44.86</td>
<td>-</td>
<td>38.92</td>
<td>-</td>
<td>20.43</td>
<td>-</td>
</tr>
<tr>
<td>No Text</td>
<td>48.25</td>
<td>-12.13</td>
<td>36.42</td>
<td>-8.44</td>
<td>30.47</td>
<td>-8.45</td>
<td>10.69</td>
<td>-9.74</td>
</tr>
<tr>
<td>Random Text</td>
<td>52.81</td>
<td>-7.57</td>
<td>38.67</td>
<td>-6.19</td>
<td>32.50</td>
<td>-6.42</td>
<td>15.30</td>
<td>-5.13</td>
</tr>
<tr>
<td>No Image</td>
<td>26.10</td>
<td>-34.28</td>
<td>21.69</td>
<td>-23.17</td>
<td>22.66</td>
<td>-16.26</td>
<td>14.98</td>
<td>-5.45</td>
</tr>
<tr>
<td>Random Image</td>
<td>28.34</td>
<td>-31.84</td>
<td>23.45</td>
<td>-21.21</td>
<td>26.88</td>
<td>-12.04</td>
<td>17.25</td>
<td>-3.18</td>
</tr>
</tbody>
</table>

Table 14: Performance of modality contribution analysis. “Original” uses the meme’s actual context; “Random Text” and “Random Image” uses mismatched context/image from a different post. “No Text” and “No Image” removes post title/image. Text modified for Meme to Enhance Context setting (MEC), while image modified for Context to explain meme setting (CEM).

[Figure: Error cases shown in two rows with meme images, Generated panels, Golden panels, and Error Analysis panels. Top meme text: “HOW HIGH ARE YOU?” and “NO OFFICER, ITS "HI HOW ARE YOU"?” Generated panel: “Post Context: Ripped on old memes”; “Comment: always”; “CMI: Meme Enhance Context”; “MT: Text-in-Meme”; “CSAC: Extension,Consistent”; “Post Connection: (1) The meme literally says "how high are you?" and bottom is "no officer, it's 'hi how are you?' indicate the mismatch of these two sentences. (2) The meme contains a smiling character to kindly show the suggestions. (3) The post means the meme is long since produced and can still amuse author”; “Post Intent: To show the amusement of kindly communication.” Golden panel: “Post Context: Ripped on old memes”; “Comment: always”; “CMI: Context Explain Meme”; “MT: Text-in-Meme”; “CSAC: Support,Consistent”; “Post Connection: (1) Post indicate this meme was posted before and can still make author laugh. (2) Meme describe a drunken face. (3) The talk "no officer" indicate he was caught by police and argue for he was not drunk. (4) He misunderstands the police instruct and plays word game to argue for he was not drunk.”; “Post Intent: To show the interesting meme that a man is drunk with ridiculously arguing by himself.” Error Analysis: “(Context) (1) wrongly understand the word game about "how high" and "hi how". Also fail to understand the difference between this two sentence. (2) fail to recognize the meme's situation that is facing a police officer.” Bottom meme text: “IF TWO VEGANS ARE ARGUING IS IT STILL CONSIDERED BEEF?” Generated panel: “Post Context: Dead memes are making a comeback you say?”; “Comment: Plant based”; “CMI: Meme Enhance Context”; “MT: Combination”; “CSAC: Support,Inconsistent”; “Post Connection: (1) The meme literally says "if two vegans are arguing, is it still considered beef?" Vegan means only accept vegetables for eating. Beef means cattle meat also means complaint. Here meme mix the two meaning of Beef to make a joke. (2) A Raptor shows to represent the meat because using beef may offend some group. (3) The post means the meme was produced before.”; “Post Intent: To tell a joke about two different meaning of "beef".” Golden panel: “Post Context: Dead memes are making a comeback you say?”; “Comment: Plant based”; “CMI: Context Explain Meme”; “MT: Text-in-Meme”; “CSAC: Support,Consistent”; “Post Connection: (1) Beef here means complaint w.r.t. "arguing" but makes laugh by co-existing with "vegans". (2) Post indicates this meme was posted before and can still make author laugh. (3) Comment shows further joke to explain this "beef" is "plant based". (4) Dinosaur shows in meme center to represent the confusing condition.”; “Post Intent: To show the interesting meme around "vegan arguing" and two meaning of "beef".” Error Analysis: “(Visual) (1) wrongly understand the dinosaur's role here (not representing meat). (2) Ignore the comment connection in the post.”]

Figure 12: Error cases for Context error and Visual error. The green text indicates the correct answer compared with golden. The red text indicates the wrong answer.



<!-- page 0021 -->

[Figure: Error cases for Semantic error and Culture error. The figure shows two meme examples on the left and generated/golden analyses with error analysis boxes on the right. Top meme text: “fun fact: the reason your internal body temperature rises when you are infected is because viruses are using your body to mine for bitcoin,” with thermal body images. Bottom meme text: “i don't use ChatGPT in 2025,” “wow, that's amazing,” and “I use copilot,” over a Simpsons scene. The analysis boxes include labels such as “Generated,” “Golden,” “Post Context,” “Comment,” “CMI,” “MT,” “CSAC,” “Post Connection,” “Post Intent,” and “Error Analysis: (Semantic),” “Error Analysis: (Visual),” “Error Analysis: (Culture).”]

Figure 13: Error cases for Semantic error and Culture error. The green text indicates the correct answer compared  
with golden. The red text indicates the wrong answer.
