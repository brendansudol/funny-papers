<!-- Transcribed from 62-humor-modeling-survey.pdf -->



<!-- page 0001 -->

[Figure: ACM Digital Library, Association for Computing Machinery, and acm open logos; “Check for updates” icon]

[Figure: DL icon] Latest updates: https://dl.acm.org/doi/10.1145/3778357

SURVEY

# Computational Humor Modeling: A Survey on the State of the Art

**JENS LEMMENS**, University of Antwerp, Antwerpen, VAN, Belgium

**VICTOR DE MAREZ**, University of Antwerp, Antwerpen, VAN, Belgium

**Open Access Support** provided by:

**University of Antwerp**

[Figure: PDF icon]

**PDF Download**  
3778357.pdf  
19 January 2026  
**Total Citations:** 0  
**Total Downloads:** 404

**Published:** 08 January 2026  
**Online AM:** 26 November 2025  
**Accepted:** 07 November 2025  
**Revised:** 14 October 2025  
**Received:** 25 April 2025

**Citation in BibTeX format**

---

ACM Computing Surveys, Volume 58, Issue 7 (May 2026)  
https://doi.org/10.1145/3778357  
EISSN: 1557-7341



<!-- page 0002 -->

# Computational Humor Modeling: A Survey on the State of the Art

JENS LEMMENS, University of Antwerp, Antwerp, Belgium  
VICTOR DE MAREZ, University of Antwerp, Antwerp, Belgium

---

AI systems are not only becoming better in solving complex reasoning challenges, but also in performing creative tasks. One of the creative tasks where AI systems still struggle to achieve human performance, however, is humor processing, for which mixed results have been reported. Therefore, the goal of this survey is to categorize recent research in computational humor modeling in order to identify current trends, advancements, and remaining gaps. The scope of this work is broader than previous survey papers, as we tackle not only text-based models, but also multimodal models, and discuss a variety of detection and generation tasks.

CCS Concepts: • **Computing methodologies → Natural language generation; Machine learning approaches; Natural language processing;**

Additional Key Words and Phrases: Humor, humor understanding, humor detection, humor generation, large language models, natural language processing, computational linguistics, computer vision, speech processing

**ACM Reference Format:**  
Jens Lemmens and Victor De Marez. 2026. Computational Humor Modeling: A Survey on the State of the Art. *ACM Comput. Surv.* 58, 7, Article 177 (January 2026), 37 pages. https://doi.org/10.1145/3778357

---

## 1 Introduction

### 1.1 Scope

AI systems are not only improving in tackling complex reasoning problems but also in handling creative tasks [69]. However, one area where they continue to fall short of human performance is understanding and generating humor, where progress has been inconsistent and mixed results have been reported [60, 93]. Nevertheless, humor is an essential part of human communication, since it has been observed in one form or another in virtually all cultures. In addition, processing humor requires world knowledge, semantic reasoning, and linguistic understanding, which is why it is an AI complete problem and a strong indicator of “intelligence”. Despite these challenges, computational methods can provide insights into humor theory by testing specific hypotheses and function as humor writing assistants [129].

In this survey, we will therefore describe trends, advancements and remaining gaps in recent computational humor modeling research with AI systems. We adopt the definition of humor that is presented in *The Psychology of Humor* [88] (p. 3): “Humor is a broad, multifaceted term that

---

This research received funding from *FWO IRI CLARIAH 2* and the *Flanders AI research program*.  
Authors’ Contact Information: Jens Lemmens (xorrepsonding author), University of Antwerp, Antwerp, Belgium; e-mail: jens.lemmens@uantwerpen.be; Victor De Marez, University of Antwerp, Antwerp, Belgium; e-mail: victor.demarez@uantwerpen.be.  
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.  
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.  
ACM 0360-0300/2026/01-ART177  
https://doi.org/10.1145/3778357



<!-- page 0003 -->

represents anything that people say or do that others perceive as funny and tends to make them laugh, as well as the mental processes that go into both creating and perceiving such an amusing stimulus, and also the emotional response of mirth involved in the enjoyment of it.” Computational humor modeling, in other words, refers to any type of task that involves using input data to perform a task related to humor detection, generation, translation, evaluation, and so on, using AI methods.

Although computational humor research sprouted in the 1990’s [12], it has mainly focused on text data until 2019 [96]. Therefore, we will not only discuss state-of-the-art text-based methods, but also study advancements in multimodal approaches. Due to the rapid pace at which the field of AI is evolving, we will focus on manuscripts that were published since 2022. Regarding dataset and shared task papers, however, we will discuss work that is up to 5 years old (from January 2020), since the resources presented in such papers are typically still frequently utilized in today’s research.

## 1.2 Related Research and Our Contributions

To our knowledge, four long format survey papers<sup>1</sup> about computational humor have been published since 2020. First, Amin and Burghardt [4] focus on humor generation research from the 1990’s until 2020. Their main takeaways are that, first of all, there is a **lack of thorough (automatic) evaluation metrics** to determine how well humor models actually grasp the concept of humor. Secondly, they argue that future humor generation systems should focus on **combining insights from both NLP/AI and psychology**, in order to integrate cognitive theories of humor into AI systems. Winters [129], who discusses both humor generation and detection papers, confirms these two gaps, and adds that the bulk of humor research until **2021 has focused on English jokes only**, which is problematic since perceptions and verbalizations of humor vary between cultures and languages. In addition, Cowie [31] observes that in recent years, more research has focused on **multimodal humor tasks**, which poses additional challenges compared to unimodal tasks, and should therefore be the focus of future work. Finally, and in contrast to the previous surveys, Kalloniatis and Adamidis [63] studied feature engineering for the task of humor detection, and reviewed 21 different features utilized in papers published between the 1990’s and 2022. They showed that **ambiguity**—inspired by cognitive theories of humor—was the most commonly used feature, but highlighted that it is particularly difficult to quantify this feature.

Our work contributes to existing research in three ways. First, it provides an overview and classification of the most recent computational humor research, while providing detailed insights into the technical aspects and the influence of recent trends in AI research. Secondly, our scope is broader than existing overview papers, since a wide variety of humor related tasks (generation, detection, evaluation, translation) and data modalities (text, audio, image/video) are included in this paper in order to suggest relevant future research directions. Note, however, that we exclude papers tailored specifically towards irony and sarcasm from this work. Since the amount of work done regarding this topic is so large, and irony per definition is not always used with the intention of producing humor, but rather negative sentiment, we believe that it is deserving of its own literature study. Thirdly, the takeaways presented in the aforementioned survey papers will be discussed in the conclusion, and it will be clarified to what extent they are still relevant to future work.

## 1.3 Overview

Section 2 presents our methodology, i.e., how relevant work was collected and filtered. Then, datasets and shared tasks are discussed in Sections 3 and 4, respectively. Furthermore, recent computational

---

<sup>1</sup>Although [94] is also presented as a survey paper, we do not treat it as such, since its main contribution is to present a dataset, instead of providing a literature overview.



<!-- page 0004 -->

Table 1. Keywords Used to Search for Related Work

| **Keywords** |
|---|
| humo(u)r(ous), funny, laughter, humo(u)r theory |
| joke, parody, one-liner, pun, wordplay, satire, satirical |
| stand-up, comedy, comedian, sketch, sitcom, meme |
| NLP, computational, model(ing) |
| AI, artificial intelligence |
| dataset, shared task |
| robotics, chatbots, conversational agents |
| **Large Language Model (LLM)**, GPT, neural |
| generation, recognition, detection, translation, evaluation |
| explanation, explainability, interpretability, |
| surprise, relief, incongruity |

models of humor are discussed in Section 5, where we distinguish between detection and generation models. Then, Section 6 elaborates not only on annotation but also on evaluation methods in recent work. Section 7 connects to the section on evaluation by discussing work on explainability and interpretability, providing more insights into the extent that models *understand* humor. Finally, the most important recent trends, advancements, and remaining gaps are summarized in the discussion in Section 8.

## 2 Methodology

To collect relevant work, we use (combinations of) the keywords mentioned in Table 1 to search for research papers in the following search engines: Google Scholar, Semantic Scholar, ACL anthology, ACM computing surveys, IEEE Xplore, and European Journal of Humor Research. In addition, we use backward and forward citation search for a more comprehensive collection of works.

To decide which papers that resulted from the search queries to include in this work, the decision tree presented in Figure 1 was used. In short, we include recent papers about computational humor modeling with AI systems which have been peer-reviewed. Non-peer-previewed papers were included only if the presented model is patented, or if the code/data was shared and novel experiments were presented. Regarding shared task papers, we only include overview papers or papers of winning teams.

## 3 Humor Datasets

In Tables 2 and 3, overviews of the humor datasets published between 2020–2022, and 2023–2024 are provided, respectively.[^2] In accordance with Martin and Ford [88], we distinguish three coarse-grained types of humor to classify these datasets: jokes, performance humor, and conversational humor. Jokes are defined as independent humorous statements, i.e., they are not part of a larger context window, such as a conversation, or a performance. Examples of jokes are satirical news headlines, humorous social media messages, wordplay, or funny one-liners. Conversational humor, on the other hand, comprises humor that occurs in dialogues or group conversations, typically to serve a social function, i.e., to boost the mood in the conversation and/or stimulate it to continue. Compared to jokes, in which a certain amount of preparation or thought has been put before uttering them, conversational humor is created spontaneously. Finally, performance humor is

[^2]: Note that datasets published in the context of shared tasks are described in Section 4.



<!-- page 0005 -->

[Figure: Decision tree for paper inclusion. Top box asks whether the paper is related to computational humor modeling, not specifically focused on sarcasm/irony, and recently published. Branches lead through questions about peer review, shared task submissions, public code/dataset availability, novel experiments, patents, overview papers, and shared task winners, ending in Include or Exclude.]

Fig. 1. Decision tree used to determine whether to include a paper in this survey or not.

humor that occurs in the context of an act or *performance*. Examples of this type of humor are jokes in sitcoms, movies, books, sketches, or stand-up comedy. In terms of spontaneity, performance humor is located on the opposite end of the spectrum compared to conversational humor, since it is by definition well prepared and practiced before it is performed. Therefore, sitcom data that has been described as *conversational humor* in dataset papers will be considered as performance humor, since sitcom conversations are not spontaneous or natural.

### 3.1 Jokes

The largest portion of humor datasets that have been published in the last 5 years contain jokes (26 out of 39 datasets, as shown in Tables 2 and 3). Although the bulk of the available joke datasets present human-written data, Horvitz et al. [52] use LLMs to generate *unfunny jokes*. The authors argue that humor detection models trained on jokes as positive data and non-humorous data from other genres as negative data show suboptimal generalization capabilities across datasets and tasks. Hence, they use LLMs to generate jokes that are not funny, but capture the same form as jokes, in order to arrive at parallel data. For example, consider the following satirical punchline and its unfunny counterpart, which has a similar structure: “Study links meat, sugar consumption to early death *among those who choose to be happy in life*” vs. “*among those with unhealthy lifestyles*”. The authors, however, do not provide a direct comparison between models fine-tuned on parallel and non-parallel data for humor detection, so although this approach has been theoretically justified, the exact benefits have not been shown empirically.

In other work, Horvitz et al. [52] and Hessel et al. [51] present datasets of satirical news headlines and news related cartoons, respectively. These are examples of how **news data** can be mined to create joke datasets. Another frequent source for joke datasets is **social media**. For example, Weller et al. [127] scraped Reddit jokes using distant supervision by mining the r/Jokes subreddit, whereas Maronikolakis et al. [86] and Bellamkonda et al. [10] leverage X (formerly known as Twitter) data to construct joke datasets. A particularly fruitful source of jokes on social media that has been used frequently in recent years are **memes**.<sup>3</sup> Merriam Webster<sup>4</sup> defines a meme as follows: “an amusing

<sup>3</sup>Note that many meme datasets focus on offensiveness detection in memes. We decided not to include these in our overview; only datasets focusing on humor in memes were studied.  
<sup>4</sup>https://www.merriam-webster.com/dictionary/meme [last accessed October 2025].



<!-- page 0006 -->

Table 2. Overview of the Humor Datasets Published between 2020–2022

| Reference | Dataset name | Task(s) | Modalities | Genre(s) | Lang(s) | Baselines | Evaluation |
|---|---|---|---|---|---|---|---|
| [29] Chiruzzo et al. (2020) | HAHA2019 | D, R | T | J | es | Various existing models | pre, rec, F1, acc / RMSE |
| [54] Hossain et al. (2020) | Humicroedit | D | T | J | en | RF, LSTM | acc |
| [86] Maronikolakis et al. (2020) | Political parody in social media | D | T | J | en | LR, LSTM, (Ro)BERT(a), XLNet, ULMFit | pre, rec, F1, acc, AUC |
| [104] Priego-Valverde et al. (2020) | CHEESE! | - | A, V | CH | fr | - | - |
| [123] Tseng et al. (2020) | Chinese humor corpus | D | T | J | zh | SVM, BERT | F1, ROCAUC |
| [128] Weller, Seppi (2020) | /r/Jokes | R | T | J | en | (Ro)BERT(a), XLNet | RMSE, Pearson/Spearman |
| [22] Chauhan et al. (2021) | M2H2 | D | T, V, A | PH | hi | MISA fusion model | pre, rec, F1 |
| [66] Kayatani et al. (2021) | Laughing Machine | D | T, V, A | PH | en | Fusion model (FACS, BERT) | pre, rec, F1, acc |
| [95] Mittal et al. (2021) | OpenMic | D | T, A | PH | en | BERT variants, XML, Glove | Quadratic Weighted Kappa |
| [99] Pamulapati, Mamidi (2021) | Telugu humor dataset | D | T | PH | pt | GCN, FastText, BERT | F1, acc |
| [100] Patro et al. (2021) | MHD | D | T, V | PH | en | Fusion model (BERT, C3D) | F1, acc, ROC |
| [130] Wu et al. (2021) | MUMOR | D | T, V, A | PH | en, zh | - | - |
| [133] Yang et al. (2021) | CHoRaL | D | T | J | en | (Ro)BERT(a) | F1, AUC |
| [2] Alkhalifa et al. (2022) | Arabic humor detection dataset | D | T | J | ar | BERT variants | pre, rec, F1, acc |
| [10] Bellamkonda et al. (2022) | Telugu humor in social media | D | T | J | te | (Ro)BERT(a) | F1, acc |
| [78] Li et al. (2022) | MemePlate | R | T, I | J | zh | Vision transformers | acc, F1 |
| [81] Liu et al. (2022) | FigMemes | D | T, I | J | en | BERT, CNN, CLIP, ViViT | f1 |
| [116] Sun et al. (2022b) | CUP | G | T | J | en | AmbiPun, T5 | Success rate (human eval.) |
| [117] Tanaka et al. (2022) | - | D | T, V | J | en | MLP fusion model | acc |
| [124] Turano, Strapparava (2022) | SCRIPTS | D | T | PH | en | LR, NB, RF | pre, rec, F1, acc |
| [131] Xu et al. (2022) | MET-Meme | D | T, I | J | en, zh, both | m-BERT, Resnet, VGG | f1 |

For each dataset, the name, tasks (D: detection, G: generation, R: ranking, M: matching, E: explanation), modalities (T: text, V: video, I: image, A: audio), genre (J: jokes, CH: conversational humor, PH: performance humor), evaluation metrics, and language(s) are specified.



<!-- page 0007 -->

Table 3. Overview of the Humor Datasets Published between 2023-2024

| Reference | Dataset name | Task(s) | Modalities | Genre(s) | Lang(s) | Baselines | Evaluation |
|---|---|---|---|---|---|---|---|
| [13] Bogreedy et al. (2023) | COVID-19 Humor dataset | D | T | J | en | GPT3, RoBERTa | pre, rec, f1, acc |
| [18] Bukhari et al. (2023) | - | D | T | J | en-ur | BERT, CNN, LSTM, classical models | pre, rec, f1, acc |
| [24] Chen et al. (2023) | - | D | T | J | zh | (Ro)BERT(a), BART, T5, CPT | acc |
| [51] Hessel et al. (2023) | New Yorker Caption Contest | M, R, E | T, I | J | en | CLIP, OFA, T5, GPT3/3.5/4 | acc, pairwise eval. |
| [56] Hwang, Schwartz (2023) | MemeCap | G | T, I | J | en | Flamingo, GPT4, LLaMA | BLEU, ROUGE, BERTScore, human eval. |
| [76] Li et al. (2023) | Chinese comical crosstalk dataset | G | T | PH | zh | CPT, UniLM, T5 | BLEU, ROUGE |
| [77] Li et al. (2023b) | OxfordTVG-HIC | G | T, I | J | en | PaLM, GPT3, CPM, BLIP, CLIP | BERTScore, Distinct n-grams, benign, fluency, and diversity (automatic) |
| [16] Boukes et al. (2024) | Pandemic Humor | D | T, I | J | multi | FaceRecognition | - |
| [27] Chen et al. (2024b) | TalkFunny! | G | T | CH | zh | Moses Pipeline, BART, T5, GPT3/3.5, CPT | mix of manual and automatic eval. |
| [30] Christ et al. (2024) | Passau-SFCH | D | T, V, A | J | de | various fusion models | AUC |
| [45] Guo et al. (2024) | MUCH | D | T, A, V | PH | zh | BERT, OMNIVORE/ViT, OpenSmile | pre, rec, F1, acc |
| [50] He et al. (2024) | CHUMOR | E | T | J | zh | GPT-4o, Ernie Bot | human eval. |
| [52] Horvitz et al. (2024) | UnFunny | - | T | J | en-hi | - | - |
| [71] Kumar et al. (2024) | HumorHindiNet | D | T | PH | hi | ANN, CNN, RNN, BERT, classical ML models | pre, rec, f1, acc |
| [73] Kumari et al. (2024) | - | D | T, I | J | hi | GCN, BERT, VGG | F1, acc |
| [74] Kuznetsova and Strapparava (2024) | - | D | T, V | PH | en, ru | BERT, VideoMAE, SVM | F1 |
| [137] Zhang et al. (2024) | Chinese Pun Rebus Art Dataset | M, E | T, I | J | zh | GPT, Gemini, Claude, Qwen | acc, manual eval. |
| [138] Zhong et al. (2024) | Oorri-GO | G, R | T, I | J | zh | Various LLMs/VLMs | human and automatic |

