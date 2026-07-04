<!-- Transcribed from 45-not-all-jokes-land.pdf -->



<!-- page 0001 -->

# Not All Jokes Land: Evaluating Large Language Models’ Understanding of Workplace Humor

**Mohammadamin Shafiei<sup>*1</sup>, Hamidreza Saffari<sup>*2</sup>**  
<sup>1</sup>University of Milan, <sup>2</sup>Politecnico di Milano  
`m.shafieiapoorvari@studenti.unimi.it`  
`hamidreza.saffari@mail.polimi.it`

## Abstract

With the recent advances in Artificial Intelligence (AI) and Large Language Models (LLMs), the automation of daily tasks, like automatic writing, is getting more and more attention. Hence, efforts have focused on aligning LLMs with human values, yet humor—particularly professional industrial humor used in workplaces—has been largely neglected. To address this, we develop a dataset of professional humor statements along with features that determine the appropriateness of each statement. Our evaluation of five LLMs shows that LLMs often struggle to judge the appropriateness of humor accurately. Etxaniz et al. (2024)

[Figure: Examples of workplace humor statements with labels. Top labeled “Offensive” with a red X: “In our Italian office, deadlines are merely suggestions - like the speed limit on a Sicilian road.” Bottom labeled “Wholesome” with a green check: “In our team meetings, the only thing bigger than our to-do list is our enthusiasm.”]

Figure 1: Examples of humor misclassified by LLMs.

# 1 Introduction

Humor is a universal fundamental aspect of human expression, (Bardon, 2005) encompassing a broad range of emotions and interactions. (Morreall, 1983) From a societal point of view, humor has long served as a means of communication in society, while also being used to cope with life’s challenges and create a sense of trust. (Meyer, 2000, 2015; Lynch, 2002; Berk, 2015) Humor is often seen as spontaneous, yet it is strongly shaped by context, including cultural and societal backgrounds and the relationship between speaker and audience.(Jiang et al., 2019; Hampes, 1992)

Many studies have focused on the relationship between the setting and humor. (Vizmuller, 1980; Banas et al., 2011; Coser, 1959; Zhou et al., 2023) In professional industrial environments, humor takes on unique dynamics, reflecting organizational structures and interpersonal relationships norms. (Mesmer-Magnus et al., 2012; Idrees et al., 2020) When used well, it strengthens teams and fosters innovation; misused, risks misunderstandings and credibility. (Meyer, 2000) Also, from the computational side, with the advances in Artificial intelligence (AI) and more specifically Large Language Models (LLMs), many efforts have been dedicated to automating various tasks like writing and content creation.(Wang, 2024; Xiao et al., 2024; Scherbakov et al., 2024; Shen et al., 2024) An example of automated writing is the use of LLM agents to write an email, a document, or a social media post, all applicable to industrial settings. (Jovic and Mnasri, 2024; Gryka et al., 2024; Lu et al., 2024) Another area that has also got attention to make automation is automating simulation of human life and interactions using persona-assigned LLM agents. (Park et al., 2023; Wang et al., 2024) In these automation scenarios, LLMs may use humor and need situational awareness to apply it appropriately. However, a gap exists in evaluating LLMs’ ability to judge humor suitability within professional settings, especially industry-specific contexts. Figure 1 illustrates two examples in which LLMs fall short of correctly determining the suitability of industry-specific humor. To fill this gap, we present the first dataset for assessing LLMs’ humor appropriateness across various industrial contexts. Our dataset includes 304 annotated humorous statements from industry-specific

<sup>*</sup> Equal contribution.



<!-- page 0002 -->

environments and a brief description of each statement.

**Contributions** 1) We introduce the first dataset about humor in industrial settings. 2) We perform a systematic exploration and comparative analysis of LLMs to predict the appropriateness of humorous content. 3) We offer a comprehensive discussion of the identified errors. Our dataset is publicly available at repository.

## 2 Related work

### 2.1 Computational Humor Generation

Computational humor lies at the intersection of Natural Language Processing (NLP) and Humor theory. (Ravi et al., 2024) Early work on computational humor generation focused on automated systems that could produce humorous content, but these were often limited to predefined templates and structures. (Binsted and Ritchie, 1994; Stock and Strapparava, 2005; Dybala et al., 2010; Hong and Ong, 2008) used fixed templates and rules to generate content like puns and acronyms.

