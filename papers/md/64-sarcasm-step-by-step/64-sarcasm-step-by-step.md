<!-- Transcribed from 64-sarcasm-step-by-step.pdf -->



<!-- page 0001 -->

# Is Sarcasm Detection A Step-by-Step Reasoning Process in Large Language Models?

**Ben Yao**^a^, **Yazhou Zhang**^b,c^, **Qiuchi Li**^a^, **Jing Qin**^b^

^a^University of Copenhagen, ^b^The Hong Kong Polytechnic University, ^c^Tianjin University

## Abstract

Elaborating a series of intermediate reasoning steps significantly improves the ability of large language models (LLMs) to solve complex problems, as such steps would evoke LLMs to think sequentially. However, human sarcasm understanding is often considered an intuitive and holistic cognitive process, in which various linguistic, contextual, and emotional cues are integrated to form a comprehensive understanding, in a way that does not necessarily follow a step-by-step fashion. To verify the validity of this argument, we introduce a new prompting framework (called SarcasmCue) containing four sub-methods, *viz.* chain of contradiction (CoC), graph of cues (GoC), bagging of cues (BoC) and tensor of cues (ToC), which elicits LLMs to detect human sarcasm by considering sequential and non-sequential prompting methods. Through a comprehensive empirical comparison on four benchmarks, we highlight three key findings: (1) CoC and GoC show superior performance with more advanced models like GPT-4 and Claude 3.5, with an improvement of 3.5% ↑. (2) ToC significantly outperforms other methods when smaller LLMs are evaluated, boosting the F1 score by 29.7% ↑ over the best baseline. (3) Our proposed framework consistently pushes the state-of-the-art (i.e., ToT) by 4.2%, 2.0%, 29.7%, and 58.2% in F1 scores across four datasets. This demonstrates the effectiveness and stability of the proposed framework.[^1]

[Figure: Side-by-side comparison diagram labeled “Mathematical Reasoning” vs “Sarcasm Detection”. Left panel: “Mathematical Reasoning” question about Alan, Ben, and Laurie collecting shells, with an LLM producing step-by-step arithmetic answers ending “Finally, Alan collected 48 shells on the school trip.” Right panel: “Sarcasm Detection” with context “Excuse me. Oh, it’s my assistant, Trevor. Go for Koothrappali.” and question “They gave him an assistant? If I want a new pen, I have to go to the bank with wire cutters. Is this sentence sarcastic or not?”, with an LLM answer analyzing linguistic, contextual, and emotional cues and concluding the sentence is markedly sarcastic.]

Figure 1: The comparison of the processes of mathematical reasoning and sarcasm detection.

## 1 Introduction

Recent large language models have demonstrated impressive performance across downstream natural language processing (NLP) tasks, in which “System 1” - the fast, unconscious, and intuitive tasks, e.g., sentiment classification, topic analysis, etc., have been argued to be successfully performed (Cui et al., 2024). Instead, increasing efforts have been devoted to the other class of tasks - “System 2”, which requires slow, deliberative and multi-steps thinking, such as logical, mathematical, and commonsense reasoning tasks (Wei et al., 2022). To improve the ability of LLMs to solve such complex problems, a popular paradigm is to decompose complex problems into a series of intermediate solution steps, and elicit LLMs to think step-by-step, such as chain of thought (CoT) (Wei et al., 2022), tree of thought (ToT) (Yao et al., 2024), graph of thought (GoT) (Besta et al., 2024), etc.

However, due to its inherent ambivalence and figurative nature, sarcasm detection is often considered a holistic and non-rational cognitive process that does not conform to step-by-step logical reasoning for two main reasons: (1) sarcasm expression does not strictly conform to formal logical structures, such as the law of hypothetical syllogism (i.e., if $\mathcal{A} \Rightarrow \mathcal{B}$ and $\mathcal{B} \Rightarrow \mathcal{C}$, then $\mathcal{A} \Rightarrow \mathcal{C}$). For example, *“Poor Alice has fallen for that stupid Bob; and that stupid Bob is head over heels for*

[^1]: Our codes are available at https://github.com/qiuchili/llm_sarcasm_detection



<!-- page 0002 -->

*Claire; but don’t assume for a second that Alice would like Claire”;* (2) sarcasm judgment is often considered a fluid combination of various cues. Each cue holds equal importance and there is no rigid sequence of steps among them, as shown in Fig. 1. Hence, the main research question can be summarized as:

**RQ:** *Is human sarcasm detection a step-by-step reasoning process?*

To answer this question, we propose a theoretical framework, called SarcasmCue, based on the sequential and non-sequential prompting paradigm. It consists of four prompting methods, i.e., *chain of contradiction (CoC)*, *graph of cues (GoC)*, *bagging of cues (BoC)* and *tensor of cues (ToC)*. Each method has its own focus and advantages. In this work, *cue* is similar to *thought*, being a coherent language sequence related to linguistics, context, or emotion that serves as an intermediate indicator for identifying sarcasm, such as rhetorical devices or emotional words. More specifically,

- **CoC.** It harnesses the quintessential property of sarcasm (namely the contradiction between surface sentiment and true intention). It aims to: (1) identify the surface sentiment by extracting keywords, etc.; (2) deduce the true intention by scrutinizing rhetorical devices, etc.; and (3) determine the inconsistency between them. It is a typical linear structure.
- **GoC.** Generalizing over CoC, GoC frames the problem of sarcasm detection as a search over a graph and treats various cues as nodes, with the relations across cues represented as edges. Unlike CoC and ToT, it goes beyond following a fixed hierarchy or linear reasoning path. In summary, both CoC and GoC follow the step-by-step reasoning process.
- **BoC.** BoC is a bagging approach that constructs a pool of diverse cues and randomly sampling multiple cue subsets. LLMs are employed to generate multiple predictions based on these subsets, and such predictions are aggregated to produce the final result. It is a set-based structure.
- **ToC.** ToC treats each type of cues (namely linguistic, contextual, and emotional cues) as an independent, orthogonal view for sarcasm understanding and constructs a multi-view representation through the tensor product. It allows language models to leverage higher-order interactions among the cues. ToC can be visualized as a 3D volumetric structure. Hence, BoC and ToC are proposed based on the assumption that sarcasm detection is not a step-by-step reasoning process.
- **Their correlation.** These four methods represent an evolution from linear to nonlinear, and from a single perspective to multiple perspectives, together forming a comprehensive theoretical framework (SarcasmCue). Their design aims to adapt to various sarcasm detection scenarios. We present empirical evaluations of the proposed prompting approaches across four benchmarks over 4 SOTA LLMs (i.e., GPT-4o, Claude 3.5 Sonnet, Llama 3-8B, Qwen 2-7B), and compare their results against 3 SOTA prompting approaches (i.e., standard IO prompting, CoT and ToT). we highlight three key observations: (1) When the base model is more advanced (such as GPT-4 and Claude 3.5 Sonnet), CoC and GoC show superior performance against the state-of-the-art (SoTA) baseline with an improvement of 3.5% ↑. (2) ToC achieves the best performance when smaller LLMs are evaluated. For example, in Llama 3-8B, ToC’s average F1 score of 65.24 represents a 29.7% improvement over the best baseline method, ToT. In Qwen 2-7B, ToC shows a 58.2% improvement over the best baseline method, IO. (3) Our proposed framework consistently pushes SoTA by 4.2%, 2.0%, 29.7% and 58.2% in F1 scores across four datasets. This demonstrates the effectiveness of the proposed framework. The main contributions are concluded as follows:

- Our work is the first to investigate the step-wise reasoning nature of sarcasm detection by using both sequential and non-sequential prompting methods.

- We propose a new prompting framework that consists of four sub-methods, *viz.* CoC, GoC, BoC and ToC.

- Comprehensive experiments over four datasets demonstrate the superiority of the proposed prompting framework.

## 2 Related Work

### 2.1 Chain-of-Thought Prompting

Inspired by the step-by-step thinking ability of humans, CoT prompting was proposed to “prompt” language models to produce intermediate reasoning steps. Wei et al. (2022) made a formal defi-



<!-- page 0003 -->

nition of CoT prompting in LLMs and proved its effectiveness by presenting empirical evaluations on arithmetic reasoning benchmarks. However, its performance hinged on the quality of manually crafted prompts. To fill this gap, Auto-CoT was proposed to automatically construct demonstrations with questions and reasoning chains (Zhang et al., 2022). Furthermore, Yao et al. (2024) introduced a non-chain prompting framework, namely ToT, which made LLMs consider multiple different reasoning paths to decide the next course of action. Beyond CoT and ToT approaches, Besta et al. (2024) modeled the information generated by an LLM as an arbitrary graph (i.e., GoT), where units of information were considered as vertices and the dependencies between these vertices were edges.