For each dataset, the name, tasks (D: detection, G: generation, R: ranking, M: matching, E: explanation), modalities (T: text, V: video, I: image, A: audio), genre (J: jokes, CH: conversational humor, PH: performance humor), evaluation metrics, and language(s) are specified.



<!-- page 0008 -->

or interesting item (such as a captioned picture or video) or genre of items that is spread widely online especially through social media.” In Tanaka et al. [117], 7,500 memes were annotated by crowdworkers for binary humor classification. These memes were obtained by scraping a meme sharing website and by using an automatic meme generator. In other work [56], a dataset for captioning and interpreting memes named “MemeCap” is presented. This dataset contains more than 6,000 memes with various types of metadata, with a focus on the metaphorical mechanisms that create humor in memes. Similarly, Xu et al. [131] published MET-Meme, a multilingual meme dataset containing annotations regarding the metaphorical mechanisms behind the humor created in memes. The dataset contains more than 10,000 memes with accompanying text transcriptions, of which approximately 60% are in Chinese, and the remaining 40% are in English. The following metaphor metadata was added by annotators: a binary label, indicating whether the meme uses a metaphor, and a more fine-grained label indicating whether the metaphorical element is expressed in the text, the image, or both. Additional annotations include emotion (7 classes), intention (“entertaining”, “offensiveness”, “other”), and in the case of offensiveness, a rating of how offensive the meme is (0–4). Depending on the experimental setting, the best models yielded F1-scores of 76.0–82.4% for metaphor detection, but surprisingly low results on emotion detection (<37.0%), in spite of the high annotator agreement (Fleiss’ Kappa > 0.80).

### 3.2 Performance Humor

Memes do not only represent the social media trend in humor datasets, but also a **multimodal** trend. In contrast, earlier work on computational humor modeling focused exclusively on the textual modality (as mentioned in the introduction); Mittal et al. [96] even claimed that the first multimodal humor dataset, URFunny [47], was published only in 2019, although humor modeling has been attempted since the 1990’s (cf. JAPE [12], often referred to as the first computational humor model). Humor, however, is a multimodal phenomenon, as it does not only rely on text and semantics, but also (and in some cases exclusively) on auditive cues, such as intonation and timing, and visual cues, like gestures and mimicry. Today, this multimodal nature of humor has been acknowledged in the state-of-the-art, since 20 out of 39 datasets included in Tables 2 and 3 are multimodal. The bulk of these multimodal datasets (11) contain performance humor, specifically **sitcoms**. The MHD and Laughing Machine datasets [66, 100], for instance, present transcriptions and video data of the American sitcom “The Big Bang Theory”, whereas the MUMOR dataset [130] contains dialogues from “Friends”. Similarly, Pamulapati and Mamidi [99] and Guo et al. [45] present data from Telugu and Chinese sitcoms, respectively. Chauhan et al. [22] and Kumar et al. [71], on the other hand, focus on collecting sitcom data in Hindi.

Next to sitcoms, other multimodal performance humor datasets we found focus on **stand-up comedy**. Turano and Strapparava [124] present “SCRIPTS”, a dataset containing 90 stand-up comedy transcripts from 68 comedians. Similarly, Kuznetsova and Strapparava [74] collect a multimodal corpus of Russian and English stand-up comedy. In total, this dataset contains 37 hours of video material scraped from YouTube, with accompanying text transcriptions. In other work, Mittal et al. [95] publish a multimodal dataset containing over 40 hours of annotated open mic clips. Finally, Li et al. [76] present a dataset of Chinese crosstalk transcripts; a traditional form of comedy dialogues.

### 3.3 Conversational Humor

Finally, the type of humor that is included the least frequently in recent humor datasets is conversational humor (2 of the 39 datasets). First, Priego-Valverde et al. [104] present a conversational humor dataset named “Cheese!”, which consists of audio and video recordings of 11 human-human interactions in French that each last approximately 15 minutes. In other work, Chen et al. [27] present “TalkFunny!”, a Chinese dataset containing dialogue utterance transcriptions and funny



<!-- page 0009 -->

responses. Although other work has claimed to present conversational humor datasets, these are to our knowledge the only datasets published since 2020 which actually contain spontaneous conversations, and not conversations that are in reality examples of performance humor, such as sitcom dialogues. Since jokes only constitute approximately 11% of our daily humor experiences, while conversational humor and performance humor cause a respective 70% and 17% of these experiences [87], **conversational humor is proportionally underrepresented** in existing humor datasets.

## 4 Shared Tasks

### 4.1 SemEval 2020 Task 7: Assessing Humor in Edited News Headlines

Task 7 of SemEval 2020 consisted of assessing humor in news headlines [54]. The participants were subjected to two subtasks: (1) estimate the funniness of an edited news headline, and (2) given two edited news headlines, predict which is funnier (or whether they are equally funny). The Humicroedit dataset was used for this shared task, consisting of approximately 5,000 news headlines that were collected from the r/Politics and r/WorldNews subreddits [53]. Three edited versions of each headline were collected by asking annotators to change one noun, verb or named entity in the headlines with another word to make them funny. For each edited headline, 5 human judges were then asked to evaluate the funniness of the headline on a Likert scale of 0–3. These ratings were then used in the first subtask for a humor rating problem, using RMSE as evaluation metric.

For task 2, the original headline and two edited versions were provided, and a model had to predict which of these three was rated the funniest. Accuracy was reported for model evaluation. The winner of both tasks used an ensemble model consisting of various pre-trained transformers, and yielded a **Root Mean Squared Error (RMSE)** and accuracy score of 0.497 and 0.674, respectively. The other participants also relied primarily on pre-trained transformers, although the 6th best ranked model for both subtasks 1 and 2 (out of 48 and 31 participating teams, respectively) used humor and sentiment lexicons for classification, indicating that rule-based methods can compete with pre-trained transformers.

### 4.2 HaHackathon@SemEval 2021 (Task 7)

The humor detection shared task “HaHackathon” of SemEval 2021, co-located with ACL, was **the first shared task to combine humor detection with offensiveness detection** [90]. In other words, this shared task was the first to deal with humor preferences and **account for personal and cultural sensitivities in humor**. Specifically, three subtasks were defined: (1) binary humor detection, (2) humor rating prediction, and (3) offensiveness rating prediction. 80% of the data was mined from X accounts based in the USA to ensure that no cultural or linguistic issues were introduced, as the annotators were also from the USA (the remaining 20% of the data consisted of Reddit posts). Since the shared task focused on personal sensitivities in humor, potentially offensive messages needed to be included in the dataset. Therefore, the data was sampled so that half of the messages contained one or more key words associated with the hate speech categories defined in Silva et al. [113]. To collect positive data, i.e., humorous messages, tweets from accounts that by definition only post content that is intended to be humorous were used, such as “@conanobrien” and “@humorous1liners”. For Reddit, posts that originated from the “r/Jokes” and “r/CleanJokes” subreddits were used. Negative data, on the other hand, was collected from X accounts that represent the targets of the offensive language mentioned above (e.g., “@BlkMentalHealth”). This strategy of collecting negative data ensured that offensive terms occurred in both humorous and non-humorous messages, and that the topics discussed in both classes were comparable to avoid topic bias in the classifiers.

In order to collect high quality labels and avoid reflections of personal subjectivity, 20 evaluators, which were equally distributed across four different age groups, were asked to provide annotations



<!-- page 0010 -->

for each data point. Specifically, they were first asked to indicate whether each post was intended to be humorous (yes/no). If this was the case, they were asked to provide a score on a Likert scale of 1 to 5 regarding how funny they found the post, and whether it was offensive (not only in general, i.e., as intended by the speaker, but also to the annotator personally). Afterward, Kippendorff’s $\alpha$ was computed to measure the inter-annotator agreement across the annotation tasks, and it was shown that there was **high agreement for detecting _humor intention_, but low agreement for rating humorousness and offensiveness.** This result was reflected in the submissions of the participating teams, which achieved high results on task 1 (F1-score>0.96 for the top 10 best performing teams), but low results on tasks 2 and 3 (which were around 0.50–0.55 RMSE and 0.62–0.63 F1-score, respectively, for the top 10 best performing participants).

### 4.3 HAHA@IberLef 2021

The goal of the HAHA shared task, co-located at IberLef 2021, was to not only perform humor detection (task 1) and humor rating (task 2), but to dive deeper into automatic humor analysis [28]. Specifically, a third task consisted of detecting humor mechanisms: absurdity, analogy, embarrassment, exaggeration, insults, irony, misunderstanding, parody, reference to world knowledge, stereotype, unmasking of someone’s intentions, and wordplay. The fourth and final task consisted of identifying the target of humor. This task included the following categories: age, body shaming, ethnicity/origin, family/relationships, health, LGBT+, men, professions, religion, self-deprecating, sexual aggressors, social status, substance use, technology, and women.

The dataset consisted of 36,000 tweets (24,000 for training, and 6,000 for development and testing, each), of which 15,000 were humorous. The humor mechanism and target(s) were labelled in 7,200 of these tweets. In total, 14 teams participated in the shared task. The winning team, all subtasks considered, used an ensemble of pre-trained transformers that was fine-tuned on the provided humor data [43]. Nine other teams also relied on pre-trained transformers, whereas the remaining participants either used other neural architectures or classical machine learning approaches.

### 4.4 HUHU@IberLef 2023

The HUrtful HUmor (HUHU) detection shared task was organized as part of the IberLef 2023 conference [75]. The goal of the shared task was to detect prejudice-spreading humor in X, in which the term _prejudice_ was defined as “the negative pre-judgment of members of a race or religion or of any other socially significant group, regardless of the facts that contradict it” [62]. Specifically, the shared task consisted of detecting stereotypes towards certain minorities that are conveyed by humor in Spanish tweets. In the first subtask, models needed to predict whether a tweet was humorous. Then, the second task was to identify the minority group targeted by the humorous stereotypes. Additionally, participants had to predict the degree of hurtfulness on a scale of 1–5. Details on how the dataset or annotations were collected are not reported.

### 4.5 JOKER@CLEF 2024

JOKER-2024 was the third iteration of the JOKER shared task, organized at the CLEF conference, and consisted of three subtasks. The first task comprised retrieving jokes about specific topics. The dataset was built from the JOKER-2023 shared task, and consisted of more than 60,000 English texts, of which 4,492 were humorous, from various genres. In total, 10 teams participated and they employed techniques ranging from TF-IDF and BM25 to BERT [34] and SimpleT5 [106]. The results showed that both precision and recall were extremely low, indicating how challenging the task is. The second task consisted of humor classification by genre (6 classes), for which approximately 2,500 humorous texts were provided for training. The best performing submission was based on Mistral-7B [61], which obtained an F1-score of 70%; 10% more than the runner up, who used DeBERTa



<!-- page 0011 -->

Table 4. Overview of Humor Shared Tasks

| Reference(s) | Name | Description of Task(s) | Modalities | Evaluation | Lang(s) |
|---|---|---|---|---|---|
| [54] Hosseini et al. (2020) | SemEval-2020 Task 7: Assessing Humor in Edited News Headlines | **Task 1:** Humor rating<br>**Task 2:** Most humorous headline prediction | T | Task Task 1: RMSE<br>Task 2: A, reward | en |
| [28] Chiruzzo et al. (2021) | HAHA@Iberlef 2021 | **Task 1:** Humor detection<br>**Task 2:** Humor rating<br>**Task 3:** Mechanism classification<br>**Task 4:** Target classification | T | Task 1, 3, 4: F1<br>Task 2: RMSE | es |
| [90] Meaney et al. (2021) | HaHackathon:<br>SemEval-2021 Task 7 | **Task 1:** Humor detection in Reddit and X<br>**Task 2:** Humor rating<br>**Task 3:** Controversy detection | T | Task 1/3: A, F1<br>Task 2: RMSE | en |
| [15] Bonet et al. (2023) | HUrtful HUmour (HUHU): Detection of humour spreading prejudice in X | **Task 1:** Humor detection in tweets<br>**Task 2a:** Classification of targeted minority group<br>**Task 2b:** Hurtfulness rating | T | Task 1/2a: F1<br>Task 2b: RMSE | es |
| [37] Ermakova et al. (2024a)<br>[103] Preciado et al. (2024)<br>[38] Ermakova et al. (2024b) | CLEF 2024 JOKER Shared Task | **Task 1:** Information retrieval<br>**Task 2:** Humor classification<br>**Task 3:** Pun translation | T | map, ndcg, pre, rec, bp<br>pre, rec, F1, acc<br>BLEU, BERTscore | en<br>en<br>en, fr, es |
| [5] Amiriparian et al. (2024) | MuSe 2024:<br>Multimodal Sentiment Analysis Challenge | **Task 1:** Social perception analysis<br>**Task 2:** Cross-cultural humor recognition | T, V, A | Task 1: Pearson<br>Task 2: AUC | en, de |

The name of the shared tasks, task descriptions, modalities (T: text, V: video, I: image, A: audio), evaluation metrics (P: precision, R: recall, F1: F1-score, A: accuracy, RMSE: Root Mean Squared Error), and languages are specified.

[49]. When observing performance per class, high imbalances could be observed, but these could be explained by correlation with class frequency in the data. Finally, the third task consisted of translating puns from English to French. For this task, the JOKER-2023 wordplay corpus was used [36]. This dataset contains 1,405 English wordplay instances, with 5,838 translations to French, performed by professional translators (72% of puns have more than 1 translation). Eleven teams participated in this task, and used mainly LLMs, commercial translation systems, and out-of-the-box translation models. Overall, approaches using Google Translate obtained the highest results.

### 4.6 MuSe@ACM-MM 2024

The fifth iteration of the **Multimodal Sentiment Analysis Challenge (MuSe)** [5] included a cross-cultural humor detection challenge based on the Passau-SFCH dataset [30]. The goal of this task was to perform multimodal humor detection in football coach interviews, where the training data consisted of Bundesliga coaches (German native speakers), and the test data consisted of Premier League coaches (various backgrounds). The best model reported an AUC-score of 0.87, and consisted of a fusion model that combined text, audio, and video data. For text, a BERT model was used, whereas Wav2Vec [8] and ViT-FER [20] were used for the audio and video data, respectively. This trimodal approach obtains substantial improvements over unimodal and bimodal systems.

### 4.7 Trends and Advancements

The main trend we observed in previous shared tasks (see Table 4) is that they all focused on humor detection while neglecting humor generation tasks (although JOKER organized the additional task of pun translation). Due to the nature of these tasks, and successes of pre-trained transformers, (BERT-based) encoders dominated in the model submissions, causing **relatively little variation in submitted models** and therefore also in the results within the same shared task. Furthermore,



<!-- page 0012 -->

it can be observed that all but one shared task exclusively used text data (social media messages specifically). On the other hand, there is a positive evolution towards more frequent research in non-English languages, which is a trend that is also visible in recently published datasets, as discussed in Section 3. Furthermore, a positive evolution towards **accounting for cultural and personal preferences in humor** can be observed in the HaHackathon shared task. Since humor is highly subjective, such setups should be considered best practice in future work.

## 5 Computational Models of Humor

In the current section, noteworthy trends and advancements in studies on computational humor models published since 2022 are described. We distinguish between models for humor detection and humor generation. Overviews of the former can be found in Tables 5 and 6, which contain unimodal and multimodal detection models, respectively. An overview of humor generation models can be found in Table 7. The models are categorized by their type of architecture (rule-based, data-driven, or hybrid). In addition, it is mentioned which architecture they are based on (if data-driven techniques are used), which language(s) and modality/-ies they are trained on, what type of humor they specialize in (jokes, conversational humor, performance humor), whether they are based on a humor theory (and which), and how they are evaluated. Note that models that were designed in the context of a shared task are discussed in Section 4, and that baseline models presented in dataset papers are also excluded from these overviews.

