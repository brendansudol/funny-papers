<!-- Transcribed from x10-humicroedit.pdf -->



<!-- page 0001 -->

# SemEval-2020 Task 7: Assessing Humor in Edited News Headlines

**Nabil Hossain<sup>†</sup>, John Krumm<sup>‡</sup>, Michael Gamon<sup>‡</sup> and Henry Kautz<sup>†</sup>**

<sup>†</sup>Department of Computer Science, University of Rochester  
<sup>‡</sup>Microsoft Research AI, Microsoft Corporation, Redmond, WA  
`{nhossain,kautz}@cs.rochester.edu, {jckrumm,mgamon}@microsoft.com`

## Abstract

This paper describes the SemEval-2020 shared task “Assessing Humor in Edited News Headlines.” The task’s dataset contains news headlines in which short edits were applied to make them funny, and the funniness of these edited headlines was rated using crowdsourcing. This task includes two subtasks, the first of which is to estimate the funniness of headlines on a humor scale in the interval 0-3. The second subtask is to predict, for a pair of edited versions of the same original headline, which is the funnier version. To date, this task is the most popular shared computational humor task, attracting 48 teams for the first subtask and 31 teams for the second.

## 1 Introduction

Humor is an important ingredient of human communication, and every automatic system aiming at emulating human intelligence will eventually have to develop capabilities to recognize and generate humorous content. In the artificial intelligence community, research on humor has been progressing slowly but steadily. As an effort to boost research and spur new ideas in this challenging area, we created a competitive task for automatically assessing humor in edited news headlines.

[Figure: Two screenshots of annotation interfaces. Top screenshot shows ORIGINAL: “Eric Trump: Those Who Oppose My Dad Are ' Not Even People '”; EDITED: “Eric Trump: Those Who support My Dad Are ' Not Even People '”; Substitute: “support”. Bottom screenshot shows Orig: “EU says summit with Turkey provides no answers to concerns”; Edit: “EU says gravy with Turkey provides no answers to concerns”; rating options: 0 (Not Funny), 1 (Slightly Funny), 2 (Moderately Funny), 3 (Funny).]

(a) The Headline Editing Interface.

(b) The Headline Rating Interface.

Figure 1: The funny headline data annotation interfaces. When editing, only the underlined tokens are replaceable.

Like other AI tasks, automatic humor recognition depends on labeled data. Nearly all existing humor datasets are annotated to study the binary task of whether a piece of text is funny (Mihalcea and Strapparava, 2005; Kiddon and Brun, 2011; Bertero and Fung, 2016; Raz, 2012; Filatova, 2012; Zhang and Liu, 2014; Reyes et al., 2012; Barbieri and Saggion, 2014). Such categorical data does not capture the non-binary character of humor, which makes it difficult to develop models that can predict a level of funniness.

Humor occurs in various intensities, and certain jokes are much funnier than others, including the supposedly funniest joke in the world (Wiseman, 2011). A system’s ability to assess the degree of humor makes it useful in various applications, such as in humor generation where such a system can be used in a generate-and-test scheme to generate many potentially humorous texts and rank them by funniness, for example, to automatically fill in the blanks in Mad Libs® for humorous effects (Hossain et al., 2017; Garimella et al., 2020).

For our SemEval task, we provided a dataset that contains news headlines with short edits applied to them to make them humorous (see Table 1). This dataset was annotated as described in Hossain et al. (2019) using Amazon Mechanical Turk, where *qualified* human workers edited headlines to make them funny and the quality of humor in these headlines was assessed by a separate set of *qualified* human judges on a 0-3 funniness scale (see Figure 1). This method of quantifying humor enables the development of systems for automatically estimating the degree of humor in text. Our task is comprised of two Subtasks:

---

This work is licensed under a Creative Commons Attribution 4.0 International License. License details: http://  
creativecommons.org/licenses/by/4.0/.



<!-- page 0002 -->

| ID | Original Headline (replaced word in **bold**) | Substitute | Rating | Est. | Err. |
|---|---|---|---:|---:|---:|
| R1 | CNN ’s Jake Tapper to **interview** Paul Ryan following retirement announcement | wrestle | 2.8 | 1.17 | -1.63 |
| R2 | 4 arrested in Sydney raids to stop terrorist **attack** | kangaroo | 2.6 | 1.06 | -1.54 |
| R3 | Man Sets Off Explosive Device at L.A.-Area Cheesecake Factory, no **Injuries** | complaints | 2.4 | 0.80 | -1.60 |
| R4 | 5 dead, 9 injured in **shooting** at Fort Lauderdale Airport | delay | 1.2 | 0.49 | -0.71 |
| R5 | Congress Struggles to **Confront** Sexual Harassment as Stories Pile Up | increase | 1.2 | 0.66 | -0.54 |
| R6 | Congress Achieves the Impossible on **Tax** Reform | toilet | 0.8 | 1.35 | +0.55 |
| R7 | Overdoses now leading **cause** of death of Americans under 50 | sign | 0.0 | 0.52 | +0.52 |
| R8 | Noor Salman, widow of Orlando massacre **shooter** Omar Mateen, arrested | columnist | 0.0 | 0.43 | +0.43 |

Table 1: Edited headlines from our dataset and their funniness rating. We report the mean of the estimated ratings from the top 20 ranked participating systems (Est.) and its difference from the true rating (Err.).

- Subtask 1: Estimate the funniness of an edited headline on a 0-3 humor scale.
- Subtask 2: Given two edited versions of the same headline, determine which one is funnier.

Inviting multiple participants to a shared task contrasts with most current work on computational humor, which consists of standalone projects, each exploring a different genre or type of humor. Such projects typically involve gathering new humor data and applying machine learning to solve a particular problem. Repeated attempts at the same problem are rare, hindering incremental progress, which emphasizes the need for unified, shared humor tasks.

Recently, competitive humor tasks including shared data have been posed to the research community. One example is #HashtagWars (Potash et al., 2017), a SemEval task from 2017 that attracted eight distinct teams, where the focus was on ranking the funniness of tweets from a television show. The HAHA competition (Chiruzzo et al., 2019) had 18 participants who detected and rated humor in Spanish language tweets. There were 10 entries in a SemEval task from 2017 that looked at the automatic detection, location, and interpretation of puns (Miller et al., 2017). Finally, a related SemEval 2018 task involved irony detection in tweets (Van Hee et al., 2018).

