<!-- Transcribed from 55-jokes-or-gibberish.pdf -->



<!-- page 0001 -->

*digital*                                  MDPI

*Article*

# Jokes or Gibberish? Humor Retention in Translation with Neural Machine Translation vs. Large Language Model

**Mondheera Pituxcoosuvarn * and Yohei Murakami**

College of Information Science and Engineering, Ritsumeikan University, Ibaraki, Osaka 567-8570, Japan;  
yohei@fc.ritsumei.ac.jp  
\* Correspondence: mond-p@fc.ritsumei.ac.jp

## Abstract

Humor translation remains a significant challenge due to its reliance on wordplay, cultural context, and nuance. This study compares a Neural Machine Translation (NMT) system (hereafter referred to as MT) with a Large Language Model (GPT-based translation using three different prompts) for translating jokes from English to Thai. Results show that GPT-based models significantly outperform MT in humor retention, with the explanation-enhanced prompt (GPT-Ex) achieving the highest joke preservation rate (62.94%) compared to 50.12% in MT. Additionally, humor loss was more frequent in MT, while GPT-based models, particularly GPT-Ex, better retained jokes. A McNemar test confirmed significant differences in annotation distributions across models. Beyond evaluation, we propose using GPT-based models with optimized prompt engineering to enhance humor translation. Our refined prompts improved joke retention by guiding the model’s understanding of humor and cultural nuances.

**Keywords:** humor translation; neural machine translation; large language models application

[Figure: “check for updates” icon]

Academic Editor: Jorge Bernardino

Received: 5 August 2025  
Revised: 17 September 2025  
Accepted: 29 September 2025  
Published: 2 October 2025

**Citation:** Pituxcoosuvarn, M.; Murakami, Y. Jokes or Gibberish? Humor Retention in Translation with Neural Machine Translation vs. Large Language Model. *Digital* **2025**, *5*, 49. https://doi.org/10.3390/digital5040049

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

Humor is a vital aspect of human communication, serving as a tool for social bonding, cultural identity, and cognitive engagement. Yet, its translation remains notoriously difficult due to its dependence on linguistic subtleties, cultural references, and pragmatic cues [1–3]. Humor often fails to be preserved across languages, particularly when relying on automated systems, since the comedic effect is closely tied to context and culture.

Among the many challenges, idioms and culturally embedded expressions stand out as particularly problematic. Idioms often encode unique perspectives and thought patterns, making their accurate translation crucial for maintaining the intended humorous effect [4]. Similar issues extend to other humor forms, such as stand-up comedy, which is widely considered a fundamental and universal medium of humorous expression [5].

Although advances in machine translation (MT) have improved fluency and coherence, they continue to fall short when tasked with humor, frequently producing literal renderings that miss the intended comedic impact [6,7]. Large Language Models (LLMs), such as GPT, offer new possibilities by demonstrating greater contextual awareness and adaptability. Recent studies suggest that Artificial Intelligence (AI)-generated translations can, in some cases, provide an equivalent or even superior viewer experience compared to human translations for dubbing purposes [8]. However, these findings also underscore the need to refine algorithms and to consider hybrid human–AI approaches to better handle humor’s complexities.



<!-- page 0002 -->

Standard machine translation (MT) and LLM benchmarks already demonstrate strong performance on general translation quality (e.g., Bilingual Evaluation Understudy (BLEU) and Crosslingual Optimized Metric for Evaluation of Translation (COMET)) [9,10]. Accordingly, this study does not reprise benchmark comparisons. Instead, we investigate a complementary evaluation axis—humor retention in translation, where culturally grounded *wordplay*, double meanings, and pragmatic cues remain poorly captured by standard metrics. In doing so, we also follow calls to consider not only the funniness of translated humor but also its broader social and cultural functions [11].

This study investigates how different translation models impact humor perception by comparing a traditional Neural Machine Translation (NMT) system, referred to as MT for brevity, with three variations in GPT-based models (GPT, GPT-P, and GPT-Ex) for translating English jokes into Thai. Using a dataset of 850 jokes, human annotators evaluated each translation, categorizing them as Non-Joke (N), Not Understandable (X), Recognized as a Joke but Not Understood (XJ) or Joke (J). Through this evaluation, we examine joke retention, humor loss, and misunderstandings to determine which approach best preserves humor.

Beyond analyzing translation accuracy, this research proposes an approach that leverages GPT models with optimized prompt engineering to improve humor translation. By refining how prompts are designed, we demonstrate that GPT-P and GPT-Ex can enhance joke retention while reducing instances where jokes are misclassified as non-jokes. The findings of this study contribute to the field of humor-aware machine translation and offer practical recommendations for improving automated humor translation using LLMs.

One of the primary objectives is to compare joke retention between MT and GPT-based models. This involves evaluating how well MT, GPT, GPT-P, and GPT-Ex preserve jokes in English-to-Thai translation and identifying whether GPT-based models outperform MT in maintaining humor.

Another objective is to analyze patterns of humor loss and misunderstandings by investigating cases where jokes are misclassified as non-jokes (J → N) or misunderstood (J → XJ). The goal is to assess which translation method minimizes humor distortion.

Additionally, this study explores the impact of prompt engineering on humor translation. Specifically, it seeks to determine whether structured prompt modifications improve joke retention in GPT-based models and compare the performance of GPT-P and GPT-Ex to standard GPT translations.

Finally, this research contributes to AI-driven humor translation by providing empirical insights into machine-translated humor and offering recommendations for improving AI-based joke translation.

This study seeks to answer the following main research questions:

1. How well do different translation models (MT, GPT, GPT-P, and GPT-Ex) preserve humor in English-to-Thai joke translation?
2. What are the most common humor loss patterns in machine-translated jokes?

## 2. Related Work

### 2.1. *Humor and Translation Challenges*

Humor has long been studied in linguistic and cognitive science, with theories such as the Incongruity Theory, which suggests that humor arises from unexpected contrasts in meaning [12–14], and the Superiority Theory [15], which frames humor as deriving from perceived dominance over others. These theories emphasize the complexity of humor perception and its dependence on contextual and cultural factors [1,2].

Humor translation is particularly challenging due to linguistic and cultural disparities. Previous studies have shown that humor often fails to be preserved when translated using



<!-- page 0003 -->

traditional approaches [2,3,16]. Researchers have noted that wordplay, cultural references, and double meanings are especially difficult for MT systems to handle [17,18].