The introduction of LLMs has revolutionized computational humor generation. Recent studies have leveraged LLMs’ flexibility and generative capabilities to create diverse, high-quality resources of humorous content. (Chen et al., 2024) generated a 2.1K dataset of puns in Chinese using LLMs, (Zhong et al., 2024) introduced a multimodal resource of humor based on the Oogiri game, and (Tikhonov and Shtykovskiy, 2024a) explored the generation of one-liner jokes using a multi-step reasoning process powered by LLMs. These works highlight LLMs’ potential to generate humor at scale, overcoming the limitations of template-based approaches. However, context-specific humor resources are still needed, as the appropriateness of humor depends on the environment.(Zhou et al., 2023) One such environment is the industrial setting, where humor must be used carefully, but no existing resource addresses this need.

### 2.2 Computational Humor Detection and Evaluation

Alongside the advancements in humor generation, researchers have also explored the use of computational techniques for humor detection, classification, and evaluation. Early studies relied on classic machine learning models like Naive Bayes and Support Vector Machines to classify or identify humor. (Mihalcea and Strapparava, 2005; Yang et al., 2015; Zhang and Liu, 2014)

The rise of LLMs has raised concerns about proper use and issues like bias, impacting computational humor detection and evaluation. (Wu et al., 2024) uses LLMs for humor classification, (Tikhonov and Shtykovskiy, 2024b) evaluates Vision-language models on humor, (Chen et al., 2024) evaluates LLMs on Chinese Pun humor, and (Ravi et al., 2024) uses LLMs as evaluator for their Humor Distillation task.

Despite the progress in computational humor research evaluation, LLMs’ reasoning for specific environments and settings, such as professional, industry-specific humor, has remained unexplored. This paper focuses on developing resources and techniques to answer this growing need.

## 3 Dataset

The proposed dataset contains humor sentences across various industrial contexts, humor types, and appropriateness. This section details the dataset’s construction and description.

### 3.1 Dataset framework

In this subsection, details about each field in the resource is presented.

**Sentence** contains LLM-generated humorous sentences tailored for industrial or professional contexts, highlighting common workplace scenarios that employees may find amusing or relatable.

**Appropriateness** indicates the sentence’s suitability for the given context with for levels. “Offensive” contains humor that targets a specific nation, culture, or group through biased content, or is overly harsh in tone; “Mildly Inappropriate” is typically humor that shows mild disrespect toward a particular role or department within the company; “Neutral” reflects factual observations about the company, avoids targeting specific individuals or departments, and remains free of bias; “Wholesome” is similar to Neutral but often carries a light-hearted tone, highlighting positive aspects of the company humorously.

**Industry-Specific Context** identifies the industry or setting relevant to the humor, like “Marketing” or “Project Management”.

**Humor Type** classifies the humor type, enabling analysis of different humor methods and their ap-



<!-- page 0003 -->

propriateness across contexts. Detailed descriptions of each type are in Appendix A.

| Model | GPT | Claude | Sum |
|---|---:|---:|---:|
| Offensive | 36 | 21 | 57 |
| Mildly inappropriate | 49 | 27 | 76 |
| Neutral | 36 | 48 | 84 |
| Wholesome | 27 | 60 | 87 |
| **Sum** | 148 | 156 | 304 |

Table 1: Sample counts by the model used and level of appropriateness.

**Short Explanation** offers a quick interpretation, outlining the joke or message.

### 3.2 Humorous content generation

Sentences along with their associated features were initially generated through LLM prompting, available in Appendix A. The prompt consists of instances of industrial settings along with a description of each feature. Additionally, several rules were established to ensure distinctiveness, diversity, and conciseness, and to prevent redundancy. Also, each prompt consists of a sequence of following prompts, which emphasize different aspects of the resource, including cultural, industrial, and appropriateness diversity. After the careful process of designing the prompts, Claude 3.5 Sonnet <sup>1</sup> and ChatGPT-4o <sup>2</sup> were used to generate the initial set of samples. This procedure resulted in 340 samples, 170 from each model. Two experienced annotators then reviewed the quality of generated samples and removed irrelevant, repetitive, or nonsensical ones. After this step, the size was reduced to 304.

