<!-- Transcribed from 30-culture-aware-captioning.pdf -->



<!-- page 0001 -->

# Culture-Aware Humorous Captioning: Multimodal Humor Generation across Cultural Contexts

Run Xu$^1$, Lu Li$^2$, Rongzhao Zhang$^{3,\dagger}$, Jie Xu$^{3,\dagger}$  
$^1$Nanyang Technological University, run001@e.ntu.edu.sg  
$^2$Tongji University, author2@yyy.edu  
$^3$Shanghai Artificial Intelligence Laboratory, zhangrongzhao@pjlab.org.cn, xujie@pjlab.org.cn

## Abstract

Recent multimodal large language models have shown promising ability in generating humorous captions for images, yet they still lack stable control over explicit cultural context, making it difficult to jointly maintain image relevance, contextual appropriateness, and humor quality under a specified cultural background. To address this limitation, we introduce a new multimodal generation task, culture-aware humorous captioning, which requires a model to generate a humorous caption conditioned on both an input image and a target cultural context. Captions generated under different cultural contexts are not expected to share the same surface form, but should remain grounded in similar visual situations or humorous rationales.

To support this task, we establish a six-dimensional evaluation framework covering image relevance, contextual fit, semantic richness, reasonableness, humor, and creativity. We further propose a staged alignment framework that first initializes the model with high-resource supervision under the Western cultural context, then performs multi-dimensional preference alignment via judge-based GRPO with a Degradation-aware Prototype Repulsion Constraint to mitigate reward hacking in open-ended generation, and finally adapts the model to the Eastern cultural context with a small amount of supervision.

Experimental results show that our method achieves stronger overall performance under the proposed evaluation framework, with particularly large gains in contextual fit and a better balance between image relevance and humor under cultural constraints.

## 1 Introduction

