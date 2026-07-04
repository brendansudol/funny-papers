<!-- Transcribed from 53-psychology-driven-translation.pdf -->



<!-- page 0001 -->

# Psychology-Driven Enhancement of Humour Translation

Yuchen Su<sup>1[0009–0007–5287–4163]</sup>, Yonghua Zhu<sup>2[0000–0003–3339–8855]</sup>, Yang Chen<sup>1[0000–0002–1148–3920]</sup>, Diana Benavides Prado<sup>3[0000–0003–1137–2822]</sup>, and Michael Witbrock<sup>1[0000–0002–7554–0971]</sup>

<sup>1</sup> School of Computer Science, University of Auckland, New Zealand  
<sup>2</sup> Singapore University of Technology and Design  
<sup>3</sup> School of Electronic Engineering and Computer Science, Queen Mary University of London  
{ysu132}@aucklanduni.ac.nz

**Abstract.** Humour translation plays a vital role as a bridge between different cultures, fostering understanding and communication. Although most existing Large Language Models (LLMs) are capable of general translation tasks, these models still struggle with humour translation, which is especially reflected through linguistic interference and lacking humour in translated text. In this paper, we propose a psychology-inspired Humour Decomposition Mechanism (HDM) that utilises Chain-of-Thought (CoT) to imitate the ability of the human thought process, stimulating LLMs to optimise the readability of translated humorous texts. Moreover, we integrate humour theory in HDM to further enhance the humorous elements in the translated text. Our automatic evaluation experiments on open-source humour datasets demonstrate that our method significantly improves the quality of humour translation, yielding average gains of 7.75% in humour, 2.81% in fluency, and 6.13% in coherence of the generated text.

**Keywords:** Large Language Model · Humour Translation · Chain-of-Thought · Psycholinguistics.

## 1 Introduction

Humour plays an important role in human interaction. Humour studies can actually gain greater insight into the linguistic, social and psychological factors of humour [41]. A comprehensive understanding of humour necessitates a deep grasp of both semantic information and cultural background [8]. Effective humour translation serves as a bridge across cultural divides, facilitating communication and fostering cross-cultural understanding [33]. Some studies [26] mention that the humour translation research can enhance the understanding of language transfer and the process of meaning reconstruction, while enriching the translation theories, especially for dynamic equivalence and functionalist translation strategies. Moreover, an effective humour translation strategy can



<!-- page 0002 -->

[Figure: An illustration comparing humour translation approaches. Visible text includes: “Traditional Translation: 田野里，一头绿色的牛叫什么？透明牛。”; “Please translate the following jokes in Chinese: What do you call a green cow in a field? Invisibull.”; “Back Translation: What color cows are not seen in a field? Green.”; “HDM: 什么颜色的牛在牧场上看不见？绿色的。”]

Fig. 1: An example of humour translation from English to Chinese.

accurately convey its intended humorous effect in the target language [41] and contribute to advancements in general translation research.

There are two fundamental approaches to general translation [25]: formal equivalence, which prioritizes literal translation, and dynamic equivalence, which focuses on emotional or contextual translation. However, the majority of existing studies focus on literal translation, with limited research exploring emotional translation, particularly in the context of humour. Chen et al. [6] use cross-language transfer to enable zero-shot neural machine translation and Wang et al. [35] explore a more efficient KNN-MT for translation. With the advent of large language models (LLMs) such as ChatGPT[^4] and GPT-4 [1], translation has become a prominent domain where LLMs demonstrate remarkable capacity and competence [42, 15]. However, these models still lack proficiency in humour translation in some cases. In Fig 1, for example, the punchline “Invisibull” is awkwardly rendered in the Chinese translation, resulting in a stiff and unnatural expression. By altering the linguistic structure and logical order, while preserving the intended meaning, the translation becomes more fluent and natural, as shown on the right side.

Due to linguistic and cultural barriers, humour translation often results in the loss of humour in the translated content [38]. The reason is that jokes often rely on extensive knowledge and common sense, and the punchline is usually hidden in the semantics of the sentence, such as cultural context, wordplay, and metaphorical expressions. These elements are challenging to identify and translate accurately [14], which weakens the humour of the joke in the target language. Additionally, the issue of linguistic interference is a factor in humour translation [17], which is a non-standard version of the target language in the product of translation. Ma and Cheung [24] indicate that linguistic interference is linked to reduced lexical variety and less cohesive discourse, while the traditional method of translation usually involves merely a linear arrangement of words or phrases [10], which can result in a lack of fluency and coherence in the translated

[^4]: https://chat.openai.com/chat



<!-- page 0003 -->

text. This requires a process that can provide a human thinking process to reconstruct the translated text.

Therefore, to address the challenge of humour translation across different languages, we propose a novel Humour Decomposition Mechanism (HDM) to improve linguistic interference, which introduces a three-step paradigm through the Chain-of-Thoughts (CoT) prompting method [37, 43] by utilising LLMs: (1) mining intrinsic knowledge related to the joke; (2) translating the intrinsic knowledge text; and (3) constructing a new joke based on the translated content. This method mimics a human thinking process for understanding, translating and generating, which allows reconstructing the translated text. Furthermore, to enhance humour in translated texts, we integrate humour theory into intrinsic knowledge by defining corresponding topics, angles, and punchlines. This approach enables the model to perform humour translations effectively based on the mined knowledge.

We use the *Estimation Metric Based Assessment* (GEMBA) [22], a type of LLM evaluation, to assess humour, fluency and coherence. Experimental results reveal that our method is demonstrably superior to existing solutions, showing an average improvement of 7.75% in humour, 2.81% in fluency, and 6.13% in coherence from English to Chinese. These findings indicate that the approach effectively mitigates humour loss and linguistic interference. The main contributions of this paper are summarized as follows:

– We propose an efficient Humour Decomposition Mechanism to guide LLMs to translate jokes, mimicking the human thought process.  
– This work is the first attempt to incorporate the Psychological theory of constructing humour into the Chain-of-Thought process to improve the humour factors.  
– The extensive experimental results demonstrate that our approach surpasses existing frameworks with respect to humour, fluency, and coherence, alleviating the problems of humour loss and linguistic interference.

## 2 Related Work

### 2.1 Humour Theory

The incongruity theory [27] believes that the key to humour is the incongruity between readers’ expectations and the ending of one story [4]. Toplyn [32] further proposes the monologue joke generation theory, which defines the structure of a joke as the topic, angle and punchline. There are currently some studies that incorporate humour theory into natural language processing for humour generation [7] and humour recognition [3, 21]. According to this theory, we will explore how to translate the jokes across different languages.

### 2.2 Translation for LLMs

Extensive research has been conducted to evaluate the translation capabilities of LLMs. Some people study issues specific to LLMs, including the selection



<!-- page 0004 -->

of prompt templates [19, 42] and In-Context Learning [34]. Other researchers investigate translation across diverse scenarios, such as low-resource translation [19], document-level [16, 20] and Multilingual machine translation [48].

[Figure: Workflow diagram titled “Humour Decomposition Mechanism with Humour Theory.” Handwritten labels include “Humour Composition,” “Translation module,” and “Humour Decomposition,” with arrows labeled “Appending to the next context.” The diagram shows a conversation-style pipeline:  
User prompt: “A joke can be thought of as being composed based on three components. Under a particular theory of joke information, those components are: 1. The topic...2. The angle ... 3. The punchline ... Please analyze the following joke in...topic ... angle ... punchline: What do you call a green cow in a field? Invisibull.”  
Model response: “Topic: A cow in a field. Angle: The cow is green... Punchline: ‘Invisibull’ is a play on the words ‘invisible’ and ‘bull’, suggesting that...”  
User prompt: “Please translate the analysis from [English] in [Chinese]. Topic: A cow in a field. Angle: The cow is green... Punchline: ‘Invisibull’ is a play on the words ‘invisible’ and ‘bull’, suggesting that...”  
Model response in Chinese: “主题：牧场上的一头牛; 角度：这头牛是绿色的...; 笑点：“Invisibull” 是 “invisible”（看不见）和 “bull”（公牛）这两个词的双关语...”  
User prompt: “Please generate a [Chinese] joke based on the analysis (only output the joke): 主题：牧场上的一头牛; 角度：这头牛是绿色的...; 笑点：“Invisibull” 是 “invisible”（看不见）和 “bull”（公牛）这两个词的双关语...”  
Model response: “Output: 什么颜色的牛在牧场上看不见？绿色的。 (Back Translation: What color cows are not seen in a field? Green.)”]

Fig. 2: The workflow of HDM.

### 2.3 Chain-of-Thought (CoT)

CoT prompting involves either providing instruction or a few chain-of-thought examples [18]. Recently, a series of studies [40, 46] have proposed their respective prompting strategies, breaking down the entire task into smaller components and then systematically addressing, strategizing, and carrying out each of these components. With the improvement of model capabilities, some works [47, 11] treat the instruction as the “program” for searching, optimization, generating programs and bootstrapping the ability to perform successively more complex reasoning.

## 3 Methodology

Fig 2 illustrates an overview of the proposed Humour Decomposition Mechanism. Instead of directly asking LLMs for the final translation result, we hypothesise that the LLMs can analyze the latent humour interpretations and intrinsic knowledge before translating the jokes, and then generate the translated jokes based on this. We present two key contributions in this section.



<!-- page 0005 -->

## 3.1 Humour Decomposition Mechanism

We design three-step paradigm using Chain-of-Thought (CoT) prompting, which mimics the human thought process in solving complex reasoning tasks [37, 36], to enhance humour translation outcomes.

**Humour Decomposition** Humour decomposition is one of the important cores for HDM. Specifically, our approach initiates the LLM with a specific task of joke analysis. The request is formulated as follows:

> You are a humour assistant. Please analyze the following joke: [Given joke $\mathcal{L}_i$]

Given a joke $\mathcal{L}_i$, we first claim the role of LLM in humour. Furthermore, we introduce an analysis process to generate the sequence of corresponding knowledge $a$, which is organized into the final analysis $\mathcal{A}$. The formulation of our *Humour Decomposition* method can be expressed as follows:

$$
\mathcal{A}_i = \arg \max p(a \mid \mathcal{L}_i)
\tag{1}
$$

where $\mathcal{L}_i$ and $\mathcal{A}_i$ denote the $i_{th}$ joke and its final analysis.

**Translation Module** After achieving *Humour Decomposition*, we use the *Translation Module* to convert the source language analysis into the target language analysis. To illustrate, given the analysis $\mathcal{A}_i$ and the type of source language $S$, we prompt the LLMs to translate $\mathcal{A}_i$ into target language $T$, with the prompt defined as:

> Please translate the analysis from [source language $S$] into [target language $T$]: [text $\mathcal{A}_i$]

Formally, the translation is determined as:

$$
\mathcal{A}'_i = \arg \max p(a' \mid \mathcal{A}_i, S, T,)
\tag{2}
$$

where $\mathcal{A}'_i$ represents the final translation of the analysis, generated from all potential translation results $a'$.

**Humour Composition** Once the translation is generated, we further propose *Humour Composition* to facilitate the generation of jokes. Given the translation version of the analysis, we design the prompt to make LLMs generate the joke of the target language. This is the structure of the prompt:



<!-- page 0006 -->

> Please generate a [target language $\mathcal{T}$] joke based on the analysis: [text $\mathcal{A}_i$]

Formally, the humour composition can be defined as:

