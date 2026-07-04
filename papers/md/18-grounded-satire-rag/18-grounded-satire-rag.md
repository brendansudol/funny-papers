<!-- Transcribed from 18-grounded-satire-rag.pdf -->



<!-- page 0001 -->

# Grounded Satirical Generation with RAG

**Oona Itkonen\*** and **Yuxin Su\*** and **Linyao Du\*** and **Ona De Gibert**  
University of Helsinki

## Abstract

Humor generation remains challenging task for Large Language Models (LLMs), due to their subjective nature. We focus on satire, a form of humor strongly shaped by context. In this work, we present a novel pipeline for grounded satire generation that uses Retrieval-Augmented Generation (RAG) over current news to produce satirical dictionary definitions in the Finnish context. We also introduce a new task-specific evaluation framework and annotate 100 generated definitions with six human annotators, enabling analysis across multiple experimental conditions, including cultural background, source-word type, and the presence or absence of RAG. Our results show that the generated definitions are perceived as more political than humorous. Both topic-based word selection and RAG improve the political relevance of the outputs, but neither yields clear gains in humor generation. In addition, our LLM-as-a-judge evaluation of five state-of-the-art models indicates that LLMs correlate well with human judgments on political relevance, but perform poorly on humor. We release our code and annotated dataset to support further research on grounded satire generation and evaluation.

## 1 Introduction

Humor is a fundamental aspect of human nature, yet defining it remains a persistent challenge (Bardon, 2005; Larkin-Galiñanes, 2017). Given this conceptual complexity, it is unsurprising that Large Language Models (LLMs) also struggle to reliably interpret and generate humor. LLMs can detect humor with relatively well, but generating it is still an unsolved problem.

In this work, we focus on satire generation and evaluation, an even more challenging task, as satire constitutes a nuanced cultural-specific form of humor, the interpretation of which depends heavily on a shared social, political, and historical context (Stinson, 2019). We adopt the definition of *Satire* from the Cambridge Dictionary[^1]: *a way of criticizing people or ideas in a humorous way, especially in order to make a political point.* Accordingly, two core components of satire are humor and political significance.

For generation, we present a novel method based on Retrieval-Augmented Generation (RAG) (Lewis et al., 2020) to produce satire from news content in the form of satirical dictionary definitions. Because satire is highly dependent on cultural and regional context, we restrict our study to the Finnish setting. As source data, we use English-language news articles published on the website of the Finnish public broadcaster Yle[^2]. Our pipeline consists of a scraper with sentiment analysis and timestamp-based filtering, a semantic search engine, a topic modeling component for selecting candidate words, and a final RAG-based generation stage.

For evaluation, we develop our own framework, motivated by the fact that humor evaluation is inherently difficult and lacks standardized evaluation practices (Hämäläinen and Alnajjar, 2021). We present evaluation results of based on two methods: human annotation and LLM-based judgment. We evaluate five mid-size state-of-the-art LLMs. We aim to answering the following Research Questions (RQ):

- RQ1: To what extent are the generated definitions humorous and politically meaningful?

- RQ2: To what extent is successful satire generation dependent on cultural context?

- RQ3: How does the choice of the candidate word affect the quality of the generated definitions?

\*Equal contribution

[^1]: https://dictionary.cambridge.org/dictionary/english/satire  
[^2]: https://yle.fi/



<!-- page 0002 -->

[Figure: Flowchart overview of a generation pipeline with three stages. Stage 1, “Web Scraping & Filtering”: Web Scraper → Timestamp Check → Batch Articles → Sentiment Analysis; Fail → Filtered-out Files; Pass → Passed News Corpus. Stage 2, “Semantic Search Engine”: Input Query and Search Context feed “Semantic Search Engine Cosine Similarity > 0.1?”; Yes → Top 3 News Snippets. Stage 3, “Retrieval-Augmented Generation”: Construct Prompt → Llama-3 via Ollama → Satirical Definition.]

Figure 1: Overview of our generation pipeline for satirical dictionary definitions with RAG.

- RQ4: Does RAG improve the quality of generated satirical definitions?

- RQ5: Can LLMs serve as reliable evaluators of satirical content?

In addition, we present a webpage application to showcase and run our generation pipeline. Furthermore, we release our annotated corpus to the research community and make our scripts publicly available for reproducibility[^3].

