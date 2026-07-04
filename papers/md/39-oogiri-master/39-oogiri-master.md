<!-- Transcribed from 39-oogiri-master.pdf -->



<!-- page 0001 -->

arXiv:2512.21494v1 [cs.CL] 25 Dec 2025

# OOGIRI-MASTER: Benchmarking Humor Understanding via Oogiri

**Soichiro Murakami**<sup>1</sup>, **Hidetaka Kamigaito**<sup>1,2</sup>, **Hiroya Takamura**<sup>3</sup>, **Manabu Okumura**<sup>3</sup>  
<sup>1</sup>CyberAgent, <sup>2</sup>Nara Institute of Science and Technology, <sup>3</sup>Institute of Science Tokyo  
murakami_soichiro@cyberagent.co.jp, kamigaito.h@is.naist.jp, {takamura,oku}@pi.titech.ac.jp

## Abstract

Humor is a salient testbed for human-like creative thinking in large language models (LLMs). We study humor using the Japanese creative response game Oogiri, in which participants produce witty responses to a given prompt, and ask the following research question: *What makes such responses funny to humans?* Previous work has offered only limited reliable means to answer this question. Existing datasets contain few candidate responses per prompt, expose popularity signals during ratings, and lack objective and comparable metrics for funniness. Thus, we introduce OOGIRI-MASTER and OOGIRI-CORPUS, which are a benchmark and dataset designed to enable rigorous evaluation of humor understanding in LLMs. Each prompt is paired with approximately 100 diverse candidate responses, and funniness is rated independently by approximately 100 human judges without access to others’ ratings, reducing popularity bias and enabling robust aggregation. Using OOGIRI-CORPUS, we conduct a quantitative analysis of the linguistic factors associated with funniness, such as text length, ambiguity, and incongruity resolution, and derive objective metrics for predicting human judgments. Subsequently, we benchmark a range of LLMs and human baselines in OOGIRI-MASTER, demonstrating that state-of-the-art models approach human performance and that insight-augmented prompting improves the model performance. Our results provide a principled basis for evaluating and advancing humor understanding in LLMs.

**Keywords:** Humor, Oogiri, Large Language Models, Benchmarking, Linguistic Analysis

## 1. Introduction

Endowing large language models (LLMs) with human-like creative thinking capabilities is a major challenge that extends beyond problem-solving abilities. Humor understanding is one of such key capabilities. Understanding and generating humor as humans require more than pattern matching; they necessitate creative reasoning that incorporates context and cultural nuances to produce witty and unexpected responses (Loakman et al., 2025). This study addresses humor as an instance of creative thinking in LLMs by focusing on the specific case of *Oogiri* (大喜利). *Oogiri* is a Japanese creative response game that involves improvising humorous responses to a given prompt, as shown in Figure 1, making it an ideal testbed for creativity and wit. This raises the central question: *What exactly makes Oogiri responses funny to humans?* The starting point of our study is to answer this question. Few studies have aimed to capture the human perception of funniness using objective metrics and to analyze its components quantitatively. This absence poses a significant barrier to the evaluation of humor understanding in LLMs.

[Figure: boxed prompt–response example. Prompt: Worst commit message ever. Response: “It works on my machine.”]

Figure 1: Oogiri prompt–response example.

We address two key challenges in evaluating the humor understanding of LLMs. First, the constituent elements of a funny response remain insufficiently understood. Humor is a subjective construct arising from a complex interplay of factors such as the violation of expectations and resonance. However, an objective, quantitative metric does not exist for measuring funniness itself. Consequently, we lack a principled basis for explaining why an Oogiri-style response is funny, which hinders the systematic improvement of LLM humor understanding. The second challenge is the low reliability of existing datasets for such analysis. For example, the Oogiri-GO dataset (Zhong et al., 2024) was collected from Bokete,[^1] a caption-contest platform on which users upvote funny responses to prompts. Although this social-voting signal is useful at this scale, it introduces two methodological limitations. First, the fairness of the evaluation process is not guaranteed: making the popularity of each response visible to other raters may introduce popularity bias and compromise objectivity. Second, the dataset exhibits structural bias. With only approximately eight candidate responses per prompt, on average, raters are likely to select a *relatively better* option rather than an intrinsically humorous one.

Therefore, in this study, we propose OOGIRI-MASTER, a benchmark that evaluates the humor understanding of LLMs using the Oogiri task. Specifically, we address the two challenges outlined above by constructing a novel dataset and conducting a quantitative analysis of the funniness components, with which we assess the current

[^1]: https://bokete.jp/



<!-- page 0002 -->

capabilities and pave the way for improvements. First, we construct Oogiri-Corpus, a dataset that ensures reliability and objectivity.<sup>2</sup> On average, each prompt is paired with approximately 100 diverse candidate responses that are rated for funniness by approximately 100 human judges in an independent setting in which they cannot see others’ ratings. This design mitigates the issues of fairness and data bias observed in existing datasets. Second, using this dataset, we quantitatively analyze the linguistic features that constitute funniness. We identify common lexical and structural patterns in high-rated responses, transforming the ambiguous notion of funniness into measurable, objective metrics. This enables explanations of *why a response is funny* based on data-driven evidence, rather than subjective intuition. Finally, we present the multifaceted benchmark results on Oogiri-Master. We benchmark humans and various LLMs to clarify the current state of the art in the humor understanding of LLMs.

The contributions of this study can be summarized as follows:<sup>3</sup> First, we constructed and release a large-scale reliable dataset, Oogiri-Corpus, which serves as a novel foundation for evaluating humor understanding in LLMs. Second, through quantitative analysis of this dataset, we identified the constituent components of funniness, demonstrating that features such as response length, perspective shift, and ambiguity are strongly correlated with high-rated responses. Third, we propose a novel benchmark, Oogiri-Master, and experimentally demonstrated that (1) state-of-the-art LLMs such as GPT-5 show performance approaching human performance; (2) our analytical insights into the constituent components of humor can contribute to performance improvements in humor judgment; (3) instructing LLMs to leverage these insights only when uncertain improves their performance; and simultaneously, (4) continued pretraining on the target-language corpus enhances the humor understanding abilities of LLMs.

## 2. Related Work

**Background on Computational Humor** Computational humor is a relatively new area, and humor understanding/generation remains a challenging problem in natural language processing (Loakman et al., 2025). One obstacle is defining “humor” appropriately. Consequently, many studies have narrowed the scope to specific forms (e.g., puns, Oogiri, satire) to make the problem tractable (Amin and Burghardt, 2020). Among these, pun generation has a particularly long history and is a central task (Ritchie, 2005; Yu et al., 2018; Luo et al., 2019)