However, all of them adopt the sequential decoding paradigm of “let LLMs think step by step”. Contrarily, it is argued that sarcasm judgment does not conform to step-by-step logical reasoning, and there is an urgent need to develop non-sequential prompting approaches.

## 2.2 Sarcasm Detection

Sarcasm detection has evolved from early statistical learning based approaches to traditional neural methods, and further advanced to modern neural methods epitomized by Transformer models. In early stage, statistical learning based approaches mainly employ statistical learning techniques, e.g., SVM, NB, etc., to extract patterns and relationships within the data (Zhang et al., 2023). As deep learning based architectures have shown the superiority, numerous base neural networks, e.g., such as CNN (Jain et al., 2020), LSTM (Ghosh et al., 2018), GCN (Liang et al., 2022), etc., have been predominantly utilized during the middle stage of sarcasm detection research. Now, sarcasm detection research has stepped into the era of pre-trained language models (PLMs). An increasing number of researchers are designing sophisticated PLM architectures to serve as encoders for obtaining effective text representations (Liu et al., 2023).

Different from them, we propose four prompting methods to make the first attempt to explore the potential of prompting LLMs in sarcasm detection.

## 3 The Proposed Framework: SarcasmCue

The proposed SarcasmCue framework is illustrated in Fig. 2. We qualitatively compare SarcasmCue

Table 1: Comparison of prompting methods.

<table>
<thead>
<tr>
<th rowspan="2">Scheme</th>
<th colspan="2">Seq?</th>
<th colspan="3">Non-Seq?</th>
</tr>
<tr>
<th>Chain?</th>
<th>Tree?</th>
<th>Graph?</th>
<th>Set?</th>
<th>Tensor?</th>
</tr>
</thead>
<tbody>
<tr>
<td>IO</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
</tr>
<tr>
<td>CoT</td>
<td>✔</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
</tr>
<tr>
<td>ToT</td>
<td>✔</td>
<td>✔</td>
<td>✖</td>
<td>✖</td>
<td>✖</td>
</tr>
<tr>
<td>GoT</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>✖</td>
<td>✖</td>
</tr>
<tr>
<td><strong>SarcasmCue</strong></td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
<td>✔</td>
</tr>
</tbody>
</table>

with other prompting approaches in Tab. 1. SarcasmCue is the only one to fully support chain-based, tree-based, graph-based, set-based and multidimensional array-based reasoning. It is also the only one that simultaneously supports both sequential and non-sequential prompting methods.

## 3.1 Task Definition

Given the data set $\mathcal{D} = \{(\mathcal{X}, \mathcal{Y})\}$, where $\mathcal{X} = \{x_1, x_2, ..., x_n\}$ denotes the input text sequence and $\mathcal{Y} = \{y_1, y_2, ..., y_n\}$ denotes the output label sequence. We use $\mathcal{L}_{\theta}$ to represent a large language model with parameter $\theta$. Our task is to leverage a collection of cues $C = \{c_1, c_2, ..., c_k\}$ to brige the input $\mathcal{X}$ and the output $\mathcal{Y}$, where each cue $c_i$ is a coherent language sequence that serves as an intermediate indicator toward identifying sarcasm.

## 3.2 Chain of Contradiction

We capture the inherent paradoxical nature of sarcasm, which is the incongruity between the surface sentiment and the true intention, and propose *chain of contradiction*, a CoT-style paradigm that allows LLMs to decompose the problem of sarcasm detection into intermediate steps and solve each before making decision (Fig. 2 (a)). Each cue $c_k \sim \mathcal{L}_{\theta}^{CoC}(c_k|\mathcal{X}, c_1, c_2, ..., c_{k-1})$ is sampled sequentially, then the output $\mathcal{Y} \sim \mathcal{L}_{\theta}^{CoC}(\mathcal{Y}|\mathcal{X}, c_1, ..., c_k)$. A specific instantiation of CoC involves three steps:

**Step 1.** We first ask LLM to detect the surface sentiment via the following prompt $p_1$:

Given the input sentence $[\mathcal{X}]$, what is the SURFACE sentiment, as indicated by clues such as keywords, sentimental phrases, emojis?

$c_1$ is the output sequence, which can be formulated as $c_1 \sim \mathcal{L}_{\theta}^{CoC}(c_1|\mathcal{X}, p_1)$.

**Step 2.** We thus ask LLM to carefully discover the true intention via the following prompt $p_2$:

Deduce what the sentence really means, namely the TRUE intention, by carefully checking any rhetorical devices, language style, unusual punctuations, common senses.



<!-- page 0004 -->

[Figure: Illustration of four prompting sub-methods with panels labeled (a) Chain of Contradiction (CoC), (b) Graph of Cues (GoC), (c) Bagging of Cues (BoC), and (d) Tensor of Cues (ToC). Readable labels include Input, Output, Step 1: The surface sentiment, Step 2: The true intention, Step 3: Examine the consistency, Linguistic cues, Contextual cues, Emotional cues, Cue subsets, LLM, Voting, Embeddings, Tensor Product, Lin, Con, Emo.]

Figure 2: An illustration of our SarcasmCue framework that consists of four prompting sub-methods.

$c_2$ is the output sequence, which can be formulated as $c_2 \sim \mathcal{L}_{\theta}^{CoC}(c_2|\mathcal{X}, c_1, p_2)$.

**Step 3.** Let LLM examine the consistency between surface sentiment and true intention and make the final prediction:

> Based on Step 1 and Step 2, evaluate whether the surface sentiment aligns with the true intention. If they do not match, the sentence is probably ‘Sarcastic’. Otherwise, the sentence is ‘Not Sarcastic’. Return the label only.

CoC raises a presumption that the cues are linearly correlated, and detects human sarcasm through step-by-step reasoning. Further details see Algorithm 1 in App. A.

### 3.3 Graph of Cues

The linear structure of CoC restricts it to a single path of reasoning. To fill this gap, we introduce *graph of cues*, a graph based paradigm that allows LLMs to flexibly choose and weigh multiple cues, unconstrained by the need for unique predecessor nodes (Fig. 2 (b)). GoC frames the problem of sarcasm detection as a search over a graph, and is formulated as a tuple $(\mathcal{M}, \mathcal{G}, \mathcal{E})$, where $\mathcal{M}$ is the cue maker used to define what are the common cues, $\mathcal{G}$ is a graph of “sarcasm detection process”, $\mathcal{E}$ is cue evaluator used to determine which cues to keep selecting.

**1. Cue maker.** Human sarcasm judgment often relies on the combination and analysis of one or more cues to achieve an accurate understanding. Such cues can be broadly categorized into three types: linguistic cues, contextual cues and emotional cues. Linguistic cues refer to the linguistic features inherent in the text, including *keywords, rhetorical devices, punctuation* and *language style*. Contextual cues refer to the environment and background of the text, including *topic, cultural background, common knowledge*. Emotional cues denote the emotions implied in the text, including *emotional words, special symbols (such as emojis)* and *emotional contrasts*. Hence, GoC can obtain $4+3+3=10$ cues.

**2. Graph construction.** In $\mathcal{G}=(V,E)$, 10 cues are regarded as vertices, constituting the vertex set $V$, the supplement relations across cues are regarded as edges. Given the cue $c_k$, the cue evaluator $\mathcal{E}$ considers cue $c_j$ to provide the most complementary information to $c_k$, which would combine with $c_k$ to facilitate a deep understanding of sarcasm.

**3. Cue evaluator.** We associate $\mathcal{G}$ with LLM detecting sarcasm process. To advance this process, the cue evaluator $\mathcal{E}$ assesses the current progress by asking the LLM whether the cumulative cues obtained thus far are sufficient to yield an accurate judgment. The search goes to an end if a positive answer is returned; otherwise, the detection process proceeds by instructing the LLM to determine which additional cues to select and in what order. In this work, an LLM will act as the cue evaluator, similar to ToT.

We employ a voting strategy to determine the most valuable cue for selection, by deliberately comparing multiple potential cue candidates in a voting prompt, such as:



<!-- page 0005 -->

> Given an input text $\mathcal{X}$, the target is to accurately detect sarcasm. Now, we have collected the keyword information as the first step: $\{keywords\}$, judge if this provides over 95% confidence for accurate detection. If so, output the result. Otherwise, from the remaining cues $\{rhetorical\ devices, punctuation, ...\}$, vote the most valuable one to improve accuracy and confidence for the next step.