## 2 Related Work

One of the first tasks related to humor in NLP is **humor detection**. Early work in computational humor focused on template-based methods (Chandrasekaran et al., 2016) and classical supervised machine learning approaches relying on static features (De Oliveira and Rodrigo, 2015). More recently, transformer-based and LLM-based methods have been proposed. Recent research has examined the generalizability of humor detection models (Baranov et al., 2023), as well as related tasks such as irony detection (Ortega-Bueno et al., 2023; Tomás et al., 2023; Lin et al., 2024) and **humor understanding** (Hessel et al., 2023; Hwang et al., 2025), in which an LLM is prompted to explain why a given text is humorous.

**Humor generation** has also attracted attention for many years (Stock and Strapparava, 2005). More recently, Jentzsch and Kersting (2023) investigated the use of ChatGPT for joke generation and found that the model tends to produce repetitive outputs. Similarly, Sakabe et al. (2025) used LLMs to generate *Oogiri*, a form of Japanese improvisational comedy. However, the field continues to observe that, while LLMs perform relatively well on humor detection, they remain less effective at humor generation (Sakabe et al., 2025).

Some work has also tried to develop improved **humor evaluation** methods. For example, Romanowski et al. (2025) propose a new metric for evaluating stand-up comedy based on statistical measures. However, humor evaluation remains difficult because no standard evaluation practices have been established. A recent trend is to design task-specific annotation guidelines, obtain judgments from both human annotators and LLMs, and then analyze the agreement between them (Bago and Bakarić, 2025; Sakabe et al., 2025; Rivera et al., 2026). This is the approach we adopt in this work.

Finally, turning specifically to satire, research on satire and LLMs has expanded rapidly in recent years. One line of work focuses on satire detection. For example, Ozturk et al. (2025) introduce a dataset of Turkish satirical news and investigate methods for reducing stylistic bias in satire detection. Another direction has been proposed by West and Horvitz (2019); Horvitz et al. (2024), who study satire by reverse-engineering satirical news headlines and evaluating LLMs’ ability to make them non-satirical or “unfunny.” Dobre and Gross (2025) compare AI-generated satire with human-written satirical articles and evaluate the outputs using an LLM-as-a-judge framework. To the best of our knowledge, we are the first to study satirical generation grounded on latest news using RAG.

## 3 Generation

In this section we present our methodology for grounded generation of satirical dictionary definitions. Our pipeline is based on a web scraper that includes timestamp filtering and sentiment analysis. We select relevant candidate words using topic modeling, find the relevant articles from our data with semantic search and, finally, we use RAG to generate definitions of the words based on the latest news. In Section 6, we present how this pipeline can be run as a web application. Figure 1 presents

[^3]: https://github.com/dlylinyao/ONLY/tree/CHUM



<!-- page 0003 -->

**Q1: Is it funny?**

| Score | Explanation |
|---|---|
| 1 | It is not funny, awkward at most. |
| 2 | It is slightly funny. |
| 3 | It is so funny I laughed. |
| 4 | It is so funny I will tell it to someone else. |
| 5 | It is so funny I will laugh if I tell it to someone else. |

Table 1: Annotation guideline for Q1: *Is it funny?*

**Q2: Is it political?**

| Score | Explanation |
|---|---|
| 1 | It is not political at all. |
| 2 | It has some political quality. |
| 3 | It is political on a general level. |
| 4 | It is political and current. |
| 5 | It is political, current and relevant in Finnish political culture. |

Table 2: Annotation guidelines for Q2: *Is it political?*

an overview of our pipeline.

### 3.1 Web Scraping

Given the definition of satire from Cambride Dictionary[^4], satire is often political. Therefore, our data should ideally have political content. As news are often about politics, or at least have content that can be interpreted in a political frame, we choose to use news as our source data. Politics is, however, not a very static field of domain and it evolves quickly to new topics. Therefore, rather than opting for a static news dataset, we built a scraper with BeautifulSoup to extract news articles published in English from the website of the Finnish broadcasting company Yle. Our scraper retrieves articles from all the different categories listed in the Yle website in English[^5], parsing their metadata. As satire is, in addition to being political on a general level, also depended on culture and region, we restrict our data to this one source, as it is the only open source site that publishes news in English in Finland.