Ours is the largest shared humor task to date in terms of participation. More than 300 participants signed up, 86 teams participated in the development phase, and 48 and 31 teams participated, respectively, in the two subtasks in the evaluation phase. By creating an intense focus on the same humor task from so many points of view, we were able to clearly understand how well these systems work as a function of different dimensions of humor, including which type of humor appears easiest to rate automatically.

## 2 Datasets

The data[^1] for this task[^2] is the **Humicroedit** dataset described in our previous work (Hossain et al., 2019). This dataset contains about 5,000 original headlines, each having three modified, potentially funny versions for a total of 15,095 edited headlines. The original headlines were collected from Reddit (`reddit.com`) via the popular subreddits `r/worldnews` and `r/politics`, where headlines from professional news sources are posted everyday. These headlines were published between 01/2017 and 05/2018, they are between 4-20 words long, and they are sampled from headlines written by 25 major English news sources.

The data was annotated using workers from Amazon Mechanical Turk, who were screened using a qualification phase to find expert headline editors and judges of humor. The editors were instructed to make a headline as funny as possible to a generic wide audience by applying a **micro-edit**, which is a replacement of a verb/noun/entity in the headline with a single word. Examples are shown in Table 1. By allowing only small edits, researchers can examine humor at the atomic level where the constrained degrees of freedom are likely to simplify analysis, understanding, and eventually generation.

Five judges were asked to rate the funniness of each edited headline using the following humor scale:

0 - Not funny&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 - Slightly funny&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 - Moderately funny&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 - Funny

The funniness of an edited headline is the mean of the ratings from its five judges. For further details and analysis of the dataset, we refer the reader to Hossain et al. (2019).

[^1]: Task dataset: `https://zenodo.org/record/3969509#.XyWh6fhKh24`
[^2]: Task competition page: `https://competitions.codalab.org/competitions/20970`



<!-- page 0003 -->

| Task | Type | Metric | Train | FunLines (Train) | Dev | Test |
|---|---|---|---:|---:|---:|---:|
| Subtask 1 | Regression | RMSE | 9,653 | 8,248 | 2,420 | 3,025 |
| Subtask 2 | Classification | Accuracy | 9,382 | 1,959 | 2,356 | 2,961 |

Table 2: Summary of the subtasks and their datasets.

For our task, we randomly sampled the Humicroedit dataset into train (64%), dev (16%) and test (20%) sets such that all edited versions of an original headline reside in exactly one of these sets, as opposed to the sampling in Hossain et al. (2019) which allowed overlap of original versions of headlines among its dataset partitions for a slightly different humorous headline classification task.

We also provided additional training data[^3] from **FunLines**[^4] (Hossain et al., 2020), a competition that we hosted to collect humorous headlines at a very low cost. The data collection approach for Humicroedit and FunLines are mostly similar, but FunLines additionally includes headlines from the news categories sports, entertainment and technology, and its headlines were published between 05/2019 and 01/2020, for a total of 8,248 annotated headlines. More than 40% of the participating teams, including the winning team, made use of the FunLines data.

## 3 Task Description

The objective of this shared task is to build systems for rating a humorous effect that is caused by small changes in text. To this end, we focus on humor obtained by applying micro-edits to news headlines.

Editing headlines presents a unique opportunity for humor research since headlines convey substantial information using only a few words. This creates a rich background against which a micro-edit can lead to a humorous effect. With that data, a computational humor model can focus on the exact localized cause of the humorous effect in a short textual context.

We split our task into two subtasks. The dataset statistics for these subtasks are shown in Table 2.

### 3.1 Subtask 1: Funniness Regression

In this task, given the original and the edited versions of a headline, the participant has to estimate the mean funniness of the edited headline on the 0-3 humor scale. Systems tackling this task can be useful in a humor generation scenario where generated candidates are ranked according to expected funniness.

### 3.2 Subtask 2: Funnier of the Two

In this task, given the original headline and two of its edited versions, the participating system has to predict which edited version is the funnier of the two. Consequently, by looking at gaps between the funniness ratings, we can begin to understand the minimal discernible difference between funny headlines.

## 4 Evaluation

### 4.1 Metrics

For Subtask 1, systems are ranked using the root mean squared error (RMSE) between the mean of the five annotators’ funniness ratings and the rating estimated by the system for the headlines. Given $N$ test samples, and given the ground truth funniness $y_i$ and the predicted funniness $\hat{y}_i$ for the $i$-th sample:

$$
RMSE = \sqrt{\frac{\sum_{i=1}^{N}(y_i - \hat{y}_i)^2}{N}}
$$

For Subtask 2, which attempts to find the funnier of the two modified versions of a headline, the evaluation metric is classification accuracy. We also report another auxiliary metric called the reward. Given $N$ test samples with $C$ correct predictions, and given the $i$-th sample, the funniness ratings of its two edited headlines $f_i^{(1)}$ and $f_i^{(2)}$, its ground truth label $y_i$ and its predicted label $\hat{y}_i$:

[^3]: FunLines dataset: `https://cs.rochester.edu/u/nhossain/funlines.html`  
[^4]: FunLines game website: `https://funlines.co`



<!-- page 0004 -->

$$
Accuracy = \frac{C}{N} \qquad Reward = \frac{1}{N}\sum_{i=1}^{N}(1_{\hat{y}_i=y_i} - 1_{\hat{y}_i \ne y_i})|f_i^{(1)} - f_i^{(2)}|
$$

In other words, for a larger funniness difference between the two edited headlines in a pair, the reward (or penalty) is higher for a correct classification (or misclassification). We ignore cases where the two edited versions of a headline have the same ground truth funniness.

### 4.2 Benchmarks

We provide several benchmarks in Table 3 to compare against participating systems:

1. BASELINE: assigns the mean rating (Subtask 1) or the majority label (Subtask 2) from the training set.

2. CBOW: the context independent word representations obtained using the pretrained GloVe word vectors with 300d embeddings and a dictionary of 2.2M words.

3. BERT: a regressor based on BERT base model embeddings (Devlin et al., 2019).

4. RoBERTa: same regressor as above but uses RoBERTa embeddings (Liu et al., 2019).