$$
\mathcal{F} = \arg\max p(f \mid \mathcal{A}'_i, \mathcal{T})
\tag{3}
$$

where $\mathcal{F}$ is the final generation of the target language joke, generated from all potential generation results $f$.

## 3.2 Integrating Humour Theory

In this section, we incorporate humour theory inspired by [32] to enhance humour factors. The basic structure of the humorous text consists of the topic $\mathcal{X}$, angle $\mathcal{Y}$ and punchline $\mathcal{Z}$. The topic $\mathcal{X}$ is the news item that the joke is based on and the angle $\mathcal{Y}$ is the particular direction that the joke takes, while the punchline $\mathcal{Z}$ which is the surprise at the end of the joke. Therefore, the *Humour Decomposition* module in HDM can be further improved as follows:

> You are a humour assistant. A joke can be thought of as being composed based on three components. Under a particular theory of joke information, those components are:  
> 1. The topic, which is the news item that the joke is based on.  
> 2. The angle, which is the particular direction that the joke takes.  
> 3. The punchline, which is the surprise at the end of the joke.

Similarly, with *Humour Decomposition*, we first claim the LLM’s role in humour. Then, we describe the components under the particular theory and give these components some details. Finally, we provide an instruction to format the model’s outputs, which are defined as:

> Please analyze the following joke and provide the best explanation of what the topic is, what the angle is, and what the punchline is: [Given joke $\mathcal{L}_i$]

Formally, The improved formulation of the Humour Decomposition can be expressed as follows:

$$
\mathcal{A}_i = \arg\max p(\mathcal{X}_i, \mathcal{Y}_i, \mathcal{Z}_i \mid \mathcal{L}_i)
\tag{4}
$$

where $\mathcal{A}_i$ denotes the analysis of the $i_{th}$ joke, including the con-cat of topic $\mathcal{X}_i$, angle $\mathcal{Y}_i$ and punchline $\mathcal{Z}_i$.

HDM leverages the advanced generative capabilities of LLMs [13] to reconstruct humour translation, overcoming the limitations of traditional translation methods, which are often constrained by linear word or phrase arrangements



<!-- page 0007 -->

and linguistic interference, to improve the fluency and coherence of jokes. Additionally, the integration of humour theory defines the general structure of joke composition within the prompts, enabling the large language model to better comprehend background and punchline information. It theoretically enhances the LLM’s ability to generate more humorous jokes, and we will also be demonstrated in our experiments.

## 4 Experiments

### 4.1 Experimental Setup

We select four representative state-of-the-art LLMs from the Chatbot Arena Leaderboard [45] as backbone references for our study: Gemini1.5-Pro [31], Yi-Large [2], GPT3.5-Turbo and GPT4-Turbo. We set the default hyperparameters of these models in their playgrounds. Additionally, we use DUAL-REFLECT [5] and MAPS [15], which are the state-of-the-art translation approaches, as our baselines. Given budget constraints, we randomly select 500 samples on the Short Jokes Dataset [^5] for experiments. Finally, we evaluate their performance by using automatic metrics.

### 4.2 Metrics

Since our approach specializes in humorous translation tasks, traditional automatic evaluation methods, such as COMET [28] and BLEURT [30], have difficulty evaluating elements like humour. Therefore, inspired by [22], we evaluate the final results by using GEMBA which is a GPT4-based metric for generation quality. We choose the open area no-reference metrics GEMBA-SQM and GEMBA-STARS for their superior performance in [22]. Specifically, GEMBA-SQM evaluates scalar quality metrics by dividing the assessment results into several stages, where 0 and 100 represent the lowest and highest scores, respectively. GEMBA-STARS is a classification task based on a one-to-five star ranking, which is a style often used when users are asked to review various services or products [22]. In this section, SQM-H, SQM-F and SQM-C represent GEMBA-SQM metrics and STAR-H, STAR-F and STAR-C represent GEMBA-STARS metrics in humour, fluency and coherence.

To adapt to the evaluation of humour translation in linguistic interference and humour factor, we modify the original translation prompts and use the keywords of humour, coherence and fluency based on [8]. We report the performance by averaging the results over three runs in each type of experiment. Additionally, some answers are observed occasionally fall outside these ranges because of the LLM’s hallucination [22]. For example, instead of providing predicted scores, the model occasionally outputs explanations as results. Therefore, we omit the invalid responses and retain only the valid results in this research.

[^5]: https://www.kaggle.com/datasets/thedevastator/short-jokes-dataset



<!-- page 0008 -->

| Method | SQM-H | STAR-H | SQM-F | STAR-F | SQM-C | STAR-C |
|---|---:|---:|---:|---:|---:|---:|
| Gemini1.5-Pro | 49.82 | 2.53 | 96.74 | 4.81 | 89.30 | 4.50 |
| + DUAL [5] | 50.86 | 2.69 | 92.98 | 4.46 | 84.74 | 4.18 |
| + MAPS [15] | 57.98 | 3.01 | 96.35 | 4.74 | 89.95 | 4.48 |
| + HDM | **63.80** | **3.19** | **98.54** | **4.93** | **94.27** | **4.74** |
| Yi-Large | 53.40 | 2.57 | 95.37 | 4.76 | 86.58 | 4.42 |
| + DUAL [5] | 56.34 | 2.85 | 94.30 | 4.63 | 87.01 | 4.34 |
| + MAPS [15] | 58.08 | 2.94 | 95.24 | 4.67 | 87.09 | 4.36 |
| + HDM | **67.99** | **3.22** | **98.99** | **4.95** | **95.56** | **4.85** |
| GPT3.5-Turbo | 50.03 | 2.52 | 94.33 | 4.72 | 86.83 | 4.41 |
| + DUAL [5] | 54.63 | 2.77 | 92.02 | 4.48 | 83.42 | 4.16 |
| + MAPS [15] | 57.66 | 2.87 | 94.58 | 4.59 | 85.90 | 4.31 |
| + HDM | **61.73** | **3.05** | **96.07** | **4.80** | **88.75** | **4.49** |
| GPT4-Turbo | 53.20 | 2.58 | 94.95 | 4.76 | 87.70 | 4.67 |
| + DUAL [5] | 58.33 | 2.95 | 91.60 | 4.43 | 83.30 | 4.13 |
| + MAPS [15] | 59.34 | 3.02 | 95.12 | 4.68 | 88.62 | 4.45 |
| + HDM | **70.54** | **3.45** | **99.45** | **4.99** | **97.73** | **4.96** |

Table 1: Main results of the automatic metrics GEMBA-SQM and GEMBA-STARS in humour, fluency and coherence for translating from English to Chinese on the Short Joke Dataset. Both higher evaluation metrics indicate better performance.

### 4.3 Main Results

As shown in Table 1, HDM outperforms all baselines in terms of humour, fluency, and coherence in automatic metrics. This is particularly evident in the translation from English to Chinese in GPT4-Turbo, where the degree of humour improves by an average of 11.2%. These results show that HDM can go beyond the other state-of-the-art translation methods, both enhancing the humour of translated text in humour translation and alleviating the problem of linguistic interference.

## 5 Analysis

### 5.1 Generality Analysis of HDM.

To further investigate the generality of our work, we verify the generality of HDM from three perspectives[^6]. MAPS [15] is selected as the baseline for the generality analysis based on the comprehensive metrics evaluated in the experiment:

[^6]: Given budget constraints, we have randomly selected 100 samples in each dataset and language.



<!-- page 0009 -->

<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="2">SQM-H</th>
      <th colspan="2">SQM-F</th>
      <th colspan="2">SQM-C</th>
    </tr>
    <tr>
      <th>base</th>
      <th>ours</th>
      <th>base</th>
      <th>ours</th>
      <th>base</th>
      <th>ours</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7" align="center">Question-Answer Joke</td>
    </tr>
    <tr>
      <td>Gemini1.5-Pro</td>
      <td>60.00</td>
      <td><strong>64.02</strong></td>
      <td>97.67</td>
      <td><strong>99.53</strong></td>
      <td>85.29</td>
      <td><strong>90.63</strong></td>
    </tr>
    <tr>
      <td>Yi-Large</td>
      <td>61.10</td>
      <td><strong>67.30</strong></td>
      <td>96.00</td>
      <td><strong>99.00</strong></td>
      <td>82.30</td>
      <td><strong>93.00</strong></td>
    </tr>
    <tr>
      <td>GPT3.5-Turbo</td>
      <td>62.30</td>
      <td><strong>64.14</strong></td>
      <td>95.45</td>
      <td><strong>97.37</strong></td>
      <td>82.12</td>
      <td><strong>87.68</strong></td>
    </tr>
    <tr>
      <td>GPT4-Turbo</td>
      <td>64.70</td>
      <td><strong>68.70</strong></td>
      <td>96.40</td>
      <td><strong>99.10</strong></td>
      <td>87.37</td>
      <td><strong>95.05</strong></td>
    </tr>
    <tr>
      <td colspan="7" align="center">SemEval-2021</td>
    </tr>
    <tr>
      <td>Gemini1.5-Pro</td>
      <td>61.20</td>
      <td><strong>64.60</strong></td>
      <td>97.90</td>
      <td><strong>99.00</strong></td>
      <td>90.95</td>
      <td><strong>93.10</strong></td>
    </tr>
    <tr>
      <td>Yi-Large</td>
      <td>57.90</td>
      <td><strong>67.50</strong></td>
      <td>96.50</td>
      <td><strong>99.20</strong></td>
      <td>92.85</td>
      <td><strong>95.35</strong></td>
    </tr>
    <tr>
      <td>GPT3.5-Turbo</td>
      <td>56.30</td>
      <td><strong>66.06</strong></td>
      <td>96.80</td>
      <td><strong>98.50</strong></td>
      <td>88.05</td>
      <td><strong>93.35</strong></td>
    </tr>
    <tr>
      <td>GPT4-Turbo</td>
      <td>59.90</td>
      <td><strong>70.10</strong></td>
      <td>96.70</td>
      <td><strong>99.10</strong></td>
      <td>91.70</td>
      <td><strong>97.20</strong></td>
    </tr>
  </tbody>
</table>

Table 2: Generality analysis of automatic metric in translating from English to Chinese in different Datasets.

<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="2">SQM-H</th>
      <th colspan="2">SQM-F</th>
      <th colspan="2">SQM-C</th>
    </tr>
    <tr>
      <th>base</th>
      <th>ours</th>
      <th>base</th>
      <th>ours</th>
      <th>base</th>
      <th>ours</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7" align="center">EN→SP</td>
    </tr>
    <tr>
      <td>Gemini1.5-Pro</td>
      <td>59.50</td>
      <td><strong>64.70</strong></td>
      <td>94.00</td>
      <td><strong>97.90</strong></td>
      <td>87.20</td>
      <td><strong>91.60</strong></td>
    </tr>
    <tr>
      <td>Yi-Large</td>
      <td>58.25</td>
      <td><strong>68.35</strong></td>
      <td><strong>96.50</strong></td>
      <td>96.30</td>
      <td>89.55</td>
      <td><strong>91.15</strong></td>
    </tr>
    <tr>
      <td>GPT3.5-Turbo</td>
      <td>57.90</td>
      <td><strong>68.20</strong></td>
      <td>95.70</td>
      <td><strong>97.00</strong></td>
      <td>88.90</td>
      <td><strong>89.48</strong></td>
    </tr>
    <tr>
      <td>GPT4-Turbo</td>
      <td>61.40</td>
      <td><strong>69.80</strong></td>
      <td>95.53</td>
      <td><strong>98.88</strong></td>
      <td>89.50</td>
      <td><strong>95.50</strong></td>
    </tr>
    <tr>
      <td colspan="7" align="center">EN→GE</td>
    </tr>
    <tr>
      <td>Gemini1.5-Pro</td>
      <td>62.80</td>
      <td><strong>65.20</strong></td>
      <td>95.10</td>
      <td><strong>95.90</strong></td>
      <td>89.00</td>
      <td><strong>89.80</strong></td>
    </tr>
    <tr>
      <td>Yi-Large</td>
      <td>61.80</td>
      <td><strong>64.55</strong></td>
      <td>94.25</td>
      <td><strong>97.50</strong></td>
      <td>87.40</td>
      <td><strong>90.40</strong></td>
    </tr>
    <tr>
      <td>GPT3.5-Turbo</td>
      <td>61.80</td>
      <td><strong>65.30</strong></td>
      <td>92.90</td>
      <td><strong>97.30</strong></td>
      <td>85.35</td>
      <td><strong>87.50</strong></td>
    </tr>
    <tr>
      <td>GPT4-Turbo</td>
      <td>61.30</td>
      <td><strong>68.50</strong></td>
      <td>95.90</td>
      <td><strong>98.00</strong></td>
      <td>88.70</td>
      <td><strong>89.85</strong></td>
    </tr>
  </tbody>
</table>

Table 3: Generality analysis of automatic metric in different languages. *SP* represents Spanish and *GE* represents German.

**Does HDM work well on other datasets?** We conduct experiments on other datasets, namely the Question-Answer Jokes dataset [29] and SemEval 2021 [12]. Table 2 shows that HDM can obtain better performance across all LLMs and metrics in different datasets, achieving improvements of at least 1.84% in humour, 1.7% in fluency and 2.15% in coherence.

**Does HDM work well on other language?** To better assess the model’s generalization capabilities, we conduct the experiments in different languages, including Spanish and German. As shown in Table 3, the experimental results demonstrate that HDM consistently performs significantly well across these languages, for instance, with improvements of 2.75% in humour, 3.25% in fluency, and 3% in coherence in Yi-Large when translating from English to German. Those further demonstrate the effectiveness and broad applicability of HDM.



<!-- page 0010 -->

| Model | SQM-H base | SQM-H ours | SQM-F base | SQM-F ours | SQM-C base | SQM-C ours |
|---|---:|---:|---:|---:|---:|---:|
| Marco-o1-7B | 50.45 | **54.40** | 91.60 | **93.75** | **84.80** | 84.00 |
| Llama3.1-8B-Instruct | 49.25 | **57.20** | **93.00** | 92.60 | **84.20** | 81.70 |
| Qwen2.5-0.5B-Instruct | **39.80** | 28.70 | 86.40 | **89.10** | 74.30 | **80.50** |
| Qwen2.5-7B-Instruct | 51.40 | **60.50** | 92.50 | **94.10** | 85.60 | **85.95** |
| Qwen2.5-14B-Instruct | 51.60 | **61.80** | 91.40 | **97.40** | 86.00 | **91.35** |

Table 4: Generality analysis of automatic metric in translating from English to Chinese in different open-source models.

**Does HDM work well on open-source models?** We also evaluate the performance of our methods using open-source models. Table 4 presents the results for humour, fluency, and coherence on the Short Joke dataset, using mainstream open-source models: Qwen2.5-(0.5B, 7B, 14B) [39], Llama3.1-8B-Instruct [^7] and Marco-o1-7B [44]. We observe a significant decline in the evaluation scores for LLMs with smaller parameter sizes, especially for SQM-H. This may be attributed to their limited capacity to capture the intrinsic humorous semantics of the source text during the humour decomposition and humour composition, thereby impairing the humour quality of the final output.

## 5.2 Prompt Selection

We also validate the robustness of the zero-shot Humour Decomposition Mechanism against the different humour translation prompting.

Figure 3 illustrates the performance of four different prompts in HDM by using GPT4-Turbo. The experimental findings reveal that despite fluctuations in GEMBA-SQM evaluation of reasoning across different prompts, all humour translation prompts consistently enhance performance compared to the traditional CoT approach. This further demonstrates the generalizability and effectiveness of the method, rather than its reliance on specific prompts.

## 5.3 Ablation Study

This analysis aims to investigate the effects of the results on Humour Theory and the Humour Decomposition Mechanism. We randomly select 100 samples to conduct the ablation study, as shown in Table 5, where:

– “-HT” denotes removing the part of humour theory. Our approach will only use the analyzes for the intermediary stage.  
– “-HDM” denotes removing the Humour Decomposition Mechanism. We directly input the prompt of decomposing humour to conduct the translation.  
– “base” denotes both removing the Humour Decomposition Mechanism and humour theory.

[^7]: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct



<!-- page 0011 -->

[Figure: Three bar charts titled “Humour”, “Fluency”, and “Coherency” comparing V1, V2, V3 and V4. Humour values: V1 71.4, V2 68.5, V3 71.9, V4 68.15. Fluency values: V1 99.15, V2 98.2, V3 98.5, V4 97.7. Coherency values: V1 93.69, V2 93.8, V3 94.5, V4 91.1.]

Fig. 3: Performance comparisons of four various prompts of HDM in humour, fluency and coherency, marked by V1, V2, V3 and V4. The y-axis is the score on the GEMBA-SQM.

[Figure: Three example panels labeled P1, P2, and P3.

P1: Joke: What did the snail say while riding on the turtle’s back? Wheeeeeee! Translation: 乌龟在蜗牛背上说了什么？哇--! (What did the turtle say on the snail’s back? Whoosh!) HDM: 一只蜗牛骑在蜗牛背上，喊道：“哇！好刺激！” (A snail rode on the back of a snail and shouted, “Wow! This is exciting!”)

P2: Joke: When whales get insomnia, I wonder if they listen to a relaxing sounds of people CD. Translation: 当鲸鱼失眠时，我想知道它们是否会听一张放松的人类声音CD。(When whales suffer from insomnia, I wonder if they listen to a relaxing CD of human sounds.) HDM: 一只鲸鱼失眠了，另一只鲸鱼建议它：“试试听人类的放松CD吧，他们总是听我们的歌声睡觉。” (“One whale was having trouble sleeping, and another whale suggested: ‘Try listening to a human relaxation CD. They always fall asleep to our songs.’”)

P3: Joke: It takes patience to be single and patience to be married. Translation: 单身需要耐心，婚姻也需要耐心。(Being single requires patience, and so does marriage.) HDM: 单身的人说：我每天都很有耐心地等待另一半出现。已婚的人说：我每天都很有耐心地等待另一半消失。(Single people say: I wait patiently for my other half to appear every day. Married people say: I wait patiently for my other half to disappear every day.)]

Fig. 4: Some correct Chinese cases generated by HDM. We present the original jokes, traditional translations and their back translation and the results of HDM and their back translation.

From Table 5 we observe that HDM demonstrates significant performance gains across all LLMs and evaluation metrics and plays a critical component of our approach, especially in humour. We attribute these improvements to CoT prompts, which help LLMs refine translated text by enhancing their parsing and reconstruction abilities.

Humour Theory (HT) further delivers some improvements after HDM. For example, Gemini1.5-Pro achieve gains of +3.3%, +1.00%, and +3.10% in humour, fluency, and coherence, respectively. However, we find that the improvements are less pronounced after removing HDM compared to the baseline. In some cases, such as with GPT4, there are even declines. This indicates that HT works more effectively when combined with HDM, leading to better overall performance.



<!-- page 0012 -->

<table>
  <thead>
    <tr>
      <th rowspan="2">Setting</th>
      <th colspan="3">EN=&gt;ZH</th>
      <th colspan="3">EN=&gt;SP</th>
    </tr>
    <tr>
      <th>SQM-H</th>
      <th>SQM-F</th>
      <th>SQM-C</th>
      <th>SQM-H</th>
      <th>SQM-F</th>
      <th>SQM-C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7" align="center">GPT4-Turbo</td>
    </tr>
    <tr>
      <td>-</td>
      <td><strong>70.50</strong></td>
      <td><strong>98.80</strong></td>
      <td><strong>96.70</strong></td>
      <td><strong>68.00</strong></td>
      <td><strong>99.10</strong></td>
      <td><strong>95.70</strong></td>
    </tr>
    <tr>
      <td>-HDM</td>
      <td>54.60</td>
      <td>95.65</td>
      <td>88.67</td>
      <td>57.30</td>
      <td>97.00</td>
      <td>89.10</td>
    </tr>
    <tr>
      <td>-HT</td>
      <td>69.15</td>
      <td>96.67</td>
      <td>91.77</td>
      <td>67.10</td>
      <td>98.67</td>
      <td>94.05</td>
    </tr>
    <tr>
      <td>base</td>
      <td>51.60</td>
      <td>93.30</td>
      <td>87.20</td>
      <td>55.20</td>
      <td>96.67</td>
      <td>88.80</td>
    </tr>
    <tr>
      <td colspan="7" align="center">Gemini1.5-Pro</td>
    </tr>
    <tr>
      <td>-</td>
      <td><strong>66.50</strong></td>
      <td><strong>97.30</strong></td>
      <td><strong>93.90</strong></td>
      <td><strong>66.20</strong></td>
      <td><strong>98.70</strong></td>
      <td><strong>94.61</strong></td>
    </tr>
    <tr>
      <td>-HDM</td>
      <td>57.40</td>
      <td>94.00</td>
      <td>93.50</td>
      <td>60.80</td>
      <td>98.30</td>
      <td>89.40</td>
    </tr>
    <tr>
      <td>-HT</td>
      <td>63.20</td>
      <td>96.30</td>
      <td>90.80</td>
      <td>65.80</td>
      <td>98.40</td>
      <td>92.00</td>
    </tr>
    <tr>
      <td>base</td>
      <td>56.30</td>
      <td>93.70</td>
      <td>87.70</td>
      <td>53.60</td>
      <td>97.23</td>
      <td>90.83</td>
    </tr>
  </tbody>
</table>

Table 5: Ablation results on Humour Decomposition Mechanism with various LLMs settings on Short Joke Dataset.

### 5.4 Case Study and Error Analysis

In this section, we present some correct examples generated by using HDM as shown in figure 4 and make some analysis for some bad cases. For instance, the generated translation of $P_1$ describes the background sentence as “the snail say while riding on the turtle’s back”, while the snail shouting “Wheeeeeee” reflects the snail’s feeling that the turtle is fast, which highlights the humorous effect. In the traditional translation, the onomatopoeia of “Wheeeeeee” is translated into “Whoosh (back translation)”, while in HDM, the snail more intuitively reflects the language humour effect by saying “Wow This is exciting! (back translation)”. The jokes generated by using HDM are more informative and coherent than directly translated text, thus allowing people to better understand the humorous connotations of the texts.

In addition, there are still some samples that HDM is hard to address. One situation involves the judgment of the source language based on the pronunciation and shape of characters within the context of puns. For example, the joke is “How do sheep in Mexico say Merry Christmas? Fleece Navidad!”. The punchline of this joke relies on the auditory similarity between “Fleece” and “Feliz.” By substituting “Feliz” with “Fleece” it creates a humorous image of sheep celebrating Christmas in their own way. In this case, HDM struggles to generate jokes that combine puns with cultural and linguistic elements.

## 6 Limitations and Future Work

While HDM shows the effectiveness in humour translation, there are some limitations worth noting:

– This study is limited to four languages: Chinese, English, Spanish, and German, with all datasets selected in English. Future research could extend both the data and the proposed method to additional translation directions.



<!-- page 0013 -->

- Although some studies have shown that GPT-4’s opinions significantly overlap with human reviewers [23], human evaluation remains the gold standard in assessing natural language generation quality [9]. The absence of human evaluation in our current metrics may introduce bias into the final results. In future work, we plan to incorporate human judgments to enhance the robustness and validity of the evaluation.
- Although Section 5.4 provides both correct examples and error cases of HDM in humour translation, its applicability to different types of humour has not yet been systematically evaluated. Given the diversity of humour across regions and cultural contexts, further in-depth analysis is required to assess the method’s generalizability in broader translational scenarios.

Nevertheless, HDM provides meaningful insights into tackling the complex problems of humour loss and linguistic interference in humour translation, facilitating the effective transfer of humour across different languages.

## 7 Conclusion

In this paper, we introduce a novel approach named Humour Decomposition Mechanism (HDM) for humour translation. Specifically, HDM consists of *humour decomposition*, *translation module* and *humour composition*, which creates a three-step paradigm of mining intrinsic knowledge of jokes, translating the intrinsic knowledge and then composing the jokes based on the translation. Moreover, we integrate humour theory into HDM to boost performance further. Experimental results in automatic evaluation reveal our method can attain promising performance in humour translation. In the future, we will explore the methods for incorporating human review in HDM to further improve the quality of humour translation.

## References

1. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023)

