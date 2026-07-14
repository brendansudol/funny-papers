<!-- Transcribed from x44-mame-re.pdf -->



<!-- page 0001 -->

arXiv:2602.15842v1 [cs.LG] 21 Jan 2026

# Memes-as-Replies: Can Models Select Humorous Manga Panel Responses?

**Ryosuke Kohita, Seiichiro Yoshioka**

CyberAgent  
{kohita_ryosuke, yoshioka_seiichiro}@cyberagent.co.jp

## Abstract

Memes are a popular element of modern web communication, used not only as static artifacts but also as interactive replies within conversations. While computational research has focused on analyzing the intrinsic properties of memes, the dynamic and contextual use of memes to create humor remains an understudied area of web science. To address this gap, we introduce the Meme Reply Selection task and present MAME-RE (Manga Meme Reply Benchmark),[^1] a benchmark of 100,000 human-annotated pairs (500,000 total annotations from 2,325 unique annotators) consisting of openly licensed Japanese manga panels and social media posts. Our analysis reveals three key insights: (1) large language models (LLMs) show preliminary evidence of capturing complex social cues such as exaggeration, moving beyond surface-level semantic matching; (2) the inclusion of visual information does not improve performance, revealing a gap between understanding visual content and effectively using it for contextual humor; (3) while LLMs can match human judgments in controlled settings, they struggle to distinguish subtle differences in wit among semantically similar candidates. These findings suggest that selecting contextually humorous replies remains an open challenge for current models.

[Figure: Three-panel overview. Visible headings/labels include “(a) Memes-as-Replies”, “SNS Post”, “Meme reply on SNS”, user names “Osamu” and “Budaō”, the post “Goodbye, holey socks! You’ve served me well but it’s time to let go 👋”, meme text “(YOU’RE GIVING UP ON HER?)”; “(b) Meme Reply Selection”, “Given a context, select the funniest meme reply”, “Context”, “Candidate memes (multiple possible replies)”, “Selected meme”; “(c) MAME-RE Benchmark”, “Exhaustive humor annotations for all context-meme pairs via crowdsourcing”.]

Figure 1: Overview of memes-as-replies. (a) Example of meme use on SNS. (b) Visualization of the Meme Reply Selection task. (c) MAME-RE benchmark with crowdsourced humor labels.

## Introduction

Memes are a popular element of modern web communication (Joshi, Ilievski, and Luceri 2024). People frequently use memes not just as static content, but as interactive replies within conversations (Wang et al. 2019; Fei et al. 2021). This practice enables creative and nuanced expressions that are difficult to convey through text alone (Grundlingh 2018). For example, in Figure 1(a), a user posts about their worn-out socks. In response, another user replies with a manga panel that dramatically asks, “YOU’RE GIVING UP ON HER?” This reply creates humor by repurposing the manga panel to treat the socks as a person. Such meme replies can express a wide range of humor, from playful teasing to irony, all of which rely on a deep understanding of context and implicit cultural knowledge (Davison 2012; Yus 2018; Sharma et al. 2022). While humans can intuitively grasp the social cues required for such humor, it reveals a significant limitation of current computational approaches (Nguyen and Ng 2024).

This gap between widespread human practice and limited computational understanding motivates our work to systematically analyze this core web phenomenon.

Most computational research on memes treats them as static content, like an isolated photograph, for analyzing intrinsic properties for tasks like harmfulness detection or humorous captioning (Shah et al. 2024; Sharma et al. 2020; Wang and Lee 2024; Loakman, Thorne, and Lin 2025). In contrast, our work focuses on the interactive function of memes as replies within a conversation. As illustrated in Figure 1(b), we define the *Meme Reply Selection* task, where the

[^1]: https://will.be.published.soon. Pronounced as /meım ri:/ (Maym-Re).



<!-- page 0002 -->

goal is to choose the funniest meme given a conversational context. This perspective recognizes that humor is not an intrinsic property of the meme itself, but an emergent quality of its interaction with context. This distinguishes our task from other forms of dialogue media selection, such as emojis or stickers, which typically prioritize simple semantic relevance (Wang and Jurgens 2021; Lu et al. 2023). We argue that modeling this dynamic and interactive use is essential to fully understand the role of memes in online communication.

We lay the foundation by formalizing the Meme Reply Selection task, making the nuanced act of humorous replies computationally tractable by defining the necessary data properties and a systematic evaluation framework. To support this task, we introduce the MAME-RE benchmark illustrated in Figure 1(c). The quality and scale of the benchmark are ensured through a rigorous crowdsourcing process, yielding annotations from five workers for each of the 100,000 pairs. Also, its exhaustive pairing design, where every context is matched with every meme, allows for a unique analysis of how a single image’s humorous potential changes with context. Finally, its openly licensed foundation ensures free redistribution and modification, fostering future research.

To demonstrate the challenges, our experiments show how current models handle contextual humor. Our analysis reveals that methods using large language models (LLMs) show an emerging ability to capture complex social cues in humor. Our qualitative analysis suggests that LLMs perform better because they can capture humorous strategies such as irony and exaggeration. In contrast, embedding-based methods focus on surface-level semantic similarity, producing replies that are contextually relevant but often lack the element of surprise essential to humor. Our analysis also identified several fundamental challenges. Current models found it difficult to effectively leverage visual information, with performance sometimes degrading when it was provided. Furthermore, while models perform well and can sometimes match human judgment when the humorous option is clearly distinguishable, they struggle with the more difficult and realistic task of selecting the best reply from a set of semantically similar candidates. These results indicate that the core challenges for this task lie in understanding multimodal humor cues, as well as discerning the subtle differences in wit that make a reply truly effective.

The main contributions of this paper are as follows:

- We propose treating memes as a form of interactive web communication, broadening the scope from the analysis of static artifacts to the dynamics of online conversation.
- We provide the foundational infrastructure for this paradigm: the formal Meme Reply Selection task and MAME-RE, a benchmark featuring 100,000 human-annotated context-meme pairs, built entirely with openly licensed materials to ensure broad reusability.
- We present the first comprehensive analysis of this benchmark, identifying fundamental challenges for current models in understanding nuanced, multimodal humor.

## Related Work

Our research lies at the intersection of web communication, multimodal analysis, and computational humor. This section moves from the broad context of online social interaction down to the specific, unaddressed challenge of modeling humorous meme replies.

**Web Communication and Multimodal Signals.** Early studies of online interaction explored how users creatively adapt text-based media to convey rich socioemotional information, compensating for the lack of non-verbal cues (Walther 1992, 1996; Dresner and Herring 2010). With the rise of social media, this adaptation has accelerated through the widespread integration of non-textual elements into digital conversations (Highfield and Leaver 2016). Simple visual cues like emojis and GIFs have become integral to online expression, helping users manage interpersonal dynamics and convey subtle emotional nuances (Hu et al. 2017; Jiang, Fiesler, and Brubaker 2018). Memes represent a more advanced form of this multimodal practice and have evolved into a sophisticated medium for communication. They are used for a wide range of purposes, including not only humor (Wu, Weber, and Müller 2025; Zhong et al. 2024) and hate speech (Kiela et al. 2020), but also political statements (Kulkarni 2017; Beskow, Kumar, and Carley 2020), social commentary (Alam et al. 2024), and marketing (Malodia et al. 2022).