Beyond general theories of humor perception, researchers have also developed frameworks to classify different joke types. Lew [19] proposed an early taxonomy of linguistic jokes, distinguishing categories such as phonological, morphological, and semantic wordplay. More recently, De Marez et al. [20] introduced a theory-driven framework for humor interpretation and classification, which provides structured criteria for analyzing how humor operates across languages. These classification models are particularly relevant for translation, as they highlight the variety of mechanisms that may or may not transfer effectively between English and Thai.

### 2.2. *Machine Translation for Humor*

Humor translation presents unique challenges because it relies on incongruity resolution, intention attribution, and cultural knowledge, all of which complicate automated processing [21]. Traditional phrase-based MT systems struggled with contextual and cultural nuances, while neural MT has improved fluency and coherence in general translation tasks [22]. However, humor remains especially difficult for MT systems. Recent empirical studies examining machine translation of humorous texts have found that MT systems struggle significantly with preserving comedic elements, as jokes often depend on wordplay, cultural references, or language-specific constructions that do not transfer directly [2,6].

Comparative studies show that human translators outperform MT systems in various translation aspects, including the use of interactional metadiscourse features such as attitude markers, which are crucial for maintaining the communicative intent of the source text [23]. This finding is particularly relevant for humor translation, where attitude and pragmatic markers play essential roles in conveying comedic effect.

Research further highlights that MT systems often fail with puns and culture-specific jokes, constraining the creativity needed for humor translation [7,24]. Similar findings in audiovisual contexts, including sitcom subtitles and film subtitling, reinforce that humor requires adaptation strategies beyond literal translation [25,26].

To advance humor translation, future work should refine AI-driven humor processing, explore collaborative approaches between humans and MT, and establish evaluation standards that account for creativity and cultural adaptation [8].

### 2.3. *Evaluating Humor Perception in Computational Linguistics*

Assessing humor in MT outputs requires human-centered evaluation approaches that capture the multifaceted nature of comedic elements. The evaluation challenge is compounded by the fact that different joke types, including bridging-inference jokes, exaggeration jokes, and ambiguity jokes, utilize distinct cognitive mechanisms, as evidenced by varying neural activities in human brains [27]. This neurological diversity suggests that effective evaluation frameworks must account for multiple humor processing pathways, making traditional computational evaluation metrics insufficient [28].

Theory-driven evaluation frameworks have emerged as promising approaches for assessing computational humor systems. Recent work has proposed structured classification systems that distinguish between different humor mechanisms, providing evaluation criteria that can systematically assess humor preservation in translation tasks [20]. These frameworks enable evaluators to measure how well different types of humor, those that generate surprise versus amusement, are maintained across translation processes [27], offering more nuanced assessment tools than generic translation quality metrics.



<!-- page 0004 -->

Evaluating large language models’ humor capabilities reveals significant assessment challenges that directly impact translation evaluation. Studies examining models like ChatGPT3.5 demonstrate the difficulty of creating reliable evaluation metrics when these systems struggle to generate novel jokes consistently and sometimes provide fictional explanations for invalid humor [29]. These findings highlight critical gaps in current evaluation methodologies, suggesting that assessment frameworks must distinguish between humor detection accuracy, generation quality, and preservation effectiveness in translation contexts.

Contemporary evaluation methodologies recognize that assessing humor requires multimodal evaluation approaches, encompassing textual, visual, and auditory components. The development of comprehensive evaluation datasets like UR-FUNNY provides assessment frameworks that can measure humor understanding across multiple communicative channels [30]. This multimodal evaluation perspective is particularly crucial for assessing humor translation, where evaluators must measure not only textual accuracy but also the preservation of contextual and paralinguistic elements that contribute to comedic effect.

Supporting evaluation technologies from emotion detection and sentiment analysis offer complementary assessment tools for humor evaluation frameworks. Deep learning approaches to emotional recognition can provide auxiliary evaluation metrics by assessing whether underlying emotions and nuances like sarcasm are preserved during humor translation [31]. Recent evaluation benchmarks for humor generation provide standardized assessment protocols [32], while evaluation studies of transfer learning across joke categories reveal assessment challenges in cross-cultural contexts where humor evaluation criteria may vary significantly [33]. Psychology-informed evaluation approaches incorporate cognitive models to create assessment frameworks that better align with human humor perception [34].

Despite these evaluation advances, significant assessment gaps persist in computational humor research. Most current evaluation methods focus on detection and generation accuracy rather than measuring preservation quality during translation processes. Existing assessment protocols often rely on basic fluency and adequacy metrics that fail to capture humor retention, cultural adaptation effectiveness, and contextual appropriateness, all critical evaluation dimensions for humor translation. The development of comprehensive evaluation frameworks for humor translation requires further exploration of assessment strategies that can measure adaptive learning effectiveness and multimodal preservation quality in real-world applications. The role of evaluation protocols in guiding prompt engineering and human–AI collaborative assessment represents a critical gap that this study addresses through systematic evaluation methodology.

## 3. Methodology

This study focuses on English-to-Thai joke translation, where the typological distance between the two languages creates additional challenges for humor preservation. English frequently relies on inflection, word order, and spelling-based puns, whereas Thai is an analytic language with no inflectional morphology and a script that does not separate words with spaces. These contrasts complicate the transfer of wordplay and idioms across the two languages [35]. Thai humor also draws on polysemy, reduplication, rhythmic word patterns, and pragmatic markers such as the politeness particles, which can be manipulated for comic effect [36]. In addition, cultural conventions in Thai, such as its high-context communication style, mean that jokes often depend on shared background knowledge and indirect cues [37]. Similar phenomena are found in neighboring languages: Lao and Thai form a dialect continuum with shared reliance on idiomatic humor, and Khmer also em-



<!-- page 0005 -->

ploys wordplay and indirect humor. These characteristics highlight why Thai is a difficult but insightful case for investigating humor translation. The overall research methodology is summarized in Figure 1.

[Figure: Overall research methodology flowchart with four stages. Data Preparation: “Kaggle Humorous Jokes dataset” → “Random sampling (N=850)” → “Multi-label joke categorization (Wordplay, Idioms, Cultural, Irony, Dark, Absurd, Other)”. Translation Models: “MT (Google Translate, NMT system as of January 2025)”; “GPT (baseline GPT-4o)”; “GPT-P (humor-preserving prompt)”; “GPT-Ex (humor + explanation)”. Human Evaluation: “Annotator training” → “Classification into: Joke (J), Not a Joke (N), Not Understandable (X), Joke but Not Understood (XJ)” → “Majority vote procedure”. Analysis: “Humor retention rate”; “Paired significance tests”; “Classification shift visualization”; “Stratified results by joke type”.]