For a thorough discussion of these benchmarks, we refer the reader to the Duluth system (Jin et al., 2020), who performed these ablation experiments. In summary, each benchmark result uses the edited headline, CONTEXT implies using the headline’s context (with the replaced word substituted with `[MASK]`), ORIG implies using the original headline, FT refers to finetuning, FREEZE implies feature extraction (no finetuning) and FUNLINES refers to using the FunLines training data.

The results for Subtask 2 were obtained by using the model trained for Subtask 1 to assign funniness ratings to both the edited versions of a headline and then choosing the version scoring higher.

| Model | Subtask 1<br>RMSE | Subtask 2<br>Acc. | Reward |
|---|---:|---:|---:|
| BASELINE | 0.575 | 0.490 | 0.020 |
| CBOW |  |  |  |
| &nbsp;&nbsp;with CONTEXT+FREEZE | **0.542** | 0.599 | 0.184 |
| &nbsp;&nbsp;+ORIG | 0.559 | 0.599 | 0.169 |
| &nbsp;&nbsp;+FUNLINES | 0.544 | 0.605 | **0.191** |
| &nbsp;&nbsp;+ORIG+FUNLINES | 0.558 | 0.601 | 0.173 |
| &nbsp;&nbsp;+FT | 0.544 | 0.604 | 0.178 |
| &nbsp;&nbsp;+FT+ORIG | 0.561 | 0.592 | 0.165 |
| &nbsp;&nbsp;+FT+FUNLINES | 0.548 | **0.606** | 0.188 |
| &nbsp;&nbsp;+FT+ORIG+FUNLINES | 0.563 | 0.589 | 0.161 |
| BERT |  |  |  |
| &nbsp;&nbsp;with CONTEXT+FREEZE | 0.531 | 0.616 | 0.207 |
| &nbsp;&nbsp;+ORIG | 0.534 | 0.603 | 0.186 |
| &nbsp;&nbsp;+FUNLINES | **0.530** | 0.615 | 0.207 |
| &nbsp;&nbsp;+ORIG+FUNLINES | 0.541 | 0.615 | 0.204 |
| &nbsp;&nbsp;+FT | 0.536 | **0.635** | 0.234 |
| &nbsp;&nbsp;+FT+ORIG | 0.536 | 0.628 | 0.231 |
| &nbsp;&nbsp;+FT+FUNLINES | 0.541 | 0.630 | 0.232 |
| &nbsp;&nbsp;+FT+ORIG+FUNLINES | 0.533 | 0.629 | **0.236** |
| RoBERTa |  |  |  |
| &nbsp;&nbsp;with CONTEXT+FREEZE | 0.528 | 0.635 | 0.246 |
| &nbsp;&nbsp;+ORIG | 0.536 | 0.625 | 0.224 |
| &nbsp;&nbsp;+FUNLINES | 0.528 | 0.640 | 0.252 |
| &nbsp;&nbsp;+ORIG+FUNLINES | 0.533 | 0.618 | 0.207 |
| &nbsp;&nbsp;+FT | 0.534 | 0.649 | **<u>0.254</u>** |
| &nbsp;&nbsp;+FT+ORIG | 0.527 | **<u>0.650</u>** | **<u>0.254</u>** |
| &nbsp;&nbsp;+FT+FUNLINES | 0.526 | 0.638 | 0.233 |
| &nbsp;&nbsp;+FT+ORIG+FUNLINES | **<u>0.522</u>** | 0.626 | 0.216 |

Table 3: Benchmarks on the test set. The best within each model type is **bolded**, and the overall best is <u>underlined</u>.

### 4.3 Results

The official results for Subtasks 1 and 2 are shown, respectively, in Tables 4 and 5, including the performance of the benchmarks. There were 48 participants for Subtask 1, while Subtask 2 attracted 31 participants. For both subtasks, the best performing system was Hitachi, achieving an RMSE of 0.49725 (a 13.5% improvement over BASELINE) for Subtask 1, and an accuracy of 67.43% (a 17.93 increase in percentage points over BASELINE) for Subtask 2.

## 5 Overview of Participating Systems

The dominant teams made use of pre-trained language models (PLM), namely BERT, RoBERTa, ELMo (Peters et al., 2018), GPT-2 (Radford et al., 2019) and XLNet (Yang et al., 2019). Context-independent word embeddings, such as Word2Vec (Mikolov et al., 2013), FastText (Joulin et al., 2017) and GloVe word vectors (Pennington et al., 2014), were also useful. The winning teams combined the predictions of several hyperparameter-tuned versions of these models using regression in an ensemble learner to arrive at the final prediction. Next, we summarize the top systems and other notable approaches.



<!-- page 0005 -->

### 5.1 Reuse of SubTask 1 System for Subtask 2

First, we note that for Subtask 2, most systems relied on the model they developed for Subtask 1. This involved using the model to estimate a real number funniness rating for each of the two edited headlines, and selecting the one which achieved the higher estimated rating. As a result, there was a strong correlation between teams’ placements in Subtask 1 and Subtask 2, with the top 3 teams in both tasks being the same.

### 5.2 The Hitachi System

The winner of both tasks, Hitachi (Morishita et al., 2020), formulated the problem as sentence pair regression and exploited an ensemble of the PLMs BERT, GPT-2, RoBERTa, XLNet, Transformer-XL and XLM. Their training data uses the pairs of headlines, with the replacement word marked with special tokens, and they fine-tune 50 instances per PLM, each having a unique hyperparameter setting. After applying 5-fold cross validation, they selected the 20 best performing settings per PLM, for a total of 700 PLMs (7 PLMs × 20 hyperparameters × 5 folds). They combined the predictions of these models via Ridge regression in the ensemble to predict final funniness scores. Hitachi uses the additional training data from FunLines.

### 5.3 The Amobee System

Amobee (Rozental et al., 2020) was the 2nd placed team for both Subtasks. Using PLM token embeddings, they trained 30 instances of BERT, RoBERTa and XLNet, combining them for an ensemble of 90 models.

### 5.4 The YNU-HPCC System

Unlike the top two systems, the 3rd placed YNU-HPCC (Tomasulo et al., 2020) employed an ensemble method that uses *only* the edited headlines. They used multiple pre-processing methods (e.g., cased vs uncased, with or without punctuation), and they encoded the edited headlines using FastText, Word2Vec, ELMo and BERT encoders. The final ensemble consists of 11 different encodings (four FastText, two W2V, four Bert, one ELMo). For each of these encodings, a bidirectional GRU was trained using the encoded vectors. In the ensemble, the GRU predictions were concatenated and fed to an XGBoost regressor.