**Oogiri as a Testbed for Humor Understanding**  
We target Oogiri as our testbed for humor understanding. Oogiri is a creative response game in which one provides a witty response to a prompt. Although the most common setup is a text-to-text format in which a textual prompt is paired with a textual response, modal variants exist (e.g., image-to-text one-liners; image&text-to-text fill-in-the-blank) (Zhong et al., 2024). These formats resemble memes (Sharma et al., 2023; Nguyen and Ng, 2024); we regard memes as a multimodal variant of Oogiri. However, we focus on text-to-text Oogiri for two reasons. First, abundant web resources exist. Oogiri is widely popular in TV programs and social media, and large platforms such as Bokete and Oogiri Sogo host substantial data. Because analyzing humor components requires diverse and numerous samples, Oogiri is suitable from a data perspective. Second, the text-to-text format is unimodal, making semantic understanding more straightforward than with multimodal variants.

**Existing Oogiri Datasets and Their Limitations**  
Although progress has been hampered by limited datasets, interest has recently increased with the advent of LLMs and the concomitant need for evaluation resources. Oogiri-specific datasets remain relatively scarce; adjacent resources include English caption datasets collected from the New Yorker Caption Contest (Hessel et al., 2023) and various meme datasets (Liu et al., 2022; Hwang and Shwartz, 2023; Hossain et al., 2022). Oogiri-GO, which was built using Bokete and social media, is a representative Oogiri dataset. However, it faces two issues: (1) fairness concerns: Voter interfaces display others’ popularity, inviting conformity and potentially compromising objectivity. (2) structural bias: Many prompts have few candidate responses (approximately eight on average); hence, raters may select responses that are merely “less bad,” rather than intrinsically funny. In this study, we construct a novel Oogiri dataset, Oogiri-Corpus, which addresses these issues and serves as a foundation for evaluating LLM humor understanding, thereby improving reliability.

**Quantitative Analyses of Humor Components**  
Although studies have been conducted on generation, understanding, and explanation in computational humor (Amin and Burghardt, 2020; Loakman et al., 2025), quantitative analyses of the constituent components of “funniness” remain underexplored. To fill this gap, using Oogiri-Corpus, we analyze how diverse linguistic features, such

<sup>2</sup>We distinguish the dataset, Oogiri-Corpus, which underpins our analyses, from the benchmark, Oogiri-Master, which builds on it to evaluate LLMs.  
<sup>3</sup>The dataset and the benchmark will be provided under the CC BY-NC-SA 4.0 license.



<!-- page 0003 -->

as perspective shift, ambiguity, harmlessness, surprisal, sentence length, and part-of-speech (POS) ratios, relate to humor, with the aim of identifying objective, quantitative indicators. Furthermore, using our benchmark experiments, we outline how these insights can improve LLM humor understanding.

## 3. Dataset Construction

Motivated by the second challenge mentioned in §1, we present Oogiri-Corpus and provide details on its construction process and descriptive statistics. We collected data from a public Japanese Oogiri competition platform, Oogiri Sogo^4. On this platform, each prompt proceeds through an answer phase, a voting phase, and a final leaderboard announcement. During the answer phase, users submit responses within a fixed time window (e.g., 12 h). This phase then transitions to the voting phase, in which users vote for the responses that they find funny among all submissions. Unlike other platforms (e.g., Bokete), vote counts are not displayed during the voting phase, which helps to mitigate popularity bias and supports fairer evaluation. Finally, the platform announces a leaderboard based on the total votes.

Dataset construction comprised two steps: web crawling^5 and quality filtering. First, we collected 2,165 prompts from the platform.^6 Each prompt is associated with many responses, and each response has a vote count indicating its perceived funniness. We applied vote-based filtering to ensure reliability: we excluded prompts for which the total number of votes was fewer than 100. This threshold reduces the variance owing to rater subjectivity and chance when the vote pool is small. In total, 908 prompts remained. We refer to this 908-prompt dataset as Oogiri-Corpus, and used it for the subsequent analyses and benchmark construction.

Oogiri-Corpus consists of prompts, responses, and vote counts. Across the 908 prompts, each prompt has approximately 96 responses and 172 votes, on average. The total number of prompt–response pairs is 82,536. This is approximately seven times larger than that of Oogiri-GO (Zhong et al., 2024) and, to the best of our knowledge, is the largest Japanese Oogiri dataset to date.^7 Moreover, although Oogiri-GO averages approximately eight responses per prompt, our dataset offers approximately 96 responses, yielding a far more diverse candidate set per prompt. This breadth enables raters to select responses that are genuinely funny rather than merely “less bad” within a limited pool. Dataset statistics are presented in Table 1.

| Statistic | Value |
|---|---:|
| Prompts | 908 |
| Responses per prompt (avg.) | 95.9 |
| Votes per prompt (avg.) | 171.6 |
| Votes per response (avg.) | 1.8 |
| Votes per top-1 response (avg.) | 10.3 |
| Prompt length in characters (avg.) | 20.4 |
| Response length in characters (avg.) | 16.4 |

Table 1: Summary statistics of Oogiri-Corpus.

## 4. Linguistic Feature Analysis

We address the first challenge mentioned in §1: elucidating the components that constitute a “funny response.” “Funniness” is subjective and complex; for example, it involves expectation violations and relatability. However, a generally accepted quantitative metric remains lacking. Accordingly, our analysis aims to explain and analyze why an Oogiri response is funny based on a variety of quantitative linguistic features. Through this analysis, we seek to identify objective and quantitative indicators for understanding humor and to pave the way for improving the ability of LLMs to understand humor.

### 4.1. Dataset for Analysis

We quantitatively examined the linguistic features that constitute “humor,” using Oogiri-Corpus as the foundation. Although the dataset links an average of 96 responses to each prompt, we did not use all responses for the analysis. This is because many responses have zero votes, creating a pronounced imbalance between high-rated responses with many votes and low-rated responses with no votes, which makes the analysis challenging.

Accordingly, we first narrowed down the responses under analysis and balanced the high- and low-rated responses. Specifically, for each prompt, we defined the top three responses by vote count as “high-rated responses” and the bottom three as “low-rated responses.” On average, high-rated responses received approximately 8.5 votes, whereas all low-rated responses had zero votes. Given this low-rated nature, we considered them as reasonable representatives of “unfunny responses.” This yielded 5,448 responses for the analysis, with 908 prompts × 6 responses.

