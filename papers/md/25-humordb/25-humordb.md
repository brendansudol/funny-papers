<!-- Transcribed from 25-humordb.pdf -->



<!-- page 0001 -->

# HumorDB: Can AI understand graphical humor?

Vedaant V Jain  
University of Illinois Urbana-Champaign  
`vvjain3@illinois.edu`

Felipe dos Santos Alves Feitosa  
University of São Paulo  
`felipefeitosa@usp.br`

Gabriel Kreiman  
Harvard Medical School  
`gabriel.kreiman@tch.harvard.edu`

## Abstract

*Despite significant advancements in image segmentation and object detection, understanding complex scenes remains a significant challenge. Here, we focus on graphical humor as a paradigmatic example of image interpretation that requires elucidating the interaction of different scene elements in the context of prior cognitive knowledge. This paper introduces **HumorDB**, a novel, controlled, and carefully curated dataset designed to evaluate and advance visual humor understanding by AI systems. The dataset comprises diverse images spanning photos, cartoons, sketches, and AI-generated content, including minimally contrastive pairs where subtle edits differentiate between humorous and non-humorous versions. We evaluate humans, state-of-the-art vision models, and large vision-language models on three tasks: binary humor classification, funniness rating prediction, and pairwise humor comparison. The results reveal a gap between current AI systems and human-level humor understanding. While pretrained vision-language models perform better than vision-only models, they still struggle with abstract sketches and subtle humor cues. Analysis of attention maps shows that even when models correctly classify humorous images, they often fail to focus on the precise regions that make the image funny. Preliminary mechanistic interpretability studies and evaluation of model explanations provide initial insights into how different architectures process humor. Our results identify promising trends and current limitations, suggesting that an effective understanding of visual humor requires sophisticated architectures capable of detecting subtle contextual features and bridging the gap between visual perception and abstract reasoning. All the code and data are available here: https://github.com/kreimanlab/HumorDB*[^1]

[^1]: *20th* International Conference on Computer Vision, ICCV 2025 (Poster)

## 1. Introduction

The last decade has seen remarkable strides in computer vision, enabling systems to segment images, label objects, and even write sophisticated captions. Despite these successes, the problem of scene understanding remains challenging. Interpreting a scene often requires elucidating the relationship between objects and their positions, the intention of agents, and linking visual information with prior knowledge. This challenge is particularly evident in tasks that require higher-level cognitive processes, such as recognizing and interpreting humor in visual content. Graphical humor understanding demands a high level of cognitive abstraction, as it requires context awareness, expectations, cultural knowledge, and the identification of incongruities [4]. Thus, graphical humor serves as an ideal testbed for scene understanding capabilities.

Consider **Fig. 1**, left. To comprehend what is going on, the viewer needs to detect locations (surgical setting), agents (patient, medical practitioners), and objects (cell phone, hand). The grasping in the hand induces us to think that the medical experts have “surgically excised” the phone from the hand. Given the prominent role of cell phones, many people have jokingly stated that phones are physically attached to hands, and the image plays with this idea. Of note, the reader has likely never seen this particular image or any similar image before. Upon first exposure to this image, readers can rapidly interpret what is going on and may consider the image to be somewhat humorous (83.3% of participants indicated that this image is funny; more on how this number was computed is described in **Sec. 3.2**). In stark contrast, consider **Fig. 1**, right. The two images are identical except that the cell phone was removed. Despite the strong similarity between the two images, the one on the right is no longer humorous (85.7% of participants indicated that the image on the right is *not* funny).

Computational humor understanding extends beyond technical complexity to practical implications for human-



<!-- page 0002 -->

[Figure: two-panel cartoon image pair of an operating room with surgeons and a patient; the left image includes a phone in a surgeon’s hand, while the right image is modified.]

Figure 1. **Example image pair.** Left: image rated as funny (83.3% of participants). Right: modified image rated as not funny (85.7% of participants). Focus on the phone in the surgeon’s hand in the left image.

AI interaction, content moderation, and creative applications. However, existing datasets often lack rigorous controls, exhibit limited diversity, or focus primarily on text rather than visual humor. To address this, we introduce **HumorDB**, a dataset of images including photos, sketches and AI-generated content. Drawing inspiration from action recognition research (e.g., [17]), a key innovation in the dataset is the inclusion of pairs of minimally different images with contrasting humor ratings distinguished only by the humorous element like the one in Fig. 1, enabling precise evaluation of models’ ability to detect humor-inducing elements while controlling for confounding factors. We also include a benchmark consisting of quantitative human measurements in three different tasks using these images: Binary classification (funny vs. not funny), Range rating (scoring images on a scale of 1-10), and Comparison (deciding which of two images is funnier). We compare human responses with both vision-only models (e.g., [10, 15, 27, 33]) and vision-language models (e.g., [20, 24, 25, 32, 38]) across diverse image types and analyze models’ explanations using mechanistic interpretability techniques. HumorDB enables precise assessment of models’ ability to detect humor-inducing features.

Our findings reveal a substantial gap between current models and human-level humor understanding. State-of-the-art models outperform chance but fall below humans. The comparison task proves particularly challenging, with models showing limited ability to make nuanced judgments between similar images. Notably, large multimodal language models demonstrate robust zero-shot performance, suggesting promising directions for bridging this gap. Beyond performance evaluation, we leverage HumorDB’s contrastive pairs to analyze how humor understanding emerges in neural networks through attention map analysis and mechanistic interpretability techniques.

## 2. Related Work

The best-known theory of humor is probably the “incongruity theory” which posits that humor arises from unexpected subversions of contextual expectations [3]. Recent datasets for computational humor understanding [7, 13] include multi-modal humor detection [7, 13, 34], funny image captioning [22], abstract clipart scenes with object replacements [6], and matching captions to cartoons [16]. However, most efforts have focused on either textual humor [8, 9, 19, 30] or multimodal contexts [18, 28, 34] rather than purely visual humor and gaining contextual clues may be easier to get from one modality than another.

Computational approaches to humor understanding have involved using attention-based Bi-LSTM for identifying humor in text on social media [19], generation of negative examples [39], the use of transformers [14], and CRF-RNN-CNN [5]. However, most of these approaches have focused on either natural language [8, 9, 19, 30] or multimodal contexts (especially videos [18, 28, 34]).

HumorDB focuses on vision and significantly extends previous datasets via (1) diversity of realistic images (photos, cartoons, sketches, AI-generated), (2) sophisticated controls to distill humor from confounding factors, and (3) a comprehensive evaluation framework including human metrics across three different tasks.

## 3. Methods

All the code and data are available here: https://github.com/kreimanlab/HumorDB

### 3.1. Building HumorDB

We constructed a diverse repository of images through (i) web scraping via the Google Search API with broad queries and specific prompts followed by manual curation, and (ii) generating novel images using AI-based models like DALL-E [31] and MidJourney [29]. We capped each search result to 15 images to avoid style biases. The resulting images consisted of: Photos (36%), Photoshopped real-life photos (35%), Cartoons (14%), Sketches (5%), and AI-Generated images (10%). We removed images with explicit/offensive material. We removed cases where humor relied on embedded text but kept any non-humor-related text (e.g., artist names) to retain authenticity in the images.

A central innovation is our collection of paired images whose only differences involve removing or modifying the humorous element (e.g., Fig. 1). This was achieved by either (i) Photo Editing, i.e., using Adobe Photoshop to carefully remove, obscure, or replace objects that contributed to humor, or (ii) AI Inpainting, i.e., employing stable diffusion-based inpainting for more naturalistic edits that seamlessly replace incongruous elements while preserving the rest of the image. Through this process, we generated 1,271 pairs of original (“funny”) and modified (“not funny”) counterparts,ensuring visual similarity except for key comedic features. Importantly, to mitigate potential editing artifacts, we applied **subtle enhancements to both versions (funny and not funny)** of each pair. We further