### 3.2 Filtering

#### 3.2.1 Timestamp Filtering

For the same reason, discussed in section 3.1, we choose to scrape our data rather than use an existing dataset we want to filter our data based on the timestamps of the articles. We chose to use 30 days as the threshold for timestamps, and articles older than a month do not get processed any further.

#### 3.2.2 Sentiment Analysis

The Cambridge Dictionary[^6] describes satire as a way of criticizing something in a humorous way. However, there are certain restrictions to what kind of topics are commonly considered acceptable for satire. On the other hand, when satire is made based on sensitive topics, the tiniest details in the choice of words can define whether it is interpreted as offensive and inappropriate instead of funny.

This kind of contextual understanding is something that humans are able to consider. As we are generating satire with an LLM, however, we need to be aware of restrictions that the model has in understanding what is appropriate and what is not. Therefore, to ensure our pipeline doesn’t produce any offensive or disturbing content, we implement sentiment analysis to filter out too negative news. Here, we are, assuming that sentiment is a proxy for how "bad" a piece of news is or how sensitive or severe the topics it covers might be.

For the sentiment analysis task, we use the NLP-Town/bert-base-multilingual-uncased-sentiment model from Hugging Face. We feed the body text of the news articles to the model, and it outputs from one up to five stars, ranging from more negative to more positive.

Our motivation for sentiment analysis is not to filter out everything negative, but rather to ensure the ethics of our output. Therefore, we set the threshold of our sentiment analysis to one, so news that get a label lower than one are discarded. To obtain a more reliable sentiment score for each news article, we split the articles into batches that fit within the model’s token limit, perform sentiment analysis on each batch, and then compute the mean label scores to obtain the final article-level score.

### 3.3 Word Candidate Selection with Topic Modeling

To generate satire that makes sense in a specific cultural context, we find topics currently discussed in the news with unsupervised topic modeling to

[^4]: https://dictionary.cambridge.org/dictionary/english  
[^5]: https://yle.fi/news  
[^6]: https://dictionary.cambridge.org/dictionary/english



<!-- page 0004 -->

automatically extract candidate words from our web-scraped data.

First, we convert the news articles into text embeddings using the paraphrase-multilingual-MiniLM-L12-v2 model. We then apply UMAP (McInnes et al., 2020) for dimensionality reduction and use BERTopic (Grootendorst, 2022) to cluster the articles into distinct news topics. After excluding outlier documents, we extract the most salient keywords from each valid cluster. This words will be used to generate satirical dictionary definitions.

### 3.4 Retrieval

To retrieve relevant news for each input word, we employ a semantic search approach to prioritize contextual meaning over exact keyword matching. We embed the news articles using the all-MiniLM-L6-v2 model.

For each input, we calculate cosine similarity to find the most relevant news contexts. The system retrieves up to 3 news snippets per input word or phrase, filtering out any results with a similarity score below 0.1. If the search engine finds exact matches of the input, the snippets consist of the immediate contexts around those matches. If the word does not occur in any of the articles, the search engine returns the snippet from the beginning of the article. The snippets are of the size 160 character each, to preserve context most relevant for the input and they always include the timestamp, the category and the title of the article.

### 3.5 RAG

We built a custom RAG system to generate definitions for words based on the news data. The retrieved snippets are passed to meta-llama/Meta-Llama-3-8B-Instruct (Grattafiori et al., 2024) using the ollama library[^7], prompted to act as the editor of a “Satirical Dictionary.” To ensure the humor is grounded, the prompt strictly instructs the model to base its definitions solely on the provided news context rather than generic stereotypes. We enforce a cynical tone to highlight the absurdity of the specific news events and limited outputs to 50 words. The exact prompt can be found in Appendix A.

## 4 Evaluation

As the amount of existing research on computational satire is rather limited, and nonexistent when it comes to grounded generation of satire, there is

[^7]: https://ollama.com/library/llama3:latest

| Annotator Group | Humor | Politics |
|---|---:|---:|
| All | 0.070 | 0.514 |
| Finnish | 0.053 | 0.646 |
| International | 0.183 | 0.490 |

Table 3: Inter-annotator agreement of normalized z-scores measured by Krippendorf’s $\alpha$