### 5.1 Humor Detection

#### 5.1.1 *Unimodal Humor Models.*

As mentioned in the introduction, earlier computational humor models focused virtually exclusively on text data. We observe that today, most humor detection approaches still focus on text data, as 18 out of 25 identified models were designed for text only. In addition, we detect that all approaches but one are data-driven. However, **no particular trends in the types of data-driven models that were utilized could be observed:** In spite of their popularity, not only generative LLMs, but also smaller (fine-tuned) language models, older neural methods, and statistical methods have been used in recent years. Below, we briefly discuss how well these different approaches perform on various humor detection tasks and how relevant older methods still are today.

*Pre-trained language models.* Jentzsch and Kersting [60] investigate the humor detection capabilities of ChatGPT [98]. More specifically, it was investigated whether the model could be misled by non-jokes which had similar structures to actual jokes. The results, however, indicated that the model could not be misled by joke-like texts that were not humorous. In similar work, Xu et al. [132] perform pun detection with LLMs, but explore a wider variety of models and prompts. The results indicated that with a basic prompt, the prediction consistency was low, especially for non-puns, which were confusing to the models due to their pun-like structure. However, adding a definition and examples of puns to the prompt substantially improved results. These results highlight the importance of adequate prompt engineering in humor detection tasks, which is necessary to tweak how the model defines humor.

Regarding encoder-decoder models, Arora et al. [7] explore a BERT-based transfer learning approach for detecting humor with different joke genres. They propose a *shared-private* multitask approach based on Liu et al. [82], consisting of frozen BERT layers pre-trained on different humor types (shared feature space) and one BERT layer dedicated to a specific joke genre (private feature space). The authors report that the proposed approach outperforms existing humor detection models and a BERT baseline on 2 out of the 4 utilized datasets. Furthermore, Ao et al. [6] leverage BERTweet to detect political parody in social media. Specifically, they design a multi-encoder



<!-- page 0013 -->

Table 5. Unimodal Humor Detection Models Published Since 2022

| Reference | Task(s) | Approach | Base model | Evaluation metrics | Genre(s) | Humor theories | Lang(s) |
|---|---|---|---|---|---|---|---|
| [6] Ao et al. (2022) | D | DD | BERTweet | F1 | J | - | en |
| [7] Arora et al. (2022) | D | DD | BERT | acc, F1 | J | - | en |
| [21] Ofer and Shahaf (2022) | D | DD | CatBoost | acc, AUC | J | - | en |
| [65] Kayastha and Reddy (2022) | D | DD | GloVe + GRU | pre, rec | J | - | en |
| [72] Kumar et al. (2022) | D | DD | CNN-LSTM | pre, rec, F1, AUC | J | - | en |
| [79] Li et al. (2022) | D | DD | GloVe + Transformer | Loss | J | - | en |
| [108] Ren et al. (2022) | D | H | CNN-LSTM + attention | pre, rec, F1 | J | Incongruity theory | en |
| [110] Shang et al. (2022) | D | DD | (Ro)BERT(a) | pre, rec, F1 | PH | - | zh |
| [115] Sun et al. (2022) | E | DD | T5 / AmbiPun | WIR, Success rate | J | - | en |
| [9] Baranov et al. (2023) | D | DD | Various existing models | F1 | various | - | en |
| [60] Jentzsch and Kersting (2023) | D | DD | ChatGPT | Human evaluation | J | - | en |
| [83] Liu and Hou (2023) | D | DD | GloVe + SVM | pre, rec, F1, acc | J | Incongruity theory | en |
| [112] Shatnawi et al. (2023) | D | DD | Various pre-trained LMs | Task-dependent | J | - | en |
| [32] De Marez et al. (2024) | D | DD | Ensemble of GA2M models | F1 | J | Surprise-disambiguation theory, incongruity, superiority, relief | en |
| [40] Fahim et al. (2022) | D | DD | Ensemble of statistical models | pre, rec, F1, acc | J | - | en |
| [57] Inácio and Oliveira (2024) | D | DD | BERTimbau | F1 | J | - | pt |
| [132] Xu et al. (2024) | D, E | DD | Various LLMs | TPR, TNR, Cohen’s K; Human eval., win/mention rate | J | - | en |
| [136] Zeng et al. (2024) | D, E | DD | BERT/NN + Graph NN | pre, rec, F1, acc | J | - | zh |

For each model, the task(s) (D: Detection, E: explanation), approach (RB: rule-based, H: hybrid, DD: data-driven), architecture, evaluation metrics, genre (J: jokes, PH: performance humor, CH: conversational humor), humor theory, and the language is specified.



<!-- page 0014 -->

Table 6. Multimodal Humor Detection Models Published Since 2022

| Reference | Task(s) | Approach | Base model | Modalities | Evaluation metrics | Genre(s) | Humor theories | Lang(s) |
|---|---|---|---|---|---|---|---|---|
| [3] Alnajjar et al. (2022) | D | DD | BERT / HuBERT | T, A | pre, rec, F1, acc | PH | - | en |
| [33] Deng et al. (2022) | D | DD | BLSTM + ConvAE | T, A, V | acc, F1 | PH | - | en |
| [117] Tanaka et al. (2022) | D | DD | ViLT / CLIP | T, I | acc | J | Incongruity theory | en |
| [51] Hessel et al. (2023) | E, M | DD | CLIP; T5, GPT(3, 3.5, 4) | T, I | acc | J | - | en |
| [70] Koutlis et al. (2023) | D | DD | VPU, ViTa | T, I | acc | J | - | en |
| [74] Kuznetsova and Strapparava (2024) | D | DD | VideoMAE/BERT to SVM/NN | T, V | F1 | PH | - | en, ru |
| [102] Phukan et al. (2024) | D | DD | VQC | T, V, A | pre, rec, F1 | PH | - | hi |

For each model, the task(s) (D: detection, E: explanation, M: matching), approach (RB: rule-based, H: hybrid, DD: data-driven), architecture, modalities (T: text, I: image, V: video, A: audio), evaluation metrics, genre (J: jokes, PH: performance humor, CH: conversational humor), humor theory, and the language is specified.



<!-- page 0015 -->

Table 7. Overview of Humor Generation Models Published between 2022–2024

| Reference | Approach | Model | Modalities | Evaluation metrics | Genre(s) | Humor theories | Lang(s) |
|---|---|---|---|---|---|---|---|
| [96] Mittal et al. (2022) | DD | GPT3 | T | Diversity, Success Rate, Human eval. | J | Incongruity theory | en |
| [116] Sun et al. (2022) | DD | AmbiPun / T5 | T | Success rate (human eval.) | J | - | en |
| [118] Tian et al. (2022) | H | GPT2-large | T | Success Rate, Human eval. | J | Surprise-disambiguation theory | en |
| [23] Chen et al. (2023) | DD | various seq2seq transformers | T | automatic and human | J | - | en |
| [60] Jentzsch et al. (2023) | DD | ChatGPT | T | Human eval. | J | - | en |
| [68] Ko et al. (2023) | DD | BART, T5, GPT3.5 | T | SentBERT, ROSCOE | PH | - | en |
| [76] Li et al. (2023) | DD | GPT3 | T | BLEU,ROUGE, BERTScore, human eval. | PH | - | zh |
| [122] Toplyn (2023) | H | DialoGPT | T | Human eval. | J | Incongruity | en |
| [26] Chen et al. (2024) | DD | Various LLMs | T | A/B testing, Success Rate Diversity | J | - | en, zh |
| [25] Chen et al. (2024c) | DD | LLaVA-1.5 (7B) | T, V | human and automatic | J | - | en |
| [41] Goel et al. (2024) | DD | Zephyr-7B-Beta, GPT4 | T | pre, rec, F1, acc | J | - | en |
| [42] Gorenz and Schwarz (2024) | DD | ChatGPT | T | Human eval. | J | - | en |
| [93] Mirowski et al. (2024) | DD | ChatGPT, BARD | T | Creativity Support Index, Human eval. | PH | - | en |
| [107] Ravi et al. (2024) | DD | LLaMA2-70B, BART-large, GPT4 | T | Win-Tie-Rate | CH | - | en |
| [119] Tikhonov et al. (2024) | DD |  | T | human eval. | J | - | en |
| [125] Wang et al. (2024) | DD | ChatGPT, LLaMA LLaVA | T, I | human eval. | J | - | en |
| [132] Xu et al. (2024) | DD | Various LLMs | T | Ambiguity, Dist, surprise, WIR | J | - | en |
| [135] Zeng et al. (2024) | H | GAN | T | Ambiguity, Dist-n | J | Surprise-disambiguation theory | en |
| [138] Zhong et al. (2024) | DD | Various LLMs | T, I | NDCG, human eval. | J | - | en, zh, ja |

For each model, the type of architecture (RB: rule-based, DD: data-driven, H: hybrid), modality/-ies (T: text, A: audio, I: image, V: video), evaluation metrics (NDCG: Normalized Discounted Cumulative Gain), humor genre (J: jokes, CH: conversational humor, PH: performance humor), humor theory it is based on (if applicable), and the language(s) of the dataset used to train/test the model is mentioned.



<!-- page 0016 -->

architecture where domain-adaptive pre-training is used to design three specialized encoders—one for sarcasm detection, one for parody detection, and one for humor detection—of which the outputs are ultimately concatenated before classification takes place. Inácio and Oliveira [57], on the other hand, follow the approach of Gu and Budhkar [44], and use a pre-trained transformer—in this case BERTimbau [114], a Brazilian-Portuguese BERT model—combined with additional feature representations to predict humor in tweets, but report that they failed to perform an extensive hyperparameter search.

Apart from humor detection, Zeng et al. [136] also develop a model to evaluate the sense of humor in social media users. In this study, *sense of humor* is measured by two criteria: one’s ability to generate humor and to appreciate humor. Based on these criteria, one of three sense of humor labels was assigned to each user: low, medium, and high. The task of sense of humor evaluation could therefore be defined as a multiclass problem. To tackle this problem, the authors propose a **social context graph (SCOG)** that consists of three components: a node representation, graph representation, and a classification component. First, the node representation component contains textual information—collections of usernames, user interactions, posts, and comments—and non-textual information, such as the number of comments, likes, or posts written by a user. These are encoded by a BERT model (textual info) and a Feed-Forward Neural Network or FFNN (for non-textual info). In a second step, a **graph neural network (GNN)** is used to learn these node representations. Then, the output is sent to the classification component which consists of two independent single-layer FFNNs (one for binary humor recognition, one for sense of humor evaluation), followed by a softmax function. The SCOG model achieved an F1-macro score of up to 62.7%, which is more than 10% higher than the best reported baseline model (RoBERTa).

*Other methods.* As mentioned above, we observed that older methodologies, such as classical machine learning methods, static word vectors, and earlier neural networks are still used frequently for certain tasks in recent humor detection literature, as explained below. The reason for this is that they are competitive with state-of-the-art pre-trained transformers, making them still relevant for humor detection. In addition, since such methods are feature-based, they have the advantage that specific theories of humor can be tested through feature engineering, making them not only competitive with LLMs, but also relevant for fundamental humor research. We therefore discuss a number of papers using these methods, and show how they contribute to automatic humor detection.

Kayastha and Redei [65] used GloVe embeddings [101] with a **Gated Recurrent Unit (GRU)** to detect humor in “That’s what she said” jokes. Precision and recall of 89.2% and 84.7% were reported, indicating strong improvements compared to the previous state-of-the-art for this task, which obtained a precision and recall of 71.4% and <20%, respectively. Similarly, Ren et al. [108] propose an LSTM network enriched with attention for humor recognition. Their approach consists of a pronunciation unit, which consists of a character-based **Convolutional Neural Network (CNN)**,[^5] a syntax unit, consisting of another CNN using part-of-speech (PoS) tag information, and a lexical unit, which uses WordNet [92] to resolve polysemy. The results show that their model performs on par with BERT for the task of pun detection (approx. 89% F1-score, depending on the experimental setting) and that it outperforms other existing neural methods. In other work, Fahim et al. [40] use an ensemble of statistical models to detect humor in a Kaggle dataset[^6] and obtain an F1-score of 93%. An ablation study showed that the SVM model contributed the most, whereas the decision tree and AdaBoost models yielded lowest individual performances. Similarly, De Marez et al. [32] designed an ensemble of various GA$^2$M models, which each represent a cognitive humor theory

[^5]: This pronunciation unit is in other words not based on audio data, but on text, which is used as a proxy for pronunciation.

[^6]: https://www.kaggle.com/datasets/amaammansuri/humor-detection [last accessed March 2025].



<!-- page 0017 -->

based on manually engineered features. The results showed the ensemble’s effectiveness in humor detection, and an ablation study provided insights into which engineered humor theory contributed the most to the model’s performance; the relief theory. Nevertheless, a BERT baseline outperformed the proposed approach.

*5.1.2 Multimodal Humor Models.* In contrast to unimodal models, we observe that all multimodal approaches except one use pre-trained language models for text processing. Deng et al. [33] use GloVe embeddings with bidirectional LSTM layers instead of a pre-trained transformer as the textual component in a fusion model for humor detection in the UR-FUNNY dataset [47]. The techniques used for other modalities, such as image and audio processing, are dependent on the specific task and available data. For instance, Alnajjar et al. [3] describe a system to detection humor and its intensity based on text and audio data. Specifically, they use laughing track data and transcriptions of the TV show “Friends” to predict when and how long the laughing track in unseen excerpts occur. To obtain text and audio representations, BERT and HuBERT [55] are used, respectively, and combined in a neural network which initially applies pooling to both representations, concatenates them, and applies dropout before sending the output to a final fully connected layer. Results show that the model is accurate in 78% of the cases, with a mean absolute error of 600 milliseconds.

In other work, models combining text and image data that perform a wide variety of humor detection tasks have been presented. Similarly to Alnajjar et al. [3] described above, Kuznetsova and Strapparava [74] present a model for laughter detection, but focus on text and vision data, rather than text and audio, and apply this task to stand-up comedy, instead of sitcoms. To perform the task, an SVM and a FFNN are used. To extract features, BERT-based embeddings (for the text data), and VideoMAE [120] (for the visual data) were used. Both unimodal and multimodal experiments were conducted, and the results indicate that visual data is more informative than textual data, as the models based on text only yield considerably lower results. Furthermore, Koutlis et al. [70] present MemeTector for detecting humor in memes. The model consists of the existing ViT model [35] enriched with an attention module. In addition, TextFuseNet is used to extract text boundaries from the image [134]. Experiments show that the proposed approach outperforms the original ViT model and other existing approaches, such as ResNet [48]. In related work, Tanaka et al. [117] hypothesized that memes are characterized by an incongruity between the image and the caption, and that such incongruity could be detected by subtracting the feature vectors of the image with the feature vectors of the caption. Experiments with CLIP [105] indicate improvements over baselines, but make clear that the task is still challenging, since accuracy scores do not exceed 60%.

Furthermore, Hessel et al. [51] tackle tasks related to funny cartoon captions. The first task, matching, consists of selecting the appropriate caption from a list of five, given a cartoon image. The authors report zero-shot and few-shot results with GPT (3, 3.5, 4), and propose fine-tuned models with T5, CLIP, and OFA [126]. In the end, few-shot GPT-4 yielded the highest performance with an accuracy of 85%, compared to a human upper bound of 94%. The second task comprises predicting which of two presented captions was rated the highest. The same models were utilized for this task as for task 1, and similarly to that task, few-shot GPT-4 yielded highest accuracy (73% compared to a human performance of 87%). In sum, more recent GPT models have shown improvements in humor detection, but still perform subpar compared to humans.

Finally, humor models that process all three modalities—text, audio, and vision—primarily comprise performance humor systems. For instance, Chauhan et al. [21] use the M2H2 dataset, described in Section 3, for multimodal, multilingual, and emotion-aware humor recognition in sitcoms. Concretely, their method utilizes a humor prediction component which consists of a transformer block. Then, a sentiment vector and emotion vector, each obtained from the output of two separate linear layers, are concatenated and multiplied with the output of the linear layer of the humor component



<!-- page 0018 -->

to arrive at a sentiment and emotion-aware humor matrix. During training, two loss functions are backpropagated: binary cross entropy (obtained from sigmoid function for humor detection), and cross entropy (obtained from softmax function for sentiment and emotion classification). The presented results showed substantial gains over baseline models in all experimental settings (unilingual vs. multilingual and unimodal vs. multimodal).

In similar work, Phukan et al. [102] propose QuMIN, a quantum multi-modal data fusion model for humor detection in the M2H2 dataset. Concretely, visual, acoustic and text features are extracted with Resnet [48], OpenSMILE [39], and FastText [14], respectively, and then concatenated and sent to a DialogueRNN [85]. The resulting output is sent through an attention network, dense layers, and a **variational quantum circuit (VQC)**, before applying layer normalization and softmax. The results show that QuMIN achieves substantially better performance than existing models on M2H2.

