<!-- Transcribed from x29-d-humor.pdf -->



<!-- page 0001 -->

# D-HUMOR: Dark Humor Understanding via Multimodal Open-ended Reasoning  
# - A Benchmark Dataset and Method

Sai Kartheek Reddy Kasu<sup>†</sup> (Indian Institute of Information Technology Dharwad, India)  
Mohammad Zia Ur Rehman<sup>†</sup> (Indian Institute of Technology Indore, India)  
Shahid Shafi Dar (Indian Institute of Technology Indore, India)  
Rishi Bharat Junghare (Indian Institute of Technology Indore, India)  
Dhanvin Sanjay Namboodiri (Malaviya National Institute of Technology Jaipur, India)  
Nagendra Kumar<sup>*</sup> (Indian Institute of Technology Indore, India)

**Email(s):** 21bds027@iiitdwd.ac.in, phd2101201005@iiti.ac.in, phd2201201004@iiti.ac.in, cse220001063@iiti.ac.in,  
2022uec1253@mnit.ac.in, nagendra@iiti.ac.in

<sup>†</sup>These are co-first authors with equal contribution.  
<sup>*</sup>Corresponding author

This is the preprint version of the accepted paper.  
**Accepted in *IEEE International Conference on Data Mining (ICDM), 2025***

arXiv:2509.06771v2 [cs.CV] 30 Oct 2025



<!-- page 0002 -->

# D-HUMOR: Dark Humor Understanding via Multimodal Open-ended Reasoning - A Benchmark Dataset and Method

Sai Kartheek Reddy Kasu<sup>†</sup>  
*Indian Institute of Information Technology Dharwad, India*  
21bds027@iiitdwd.ac.in

Mohammad Zia Ur Rehman<sup>†</sup>  
*Indian Institute of Technology Indore, India*  
phd2101201005@iiti.ac.in

Shahid Shafi Dar  
*Indian Institute of Technology Indore, India*  
phd2201201004@iiti.ac.in

Rishi Bharat Junghare  
*Indian Institute of Technology Indore, India*  
cse220001063@iiti.ac.in

Dhanvin Sanjay Namboodiri  
*Malaviya National Institute of Technology Jaipur, India*  
2022uec1253@mnit.ac.in

Nagendra Kumar<sup>*</sup>  
*Indian Institute of Technology Indore, India*  
nagendra@iiti.ac.in

**Abstract—**Dark humor in online memes poses unique challenges due to its reliance on implicit, sensitive, and culturally contextual cues. To address the lack of resources and methods for detecting dark humor in multimodal content, we introduce a novel dataset of 4,379 Reddit memes annotated for dark humor, target category (gender, mental health, violence, race, disability, and other), and a three-level intensity rating (mild, moderate, severe). Building on this resource, we propose a reasoning-augmented framework that first generates structured explanations for each meme using a Large Vision–Language Model (VLM). Through a Role-Reversal Self-Loop, VLM adopts the author’s perspective to iteratively refine its explanations, ensuring completeness and alignment. We then extract textual features from both the OCR transcript and the self-refined reasoning via a text encoder, while visual features are obtained using a vision transformer. A Tri-stream Cross-Reasoning Network (TCRNet) fuses these three streams, text, image, and reasoning, via pairwise attention mechanisms, producing a unified representation for classification. Experimental results demonstrate that our approach outperforms strong baselines across three tasks: dark humor detection, target identification, and intensity prediction. The dataset, annotations, and code are released to facilitate further research in multimodal humor understanding and content moderation.  
**Code and Dataset Access:** https://github.com/Sai-Kartheek-Reddy/D-Humor-Dark-Humor-Understanding-via-Multimodal-Open-ended-Reasoning

**Index Terms—**Multimodal Data Mining, Dark Humor Detection, VLMs, Social Media Analysis, Content Moderation.

**Caution:** This paper contains offensive content due to the nature of the topic, which may be disturbing or offensive to some readers. Reader discretion is advised.

## I. Introduction

Dark humor represents a challenging domain for data mining, as it uses subtle elements to convey complex and often controversial forms of humor. The difference between conventional “clean” humor and dark humor can be quite subtle. While there can never be an objective way to distinguish them, there are some key identifiers for dark humor. Clean humor generally uses topics that everyone can relate to and collectively laugh at. On the other hand, dark humor exploits topics that are typically considered insensitive, as shown in Figure 1. According to Ruch et al. [1], dark humor typically incorporates one of four distinct elements, sarcasm, cynicism, satire, or irony, each characterized by unique linguistic and cognitive features that shape its expression.

[Figure: Four meme examples arranged in a 2×2 grid. Top-left text: “IM JUST GONNA SAY IT” and “PEOPLE HATE PINEAPPLE ON PIZZA BECAUSE OF THE INTERNET”. Top-right text: “Tax return: $1200” and “Me: put 4 eggs in my omelette...”. Bottom-left text: “DARK HUMOR NEVER GROWS OLD...” and “LIKE KIDS WITH CANCER.” Bottom-right text: “FINALLY” and “‘I’VE GATHERED THE WHOLE FAMILY”.]

(a) Clean humor

(b) Clean humor

(c) Dark humor

(d) Dark humor

Fig. 1: A comparison of clean and dark humor (Source: Reddit).

<sup>†</sup>These are co-first authors with equal contribution.  
<sup>*</sup>Corresponding author



<!-- page 0003 -->

However, in today’s digital landscape, social media platforms frequently convey dark humor not just through linguistic expressions but also by image-text combinations [2], [3] such as memes, which add a multimodal layer to their interpretation. While memes have become a dominant form of online communication, detecting dark humor within them remains an underexplored problem due to the interplay between imagery, text, and cultural context. Effectively mining and detecting dark humor memes requires multimodal approaches capable of integrating textual and visual cues to accurately capture these subtle humor styles [4], [5]. Advancing automated detection in this space can significantly enhance content moderation, sentiment analysis, and the broader understanding of how humor operates in complex, multimodal social media data [6]. However, to the best of our knowledge, there exists no multimodal dark humor dataset, which limits progress in this underexplored yet critical area.

To address the scarcity of resources for studying dark humor in memes, we introduce a novel dataset comprising a large collection of memes sourced from popular social media platforms, each containing both visual and textual components for comprehensive multimodal analysis. Annotators annotated the dataset not only to distinguish between dark humor and non-dark humor memes in a binary classification framework but also to identify target groups commonly referenced or affected by dark humor, including gender, mental health, violence, race, disability, and other sensitive categories. This granular labeling supports a deeper exploration of the social and ethical dimensions embedded within dark humor, enabling both the technical challenge of humor detection and the analysis of its underlying themes and potential impacts in online meme culture. Since humor plays an important role in mental health [7], [8], our dataset could be an important resource.