2. AI, ., ; Young, A., Chen, B., Li, C., Huang, C., Zhang, G., Zhang, G., Li, H., Zhu, J., Chen, J., Chang, J., Yu, K., Liu, P., Liu, Q., Yue, S., Yang, S., Yang, S., Yu, T., Xie, W., Huang, W., Hu, X., Ren, X., Niu, X., Nie, P., Xu, Y., Liu, Y., Wang, Y., Cai, Y., Gu, Z., Liu, Z., Dai, Z.: Yi: Open foundation models by 01.ai (2024)

3. Alnajjar, K., Hämäläinen, M., Tiedemann, J., Laaksonen, J., Kurimo, M.: When to laugh and how hard? a multimodal approach to detecting humor and its intensity. arXiv preprint arXiv:2211.01889 (2022)

4. Amir, S., Wallace, B.C., Lyu, H., Silva, P.C.M.J.: Modelling context with user embeddings for sarcasm detection in social media. arXiv preprint arXiv:1607.00976 (2016)

5. Chen, A., Lou, L., Chen, K., Bai, X., Xiang, Y., Yang, M., Zhao, T., Zhang, M.: DUAL-REFLECT: Enhancing large language models for reflective translation through dual learning feedback mechanisms. In: Ku, L.W., Martins,



<!-- page 0014 -->