This step can be formulated as $\mathcal{E}(\mathcal{L}_{\theta}^{GoC}, c_{j+1}) \sim Vote\{\mathcal{L}_{\theta}^{GoC}(c_{j+1}|\mathcal{X}, c_{1,2,...,j})\}_{c_{j+1}\in\{c_{j+1},...,c_k\}}$. Until the final judgment is reached, the most valuable cue are always selected in a greedy fashion. Although GoC enables the exploration of many possible paths across the cue graph, its nature remains grounded in a step-by-step reasoning paradigm (see Algorithm 2 in App. A).

### 3.4 Bagging of Cues

We relax the assumption that the cues are interrelated in detecting sarcasm. We introduce *bagging of cues*, an ensemble learning based paradigm that allows LLMs to independently consider varied combinations of cues without assuming a fixed order or dependency among them (Fig. 2 (c)).

BoC constructs a pool of the pre-defined 10 cues $\mathcal{C}$. From this pool, $\mathcal{T}$ subsets are obtained through $\mathcal{T}$ random samplings, where each subset $S_t$ consists of $q$ (*i.e*., $1 \le q \le 10$) cues. BoC thus leverages LLMs to generate $T$ independent sarcasm predictions $\hat{y}_t$ based on the cues of each subset. Finally, such predictions are aggregated using a majority voting mechanism to produce the final result. This approach embraces randomness in cue selection, enhancing the LLM’s ability to explore numerous potential paths. BoC consists of three key steps:

**Step 1.** Cue subsets construction. A total of $\mathcal{T}$ cue subsets $S_{t\in\{1,2,...,\mathcal{T}\}}=\{c_{t1}, c_{t2}, ..., c_{tq}\}$ are created by randomly sampling without replacement from the complete pool of cues $\mathcal{C}$. Each sampling is independent.

**Step 2.** LLM prediction. For each subset $S_t$, a LLM $\mathcal{L}_{\theta}^{BoC}$ is used to independently make sarcasm prediction through the comprehensive analysis of the cues in the subset and the input text. This can be conceptually encapsulated as $\hat{y}_t \sim \mathcal{L}_{\theta}^{BoC}(\hat{y}_t|S_t, \mathcal{X})$.

**Step 3.** Prediction aggregation. Such predictions $\{\hat{y}_1,\hat{y}_2,...,\hat{y}_T\}$ are then combined using majority voting to yield the final prediction: $Y$.

BoC does not follow the step-by-step reasoning paradigm for sarcasm detection (see Algorithm 3 in App. A.)

### 3.5 Tensor of Cues

CoC and GoC methods mainly handle low-order interactions between cues, while BoC assumes cues are independent. To capture high-order interactions among cues, we introduce *tensor of cues*, a stereo paradigm that allows LLMs to amalgamate three types of cues (*viz*. linguistic, contextual and emotional cues) into a high-dimensional representation. (Fig. 2 (d)).

ToC treats each type of cues as an independent, orthogonal view for sarcasm understanding, and constructs a multi-view representation through the tensor product of such three types of cues. We first ask the LLM to extract linguistic, contextual, and emotional cues respectively via a simple prompt. For example:

> Extract the linguistic cues from the input sentence for sarcasm detection, such as keywords, rhetorical devices, punctuation and language style.

We take the outputs of the LLM’s final hidden layer as the embeddings of the linguistic, contextual and emotional cues, and apply a tensor fusion mechanism to fuse the cues as additional inputs to the sarcasm detection prompt. Inspired by the success of tensor fusion network (TFN) for multi-modal sentiment analysis (Zadeh et al., 2017), we apply token-wise tensor fusion to aggregate the cues. In particular, the embeddings are projected on a low-dimensional space via the fully-connected layers, i.e., $\overrightarrow{Lin}=(e_1^l,e_2^l,...,e_L^l)^T$, $\overrightarrow{Con}=(e_1^c,e_2^c,...,e_L^c)^T$, $\overrightarrow{Emo}=(e_1^e,e_2^e,...,e_L^e)^T$. Then, a tensor product is computed to combine the cues into a high-dimensional representation $\overrightarrow{Z}=(e_1,e_2,...,e_L)^T$, where

$$
e_i =
\begin{bmatrix}
e_i^l \\
1
\end{bmatrix}
\otimes
\begin{bmatrix}
e_i^c \\
1
\end{bmatrix}
\otimes
\begin{bmatrix}
e_i^e \\
1
\end{bmatrix}
,\forall i \in [1,2,...,L].
\tag{1}
$$

The additional value of 1 facilitates an explicit rendering of single-cue features and bi-cue interactions, leading to a comprehensive fusion of different cues encapsulated in each fused token $e_i \in \mathbb{R}^{(d_l+1)\times(d_c+1)\times(d_e+1)}$. The values of $d_l$, $d_c$ and $d_e$ are delicately chosen such that the dimensionality of fused token is precisely $d^2$.[^2] That enables an integration of the aggregated cues to the main prompt via:

[^2]: Otherwise the fused tokens are truncated to d-dim vectors



<!-- page 0006 -->

> Consider the information provided in the current cue above. Classify whether the input text is sarcastic or not. If you think the Input text is sarcastic, answer: yes. If you think the Input text is not sarcastic, answer: no.

The embedded prompt above is **prepended** with the aggregated cue sequence $\mathcal{Z}$ before fed to the LLM. As it is expected to output a single token of “yes” or “no” by design, we take the logit of the first generated token and decode the label accordingly as the output of ToC.

ToC facilitates deep interactions among these cues (see Algorithm 4 in App. A). Notably, as ToC manipulates cues on the vector level via neural structures, it requires access to the LLM structure and calls for supervised training on a collection of labeled samples. During training, the weights of the LLM are frozen, and the linear weights in $f_{lin}, f_{con}, f_{emo}$ are updated as an adaptation of LLM to the task context.

## 4 Experiments

### 4.1 Experiment Setups

**Datasets.** Four benchmarking datasets are selected as the experimental beds, *viz*. IAC-V1 (Lukin and Walker, 2013), IAC-V2 (Oraby et al., 2016), SemEval 2018 Task 3 (Van Hee et al., 2018) and MUStARD (Castro et al., 2019). The details and statistics for each dataset are shown in Table 1 in App. B.

**Baselines.** A wide range of SOTA baselines are included for comparison. They are:

- **Prompt tuning.** (1) IO, (2) CoT (Wei et al., 2022) and (3) ToT (Yao et al., 2024) are three SOTA prompting approaches by leveraging advanced prompt approaches to enhance LLM’s performance.
- **LLMs.** We involve four general LLMs in the experiment, including (4) GPT-4o, (5) Claude 3.5 Sonnet, (6) Llama 3-8B and (7) Qwen 2-7B (Bai et al., 2023). The first two are non-open-source LLMs while the last two are open-source LLMs. All four LLMs are representative of the strongest capabilities of their kinds.

**Implementation.** We have implemented the prompting methods for GPT-4o, Claude 3.5 Sonnet, Llama 3-8B and Qwen2-7B. The GPT-4o and Claude 3.5 Sonnet methods are implemented with the respective official Python API library: openAI[^3] and anthropic[^4], while the LLaMA and Qwen methods are implemented based on the Hugging Face Transformers library[^5]. Further details are presented in App. C.

### 4.2 Main Results

We report both **Accuracy** and **Macro-F1** scores for **SarcasmCue** and baselines in Table 2.

**(1) SarcasmCue consistently outperforms SoTA prompting baselines.** The proposed prompting strategies in the **SarcasmCue** framework achieve an overall superior performance compared to the baselines and consistently push the SoTA by 4.2%, 2.0%, 29.7% and 58.2% on F1 scores across four datasets. In particular, by explicitly designing the reasoning steps for sarcasm detection, CoC beats CoT by a tremendous margin on **GPT-4o** and **Claude 3.5 Sonnet**, whilst performing in par with CoT on **Llama 3-8B** and **Qwen 2-7B**. By predefining the set of cues in three main categories, GoC and BoC effectively guide LLMs to reason along correct paths, leading to more accurate judgments of sarcasm compared to the freestyle thinking in ToT. For example, the best proposed method, CoC (74.74), brings a 2.0% improvement over the best baseline method, IO (73.26). ToC achieves an effective tensor fusion of multi-aspect cues for sarcasm detection, significantly outperforming other baselines. For instance, it exhibits a 29.7% improvement over the best baseline method, ToT (50.31).

**(2) Sarcasm detection does not necessarily follow a step-by-step reasoning process.** The comparison between sequential (CoT, CoC, GoC, ToT) and non-sequential (BoC, ToC) prompting strategies fails to provide clear empirical evidences on whether sarcasm detection follows a step-by-step reasoning process. Nevertheless, the results on **Llama 3-8B** are more indicative to **GPT-4o** and **Claude 3.5 Sonnet**, since the latter models have strong capabilities on their own (IO) and do not significantly benefit from any prompting strategies. For **Llama 3-8B** and **Qwen 2-7B**, non-sequential methods, particularly ToC, show superior performance. In **Llama 3-8B**, ToC achieves an average F1 score of 65.24%, which is 8.9% higher than the best sequential method (GoC at 54.54%). The difference is even more pronounced on **Qwen 2-7B**. This seems to support our hypothesize that sarcasm