In addition to the dataset, we propose a novel multimodal approach for dark humor detection in memes that harnesses the complementary strengths of large language models (LLMs) [9] and visual-textual feature extraction. Specifically, we first employ the Qwen-2.5-7B Vision–Language Model to generate an initial structured reasoning for each meme, capturing high-level contextual and inferential cues. Next, we apply an Iterative Reasoning Refinement via Role-Reversal Self-Loop. Qwen is prompted to “become the original author” of the meme and critically review its own explanation, verifying that each field (summary, implied joke, narrative structure, emotional effect, dark attributes, and target) is both faithful and complete. This role-reversal step mimics reflective human reasoning, encouraging the model to correct omissions or misalignments before yielding a final, refined explanation. Textual features are then extracted from both the meme’s transcript using BERT and the self-refined reasoning using S-BERT, while visual features are obtained via ViT for multimodal representation learning. To effectively model the interplay among text, image, and reasoning, we employ a Tri-stream Cross-Reasoning Network (TCRNet) that applies pairwise scaled dot-product attention across all three modalities. The resulting attended representations are concatenated into a unified feature vector, which is passed to a final classification head. This pipeline, combining self-refined reasoning with multimodal fusion, demonstrates the power of hybrid, alignment-aware architectures in capturing the nuanced affective and figurative characteristics of dark humor in social media memes.

Key Contributions of this work are as follows:

- **Dark Humor Meme Dataset:** We introduce a first multimodal dark humor dataset consisting of memes collected from Reddit. Each entry includes both image and OCR-extracted text, annotated not only for binary *dark humor* versus *non-dark humor*, but also for *target category* (gender, mental health, violence, race, disability, and other) and a three-level *intensity* rating (mild, moderate, severe). This granular annotation enables detailed analysis of social and ethical dimensions in dark humor in memes.
- **Iterative Self-Refined Reasoning:** We use Qwen-2.5-7B VLM to generate an initial structured explanation (summary, implied joke, narrative, emotional effect, dark attributes, target). Then, via a *Role-Reversal Self-Loop*, Qwen assumes the meme author’s perspective to critique and refine its own reasoning, ensuring higher alignment and completeness before feature extraction.
- **Reasoning-Enhanced Multimodal Framework:** We propose a multimodal architecture that fuses image embeddings, text embeddings, and embeddings of the self-refined Qwen reasoning through a Tri-stream Cross-Reasoning Network (TCRNet). Pairwise attention across the three streams captures implicit and semantic cues, yielding state-of-the-art performance on dark humor detection, target identification, and intensity prediction.

## II. LITERATURE REVIEW

Dark humor, while increasingly present in online discourse, remains underexplored in computational linguistics. Unlike general humor detection, dark humor poses unique challenges due to its reliance on morally deviant, taboo, or emotionally provocative content. Ruch et al. [1] identify four rhetorical styles central to dark humor, sarcasm, cynicism, satire, and irony, each involving complex linguistic and psychological cues. While studies directly targeting dark humor are rare, significant advances have been made in detecting its constituent forms.

Sarcasm detection has seen considerable progress, particularly through multimodal approaches. Bao et al. [10] proposed HIAN, which uses BiLSTM, attention, and transformers to fuse text, image, and class-based features, capturing cross-modal inconsistencies indicative of sarcasm. Gupta et al. [11] extended this with MLFTI, a weighted multimodal fusion model combining text and visual cues in a shared latent space, achieving 93% accuracy on Twitter data. Jia et al. [12] addressed generalization challenges with DMSD-CL, which uses counterfactual data augmentation and contrastive learning to reduce bias from spurious correlations. Liang et al. [13] introduced MMGCL, a graph-based contrastive learning model that integrates text, OCR, and visual objects, effectively mod-



<!-- page 0004 -->

eling sentiment incongruity, an important signal in sarcastic and darkly humorous content.

Irony detection has also been actively explored. Saroj and Pal [14] demonstrated the importance of domain adaptation with an ensemble of contextual models fine-tuned for political discourse. Maladry et al. [15] achieved strong results in Dutch by combining transformer models with engineered sentiment-clash features. In a low-resource setting, Bölücü and Can [16] employed UCCA-based graph neural networks for Turkish irony detection, achieving an F1-score of 94.85%, and demonstrating the value of structured semantic modeling.

Satire, though less studied, has seen recent computational advances. Goyal et al. [17] contrasted satire with sarcasm in a multimodal framework, combining BERT, ResNet, and I3D to capture linguistic and visual nuances. Ortega-Bueno et al. [18] proposed MvAttLSTM, a multilingual model that integrates linguistic, sentence-level, and contextual embeddings to detect satire and irony in Spanish. Kamal et al. [19] introduced BiSAT, a BiLSTM with self-attention and handcrafted linguistic features, achieving strong results on short satirical texts across multiple datasets.

While these studies provide a robust foundation, several limitations remain. Most notably, research tends to treat sarcasm, irony, satire, and related styles as isolated tasks, overlooking the fact that they frequently co-occur or interact within a single instance of humor, particularly in dark humor. Though there are a few works [20], [21], cynicism remains virtually unexamined as a computational task. Furthermore, many models are tailored to narrow domains or specific modalities, limiting their generalizability across contexts, cultures, and moral boundaries. These gaps highlight the necessity of framing sarcasm, irony, satire, and cynicism not as independent phenomena but as interrelated components of a broader category, dark humor. A unified modeling approach is essential to capture the layered, morally provocative, and affectively ambiguous nature of dark humor in real-world discourse.

## III. Dataset Description and Annotation Process

In this section, we describe the process of dataset collection and the annotation methodology employed. We detail the sources from which the data is gathered, the criteria used for selecting samples, and the steps taken to ensure annotation quality and consistency. This comprehensive overview provides the foundation for understanding the dataset’s structure and reliability for subsequent analysis.

### A. *Dataset Collection*

All memes in our dataset were sourced from Reddit. We used the Reddit API to retrieve posts containing both an image and accompanying text, and applied OCR to extract embedded text. A subsequent manual screening eliminated the duplicates, resulting in a high-quality corpus of 4,379 multimodal memes for annotation and analysis.

### B. *Annotator Training*

The annotation process was overseen by a faculty member and a PhD researcher with expertise in computational humor and harmful content analysis. The actual annotations were carried out by three undergraduate computer science students who voluntarily participated with informed consent. As a token of appreciation, they were granted access to A100 GPU resources for their own research.

A gold-standard seed set of 100 memes, balanced across dark and non-dark humor, was first annotated by the expert team. This dataset, along with a detailed codebook, was used to train the student annotators. The codebook defined annotation criteria with examples for three subtasks: (i) dark humor identification, (ii) target of the humor, and (iii) intensity level. After the initial labeling round, annotation discrepancies were discussed collectively to refine interpretation and improve consistency.

1) *Annotation Dimensions:* Each meme was annotated across three distinct dimensions:

- **Dark Humor (DH):** Binary label indicating whether the meme contains dark humor.
- **Target:** The specific group, topic, or subject that is the focus of the meme’s humor (e.g., gender, mental health, disability).
- **Intensity:** The perceived intensity of the dark humor, annotated on a three-level ordinal scale:
  - *Mild (1):* Humor that is subtly dark or lightly suggestive.
  - *Moderate (2):* Humor that is more direct and clearly involves a sensitive theme.
  - *Severe (3):* Highly explicit or extreme dark humor involving graphic or taboo content.