A., Srikumar, V. (eds.) Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). pp. 693–704. Association for Computational Linguistics, Bangkok, Thailand (Aug 2024), https://aclanthology.org/2024.acl-short.64

6. Chen, G., Ma, S., Chen, Y., Zhang, D., Pan, J., Wang, W., Wei, F.: Towards making the most of cross-lingual transfer for zero-shot neural machine translation. In: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). pp. 142–157 (2022)

7. Chen, Y., Shi, B., Si, M.: Prompt to gpt-3: Step-by-step thinking instructions for humor generation. arXiv preprint arXiv:2306.13195 (2023)

8. Chen, Y., Yuan, Y., Liu, P., Liu, D., Guan, Q., Guo, M., Peng, H., Liu, B., Li, Z., Xiao, Y.: Talk funny! a large-scale humor response dataset with chain-of-humor interpretation. In: Proceedings of the AAAI Conference on Artificial Intelligence. vol. 38, pp. 17826–17834 (2024)

9. Clark, E., August, T., Serrano, S., Haduong, N., Gururangan, S., Smith, N.A.: All that’s’ human’is not gold: Evaluating human evaluation of generated text. arXiv preprint arXiv:2107.00061 (2021)

10. Gambier, Y.: Translations| rapid and radical changes in translation and translation studies. International Journal of Communication 10, 20 (2016)

11. Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., Neubig, G.: Pal: Program-aided language models. In: International Conference on Machine Learning. pp. 10764–10799. PMLR (2023)

12. García-Díaz, J.A., Valencia-García, R.: UMUTeam at SemEval-2021 task 7: Detecting and rating humor and offense with linguistic features and word embeddings. In: Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021). pp. 1096–1101. Association for Computational Linguistics, Online (Aug 2021), https://aclanthology.org/2021.semeval-1.152

13. Hagos, D.H., Battle, R., Rawat, D.B.: Recent advances in generative ai and large language models: Current status, challenges, and perspectives. IEEE Transactions on Artificial Intelligence (2024)

14. Hasan, M.K., Lee, S., Rahman, W., Zadeh, A., Mihalcea, R., Morency, L.P., Hoque, E.: Humor knowledge enriched transformer for understanding multimodal humor. In: Proceedings of the AAAI conference on artificial intelligence. vol. 35, pp. 12972–12980 (2021)

15. He, Z., Liang, T., Jiao, W., Zhang, Z., Yang, Y., Wang, R., Tu, Z., Shi, S., Wang, X.: Exploring human-like translation strategy with large language models. Transactions of the Association for Computational Linguistics 12, 229–246 (2024)

16. Hendy, A., Abdelrehim, M., Sharaf, A., Raunak, V., Gabr, M., Matsushita, H., Kim, Y.J., Afify, M., Awadalla, H.H.: How good are gpt models at machine translation? a comprehensive evaluation. arXiv preprint arXiv:2302.09210 (2023)