### 3.3 Annotation

During sample generation, both LLMs were prompted to not only create but also label examples to ensure diversity by type, level, and features, though these initial labels were later discarded. Two male annotators independently assessed each sample for appropriateness, required knowledge, industry context, and humor type. For consistency, they standardized labels when samples described the same context differently. In cases of disagreement between annotators, a third male reviewer was consulted to resolve conflicts.

<sup>1</sup>https://www.anthropic.com/  
<sup>2</sup>https://chatgpt.com/

### 3.4 Description

The resource includes 304 samples, with 138 different industry-specific contexts. The overall distribution of appropriateness levels, humor types, and counts of each model is presented in Tables 1 and 3.

## 4 Experiments

**Data** Our experiments center around the professional, industry-specific dataset introduced in this work. For each experiment, we craft a prompt that includes a general dataset description, explanations of appropriateness levels, and details of the appropriateness classification task. This prompt is paired with a humorous sentence from the dataset and then given to the model. A complete version of the prompt is available in B.

**Model** In addition to Claude3.5 Sonnet and ChatGPT-4o, we evaluated three additional models, two of which are openly accessible: Llama-3.2-1B-Instruct (Meta et al., 2024), Qwen2.5-72B-Instruct (Yang et al., 2024), and Gemini 1.5 Flash<sup>3</sup>. Since the two first models were used in the initial data generation step, each was only tested on the subset they were not involved in generating. We set the temperature to zero in all experiments to ensure deterministic model responses. All responses were collected in November 2024.

## 5 Results

The results of our analysis in Table 2 reveal that both Claude3.5 Sonnet and ChatGPT-4o can determine the appropriateness level of the subset that they were not involved in the generation better than the rest of the models. Apart from the two mentioned models, Llama-3.2-1B-Instruct performs better than Qwen and Gemini. Furthermore, the average f1-score of models on the subset generated by GPT-4o is lower than that of the Claude subset, suggesting it contains more nuanced, context-specific humor that demands a deeper understanding of professional dynamics and workplace culture. The offensive category has low F1-scores in both subsets, indicating that models may overlook cultural or national references, revealing potential biases. For instance, *“In our Italian office, deadlines are merely suggestions – like the speed limit on a Sicilian road”* is offensive toward Italian culture, yet Qwen and Llama classify it as Neutral. The

<sup>3</sup>https://gemini.google.com/



<!-- page 0004 -->

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Generated by Claude3.5 Sonnet</th>
      <th colspan="5">Generated by GPT-4o</th>
    </tr>
    <tr>
      <th>Model</th>
      <th>O</th>
      <th>M</th>
      <th>N</th>
      <th>W</th>
      <th>W. Avg.</th>
      <th>O</th>
      <th>M</th>
      <th>N</th>
      <th>W</th>
      <th>W. Avg.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GPT-4o</td>
      <td><strong>0.50</strong></td>
      <td>0.50</td>
      <td>0.34</td>
      <td>0.88</td>
      <td><strong>0.60</strong></td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Claude3.5 Sonnet</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td><strong>0.74</strong></td>
      <td><strong>0.60</strong></td>
      <td><strong>0.86</strong></td>
      <td>0.77</td>
      <td><strong>0.73</strong></td>
    </tr>
    <tr>
      <td>Gemini 1.5 Flash</td>
      <td>0.17</td>
      <td>0.41</td>
      <td>0.00</td>
      <td><strong>0.99</strong></td>
      <td>0.48</td>
      <td>0.11</td>
      <td><strong>0.60</strong></td>
      <td>0.00</td>
      <td><strong>1.0</strong></td>
      <td>0.41</td>
    </tr>
    <tr>
      <td>Llama-3.2-1B-Instruct</td>
      <td>0.44</td>
      <td>0.46</td>
      <td><strong>0.77</strong></td>
      <td>0.52</td>
      <td>0.58</td>
      <td>0.20</td>
      <td>0.52</td>
      <td>0.80</td>
      <td>0.58</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td>Qwen2.5-72B-Instruct</td>
      <td>0.17</td>
      <td><strong>0.54</strong></td>
      <td>0.15</td>
      <td>0.97</td>
      <td>0.54</td>
      <td>0.00</td>
      <td>0.47</td>
      <td>0.05</td>
      <td>0.96</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td>Average</td>
      <td>0.32</td>
      <td>0.48</td>
      <td>0.31</td>
      <td><strong>0.84</strong></td>
      <td><strong>0.55</strong></td>
      <td>0.26</td>
      <td>0.55</td>
      <td>0.43</td>
      <td><strong>0.83</strong></td>
      <td>0.50</td>
    </tr>
  </tbody>