### C. *Annotation in Batch Mode*

Following the training phase, the remaining memes were annotated in weekly batches of 200 memes. To mitigate potential cognitive fatigue from exposure to sensitive content, annotators were encouraged to take breaks of 10–15 minutes after each set of 10 memes, aligning with recommendations in prior work on annotator well-being [22]. We also enforced a soft cap of 50 memes per day to prevent overload. Regular check-in meetings were held to discuss any difficult cases, resolve annotation conflicts, and monitor the psychological impact of labeling dark content [23]. All annotations were finally reviewed by the supervising researchers to create a high-quality, adjudicated gold-standard dataset.

### D. *Inter-Annotator Agreement*

To assess the consistency of annotations across annotators, we computed inter-annotator agreement scores using both pairwise Cohen’s Kappa and Fleiss’ Kappa. Table I summarizes the results for the three annotation tasks: *Dark Humor* (DH), *Target*, and *Intensity*.

For the dark humor task, unweighted Cohen’s Kappa scores ranged from 58.92 to 85.88 across annotator pairs, with a Fleiss’ Kappa of 70.29, indicating substantial agreement. The target task yielded similarly strong results, with pairwise Cohen’s Kappa scores as high as 83.55 and a Fleiss’ Kappa



<!-- page 0005 -->

[Figure: A subset of memes in a 2×4 grid. Readable meme text includes: “Me after completing 1 of the 20 things I’m supposed to do”; “MINIBAR”; “9 hours into NoNutNovember and you bump shoulders with a female in the hallway”; “HOW DARK IS YOUR HUMOR? ME:”; “Every sister has 2 moods”; “Step sisters:”; “There’s three, actually”; “READING THE NEWS REMINDS ME OF MY ABUSIVE CHILDHOOD WITH WORST CASE SCENARIOS”; “NOT SAYING A WORD BECAUSE PEOPLE WOULD GET TRIGGERED AND HATE ME”; “WIRELESS TECHNOLOGIES”.]

(a) Dark Humor: No  
Target: N/A  
Intensity: N/A

(b) Dark Humor: Yes  
Target: Disability  
Intensity: 2

(c) Dark Humor: Yes  
Target: Gender/Sex  
Intensity: 3

(d) Dark Humor: Yes  
Target: Race/Ethnicity  
Intensity: 3

(e) Dark Humor: Yes  
Target: Gender/Sex  
Intensity: 2

(f) Dark Humor: Yes  
Target: Mental Health  
Intensity: 2

(g) Dark Humor: Yes  
Target: Disability  
Intensity: 2

(h) Dark Humor: Yes  
Target: Violence/Death  
Intensity: 3

Fig. 2: A subset of memes from D-Humor dataset, classified by their dark humor presence, target, and intensity. (Source: Reddit)

of 72.13, reflecting high agreement on identifying the meme’s intended subject.

TABLE I: Inter-annotator agreement scores. **A:** Annotator; **DH:** Dark Humor; **Unwt:** Unweighted; **Wt:** Weighted; **C Kappa:** Cohen’s Kappa; **Wt C Kappa:** Weighted Cohen’s Kappa; **F Kappa:** Fleiss’ Kappa.

| Task | Ann Pair | UnWt C Kappa | Wt C Kappa | F Kappa |
|---|---|---:|---:|---:|
| DH | A1&A2 | 66.05 | - | 70.29 |
| DH | A2&A3 | 85.88 | - |  |
| DH | A3&A1 | 58.92 | - |  |
| Target | A1&A2 | 70.31 | - | 72.13 |
| Target | A2&A3 | 83.55 | - |  |
| Target | A3&A1 | 62.47 | - |  |
| Intensity | A1&A2 | 53.24 | 74.39 | 58.57 |
| Intensity | A2&A3 | 76.59 | 87.26 |  |
| Intensity | A3&A1 | 45.89 | 69.45 |  |

The intensity task, which involves ordinal labels (mild, moderate, severe), naturally presents more subjectivity. We computed both unweighted and **weighted** Cohen’s Kappa for this task only, since weighted Kappa accounts for the degree of disagreement in ordinal annotations. While unweighted scores ranged from 45.89 to 76.59, the weighted Kappa values were significantly higher, reaching up to 87.26. The Fleiss’ Kappa for intensity was 58.57, suggesting moderate agreement overall.

The use of annotator training, expert supervision, and structured annotation guidelines helped ensure consistent and replicable labeling across complex and sensitive humor categories.

*E. Dataset Statistics*

Table II presents a detailed breakdown of our dataset across both training and test splits. The dataset consists of meme samples labeled for the presence or absence of dark humor, along with fine-grained annotations on their target category and humor intensity. A sample of memes from the D-HUMOR dataset is shown in Figure 2.

*1) Dark Humor Distribution:* The training set contains a total of 3,503 memes, with 1,577 labeled as containing dark humor and 1,926 as non-dark humor. The test set comprises 876 memes, including 397 positive and 479 negative samples. This relatively balanced distribution supports effective supervised training and facilitates fair evaluation.

*2) Target Categories:* Each meme labeled as dark humor was further annotated with the specific target of its humor. In the training set, the most frequently targeted categories are *Gender/Sex-Related Topics* (683 instances), followed by *Other* (351), and *Mental Health* (222). These three categories also dominate the test set distribution, indicating consistent prevalence across both data splits.

*3) Intensity Levels:* In the training data, the distribution is skewed toward lower intensity: 903 memes are rated as *Mild*, 466 as *Moderate*, and only 208 as *Severe*. A similar trend appears in the test set, with 229, 132, and 46 memes across the three levels, respectively. This distribution reflects the real-world observation that while most dark humor is implicit or moderately suggestive, highly explicit content is comparatively rare.



<!-- page 0006 -->

TABLE II: Summary of dataset