<!-- page 0003 -->

validated that models learn humor-relevant features, not just editing artifacts, by also testing on a control set of 650 non-modified, non-funny images (see Sec. 5 for results and Appendix 4 for details). Throughout the manuscript, “original images” refer to humor-laden content, while “modified images” are those we altered to remove the humor.

### 3.2. Assessing human performance

We conducted online psychophysics experiments with 650 participants through Amazon Mechanical Turk and Prolific to gather human evaluations. Each participant rated 100 images in one of three tasks:

1. **Binary Task:** Two-alternative forced choice classification as “Funny” or “Not Funny”
2. **Range Task:** Rating funniness on a scale of 1 (Not at all funny) to 10 (Extremely funny)
3. **Comparison Task:** Selecting the funnier of two side-by-side images, followed by providing a brief justification for the choice

**Quality control.** We implemented 5 controls:

1. **Minimum Viewing Time:** 500ms minimum viewing time per image before response submission (based on [11]), with task termination after 4 violations
2. **Repeated Images:** 10% of images were repeated at random time points to assess self-consistency
3. **Outlier Removal:** Participants with >10% of ratings having z-scores outside ±1.96 were excluded
4. **Textual Justifications:** Brief justification of choices verified attention to content. Only in comparison task.
5. **Unique Task Enrollment:** Prevention of repeated participation in the same task

**Comparison Task Design.** To make pairwise comparisons tractable, we employed a stratified sampling approach:

1. Divided images into 8 strata using mean Binary ratings
2. Selected five representative images per stratum (40 total)
3. Collected additional Binary ratings for validation
4. Identified an anchor image per stratum for comparisons.

All comparisons had at least one of the 8 anchor images.

**Participant Reliability Assessment.** For the repeated images (10%), we applied the following exclusion criteria:

- Binary and Comparison Tasks: Excluded participants with >3 inconsistent responses on repeated images
- Range Task: Excluded participants if any single image received ratings differing by >4 points, or if >4 images showed differences exceeding 2 points

The results showed strong self-reliability in all tasks:

- Binary Task: The degree of self-consistency for repeated images was 84.2 ± 13.3%
- Range Task: Numerical judgments were highly stable ($\rho = 0.89$, Fig.5)
- Comparison Task: The degree of self-consistency for repeated choices was 91.3 ± 14.8%
- Original vs. Modified: Original images were consistently rated as funnier than their modified counterparts (86.4% of pairs, Fig.3)

[Figure: Heatmap showing pairwise percentages for Image i versus Image j, axes labeled Image i and Image j, colorbar labeled Percentage ranging 0 to 100.]

**Figure 2. The data showed between-subject consistency.** Each cell (i, j) represents the percentage of times when image i was rated funnier than image j. Participants tended to agree on which image was funnier, showing images 6 and 3 being rated funnier than others most times.

[Figure: Scatter plot of Modified ratings on the x-axis and Original ratings on the y-axis, with gray points and a dashed identity line.]

**Figure 3. Modifications rendered images less humorous.** Each point compares the rating of image pairs (y-axis: original, x-axis: modified pair; total 1,271 pairs; line = identity). For the majority of images (86.4%), the ratings for the original images were higher.

**Reliability between participants.** We assessed between-participant agreement for the comparison task through:

- Anchor Image Comparisons: There was high reliability when comparing results against anchor images (Fig.4)
- Comprehensive Pilot: There was strong agreement in all possible pairwise comparisons of 10 random images (different from anchor images) ($\binom{10}{2}$) pairs, Fig.2)

**Final Dataset**

Each image in our 3,542-image set received 6-8 ratings (Binary or Range tasks) or 4-6 comparisons. Of these, 1,771 images were labeled “funny” (mean binary rating ≥ 0.5). To ensure balance, we removed additional non-funny images with the highest rating variance. For training/validation/test splits, we ensured each set contained both original and modified versions of any given image pair to avoid biases. Table 1 summarizes the final dataset composition.

We conducted two separate evaluations: one on the entire test set (testAllSet) and the other on the subset of the test



<!-- page 0004 -->

[Figure: Bar chart showing percentage consistency by representative image used in comparison. Y-axis: “% rating 1 and rating 2 consistent”; x-axis: “Representative image used in comparison”; bars labeled 1–8.]

Figure 4. **Participants showed self-consistency in the Comparison task.** The x-axis shows the representative images, while the y-axis shows the percentage of instances where a user’s second rating matched their first for comparison containing the particular comparison image. A 100% match is perfect self-consistency.

[Figure: Bubble scatter plot of Rating 1 vs Rating 2 with dashed diagonal line; larger bubbles indicate more ratings/pair.]

Figure 5. **Participants showed high self-reliability (Range Ratings).** Higher ratings denote more humorous images. For each participant, 10 images were presented twice at random time points to assess reliability. There was a strong correlation ($\rho = 0.89$) between the first and second ratings (1,800 pairs; circle sizes indicate number of ratings/pair). The dashed line shows the diagonal.

set consisting of only the original/modified pairs of images in the test set (testOnlyPairs).

## 4. Experiments

### Models

We evaluated state-of-the-art visual architectures, including vision-only and vision-language models, using both pretrained and non-pretrained settings. We evaluated the following models: DINOv2 large [33], ViT huge [10], Swin2 large [26], ConvNeXt large [27], ViTG-14 [21, 37], ResNet152 [15], LLaVA (in zero-shot and fine-tuned configurations) [24, 25], BLIP (fine-tuned) [20], GPT-4o (gpt-4o-2024-05-13) [32], and Gemini 1.5-002 Flash [38]. Pre-trained vision models were initialized with weights from either ImageNet [35] or LAION-2B [36]. BLIP and LLaVA, use a combination of various datasets for training. GPT-4o and Gemini-Flash do not open-source their training data.

For vision-only models in the Binary and Range tasks, we added a final fully connected layer for predictions (funny/not funny and 1–10, respectively). For the Comparison task, we extracted features before the classification layer, computed the difference between the two images’ features, and passed the difference to a classifier for prediction.

For vision-language models, we framed our tasks as VQA problems. For the Binary task, the prompts were “Is the image funny?” and “Is the image not funny?”, averaging results as performance was comparable between the two. For the Range task, we asked “What is the degree of funniness of this image from 1 to 10?” For the Comparison task in zero-shot setting, we prompted: “Given these two images, answer which is funnier with ’first’ or ’second’ and explain why succinctly”. We confirmed that removing the word ”succinctly” did not significantly alter performance.

We also used the words participants used to describe funny images (Comparison task). We selected words common in at least 30% of the responses for each image. For fine-tuning, we modified the prompt by using a prefix: “The prominent features of this image are: common words”.

Each experiment was conducted 5 times for all models except for GPT-4o and Gemini-Flash, which were run only. Further training details are shown in Appendix Sec. 7.1.

### Tasks

**Binary Task.** We measured accuracy, comparing the predicted label (“funny” or “not funny”) against the average human-based label (threshold of 0.5). Chance was 50%. To assess control for editing artifacts and model learning beyond HumorDB, we also evaluated model performance on an external set of 650 non-humorous, non-edited images (MSCOCO[23]: 250, Places365[41]: 400).

**Range Task.** We computed the root mean square error (RMSE) between the predicted rating (1–10) and the mean human rating. Chance levels were estimated under two null hypotheses: (i) sampling random labels from the empirical distribution of funniness ratings in the dataset, (ii) sampling uniform random integers in 1–10 (for zero-shot models).