## 5.2 Humor Generation

### 5.2.1 *Unimodal Approaches.*

*Pre-trained language models.* In contrast to recent humor detection models, **all work on unimodal humor generation we found published since 2022 uses pre-trained language models.** A first trend we observe in recent research focusing on LLMs is **zero-shot/few-shot generation of ambiguous puns.** Gorenz and Schwarz [42], for instance, designed two experiments to investigate the humor generation capabilities of ChatGPT. First, both ChatGPT and laypeople (i.e., non-professional comedy writers) were asked to respond to various types of humorous prompts. Then, ChatGPT was asked to generate satirical news headlines to create parallel data for headlines written by human professionals. Afterward, Amazon Mechanical Turk workers blindly evaluated the human and AI generated responses. From the results it could be concluded that the jokes produces by ChatGPT were at least as funny or even funnier than the human counterparts, indicating that ChatGPT grasps the concept of humor.

In other work, Mittal et al. [96] present AmbiPun, a model designed for ambiguous pun generation, of which the input consists of a target pun word and two of its sense definitions. For instance the noun “drive”, which can both mean “motivation”, and “journey in a vehicle”. The output, on the other hand, comprises a list of pun sentences, such as “a boy saving up for a car has a lot of drive”. The approach consists of the following steps: first, 5 semantically related context words are generated with GPT3 for each of the word meanings of the pun word. Then, a fine-tuned T5 model is used to generate candidate pun sentences based on the pun word, its meanings, and the context words. Finally, humor classification is performed on the generated candidate sentences to rank them and select the final output sentence. AmbiPun was later used by Sun et al. [116] as a baseline model for the task of context-situated pun generation, which involves adding a context constraint.

Although the aforementioned papers report fair results, Xu et al. [132] argue that out-of-the-box LLMs do not generate high-quality puns, since they show the tendency to clarify ambiguity, rather than creating it, for which the authors use the term *lazy pun generation*. Similarly, Chen et al. [24] design a transformer for generating pun titles for scientific abstracts, compare it to ChatGPT, and report that “automatic systems clearly underperform relative to humans” (p. 62), highlighting the mixed results reported in recent humor generation experiments with LLMs.

A second trend we observed in papers on unimodal humor generation is a focus on **using LLMs as writing assistants for performance humor**. Mirowski et al. [93], for example, perform an experiment in stand-up comedy writing assistance with professional stand-up comedians at the 2023 Edinburgh Festival Fringe, and conclude that although more than 50% of the participants enjoyed working with AI, approximately 70% disagreed with the statement that the generated output feels unique, showing that LLMs still struggle with producing original content. Jentzsch and Kersting [60] arrive at the same conclusion after performing a manual analysis on jokes generated



<!-- page 0019 -->

by ChatGPT, and claim that over 90% of the 1008 generated jokes were the same 25 specific jokes. The prompt that was used however, “Tell me a joke, please!”, was not optimized for diversity, which emphasizes the importance of adequate prompt design in zero-shot joke generation. Compared to the previous work, which explored both zero-shot and few-shot (RAG) experiments, Li et al. [76] explored LLM fine-tuning for Chinese dialogue comedy. Interestingly, they show that fine-tuning GPT-3 [17] for this task does not improve performance. In short, **recent work on humor generation with LLMs presents rather negative conclusions.**

*Hybrid models.* Three hybrid approaches could be identified, which exploit both pre-trained language models and top-down heuristics or manually crafted resources. First, Tian et al. [118] propose a hybrid approach for puns generated based on homographs and homophones. The task consists of generating a pun, given a word pair consisting of a pun word and a target word. For instance, given the word pair *soled-sold*, where the pun word is *soled* and the target word is *sold*, a potential pun could be “The leather boots he was wearing were heavily abraded, and were *soled* at the store at half price.” Similarly to the AmbiPun model described above, this approach leverages linguistic ambiguity and heuristics to create puns by first retrieving a number of prototypical phrases for the target word, while ranking them according to semantic relevance to the pun word. In contrast to AmbiPun, which uses a reverse dictionary to obtain context words, Tian et al. [118] use a **Masked Language Modeling (MLM)** task to retrieve phrases containing the pun word and rank them according to both typicality and surprise. The middle-ranked phrase is then used for candidate pun generation to avoid it being too general or incompatible with the target word. A fine-tuned T5 model is used to generate such candidate pun phrases, and BERT-based classifier is used to rank the phrases and provide the final output decision.

In other work, Toplyn [122] developed the third version of a system named “Witscript” (original version is presented in Toplyn [121]), a system for generating humoristic punchlines based on a provided set-up. The original Witscript model first extracts nouns, noun phrases and named entities from said set-up line. Then, using Word2Vec, it is determined which of these two words or phrases are the least likely to co-occur in order to create a surprising effect. These key words/phrases are then used as *topic words*. Next, Word2Vec is used to generate 50 associations for both topic words. Afterward, three types of puns are generated: a juxtaposition, a word phrase in which a word has been substituted, and a word in which a syllable has been replaced to create a humorous effect (portmanteaux). Then, a wordplay score based on linguistic features is assigned to each pun as a form of evaluation; the pun with the highest word play score is selected, and an angle is generated with a fine-tuned BERT model to connect the input sentence and the generated pun. In the third version, a large part of the heuristics were replaced by GPT.

Finally, the third hybrid approach we identified is “PunIntended” [135], a **Generative Adversarial Network (GAN)** for pun generation inspired by the surprise-disambiguation humor theory. The GAN consists of a discriminator (BERT-large-uncased) and a generator (T5). The generator produces a pun by exploiting a pruned semantic tree of an input sentence obtained through WordNet and Stanza constituency parser. The discriminator, on the other hand, evaluates the puns produced by the generator. It was fine-tuned for the task of distinguishing between correct and incorrect interpretations of a pun using contrastive loss. For this task, artificially generated explanations were used as incorrect, negative samples, and correct explanations from an existing pun dataset were used as positive examples. To evaluate the GAN, puns were generated based on the ExPunations dataset [115]. The results show that this method outperforms a number of pun generation baselines, including both zero-shot LLMs and fine-tuned transformers.

5.2.2 *Multimodal Approaches.* We identified three multimodal generative humor approaches. First, Wang and Lee [125] present MemeCraft, a creative meme generator based on LLMs and



<!-- page 0020 -->

VLMs (Vision Language Models). MemeCraft uses meme template images as input data. These were mined from the Meme Generator dataset,<sup>7</sup> from which all offensive memes were filtered automatically and all captions/texts were removed. Then, for each image, a neutral description for that image is generated with LLaVA-7B. Afterward, a funny caption is generated based on a prompt that includes the topic (either *gender equality* or *climate change*), a stance (*for* or *against*), and one of six persuasion techniques used to convince the reader of that stance. Finally, a multimodal bi-transformer detects whether the generated memes are hateful, as a post-production safety mechanism. To evaluate MemeCraft, human evaluators rate authenticity, funniness, how well the intended message and stance were conveyed, how persuasive the meme is, and its hatefulness. After evaluation, the authors conclude that there was mainly room for improvement in the funniness metric, while MemeCraft scores relatively well on the other aspects.

Furthermore, Chen et al. [27] design a multitask **Chain-of-Humor** approach, which involves adding humor mind maps and **Chain-of-Thought (CoT)** reasoning in the prompt to break down the thought process behind humor generation. In addition, the model is fine-tuned with two auxiliary tasks: sentiment classification and humor rewriting in order to boost the quality of the produced outputs. An evaluation on the TalkFunny dataset using various LLMs and VLMs shows that both the prompting strategies and multitask learning improve the humor generation capabilities of these models.

In similar work, [138] propose **Creative Leap-of-Thought (CLoT)** prompting as an alternative for CoT prompting for creative humor generation in the Oogiri-Go dataset, which is a Chinese humor game in which a person must reply with a funny response given a prompt (either text or image). They hypothesize that the latter is more efficient in logical problem solving, whereas the former is more appropriate for creative tasks. CLOT consists of two stages: first, associable instruction fine-tuning, during which a model learns to generate creative associations between seemingly unrelated concepts, and secondly, self-refinement, during which the model reflects and provides feedback on its own ideas to improve the final output. The proposed CLOT prompting was evaluated for various LLMs and VLMs using both human evaluations and automatic metrics, and it was shown that it is more efficient for creative generation tasks than LoT prompting.

## 6 Annotation and Evaluation

Due to the subjective nature of humor, and a lacking gold standard, two of the most foundational challenges are how to annotate humor on the one hand, and how to evaluate generative models on the other hand. In this section, we will therefore describe how existing work approaches these tasks, and what gaps remain in the state-of-the-art.

### 6.1 Detection

The evaluation of humor detection models is essentially the same as for other classification tasks: precision, recall, F1-score, and/or accuracy are used for the evaluation of both binary and multiclass classification tasks. Other metrics that are used (albeit infrequently) are **Area Under the Curve (AUC)**, **True Positive/Negative Ratio (TPR, TNR)**, cross-entropy loss, Cohen’s Kappa, and Pearson/Spearman correlation tests (for rating tasks). Regarding the collection of gold standard labels, annotators are typically asked to determine whether a series of data points are humorous or not. This can be done either in binary fashion (yes/no) or through a multiclass approach (Likert scores).

Since, as mentioned, humor is subjective, annotation tasks need to be setup carefully in order to obtain high-quality labels. Therefore, Loakman et al. [84] argue that the following types of

<sup>7</sup>https://www.kaggle.com/datasets/electron0zero/memegenerator-dataset



<!-- page 0021 -->

**annotator information should be reported by default in future work:** demographic info (e.g., age, gender, and language proficiency), logistic info (e.g., number of annotators, how they were recruited and rewarded), and training info (annotator guidelines, training examples, agreement, etc.). Also mindful of the subjective nature of humor, Meaney [89] designed not one but two binary labeling tasks, where the distinction between perceived humor and intended humor is made in order to account for **annotator opinions** (as mentioned in Section 4). In addition, they also ask the annotators to rate offensiveness in jokes to anticipate **personal sensitivities**. Finally, the authors did not only ensure that each training instance was annotated by multiple annotators from different age groups (in order to avoid bias as a result of the variable age), but also ensured that the annotators had cultural background as the writers of the texts (USA). They argued that this setup minimizes the number of misinterpretations during annotation that are the result of a gap in the background knowledge of the annotator.

### 6.2 Generation

To evaluate generative humor models, **both human and automatic methods have been used in previous work.** Human evaluation, on the one hand, can include evaluation by means of comparison, such as in A/B testing (e.g., [26]), or by calculating binary success rate, i.e., the ratio of times the humor generator successfully completed a specific task (e.g., [96]). On the other hand, manual evaluation can involve a qualitative analysis (e.g., [60]), or assigning a score to fine-grained aspects of humor. Examples of said aspects we found in this survey are the following: funniness [23, 25, 42, 76, 96, 119, 125], creativity/originality/authenticity [25, 119, 125], ambiguity [118], offensiveness [119], persuasiveness [125], coherence [76, 96], relevance/informativeness [25, 125], an overall score [76, 122], and a Creativity Support Index [93].

While human evaluators can provide the most nuanced feedback, they are subject to personal and cultural preferences. This means that many annotators from balanced demographic groups must be included to provide representative evaluations, which is not only expensive, but also challenging from a logistic perspective. Zeng et al. [135] take a radical stance in this issue and propose to use only automatic evaluation for humor generation tasks. Specifically, they use ambiguity and distinctiveness. The former is based on Kao et al. [64], who use ambiguity as a proxy for humor, and quantify this concept by computing the entropy of the joint probability distribution of sentence meanings. Higher entropy therefore signifies more ambiguity and therefore humor. Distinctiveness, on the other hand, comprises lexical diversity between generated outputs based on unigrams and bigrams (Dist-1 and Dist-2, respectively). While claiming that automatic methods provide objective scoring, however, they also mention that ambiguity may not always reflect pun quality, and that distinctiveness overlooks aspects such as coherence and semantics. Therefore, the authors conclude that “these metrics alone do not intuitively capture the characteristics of the pun generation task” [135] (p. 2125).

Another method includes utilizing humor detection or rating models for automatic evaluation. Góes et al. [46], for instance, explore the humor evaluation capabilities of GPT-4. They show, however, that there is only a weak correlation between the judgments of GPT-4 and human evaluators. The aforementioned results indicate that in spite of their speed, scalability, and low cost, automatic evaluation methods are not necessarily accurate alternatives that reflect human judgment, which is also an issue in other NLG (or seq2seq) tasks, such as machine translation, text summarization, dialogue completion, and so on. Regardless of the advantages and disadvantages of both human and automatic evaluation, it is apparent that for generation tasks, different papers use completely different types and combinations of evaluation metrics. In other words, there is still **no uniform evaluation framework** to evaluate humor generation models which allows for the comparison of models across research projects.



<!-- page 0022 -->

## 7 Interpretability and Explainability

This section addresses how interpretability and explainability efforts help gaining insights into what LLMs actually know and *understand* about humor. Humor is considered an AI-complete problem [129], making interpretability a valuable lens for assessing humor as a way to evaluate how LLMs perform on creative tasks that demand human-like reasoning and cognition. We review the relationship between AI-based humor detection and generation techniques, along with relevant datasets, and existing linguistic and psychological humor knowledge and research outside of AI. We consider how insights from the latter inform AI approaches and how AI, in turn, might contribute to humor research.

Interpretability aims to show a clear causal link from the model input or the model working to the output [80]. In contrast, explainability refers to those methods that allow human understanding of the internal model workings. While distinct terms,[^8] their approaches can overlap. Ideally, a system possesses both qualities: a causal input-to-output link that accurately represents the model’s functioning and is also understandable by humans.

Within computational humor, interpretability and explainability operate in **two directions**: existing knowledge about humor that is implemented in humor systems (direction *from*), and working humor systems that contribute towards specifying our knowledge about humor or creating an entire new humor theory, explicitly or inadvertently (direction *to*). In practice, these two directions are not as extreme, because humor knowledge is only partially considered or contributed to.

### 7.1 The Direction *from*

The direction *from* contains theory-driven or symbolic explanations. Interpretability is by design: models, corpora, or feature sets are explicitly built around cognitive humor theories, symbolic humor rules, or well-defined linguistic humor features.

*Datasets.* Tseng et al. [123] provide a corpus of 3,365 Chinese jokes annotated with explicit *humor skills* (e.g., double meaning) and *intents*, making humorous elements explicit based on theoretical humor-building blocks.

Tanaka et al. [117] explicitly model meme-caption incongruity by subtracting the caption’s CLIP embedding from the image’s CLIP embedding, improving meme detection accuracy 4% (totaling 57.7%) over a ViT baseline.

Liu and Hou [83] applied the incongruity theory of humor (specifically, Script-Based Semantic Theory) to verbal humor, measuring setup uncertainty and setup-punchline incongruity using entropy on density matrices, representing semantic dispersion in a higher-dimensional space. An SVM trained on these theory-driven features achieved higher F1 scores than one using baseline features, aligning with theoretical definitions. However, performance (max F1 63.2%) remained below black-box methods on the same dataset (Section 4.2, task 1).

De Marez et al. [32] use an ensemble of interpretable **generalized additive models (GAMs)**, each mapping numeric proxy features onto a specific humor theory by design. The GAMs’ interpretability allows verifying the proxies and pinpointing feature contributions (which can also be seen as a direction *to* humor knowledge). This approach also showed lower performance compared to black-box methods on the same dataset, with a maximal F1 of 85%.

Bunescu and Uduehi [19] evaluate several surprise measures based on BERT’s word probability distributions for predicting humorous headlines, based on derivatives of the incongruity theory of humor. Using these measures as features in logistic regression, they found surprise outperformed

[^8]: There is no generally agreed upon definition of interpretability and explainability, but for clarity, in this review they are considered to mean as is stated in Linardatos et al. [80].



<!-- page 0023 -->

random baselines, but not better than information content alone (negative log of LLM probability). Combining surprise, information content, and entropy yielded only a 0.17% F1 increase, hinting surprise captures unique aspects of creative language use. The combined model still lags behind a black-box classifier that uses contextual representations from a frozen LM and an FCN (F1 84.5%).

The four unit humor detection method of Ren et al. [108] draws from humor linguistics, focusing on incongruity and ambiguity in language. Their approach offers modular interpretability, with three units directly corresponding to specific humor sources: pronunciation ambiguity (heterographic puns), lexical ambiguity (homographic puns), and structural ambiguity. Ablation studies confirm each unit’s importance, showing heterographic puns suffer most without the pronunciation understanding unit, while homographic puns decline without the lexicon understanding unit.