<table>
<thead>
<tr>
<th colspan="2">Train Data</th>
<th colspan="2">Test Data</th>
</tr>
<tr>
<th>Dark Humor</th>
<th>Count</th>
<th>Dark Humor</th>
<th>Count</th>
</tr>
</thead>
<tbody>
<tr>
<td>No</td>
<td>1,926</td>
<td>No</td>
<td>479</td>
</tr>
<tr>
<td>Yes</td>
<td>1,577</td>
<td>Yes</td>
<td>397</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="5">Train Data: Target vs Intensity</th>
<th colspan="5">Test Data: Target vs Intensity</th>
</tr>
<tr>
<th>Target</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>Total</th>
<th>Target</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>Total</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gender/Sex-Related Topics</td>
<td>303</td>
<td>248</td>
<td>132</td>
<td>683</td>
<td>Gender/Sex-Related Topics</td>
<td>59</td>
<td>74</td>
<td>28</td>
<td>161</td>
</tr>
<tr>
<td>Mental Health</td>
<td>169</td>
<td>49</td>
<td>4</td>
<td>222</td>
<td>Mental Health</td>
<td>46</td>
<td>9</td>
<td>3</td>
<td>58</td>
</tr>
<tr>
<td>Disability</td>
<td>30</td>
<td>26</td>
<td>19</td>
<td>75</td>
<td>Disability</td>
<td>9</td>
<td>7</td>
<td>3</td>
<td>19</td>
</tr>
<tr>
<td>Race/Ethnicity</td>
<td>32</td>
<td>35</td>
<td>19</td>
<td>86</td>
<td>Race/Ethnicity</td>
<td>5</td>
<td>7</td>
<td>6</td>
<td>18</td>
</tr>
<tr>
<td>Violence/Death</td>
<td>94</td>
<td>48</td>
<td>18</td>
<td>160</td>
<td>Violence/Death</td>
<td>31</td>
<td>13</td>
<td>3</td>
<td>47</td>
</tr>
<tr>
<td>Other</td>
<td>275</td>
<td>60</td>
<td>16</td>
<td>351</td>
<td>Other</td>
<td>79</td>
<td>12</td>
<td>3</td>
<td>94</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td><strong>903</strong></td>
<td><strong>466</strong></td>
<td><strong>208</strong></td>
<td><strong>1,577</strong></td>
<td><strong>Total</strong></td>
<td><strong>229</strong></td>
<td><strong>132</strong></td>
<td><strong>46</strong></td>
<td><strong>397</strong></td>
</tr>
</tbody>
</table>

Overall, this rich annotation framework provides valuable granularity for developing and benchmarking models that aim to understand not only the presence of dark humor but also its target and intensity.

## IV. METHODOLOGY

Understanding dark humor in memes requires reasoning beyond literal content, as it often relies on abstract incongruity between text and visuals. To address this, we propose a reasoning-augmented multimodal framework that leverages linguistic cues, image semantics, and inferred commonsense reasoning. The architecture, as shown in Figure 3, comprises five components: reasoning refinement, feature extraction, cross-attention fusion, feature aggregation, and final classification.

### A. *Structured Reasoning Generation*

Understanding dark humor memes requires more than just identifying surface-level content. The humor often hinges on subtle context, cultural subtext, visual incongruities, and emotionally conflicting cues, many of which may be implicit, taboo, or deliberately ambiguous. These characteristics make dark humor memes uniquely challenging to interpret, both for humans and machines.

To address this, we enrich the meme classification process with structured explanatory signals. By explicitly breaking down the reasoning behind a meme’s humor, emotional tone, and target, we provide the model with additional context that aids in disambiguation. This additional supervision helps the model move beyond superficial patterns and capture the deeper intent and affective contrast that are typical in dark humor. Moreover, structured reasoning allows for improved transparency and interpretability, supporting downstream applications like content moderation, harm detection, and bias analysis.

***1) Structured Explanation Schema:*** We design each explanation using a six-part schema that captures distinct dimensions of the meme’s communicative intent and stylistic choices:

1) **Meme Summary:** A concise description of the meme’s image and text.  
2) **Implied Joke:** The core humorous element inferred from the meme.  
3) **Narrative Structure:** The rhetorical style (e.g., sarcasm, irony, absurdism).  
4) **Emotional Effect:** The emotional response the meme is designed to elicit.  
5) **Dark Attributes:** Any presence of taboo, offensive, or socially sensitive themes.  
6) **Target:** The entity, group, or concept being referenced or mocked.

This decomposition facilitates fine-grained understanding, and the modular format can be encoded and fused with vision-language features during classification.

***2) Iterative Reasoning Refinement via Role-Reversal Self-Loop:*** Interpreting dark humor requires not only visual-textual understanding but also alignment with nuanced social, cultural, and emotional cues, an area where even large models often fail. To bridge this gap, we propose a novel technique called **Role-Reversal Self-Loop**, a simple yet powerful mechanism for enhancing *AI alignment* in tasks involving implicit reasoning and culturally sensitive content.

After generating an initial structured reasoning using the Qwen-2.5-7B Vision-Language Model (VLM), we prompt the model to assume a reversed role: *it becomes the original author of the meme.* Under this setup, the model is asked to review the reasoning it “received” for its own meme and critically assess whether the fields are faithful and complete as shown in Figure 4. This role-flip is psychologically aligned with reflective human behavior, encouraging the model to evaluate explanations with a self-interested perspective, thereby improving alignment.

This approach has two key benefits:

• It ensures that each explanation component is reviewed in context, preventing the model from over-focusing on only one field (e.g., the joke or the target).



<!-- page 0007 -->

[Figure: Overview diagram of the proposed architecture. Readable labels include “Reasoning Refinement via Role-Reversal Self-Loop,” “Multimodal Dataset,” “VLM,” “Reasoning Features,” “Preprocessing,” “Image,” “Transcript,” “Feature Extraction,” “Image Encoder,” “Text Encoder,” “Embeddings,” “Image Features,” “Text Features,” “TCRNet,” “Image-Reason,” “Text-Reason,” “Image-Text,” “Classsfication,” and “Label y1 y2 ... yn.”]

Fig. 3: Overview of the proposed reasoning-augmented multimodal architecture. Each meme (image + OCR text) is first processed by VLM to generate and refine a structured explanation via the Role-Reversal Self-Loop mechanism. Text encoders encode the OCR transcript and the self-refined explanation into textual embeddings, while the image encoder extracts visual embeddings from the meme image. A Tri-stream Cross-Reasoning Network (TCRNet) then applies pairwise scaled dot-product attention across the three modalities, text, image, and reasoning, to produce attended representations. These representations are concatenated into a unified feature vector, which is passed through a classification head to predict dark humor presence, target category, and intensity.

[Figure: Self-loop diagram for Role Reversal prompting. Readable labels include “Input,” “Model,” “Initial Explanation,” “Role Reversal (RR) Prompting,” “Iterative refinement using RR Prompt,” “After N RR Iterations,” and “Final Exp.”]

Fig. 4: **Self-loop mechanism using Role Reversal (RR) Prompting.** The input meme is passed to a language model which generates an initial explanation. This explanation is then refined iteratively through Role Reversal prompting, where the model assumes the role of a reviewer to critique and improve its own output. After $N$ such refinement cycles, a final explanation is obtained. This mechanism enables the model to simulate self-awareness and improve explanatory coherence without external supervision.

- It encourages introspective correction without requiring external feedback or manual interventions, thereby improving scalability and automation.

We apply this refinement loop iteratively for a maximum of 5 epochs. On average, explanations converge and stabilize by approximately 3 epochs, indicating that the model typically needs only a few rounds to self-correct and align its output.

Importantly, our manual review of a subset of explanations revealed that most improvements were concentrated in the fields of Narrative Structure, Dark Attributes, and Implied Joke, components that demand deeper contextual reasoning. Fields like Meme Summary, Target, and Emotional Effect were more stable across iterations, suggesting they are more straightforward to interpret initially.