#### 5.4.1 MLEngineer

The MLEngineer (Shatnawi et al., 2020) team also used only the edited headlines. They fine-tune and combine four BERT sentence regression models to estimate a rating, and they combine it with the estimated rating from a model that incorporates RoBERTA embeddings and a Naïve Bayes regressor to generate the final rating.

| Rank | Team | RMSE |
|---:|---|---:|
| 1 | Hitachi | 0.49725 |
| 2 | Amobee | 0.50726 |
| 3 | YNU-HPCC | 0.51737 |
| 4 | MLEngineer | 0.51966 |
| 5 | LMML | 0.52027 |
| 6 | ECNU | 0.52187 |
| **bench.** | **RoBERTa** | **0.52207** |
| 7 | LT3 | 0.52532 |
| 8 | WMD | 0.52603 |
| 9 | Ferryman | 0.52776 |
| 10 | zxchen | 0.52886 |
| **bench.** | **BERT** | **0.53036** |
| 11 | Duluth | 0.53108 |
| 12 | will_go | 0.53228 |
| 13 | XSYSIGMA | 0.53308 |
| 14 | LRG | 0.53318 |
| 15 | MeisterMorxrc | 0.53383 |
| 16 | JUST-Farah | 0.53396 |
| 17 | Lunex | 0.53518 |
| 18 | UniTuebingenCL | 0.53954 |
| **bench.** | **CBOW** | **0.54242** |
| 19 | IRLab_DAIICT | 0.54670 |
| 20 | O698 | 0.54754 |
| 21 | UPB | 0.54803 |
| 22 | Buhscitu | 0.55115 |
| 23 | Fermi | 0.55226 |
| 24 | INGEOTEC | 0.55391 |
| 25 | JokeMeter | 0.55791 |
| 26 | testing | 0.55838 |
| 27 | HumorAAC | 0.56454 |
| 28 | ELMo-NB | 0.56829 |
| 29 | prateekgupta2533 | 0.56983 |
| 30 | funny3 | 0.57237 |
| 31 | WUY | 0.57369 |
| 32 | XTHL | 0.57470 |
| **bench.** | **BASELINE** | **0.57471** |
| 33 | HWMT_Squad | 0.57471 |
| 34 | moonalasad | 0.57479 |
| 35 | dianenhu | 0.57488 |
| 36 | Warren | 0.57527 |
| 37 | tangmen | 0.57768 |
| 38 | Lijunyi | 0.57946 |
| 39 | Titowak | 0.58157 |
| 40 | xenia | 0.58286 |
| 41 | Smash | 0.59202 |
| 42 | KdeHumor | 0.61643 |
| 43 | uir | 0.62401 |
| 44 | SO | 0.65099 |
| 45 | heidy | 0.68338 |
| 46 | Hasyarasa | 0.70333 |
| 47 | frietz58 | 0.72252 |
| 48 | SSN_NLP | 0.84476 |

Table 4: Official results and benchmarks for Subtask 1.

### 5.5 The LMML and ECNU Systems

These systems (Ballapuram, 2020; Zhang et al., 2020) estimate the funniness of headlines using a neural architecture that focuses on the importance of the replaced and replacement words against the contextual



<!-- page 0006 -->

words in the headline. They use BERT embeddings and compute feature vectors based on the global attention between contextual words and the replaced (and replacement) word. These two vectors and the vectors of the replaced and replacement are combined, and the resulting vector is passed through a multi-layer perceptron to estimate the headline’s funniness.

### 5.6 Other Notable Approaches

ECNU used sentiment and humor lexicons, respectively, to extract polarities and humor rating features of headlines. They also used the average, minimum and maximum humor ratings of replaced/replacement words from the training set as additional features.

LT3 (Vanroy et al., 2020) created an entirely feature-engineered baseline which obtained an RMSE of 0.572. It uses lexical, entity, readability, length, positional, word embedding similarity, perplexity and string similarity features.

IRLab_DAIICT trained five BERT classifiers, one for each of the five ratings for a headline, and calculated the mean of the five classifiers’ outputs. This mean was further averaged with the output of a BERT regression model which predicts the overall mean rating.

Buhscitu (Jensen et al., 2020) used knowledge bases (e.g. WordNet), a language model and hand-crafted features (e.g. phoneme level distances). Their neural model combines feature, knowledge and word (replaced/replacement) encoders.

Hasyarasa (Desetty et al., 2020) used a word embedding and knowledge graph based approach to build a contextual neighborhood of words to exploit entity interrelationships and to capture contextual absurdity. Features from this and semantic distance based features are finally combined with headline representations from a Bi-LSTM.

UTFPR (Paetzold, 2020) is a minimalist unsupervised approach that uses word co-occurrence features derived from news and EU parliament transcripts to capture unexpectedness.

| Rank | Team | Accuracy | Reward |
|---:|---|---:|---:|
| 1 | Hitachi | 0.6743 | 0.2988 |
| 2 | Amobee | 0.6606 | 0.2766 |
| 3 | YNU-HPCC | 0.6591 | 0.2783 |
| **bench.** | **RoBERTa** | **0.6495** | **0.2541** |
| 4 | LML | 0.6469 | 0.2601 |
| 5 | XSYSIGMA | 0.6446 | 0.2541 |
| 6 | ECNU | 0.6438 | 0.2508 |
| 7 | Fermi | 0.6393 | 0.2438 |
| **bench.** | **BERT** | **0.6355** | **0.2345** |
| 8 | zcxchen | 0.6347 | 0.2399 |
| 9 | Duluth | 0.6320 | 0.2429 |
| 10 | WMD | 0.6294 | 0.2291 |
| 11 | Buhscitu | 0.6271 | 0.2190 |
| 12 | MLEngineer | 0.6229 | 0.2046 |
| 13 | LRG | 0.6218 | 0.2077 |
| 14 | UniTuebingenCL | 0.6183 | 0.2110 |
| 15 | O698 | 0.6134 | 0.1954 |
| 16 | JUST_Farah | 0.6088 | 0.1841 |
| **bench.** | **CBOW** | **0.6057** | **0.1878** |
| 17 | INGEOTEC | 0.6050 | 0.1779 |
| 18 | Ferryman | 0.6027 | 0.1771 |
| 19 | UPB | 0.6001 | 0.1772 |
| 20 | Hasyarasa | 0.5970 | 0.1673 |
| 21 | JokeMeter | 0.5776 | 0.1487 |
| 22 | UTFPR | 0.5696 | 0.1181 |
| 23 | Smash | 0.5426 | 0.0747 |
| 24 | SSN_NLP | 0.5377 | 0.0622 |
| 25 | WUY | 0.5320 | 0.1113 |
| 26 | uir | 0.5213 | 0.0567 |
| 27 | KdeHumor | 0.5190 | 0.0272 |
| 28 | Titowak | 0.5038 | -0.0021 |
| **bench.** | **BASELINE** | **0.4950** | **-0.0196** |
| 29 | heidy | 0.4197 | -0.0995 |
| 30 | SO | 0.3291 | -0.2064 |
| 31 | HumorAAC | 0.3204 | -0.2177 |