**Comparison Task.** Accuracy was computed as the fraction of pairs correctly identified as “A is funnier” or “B is funnier,” matching the majority human vote. Chance was 50%.

**Testing VLM Explanations** We conducted a human evaluation of VLM explanations Participants rated explanations on a 1–5 scale based on: (1) how well they identified why an image is funny, and (2) factual accuracy of scene. We also used an automated mechanism by checking the presence of word synonyms from human annotations using: (1) All Words Score - considering all annotator words, and (2) Common Words Score - focusing on words appearing in at least 30% of human responses. (see Appendix Sec. 8).

**Attention Maps** We analyzed attention maps in vision transformers using attention rollout [1]. We produced global attention maps over image tokens for test images. For paired images, we approximated the humorous region



<!-- page 0005 -->

| Dataset | Total | Pairs | Funny images N | Funny Binary | Funny Range | Not Funny N | Not Funny Binary | Not Funny Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Training | 2,136 | 698 | 1,068 | 0.79±0.18 | 5.75±1.42 | 1,068 | 0.12±0.16 | 3.62±1.75 |
| Valid. | 703 | 273 | 351 | 0.78±0.19 | 5.68±1.40 | 351 | 0.12±0.17 | 3.65±1.65 |
| testAll | 706 | 300 | 352 | 0.77±0.19 | 5.60±1.37 | 352 | 0.14±0.17 | 3.39±1.68 |
| testOnlyPairs | 600 | 300 | 300 | 0.77±0.19 | 5.62±1.36 | 300 | 0.13±0.16 | 3.30±1.68 |
| **Total** | **3,542** | **1,271** | **1,771** | **0.79±0.20** | **5.70±1.40** | **1,771** | **0.13±0.17** | **3.58±1.72** |

Table 1. Dataset summary. Images were labeled as humorous if the mean participant rating was ≥ 0.5. The dataset was balanced by removing non-funny images with the highest rating standard deviations. Splits (training, validation, test) contain both original and modified versions of each image to avoid bias. The table presents two test evaluations: testAllSet (entire test set) and testOnlyPairs (subset with original/modified pairs). Note: The Total excludes testOnlyPairs as it’s a subset of testAllSet.

[Figure: Two side-by-side bar charts with y-axis “Performance” and legend “pretrained” / “not pretrained”; dotted horizontal chance line near 50. X-axis labels include sNet150, xLarge, ViTlarge, ViTHuge, SwinV2Large, DinoV2Large, ViTG14, BLIPft, BLIPWordft, Llavashot, Llavaft, GPT4, LlavaWordft, GeminiFlash, Humans.]

Figure 6. **Binary task results for (a) `testAllSet` and (b) `testOnlyPairs`.** Dark grey bars represent pretrained models; light grey bars represent non-pretrained models. The dotted line indicates chance performance. The last column shows human performance. Error bars represent standard deviation. “ft” denotes fine tuning. “Wordft” denotes fine tuning and usage of word descriptors (see text for details).

using pixel-level differences between original and modified versions. We evaluated attention map quality using recall, strict box containment, and outside box ratio (Appendix Sec. 9).

**Mechanistic Interpretability** We adapted logit attribution to evaluate how each transformer layer contributed to humor detection. We treated each ViT block as a layer and measured classification accuracy using each layer’s predictions (Appendix Sec. 10).

## 5. Results

We evaluated models on three tasks: (1) Binary Classification, (2) Range Rating, and (3) Comparison, using both the full test set (`testAllSet`) and a subset containing only paired images (`testOnlyPairs`, e.g., Fig. 1).

**Binary Task.** As expected, pretrained models (dark bars) consistently outperformed non-pretrained models (light bars) both for `testAllSet` (Figure 6a) and `testOnlyPairs` (Figure 6b). The latter generally performed near chance, demonstrating the importance of pretraining priors. Performance dropped when evaluating only on paired images, emphasizing that such contrastive examples pose a more stringent test for visual tasks. Large vision-language models (e.g., Gemini-Flash, fine-tuned LLaVA) outperformed vision-only models, while zero-shot large multimodal LLMs also performed surprisingly well despite no *specific* humor training (though these models have likely been exposed to humorous content). Higher-capacity models maintained relatively stable performance from `testAllSet` to `testOnlyPairs`, whereas smaller models showed a bigger drop. Finally, vision-language models (LLaVA, BLIP [20]) trained with supporting words for a portion of the images further enhanced performance, indicating the value of human-guided training.

On the control set of not funny images from external datasets, models classified images as “not funny”: ViT-G14 (81%), LLaVA FT (80%), SwinV2 (76%), ViTHuge (71%), DinoV2 (62%). Thus, models are learning beyond superficial editing cues and showing learning beyond HumorDB.

**Range Task.** The strongest models achieved RMSE values around 1.7-2.0, significantly better than random baselines Table 3. Large language models performed reasonably well even in zero-shot settings, suggesting an inherent numeric humor scoring ability. Fine-tuned LLaVA variants (especially those trained with human keywords) performed best,



<!-- page 0006 -->

verifying the usefulness of targeted training.

**Comparison Task.** Choosing which of two images is funnier proved more challenging **(Fig. 9)**. Although performance exceeded chance levels (50%), it was notably lower than on the Binary task, highlighting the additional complexity of making nuanced judgments between similar images. Interestingly, models trained directly on comparison data outperformed larger zero-shot LLMs in this task.

**Performance Across Image Categories.** Performance varied markedly by image type (6). All models performed near chance on sketches, likely due to their abstract nature. Performance on photoshopped and AI-generated images was strongest, perhaps because these images share characteristics with the models’ training data.

**Importance of Minimally Contrastive Pairs.** When evaluated only on original images (excluding modified pairs), several models showed significant performance increases **(Fig. 7)**. GPT-4o exhibited a surprising 10% improvement, reinforcing the necessity of contrastive pairs for rigorous evaluation and suggesting potential exposure to similar internet images during training.

[Figure: Bar chart showing performance for pretrained and not pretrained models. Y-axis labeled “Performance” ranging from 40 to 100. Legend: pretrained, not pretrained. X-axis labels include AlexNetFL, ConvNextLarge, ViTLarge, CLIPLarge, SwinLarge, DeiTLarge, DINOv2Large, BLIPft, BLIPwordft, LlavaZeroShot, Llavaft, LlavaWordft, GPT4, GeminiFlash, Humans.]

Figure 7. **Binary task results evaluated only with original images in the testAllSet (i.e., excluding testing on modified images).** Format and conventions as in **Fig. 6**. Several models improve their performance on the original images, indicating that the modified images serve as an important control. GPT-4o shows a particularly surprising increase in performance suggesting that it probably has seen the original images from the internet in its training set.

**Explanation Quality. Explanation Quality.** Our human evaluation of VLM explanations revealed strong performance, particularly from larger models. On a 1–5 scale, Gemini’s explanations were rated highest for both identifying the source of humor (4.1 ± 0.6) and for overall accuracy (4.24 ± 0.47). GPT-4o also performed well (Why Funny: 3.9 ± 0.7, Accuracy: 4.12 ± 0.63), followed by LLaVA (Why Funny: 3.5 ± 0.9, Accuracy: 3.57 ± 0.95). These results suggest a robust, though not perfect, ability to articulate visual humor beyond simple keyword matching. Automated scores are detailed in Appendix 8.

**Qualitative Analysis. Fig. 8** shows examples of GPT-4o classification and explanations. The model sometimes labeled both paired images as funny, failing to grasp distinguishing elements (e.g., **Fig. 8g-h**). In some cases, the model provided eloquent explanations aligned with human reasoning while in others, it missed subtle but critical elements (e.g., **Fig. 8c-d**).