### 4.2. Analysis Methodology

We examined the relationships between linguistic features and response humor. Specifically, for each response, we quantitatively measured a range of

^4 https://chinsukoustudy.com/  
^5 The site explicitly permits web crawling.  
^6 Prompt IDs 87–2254 were available when accessed.  
^7 Compared with 11,842 Japanese Oogiri instances in a text-to-text setting.



<!-- page 0004 -->

linguistic features and analyzed the relationship of these feature values to response humor (i.e., differences between the high- and low-rated groups). We defined and quantified various aspects of linguistic features by borrowing ideas from theories of humor, such as incongruity theory (Morreall, 2024). These include basic linguistic features, such as sentence length, as well as higher-order features, such as resolution of incongruity (see details in §4.3). We considered that, when a feature exhibits a significantly higher or lower value in high-rated responses, it may constitute a component of humor.

We reported these relationships using an independent two-sample Student’s t-test (two-sided, assuming equal variances) (Fisher, 1925) and Cohen’s d (Cohen, 1988). The t-test assesses whether there is a statistically significant difference between two group means. Because the t-tests are sensitive to large sample sizes, we also reported Cohen’s d, an effect-size measure. Cohen’s d is the difference between the two group means divided by a pooled standard deviation and is used to evaluate the magnitude of the effect. Larger values indicate more substantively meaningful group differences. The formula for Cohen’s d is as follows:

$$
d = \frac{\bar{X}_1 - \bar{X}_2}{s_p}, \quad
s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}},
$$

where $\bar{X}$, $s$, and $n$ are the mean, standard deviation, and sample size for each group, and $s_p$ is the pooled standard deviation. The conventional benchmarks interpreted $d = 0.2$, 0.5, and 0.8 as small, medium, and large effects, respectively.

## 4.3. Linguistic Features

To capture humor from multiple perspectives, we defined four groups of features listed in Table 2 and measured them quantitatively. Inspired by the theories of humor (Morreall, 2024) and prior research on humor and other creative domains (Zhong et al., 2024; Murakami et al., 2025), we selected these features as plausible constituents of humor.

**Basic Linguistic Features** We defined basic linguistic features that comprise (i) response-independent measures and (ii) prompt–response relative measures. The former is based solely on the response, whereas the latter is based on the relationship between the prompt and response. The response-independent measures include sentence length based on character count, number of unique characters, ratios of character types (e.g., *hiragana* and *katakana* in Japanese), and POS ratios (e.g., nouns, verbs, and symbol marks). We used a Japanese morphological analyzer, MeCab (Kudo et al., 2004), to perform tokenization and POS tagging. The prompt–response relative measures include length ratios of prompt–response pairs based on character count, lexical novelty ratios, and relative change in character-type ratios. We defined the lexical novelty ratio as the proportion of words in the response that do not appear in the prompt and the relative change in character-type ratios as the difference in the ratios of character types between the prompt and response.

**Semantic Distance and Textual Entailment** Inspired by incongruity theory (McDonald, 2013), we introduced semantic features that capture how a response deviates from the expectations set by the prompt. Incongruity theory states that *humor arises when expectations are violated* (Morreall, 2024). In a prompt–response setting, this corresponds to semantic divergence or explicit contradiction between the two texts. To capture this relationship, we used two signals: (i) semantic distance and (ii) textual entailment. Semantic distance is measured as one minus the cosine similarity between the prompt and response embeddings. Textual entailment is measured using natural language inference (NLI) probabilities, namely entailment, neutral, and contradiction, predicted using an NLI model. We used the `text-embedding-3-large` (OpenAI, 2025) to obtain the text embeddings and the `mDeBERTa-v3-base` (He et al., 2021) fine-tuned on the XNLI (Conneau et al., 2018) and `multilingual-NLI-26lang-2mil7` datasets (Lauer et al., 2022) to obtain the NLI probabilities.[^8] We assumed that higher semantic distance or explicit contradiction indicates higher unexpectedness. We then quantitatively tested whether leveraging contradictions increases the degree of humor.

**Surprisal and Pointwise Mutual Information** In addition to the aforementioned features grounded in incongruity theory, we introduced two metrics by borrowing ideas from information theory: surprisal (Shannon, 1948) and normalized pointwise mutual information (nPMI) (Fano, 1961). Surprisal is the length-normalized negative log-probability under a language model; higher values indicate less predictable responses. nPMI quantifies the association between a prompt and its response; lower values imply co-occurrence that is close to chance. Both metrics also capture deviation from expectation in incongruity theory: surprisal reflects unpredictability of the prompt–response pair or response text itself, whereas nPMI captures unexpectedness in the prompt–response relationship. We computed these using GPT-2.[^9]

[^8]: https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7  
[^9]: https://huggingface.co/rinna/japanese-gpt2-medium



<!-- page 0005 -->

**LLM-Scored Higher-Order Features** We used an LLM to measure eight higher-order linguistic features. By “higher-order,” we mean features that extend beyond surface cues (e.g., length) and probabilistic or embedding-based signals (e.g., surprisal). Therefore, we used an LLM to score each prompt–response pair on a 1–5 scale across the eight aspects listed in Table 2. These aspects include the following: (1) *Ambiguity exploitation*: The use of lexical or structural ambiguity, (2) *Associative distance*: A moderate and natural conceptual leap, (3) *Benign violation*, grounded in benign violation theory (McGraw and Warren, 2010), with deviations framed as harmless and acceptable, (4) *Coherence*: Strong discourse-level connectedness, (5) *Expectedness*: The ease of predicting the response, (6) *Incongruity resolution*, grounded in incongruity-resolution theory (Ritchie, 2009); the natural resolution of an initial mismatch by a coherent reinterpretation, (7) *Metaphor use*: The presence of metaphorical expression in the response, (8) *Perspective shift*: A meaningful change in viewpoint or framing that enables a punchline. In all cases, higher scores indicate more of the stated property. We defined clear evaluation criteria for each aspect and incorporated them into the prompt.[^10] Because of API cost considerations, we sampled 2,000 prompt–response pairs, where 1,000 pairs were randomly selected from high- and low-rated groups, and conducted batched evaluations for each pair using GPT-5.

### 4.4. Analysis Results

We report on the relationships between each linguistic feature and response humor. Table 2 presents the mean of each feature for the high- and low-rated groups, p-value of the t-test, and Cohen’s d. Our analysis yielded the following findings:

**High-Rated Responses Tend to be Shorter**  
Length-related features such as the length and prompt–response length ratios were significantly lower in the high-rated group than in the low-rated group, with small effect sizes. This suggests that brevity contributes to humor.

**Appropriate Vocabulary Diversity is Beneficial**  
Interestingly, the high-rated group showed significantly lower values for the unique character count (unique chars) and the rate at which vocabulary that is not in the prompt appears in the response (lexical novelty), with small effect sizes. This indicates that, relative to the low-rated group, high-rated responses had a lower tendency to use new vocabulary and may benefit from selecting appropriate words without straying far from the topic of the prompt.

| Feature names | High | Low | Cohen’s d |
|---|---:|---:|---:|
| **Basic Features** |  |  |  |
| *Response-independent* |  |  |  |
| length<sup>*†</sup> | 14.12 | 16.40 | **-0.28** |
| unique chars<sup>*†</sup> | 13.24 | 15.32 | **-0.30** |
| hiragana ratio<sup>*</sup> | 0.46 | 0.44 | 0.11 |
| katakana ratio<sup>*†</sup> | 0.14 | 0.16 | -0.11 |
| noun ratio<sup>*</sup> | 0.42 | 0.45 | -0.13 |
| verb ratio<sup>*</sup> | 0.16 | 0.14 | 0.10 |
| symbol ratio<sup>*†</sup> | 1.91 | 2.24 | -0.07 |
| *Prompt-response* |  |  |  |
| length ratio<sup>*†</sup> | 0.76 | 0.90 | **-0.27** |
| lexical novelty<sup>*</sup> | 0.80 | 0.93 | **-0.21** |
| hiragana changes<sup>*</sup> | -0.04 | -0.06 | 0.10 |
| katakana changes<sup>*</sup> | 0.02 | 0.05 | -0.10 |
| **Semantic / NLI** |  |  |  |
| semantic distance<sup>*</sup> | 0.73 | 0.72 | 0.16 |
| contradiction<sup>*</sup> | 0.28 | 0.27 | 0.06 |
| entailment<sup>*</sup> | 0.17 | 0.14 | 0.18 |
| neutral<sup>*</sup> | 0.55 | 0.59 | -0.15 |
| **Surprisal / PMI** |  |  |  |
| nPMI<sup>*</sup> | 0.12 | 0.14 | -0.14 |
| surprisal<sup>*</sup><sub>response-independent</sub> | 5.17 | 5.08 | 0.08 |
| surprisal<sup>*</sup><sub>prompt-response</sub> | 4.66 | 4.51 | 0.13 |
| **LLM-Scored Features** |  |  |  |
| ambiguity exploitation<sup>*†</sup> | 2.10 | 1.61 | **0.42** |
| associative distance<sup>*†</sup> | 4.38 | 3.90 | **0.33** |
| benign violation<sup>*†</sup> | 4.73 | 4.49 | **0.27** |
| coherence<sup>*</sup> | 4.11 | 3.95 | 0.15 |
| expectedness | 2.68 | 2.78 | -0.08 |
| incongruity resolution<sup>*†</sup> | 3.71 | 3.35 | **0.36** |
| metaphor use<sup>*†</sup> | 1.54 | 1.31 | **0.24** |
| perspective shift<sup>*†</sup> | 2.40 | 1.87 | **0.50** |

Table 2: Comparison of linguistic features between high- and low-rated responses. * indicates statistical significance ($p < 0.05$). Bold values in the Cohen’s d indicate a small or medium effect size ($|d| \ge 0.2$). † indicates features that are employed in the benchmark experiments (§5).

**Higher-Order Linguistic Features are Effective**  
Ambiguity exploitation, associative distance, benign violation, incongruity resolution, metaphor use, and perspective shift were significantly higher in the high-rated group, with small-to-medium effect sizes. Among these, perspective shift and ambiguity showed relatively larger effects, indicating particular importance for humor. Incongruity resolution, grounded in incongruity-resolution theory (Ritchie, 2009), also showed a relatively large effect size, suggesting its contribution to humor.

**Other Features Have Limited Impact**  
Semantic distance, textual entailment, surprisal, nPMI, and other linguistic features (e.g., POS ratio) showed statistically significant differences, but the effect sizes were below small, suggesting limited contri-

[^10]: The full prompt is provided in Appendix A.



<!-- page 0006 -->

butions to humor. Notably, textual entailment and surprisal captured similar aspects to coherence and expectedness in higher-order linguistic features, but their effect sizes were below small, consistently suggesting their limited role in constituting humor.

## 5. Oogiri Understanding Benchmark

We propose a novel benchmark, OOGIRI-MASTER. The aim of this benchmark is to measure the ability of an LLM to understand and judge “humor” in Oogiri from different perspectives. Specifically, we propose five tasks that can be broadly grouped into two categories: four relative-judgment tasks using multiple-choice question answering (MCQA) and one absolute-judgment task using binary classification. Standardized prompt templates and strict evaluation criteria were used to ensure reproducibility and comparability. In the experiments, we tested the insights from our analysis results in §4 and reflected the multiple linguistic features into prompt templates, seeking the performance gains of LLMs (§5.3). Our goal was to clarify the current state of LLM humor understanding and outline a path for further improvement.

### 5.1. Task Design

**Relative Judgment Tasks** In the MCQA setting, the model selects the most humorous response to a given prompt from several candidate responses. We defined four types of tasks: two binary-choice tasks, a three-choice task, and a four-choice task. In all tasks, the high-rated response for each prompt served as the positive example, and the negatives were constructed differently for each task. For the two binary-choice tasks, we constructed negatives in two ways: (i) we paired the positive with one low-rated response from the same prompt (Binary$_{\text{same}}$) and (ii) we paired the positive with one high-rated response for a different prompt (Binary$_{\text{diff}}$). The latter evaluates whether the model can judge funniness as a response to the given prompt, rather than merely ranking responses within the same prompt, following Hessel et al. (2023). For the three- and four-choice tasks, we used one low-rated same-prompt response and one or two high-rated different-prompt responses as negatives, respectively.

**Absolute Judgment Task** In the binary classification setting, the model decides whether a response to a prompt is “funny” or “not funny.” For each prompt, we used the high-rated response as the positive and the low-rated response as the negative, measuring the ability of the model to evaluate funniness in absolute terms. Figure 2 shows an example of the absolute-judgment prompt.