[^3]: https://github.com/openai/openai-python

[^4]: https://github.com/anthropics/anthropic-sdk-python

[^5]: https://huggingface.co/docs/transformers



<!-- page 0007 -->

**Table 2:** Performance on four datasets. For LLMs, all strategies are based on a zero-shot setting. <span style="color:blue">Blue</span> and <span style="color:purple">purple</span> indicate the best and second-best results for each dataset. ♣ represents significance improvement over the best baseline via unpaired t-test (p < 0.05).

| Paradigm | Method | IAC-V1 Acc. | IAC-V1 Ma-F1 | IAC-V2 Acc. | IAC-V2 Ma-F1 | SemEval 2018 Acc. | SemEval 2018 Ma-F1 | MUStARD Acc. | MUStARD Ma-F1 | Avg. of F1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **GPT-4o** | IO | 70.63 | 70.05 | 73.03 | 71.99 | 64.03 | 63.17 | 67.24 | 65.79 | 67.75 |
|  | CoT | 61.56 | 58.49 | 58.83 | 56.42 | 58.92 | 51.99 | 58.11 | 55.76 | 55.67 |
|  | ToT | 71.56 | 71.17 | 70.63 | 69.07 | 63.90 | 63.02 | 69.00 | 68.27 | 67.88 |
|  | **CoC (Ours)** | **72.19** | **71.52** | **73.36** | **72.31** | 70.79 | 70.60 | 69.42 | 68.48 | **70.73♣** |
|  | **GoC (Ours)** | 65.00 | 62.91 | 64.97 | 61.30 | **74.03♣** | **74.02♣** | **70.69♣** | **69.91♣** | 67.04 |
|  | **BoC (Ours)** | 68.75 | 67.36 | 71.35 | 69.39 | 62.12 | 61.85 | 69.42 | 68.45 | 66.76 |
| **Claude 3.5 Sonnet** | IO | 66.56 | 66.54 | **76.78** | **76.62** | 75.13 | 75.11 | **74.78** | **74.78** | 73.26 |
|  | CoT | **71.25** | **71.14** | 74.66 | 74.10 | 71.56 | 71.47 | 73.62 | 73.53 | 72.56 |
|  | ToT | 63.44 | 62.48 | 71.88 | 71.74 | 68.62 | 68.61 | 58.84 | 54.46 | 64.32 |
|  | **CoC (Ours)** | 69.69 | 69.40 | 73.22 | 73.17 | **82.27♣** | **82.23♣** | 74.20 | 74.16 | **74.74♣** |
|  | **GoC (Ours)** | 70.94 | 70.93 | 74.67 | 74.18 | 76.91 | 76.91 | 70.00 | 69.85 | 72.97 |
|  | **BoC (Ours)** | 66.88 | 66.40 | 73.61 | 72.82 | 70.28 | 70.07 | 72.61 | 71.93 | 70.31 |
| **Llama 3-8B** | IO | 55.94 | 46.40 | 54.70 | 43.74 | 49.36 | 44.46 | 54.64 | 44.99 | 44.90 |
|  | CoT | 56.25 | 47.28 | 54.22 | 42.96 | 49.36 | 44.55 | 54.20 | 44.86 | 44.91 |
|  | ToT | 52.50 | 48.98 | 55.95 | 53.05 | 50.64 | 48.63 | 54.35 | 50.56 | 50.31 |
|  | **CoC (Ours)** | 56.25 | 46.95 | 54.03 | 42.60 | 49.23 | 44.36 | 54.93 | 45.66 | 44.89 |
|  | **GoC (Ours)** | 57.10 | 54.96 | 54.22 | 53.30 | 57.33 | 57.24 | 52.77 | 52.67 | 54.54 |
|  | **BoC (Ours)** | **62.50** | 59.28 | 62.57 | 58.11 | 65.94 | 65.50 | 59.71 | 56.70 | 59.90 |
|  | **ToC (Ours)** | 62.19 | **61.78♣** | **72.95♣** | **72.94♣** | **68.88♣** | **68.21♣** | **61.26♣** | **58.03♣** | **65.24♣** |
| **Qwen 2-7B** | IO | 56.56 | 49.32 | 51.82 | 38.57 | 45.15 | 38.83 | 54.78 | 46.17 | 43.22 |
|  | CoT | 54.69 | 46.53 | 52.88 | 40.12 | 43.24 | 35.79 | 54.93 | 45.81 | 42.06 |
|  | ToT | 53.44 | 43.71 | 50.29 | 39.62 | 44.26 | 38.12 | 52.90 | 44.60 | 41.51 |
|  | **CoC (Ours)** | 55.00 | 45.77 | 51.92 | 38.90 | 43.75 | 36.37 | 53.77 | 44.26 | 41.33 |
|  | **GoC (Ours)** | 55.00 | 47.35 | 53.45 | 42.25 | 45.03 | 38.17 | 54.49 | 47.49 | 43.82 |
|  | **BoC (Ours)** | 52.50 | 43.78 | 52.40 | 40.24 | 49.87 | 45.63 | 54.06 | 46.11 | 43.94 |
|  | **ToC (Ours)** | **71.56♣** | **71.56♣** | **72.33** | **71.76♣** | **68.88♣** | **68.77♣** | **65.94♣** | **61.46♣** | **68.39♣** |

has a non-sequential nature.

### 4.3 Ablation Study

Table 3 presents the result of ablation study. *w/o Lin*, *w/o Emo*, *w/o Con* refer to the method where linguistic, emotional and contextual cues are ablated, respectively. To avoid proactive extraction of ablated cues by an LLM, we explicitly “prompt away” the cues in the inputs. An example prompt could be “You can only use the emotional cues and contextual cues, and do not use any linguistic information here” for the *w/o Lin* case.

The experiment results highlight the following conclusions: (a) the removal of any single type of cue leads to a noticeable drop in performance across all datasets, demonstrating the importance of each type of cue in sarcasm detection; (b) linguistic cues appear to have the most significant impact, as removing them leads to a noticeable decrease in performance across most settings; (c) the absence of contextual cues also affects the performance, but to a lesser extent compared to linguistic cues.

### 4.4 Zero-shot v/s Few-shot Prompting

Since the above experiments are mainly based on a zero-shot setting, we are curious of whether the conclusions also apply in a few-shot scenario. Therefore, we perform few-shot experiments to evaluate whether the proposed SarcasmCue framework can perform better when a limited number of contextual examples are available. We plot the main results in Fig. 3, we randomly sample $k = \{0, 1, 5, 10\}$ examples from the training set. Please refer to Table 2, App. D for the full result.

As shown in the plot, the number of demonstrations has a significant impact on the results. For example, CoC appears sensitive to the initial introduction of demonstration examples with a slight descent in performance when only 1 example is provided. However, as the number of shots increases to 5 and 10, the performance progressively improves. This trend underscores the effectiveness of CoC in adapting and refining its approach with more examples. In contrast, BoC demonstrates a consistent improvement in performance as the number of shots increases.



<!-- page 0008 -->

Table 3: Ablation study of BoC, GoC and ToC. All strategies are run on a zero-shot setting. The best results for each dataset are colored in blue.