17. Hopkinson, C.: Factors in linguistic interference: A case study in translation. SKASE Journal of translation and interpretation 2(1), 13–23 (2007)

18. Ji, B., Liu, H., Du, M., Ng, S.K.: Chain-of-thought improves text generation with citations in large language models. In: Proceedings of the AAAI Conference on Artificial Intelligence. vol. 38, pp. 18345–18353 (2024)

19. Jiao, W., Wang, W., Huang, J.t., Wang, X., Tu, Z.: Is chatgpt a good translator? a preliminary study. arXiv preprint arXiv:2301.08745 1(10) (2023)

20. Karpinska, M., Iyyer, M.: Large language models effectively leverage document-level context for literary translation, but critical errors persist. arXiv preprint arXiv:2304.03245 (2023)



<!-- page 0015 -->

21. Kenneth, M.O., Khosmood, F., Edalat, A.: A two-model approach for humour style recognition. arXiv preprint arXiv:2410.12842 (2024)

22. Kocmi, T., Federmann, C.: Large language models are state-of-the-art evaluators of translation quality. arXiv preprint arXiv:2302.14520 (2023)

23. Liang, W., Zhang, Y., Cao, H., Wang, B., Ding, D.Y., Yang, X., Vodrahalli, K., He, S., Smith, D.S., Yin, Y., et al.: Can large language models provide useful feedback on research papers? a large-scale empirical analysis. NEJM AI **1**(8), AIoa2400196 (2024)