[Figure: Prompt box containing the following text]

    You are an expert judge of Oogiri humor.
    Prompt: {prompt}
    Response: {response}
    Is this response funny?
    Important: Answer with either funny or not
    funny only. No explanation is required.
    Answer:

Figure 2: Prompt for the absolute judgment task.

### 5.2. Dataset Construction

OOGIRI-MASTER is built on OOGIRI-CORPUS. For the MCQA setting, we sampled 100 prompts per task from OOGIRI-CORPUS, and selected positives and negatives according to each task design, yielding 400 items across the four tasks. For binary classification, we sampled 100 prompts from OOGIRI-CORPUS, pairing one high-rated response and one low-rated response per prompt for 200 items. In total, OOGIRI-MASTER comprised 600 items.[^11]

### 5.3. Benchmark Experiments

#### 5.3.1. Experimental Setup

We evaluated a range of LLMs listed in Table 3, from proprietary (e.g., GPT-5) to open-source (e.g., DeepSeek-R1), on five tasks in OOGIRI-MASTER. We report the accuracy as an evaluation metric. For API-based models, we averaged results over three trials. During inference, we set the temperature parameter to zero for all models.

We compared two prompting strategies when instructing the LLMs to solve each task. (1) a *baseline prompt* that simply instructs the model to select options, as shown in Figure 2, (2) an *insight-augmented prompt* that incorporates features computed from given prompt–response pairs based on the findings of our data analysis. To keep the prompts concise, we included only a small set of features selected with reference to the observed effect sizes in Table 2. Specifically, we used five basic features: length, unique character count, prompt–response length ratio, symbol ratio, and katakana ratio; and six LLM-scored features: ambiguity exploitation, associative distance, benign violation, incongruity resolution, metaphor use, and perspective shift. The basic features were precomputed and inserted directly into the prompt. LLM-scored features followed a two-step procedure: first, for each prompt–response pair, the target LLM computed scores for each aspect (e.g., metaphor use); second, these scores were included as context when instructing the model to select the options for each task.

To validate the human performance on this benchmark, we recruited crowdworkers from the

[^11]: To prevent data contamination, we sampled different data points from the analysis dataset in §4.



<!-- page 0007 -->

crowdsourcing platform<sup>12</sup> and asked them to solve each item using the same baseline prompt that was shown to the LLMs. Each item was answered by 21 workers, and the final labels were determined by majority vote. We included attention checks with unambiguous answers and aggregated the results only for the 21 workers who passed the checks for each item.

### 5.3.2. Results and Discussion

Table 3 lists the benchmark results. We compared two prompting strategies: a baseline prompt and an insight-augmented prompt.

**Baseline Prompt** When averaging the accuracy across the five tasks, Claude-Opus-4 performed the best (68.7%), followed by GPT-5 (67.6%) and Gemini-2.5-Pro (53.4%). Open LLMs lagged behind these proprietary LLMs; even the strongest, LLM-jp-3.1-13b$_{\mathrm{ja}}$, reached only 49.8%. Additionally, with the same instructions as those provided to the LLMs, the 21 crowdworkers achieved 68.7%, which is comparable to that of Claude-Opus-4. One possible reason that the human performance was relatively low compared with our expectations is the demographic mismatch between crowdworkers and users of the Oogiri platform.<sup>13</sup> Humor is subjective, and differences in age and interests can yield different judgments of funniness. Future studies will include analyses that account for annotator attributes and evaluations using more diverse raters.

**Insight-Augmented Prompt** With feature incorporation, four models, namely GPT-5, Gemini-2.5-Pro, DeepSeek-R1, and DeepSeek-R1$_{\mathrm{ja}}$, improved their average accuracy across the five tasks. Notably, GPT-5 increased from 67.6% to 70.7% (+3.1%), surpassing both human performance and Claude-Opus-4 in the baseline setting. This supports the effectiveness of the linguistic features that reflect the components of humor in improving Oogiri understanding. However, three models, namely Claude-Opus-4, gpt-oss-20b, and LLM-jp-3.1-13b$_{\mathrm{ja}}$, degraded. One possible factor is differences in the reasoning ability. Compared with the baseline, the insight-augmented prompt was longer and more complex because of the added features and instructions. Stronger reasoners (e.g., GPT-5) could correctly interpret these complex prompts and benefits, whereas weaker models (e.g., LLM-jp-3.1-13b$_{\mathrm{ja}}$) tended to misinterpret them and over-rely on feature magnitudes. For example, given the insight that funnier responses tend to be shorter, weaker models over-selected very short responses. This suggests that when reasoning is limited, instructing models to consider features can introduce overfitting problems and reduce performance.

### 5.3.3. Analysis

**Effectiveness of Continued Pretraining on Japanese Corpus** We compared the two models in Table 3, namely DeepSeek-R1 and DeepSeek-R1$_{\mathrm{ja}}$, which share the same architecture and parameter count; the only difference is the pretraining data. DeepSeek-R1$_{\mathrm{ja}}$ continues pretraining DeepSeek-R1 on a Japanese corpus.<sup>14</sup> DeepSeek-R1$_{\mathrm{ja}}$ improved the average accuracy across the five tasks from 41.3% to 44.6% in the baseline setting (+3.3 points) and from 41.4% to 46.0% in the insight-augmented setting (+4.6 points). As our benchmark is based on Japanese Oogiri, these results suggest that continued pretraining on a Japanese corpus is effective in improving Oogiri understanding. Although prior work has shown benefits for Japanese cultural and knowledge understanding (Tsutsumi and Jinnai, 2025), our findings indicate that such continued pretraining aids in the more advanced language understanding required for Japanese Oogiri.

**Ablation Study of Feature Groups** Table 4 presents the average accuracy over the five tasks for GPT-5 and Gemini-2.5-Pro under four settings: introducing only basic linguistic features, introducing only LLM-scored higher-order features, introducing both, and using the baseline with no features. In all cases, incorporating features into a prompt improved the average accuracy over the baseline. For GPT-5, using both feature groups yielded the best results. For Gemini-2.5-Pro, introducing only basic linguistic features (e.g., length and character-type ratios) performed the best. Notably, when introducing only basic linguistic features, both Gemini-2.5-Pro and GPT-5 improved more than when introducing higher-order features alone (e.g., +3.7 and +2.2 points, respectively). Response length was already identified in our analysis as a constituent component of humor, and the benchmark results empirically confirm that such simple heuristics can be effective criteria for evaluating funniness. These findings suggest that exploring a broad range of linguistic features is a promising direction for enhancing the humor understanding of LLMs further.