</table>

Table 2: F1-score of 5 LLMs on the two subsets of the resource. O, M, N, and W are Offensive, Mildly Inappropriate, Neutral, and Wholesome respectively. W. Avg. stands for Weighted average.

| Humor type | Count |
|---|---:|
| Irony | 59 |
| Hyperbole | 26 |
| Self-deprecation | 16 |
| Metaphorical Humor | 43 |
| Situational Humor | 39 |
| Positive Humor | 38 |
| Cultural Reference Humor | 83 |

Table 3: Sample counts by humor type.

| Type | O | M | N | W | W A |
|---|---:|---:|---:|---:|---:|
| Irony | **0.70** | 0.51 | 0.80 | 0.25 | **0.60** |
| Hyperbole | 0.33 | 0.33 | **0.82** | **0.80** | **0.60** |
| Self-dep. | 0.00 | 0.40 | 0.57 | 0.00 | 0.38 |
| Metaphor | 0.33 | **0.60** | 0.75 | 0.33 | 0.56 |
| Situational | 0.00 | 0.44 | 0.84 | 0.46 | 0.56 |
| Positive | - | - | 0.80 | 0.54 | 0.56 |
| Cultural Ref. | 0.07 | 0.53 | 0.75 | 0.73 | 0.41 |

Table 4: F1-score of Llama-3.2-1B-Instruct across different types of humor and levels of appropriateness. O, M, N, and W are Offensive, Mildly Inappropriate, Neutral, and Wholesome respectively. W A stands for Weighted average.

Neutral category also has low F1-scores due to its broad, flexible nature. In contrast, Wholesome and Mildly Inappropriate achieve better scores, especially Wholesome, suggesting these categories are easier for LLMs to detect due to their distinctive boundaries. We choose Llama-3.2-1B-Instruct as the best model since among the models tested on both subsets to analyze the relationship between humor type and models’ ability to predict appropriateness levels.

Table 4 presents the f1-score of the best model across all humor types for each appropriateness level. The natural relationship between each humor type and each level of appropriateness can explain the scores. Irony achieves the highest F1-score in the Offensive category, likely due to its subtle contradictions or contrasts, which can sometimes be interpreted as offensive, especially when highlighting flaws. In the Mildly Inappropriate category, metaphorical humor scores the highest, as metaphors often introduce suggestive comparisons that come close to inappropriateness without being overtly offensive. Hyperbole achieves top scores in both Neutral and Wholesome categories, as its exaggerated statements are humorous yet boundary-respecting, making it well-suited for neutral and wholesome contexts.

## 6 Conclusion

We present the first resource focused on humor within industrial contexts, encompassing a diverse range of humor types and levels of appropriateness. Each sample is tied to a specific context, which shapes its unique humorous character. This work is timely, as humor studies are gaining momentum due to the potential applications of humor in automated tasks, such as email writing. Our goal is to promote human-aligned humor, enabling AI assistants to communicate in a more relatable, human-like manner, by focusing on the intersection of NLP and humor theory.

## 7 Limitations

The present work is not without limitations. Mainly, there are three important limitations associated with the work.

Firstly, the dataset size is limited. While we made efforts to create a valuable resource with a diverse range of contexts, we took care to minimize redundancy by avoiding the creation of samples with similar contexts, meanings, and labels. Nevertheless, the dataset currently contains 304 samples, which presents an opportunity for future expansion.



<!-- page 0005 -->

Additionally, our classification of humor types has some limitations and could be expanded to capture more nuances. For instance, we grouped samples that could be classified as sarcasm under the broader category of irony. This was done to maintain a minimal set of types, as some categories, such as sarcasm, had limited samples in the initial dataset.

Lastly, as both annotators are male we removed all samples containing gender references to avoid bias.

## 8 Ethical Considerations