**Role-Reversal Self-Loop Prompt Template**

You are the author and creator of the given dark humor meme. Someone else has provided a detailed explanation of your meme’s meaning, humor, and components, including the Meme Summary, Implied Joke, Narrative Structure, Emotional Effect, Dark Attributes, and Target.

Your task is to review their explanation from your perspective as the original author. Analyze how well their reasoning aligns with your intended humor, message, tone, and overall context. For each component, identify any inaccuracies, missing details, or misunderstandings. Then, provide a thorough, corrected explanation that fully reflects your original intent, ensuring clarity, accuracy, and completeness.  
Please present your revised explanation below.

`[Explanation Components Inserted Here]`



<!-- page 0008 -->

*B. Feature Extraction*

We extract embeddings from three modalities: the meme’s original transcript $T$, the generated reasoning $R$, and the image $I$.

**Textual Features:** We use the BERT model to encode both $T$ and $R$ into contextual token embeddings:

$$
\mathbf{F}_T = \mathrm{BERT}(T) \in \mathbb{R}^{197 \times 768}
\tag{1}
$$

$$
\mathbf{F}_R = \mathrm{S\text{-}BERT}(R) \in \mathbb{R}^{197 \times 768}
\tag{2}
$$

Each row corresponds to a subword token in a 768-dimensional embedding space.

**Visual Features:** We use the ViT model, which combines vision and language pretraining objectives, to extract features from the meme image:

$$
\mathbf{F}_I = \mathrm{ViT}(I) \in \mathbb{R}^{197 \times 768}
\tag{3}
$$

This representation captures visual cues such as objects, expressions, and contextual artifacts relevant to the meme.

*C. Tri-stream Cross-Reasoning Network (TCRNet)*

To effectively model inter-modal interactions and capture reasoning-driven dependencies, we introduce a *Tri-stream Cross-Reasoning Network* [24], [25]. This module enables each modality, text ($T$), image ($I$), and LLM-generated reasoning ($R$), to mutually inform and align with one another by attending across pairs.

Specifically, we use scaled dot-product attention to implement pairwise reasoning flows. Let $\mathbf{Q}_X = \mathbf{F}_X \mathbf{W}_Q$, $\mathbf{K}_Y = \mathbf{F}_Y \mathbf{W}_K$, and $\mathbf{V}_Y = \mathbf{F}_Y \mathbf{W}_V$ be the linear projections of modalities $X$ and $Y$, where $X, Y \in \{T, I, R\}$. The attention from $X$ to $Y$ is computed as:

$$
\operatorname{Attn}(X \to Y) = \operatorname{softmax}\left(\frac{\mathbf{Q}_X \mathbf{K}_Y^\top}{\sqrt{d_k}}\right)\mathbf{V}_Y
\tag{4}
$$

This formulation allows modality $X$ to selectively extract context-aware signals from modality $Y$, thereby modeling semantic incongruity, visual-verbal contradictions, and inferential alignment, all of which are critical in dark humor.

We compute such cross-reasoning across all three modality pairs:

$$
\tilde{\mathbf{F}}_{T \leftrightarrow I} = \operatorname{Attn}(T \to I)
\tag{5}
$$

$$
\tilde{\mathbf{F}}_{T \leftrightarrow R} = \operatorname{Attn}(T \to R)
\tag{6}
$$

$$
\tilde{\mathbf{F}}_{I \leftrightarrow R} = \operatorname{Attn}(I \to R)
\tag{7}
$$

*D. Feature Aggregation*

Each cross-reasoned output is aggregated using average pooling to yield fixed-length vectors:

$$
\mathbf{v}_{T \leftrightarrow I} = \operatorname{AvgPool}(\tilde{\mathbf{F}}_{T \leftrightarrow I})
\tag{8}
$$

$$
\mathbf{v}_{T \leftrightarrow R} = \operatorname{AvgPool}(\tilde{\mathbf{F}}_{T \leftrightarrow R})
\tag{9}
$$

$$
\mathbf{v}_{I \leftrightarrow R} = \operatorname{AvgPool}(\tilde{\mathbf{F}}_{I \leftrightarrow R})
\tag{10}
$$

We concatenate the resulting vectors to obtain a unified representation:

$$
\mathbf{v} = [\mathbf{v}_{T \leftrightarrow I}; \mathbf{v}_{T \leftrightarrow R}; \mathbf{v}_{I \leftrightarrow R}] \in \mathbb{R}^{2,304}
\tag{11}
$$

This vector serves as the multimodal reasoning-aware representation fed into the final classification layer.

*E. Hyperparameters and System Description*

Table III lists the primary hyperparameters used for the proposed framework. Encoder-only text and image models share identical training configurations, while LLMs fine-tuned with QLoRA use 3 epochs and low-rank adaptation settings ($r = 8$, $\alpha = 32$, dropout 0.1). The TCRNet additionally employs dropout (0.3) and eight attention heads in its training setup.

TABLE III: Key hyperparameter configurations used across different model types.

| Model Type | Hyperparameter | Value |
|---|---|---|
| Encoder-Only Text Models | Epochs | 5 |
|  | Batch Size | 16 |
|  | Learning Rate | 0.00002 |
| LLMs with QLoRA | Epoch | 3 |
|  | LoRA Rank ($r$) | 8 |
|  | LoRA Alpha | 32 |
|  | LoRA Dropout | 0.1 |
|  | Target Modules | q_proj, v_proj |
| Image Models | Epochs | 5 |
|  | Batch Size | 16 |
|  | Learning Rate | 0.00002 |
| TCRNet | Epochs | 5 |
|  | Batch Size | 16 |
|  | Learning Rate | 0.00002 |
|  | Dropout | 0.3 |
|  | Attention Heads | 8 |

All experiments were conducted on a server equipped with Intel(R) Xeon(R) Silver 4316 CPU @ 2.30GHz, 4× NVIDIA A16 GPUs (each with 16 GB VRAM), running CUDA 12.8 and driver version 570.133.07. The training utilized PyTorch with GPU acceleration, and computations were distributed using a single GPU unless specified otherwise.

V. RESULTS AND DISCUSSION

*A. Experimental Findings*

Table IV presents a comprehensive evaluation of various models on three tasks: dark humor detection (binary classification), target identification (multi-class classification), and intensity prediction. We report Accuracy, Macro-F1, and Weighted-F1 for all tasks, and additionally include Pearson correlation for intensity prediction, as it is ordinal. When relying solely on OCR-extracted text, pretrained models like BERT, DistilBERT, and LLaMA achieve reasonable performance for dark humor detection. LLaMA leads with 71.72% accuracy and a Macro-F1 of 71.14%. However, these text-only systems struggle to identify the specific target of the humor and to gauge its intensity. For instance, DistilBERT’s target identification Macro-F1 is only 55.98%, and BERT’s intensity Pearson correlation is a modest 27.18%. These results indicate that while textual cues carry considerable information



<!-- page 0009 -->