| LLMs | Method | IAC-V1 | IAC-V2 | SemEval | MUStARD | Avg. of F1 |
|---|---|---:|---:|---:|---:|---:|
| **Claude 3.5** | w/o Lin | 68.41 | <span style="color: blue;"><u>75.62</u></span> | 77.42 | 69.66 | 72.78 |
|  | w/o Emo | 69.65 | 74.04 | <span style="color: blue;"><u>78.70</u></span> | <span style="color: blue;"><u>70.57</u></span> | <span style="color: blue;"><u>73.24</u></span> |
|  | w/o Con | 70.53 | 74.91 | 76.39 | 70.11 | 72.99 |
|  | **GoC** | <span style="color: blue;"><u>70.93</u></span> | 74.18 | 76.91 | 69.85 | 72.97 |
|  | w/o Lin | 45.89 | 42.49 | 47.47 | 65.33 | 50.30 |
|  | w/o Emo | 58.00 | 56.99 | 56.81 | 68.84 | 60.16 |
|  | w/o Con | 61.71 | 63.70 | 69.53 | 74.80 | 67.44 |
|  | **BoC** | <span style="color: blue;"><u>66.40</u></span> | <span style="color: blue;"><u>72.82</u></span> | <span style="color: blue;"><u>70.07</u></span> | <span style="color: blue;"><u>71.93</u></span> | <span style="color: blue;"><u>70.31</u></span> |
| **Llama 3-8B** | w/o Lin | 45.79 | 51.90 | 56.01 | 46.84 | 50.14 |
|  | w/o Emo | 48.60 | 49.40 | 52.38 | 45.12 | 48.88 |
|  | w/o Con | 52.51 | <span style="color: blue;"><u>53.69</u></span> | 52.14 | 48.28 | 51.66 |
|  | **GoC** | <span style="color: blue;"><u>54.96</u></span> | 53.30 | <span style="color: blue;"><u>57.24</u></span> | <span style="color: blue;"><u>52.67</u></span> | <span style="color: blue;"><u>54.54</u></span> |
|  | w/o Lin | 52.71 | 57.51 | 57.53 | 53.06 | 55.20 |
|  | w/o Emo | 57.33 | 59.40 | 62.01 | 53.06 | 57.95 |
|  | w/o Con | 56.88 | <span style="color: blue;"><u>60.36</u></span> | 59.04 | 52.30 | 57.15 |
|  | **BoC** | <span style="color: blue;"><u>59.28</u></span> | 58.11 | <span style="color: blue;"><u>65.50</u></span> | <span style="color: blue;"><u>56.70</u></span> | <span style="color: blue;"><u>59.90</u></span> |
|  | w/o Lin | 53.31 | 67.05 | 59.20 | 48.05 | 56.90 |
|  | w/o Emo | 57.42 | 67.08 | 64.01 | 52.89 | 60.35 |
|  | w/o Con | 55.26 | 71.78 | 63.93 | 52.48 | 60.86 |
|  | **ToC** | <span style="color: blue;"><u>61.78</u></span> | <span style="color: blue;"><u>72.94</u></span> | <span style="color: blue;"><u>68.21</u></span> | <span style="color: blue;"><u>58.03</u></span> | <span style="color: blue;"><u>65.24</u></span> |

[Figure: Three line charts with legend “GPT-4o” and “Claude 3.5 Sonnet”; panels titled “CoC”, “GoC”, and “BoC”; y-axis “Avg. of Ma-F1 (±SD)”; x-axis “K-shot” with ticks 0, 1, 5, 10.]

Figure 3: The average Macro-F1 across K-shots for the **GPT-4o** and **Claude 3.5 Sonnet** models.

[Figure: Multiple line charts showing influence of model scale; top row for Qwen 2 with panels “CoC”, “GoC”, “BoC”, “ToC” and x-axis labels 1.5B, 7B, 72B; bottom row for Llama 3 with panels “CoC”, “GoC”, “BoC” and x-axis labels 8B, 70B; y-axis “Avg. of Ma-F1 (±SD)”; legend “Qwen 2” and “Llama 3”.]

Figure 4: The influence of model scale. The figures in the top and bottom correspond to Qwen and Llama models, respectively.

Overall, these results demonstrate the robustness and adaptability of the SarcasmCue framework in zero-shot and few-shot scenarios. The framework can effectively utilize limited contextual examples to further improve sarcasm detection, making it suitable for applications where large annotated datasets are not readily available.

### 4.5 Influences of LLM scales

In an attempt to study the influence of different LLM scales, we evaluate the performance of sarcasm detection of **Qwen** and **Llama** of varying sizes, see Fig. 4.

The key take-aways are two-fold. First, the efficacy of our prompting methods is amplified with increasing model scale. This aligns closely with the key findings of the CoT method (Wei et al., 2022). This occurs because when an LLM is sufficiently large, its capabilities for multi-hop reasoning and understanding language are significantly enhanced. Second, ToC exhibits high sensitivity to model scale, performing significantly better in larger models, making it particularly suitable for larger-scale applications. CoC and GoC demonstrate moderate sensitivity, indicating a balance between performance improvement and scalability. BoC offers robust performance even in smaller models, suggesting its utility in resource-constrained scenarios. Overall, our proposed framework has a high adaptability across various model scales by offering suitable methods. Please see Table 3 and Fig. 1, App. E for the full results.



<!-- page 0009 -->

[Figure: Stacked bar chart showing average error rates by method. Legend: False Negative (pink), False Positive (blue). Y-axis: “Avg. of Error”; X-axis: “Method”. CoC: False Negative 4.92, False Positive 32.39. GoC: False Negative 8.65, False Positive 29.08. BoC: False Negative 4.74, False Positive 31.85. ToC: False Negative 13.16, False Positive 18.90.]

Figure 5: The average error rate of the four prompting methods.

### 4.6 Error Analysis

Fig. 5 shows the error rates of failure cases in terms of false negative (FN) and false positive (FP) for all four prompting methods in SarcasmCue. CoC, GoC and BoC exhibit higher false positive rates, indicating an over-detection of sarcasm that could lead to the frequent misclassification of normal statements as sarcastic. In contrast, ToC exhibits the lowest overall error rate and the FP and FN rates are indeed much closer to each other, indicating a balanced performance in detecting both sarcastic and non-sarcastic texts. These insights highlight potential directions for future improvements in sarcasm detection methodologies. The higher false positive rates suggest a need for refining these methods to reduce over-sensitivity and improve discrimination between sarcastic and non-sarcastic texts. The detailed case study is presented in App. F.

### 4.7 Extension to New Task

To evaluation the generalization capability of SarcasmCue, we apply it to another complex affection understanding task, **humor detection**. We compare our proposed SarcasmCue (where the backbone is GPT-4o) with two supervised PLMs (MFN (Hasan et al., 2021) and SVM+BERT (Zhang et al., 2024)) on two benchmarking datasets, CMMA (Zhang et al., 2024) and UR-FUNNY-V2 (Hasan et al., 2019).

As shown in Table 4, our methods (BoC and CoC) surpass the baseline on CMMA, whilst performing in par to the strongest baselines on the UR-FUNNY-V2 dataset. These results highlight the strong generalizability and versatility of our framework, confirming its potential utility across a wide range of affection understanding tasks.

Table 4: Performance on two humor detection datasets.

| Method | CMMA Acc. | CMMA Ma-F1 | UR-FUNNY-V2 Acc. | UR-FUNNY-V2 Ma-F1 | Avg. of F1 |
|---|---:|---:|---:|---:|---:|
| MFN | - | - | 64.44 | 64.12 | - |
| SVM+BERT | 55.23 | 54.08 | **69.62** | **69.27** | 61.68 |
| CoC | 78.14 | **58.60** | 64.08 | 60.13 | 65.24 |
| GoC | 79.60 | 57.42 | 64.89 | 61.65 | 65.89 |
| BoC | **75.81** | 58.58 | 68.71 | 66.83 | **67.48** |

## 5 Conclusions

This work aims to study the stepwise reasoning nature of sarcasm detection, and introduces a prompting framework (called SarcasmCue) containing four sub-methods, *viz*. CoC, GoC, BoC and ToC. It elicits LLMs to detect human sarcasm by considering sequential and non-sequential prompting methods. Our comprehensive evaluations across multiple benchmarks and SoTA LLMs demonstrate that SarcasmCue outperforms traditional methods and pushes the state-of-the-art by 4.2%, 2.0%, 29.7% and 58.2% F1 scores across four datasets. Additionally, the performance of SarcasmCue on humor detection further validate its robustness and versatility.

**Limitations.** SarcasmCue has its limitation: it incorporates only three types of cues, while other potentially useful cues have not been integrated, potentially limiting the model’s comprehensive understanding of sarcasm.

## References

Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. 2023. Qwen technical report. *arXiv preprint arXiv:2309.16609*.

Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawki, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, et al. 2024. Graph



<!-- page 0010 -->

of thoughts: Solving elaborate problems with large language models. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 38, pages 17682–17690.

Santiago Castro, Devamanyu Hazarika, Verónica Pérez-Rosas, Roger Zimmermann, Rada Mihalcea, and Soujanya Poria. 2019. Towards multimodal sarcasm detection (an \_obviously\_ perfect paper). In *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, Florence, Italy. Association for Computational Linguistics.

Can Cui, Yunsheng Ma, Xu Cao, Wenqian Ye, Yang Zhou, Kaizhao Liang, Jintai Chen, Juanwu Lu, Zichong Yang, Kuei-Da Liao, et al. 2024. A survey on multimodal large language models for autonomous driving. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*, pages 958–979.

Debanjan Ghosh, Alexander R Fabbri, and Smaranda Muresan. 2018. Sarcasm analysis using conversation context. *Computational Linguistics*, 44(4):755–792.