To streamline dataset compilation, we used LLMs to generate potential humorous examples. While this significantly enhanced efficiency, it may also introduce biases. The humor generated by LLMs could differ from what human experts might select, potentially reflecting biases inherent in the model or prompt design.

The annotation process was carried out by two experienced annotators with industry experience. However, since both annotators are male, there is potential for bias, despite our efforts to eliminate gender references in order to minimize this effect.

## References

John A Banas, Norah Dunbar, Dariela Rodriguez, and Shr-Jie Liu. 2011. A review of humor in educational settings: Four decades of research. *Communication Education*, 60(1):115–144.

Adrian Bardon. 2005. The philosophy of humor. *Comedy: A geographic and historical guide*, 2:462–476.

Ronald A Berk. 2015. The greatest veneration: Humor as a coping strategy for the challenges of aging. *Social Work in Mental Health*, 13(1):30–47.

Kim Binsted and Graeme Ritchie. 1994. An implemented model of punning riddles. *Preprint*, arXiv:cmp-lg/9406022.

Yang Chen, Chong Yang, Tu Hu, Xinhao Chen, Man Lan, Li Cai, Xinlin Zhuang, Xuan Lin, Xin Lu, and Aimin Zhou. 2024. Are U a joke master? pun generation via multi-stage curriculum learning towards a humor LLM. In *Findings of the Association for Computational Linguistics: ACL 2024*, pages 878–890, Bangkok, Thailand. Association for Computational Linguistics.

Rose Laub Coser. 1959. Some social functions of laughter: A study of humor in a hospital setting. *Human relations*, 12(2):171–182.

Pawel Dybala, Michal Ptaszynski, Jacek Maciejewski, Mizuki Takahashi, Rafal Rzepka, and Kenji Araki. 2010. Multiagent system for joke generation: Humor and emotions combined in human-agent conversation. *J. Ambient Intell. Smart Environ.*, 2(1):31–48.

Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier Lopez de Lacalle, and Mikel Artetxe. 2024. BertaQA: How much do language models know about local culture? In *The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track.*

Paweł Gryka, Kacper Gradoń, Marek Kozłowski, Miłosz Kutyła, and Artur Janicki. 2024. Detection of ai-generated emails-a case study. In *Proceedings of the 19th International Conference on Availability, Reliability and Security*, pages 1–8.

William P Hampes. 1992. Relation between intimacy and humor. *Psychological reports*, 71(1):127–130.

Bryan Anthony Hong and Ethel Ong. 2008. Generating punning riddles from examples. In *2008 Second International Symposium on Universal Communication*, pages 347–352.

Ayesha Idrees, Saira Batool, and Rukhsana Kausar. 2020. Styles of humor and interpersonal relationships in university students. *FWU Journal of Social Sciences*, 14(4):57–67.

Tonglin Jiang, Hao Li, and Yubo Hou. 2019. Cultural differences in humor perception, usage, and implications. *Frontiers in psychology*, 10:123.

Marina Jovic and Salaheddine Mnasri. 2024. Evaluating ai-generated emails: A comparative efficiency analysis. *World Journal of English Language*, 14(2).

Zhuoran Lu, Sheshera Mysore, Tara Safavi, Jennifer Neville, Longqi Yang, and Mengting Wan. 2024. Corporate communication companion (ccc): An llm-empowered writing assistant for workplace social media. *arXiv preprint arXiv:2405.04656.*

Owen H Lynch. 2002. Humorous communication: Finding a place for humor in communication research. *Communication theory*, 12(4):423–445.

Jessica Mesmer-Magnus, David J Glew, and Chockalingam Viswesvaran. 2012. A meta-analysis of positive humor in the workplace. *Journal of Managerial Psychology*, 27(2):155–190.

AI Meta, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. 2024. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2.

John C Meyer. 2000. Humor as a double-edged sword: Four functions of humor in communication. *Communication theory*, 10(3):310–331.



<!-- page 0006 -->

John C Meyer. 2015. *Understanding humor through communication: Why be funny, anyway?* Lexington Books.

Rada Mihalcea and Carlo Strapparava. 2005. Making computers laugh: Investigations in automatic humor recognition. In *Proceedings of Human Language Technology Conference and Conference on Empirical Methods in Natural Language Processing*, pages 531–538, Vancouver, British Columbia, Canada. Association for Computational Linguistics.