Multimodal large language models (MLLMs) have recently shown strong progress in visual understanding and open-ended text generation, but they still remain unreliable on generation tasks that require fine-grained visual grounding, explicit controllability, and complex pragmatic objectives [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].This limitation becomes more evident in humorous caption generation, where the model must go beyond literal description and coordinate visual cues, implicit meaning, and expressive novelty [12, 13, 14, 15, 16, 17]. At the same time, recent studies on LLMs and MLLMs have increasingly shown that culture is not a superficial label, but a factor that systematically shapes commonsense activation, expression preferences, and task completion strategies [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. These observations motivate a new question: whether a model can generate humorous captions that remain visually grounded while adapting to an explicitly specified cultural context.

However, existing work has not systematically modeled the intersection of humor and culture in multimodal generation. Prior multimodal humor studies mainly focus on understanding or generating punchlines, sarcasm, and metaphor [12, 13, 14, 15, 16, 17],



<!-- page 0002 -->

[Figure: “Culture-aware Humorous Captioning.” Subtitle: “The same image can evoke different humorous reconstructions under different cultural contexts.” Legend: No context; Western Culture context; Eastern Culture context. Four example panels show the same image with different captions under no context, Eastern context, and Western context. Readable English captions include: “When the dress code says ‘blend in,’ but you’re already the middle manager.” / “When the invite said daycare drop-off, but one penguin heard ‘Met Gala.’”; “That day, the pipe finally remembers that it was born to be a lightsaber.” / “The landlord said the building had central heating; he forgot to mention it was installed by Sauron.”; “He said he was fine with needles right up until the needle became real.” / “That moment the shot is fine, but the doctor says, ‘Good news — it’s covered... just not in-network.’”; “You’re fully dressed for battle, yet people still somehow ask you for directions.” / “Camelot’s idea of business casual.”]

Figure 1: Qualitative examples of culture-aware humorous captioning under different culture contexts. The same image can trigger distinct humorous captions with different framing and cultural references when conditioned on no context, Western context, or Eastern context.

while cultural studies primarily examine cultural commonsense, value alignment, and open-ended cultural evaluation in LLMs and MLLMs [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]. As a result, there is still no clear task formulation, evaluation protocol, or alignment method for generating humorous captions under explicit cultural context. The key difficulty is that the same image may evoke different shared experiences, default assumptions, and associative pathways across cultures, leading to different yet individually reasonable humorous expressions. Therefore, cultural context should be treated not as a surface style tag, but as a condition that directly affects how humor is constructed from the image [12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29].

To address this gap, we propose culture-aware humorous captioning, a task in which the model generates a humorous caption conditioned on both an input image and a target cultural context. Compared with general humorous captioning, this task requires the model to satisfy three objectives simultaneously: preserving stable grounding in the image, making the target cultural context genuinely participate in humor construction, and still producing a caption with a perceptible punchline and expressive novelty. This also makes evaluation more difficult, since a single metric is insufficient once the task becomes open-ended, culturally conditioned, and humor-sensitive [3, 4, 5, 6, 7, 8, 9, 10, 11, 11]. We therefore formulate the task under coarse-grained Eastern and Western cultural context settings and build a six-dimensional evaluation framework covering Image Relevance, Contextual Fit, Semantic Richness, Reasonableness, Humor, and Creativity.

Based on this formulation, we propose a staged alignment framework for culture-aware humorous



<!-- page 0003 -->

captioning. The model is first initialized with high-resource supervision under the Western cultural context, then optimized through multi-dimensional preference alignment via judge-based GRPO, and finally adapted to the Eastern cultural context with a small amount of supervision. To reduce reward hacking in open-ended preference optimization, we further introduce a Degradation-aware Prototype Repulsion Constraint. Experimental results show that this framework more effectively converts explicit cultural conditions into actual generation capability, yielding especially clear gains in Contextual Fit while better balancing image relevance and humor under cultural constraints.

## 2 Related Works

### 2.1 Humorous Image Captioning

Humorous image captioning aims to generate captions that are not only grounded in the visual content of an image but also convey a recognizable humorous effect. Humorous image captioning has progressed from early supervised joke generation to large-scale, reasoning-driven, and preference-aware multi-modal systems. Recent methods can be roughly grouped into two lines: benchmark-building efforts that scale humorous captioning into a systematic research problem [30, 31, 32, 16, 33], and reasoning- or preference-based models that improve specificity, creativity, or alignment with human judgments [34, 12, 35, 36, 37]. Despite significant advancements, most prior work optimizes funniness, content-specificity, or pairwise preference under implicitly shared social assumptions, rather than requiring stable responses aligned with explicit specified cultural context. In response, our work formulates and explores the potential of culture-aware humorous captioning, where humor must remain image-grounded while adapting its rationale and expression to the target culture.

### 2.2 Controllable Image Captioning and Culture-Aware Generation

Recent controllable captioning studies can be summarized into content or structure control [38, 39, 40], context-aware control [41, 42], and style-aware control [43, 44, 45]. In parallel, recent work on cultural alignment in LLMs suggests that explicit cultural conditioning can substantially reshape model behavior and often yield responses that are better aligned with culture-specific values, norms, and situational expectations [20, 21, 46]. However, these two lines of work remain weakly connected: controllable captioning usually emphasizes regions, attributes, or surface style, whereas culture-aware generation is largely text-only and rarely grounded in images or humor. Our task therefore goes beyond style transfer by treating cultural context as a deeper interpretive condition that changes what knowledge is activated, which incongruity is foregrounded, and how humor is verbalized.

### 2.3 Evaluation and Alignment of MLLMs

Current evaluation of MLLMs mainly follows two paradigms: benchmark-based testing for standardized measurement of multimodal perception and reasoning, and judge-based assessment for open-ended generation. On the benchmark side, recent datasets provide broad and systematic evaluation of multimodal capabilities [47, 48, 49]. For open-ended outputs, evaluation has increasingly adopted LLM-as-a-Judge and MLLM-as-a-Judge frameworks as scalable evaluators[50, 51, 52, 53, 54, 55, 56, 57]. In parallel, alignment of MLLMs is typically achieved through supervised fine-tuning, RLHF-style optimization, or preference-based post-training [58, 59, 60, 61, 62, 63, 42, 64, 65]. For creative captioning in particular, large-scale human preference data has proven highly effective for both evaluation and alignment [31]. However, these general paradigms remain insufficient or partly inapplicable for culture-aware humorous captioning, where a valid output should jointly satisfy image grounding, contextual fit, semantic richness, coherence, humor, and creativity. This mismatch



<!-- page 0004 -->

motivates our task-specific six-dimensional evaluation framework and staged alignment strategy tailored to open-ended, culture-conditioned humorous generation.

## 3 Task Definition

Humorous caption generation is not determined solely by the explicit visual content of an image, but is also substantially influenced by external context. For the same visual situation, different cultural backgrounds may activate different shared experiences, default assumptions, and associative pathways, thereby changing how the image is interpreted and how humor is constructed. Therefore, generating humorous captions under a cultural constraint is not a matter of adding superficial stylistic variation to a general humorous caption. Instead, it requires the model to produce different yet reasonable humorous reconstructions of the same visual situation, conditioned on the target cultural context while remaining grounded in the image.

Based on this observation, we define the task of culture-aware humorous captioning. Given an input image $x$ and a text condition $c$ that explicitly specifies the target cultural context, the model is required to generate a short, natural, and humorous caption $y$. The generation process can be formulated as:

$$
y \sim p(y \mid x, c)
\tag{1}
$$

where $c$ indicates the target cultural background, for example, generating a humorous caption under the Eastern cultural context or the Western cultural context.

In this work, cultural context is instantiated using two coarse-grained conditions: the Eastern cultural context and the Western cultural context. This distinction is introduced for task modeling purposes, with the goal of capturing broad differences in associative patterns and expressive tendencies across cultural backgrounds, rather than providing a fine-grained or exhaustive definition of culture.

Unlike conventional image captioning, the goal of our task is not to provide an objective transcription of image content. Instead, the model must organize a humorous caption for the same visual situation by combining visual understanding with the shared experiences, expressive conventions, and potential associative pathways associated with the target cultural context. Accordingly, captions generated for the same image under different cultural contexts are not expected to share the same surface wording or even exactly the same humorous trigger. More importantly, however, they should all remain centered on the same input image and maintain clear semantic connections to the entities, actions, scenes, or relations depicted in it. In other words, differences across cultural versions should primarily lie in the interpretive pathway and humor construction, rather than in arbitrary divergence from the image content.

From the perspective of task objectives, an ideal output should satisfy at least three requirements. First, the caption should maintain stable correspondence with the visible content of the image, rather than introducing core information without visual support. Second, it should reflect more natural associative patterns and expressive logic under the target cultural context, rather than creating superficial variation by mechanically inserting cultural symbols. Third, the caption itself should exhibit a perceptible humorous effect while remaining concise. Based on this task definition, we next establish a six-dimensional evaluation framework to characterize generation quality in a more systematic manner.

## 4 Evaluation Framework

Generating humorous captions under cultural constraints simultaneously involves visual understanding, contextual alignment, linguistic organization, and humorous expression, making it difficult to characterize output quality with a single metric. A caption may be highly relevant to the image yet fail to reflect the target cultural context, or it may align with the cultural context while lacking a clear humorous effect. To enable a more stable and fine-grained analysis of model performance on this task, we establish a six-dimensional evaluation framework covering Image Relevance, Contextual Fit, Semantic Richness, Reasonableness, Humor, and Creativity.



<!-- page 0005 -->

Overall, these six dimensions can be grouped into three categories. The first category concerns visual-context alignment, including Image Relevance and Contextual Fit. The second concerns semantic and expressive quality, including Semantic Richness and Reasonableness. The third concerns humor performance, including Humor and Creativity. The first two categories are used to evaluate whether the output is genuinely grounded in both the image and the target cultural context, while the last category assesses whether the caption further develops effective and non-trivial humorous expression on that basis.

Specifically, Image Relevance (IR) measures whether the caption is anchored in the visible content of the image. Contextual Fit (CF) measures whether the caption naturally reflects the associative patterns and expressive logic of the target cultural context. Semantic Richness (SR) measures whether the text provides additional semantic layers or interpretive space beyond surface-level description. Reasonableness (Ra) measures whether the expression is natural, coherent, and broadly consistent with commonsense. Humor (Hu) measures whether the output contains a perceptible humorous effect. Creativity (Cr) measures whether the idea or expression shows novelty and avoids overly templated responses.

To improve evaluation consistency and interpretability, each dimension is scored on a 10-point scale, together with a four-level rubric constraining different score ranges. Specifically, scores of 0–2 indicate extremely poor performance on the target dimension, typically involving severe distortion, obvious conflict, or near-complete failure. Scores of 3–5 indicate relatively weak performance: the dimension is only partially satisfied and still exhibits clear deficiencies. Scores of 6–7 indicate generally good performance: the major requirements are met, but there remains room for improvement in completeness, detail, or stability. Scores of 8–10 indicate strong performance with high completion quality and only minor or negligible defects. For this task, scores in the 8–10 range usually correspond to relatively strong and comparatively rare high-quality outputs. We report both the score of each individual dimension and their overall average to present model performance from multiple perspectives (See Appendix B for the

Table 1: Dataset organization. The three splits are image-disjoint. “Asym.” denotes asymmetric cultural organization for training, and “Sym.” denotes symmetric dual-context references for evaluation.

| Split | Images | Role | Culture | Output |
|---|---:|---|---|---|
| Train | 3500 | Training | Asym. | Captions<br>+ refusal |
| Dev | 500 | Validation | Asym. | Captions |
| Benchmark | 1000 | Evaluation | Sym. | Western/Eastern<br>refs. |

full evaluation protocol).

## 5 Data Construction

To support culture-aware humorous captioning, we construct both training/development data and a cross-cultural benchmark under a unified task definition: generating a short humorous caption conditioned on an input image and a target cultural context. Starting from the raw source pool, we retain 5,000 task-suitable images and divide them into three disjoint subsets: 3,500 for training, 500 for development, and 1,000 for benchmark evaluation. Table 1 summarizes the resulting data organization.

The raw images are collected from CLoT. We filter them according to visual richness and reinterpretability, favoring samples that contain object relations, action interactions, scene cues, or situational contrast that can support culture-conditioned humorous reconstruction. We remove text-dominant images and multi-panel composites to avoid heavy OCR dependence and cross-panel narrative complexity. Explicit cultural symbols are treated as a preference rather than a strict requirement. The final filtered pool contains 5,000 images.

All high-quality captioned data in this work are constructed under a unified pipeline consisting of candidate generation, automatic screening, and manual spot-checking (see the appendix for details), with additional review of ambiguous cases when necessary. This pipeline is applied consistently across both training supervision and benchmark reference con-



<!-- page 0006 -->

struction. Different subsets mainly differ in their functional role and in the model used for candidate generation, rather than in the quality-control procedure itself.

For the training data, we adopt an asymmetric cross-cultural design. Large-scale captions under the Western cultural context are used to learn shared capabilities, including visual grounding, conditional response, and humor organization, while captions under the Eastern cultural context are reserved as a smaller high-quality resource for later adaptation. We additionally include a small number of refusal samples to model context-mismatch cases, where the image does not provide sufficient support for the target cultural context. For standard caption samples, candidate captions are generated for each image-context pair and one caption is retained after screening; for refusal samples, a unified short template is used as the target output. Quality control focuses on image relevance, contextual fit, linguistic naturalness, and humor effectiveness.

The benchmark is constructed on the 1,000-image test split, which is fully disjoint from the training and development sets. For each benchmark image, we build reference captions under both the Western cultural context and the Eastern cultural context using the same high-quality construction pipeline. These references are not intended to exhaust all valid humorous expressions; instead, they provide stable and high-quality anchors for evaluating Image Relevance, Contextual Fit, Humor, and Creativity under controlled cross-cultural comparison.

## 6 Method

### 6.1 Method Overview

For the task of culture-aware humorous captioning, we propose CuHAlign, a staged alignment framework, as in Figure 2. Given an input image $x$ and a target cultural context condition $c$, the model generates a caption $y \sim p(y \mid x, c)$. Since this task requires the model to jointly satisfy Image Relevance, Contextual Fit, and Humor, a single supervision objective is insufficient to fully optimize generation quality. We therefore adopt a three-stage training pipeline. First, the model is initialized with high-resource supervision under the Western cultural context to establish task response patterns and output format constraints. Second, multi-dimensional preference alignment is performed via judge-based GRPO, together with a Degradation-aware Prototype Repulsion Constraint to mitigate reward hacking in open-ended generation. Third, the model is adapted with a small amount of supervision under the Eastern cultural context to support low-resource cultural transfer. This design is consistent with the data construction strategy in Section 5: large-scale data under the Western cultural context is used to learn shared capabilities, while smaller-scale data under the Eastern cultural context is reserved for later adaptation.

### 6.2 Backbone Model and Task Initialization

We adopt Qwen3-VL-8B [66] as the backbone model and use LoRA for parameter-efficient fine-tuning. Preliminary analysis suggests that, although the backbone already possesses strong visual understanding ability, it remains insufficient in responding to explicit cultural conditions, producing compressed humorous captions, and controlling output format. To bring the model distribution into the target task space, in the first stage we conduct supervised fine-tuning on 3,000 image-text samples under the Western cultural context from the training pool described in Section 5. Given a training sample $(x_i, c_i, y_i)$, the optimization objective is

$$
\mathcal{L}_{\mathrm{SFT}} = - \sum_i \log p_\theta(y_i \mid x_i, c_i).
\tag{2}
$$

This stage mainly establishes instruction following for the task, caption-format constraints, and the basic ability to generate humorous captions under a cultural context. However, supervised fine-tuning alone cannot directly optimize the joint balance among Image Relevance, Contextual Fit, and Humor, which motivates the subsequent preference alignment stage.



<!-- page 0007 -->

[Figure: Three-stage framework diagram for CuHAlign. Stage 1: “Western-culture SFT” with “Images” and “Western Cultural Context” fed into “Qwen3-VL-8B” + “LoRA”, producing $\mathcal{L}_{\mathrm{SFT}}$. Stage 2: “Preference Alignment via GRPO” with “Sample model”, “Candidate Set” containing $y_1, y_2, y_3, y_4, y_5, y_6, y_6, y_7, y_8$ and $y_{\mathrm{ref}}$ “(Anchor)”, “LLM Judge”, “Relative Order w.r.t. $y_{\mathrm{ref}}$” showing $y_5$ ++, $y_2$ +, $y_{\mathrm{ref}}$ 0 “Reference”, $y_3$ −, $y_1$ −−, losses $\mathcal{L}_{\mathrm{GRPO}}$ and $\mathcal{L}_{\mathrm{deg}}$, and “DPRC ($\mathcal{L}_{\mathrm{deg}}$ penalty)” with “Degradation Prototypes”, vectors $\mathbf{g}$ and $\mathbf{p}$. Stage 3: “Low-resource Adaptation to Eastern Context” with “Eastern Adaptation Data Mixture (1,000 samples)”: “50% - Target-domain Adaptation (New Images)”, “30% - Cross-cultural Reconstruction (Shared Images)”, “20% - Western Replay (Anti-forgetting)”, followed by “Qwen3-VL-8B + LoRA” and “CuHAlign Model”.]

Figure 2: Overall three-stage framework of CuHAlign. We first perform SFT on a Western-culture dataset to initialize the task, training the model to generate humorous captions from the input image and target cultural context (Stage 1). We then conduct preference alignment with a judge-based GRPO trainer, where multiple rollouts are ranked against a reference under a cultural-humor rubric and jointly optimized with a degradation-aware prototype repulsion constraint (Stage 2). Finally, the aligned model is adapted to the Eastern cultural context through few-shot SFT on the Eastern dataset, while a small-size replay set of Western dataset is jointly used to mitigate forgetting (Stage 3).

### 6.3 Multi-dimensional Preference Alignment via an LLM Judge

Since our task is an open-ended creative generation problem without an explicitly verifiable reward, we use an LLM-as-a-Judge to provide preference signals. For each training sample, the current policy model samples $K = 8$ rollouts, which, together with the reference caption, form a candidate set. Given the input image, the cultural context condition, the candidate captions, and the evaluation rubric, the judge outputs a joint ranking over the candidate set. Compared with directly predicting absolute scores, within-group ranking can partially alleviate the instability of the judge’s scoring scale.

We treat the reference caption as an anchor and construct rewards only for the sampled rollouts. Let $\mathrm{rank}_j$ denote the rank of the $j$-th rollout in the joint ranking, and let $\mathrm{rank}_{\mathrm{ref}}$ denote the rank of the reference caption. The raw reward of rollout $j$ is defined as

$$
r_j = f(\mathrm{rank}_j, \mathrm{rank}_{\mathrm{ref}}),
\tag{3}
$$

where $f(\cdot)$ maps the relative rank difference to a bounded scalar: rollouts ranked above the reference receive positive rewards, while those ranked below it receive negative rewards, with the magnitude increasing as the rank gap grows. We then perform a relative-advantage transformation on $\{r_j\}_{j=1}^{K}$ within each sampled group, and use the resulting advantages



<!-- page 0008 -->

for GRPO updates.

After obtaining within-group relative rewards, we optimize the policy using GRPO. Unlike supervised learning, which performs token-level likelihood fitting to a single reference answer, GRPO still operates on the token probability distribution of the generated sequence, but weights it according to sequence-level relative advantage. As a result, the optimization target shifts from “reproducing the reference caption” to “increasing the probability of outputs that better satisfy multi-dimensional preferences.”

To alleviate reward hacking in judge-based preference optimization, we further introduce a Degradation-aware Prototype Repulsion Constraint. For training samples with degradation annotations (see the appendix for details), each annotation contains one or more degradation directions together with their corresponding evidence texts. Before training, we aggregate evidence texts by degradation direction and map them into a shared representation space using a unified text encoder. The mean representation of evidence texts from the same direction is taken as the prototype vector $\mathbf{p}$ for that degradation direction. For a generated output, we use the same encoder to obtain its sequence-level representation $\mathbf{g}$. For generated samples with degradation annotations, we compute the cosine similarity between $\mathbf{g}$ and the corresponding degradation prototype. When the similarity exceeds a threshold $m$, a repulsion penalty is imposed:

$$
\mathcal{L}_{\mathrm{deg}} = \max(0, \cos(\mathbf{g}, \mathbf{p}) - m).
\tag{4}
$$

If a sample is associated with multiple degradation directions, the losses for different directions are combined by weighted summation to obtain $\mathcal{L}_{\mathrm{deg}}$. The final optimization objective is

$$
\mathcal{L} = \mathcal{L}_{\mathrm{GRPO}} + \lambda \mathcal{L}_{\mathrm{deg}}.
\tag{5}
$$

Here, $\mathcal{L}_{\mathrm{deg}}$ is activated only for samples with degradation annotations, serving as an additional structured negative constraint around known degradation neighborhoods. It complements the judge-ranking signal and reduces the risk that the policy exploits local rubric preferences while drifting away from the true task objective.

### 6.4 Low-resource Adaptation to the Eastern Cultural Context

After the first two stages, the model has acquired relatively strong shared capabilities under the high-resource distribution of the Western cultural context, including visual understanding, conditional response, caption organization, and multi-dimensional preference balancing. However, because these capabilities are mainly learned from high-resource Western-distribution data, the model’s default associative pathways and expressive tendencies may still remain biased toward that context. To address this issue, in the final stage we introduce a lightweight adaptation process using data under the Eastern cultural context to calibrate the model toward the low-resource target setting.

This stage uses 1,000 image-text pairs in total. Among them, 50% are new images paired with captions under the Eastern cultural context, which are used for target-domain adaptation; 30% are Eastern-context captions for images already appearing in the training pool, which are used to learn cross-cultural humorous reconstruction for the same visual situation; and the remaining 20% are supervised samples under the Western cultural context, which are replayed to mitigate catastrophic forgetting. The training procedure is the same as in the first stage and still uses supervised fine-tuning. However, the goal here is no longer to establish basic task ability, but to perform targeted adaptation of the shared capabilities to the low-resource Eastern cultural context.

## 7 Experiments

### 7.1 Experimental Setup

We construct a cross-cultural benchmark containing 1,000 images in total. Each test sample consists of an input image and an explicitly specified cultural context condition, and the model is required to generate a short humorous caption. To ensure fair comparison, all models are evaluated on the same test split, and results are reported separately under the Western cultural context and the Eastern cultural context.



<!-- page 0009 -->

To reduce additional bias caused by cross-lingual mismatch, the Eastern cultural context setting uses Chinese prompts for inference, Chinese prompts for evaluation, and Chinese generated outputs, while the Western cultural context setting uses English prompts for inference, English prompts for evaluation, and English generated outputs. Accordingly, our analysis mainly focuses on relative model performance within the same cultural setting, as well as the difference between the same model with and without explicit cultural conditioning.

We adopt the six-dimensional evaluation framework introduced in Section 4, including Image Relevance (IR), Contextual Fit (CF), Semantic Richness (SR), Reasonableness (Ra), Humor (Hu), and Creativity (Cr). Each dimension is scored on a 10-point scale, and the overall score is computed as the unweighted average of the six dimensions. Evaluation follows a human-machine hybrid protocol: among the 1,000 test samples, a fixed 20% subset is scored by human annotators, while the remaining 80% is scored automatically by an LLM-as-a-Judge under a unified rubric. For each metric, the final result is obtained by directly averaging the human-scored portion and the judge-scored portion over the full test set, thereby combining manual reliability with scalable automatic evaluation. The compared baselines include general-purpose multimodal large language models, the Qwen3-VL-8B backbone, and the prior relevant method CLoT[12]. In all subsequent experiments, we report both the six individual dimension scores and the overall average, with particular attention to CF, since it most directly reflects the model’s ability to respond to explicit cultural context conditions.Additional qualitative examples and failure cases are provided in Appendix.

## 7.2 Main Results

Tables 2 report the main results under the Western cultural context and the Eastern cultural context, respectively. Overall, existing multimodal large language models already exhibit a certain capability for humorous image captioning. However, under explicit cultural constraints, performance differences across models are much larger on Contextual Fit (CF) than on several dimensions more closely related to general caption quality. This indicates that generating an amusing caption and generating a humorous caption that is appropriate for a target cultural context are not the same capability; the latter places substantially higher demands on conditional response and contextual modeling.

In contrast, CuHAlign achieves the best CF under both cultural settings while maintaining strong overall quality. Under the Western cultural context, CuHAlign obtains an overall average score of 6.63 and a CF score of 6.63. Under the Eastern cultural context, it achieves an overall average of 6.66 and a CF score of 6.30. Compared with the Qwen3-VL-8B backbone, CuHAlign improves CF from 5.49 to 6.63 under the Western setting and from 5.22 to 6.30 under the Eastern setting, showing that the proposed method more effectively translates explicit cultural conditions into actual generation capability. At the same time, CuHAlign remains highly competitive in overall average score under both settings, indicating that these gains are not obtained by sacrificing general generation quality.

More importantly, the advantage of CuHAlign is concentrated on the task-specific dimension of Contextual Fit, rather than being merely a uniform improvement in general caption quality. This result is consistent with both the task formulation and the method design: for culture-aware humorous captioning, the key is not simply to generate more generally amusing text, but to make the target cultural context genuinely participate in humor construction while preserving relevance to the image. The main results therefore support the necessity of studying culture-aware humorous captioning as an independent research problem and demonstrate that the proposed staged alignment framework can serve this goal effectively and stably.

## 7.3 Effect of Explicit Cultural Context

To verify the necessity of explicit cultural conditioning in this task, we compare model performance under three settings: the Western cultural context, the Eastern cultural context, and no cultural context. All



<!-- page 0010 -->

Table 2: Results under Western and Eastern culture contexts.

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="7">Western Culture Context</th>
<th colspan="7">Eastern Culture Context</th>
</tr>
<tr>
<th>IR</th>
<th>CF</th>
<th>SR</th>
<th>Ra</th>
<th>Hu</th>
<th>Cr</th>
<th>Avg.</th>
<th>IR</th>
<th>CF</th>
<th>SR</th>
<th>Ra</th>
<th>Hu</th>
<th>Cr</th>
<th>Avg.</th>
</tr>
</thead>
<tbody>
<tr>
<td>GPT-4o [67]</td>
<td>7.27</td>
<td>6.11</td>
<td>5.91</td>
<td>8.06</td>
<td>6.76</td>
<td>6.47</td>
<td>6.76</td>
<td>7.51</td>
<td>5.72</td>
<td>5.96</td>
<td>8.04</td>
<td>6.74</td>
<td>6.50</td>
<td>6.75</td>
</tr>
<tr>
<td>gemini-3-flash-preview [68]</td>
<td>7.32</td>
<td>5.71</td>
<td>5.86</td>
<td>8.14</td>
<td>6.92</td>
<td>6.25</td>
<td>6.70</td>
<td>7.23</td>
<td>5.23</td>
<td>5.89</td>
<td>8.01</td>
<td>6.83</td>
<td>6.17</td>
<td>6.56</td>
</tr>
<tr>
<td>Claude Sonnet 4.5_pred [69]</td>
<td>7.11</td>
<td>5.66</td>
<td>5.89</td>
<td>8.05</td>
<td>6.82</td>
<td>6.21</td>
<td>6.62</td>
<td>7.21</td>
<td>5.11</td>
<td>5.72</td>
<td>7.97</td>
<td>6.78</td>
<td>6.16</td>
<td>6.49</td>
</tr>
<tr>
<td>InternVL3-8B-Instruct [70]</td>
<td>7.08</td>
<td>4.90</td>
<td>4.95</td>
<td>7.79</td>
<td>6.00</td>
<td>5.61</td>
<td>6.06</td>
<td>6.83</td>
<td>4.79</td>
<td>5.24</td>
<td>7.78</td>
<td>6.10</td>
<td>5.78</td>
<td>6.09</td>
</tr>
<tr>
<td>LLaVA-OneVision-7B [71]</td>
<td>6.02</td>
<td>4.67</td>
<td>4.44</td>
<td>6.97</td>
<td>4.55</td>
<td>4.64</td>
<td>5.21</td>
<td>6.03</td>
<td>3.15</td>
<td>3.40</td>
<td>6.60</td>
<td>3.69</td>
<td>3.74</td>
<td>4.44</td>
</tr>
<tr>
<td>MiniCPM-V 2.6 [72]</td>
<td>6.82</td>
<td>5.17</td>
<td>5.21</td>
<td>7.75</td>
<td>5.86</td>
<td>5.82</td>
<td>6.10</td>
<td>6.52</td>
<td>3.80</td>
<td>4.37</td>
<td>7.15</td>
<td>4.87</td>
<td>4.61</td>
<td>5.22</td>
</tr>
<tr>
<td>MiniGPT-4 [73]</td>
<td>6.54</td>
<td>3.94</td>
<td>2.95</td>
<td>6.98</td>
<td>3.97</td>
<td>3.36</td>
<td>4.62</td>
<td>4.88</td>
<td>2.41</td>
<td>2.52</td>
<td>5.73</td>
<td>1.90</td>
<td>2.32</td>
<td>3.29</td>
</tr>
<tr>
<td>GLM-4V-9B [74]</td>
<td>4.79</td>
<td>3.70</td>
<td>3.60</td>
<td>5.67</td>
<td>2.25</td>
<td>3.01</td>
<td>3.84</td>
<td>5.42</td>
<td>3.01</td>
<td>3.37</td>
<td>6.62</td>
<td>2.72</td>
<td>3.14</td>
<td>4.05</td>
</tr>
<tr>
<td>Qwen2.5-VL-7B-Instruct [75]</td>
<td>6.60</td>
<td>4.94</td>
<td>4.93</td>
<td>7.61</td>
<td>5.92</td>
<td>5.55</td>
<td>5.92</td>
<td>6.88</td>
<td>4.19</td>
<td>4.87</td>
<td>7.74</td>
<td>5.39</td>
<td>5.31</td>
<td>5.73</td>
</tr>
<tr>
<td>Qwen3-VL-8B-Instruct [66]</td>
<td>7.04</td>
<td>5.49</td>
<td>5.61</td>
<td>7.84</td>
<td>6.41</td>
<td>6.20</td>
<td>6.43</td>
<td>7.17</td>
<td>5.22</td>
<td>5.73</td>
<td>7.87</td>
<td>6.63</td>
<td>6.28</td>
<td>6.48</td>
</tr>
<tr>
<td>cogvlm2-llama3-chat-19B [76]</td>
<td>6.92</td>
<td>4.93</td>
<td>5.03</td>
<td>7.76</td>
<td>5.80</td>
<td>5.57</td>
<td>6.00</td>
<td>7.20</td>
<td>3.93</td>
<td>4.52</td>
<td>7.73</td>
<td>5.02</td>
<td>4.84</td>
<td>5.54</td>
</tr>
<tr>
<td>QwenVL+CLoT [12]</td>
<td>7.11</td>
<td>4.32</td>
<td>4.38</td>
<td>7.80</td>
<td>5.67</td>
<td>5.02</td>
<td>5.72</td>
<td>7.26</td>
<td>3.75</td>
<td>3.56</td>
<td>7.76</td>
<td>4.80</td>
<td>4.10</td>
<td>5.20</td>
</tr>
<tr>
<td>CuHAlign</td>
<td>6.88</td>
<td>6.63</td>
<td>5.60</td>
<td>7.84</td>
<td>6.67</td>
<td>6.16</td>
<td>6.63</td>
<td>6.89</td>
<td>6.30</td>
<td>5.91</td>
<td>7.88</td>
<td>6.68</td>
<td>6.30</td>
<td>6.66</td>
</tr>
</tbody>
</table>

Table 3: Effect of explicit cultural context conditioning.

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="2">No Context</th>
<th colspan="2">Western Context</th>
<th colspan="2">Eastern Context</th>
</tr>
<tr>
<th>CF</th>
<th>Overall</th>
<th>CF</th>
<th>Overall</th>
<th>CF</th>
<th>Overall</th>
</tr>
</thead>
<tbody>
<tr>
<td>InternVL3-8B-Instruct [70]</td>
<td>3.55</td>
<td>5.84</td>
<td>4.90</td>
<td>6.06</td>
<td>4.79</td>
<td>6.09</td>
</tr>
<tr>
<td>MiniCPM-V 2.6 [72]</td>
<td>3.34</td>
<td>5.43</td>
<td>5.17</td>
<td>6.10</td>
<td>3.80</td>
<td>5.22</td>
</tr>
<tr>
<td>Qwen3-VL-8B-Instruct [66]</td>
<td>3.97</td>
<td>6.24</td>
<td>5.49</td>
<td>6.43</td>
<td>5.22</td>
<td>6.48</td>
</tr>
<tr>
<td>CuHAlign</td>
<td>5.21</td>
<td>6.37</td>
<td>6.63</td>
<td>6.63</td>
<td>6.30</td>
<td>6.66</td>
</tr>
</tbody>
</table>

results are obtained on the same 1,000 test samples and are evaluated under the unified six-dimensional framework introduced in Section 4.

Overall, as in Table 3, the introduction of explicit cultural context leads to the most significant gains on Contextual Fit (CF) across models. For example, for Qwen3-VL-8B, the CF score increases from 3.97 in the no-context setting to 5.49 and 5.22 under the Western and Eastern settings, respectively. Its overall average score also rises from 6.24 to 6.43 and 6.48. By comparison, CuHAlign makes more effective use of explicit cultural conditions: its CF score increases from 5.21 in the no-context setting to 6.63 and 6.30 under the Western and Eastern settings, while its overall average score improves from 6.37 to 6.63 and 6.66.

These results show that explicit cultural context is not an optional auxiliary prompt, but a factor that substantially changes how the model interprets the image and organizes humorous expression. Meanwhile, the larger CF gains achieved by CuHAlign under culturally conditioned settings indicate that the proposed method can not only generate humorous captions in a general sense, but can also more reliably convert the target cultural context into actual generation behavior. This finding is consistent with the main results in Section 7.2 and the ablation analysis in Section 7.4, and further supports the necessity of distinguishing culture-aware humorous captioning from general humorous captioning.



<!-- page 0011 -->

Table 4: Ablation study of the staged alignment framework under Western and Eastern cultural settings.  
The best results are highlighted in bold.

<table>
<thead>
<tr>
<th rowspan="2">Model Variant</th>
<th rowspan="2">SFT</th>
<th rowspan="2">GRPO</th>
<th rowspan="2">Deg.</th>
<th rowspan="2">E. Adapt.</th>
<th colspan="4">Western Context</th>
<th colspan="4">Eastern Context</th>
</tr>
<tr>
<th>IR</th>
<th>CF</th>
<th>Hu</th>
<th>Overall</th>
<th>IR</th>
<th>CF</th>
<th>Hu</th>
<th>Overall</th>
</tr>
</thead>
<tbody>
<tr>
<td>Base</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>7.04</strong></td>
<td>5.49</td>
<td>6.41</td>
<td>6.43</td>
<td>7.17</td>
<td>5.22</td>
<td>6.63</td>
<td>6.48</td>
</tr>
<tr>
<td>+ SFT</td>
<td>✓</td>
<td></td>
<td></td>
<td></td>
<td>6.42</td>
<td>6.13</td>
<td>6.25</td>
<td>6.38</td>
<td>6.80</td>
<td>5.25</td>
<td>5.98</td>
<td>6.01</td>
</tr>
<tr>
<td>+ GRPO</td>
<td>✓</td>
<td>✓</td>
<td></td>
<td></td>
<td>6.86</td>
<td>6.59</td>
<td>6.47</td>
<td>6.60</td>
<td>6.84</td>
<td>5.40</td>
<td>5.97</td>
<td>6.07</td>
</tr>
<tr>
<td>+ Deg.</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td></td>
<td>6.88</td>
<td>6.62</td>
<td>6.65</td>
<td>6.61</td>
<td>6.87</td>
<td>5.43</td>
<td>5.97</td>
<td>6.09</td>
</tr>
<tr>
<td>CuHAlign (full model)</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>6.88</td>
<td><strong>6.63</strong></td>
<td><strong>6.67</strong></td>
<td><strong>6.63</strong></td>
<td><strong>6.89</strong></td>
<td><strong>6.30</strong></td>
<td><strong>6.68</strong></td>
<td><strong>6.66</strong></td>
</tr>
</tbody>
</table>

### 7.4 Ablation Study of the Staged Alignment Framework

To examine the contribution of each component in the staged alignment framework proposed in Section 6, we conduct ablation studies under both the Western cultural context and the Eastern cultural context. The compared variants are, in order: the backbone model Qwen3-VL-8B; the model after supervised fine-tuning under the Western cultural context; the model further enhanced with GRPO; and the model further augmented with the Degradation-aware Prototype Repulsion Constraint. On top of these variants, we then add the final low-resource adaptation stage under the Eastern cultural context, together with a small amount of replayed Western supervision to mitigate catastrophic forgetting, yielding the final CuHAlign full model. Results are shown in Table 4.

Under the Western cultural context, the ablation results show a clear progressive trend. Compared with the backbone, Western-context supervised fine-tuning improves CF from 5.49 to 6.13, indicating that the first stage effectively establishes task response behavior and output format. After adding GRPO, the overall average score further increases to 6.60, and CF rises to 6.59, showing that multi-dimensional preference alignment is the key step for improving overall quality. Adding the Degradation-aware Prototype Repulsion Constraint further improves the overall average to 6.61, suggesting that this constraint provides additional benefit in balancing open-ended generation quality. Finally, the full model achieves the best results in this group, with an overall average of 6.63 and a CF score of 6.63.

Under the Eastern cultural context, the role of the final adaptation stage is even more pronounced. After Western-context supervised fine-tuning, GRPO, and the degradation-aware constraint, CF improves progressively from 5.25 to 5.40 and 5.43. On this basis, after further adaptation to the Eastern cultural context, the full model reaches an overall average of 6.66 and a CF score of 6.30, while Humor (Hu) and Creativity (Cr) also increase to 6.68 and 6.30, respectively. These results indicate that the first two stages mainly learn transferable task structure and alignment capability, whereas the final lightweight cultural adaptation stage effectively calibrates these shared capabilities toward the low-resource Eastern setting.

Overall, the ablation results support the functional division of CuHAlign. The first-stage supervised fine-tuning under the Western cultural context mainly establishes task format and basic conditional response. The second-stage GRPO is the most important step for improving generation quality. The Degradation-aware Prototype Repulsion Constraint further improves the overall balance in open-ended generation. The final adaptation stage under the Eastern cultural context is crucial for improving performance in the low-resource cultural setting. Notably, the full model achieves the highest CF under both cultural settings, further confirming that the staged framework can stably transform explicit cultural conditions into actual generation capability.



<!-- page 0012 -->

[Figure: Bar chart comparing three LLM judges on agreement with human preference (%). Legend: CN - harder subset, CN - easier subset, EN - harder subset, EN - easier subset. Models: GPT-5.1 (68.2, 77.3, 71.6, 79.2), Gemini-3-Flash-Preview (63.7, 71.9, 65.1, 77.6), Claude Sonnet 4.5 (61.8, 69.5, 67.3, 75.4).]

Figure 3: Comparison of three LLM judges on the judge validation set for assessing the reliability of automatic pairwise evaluation across languages and difficulty levels.

### 7.5 Judge Reliability and Agreement with Human Evaluation

To assess the reliability of automatic evaluation, we further construct a dedicated judge validation set. Specifically, we sample 400 image instances from the test set and build pairwise evaluation samples of the form image + high-quality caption + low-quality caption (see the appendix for details). The high-quality captions are taken from the human reference captions in the dataset, while the low-quality captions are mainly sampled from relatively poor outputs of baseline models on the corresponding images, with an effort to cover different types of quality defects.

To distinguish judge performance under different levels of difficulty, we further divide the validation set into two subsets. The first 200 cases contain caption pairs with relatively large quality gaps, while the remaining 200 contain pairs with smaller quality differences and more ambiguous decision boundaries. We then ask GPT-5.1, Gemini-3-Flash-Preview[68], and Claude Sonnet 4.5[69] to perform pairwise judgments on these samples, and compute their agreement rates with the manually predefined better-worse labels. The results are reported in Figure 3.

Overall, all three judges achieve higher agreement on samples with clear quality differences, while accuracy drops on more ambiguous pairs. This indicates that automatic evaluation is reliable for distinguishing outputs with obvious quality gaps, but remains challenging for fine-grained discrimination. Our validation focuses on pairwise comparison rather than absolute score calibration, since the latter is inherently difficult for culture-aware humorous captioning due to its open-ended and multi-dimensional nature. In practice, the judge in our framework mainly provides relative quality signals, so strong better-worse discrimination already offers meaningful evidence of judge adequacy for both evaluation and preference alignment. Among the three judges, GPT-5.1 achieves the highest agreement in all four settings and shows the most stable overall performance, so we adopt a hybrid protocol with 20% human scoring and 80%judge scoring to balance scalability and reliability.

## 8 Conclusion

We introduce culture-aware humorous captioning and propose CuHAlign to improve multimodal humor generation under explicit cultural contexts. Results show clear gains, especially in contextual fit, while the current Chinese–Eastern and English–Western setup may not fully disentangle language effects from cultural effects.

## References

[1] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 26296–26306, 2024.

[2] Yuqian Yuan, Wentong Li, Jian Liu, Dongqi Tang, Xinjie Luo, Chi Qin, Lei Zhang, and Jianke Zhu. Osprey: Pixel understanding with visual instruction tuning. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 28202–28211, 2024.

[3] Ruotian Peng, Haiying He, Yake Wei, Yandong Wen, and Di Hu. Patch matters: Training-free



<!-- page 0013 -->

fine-grained image caption enhancement via local perception. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 3963–3973, 2025.

[4] Fan Lu, Wei Wu, Kecheng Zheng, Shuailei Ma, Biao Gong, Jiawei Liu, Wei Zhai, Yang Cao, Yujun Shen, and Zheng-Jun Zha. Benchmarking large vision-language models via directed scene graph for comprehensive image captioning. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 19618–19627, 2025.

[5] Yebin Lee, Imseong Park, and Myungjoo Kang. Fleur: An explainable reference-free evaluation metric for image captioning using a large multimodal model. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3732–3746, 2024.

[6] Kanzhi Cheng, Wenpo Song, Jiaxin Fan, Zheng Ma, Qiushi Sun, Fangzhi Xu, Chenyang Yan, Nuo Chen, Jianbing Zhang, and Jiajun Chen. Caparena: Benchmarking and analyzing detailed image captioning in the llm era. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 14077–14094, 2025.

[7] Long Lian, Yifan Ding, Yunhao Ge, Sifei Liu, Hanzi Mao, Boyi Li, Marco Pavone, Ming-Yu Liu, Trevor Darrell, Adam Yala, et al. Describe anything: Detailed localized image and video captioning. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 21766–21777, 2025.

[8] Xiaohui Chen, Satya Narayan Shukla, Mahmoud Azab, Aashu Singh, Qifan Wang, David Yang, ShengYun Peng, Hanchao Yu, Shen Yan, Xuewen Zhang, et al. Compcap: Improving multimodal large language models with composite captions. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 23582–23592, 2025.

[9] Lin Zhang, Xianfang Zeng, Kangcong Li, Gang Yu, and Tao Chen. Sc-captioner: Improving image captioning with self-correction by reinforcement learning. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 23145–23155, 2025.

[10] Yahan Tu, Rui Hu, and Jitao Sang. Ode: Open-set evaluation of hallucinations in multimodal large language models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 19836–19845, 2025.

[11] Jeong Ryong Lee, Yejee Shin, Geonhui Son, and Dosik Hwang. Diffusion bridge: leveraging diffusion model to reduce the modality gap between text and vision for zero-shot image captioning. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 4050–4059, 2025.

[12] Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, and Pan Zhou. Let’s think outside the box: Exploring leap-of-thought in large language models with creative humor generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 13246–13257, 2024.

[13] Abhilash Nandy, Yash Agarwal, Ashish Patwa, Millon Madhur Das, Aman Bansal, Ankit Raj, Pawan Goyal, and Niloy Ganguly. \*\*\* vers-but\*\*\*: A high-quality annotated multimodal dataset for evaluating satire comprehension capability of vision-language models. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, pages 16878–16895, 2024.

[14] Arkady Saakyan, Shreyas Kulkarni, Tuhin Chakrabarty, and Smaranda Muresan. Understanding figurative meaning through explainable visual entailment. In *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 1–23, 2025.



<!-- page 0014 -->

[15] Yuriel Ryan, Rui Yang Tan, Kenny Tsu Wei Choo, and Roy Ka-Wei Lee. Humor in pixels: Benchmarking large multimodal models understanding of online comics. *arXiv preprint arXiv:2509.12248*, 2025.

[16] Vedaant V Jain, Gabriel Kreiman, and Felipe dos Santos Alves Feitosa. Humordb: Can ai understand graphical humor? In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 604–613, 2025.

[17] EunJeong Hwang, Peter West, and Vered Shwartz. Bottlehumor: Self-informed humor explanation using the information bottleneck principle. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 22611–22632, 2025.

[18] Siqi Shen, Lajanugen Logeswaran, Moontae Lee, Honglak Lee, Soujanya Poria, and Rada Mihalcea. Understanding the capabilities and limitations of large language models for cultural commonsense. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 5668–5680, 2024.

[19] Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Siddhant Shivdutt Singh, Alham Fikri Aji, Jacki O’Neill, Ashutosh Modi, and Monojit Choudhury. Towards measuring and modeling “culture” in llms: A survey. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, pages 15763–15784, 2024.

[20] Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, and Mona Diab. Investigating cultural alignment of large language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 12404–12422, 2024.

[21] Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie. Culturellm: Incorporating cultural differences into large language models. *Advances in Neural Information Processing Systems*, 37:84799–84838, 2024.

[22] Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen, Xing Xie, and Jindong Wang. Culturepark: Boosting cross-cultural understanding in large language models. *Advances in Neural Information Processing Systems*, 37:65183–65216, 2024.

[23] Shaily Bhatt and Fernando Diaz. Extrinsic evaluation of cultural competence in large language models. In *Findings of the Association for Computational Linguistics: EMNLP 2024*, pages 16055–16074, 2024.

[24] Chen Cecilia Liu, Iryna Gurevych, and Anna Korhonen. Culturally aware and adapted nlp: A taxonomy and a survey of the state of the art. *Transactions of the Association for Computational Linguistics*, 13:652–689, 2025.

[25] Arijit Maji, Raghvendra Kumar, Akash Ghosh, Nemil Shah, Abhilekh Borah, Vanshika Shah, Nishant Mishra, Sriparna Saha, et al. Drishtikon: A multimodal multilingual benchmark for testing language models’ understanding on indian culture. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 1289–1313, 2025.

[26] Mohsinul Kabir, Ajwad Abrar, and Sophia Ananiadou. Break the checkbox: challenging closed-style evaluations of cultural alignment in llms. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 24–51, 2025.

[27] Meng-Chen Wu, Si-Chi Chin, Tess Wood, Ayush Goyal, and Narayanan Sadagopan. Incorporating diverse perspectives in cultural alignment: Survey of evaluation benchmarks through a three-dimensional framework. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 17037–17072, 2025.



<!-- page 0015 -->

[28] Jincenzi Wu, Jianxun Lian, Dingdong Wang, and Helen Meng. Socialcc: Interactive evaluation for cultural competence in language agents. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 33242–33271, 2025.

[29] Geyang Guo, Tarek Naous, Hiromi Wakaki, Yukiko Nishimura, Yuki Mitsufuji, Alan Ritter, and Wei Xu. Care: Multilingual human preference learning for cultural awareness. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 32854–32883, 2025.

[30] Runjia Li, Shuyang Sun, Mohamed Elhoseiny, and Philip Torr. Oxfordtvg-hic: Can machine make humorous captions from images? In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 20293–20303, 2023.

[31] Jifan Zhang, Lalit Jain, Yang Guo, Jiayi Chen, Kuan L Zhou, Siddharth Suresh, Andrew Wagenmaker, Scott Sievert, Timothy Rogers, Kevin Jamieson, et al. Humor in ai: Massive scale crowd-sourced preferences and benchmarks for cartoon captioning. *Advances in Neural Information Processing Systems*, 37:125264–125286, 2024.

[32] EunJeong Hwang and Vered Shwartz. Memecap: A dataset for captioning and interpreting memes. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 1433–1445, 2023.

[33] Zhijun Xu, Siyu Yuan, Yiqiao Zhang, Jingyu Sun, Tong Zheng, and Deqing Yang. Punmemecn: A benchmark to explore vision-language models’ understanding of chinese pun memes. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 18705–18721, 2025.

[34] Kuan Lok Zhou, Jiayi Chen, Siddharth Suresh, Reuben Narad, Timothy T Rogers, Lalit K Jain, Robert D Nowak, Bob Mankoff, and Jifan Zhang. Bridging the creativity understanding gap: Small-scale human alignment enables expert-level humor ranking in llms. *arXiv preprint arXiv:2502.20356*, 2025.

[35] Yuyan Chen, Songzhou Yan, Zhihong Zhu, Zhixu Li, and Yanghua Xiao. Xmecap: Meme caption generation with sub-image adaptability. In *Proceedings of the 32nd ACM International Conference on Multimedia*, pages 3352–3361, 2024.

[36] Jiajun Zhang, Shijia Luo, Ruikang Zhang, and Qi Su. Humorchain: Theory-guided multi-stage reasoning for interpretable multimodal humor generation. *arXiv preprint arXiv:2511.21732*, 2025.

[37] Wenbo Shang, Yuxi Sun, Jing Ma, and Xin Huang. On the wings of imagination: Conflicting script-based multi-role framework for humor caption generation. *arXiv preprint arXiv:2602.06423*, 2026.

[38] Zhen Wang, Jun Xiao, Yueting Zhuang, Fei Gao, Jian Shao, and Long Chen. Learning combinatorial prompts for universal controllable image captioning. *International Journal of Computer Vision*, 133(1):129–150, 2025.

[39] Yuzhong Zhao, Yue Liu, Zonghao Guo, Weijia Wu, Chen Gong, Qixiang Ye, and Fang Wan. Controlcap: Controllable region-level captioning. In *European Conference on Computer Vision*, pages 21–38. Springer, 2024.

[40] Shanshan Zhao, Teng Wang, Jinrui Zhang, Xiangchen Wang, and Feng Zheng. Mcoca: Towards fine-grained multimodal control in image captioning. *Pattern Recognition*, page 112381, 2025.

[41] Shunqi Mao, Chaoyi Zhang, Hang Su, Hwanjun Song, Igor Shalyminov, and Weidong Cai. Controllable contextualized image captioning: Directing the visual narrative through user-defined highlights. In *European Conference on Computer Vision*, pages 464–481. Springer, 2024.



<!-- page 0016 -->

[42] Yeongtak Oh, Dohyun Chung, Juhyeon Shin, Sangha Park, Johan Barthelemy, Jisoo Mok, and Sungroh Yoon. Repic: Reinforced post-training for personalizing multi-modal language models. *arXiv preprint arXiv:2506.18369*, 2025.

[43] Dingyi Yang, Hongyu Chen, Xinglin Hou, Tiezheng Ge, Yuning Jiang, and Qin Jin. Visual captioning at will: Describing images and videos guided by a few stylized sentences. In *Proceedings of the 31st ACM international conference on multimedia*, pages 5705–5715, 2023.

[44] Kuniaki Saito, Donghyun Kim, Kwanyong Park, Atsushi Hashimoto, and Yoshitaka Ushiku. Captionsmiths: Flexibly controlling language pattern in image captioning. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 19872–19881, 2025.

[45] Yiming Ren, Zhiqiang Lin, Yu Li, Gao Meng, Weiyun Wang, Junjie Wang, Zicheng Lin, Jifeng Dai, Yujiu Yang, Wenhai Wang, et al. Anycap project: A unified framework, dataset, and benchmark for controllable omni-modal captioning. *arXiv preprint arXiv:2507.12841*, 2025.

[46] Chen Cecilia Liu, Anna Korhonen, and Iryna Gurevych. Cultural learning-based culture adaptation of language models. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 3114–3134, 2025.

[47] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, et al. Mmbench: Is your multi-modal model an all-around player? In *European conference on computer vision*, pages 216–233. Springer, 2024.

[48] Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. Seed-bench: Benchmarking multimodal llms with generative comprehension. *arXiv preprint arXiv:2307.16125*, 2023.

[49] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 9556–9567, 2024.

[50] Lianghui Zhu, Xinggang Wang, and Xinlong Wang. Judgelm: Fine-tuned large language models are scalable judges. *arXiv preprint arXiv:2310.17631*, 2023.

[51] Tianyi Xiong, Xiyao Wang, Dong Guo, Qinghao Ye, Haoqi Fan, Quanquan Gu, Heng Huang, and Chunyuan Li. Llava-critic: Learning to evaluate multimodal models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 13618–13628, 2025.

[52] Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee, Yuxuan Jiang, Canyu Chen, Tianhao Wu, et al. From generation to judgment: Opportunities and challenges of llm-as-a-judge. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 2757–2791, 2025.

[53] Dongping Chen, Ruoxi Chen, Shilin Zhang, Yaochen Wang, Yinuo Liu, Huichi Zhou, Qihui Zhang, Yao Wan, Pan Zhou, and Lichao Sun. Mllm-as-a-judge: Assessing multimodal llm-as-a-judge with vision-language benchmark. In *Forty-first International Conference on Machine Learning*, 2024.

[54] Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran Vaidyanathan, and Dieuwke Hupkes. Judging the judges: Evaluating alignment and vulnerabilities in llms-as-judges. In *Proceedings of the Fourth Workshop on Generation, Evaluation and Metrics (GEM$^2$)*, pages 404–430, 2025.

[55] Shu Pu, Yaochen Wang, Dongping Chen, Yuhang Chen, Guohao Wang, Qi Qin, Zhongyi Zhang, Zhiyuan Zhang, Zetong Zhou, Shuang Gong, et al. Judge anything: Mllm as a judge



<!-- page 0017 -->

across any modality. In *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2*, pages 5742–5753, 2025.

[56] Qiyuan Zhang, Yufei Wang, Yuxin Jiang, Liangyou Li, Chuhan Wu, Yasheng Wang, Xin Jiang, Lifeng Shang, Ruiming Tang, Fuyuan Lyu, et al. Crowd comparative reasoning: Unlocking comprehensive evaluations for llm-as-a-judge. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 5059–5074, 2025.

[57] Yixin Liu, Pengfei Liu, and Arman Cohan. On evaluating llm alignment by evaluating llms as judges. *arXiv preprint arXiv:2511.20604*, 2025.

[58] Jiawei Guo, Tianyu Zheng, Yizhi Li, Yuelin Bai, Bo Li, Yubo Wang, King Zhu, Graham Neubig, Wenhu Chen, and Xiang Yue. Mammoth-vl: Eliciting multimodal reasoning with instruction tuning at scale. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 13869–13920, 2025.

[59] Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han, Ganqu Cui, Jinyi Hu, Zhiyuan Liu, Hai-Tao Zheng, Maosong Sun, et al. Rlhf-v: Towards trustworthy mllms via behavior alignment from fine-grained correctional human feedback. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 13807–13816, 2024.

[60] Shengzhi Li, Rongyu Lin, and Shichao Pei. Multi-modal preference alignment remedies degradation of visual instruction tuning on language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 14188–14200, 2024.

[61] Yi-Fan Zhang, Tao Yu, Haochen Tian, Chaoyou Fu, Peiyan Li, Jianshu Zeng, Wulin Xie, Yang Shi, Huanyu Zhang, Junkang Wu, et al. Mm-rlhf: The next step forward in multimodal llm alignment. *arXiv preprint arXiv:2502.10391*, 2025.

[62] Jinhe Bi, Yujun Wang, Haokun Chen, Xun Xiao, Artur Hecker, Volker Tresp, and Yunpu Ma. Llava steering: Visual instruction tuning with 500x fewer parameters through modality linear representation-steering. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 15230–15250, 2025.

[63] Xintong Li, Junda Wu, Tong Yu, Rui Wang, Yu Wang, Xiang Chen, Jiuxiang Gu, Lina Yao, Julian McAuley, and Jingbo Shang. Commit: Coordinated multimodal instruction tuning. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 11533–11547, 2025.

[64] Ziang Yan, Zhilin Li, Yinan He, Chenting Wang, Kunchang Li, Xinhao Li, Xiangyu Zeng, Zilei Wang, Yali Wang, Yu Qiao, et al. Task preference optimization: Improving multimodal large language models with vision task alignment. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 29880–29892, 2025.

[65] Shuo Xing, Peiran Li, Yuping Wang, Ruizheng Bai, Yueqi Wang, Chan-Wei Hu, Chengxuan Qian, Huaxiu Yao, and Zhengzhong Tu. Re-align: Aligning vision language models via retrieval-augmented direct preference optimization. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*, pages 2379–2397, 2025.

[66] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-vl technical report. *arXiv preprint arXiv:2511.21631*, 2025.

[67] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark,



<!-- page 0018 -->

AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.

[68] Google. Gemini 3 flash preview. https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview, 2026. Official model documentation, accessed 2026-04-02.

[69] Anthropic. Claude sonnet 4.5 system card. https://www.anthropic.com/claude-sonnet-4-5-system-card, 2025. Official system card, accessed 2026-04-02.

[70] Jinguo Zhu, Weiyun Wang, Zhe Chen, Zhaoyang Liu, Shenglong Ye, Lixin Gu, Hao Tian, Yuchen Duan, Weijie Su, Jie Shao, et al. Internvl3: Exploring advanced training and test-time recipes for open-source multimodal models. *arXiv preprint arXiv:2504.10479*, 2025.

[71] Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Peiyuan Zhang, Yanwei Li, Ziwei Liu, et al. Llava-onevision: Easy visual task transfer. *arXiv preprint arXiv:2408.03326*, 2024.

[72] Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang, Junbo Cui, Hongji Zhu, Tianchi Cai, Haoyu Li, Weilin Zhao, Zhihui He, et al. Minicpm-v: A gpt-4v level mllm on your phone. *arXiv preprint arXiv:2408.01800*, 2024.

[73] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language understanding with advanced large language models. *arXiv preprint arXiv:2304.10592*, 2023.

[74] Team Glm, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan Zhang, Diego Rojas, Guanyu Feng, Hanlin Zhao, et al. Chatglm: A family of large language models from glm-130b to glm-4 all tools. *arXiv preprint arXiv:2406.12793*, 2024.

[75] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Junyang Lin. Qwen2.5-vl technical report. *ArXiv*, abs/2502.13923, 2025. URL https://api.semanticscholar.org/CorpusID:276449796.

[76] Wenyi Hong, Weihan Wang, Ming Ding, Wenmeng Yu, Qingsong Lv, Yan Wang, Yean Cheng, Shiyu Huang, Junhui Ji, Zhao Xue, et al. Cogvlm2: Visual language models for image and video understanding. *arXiv preprint arXiv:2408.16500*, 2024.