*Generation.* Generation approaches that are purely data-driven by definition do not incorporate existing humor knowledge and do hence not fall under the direction *from*. The hybrid approaches discussed in Section 5.2.1 usually do, but since every hybrid method necessarily has an uninterpretable neural part, the focus in this section lies on how the interpretable part leverages humor knowledge.

Tian et al. [118] propose a hybrid model for generating puns, explicitly incorporating known humor mechanisms: ambiguity, distinctiveness of viewpoints, and surprising effect of an incongruity and its resolution. A multilabel classifier learns pun structure (through the ambiguity and distinctiveness) to guide GPT-2 (also contributing to the direction *to*), while surprise is introduced via targeted word replacement, creating an unexpected yet interpretable meaning switch. Generated puns outperformed baselines in informativeness and funniness.

Toplyn [122] (and Toplyn [121]) introduces Witscript, a hybrid approach blending a symbolic joke-writing algorithm using an LLM (for content) and NLP tools (for wordplay). Its transparent steps trace joke generation to comedic heuristics, enhancing controllability, debuggability and explainability over purely neural models.

## 7.2 The Direction *to*

The direction *to* contains two main approaches. The first, explanation by free-text, provides a textual rationalization alongside a humor classification or instance, offering human-readable insights but risking hallucination or superficiality. The second uses post-hoc methods like saliency or feature importance aiming to uncover which features most influence model decisions, or to perform a humor analysis after the dataset is made. Such analyses reveal whether the model is exploiting superficial cues such as punctuation or deeper comedic signals.

### 7.2.1 *Explanation by Free-text.*

*Datasets.* Sun et al. [115] create *ExPUN*, an augmented version of the SemEval 2017 Task 7 puns dataset, annotated with distinctive keywords that make the text funny, short textual explanations and funniness ratings. They find that human-written explanations improve pun classification accuracy, while LLM-generated explanations lack the depth of human annotations, and human-annotated keywords produce better puns than automatically extracted ones.

In TalkFunny [27], a large-scale Chinese conversational humor dataset, each context-response humor pair features a step-by-step textual explanation called a *chain-of-humor*, and a *humor mind map*, a graph-like structure of entities and relations underlying the humor. Injecting these structured explanations into model training improved humor generation performance.

He et al. [50] introduce Chumor, a Chinese humor dataset containing 1,951 jokes paired with a human-written free-text explanation. A/B testing showed human explanations were preferred over those from LLMs (GPT-4o, ERNIE Bot by Baidu), which recurrently lacked cultural awareness,



<!-- page 0024 -->

struggled with Chinese homophones, misinterpreted puns, hallucinations, or insufficient contextual grounding.

*Detection.* Xu et al. [132] evaluate LLMs on providing CoT pun explanations (identifying the pun word, the alternative word, and their respective meanings). While most LLMs identify the pun word well, many (except top models like GPT-4-Turbo and Claude-3-Opus) struggle with the alternative word and its meaning in heterographic puns due to phonetic similarity. These top models approach or surpass human explanation quality (judged by GPT-4), showing strong ability especially for homographic puns. However, LLMs may still produce errors (pun type misclassifications, misidentifying pun elements, meaning fabrication), whose frequency was not checked.

Bogireddy et al. [13] use a COVID-19 humor dataset (texts/memes) annotated with humor facets to test detection models like RoBERTa and GPT-3 on humor detection and distinguishing adaptive/maladaptive humor. While GPT-3 underperformed RoBERTa, it uniquely provides explanations for its reasoning, rated as *good enough* by human annotators 60–71% of the time. However, these explanations can be generic and struggle with subtle humor, especially when lacking explicit insults or profanities.

Hessel et al. [51] evaluate models’ ability to explain cartoon humor via free-text generation. Larger models and few-shot learning improve performance, and using human-authored cartoon descriptions (mimicking high-level visual understanding) instead of raw images yields better explanations. However, machine explanations still lag behind human ones, with annotators preferring human writing 68% of the time even over the best model, GPT-4. While models often grasp the gist, they frequently make errors or miss humor’s nuance, indicating a lack of true human-like understanding.

Ko et al. [68] evaluate models on explaining funny videos using a dataset with timestamped textual explanations of funny moments. Their best method involved using zero-shot GPT-3.5 to convert video and audio content to detailed text descriptions, then using GPT-3.5 again to generate humor explanations from these descriptions. This approach captured multimodal nuances missed by transcript-only methods, achieving a human rating of 0.523—significantly better than using transcripts alone (0.385), though still below the human benchmark (0.792).

*Generation.* Jentzsch and Kersting [60] conducted a prompt-based experiment where ChatGPT indirectly explained its own top 25 generated jokes via a separate prompt (“*Can you explain why this joke is funny?*”). They found explanations mostly accurate (23/25) for standard jokes but noted struggles with jokes deviating from familiar patterns, where it tended to fabricate plausible rationales rather than admit uncertainty or absence of funniness. As an honorable note, they cautioned that such free-text explanations do “not necessarily reflect the system’s ability to understand humor”.

Tikhonov and Shtykovskiy [119] developed a humor interpretability approach using GPT-4. They instructed GPT-4 to analyze 30 human jokes, identify humor elements, and explain their effects. This analysis was compiled into a policy for humor generation. Their two-step generation process begins with GPT-4 creating novel associations related to a given topic (the creative phase), followed by combining these associations with the humor generation theory to produce jokes that follow the established principles.

7.2.2 *Post-hoc Explanation Methods.*

*Dataset.* Yang et al. [133] collected 785,000 COVID-19 humor posts from Facebook, annotated automatically using user *Haha* reactions. Lexico-semantic and affective analysis reveals correlations between humor scores and features like negative emotions, informal language, first-person pronouns, and lower linguistic complexity, while negatively associating with pleasant imagery,



<!-- page 0025 -->

positive sentiment, and contextual detail. This pattern suggests that humor often employs personal, emotionally charged language with simpler constructions.

Maronikolakis et al. [86] introduced a dataset of 131,666 English tweets from 184 real politicians and their parody accounts, using post-hoc linguistic feature analysis (unigrams and part-of-speech tags) to distinguish them. They found stylistic markers, not topic, were key differentiators: parody tweets were more personal and informal (first-person pronouns, contractions, slang), while real tweets were formal and structured (collective pronouns, proper grammar, function words).

*Detection.* Inácio et al. [58] compared models for Portuguese humor detection: three ML approaches (SVM with *content features*, **random forest (RF)** with *humor related features*, RF with both) and fine-tuned BERT. SHAP analysis showed all models used superficial features rather than understanding humor. Content models relied on punctuation and question words; humor models used named entities and concreteness, while confirming incongruity and ambiguity as known humor indicators. BERT mainly leveraged punctuation and question words rather than deeper comedic mechanisms.

To mitigate reliance on superficial cues, Inácio and Oliveira [57] created a corpus with micro-edited humor/non-humor pairs that contain similar surface characteristics but differing humor effects. SHAP analysis of a BERT model trained on this corpus revealed reliance on diverse textual elements (general words, punchline elements), with no single token holding disproportionate importance and less focus on irrelevant cues.

Ofer and Shahaf [97] show that their model can predict the most successful punchline in the Cards Against Humanity game, but also indicate that the models focus primarily on the punchline card, while disregarding context, and that feature importance analysis shows that short, offensive punchlines tend to win. These results indicate that although models may show high performance, they can still fail to grasp the concept of humor and tend to overfit.

Chen et al. [24] investigated LLM humor detection on Chinese data using gradient-based saliency maps (input × gradient) to compare base models, such as BERT and T5, with fine-tuned versions. Base models highlighted punctuation or special tokens, but after fine-tuning, they focused more on sentiment words or mismatched meanings, partially aligning with human perception. The authors concluded this indicates “a certain degree of humor understanding,” despite limitations like punctuation focus sometimes persisting, and argued that current knowledge bases are insufficient for true humor comprehension by LLMs.

Shatnawi et al. [112] developed a BERT + RoBERTa ensemble model for humor detection in edited news headlines. Their interpretability analysis identified BERT’s strong vocabulary overlap with the humor dataset as a key success factor. Furthermore, probing linguistic tasks (e.g., sentence length, part-of-speech) indicated that BERT captures surface, syntactic, and semantic knowledge hierarchically across its layers, which the authors state also contributes to its performance.

Li et al. [77] developed a humor captioning system using a new dataset of image-text pairs with humor scores. They trained a humor caption generator and a humor classifier. Interpretability methods (attention mapping, Grad-CAM, gradient magnitude analysis) revealed that both models focus on exaggerated or incongruous visual details, such as odd facial expressions or dramatic scenes. This aligns with the benign violation humor theory (cognitive incongruity that remains harmless), though the alignment is correlational, not symbolic or rule-based. The classifier also showed high attention to pronouns like *you*, suggesting audience engagement enhances humor perception.

Koutlis et al. [70] uses a trainable attention mechanism with vision transformers to distinguish image memes from regular images, enhancing performance and interpretability. Visualizing attention weights shows the model focuses on characteristic meme text patterns in text regions–ignoring



<!-- page 0026 -->

backgrounds–rather than analyzing entire sequences. For non-meme images containing text, the model recognizes differences in text formatting and placement, preventing misclassification.

Tangential to interpretable humor detection in the direction *from*, Merlo et al. [91] uses interpretable linguistic (but not necessarily humor-related or theory-inspired) markers to distinguish hurtful from inoffensive jokes. With an ablation study they found that content features related to negative stereotypes, moral defects, swear words, and ethnic slurs are the most influential in classifying jokes as offensive.

### 7.3 Discussion and Conclusion

We identify two primary directions for interpretability and explainability in AI humor systems: existing humor knowledge being implemented in humor systems (direction *from*, humor knowledge *in*), and working humor systems that contribute towards humor knowledge (direction *to*, humor knowledge *out*).

In the **direction *from***, existing humor knowledge is explicitly integrated through various means, such as annotating datasets with theoretical components, engineering features to represent humor concepts like incongruity or surprise, designing model architectures around humor mechanisms, or using symbolic rules to guide generation. Detection models explicitly built around or inspired by humor knowledge tend to underperform large black-box neural networks on the same tasks, illustrating the common accuracy versus interpretability tradeoff inherent in their faithful design. Generation methods that incorporate humor knowledge explicitly, like those using specific pun traits or joke-writing algorithms, are hybrid by default, aiming to guide model decisions while preserving some transparency. Although this often yields better control and debuggability than purely neural systems, it also introduces neural black-box components that reduce overall interpretability compared to what a purely symbolic pipeline would offer.

In the **direction *to***, we see contributions towards understanding how AI processes humor (or fails to) through either free-text explanations or post-hoc explanation methods. In general, the quality and reliability of free-text explanations generated by large language models for why something is funny is frequently found to be subpar compared to explanations created by humans. While LLMs show improving capabilities, especially in recent top models on specific tasks like pun analysis [132], they often struggle with subtlety, complex linguistic features, and can produce errors or hallucinations. Post-hoc interpretability methods like SHAP and saliency maps often reveal that models, even those with good task performance, rely on superficial cues (like punctuation, specific words, formatting, and offensiveness) rather than deeper humor understanding. Specialized approaches, such as targeted fine-tuning or using carefully constructed datasets, can mitigate this problem to a certain extent, leading models to focus more on textual or image regions that align better with human humor reasoning. Interestingly, we found no generation approaches that use post-hoc interpretability methods.

Crucially, the explainability methods associated with the direction *to* carry inherent caveats. First, when free-text explanations are self-explanations generated by the model itself, they risk becoming more plausible than faithful, potentially not reflecting the actual reasoning process behind the model [1], even though they might increase user trust when deceptive [111]. Most papers using LLMs for explanation focus on evaluating explanation quality against human standards rather than interrogating their faithfulness, often finding the LLM explanations lacking nuance, cultural context, or accuracy. The approach of Tikhonov and Shtykovskiy [119] sidesteps the faithfulness issue somewhat by leveraging generated free-text analysis as input (a policy guideline) for subsequent generation, rather than as a post-hoc explanation of an output. Second, classical post-hoc interpretability methods are criticized for being fragile and easy to misinterpret [59, 67]. Such post-hoc methods can further not be applied to close-sourced LLMs due to their unavailable



<!-- page 0027 -->

model internals. These methodological limitations are generally not addressed in the reviewed humor papers using them. Finally, due to the potential unreliability and indirect nature of the explainability methods in the direction to (both free-text and post-hoc), observing explainable behavior does not necessarily entail genuine humor understanding by the AI, as findings often highlight correlations rather than proven causal reasoning.

## 8 Discussion

In this section, our most important findings are discussed. The gaps presented in earlier survey papers, which were mentioned in the introduction, will be taken into consideration during this discussion. In addition, relevant future research directions based on remaining challenges will be suggested.

### 8.1 Annotation and Evaluation

Due to personal preferences, annotation and evaluation are two of the most foundational challenges in computational humor modeling. With respect to humor annotation, a positive evolution towards certain standard practices can be observed. First, Loakman et al. [84] argue that various types of demographic information should be reported in annotation experiments. In addition, Meaney [89] and Meaney et al. [90] propose an annotation setup where annotators have to distinguish between intended and perceived humor, and annotate offensiveness in humor. Furthermore, they argue that multiple annotators from varying demographics should assign labels to the same data points in order to establish high quality gold standard labels. These measures account for the subjective preferences and personal sensitivities in humor, and should therefore be considered standard practice in future work.

Regarding evaluation, on the other hand, we showed that there is currently no generally accepted evaluation paradigm that allows for (1) a comprehensive evaluation of humor models, and (2) comparability across research projects. This issue was already addressed in various survey papers published in 2020–2021 [4, 129], and likely contributes to the mixed results that have been reported for generative models in recent research, as also hypothesized in Li et al. [76]. Therefore, we argue that investigating what appropriate evaluation methods are should be prioritized in future work. As an initial template, we propose to use a multidimensional evaluation method, which accounts for (1) the diversity in humor mechanisms a single model can produce, (2) its appropriateness when producing jokes (accounting for the pragmatic and social context), and (3) originality, i.e., its ability to produce jokes that have not been seen during training. To test the validity of such a paradigm, it must be compared to human evaluations by testing their correlation.

### 8.2 Modalities and Genres of Humor

It has been mentioned that most previous computational humor research pertains to the modality of text, although humor is in reality a multimodal phenomenon. In this survey, we showed that more work has been done in multimodal research in recent years, especially for detection tasks. The main trend in the proposed approaches for these tasks is to utilize fusion models, which combine text embeddings (typically BERT-based), with auditive and visual components (e.g., ViT/CLIP and HuBERT/Wav2Vec, respectively) into a multilayer perceptron. For generation tasks, however, multimodality is still relatively understudied, although existing work has addressed tasks such as meme generation and cartoon caption generation.

Another issue, which has not been identified in previous survey papers, is an imbalance in the types of humor that are being studied. While Martin and Ford [88] claim that conversational humor constitutes most of our daily humor experiences, followed by performance humor, and finally jokes, this order is reversed when it comes to the amount of attention that is being spent to these genres



<!-- page 0028 -->

in computational humor research. As it is the goal of NLP research to make language models more human-like, it should be investigated how they can effectively generate humor in conversations in order to mimic human spontaneity and creativity. Combined with the aforementioned issues regarding evaluation, we argue that future work should focus on extrinsic evaluation of humor generation in conversations in order to tackle both issues at the same time.

### 8.3 WEIRD Problem

Winters [129] mentioned that most computational humor research is conducted for the English language, although humor verbalizations and perceptions vary between cultures and languages. This problem can be extended to the fact that most empirical data in research in general comes from Western, Educated, Industrialized, Rich, and Democratic areas [109]. This is known as the **WEIRD** problem, and can also be observed in existing humor corpora, as most contain English data or other Western Languages, such as French [104] and Portuguese [99]. In more recent humor datasets, however, we observe a trend towards a more frequent presentation of non-Western language data. Specifically, all 11 identified humor datasets published in 2024 contain at least 1 non-English language, indicating a positive evolution towards more diversity in the data utilized in computational humor research.

### 8.4 Pre-trained Language Models

For humor generation, all systems described in this paper utilized pre-trained language models. Although LLMs still do not match human performance when it comes to humor generation, there seems to be a consensus that LLMs are currently state-of-the-art in humor generation and outperform earlier methods with a large margin. As shown in the methods that were discussed in this survey, an important consideration to make is the design of the prompt. While it has been shown that complex CoT prompting leads to promising results, studies have also reported negative results using simple prompting strategies, which highlights the fact that LLM performance is very prompt dependent. Nevertheless, due to the aforementioned issues with evaluation, mixed results have been reported.

In spite of the successes of LLMs, and in contrast to humor generation systems, no specific trends could be observed in recent humor detection systems, meaning that they rely on a variety of different approaches: not only pre-trained language models, but also older neural approaches, statistical methods, and hybrid systems that involve manually crafted rules or resources. We found that for specific tasks, such methods can achieve comparable performance to state-of-the-art pre-trained language models, while providing more insights into humor mechanisms and humor theories. Future work in humor detection should therefore focus on comparing the usefulness of these different systems humor detection tasks and exploring the validity of existing humor theories in order to clarify the relevance of older methods in this era of LLMs.