John Morreall. 1983. Humor and emotion. *American Philosophical Quarterly*, 20(3):297–304.

Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. 2023. Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th annual acm symposium on user interface software and technology*, pages 1–22.

Sahithya Ravi, Patrick Huber, Akshat Shrivastava, Aditya Sagar, Ahmed Aly, Vered Shwartz, and Arash Einolghozati. 2024. Small but funny: A feedback-driven approach to humor distillation. *arXiv preprint arXiv:2402.18113.*

Dmitry Scherbakov, Nina Hubig, Vinita Jansari, Alexander Bakumenko, and Leslie A Lenert. 2024. The emergence of large language models (llm) as a tool in literature reviews: an llm automated systematic review. *arXiv preprint arXiv:2409.04600.*

Leixian Shen, Haotian Li, Yun Wang, and Huamin Qu. 2024. From data to story: Towards automatic animated data video creation with llm-based multi-agent systems. *arXiv preprint arXiv:2408.03876.*

Oliviero Stock and Carlo Strapparava. 2005. HAHAcronym: A computational humor system. In *Proceedings of the ACL Interactive Poster and Demonstration Sessions*, pages 113–116, Ann Arbor, Michigan. Association for Computational Linguistics.

Alexey Tikhonov and Pavel Shtykovskiy. 2024a. Humor mechanics: Advancing humor generation with multistep reasoning. *Preprint*, arXiv:2405.07280.

Alexey Tikhonov and Pavel Shtykovskiy. 2024b. Humor mechanics: Advancing humor generation with multistep reasoning. *arXiv preprint arXiv:2405.07280.*

Jana Vizmuller. 1980. Psychological reasons for using humor in a pedagogical setting. *Canadian modern language review*, 36(2):266–271.

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024. A survey on large language model based autonomous agents. *Frontiers of Computer Science*, 18(6):186345.

Shan Wang. 2024. Investigating the potential of large language models for automated writing scoring. In *2024 5th International Conference on Education, Knowledge and Information Management (ICEKIM 2024)*, pages 1091–1098. Atlantis Press.

Shih-Hung Wu, Yu-Feng Huang, and Tsz-Yeung Lau. 2024. Humour classification by fine-tuning llms: Cyut at clef 2024 joker lab subtask humour classification according to genre and technique. In *Working Notes of the Conference and Labs of the Evaluation Forum (CLEF 2024). CEUR Workshop Proceedings*, pages 1933–1947.

Changrong Xiao, Wenxing Ma, Sean Xin Xu, Kunpeng Zhang, Yufang Wang, and Qi Fu. 2024. From automation to augmentation: Large language models elevating essay scoring landscape. *arXiv preprint arXiv:2401.06431.*

An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. 2024. Qwen2 technical report. *arXiv preprint arXiv:2407.10671.*

Diyi Yang, Alon Lavie, Chris Dyer, and Eduard Hovy. 2015. Humor recognition and humor anchor extraction. In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*, pages 2367–2376, Lisbon, Portugal. Association for Computational Linguistics.

Renxian Zhang and Naishi Liu. 2014. Recognizing humor on twitter. In *Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management*, CIKM ’14, page 889–898, New York, NY, USA. Association for Computing Machinery.

Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, and Pan Zhou. 2024. Let’s think outside the box: Exploring leap-of-thought in large language models with creative humor generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pages 13246–13257.

Xuhui Zhou, Hao Zhu, Akhila Yerukola, Thomas Davidson, Jena D. Hwang, Swabha Swayamdipta, and Maarten Sap. 2023. COBRA frames: Contextual reasoning about effects and harms of offensive statements. In *Findings of the Association for Computational Linguistics: ACL 2023*, pages 6294–6315, Toronto, Canada. Association for Computational Linguistics.

## A Generation of the data

In this appendix, we provide a detailed overview of the process for generating the initial samples. First, various types of humor type in the dataset are explained below:



<!-- page 0007 -->

- **Irony** conveys humor through contrast or subtle contradictions that highlight a disparity between expectations and reality.

- **Hyperbole** uses exaggeration to humorously emphasize a point, often to highlight absurdity or a commonly shared frustration.