**Figure 1.** Overall research methodology. The workflow begins with data preparation (dataset sampling and multi-label joke categorization), followed by translation using MT and GPT-4o variants, human evaluation by annotators, and statistical analysis of humor retention.

### 3.1. *Data Preparation*

The dataset used in this study consists of 850 English jokes randomly selected from the Humorous Jokes Dataset available on Kaggle [38]. The jokes were collected from various online sources, including Twitter, Textfiles.com, FunnyShortJokes.com, LaughFactory.com, and OneLineFun.com. These jokes were compiled as positive samples for humor recognition tasks. To ensure uniqueness, jokes with a Jaccard similarity coefficient of 0.9 or higher were removed during the deduplication process. While the dataset provides a diverse range of humor, it is noted that some jokes may contain offensive content.

As part of data preparation, we applied a multi-label scheme to classify jokes into overlapping categories, following prior work on linguistic vs. cultural humor in translation [1,16,39,40], taxonomies of linguistic jokes [19], and recent computational humor frameworks [20]. The categories comprised: Wordplay, Idioms, Cultural Reference, Irony, Dark Humor, Absurd Humor, and Other. Classification was performed manually based on structural and semantic cues in the original English jokes.

### 3.2. *Translation*

The selected jokes were translated into Thai using multiple machine translation models and prompt strategies. These different approaches aimed to assess the impact of translation techniques on humor preservation. The specific translation models and strategies will be detailed in the subsequent section.

In this study, we employed four distinct translation approaches to evaluate humor retention in machine-translated jokes from English to Thai. These methods include Neural Machine Translation using Google Translate, Baseline GPT translation, and two enhanced GPT-based models with humor-aware prompts. Each method was chosen to examine different aspects of humor preservation and the effectiveness of AI-driven translation in handling jokes.

#### 3.2.1. MT-Google Translate

The MT-based approach was implemented using Google Translate via the `deep_translator` Python package (version 1.11.4). This method represents a widely used



<!-- page 0006 -->

statistical and neural-based machine translation system, which primarily focuses on literal accuracy and fluency rather than semantic adaptation or humor preservation. While Google Translate has improved significantly with neural network training, it often fails to capture cultural nuances and comedic intent, making it a strong baseline comparison for more sophisticated models.

3.2.2. Baseline GPT Translation

The Baseline GPT translation was configured as a professional translator, ensuring natural and accurate translations from English to Thai. Unlike MT, LLMs (in this study, GPT-4o) leverage contextual understanding and semantic alignment, leading to more human-like translations. However, without humor-specific instructions, GPT often produces literal translations, which may result in humor loss if direct adaptation is insufficient.

System Prompt:

“You are a professional translator who translates messages from English to Thai accurately and naturally.”

3.2.3. GPT with Humor Preservation (GPT-P)

To enhance humor retention, GPT-P was designed with a humor-aware prompt. This model was explicitly instructed to recognize jokes, Wordplay, and Cultural References and adapt them for a Thai-speaking audience. Instead of directly translating, GPT-P modifies the wording creatively to maintain the comedic intent. The goal was to increase joke retention rates while ensuring the humor remains natural and relatable in Thai.

System Prompt:

“You are a translator specializing in preserving humor when translating from English to Thai. If a message contains humor—such as wordplay, puns, or cultural references—adapt it to make it naturally funny in Thai. If a direct translation does not work, creatively modify the wording while keeping the comedic effect intact. Avoid explaining the joke; only provide the translated text.”

3.2.4. GPT with Humor Preservation and Explanation (GPT-Ex)

While GPT-P focused on retaining humor, GPT-Ex extends this by also providing an explanation. Some jokes rely on linguistic play, double meanings, or cultural nuances that Thai speakers may not inherently recognize. GPT-Ex preserves humor while adding an explanation in parentheses, clarifying the joke when necessary. This method is particularly useful for evaluating whether joke comprehension improves when explanations accompany the humor.

System Prompt:

“You are a translator specializing in preserving humor when translating from English to Thai. If a message contains humor—such as wordplay, puns, or cultural references—adapt it to make it naturally funny in Thai. If a direct translation does not work, creatively modify the wording while keeping the comedic effect intact. Additionally, provide an explanation in parentheses after the translation, clarifying the joke for Thai speakers, especially if it involves wordplay, double meanings, or cultural references.”

3.3. *Annotation*

To evaluate how well humor was retained in the translated jokes, three Thai-native annotators manually categorized the jokes. The final tag assigned to each joke was deter-



<!-- page 0007 -->

mined based on the majority vote among the annotators. The annotation categories are as follows:

- X (Not Understandable): The annotator could not comprehend the joke at all.
- XJ (Recognized as a Joke but Not Understood): The annotator recognized that the sentence was intended to be a joke but could not grasp the humor.
- J (Joke Understood): The joke was both recognized and understood as humorous.
- N (Not a Joke): The sentence was not perceived as a joke at all.

Annotators were instructed to classify each translated text into one of four categories: Joke (J), Not a Joke (N), Not Understandable (X), or Recognized as a Joke but Not Understood (XJ). Training was delivered through both written bilingual guidelines and oral explanations, ensuring that annotators fully understood the task requirements. The instructions emphasized recognizability and comprehensibility rather than joke difficulty, and we did not provide an explicit difficulty baseline. Therefore, the complexity was indirectly reflected in cases where jokes were labeled as X or XJ. We acknowledge this as a limitation and note that future work will incorporate explicit difficulty scales and calibrated exemplars.

After the training session, annotators completed a 15-item test set. Their answers were compared to gold-standard labels, and feedback was provided. Since all annotators performed well, additional training sets were not necessary; however, we had prepared further practice rounds if needed. This training procedure, combined with majority voting and inter-rater reliability checks (Fleiss’κ = 0.65), ensured consistent application of the classification scheme and minimized the influence of individual annotator backgrounds.

We used a two-step protocol. First, three annotators labeled each item independently; inter-annotator agreement (Fleiss’κ and simple agreement) was computed on these pre-consensus labels. Second, the final label per joke was set by majority vote. In the event of a 1–1–1 split, the annotators held a brief consensus discussion guided by the written criteria; if still unresolved, a blinded adjudicator assigned the label. We report the number of adjudicated items, and all statistical analyses use the consensus and adjudicated labels.