**From Static Content to Interactive Replies.** Computational research has predominantly treated memes as static artifacts for content analysis (Sharma et al. 2020; Pramanick et al. 2021; Hossain, Sharif, and Hoque 2022; Wang and Lee 2024; Hwang and Shwartz 2023). This paradigm has proven valuable, advancing detection of harmful content (Zhuang et al. 2025), understanding meme contexts (Sharma et al. 2023b), and generating humorous captions (Zhang et al. 2024). However, the focus on intrinsic properties of memes overlooks another key aspect of how memes function in online communication: as an interactive reply. In this view, the meaning and humorous effect are not contained within the meme itself, but are generated by the interaction between the meme and the conversational context.

**Humor Mechanisms in Memes and Dialogue.** The landscape of memes is diverse, ranging from reaction GIFs that convey a short story (Wang and Jurgens 2021) to photographic templates that derive new meaning from user-generated captions (Chen et al. 2024). A useful lens for understanding meme replies is recontextualization (Bauman and Briggs 1990), the act of taking a piece of media with a fixed meaning and placing it in a new conversational context to create a surprising juxtaposition. While some dialogue system research has explored selecting visual replies like stickers or emojis, these studies have primarily focused on semantic relevance (Lu et al. 2023; Wang et al. 2019; Wang and Jurgens 2021), rather than evaluating the humorous quality of the reply. This leaves the specific challenge of generating humorous replies largely unaddressed.



<!-- page 0003 -->

## Problem Formulation

In this section, we formally define the task of meme reply selection, specify the dataset requirements, and propose evaluation metrics for assessing model performance.

**Task Definition.** Let the context be a natural-language utterance $c \in \mathcal{C}$, where $\mathcal{C}$ is the set of arbitrary contexts in natural language. Given a set of memes $\mathcal{M} = \{m_1, \ldots, m_{|\mathcal{M}|}\}$, the task is to select the funniest meme for a given context:

$$
\hat{m}(c) = \arg \max_{m \in \mathcal{M}} s(c, m),
$$

where $s(c, m)$ is a scoring function that measures the funniness of meme $m$ given the context $c$.

**Dataset Requirements.** To evaluate models for this task, we require a dataset $\mathcal{D}$ that consists of a finite set of contexts $\mathcal{C}_D = \{c_1, \ldots, c_{|\mathcal{C}_D|}\} \subset \mathcal{C}$, a finite set of memes $\mathcal{M}_D = \{m_1, \ldots, m_{|\mathcal{M}_D|}\} \subset \mathcal{M}$, and a real-valued scoring function $r : \mathcal{C}_D \times \mathcal{M}_D \to \mathbb{R}$, which assigns a funniness score to each context–meme pair. Thus, the dataset is represented as a set of annotated triples:

$$
\mathcal{D} = \{(c, m, r(c, m)) \mid c \in \mathcal{C}_D, m \in \mathcal{M}_D\}.
$$

**Evaluation Metric.** To evaluate model performance, we define Score@1 as the average reference funniness score of selected memes:

$$
\mathrm{Score@1} = \frac{1}{|\mathcal{C}_D|} \sum_{c \in \mathcal{C}_D} r(c, \hat{m}(c)),
$$

where $r(c, m)$ denotes the reference funniness score from the dataset. This metric directly evaluates our objective of selecting the most humorous meme reply for each given context.

## MAMe-RE: Manga Meme Reply Benchmark

This section introduces MAMe-RE, a dataset for the meme reply selection task. It is designed to serve as a fundamental resource for this new research area. To ensure data consistency and reusability, we focused on a single meme domain, Japanese manga panels taken from a single copyright-free source, *Black Jack ni Yoroshiku*.[^2] The benchmark comprises 250 synthetically generated social media contexts and 400 manga panels, which form 100,000 unique context-meme pairs. Each pair was evaluated by five independent crowdworkers on a binary funniness scale, yielding a total of 500,000 annotations.

**Content Collection and Curation.** We created the benchmark content with a focus on reusability and variety within a specific domain. We extracted 400 panels from *Black Jack ni Yoroshiku* (*Give My Regards to Black Jack* in English), provided by Sato Manga Works Ltd. under a free-use license that allows both commercial and non-commercial reproduction, public transmission, and a broad range of derivative uses, provided that attribution of the original title is maintained. The panels cover a wide range of characters, scenes, and emotions. For each panel, the in-panel speech text was transcribed, and GPT-4.1 was used to generate a visual description. We also prepared 250 synthetic social media contexts, generated by GPT-4.1 to mimic posts on X (formerly Twitter) and screened for relevance and diversity. We chose synthetic contexts instead of real posts to ensure privacy safety and open licensing, avoiding the ethical risks of scraping real tweets while maintaining the dataset’s reusability. We chose manga because its humor often arises from re-contextualizing original scenes without alteration, enabling a focused study of humor as an emergent property of the interaction between meme and context. Since both the images and the generated texts are based on freely licensed or synthetic content, the dataset is openly available and easy to reuse for further research.

[Figure: Crowdworker annotation interface screenshot. Top shows an SNS post in Japanese, a manga panel with Japanese speech bubbles, and radio-button choices labeled “面白い” and “面白くない”. Bottom shows an instruction box with headings “[Overview]”, “[Example]”, and “[Agreement]”, including bullet-point task instructions and “${CONSENT_STATEMENT}”.]

Figure 2: Crowdworker annotation interface and full task instruction for the funniness scoring task in MAMe-RE. Top: interface screenshot. Bottom: instruction text shown to annotators.

**Funniness Annotation.** To obtain ground-truth labels for humor, we conducted a crowdsourcing task involving 2,325 unique annotators on Yahoo! Crowdsourcing[^3] in which annotators were shown a context–meme pair and asked to make a binary judgment: *funny* or *not funny*. The annotation interface displayed the context, meme image, and a binary choice, with full task instructions shown to annotators (Figure 2). This controlled annotation setup allows us to isolate the humor signal from social factors such as post popularity or user influence. To ensure high-quality data, we included quality-control questions with explicit instructions and discarded submissions from annotators who failed them. Anno-

[^2]: https://densho810.com/free/. All data and annotations are in Japanese; English translations are provided for clarity.

[^3]: https://crowdsourcing.yahoo.co.jp/



<!-- page 0004 -->

tators were informed that responses would be used for academic research and provided consent through the platform interface. No personal or demographic information (e.g., age, gender, cultural background) was collected, as such information was not available through the crowdsourcing platform; only aggregate, anonymized responses were used.[^4] The final funniness score for each pair is defined as the proportion of annotators who judged it to be funny. We adopted the binary format, simply asking whether a reply is funny or not, based on preliminary experiments.[^5]

**Dataset Statistics.** The MAME-RE dataset consists of 250 contexts and 400 manga panels, forming 100,000 unique context-meme pairs with five annotations each, yielding a total of 500,000 annotations. The overall inter-annotator agreement, measured by Fleiss’ $\kappa$, is -0.022, reflecting the profound subjectivity of humor. However, this low overall agreement does not imply that the annotations are random noise. Crucially, a substantial portion of the data reached high levels of consensus: 20.4% of pairs achieved unanimous agreement (a score of 0.0 or 1.0), and an additional 21.8% had high agreement (a score of 0.2 or 0.8). This demonstrates that while many pairs are subjective, a significant subset elicits consistent judgments, providing a solid foundation for evaluating models.