TABLE IV: Evaluation of various models across different input modalities for dark humor meme analysis. The highest performance in each metric is highlighted in **bold**, while the second-best performance is marked with a <sup>†</sup> symbol. **P-corr** denotes the Pearson correlation coefficient used to evaluate the ordinal classification task for Intensity.

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="3">Dark Humor (Yes/No)</th>
<th colspan="3">Target</th>
<th colspan="4">Intensity</th>
</tr>
<tr>
<th>Accuracy</th>
<th>Macro-F1</th>
<th>Wt-F1</th>
<th>Accuracy</th>
<th>Macro-F1</th>
<th>Wt-F1</th>
<th>Accuracy</th>
<th>Macro-F1</th>
<th>Wt-F1</th>
<th>P-Corr.</th>
</tr>
</thead>
<tbody>
<tr><td colspan="11"><strong>OCR Text Only</strong></td></tr>
<tr>
<td>BERT [26]</td><td>70.05</td><td>69.41</td><td>69.75</td><td>59.69</td><td>53.27</td><td>59.53</td><td>58.91<sup>†</sup></td><td>46.59<sup>†</sup></td><td>57.63<sup>†</sup></td><td>27.18</td>
</tr>
<tr>
<td>Distil-BERT [27]</td><td>69.81</td><td>69.23</td><td>69.55</td><td>61.50</td><td>55.98</td><td>60.91</td><td>55.81</td><td>45.75</td><td>55.22</td><td>26.25</td>
</tr>
<tr>
<td>Llama-3.2-3b-it [28]</td><td>71.72</td><td>71.14</td><td>71.45</td><td>54.52</td><td>38.20</td><td>51.96</td><td>57.62</td><td>37.41</td><td>52.58</td><td>17.05</td>
</tr>
<tr><td colspan="11"><strong>Image Only</strong></td></tr>
<tr>
<td>CLIP [29]</td><td>57.76</td><td>57.69</td><td>57.85</td><td>37.53</td><td>35.43</td><td>38.47</td><td>40.30</td><td>31.18</td><td>40.72</td><td>2.40</td>
</tr>
<tr>
<td>ViT [30]</td><td>64.04</td><td>62.82</td><td>63.45</td><td>45.59</td><td>32.76</td><td>39.86</td><td>54.66</td><td>36.22</td><td>51.14</td><td>7.14</td>
</tr>
<tr>
<td>BLIP [31]</td><td>64.95</td><td>64.25</td><td>64.72</td><td>44.84</td><td>40.53</td><td>43.79</td><td>58.19</td><td>41.69</td><td>54.40</td><td>19.96</td>
</tr>
<tr><td colspan="11"><strong>VLMs (Prompt based Zero-Shot)</strong></td></tr>
<tr>
<td>Qwen-2.5-7b-it [32]</td><td>64.27</td><td>63.26</td><td>63.83</td><td>57.68</td><td>53.70</td><td>56.28</td><td>17.63</td><td>15.27</td><td>14.14</td><td>17.50</td>
</tr>
<tr>
<td>LLaVA-1.6-mistral-7b [33]</td><td>45.32</td><td>31.19</td><td>28.27</td><td>48.87</td><td>48.30</td><td>49.14</td><td>30.23</td><td>24.22</td><td>29.92</td><td>11.48</td>
</tr>
<tr><td colspan="11"><strong>OCR Text + Structured Explanation (with Role-Reversal Prompting)</strong></td></tr>
<tr>
<td>BERT</td><td>71.24</td><td>70.88</td><td>71.13</td><td>65.37<sup>†</sup></td><td>61.67<sup>†</sup></td><td>65.42<sup>†</sup></td><td>56.33</td><td>43.16</td><td>55.10</td><td>32.12</td>
</tr>
<tr>
<td>Distil-BERT</td><td>70.53</td><td>70.02</td><td>70.32</td><td><strong>66.41</strong></td><td><strong>62.53</strong></td><td><strong>66.07</strong></td><td>55.56</td><td>43.98</td><td>54.95</td><td>32.56<sup>†</sup></td>
</tr>
<tr>
<td>Llama-3.2-3b-it</td><td>73.39<sup>†</sup></td><td>72.91<sup>†</sup></td><td>73.19<sup>†</sup></td><td>59.17</td><td>50.37</td><td>57.62</td><td>58.14</td><td>37.94</td><td>53.76</td><td>24.4</td>
</tr>
<tr><td colspan="11"><strong>VLMs (Prompt based Zero-Shot with Role-Reversal Prompting)</strong></td></tr>
<tr>
<td>Qwen-2.5-7b-it</td><td>64.04</td><td>64.02</td><td>63.95</td><td>55.67</td><td>50.97</td><td>55.01</td><td>29.22</td><td>28.97</td><td>29.33</td><td>11.84</td>
</tr>
<tr>
<td>LLaVA-1.6-mistral-7b</td><td>46.80</td><td>35.40</td><td>32.86</td><td>49.62</td><td>51.44</td><td>50.03</td><td>37.03</td><td>34.41</td><td>39.35</td><td>15.22</td>
</tr>
<tr>
<td><strong>TCRNet (ours)</strong></td><td><strong>75.00</strong></td><td><strong>73.55</strong></td><td><strong>74.13</strong></td><td>64.48</td><td>60.54</td><td>64.17</td><td><strong>62.72</strong></td><td><strong>49.71</strong></td><td><strong>60.74</strong></td><td><strong>38.63</strong></td>
</tr>
</tbody>
</table>

for detecting the presence of dark humor, they lack the broader context and implicit signals needed to pinpoint whom or what the joke is aimed at, and how severe it is.

Purely image-based models, such as CLIP, ViT, and BLIP, underperform compared to text-only baselines. BLIP achieves the highest image-only dark humor accuracy at 64.95%, but target identification accuracy remains below 45% and intensity accuracy under 60%. The Pearson correlation for intensity is especially low, for instance, 19.96% for BLIP. This suggests that, although visual features capture facial expressions, color palettes, and scene context, they fail to convey the nuanced semantics that define dark humor. In other words, imagery alone lacks the explicit linguistic content that often carries the punchline or the taboo reference.

Zero-shot vision-language models, such as Qwen-VL and Next-LLaVA-VL, demonstrate limited effectiveness without task-specific fine-tuning. Qwen-VL achieves 64.27% dark humor accuracy and a 17.50% intensity correlation, while Next-LLaVA-VL lags further behind (45.32% accuracy for humor detection, 11.48% intensity correlation). Even when provided with structured explanations as prompts, these VLMs show only marginal improvements. For example, Next-LLaVA-VL’s intensity correlation rises from 11.48% to 15.22% with explanations, but remains far below the performance of models trained on text-plus-explanation inputs. These observations highlight that, although large VLMs contain rich pretraining knowledge, they still require supervised adaptation to handle the implicit, sensitive nature of dark humor.