Table 5: Official results and benchmarks for Subtask 2.

Some noteworthy pre-processing techniques included non-word symbol removal, word segmentation, manually removing common text extensions in headlines (e.g. “– live updates”). Finally, notable datasets used were the iWeb corpus[^5] and a news headline corpus[^6].

### 5.7 General Trends

Here we discuss the relative merits of the different systems, with respect to the participants’ findings.

Table 3 suggests that contextual information is useful in our humor recognition tasks, since the context independent GloVe embeddings (CBOW) led to weaker performance compared to using the context-sensitive BERT and RoBERTa embeddings.

According to ablation experiments by Hitachi (Morishita et al., 2020), the ranking of best performing to least superior individual PLM are as follows: RoBERTa, GPT-2, BERT, XLM, XLNet and Transformer-XL.

[^5]: https://www.english-corpora.org/iweb/  
[^6]: https://www.kaggle.com/snapcrack/all-the-news



<!-- page 0007 -->

Analysis performed by several task participants indicates that the neural embeddings were unable to recognize humor where a rich set of common sense and/or background knowledge is required, for example, in the case of irony.

Lastly, a few systems had quite low accuracy for Subtask 2. They reported having bugs that caused them to submit a random baseline, which has about a 33% chance of success (since the possible predictions were “headline 1 is funnier”, “headline 2 is funnier” and “both headlines have equal funniness”).

## 6 Analysis and Discussion

The outputs of 48 participating systems for Subtask 1 and 31 for Subtask 2 present an opportunity to not only study individual solutions and numeric results, but to also take a deeper qualitative look at the output of these systems. Here, we collectively analyze the performance of the top 20 systems per subtask to find aggregate trends that characterize the general approaches and the challenges of assessing humor itself.

### 6.1 Subtask 1 (Regression)

To better understand which funniness ranges are particularly hard for systems to assess, we study the performance of the systems as a function of ground truth funniness. As shown in Figure 2, we grouped the edited headlines into funniness bins of width 0.2. For each bin, we plotted the mean absolute regression errors for the top 20 systems aggregated (max RMSE = 0.547), the winning Hitachi system (RMSE = 0.497), the 19 other systems and BASELINE (RMSE = 0.575).

[Figure: Line chart showing mean absolute regression error by mean funniness bin, with curves labeled Headline Frequency, Aggregate, Hitachi, others, and BASELINE. Axes labeled Mean Absolute Regression Error, Mean Funniness, and Normalized Headline Frequency.]

Figure 2: Mean absolute error per funniness bin of width 0.2 for the top 20 systems aggregated, the best system (Hitachi), the 19 other systems and BASELINE for Subtask 1. The blue curve shows the normalized headline frequency for each funniness bin.

In general, all these systems have their minimum error at a funniness score of about 1.0. While the Hitachi system stands out somewhat in its superior performance at the two extremes of the funniness scale, the other systems follow generally the same pattern, and none appear to be outliers. Assessing more extreme humor (or lack thereof) appears to be harder since all the systems have larger errors toward the extremes of the funniness scale. This may also be due to the non-uniform distribution of ground truth funniness scores in the dataset (shown as the blue curve), with the extreme values being less frequent.

#### 6.1.1 Antipodal RMSEs

Figure 3 shows the systems’ antipodal RMSE, an auxiliary metric for Subtask 1, which we calculated by considering only the $X\%$ most funny headlines and $X\%$ least funny headlines, for $X \in \{10, 20, 30, 40\}$ in the RMSE metric. The systems are ranked by their overall RMSE for Subtask 1. It appears that some of the systems further down the ranking are doing much better at estimating the funniness of the extremes in the dataset than their superiors. For example, the large dip shows the system ranked 41 (Hahackathon) is performing better at estimating the funniness of the top 10-40% most/least funny headlines than several systems ranked before it. This suggests that

[Figure: Line chart of overall and antipodal RMSE by system rank for Subtask 1, with curves labeled RMSE@10, RMSE@20, RMSE@30, RMSE@40, RMSE, and BASELINE. Axes labeled RMSE and System Rank for Subtask 1.]

Figure 3: Overall and antipodal RMSE of the ranked participating systems and BASELINE for Subtask 1.



<!-- page 0008 -->

combining these approaches can yield better results, for example, using some selected systems to rank certain subsets of headlines.

### 6.1.2 Systematic Estimation Errors

We now analyze headlines for which the ratings from the top 20 systems were *all* either underestimates or overestimates. Table 1 shows examples of these headlines, their ground truth funniness rating, the mean of the estimated ratings of the top 20 systems and its difference from the ground truth.

Lack of understanding of world knowledge (Headline R1), cultural references (R2) and sarcasm (R3, R4 and R5) are clearly hurting these systems. The models are having difficulty recognizing the effects of negative sentiments on humor (R7 and R8) and the complex boundaries between negative sentiment and sarcastic humor (R4 and R8 both discuss death but R4 does it in a funny way). A better understanding of common sense could have helped resolve these subtleties. R3 also has the humorous effect brought about by a tension relief, which is a complex phenomenon to model. Finally, the systems are not expected to infer that bathroom humor (R6) was purposely annotated as “not funny” in the data (Hossain et al., 2019).

## 6.2 Subtask 2 (Classification)

Here we examine the top 20 aggregate system performances on Subtask 2. These 20 systems have at least 59.7% classification accuracy, much higher than the 49.5% accuracy of BASELINE.