### 8.5 Interpretability and Explainability

Interpretability and explainability in humor systems can occur in two directions: existing humor knowledge being implemented in humor systems (direction *from*, humor knowledge *in*), and working humor systems that contribute towards humor knowledge (direction *to*, humor knowledge *out*). The direction *from*, integrating known humor principles, often leads to models with higher interpretability but lower accuracy compared to black-box systems, or involves hybrid designs limiting full transparency. In the direction *to*, explanations and post-hoc analyses reveal models lack human depth and often rely on superficial cues, though specialized methods can encourage somewhat deeper processing aligned with human reasoning. However, the methods of the direction *to* are often unreliable, as generated explanations risk being plausible but unfaithful, while



<!-- page 0029 -->

post-hoc techniques face fragility issues and limited applicability in closed-source models. Overall, while hybrid approaches *from* offer some control and methods *to* show incremental progress, both directions currently highlight the significant remaining challenge in achieving genuine, verifiable humor understanding, often revealing shallow processing or inherent methodological limitations.

For future research, we advocate for the development of datasets containing theory-guided or generally correct explanatory annotations for explainability purposes. As evidence suggests they can facilitate better explanations and help models understand humor mechanisms. Explainability methods then demonstrate to users whether and how these datasets help teaching models about humor. Ideally, the datasets should be large-scale, multimodal, and multilingual.

Hybrid approaches that combine interpretability with neural components currently offer an advantageous balance between creativity and model transparency. While these primarily emerge from the direction *from* of humor knowledge implementation, we propose extending their scope to encompass both the directions *from* and *to*. This integration could, among other interpretability methods, be achieved by applying post-hoc interpretability methods to these hybrid approaches to confirm, challenge or deepen our understanding of their functioning.

Interpretability analyses in the direction *to* are subject to interpretation–a characteristic that presents both advantages and challenges. Their flexibility in interpretation can lead to biased confirmation of existing theories, especially through selective example use. However, this openness also provides opportunities to develop novel and robust humor theories by generalizing insights gained from interpretability, irrespective of initial expectations. To this end, models should be rigorously put to the test based on general interpretability insights. Since current methods often identify superficial features, researchers should for instance seek to discover adversarial cases, potentially creating adversarial datasets, and leverage these to contribute against superficial model reasoning.

Additionally, we identify two unexplored interpretability directions holding promise for computational humor. First, researchers should leverage the trend toward test-time computation in AI, exemplified by reasoning models. Humor systems could explicitly utilize transparent reasoning processes, possibly intervening or debugging within their inference pathways. These models can contribute in both the direction *from* (showing how features are utilized) and the direction *to* (illustrating how humor is reasoned about). However, future research must determine if transparent reasoning tokens genuinely reflect model-internal reasoning or remain comparable to existing CoT approaches regarding faithfulness. Second, mechanistic interpretability, which aims to reverse-engineer language models to uncover precise causal mechanisms from inputs to outputs [11], has yet to be applied to computational humor. Even partial causal findings would represent significant progress toward developing a computational humor theory. This approach is primarily applicable in the direction *to*, potentially revealing how models actually process and generate humor.

Pursuing these directions holds the potential not only to create more trustworthy and effective humor systems but also to advance our fundamental understanding of humor itself.

## References

[1] Chirag Agarwal, Sree Harsha Tanneru, and Himabindu Lakkaraju. 2024. Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models. 10 pages. arXiv:2402.04614. Retrieved from https://arxiv.org/abs/2402.04614

[2] Hend Alkhalifa, Fetoun Alzahrani, Hala Qawara, Reema Alrowais, Sawsan Alowa, and Luluh Aldhubayi. 2022. A dataset for detecting humor in arabic text. In *Proceedings of the 5th International Conference on Natural Language and Speech Processing (ICNLSP 2022)*. Mourad Abbas and Abed Alhakim Freihat (Eds.), ACL, Trento, Italy, 219–225. Retrieved from https://aclanthology.org/2022.icnlsp-1.25

[3] Khalid Alnajjar, Mika Hämäläinen, Jörg Tiedemann, Jorma Laaksonen, and Mikko Kurimo. 2022. When to laugh and how hard? A multimodal approach to detecting humor and its intensity. In *Proceedings of the 29th International*



<!-- page 0030 -->

*Conference on Computational Linguistics*. Nicoletta Calzolari, Chu-Ren Huang, Hansaem Kim, James Pustejovsky, Leo Wanner, et al. (Eds.), International Committee on Computational Linguistics, Gyeongju, Republic of Korea, 6875–6886. Retrieved from https://aclanthology.org/2022.coling-1.598

[4] Miriam Amin and Manuel Burghardt. 2020. A survey on approaches to computational humor generation. In *Proceedings of the 4th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature*. Stefania DeGaetano, Anna Kazantseva, Nils Reiter, and Stan Szpakowicz (Eds.), International Committee on Computational Linguistics, 29–41. Retrieved from https://aclanthology.org/2020.latechclfl-1.4

[5] Shahin Amiriparian, Lukas Christ, Alexander Kathan, Maurice Gerczuk, Niklas Müller, Steffen Klug, Lukas Stappen, Andreas König, Erik Cambria, Björn W. Schuller, and Simone Eulitz. 2024. The muse 2024 multimodal sentiment analysis challenge: Social perception and humor recognition. In *Proceedings of the 5th on Multimodal Sentiment Analysis Challenge and Workshop: Social Perception and Humor (MuSe’24)*. ACM, New York, NY, USA, 1–9. DOI:https://doi.org/10.1145/3689062.3689088

[6] Xiao Ao, Danae Sanchez Villegas, Daniel Preoțiuc-Pietro, and Nikolaos Aletras. 2022. Combining humor and sarcasm for improving political parody detection. In *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*. Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz (Eds.), ACL, Seattle, United States, 1800–1807. DOI:https://doi.org/10.18653/v1/2022.naacl-main.131

[7] Aseem Arora, Gaël Dias, Adam Jatowt, and Asif Ekbal. 2022. Transfer learning for humor detection by twin masked yellow muppets. In *Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)*. Yulan He, Heng Ji, Sujian Li, Yang Liu, and Chua-Hui Chang (Eds.), ACL, Online only, 1–7. DOI:https://doi.org/10.18653/v1/2022.aacl-short.1

[8] Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, and Michael Auli. 2020. wav2vec 2.0: A framework for self-supervised learning of speech representations. In *Proceedings of the 34th International Conference on Neural Information Processing Systems (NIPS’20)*. Curran Associates Inc., Red Hook, NY, USA, Article 1044, 12 pages.

[9] Alexander Baranov, Vladimir Kniazhevsky, and Pavel Braslavski. 2023. You told me that joke twice: A systematic investigation of transferability and robustness of humor detection models. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*. Houda Bouamor, Juan Pino, and Kalika Bali (Eds.), ACL, Singapore, 13701–13715. DOI:https://doi.org/10.18653/v1/2023.emnlp-main.845

[10] Sriphani Bellamkonda, Maithili Lohakare, and Shaswat Patel. 2022. A dataset for detecting humor in telugu social media text. In *Proceedings of the Second Workshop on Speech and Language Technologies for Dravidian Languages*. Bharathi Raja Chakravarthi, Ruba Priyadharshini, Anand Kumar Madasamy, Parameswari Krishnamurthy, Elizabeth Sherly, and Sinnathamby Mahesan (Eds.), ACL, Dublin, Ireland, 9–14. DOI:https://doi.org/10.18653/v1/2022.dravidianlangtech-1.2

[11] Leonard bereska and Efstratios Gavves. 2024. Mechanistic Interpretability for AI Safety – A Review. Preprint: https://arxiv.org/abs/2404.14082

[12] Kim Binsted and Graeme Ritchie. 1994. An implemented model of punning riddles. In *Proceedings of the 12th AAAI National Conference on Artificial Intelligence (AAAI’94)*. AAAI, 633–638.

[13] Neha Reddy Bogireddy, Smriti Suresh, and Sunny Rai. 2023. I’m out of breath from laughing! I think? A dataset of COVID-19 Humor and its toxic variants. In *Companion Proceedings of the ACM Web Conference 2023 (WWW’23 Companion)*. Association for Computing Machinery, New York, NY, USA, 1004–1013. DOI:https://doi.org/10.1145/3543873.3587591

[14] Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. 2016. Enriching word vectors with subword information. 12 pages. arXiv:1607.04606. Retrieved from https://arxiv.org/abs/1607.04606

[15] Hugo Albert Bonet, Aina Magraner Rincón, and Alba Martínez López. 2023. Detection, classification and quantification of hurtful humor (HUHU) on twitter using classical models, ensemble models, and transformers. In *Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2023) co-located with the Conference of the Spanish Society for Natural Language Processing (SEPLN 2023), Jaén, Spain, September 26, 2023*. Manuel Montes-y-Gómez, Francisco Rangel, Salud María Jiménez-Zafra, Marco Casavantes, Begoña Altuna, Miguel Ángel Álvarez-Carmona, Gemma Bel-Enguix, Luis Chiruzzo, Iker de la Iglesia, Hugo Jair Escalante, Miguel Ángel García Cumbreras, José Antonio García-Díaz, José Ángel González Barba, Roberto Labadie Tamayo, Salvador Lima, Pablo Moral, Flor Miriam Plaza del Arco, and Rafael Valencia-García (Eds.), CEUR Workshop Proceedings, Vol. 3496, CEUR-WS.org. Retrieved from https://ceur-ws.org/Vol-3496/huhu-paper6.pdf

[16] Mark Boukes, Giselinde Kuipers, Zilin Lin, and Savvas Zannettou. 2024. The faces and forms of pandemic humor: Exploring Covid-19 memes with visual machine learning. *Journal of Quantitative Description: Digital Media* 4 (2024), 1–59. DOI:https://doi.org/10.51685/jqd.2024.icwsm.6



<!-- page 0031 -->

[17] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. 2020. Language models are few-shot learners. 75 pages. arXiv:2005.14165. Retrieved from https://arxiv.org/abs/2005.14165

[18] Syed Husnain Haider Bukhari, Anusha Zubair, and Muhammad Umair Arshad. 2023. Humor detection in english-urdu code-mixed language. In *Proceedings of the 2023 3rd International Conference on Artificial Intelligence (ICAI)*. 26–31. DOI: https://doi.org/10.1109/ICAI58407.2023.10136656

[19] Razvan C. Bunescu and Oseremen O. Uduehi. 2022. Distribution-based measures of surprise for creative language: Experiments with humor and metaphor. In *Proceedings of the 3rd Workshop on Figurative Language Processing (FLP)*. Debanjan Ghosh, Beata Beigman Klebanov, Smaranda Muresan, Anna Feldman, Soujanya Poria, and Tuhin Chakrabarty (Eds.), ACL, Abu Dhabi, UAE (Hybrid), 68–78. DOI: https://doi.org/10.18653/v1/2022.flp-1.10

[20] Aayushi Chaudhari, Chintan Bhatt, Achyut Krishna, and Pier Luigi Mazzeo. 2022. VITFER: Facial emotion recognition with vision transformers. *Applied System Innovation* 5, 4 (2022), 1–16. DOI: https://doi.org/10.3390/asi5040080

[21] Dushyant Singh Chauhan, Gopendra Vikram Singh, Aseem Arora, Asif Ekbal, and Pushpak Bhattacharyya. 2022. A sentiment and emotion aware multimodal multiparty humor recognition in multilingual conversational setting. In *Proceedings of the 29th International Conference on Computational Linguistics*. Nicoletta Calzolari, Chu-Ren Huang, Hansaem Kim, James Pustejovsky, Leo Wanner, Key-Sun Choi, Pum-Mo Ryu, Hsin-Hsi Chen, Lucia Donatelli, Heng Ji, Sadao Kurohashi, Patrizia Paggio, Nianwen Xue, Seokhwan Kim, Younggyun Hahm, Zhong He, Tony Kyungil Lee, Enrico Santus, Francis Bond, and Seung-Hoon Na (Eds.), International Committee on Computational Linguistics, Gyeongju, Republic of Korea, 6752–6761. Retrieved from https://aclanthology.org/2022.coling-1.587

[22] Dushyant Singh Chauhan, Gopendra Vikram Singh, Navonil Majumder, Amir Zadeh, Asif Ekbal, Pushpak Bhattacharyya, Louis-philippe Morency, and Soujanya Poria. 2021. M2H2: A multimodal multiparty hindi dataset for humor recognition in conversations. In *Proceedings of the 2021 International Conference on Multimodal Interaction (ICMI’21)*. Association for Computing Machinery, New York, NY, USA, 773–777. DOI: https://doi.org/10.1145/3462244.3479959

[23] Yanran Chen and Steffen Eger. 2023. Transformers go for the LOLs: Generating (humourous) titles from scientific abstracts end-to-end. In *Proceedings of the 4th Workshop on Evaluation and Comparison of NLP Systems*. Daniel Deutsch, Rotem Dror, Steffen Eger, Yang Gao, Christoph Leiter, Juri Opitz, and Andreas Rücklé (Eds.), ACL, Bali, Indonesia, 62–84. DOI: https://doi.org/10.18653/v1/2023.eval4nlp-1.6

[24] Yuyan Chen, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Bang Liu, and Yunwen Chen. 2023. Can pre-trained language models understand chinese humor?. In *Proceedings of the 16th ACM International Conference on Web Search and Data Mining (WSDM’23)*. Association for Computing Machinery, New York, NY, USA, 465–480. DOI: https://doi.org/10.1145/3539597.3570431

[25] Yuyan Chen, Songzhou Yan, Zhihong Zhu, Zhixu Li, and Yanghua Xiao. 2024. XMeCap: Meme caption generation with sub-image adaptability. In *Proceedings of the 32nd ACM International Conference on Multimedia (MM’24)*. Association for Computing Machinery, New York, NY, USA, 3352–3361. DOI: https://doi.org/10.1145/3664647.3681332

[26] Yang Chen, Chong Yang, Tu Hu, Xinhao Chen, Man Lan, Li Cai, Xinlin Zhuang, Xuan Lin, Xin Lu, and Aimin Zhou. 2024. Are U a joke master? Pun generation via multi-stage curriculum learning towards a humor LLM. In *Findings of the Association for Computational Linguistics: ACL 2024*. Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.), ACL, Bangkok, Thailand, 878–890. DOI: https://doi.org/10.18653/v1/2024.findings-acl.51

[27] Yuyan Chen, Yichen Yuan, Panjun Liu, Dayiheng Liu, Qinghao Guan, Mengfei Guo, Haiming Peng, Bang Liu, Zhixu Li, and Yanghua Xiao. 2024. Talk funny! a large-scale humor response dataset with chain-of-humor interpretation. *Proceedings of the AAAI Conference on Artificial Intelligence* 38, 16 (2024), 17826–17834. DOI: https://doi.org/10.1609/aaai.v38i16.29736

[28] Luis Chiruzzo, Santiago Castro, Santiago Góngora anad Aiala Rosá, J. A. Meaney, and Rada Mihalcea. 2021. Overview of HAHA at IberLEF 2021: Detecting, rating and analyzing humor in spanish. In *Procesamiento del Lenguaje Natural*. 257–268.

[29] Luis Chiruzzo, Santiago Castro, and Aiala Rosá. 2020. HAHA 2019 dataset: A corpus for humor analysis in spanish. In *Proceedings of the 12th Language Resources and Evaluation Conference*. Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (Eds.), European Language Resources Association, Marseille, France, 5106–5112. Retrieved from https://aclanthology.org/2020.lrec-1.628/

[30] Lukas Christ, Shahin Amiriparian, Alexander Kathan, Niklas Müller, Andreas König, and Björn W. Schuller. 2024. Towards multimodal prediction of spontaneous humor: A novel dataset and first results. *IEEE Transactions on Affective Computing* 16, 2 (2024), 1–18. DOI: https://doi.org/10.1109/TAFFC.2024.3475736



<!-- page 0032 -->

[31] Roddy Cowie. 2023. Computational research and the case for taking humor seriously. *HUMOR* 36, 2 (2023), 207–223. DOI : https://doi.org/doi:10.1515/humor-2023-0021

[32] Victor De Marez, Thomas Winters, and Ayla Rigouts Terryn. 2024. THInC: A theory-driven framework for computational humor detection. In *Proceedings of the 3rd Workshop on Artificial Intelligence and Creativity (CREAI 2024).* CEUR-WS, Santiago De Compostella, Spain. Retrieved from https://ceur-ws.org/Vol-3810/paper10.pdf

[33] Boya Deng, Jiayin Tian, and Hao Li. 2022. Transformer-based multimodal contextual co-encoding for humour detection. In *Proceedings of the 2022 International Conference on Culture-Oriented Science and Technology (CoST).* 292–297. DOI : https://doi.org/10.1109/CoST57098.2022.00067