**Attention Maps and Mechanistic Interpretability.** SOTA Vision Transformers (ViTs) show limited ability to identify humorous regions in images. Across ViT variants, attention maps achieved modest recall (0.17–0.26) with the humorous regions, with ViTG-14 performing slightly better (0.27) and DINOv2-Large notably worse (0.006). Models generally struggled with precise attention containment. ViTG-14 led with 42% of its attention staying within the humor bounding box, followed by ViT-Huge (38%) and ViT-Large (31%). While DINOv2-Large showed higher containment (55%), this was misleading given its near-zero recall. All models exhibited similar ratios of attention spillage outside the target box (0.30–0.36), indicating consistent difficulty in focusing specifically on humorous elements.

The logit attribution analysis revealed distinct patterns in how different architectures process humor across their network depths **(Fig. 10)**. The ViTG-14, the largest model tested, showed the most dramatic improvement in humor detection capability through its layers, reaching peak accuracy of 70% in its final layers. This suggests that humor understanding in this model emerges gradually through successive transformations of the visual features. In contrast, DINOv2-Large exhibited early learning with rapid improvement in the first 20% of layers but plateaued around 58% accuracy, maintaining relatively consistent performance through deeper layers. ViT-Huge and ViT-Large showed similar patterns, with minimal learning in early layers (0-40%) followed by steady improvement. However, their performance peaked lower than ViT-G14, at around 62% and 57% respectively. Both models showed slight performance degradation in their final layers, suggesting possible overfitting or feature collapse at extreme depths.

Table 2. Attention Evaluation: Comparison of Selected Metrics  
(Recall, Strict Box Containment, Outside Box Ratio)

|  | Recall Mean | Recall Std | SBC Mean | SBC Std | OBR Mean | OBR Std |
|---|---:|---:|---:|---:|---:|---:|
| ViT-L | 0.240 | 0.268 | 0.308 | 0.465 | 0.350 | 0.401 |
| ViT-H | 0.170 | 0.250 | 0.378 | 0.487 | 0.355 | 0.420 |
| DINOv2 | 0.006 | 0.013 | 0.552 | 0.502 | 0.324 | 0.440 |
| ViTG-14 | 0.265 | 0.218 | 0.425 | 0.497 | 0.348 | 0.381 |

## Discussion

**Performance Gaps.** All models performed above chance levels in the Binary task but were below human accuracy despite fine-tuning. This gap was more pronounced in the



<!-- page 0007 -->

[Figure: eight example image pairs with LLM responses shown beneath each image: wing-cutting illustration, snowboarder/moon perspective, beach shadow illusion, and surgical cartoon.]

(a) LLM response: *no. this image appears to depict a somber or serious theme. The artistic representation of a person cutting another individual’s wings suggests a metaphor for limiting someone’s freedom or potential.* Range rating: 1

(b) LLM response: *no, the image is not funny. it appears to be a serious, thought-provoking illustration that likely carries a significant meaning or message. the imagery of a person putting a hood over a winged figure.* Range rating: 1

(c) LLM response: *yes. the image is funny because it shows a snowboarder appearing to step on the moon, playing with perspective to create a humorous and surreal visual effect.* Range rating: 7

(d) LLM response: *no. the image depicts someone who appears to be about to step off a ledge while holding a snowboard, which could be interpreted as potentially dangerous rather than funny.* Range rating: 1

(e) LLM response: *yes, the image can be considered funny due to the optical illusion created by the shadow on the beach, which makes it appear as though someone is flying on a magic carpet.* Range rating: 9

(f) LLM response: *yes. the image is funny due to the optical illusion caused by the shadow of the flagpole, which makes it appear as though there is a large figure casting a long shadow on the beach.* Range rating: 7

(g) LLM response: *yes, the image is funny. Explanation: The cartoon depicts a surgical operation where the surgeons, instead of using typical medical equipment, appear to be treating the patient as if they are preparing food.* Range rating: 8

(h) LLM response: *Yes. The humor comes from a surgeon theatrically throwing the patient’s internal organs like a basketball while another surgeon waits to catch them with a plate.* Range rating: 8

Figure 8. **Example GPT-4 binary classification, range ratings, and explanations.** The human binary and range ratings are as follows for the images: (a) 66%, 4.20, (b) 0%, 5.6, (c) 71%, 6.70, (d) 0%, 3.60, (e) 60%, 2.80, (f) 0%, 5.57, (g) 83%, 6.75, (h) 14%, 5.70

[Figure: bar chart comparing task performance on `testAllSet`; y-axis “Performance”; x-axis “Models” with labels ResNet50, ConvNeXt_Large, ViT_Large, ViT_Huge, SwinV2_Large, DiNov2_Large, ViTG14, GPT-4o, Gemini-Flash, Human; legend “Pretrained” and “Not Pretrained”; dotted horizontal line around 50.]

Figure 9. **Comparison task performance** on `testAllSet`. Pre-trained models still trail far behind humans.

[Figure: line chart of layerwise binary classification results; y-axis “Accuracy”; x-axis “Layer (%)”; legend DINOv2Large, ViTHuge, ViTLarge, ViTG14.]

Figure 10. **Layerwise binary classification results**

Comparison task, underscoring the nuanced visual reasoning required for humor. Interestingly, in the Range task, some models achieved performance comparable to humans.

**Value of Contrastive Pairs.** The minimally contrastive pairs proved crucial for exposing model limitations. Performance consistently dropped on such pairs, revealing that many models rely on superficial cues rather than identifying precise humor-inducing elements. Notably, when evaluated only on original images, several models (particularly GPT-4o) showed significant performance increases, suggesting



<!-- page 0008 -->

| Model Name | testAllSet RMSE $\pm SD$ | testOnlyPairs RMSE $\pm SD$ |
|---|---:|---:|
| dinov2 large | $1.98 \pm 0.08$ | $1.96 \pm 0.09$ |
| vit huge | $1.88 \pm 0.09$ | $1.92 \pm 0.07$ |
| swin2 large | $1.96 \pm 0.12$ | $1.98 \pm 0.11$ |
| convnext large | $2.10 \pm 0.06$ | $2.15 \pm 0.07$ |
| vitg 14 | $1.76 \pm 0.08$ | $1.80 \pm 0.06$ |
| resnet152 | $2.11 \pm 0.09$ | $2.09 \pm 0.11$ |
| LLaVA(Zero-Shot) | $2.95 \pm 0.33$ | $2.98 \pm 0.34$ |
| LLaVA(fine-tuned) | $1.70 \pm 0.22$ | $1.69 \pm 0.22$ |
| LLaVA(words fine-tuned) | **$1.68 \pm 0.28$** | **$1.66 \pm 0.31$** |
| BLIP (fine-tuned) | $1.94 \pm 0.05$ | $1.96 \pm 0.05$ |
| BLIP (words fine-tuned) | $1.92 \pm 0.06$ | $1.95 \pm 0.04$ |
| GPT-4o(Zero-Shot) | $2.61$ | $2.63$ |
| Gemini-Flash | $2.06$ | $2.11$ |
| Humans | $2.72 \pm 0.88$ | $2.71 \pm 0.86$ |
| Chance(from distribution) | $2.69 \pm 0.05$ | $2.50 \pm 0.06$ |
| Chance(for zero-shot) | $3.58 \pm 0.07$ | $3.33 \pm 0.07$ |