First, we analyze the difficulty of the classification by calculating the percentage of headline pairs correctly classified by exactly $N$ systems, for $0 \leq N \leq 20$, as shown in the blue curve in Figure 4(a). As an example, there is a subset of about 3% of the headline pairs that were correctly classified by 10 of the top 20 systems. The curve rises rapidly to the right, indicating that a large fraction of the pairs can be correctly classified by 16 or more systems.

### 6.2.1 Incongruity at Play

We investigate to what extent the participating systems model incongruity as a cause of humor, as postulated in the incongruity theory of humor (Morreall, 2016). This theory claims that jokes set up an expectation that they violate later, triggering surprise and thereby generating humor. We test this hypothesis by examining the cosine distances between the GloVe vectors of the original word and each replacement word. We assume that the larger this distance is, the higher is the expected incongruity.

The dashed curve in Figure 4(a) shows the **incongruity measure** obtained using GloVe word distances:

$$
\boxed{
\begin{aligned}
\text{incongruity difference} &= \texttt{distance(orig, edit}_2\texttt{)} - \texttt{distance(orig, edit}_1\texttt{)} \\
\text{incongruity measure} &= \texttt{correlation}(\text{incongruity difference, ground truth label} \in \{1,2\})
\end{aligned}
}
$$

This rising curve implies that the funnier headline in a pair is recognized by more systems if its replacement word is more distant from the original word compared to the distance between the original word and the less funny headline’s replacement word. This indicates that these systems are possibly detecting which headline in the pair is more incongruous compared to the original headline. Moreover, for the headline

[Figure: Two line charts. Left chart legend: “aggregate classification” and “incongruity measure”; x-axis: “Number of top 20 systems correctly classifying a headline pair”; left y-axis: “% of correctly classified headline pairs”; right y-axis: “correlation between label and dist(orig,edit2) - dist(orig,edit1)”. Right chart x-axis: “Number of participating systems correctly classifying a headline pair”; y-axis: “Mean of absolute rating difference between the two headlines”.]

(a) Classification vs. incongruity.

(b) Funniness gaps vs. classification.

Figure 4: Aggregate top 20 system classification performance for Subtask 2.



<!-- page 0009 -->

| **ID** | **Original Headline** (replaced word in **bold**) | **Substitute** | **Rating** | **Dist.** |
|---|---|---|---:|---:|
| C1 | Secret **Service** likely wouldn’t have intervened in Trump Jr.-Russia meeting | police | 0.0 | 0.72 |
| ✔ | Secret **Service** likely wouldn’t have intervened in Trump Jr.-Russia meeting | Santa | 2.6 | 0.85 |
| C2 | Amazon, Facebook and Google could save **billions** thanks to the GOP tax bill | puppies | 1.0 | 0.89 |
| ✖ | Amazon, Facebook and Google could save **billions** thanks to the GOP tax bill | pennies | 2.2 | 0.54 |
| C3 | LA Times editorial board condemns Donald Trump **presidency** as ’trainwreck’ | diet | 1.2 | 0.96 |
| ✔ | LA Times editorial board **condemns** Donald Trump presidency as ’trainwreck’ | celebrates | 1.0 | 0.69 |
| C4 | US officials drop **mining** cleanup rule after industry objects | floor | 1.4 | 0.86 |
| ✖ | US officials drop **mining** cleanup rule after industry objects | Bedroom | 1.2 | 1.01 |

Table 6: Examples from Subtask 2 where the top 20 systems collectively either failed (✖) or succeeded (✔) in recognizing the funnier headline. On the overall dataset, these were the extreme headline pairs, having either the largest or the smallest differences in funniness between their headlines. We also report the GloVe word vector distances, mapped to the range 0-2, between the replaced and replacement words.

pairs which were incorrectly classified by all systems, the incongruity measure is around -0.6, implying that in these headline pairs, the less incongruous (*i.e.*, more coherent) version is the funnier of the two. This further indicates that these systems are mostly recognizing incongruity and they tend to fail where incongruity is not the cause of humor.

### 6.2.2 Funniness Gaps

Next, we inspect whether the funniness difference between the two headlines in a pair affects classification accuracy. We calculate the mean absolute funniness difference between the headline pairs within each of the $N$ bins of systems that correctly classified them, as shown in Figure 4(b). For example, the funniness difference between the two headlines in the pairs, which were correctly classified by all 20 systems, was around 0.8 on average. The rising trend in the curve suggests that, in general, more systems are able to correctly classify headline pairs having larger differences in humor. This helps confirm the annotation quality in the dataset, showing that humans and machines both agree on the intensity of humor in the dataset, and both can distinguish between slight humor and extreme humor.

Recall also from Section 5.1 that most of the systems for Subtask 2 were simply applying the systems from Subtask 1 to find the funnier of the two headlines by comparing their funniness scores. Pairs with widely different funniness would less likely have overlapping uncertainty, leading to more accurate pairwise rankings.

### 6.2.3 Extreme Examples

We discuss the collective top 20 system performance on edge case examples, with references to Table 6:

- **C1:** Among all the test examples which were *correctly* classified by the 20 systems, C1 has the largest funniness difference between its pair of headlines. “Secret service” and “secret police” are quite natural in text and substituting one with the other barely changes the headline’s meaning. However, using “secret santa” clearly raises the surprise. All classifiers were able to assess this relatively easy example.
- **C2:** This is the example with the largest funniness difference which all 20 systems *incorrectly* classified. This could be because “puppies” is semantically more distant from “billions” than “pennies” (according to GloVe). Although both headline substitutions are funny and incongruous, the antonym effect of the “pennies” version triggers a further sarcastic humor, since “pennies” is numerically much less than the original word “billions”, but still in the category of money. Lacking world knowledge of this numerical difference, the systems award the more incongruous “puppies” the higher ranking. As mentioned in 6.2.1, these systems are especially sensitive to general incongruity as a source of humor and they are likely less aware of other causes of humor, such as meaning reversal.
- **C3:** This example has the smallest funniness difference of the sentences that were correctly classified by all 20 systems. Its less funny headline is sarcastic and most likely all classifiers were unable to recognize sarcasm and thus correctly chose the other headline as the funnier. If this is true, then ignorance about sarcasm was a lucky benefit in this case.



<!-- page 0010 -->

- **C4:** This was one of the examples with the smallest funniness differences which was misclassified by all systems. Both its headlines are quite funny and they are similar as they both discuss cleaning spaces. However, all systems found bedroom cleaning as a funnier reference than floor cleaning, likely because floor cleaning occurs much more frequently in our day-to-day conversations, making bedroom cleaning a more incongruous substitution to the classifiers, as indicated by the semantic distances in Table 6.