no standard evaluation method that we could apply in this study. We choose to use human evaluation as our evaluation method, and in addition to that, we investigate whether LLMs agree with our human evaluation results using LLMs as judges. We base the choice and design of our evaluation method on practices from creative natural language generation (Hämäläinen and Alnajjar, 2021) and existing studies on computational satire evaluation (West and Horvitz, 2019; Horvitz et al., 2024; Dobre and Gross, 2025).

For the evaluation, we generate definitions for 50 words. 25 of these are drawn from the topics identified in Section 3.3. The remaining 25 consist of randomly selected English words. This setup allows us to examine whether news-related words lead to different generated definitions than unrelated random words. In addition, for each word we generate two definitions, one with RAG and one without RAG, in order to assess the impact of retrieval augmentation. The exact prompts can be found in Appendix A. For generating the definitions, we use news articles scraped on March 3, 2026.

We develop our own annotation guidelines both for human evaluation and LLM judges. Drawing on the Cambridge Dictionary definition of satire, we formulate two questions based on two dimensions: *Q1: Is it funny?*, and *Q2: Is it political?*. Annotators are then asked to rate each definition on both questions using a 1-to-5 Likert scale. For each question, we provide a verbal description of the scores from 1 to 5, as shown in Tables 1 and 2.

### 4.1 Human Evaluation

For the human evaluation, we randomly shuffle the 100 definitions to ensure a blind annotation setup, such that annotators rate each sample without knowing which model generated it or under which experimental condition it was produced.

We employ six annotators to evaluate the 100 definitions. Half of the annotators are Finnish, while the other half come from different cultural backgrounds. This design allows us to examine



<!-- page 0005 -->

[Figure: Two side-by-side bar charts showing score distributions. Left chart: y-axis “Percentage (%)”, x-axis “Funny”, scores 1–5. Right chart: y-axis “Percentage (%)”, x-axis “Political”, scores 1–5.]

(a) Funny score distribution

(b) Political score distribution

Figure 2: Distribution of absolute quality scores across annotators.

whether cultural background influences the interpretation of the generated definitions.

### 4.2 LLM-as-a-Judge

Human annotation is costly and time-consuming. Recently, LLMs have increasingly been used as automatic evaluators for a variety of NLP tasks. We aim to investigate whether LLMs can reliably evaluate humor and political relevance in satirical definitions.

To this end, we evaluate several open-weight models and instruct them to score definitions according to the same annotation guidelines used in the human evaluation setting described above. Each model is prompted with the evaluation prompt provided in Appendix A. The models assign scores for humor and political relevance following the same scale as used by human annotators.

We evaluate the following instruction-tuned models of comparable size: Qwen/Qwen2.5-7B-Instruct (Ahmed et al., 2025), meta-llama/Llama-3.1-8B-Instruct (Grattafiori et al., 2024), mistralai/Mistral-7B-Instruct-v0.3 (Jiang et al., 2023), CohereLabs/aya-expanse-8b (Dang et al., 2024) and utter-project/EuroLLM-9B-Instruct (Martins et al., 2025).

## 5 Results

In this section, we analyze the annotated data (both by humans and LLMs) to address the research questions outlined in the Introduction.

**RQ1: To what extent are the generated definitions humorous and politically meaningful?** Figure 3 shows the percentage distribution of scores for the two proposed questions. The generated satirical definitions are not perceived as funny by human annotators (M=1.98, SD=1.06), with 40% of the annotations receiving a score of 1. They receive slightly higher ratings for political relevance (M=2.53, SD=1.55) and a more diverse distribution of scores, which indicates that the definitions are perceived as more political than funny. For both dimensions, we observe a large standard deviation, which reflects substantial variability in the judgments. Variation in the ratings for both questions is expected, as both humor and political quality are subject to individual interpretation. This confirms that satire annotation is a hard task for humans.

**RQ2: To what extent is successful satire generation dependent on cultural context?** Table 3 reports inter-annotator agreement in the human evaluation, measured using Krippendorff’s $\alpha$. For the funny dimension, agreement is very low, which is consistent with the observations above and supports the view that humor perception is highly subjective. For the political dimension, agreement is somewhat higher, with an overall agreement above 0.5; however, this level should still be interpreted cautiously, as it falls below commonly used thresholds for strong reliability.

