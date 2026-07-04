<!-- Transcribed from 63-sarcasmbench.pdf -->



<!-- page 0001 -->

# SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding

Yazhou Zhang<sup>a,e</sup>, Chunwang Zou<sup>b</sup>, Zheng Lian<sup>c,*</sup>, Prayag Tiwari<sup>d,*</sup>, Jing Qin<sup>e</sup>

<sup>a</sup>*College of Intelligence and Computing, Tianjin University, Tianjin, China*  
<sup>b</sup>*College of Software Engineering, Zhengzhou University of Light Industry, China*  
<sup>c</sup>*Institute of Automation, Chinese Academy of Sciences, China*  
<sup>d</sup>*School of Information Technology, Halmstad University, Sweden*  
<sup>e</sup>*The Hong Kong Polytechnic University, HongKong*

---

## Abstract

In the era of large language models (LLMs), the task of “System I” - the fast, unconscious, and intuitive tasks, e.g., sentiment analysis, text classification, etc., have been argued to be successfully solved. However, sarcasm, as a subtle linguistic phenomenon, often employs rhetorical devices like hyperbole and figuration to convey true sentiments and intentions, involving a higher level of abstraction than sentiment analysis. There is growing concern that the argument about LLMs’ success may not be fully tenable when considering sarcasm understanding. To address this question, we select eleven SOTA LLMs and eight SOTA pre-trained language models (PLMs) and present comprehensive evaluations on six widely used benchmark datasets through different prompting approaches, i.e., zero-shot input/output (IO) prompting, few-shot IO prompting, chain of thought (CoT) prompting. We build SarcasmBench, the first benchmark to comprehensively evaluate LLMs on sarcasm understanding. Our results highlight three key findings: (1) current LLMs underperform supervised PLMs based sarcasm detection baselines. This suggests that significant efforts are still required to improve LLMs’ understanding of human sarcasm. (2) GPT-4 consistently and significantly outperforms other LLMs across various prompting methods, with an average improvement of 14.0%↑. (3) Few-shot IO prompting method outperforms the other two methods: zero-shot IO and few-shot CoT. We hope this paper can provide some guidance for subsequent researchers to better solve sarcasm detection in the era of LLMs.

*Keywords:* Large language models, sarcasm detection, prompting strategy

---

## 1. Introduction

Recent large language models (LLMs) have demonstrated outstanding instruction-following and in-context learning abilities across various natural language processing (NLP) tasks, such as question answering [1], sentiment analysis [2], text classification [3], etc. In the era of LLMs, it has been argued that “System I” tasks - the fast, unconscious, and intuitive tasks have been successfully solved [4]. Persistent focus and efforts from both the academic and industrial sectors have primarily concentrated on what is known as “System II” tasks. Such tasks demand slow, deliberate, and multiple-step cognitive processes, including logical, mathematical, and commonsense reasoning [5].

Sarcasm is a subtle linguistic phenomenon that employs rhetorical devices like hyperbole and figuration to convey true sentiments and intentions that are opposite to the literal meanings of the words used [6]. Humans might say something that sounds positive on the surface, but in reality, they are expressing a negative sentiment. For example, the sentence “I like to be reprimanded.” appears to convey a positive sentiment because it includes the word “like”, which typically signifies positive emotion. However, “reprimanded” generally implies criticism and negative feedback. Sarcasm detection aims to determine whether a given text is sarcastic or non-sarcastic by leveraging different types of information, such as linguistic features, contextual information, etc [7]. Due to its inherently ambiguous and metaphorical nature, sarcasm detection has consistently presented significant challenges, evolving from the era of feature engineering to that of prompt engineering [8, 9].

There is growing concern that the argument about

<sup>*</sup>Corresponding authors.

*Preprint submitted to INFORMATION PROCESSING & MANAGEMENT* August 27, 2024



<!-- page 0002 -->

[Figure: Side-by-side diagram titled “Sentiment Analysis vs Sarcasm Detection.” Left panel: “Instruction: Classify the sentiment of the Input text as Positive or Negative.” “Input: I never thought I’d say this, but I have become one of those people who like bounty bars.” “Output: Negative. The speaker seems to express a negative shift in preference towards liking bounty bars. The use of ‘never thought I’d say this’ seems to add a note of surprise.” “True Label: Negative.” Right panel: “Instruction: Classify the sarcasm polarity of the Input text as Sarcastic or Not Sarcastic.” “Input: I never thought I’d say this, but I have become one of those people who like bounty bars.” “Output: Not Sarcastic. It simply expresses surprise or a change in the speaker’s preferences regarding Bounty bars, which are a type of chocolate bar filled with coconut. Based on the text alone, there is no strong indication of sarcasm.” “True Label: Sarcastic.”]

Figure 1: The comparison of sentiment analysis and sarcasm detection via a LLM.

LLMs’ success may not be fully tenable when considering sarcasm understanding, as it involves a higher level of abstraction than sentiment analysis, as shown in Fig. 1. Hence, the main research question can be written as:

**RQ:** *Have LLMs really made significant progress in understanding sarcasm?*

To answer this question, we propose an evaluation framework that consists of various combinations of LLMs and prompting approaches, systematically assessing the performance of LLMs on sarcasm detection. In particular, we select eleven SOTA LLMs, including ChatGPT[^1], GPT-4 [10], Claude 3[^2], Mistral [11], Baichuan 2/3 [12], ChatGLM 2/3 [13], LLaMA 2/3 [14], Qwen 1.5 [15], and eight PLMs to evaluate their performance on six benchmarks using three popular prompting methods: zero-shot IO prompting, few-shot IO prompting, and CoT prompting.

The experimental results highlight three key findings: (1) Current prompting-based LLMs underperform supervised PLMs across six benchmark datasets. This suggests that significant efforts are still required to improve LLMs’ understanding of human sarcasm. (2) GPT-4 consistently and significantly outperforms other LLMs across various prompting methods, with an average improvement of 14.0%↑. Claude 3 and ChatGPT demonstrate the next best performance after GPT-4. (3) Few-shot IO prompting method outperforms the other two methods: zero-shot IO and few-shot CoT, with an average improvement of 4.5%↑. The reason is that sarcasm detection, being a holistic, intuitive, and non-rational cognitive process, is argued not to adhere to step-by-step logical reasoning, making CoT less effective in understanding sarcasm compared to its effectiveness in mathematical reasoning tasks. This also aligns closely with the key findings of the SarcasmCue framework [16]. These findings underscore the complex nature of sarcasm detection and the current limitations of LLMs, while also highlighting the further need of stronger LLMs.

The main contributions are concluded as follows:

- This is the first work that comprehensively evaluates the performance of LLMs in understanding sarcasm.

- We propose an evaluation framework that consists of various combinations of eleven LLMs and three prompting approaches.

- Comprehensive experiments over six datasets demonstrate the strengths and the limitations of current LLMs.

## 2. Related Work

This section reviews two lines of research that form the basis of this work: sarcasm detection and large language models.

### 2.1. *Sarcasm Detection*

Sarcasm detection aims to identify whether the given text is sarcastic or not [17]. It has evolved from early rule based and statistical learning based approaches to traditional neural methods, such as CNN, RNN, and further advanced to modern neural methods epitomized by Transformer models. In the early stage, the rule based approaches infer the overall sarcasm polarity based on the refined sarcasm rules, such as the occurrence of the interjection word [9]. Statistical learning based approaches mainly employ statistical learning techniques, e.g., SVM, RF, NB, etc., to extract patterns and relationships within the data [18].

As deep learning has shown the superiority over statistical learning, numerous base neural networks, e.g., such as CNN [19], LSTM [20], GCN [21], etc., have been predominantly utilized during the middle stage of sarcasm detection research, aiming to learn and extract complex features in an end-to-end fashion. As the field of deep learning continues to evolve, sarcasm detection research has stepped into the era of pre-trained language models (PLMs). An increasing number of researchers are designing sophisticated PLM architectures to serve

[^1]: https://chat.openai.com/

[^2]: https://claude.ai/



<!-- page 0003 -->

as encoders for obtaining effective text representations. For example, Liu et al. [22] proposed a dual-channel framework by modeling both literal and implied sentiments separately [22]. They also constructed two conflict prompts to elicit PLMs to generate the sarcasm polarity [23]. Qiao et al. presented a mutual-enhanced incongruity learning network to take advantage of the underlying consistency between the two modules to boost the performance [24]. Tian et al. proposed a dynamic routing Transformer network to activate different routing transformer modules for modeling the dynamic mechanism in sarcasm detection [25].

However, the above-mentioned works still focus on how to utilize PLMs to extract effective features, without leveraging the extraordinary understanding capabilities of LLMs. In contrast, this paper employs three prompting methods to make the first attempt to explore the potential of prompting LLMs in sarcasm detection.

### 2.2. *Large Language Models*

LLMs are advanced language models characterized by their substantial parameter sizes and exceptional learning capabilities [26]. In recent years, the community of natural language processing (NLP) has witnessed substantial progress largely due to the development of LLMs. These models excel in areas such as in-context learning, few-shot prompting, and following complex instructions. OpenAI has been at the forefront of this innovation, notably with the introduction of transformative models such as ChatGPT and GPT-4. Nevertheless, the exclusive nature of these technologies has led to the emergence of various LLM versions, which often incorporate tens or even hundreds of billions of parameters [27]. We categorize these LLMs into two groups based on their specialization: general LLMs and specialized LLMs.

General LLMs are designed for versatility across a wide spectrum of NLP tasks. Prominent examples of these models are GPT-4, ChatGLM 4, LLaMA 3<sup>3</sup>, PanGu-Σ [28], Baichuan 3<sup>4</sup>, etc. Such LLMs often perform well across a range of tasks, but their potentials in specific domains await further exploration. In contrast, specialized LLMs are fine-tuned for specific tasks via task-specific architectures and knowledge, allowing them to achieve higher performance. For example, Zhang et al. proposed a fine-tuned context and emotion knowledge tuned LLM for emotion recognition in conversations [2]. They also presented RGPT, an adaptive boosting framework tailored to produce a specialized text classification LLM by recurrently ensembling a pool of strong base learners [3, 29].

However, the above-mentioned studies do not involve sarcasm understanding, we propose an evaluation framework to unlock its potential in sarcasm understanding.

## 3. The Proposed Approach

### 3.1. *Task Definition*

Sarcasm detection is transformed as a conditional generative task, where the output $\mathcal{Y}$ will be the labels. Given a set of input texts $\mathcal{X}=\{x_1,x_2,\ldots,x_N\}$ where each document $x_i$ is augmented with a designed prompt $Prompt_i \in \mathcal{P}$ that provides contextual guidance, i.e., $Prompt_i = INS_i \oplus x_i$, where $INS_i$ represents the task instruction, $\mathcal{P}$ represents the prompt set. Our task is to let a LLM $\mathcal{M}$ map an input document to its target label: $\mathcal{M}(\mathcal{X}, \mathcal{P}, \theta) \rightarrow \mathcal{Y}$, where $\mathcal{Y}=\{y_1,y_2,\ldots,y_N\}$ denotes the label sequence generated by the LLM $\mathcal{M}$. We formulate the problem as:

$$
\mathcal{M}=\arg \max_c \prod_i Prob(y_i=c|x_i, INS_i, \theta)
\tag{1}
$$

### 3.2. *Evaluation Approach*

Fig. 2 shows the overview of our proposed evaluation framework. Initially, we take both sarcastic and non-sarcastic samples as inputs. Subsequently, we design prompts tailored specifically for sarcasm. This involves constructing task instructions and providing examples for few-shot learning. Our evaluation utilizes three distinct prompting approaches: zero-shot IO prompting, few-shot IO prompting, and CoT prompting. These methods are implemented to assess how effectively LLMs generate responses that are both valid and rigorously aligned with the subtleties of sarcastic expressions. Finally, we analyze and compare the outputs generated by the LLMs against the ground truth to evaluate the models’ proficiency in understanding and detecting sarcasm.

### 3.3. *Prompt Construction*

Our prompt $Prompt_i$ contains of three key components:

**(1) Task instruction.** It clearly defines the specific sarcasm detection task the model needs to accomplish. In this work, the task instruction is given as follows:

<sup>3</sup>https://llama.meta.com/  
<sup>4</sup>https://www.baichuan-ai.com



<!-- page 0004 -->

[Figure: Proposed evaluation framework. Top pipeline labeled “Prompting based LLMs” showing example texts passed as a “Prompt” into boxes for “Zero-Shot IO Prompting,” “Few-Shot IO Prompting,” and “CoT Prompting,” then into an LLM architecture block labeled “Linear,” “RMS Norm,” “SwiGLU,” “Grouped Multi-Query K-V Self-Attention,” “Embeddings,” and finally a “Response” box with “Not Sarcastic” and “Sarcastic.” Bottom pipeline labeled “Fine-tuning PLMs/DLMs” showing example texts split into “Training Set” and “Testing Set,” passed through transformer blocks, producing a “Label” box with “Not Sarcastic” and “Sarcastic.”]

Figure 2: The proposed evaluation framework for LLMs and PLMs/DLMs.

*This is a sarcasm classification task. Determine whether the following input text expresses sarcasm, if it does, output ‘sarcastic’, otherwise, output ‘non-sarcastic’. Return the label only without any other text.*

**(2) Input.** The input is every testing sample $x_i$ to classify.

**(3) Demonstration.** It provides specific examples of how to analyze text for sarcasm, showing both sarcastic and non-sarcastic responses to similar situations. It will guide the LLMs in recognizing subtle cues and patterns that identify sarcasm. In addition, it also provides an output format that LLM’s outputs should follow. Note that demonstrations are only needed for the few-shot setup, but not for the zero-shot setup.

We adopt KNN search [30] to sample examples that are similar to the test sequence. In this method, the text initially undergoes transformation into a vector via the encoding function $f$. This vector is then employed as a query to traverse the complete training dataset, aiming to identify the $k$ text sequences closest to it. From these, we extract the $k$ most similar data examples to use as demonstrations.

### 3.4. Three Prompting Approaches

**Zero-shot IO Prompting** refers to the scenario where LLMs generate the output $y$ based purely on the input $x$, without any additional examples or guidance. Mathematically, this can be represented as:

$$
y \sim p_\theta(y \mid x),
$$

where $p_\theta$ represents the pre-trained model, and $x$ is directly passed to the model to generate $y$. The model must rely solely on its prior knowledge and understanding of the task.

**Few-shot IO Prompting** involves providing LLMs with a limited number of examples or demonstrations of the task before predicting the output for a new input $x$. This can be formalized as:

$$
y \sim p_\theta(y \mid \text{prompt}_{IO}(x)),
$$

where $\text{prompt}_{IO}(x)$ embeds input $x$ within a context of task instructions and few-shot examples. In this approach, $p_\theta$ adapts based on the provided examples, which helps guide the model in generating more accurate outputs.



<!-- page 0005 -->

**Few-shot CoT prompting** extends the idea of few-shot prompting by explicitly modeling intermediate reasoning steps between the input $x$ and the final output $y$. The LLM is guided through a sequence of logical steps $z_1, z_2, \ldots, z_n$, leading to the final answer. This process is described as:

$$
[z_1, z_2, \ldots, z_n, y] \sim p_{\mathrm{CoT}\theta}(z_1, z_2, \ldots, z_n, y \mid x),
$$

where each $z_i$ represents a coherent reasoning step. By incorporating these intermediate steps, the model is better able to handle complex tasks, such as solving multi-step problems or answering detailed questions.

## 4. Experiments

### 4.1. *Dataset*

**Datasets.** Six benchmark datasets are selected as the experimental beds which encompass the most significant datasets used in sarcasm detection tasks. They are IAC-V1 [31], IAC-V2 [32], Ghosh [33], iSarcasmEval [34], Riloff [35] and SemEval 2018 Task 3 [36].

**IAC-V1 and IAC-V2** are from the Internet Argument Corpus (IAC) [37], specifically designed for the task of identifying and analyzing sarcastic remarks within online debates and discussions. It encompasses a balanced mixture of sarcastic and non-sarcastic comments.