## 6.3 Quirks of the Dataset

It is challenging to effectively construct a dataset that depends on human creativity, such as humor. Not only generating high quality humor requires more effort from humans making the process expensive, but also reliably assessing the level of humor is challenging as humor understanding is subjective.

Although we carefully annotated our dataset, we have observed some quirks. Some of our headlines showed lack of sufficient agreement between judges. For example, in the headline **C2** in Table 6, the standard deviation in judges’ ratings for the “puppies” version ($\sigma$ = 0.9) was much higher than that in the “pennies” version ($\sigma$ = 0.4), implying that using more judges for the “puppies” version could have given it a more reliable funniness rating. However, ensuring such quality control would make the data collection process more expensive.

Additionally, some participating teams reported the frequent mention of President Trump in the dataset, and that there were a non-trivial number of headlines that mentioned both “Trump” and “hair”, and these headlines had received high humor scores, adding certain biases on the data.

Although the FunLines training data was useful, it was annotated using a different set of judges. It is reasonable to expect that the rating scales of FunLines and our task dataset are not calibrated, and a proper calibration could have possibly increased the value of the FunLines data. However, we have not seen any participating system trying to address this problem, for example, by using a standardization technique to unify the two funniness scales.

# 7 Conclusion and Future Perspectives

We provided 15,095 edited and humor-rated, potentially funny headlines and defined subtasks for (1) rating the funniness of each one and (2) determining the funnier headline from a pair that came from editing the same original headline. Both humor subtasks were popular, attracting 48 and 31 teams respectively, showing that shared tasks can unify the relatively smaller humor research community.

For both subtasks, the highly rated solutions show that pre-trained language models work well for rating the humor. For Subtask 2, nearly all the participating teams used their solution from Subtask 1 for ranking the two headlines. For Subtask 2, we found that larger disparities in ground truth funniness made ranking easier and that incongruity in a headline was positively correlated with more accurate ranking of humor. For Subtask 1, we discovered that, over the range of funniness scores, the top systems were most accurate at rating humor near the middle of the funniness range where we had the most training data.

For future contests like this, we advocate for more uniformly labeled humor data, though that can be hard and expensive to collect. Another direction worth pursuing is humor recognition in a closed setting such as reading comprehension, where both annotators and systems make judgments based only on a limited amount of provided contextual information. This would constrain the problem, setting a well-defined scope, and potentially lead to stronger annotator agreements.

We also believe that focusing on specific labeled forms of humor, such as incongruity, sarcasm, irony, puns, and superiority would be advantageous. This could help to better understand how different modeling strategies can identify different root causes of humor. We would also want to design Subtask 2 to be more independent of Subtask 1 to encourage fresh approaches for Subtask 2. Finally, improving the common sense and world knowledge understanding capabilities of AI systems will be crucial for substantially improving the performance of computational humor systems. We hope that both the current results and the dataset in this task provide a stepping stone towards this goal.



<!-- page 0011 -->

## References

Charlotte Sophie Ammer and Lea Hannah Grüner. 2020. UniTuebingenCL at SemEval-2020 task 7: Humor detection in news headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Pramodith Ballapuram. 2020. LMML at SemEval-2020 task 7: Siamese transformers for rating humor in edited news headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Francesco Barbieri and Horacio Saggion. 2014. Automatic detection of irony and humour in twitter. In *ICCC*, pages 155–162.

Dario Bertero and Pascale Fung. 2016. A long short-term memory framework for predicting humor in dialogues. In *Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, pages 130–135, San Diego, California, June. Association for Computational Linguistics.

Weilong Chen, Jipeng Li, Chenghao Huang, Wei Bai, Yanru Zhang, and Yan Wang. 2020. Ferryman at SemEval-2020 task 7: Ensemble model for assessing humor in edited news headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Luis Chiruzzo, Santiago Castro, Mathias Etcheverry, Diego Garat, Juan José Prada, and Aiala Rosá. 2019. Overview of haha at iberlef 2019: Humor analysis based on human annotation. In *Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2019). CEUR Workshop Proceedings, CEUR-WS, Bilbao, Spain (9 2019)*.

Ravi Theja Desetty, Ranit Chatterjee, and Smita Ghaisas. 2020. Hasyarasa at SemEval-2020 task 7: Quantifying humor as departure from expectedness. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 4171–4186, Minneapolis, Minnesota, June. Association for Computational Linguistics.

Anna-Katharina Dick, Charlotte Weirich, and Alla Kutkina. 2020. HumorAAC at SemEval-2020 task 7: Assessing the funniness of edited news headlines through regression and Trump mentions. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Martin Docekal, Martin Fajcik, Josef Jon, and Pavel Smrz. 2020. JokeMeter at SemEval-2020 task 7: Convolutional humor. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Elena Filatova. 2012. Irony and sarcasm: Corpus generation and analysis using crowdsourcing. In *Lrec*, pages 392–398. Citeseer.

Aparna Garimella, Carmen Banea, Nabil Hossain, and Rada Mihalcea. 2020. “Judge me by my size (noun), do you?” YodaLib: A demographic-aware humor generation framework. *arXiv preprint arXiv:2006.00578*.

Nabil Hossain, John Krumm, Lucy Vanderwende, Eric Horvitz, and Henry Kautz. 2017. Filling the blanks (hint: plural noun) for mad Libs humor. In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing*, pages 638–647, Copenhagen, Denmark, September. Association for Computational Linguistics.

Nabil Hossain, John Krumm, and Michael Gamon. 2019. “President vows to cut &lt;taxes&gt; hair”: Dataset and analysis of creative text editing for humorous headlines. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 133–142, Minneapolis, Minnesota, June. Association for Computational Linguistics.

Nabil Hossain, John Krumm, Tanvir Sajed, and Henry Kautz. 2020. Stimulating creativity with funlines: A case study of humor generation in headlines. In *Proceedings of ACL 2020, System Demonstrations*, Seattle, Washington, July. Association for Computational Linguistics.

Kristian Nørgaard Jensen, Nicolaj Filrup Rasmussen, Thai Wang, Marco Placenti, and Barbara Plank. 2020. Buhscitu at SemEval-2020 task 7: Assessing humour in edited news headlines using hand-crafted features and online knowledge bases. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.