Augmenting OCR text with structured explanations yields consistent and substantive gains across all tasks. Under the “OCR Text + Structured Explanation” setting, BERT’s dark humor accuracy increases from 70.05% to 71.24%, and DistilBERT’s target Macro-F1 jumps from 55.98% to 62.53%. Most notably, intensity Pearson correlation for DistilBERT improves from 26.25% to 32.56%. These results underline that structured explanations, capturing implied jokes, narrative structure, and emotional effect, supplement raw text with crucial contextual cues. Even LLaMA, which already performs well with text alone, sees its dark humor accuracy rise to 73.39% when explanations are included, confirming that reasoning signals complement large language model outputs.

Our proposed **TCRNet** model, which implements a Tri-stream Cross-Reasoning Network to fuse OCR text, image features, and structured explanations, achieves the best overall results. TCRNet attains 75.00% accuracy on dark humor detection and 62.72% accuracy on intensity prediction, both the highest scores among all evaluated methods. By explicitly aligning visual and textual streams with reasoning-derived explanations, TCRNet captures implicit associations and semantic incongruities that single-modality or non-reasoning models miss. These improvements demonstrate that reasoning-aware, multimodal fusion is essential for accurately understanding and categorizing dark humor memes.

## VI. ABLATION STUDY

From the ablation study presented in Figure 5, it is evident that the reasoning component based on structured explanations plays a critical role in enhancing the performance of TCRNet across all three tasks. When the explanation modality is removed, there is a substantial drop in performance, particularly in Target Identification (Macro-F1 drops from 60.54 to 35.11) and Dark Humor Classification (Weighted-F1 drops from 74.13 to 67.31). This clearly indicates that dark humor memes often rely on implicit, nuanced reasoning that goes beyond surface-level textual or visual cues.

Unlike typical classification problems, where raw OCR text or image features might suffice, dark humor detection



<!-- page 0010 -->

[Figure: Three bar charts showing an ablation study. (a) “Dark Humor (yes/no)” with groups “w/o OCR Text,” “w/o Image,” and “w/o Reasoning,” and legend “Accuracy,” “Macro-F1,” “Weighted-F1.” (b) “Target Identification” with the same groups and legend. (c) “Intensity Prediction” with the same groups and legend “Accuracy,” “Macro-F1,” “Weighted-F1,” “Pearson Corr.”]

(a) Dark humor  (b) Target identification  (c) Intensity prediction

Fig. 5: The charts represent an ablation study of TCRNet on Dark Humor Meme Analysis. Each ablation removes one component (OCR Text, Image, or Explanation) to study its impact. The full TCRNet results are included in Table IV.

demands an externalized and structured interpretive view. The explanation-based features help the model contextualize morally ambiguous content, sarcasm, or deception, which are often difficult to infer directly from the raw input. These findings emphasize the importance of integrating explicit reasoning mechanisms into multimodal understanding systems, especially for complex, subjective tasks like dark humor analysis.

## VII. CONCLUSION

In this work, we introduced the D-Humor dataset, a multimodal collection of 4,397 Reddit memes annotated for dark humor (yes/no), target category (gender, mental health, violence, race, disability, other), and a three-level intensity rating (mild, moderate, severe). We further proposed a reasoning-augmented framework that first generates and self-refines structured explanations using Qwen-2.5-7B VLM, then fuses OCR text, ViT-based image features, and refined reasoning via a Tri-stream Cross-Reasoning Network (TCRNet). Experimental results across three tasks, dark humor detection, target identification, and intensity prediction, demonstrate that (1) text-only or image-only models are insufficient for capturing the nuances of dark humor, (2) zero-shot vision-language models underperform without fine-tuning, and (3) augmenting OCR text with structured explanations yields consistent gains.

Our proposed TCRNet achieves state-of-the-art performance, attaining 75.00% accuracy on dark humor detection and 62.72% accuracy on intensity prediction, outperforming all baselines by a significant margin. An ablation study confirms that the structured explanation component is critical: removing explanations leads to a dramatic drop in Target Identification Macro-F1 (from 60.54% to 35.11%) and Dark Humor Weighted-F1 (from 74.13% to 67.31%). These findings highlight that dark humor in memes relies on implicit, context-dependent cues, such as implied jokes and emotional effect, that cannot be inferred from raw text or images alone, necessitating explicit reasoning signals.

While we acknowledge that D-Humor is skewed toward the *Gender/Sex-Related Topics* label, likely reflecting the greater availability of such content online, models trained on this data generalize well across all categories and do not exhibit overfitting. For future work, we plan to expand the dataset with additional target classes to enable finer-grained analyses, as well as investigate semi-supervised and self-supervised techniques to further improve generalization to emerging dark humor trends. We also aim to explore more advanced alignment mechanisms within the Tri-stream Cross-Reasoning framework to better capture evolving cultural and social nuances in online humor.

## ETHICAL CONSIDERATION

We propose the D-Humor Dataset as a novel resource to study dark humor in memes. Due to the sensitive and potentially offensive nature of the content, users should exercise caution and follow ethical guidelines when handling the data. The dataset is intended exclusively for academic and research purposes aimed at advancing understanding in this domain. To protect the privacy of individuals and maintain data integrity, public redistribution, sharing, or any unauthorized dissemination of the dataset is strictly prohibited. Access will be granted only upon signing a data usage agreement.

## REDDIT ETHICAL POLICY FOR SCRAPING THE MEMES

In conducting our D-Humor Project, we collected publicly available memes from Reddit, ensuring strict adherence to Reddit’s Privacy Policy and Public Content Policy.[^1] Reddit emphasizes user anonymity by not requiring real names or photos, stripping metadata from shared media, and prohibiting doxxing. Our data collection excluded any personally identifiable information, such as usernames, email addresses, or IP data, focusing solely on content that users have made publicly accessible. Reddit’s Public Content Policy permits the use of public posts and comments for research, provided that user privacy is respected and content is not used for surveillance or identification.[^2] We also ensured that no deleted or private content was included, aligning with Reddit’s guidelines that prohibit unauthorized scraping and highlight the importance of user consent and data protection. We took care to follow the platform’s stated policies and norms regarding data usage.[^3]

[^1]: https://www.redditinc.com/policies/privacy-policy  
[^2]: https://support.reddithelp.com/hc/en-us/articles/26410290525844  
[^3]: https://www.redditinc.com/policies/user-agreement-april-18-2023



<!-- page 0011 -->

## ACKNOWLEDGMENT

The authors thank IIT Indore for providing financial support for the registration of the article. The authors thank the UGC Junior Research Fellowship (UGC-JRF) scheme, an initiative of the Government of India, for providing the Ph.D. fellowship to Mohammad Zia Ur Rehman (NTA Ref. No.: 190510846524). The authors are also thankful for the Young Faculty Research Catalysing Grant (YFRCG) by the Indian Institute of Technology Indore for providing the resources to the project (Project ID: IITI/YFRCG/2023-24/03).

## REFERENCES

[1] W. Ruch, S. Heintz, T. Platt, L. Wagner, and R. T. Proyer, “Broadening humor: Comic styles differentially tap into temperament, character, and ability,” *Frontiers in psychology*, vol. 9, p. 6, 2018.