When considering the annotator groups separately, the international group shows slightly higher agreement on humor, whereas the Finnish group shows slightly higher agreement on political relevance. One possible explanation is that Finnish annotators may have been more familiar with current news topics, political discourse, and locally-grounded satire, which could have led to more consistent judgments regarding what counts as political



<!-- page 0006 -->

[Figure: Three bar charts showing average scores (Score 1–5) across experimental conditions, with legends titled “Dimension” for Funny and Political. (a) Finnish vs. International annotators; x-axis labels Finnish, International. (b) Topic (News) vs Random words; x-axis labels Topic (News), Random. (c) Non-RAG vs. RAG-based definitions; x-axis labels Non-RAG, RAG.]

(a) Finnish vs. International annotators  
(b) Topic vs Random words  
(c) Non-RAG vs. RAG-based definitions

Figure 3: Average scores across experimental conditions.

and contextually relevant in the Finnish setting.

Figure 3a shows the mean scores for both annotation questions. Contrary to our expectations, comparisons between Finnish and international annotators revealed no statistically significant differences in either of the ratings (p>0.1, Mann-Whitney U test). These results indicate that, in this dataset, cultural background did not have a systematic effect on the ratings.

**RQ3: How does the choice of the candidate word affect the quality of the generated definitions?** We conduct a Mann-Whitney U test to compare annotations for randomly selected words and topic-modeled candidate words. The results show no statistically significant difference for the funny dimension (p=0.758), whereas the political dimension exhibits a statistically significant difference (p<0.001). These findings indicate that words selected through topic modeling lead to definitions that are perceived as more political, but not funnier, than definitions based on randomly selected words.

**RQ4: Does RAG improve the quality of generated satirical definitions?** To compare annotations for definitions generated with and without RAG, we conduct a Wilcoxon signed-rank test. Figure 3c presents the mean scores for this comparison. As in the previous analysis, RAG does not yield a statistically significant difference in the funny dimension (p=.05), but it does lead to a statistically significant improvement in the political dimension (p<.001). These results indicate that our RAG pipeline is more effective than the non-RAG baseline at generating politically relevant content, but not at improving humor. This outcome is in line with our expectations, since the purpose of grounded generation is to anchor outputs in the provided source material, and in our case the retrieved news snippets are not themselves expected to be humorous or satirical.

**RQ5: Can LLMs serve as reliable evaluators of satirical content?** Table 4 reports the mean scores assigned by each LLM judge, together with their correlations with human ratings. Figures 4a and 4b present the score distributions for Aya-Expanse-8B and its correlation with human judgments, while Appendix B provides the corresponding figures for the remaining four models.

Overall, the LLMs assign higher mean scores to humor, with relatively low variance, and lower mean scores to political relevance, with greater variability. Based on the correlation scores, the evaluated LLMs do not capture humor well, as their correlations with human ratings on the funny dimension are uniformly low. By contrast, all models show strong correlations with human judgments on the political dimension, indicating that they are much better at identifying political relevance than humor. Among the evaluated models, Aya-Expanse-8B achieves the highest correlation with human judgments overall.

Taken together, these results indicate that LLMs can serve as reasonably reliable evaluators of the political relevance of satirical definitions, but they remain poor judges of subjective qualities such as humor.

## 6 Web Application

To showcase our pipeline we built a web application. It can be run locally to generate definitions and search for relevant news with any user input, e.g. keywords presented in a plotting based on



<!-- page 0007 -->

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="2">Average Score</th>
<th colspan="2">Human Correlations</th>
</tr>
<tr>
<th>Funny</th>
<th>Political</th>
<th>Funny</th>
<th>Political</th>
</tr>
</thead>
<tbody>
<tr>
<td>Aya-Expanse-8B</td>
<td>3.83 ± 0.77</td>
<td>3.40 ± 1.32</td>
<td><strong>0.199* [0.005, 0.373]</strong></td>
<td><strong>0.826** [0.758, 0.872]</strong></td>
</tr>
<tr>
<td>EuroLLM-9B-Instruct</td>
<td>3.46 ± 0.81</td>
<td>2.41 ± 1.74</td>
<td>0.161 [-0.035, 0.334]</td>
<td>0.663** [0.534, 0.760]</td>
</tr>
<tr>
<td>Llama-3.1-8B-Instruct</td>
<td>3.96 ± 0.57</td>
<td>3.21 ± 1.89</td>
<td>0.084 [-0.119, 0.265]</td>
<td>0.756** [0.671, 0.825]</td>
</tr>
<tr>
<td>Mistral-7B-Instruct-v0.3</td>
<td>2.81 ± 0.67</td>
<td>1.83 ± 1.06</td>
<td>-0.065 [-0.261, 0.134]</td>
<td>0.751** [0.669, 0.816]</td>
</tr>
<tr>
<td>Qwen2.5-7B-Instruct</td>
<td>3.52 ± 0.64</td>
<td>3.50 ± 1.50</td>
<td>0.069 [-0.145, 0.263]</td>
<td>0.688** [0.580, 0.772]</td>
</tr>
</tbody>
</table>