## Reply Selection Methods

We investigate two different strategies for meme reply selection: (i) similarity-based selection, which relies on indirect semantic matching, and (ii) preference-based selection, which directly models funniness given the context.

**Similarity-based Selection (`sim-select`).** This approach selects memes by measuring cosine similarity between the context and each candidate meme in embedding space. This score serves as an indirect proxy for funniness, relying on the assumption that similar memes are more likely to be suitable and funny replies. Specifically, we use a text encoder $f_c$ to obtain $f_c(c) \in \mathbb{R}^d$ for the context, and text or multimodal encoders $f_m$ to obtain $f_m(m) \in \mathbb{R}^d$ for the memes. The meme with the highest cosine similarity to the context is selected:

[^4]: Annotators were compensated at approximately 200 JPY per hour (10 JPY per batch of 50 annotations, with an average completion time of three minutes per batch). This rate was set with reference to the standard for simple questionnaire crowdsourcing tasks in Japan (typically 50-300 JPY per hour) and was two-four times higher than the compensation for other comparable tasks on the same platform. This study was deemed exempt from IRB review as minimal-risk research using only anonymized, aggregated responses with no collection of personal information.

[^5]: We initially considered a multi-level Likert scale for graded humor ratings. However, pilot annotations revealed that distinguishing fine-grained degrees of funniness was difficult for annotators, resulting in inconsistent and noisy labels. The higher cognitive load required for ranking also appeared to degrade annotation quality. In contrast, the binary judgment of funny or unfunny is intuitive and easy to answer, and aligns well with our goal of selecting a funny reply. Given these findings and the exploratory nature of this benchmark, we opted for the simpler binary approach.

[Figure: Prompt template with instructions, output format, candidates, and post context.]

    [Instructions]
    You will be given a post and a set of meme candidates.
    Select the funniest reply to the post from the candidates.
    Meme candidates appear in CSV with the columns: ${FORMAT}
    Choose the single option that will be the funniest.

    [Output Format]
    Output only the ID.
    Do not include any extra wording or markup.

    [Candidates]
    ${CANDIDATES}

    --------------
    post: {context}

Figure 3: Prompt template. ${FORMAT} has “*id, speech*” or “*id, speech, description*” and ${CANDIDATES} have meme candidates in the corresponding csv format.

$$
\hat{m}(c) = \arg \max_{m \in \mathcal{M}} \cos(f_c(c), f_m(m)).
$$

The embedding $f_m(m)$ can use speech text, panel description, or the image. In our experiments, we implement $f_m$ with four model types: text embeddings (Text-Emb), LLM embeddings (LLM-Emb), multimodal embeddings (Multi-Emb), and vision-language model embeddings (VLM-Emb). For text inputs, we use either speech text alone or with the panel description. Multi-Emb uses only the image, while VLM-Emb incorporates both speech text and panel image.

**Preference-based Selection (`pref-select`).** Preference-based selection directly estimates the funniness of each candidate given the context, rather than relying on vector proximity. Specifically, given a context $c$ and meme set $\mathcal{M}$, a preference function $f_p$ evaluates candidates and selects the meme judged funniest by the model:

$$
\hat{m}(c) = f_p(c, \mathcal{M}).
$$

In our experiments, we implement $f_p$ using LLMs with prompts instructing the model to choose the funniest meme (Figure 3), corresponding to the standard multiple-choice question answering (Hendrycks et al. 2021; Robinson and Wingate 2023). For meme information in the prompts, we use either speech text alone or with the panel description, mirroring the `sim-select` setting.

## Experiments

Our experiments are designed as a sequential investigation to identify the core challenges in humorous meme reply selection. We begin in Exp1 with a broad comparison of `sim-select` and `pref-select` methods to establish baseline performance. Finding that `pref-select` is promising but limited, we test a standard retrieve-and-rerank architecture in Exp2, which surprisingly fails to improve performance. To understand this failure, Exp3 simplifies the task to test if models can select a clearly humorous meme from a set of non-humorous ones. After confirming that the models can, Exp4 directly tests our final hypothesis: that performance drops when models must choose from a pool of



<!-- page 0005 -->

semantically similar candidates. Finally, our case study provides a qualitative analysis of the models’ humor generation strategies.

## Overall Settings

We used Score@1 as our primary evaluation metric, which directly measures how often the system selects a meme reply judged to be funny in each context. To account for the inherent subjectivity of humor, we also report the Consensus Hit Rate (CHR), defined as the rate of selecting memes that all five annotators unanimously judged as funny, and nDCG to evaluate model performance from a retrieval and ranking perspective. For similarity-based selection, we evaluated 21 model variants across four model types, focusing on Japanese-optimized models. In this section, we report results from the top-performing models in each category: Sarashina-Text-Emb and OpenAI-Text-Emb for Text-Emb; Calm2-LLM-Emb and Qwen2.5-LLM-Emb for LLM-Emb; LAION-CLIP-Multi-Emb and Jina-CLIP-Multi-Emb for Multi-Emb; EvoVLM-VLM-Emb and Sarashina-VLM-Emb for VLM-Emb. For preference-based selection, we used six production-grade LLMs: GPT-5, GPT-5-mini, GPT-OSS, Gemini 2.5 Pro, Gemini 2.5 Flash, and Claude 4 Sonnet.^6

## Exp1: Main Results

Figure 4a shows the results of Exp1. The `pref-select` method using GPT-5 achieved a Score@1 of 0.325 when using panel descriptions. For `sim-select` methods, Sarashina-Text-Emb achieved 0.320 without descriptions. Calm2-LLM-Emb (LLM-Emb) achieved 0.306, while multimodal and vision-language models showed lower scores: Jina-CLIP-Multi-Emb (0.282) and EvoVLM-VLM-Emb (0.263). This pattern reveals that methods capable of reasoning about contextual humor (`pref-select`) outperform those relying on semantic similarity alone, and that visual information does not consistently improve performance. To assess the ranking quality of the `sim-select` methods, we also calculated nDCG@5. While these scores were broadly consistent with the Score@1 rankings, the performance differences among the top models were marginal.

Figure 4b shows the effect of including textual panel descriptions on model performance. Overall, the results indicate that providing these descriptions did not consistently improve scores. For the `pref-select` and Text-Emb models, performance slightly decreased when descriptions were included. Only the LLM-Emb models showed a minor benefit. Since the score ranges with and without descriptions largely overlap, this additional text offered limited benefit.

This finding, combined with the poor performance of models that directly process images, highlights a significant challenge: current models struggle to use visual information effectively, whether it is provided as text or as pixels.

To address concerns about annotation reliability raised by low overall agreement, we evaluated models on a high-agreement subset where ground truth is defined strictly as pairs with a funniness score ≥ 0.8 (unanimous or near-unanimous agreement). The Consensus Hit Rate (CHR) (the proportion of universally funny memes selected by each model) is shown in Figure 4a. GPT-5 with description achieved the highest consensus hit rate of 0.052 (±0.016), which is approximately 3.5 times higher than the random baseline (0.015) and 2.2 times higher than Sarashina-Text-Emb without description (0.024, ±0.019). This demonstrates that LLMs maintain their advantage even when evaluated on the most reliable subset of annotations, validating our findings in a noise-free setting. However, the absolute performance remains low (only 5.2% of universally funny memes are selected), highlighting the persistent challenge of humor detection.