Md Kamrul Hasan, Sangwu Lee, Wasifur Rahman, Amir Zadeh, Rada Mihalcea, Louis-Philippe Morency, and Ehsan Hoque. 2021. Humor knowledge enriched transformer for understanding multimodal humor. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(14):12972–12980.

Md Kamrul Hasan, Wasifur Rahman, Amir Zadeh, Jianyuan Zhong, Md Iftekhar Tanveer, Louis-Philippe Morency, et al. 2019. Ur-funny: A multimodal language dataset for understanding humor. *arXiv preprint arXiv:1904.06618.*

Deepak Jain, Akshi Kumar, and Geetanjali Garg. 2020. Sarcasm detection in mash-up language using soft-attention based bi-directional lstm and feature-rich cnn. *Applied Soft Computing*, 91:106198.

Bin Liang, Chenwei Lou, Xiang Li, Min Yang, Lin Gui, Yulan He, Wenjie Pei, and Ruifeng Xu. 2022. Multi-modal sarcasm detection via cross-modal graph convolutional network. In *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, volume 1, pages 1767–1777. Association for Computational Linguistics.

Yiyi Liu, Ruqing Zhang, Yixing Fan, Jiafeng Guo, and Xueqi Cheng. 2023. Prompt tuning with contradictory intentions for sarcasm recognition. In *Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics*, pages 328–339.

Stephanie Lukin and Marilyn Walker. 2013. Really? well. apparently bootstrapping improves the performance of sarcasm and nastiness classifiers for online dialogue. In *Proceedings of the Workshop on Language Analysis in Social Media*, pages 30–40, Atlanta, Georgia. Association for Computational Linguistics.

Shereen Oraby, Vrindavan Harrison, Lena Reed, Ernesto Hernandez, Ellen Riloff, and Marilyn Walker. 2016. Creating and characterizing a diverse corpus of sarcasm in dialogue. In *Proceedings of the 17th Annual Meeting of the Special Interest Group on Discourse and Dialogue*, pages 31–41, Los Angeles. Association for Computational Linguistics.

Cynthia Van Hee, Els Lefever, and Véronique Hoste. 2018. SemEval-2018 task 3: Irony detection in English tweets. In *Proceedings of the 12th International Workshop on Semantic Evaluation*, pages 39–50, New Orleans, Louisiana. Association for Computational Linguistics.

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837.

Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. 2024. Tree of thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems*, 36.

Amir Zadeh, Minghai Chen, Soujanya Poria, Erik Cambria, and Louis-Philippe Morency. 2017. Tensor fusion network for multimodal sentiment analysis. In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing*, pages 1103–1114, Copenhagen, Denmark. Association for Computational Linguistics.



<!-- page 0011 -->

Yazhou Zhang, Dan Ma, Prayag Tiwari, Chen  
Zhang, Mehedi Masud, Mohammad Shorfuz-  
zaman, and Dawei Song. 2023. Stance-level  
sarcasm detection with bert and stance-centered  
graph attention networks. *ACM Transactions on*  
*Internet Technology*, 23(2):1–21.

Yazhou Zhang, Yang Yu, Qing Guo, Benyou Wang,  
Dongming Zhao, Sagar Uprety, Dawei Song, Qi-  
uchi Li, and Jing Qin. 2024. Cmma: Benchmark-  
ing multi-affection detection in chinese multi-  
modal conversations. *Advances in Neural Infor-*  
*mation Processing Systems*, 36.

Zhuosheng Zhang, Aston Zhang, Mu Li, and  
Alex Smola. 2022. Automatic chain of thought  
prompting in large language models. *arXiv*  
*preprint arXiv:2210.03493*.



<!-- page 0012 -->

## A A. Algorithms of Four Prompting Methods

**1. CoC.** We present further details of CoC in Algorithm 1.

---

**Algorithm 1** Chain of contradiction

**Require:**  
1: **Input:** Sentence $\mathcal{X}$, an LLM $\mathcal{L}_{\theta}$

**Ensure:**  
2: **Output:** Sarcasm Label $\mathcal{Y}$  
3: **Step 1:** Detect surface sentiment  
4: Output cue $c_1$: $c_1 \sim \mathcal{L}_{\theta}^{CoC}(c_1|\mathcal{X}, p_1)$  
5: **Step 2:** Discover true intention  
6: Output cue $c_2$: $c_2 \sim \mathcal{L}_{\theta}^{CoC}(c_2|\mathcal{X}, c_1, p_2)$  
7: **Step 3:** Evaluate consistency and make prediction  
8: Output cue $c_3$: $c_3 \sim \mathcal{L}_{\theta}^{CoC}(c_3|\mathcal{X}, c_1, c_2, p_3)$  
9: $\mathcal{Y} = \begin{cases}
\text{Sarcastic} & \text{if } c_1 \ne c_2 \\
\text{Not Sarcastic} & \text{otherwise}
\end{cases}$  
10: **return** $\mathcal{Y}$

---

**2. GoC.** We present further details of GoC in Algorithm 2.

---

**Algorithm 2** Graph of Cues (GoC) for Sarcasm Detection

**Require:**  
1: **Input:** Sentence $\mathcal{X}$, an LLM $\mathcal{L}_{\theta}$

**Ensure:**  
2: **Output:** Sarcasm Label $\mathcal{Y}$  
3: **1. Graph Construction**  
4: Construct graph $\mathcal{G} = (V, E)$ where 10 cues are vertices $V$ and relationships between cues are edges $E$  
5: **2. Sarcasm Detection Process**  
6: Initialize selected cues $C_{\text{selected}} = \emptyset, j = 0$  
7: Initialize current confidence $C = 0$  
8: **while** $C < 0.95 \cap j \leq 10$ **do**  
9: &nbsp;&nbsp;&nbsp;&nbsp;Select the most valuable cue:  
10: &nbsp;&nbsp;&nbsp;&nbsp;$c_{j+1} \sim Vote\ \{\mathcal{L}_{\theta}^{GoC}(c_{j+1}|\mathcal{X}, c_1, c_2, ..., c_j)\}_{c_{j+1}\in\{c_{j+1},...,c_{10}\}}$  
11: &nbsp;&nbsp;&nbsp;&nbsp;Add $c_{j+1}$ to $C_{\text{selected}}$  
12: &nbsp;&nbsp;&nbsp;&nbsp;Update current confidence $C$, $j$++  
13: Make final judgment based on $C_{\text{selected}}$: $\mathcal{Y} = \mathcal{L}_{\theta}^{GoC}(\mathcal{Y}|\mathcal{X}, C_{\text{selected}})$  
14: **return** $\mathcal{Y}$

---

**3. BoC.** We present further details of BoC in Algorithm 3.  
**4. ToC.** We present further details of ToC in Algorithm 4.

## B B. Datasets Details

**Datasets.** Four benchmarking datasets are selected as the experimental beds, *viz.* IAC-V1 (Lukin and Walker, 2013), IAC-V2 (Oraby et al., 2016), SemEval 2018 Task 3 (Van Hee et al., 2018) and MUStARD (Castro et al., 2019).

Table 5: Dataset statistics.

| Dataset | Avg. Length | #Train | #Dev | #Test |
|---|---:|---:|---:|---:|
| IAC-V1 | 68 | 1,595 | 80 | 320 |
| IAC-V2 | 43 | 5,216 | 262 | 1,042 |
| SemEval 2018 | 14 | 3,634 | 200 | 784 |
| MUStARD | 14 | 552 | - | 138 |

**IAC-V1 and IAC-V2** are from the Internet Argument Corpus (IAC) (Lukin and Walker, 2013), specifically designed for the task of identifying and analyzing sarcastic remarks within online debates and



<!-- page 0013 -->

**Algorithm 3** Bagging of cues

**Require:**  
1: **Input:** Sentence $\mathcal{X}$, Cue Pool $C$, Number of Subsets $T$, Number of Cues per Subset $q$, an LLM $\mathcal{L}_{\theta}$  
**Ensure:**  
2: **Output:** Sarcasm Label $Y$  
3: **Step 1: Cue Subsets Construction**  
4: **for** $t = 1$ **to** $T$ **do**  
5: &emsp;Randomly sample a subset $S_t = \{c_{t1}, c_{t2}, \ldots, c_{tq}\}$ from $C$  
6: **Step 2: LLM Prediction**  
7: **for** $t = 1$ **to** $T$ **do**  
8: &emsp;Generate sarcasm prediction $\hat{y}_t \sim \mathcal{L}_{\theta}^{BoC}(\hat{y}_t|S_t, \mathcal{X})$  
9: **Step 3: Prediction Aggregation**  
10: Aggregate predictions using majority voting:  
11: $Y \sim Vote(\{\hat{y}_1, \hat{y}_2, \ldots, \hat{y}_T\})$  
12: **return** $Y$