- **Self-deprecation humor** employs humility, allowing the speaker to make light of their own flaws or challenges in a relatable way.

- **Metaphorical Humor** uses creative comparisons to convey ideas, often making complex or dry topics more engaging and accessible.

- **Situational Humor** draws humor from specific workplace scenarios or events, creating relatability through common professional experiences.

- **Positive Humor** emphasizes lighthearted, uplifting jokes that foster a positive atmosphere without targeting anyone.

- **Cultural Reference Humor** incorporates widely known cultural elements, allowing the audience to connect over shared knowledge or experiences.

Moreover, we provide the prompt we used to generate the initial dataset. Below, the generation prompt is available:

I am developing a dataset of Professional industries-specific Humor. In the following paragraphs, I will provide some general contexts in which professional humor might appear: Corporate, communications, Marketing, campaigns, Professional presentations, and Email threads.

Also, here are the columns in my dataset:

- **Sentence:** The humorous sentence reflects humor within an industrial or professional context. The sentence aims to highlight a common workplace or industry-specific content in a way that employees can find amusing or relatable.

- **Appropriateness level:** Indicates the sentence’s suitability for the given context with four levels. “Offensive” contains humor that targets a specific nation, culture, or group through biased content, or is overly harsh in tone; “Mildly Inappropriate” is typically humor that shows mild disrespect toward a particular role or department within the company; “Neutral” reflects factual observations about the company, avoids targeting specific individuals or departments, and remains free of bias; “Wholesome” is similar to Neutral but often carries a lighthearted tone, highlighting positive aspects of the company humorously.

- **Industry-specific context:** Identifies the specific industry or professional setting relevant to the humor, such as “Marketing” or “Project Management”.

- **Humor type:** categorizes the type of humor, with various categories. “Irony” conveys humor through contrast or subtle contradictions that highlight a disparity between expectations and reality; “Hyperbole” uses exaggeration to humorously emphasize a point, often to highlight absurdity or a commonly shared frustration; “Self-deprecation” employs humility, allowing the speaker to make light of their own flaws or challenges in a relatable way; “Metaphorical Humor” uses creative comparisons to convey ideas, often making complex or dry topics more engaging and accessible; “Situational Humor” draws humor from specific workplace scenarios or events, creating relatability through common professional experiences; “Positive Humor” emphasizes lighthearted, uplifting jokes that foster a positive atmosphere without targeting anyone; “Cultural Reference Humor” incorporates widely known cultural elements, allowing the audience to connect over shared knowledge or



<!-- page 0008 -->

experiences.

- **Short explanation:** provides a brief interpretation of the humor, outlining the underlying joke or message. This explanation aids in annotating the dataset, helping reviewers understand the humor’s intent and contextual relevance, which is essential for quality control and evaluation.

There are some generation rules:

- Generate as distinct samples as possible.

- Focus on different industries and create diversity in the dataset.

- Use the same words for similar classes, types, etc, when possible.

- Be concise.

- You must return in a CSV-like format, where the separator is "|".

Now, generate 10 samples based on the given description.

Additionally, to increase the diversity of generated samples, we occasionally appended one of several specific sentences to the end of the prompt.

- Focus on different cultures and countries.

- Focus on different industries and companies.

- Focus on different levels of Appropriateness.

- Focus on different types of humor.

- Focus on those that require specific background knowledge.

- Focus on those with the potential of being offensive.

- Focus on those with the potential of being Mildly Inappropriate.

- Focus on those with the potential of being Neutral.

- Focus on those with the potential to be Wholesome.

## B Evaluation Prompt

This appendix provides additional details on our experiments, focusing on the prompt used, as outlined below. We have a dataset of humorous sentences in professional industrial settings. We want you to classify the given sentences based on their appropriateness level. There are four levels of appropriateness:

- “Offensive” contains humor that targets a specific nation, culture, or group through biased content, or is overly harsh in tone.

- “Mildly Inappropriate” is typically humor that shows mild disrespect toward a particular role or department within the company.

- “Neutral” reflects factual observations about the company, avoids targeting specific individuals or departments, and remains free of bias.

- “Wholesome” is similar to Neutral but often carries a lighthearted tone, highlighting positive aspects of the company humorously.

Classify each sentence according to the provided description. Only state the level without further explanation.