To better understand model behavior, we analyzed the distribution of funniness scores for the memes selected by each model. Figure 4c shows the score distributions for the LLMs used in the `pref-select` approach. GPT-5 and GPT-5-mini effectively avoided completely unfunny memes (score of 0.0), selecting them less than 10% of the time. These models also selected funny memes (scores ≥ 0.6) more often than the other LLMs. In contrast, Claude 4 was more likely to choose memes with a score of zero and less likely to select highly rated ones. These different patterns suggest that LLMs have varying abilities to understand and select for humor.

Figure 4d presents the distributions for the `sim-select` models. The Text-Emb and LLM-Emb models show an advantage in avoiding zero-score memes compared to multimodal models. At the higher end of the funniness scale, the differences were less pronounced, though Text-Emb and LLM-Emb models performed slightly better. This suggests that text-based similarity is effective at capturing enough semantic relevance to avoid completely inappropriate replies. Conversely, the frequent selection of such memes by multimodal models may indicate a fundamental difficulty in grasping contextual relevance from visual information for this task.

## Exp2: Retrieve-and-Rerank Approach

**Settings** In this experiment, we examined a hybrid retrieve-and-rerank approach, combining the `sim-select` and `pref-select` methods. This method first utilizes `sim-select` to retrieve the top-k similar candidates for a given context. Subsequently, a `pref-select` model is employed to identify the most humorous option from this reduced set. For the retrieval step, we used Sarashina-Text-Emb, the top-performing similarity-based model from Exp1. For the selection step, we evaluated three large language models chosen from our Exp1 results to represent a range of top-performing proprietary and open models: GPT-5, Gemini 2.5 Pro, and GPT-OSS. To better interpret their perfor-

---

^6 Model details: sarashina-embedding-v1-1b and text-embedding-3-large for Text-Embs, CLIP-ViT-H-14-frozen-xlm-roberta-large-laion5B-s13B-b90k and jina-clip-v2 for Multimodal-Embs, Calm2-7b and Qwen2.5-7B for LLM-Embs, and sarashina2-vision-8b and Llama-3-EvoVLM-JP-v2 for VLM-Embs. gpt-5-2025-08-07, gpt-5-mini-2025-08-07, gpt-oss-120b, gemini-2.5-flash, gemini-2.5-pro, and claude-sonnet-4-20250514 for LLMs. For compute resources, preference-based selection used commercial APIs (OpenAI, Google, Anthropic), while similarity-based models were run on a single NVIDIA A100 GPU.



<!-- page 0006 -->

| Model | Desc | Score@1 | CHR | nDCG@5 |
|---|---:|---:|---:|---:|
| **GPT-5 (P)** | **Y** | **0.325 (±0.014)** | **0.052 (±0.016)** | - |
| GPT-5 mini (P) | N | 0.322 (±0.014) | 0.045 (±0.015) | - |
| **Sarashina-Text-Emb (S)** | **N** | **0.320 (±0.022)** | 0.024 (±0.019) | 0.317 |
| GPT-5 (P) | N | 0.314 (±0.014) | 0.048 (±0.015) | - |
| OpenAI-Text-Emb (S) | N | 0.307 (±0.024) | 0.032 (±0.022) | 0.321 |
| **Calm2-LLM-Emb (S)** | **Y** | **0.306 (±0.024)** | 0.028 (±0.020) | 0.284 |
| GPT-5 mini (P) | Y | 0.300 (±0.013) | 0.024 (±0.011) | - |
| Qwen2.5-LLM-Emb (S) | Y | 0.299 (±0.023) | 0.032 (±0.022) | 0.278 |
| Gemini 2.5 Flash (P) | N | 0.296 (±0.014) | 0.029 (±0.012) | - |
| Calm2-LLM-Emb (S) | N | 0.295 (±0.023) | 0.024 (±0.019) | 0.294 |
| Gemini 2.5 Pro (P) | Y | 0.294 (±0.014) | 0.033 (±0.013) | - |
| GPT-OSS (P) | N | 0.292 (±0.014) | 0.035 (±0.013) | - |
| Gemini 2.5 Pro (P) | N | 0.286 (±0.014) | 0.032 (±0.013) | - |
| OpenAI-Text-Emb (S) | Y | 0.285 (±0.024) | 0.020 (±0.017) | 0.314 |
| Sarashina-Text-Emb (S) | Y | 0.285 (±0.023) | 0.012 (±0.013) | 0.294 |
| GPT-OSS (P) | Y | 0.284 (±0.014) | 0.024 (±0.011) | - |
| **Jina-CLIP-Multi-Emb (S)** | **N** | **0.282 (±0.025)** | 0.020 (±0.017) | 0.294 |
| LAION-CLIP-Multi-Emb (S) | N | 0.280 (±0.025) | 0.028 (±0.020) | 0.289 |
| Claude 4 (P) | N | 0.280 (±0.013) | 0.041 (±0.046) | - |
| Qwen2.5-LLM-Emb (S) | N | 0.279 (±0.023) | 0.016 (±0.016) | 0.289 |
| Gemini 2.5 Flash (P) | Y | 0.276 (±0.014) | 0.023 (±0.011) | - |
| **EvoVLM-VLM-Emb (S)** | **N** | **0.263 (±0.022)** | 0.012 (±0.013) | 0.262 |
| Claude 4 (P) | Y | 0.261 (±0.013) | 0.000 (±0.000) | - |
| Sarashina-VLM-Emb (S) | N | 0.261 (±0.023) | 0.020 (±0.017) | 0.280 |
| Random | - | 0.255 (±0.001) | 0.015 (±0.015) | 0.271 |

(a) Performance ranking (Exp1).

[Figure: (b) Box plot by description. Legend: w/ Description, w/o Descriptions. Axes labeled Score and Models; model groups include LLM (P), Text-Emb (S), LLM-Emb (S), Multi-Emb (S), VLM-Emb (S).]

(b) By description

[Figure: (c) Histogram by LLMs. Legend includes GPT-5, Gemini 2.5 Pro, GPT-OSS, GPT-5 mini, Gemini 2.5 Flash, Claude 4. Axes labeled Percent (%) and Score.]

(c) By LLMs

[Figure: (d) Histogram by embeddings. Legend includes Text-Emb, LLM-Emb, Multi-Emb, VLM-Emb. Axes labeled Percent (%) and Score.]

(d) By embeddings

Figure 4: Main experimental results for Exp1. (a) **Table** showing the performance ranking across models and methods. S/P: similarity/preference-based; Y/N: with/without descriptions; CHR: Consensus Hit Rate; values in parentheses denote 95% confidence intervals. (b)–(d) **Plots** of score distributions categorized by panel descriptions, LLMs, and embedding models respectively.