24. Ma, X., Cheung, A.K.: Language interference in english-chinese simultaneous interpreting with and without text. Babel **66**(3), 434–456 (2020)

25. Nida, E.A.: Toward a science of translating: with special reference to principles and procedures involved in Bible translating. Brill Archive (1964)

26. Pym, A.: Exploring translation theories. Routledge (2023)

27. Raskin, V.: Semantic mechanisms of humor. In: Annual Meeting of the Berkeley Linguistics Society. pp. 325–335 (1979)

28. Rei, R., Stewart, C., Farinha, A.C., Lavie, A.: Comet: A neural framework for mt evaluation. arXiv preprint arXiv:2009.09025 (2020)

29. Roznovjak, J.: Question-answer jokes (2016), kaggle, Data set. Available at: https://www.kaggle.com/datasets/jiriroz/qa-jokes

30. Sellam, T., Das, D., Parikh, A.: BLEURT: Learning robust metrics for text generation. In: Jurafsky, D., Chai, J., Schluter, N., Tetreault, J. (eds.) Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. pp. 7881–7892. Association for Computational Linguistics, Online (Jul 2020). https://doi.org/10.18653/v1/2020.acl-main.704, https://aclanthology.org/2020.acl-main.704

31. Team, G., Georgiev, P., Lei, V.I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al.: Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530 (2024)

32. Toplyn, J.: Comedy Writing for Late-night TV: How to Write Monologue Jokes, Desk Pieces, Sketches, Parodies, Audience Pieces, Remotes, and Other Short-form Comedy. Twenty Lane Media, LLC (2014), https://books.google.co.nz/books?id=yYKooAEACAAJ

33. Vandaele, J.: Translating humour. Routledge (2016)

34. Vilar, D., Freitag, M., Cherry, C., Luo, J., Ratnakar, V., Foster, G.: Prompting palm for translation: Assessing strategies and performance. arXiv preprint arXiv:2211.09102 (2022)

35. Wang, D., Fan, K., Chen, B., Xiong, D.: Efficient cluster-based k-nearest-neighbor machine translation. arXiv preprint arXiv:2204.06175 (2022)

36. Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., Zhou, D.: Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171 (2022)

37. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou, D., et al.: Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems **35**, 24824–24837 (2022)

38. Xia, C., Amini, M., Lee, K.F.: Humor translation: A case study on the loss of humorous loads in spongebob squarepants. Cadernos de Tradução **43**, e89705 (2023)

39. Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., et al.: Qwen2. 5 technical report. arXiv preprint arXiv:2412.15115 (2024)

40. Ye, X., Durrett, G.: Explanation selection using unlabeled data for chain-of-thought prompting. arXiv preprint arXiv:2302.04813 (2023)



<!-- page 0016 -->

41. Zabalbeascoa, P.: Humor and translation—an interdiscipline (2005)

42. Zhang, B., Haddow, B., Birch, A.: Prompting large language model for machine translation: A case study. In: International Conference on Machine Learning. pp. 41092–41110. PMLR (2023)

43. Zhang, Z., Zhang, A., Li, M., Smola, A.: Automatic chain of thought prompting in large language models. arXiv preprint arXiv:2210.03493 (2022)

44. Zhao, Y., Yin, H., Zeng, B., Wang, H., Shi, T., Lyu, C., Wang, L., Luo, W., Zhang, K.: Marco-o1: Towards open reasoning models for open-ended solutions. arXiv preprint arXiv:2411.14405 (2024)

45. Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I.: Judging llm-as-a-judge with mt-bench and chatbot arena (2023)

46. Zhou, D., Schärli, N., Hou, L., Wei, J., Scales, N., Wang, X., Schuurmans, D., Cui, C., Bousquet, O., Le, Q., et al.: Least-to-most prompting enables complex reasoning in large language models. arXiv preprint arXiv:2205.10625 (2022)

47. Zhou, Y., Muresanu, A.I., Han, Z., Paster, K., Pitis, S., Chan, H., Ba, J.: Large language models are human-level prompt engineers. arXiv preprint arXiv:2211.01910 (2022)

48. Zhu, W., Liu, H., Dong, Q., Xu, J., Huang, S., Kong, L., Chen, J., Li, L.: Multilingual machine translation with large language models: Empirical results and analysis. arXiv preprint arXiv:2304.04675 (2023)