The inter-rater agreement among the three raters was evaluated using Fleiss’ Kappa and the simple agreement percentage. The Fleiss’ Kappa coefficient was calculated as $\kappa = 0.6536$, indicating a moderate to substantial level of agreement beyond what would be expected by chance. Additionally, the simple agreement percentage was 78.57%, meaning that in nearly four out of five cases, all three raters assigned the same classification. This suggests a relatively high level of consistency in their ratings. While the results indicate strong reliability, the presence of some variations highlights the potential for differences in interpretation among the raters.

### 3.4. *Evaluation and Analysis*

#### 3.4.1. Outcome Definition

The primary outcome is humor retention, defined as the proportion of items labeled J (“Joke understood”) by majority vote. For item $i$ and model $m \in \{\mathrm{MT}, \mathrm{GPT}, \mathrm{GPT\text{-}P}, \mathrm{GPT\text{-}Ex}\}$ with final label $y_{i,m} \in \{\mathrm{N}, \mathrm{X}, \mathrm{XJ}, \mathrm{J}\}$, retention was calculated as follows:

$$
R_m = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}[y_{i,m} = \mathrm{J}].
$$

In all subsequent analyses, a translation was considered retained if labeled as J; outputs labeled N, X, or XJ were treated as not retained. We also report full class distributions over {N, X, XJ, J} (see Figure 2). Retention rates ($R_m$) are reported in percentage terms throughout the Results Section.



<!-- page 0008 -->

[Figure: stacked bar chart titled “Joke Retention and Humor Loss Across Translation Methods (Percentage)”. Y-axis: “Percentage of Annotations (%)” from 0 to 100. X-axis: “Translation Method” with bars MT, GPT, GPT-P, GPT-Ex. Legend titled “Annotation Categories” with J, XJ, X, N.]

**Figure 2.** Joke retention rate across translation methods.

### 3.4.2. Paired Comparisons

Because each joke is translated by all four systems, outcomes are paired within an item. To test differences in humor retention, we dichotomized outcomes to J vs. non-J and conducted pairwise McNemar tests between models on discordant pairs. For each comparison, we report the exact $p$-value, the paired percentage-point gap in retention ($\Delta J$), and the win–loss ratio of discordant items, as summarized in Table.1.

**Table 1.** Paired case-count comparisons versus MT ($N = 850$). $n_{01}$: J in second model only; $n_{10}$: J in first model only. $\Delta J$ is the paired percentage-point gap (second minus first). $p$ from the exact McNemar test on discordant pairs.

| Pair | $n_{01}$ | $n_{10}$ | $\Delta J$ (pp) | Win–Loss ($n_{01}:n_{10}$) | $p$ (McNemar) |
|---|---:|---:|---:|---:|---:|
| MT $\rightarrow$ GPT | 127 | 204 | −9.06 | 127:204 | $1.19 \times 10^{-8}$ |
| MT $\rightarrow$ GPT-P | 206 | 172 | +4.00 | 206:172 | 0.0649 |
| MT $\rightarrow$ GPT-Ex | 270 | 161 | +12.82 | 270:161 | $9.40 \times 10^{-11}$ |

### 3.4.3. Multiclass and Shift Summaries

To characterize where gains and losses occur, we present (i) model-wise distributions over all four categories {N, X, XJ, J} and (ii) heatmaps of classification shifts between systems (e.g., MT $\rightarrow$ GPT, MT $\rightarrow$ GPT-P, MT $\rightarrow$ GPT-Ex). These descriptive visualizations highlight whether improvements arise from converting “non-joke” outputs into jokes or from clarifying previously misunderstood jokes. Statistical significance claims are based only on the paired McNemar tests above.

### 3.4.4. Stratified (Joke-Type) Analysis

To explore whether certain joke types are more or less preserved, we calculated humor retention within the categories defined during data preparation (Wordplay, Idioms, Cultural Reference, Irony, Dark Humor, Absurd Humor, and Other).

## 4. Results

### 4.1. *Humor Retention Analysis*

The ability of machine translation (MT) and AI-driven language models to retain humor in translated jokes is crucial in assessing their effectiveness. Since all original texts in this dataset were jokes, a successful translation should maintain humor and be classified as



<!-- page 0009 -->

a joke (J). This section examines joke retention across different translation methods—MT, GPT, GPT-P, and GPT-Ex—analyzing their effectiveness in preserving humor.

#### 4.1.1. Retention Rate

We report overall retention rates ($R_m$) for MT, GPT, GPT-P, and GPT-Ex, defined as the percentage of translations labeled J. Figure 2 summarizes distributions across all four annotation categories.

GPT-P maintained a retention rate of 54.12%. While it improved over GPT, it retained more jokes than MT, indicating that prompt modifications helped stabilize joke recognition and slightly improved humor retention.

GPT-Ex achieved a retention rate of 62.94%, making it the best-performing GPT-based method. This suggests that explanation-based models significantly enhance humor comprehension and preservation, surpassing both MT and other GPT variants.

#### 4.1.2. Pairwise Retention Rate Comparisons

A McNemar’s test was conducted to compare humor retention across methods. The results show significant differences in joke retention among models ($p < 0.05$), highlighting the varying effects of translation approaches on humor preservation.

To complement McNemar significance testing, we report two paired effect sizes for each model pair: (i) the paired percentage-point gap in humor retention, $\Delta J = 100 \ (n_{01} - n_{10}) / N$, and (ii) the win–loss ratio on discordant items ($n_{01} : n_{10}$), where $n_{01}$ counts jokes labeled J by the second model but not the first, and $n_{10}$ counts jokes labeled J by the first model but not the second.

Relative to MT, GPT shows a statistically significant *decrease* in humor retention ($\Delta J = -9.06$ percentage points, exact McNemar $p = 1.19 \times 10^{-8}$). GPT-P shows a numerically higher retention than MT ($\Delta J = +4.00$ percentage points), but this difference is not statistically significant at $\alpha = 0.05$ ($p = 0.0649$). GPT-Ex shows a statistically highly significant increase over MT ($\Delta J = +12.82$ percentage points, $p = 9.40 \times 10^{-11}$).