[Figure: Bar and line chart showing performance of retrieve-and-rerank approach. Legend includes GPT-5, Gemini 2.5 Pro, GPT-OSS, Oracle, Random. Y-axis: Score. X-axis: Candidate size ($k$), with ticks 4, 8, 12, 16, 32, 64, 128, 256, 400. A dashed horizontal line is labeled “Embedding ($k=1$): 0.320”; Oracle line has labeled values 0.48, 0.55, 0.60, 0.64, 0.70, 0.76, 0.82, 0.85, 0.87.]

Figure 5: Performance of the retrieve-and-rerank approach (Exp2).

mance, we established two baselines: Random, which randomly selects a meme from the $k$ candidates, and Oracle, which serves as an oracle upper bound by always choosing the candidate with the highest ground-truth funniness score within the retrieved set.

**Results** Figure 5 shows the results of our retrieve-and-rerank approach. A key observation is the notable gap between the oracle upper bound and the actual performance of the `pref-select` models. The rising oracle baseline indicates that the initial retrieval phase successfully included high-quality candidates in the selection pool, even for small values of $k$; for example, Score@1 reached 0.48 at $k = 4$ and 0.55 at $k = 8$. However, the models did not effectively leverage this advantage.

The performance of the `pref-select` models remained near or below the dashed line representing the standalone `sim-select` baseline of 0.320. This suggests that adding a `pref-select` step did not yield a consistent improvement over the simpler retrieval method. The models showed different behaviors as the candidate pool size $k$ varied. The performance of GPT-5 was highly stable, with scores showing little variation around 0.31 regardless of $k$. In contrast, Gemini 2.5 Pro and GPT-OSS showed a tendency for their performance to degrade as $k$ increased. Specifically, their scores dropped at $k \geq 256$.

This result indicates a mixed pattern of behavior. The stability of GPT-5 suggests that for some models, the task’s difficulty is not a function of the number of candidates, which appears to contradict the common *lost-in-the-middle* problem in LLMs (Li et al. 2024; Liu et al. 2024). Conversely, the performance decline of other models suggests a degree



<!-- page 0007 -->

[Figure: Bar chart showing performance on selecting from distinguishable candidates. Legend: GPT-5, Gemini 2.5 Pro, GPT-OSS, Embedding, GPT-5 Vision, Gemini 2.5 Pro Vision, Human. Y-axis: Score. X-axis: Candidate size ($k$), with groups 4, 8, 12.]

Figure 6: Performance on selecting from distinguishable candidates (Exp3). Human and vision-language models are included as baselines.

<table>
<thead>
<tr>
<th rowspan="2">$k$</th>
<th rowspan="2">Model</th>
<th colspan="3">Candidate Similarity</th>
<th rowspan="2">$\Delta$</th>
</tr>
<tr>
<th>Low</th>
<th>Mid</th>
<th>High</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">4</td>
<td>GPT-5</td>
<td>0.457</td>
<td>0.459</td>
<td>0.437</td>
<td>-0.020</td>
</tr>
<tr>
<td>Gemini 2.5 Pro</td>
<td>0.467</td>
<td>0.468</td>
<td>0.444</td>
<td>-0.023</td>
</tr>
<tr>
<td>GPT-OSS</td>
<td>0.457</td>
<td>0.456</td>
<td>0.385</td>
<td>-0.072</td>
</tr>
<tr>
<td rowspan="3">8</td>
<td>GPT-5</td>
<td>0.396</td>
<td>0.416</td>
<td>0.379</td>
<td>-0.017</td>
</tr>
<tr>
<td>Gemini 2.5 Pro</td>
<td>0.389</td>
<td>0.400</td>
<td>0.375</td>
<td>-0.014</td>
</tr>
<tr>
<td>GPT-OSS</td>
<td>0.402</td>
<td>0.386</td>
<td>0.348</td>
<td>-0.054</td>
</tr>
<tr>
<td rowspan="3">12</td>
<td>GPT-5</td>
<td>0.365</td>
<td>0.365</td>
<td>0.356</td>
<td>-0.009</td>
</tr>
<tr>
<td>Gemini 2.5 Pro</td>
<td>0.370</td>
<td>0.371</td>
<td>0.356</td>
<td>-0.014</td>
</tr>
<tr>
<td>GPT-OSS</td>
<td>0.371</td>
<td>0.355</td>
<td>0.341</td>
<td>-0.030</td>
</tr>
</tbody>
</table>

Table 1: LLM performance under different candidate similarities. $\Delta$ represents the performance change between the Low and High similarity conditions. (Exp4).

of sensitivity to context length. Overall, these results suggest that the limited improvement may not stem from the retrieval process itself, but rather from the difficulty of distinguishing subtle differences in humor among semantically similar candidates.

## Exp3: Distinguishable Candidate Selection

**Settings** To better understand why the retrieve-and-rerank approach from Exp2 was limited, we designed a controlled experiment with a simplified task. The goal was to test two basic hypotheses under controlled conditions: (1) that models can reliably select a distinctly humorous meme from a set of less funny alternatives, and (2) that performance would decrease as the number of candidates $k$ increases. To do this, we constructed test sets where each contained one funny meme (score $\geq 0.8$), half the candidates ($k/2$) were unfunny memes (score $\leq 0.2$), and the remaining ones were somewhat funny ($0.2 <$ score $< 0.8$).

In addition to the models from our previous experiments, we included two additional baselines for a comprehensive comparison. First, we collected human performance data through a crowdsourced selection task to serve as a practical reference. Second, to assess the role of visual understanding, we evaluated vision-language models (GPT-5 Vision, Gemini 2.5 Pro Vision). For these models, all candidate images for a given context were combined into a single grid image, and the model was prompted to select the best option from this composite image.

**Results** As shown in Figure 6, the results from this controlled experiment were consistent with the hypotheses. First, the LLMs were effective at identifying the target funny meme, with scores up to 0.46. Second, unlike in Exp2, there was a clear decrease in performance as $k$ increased for both the models and the human reference. For instance, the scores for GPT-5 were 0.46, 0.41, and 0.37 for $k$=4, 8, and 12, respectively.

While the artificial setting of this experiment limits its real-world applicability, it reveals important aspects of model behavior. The results show that when a humorous option was clearly distinguishable, the `pref-select` models were close to, and in some cases slightly higher than, the average human performance on this task. This success was not replicated by the vision-language models, whose poor performance indicated that a deep understanding of visual humor remains a challenge. The experiment highlights a key distinction: while models can approach human performance on tasks with clear signals, their ability to navigate more complex, real-world scenarios has not yet been demonstrated.

## Exp4: Sensitivity to Candidate Similarity

**Settings** In Exp3, we observed that LLMs performed well when funny memes were clearly distinguishable from less funny ones. Building on this observation, we examined how LLM performance changes when the candidate memes become more similar to each other, extending the controlled setting of Exp3. This follows the implication from Exp2 that the retrieve-and-rerank approach may have been limited by the high similarity among retrieved candidates, creating a *hard negative* scenario that makes it difficult for the reranker to identify the single best option.

To test this hypothesis, we modified the evaluation sets from Exp3. We retained the funny candidates (score $\geq 0.8$) and resampled the other candidates based on their similarity to the funny one, using the similarity threshold $t$. We selected only candidates whose similarity score with the funny meme exceeded this threshold. This approach allowed us to control the similarity within the candidate pool. We used three thresholds ($t$={-2,0,2}), based on the standardized cosine similarity from Sarashina-Text-Emb embeddings, denoting these conditions as Low, Mid, and High, respectively. The Low condition contains a diverse set of candidates, whereas the High condition requires the model to distinguish the funny meme from a pool of semantically similar yet unfunny alternatives.