<!-- page 0012 -->

Shuning Jin, Yue Yin, Xiane Tang, and Ted Pedersen. 2020. Duluth at SemEval-2020 task 7: Using surprise as a key to unlock humorous headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Armand Joulin, Edouard Grave, Piotr Bojanowski, and Tomas Mikolov. 2017. Bag of tricks for efficient text classification. In *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers*, pages 427–431, Valencia, Spain, April. Association for Computational Linguistics.

S Kayalvizhi, D Thenmozhi, and Aravindan Chandrabose. 2020. SSN_NLP at SemEval-2020 task 7: Detecting funniness level using traditional learning with sentence embeddings. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Enas Khwaileh and Muntaha Al-as’ad. 2020. ELMo-NB at SemEval-2020 task 7: Assessing sense of humor in edited news headlines using ELMo and NB. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Chloe Kiddon and Yuriy Brun. 2011. That’s what she said: double entendre identification. In *Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies: short papers-Volume 2*, pages 89–94. Association for Computational Linguistics.

Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A robustly optimized bert pretraining approach. *arXiv preprint arXiv:1907.11692.*

Xuefeng Luo and Kuan Tang. 2020. funny3 at SemEval-2020 task 7: Humor detection of edited headlines with LSTM and TFIDF neural network system. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Jian Ma, Shu-Yi Xie, Mei-Zhi Jin, Lian-Xin Jiang, Yang Mo, and Jian-Ping Shen. 2020. XSYSIGMA at SemEval-2020 task 7: Method for predicting headlines humor based on auxiliary sentences with El-Bert. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Siddhant Mahurkar and Rajaswa Patil. 2020. LRG at SemEval-2020 task 7: Assessing the ability of BERT and derivative models to perform short-edits based humor grading. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

J.A. Meaney, Steven R. Wilson, and Walid Magdy. 2020. Smash at SemEval-2020 task 7: Optimizing the hyperparameters of ERNIE 2.0 for humor ranking and rating. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Rada Mihalcea and Carlo Strapparava. 2005. Making computers laugh: Investigations in automatic humor recognition. In *Proceedings of Human Language Technology Conference and Conference on Empirical Methods in Natural Language Processing*, pages 531–538, Vancouver, British Columbia, Canada, October. Association for Computational Linguistics.

Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, and Jeff Dean. 2013. Distributed representations of words and phrases and their compositionality. In *Advances in neural information processing systems*, pages 3111–3119.

Tristan Miller, Christian Hempelmann, and Iryna Gurevych. 2017. SemEval-2017 task 7: Detection and interpretation of English puns. In *Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)*, pages 58–68, Vancouver, Canada, August. Association for Computational Linguistics.

Rida Miraj and Masaki Aono. 2020. KdeHumor at SemEval-2020 task 7: A neural network model for detecting funniness in dataset humicroedit. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

Terufumi Morishita, Gaku Morio, Hiroaki Ozaki, and Toshinori Miyoshi. 2020. Hitachi at SemEval-2020 task 7: Stacking at scale with heterogeneous language models for humor recognition. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*

John Morreall. 2016. Philosophy of humor. In Edward N. Zalta, editor, *The Stanford Encyclopedia of Philosophy*. Metaphysics Research Lab, Stanford University, winter 2016 edition.

Gustavo H. Paetzold. 2020. UTFPR at SemEval-2020 task 7: Using co-occurrence frequencies to capture unexpectedness. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020).*



<!-- page 0013 -->

Jeffrey Pennington, Richard Socher, and Christopher Manning. 2014. Glove: Global vectors for word representation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1532–1543, Doha, Qatar, October. Association for Computational Linguistics.

Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. 2018. Deep contextualized word representations. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)*, pages 2227–2237, New Orleans, Louisiana, June. Association for Computational Linguistics.

Peter Potash, Alexey Romanov, and Anna Rumshisky. 2017. Semeval-2017 task 6:# hashtagwars: Learning a sense of humor. In *Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)*, pages 49–57.

Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. Language models are unsupervised multitask learners. *OpenAI Blog*, 1(8):9.

Yishay Raz. 2012. Automatic humor classification on twitter. In *Proceedings of the 2012 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Student Research Workshop*, pages 66–70. Association for Computational Linguistics.

Antonio Reyes, Paolo Rosso, and Davide Buscaldi. 2012. From humor recognition to irony detection: The figurative language of social media. *Data & Knowledge Engineering*, 74:1–12.

Alon Rozental, Dadi Biton, and Ido Blank. 2020. Amobee at SemEval-2020 task 7: Regularization of language model based classifiers. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Fara Shatnawi, Malak Abdullah, and Mahmoud Hammad. 2020. MLEngineer at SemEval-2020 task 7: BERT-flair based humor detection model (BFHumor). In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Anita Soloveva. 2020. SO at SemEval-2020 task 7: DeepPavlov logistic regression with BERT embeddings vs SVR at funniness evaluation. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Joseph J. Tomasulo, Jin Wang, and Xuejie Zhang. 2020. YNU-HPCC at SemEval-2020 task 7: Using an ensemble biGRU model to evaluate the humor of edited news titles. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Cynthia Van Hee, Els Lefever, and Véronique Hoste. 2018. Semeval-2018 task 3: Irony detection in english tweets. In *Proceedings of The 12th International Workshop on Semantic Evaluation*, pages 39–50.

Bram Vanroy, Sofie Labat, Olha Kaminska, Els Lefever, and Véronique Hoste. 2020. LT3 at SemEval-2020 task 7: Comparing feature-based and transformer-based approaches to detect funny headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Richard Wiseman. 2011. *Laughlab*. Arrow.

Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhtdinov, and Quoc V Le. 2019. Xlnet: Generalized autoregressive pretraining for language understanding. In *Advances in neural information processing systems*, pages 5754–5764.

Renxian Zhang and Naishi Liu. 2014. Recognizing humor on twitter. In *Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management*, pages 889–898.

Cheng Zhang and Hayato Yamana. 2020. WUY at SemEval-2020 task 7: Combining BERT and Naïve Bayes-SVM for humor assessment in edited news headlines. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.

Tiantian Zhang, Zhixuan Chen, and Man Lan. 2020. ECNU at SemEval-2020 task 7: Assessing humor in edited news headlines using biLSTM with attention. In *Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020)*.