[34] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers).* Jill Burstein, Christy Doran, and Thamar Solorio (Eds.), Association for Computational Linguistics, Minneapolis, Minnesota, 4171–4186. DOI : https://doi.org/10.18653/v1/N19-1423

[35] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. 2020. An image is worth 16x16 words: Transformers for image recognition at scale. 22 pages. arXiv:2010.11929. Retrieved from https://arxiv.org/abs/2010.11929

[36] Liana Ermakova, Anne-Gwenn Bosser, Adam Jatowt, and Tristan Miller. 2023. The JOKER corpus: English-french parallel data for multilingual wordplay recognition. In *Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR’23).* Association for Computing Machinery, New York, NY, USA, 2796–2806. DOI : https://doi.org/10.1145/3539618.3591885

[37] Liana Ermakova, Anne-Gwenn Bosser, Tristan Miller, and Adam Jatowt. 2024. Overview of the CLEF 2024 JOKER task 1: Humour-aware information retrieval. In *CEUR Workshop Proceedings.*

[38] Liana Ermakova, Anne-Gwenn Bosser, Tristan Miller, and Adam Jatowt. 2024. Overview of the CLEF 2024 JOKER Task 3: Translate puns from english to french. In *CEUR Workshop Proceedings.*

[39] Florian Eyben, Martin Wöllmer, and Björn Schuller. 2010. Opensmile: The munich versatile and fast open-source audio feature extractor. In *Proceedings of the 18th ACM International Conference on Multimedia (MM’10).* Association for Computing Machinery, New York, NY, USA, 1459–1462. DOI : https://doi.org/10.1145/1873951.1874246

[40] Neamul Islam Fahim, Rifah Khan, Sujana Rahman, Nusrat Akter, and Mohammad Nurul Huda. 2024. Humor detection using machine learning approach. In *Proceedings of the 2024 6th International Conference on Electrical Engineering and Information and Communication Technology (ICEEICT).* 1217–1222. DOI : https://doi.org/10.1109/ICEEICT62016.2024.10534417

[41] Mayank Goel, Parameswari Krishnamurthy, and Radhika Mamidi. 2024. Automating humor: A novel approach to joke generation using template extraction and infilling. In *Proceedings of the 21st International Conference on Natural Language Processing (ICON).* Sobha Lalitha Devi and Karunesh Arora (Eds.), NLP Association of India (NLPAI), AU-KBC Research Centre, Chennai, India, 442–448. Retrieved from https://aclanthology.org/2024.icon-1.51/

[42] Drew Gorenz and Norbert Schwarz. 2024. How funny is ChatGPT? A comparison of human- and A.I.-produced jokes. *PLOS ONE* 19, 7 (2024), 1–13.

[43] Karish Grover and Tanishq Goel. 2021. HAHA@IberLEF2021: Humor analysis using ensembles of simple transformers. In *Proceedings of the IberLEF@ SEPLN.* 883–890.

[44] Ken Gu and Akshay Budhkar. 2021. A package for learning on tabular and text data with transformers. In *Proceedings of the 3rd Workshop on Multimodal Artificial Intelligence.* Amir Zadeh, Louis-Philippe Morency, Paul Pu Liang, Candace Ross, Ruslan Salakhutdinov, Soujanya Poria, Erik Cambria, and Kelly Shi (Eds.), ACL, Mexico City, Mexico, 69–73. DOI : https://doi.org/10.18653/v1/2021.maiworkshop-1.10

[45] Hongyu Guo, Wenbo Shang, Xueyao Zhang, Shubo Zhang, Xu Han, and Binyang Li. 2024. MUCH: A multimodal corpus construction for conversational humor recognition based on chinese sitcom. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024).* Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.), ELRA and ICCL, Torino, Italia, 11692–11698. Retrieved from https://aclanthology.org/2024.lrec-main.1021

[46] Luis Fabricio Góes, Piotr Sawicki, Marek Grzes, Dan Brown, and Marco Volpe. 2023. Is GPT-4 good enough to evaluate jokes? University of Leicester. Retrieved from https://figshare.le.ac.uk/articles/conference_contribution/Is_GPT-4_Good_Enough_to_Evaluate_Jokes_/24324415

[47] Md Kamrul Hasan, Wasifur Rahman, AmirAli Bagher Zadeh, Jianyuan Zhong, Md Iftekhar Tanveer, Louis-Philippe Morency, and Mohammed (Ehsan) Hoque. 2019. UR-FUNNY: A multimodal language dataset for understanding humor. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).* Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan (Eds.), ACL, Hong Kong, China, 2046–2056. DOI : https://doi.org/10.18653/v1/D19-1211



<!-- page 0033 -->

[48] Kaiming He, X. Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. In *Proceedings of the 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*. 770–778. Retrieved from https://api.semanticscholar.org/CorpusID:206594692

[49] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. 2020. DeBERTa: Decoding-enhanced BERT with disentangled attention. 23 pages. arXiv:2006.03654. Retrieved from https://arxiv.org/abs/2006.03654

[50] Ruiqi He, Yushu He, Longju Bai, Jiarui Liu, Zhenjie Sun, Zenghao Tang, He Wang, Hanchen Xia, and Naihao Deng. 2024. Chumor 1.0: A Truly Funny and Challenging Chinese Humor Understanding Dataset from Ruo Zhi Ba. 13 pages. arXiv:2406.12754. Retrieved from https://arxiv.org/abs/2406.12754

[51] Jack Hessel, Ana Marasovic, Jena D. Hwang, Lillian Lee, Jeff Da, Rowan Zellers, Robert Mankoff, and Yejin Choi. 2023. Do androids laugh at electric sheep? Humor “understanding” benchmarks from the new yorker caption contest. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*. Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.), ACL, Toronto, Canada, 688–714. DOI: https://doi.org/10.18653/v1/2023.acl-long.41

[52] Zachary Horvitz, Jingru Chen, Rahul Aditya, Harshvardhan Srivastava, Robert West, Zhou Yu, and Kathleen McKeown. 2024. Getting serious about humor: Crafting humor datasets with unfunny large language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*. Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.), ACL, Bangkok, Thailand, 855–869. DOI: https://doi.org/10.18653/v1/2024.acl-short.76

[53] Nabil Hossain, John Krumm, and Michael Gamon. 2019. “President vows to cut <Taxes> hair”: Dataset and analysis of creative text editing for humorous headlines. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*. Jill Burstein, Christy Doran, and Thamar Solorio (Eds.), ACL, Minneapolis, Minnesota, 133–142. DOI: https://doi.org/10.18653/v1/N19-1012

[54] Nabil Hossain, John Krumm, Michael Gamon, and Henry Kautz. 2020. SemEval-2020 task 7: Assessing humor in edited news headlines. In *Proceedings of the 14th Workshop on Semantic Evaluation*. Aurelie Herbelot, Xiaodan Zhu, Alexis Palmer, Nathan Schneider, Jonathan May, and Ekaterina Shutova (Eds.), International Committee for Computational Linguistics, Barcelona (online), 746–758. DOI: https://doi.org/10.18653/v1/2020.semeval-1.98

[55] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal Lakhotia, Ruslan Salakhutdinov, and Abdelrahman Mohamed. 2021. HuBERT: Self-supervised speech representation learning by masked prediction of hidden units. *IEEE/ACM Transactions on Audio, Speech, and Language Processing* 29 (2021), 3451–3460. DOI: https://doi.org/10.1109/TASLP.2021.3122291

[56] EunJeong Hwang and Vered Shwartz. 2023. MemeCap: A dataset for captioning and interpreting memes. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*. Houda Bouamor, Juan Pino, and Kalika Bali (Eds.), ACL, Singapore, 1433–1445. DOI: https://doi.org/10.18653/v1/2023.emnlp-main.89

[57] Marcio Inácio and Hugo Gonçalo Oliveira. 2024. Exploring multimodal models for humor recognition in portuguese. In *Proceedings of the 16th International Conference on Computational Processing of Portuguese – Vol. 1*. Pablo Gamallo, Daniela Claro, António Teixeira, Livy Real, Marcos Garcia, Hugo Gonçalo Oliveira, and Raquel Amaro (Eds.), Association for Computational Linguistics, Santiago de Compostela, Galicia/Spain, 568–574. Retrieved from https://aclanthology.org/2024.propor-1.62

[58] Marcio Inácio, Gabriela Wick-pedro, and Hugo Goncalo Oliveira. 2023. What do humor classifiers learn? An attempt to explain humor recognition models. In *Proceedings of the 7th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature*. Stefania Degaetano-Ortlieb, Anna Kazantseva, Nils Reiter, and Stan Szpakowicz (Eds.), ACL, Dubrovnik, Croatia, 88–98. DOI: https://doi.org/10.18653/v1/2023.latechclfl-1.10

[59] Sarthak Jain and Byron C. Wallace. 2019. Attention is not explanation. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*. Jill Burstein, Christy Doran, and Thamar Solorio (Eds.), ACL, Minneapolis, Minnesota, 3543–3556. DOI: https://doi.org/10.18653/v1/N19-1357

[60] Sophie Jentzsch and Kristian Kersting. 2023. ChatGPT is fun, but it is not funny! Humor is still challenging large language models. In *Proceedings of the 13th Workshop on Computational Approaches to Subjectivity, Sentiment, and Social Media Analysis*. Jeremy Barnes, Orphée De Clercq, and Roman Klinger (Eds.), ACL, Toronto, Canada, 325–340. DOI: https://doi.org/10.18653/v1/2023.wassa-1.29

[61] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023. Mistral 7B. 9 pages. arXiv:2310.06825. Retrieved from https://arxiv.org/abs/2310.06825

[62] James M. Jones. 1972. *Prejudice and Racism*. Addison-Wesley.



<!-- page 0034 -->

[63] Antony Kalloniatis and Panagiotis Adamidis. 2025. Computational humor recognition: A systematic literature review. *Artificial Intelligence Review* 58 (2025), 1–53. DOI: https://doi.org/10.1007/s10462-024-11043-3

[64] Justine T. Kao, Roger Levy, and Noah D. Goodman. 2016. A computational model of linguistic humor in puns. *Cognitive Science* 40, 5 (2016), 1270–1285. DOI: https://doi.org/10.1111/cogs.12269

[65] Ashish Kayastha and Alexander Redei. 2022. That’s what she said: Humor identification with word embeddings and recurrent neural networks. In *Advances in Information and Communication: Proceedings of the 2022 Future of Information and Communication Conference (FICC), Volume 2.*

[66] Yuta Kayatani, Zekun Yang, Mayu Otani, Noa Garcia, Chenhui Chu, Yuta Nakashima, and Haruo Takemura. 2021. The laughing machine: Predicting humor in video. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV).* 2073–2082.

[67] Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne, Dumitru Erhan, and Been Kim. 2019. *The (Un)reliability of Saliency Methods.* Springer International. DOI: https://doi.org/10.1007/978-3-030-28954-6_14

[68] Dayoon Ko, Sangho Lee, and Gunhee Kim. 2023. Can language models laugh at YouTube short-form videos?. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing.* Houda Bouamor, Juan Pino, and Kalika Bali (Eds.), ACL, Singapore, 2897–2916. DOI: https://doi.org/10.18653/v1/2023.emnlp-main.176

[69] Mika Koivisto and Simone Grassini. 2023. Best humans still outperform artificial intelligence in a creative divergent thinking task. *Scientific Reports* 13, 1 (2023), 1–10.

[70] C. Koutlis, M. Schinas, and S. Papadopoulos. 2023. MemeTector: Enforcing deep focus for meme detection. *International Journal of Multimedia Information Retrieval* 12 (2023), 1–11. DOI: https://doi.org/10.1007/s13735-023-00277-6

[71] Akshi Kumar, Abhishek Mallik, and Sanjay Kumar. 2024. HumourHindiNet: Humour detection in Hindi web series using word embedding and convolutional neural network. *ACM Transactions on Asian and Low-Resource Language Information Processing* 23, 7, Article 98 (2024), 21 pages. DOI: https://doi.org/10.1145/3661306

[72] Vijay. Kumar, Ranjeet Walia, and Shivam Sharma. 2022. DeepHumor: A novel deep learning framework for humor detection. *Multimedia Tools and Applications* 81 (2022), 16797–16812. DOI: https://doi.org/10.1007/s11042-022-12739-w

[73] Gitanjali Kumari, Dibyanayan Bandyopadhyay, Asif Ekbal, Santanu Pal, Arindam Chatterjee, and Vinutha B. N. 2024. Let’s all laugh together: A novel multitask framework for humor detection in internet memes. *IEEE Transactions on Computational Social Systems* 11, 3 (2024), 4385–4395. DOI: https://doi.org/10.1109/TCSS.2024.3362811

[74] Anna Kuznetsova and Carlo Strapparava. 2024. Multimodal and multilingual laughter detection in stand-up comedy videos. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024).* Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.), ELRA and ICCL, Torino, Italia, 11884–11889. Retrieved from https://aclanthology.org/2024.lrec-main.1037

[75] Roberto Labadie Tamayo, Berta Chulvi, and Paolo Rosso. 2023. Everybody hurts, sometimes. overview of HUrtful humour at IberLEF 2023: Detection of humour spreading prejudice in twitter. *Procesamiento del Lenguaje Natural* 71 (2023), 383–395. DOI: https://doi.org/10.26342/2023-71-30

[76] Jianquan Li, XiangBo Wu, Xiaokang Liu, Qianqian Xie, Prayag Tiwari, and Benyou Wang. 2023. Can language models make fun? A case study in chinese comic crosstalk. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).* Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.), ACL, Toronto, Canada, 7581–7596. DOI: https://doi.org/10.18653/v1/2023.acl-long.419

[77] Runjia Li, Shuyang Sun, Mohamed Elhoseiny, and Philip Torr. 2023. OxfordTVG-HIC: Can machine make humorous captions from images?. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV).* 20293–20303.

[78] Zefeng Li, Hongfei Lin, Liang Yang, Bo Xu, and Shaowu Zhang. 2022. Memeplate: A chinese multimodal dataset for humor understanding in meme templates. In *Proceedings of the Natural Language Processing and Chinese Computing: 11th CCF International Conference, NLPCC 2022, Guilin, China, September 24–25, 2022, Part I.* Springer, Berlin, 527–538. DOI: https://doi.org/10.1007/978-3-031-17120-8_41

[79] Zhuohang Li, Jiashuo Liu, and Yuci Wang. 2022. Performance analysis on deep learning models in humor detection task. In *Proceedings of the 2022 International Conference on Machine Learning and Knowledge Engineering (MLKE).* 93–97. DOI: https://doi.org/10.1109/MLKE55170.2022.00023

[80] Pantelis Linardatos, Vasilis Papastefanopoulos, and Sotiris Kotsiantis. 2021. Explainable AI: A review of machine learning interpretability methods. *Entropy* 23, 1 (2021), 1–18. DOI: https://doi.org/10.3390/e23010018

[81] Chen Liu, Gregor Geigle, Robin Krebs, and Iryna Gurevych. 2022. FigMemes: A dataset for figurative language identification in politically-opinionated memes. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.* Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 7069–7086. DOI: https://doi.org/10.18653/v1/2022.emnlp-main.476



<!-- page 0035 -->

[82] Pengfei Liu, Xipeng Qiu, and Xuanjing Huang. 2017. Adversarial multi-task learning for text classification. In *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*. Regina Barzilay and Min-Yen Kan (Eds.), ACL, Vancouver, Canada, 1–10. DOI : https://doi.org/10.18653/v1/P17-1001

[83] Yang Liu and Yuexian Hou. 2023. Mining effective features using quantum entropy for humor recognition. In *Findings of the Association for Computational Linguistics: EACL 2023*. Andreas Vlachos and Isabelle Augenstein (Eds.), ACL, Dubrovnik, Croatia, 2048–2053. DOI : https://doi.org/10.18653/v1/2023.findings-eacl.152

[84] Tyler Loakman, Aaron Maladry, and Chenghua Lin. 2023. The iron(ic) melting pot: Reviewing human evaluation in humour, irony and sarcasm generation. In *Findings of the Association for Computational Linguistics: EMNLP 2023*. Houda Bouamor, Juan Pino, and Kalika Bali (Eds.), ACL, Singapore, 6676–6689. DOI : https://doi.org/10.18653/v1/2023.findings-emnlp.444

[85] Navonil Majumder, Soujanya Poria, Devamanyu Hazarika, Rada Mihalcea, Alexander Gelbukh, and Erik Cambria. 2019. DialogueRNN: An attentive RNN for emotion detection in conversations. In *Proceedings of the 33rd AAAI Conference on Artificial Intelligence and 31st Innovative Applications of Artificial Intelligence Conference and the AAAI Symposium on Educational Advances in Artificial Intelligence (AAAI’19/IAAI’19/EAAI’19)*. AAAI, Article 837, 8 pages. DOI : https://doi.org/10.1609/aaai.v33i01.33016818