**Effect of Instruction Style for Feature Use** We also examined the influence of instruction style

<sup>12</sup>https://crowdsourcing.yahoo.co.jp/

<sup>13</sup>Because neither the crowdsourcing service nor the Oogiri platform discloses detailed user attributes, we could not perform a precise comparison; however, some differences in user populations are plausible.

<sup>14</sup>https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-14B-Japanese



<!-- page 0008 -->

<table>
<thead>
<tr>
<th rowspan="2">Models</th>
<th rowspan="2">Features</th>
<th colspan="1">Absolute.</th>
<th colspan="4">Relative.</th>
<th colspan="1">Ave.</th>
<th colspan="1">ΔAve.</th>
</tr>
<tr>
<th>Binary<sub>class</sub></th>
<th>Binary<sub>diff</sub></th>
<th>Binary<sub>same</sub></th>
<th>Triple</th>
<th>Quad</th>
<th>Accuracy</th>
<th>Accuracy</th>
</tr>
</thead>
<tbody>
<tr><td colspan="9"><strong>Open LLMs</strong></td></tr>
<tr><td>gpt-oss-20b</td><td>–</td><td>50.5</td><td>64.0</td><td>45.0</td><td>33.0</td><td>37.0</td><td>45.9</td><td>–</td></tr>
<tr><td>gpt-oss-20b</td><td>✓</td><td>54.0</td><td>52.0</td><td>57.0</td><td>27.0</td><td>22.0</td><td>42.4</td><td>-3.5</td></tr>
<tr><td>DeepSeek-R1-14b</td><td>–</td><td>48.5</td><td>56.0</td><td>43.0</td><td>31.0</td><td>28.0</td><td>41.3</td><td>–</td></tr>
<tr><td>DeepSeek-R1-14b</td><td>✓</td><td>46.0</td><td>57.0</td><td>49.0</td><td>24.0</td><td>31.0</td><td>41.4</td><td>+0.1</td></tr>
<tr><td>DeepSeek-R1-14b<sub>ja</sub></td><td>–</td><td>52.0</td><td>61.0</td><td>42.0</td><td>38.0</td><td>30.0</td><td>44.6</td><td>–</td></tr>
<tr><td>DeepSeek-R1-14b<sub>ja</sub></td><td>✓</td><td>50.0</td><td>59.0</td><td>53.0</td><td>44.0</td><td>24.0</td><td>46.0</td><td>+1.4</td></tr>
<tr><td>LLM-jp-3.1-13b<sub>ja</sub></td><td>–</td><td>47.0</td><td>80.0</td><td>45.0</td><td>39.0</td><td>38.0</td><td>49.8</td><td>–</td></tr>
<tr><td>LLM-jp-3.1-13b<sub>ja</sub></td><td>✓</td><td>50.5</td><td>58.0</td><td>45.0</td><td>30.0</td><td>28.0</td><td>42.3</td><td>-7.5</td></tr>
<tr><td colspan="9"><strong>Proprietary LLMs</strong></td></tr>
<tr><td>Claude-Opus-4</td><td>–</td><td>57.2</td><td>83.0</td><td><strong>70.0</strong></td><td>63.0</td><td><strong>70.3</strong></td><td>68.7</td><td>–</td></tr>
<tr><td>Claude-Opus-4</td><td>✓</td><td>50.8</td><td>72.7</td><td>68.0</td><td>53.0</td><td>51.3</td><td>59.2</td><td>-9.5</td></tr>
<tr><td>Gemini-2.5-Pro</td><td>–</td><td>51.3</td><td>62.0</td><td>61.7</td><td>46.3</td><td>45.7</td><td>53.4</td><td>–</td></tr>
<tr><td>Gemini-2.5-Pro</td><td>✓</td><td>50.8</td><td>58.7</td><td>66.3</td><td>51.3</td><td>47.0</td><td>54.8</td><td>+1.4</td></tr>
<tr><td>GPT-5</td><td>–</td><td><strong>61.7</strong></td><td>89.7</td><td>65.3</td><td>62.3</td><td>59.0</td><td>67.6</td><td>–</td></tr>
<tr><td>GPT-5</td><td>✓</td><td>60.0</td><td>93.3</td><td>69.0</td><td><strong>69.0</strong></td><td>62.0</td><td><strong>70.7</strong></td><td><strong>+3.1</strong></td></tr>
<tr><td>human</td><td>–</td><td>54.5</td><td><strong>95.0</strong></td><td>59.0</td><td>67.0</td><td>68.0</td><td>68.7</td><td></td></tr>
</tbody>
</table>

Table 3: Results of benchmark experiments. The best results for each column are **bolded**. “Ave. Accuracy” indicates the average accuracy (%) across five tasks, and “ΔAve. Accuracy” indicates the difference in average accuracy (%) when using features from our analysis.

<table>
<thead>
<tr>
<th rowspan="2">Models</th>
<th colspan="2">Features</th>
<th rowspan="2">Ave.<br>Acc.</th>
<th rowspan="2">ΔAve.<br>Acc.</th>
</tr>
<tr>
<th>Basic.</th>
<th>LLM-scored.</th>
</tr>
</thead>
<tbody>
<tr><td>Gemini-2.5-Pro</td><td>–</td><td>–</td><td>53.4</td><td>–</td></tr>
<tr><td>Gemini-2.5-Pro</td><td>✓</td><td>–</td><td><strong>57.1</strong></td><td><strong>+3.7</strong></td></tr>
<tr><td>Gemini-2.5-Pro</td><td>–</td><td>✓</td><td>54.5</td><td>+1.1</td></tr>
<tr><td>Gemini-2.5-Pro</td><td>✓</td><td>✓</td><td>54.8</td><td>+1.4</td></tr>
<tr><td>GPT-5</td><td>–</td><td>–</td><td>67.6</td><td>–</td></tr>
<tr><td>GPT-5</td><td>✓</td><td>–</td><td>69.8</td><td>+2.2</td></tr>
<tr><td>GPT-5</td><td>–</td><td>✓</td><td>68.0</td><td>+0.4</td></tr>
<tr><td>GPT-5</td><td>✓</td><td>✓</td><td><strong>70.7</strong></td><td><strong>+3.1</strong></td></tr>
</tbody>
</table>

Table 4: Ablation study on feature types. “ΔAve. Acc.” represents the difference in average accuracy compared to the model without any features. The best accuracy for each model is **bolded**.