Table 3. Range Task Results on testAllSet and testOnlyPairs. Bold indicates the best model result. The chance(from distribution) scores are calculated by random sampling from the distribution of ratings in the dataset after rounding the mean range ratings to the nearest integer. The chance(zero-shot) scores are calculated after randomly sampling an integer from 1 to 10.

potential familiarity with internet-sourced funny images.

**Image Type Variation.** Performance varied across categories: models handled photoshopped and AI-generated content better but struggled with sketches, highlighting how abstraction challenges humor recognition.

**Large Model Advantages.** Large vision-language models achieved higher accuracy than vision-only models, suggesting broad pretraining aids in detecting humor-related cues. Zero-shot large multimodal LLMs (GPT-4o, Gemini-Flash) displayed promising capabilities, though they still made systematic errors on challenging examples and showed inconsistencies in explanations.

**Understanding vs. Classification.** While models often classified images correctly, deeper analyses revealed limitations. Attention maps showed that even when models were correct, they rarely focused precisely on the humorous regions. Model explanations sometimes aligned with human annotations but often hallucinated reasons or highlighted irrelevant details, particularly for contrastive pairs. This disconnect between classification and “understanding” highlights the ongoing challenge in grounding visual-linguistic representations in genuinely human-like reasoning.

**Limitations.** Our dataset is comparable to established benchmarks in terms of #images per class, but it is conceivable, even likely, that more data would improve performance. Substantially enlarging **HumorDB** would introduce logistical hurdles, such as additional image modifications, curation, and participant annotations. Moreover, humor is highly culture-dependent; thus, achieving a fully global perspective would necessitate broader sampling across numerous cultural contexts and humor styles. We expect that the observed gap in model performance—especially in the Binary and Comparison tasks—is driven less by data quantity than by the inherent challenges in abstract visual reasoning required for humor. Evidence of this limitation appears in **Fig. 8** and Appendix Sec. 7.3, where GPT-4o explanations and ViT-Huge attention maps fail to highlight critical incongruities (e.g., overlooking the cell phone in **Fig. 1**). Such omissions emphasize the difficulty of pinpointing subtle yet crucial cues that distinguish “funny” from “not funny.”

Furthermore, while our participant pool was diverse (see Appendix 7.6), it was predominantly from the United States (54%) and younger demographics (<40 years). As humor is culture-dependent, future work could improve upon the work by considering a stratified demographic group.

Using **HumorDB** as a zero-shot benchmark for large multimodal models could shed light on how these models generalize to complex, abstract tasks like humor. Our dataset construction methodology including *minimally-contrastive* pairs may also benefit other domains to isolate subtle semantic changes. As the field moves from labeling individual objects to more nuanced scene interpretation, accounting for human variation becomes crucial (e.g., one viewer’s “funny” might be another’s “not funny”). Although **HumorDB** focuses on majority votes and average ratings, future expansions could gather per-user data and probe the subjective core of humor. Such refinements would deepen our grasp of subjective labeling, cultural dependencies, and the abstract reasoning that still eludes current AI systems (see also AppendixSec. 11).



<!-- page 0009 -->

## 6. Acknowledgements

The authors would like to thank Morgan Talbot and Spandan Madan for their help with the GPU cluster and running experiments, the members of Kreiman Lab for the In-Lab study and weekly discussions.

This research was supported by the Illinois Computes project at the University of Illinois Urbana-Champaign (JV), NIH Grant R01EY026025 (GK), and the Center for Brains, Minds and Machines at Harvard/MIT (GK).

## References

[1] Samira Abnar and Willem Zuidema. Quantifying attention flow in transformers, 2020. 4, 1, 3

[2] Jason Ansel, Edward Yang, Horace He, Natalia Gimelshein, Animesh Jain, Michael Voznesensky, Bin Bao, Peter Bell, David Berard, Evgeni Burovski, Geeta Chauhan, Anjali Chourdia, Will Constable, Alban Desmaison, Zachary DeVito, Elias Ellison, Will Feng, Jiong Gong, Michael Gschwind, Brian Hirsh, Sherlock Huang, Kshiteej Kalambarkar, Laurent Kirsch, Michael Lazos, Mario Lezcano, Yanbo Liang, Jason Liang, Yinghai Lu, C. K. Luk, Bert Maher, Yunjie Pan, Christian Puhrsch, Matthias Reso, Mark Saroufim, Marcos Yukio Siraichi, Helen Suk, Shunting Zhang, Michael Suo, Phil Tillet, Xu Zhao, Eikan Wang, Keren Zhou, Richard Zou, Xiaodong Wang, Ajit Mathews, William Wen, Gregory Chanan, Peng Wu, and Soumith Chintala. Pytorch 2: Faster machine learning through dynamic python bytecode transformation and graph compilation. page 929–947, New York, NY, USA, 2024. Association for Computing Machinery. 1

[3] Salvatore Attardo. 57 Theories of humor and their levels. In *The Linguistics of Humor: An Introduction*. Oxford University Press, 2020. 2

[4] Simge Aykan and Erhan Nalçacı. Assessing theory of mind by humor: The humor comprehension and appreciation test (tom-hcat). *Frontiers in Psychology*, 9, 2018. 1

[5] Dario Bertero and Pascale Fung. Deep learning of audio and language features for humor prediction. In *Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC’16)*, pages 496–501, Portorož, Slovenia, 2016. European Language Resources Association (ELRA). 2

[6] Arjun Chandrasekaran, Ashwin K. Vijayakumar, Stanislaw Antol, Mohit Bansal, Dhruv Batra, C. Lawrence Zitnick, and Devi Parikh. We are humor beings: Understanding and predicting visual humor. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016. 2

[7] Dushyant Singh Chauhan, Gopendra Vikram Singh, Navonil Majumder, Amir Zadeh, Asif Ekbal, Pushpak Bhattacharyya, Louis philippe Morency, and Soujanya Poria. M2h2: A multimodal multiparty hindi dataset for humor recognition in conversations, 2021. 2

[8] Lei Chen and Chong Min Lee. Predicting audience’s laughter during presentations using convolutional neural network. In *Proceedings of the 12th Workshop on Innovative Use of NLP for Building Educational Applications*, pages 86–90, Copenhagen, Denmark, 2017. Association for Computational Linguistics. 2

[9] Peng-Yu Chen and Von-Wun Soo. Humor recognition using deep learning. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*, pages 113–117, New Orleans, Louisiana, 2018. Association for Computational Linguistics. 2

[10] Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin, Rodolphe Jenatton, Lucas Beyer, Michael Tschannen, Anurag Arnab, Xiao Wang, Carlos Riquelme, Matthias Minderer, Joan Puigcerver, Utku Evci, Manoj Kumar, Sjoerd van Steenkiste, Gamaleldin F. Elsayed, Aravindh Mahendran, Fisher Yu, Avital Oliver, Fantine Huot, Jasmijn Bastings, Mark Patrick Collier, Alexey Gritsenko, Vighnesh Birodkar, Cristina Vasconcelos, Yi Tay, Thomas Mensink, Alexander Kolesnikov, Filip Pavetić, Dustin Tran, Thomas Kipf, Mario Lučić, Xiaohua Zhai, Daniel Keysers, Jeremiah Harmsen, and Neil Houlsby. Scaling vision transformers to 22 billion parameters, 2023. 2, 4, 1

[11] Stephanie Fu, Netanel Tamir, Shobhita Sundaram, Lucy Chai, Richard Zhang, Tali Dekel, and Phillip Isola. Dreamsim: Learning new dimensions of human visual similarity using synthetic data, 2023. 3

[12] Sylvain Gugger, Lysandre Debut, Thomas Wolf, Philipp Schmid, Zachary Mueller, Sourab Mangrulkar, Marc Sun, and Benjamin Bossan. Accelerate: Training and inference at scale made simple, efficient and adaptable. https://github.com/huggingface/accelerate, 2022. 1