---

**Algorithm 4** Tensor of cues

**Require:**  
1: **Input:** Sentence $\mathcal{X}$, an LLM $\mathcal{L}_{\theta}$  
**Ensure:**  
2: **Output:** Sarcasm Label $\mathcal{Y}$  
3: **Step 1: Extract Cues**  
4: Obtain linguistic cue embeddings $\overrightarrow{Lin} = (e_1^l, e_2^l, \ldots, e_m^l)^T$, contextual cue embeddings $\overrightarrow{Con} = (e_1^c, e_2^c, \ldots, e_p^c)^T$, emotional cue embeddings $\overrightarrow{Emo} = (e_1^e, e_2^e, \ldots, e_s^e)^T$  
5: **Step 2: Construct Tensor Representation**  
6: Compute tensor product to combine cues: $\mathcal{Z} = \begin{bmatrix} \overrightarrow{Lin} \\ 1 \end{bmatrix} \otimes \begin{bmatrix} \overrightarrow{Con} \\ 1 \end{bmatrix} \otimes \begin{bmatrix} \overrightarrow{Emo} \\ 1 \end{bmatrix}$  
7: **Step 3: Sarcasm Detection**  
8: Take tensor $\mathcal{Z}$ as input to a LLM for sarcasm detection:  
9: $\mathcal{Y} \sim \mathcal{L}_{\theta}^{ToC}(\mathcal{Y}|\mathcal{Z}, \mathcal{X})$  
10: **return** $\mathcal{Y}$

---

discussions. It encompasses a balanced mixture of sarcastic and non-sarcastic comments.