These findings confirm that AI-based translation significantly impacts joke retention. While GPT-Ex enhances joke recognition through explanations and even surpasses MT, further improvements in prompt design and contextual understanding may further bridge the gap between AI translation and human-level humor preservation.

#### 4.2. *Joke Perception Shifts Across Translation Methods (Shift Summaries)*

Understanding how humor perception changes across translation methods is crucial in evaluating joke retention. The following heatmaps illustrate how jokes originally classified as “Joke (J)” in MT are perceived when translated using GPT, GPT-P, and GPT-Ex. Each heatmap represents the transition probabilities of joke classifications, highlighting shifts such as jokes becoming “Not a Joke (N)” or “Not Understandable (X)” in different translation methods.

#### 4.2.1. MT to GPT

Figure 3a presents the joke perception shifts when transitioning from MT to GPT. The results indicate a significant loss of humor, as many jokes that were originally classified as “J” in MT are misclassified as “X” (Not Understandable) or “N” (Not a Joke) in GPT. This suggests that GPT struggles with humor recognition, possibly due to its tendency to reinterpret humor rather than translating it directly. The high transition from J to X and J to N further supports the idea that GPT fails to preserve the intended joke structure in many cases.



<!-- page 0010 -->

[Figure: Three blue heatmaps comparing joke perception shifts. (a) Title: “Joke Perception Shift: MT → GPT”; axes: “MT (Original) Output” and “GPT Output”; labels J, N, X, XJ; values: J row 69.48, 19.95, 10.56, 0.00; N row 11.15, 79.62, 9.24, 0.00; X row 16.67, 34.38, 48.96, 0.00; XJ row 15.38, 23.08, 15.38, 46.15. (b) Title: “Joke Perception Shift: MT → GPT-P”; axes: “MT (Original) Output” and “GPT-P Output”; labels J, N, X, XJ; values: J row 66.43, 19.25, 14.08, 0.23; N row 43.63, 23.25, 32.17, 0.96; X row 34.38, 20.83, 44.79, 0.00; XJ row 46.15, 7.69, 46.15, 0.00. (c) Title: “Joke Perception Shift: MT → GPT-Ex”; axes: “MT (Original) Output” and “GPT-Ex Output”; labels J, N, X, XJ; values: J row 79.34, 3.05, 13.62, 3.99; N row 48.73, 14.33, 26.75, 10.19; X row 36.46, 10.42, 39.58, 13.54; XJ row 61.54, 0.00, 15.38, 23.08.]

**Figure 3.** Comparison of joke perception shifts across different translation methods. **(a)** Joke perception shift: MT to GPT. **(b)** Joke perception shift: MT to GPT-P. **(c)** Joke perception shift: MT to GPT-Ex.

#### 4.2.2. MT to GPT-P

Figure 3b illustrates the joke perception shifts when transitioning from MT to GPT-P. Compared to standard GPT, GPT-P shows a moderate increase in J to J transitions. This indicates a higher proportion of jokes were retained under GPT-P than under GPT. However, humor loss is still present, as some jokes continue to be reclassified as N or X. While GPT-P mitigates some of the issues seen in GPT, it does not fully retain humor as effectively as MT.

#### 4.2.3. MT to GPT-Ex

Figure 3c shows the transition results for MT to GPT-Ex. Among all translation methods, GPT-Ex achieves the highest joke retention rate. The increase in J to J transitions indicates that GPT-Ex outputs were more frequently annotated as jokes compared to MT. Furthermore, the reduction in J to X and J to N transitions suggests that explanations clarify the joke structure, preventing misinterpretation. This result confirms that explanation-based translation improves humor preservation, making GPT-Ex the most effective method for maintaining joke integrity.

#### 4.2.4. Comparative Analysis of Translation Methods

The comparative analysis of the three heatmaps reveals clear trends in humor retention across translation methods. Standard GPT shows higher rates of joke misclassification,



<!-- page 0011 -->

with more J→N and J→X transitions compared to MT. GPT-P reduces these losses modestly, while GPT-Ex achieves the highest joke retention and the lowest rates of humor loss.

These results indicate that explanation-based prompting is associated with improved retention outcomes.These findings suggest that explanation-based translation is a crucial factor in preserving humor during machine translation.

### 4.3. *Humor Retention by Joke Type (Stratified Analysis)*

We annotated the corpus ($N$ = 850) using a multi-label scheme (*Wordplay, Idioms, Cultural Reference, Irony, Dark, Absurd, Other*), allowing a joke to belong to multiple mechanisms (e.g., a pun that also invokes a cultural reference). A joke was counted as *retained* if the translation output was labeled as a joke (“J”); outputs labeled “N”, “X”, or “XJ” were treated as not retained. The category sizes were: Wordplay ($n = 413$), Idioms ($n = 24$), Cultural Reference ($n = 203$), Irony ($n = 224$), Dark ($n = 177$), Absurd ($n = 28$), and Other ($n = 47$). Retention percentages by joke type across MT, GPT, GPT-P, and GPT-EX are shown in Figure 4.

[Figure: Bar chart titled “Joke Retention Rates by Type Across Translation Methods”. Y-axis labeled “Retention Rate (%)”; X-axis labeled “Joke Type” with categories Wordplay, Idioms, CulturalRef., Irony, Dark, Absurd, Other. Legend titled “Translation Method” with MT, GPT, GPT-P, GPT-Ex.]

**Figure 4.** Humor retention by joke type across translation systems.

To assess the robustness of these patterns, we conducted McNemar’s tests per joke type (Table 2). Statistically significant gains of GPT-Ex over MT were confirmed for Wordplay, Cultural Reference, Irony, and Dark Humor. In contrast, differences in Idioms, Absurd, and Other were not statistically significant due to small sample sizes, and should be interpreted as exploratory. This provides statistical support for the improvements seen in Figure 4 while also clarifying the limitations of low-$n$ categories.

**Table 2.** McNemar significance tests by joke type (MT vs. GPT-based systems). $n_{01}$: jokes retained only by GPT-based system; $n_{10}$: jokes retained only by MT. “n.s.” = not significant.