Table 4: Mean scores ($M \pm SD$) assigned by the LLM judges for the funny and political dimensions, together with Spearman correlation $\rho$ with human mean scores. Brackets indicate 95% confidence intervals. \*\* $p < 0.001$, \* $p < 0.05$.

[Figure: Two scatter plots with regression lines comparing Human Average Score on the x-axis to Aya-Expanse-8B Score on the y-axis. Subplots labeled (a) Funny and (b) Political.]

(a) Funny

(b) Political

Figure 4: Correlation of human scores with Aya-Expanse-8B annotations.

topic modeling. The repository of the application will be made public upon acceptance.

## 7 Conclusions

In this study, we presented a novel pipeline that uses RAG for grounded satire generation. We formulated five research questions and evaluated the system through both human annotation and an LLM-as-a-judge framework.

Our results show that the generated definitions are perceived as more political than humorous. Contrary to our expectations, considering satire as a culturally dependent phenomenon, we do not find a statistically significant effect of cultural background on annotation outcomes in our dataset. We found that both RAG and topic-based word selection improve the political relevance of the generated content, indicating that our pipeline is effective for generating politically grounded satire. However, neither leads to clear improvements in humor generation. Finally, the results of our LLM-as-a-judge evaluation show that LLMs are effective at identifying politically relevant content, but perform poorly at detecting humor. This further supports the view that humor remains a particularly difficult and subjective evaluation task for current language models.

Our current pipeline is limited to English news from the Finnish public broadcaster Yle. Future work should extend the approach to additional languages and sources, and explore alternative evaluation methods in order to provide a broader and more robust assessment of system performance.

## References

Imtiaz Ahmed, Sadman Islam, Partha Protim Datta, Imran Kabir, Naseef Ur Rahman Chowdhury, and Ahshanul Haque. 2025. Qwen 2.5: A comprehensive review of the leading resource-efficient llm



<!-- page 0008 -->

with potential to surpass all competitors. *Authorea Preprints*.

Petra Bago and Nikola Bakarić. 2025. Few-shot prompting, full-scale confusion: Evaluating large language models for humor detection in croatian tweets. In *Proceedings of the 10th Workshop on Slavic Natural Language Processing (Slavic NLP 2025)*, pages 9–16.

Alexander Baranov, Vladimir Kniazhevsky, and Pavel Braslavski. 2023. You told me that joke twice: A systematic investigation of transferability and robustness of humor detection models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, pages 13701–13715, Singapore. Association for Computational Linguistics.

Adrian Bardon. 2005. The philosophy of humor. *Comedy: A geographic and historical guide*, 2(1):462–476.

Arjun Chandrasekaran, Ashwin K Vijayakumar, Stanislaw Antol, Mohit Bansal, Dhruv Batra, C Lawrence Zitnick, and Devi Parikh. 2016. We are humor beings: Understanding and predicting visual humor. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, pages 4603–4612.

John Dang, Shivalika Singh, Daniel D’souza, Arash Ahmadian, Alejandro Salamanca, Madeline Smith, Aidan Peppin, Sungjin Hong, Manoj Govindassamy, Terrence Zhao, and 1 others. 2024. Aya expanse: Combining research breakthroughs for a new multilingual frontier. *arXiv preprint arXiv:2412.04261*.

Luke De Oliveira and Alfredo L Rodrigo. 2015. Humor detection in yelp reviews. *Retrieved on December*, 15:2019.