**Results** Table 1 shows the results. As hypothesized, LLM performance generally decreased as the similarity between candidates increased. This effect was most pronounced for smaller candidate pools ($k$=4), suggesting that high similarity makes it more difficult for the models to identify the funniest meme. As $k$ increased, the performance drop be-



<!-- page 0008 -->

[Figure: Bar chart showing score distributions for Sarashina-Text-Emb and GPT-5. x-axis: Score (0.0, 0.2, 0.4, 0.6, 0.8, 1.0); y-axis: Percent (%). Legend: Sarashina-Text-Emb, GPT-5. Values shown include Sarashina-Text-Emb 7.2, 43.6, 34.0, 12.8, 2.0, 0.4 and GPT-5 6.4, 47.6, 29.2, 11.6, 4.5, 0.7.]

Figure 7: Score distributions of Sarashina-Text-Emb and GPT-5.

came smaller. This suggests that the challenge of processing a larger number of candidates may outweigh the difficulty caused by their similarity. This effect was also stronger for GPT-OSS, which, as a less powerful model, was more affected by this hard negative scenario.

These findings suggest that LLMs struggle to distinguish subtle differences in humor among semantically similar candidates. This observation offers a plausible explanation for the limited performance of the retrieve-and-rerank approach in Exp2. It is possible that the initial retrieval step in that experiment created a pool of highly similar candidates, making it difficult for LLMs to discern the most humorous option.

## Case Study

This section analyzes how the `sim-select` and `pref-select` approaches create humor by examining their patterns of success and failure. We focus on the outputs of Sarashina-Text-Emb and GPT-5, the best-performing models from each method. An analysis of their overall performance in Figure 7 reveals two distinct behavioral patterns. The approach of Sarashina-Text-Emb is reliable but conservative; it tended to select memes that are moderately funny but semantically close to the context. In contrast, GPT-5 showed a high-risk, high-reward pattern, more frequently selecting very funny replies. To understand the mechanisms that produce these different outcomes, we now examine specific examples in Table 2.

The `sim-select` model, Sarashina-Text-Emb, succeeds when its keyword-matching mechanism produces unexpectedly complex humor like personification or irony. In case (A), a simple match for “fast” selects the meme “HE’S JUST SO FAST...” The humor arose not from the word match itself, but because the reply personifies the Wi-Fi with an overly dramatic, human-like reaction. This pattern continued in case (B), where a more subtle match for “lost” selects “LATELY I DON’T UNDERSTAND MYSELF.” This reply unexpectedly reinterprets a simple problem as a deep philosophical one, producing humor through its sudden exaggeration. Finally, in case (C), a literal match for “I give up” resulted in a blunt, agreeing reply (“GIVE UP.”). The humor here comes from its cold, dismissive tone, which is the opposite of the supportive reaction expected from a typical conversational agent.

| Context | Sarashina-Text-Emb<br>(Similarity-based) | GPT-5<br>(Preference-based) |
|---|---|---|
| (A) *The Wi-Fi at my new place is seriously fast!* | ✓ (0.8)<br>[Figure: manga panel with text “HE’S JUST SO FAST...” and “HE’S FAST...”] | ✓ (0.8)<br>[Figure: manga panel with text “HE’S JUST SO FAST...” and “HE’S FAST...”] |
| (B) *I think I’m lost...* | ✓ (1.0)<br>[Figure: manga panel with text “LATELY I DON’T UNDERSTAND MYSELF.”] | ✗ (0.2)<br>[Figure: manga panel with text “I CAN GO ANY-WHERE!”] |
| (C) *I’m done. I give up.* | ✓ (0.6)<br>[Figure: manga panel with text “GIVE UP.”] | ✗ (0.2)<br>[Figure: manga panel with text “COME BACK!”] |
| (D) *Just found a 10-year-old pudding in the back of my fridge...* | ✗ (0.2)<br>[Figure: manga panel with text “YOU USED TO BE COOLER THAN THAT.”] | ✓ (0.8)<br>[Figure: manga panel with text “THIS IS POISON.”] |
| (E) *Rumor has it that chocolate makes you 3x more productive when studying.* | ✗ (0.2)<br>[Figure: manga panel with text “HISTORY IS MY BEST SUBJECT!” and “MY MEMORY IS SECOND TO NONE!”] | ✓ (0.8)<br>[Figure: manga panel with text “IS TIMES.”] |
| (F) *Maybe life without a smartphone isn’t so bad after all.* | ✗ (0.2)<br>[Figure: manga panel with text “NOTHING.”] | ✓ (1.0)<br>[Figure: manga panel with text “I REFUSE.”] |
| (G) *Whoops, I gamed straight through to the morning.* | ✗ (0.2)<br>[Figure: manga panel with text “I ONLY SLEPT 2 HOURS!”] | ✗ (0.2)<br>[Figure: manga panel with text “I ONLY SLEPT 2 HOURS!”] |

Table 2: Examples of selected replies by Sarashina-Text-Emb (similarity-based) and GPT-5 (preference-based). Numbers in parentheses represent funniness score.



<!-- page 0009 -->

In contrast, the `pref-select` model GPT-5 excels at understanding context that goes beyond simple keywords. This contextual inference is clear in case (D). While the `sim-select` model failed due to a superficial connection between “*fridge*” and “*cool*,” GPT-5 infers the dangerous nature of the “*10-year-old pudding*” and provided the fitting reply, “*THIS IS POISON.*”. Another key strength of GPT-5 was its ability to create a humorous persona. This was illustrated in case (E), where the simple association made by Sarashina-Text-Emb between “*studying*” and related keywords like “*memory*,” “*history*,” or “*subject*” was not effective. GPT-5, however, adopts the persona of a confident expert making an overconfident claim. The core of the humor lies in its statement, “*15 TIMES.*”. It directly builds on the “*3x*” in the context, absurdly escalating it with a larger, baseless number. This overconfidence makes the reply far funnier. Likewise, in case (F), the direct “*I REFUSE*” to living without a smartphone created another strong, humorous personality. In these instances, the humor arose from the character the reply embodies, making it more effective than the simple associations of the `sim-select` model.

However, both models can fail when a contextually relevant reply is too obvious and lacks an element of surprise. This is evident in case (G), where for the context “*gamed straight through to the morning*,” both models had selected the most predictable meme: “*I ONLY SLEPT 2 HOURS...*”. While this reply is perfectly relevant, it is also highly predictable and therefore received a low humor score. This highlights a core challenge for automated humor generation: models need to distinguish simple contextual relevance from genuine, surprising humor.

In summary, these case studies show that the `sim-select` method provides reliable relevance but struggles to create high-impact humor consistently. The `pref-select` approach shows greater potential for more complex, context-aware humor, but it must also avoid predictable responses to be truly effective.

## Discussion

In this section, we discuss what our findings reveal about the broader challenges of modeling humor in online communication. We focus on two complementary perspectives: (1) what these results suggest about multimodal and social understanding in current systems, and (2) how they inform future directions for building more contextually aware conversational models.