| Category | Comparison | $n_{01}$ | $n_{10}$ | $p$ |
|---|---|---:|---:|---:|
| Wordplay ($n = 413$) | MT vs. GPT | 22 | 67 | $1.9 \times 10^{-6}$ |
|  | MT vs. GPT-P | 86 | 58 | 0.024 |
|  | MT vs. GPT-Ex | 113 | 44 | $3.5 \times 10^{-8}$ |
| Idioms ($n = 24$) | all pairs | – | – | n.s. |
| Cultural Ref. ($n = 203$) | MT vs. GPT | 8 | 36 | $2.5 \times 10^{-5}$ |
|  | MT vs. GPT-Ex | 50 | 24 | 0.003 |
| Irony ($n = 224$) | MT vs. GPT | 14 | 28 | 0.043 |
|  | MT vs. GPT-Ex | 45 | 23 | 0.010 |
| Dark ($n = 177$) | MT vs. GPT-Ex | 33 | 14 | 0.008 |
| Absurd/Other | all pairs | – | – | n.s. |



<!-- page 0012 -->

Across all jokes, GPT-Ex achieved the highest overall humor retention (62.94%), followed by GPT-P (54.12%), MT (50.12%), and GPT (41.06%). Figure 4 visualizes retention percentages by joke type and system.

Some categories were already relatively well preserved by MT and GPT. Irony showed the highest baseline retention (MT 59.82%, GPT 53.57%), with GPT-Ex reaching 69.64%. Dark humor was also comparatively well handled (MT 53.11%, GPT 48.59%), with GPT-Ex improving further (63.84%). Cultural Reference exhibited a decent MT baseline (51.72%) and improved consistently with GPT-Ex (64.53%).

The largest numerical gains from explanation-based prompting occurred for Idioms, Wordplay, and Absurd. Idioms were poorly preserved by GPT (29.17%), but GPT-Ex achieved 62.50% (+33.33 percentage points), although the small sample size $n = 24$ means this difference was not statistically significant. Wordplay, typically one of the hardest categories, improved from GPT’s 32.20% to GPT-Ex’s 59.81% (+27.61 percentage points), a statistically robust difference. Absurd humor also showed a large numerical gain (50.00% → 67.86%, +17.86 percentage points), but with only 28 items this result was not statistically significant. These results suggest that explanation-based translations help especially for categories requiring resolution of ambiguity, idiomatic meaning, or surreal logic.

In summary, Irony and Dark are comparatively baseline-friendly, while Idioms, Wordplay, and Absurd show the largest room for improvement and benefit most from GPT-Ex. Cultural Reference sits between these extremes: partially preserved by MT but substantially boosted by GPT-Ex.

## 5. Discussion

While GPT has demonstrated advancements in natural language processing, our analysis shows that it struggles significantly with humor translation. Based on the dataset, GPT failed to retain humor in 130 jokes, representing 30.52% of all jokes originally classified as jokes (J) in MT. This substantial humor loss suggests that GPT frequently misinterprets the structure and intent of jokes.

### 5.1. Failure Modes of GPT in Humor Translation

To better understand why GPT fails at humor translation, we examined the two dominant failure modes:

First, GPT often produces translations that are not understandable (X). In 45 cases (10.56% of all jokes), GPT’s output was judged as completely incomprehensible by human annotators. This indicates that GPT sometimes misrepresents joke structures, leading to incoherent translations.

Second, in 85 cases (19.95% of all jokes), GPT’s output was classified as “Not a Joke (N)”, meaning the humorous intent was completely lost. This suggests that GPT often renders a direct translation without capturing the comedic structure, resulting in humor loss.

A clear example of this is the following joke:

MT:  
ฉันอยากทำงานทำความสะอาดกระจก มันเป็นงานที่ฉันเห็นตัวเองทำได้จริงๆ (I want a job cleaning mirrors. It’s a job I can really see myself doing).

Here, MT successfully retained the pun-like structure by keeping the phrase meaning intact.

GPT:  
ฉันจะดีใจมากถ้ามีงานทำความสะอาดกระจก นี่คือสิ่งที่ฉันอยากทำ (I would be very happy if I had a job cleaning mirrors. This is something I want to do).

GPT, however, removes the wordplay entirely, failing to preserve the joke’s humor.



<!-- page 0013 -->

GPT-P:  
ฉันอยากมีงานทำที่ทำความสะอาดกระจกจัง มันเป็นงานที่ฉันสามารถเห็นตัวเองทำได้ (I really want a job cleaning mirrors. It’s a job I can see myself doing).

GPT-P performs slightly better, as it retains the reflective meaning, though the phrasing is still less natural than MT.

GPT-Ex:  
ฉันอยากมีงานทำที่ทำความสะอาดกระจกจังเลย มันเป็นงานที่ฉันสามารถเห็นตัวเองในกระจกได้จริงๆ (I really want a job cleaning mirrors. It’s a job where I can literally see myself in the mirror).

GPT-Ex performs the best, as it explicitly clarifies the joke’s double meaning, making it more understandable.

### 5.2. *When MT Performs Better Than GPT*

In some cases, MT retains humor better than GPT, particularly when it mixes English and Thai to preserve wordplay. One such example is the following joke:

English (Original Joke):  
*Umbrella: An umbrella which has no further use because it has turned upside down.*

MT’s translation preserves the English word “Unbrella” while explaining it in Thai:

MT:  
*Umbrella:* ร่มที่ไม่สามารถใช้งานได้อีกต่อไป เช่นเวลาที่มันกลับด้าน (Unbrella: A useless umbrella, such as when it turns upside down).

By keeping the original word “Unbrella”, MT ensures that Thai speakers understand the wordplay.

However, GPT removes the English pun:

GPT:  
ร่มที่ไม่สามารถใช้งานได้อีกต่อไป เนื่องจากลมพัด (An umbrella that can no longer be used due to the wind).

GPT completely loses the humor by omitting the key pun (Unbrella) and only describing the situation.

GPT-P improves slightly:

GPT-P:  
ร่มกลาย: ร่มที่หมดประโยชน์ เพราะลมพัดไปทำให้มันกลับด้าน (Umbrella transformation: An umbrella that is useless because the wind turns it upside down).

GPT-Ex performs the best by explicitly referencing the joke’s pun-like structure:

GPT-Ex:  
ร่มจบชีวิต: ร่มที่ไม่มีประโยชน์อีกต่อไป เพราะลมพัดมันกลับด้าน คล้ายกับคำว่า “Unbrella” ในภาษาอังกฤษ (Dead umbrella: An umbrella that is no longer useful because the wind flips it upside down, similar to the English pun “Unbrella”).

### 5.3. *Why GPT Translation Fails at Humor*

These examples illustrate the fundamental weaknesses in GPT’s humor translation:

- Loss of wordplay: GPT often translates jokes literally, failing to preserve puns and double meanings.
- Misinterpretation of humor structure: GPT tends to rewrite jokes in a way that removes their comedic effect.
- Failure to handle cultural references: Jokes relying on cultural context are often misclassified or lost.



<!-- page 0014 -->

- Inability to balance English and Thai: MT sometimes performs better because it retains English words that are crucial for certain wordplays.

5.4. *Implications for AI-Driven Humor Translation*

The results highlight that humor translation requires more than just linguistic accuracy; it necessitates cultural and contextual awareness. GPT’s limitations in humor translation indicate that future AI models should incorporate:

- Semantic interpretation mechanisms that adapt humor beyond direct translation.
- Cultural and linguistic databases to improve recognition of context-specific jokes.
- Humor-specific training datasets to help AI models learn how humor functions across languages.
- Explanatory translation approaches, similar to GPT-Ex, to provide additional context for preserving humor.

Overall, while GPT represents a significant advancement in machine translation, its inability to consistently retain humor highlights the need for specialized humor-aware translation models. Addressing these challenges will be crucial for improving AI-driven humor translation in multilingual contexts.

5.5. *Limitations and Future Work*

A limitation of this study is the absence of an explicit complexity baseline in the annotation protocol. We intentionally focused on recognizability and comprehensibility (J/N/X/XJ) and did not elicit difficulty ratings or calibrate examples by difficulty level. Future work will introduce a difficulty rubric and per-item difficulty ratings (e.g., Likert scales), pre-annotation calibration with “easy/medium/hard” exemplars, and analyses that disentangle model effects from inherent joke difficulty.

Another limitation lies in the stratified analysis by joke type. Some categories, such as Idioms ($n = 24$) and Absurd Humor ($n = 28$), contain relatively few examples. This limits the statistical power of significance testing and means that results for these categories should be interpreted as exploratory rather than conclusive. Future work will expand the dataset to balance joke types, which will enable more robust statistical testing across categories and reduce reliance on small-$n$ subsets.

## 6. Conclusions

This study investigated the challenges of translating humor across different machine translation methods, including MT, GPT, GPT-P, and GPT-Ex. By analyzing joke retention rates and categorizing jokes into Puns, Cultural References, Idioms, and Dark Humor, we were able to identify patterns in humor loss and assess the effectiveness of explanation-based translation approaches.

Our findings indicate that humor translation remains a complex task, with significant variations in joke retention across different methods. Puns and wordplay prove to be the most difficult to translate, as they often rely on phonetic similarities and double meanings that are not easily preserved in different languages. Even the best-performing method, GPT-Ex, struggled to retain these jokes effectively. In contrast, Cultural References and Idioms benefited the most from explanation-based translation, with GPT-Ex significantly outperforming other models in retaining these types of jokes. This suggests that additional context and elaboration help human annotators recognize humor that might otherwise be lost in direct translation.

Furthermore, our results confirm that MT retains humor better than standard GPT, as GPT tends to reinterpret jokes in ways that lead to misclassification. However, GPT-P and GPT-Ex introduce notable improvements with GPT-Ex achieving the highest overall joke



<!-- page 0015 -->

retention rate. This highlights the importance of integrating explanatory mechanisms in AI-based humor translation to mitigate meaning loss.

The implications of this study extend beyond joke translation, as humor is deeply intertwined with cultural and linguistic nuances. The findings suggest that improving humor-aware translation techniques requires integrating not only linguistic context but also cultural awareness and interpretative explanations. Future work should explore more advanced contextual learning techniques, including fine-tuned language models with cultural adaptation and interactive translation systems that allow human oversight to enhance joke preservation.

In conclusion, while explanation-based translation (GPT-Ex) demonstrates promising advancements in humor retention, humor translation remains an ongoing challenge that necessitates further research. Future AI translation models should focus on improving contextual understanding, phonetic wordplay adaptation, and cultural nuance integration to bridge the gap between machine translation and human humor comprehension.

**Author Contributions:** Conceptualization, M.P.; methodology, M.P.; software, M.P.; validation, M.P.; formal analysis, M.P.; investigation, M.P.; resources, Y.M.; data curation, M.P.; writing—original draft preparation, M.P.; writing—review and editing, M.P. and Y.M.; visualization, M.P.; supervision, Y.M.; project administration, M.P. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by the Japan Society for the Promotion of Science (JSPS) KAKENHI Grant-in-Aid for Early-Career Scientists, grant number 21K17794.

**Data Availability Statement:** The data presented in this study are available on request from the corresponding author.

**Conflicts of Interest:** The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

## References

1. Zabalbeascoa, P. Humor and translation—An interdiscipline. *Humor* **2005**, *18*, 185–207. [CrossRef]
2. Chiaro, D. *Translation, Humour and Literature: Translation and Humour*; Continuum International Publishing Group: London, UK; New York, NA, USA, 2010.
3. Attardo, S. Translation and Humour: An Approach Based on the General Theory of Verbal Humour (GTVH). *Translator* **2002**, *8*, 173–194. [CrossRef]
4. Andayani, A.; Herman, H.; Syathroh, I.L.; Fatmawati, E.; Syahrul, N.; Al-Awawdeh, N.; Batubara, J.; Saputra, N. Inquiry into the challenges of translating idioms extracted from musical lyrics. *Res. J. Adv. Humanit.* **2023**, *4*, 196–206. [CrossRef]
5. Mintz, L.E. Standup Comedy as Social and Cultural Mediation. *Am. Q.* **1985**, *37*, 71–80. [CrossRef]
6. Günel, L.; Miller, T.; Reiter, N.; Touileb, S. Can Machine Translations Translate Humorous Texts? In *Proceedings of the Working Notes of CLEF 2022—Conference and Labs of the Evaluation Forum*; CEUR Workshop Proceedings; CEUR: Aachen, Germany, 2022; pp. 912–923.
7. Ardi, H.; Al Hafizh, M.; Rezqi, I.; Tuzzikriah, R. Can Machine Translations Translate Humorous Texts? *Humanus* **2022**, *21*, 99. [CrossRef]
8. Abu-Rayyash, H. AI Meets Comedy: Viewers’ Reactions to GPT-4 Generated Humor Translation. *Ampersand* **2023**, *12*, 100162. [CrossRef]
9. Jiao, W.; Wang, X.; Huang, J.; Wang, X.; Shi, S.; Tu, Z. Is ChatGPT a Good Translator? Yes with GPT-4 as the Engine. *arXiv* **2023**, arXiv:2301.08745. [CrossRef]
10. Zhu, W.; Ma, J.; Xiong, D. Large Language Models for Machine Translation: A Survey. *arXiv* **2023**, arXiv:2304.04675.
11. Cann, A.; Jordan, J.A.; Cann, A.T. Understanding the Effects of Exposure to Humor Expressing Affiliative and Aggressive Motivations. *Motiv. Emot.* **2015**, *40*, 258–267. [CrossRef]
12. Raskin, V. *Semantic Mechanisms of Humor*; D. Reidel Publishing Company: Dordrecht, The Netherlands; Boston, MA, USA, 1985.
13. Attardo, S. *Linguistic Theories of Humor*; Mouton de Gruyter: Berlin, Germany; New York, NY, USA, 1994.
14. Attardo, S. *The Linguistics of Humor: An Introduction*; Oxford University Press: Oxford, UK, 2020.
15. Morreall, J. *Taking Laughter Seriously*; SUNY Press: Albany, NY, USA, 1983.