A-S Dobre and E-C Gross. 2025. Evaluating ai-generated satire against human-written content: A comparative analysis. *Bulletin of the Transilvania University of Braşov. Series VII: Social Sciences• Law*, pages 157–166.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, and 1 others. 2024. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*.

Maarten Grootendorst. 2022. Bertopic: Neural topic modeling with a class-based tf-idf procedure. *Preprint*, arXiv:2203.05794.

Mika Hämäläinen and Khalid Alnajjar. 2021. Human evaluation of creative NLG systems: An interdisciplinary survey on recent papers. In *Proceedings of the First Workshop on Natural Language Generation, Evaluation, and Metrics (GEM)*, pages 84–95, Online. Association for Computational Linguistics.

Jack Hessel, Ana Marasović, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, and Yejin Choi. 2023. Do androids laugh at electric sheep? humor “understanding” benchmarks from the new yorker caption contest. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 688–714, Toronto, Canada. Association for Computational Linguistics.

Zachary Horvitz, Jingru Chen, Rahul Aditya, Harshvardhan Srivastava, Robert West, Zhou Yu, and Kathleen McKeown. 2024. Getting serious about humor: Crafting humor datasets with unfunny large language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*, pages 855–869, Bangkok, Thailand. Association for Computational Linguistics.

EunJeong Hwang, Peter West, and Vered Shwartz. 2025. Bottlehumor: Self-informed humor explanation using the information bottleneck principle. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 22611–22632.

Sophie Jentzsch and Kristian Kersting. 2023. ChatGPT is fun, but it is not funny! humor is still challenging large language models. In *Proceedings of the 13th Workshop on Computational Approaches to Subjectivity, Sentiment, & Social Media Analysis*, pages 325–340, Toronto, Canada. Association for Computational Linguistics.

Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023. Mistral 7b. *Preprint*, arXiv:2310.06825.

Cristina Larkin-Galiñanes. 2017. An overview of humor theory. *The Routledge handbook of language and humor*, pages 4–16.

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks. *Preprint*, arXiv:2005.11401.

Yucheng Lin, Yuhan Xia, and Yunfei Long. 2024. Augmenting emotion features in irony detection with large language modeling. In *Workshop on Chinese Lexical Semantics*, pages 196–206. Springer.

Pedro Henrique Martins, Patrick Fernandes, João Alves, Nuno M Guerreiro, Ricardo Rei, Duarte M Alves, José Pombal, Amin Farajian, Manuel Faysse, Mateusz Klimaszewski, and 1 others. 2025. Eurollm: Multilingual language models for europe. *Procedia Computer Science*, 255:53–62.

Leland McInnes, John Healy, and James Melville. 2020. Umap: Uniform manifold approximation and projection for dimension reduction. *Preprint*, arXiv:1802.03426.



<!-- page 0009 -->

Reynier Ortega-Bueno, Paolo Rosso, and Elisabetta Fersini. 2023. Cross-domain and cross-language irony detection: The impact of bias on models’ generalization. In *International Conference on Applications of Natural Language to Information Systems*, pages 140–155. Springer.

Asli Umay Ozturk, Recep Firat Cekinel, and Pinar Karagoz. 2025. Make satire boring again: Reducing stylistic bias of satirical corpus by utilizing generative LLMs. In *Proceedings of the 18th Workshop on Building and Using Comparable Corpora (BUCC)*, pages 19–35, Abu Dhabi, UAE. Association for Computational Linguistics.

Fabricio Rivera, Rohit Pochugari, Tessa Chan, Devansh Katakwar, Kevin Zhu, and Michael Saxon. 2026. Not funny anymore: Llm judges confuse literal similarity for humor in translated jokes. In *Second Workshop on Language Models for Underserved Communities (LM4UC)*.

Adrianna Romanowski, Pedro HV Valois, and Kazuhiro Fukui. 2025. From punchlines to predictions: A metric to assess llm performance in identifying humor in stand-up comedy. In *Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics*, pages 36–46.

Ritsu Sakabe, Hwichan Kim, Tosho Hirasawa, and Mamoru Komachi. 2025. Assessing the capabilities of llms in humor: A multi-dimensional analysis of oogiri generation and evaluation. *arXiv preprint arXiv:2511.09133.*

Emmett Stinson. 2019. Satire. In *Oxford Research Encyclopedia of Literature.*