### Implications for Computational Humor

**LLMs Show Preliminary Evidence of Capturing Social Cues** Our results show that `pref-select` methods using LLMs demonstrate advantages over `sim-select` methods. While the difference in scores was small, our case studies suggest this advantage comes from a more advanced capability. LLMs appear to capture complex social cues such as irony and exaggeration, going beyond the surface-level semantic relevance that `sim-select` methods rely on. This finding suggests that computational models are moving beyond simple relevance matching and are starting to develop an ability to reason about the social and contextual nature of humor as it is used on the web. These results suggest that LLMs can represent some social cues, but how these representations translate into explicit humor judgments remains an open question.

**The Gap Between Understanding and Using Multimodal Memes** Through our experiments, we identified the difficulty of using visual information. Providing visual information, either as text descriptions or direct images, failed to improve performance. It was particularly ineffective for models that process images directly. This points to a critical distinction between understanding and using visual humor. While prior work shows that models can achieve some success in interpretation tasks like classifying a meme’s sentiment or explaining its humor (Sharma et al. 2023a), our findings suggest this understanding does not easily translate into effective action. The difficulty seems to arise when models must actively use socio-cultural cues from an image, such as exaggerated expressions or ironic situations, to distinguish the wittiest reply from a set of plausible candidates. Closing this gap between passive understanding and active contextual use remains a fundamental challenge as web communication becomes increasingly visual.

We hypothesize that three fundamental mismatches may explain why visual information fails to improve performance. First, there may be an *objective mismatch*: models are trained on semantic similarity (matching objects and scenes), whereas humor requires pragmatic alignment through recontextualization, the act of placing fixed visual content in a new conversational context to create surprising juxtaposition. Second, there may be a *data mismatch*: pre-training relies on descriptive captions that state explicit facts about images, while humor depends on implicit contextual cues that are not present in the image itself. Third, there may be a *domain mismatch*: the uniform visual style of manga makes it difficult for general-purpose models to distinguish the fine-grained facial expressions and subtle visual cues that are essential for humor. Further investigation is needed to validate these hypotheses. We also note that these findings may be specific to our manga-based benchmark, and results could differ with other meme formats such as photographic memes or reaction GIFs.

Addressing this limitation may require new objectives or architectures that couple visual recognition with contextual inference, rather than simply scaling multimodal encoders.

**From Simple Choices to Nuanced Judgments** Finally, our experiments identify the core challenge for current models: distinguishing subtle differences in wit among semantically similar candidates. While the models demonstrated near-human performance in controlled situations with clearly distinguishable choices (Exp3), their ability to select the best option decreased in more realistic scenarios, such as the retrieve-and-rerank approach in Exp2 or when candidate similarity was high in Exp4. This suggests that the retrieve-and-rerank architecture itself is a promising approach. The initial retrieval is effective at narrowing the pool to relevant and often humorous content. The main difficulty, therefore, lies in the final selection step. Future work



<!-- page 0010 -->

should focus on designing evaluation settings that better capture these subtle humor distinctions, enabling more reliable progress across models.

## Limitations and Future Directions

**Scope of the Benchmark** The design of our benchmark involves intentional scope limitations. First, we focused on a single domain: freely licensed Japanese manga panels. This choice was made to isolate humor signals in a controlled setting: unlike generative memes, manga panels have fixed content, which is ideal for isolating selection capabilities rather than generation. As subjectivity was high even in this controlled setting, adding cultural diversity prematurely would have made consensus impossible. This controlled framework can serve as a baseline for future cross-cultural studies. Online meme formats are diverse, and each creates humor through different conventions, such as image-macro captions or ongoing narratives. A key direction for future work is to expand this scope to other formats, like GIFs or reaction photos, to analyze how each generates its own unique humorous social dynamics. Second, we used a binary “funny/not funny” scale. This approach bases the subjective task of humor evaluation on a clearer, more observable reaction (whether the content elicits a laugh), which simplifies judgment for annotators and reduces subjective variance. Future benchmarks could use more detailed annotations to gain deeper insights. For example, graded scales could be used to analyze humor intensity, while the categorization of humor types could allow for a more detailed analysis of which humorous strategies are most effective in different contexts.

Ultimately, this research aims to enable systems that can produce genuinely funny replies in real-world interactions. While our use of synthetic contexts provides a controlled setting for this initial investigation, validating these findings in naturalistic environments remains an important next step.

**Towards More Socially Aware Agents** The practical implication of this research lies in improving how conversational systems respond to social and multimodal cues in online communication. A natural next step is to generate or select visual replies that align with contextual humor, extending beyond the simple retrieve-and-rank baseline explored in this study. To make such systems practical, several open challenges remain. These include modeling user and cultural context, integrating multimodal reasoning across text and images, and handling the temporal dynamics of memes, whose formats and popularity change rapidly over time. Further progress will also depend on developing evaluation frameworks that reflect these evolving conditions rather than static benchmarks alone. Beyond these technical challenges, practical deployment also requires attention to potential risks, such as selecting inappropriate or offensive content in sensitive contexts; human oversight and context-aware filtering will be essential. The MAME-RE benchmark provides a foundation for addressing these issues under controlled conditions, serving as a bridge between computational humor research and socially aware dialogue systems.

## Conclusion

Humor is a defining element of human communication, and our work takes an early step toward enabling machines to recognize and participate in this social form of expression. In this work, we proposed a new research direction for computational meme analysis, shifting the focus from static content to dynamic, interactive communication. To support this direction, we introduced the Meme Reply Selection task and the MAME-RE benchmark. This work establishes a systematic framework for studying contextual humor in online conversations. Our analysis revealed several fundamental challenges for current models. These include the gap between passively understanding and actively using visual humor, and the difficulty of distinguishing subtle differences in wit among similar candidates. We offer MAME-RE as a benchmark to measure progress on these fundamental challenges and to advance research on how AI systems understand and participate in humor within human communication.

## References

Alam, F.; Hasnat, A.; Ahmad, F.; Hasan, M. A.; and Hasanain, M. 2024. ArMeme: Propagandistic Content in Arabic Memes. In *Proc. EMNLP*, 21071–21090.

Bauman, R.; and Briggs, C. L. 1990. Poetics and performance as critical perspectives on language and social life. *Annual Review of Anthropology*.

Beskow, D. M.; Kumar, S.; and Carley, K. M. 2020. The evolution of political memes: Detecting and characterizing internet memes with multi-modal deep learning. *Information Processing & Management*, 57(2): 102170.

Chen, Y.; Yan, S.; Zhu, Z.; Li, Z.; and Xiao, Y. 2024. XMe-Cap: Meme Caption Generation with Sub-Image Adaptability. In *Proc. ACM MM*, 3352–3361.

Davison, P. 2012. The language of internet memes. *The Social Media Reader*, 120–134.

Dresner, E.; and Herring, S. C. 2010. Functions of the Nonverbal in CMC: Emoticons and Illocutionary Force. *Communication Theory*, 20: 249–268.

Fei, Z.; Li, Z.; Zhang, J.; Feng, Y.; and Zhou, J. 2021. Towards Expressive Communication with Internet Memes: A New Multimodal Conversation Dataset and Benchmark. *arXiv preprint arXiv:2109.01839*.