**SemEval 2018 Task 3** is collected using irony-related hashtags (i.e. #irony, #sarcasm, #not) and are subsequently manually annotated to minimise the amount of noise in the corpuses. It emphasize the challenges inherent in identifying sarcasm within the constraints of Twitter’s concise format, and highlight the importance of context and linguistic subtleties in recognizing sarcasm.

**MUStARD** is compiled from popular TV shows including Friends, The Golden Girls, The Big Bang Theory, etc. It consists of 690 samples total of 3,000 utterances. Each sample is a conversation consisting of several utterances. In this work, we only use the textual information.

The statistics for each dataset are shown in Table 5.

**C C. Implementation Details**

We have implemented the prompting methods for **GPT-4o, Claude 3.5 Sonnet, LLaMA3-8B-Instruct** and **Qwen 2-7B**. The GPT-4o and Claude 3.5 Sonnet methods are implemented with the respective official Python API library: openAI[^6] and anthropic[^7], while the LLaMA and Qwen methods are implemented based on the Hugging Face Transformers library[^8]. All prompting strategies are implemented for **GPT-4o** and **Claude 3.5 Sonnet** except for ToC, which can solely be deployed on open-sourced LLMs. Following previous works in this field, LangChain[^9] is employed for the implementation of ToT and GoC. For the

[^6]: https://github.com/openai/openai-python  
[^7]: https://github.com/anthropics/anthropic-sdk-python  
[^8]: https://huggingface.co/docs/transformers  
[^9]: https://github.com/langchain-ai/langchain



<!-- page 0014 -->

Table 6: Few shot performance testing.

| LLMs | Method | K-shot | IAC-V1 | IAC-V2 | SemEval | MUStARD | Avg. of F1 |
|---|---|---|---:|---:|---:|---:|---:|
| GPT-4o | CoC | 0-shot | <u>71.52</u> | <u>72.31</u> | <u>70.60</u> | <u>68.48</u> | <u>70.73</u> |
|  |  | 1-shot | 58.91 | 61.99 | 63.69 | 60.98 | 61.39 |
|  |  | 5-shot | 60.65 | 66.00 | 65.39 | 63.60 | 63.91 |
|  |  | 10-shot | 63.34 | 70.29 | 67.59 | 63.40 | 66.16 |
|  | GoC | 0-shot | 62.91 | 61.30 | <u>74.02</u> | <u>69.91</u> | 67.04 |
|  |  | 1-shot | 66.00 | <u>66.70</u> | 73.00 | 64.12 | 67.45 |
|  |  | 5-shot | 66.93 | 65.88 | 73.41 | 67.77 | 68.50 |
|  |  | 10-shot | <u>74.38</u> | 66.36 | 69.34 | 68.61 | <u>69.67</u> |
|  | BoC | 0-shot | 67.36 | <u>69.39</u> | 61.85 | 68.45 | 66.76 |
|  |  | 1-shot | 64.67 | 66.36 | 61.08 | 73.47 | 66.40 |
|  |  | 5-shot | 65.66 | 67.52 | 64.06 | 73.97 | 67.80 |
|  |  | 10-shot | <u>70.70</u> | 69.06 | <u>68.12</u> | <u>76.51</u> | <u>71.10</u> |
| Claude 3.5 Sonnet | CoC | 0-shot | 69.40 | 73.17 | 82.23 | 74.16 | 74.74 |
|  |  | 1-shot | 72.45 | 74.38 | 77.29 | 72.75 | 74.22 |
|  |  | 5-shot | 71.99 | 78.12 | 79.42 | 75.65 | 76.30 |
|  |  | 10-shot | <u>75.49</u> | <u>79.07</u> | <u>83.46</u> | <u>79.56</u> | <u>79.40</u> |
|  | GoC | 0-shot | 70.93 | 74.18 | <u>76.91</u> | <u>69.85</u> | 72.97 |
|  |  | 1-shot | 65.16 | 69.29 | 74.98 | 65.40 | 68.71 |
|  |  | 5-shot | 69.01 | 72.76 | 75.62 | 67.12 | 71.13 |
|  |  | 10-shot | <u>72.80</u> | <u>74.71</u> | 76.65 | 68.36 | <u>73.13</u> |
|  | BoC | 0-shot | 66.40 | 72.82 | 70.07 | 71.93 | 70.31 |
|  |  | 1-shot | 74.63 | 81.09 | 76.64 | 75.38 | 76.94 |
|  |  | 5-shot | 78.40 | 84.34 | 79.72 | 82.83 | 81.32 |
|  |  | 10-shot | <u>80.27</u> | <u>84.82</u> | <u>82.76</u> | <u>85.76</u> | <u>83.40</u> |

training of ToC, cross-entropy loss between the output logit and the true label token is computed to update the weights of the fully-connected layers. The mean performance of each model over 5 runs is calculated.

Given the proprietary nature of GPT-4o and Claude 3.5 Sonnet, we have implemented only CoC, GoC and BoC prompting approaches. For Llama 3-8B and Qwen 2-7B, we implemented all four proposed prompting approaches. This is due to the reasons previously discussed: ToC requires access to and modification of the base model. We run all the models on four A100 GPUs.

## D D. Zero-shot v/s Few-shot Prompting

We perform zero-shot and few-shot experiments to evaluate whether the proposed SarcasmCue framework can perform better when a limited number of contextual examples are available. The results are shown in Table 6. We design four $k$-shot settings: zero-shot, one-shot, five-shot, ten-shot. For each setting, we randomly sample $k = \{0, 1, 5, 10\}$ examples from the training set.

The impact of adding shots varies with the number of shots. For example, CoC appears sensitive to the initial introduction of demonstration examples with a slight descent in performance when only 1 example is provided. However, as the number of shots increases to 5 and 10, the performance progressively improves. This trend underscores the effectiveness of CoC in adapting and refining its approach with more examples. In contrast, BoC demonstrates a consistent improvement in performance as the number of shots increases. Compared to CoC and BoC, GoC exhibits a relatively lower sensibility to the presence of demonstration examples, while still showing a slight but stable improvement with more shots.

Overall, these results demonstrate the robustness and adaptability of the SarcasmCue framework in zero-shot and few-shot scenarios. The framework can effectively utilize limited contextual examples to improve sarcasm detection, making it suitable for applications where large annotated datasets are not readily available. This adaptability underscores the practical value of SarcasmCue in real-world settings where training data may be scarce.

## E E. Influences of LLM scales

In an attempt to study the influence of different LLM scales, we evaluate the performance of sarcasm detection of Qwen and Llama of varying sizes. Table 7 presents the macro-F1 scores of each model across



<!-- page 0015 -->

Table 7: Influence of model scale. Macro-F1 score is measured on all four datasets, and the average Macro-F1 score is computed and shown in the last column.

| LLMs | Method | IAC-V1 | IAC-V2 | SemEval | MUSTARD | Avg. of F1 |
|---|---|---:|---:|---:|---:|---:|
| Qwen 2-1.5B | CoC | 48.05 | 44.43 | 44.05 | 50.66 | 46.80 |
|  | GoC | 43.75 | 53.21 | 50.69 | 45.63 | 48.32 |
|  | BoC | 43.84 | 42.86 | 42.87 | 52.41 | 45.49 |
|  | ToC | 57.46 | 57.60 | 60.69 | 54.40 | 57.53 |
| Qwen 2-7B | CoC | 45.77 | 38.90 | 36.37 | 44.26 | 41.33 |
|  | GoC | 47.35 | 42.25 | 38.17 | 47.49 | 43.82 |
|  | BoC | 43.78 | 40.24 | 45.63 | 46.11 | 43.94 |
|  | ToC | 71.56 | 71.76 | 68.77 | 61.46 | 68.39 |
| Qwen 2-72B | CoC | 61.33 | 59.42 | 44.92 | 51.63 | 54.33 |
|  | GoC | 57.67 | 68.78 | 65.28 | 61.87 | 63.40 |
|  | BoC | 45.24 | 43.38 | 44.18 | 48.10 | 45.23 |
| LlaMA 3-8B | CoC | 46.95 | 42.60 | 44.36 | 45.66 | 44.89 |
|  | GoC | 54.96 | 53.30 | 57.24 | 52.67 | 54.54 |
|  | BoC | 59.28 | 58.11 | 65.50 | 56.70 | 59.90 |
| LlaMA 3-70B | CoC | 68.94 | 77.29 | 62.59 | 59.73 | 67.14 |
|  | GoC | 56.83 | 62.57 | 58.66 | 53.81 | 57.97 |
|  | BoC | 65.49 | 68.52 | 55.14 | 45.72 | 58.72 |

[Figure: Multiple line charts showing the influence of model scale. Columns labeled CoC, GoC, BoC, ToC; rows labeled Qwen 2 and Llama 3. Legends include IAC-V1, IAC-V2, SemEval, MUSTARD, and Avg. of F1; x-axis model scales include Qwen 2-1.5B, Qwen 2-7B, Qwen 2-72B, LlaMA 3-8B, and LlaMA 3-70B.]

Figure 6: The influence of model scale.

the four sarcasm detection tasks.

The key take-aways are two-fold. First, with increasing model scale, the efficacy of our prompting is exponentially amplified. This aligns closely with the key findings of the CoT method (Wei et al., 2022). This is because when an LLM is sufficiently large, its capabilities for multi-hop reasoning are greatly developed and strengthened. More specifically:

(1) CoC demonstrates a significant improvement in performance as model scale increases. For Qwen models, the average F1 score rises from 46.80% (1.5B) to 54.33% (72B). LLaMA models show an even more pronounced enhancement, with the average F1 score jumping from 44.89% (8B) to 67.14% (70B). This indicates that CoC becomes more effective with larger model scales.

(2) GoC also exhibits a positive trend with increasing model size. In Qwen models, performance improves from 48.32% (1.5B) to 63.40% (72B) average F1 score. LLaMA models display a similar trend, with the average F1 score increasing from 54.54% (8B) to 57.97% (70B). These results suggest that GoC generally benefits from larger model scales across different architectures.

(3) BoC shows inconsistent performance across model scales. For Qwen models, performance remains relatively stable, with a slight decrease in the 72B model (45.23% average F1) compared to smaller versions. LLaMA models demonstrate a minor decline in performance, with the average F1 score



<!-- page 0016 -->

decreasing from 59.90% (8B) to 58.72% (70B). This suggests that BoC might be more effective with smaller model scales.

(4) ToC exhibits the most substantial improvement within the available data range. For Qwen models, the average F1 score increases dramatically from 57.53% (1.5B) to 68.39% (7B).

Overall, our proposed framework demonstrates high adaptability across different model scales by offering a range of methods. This adaptability allows for optimized performance based on available computational resources and specific task requirements

## F F. Case Study

We analyze the proposed four prompting approaches on several typical cases in Table 8. We categorize and analyze sarcasm detection methods. In scenarios involving straightforward statements (Examples 8, 15), all methods correctly identify texts as non-sarcastic, showcasing the SarcasmCue framework’s efficacy in clear-cut non-sarcastic contexts. For scenarios marked by clear linguistic contrasts (Examples 1, 6, 7), the CoC and GoC methods demonstrate superior performance. They effectively capture textual contradictions, making them ideally suited for texts where the apparent meaning sharply diverges from the intended message.

For texts involving complex contexts that necessitate an understanding of nuanced background knowledge (Examples 2, 3, 9, 10), the BoC and ToC methods prove more effective. BoC achieves this through sampling multiple subsets of cues, thus capturing the complexity of the context, whereas ToC employs a multi-view representation to process intricate high-order interactions.

In scenarios characterized by subtle sarcasm (Examples 5, 11)—where texts may lack overt sarcastic markers or structural clues—ToC outperforms other methods. It excels in capturing the intricate interaction among linguistic, contextual, and emotional cues. Additionally, for texts involving specialized domain knowledge (Examples 13, 14), both BoC and ToC are effective due to their ability to integrate and analyze domain-specific cues.

This analysis highlights that different sarcasm detection methods are tailored to specific textual scenarios. CoC and GoC are highly effective in environments with straightforward linguistic oppositions, where the sarcasm is direct and easily discernible. Conversely, BoC and ToC are particularly adept in scenarios that demand a deeper understanding of complex and subtle cues. ToC is especially notable for its performance across a broad range of scenarios, attributed to its capability to capture and analyze complex interactions among multiple layers of cues.

However, in highly ambiguous situations, a blend of methods or the addition of extra contextual information may be required. This insight directs future research towards identifying or combining the most appropriate methods for enhancing the overall accuracy of sarcasm detection across varied scenarios.



<!-- page 0017 -->

Table 8: Typical examples for case study.

| Example | Text | Golden | CoC | GoC | BoC | ToC |
|---|---|---|---|---|---|---|
| 1 | Now that is funny, the marie troll not knowing its a troll. | Sarcastic | ✔ | ✔ | ✔ | ✔ |
| 2 | You are aware that words have more than one meaning, right? And that every definition isn’t appropriate in every situation? The definition, from dictionary.com, that you should have used is: To infer or estimate by extending or projecting known information. | Sarcastic | ✘ | ✘ | ✔ | ✔ |
| 3 | Do you grasp the concept of “consentual”? consentual definition \| Dictionary.com | Sarcastic | ✘ | ✘ | ✘ | ✔ |
| 4 | No, this is the point of the 10th amendment. Article 1 Section 8 applies to Congress...the 10th amendment grants all powers not listed to the states or people. The 14th amendment is not the “federal government can do whatever” amendment. | Sarcastic | ✘ | ✘ | ✘ | ✘ |
| 5 | You make it seem as if you are doing me a favor by reading what I post | Sarcastic | ✔ | ✘ | ✔ | ✔ |
| 6 | Just out of interest, which particular aspect of “truth” are you getting at here? | Sarcastic | ✔ | ✔ | ✘ | ✔ |
| 7 | You forgot to mention that we would have to change our numbering system so that grasshoppers had 4 legs. | Sarcastic | ✔ | ✔ | ✔ | ✘ |
| 8 | Science is the current sum of human knowledge about how the world works. | Not Sarcastic | ✔ | ✔ | ✔ | ✔ |
| 9 | I think its actually the states job...the judiciary does need to overturn Roe v. Wade to get this done though...which doesn’t mean it becomes illegal. | Not Sarcastic | ✘ | ✔ | ✔ | ✔ |
| 10) | Mmmmm, not necessarily. Many of the arguments of against gods (those with specific properties, not just a general deity) deal with incompatible traits, like a square circle has. One does not have to search the universe to know square circles do not exist.People state simple negatives all the time. The lack of evidence for the positive makes them reasonable. | Not Sarcastic | ✘ | ✘ | ✔ | ✔ |
| 11 | Apples and oranges. We’re not demanding that they have abortions either. | Not Sarcastic | ✘ | ✘ | ✘ | ✔ |
| 12 | and how do you know this......oh I see...you said “I think”....but you don’t really “know” what most Americans favor or don’t favor...you just "think" | Not Sarcastic | ✘ | ✘ | ✘ | ✘ |
| 13 | Well, there certainly is here with these cats, because they’re not actually inheriting a trait; the symptoms are being independently induced in all the cats, parents and offspring, by denying them all particular nutrients. | Not Sarcastic | ✔ | ✘ | ✔ | ✔ |
| 14 | The human collective is the authority. One major advantage of this authority over a theistic one is that it actually exists. | Not Sarcastic | ✔ | ✔ | ✘ | ✔ |
| 15 | Did you read the article? A capuchin is type of monkey, in this case, the type that was used in the experiment. | Not Sarcastic | ✔ | ✔ | ✔ | ✘ |