[86] Antonis Maronikolakis, Danae Sánchez Villegas, Daniel Preoţiuc-Pietro, and Nikolaos Aletras. 2020. Analyzing political parody in social media. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*. Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (Eds.), ACL, Online, 4373–4384. DOI : https://doi.org/10.18653/v1/2020.acl-main.403

[87] R. A. Martin and N. A. Kuiper. 1999. Daily occurrence of laughter: Relationships with age, gender, and type a personality. *Humor: International Journal of Humor Research* 12, 4 (1999), 355–384.

[88] Rod A. Martin and Thomas E. Ford. 2018. *The Psychology of Humor*. Elsevier Inc.

[89] J. A. Meaney. 2020. Crossing the line: Where do demographic variables fit into humor detection?. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: Student Research Workshop*. Shruti Rijhwani, Jiangming Liu, Yizhong Wang, and Rotem Dror (Eds.), ACL, Online, 176–181. DOI : https://doi.org/10.18653/v1/2020.acl-srw.24

[90] J. A. Meaney, Steven Wilson, Luis Chiruzzo, Adam Lopez, and Walid Magdy. 2021. SemEval 2021 task 7: HaHackathon, detecting and rating humor and offense. In *Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)*. Alexis Palmer, Nathan Schneider, Natalie Schluter, Guy Emerson, Aurelie Herbelot, and Xiaodan Zhu (Eds.), ACL, Online, 105–119. DOI : https://doi.org/10.18653/v1/2021.semeval-1.9

[91] Lucía I. Merlo, Berta Chulvi, Reynier Ortega, and Paolo Rosso. 2023. When humour hurts: Linguistic features to foster explainability. In *Proceedings of the Procesamiento del Lenguaje Natural*. 85–98. DOI : https://doi.org/10.26342/2023-70-7

[92] George A. Miller. 1994. WordNet: A lexical database for english. In *Human Language Technology: Proceedings of a Workshop held at Plainsboro, New Jersey, March 8-11, 1994*. Retrieved from https://aclanthology.org/H94-1111/

[93] Piotr Mirowski, Juliette Love, Kory Mathewson, and Shakir Mohamed. 2024. A robot walks into a bar: Can language models serve as creativity supporttools for comedy? An evaluation of LLMs’ humour alignment with comedians. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT’24)*. Association for Computing Machinery, New York, NY, USA, 1622–1636. DOI : https://doi.org/10.1145/3630106.3658993

[94] Anirudh Mittal, Diptesh Kanojia, and Pushpak Bhattacharyya. 2022. Survey on computational humour. Preprint, IIT Bombay. Retrieved from https://api.semanticscholar.org/CorpusID:251341949

[95] Anirudh Mittal, Pranav Jeevan P, Prerak Gandhi, Diptesh Kanojia, and Pushpak Bhattacharyya. 2021. “So you think you’re funny?”: Rating the humour quotient in standup comedy. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*. Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.), ACL, Online and Punta Cana, Dominican Republic, 10073–10079. DOI : https://doi.org/10.18653/v1/2021.emnlp-main.789

[96] Anirudh Mittal, Yufei Tian, and Nanyun Peng. 2022. AmbiPun: Generating humorous puns with ambiguous context. In *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*. Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz (Eds.), ACL, Seattle, United States, 1053–1062. DOI : https://doi.org/10.18653/v1/2022.naacl-main.77

[97] Dan Ofer and Dafna Shahaf. 2022. Cards against AI: Predicting humor in a fill-in-the-blank party game. In *Findings of the Association for Computational Linguistics: EMNLP 2022*. Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 5397–5403. DOI : https://doi.org/10.18653/v1/2022.findings-emnlp.394

[98] OpenAI. 2022. ChatGPT. Retrieved from https://openai.com/chatgpt Accessed: 2025-03-26.

[99] Vaishnavi Pamulapati and Radhika Mamidi. 2021. Developing conversational data and detection of conversational humor in telugu. In *Proceedings of the 2nd Workshop on Computational Approaches to Discourse*. Chloé Braud, Christian Hardmeier, Junyi Jessy Li, Annie Louis, Michael Strube, and Amir Zeldes (Eds.), ACL, Punta Cana, Dominican Republic and Online, 12–19. DOI : https://doi.org/10.18653/v1/2021.codi-main.2



<!-- page 0036 -->

[100] Badri N. Patro, Mayank Lunayach, Deepankar Srivastava, Sarvesh Hunar Singh, and Vinay P. Namboodiri. 2021. Multimodal humor dataset: Predicting laughter tracks for sitcoms. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV).* 576–585.

[101] Jeffrey Pennington, Richard Socher, and Christopher Manning. 2014. GloVe: Global vectors for word representation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP).* Alessandro Moschitti, Bo Pang, and Walter Daelemans (Eds.), ACL, Doha, Qatar, 1532–1543. DOI :https://doi.org/10.3115/v1/D14-1162

[102] Arpan Phukan, Anas Anwarul Haq Khan, and Asif Ekbal. 2024. QuMIN: Quantum multi-modal data fusion for humor detection. *Multimedia Tools and Applications* 84, 18 (2024), 18855–18872. DOI :https://doi.org/10.1007/s11042-024-19790-9

[103] Victor Manuel Palma Preciado, Grigori Sidorov, Liana Ermakova, Anne-Gwenn Bosser, Tristan Miller, and Adam Jatowt. 2024. Overview of the CLEF 2024 JOKER Task 2: Humour classification according to genre and technique. In *CEUR Workshop Proceedings.*

[104] Béatrice Priego-Valverde, Brigitte Bigi, and Mary Amoyal. 2020. “Cheese!”: A corpus of face-to-face french interactions. a case study for analyzing smiling and conversational humor. In *Proceedings of the 12th Language Resources and Evaluation Conference.* Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (Eds.), European Language Resources Association, Marseille, France, 467–475. Retrieved from https://aclanthology.org/2020.lrec-1.59

[105] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. 2021. Learning transferable visual models from natural language supervision. 48 pages. arXiv:2103.00020. Retrieved from https://arxiv.org/abs/2103.00020

[106] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research* 21, 1, Article 140 (2020), 67 pages.

[107] Sahithya Ravi, Patrick Huber, Akshat Shrivastava, Vered Shwartz, and Arash Einiolghozati. 2024. Small but funny: A feedback-driven approach to humor distillation. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).* Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.), ACL, Bangkok, Thailand, 13078–13090. DOI :https://doi.org/10.18653/v1/2024.acl-long.706

[108] Lu Ren, Bo Xu, Hongfei Lin, Jinhui Zhang, and Liang Yang. 2022. An attention network via pronunciation, lexicon and syntax for humor recognition. *Applied Intelligence* 52 (2022), 2690–2702.

[109] Guilherme Sanches de Oliveira and Edward Baggs. 2023. *Psychology’s WEIRD Problems.* Cambridge University Press.

[110] Wenbo Shang, Jiangjiang Zhao, Zezhong Wang, Binyang Li, Fangchun Yang, and Kam-Fai Wong. 2022. “I know who you are”: Character-based features for conversational humor recognition in chinese. In *Findings of the Association for Computational Linguistics: EMNLP 2022.* Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 2927–2932. DOI :https://doi.org/10.18653/v1/2022.findings-emnlp.212

[111] Manasi Sharma, Ho Chit Siu, Rohan Paleja, and Jaime D. Peña. 2024. Why Would You Suggest That? Human Trust in Language Model Responses. 18 pages. arXiv:2406.02018. Retrieved from https://arxiv.org/abs/2406.02018

[112] Farah Shatnawi, Malak Abdullah, Mahmoud Hammad, and Mahmoud Al-Ayyoub. 2023. Comprehensive study of pre-trained language models: Detecting humor in news headlines. *Soft Computing* 27 (2023), 2575–2599. DOI :https://doi.org/10.1007/s00500-022-07573-z

[113] Leandro Silva, Mainack Mondal, Denzil Correa, Fabrício Benevenuto, and Ingmar Weber. 2021. Analyzing the targets of hate in online social media. *Proceedings of the International AAAI Conference on Web and Social Media* 10, 1 (2021), 687–690. DOI :https://doi.org/10.1609/icwsm.v10i1.14811

[114] Fábio Souza, Rodrigo Nogueira, and Roberto Lotufo. 2020. BERTimbau: Pretrained BERT models for brazilian portuguese. In *Proceedings of the Intelligent Systems: 9th Brazilian Conference, BRACIS 2020, Rio Grande, Brazil, October 20–23, 2020, Part I.* Springer-Verlag, Berlin, 403–417. DOI :https://doi.org/10.1007/978-3-030-61377-8_28

[115] Jiao Sun, Anjali Narayan-Chen, Shereen Oraby, Alessandra Cervone, Tagyoung Chung, Jing Huang, Yang Liu, and Nanyun Peng. 2022. ExPUNations: Augmenting puns with keywords and explanations. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.* Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 4590–4605. DOI :https://doi.org/10.18653/v1/2022.emnlp-main.304

[116] Jiao Sun, Anjali Narayan-Chen, Shereen Oraby, Shuyang Gao, Tagyoung Chung, Jing Huang, Yang Liu, and Nanyun Peng. 2022. Context-situated pun generation. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.* Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 4635–4648. DOI :https://doi.org/10.18653/v1/2022.emnlp-main.306

[117] Kohtaro Tanaka, Hiroaki Yamane, Yusuke Mori, Yusuke Mukuta, and Tatsuya Harada. 2022. Learning to evaluate humor in memes based on the incongruity theory. In *Proceedings of the 2nd Workshop on When Creative AI Meets*



<!-- page 0037 -->

*Conversational AI.* Xianchao Wu, Peiying Ruan, Sheng Li, and Yi Dong (Eds.), ACL, Gyeongju, Republic of Korea, 81–93. Retrieved from https://aclanthology.org/2022.cai-1.9

[118] Yufei Tian, Divyanshu Sheth, and Nanyun Peng. 2022. A unified framework for pun generation with humor principles. In *Findings of the Association for Computational Linguistics: EMNLP 2022.* Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.), ACL, Abu Dhabi, UAE, 3253–3261. DOI : https://doi.org/10.18653/v1/2022.findings-emnlp.237

[119] Alexey Tikhonov and Pavel Shtykovskiy. 2024. Humor mechanics: Advancing humor generation with multistep reasoning. In *Proceedings of the International Conference on Computational Creativity 2024.* Association for Computational Creativity, 31–41. Retrieved from https://computationalcreativity.net/iccc24/papers/ICCC24_paper_128.pdf

[120] Zhan Tong, Yibing Song, Jue Wang, and Limin Wang. 2022. VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training. 25 pages. arXiv:2203.12602. Retrieved from https://arxiv.org/abs/2203.12602

[121] Joe Toplyn. 2021. Witscript: A system for generating improvised jokes in a conversation. In *Proceedings of the 12th International Conference on Computational Creativity (ICCC’21).* Association for Computational Creativity, Online, 22–31. Retrieved from https://computationalcreativity.net/iccc21/wp-content/uploads/2021/09/ICCC_2021_paper_15.pdf

[122] Joe Toplyn. 2023. Witscript 3: A Hybrid AI System for Improvising Jokes in a Conversation. 5 pages. arXiv:2301.02695. Retrieved from https://arxiv.org/abs/2301.02695

[123] Yuen-Hsien Tseng, Wun-Syuan Wu, Chia-Yueh Chang, Hsueh-Chih Chen, and Wei-Lun Hsu. 2020. Development and validation of a corpus for machine humor comprehension. In *Proceedings of the 12th Language Resources and Evaluation Conference.* Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (Eds.), European Language Resources Association, Marseille, France, 1346–1352. Retrieved from https://aclanthology.org/2020.lrec-1.168

[124] Beatrice Turano and Carlo Strapparava. 2022. Making people laugh like a pro: Analysing humor through stand-up comedy. In *Proceedings of the 13th Language Resources and Evaluation Conference.* Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Jan Odijk, and Stelios Piperidis (Eds.), European Language Resources Association, Marseille, France, 5206–5211. Retrieved from https://aclanthology.org/2022.lrec-1.558

[125] Han Wang and Roy Ka-Wei Lee. 2024. MemeCraft: Contextual and stance-driven multimodal meme generation. In *Proceedings of the ACM Web Conference 2024 (WWW’24).* Association for Computing Machinery, New York, NY, USA, 4642–4652. DOI : https://doi.org/10.1145/3589334.3648151

[126] Peng Wang, An Yang, Rui Men, Junyang Lin, Shuai Bai, Zhikang Li, Jianxin Ma, Chang Zhou, Jingren Zhou, and Hongxia Yang. 2022. Unifying architectures, tasks, and modalities through a simple sequence-to-sequence learning framework. 26 pages. arXiv:2202.03052. Retrieved from https://arxiv.org/abs/2202.03052

[127] Orion Weller, Nancy Fulda, and Kevin Seppi. 2020. Can humor prediction datasets be used for humor generation? Humorous headline generation via style transfer. In *Proceedings of the 2nd Workshop on Figurative Language Processing.* Beata Beigman Klebanov, Ekaterina Shutova, Patricia Lichtenstein, Smaranda Muresan, Chee Wee, Anna Feldman, and Debanjan Ghosh (Eds.), ACL, Online, 186–191. DOI : https://doi.org/10.18653/v1/2020.figlang-1.25

[128] Orion Weller and Kevin Seppi. 2020. The rjokes dataset: A large scale humor collection. In *Proceedings of the 12th Language Resources and Evaluation Conference.* Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Asuncion Moreno, Jan Odijk, and Stelios Piperidis (Eds.), European Language Resources Association, Marseille, France, 6136–6141. Retrieved from https://aclanthology.org/2020.lrec-1.753

[129] Thomas Winters. 2021. Computers learning humor is no joke. *Harvard Data Science Review* 3, 2 (2021), 1–18. Retrieved from https://hdsr.mitpress.mit.edu/pub/wi9yky5c/release/3

[130] Jiaming Wu, Hongfei Lin, Liang Yang, and Bo Xu. 2021. MUMOR: A multimodal dataset for humor detection in conversations. In *Proceedings of the Natural Language Processing and Chinese Computing.* Lu Wang, Yansong Feng, Yu Hong, and Ruifang He (Eds.), Springer International, Cham, 619–627.

[131] Bo Xu, Tingting Li, Junzhe Zheng, Mehdi Naseriparsa, Zhehuan Zhao, Hongfei Lin, and Feng Xia. 2022. MET-Meme: A multimodal meme dataset rich in metaphors. In *Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR’22).* Association for Computing Machinery, New York, NY, USA, 2887–2899. DOI : https://doi.org/10.1145/3477495.3532019

[132] Zhijun Xu, Siyu Yuan, Lingjie Chen, and Deqing Yang. 2024. “A good pun is its own reword”: Can large language models understand puns?. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing.* Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen (Eds.), ACL, Miami, Florida, USA, 11766–11782. DOI : https://doi.org/10.18653/v1/2024.emnlp-main.657



<!-- page 0038 -->

[133] Zixiaofan Yang, Shayan Hooshmand, and Julia Hirschberg. 2021. CHoRaL: Collecting humor reaction labels from millions of social media users. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*. Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.), ACL, Online and Punta Cana, Dominican Republic, 4429–4435. DOI: https://doi.org/10.18653/v1/2021.emnlp-main.364

[134] Jian Ye, Zhe Chen, Juhua Liu, and Bo Du. 2020. TextFuseNet: Scene text detection with richer fused features. In *Proceedings of the 29th International Joint Conference on Artificial Intelligence, IJCAI-20*. Christian Bessiere (Ed.), International Joint Conferences on Artificial Intelligence Organization, 516–522. DOI: https://doi.org/10.24963/ijcai.2020/72

[135] JingJie Zeng, Liang Yang, Jiahao Kang, Yufeng Diao, Zhihao Yang, and Hongfei Lin. 2024. “Barking up the right tree”, a GAN-based pun generation model through semantic pruning. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*. Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.), ELRA and ICCL, Torino, Italia, 2119–2131. Retrieved from https://aclanthology.org/2024.lrec-main.191/

[136] Zeyuan Zeng, Zefeng Li, Liang Yang, and Hongfei Lin. 2024. Leveraging social context for humor recognition and sense of humor evaluation in social media with a new chinese humor corpus - humorWB. In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*. Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.), ELRA and ICCL, Torino, Italia, 10393–10402. Retrieved from https://aclanthology.org/2024.lrec-main.908

[137] Tuo Zhang, Tiantian Feng, Yibin Ni, Mengqin Cao, Ruying Liu, Katharine Butler, Yanjun Weng, Mi Zhang, Shrikanth S. Narayanan, and Salman Avestimehr. 2024. Creating a Lens of Chinese Culture: A Multimodal Dataset for Chinese Pun Rebus Art Understanding. 16 pages. arXiv:2406.10318. Retrieved from https://arxiv.org/abs/2406.10318

[138] Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, and Pan Zhou. 2024. Let’s think outside the box: Exploring leap-of-thought in large language models with creative humor generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. 13246–13257.

Received 25 April 2025; revised 14 October 2025; accepted 7 November 2025