[13] Md Kamrul Hasan, Wasifur Rahman, AmirAli Bagher Zadeh, Jianyuan Zhong, Md Iftekhar Tanveer, Louis-Philippe Morency, and Mohammed (Ehsan) Hoque. UR-FUNNY: A multimodal language dataset for understanding humor. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).* Association for Computational Linguistics, 2019. 2

[14] Md Kamrul Hasan, Sangwu Lee, Wasifur Rahman, Amir Zadeh, Rada Mihalcea, Louis-Philippe Morency, and Ehsan Hoque. Humor knowledge enriched transformer for understanding multimodal humor. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(14):12972–12980, 2021. 2

[15] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition, 2015. 2, 4

[16] Jack Hessel, Ana Marasović, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, and Yejin Choi. Do androids laugh at electric sheep? humor ”understanding” benchmarks from the new yorker caption contest, 2023. 2

[17] Vincent Jacquot, Zhuofan Ying, and Gabriel Kreiman. Can deep learning recognize subtle human activities? In Pro-



<!-- page 0010 -->

*ceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020. 2

[18] Yuta Kayatani, Zekun Yang, Mayu Otani, Noa Garcia, Chen-hui Chu, Yuta Nakashima, and Haruo Takemura. The laughing machine: Predicting humor in video. In *2021 IEEE Winter Conference on Applications of Computer Vision (WACV)*, pages 2072–2081, 2021. 2

[19] Da Li, Rafal Rzepka, Michal Ptaszynski, and Kenji Araki. Hemos: A novel deep learning-based fine-grained humor detecting method for sentiment analysis of social media. *Information Processing & Management*, 57(6):102290, 2020. 2

[20] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation, 2022. 2, 4, 5

[21] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models, 2023. 4

[22] Runjia Li, Shuyang Sun, Mohamed Elhoseiny, and Philip Torr. Oxfordtvg-hic: Can machine make humorous captions from images?, 2023. 2

[23] Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva Ramanan, C. Lawrence Zitnick, and Piotr Dollár. Microsoft coco: Common objects in context, 2015. 4

[24] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023. 2, 4, 1

[25] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023. 2, 4, 1

[26] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie, Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, Furu Wei, and Baining Guo. Swin transformer v2: Scaling up capacity and resolution, 2022. 4

[27] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feichtenhofer, Trevor Darrell, and Saining Xie. A convnet for the 2020s, 2022. 2, 4

[28] Zhi-Song Liu, Robin Courant, and Vicky Kalogeiton. Funnynet: Audiovisual learning of funny moments in videos. In *Computer Vision – ACCV 2022*, pages 433–450, Cham, 2023. Springer Nature Switzerland. 2

[29] Midjourney Inc. Midjourney. https://www.midjourney.com/, 2023. 2

[30] Rada Mihalcea and Carlo Strapparava. Making computers laugh: Investigations in automatic humor recognition. In *Proceedings of Human Language Technology Conference and Conference on Empirical Methods in Natural Language Processing*, pages 531–538, Vancouver, British Columbia, Canada, 2005. Association for Computational Linguistics. 2

[31] OpenAI. Dall·e 2. https://openai.com/dall-e-2/, 2023. 2

[32] OpenAI. Gpt-4 technical report, 2023. 2, 4

[33] Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr Bojanowski. Dinov2: Learning robust visual features without supervision, 2023. 2, 4

[34] Badri N. Patro, Mayank Lunayach, Deepankar Srivastava, Sarvesh Sarvesh, Hunar Singh, and Vinay P. Namboodiri. Multimodal humor dataset: Predicting laughter tracks for sitcoms. In *2021 IEEE Winter Conference on Applications of Computer Vision (WACV)*, pages 576–585, 2021. 2

[35] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei. Imagenet large scale visual recognition challenge, 2015. 4

[36] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine Crowson, Ludwig Schmidt, Robert Kaczmarczyk, and Jenia Jitsev. Laion-5b: An open large-scale dataset for training next generation image-text models, 2022. 4

[37] Quan Sun, Yuxin Fang, Ledell Wu, Xinlong Wang, and Yue Cao. Eva-clip: Improved training techniques for clip at scale, 2023. 4

[38] Gemini Team and et al. Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, 2024. 2, 4

[39] Thomas Winters and Pieter Delobelle. Dutch humor detection by generating negative examples, 2020. 2

[40] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. Huggingface’s transformers: State-of-the-art natural language processing, 2020. 1

[41] Bolei Zhou, Agata Lapedriza, Aditya Khosla, Aude Oliva, and Antonio Torralba. Places: A 10 million image database for scene recognition. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 40(6):1452–1464, 2018. 4



<!-- page 0011 -->

# HumorDB: Can AI understand graphical humor?

## Supplementary Material

## 7. Appendix

### 7.1. Training details

Models were trained using the Adam optimization algorithm with weight decay. We conducted a hyperparameter grid search across learning rates in the set 0.01, 0.001, 0.0001, 0.00001, batch sizes in the set 4, 8, 16, and weight decay parameters in the set 0.1, 0.01, 0.001. Model training proceeded for a fixed number of 10 epochs, with periodic checkpoints. For the final evaluation on the unseen test set, we used the model iteration exhibiting optimal performance on the validation set. We used cross-entropy loss for the Binary classification and Comparison tasks, while mean square loss was used for the Regression task. For all architectures except GPT-4o and Gemini-Flash, we fine-tuned the models. For LLaVA, we performed LoRA finetuning instead of full fine-tuning. Due to the uneven distribution of range ratings, we employed a sampling strategy that grouped images into bins according to their funniness ratings. This allowed us to randomly select a balanced number of images from each bin for every training epoch, ensuring a uniform distribution of sample images across all ratings in the training set. We applied the same sampling strategy for the Comparison task, which also contained a slightly uneven distribution.

Models were trained using the Adam optimization algorithm with weight decay. A hyperparameter grid search was conducted across learning rates in the set {0.01, 0.001, 0.0001, 0.00001}, batch sizes in the set {4, 8, 16}, and weight decay parameters in the set {0.1, 0.01, 0.001}. Model training proceeded for a fixed number of 10 epochs, with periodic checkpoints. For the final evaluation on the unseen test set, we used the model iteration exhibiting optimal performance on the validation cohort. We used cross-entropy loss for the Binary classification and Comparison tasks while mean square loss was used for the Regression task. For all architectures except GPT-4o and Gemini-Flash, we fine-tuned the models(Pretraining details are mentioned in Section 4.1). For LlaVA we did lora fine-tuning instead of full fine-tuning. To ensure statistical robustness, each experiment was conducted 5 times for all the experiments except for GPT-4o and Gemini-Flash which were run only one time.

Most of the experiments were run on 4 Nvidia GeForce RTX 2080 Ti GPUs which were part of an internal cluster. However, for training LLaVA and some models for the Comparison task, we used an Nvidia A100 GPU.

### 7.2. External assets used

We utilized the following assets: The LLaVA repository (Apache-2.0 license) [24, 25], PyTorch [2], huggingface transformers (Apache-2.0 license) [40], and huggingface accelerate (Apache-2.0 license) [12].

Additionally, for the images collected from the internet, we provide reference links in the repository.

### 7.3. Attention maps

We examined the attention maps using the attention rollout technique [1] on the ViT-Huge model [10]. This helped us understand whether the models focused on the actual humorous parts of images or other biases in the dataset. The attention maps may help to better understand how the models classify the images and identify potential shortcomings (Fig. 11).