Oliviero Stock and Carlo Strapparava. 2005. Hahacronym: A computational humor system. In *Proceedings of the ACL Interactive Poster and Demonstration Sessions*, pages 113–116.

David Tomás, Reynier Ortega-Bueno, Guobiao Zhang, Paolo Rosso, and Rossano Schifanella. 2023. Transformer-based models for multimodal irony detection. *Journal of Ambient Intelligence and Humanized Computing*, 14(6):7399–7410.

Robert West and Eric Horvitz. 2019. Reverse-engineering satire, or “paper on computational humor accepted despite making serious advances”. In *Proceedings of the aaai conference on artificial intelligence*, volume 33, pages 7265–7272.

# A Prompts for Generating Definitions

## A.1 Prompt with RAG

<pre>
You are the editor of a ’Satirical Dictionary’.
    Define the term based SOLELY on the provided
    news context.
CRITICAL RULE: You must use the SPECIFIC IRONY
    found in the text, not generic stereotypes.
Example: If the text says ’working people need
    food’, do NOT joke about laziness. Joke
    about how wages are useless.
Style Guidelines:
1. Cynical and Dark.
2. Highlight the absurdity of the specific
    situation described in the text.
3. ATTENTION: Keep it under 50 words.
Only output the definition, No explanations or
    commentary.
</pre>

## A.2 Prompt without RAG

<pre>
You are the editor of a ’Satirical Dictionary’.
CRITICAL RULE: You must use SPECIFIC IRONY
    typical for Finnish culture.
Style Guidelines:
1. Cynical and Dark.
2. ATTENTION: Keep it under 50 words.
Only output the definition, No explanations or
    commentary.
</pre>

## A.3 Prompt for LLM-as-a-judge

<pre>
Task:
Score a satirical definition on two dimensions:
- funny
- political

Use only the text provided by the user.
Do not use external knowledge.
Do not explain your answer.
Do not add any text before or after the JSON.

Scales:

funny:
1 = not funny
2 = slightly funny
3 = funny
4 = very funny
5 = extremely funny

political:
1 = not political
2 = slightly political
3 = generally political
4 = clearly political and topical
5 = strongly political and specifically relevant
      to Finnish political culture

Output rules:
- Output exactly one JSON object
- Use exactly these two keys: "funny", "
    political"
- Both values must be integers from 1 to 5
- Do not use markdown
- Do not use code fences
- Do not output anything except the JSON object

Valid output example:
{"funny": 3, "political": 4}
"""
</pre>

# B Correlations with Human Judgements

Figures 5, 6, 7 and 8 show the correlations of LLM judgments with human annotations.



<!-- page 0010 -->

[Figure: Two side-by-side scatter plots with regression lines. Left plot y-axis: “EuroLLM-9B-Instruct Score”, x-axis: “Human Average Score”; right plot y-axis: “EuroLLM-9B-Instruct Score”, x-axis: “Human Average Score”.]

(a) Funny

(b) Political

Figure 5: Correlation of human scores with EuroLLM-9B-Instruct Annotations

[Figure: Two side-by-side scatter plots with regression lines. Left plot y-axis: “Llama-3.1-8B-Instruct Score”, x-axis: “Human Average Score”; right plot y-axis: “Llama-3.1-8B-Instruct Score”, x-axis: “Human Average Score”.]

(a) Funny

(b) Political

Figure 6: Correlation of human scores with Llama-3.1-8B-Instruct Annotations

[Figure: Two side-by-side scatter plots with regression lines. Left plot y-axis: “Mistral-7B-Instruct-v0.3 Score”, x-axis: “Human Average Score”; right plot y-axis: “Mistral-7B-Instruct-v0.3 Score”, x-axis: “Human Average Score”.]

(a) Funny

(b) Political

Figure 7: Correlation of human scores with Mistral-7B-Instruct Annotations

[Figure: Two side-by-side scatter plots with regression lines. Left plot y-axis: “Qwen2.5-7B-Instruct Score”, x-axis: “Human Average Score”; right plot y-axis: “Qwen2.5-7B-Instruct Score”, x-axis: “Human Average Score”.]

(a) Funny

(b) Political

Figure 8: Correlation of human scores with Qwen2.5-7B-Instruct Annotations