Grundlingh, L. 2018. Memes as speech acts. *Social Semiotics*, 28(2): 147–168.

Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.; Song, D.; and Steinhardt, J. 2021. Measuring Massive Multitask Language Understanding. In *Proc. ICLR*.

Highfield, T.; and Leaver, T. 2016. Instagrammatics and digital methods: studying visual social media, from selfies and GIFs to memes and emoji. *Communication Research and Practice*, 2(1): 47–62.

Hossain, E.; Sharif, O.; and Hoque, M. M. 2022. MUTE: A Multimodal Dataset for Detecting Hateful Memes. In *Proc. AACL-IJCNLP SRW*, 32–39.

Hu, T.; Guo, H.; Sun, H.; vy Thi Nguyen, T.; and Luo, J. 2017. Spice Up Your Chat: The Intentions and Sentiment Effects of Using Emojis. In *Proc. ICWSM*, 102–111.



<!-- page 0011 -->

Hwang, E.; and Shwartz, V. 2023. MemeCap: A Dataset for Captioning and Interpreting Memes. In *Proc. EMNLP*, 1433–1445.

Jiang, J. A.; Fiesler, C.; and Brubaker, J. R. 2018. ‘The Perfect One’: Understanding Communication Practices and Challenges with Animated GIFs. *Proc. ACM Hum.-Comput. Interact.*, 2(CSCW).

Joshi, S.; Ilievski, F.; and Luceri, L. 2024. Contextualizing Internet Memes Across Social Media Platforms. In *Companion Proc. WWW*, 1831–1840.

Kiela, D.; Firooz, H.; Mohan, A.; Goswami, V.; Singh, A.; Ringshia, P.; and Testuggine, D. 2020. The hateful memes challenge: detecting hate speech in multimodal memes. In *Proc. NeurIPS*.

Kulkarni, A. 2017. Internet meme and Political Discourse: A study on the impact of internet meme as a tool in communicating political satire. *Journal of Content, Community & Communication*, 6.

Li, J.; Wang, M.; Zheng, Z.; and Zhang, M. 2024. LooGLE: Can Long-Context Language Models Understand Long Contexts? In *Proc. ACL*, 16304–16333.

Liu, N. F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; and Liang, P. 2024. Lost in the Middle: How Language Models Use Long Contexts. *Trans. Assoc. Comput. Linguistics*, 12: 157–173.

Loakman, T.; Thorne, W.; and Lin, C. 2025. Who’s Laughing Now? An Overview of Computational Humour Generation and Explanation. *arXiv preprint arXiv:2509.21175*.

Lu, H.; Guo, Z.; Li, C.; Yang, Y.; He, H.; and Bao, S. 2023. Towards Building an Open-Domain Dialogue System Incorporated With Internet Memes. *IEEE/ACM Trans. Audio Speech Lang. Process.*, 32: 721–726.

Malodia, S.; Dhir, A.; Bilgihan, A.; Sinha, P.; and Tikoo, T. 2022. Meme marketing: How can marketers drive better engagement using viral memes? *Psychology & Marketing*, 39(9): 1775–1801.

Nguyen, K. P. N.; and Ng, V. 2024. Computational Meme Understanding: A Survey. In *Proc. EMNLP*, 21251–21267.

Pramanick, S.; Dimitrov, D.; Mukherjee, R.; Sharma, S.; Akhtar, M. S.; Nakov, P.; and Chakraborty, T. 2021. Detecting Harmful Memes and Their Targets. In *Findings of ACL*, 2783–2796.

Robinson, J.; and Wingate, D. 2023. Leveraging Large Language Models for Multiple Choice Question Answering. In *Proc. ICLR*.

Shah, S. B.; Shiwakoti, S.; Chaudhary, M.; and Wang, H. 2024. MemeCLIP: Leveraging CLIP Representations for Multimodal Meme Classification. In *Proc. EMNLP*, 17320–17332.

Sharma, C.; Bhageria, D.; Scott, W.; PYKL, S.; Das, A.; Chakraborty, T.; Pulabaigari, V.; and Gambäck, B. 2020. SemEval-2020 Task 8: Memotion Analysis— the Visuo-Lingual Metaphor! In *Proc. SemEval*, 759–773.

Sharma, S.; Agarwal, S.; Suresh, T.; Nakov, P.; Akhtar, M. S.; and Chakraborty, T. 2023a. What do you MEME? generating explanations for visual semantic role labelling in memes. In *Proc. AAAI*.

Sharma, S.; Alam, F.; Akhtar, M. S.; Dimitrov, D.; Da San Martino, G.; Firooz, H.; Halevy, A.; Silvestri, F.; Nakov, P.; and Chakraborty, T. 2022. Detecting and Understanding Harmful Memes: A Survey. In *Proc. IJCAI*, 5597–5606.

Sharma, S.; S, R.; Arora, U.; Akhtar, M. S.; and Chakraborty, T. 2023b. MEMEX: Detecting Explanatory Evidence for Memes via Knowledge-Enriched Contextualization. In *Proc. ACL*, 5272–5290.

Walther, J. B. 1992. Interpersonal Effects in Computer-Mediated Interaction: A Relational Perspective. *Communication Research*, 19(1): 52–90.

Walther, J. B. 1996. Computer-Mediated Communication: Impersonal, Interpersonal, and Hyperpersonal Interaction. *Communication Research*, 23(1): 3–43.

Wang, H.; and Lee, R. K.-W. 2024. MemeCraft: Contextual and Stance-Driven Multimodal Meme Generation. In *Proc. WWW*, 4642–4652.

Wang, X.; and Jurgens, D. 2021. An animated picture says at least a thousand words: Selecting Gif-based Replies in Multimodal Dialog. In *Findings of EMNLP*, 3228–3257.

Wang, Y.; Li, Y.; Gui, X.; Kou, Y.; and Liu, F. 2019. Culturally-Embedded Visual Literacy: A Study of Impression Management via Emoticon, Emoji, Sticker, and Meme on Social Media in China. *Proc. ACM Hum.-Comput. Interact.*, 3(CSCW).

Wu, Z.; Weber, T.; and Müller, F. 2025. One Does Not Simply Meme Alone: Evaluating Co-Creativity Between LLMs and Humans in the Generation of Humor. In *Proc. IUI*, 1082–1092.

Yus, F. 2018. Identity-related issues in meme communication. *Internet Pragmatics*, 1(1): 113–133.

Zhang, J.; Jain, L. K.; Guo, Y.; Chen, J.; Zhou, K. L.; Suresh, S.; Wagenmaker, A.; Sievert, S.; Rogers, T. T.; Jamieson, K.; Mankoff, B.; and Nowak, R. D. 2024. Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning. In *NeurIPS Datasets and Benchmarks Track*.

Zhong, S.; Huang, Z.; Gao, S.; Wen, W.; Lin, L.; Zitnik, M.; and Zhou, P. 2024. Let’s Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Creative Humor Generation. In *Proc. CVPR*, 13246–13257.

Zhuang, Y.; Guo, K.; Wang, J.; Jing, Y.; Xu, X.; Yi, W.; Yang, M.; Zhao, B.; and Hu, H. 2025. I know what you MEME! Understanding and Detecting Harmful Memes with Multimodal Large Language Models. In *Proc. NDSS*.