As an example, consider the case of Fig. 1. The attention maps for the vit huge model are shown in Fig.11. The model fails to pay attention to the most humorous part of the image (the phone, black rectangle), which is critical to assess whether the image is funny or not. Therefore the model is not able to correctly classify both images.

### 7.4. Crowdsourcing details

There were 850 participants: 200 for binary task, 215 for the range task and 435 for the comparison task. The interfaces used by the participants for the three tasks are shown in Fig. 12. The generic instructions given for all tasks were:

- **Binary Task:** Please rate if the image is funny or not.
- **Range Task:** Please rate the degree of funniness of the image on a scale from 1 (not funny) to 10 (very funny).
- **Comparison Task:** Please indicate which of the two images is funnier.
- For funny images write a word that makes the image funny, for not funny images, write a word about the most prominent feature of the image.
- The time required to rate all the images is approximately 9-11 minutes
- Only click on the rating buttons once, and wait till the next image loads (maximum 1 second), a message will show you when the next image is being processed.
- Please do not refresh the page. You will lose progress and will have to start again.
- There are 100-120 images in this survey.
- At the end of the survey, we will provide you a code, please store it and use it appropriately to get the reward.
- Click the button below to begin.

Some participants were discarded due to reliability and



<!-- page 0012 -->

[Figure: Four-panel figure showing an “Original image” and “Modified image” of an operating-room cartoon on the left, and corresponding heatmaps labeled “Attention map, last layer vitg” on the right. The heatmaps include a black rectangle marking an object location and a vertical color scale.]

Figure 11. **Attention maps fail to capture elements critical to discern humor.** Attention maps based on the last layer of the vit huge model for the example images from Fig. 1. The black rectangle in the attention maps indicates the location of the phone. The maximum attention activation highlights the plate, which does not help distinguish between the original and modified images. Indeed, the model classified both images as funny.

[Figure: Three crowdsourcing interface screenshots. (a) A binary task interface showing an image, “Continue,” the question “Is the Image funny?”, and buttons “Funny” and “Not Funny.” (b) A range task interface showing an image, “Continue,” the question “How funny is the image?”, and a 1–10 scale from “Not Funny” to “Very Funny.” (c) A compare task interface showing two images, “Continue,” the question “Which image is funnier?”, and buttons “Image 1” and “Image 2.”]

(a) Binary Task Interface

(b) Range Task Interface

(c) Compare Task Interface

Figure 12. **Crowd sourcing interfaces for the three tasks.**

the amount of outliers in their responses as detailed in Section3.2. All participants were required to submit all questions in the survey for the response to count.

### 7.5. Multimodal models’ answer explanations

For evaluating zero-shot performance of the large multimodal models we test them on testAllSet and testAllPairs sets. We do this to compare the performance of these models with the other fine tuned models on the same test set. The two variants of prompts in binary task as mentioned in section 4.1 were: : (i) “Is the image funny?”, and (ii) “Is the image not funny?”. The performance on both prompts were similar so we reported the average for the results. In addition for succinct explanations in a particular format for the figures like Fig. 8, we add a suffix ’start answer with yes/no then explain’. In this section we present similar figures to Fig. 8 for Gemini-Flash and LlaVA on zero-shot prompting. We also mention the range ratings these models give for the images and the range rating prompt is mentioned in section 4.1. Gemini-Flash answer explanations are presented in Fig. 13. The answer explanation from LlaVA zero-shot are presented in Fig. 14.



<!-- page 0013 -->

[Figure: Eight example images with LLM responses and range ratings. (a) Cartoon operating room with surgeons and patient; (b) similar cartoon operating room; (c) illustration of two women on couch with shadow like snakes; (d) illustration of two people on couch; (e) beach scene with person speaking; (f) beach scene; (g) dog wearing sunglasses with coconut drink; (h) child sleeping on beach.]

(a) LLM response: yes. the humor lies in the fact that the patient’s hand is being operated on with a smartphone. Range rating: 7

(b) LLM response: yes. the patient’s hand is detached from their body. Range rating: 8

(c) LLM response: yes. the shadow of the women looks like two snakes, it is a dark and ironic humor. Range rating: 7

(d) LLM response: no. the image is not inherently funny. it depicts two people sitting on a couch, and there’s no clear comedic element. Range rating: 3

(e) LLM response: no. it’s a standard photo of a person speaking. there is nothing humorous. Range rating: 2

(f) LLM response: no. it is a picture of a beach with some people on it. Range rating: 1

(g) LLM response: yes. the dog is wearing sunglasses and enjoying a coconut drink. Range rating: 8

(h) LLM response: no. the image is of a child sleeping. there is no humor in the image. Range rating: 2

Figure 13. **Example Gemini-Flash binary classification, range ratings, and explanations.** The human binary and range ratings are as follows for the images: (a) *83%, 6.75*, (b) *14%, 5.70*, (c) *60%, 3.60*, (d) *33%, 3.00*, (e) *60%, 2.80*, (f) *0%, 5.57*, (g) *100%, 5.60*, (h) *33%, 4.86*.

## 7.6. Participants’ Demographics

The demographics of the participants are described in the table Tab. 4.

# 8. Scoring for VLM explanation evaluation

The scoring process for all words and common words scores involved:

- Stemming words from human and VLM explanations using the spacy library.
- Matching synonyms using the nltk library.
- Marking an explanation as satisfactory if any stemmed word synonym from human raters is contained in the model explanation.

## 8.1. Results for automated VLM explanation evaluation

VLM explanations for correctly classified funny images showed varying alignment with human annotations (Table 5). Gemini provided the most accurate explanations (87.6% All Words Score, 74% Common Words Score), followed by GPT-4o and LLaVA.

# 9. Attention Map Evaluation

To gain insight into what regions of an image the model relies on to infer humor, we analyzed attention maps in vision transformer models [1]. Specifically, we examined the attention on images from the test set. We used an *attention rollout* technique that iteratively multiplies the raw attention matrices (augmented by the identity matrix to include residual connections), producing a global attention map over image tokens. We then reshaped this map into a 2D image by mapping each token to its position in the image grid and upsampling it to the original resolution. Attention Rollout does not work for SwinV2 because of its hierarchical attention architecture.

After computing the final attention map, we optionally convert this attention to a *segmentation-like* mask. We smooth the attention map, detect local peaks, and ex-



<!-- page 0014 -->

[Figure: composite of eight subfigures showing humorous/non-humorous images with LLaVA responses and range ratings.]

(a) LLM response: Yes. The humor comes from the juxtaposition of a serious medical situation with the casual and nonchalant behavior of the doctors, who seem more interested in using their phones than focusing on the patient. Range rating: 6

(b) LLM response: Yes, the image is intended to be humorous. It depicts a cartoon of a patient in a hospital bed with two doctors, one holding a tray of food and the other holding a tray of surgical instruments, both seemingly confused about which tray to use. Range rating: 6

(c) LLM response: Yes, the image is funny. It depicts two people sitting on a couch, seemingly engaged in a conversation, but the shadow on the wall behind them forms a shape that looks like a snake eating its own tail. Range rating: 5

(d) LLM response: Yes, the image is funny. It depicts two people sitting on a couch, but their bodies are mirrored, with their heads on the wrong sides of their bodies, creating a humorous and surreal visual effect. Range rating: 6

(e) LLM response: Yes, the image is funny. It depicts a cartoon of a person inside a box, seemingly being ”pulled out” by a hand using a toothpick. The humor comes from the absurdity and unexpectedness of the situation. Range rating: 6