| Models | Features | Uncertain | Ave. Accuracy |
|---|---|---|---|
| GPT-5 | – | – | 67.6 |
| GPT-5 | ✓ | – | 68.9 |
| GPT-5 | ✓ | ✓ | 70.7 |

Table 5: Ablation study on instruction styles. “Uncertain” indicates whether the uncertain instruction style is used. “Ave. Accuracy” indicates the average accuracy (%) across five tasks.

on performance when incorporating features into prompts, that is, how we should tell the model to use the features. We considered two styles: (1) instructing the model to use the features when judging funniness, and (2) instructing the model to consult the features only when uncertain. In our preliminary experiments, we first attempted style (1) and observed an over-reliance on feature magnitudes, which motivated the proposal of style (2). Table 5 shows the average accuracy of GPT-5 over the five tasks for the no-feature baseline and the two instruction styles. Here, the “Uncertain” column corresponds to style (2). In both styles, incorporating features improved over the baseline; notably, style (2) yielded the highest performance, improving the average accuracy by 3.1 points over the baseline. This indicates that asking the model to consider features only when uncertain helps to prevent overdependence on feature magnitudes and enables more appropriate use of the features. The results highlight instruction design as an important lever for improving the humor understanding of LLMs, and the value of exploring more effective instruction styles in future studies.

## 6. Conclusion

We presented a systematic study of humor on Oogiri-Corpus, and introduced Oogiri-Master, a benchmark covering relative and absolute judgments. Our analysis showed that multiple linguistic features, such as length and ambiguity, correlated with high-rated responses. In the benchmark experiments, we showed that incorporating these features into prompts improves the model performance. Furthermore, we demonstrated that continued pretraining on a Japanese corpus further boosts accuracy and instructing models to consider features only when uncertain mitigates over-reliance on heuristics. Future work will include ex-



<!-- page 0009 -->

ploring other effective linguistic features and refining prompt design, scaling human evaluations with annotator attributes, and extending the method to other languages and multimodal settings.

## 7. Ethics Statements

**Data Collection and Licensing** OOGIRI-CORPUS was constructed by collecting data from the public Japanese Oogiri competition platform, Oogiri Sogo. We confirm that the site explicitly permits web crawling, ensuring the legitimacy of the data collection process in §3. To promote transparency and facilitate further research, OOGIRI-CORPUS and OOGIRI-MASTER will be made available under the CC BY-NC-SA 4.0 license.

**Human Evaluation on OOGIRI-MASTER** We recruited crowdworkers for human baseline evaluation in §5. We used Yahoo! Crowdsourcing as the crowdsourcing platform. In accordance with the platform’s regulations, the compensation was set at 10 yen per 20 tasks. Workers were informed that the annotated results would be used for research purposes. In addition, we acknowledge that a potential demographic mismatch between the crowdworkers and Oogiri-platform users exists as discussed in §5.3.2, suggesting that a further analysis accounting for annotator attributes is necessary to improve the evaluation reliability.

## 8. Limitations

**Limited to Japanese Oogiri** Our analysis and benchmark are based on Japanese Oogiri data. Some humor depends on culture-specific knowledge (e.g., a response such as “Mount Fuji” may be funny to Japanese users because it evokes familiar shared knowledge), and similar effects may not hold in other languages or cultural contexts. Moreover, our feature analysis included Japanese-specific elements (e.g., character-type ratios), which may not be directly transferred. Future work should include collecting and analyzing Oogiri-like data in other languages and cultures to better understand the cross-lingual and cross-cultural variations in humor.

**Benchmark Scope Limited to Oogiri Understanding** We proposed a benchmark focused on understanding “funniness” in Oogiri: four MCQA subtasks and one binary classification task. However, humor understanding is related to other capabilities such as generation and explanation (Loakman et al., 2025). Although these are beyond the scope of this study, extending the benchmark to evaluate generation and explanation is an important direction for future research.

**Focus on Unimodal Settings** As discussed in Related Work (§2), Oogiri can be framed as text-to-text, image-to-text, or image&text-to-text (Zhong et al., 2024). We focused on the text-to-text approach for two reasons: (1) as a first step toward measuring LLM humor understanding, a unimodal text-only setup reduces complexity relative to multimodal settings, and (2) text-to-text Oogiri data are more abundant on the web, facilitating robust dataset construction and generalizable analysis. An important next step is to extend the dataset to multimodal variants and study humor understanding involving visual information.

## 9. Bibliographical References

Miriam Amin and Manuel Burghardt. 2020. A survey on approaches to computational humor generation. In *Proceedings of the 4th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature*, pages 29–41, Online. International Committee on Computational Linguistics.

J. Cohen. 1988. *Statistical Power Analysis for the Behavioral Sciences*. Lawrence Erlbaum Associates.

Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk, and Veselin Stoyanov. 2018. XNLI: Evaluating cross-lingual sentence representations. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 2475–2485, Brussels, Belgium. Association for Computational Linguistics.

R.M. Fano. 1961. *Transmission of Information: A Statistical Theory of Communication*. MIT Press Classics. MIT Press.

R.A. Fisher. 1925. *Statistical methods for research workers*. Edinburgh Oliver & Boyd.

Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. 2021. Deberta: Decoding-enhanced bert with disentangled attention. In *International Conference on Learning Representations*.

Jack Hessel, Ana Marasovic, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, and Yejin Choi. 2023. Do androids laugh at electric sheep? humor “understanding” benchmarks from the new yorker caption contest. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 688–714, Toronto, Canada. Association for Computational Linguistics.



<!-- page 0010 -->

Eftekhar Hossain, Omar Sharif, and Mohammed Moshiul Hoque. 2022. MemoSen: A multimodal dataset for sentiment analysis of memes. In *Proceedings of the Thirteenth Language Resources and Evaluation Conference*, pages 1542–1554, Marseille, France. European Language Resources Association.

EunJeong Hwang and Vered Shwartz. 2023. MemeCap: A dataset for captioning and interpreting memes. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 1433–1445, Singapore. Association for Computational Linguistics.

Taku Kudo, Kaoru Yamamoto, and Yuji Matsumoto. 2004. Applying conditional random fields to Japanese morphological analysis. In *Proceedings of the 2004 Conference on Empirical Methods in Natural Language Processing*, pages 230–237, Barcelona, Spain. Association for Computational Linguistics.