**Ghosh** consists of 51,189 tweets (24,453 sarcastic tweets and 26,736 non-sarcastic tweets) in which sarcastic tweets are automatically collected from Twitter using the user’s self-declaration of sarcasm/irony with sarcastic and ironic hashtags (e.g. #irony, #sarcasm). In this work, we have conducted a thorough double-check of this dataset and successfully filtered out 7,804 noisy tweets.

**iSarcasmEval** is the first shared task to target intended sarcasm detection. Each sample in this dataset is provided and labelled by the authors of the texts themselves. For sarcastic texts, there is a rephrase that conveys the same message non-sarcastically. For English sarcastic texts, there is a label specifying the category of ironic speech that it reflects.

**Riloff** collects a set of 1,600 tweets that contain #sarcasm or #sarcastic, and another 1,600 without these tags. It chooses to remove such tags from all tweets and present the tweets to a group of human annotators for final labelling.

**SemEval 2018 Task 3** is collected using irony-related hashtags (i.e. #irony, #sarcasm, #not) and are subsequently manually annotated to minimize the amount of noise in the corpora. It emphasizes the challenges inherent in identifying sarcasm within the constraints of MUStARD’s concise format and highlights the importance of context and linguistic subtleties in recognizing sarcasm. The statistics for each dataset are shown in Table 1.

Table 1: Dataset statistics.

| Dataset | Train | Valid | Test | Sarcastic | Non-sarcastic |
|---|---:|---:|---:|---:|---:|
| IAC-V1 | 1214 | 304 | 417 | 973 | 962 |
| IAC-V2 | 4031 | 1008 | 1481 | 3260 | 3260 |
| Ghosh | 32708 | 8687 | 2000 | 19546 | 23839 |
| iSarcasmEval | 821 | 280 | 299 | 200 | 1200 |
| Riloff | 276 | 100 | 113 | 77 | 412 |
| SemEval Task 3 | 2910 | 924 | 784 | 2222 | 2396 |

### 4.2. *Evaluation Metrics*

To make a fair comparison, we employ *precision* (P), *recall* (R), *accuracy* (Acc) and *F1* as evaluation metrics. For each method, we run five random seeds and report the average result of the test sets. The metrics are written as:

$$
\begin{aligned}
P &= \frac{TP}{TP + FP}, \\
R &= \frac{TP}{TP + FN}, \\
F1 &= \frac{2 * P * R}{P + R}, \\
Acc &= \frac{TP + TN}{TP + FN + FP + TN},
\end{aligned}
\tag{2}
$$

where TP (True Positives) is the number of positive samples correctly identified, FP (False Positives) is the number of negative samples incorrectly labeled as positive, FN (False Negatives) is the number of positive samples incorrectly labeled as negative, TN (True Negatives) is the number of negative samples correctly identified.

### 4.3. *Implementation Details*

We use the official implementations and hyper-parameters for all traditional deep learning models (DLMs) and PLMs based approaches. For example, all weight matrices are given their initial values by sampling from a uniform distribution $U(-0.1, 0.1)$. The learning rate is set to 5e-5. The batch size is set to 32 and the number of epochs is set to 30. The dropout rate is set to 0.5. In contrast, the LLMs based methods are implemented with the respective official Python API library and the Hugging Face Transformers library[^5]. All

[^5]: https://huggingface.co/docs/transformers



<!-- page 0006 -->

the experiments are conducted on an NVIDIA GeForce GTX 4090 GPU.

#### 4.4. *Compared Baselines*

A wide range of strong baselines are included for comparison including DLMs, PLMs and LLMs. They are:

- ***Random:***

  **(1) Random** This baseline makes random predictions sampled uniformly across the test set.

- ***DLMs based approaches:***

  **(2) TextCNN [38]** designs a CNN [38] with three convolutional layers and a fully connected layer. It is trained on top of word embeddings for utterance-level classification.

  **(3) LSTM** takes word embeddings as input and takes the hidden representation of each word for sarcasm classification.

  **(4) Bi-LSTM [39]** implements a bidirectional LSTM to learn both forward and backward long-range dependency information.

  **(5) AT-LSTM [40]:** is an attention-based LSTM with aspect embedding. We obtain aspect embeddings by averaging the vectors of words, and append it with each word embedding vector.

- ***PLMs based approaches:***

  **(6) BERT [41]** produces contextualized word embeddings for sarcasm detection.

  **(7) RoBERTa [42]** builds on BERT and modifies key hyperparameters, removing the next-sentence pretraining objective and training with much larger mini-batches and learning rates.

  **(8) DeBERT [43]** improves the BERT and RoBERTa models using the disentangled attention mechanism.

  **(9) XLNet [44]** improves the BERT through a generalized autoregressive pretraining method enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order.

  **(10) DC-Net-RoBERTa [45]** designs the dual-channel network (DC-Net) to recognize sentiment conflict by modeling both literal and implied sentiments separately.

- ***LLMs based approaches:***

  **(11) Baichuan 2 [12]** is a Chinese LLM trained from scratch, on 2.6 trillion tokens. It matches or outperforms other open-source models of similar size on public benchmarks.

  **(12-13) ChatGLM 2/3 [13]** are two open bilingual language model based on General Language Model (GLM) framework, with 6.2 billion parameters.

  **(14-15) LLaMA 2/3 [14]** are trained on 2 trillion tokens, and have double the context length than Llama 1, and outperform other open source language models on many external benchmarks.

  **(16) Mistral [11]** consistently outperforms Llama2-13B on all metrics and stands competitively with Llama-34B.

  **(17-18) Qwen 1.5/2 [15]** are two SOTA LLMs trained on data in 27 additional languages besides English and Chinese and achieves state-of-the-art performance in a large number of benchmark evaluations.

  **(19-20) GPT-3.5/4 [10]** are considered as two strongest general LLM.

  **(21) Claude 3**[^6] is Anthropic’s second-most powerful AI model, with strong performance on highly complex tasks.

#### 4.5. *Results and Analysis of Zero-Shot IO Prompting*

We report all of the **Accuracy, Precision, Recall** and macro **F1** scores for 21 models in Table 2. We highlight three key observations:

**(1) In the zero-shot IO setting, PLMs demonstrate outstanding performance, significantly surpassing traditional DLMs.** For instance, RoBERTa achieves an average F1 score of 71.3 across all datasets, while DC-Net-RoBERTa reaches 71.5. In contrast, traditional models like Bi-LSTM and AT-LSTM score lower, with F1 scores of 66.7 and 65.3, respectively. PLMs outperform traditional methods by approximately 7.8%↑. This superiority stems from the extensive pretraining that PLMs undergo on large-scale data, enabling them to better capture contextual information and adapt to various tasks. Although traditional deep learning models perform adequately on specific tasks, their lack of large-scale pretraining support limits their generalization capabilities, resulting in weaker performance.

[^6]: https://claude.ai/



<!-- page 0007 -->

[Figure: Three side-by-side boxed examples titled “Zero-shot IO setting”, “Few-shot IO setting”, and “Chain-of-Thought setting”.]

**Zero-shot IO setting**

**Instruction:** This is a sarcasm classification task. Determine whether the following input text expresses sarcasm, if it does, output ‘sarcastic’, otherwise, output ‘non-sarcastic’.

**Input:** I love doing 20 sprints in 103 degree weather.

**Output:** sarcastic

**Few-shot IO setting**

**Instruction:** This is a sarcasm classification task. Determine whether the following input text expresses sarcasm, if it does, output ‘sarcastic’, otherwise, output ‘non-sarcastic’.

**# Example:**  
Input: Oh No, everyone! Our class project has been plagiarized! What on earth shall we do to salvage our grades?  
Output: sarcastic

**Input:** So many useless classes , great to be student.

**Output:** sarcastic

**Chain-of-Thought setting**

**Instruction:** This is a sarcasm classification task. Determine whether the following input text expresses sarcasm, if it does, output ‘sarcastic’, otherwise, output ‘non-sarcastic’.

**# Example:**  
Input: Oh No, everyone! Our class project has been plagiarized! What on earth shall we do to salvage our grades?  
**Let's think step-by-step.** The input text "Oh No, everyone! Our class project has been plagiarized! What on earth shall we do to salvage our grades?" expresses sarcasm. The exaggerated despair and rhetorical question suggest a sarcastic tone.  
Output: sarcastic

**Input:** I know, Chloe's misuse of the word strikes again.

**Output:** Let's think step-by-step.....The overall sentiment is non-sarcastic.

Figure 3: Examples of three prompting approaches.

**(2) Despite that current LLMs have not yet fully outperformed PLMs, their potential is evident in particular tasks.** For example, GPT-4 Turbo excels in the IAC-V1 and SemEval Task 3 datasets, achieving F1 scores of 78.7 and 76.5, respectively, significantly outperforming RoBERTa’s scores of 69.9 and 72.0, with the margin of 8.8% and 4.5%↑. However, LLMs fall short in datasets like iSarcasmEval and Riloff, where their performance does not meet expectations. The average F1 score shows that GPT-4 Turbo’s difference from RoBERTa in the IAC-V2 and Ghosh datasets is relatively small. This performance variation may be due to LLMs’ advantage in handling long texts and complex semantics, but their generalization capabilities are weaker when facing domain-specific or fine-grained tasks without specialized tuning. Therefore, while LLMs show strong potential in some tasks, their consistency and generalization across different tasks still need improvement.

**(3) Among all 11 LLMs, GPT-4 Turbo demonstrates a comprehensive lead.** It performs exceptionally well across multiple datasets, particularly in IAC-V1 and SemEval Task 3, where it achieves F1 scores of 78.7 and 76.5, significantly higher than Claude-3-haiku’s 77.0 and 57.9. Additionally, in the Ghosh dataset, GPT-4 Turbo reaches an F1 score of 82.2, far surpassing other models like ChatGPT (71.4), Claude-3-haiku (71.8) and LLaMA 3-8B (66.8). A significant reason for GPT-4’s superiority over other models is its larger parameter size, which enhances its human language comprehension and reasoning capabilities. In contrast, most other models are smaller, with around 7B/8B parameters, which limits their ability to handle complex tasks. Moreover, GPT-4’s ability to adapt to various data types and text structures across different tasks further contributes to its outstanding performance. Thus, GPT-4’s strong results underscore its leading position among LLMs and its powerful generalization capabilities.

#### 4.6. Few-Shot vs. Zero-Shot

Since the above experiments are mainly based on a zero-shot IO setting, we are curious of whether the conclusions also apply in a few-shot scenario. Therefore, we perform few-shot experiments to evaluate whether the LLMs can perform better with a limited number of examples. We show the main results in Table 3 and Fig. 5, we sample $k = 2$ examples (including one sarcastic example and one non-sarcastic example) from the training set via KNN search.

We can make two main observations. (1) In the few-shot IO prompting setting, GPT-4 consistently outperforms RoBERTa and DC-Net-RoBERTa on three datasets: IAC-V1, SemEval 2018 Task 3, and Ghosh. Specifically, GPT-4 achieves an F1 score of 79.6 on IAC-V1, which is significantly higher than RoBERTa’s 69.9 and DC-Net-RoBERTa’s 69.1. On SemEval 2018 Task 3, GPT-4 reaches an F1 score of 68.3, surpassing RoBERTa’s 64.0 and DC-Net-RoBERTa’s 67.8. Compared to the zero-shot setting, GPT-4 shows improvement on the remaining three datasets, indicating that with the benefit of a few examples, GPT-4 significantly enhances its performance. For example, on the iSarcasmEval dataset, GPT-4’s F1 score increases from 39.8



<!-- page 0008 -->

Table 2: Performance on six datasets. For LLMs, all strategies are based on a **zero-shot IO setting**. <span style="color: blue">Blue</span> indicates the best results across LLMs.

| Paradigm | Model | IAC-V1 Acc | IAC-V1 P | IAC-V1 R | IAC-V1 F1 | IAC-V2 Acc | IAC-V2 P | IAC-V2 R | IAC-V2 F1 | iSarcasmEval Acc | iSarcasmEval P | iSarcasmEval R | iSarcasmEval F1 | Avg. of F1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Random | Random | 52.0 | 62.5 | 48.4 | 54.5 | 51.9 | 52.1 | 53.2 | 52.7 | 56.5 | 15.2 | 52.6 | 23.5 | 43.5 |
| DLMs | LSTM | 55.3 | 54.9 | 54.9 | 54.8 | 68.5 | 72.3 | 68.0 | 68.8 | 72.7 | 57.0 | 55.1 | 55.6 | 59.7 |
|  | TextCNN | 54.2 | 53.7 | 53.6 | 53.6 | 68.2 | 68.3 | 67.7 | 67.9 | 72.1 | 54.5 | 53.1 | 53.4 | 58.3 |
|  | Bi-LSTM | 64.6 | 64.6 | 64.6 | 64.6 | 79.7 | 79.8 | 79.7 | 79.7 | 74.9 | 57.0 | 55.4 | 55.8 | 66.7 |
|  | AT-LSTM | 65.5 | 65.9 | 65.5 | 65.3 | 76.2 | 76.7 | 76.2 | 76.1 | 73.5 | 55.8 | 53.2 | 54.6 | 65.3 |
| PLMs | BERT | 65.3 | 65.4 | 65.1 | 65.2 | 76.4 | 76.5 | 76.1 | 76.2 | 74.0 | 62.5 | 58.2 | 58.8 | 66.8 |
|  | RoBERTa | **70.1** | **70.0** | **70.1** | **69.9** | 80.7 | 80.9 | 80.8 | 80.7 | 78.9 | 66.4 | 57.5 | 63.5 | 71.3 |
|  | DeBERT | 66.7 | 66.8 | 66.7 | 66.6 | 78.3 | 78.4 | 78.1 | 78.2 | 71.2 | 58.4 | 55.6 | 56.9 | 67.2 |
|  | DC-Net-RoBERTa | 69.3 | 69.7 | 69.3 | 69.1 | **81.7** | **81.7** | **81.7** | **81.7** | **79.5** | **67.1** | **58.3** | **64.0** | **71.5** |
| LLMs$_{0\text{-shot IO}}$ | Baichuan 2-7B | 57.3 | 67.5 | 54.4 | 60.2 | 62.8 | 62.3 | 65.9 | 64.0 | 38.5 | 12.4 | 63.2 | 20.7 | 48.3 |
|  | ChatGLM 2-6B | 47.0 | 69.0 | 19.8 | 30.7 | 51.0 | 54.5 | 15.6 | 24.2 | <span style="color: blue">**66.6**</span> | 6.9 | 13.2 | 9.1 | 21.3 |
|  | ChatGLM 3-6B | 54.0 | 62.1 | 58.1 | 60.0 | 61.8 | 59.8 | 73.3 | 65.9 | 66.6 | 20.2 | 55.3 | 30.0 | 52.0 |
|  | LLaMA 2-7B | 59.2 | 59.7 | 96.8 | 73.9 | 50.6 | 50.4 | 97.3 | 66.4 | 19.1 | 13.3 | 97.4 | 23.4 | 54.6 |
|  | LLaMA 3-8B | 60.4 | 60.1 | 93.5 | 73.8 | 52.1 | 51.2 | 97.8 | 67.2 | 13.4 | 12.8 | <span style="color: blue">**100.0**</span> | 22.7 | 54.6 |
|  | Mistral-7B | 61.9 | 67.6 | 69.0 | 68.3 | 57.9 | 56.1 | 75.0 | 64.2 | 46.8 | 16.2 | 76.3 | 26.7 | 53.1 |
|  | Qwen 1.5-7B | 59.2 | 59.4 | <span style="color: blue">**99.6**</span> | 74.4 | 50.0 | 50.1 | <span style="color: blue">**99.5**</span> | 66.7 | 12.7 | 12.7 | <span style="color: blue">**100.0**</span> | 22.6 | 54.6 |
|  | Qwen 2-7B | 56.6 | 36.3 | 76.9 | 49.3 | 51.8 | 28.9 | 57.8 | 38.6 | 46.1 | 18.2 | 36.4 | 24.3 | 37.4 |
|  | ChatGPT | 63.6 | 61.2 | 81.8 | 70.0 | 56.4 | 50.2 | 91.6 | 64.9 | 51.5 | 14.3 | 91.7 | 26.2 | 53.7 |
|  | GPT-4 Turbo | <span style="color: blue">**72.7**</span> | <span style="color: blue">**73.3**</span> | 85.1 | <span style="color: blue">**78.7**</span> | <span style="color: blue">**71.4**</span> | <span style="color: blue">**65.1**</span> | 92.9 | <span style="color: blue">**76.6**</span> | 65.6 | <span style="color: blue">**25.6**</span> | 89.5 | <span style="color: blue">**39.8**</span> | <span style="color: blue">**65.0**</span> |
|  | Claude-3-haiku | 66.7 | 65.3 | 94.0 | 77.0 | 58.3 | 54.7 | 97.8 | 70.2 | 31.4 | 15.4 | 97.4 | 26.5 | 57.9 |

| Paradigm | Model | Riloff Acc | Riloff P | Riloff R | Riloff F1 | SemEval Task 3 Acc | SemEval Task 3 P | SemEval Task 3 R | SemEval Task 3 F1 | Ghosh Acc | Ghosh P | Ghosh R | Ghosh F1 | Avg. of F1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Random | Random | 50.4 | 5.8 | 30.0 | 9.7 | 48.9 | 38.5 | 48.2 | 42.8 | 49.8 | 49.8 | 51.4 | 50.6 | 34.3 |
| DLMs | LSTM | 76.0 | 61.0 | 64.0 | 62.0 | 73.2 | 65.4 | 68.7 | 67.3 | 70.4 | 73.2 | 58.7 | 65.2 | 65.0 |
|  | TextCNN | 75.1 | 62.8 | 62.2 | 62.7 | 64.0 | 65.0 | 64.0 | 63.0 | **84.8** | **83.3** | **82.9** | **83.1** | 69.6 |
|  | Bi-LSTM | 69.6 | 60.5 | 64.2 | 61.7 | 66.4 | 60.5 | 66.7 | 63.4 | 74.7 | 70.8 | 67.9 | 69.3 | 64.8 |
|  | AT-LSTM | 77.7 | 58.5 | 60.4 | 59.6 | 72.8 | 64.8 | 69.3 | 67.0 | 75.2 | 68.7 | 69.8 | 70.1 | 65.6 |
| PLMs | BERT | 79.7 | **72.6** | 56.6 | 63.6 | 69.6 | 63.5 | 74.1 | 68.4 | 79.2 | 70.9 | 80.6 | 78.8 | 70.2 |
|  | RoBERTa | **84.0** | 64.0 | **75.0** | **69.0** | **75.0** | 64.0 | **84.0** | **72.0** | 80.3 | 80.3 | 79.8 | 80.0 | **73.7** |
|  | XLNet | 83.5 | 52.0 | 73.0 | 61.0 | 66.0 | 55.0 | 83.0 | 66.0 | 77.2 | 77.7 | 78.2 | 77.9 | 68.3 |
|  | DC-Net-RoBERTa | 82.6 | 67.4 | 70.3 | 67.8 | 70.9 | **69.7** | 68.3 | 68.7 | **82.2** | **81.0** | **81.7** | **81.3** | 72.6 |
| LLMs$_{0\text{-shot IO}}$ | Baichuan 2-7B | 25.7 | 9.8 | 90.0 | 17.6 | 47.2 | 41.9 | 85.5 | 56.2 | 55.7 | 53.7 | 82.4 | 65.0 | 46.3 |
|  | ChatGLM 2-6B | 67.3 | 0.9 | 0.0 | 0.0 | 54.0 | 32.1 | 14.5 | 20.0 | 41.1 | 24.1 | 8.3 | 12.4 | 10.8 |
|  | ChatGLM 3-6B | <span style="color: blue">**74.3**</span> | 14.8 | 40.0 | 21.6 | 74.1 | <span style="color: blue">**62.8**</span> | 85.2 | 72.3 | 64.1 | 66.7 | 56.2 | 61.0 | 51.6 |
|  | LLaMA 2-7B | 15.0 | 9.4 | <span style="color: blue">**100.0**</span> | 17.2 | 41.2 | 39.9 | 95.8 | 56.4 | 49.7 | 49.8 | 97.7 | 66.0 | 46.5 |
|  | LLaMA 3-8B | 9.7 | 8.9 | <span style="color: blue">**100.0**</span> | 16.4 | 40.2 | 39.9 | <span style="color: blue">**100.0**</span> | 57.0 | 50.4 | 50.2 | 99.7 | 66.8 | 46.7 |
|  | Mistral-7B | 57.5 | 12.0 | 60.0 | 20.0 | 54.2 | 46.3 | 95.8 | 62.4 | 59.7 | 56.3 | 86.5 | 68.2 | 50.2 |
|  | Qwen 1.5-7B | 8.8 | 8.5 | <span style="color: blue">**100.0**</span> | 16.3 | 39.7 | 39.7 | <span style="color: blue">**100.0**</span> | 56.8 | 50.0 | 50.0 | <span style="color: blue">**100.0**</span> | 66.7 | 46.6 |
|  | Qwen 2-7B | 51.6 | <span style="color: blue">**20.8**</span> | 30.1 | 23.4 | 45.1 | 30.7 | 51.0 | 38.3 | 65.6 | 54.4 | 87.7 | 68.3 | 43.3 |
|  | ChatGPT | 55.0 | 15.4 | 96.7 | 26.6 | 52.2 | 48.3 | 99.7 | 65.1 | 63.3 | 58.2 | 90.4 | 71.4 | 54.4 |
|  | GPT-4 Turbo | 64.6 | 20.0 | <span style="color: blue">**100.0**</span> | <span style="color: blue">**33.3**</span> | <span style="color: blue">**76.1**</span> | <span style="color: blue">**62.8**</span> | 98.1 | <span style="color: blue">**76.5**</span> | <span style="color: blue">**79.8**</span> | <span style="color: blue">**73.5**</span> | 93.3 | <span style="color: blue">**82.2**</span> | <span style="color: blue">**64.0**</span> |
|  | Claude-3-haiku | 24.8 | 10.5 | <span style="color: blue">**100.0**</span> | 19.0 | 46.8 | 42.7 | 99.7 | 59.8 | 61.2 | 56.4 | 98.8 | 71.8 | 50.2 |

in zero-shot to 52.3 in few-shot, marking a 31.4% improvement.

(2) A series of LLMs exhibit slight performance improvements compared to the zero-shot setting. For instance, ChatGPT’s F1 score on the IAC-V1 dataset rises from 70.0 in zero-shot to 73.2 in few-shot, reflecting a 4.6% improvement. Similarly, ChatGLM 3-6B shows an increase in its F1 score on IAC-V1 from 52.0 in zero-shot to 52.7 in few-shot, representing a 1.3% gain. Mistral-7B displays a more notable improvement on the iSarcasmEval dataset, where its F1 score advances from 26.7 in zero-shot to 28.0 in few-shot, indicating a 2.9% enhancement. Even though the extent of enhancement differs across models and datasets, the few-shot setup generally contributes to better outcomes. We can also see that 7B/6B LLMs has relatively based in-context learning ability and they cannot address too complex prompts. But for some business LLMs such as GPT-4, with larger model size, they have better in-context learning ability.



<!-- page 0009 -->

Table 3: Performance on six datasets. For LLMs, all strategies are based on a **few-shot IO setting**. <span style="color:blue">Blue</span> indicates the best results across LLMs.

<table>
<thead>
<tr>
<th rowspan="2">Paradigm</th>
<th rowspan="2">Model</th>
<th colspan="4">IAC-V1</th>
<th colspan="4">IAC-V2</th>
<th colspan="4">iSarcasmEval</th>
<th rowspan="2">Avg. of F1</th>
</tr>
<tr>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">PLMs</td>
<td>RoBERTa</td>
<td><strong>70.1</strong></td><td><strong>70.0</strong></td><td><strong>70.1</strong></td><td><strong>69.9</strong></td>
<td>80.7</td><td>80.9</td><td>80.8</td><td>80.7</td>
<td>78.9</td><td>66.4</td><td>57.5</td><td>63.5</td>
<td style="background-color:#e6ffb8;">71.3</td>
</tr>
<tr>
<td>DC-Net-RoBERTa</td>
<td>69.3</td><td>69.7</td><td>69.3</td><td>69.1</td>
<td><strong>81.7</strong></td><td><strong>81.7</strong></td><td><strong>81.7</strong></td><td><strong>81.7</strong></td>
<td><strong>79.5</strong></td><td><strong>67.1</strong></td><td><strong>58.3</strong></td><td><strong>64.0</strong></td>
<td style="background-color:#e6ffb8;"><strong>71.5</strong></td>
</tr>
<tr>
<td rowspan="11">$LLMs_{k\text{-shot IO}}$</td>
<td>BaiChuan 2-7B</td>
<td>46.5</td><td>57.5</td><td>38.7</td><td>46.3</td>
<td>53.5</td><td>53.9</td><td>51.6</td><td>52.7</td>
<td>61.2</td><td>13.9</td><td>39.5</td><td>20.5</td>
<td style="background-color:#e6ffb8;">39.8</td>
</tr>
<tr>
<td>ChatGLM 2-6B</td>
<td>46.3</td><td>61.3</td><td>26.2</td><td>36.7</td>
<td>52.3</td><td>54.2</td><td>31.9</td><td>40.1</td>
<td>58.2</td><td>14.6</td><td>47.4</td><td>22.4</td>
<td style="background-color:#e6ffb8;">33.1</td>
</tr>
<tr>
<td>ChatGLM 3-6B</td>
<td>56.1</td><td>73.4</td><td>41.1</td><td>52.7</td>
<td>66.2</td><td>69.6</td><td>58.1</td><td>63.3</td>
<td>73.6</td><td>21.1</td><td>39.5</td><td>27.5</td>
<td style="background-color:#e6ffb8;">47.8</td>
</tr>
<tr>
<td>LLaMA 2-7B</td>
<td>46.0</td><td>55.8</td><td>44.8</td><td>50.0</td>
<td>45.9</td><td>45.8</td><td>42.1</td><td>43.9</td>
<td>63.9</td><td>10.2</td><td>23.7</td><td>14.3</td>
<td style="background-color:#e6ffb8;">36.1</td>
</tr>
<tr>
<td>LLaMA 3-8B</td>
<td>43.4</td><td>61.5</td><td>12.9</td><td>21.3</td>
<td>56.4</td><td>68.1</td><td>24.7</td><td>36.3</td>
<td>84.6</td><td>21.4</td><td>7.9</td><td>11.5</td>
<td style="background-color:#e6ffb8;">23.0</td>
</tr>
<tr>
<td>Mistral-7B</td>
<td>65.2</td><td>65.7</td><td>86.7</td><td>74.8</td>
<td>57.4</td><td>54.6</td><td>90.7</td><td>68.1</td>
<td>51.8</td><td>17.3</td><td>73.7</td><td>28.0</td>
<td style="background-color:#e6ffb8;">57.0</td>
</tr>
<tr>
<td>Qwen 1.5-7B</td>
<td>60.9</td><td>62.5</td><td>85.5</td><td>72.2</td>
<td>52.1</td><td>51.5</td><td>80.6</td><td>62.8</td>
<td>31.4</td><td>13.9</td><td>84.2</td><td>23.8</td>
<td style="background-color:#e6ffb8;">52.9</td>
</tr>
<tr>
<td>Qwen 2-7B</td>
<td>61.5</td><td>63.5</td><td>84.7</td><td>73.0</td>
<td>53.5</td><td>53.3</td><td>75.1</td><td>62.7</td>
<td>33.0</td><td>16.7</td><td>78.8</td><td>26.4</td>
<td style="background-color:#e6ffb8;">54.0</td>
</tr>
<tr>
<td>ChatGPT</td>
<td>69.4</td><td>74.3</td><td>72.1</td><td>73.2</td>
<td>72.2</td><td>67.8</td><td>83.1</td><td>75.1</td>
<td>76.1</td><td>34.7</td><td>85.3</td><td>49.2</td>
<td style="background-color:#e6ffb8;">65.9</td>
</tr>
<tr>
<td>GPT-4 Turbo</td>
<td><span style="color:blue"><strong><u>73.3</u></strong></span></td><td><span style="color:blue"><strong><u>75.4</u></strong></span></td><td>84.6</td><td><span style="color:blue"><strong><u>79.6</u></strong></span></td>
<td><span style="color:blue"><strong><u>74.5</u></strong></span></td><td><span style="color:blue"><strong><u>70.0</u></strong></span></td><td>86.2</td><td><span style="color:blue"><strong><u>77.2</u></strong></span></td>
<td><span style="color:blue"><strong><u>79.3</u></strong></span></td><td><span style="color:blue"><strong><u>37.0</u></strong></span></td><td>89.5</td><td><span style="color:blue"><strong><u>52.3</u></strong></span></td>
<td style="background-color:#e6ffb8;"><span style="color:blue"><strong><u>69.7</u></strong></span></td>
</tr>
<tr>
<td>Claude-3-haiku</td>
<td>63.5</td><td>63.9</td><td><span style="color:blue"><strong><u>89.1</u></strong></span></td><td>74.4</td>
<td>61.0</td><td>56.5</td><td><span style="color:blue"><strong><u>96.6</u></strong></span></td><td>71.3</td>
<td>36.5</td><td>16.4</td><td><span style="color:blue"><strong><u>97.4</u></strong></span></td><td>28.0</td>
<td style="background-color:#e6ffb8;">57.9</td>
</tr>
</tbody>
<thead>
<tr>
<th rowspan="2">Paradigm</th>
<th rowspan="2">Model</th>
<th colspan="4">Riloff</th>
<th colspan="4">SemEval Task 3</th>
<th colspan="4">Ghosh</th>
<th rowspan="2">Avg. of F1</th>
</tr>
<tr>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">PLMs</td>
<td>RoBERTa</td>
<td><strong>84.0</strong></td><td>64.0</td><td><strong>75.0</strong></td><td><strong>69.0</strong></td>
<td><strong>75.0</strong></td><td>64.0</td><td><strong>84.0</strong></td><td><strong>72.0</strong></td>
<td>80.3</td><td>80.3</td><td>79.8</td><td>80.0</td>
<td style="background-color:#e6ffb8;"><strong>73.7</strong></td>
</tr>
<tr>
<td>DC-Net-RoBERTa</td>
<td>82.6</td><td><strong>67.4</strong></td><td>70.3</td><td>67.8</td>
<td>70.9</td><td><strong>69.7</strong></td><td>68.3</td><td>68.7</td>
<td><strong>82.2</strong></td><td><strong>81.0</strong></td><td><strong>81.7</strong></td><td><strong>81.3</strong></td>
<td style="background-color:#e6ffb8;">72.6</td>
</tr>
<tr>
<td rowspan="11">$LLMs_{k\text{-shot IO}}$</td>
<td>BaiChuan 2-7B</td>
<td>52.2</td><td>9.3</td><td>50.0</td><td>15.6</td>
<td>53.7</td><td>44.7</td><td>71.1</td><td>54.9</td>
<td>58.5</td><td>57.2</td><td>67.3</td><td>61.9</td>
<td style="background-color:#e6ffb8;">44.1</td>
</tr>
<tr>
<td>ChatGLM 2-6B</td>
<td>51.3</td><td>4.1</td><td>20.0</td><td>6.8</td>
<td>52.6</td><td>40.3</td><td>40.8</td><td>40.6</td>
<td>45.1</td><td>44.4</td><td>39.6</td><td>41.9</td>
<td style="background-color:#e6ffb8;">29.8</td>
</tr>
<tr>
<td>ChatGLM 3-6B</td>
<td><span style="color:blue"><strong><u>81.4</u></strong></span></td><td>7.7</td><td>10.0</td><td>8.7</td>
<td>69.6</td><td>63.3</td><td>55.9</td><td>59.4</td>
<td>53.7</td><td>59.1</td><td>24.0</td><td>34.1</td>
<td style="background-color:#e6ffb8;">34.1</td>
</tr>
<tr>
<td>LLaMA 2-7B</td>
<td>66.4</td><td>3.3</td><td>10.0</td><td>5.0</td>
<td>46.9</td><td>30.0</td><td>25.4</td><td>27.5</td>
<td>45.3</td><td>34.8</td><td>10.8</td><td>16.5</td>
<td style="background-color:#e6ffb8;">16.3</td>
</tr>
<tr>
<td>LLaMA 3-8B</td>
<td>9.7</td><td>8.9</td><td><span style="color:blue"><strong><u>100.0</u></strong></span></td><td>16.4</td>
<td>60.8</td><td>51.7</td><td>20.0</td><td>28.8</td>
<td>51.3</td><td>63.3</td><td>6.2</td><td>11.3</td>
<td style="background-color:#e6ffb8;">18.8</td>
</tr>
<tr>
<td>Mistral-7B</td>
<td>66.4</td><td>15.0</td><td>60.0</td><td>24.0</td>
<td>63.9</td><td>52.5</td><td>94.2</td><td>67.4</td>
<td>71.6</td><td>69.9</td><td>76.0</td><td>72.8</td>
<td style="background-color:#e6ffb8;">54.7</td>
</tr>
<tr>
<td>Qwen 1.5-7B</td>
<td>27.4</td><td>10.9</td><td><span style="color:blue"><strong><u>100.0</u></strong></span></td><td>19.6</td>
<td>53.4</td><td>45.9</td><td>98.1</td><td>62.6</td>
<td>55.7</td><td>53.2</td><td>95.9</td><td>68.4</td>
<td style="background-color:#e6ffb8;">50.2</td>
</tr>
<tr>
<td>Qwen 2-7B</td>
<td>40.2</td><td>16.8</td><td>89.7</td><td>20.8</td>
<td>54.7</td><td>50.3</td><td>95.8</td><td>65.7</td>
<td>57.9</td><td>55.6</td><td>93.2</td><td>69.8</td>
<td style="background-color:#e6ffb8;">52.1</td>
</tr>
<tr>
<td>ChatGPT</td>
<td>67.5</td><td>20.0</td><td>84.9</td><td>30.5</td>
<td>68.9</td><td>60.9</td><td>92.6</td><td>71.2</td>
<td>76.8</td><td>72.3</td><td>86.2</td><td>75.4</td>
<td style="background-color:#e6ffb8;">59.0</td>
</tr>
<tr>
<td>GPT-4 Turbo</td>
<td>72.6</td><td><span style="color:blue"><strong><u>23.1</u></strong></span></td><td>90.0</td><td><span style="color:blue"><strong><u>36.7</u></strong></span></td>
<td><span style="color:blue"><strong><u>81.1</u></strong></span></td><td><span style="color:blue"><strong><u>68.3</u></strong></span></td><td>97.7</td><td><span style="color:blue"><strong><u>80.4</u></strong></span></td>
<td><span style="color:blue"><strong><u>83.9</u></strong></span></td><td><span style="color:blue"><strong><u>80.7</u></strong></span></td><td>88.9</td><td><span style="color:blue"><strong><u>84.6</u></strong></span></td>
<td style="background-color:#e6ffb8;"><span style="color:blue"><strong><u>67.2</u></strong></span></td>
</tr>
<tr>
<td>Claude-3-haiku</td>
<td>36.3</td><td>12.2</td><td><span style="color:blue"><strong><u>100.0</u></strong></span></td><td>21.7</td>
<td>49.9</td><td>44.2</td><td><span style="color:blue"><strong><u>99.7</u></strong></span></td><td>61.2</td>
<td>66.7</td><td>60.2</td><td><span style="color:blue"><strong><u>98.0</u></strong></span></td><td>74.6</td>
<td style="background-color:#e6ffb8;">52.5</td>
</tr>
</tbody>
</table>

#### 4.7. *Impact of Number of Demonstrations*

In few-shot settings, we investigate the impact of the number of demonstrations for the state-of-the-art LLM, namely whether GPT-4 could perform better or not if more contextual examples are provided. We design five $k$-shot settings: zero-shot, two-shot, four-shot, six-shot, eight-shot. For each setting, we select sample $k = \{0, 2, 4, 6, 8\}$ examples that are similar to the test sample using the kNN sampling algorithm. The results are shown in Fig. 4.

As we can see, the number of demonstrations (k-shot) has a significant impact on the F1 scores for both Mistral and GPT-4 in the sarcasm classification task. For instance, Mistral shows an overall upward trend in F1 scores from 0-shot to 8-shot, increasing from 51.6 to 56.2, representing a total improvement of 8.7% ↑. The most significant performance boost occurs at 2-shot, reaching 55.8, which is an 8.2% increase compared to 0-shot. This shows that Mistral has greater sensitivity to the number of examples provided, benefiting more from additional examples.

In contrast, GPT-4 consistently outperforms Mistral across all shot numbers, with a baseline performance of 64.5 F1 score. GPT-4 achieves its best performance at 2-shot, with an F1 score of 67.5, showing a 4.6% improvement over 0-shot. However, it experiences a slight decline in performance at 6-shot (63.4) and 8-shot (64.3). This indicates that GPT-4 may reach its peak performance with fewer examples and does not benefit as much from additional demonstrations.

These results suggest that both models reach their optimal performance with 2-4 samples, indicating that moderate few-shot learning may be more effective than using a large number of samples for sarcasm detection tasks. Sarcasm detection can vary significantly across textual contexts and datasets, potentially explaining the variations in optimal demonstration numbers.

#### 4.8. *CoT Results*

In few-shot settings, we investigate a widely used prompting approach, CoT. The experimental results are shown in Table 4 and Fig. 5. Despite that CoT prompting has a significant advantage over standard IO



<!-- page 0010 -->

[Figure: Two line charts showing F1 results with different numbers of demonstrations. Top chart titled “Mistral-7B” with x-axis values 0, 2, 4, 6, 8 and legend: IAC-V1, IAC-V2, iSarcasmEval, Riloff, SemEval Task, Ghosh, Average; labeled (a). Bottom chart titled “GPT-4” with x-axis values 0, 2, 4, 6, 8 and legend: IAC-V1, IAC-V2, iSarcasmEval, Riloff, SemEval Task 3, Ghosh, Average; labeled (b).]

Figure 4: The F1 results of Mistral and GPT-4 using different numbers of demonstrations.

prompting across logical, mathematical, and common-sense reasoning tasks, it may be not sufficient in solving sarcasm understanding tasks. For example, GPT-4 sees a decline in its average F1 score from 68.4 with IO prompting to 64.7 with CoT prompting, a 5.5% decrease. Similarly, Mistral, which benefits from IO prompting with an F1 score of 55.8, drops to 47.5 with CoT prompting, reflecting a 14.8% reduction. These examples highlight that while CoT can improve reasoning, it may introduce complexity that hinders models’ ability to effectively detect and interpret sarcasm. Qwen 2 sees a 25.1% reduction, from 53.1 to 39.7. These results indicate that CoT often complicates sarcasm understanding, negatively impacting performance. We present an intuitive comparison in Fig. 6.

The reason is that sarcasm detection is often considered a holistic and non-rational cognitive process that does not conform to step-by-step logical reasoning. Sarcasm expression does not strictly conform to formal logical structures, such as the law of hypothetical syllogism (i.e., if $\mathcal{A} \Rightarrow \mathcal{B}$ and $\mathcal{B} \Rightarrow C$, then $\mathcal{A} \Rightarrow C$). For example, “Poor Alice has fallen for that stupid Bob; and that stupid Bob is head over heels for Claire; but don’t assume for a second that Alice would like Claire”. Another possible reason is that CoT does not explicitly harnesses the quintessential property of sarcasm (namely the contradiction between surface sentiment and true intention). Hence, CoT prompting is less effective for sarcasm classification compared to the more straightforward IO approach. There is an urgent need to develop sarcasm understanding prompting approaches.

#### 4.9. *Error Analysis*

The detailed error analysis is also conducted via the confusion matrices that are shown in Fig. 7, Fig. 8 and Fig. 9. Each cell $(i, j)$ represents the percentage of class $i$ that is classified to be class $j$. Upon reviewing the classification results produced by GPT-4 Turbo on six datasets with three prompting approaches, we discover that imbalanced categories and the sarcastic samples are the key factors contributing to misclassification.

In the zero-shot IO setting, GPT-4 Turbo performs well in identifying non-sarcastic instances, particularly on datasets like IAC-V2 and SemEval Task 3, where the true positive rates for non-sarcastic labels are very high. However, the model struggles more with distinguishing sarcastic instances, especially on datasets like IAC-V1 and iSarcasmEval, where the true positive rates for sarcastic labels are lower (0.46 and 0.38, respectively). This indicates that without any prior examples, the model tends to lean towards non-sarcastic predictions, failing to capture the nuanced language that often accompanies sarcasm.

In the few-shot IO setting, we observe the improvement in performance across the datasets. The model benefits from a few examples, particularly in non-sarcastic classifications. In datasets like IAC-V2, the model still struggles, with only 46% of sarcastic instances correctly identified. The model shows improvement but remains inconsistent in sarcastic classifications, indicating that while few-shot prompting provides some benefit, it may not be sufficient to fully capture sarcasm’s complexity.

In the few-shot CoT setting, GPT-4 Turbo also similar difficulties in distinguishing between sarcastic and non-sarcastic instances, particularly in datasets with more subtle or nuanced sarcastic content.The reason is that CoT is not suitable to solve human sarcasm understanding tasks.

The improvements from few-shot IO and CoT are present but limited, suggesting that sarcasm requires



<!-- page 0011 -->

[Figure: Bar chart comparing Zero-Shot IO, Few-Shot IO, and CoT prompting across Baichuan 2-7B, ChatGLM 2-6B, ChatGLM 3-6B, LLaMA 2-7B, LLaMA 3-8B, Mistral-7B, Qwen 1.5-7B, Qwen 2-7B, ChatGPT, GPT-4, and Claude 3; y-axis ranges from 10 to 80.]

Figure 5: The comparison between zero-shot IO prompting, few-shot IO prompting and CoT prompting.

Table 4: Performance on six datasets. For LLMs, all strategies are based on a **few-shot CoT** setting. <span style="color:blue">Blue</span> indicates the best results across LLMs.

<table>
<thead>
<tr>
<th rowspan="2">Paradigm</th>
<th rowspan="2">Model</th>
<th colspan="4">IAC-V1</th>
<th colspan="4">IAC-V2</th>
<th colspan="4">iSarcasmEval</th>
<th rowspan="2">Avg. of F1</th>
</tr>
<tr>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">PLMs</td>
<td>RoBERTa</td>
<td><strong>70.1</strong></td><td><strong>70.0</strong></td><td><strong>70.1</strong></td><td><strong>69.9</strong></td>
<td>80.7</td><td>80.9</td><td>80.8</td><td>80.7</td>
<td>78.9</td><td>66.4</td><td>57.5</td><td>63.5</td>
<td>71.3</td>
</tr>
<tr>
<td>DC-Net-RoBERTa</td>
<td>69.3</td><td>69.7</td><td>69.3</td><td>69.1</td>
<td><strong>81.7</strong></td><td><strong>81.7</strong></td><td><strong>81.7</strong></td><td><strong>81.7</strong></td>
<td><strong>79.5</strong></td><td><strong>67.1</strong></td><td><strong>58.3</strong></td><td><strong>64.0</strong></td>
<td><strong>71.5</strong></td>
</tr>
<tr>
<td rowspan="11">LLMs<sub>+CoT</sub></td>
<td>Baichuan 2-7B</td>
<td>46.8</td><td>58.0</td><td>37.9</td><td>45.9</td>
<td>52.5</td><td>52.9</td><td>50.7</td><td>51.8</td>
<td>57.9</td><td>9.3</td><td>26.3</td><td>13.7</td>
<td>37.1</td>
</tr>
<tr>
<td>ChatGLM 2-6B</td>
<td>51.3</td><td>61.2</td><td>50.0</td><td>54.8</td>
<td>55.0</td><td>55.0</td><td>56.7</td><td>55.9</td>
<td>57.2</td><td>12.5</td><td>39.5</td><td>19.0</td>
<td>43.2</td>
</tr>
<tr>
<td>ChatGLM 3-6B</td>
<td>60.7</td><td>64.7</td><td>74.6</td><td>69.3</td>
<td>59.5</td><td>56.8</td><td>80.5</td><td>66.6</td>
<td>49.8</td><td>18.5</td><td>86.8</td><td>30.6</td>
<td>55.5</td>
</tr>
<tr>
<td>LLaMA 2-7B</td>
<td>51.1</td><td>59.9</td><td>53.6</td><td>56.6</td>
<td>52.0</td><td>51.8</td><td>62.2</td><td>56.6</td>
<td>49.5</td><td>15.8</td><td>68.4</td><td>25.6</td>
<td>46.3</td>
</tr>
<tr>
<td>LLaMA 3-8B</td>
<td>52.5</td><td>61.7</td><td>53.2</td><td>57.1</td>
<td>52.3</td><td>52.2</td><td>57.8</td><td>54.9</td>
<td>55.5</td><td>13.2</td><td>44.7</td><td>20.4</td>
<td>44.1</td>
</tr>
<tr>
<td>Mistral-7B</td>
<td>59.0</td><td>65.1</td><td>66.9</td><td>66.0</td>
<td>57.1</td><td>55.7</td><td>71.0</td><td>62.4</td>
<td>59.9</td><td>18.5</td><td>63.2</td><td>28.6</td>
<td>52.3</td>
</tr>
<tr>
<td>Qwen 1.5-7B</td>
<td>52.5</td><td>61.6</td><td>53.6</td><td>57.3</td>
<td>55.7</td><td>52.6</td><td>64.3</td><td>59.4</td>
<td>51.8</td><td>16.9</td><td>71.1</td><td>27.3</td>
<td>48.0</td>
</tr>
<tr>
<td>Qwen 2-7B</td>
<td>54.7</td><td>42.5</td><td>51.4</td><td>46.5</td>
<td>52.9</td><td>40.1</td><td>56.4</td><td>40.1</td>
<td>53.7</td><td>20.3</td><td>71.8</td><td>28.5</td>
<td>38.3</td>
</tr>
<tr>
<td>ChatGPT</td>
<td>64.7</td><td>64.4</td><td>81.5</td><td>69.6</td>
<td>61.9</td><td>56.4</td><td>82.8</td><td>67.3</td>
<td>53.6</td><td>15.6</td><td>87.7</td><td>33.6</td>
<td>56.8</td>
</tr>
<tr>
<td>GPT-4-Turbo</td>
<td><span style="color:blue"><u><strong>72.2</strong></u></span></td><td><span style="color:blue"><u><strong>72.4</strong></u></span></td><td>85.9</td><td><span style="color:blue"><u><strong>78.6</strong></u></span></td>
<td><span style="color:blue"><u><strong>69.5</strong></u></span></td><td><span style="color:blue"><u><strong>63.4</strong></u></span></td><td>93.0</td><td><span style="color:blue"><u><strong>75.4</strong></u></span></td>
<td><span style="color:blue"><u><strong>65.9</strong></u></span></td><td><span style="color:blue"><u><strong>25.4</strong></u></span></td><td>86.8</td><td><span style="color:blue"><u><strong>39.3</strong></u></span></td>
<td><span style="color:blue"><u><strong>64.4</strong></u></span></td>
</tr>
<tr>
<td>Claude-3-haiku</td>
<td>63.8</td><td>63.9</td><td><span style="color:blue"><u><strong>89.9</strong></u></span></td><td>74.7</td>
<td>59.8</td><td>55.8</td><td><span style="color:blue"><u><strong>95.8</strong></u></span></td><td>70.6</td>
<td>33.4</td><td>15.2</td><td><span style="color:blue"><u><strong>92.1</strong></u></span></td><td>26.0</td>
<td>57.1</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th rowspan="2">Paradigm</th>
<th rowspan="2">Model</th>
<th colspan="4">Riloff</th>
<th colspan="4">SemEval Task 3</th>
<th colspan="4">Ghosh</th>
<th rowspan="2">Avg. of F1</th>
</tr>
<tr>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
<th>Acc</th><th>P</th><th>R</th><th>F1</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">PLMs</td>
<td>RoBERTa</td>
<td><strong>84.0</strong></td><td>64.0</td><td><strong>75.0</strong></td><td><strong>69.0</strong></td>
<td><strong>75.0</strong></td><td>64.0</td><td><strong>84.0</strong></td><td><strong>72.0</strong></td>
<td>80.3</td><td>80.3</td><td>79.8</td><td>80.0</td>
<td><strong>73.7</strong></td>
</tr>
<tr>
<td>DC-Net-RoBERTa</td>
<td>82.6</td><td><strong>67.4</strong></td><td>70.3</td><td>67.8</td>
<td>70.9</td><td><strong>69.7</strong></td><td>68.3</td><td>68.7</td>
<td><strong>82.2</strong></td><td><strong>81.0</strong></td><td><strong>81.7</strong></td><td><strong>81.3</strong></td>
<td>72.6</td>
</tr>
<tr>
<td rowspan="11">LLMs<sub>+CoT</sub></td>
<td>Baichuan 2-7B</td>
<td>56.6</td><td>6.7</td><td>30.0</td><td>10.9</td>
<td>53.7</td><td>43.6</td><td>56.6</td><td>49.2</td>
<td>50.7</td><td>50.7</td><td>50.1</td><td>50.4</td>
<td>36.7</td>
</tr>
<tr>
<td>ChatGLM 2-6B</td>
<td>52.2</td><td>2.2</td><td>10.0</td><td>3.6</td>
<td>54.3</td><td>43.9</td><td>54.0</td><td>48.4</td>
<td>50.1</td><td>50.1</td><td>50.8</td><td>50.4</td>
<td>34.1</td>
</tr>
<tr>
<td>ChatGLM 3-6B</td>
<td>47.8</td><td>14.5</td><td><span style="color:blue"><u><strong>100.0</strong></u></span></td><td>25.3</td>
<td><span style="color:blue"><u><strong>88.1</strong></u></span></td><td>53.3</td><td>64.7</td><td>66.4</td>
<td><span style="color:blue"><u><strong>83.3</strong></u></span></td><td>60.4</td><td>64.4</td><td>70.1</td>
<td>53.9</td>
</tr>
<tr>
<td>LLaMA 2-7B</td>
<td>51.3</td><td>9.1</td><td>50.0</td><td>15.4</td>
<td>51.8</td><td>42.2</td><td>58.5</td><td>49.1</td>
<td>45.1</td><td>45.2</td><td>46.3</td><td>45.7</td>
<td>36.7</td>
</tr>
<tr>
<td>LLaMA 3-8B</td>
<td>54.0</td><td>9.6</td><td>50.0</td><td>16.1</td>
<td>51.1</td><td>40.9</td><td>51.8</td><td>45.7</td>
<td>49.9</td><td>49.9</td><td>51.4</td><td>50.6</td>
<td>37.5</td>
</tr>
<tr>
<td>Mistral-7B</td>
<td>68.1</td><td>11.8</td><td>40.0</td><td>18.2</td>
<td>61.5</td><td>51.1</td><td>65.9</td><td>57.6</td>
<td>54.7</td><td>55.1</td><td>50.1</td><td>52.5</td>
<td>42.8</td>
</tr>
<tr>
<td>Qwen 1.5-7B</td>
<td>43.4</td><td>9.1</td><td>60.0</td><td>15.8</td>
<td>51.5</td><td>43.1</td><td>54.7</td><td>48.5</td>
<td>55.8</td><td>55.7</td><td>52.4</td><td>53.2</td>
<td>39.2</td>
</tr>
<tr>
<td>Qwen 2-7B</td>
<td>49.9</td><td>10.5</td><td>66.0</td><td>16.6</td>
<td>56.7</td><td>47.4</td><td>60.2</td><td>50.9</td>
<td>61.4</td><td>61.3</td><td>57.6</td><td>55.9</td>
<td>41.1</td>
</tr>
<tr>
<td>ChatGPT</td>
<td>59.6</td><td>19.1</td><td>86.4</td><td>31.4</td>
<td>64.9</td><td>53.4</td><td>84.4</td><td>65.4</td>
<td>69.8</td><td>64.3</td><td>80.9</td><td>71.7</td>
<td>56.1</td>
</tr>
<tr>
<td>GPT-4-Turbo</td>
<td><span style="color:blue"><u><strong>69.0</strong></u></span></td><td><span style="color:blue"><u><strong>22.2</strong></u></span></td><td><span style="color:blue"><u><strong>100.0</strong></u></span></td><td><span style="color:blue"><u><strong>36.4</strong></u></span></td>
<td>75.1</td><td><span style="color:blue"><u><strong>61.8</strong></u></span></td><td>97.7</td><td><span style="color:blue"><u><strong>75.7</strong></u></span></td>
<td>80.8</td><td><span style="color:blue"><u><strong>74.5</strong></u></span></td><td>93.6</td><td><span style="color:blue"><u><strong>83.0</strong></u></span></td>
<td><span style="color:blue"><u><strong>65.0</strong></u></span></td>
</tr>
<tr>
<td>Claude-3-haiku</td>
<td>34.5</td><td>11.9</td><td><span style="color:blue"><u><strong>100.0</strong></u></span></td><td>21.3</td>
<td>54.0</td><td>46.2</td><td><span style="color:blue"><u><strong>99.0</strong></u></span></td><td>63.1</td>
<td>65.3</td><td>59.3</td><td><span style="color:blue"><u><strong>97.2</strong></u></span></td><td>73.7</td>
<td>52.7</td>
</tr>
</tbody>
</table>

more sophisticated handling, potentially incorporating richer contextual understanding and more advanced prompting strategies.

### 4.10. Case Study

Table 5 presents several examples where three representative LLMs made predictions. We conduct a brief analysis of the reasons behind these prediction errors.

**(1) Contextual misunderstanding.** GPT-4 struggled



<!-- page 0012 -->

[Figure: Three radar charts showing all models’ F1 performance across six datasets. Axes include iSarcasmEval, IAC-V2, IAC-V1, Ghosh, SemEval Task 3, and Riloff. Legends include Baichuan 2, ChatGLM 2, ChatGLM 3, Llama 2, Llama 3, Mistral, Qwen 1.5, Qwen 2, ChatGPT, GPT-4, and Claude 3.]

(a) Zero-shot IO setting.

(b) Few-shot IO setting.

(c) CoT setting.

Figure 6: The radar illustration of all models’ F1 performance across six datasets.

with texts where sarcasm was deeply tied to contextual or cultural nuances. For instance, in Example 3 (“Being half Spanish and not being able to speak Spanish is honestly so disappointing”), the sarcasm lies in the speaker’s ironic expression of disappointment. GPT-4 misclassified this as non-sarcastic, possibly due to its difficulty in detecting sarcasm embedded in personal or cultural identity issues. Similarly, in Example 4 (“I literally just ate 1/4 of a pan of brownies ... #damnit #notagain”), the self-deprecating tone and hashtags signal sarcasm, which GPT-4 failed to recognize.

**(2) Literal interpretation.** Claude 3 and LLaMA 3 generally performed better in identifying sarcasm when there was a stark contrast between the literal meaning and the intended message. For example, in Example 1 (“So many useless classes, great to be a student”), both models correctly identified the sarcastic tone. However, Claude 3 failed to detect sarcasm in Example 5 (“i love doing laundry”), where the lack of overt emotional indicators may have led to a more literal interpretation, causing the model to misclassify it as non-sarcastic.

**(3) Bias.** All three models misclassified Example 6 (“I just love not hanging out with my boyfriend”) as sarcastic, despite the straightforward nature of the statement. This suggests that the models might be overfitting to common sarcastic patterns, such as the phrase “I just love...” which is often used sarcastically. This shows that the models rely heavily on pattern recognition rather than contextual understanding. In addition, the ambiguity of the phrase posed a challenge for Claude 3 and LLaMA 3.

This analysis underscores the necessity for LLMs to develop a more profound contextual comprehension and enhanced interpretative skills to minimize prediction inaccuracies in sarcasm detection.

#### 4.11. Evaluating LLMs on Multi-Modal Sarcasm Understanding

Due to the rapid surge of multi-modal data on social networks, leveraging multi-modal information to enhance human language understanding and reasoning has become increasingly attractive and significant. Beyond text-based LLMs, multi-modal LLMs typically incorporate modality encoders, connectors, and generators. Through modality-aligned pre-training, these models acquire the ability to process multi-modal information. Therefore, in this section, we aim to investigate their capabilities for understanding multi-modal sarcasm.

More specifically, we select two popular and publicly accessible multi-modal sarcasm detection datasets, namely, MMSD [46] and CMMA [17], as our experimental platforms. We evaluate four state-of-the-art multi-modal LLMs: Retrieval-LLaVA 1.5 [47], GPT-4V<sup>7</sup>, Wenxin 4<sup>8</sup>, and Qwen-VL-Plus [48]. Given that CoT prompting is less effective in sarcasm understanding, we employ only the zero-shot IO prompting method for GPT-4V, Qwen-VL-Plus and Wenxin 4. Their prompts are: “Based on the image and corresponding text below, analysis both the image and the text, determine whether they are sarcastic or not. If they are sarcastic output ‘sarcastic’, otherwise, output ‘non-sarcastic’. Return the label only without any other

<sup>7</sup>https://openai.com/index/gpt-4v-system-card/  
<sup>8</sup>https://yiyan.baidu.com/



<!-- page 0013 -->

[Figure: Six normalized confusion matrix heatmaps for GPT-4 in the zero-shot IO setting. Subfigures: (a) IAC-V1, (b) IAC-V2, (c) Roliff, (d) iSarcasmEval, (e) SemEval Task 3, (f) Ghosh. Axes labels include “non-sarcastic” and “sarcastic”.]

Figure 7: The normalized confusion matrices for GPT-4 across six datasets in the **zero-shot IO** setting.

[Figure: Six normalized confusion matrix heatmaps for GPT-4 in the few-shot IO setting. Subfigures: (a) IAC-V1, (b) IAC-V2, (c) Roliff, (d) iSarcasmEval, (e) SemEval Task 3, (f) Ghosh. Axes labels include “non-sarcastic” and “sarcastic”.]

Figure 8: The normalized confusion matrices for GPT-4 across six datasets in the **few-shot IO** setting.

*text.”* Retrieval-LLaVA 1.5 proposes a retrieval module for LLaVA 1.5 to search for demonstrations, aiming at further bridging the gap between LLaVA 1.5 and the specific multi-modal sarcasm detection task. Additionally, we present four state-of-the-art multi-modal sarcasm detection baselines for comparison. The results



<!-- page 0014 -->

[Figure: Six 2×2 normalized confusion matrices for GPT-4 with axes labeled “non-sarcastic” and “sarcastic”: (a) IAC-V1 values 88, 81, 35, 213; (b) IAC-V2 values 338, 399, 52, 692; (c) Roliff values 68, 35, 0, 10; (d) iSarcasmEval values 164, 97, 5, 33; (e) SemEval Task 3 values 285, 188, 7, 304; (f) Ghosh values 680, 320, 64, 936.]

Figure 9: The normalized confusion matrices for GPT-4 across six datasets in the **few-shot CoT** setting.

Table 5: Typical examples for case study.

| Example | Text | Golden | GPT-4 | Claude 3 | LLaMA3 |
|---|---|---|---|---|---|
| 1 | So many useless classes, great to be student. | sarcastic | ✓ | ✓ | ✓ |
| 2 | I just love having grungy ass hair #not. | sarcastic | ✓ | ✓ | ✓ |
| 3 | Being half spanish and not being able to speak spanish is honestly so disappointing. | sarcastic | × | ✓ | ✓ |
| 4 | I literally just ate 1/4 of a pan of brownies ... #damnit #notagain. | sarcastic | × | ✓ | ✓ |
| 5 | i love doing laundry. | sarcastic | ✓ | × | ✓ |
| 6 | I just love not hanging out with my boyfriend. | non-sarcastic | × | × | × |
| 7 | 10 tell us how you really feel. | non-sarcastic | ✓ | × | × |

are shown in Table 6.

We can notice: (1) Zero-shot IO prompting-based multi-modal LLMs exhibit weak performance across both datasets when compared to PLMs. This suggests a possible limitation in their generalizability or adaptability to complex multi-modal tasks without additional contextual support. (2) Among the LLMs tested, GPT-4V shows superior results on the MMSD dataset, which is English, compared to Wenxin 4 and Qwen-VL-Plus. In contrast, Qwen-VL-Plus excels on the CMMA dataset, which is Chinese. This divergence likely stems from the inherent differences in how sarcasm is expressed and contextualized in English versus Chinese. This indicates that GPT-4V may be more suitable for processing sarcasm in English while Qwen-VL-Plus may be suited for Chinese sarcasm understanding. (3) The superior performance of Retrieval-LLaVA 1.5, particularly notable when it utilizes a retrieval approach to incorporate relevant examples into its prompts. This model outperforms the four PLMs significantly, demonstrating that adding contextually appropriate examples can substantially enhance model performance. We also present several examples in Fig. 7.

## 5. Conclusion

In the era of large language models (LLMs), there is growing concern that LLMs’ success may not be fully



<!-- page 0015 -->

Table 6: Performance on two multi-modal sarcasm datasets. <span style="color: blue">Blue</span> indicates the best results across LLMs.

<table>
<thead>
<tr>
<th rowspan="2">Paradigm</th>
<th rowspan="2">Model</th>
<th colspan="4">MMSD</th>
<th colspan="4">CMMA</th>
</tr>
<tr>
<th>Acc</th>
<th>P</th>
<th>R</th>
<th>F1</th>
<th>Acc</th>
<th>P</th>
<th>R</th>
<th>F1</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Multi-Modal PLMs</td>
<td>MMMA [17]</td>
<td>86.7</td>
<td>80.2</td>
<td>84.4</td>
<td>82.6</td>
<td>77.5</td>
<td>76.3</td>
<td>74.2</td>
<td>75.2</td>
</tr>
<tr>
<td>ResNet+BERT [49]</td>
<td>84.8</td>
<td>77.8</td>
<td>84.1</td>
<td>80.8</td>
<td>69.4</td>
<td>67.8</td>
<td>65.7</td>
<td>66.8</td>
</tr>
<tr>
<td>MILNet [50]</td>
<td>89.5</td>
<td>85.2</td>
<td>89.2</td>
<td>87.1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Multi-view CLIP [51]</td>
<td>88.3</td>
<td>82.7</td>
<td>88.7</td>
<td>85.6</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td rowspan="4">Multi-Modal LLMs</td>
<td>Retrieval-LLaVA 1.5 [47]</td>
<td><span style="color: blue"><u>90.0</u></span></td>
<td><span style="color: blue"><u>89.3</u></span></td>
<td><span style="color: blue"><u>89.6</u></span></td>
<td><span style="color: blue"><u>89.4</u></span></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Wenxin 4</td>
<td>60.0</td>
<td>52.6</td>
<td>31.5</td>
<td>39.4</td>
<td>50.0</td>
<td><span style="color: blue"><u>40.0</u></span></td>
<td>50.0</td>
<td>44.4</td>
</tr>
<tr>
<td>Qwen-VL-Plus</td>
<td>64.4</td>
<td>52.7</td>
<td>95.0</td>
<td>67.8</td>
<td>39.0</td>
<td>39.4</td>
<td><span style="color: blue"><u>97.5</u></span></td>
<td><span style="color: blue"><u>56.1</u></span></td>
</tr>
<tr>
<td>GPT-4V</td>
<td>71.0</td>
<td>59.4</td>
<td>96.5</td>
<td>73.5</td>
<td><span style="color: blue"><u>52.0</u></span></td>
<td>31.8</td>
<td>17.6</td>
<td>22.6</td>
</tr>
</tbody>
</table>

Table 7: Typical multi-modal examples for case study.

<table>
<thead>
<tr>
<th>Example</th>
<th>Image</th>
<th>Text</th>
<th>Golden</th>
<th>GPT-4V</th>
<th>Qwen-VL</th>
<th>WenXin4</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>[Figure: meme-like image with toast/drink; readable text includes “DRINK YOURSELF TO DEATH”]</td>
<td>happy new year , everyone ! xoxo # year2016<br># partyhard # nihilistmemes</td>
<td>sarcastic</td>
<td>✓</td>
<td>✓</td>
<td>×</td>
</tr>
<tr>
<td>2</td>
<td>[Figure: photo of a mostly empty road/parking area near buildings]</td>
<td>the pa welcome center is hopping today .</td>
<td>sarcastic</td>
<td>✓</td>
<td>✓</td>
<td>×</td>
</tr>
<tr>
<td>3</td>
<td>[Figure: photo of burgers and food in containers]</td>
<td>feeding my abs nothing but the best quality<br>beef</td>
<td>sarcastic</td>
<td>✓</td>
<td>✓</td>
<td>×</td>
</tr>
<tr>
<td>4</td>
<td>[Figure: photo of a screen showing Netflix; readable text includes “NETFLIX” and “THE CROODS”]</td>
<td>because every mildly successful cgi film needs<br>an animated spinoff .</td>
<td>sarcastic</td>
<td>✓</td>
<td>✓</td>
<td>×</td>
</tr>
<tr>
<td>5</td>
<td>[Figure: close-up photo of a woman’s face]</td>
<td>when ryan seacrest air-kisses you , but you<br>went for the real kiss</td>
<td>non-sarcastic</td>
<td>×</td>
<td>×</td>
<td>×</td>
</tr>
<tr>
<td>6</td>
<td>[Figure: photo of a person lying down with a dog]</td>
<td>bae and i ...... all day .</td>
<td>non-sarcastic</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
</tbody>
</table>

tenable when considering sarcasm understanding. To address this question, we select eleven SOTA LLMs and eight SOTA PLMs and present comprehensive evaluations on six widely used benchmark datasets. The re-



<!-- page 0016 -->

sults show that current LLMs underperform supervised PLMs based sarcasm detection baselines across six sarcasm benchmarks. In addition, GPT-4 consistently and significantly outperforms other LLMs across various prompting methods. This suggests that significant efforts are still required to improve LLMs’ understanding of human sarcasm. In the future, we plan to improve the classification performance by integrating the predictions of multiple models using methods such as bagging or boosting.

**Limitations.** Our research also has several limitations. (1) We only employed standard prompting methods and chain-of-thought techniques to guide large language models in detecting human sarcasm, without exploring more refined prompting methods such as tree-based or graphical approaches. These methods will be further investigated in our future work. (2) Our study did not consider the variation in model performance on sarcasm across different contexts. Future work could explore how to enhance the model’s understanding of sarcastic language by refining context processing mechanisms.

## References

[1] Z. Shao, Z. Yu, M. Wang, J. Yu, Prompting large language models with answer heuristics for knowledge-based visual question answering, in: Proceedings of the IEEE/CVF Conference on computer vision and pattern recognition, 2023, pp. 14974–14983.

[2] Y. Zhang, M. Wang, P. Tiwari, Q. Li, B. Wang, J. Qin, DialogueLLM: Context and emotion knowledge-tuned llama models for emotion recognition in conversations, arXiv preprint arXiv:2310.11374 (2023).

[3] Y. Zhang, M. Wang, C. Ren, Q. Li, P. Tiwari, B. Wang, J. Qin, Pushing the limit of llm capacity for text classification, arXiv preprint arXiv:2402.07470 (2024).

[4] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al., Chain-of-thought prompting elicits reasoning in large language models, Advances in neural information processing systems 35 (2022) 24824–24837.

[5] S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, K. Narasimhan, Tree of thoughts: Deliberate problem solving with large language models, Advances in Neural Information Processing Systems 36 (2024).

[6] Y. Ren, Z. Wang, Q. Peng, D. Ji, A knowledge-augmented neural network model for sarcasm detection, Information Processing & Management 60 (6) (2023) 103521.

[7] Y. Zhang, Y. Yu, D. Zhao, Z. Li, B. Wang, Y. Hou, P. Tiwari, J. Qin, Learning multi-task commonness and uniqueness for multi-modal sarcasm detection and sentiment analysis in conversation, IEEE Transactions on Artificial Intelligence (2023).

[8] T. Yue, R. Mao, H. Wang, Z. Hu, E. Cambria, Knowlenet: Knowledge fusion network for multimodal sarcasm detection, Information Fusion 100 (2023) 101921.

[9] Y. Zhang, D. Ma, P. Tiwari, C. Zhang, M. Masud, M. Shorfuzzaman, D. Song, Stance-level sarcasm detection with bert and stance-centered graph attention networks, ACM Transactions on Internet Technology 23 (2) (2023) 1–21.

[10] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al., Gpt-4 technical report, arXiv preprint arXiv:2303.08774 (2023).

[11] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. d. l. Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, et al., Mistral 7b, arXiv preprint arXiv:2310.06825 (2023).

[12] A. Yang, B. Xiao, B. Wang, B. Zhang, C. Bian, C. Yin, C. Lv, D. Pan, D. Wang, D. Yan, et al., Baichuan 2: Open large-scale language models, arXiv preprint arXiv:2309.10305 (2023).

[13] T. GLM, A. Zeng, B. Xu, B. Wang, C. Zhang, D. Yin, D. Rojas, G. Feng, H. Zhao, H. Lai, et al., Chatglm: A family of large language models from glm-130b to glm-4 all tools, arXiv preprint arXiv:2406.12793 (2024).

[14] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al., Llama: Open and efficient foundation language models, arXiv preprint arXiv:2302.13971 (2023).

[15] A. Yang, B. Yang, B. Hui, B. Zheng, B. Yu, C. Zhou, C. Li, C. Li, D. Liu, F. Huang, et al., Qwen2 technical report, arXiv preprint arXiv:2407.10671 (2024).

[16] B. Yao, Y. Zhang, Q. Li, J. Qin, Is sarcasm detection a step-by-step reasoning process in large language models? (2024). arXiv: 2407.12725. URL https://arxiv.org/abs/2407.12725

[17] Y. Zhang, Y. Yu, Q. Guo, B. Wang, D. Zhao, S. Uprety, D. Song, Q. Li, J. Qin, Cmma: Benchmarking multi-affection detection in chinese multi-modal conversations, Advances in Neural Information Processing Systems 36 (2024).

[18] L. Zhou, X. Xu, X. Wang, Bns-net: A dual-channel sarcasm detection method considering behavior-level and sentence-level conflicts, arXiv preprint arXiv:2309.03658 (2023).

[19] D. Jain, A. Kumar, G. Garg, Sarcasm detection in mash-up language using soft-attention based bi-directional lstm and feature-rich cnn, Applied Soft Computing 91 (2020) 106198.

[20] D. Ghosh, A. R. Fabbri, S. Muresan, Sarcasm analysis using conversation context, Computational Linguistics 44 (4) (2018) 755–792.

[21] B. Liang, C. Lou, X. Li, M. Yang, L. Gui, Y. He, W. Pei, R. Xu, Multi-modal sarcasm detection via cross-modal graph convolutional network, in: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Vol. 1, Association for Computational Linguistics, 2022, pp. 1767–1777.

[22] Y. Liu, Y. Wang, A. Sun, X. Meng, J. Li, J. Guo, A dual-channel framework for sarcasm recognition by detecting sentiment conflict, in: M. Carpuat, M.-C. de Marneffe, I. V. Meza Ruiz (Eds.), Findings of the Association for Computational Linguistics: NAACL 2022, Association for Computational Linguistics, Seattle, United States, 2022, pp. 1670–1680. doi:10.18653/v1/2022.findings-naacl.126. URL https://aclanthology.org/2022.findings-naacl.126

[23] Y. Liu, R. Zhang, Y. Fan, J. Guo, X. Cheng, Prompt tuning with contradictory intentions for sarcasm recognition, in: Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics, 2023, pp. 328–339.

[24] Y. Qiao, L. Jing, X. Song, X. Chen, L. Zhu, L. Nie, Mutual-enhanced incongruity learning network for multi-modal sarcasm detection, in: Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 37, 2023, pp. 9507–9515.

[25] Y. Tian, N. Xu, R. Zhang, W. Mao, Dynamic routing transformer network for multimodal sarcasm detection, in: A. Rogers, J. Boyd-Graber, N. Okazaki (Eds.), Proceedings of the 61st



<!-- page 0017 -->

Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Association for Computational Linguistics, Toronto, Canada, 2023, pp. 2468–2480. doi: 10.18653/v1/2023.acl-long.139.  
URL https://aclanthology.org/2023.acl-long.139

[26] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al., Evaluating large language models trained on code, arXiv preprint arXiv:2107.03374 (2021).

[27] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang, J. Zhang, Z. Dong, Y. Du, C. Yang, Y. Chen, Z. Chen, J. Jiang, R. Ren, Y. Li, X. Tang, Z. Liu, P. Liu, J.-Y. Nie, J.-R. Wen, A survey of large language models (2023). arXiv:2303.18223.

[28] X. Ren, P. Zhou, X. Meng, X. Huang, Y. Wang, W. Wang, P. Li, X. Zhang, A. Podolskiy, G. Arshinov, et al., Pangu-{\Sigma}: Towards trillion parameter language model with sparse heterogeneous computing, arXiv preprint arXiv:2303.10845 (2023).

[29] B. Yao, Y. Zhang, Q. Li, J. Qin, Is sarcasm detection a step-by-step reasoning process in large language models?, arXiv preprint arXiv:2407.12725 (2024).

[30] X. Sun, X. Li, J. Li, F. Wu, S. Guo, T. Zhang, G. Wang, Text classification via large language models, arXiv preprint arXiv:2305.08377 (2023).

[31] S. Lukin, M. Walker, Really? well. apparently bootstrapping improves the performance of sarcasm and nastiness classifiers for online dialogue, arXiv preprint arXiv:1708.08572 (2017).

[32] S. Oraby, V. Harrison, L. Reed, E. Hernandez, E. Riloff, M. Walker, Creating and characterizing a diverse corpus of sarcasm in dialogue, arXiv preprint arXiv:1709.05404 (2017).

[33] A. Ghosh, T. Veale, Fracking sarcasm using neural network, in: Proceedings of the 7th workshop on computational approaches to subjectivity, sentiment and social media analysis, 2016, pp. 161–169.

[34] I. A. Farha, S. Oprea, S. Wilson, W. Magdy, Semeval-2022 task 6: isarcasmeval, intended sarcasm detection in english and arabic, in: The 16th International Workshop on Semantic Evaluation 2022, Association for Computational Linguistics, 2022, pp. 802–814.

[35] E. Riloff, A. Qadir, P. Surve, L. De Silva, N. Gilbert, R. Huang, Sarcasm as contrast between a positive sentiment and negative situation, in: Proceedings of the 2013 conference on empirical methods in natural language processing, 2013, pp. 704–714.

[36] C. Van Hee, E. Lefever, V. Hoste, Semeval-2018 task 3: Irony detection in english tweets, in: Proceedings of the 12th international workshop on semantic evaluation, 2018, pp. 39–50.

[37] S. Lukin, M. Walker, Really? well. apparently bootstrapping improves the performance of sarcasm and nastiness classifiers for online dialogue, in: C. Danescu-Niculescu-Mizil, A. Farzindar, M. Gamon, D. Inkpen, M. Nagarajan (Eds.), Proceedings of the Workshop on Language Analysis in Social Media, Association for Computational Linguistics, Atlanta, Georgia, 2013, pp. 30–40.  
URL https://aclanthology.org/W13-1104

[38] Y. Kim, Convolutional neural networks for sentence classification, arXiv preprint arXiv:1408.5882 (2014).

[39] Y. Zhang, Q. Li, D. Song, P. Zhang, P. Wang, Quantum-inspired interactive networks for conversational sentiment analysis, in: Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19, International Joint Conferences on Artificial Intelligence Organization, 2019, pp. 5436–5442. doi:10.24963/ijcai.2019/755.  
URL https://doi.org/10.24963/ijcai.2019/755

[40] Y. Wang, M. Huang, L. Zhao, et al., Attention-based lstm for aspect-level sentiment classification, in: Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing, 2016, pp. 606–615.

[41] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: Pre-training of deep bidirectional transformers for language understanding, in: J. Burstein, C. Doran, T. Solorio (Eds.), Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), Association for Computational Linguistics, Minneapolis, Minnesota, 2019, pp. 4171–4186. doi:10.18653/v1/N19-1423.  
URL https://aclanthology.org/N19-1423

[42] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, V. Stoyanov, Roberta: A robustly optimized bert pretraining approach (2019). arXiv:1907.11692.  
URL https://arxiv.org/abs/1907.11692

[43] P. He, X. Liu, J. Gao, W. Chen, Deberta: Decoding-enhanced bert with disentangled attention, in: International Conference on Learning Representations, 2021.  
URL https://openreview.net/forum?id=XPZIaotutsD

[44] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, Q. V. Le, Xlnet: Generalized autoregressive pretraining for language understanding, Advances in neural information processing systems 32 (2019).

[45] Y. Liu, Y. Wang, A. Sun, X. Meng, J. Li, J. Guo, A dual-channel framework for sarcasm recognition by detecting sentiment conflict, in: M. Carpuat, M.-C. de Marneffe, I. V. Meza Ruiz (Eds.), Findings of the Association for Computational Linguistics: NAACL 2022, Association for Computational Linguistics, Seattle, United States, 2022, pp. 1670–1680. doi:10.18653/v1/2022.findings-naacl.126.  
URL https://aclanthology.org/2022.findings-naacl.126

[46] Y. Cai, H. Cai, X. Wan, Multi-modal sarcasm detection in Twitter with hierarchical fusion model, in: A. Korhonen, D. Traum, L. Màrquez (Eds.), Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, Association for Computational Linguistics, Florence, Italy, 2019, pp. 2506–2515. doi:10.18653/v1/P19-1239.  
URL https://aclanthology.org/P19-1239

[47] B. Tang, B. Lin, H. Yan, S. Li, Leveraging generative large language models with visual instruction and demonstration retrieval for multimodal sarcasm detection, in: Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 2024, pp. 1732–1742.

[48] J. Bai, S. Bai, S. Yang, S. Wang, S. Tan, P. Wang, J. Lin, C. Zhou, J. Zhou, Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond (2023). arXiv:2308.12966.  
URL https://arxiv.org/abs/2308.12966

[49] H. Pan, Z. Lin, P. Fu, Y. Qi, W. Wang, Modeling intra and inter-modality incongruity for multi-modal sarcasm detection, in: T. Cohn, Y. He, Y. Liu (Eds.), Findings of the Association for Computational Linguistics: EMNLP 2020, Association for Computational Linguistics, Online, 2020, pp. 1383–1392. doi:10.18653/v1/2020.findings-emnlp.124.  
URL https://aclanthology.org/2020.findings-emnlp.124

[50] Y. Qiao, L. Jing, X. Song, X. Chen, L. Zhu, L. Nie, Mutual-enhanced incongruity learning network for multi-modal sarcasm detection, Proceedings of the AAAI Conference on Artificial Intelligence 37 (8) (2023) 9507–9515. doi:10.1609/aaai.v37i8.26138.  
URL https://ojs.aaai.org/index.php/AAAI/article/view/26138



<!-- page 0018 -->

[51] L. Qin, S. Huang, Q. Chen, C. Cai, Y. Zhang, B. Liang, W. Che, R. Xu, MMSD2.0: Towards a reliable multi-modal sarcasm detection system, in: A. Rogers, J. Boyd-Graber, N. Okazaki (Eds.), Findings of the Association for Computational Linguistics: ACL 2023, Association for Computational Linguistics, Toronto, Canada, 2023, pp. 10834–10845. doi:10.18653/v1/2023.findings-acl.689. URL https://aclanthology.org/2023.findings-acl.689