(f) LLM response: Yes, the image is funny because it shows a hand pushing a button on a box that is labeled ”Emergency Button,” but instead of a typical emergency response, the box is filled with a bunch of pencils, which is an unexpected and humorous outcome. Range rating: 5

(g) LLM response:Yes, the image is funny because it shows a car with a large inflatable pool toy, specifically a white inflatable animal, strapped to its roof. This is an unusual and humorous sight because it’s not common to see such a large and whimsical item being transported in this manner. Range rating: 7

(h) LLM response: No. The image shows a car parked in a snowy environment, which is a common sight during winter. There is nothing inherently funny about the image; it appears to be a typical winter scene. Range rating: 2

Figure 14. **Example LLaVA binary classification, range ratings, and explanations.** The human binary and range ratings are as follows for the images: (a) 83%, 6.75, (b) 14%, 5.70, (c) 60%, 3.60, (d) 33%, 3.00, (e) 60%, 2.80, (f) 0%, 3.00, (g) 50%, 5.25, (h) 0%, 1.00.

pand those peaks into connected blobs whose intensities exceed a fraction of the peak value. This yields “peak-centered blobs,” each one capturing a region of high attention. Specifically:

**Peak-Centered Blob Detection.** We developed a systematic approach to identify and analyze significant attention regions:

1. Applied Gaussian smoothing ($\sigma=2.0$) to reduce noise in attention maps
2. Detected local maxima using peak_local_max with rela-



<!-- page 0015 -->

| Demographic Category | Percentage |
|---|---:|
| **Age** | |
| 20-29 | 47.0% |
| 30-39 | 30.3% |
| 40-49 | 13.8% |
| 50-59 | 5.2% |
| 0-19 | 2.1% |
| 60-69 | 1.6% |
| **Education** | |
| Undergraduate | 56.3% |
| Postgraduate | 29.5% |
| High School | 14.2% |
| **Gender** | |
| Male | 52.6% |
| Female | 46.6% |
| Non-binary | 0.8% |
| **Nationality** | |
| United States | 54.0% |
| South Africa | 9.0% |
| Other (41 total) | 37.0% |

Table 4. Demographic Data

| Model | All Words Score | Common Words Score |
|---|---:|---:|
| Gemini | 0.876 | 0.74 |
| GPT4o | 0.840 | 0.724 |
| LLaVA | 0.74 | 0.50 |

Table 5. VLM explanation accuracy compared to humans annotations

tive threshold 0.5

3. Generated connected components around peaks using intensity-based thresholding  
4. Filtered small regions (<50 pixels) to focus on significant attention areas

Since our dataset contains minimally contrastive pairs, one can also approximate the “true” humorous region by taking the pixel-level difference between the original (funny) and modified (not funny) image in each pair.

**Difference Map Generation.** For paired images (funny/not-funny versions), we:

1. Computed pixel-wise differences across RGB channels  
2. Applied Gaussian smoothing ($\sigma=1.0$) to the difference map  
3. Identified connected components with significant differences (threshold > 0.1)  
4. Generated binary masks highlighting modified regions

**Evaluation Metrics.** We evaluated attention map quality using three primary metrics:

- Recall: Proportion of ground truth funny regions captured by attention
- Strict Box Containment: Binary measure of whether attention stays within ground truth regions
- Outside Box Ratio: Proportion of attention allocated outside ground truth regions

We could only do this for the ViT and DinoV2 models as attention rollout cannot be directly be applied to SwinV2 type models which is the only other vision only transformer.

## 10. Logit Attribution Details

Transformer-based NLP models can be probed using *logit attribution* to evaluate how each layer’s hidden state contributes to the final output. Here, we adapt the same concept to our ViT-based model, treating each ViT block (and the final classifier) as a “layer.”

**Layer-wise Analysis.** For each layer in the transformer models (ViTs and DINOv2):

1. Extracted hidden states from each transformer layer  
2. Applied the classification head to each layer’s output regarding that layer as the ”last layer” before layernorm and classification head.  
3. Computed softmax probabilities for binary humor classification  
4. Measured classification accuracy using each layer’s predictions

## 11. Future Directions.

Beyond expanding the cultural breadth of **HumorDB**, we envision several promising research avenues:

- **Interpreting Vision Models.** Recent progress in interpreting transformer-based language models can inform the study of multimodal and vision-only architectures. HumorDB’s carefully constructed minimal pairs provide an ideal testbed for *mechanistic interpretability* in vision, offering the kinds of subtle input differences that are otherwise hard to curate for images.
- **Expanded Evaluation Metrics.** Novel benchmarks could explore multi-modal inputs (e.g., text, video, audio) to capture richer humor contexts. This would help evaluate how well models integrate multiple information streams to detect incongruities or comedic timing.
- **Personalized Humor.** Because individual comedic tastes vary, it would be valuable to test models on how well they adapt to personal preferences. Such personalization could move beyond majority voting to reflect diverse humor perceptions.
- **Cultural and Linguistic Diversity.** Truly universal humor comprehension requires sampling across diverse cultural and linguistic backgrounds. Curating a broader spectrum of comedic tropes—slapstick, satire, wordplay,



<!-- page 0016 -->

and so on—will challenge models to generalize beyond Western-centric contexts.

## 12. In-Lab Validation of Crowdsourced Data

To validate our primary crowdsourced annotations, we conducted a separate in-lab (non-crowdsourced) study. Participants provided ratings for 400 images, yielding $\geq 5$ ratings per image. We found high correlation between the in-lab and online data for both the binary task ($\rho = 0.78$) and the range task ($\rho = 0.72$), which reinforces the reliability of our HumorDB.

## 13. Image categories results

The results of models on various image categories are described in Tab. 6.



<!-- page 0017 -->

| Model Name | Photos | Photoshopped | Sketches | Cartoons | AI-Gen |
|---|---|---|---|---|---|
| dinov2 large | 59 ± 3 | 60 ± 1 | 47 ± 1 | 59 ± 2 | 51 ± 2 |
| vit huge | 64 ± 3 | 61 ± 2 | 48 ± 2 | 62 ± 2 | 52 ± 2 |
| vit large | 58 ± 2 | 58 ± 2 | 47 ± 1 | 59 ± 2 | 51 ± 2 |
| swin2 large | 61 ± 2 | 60 ± 2 | 47 ± 1 | 60 ± 2 | 52 ± 2 |
| convnext large | 57 ± 2 | 57 ± 1 | 46 ± 1 | 57 ± 2 | 50 ± 0 |
| vitg 14 | 72 ± 3 | 70 ± 3 | 51 ± 2 | 68 ± 3 | 53 ± 2 |
| resnet152 | 56 ± 1 | 55 ± 2 | 46 ± 1 | 56 ± 2 | 50 ± 1 |
| LLaVA (Zero-Shot) | 63 ± 5 | 66 ± 4 | 46 ± 1 | 52 ± 2 | 66 ± 3 |
| LLaVA (fine-tuned) | 72 ± 2 | 76 ± 2 | 54 ± 2 | 65 ± 2 | 69 ± 3 |
| LLaVA (words fine-tuned) | 79 ± 2 | 83 ± 1 | 54 ± 1 | 69 ± 2 | 73 ± 1 |
| BLIP (fine-tuned) | 59 ± 1 | 59 ± 2 | 48 ± 1 | 59 ± 2 | 52 ± 2 |
| BLIP (words fine-tuned) | 63 ± 2 | 66 ± 2 | 49 ± 1 | 61 ± 2 | 55 ± 1 |
| GPT-4o (Zero-Shot) | 75 | 69 | 50 | 58 | 76 |
| Gemini-Flash | 73 | 84 | 53 | 74 | 82 |

Table 6. Binary Classification Results on various image types present in the dataset.