<!-- page 0016 -->

16. Zabalbeascoa, P. Translating Jokes for Dubbed Television Comedy. *Translator* **1996**, *2*, 235–257. [CrossRef]

17. Cintas, J.D.; Remael, A. *Audiovisual Translation: Subtitling*; Routledge: London, UK, 2007.

18. Delabastita, D. *Wordplay and Translation: Special Issue of ‘the Translator’2/2 1996*; Routledge: London, UK, 2016.

19. Lew, R. Towards a Taxonomy of Linguistic Jokes. In Proceedings of the Annual Conference of the Polish Association for the Study of English (PASE), Puławy, Poland, 21–23 April 1997.

20. De Marez, V.; Winters, T.; Rigouts Terryn, A. THInC: A Theory-Driven Framework for Computational Humor Detection. *arXiv* **2024**, arXiv:2409.01232.

21. Bartolo, A.; Nichelli, P.; Baraldi, P.; Benuzzi, F.; Nocetti, L. Humor Comprehension and Appreciation: An fMRI Study. *J. Cogn. Neurosci.* **2006**, *18*, 1789–1798. [CrossRef]

22. Stahlberg, F. Neural machine translation: A review of methods, resources, and tools. *Mach. Transl.* **2020**, *34*, 365–380.

23. Afzaal, M.; Du, X.; Almusharraf, N.; Imran, M. Automated and Human Interaction in Written Discourse: A Contrastive Parallel Corpus-based Investigation of Metadiscourse Features in Machine-Human Translations. *SAGE Open* **2022**, *12*, 215824402211422. [CrossRef]

24. Corpas Pastor, G. Human versus Neural Machine Translation Creativity. *Information* **2024**, *15*, 530. [CrossRef]

25. Hallberg, L. Humor in Translation and What It Can Entail: A Linguistic Analysis of Humorous Elements in Audiovisual Translation. Bachelor’s Thesis, Umeå University, Umeå, Sweden, 2024.

26. Amirdabbaghian, A. Assessing Translation of Humor in the English Subtitles of *Goodbye, Mr. Loser*. *J. Dev. Soc.* **2024**, *1*, 75–91. [CrossRef]

27. Chan, Y.C. Neural Correlates of Sex/Gender Differences in Humor Processing for Different Joke Types. *Front. Psychol.* **2016**, *7*, 536. [CrossRef]

28. Winters, T. Computers Learning Humor Is No Joke. *Harv. Data Sci. Rev.* **2021**, *3*, 1–18.

29. Jentzsch, S.; Kersting, K. ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models. In Proceedings of the 13th Workshop on Computational Approaches to Subjectivity, Sentiment, & Social Media Analysis, Toronto, ON, Canada, 14 July 2023; Association for Computational Linguistics: Stroudsburg, PA, USA, 2023. [CrossRef]

30. Hasan, M.K.; Rahman, W.; Zadeh, A.B.; Zhong, J.; Tanveer, M.I.; Turrin, L.P.; Hoque, E. UR-FUNNY: A Multimodal Language Dataset for Understanding Humor. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), Hong Kong, China, 3–7 November 2019; Association for Computational Linguistics: Stroudsburg, PA, USA, 2019. [CrossRef]

31. Guo, J. Deep learning approach to text analysis for human emotion detection from big data. *J. Intell. Syst.* **2022**, *31*, 113–126. [CrossRef]

32. Chen, Y.; Eger, S. Transformers Go for the LOLs: Generating (Humourous) Titles from Scientific Abstracts End-to-End. *arXiv* **2022**, arXiv:2212.10522.

33. Turgeman, M.; Shani, C.; Shahaf, D. One Joke to Rule Them All? On the (Im)possibility of Humor Transfer Learning Across Multiple Humor Types. *arXiv* **2025**, arXiv:2508.19402.

34. Su, Y.; Zhu, Y.; Chen, Y.; Benavides-Prado, D.; Witbrock, M. Psychology-Driven Enhancement of Humour Translation. *arXiv* **2025**, arXiv:2507.09259. [CrossRef]

35. Wiboolyasarin, W. Comparative Grammar: Thai and English Languages. In *Thai Grammar Instruction*; Springer Texts in Education; Springer: Singapore, 2025. [CrossRef]

36. Wangsomchok, C. A Linguistic Strategies to Express Humor in Thai Context. *Int. J. Soc. Sci. Humanit.* **2016**, *6*, 462–465. [CrossRef]

37. Kanchanapoomi, T.; Trakulkasemsuk, W. Laughter: A Communication Strategy in Business Meeting between Thai and Burmese Professionals. *rEFLections* **2020**, *27*, 22–43. [CrossRef]

38. Chen, E.; Jiang, Y. Humor Detection. Kaggle Competition. 2020. Available online: https://kaggle.com/competitions/humor-detection (accessed on 14 January 2025).

39. Chiaro, D. Verbally Expressed Humour and Translation: An Overview of a Neglected Field. In *Humor and Translation*; Chiaro, D., Ed.; Mouton de Gruyter: Berlin, Germany, 2006; pp. 135–154.

40. Chiaro, D. Verbally Expressed Humour and Translation. In *The Primer of Humor Research*; Raskin, V., Ed.; Mouton de Gruyter: Berlin, Germany, 2008; pp. 569–608. [CrossRef]

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