[2] Y. Li, Y. Li, S. Zhang, G. Liu, Y. Chen, R. Shang, and L. Jiao, “An attention-based, context-aware multimodal fusion method for sarcasm detection using inter-modality inconsistency,” *Knowledge-Based Systems*, vol. 287, p. 111457, 2024.

[3] Z. Xi, B. Yu, and H. Wang, “Multimodal sarcasm detection based on sentiment-clue inconsistency global detection fusion network,” *Expert Systems with Applications*, vol. 275, p. 127020, 2025.

[4] M. Rahman, M. A.-M. Provath, K. Deb, P. K. Dhar, and T. Shimamura, “Camfusion: Context-aware multi-modal fusion framework for detecting sarcasm and humor integrating video and textual cues,” *IEEE Access*, 2025.

[5] A. K. Singh, G. Kim, J. Kim, H.-m. Park, B. J. Choi, and W. De Neve, “Ramm: A residual attention multimodal model for humor detection,” in *International Conference on Intelligent Human Computer Interaction*. Springer, 2025, pp. 229–240.

[6] M. Z. U. Rehman, D. Raghuvanshi, U. Jain, S. Bansal, and N. Kumar, “A multimodal-multitask framework with cross-modal relation and hierarchical interactive attention for semantic comprehension,” *Information Fusion*, p. 103628, 2025.

[7] A. Szabo, “The acute effects of humor and exercise on mood and anxiety,” *Journal of leisure research*, vol. 35, no. 2, pp. 152–162, 2003.

[8] J. Basler, D. Potó, M. Ferincz, S. Kárpáti, and A. N. Zsidó, “Why aren’t you laughing?–the effect of dark and light humor on anxiety and affective state,” *Personality and Individual Differences*, vol. 240, p. 113133, 2025.

[9] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell *et al.*, “Language models are few-shot learners,” *Advances in neural information processing systems*, vol. 33, pp. 1877–1901, 2020.

[10] Y. Bao, X. Zhao, P. Zhang, Y. Qi, and H. Li, “Hian: A hybrid interactive attention network for multimodal sarcasm detection,” *Pattern Recognition*, vol. 164, p. 111535, 2025.

[11] A. Gupta, A. Mittal, and R. Jain, “A novel sarcasm detection approach for text-image data: Leveraging multimodal fusion and weighted latent factors,” *Information Fusion*, p. 103266, 2025.

[12] M. Jia, C. Xie, and L. Jing, “Debiasing multimodal sarcasm detection with contrastive learning,” in *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 38, no. 16, 2024, pp. 18 354–18 362.

[13] B. Liang, L. Gui, Y. He, E. Cambria, and R. Xu, “Fusion and discrimination: A multimodal graph contrastive learning framework for multimodal sarcasm detection,” *IEEE Transactions on Affective Computing*, 2024.

[14] A. Saroj and S. Pal, “Ensemble-based domain adaptation on social media posts for irony detection,” *Multimedia Tools and Applications*, vol. 83, no. 8, pp. 23 249–23 268, 2024.

[15] A. Maladry, E. Lefever, C. Van Hee, and V. Hoste, “The limitations of irony detection in dutch social media,” *Language Resources and Evaluation*, vol. 58, no. 4, pp. 1355–1386, 2024.

[16] N. Bölücü and B. Can, “Semantically-informed graph neural networks for irony detection in turkish,” *ACM Transactions on Asian and Low-Resource Language Information Processing*, vol. 24, no. 1, pp. 1–20, 2025.

[17] D. Goyal, S. K. Mishra, and V. K. Rai, “A multimodal framework for satire vs. sarcasm detection,” in *2024 15th International Conference on Computing Communication and Networking Technologies (ICCCNT)*. IEEE, 2024, pp. 1–7.

[18] R. Ortega-Bueno, P. Rosso, and L. E. M. Pagola, “Multi-view informed attention-based model for irony and satire detection in spanish variants,” *Knowledge-Based Systems*, vol. 235, p. 107597, 2022.

[19] A. Kamal, M. Abulaish *et al.*, “Contextualized satire detection in short texts using deep learning techniques,” *Journal of Web Engineering*, vol. 23, no. 1, pp. 27–52, 2024.

[20] O. Ogbanufe, M. C. Jones, and J. I. Hancock, “Job demands, identity, and outcomes: The mediating role of cynicism among cybersecurity-focused employees,” *Computers & Security*, vol. 150, p. 104277, 2025.

[21] Q. Liu, L. Wang, and M. Luo, “When seeing is not believing: self-efficacy and cynicism in the era of intelligent media,” *Humanities and Social Sciences Communications*, vol. 12, no. 1, pp. 1–13, 2025.

[22] M. L. Ybarra, K. J. Mitchell, J. Wolak, and D. Finkelhor, “Examining characteristics and associated distress related to internet harassment: findings from the second youth internet safety survey,” *Pediatrics*, vol. 118, no. 4, pp. e1169–e1177, 2006.

[23] M. Z. U. Rehman, A. Bhatnagar, O. Kabde, S. Bansal, and N. Kumar, “Implihatevid: A benchmark dataset and two-stage contrastive learning framework for implicit hate speech detection in videos,” in *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 2025, pp. 17 209–17 221.

[24] Y. Zhou, Z. Chen, and H. Yang, “Multimodal learning for hateful memes detection,” in *2021 IEEE International conference on multimedia & expo workshops (ICMEW)*. IEEE, 2021, pp. 1–6.

[25] Y. Tang, L. Zhang, Q. Teng, F. Min, and A. Song, “Triple cross-domain attention on human activity recognition using wearable sensors,” *IEEE Transactions on Emerging Topics in Computational Intelligence*, vol. 6, no. 5, pp. 1167–1176, 2022.

[26] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transformers for language understanding,” in *Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers)*, 2019, pp. 4171–4186.

[27] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter,” *arXiv preprint arXiv:1910.01108*, 2019.

[28] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar *et al.*, “Llama: Open and efficient foundation language models,” *arXiv preprint arXiv:2302.13971*, 2023.

[29] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark *et al.*, “Learning transferable visual models from natural language supervision,” in *International conference on machine learning*. PMLR, 2021, pp. 8748–8763.

[30] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly *et al.*, “An image is worth 16x16 words: Transformers for image recognition at scale,” in *International Conference on Learning Representations*, 2021.

[31] J. Li, D. Li, C. Xiong, and S. Hoi, “Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation,” in *International conference on machine learning*. PMLR, 2022, pp. 12 888–12 900.

[32] Qwen Team, “Qwen2.5-7B-Instruct,” https://huggingface.co/Qwen/Qwen2.5-7B-Instruct, 2025, [Online; accessed 2-June-2025].

[33] H. Liu, C. Li, Q. Wu, and Y. J. Lee, “Visual instruction tuning,” *Advances in neural information processing systems*, vol. 36, pp. 34 892–34 916, 2023.