Moritz Lauer, Wouter van Atteveldt, Andreu Salleras Casas, and Kasper Welbers. 2022. Less Annotating, More Classifying – Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT - NLI. *Preprint.* Publisher: Open Science Framework.

Chen Liu, Gregor Geigle, Robin Krebs, and Iryna Gurevych. 2022. FigMemes: A dataset for figurative language identification in politically-opinionated memes. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*, pages 7069–7086, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.

Tyler Loakman, William Thorne, and Chenghua Lin. 2025. Who’s laughing now? an overview of computational humour generation and explanation. Preprint, arXiv:2509.21175.

Fuli Luo, Shunyao Li, Pengcheng Yang, Lei Li, Baobao Chang, Zhifang Sui, and Xu Sun. 2019. Pun-GAN: Generative adversarial network for pun generation. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, pages 3388–3393, Hong Kong, China. Association for Computational Linguistics.

P. McDonald. 2013. *The Philosophy of Humour.* Philosophy Insights. HEB Humanities E-Books.

A Peter McGraw and Caleb Warren. 2010. Benign violations: making immoral behavior funny. *Psychol. Sci.*, 21(8):1141–1149.

John Morreall. 2024. Philosophy of Humor. In Edward N. Zalta and Uri Nodelman, editors, *The Stanford Encyclopedia of Philosophy*, Fall 2024 edition. Metaphysics Research Lab, Stanford University.

Soichiro Murakami, Peinan Zhang, Hidetaka Kamigaito, Hiroya Takamura, and Manabu Okumura. 2025. AdParaphrase v2.0: Generating attractive ad texts using a preference-annotated paraphrase dataset. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 15212–15230, Vienna, Austria. Association for Computational Linguistics.

Khoi P. N. Nguyen and Vincent Ng. 2024. Computational meme understanding: A survey. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, pages 21251–21267, Miami, Florida, USA. Association for Computational Linguistics.

OpenAI. 2025. New embedding models and API updates. Accessed: 2025-10-21.

Graeme Ritchie. 2005. Computational mechanisms for pun generation. In *Proceedings of the Tenth European Workshop on Natural Language Generation (ENLG-05)*, Aberdeen, Scotland. Association for Computational Linguistics.

Graeme Ritchie. 2009. Variants of incongruity resolution. *Journal of Literary Theory (18625290)*, 3(2).

C. E. Shannon. 1948. A mathematical theory of communication. *The Bell System Technical Journal*, 27(3):379–423.

Shivam Sharma, Siddhant Agarwal, Tharun Suresh, Preslav Nakov, Md. Shad Akhtar, and Tanmoy Chakraborty. 2023. What do you meme? generating explanations for visual semantic role labelling in memes. *Proceedings of the AAAI Conference on Artificial Intelligence*, 37(8):9763–9771.

Ayuto Tsutsumi and Yuu Jinnai. 2025. Do large language models know folktales? a case study of yokai in Japanese folktales. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 16124–16146, Vienna, Austria. Association for Computational Linguistics.

Zhiwei Yu, Jiwei Tan, and Xiaojun Wan. 2018. A neural approach to pun generation. In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 1650–1660, Melbourne,



<!-- page 0011 -->

Australia. Association for Computational Linguis-
tics.

Shanshan Zhong, Zhongzhan Huang, Shanghua
Gao, Wushao Wen, Liang Lin, Marinka Zitnik,
and Pan Zhou. 2024. Let’s think outside the box:
Exploring leap-of-thought in large language mod-
els with creative humor generation. In *Proceed-
ings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR)*, pages
13246–13257.

## A. Prompt Example

Figure 3 presents a prompt template used to in-
struct LLMs to evaluate the higher-order linguistic
features for given prompt–response pairs.



<!-- page 0012 -->

<pre>You receive a prompt and a response, and your task is to evaluate how appropriate the response is for
the prompt.  Please evaluate the characteristics of the response to the prompt for the following “Oogiri”
scenario on a scale of 1-5.
Prompt:  {prompt}
Response:  {response}
Evaluate based on the following criteria and respond in JSON format.
In doing so, please explain the reasoning for the scores.

1) ambiguity_exploitation (1-5):  Use of Ambiguity
1:  The response does not exploit ambiguity.
3:  The response is somewhat ambiguous.
5:  The response effectively exploits ambiguity.

2) associative_distance (1-5):  Appropriateness of Association
1:  The association between prompt and response is direct OR requires 5 or more associative leaps.
3:  The association is reached in 1 step OR requires 4 steps with somewhat unnatural association.
5:  The association is naturally reached in 2-3 steps.

3) benign_violation (1-5):  Degree of Harmless Violation
1:  The response deviates from the prompt and is extremely harmful/offensive.
3:  The response deviates from the prompt and is somewhat harmful/offensive.
5:  The response deviates from the prompt but is harmless.

4) coherence (1-5):  Logical Coherence between prompt and Response
1:  The prompt and response are not logically connected.
3:  The prompt and response are somewhat logically connected.
5:  The prompt and response are perfectly logically connected.

5) expectedness (1-5):  Predictability of the Response
1:  The response is completely unexpected and surprising relative to the prompt.
3:  The response is somewhat unexpected or surprising relative to the prompt.
5:  The response is very predictable or obvious relative to the prompt.

6) incongruity_resolution (1-5):  Degree of Resolution of Incongruity
1:  The incongruity between the prompt and response is not resolved at all.
3:  The incongruity between the prompt and response is somewhat resolved.
5:  The incongruity between the prompt and response is naturally resolved.

7) metaphor_use (1-5):  Appropriateness of Metaphor Use
1:  The response does not use metaphor regarding the prompt.
3:  The response somewhat uses metaphor regarding the prompt.
5:  The response uses metaphor regarding the prompt.

8) perspective_shift (1-5):  Shift in Perspective
1:  The response shows no shift in perspective regarding the prompt.
3:  The response shows a partial shift in perspective regarding the prompt.
5:  The response shows a clear shift in perspective regarding the prompt.

Output Requirements:
- All scores must be integers (1-5).
- In the reasoning field, summarize the concise basis for each score in 1-3 sentences.
- Return in JSON format.

{
"reasoning":  "Reason for the scores",
"ambiguity_exploitation":  number,
"associative_distance":  number,
"benign_violation":  number,
"coherence":  number,
"expectedness":  number,
"incongruity_resolution":  number,
"metaphor_use":  number,
"perspective_shift":  number
}</pre>

Figure 3: Prompt for LLM-based scoring of higher-order linguistic features.
