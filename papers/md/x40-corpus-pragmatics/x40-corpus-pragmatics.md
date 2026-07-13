<!-- Transcribed from x40-corpus-pragmatics.pdf -->



<!-- page 0001 -->

Corpus Pragmatics (2026) 10:33  
https://doi.org/10.1007/s41701-026-00235-7

RESEARCH

[Figure: Check for updates icon]

# Assessing the Potential of LLM-assisted Annotation for Corpus Pragmatics: The Case of Humor

Antonio Bianco^1 · Nicola Brocca^2 · Davide Garassino^3

Received: 9 January 2026 / Accepted: 25 February 2026  
© The Author(s) 2026

## Abstract

Corpus pragmatics faces ongoing challenges in quantitatively studying context-dependent categories like humor, given their subjectivity and the need for costly inter-rater reliability checks. Recent advances in LLMs offer a potential way to streamline these processes for pragmatic annotation tasks. This paper investigates that potential through an analysis of Italian political discourse on X, focusing on humorous tweets and their discursive functions (Attardo, 2020). We compare the performance of GPT-4o, LLaMA-3.3-70B-Instruct, and a novice annotator against that of an expert annotator. For the detection of humor, both models reached high agreement with the expert annotator (in particular, GPT-4o: Cohen’s κ=0.75; AC1=0.87). Instead, agreement dropped for the classification of humor functions (GPT-4o: Cohen’s κ=0.37; AC1=0.70). Qualitative results suggest that the models rely heavily on lexical cues rather than demonstrating deeper pragmatic competence. These findings indicate that while LLMs can provide useful assistance in the initial stages of large-scale annotation, they remain limited in capturing the nuanced and context-dependent nature of pragmatic functions.

**Keywords** Humor · LLMs · Political communication · LLaMA · GPT · Automatic annotation

✉ Nicola Brocca  
nicola.brocca@uibk.ac.at

Antonio Bianco  
antonio.bianco@unibg.it

Davide Garassino  
davide.garassino@uzh.ch

^1 University of Bergamo, Bergamo, Italy

^2 Universität Innsbruck, Innsbruck, Austria

^3 University of Zurich & Zurich University of Applied Sciences, Winterthur, Switzerland

Published online: 21 March 2026

Springer



<!-- page 0002 -->

## Introduction

This article investigates the potential of two large language models (LLMs), GPT-4o and LLaMA-3.3, to recognize humorous content and to distinguish among different communicative functions of humor. Evaluating the ability of LLMs to identify humor and other pragmatic categories is essential for determining whether they can be reliably employed as research assistants in corpus construction.

LLM-assisted annotation has recently emerged as an innovative approach that promises to reduce costs and streamline the creation of corpora annotated according to pragmatic categories (Brocca et al., 2026). The availability of large-scale pragmatically annotated corpora would substantially advance pragmatic research, a domain that has traditionally remained at the margins of the “quantitative turn” characterizing linguistic research over the past decades (Joseph, 2008). While previous studies have reported promising results in the use of LLMs for discourse analysis (Fuoli et al., 2025; Yu, 2025), or the recognition of speech acts (Yu et al., 2024), investigations into the effectiveness of LLMs for the annotation of humor remain relatively scarce.

In this paper, *humor* is adopted as an umbrella term (Attardo, 2020: 7) encompassing a wide range of humorous phenomena as well as different humor types (Dynel 2009). The study is theoretically grounded in Raskin’s Semantic Script Theory, which conceptualizes humor as emerging from the overlap of two opposite scripts (Raskin, 1985). This framework is further developed through General Theory of Verbal Humor (GTVH), which extends the analysis by introducing multiple knowledge resources, including script opposition and target(s) (Attardo & Raskin, 1991; Attardo, 1994).

Humor often involves deliberate violations of Grice’s Cooperative Principle (Attardo, 2020: 165). Its interpretation is cognitively demanding, as it relies heavily on shared cultural background and contextual knowledge. Historically, the automatic detection of humor has been regarded as a limitation within NLP (Natural Language Processing) research (Chiruzzo et al., 2019). Like other pragmatic phenomena, such as implicit meaning (Garassino et al., 2022), the inherently elusive nature of humor has hindered its integration into quantitative corpus analysis (Scott-Phillips, 2017). Despite these challenges, the rise of LLMs may open new avenues for automated humor recognition and annotation, making such methods accessible even to linguists without advanced programming skills.

## State of the Art

### Challenges in Pragmatic Annotation

Often dubbed the “Cinderella” of linguistics (Bianchi, 2004), pragmatics has remained in the background during the field’s shift toward quantitative methods (Joseph, 2008). Although recent projects have introduced pragmatically annotated corpora (Cominetti et al., 2024), the field still lacks sufficiently large and interoperable datasets (Weisser, 2016; 2018). Three main reasons explain why pragmatic annotation resists automation:



<!-- page 0003 -->

i. Pragma-discursive features often extend beyond single lexical units, complicating parsing and categorization.  
ii. Pragmatic functions have highly variable realizations: a single function may be expressed through many forms, hindering systematic mappings (Cavasso & Taboada, 2021).  
iii. Interpretation is context-dependent. For instance, “I know where you live!” may be a statement of knowledge or a threat, depending on assumptions, intentions, and social dynamics (Weisser, 2015).

Manual annotation, though essential for capturing contextual nuance and implicit meaning, is time-consuming, cognitively demanding, and prone to annotator fatigue. Inter-coder agreement can be improved through training and calibration, but even expert annotators often achieve only partial agreement (Garassino et al., 2022). Consequently, pragmatically annotated corpora are small, costly, and limited in generalizability. These issues are especially acute in humor annotation, as discussed in “Technology-assisted Pragmatic Annotation” section.

**Technology-assisted Pragmatic Annotation**

Recent years have seen notable progress in pragmatic annotation through semi-automated tools, particularly in dialogue structure (Weisser, 2016; Zhao & Kawahara, 2019), propaganda detection (Hamilton et al., 2024), and stance or relevance analysis (Gilardi et al., 2023). Earlier systems followed a function-to-form model (O’Keeffe, 2018), relying on supervised learning with curated datasets and engineered features. An example is the Ladder Web (Brocca et al., 2026), a machine-learning web app designed to annotate request and cancellation acts in Italian and German.

A major shift has come with large pre-trained models, among which the GPT family is one of the most widely used. Unlike supervised systems that are tightly coupled to particular datasets, LLMs rely primarily on extensive unsupervised pretraining. Owing to their broad and generic knowledge base, the quality of their output is strongly shaped by how users interact with them. Among the interaction strategies discussed in the literature, Fuoli et al. (2025) identify prompt engineering as particularly promising for the identification of context-sensitive items such as metaphors. Prompt engineering refers to the careful design of input instructions, examples, and contextual cues so as to guide the model toward a desired interpretive behavior without modifying its internal parameters (Brown et al., 2020).

LLMs’ apparent ability to engage with pragmatic phenomena stems from several interconnected factors: (i) extensive exposure to context-rich input during training (Baker, 2023: 32), (ii) the capacity to model semantic relationships across discourse units, and (iii) a demonstrated ability to generalize from examples and adapt to task-specific prompts (Brocca et al., in review; Brown et al., 2020). These capabilities collectively allow LLMs to approximate certain aspects of context-dependent and implied interpretation. In certain circumstances, LLMs have been shown to rival or even surpass human annotators in accuracy: GPT-based systems have outperformed crowdworkers on sentiment, stance, and relevance (Gilardi et al., 2023; Zhu et al., 2023), with GPT-4 approaching expert-level precision (Ostyakova et al., 2023). They



<!-- page 0004 -->

also offer substantial speed gains. Hamilton et al. (2024) report propaganda annotation with GPT-4 to be ten times faster than manual work, while Yu et al. (2024) show that GPT models annotate complex speech acts in seconds with near-human accuracy.

Despite these advances, challenges remain. Pragmatic competence of LLMs does not seem to reflect genuine pragmatic reasoning (such as the ability to be coherent with previously mentioned context and understanding implicit meaning) and remains limited compared to that of human speakers (Ma et al., 2025). For example, some tests conducted on comprehension of presuppositions (Kabbara & Cheung, 2022; Sieker & Zarrieß, 2023) confirm that LLMs rely primarily on patterns grounded in semantics and morphosyntactic regularities, rather than on genuine contextual inference (see Brocca et al., in review and Garassino et al., 2025 for a detailed discussion). As a result, their performance on certain pragmatic tasks continues to fall short of the benchmark set by human annotators (Settaluri et al., 2024). Moreover, variability in model outputs undermines reproducibility (Yu, 2025), with Brocca et al. (2026) reporting inconsistencies across sessions. Opacity in model parameters and training data, along with ethical concerns about prompt reuse in commercial closed-source LLMs, raises questions about privacy and scientific suitability.

## Automatic Analysis of Humor

The automatic analysis of humor has long been well represented in NLP (Binsted, 2006). In recent years, however, LLMs have marked a major shift in this domain as well. The purported ability of LLMs to “understand” humor is typically operationalized through three task types: humor detection, humor explanation, and humor generation.

Chiruzzo et al. (2019), drawing on a corpus of 30,000 annotated Spanish tweets, show that models such as multilingual BERT approach near-human performance in humor identification and funniness prediction, and consistently outperform traditional machine-learning approaches.

More recently, with respect to humor identification, Jentzsch and Kersting (2023) show that GPT-3.5 can determine whether a text is humorous. However, while the model performs well on overt forms of wordplay, its accuracy drops when humor is expressed implicitly and is culturally grounded. Importantly, the model struggles once key structural or semantic cues are removed, suggesting that its capacity to detect humor remains superficial (see “Technology-assisted Pragmatic Annotation” section). By contrast, in the explanation task the model shows its strongest performance: when presented with a joke, GPT-3.5 is generally able to articulate the relevant humorous mechanism, although its explanations occasionally overinterpret or misattribute cultural references. Similar limitations to those noted by Jentzsch and Kersting (2023) are also reported in other studies, such as Zangari et al. (2025). In their investigation of pun detection and understanding, GPT-4o is shown to over-rely on structural cues, identifying puns primarily on the basis of “typical pun-like patterns” (Zangari et al., 2025: 27930). Based on a study of humor detection in emotionally sensitive and support-oriented conversations, Quan et al. (2025) likewise argue that state-of-the-art models such as GPT-4o, Gemini-1.5, and LLaMA-3.3 struggle with subtle forms of humor.



<!-- page 0005 -->

With respect to humor generation, Jentzsch and Kersting (2023) asked GPT-3.5 to produce jokes based on prompts specifying topics or humor styles. While the model consistently generates well-formed and contextually appropriate outputs, the more than one thousand jokes analyzed tend to rely on familiar templates and widely circulated internet humor, exhibiting recurring predictable pun structures. Similarly, Xu et al.’s (2024) experiments indicate that “although LLMs perform satisfactorily in recognizing and explaining puns, there is still room for improvement in their ability to generate creative and humorous puns” (Xu et al., 2024: 11773).

Concerning effective prompting strategies, existing studies highlight the importance of detailed prompts for humor identification and explanation. These approaches typically use few- or many-shot prompting with examples of humorous texts (e.g., Goes et al., 2023), along with Chain-of-Thought strategies (Xu et al., 2024), which enhance LLM performance in detecting and explaining puns.

## Research Questions

This study investigates the ability of LLMs to detect humorous tweets and analyze humor communicative functions, with a focus on how their performance compares to human annotators. Two questions guide the analysis:

**RQ1** *Can LLMs detect humorous tweets?*

**RQ1a** *How do they perform compared to expert and novice annotators?*

**RQ1b** *What kinds of errors do they most often make?*

**RQ2** *Can LLMs annotate humor functions according to a given taxonomy?*

**RQ2a** *How do they perform compared to expert and novice annotators?*

**RQ2b** *Which humor functions are most frequently misinterpreted?*

Additionally, since prior research (e.g., Carvalho et al., 2009) suggests that automatic detection systems rely heavily on lexical and graphical cues (e.g., emojis, laughter markers, ironic hashtags) to identify humor, the most frequent sources of (dis)agreement between human annotators and LLMs will be examined through qualitative analysis in an exploratory manner, addressing RQ1b and RQ2b.

## Methodology

### Humorous vs. Non-humorous Tweets

The theoretical models adopted to distinguish humorous tweets from non-humorous tweets are the Semantic Script Theory (Raskin, 1985) and its expansion, that is



<!-- page 0006 -->

General Theory of Verbal Humor, GTVH (Attardo & Raskin, 1991; Attardo, 2020). According to the GTVH, there are six knowledge resources, hierarchically organized, that are necessary to interpret and/or compare humorous texts, namely: Script Opposition (SO) → Logical Mechanism (LM) → Situation (SI) → Target (TA) → Narrative Strategy (NS) → Language (LA). The most important of the six knowledge resources is the Script Opposition. Specifically, a text can be considered humorous if and only if the criteria in (1) are simultaneously satisfied (Attardo, 2020):

(1)

a. The text is compatible (fully or in part) with two different scripts (Overlapping);  
b. The two scripts with which the text is compatible are opposite (Oppositeness).

Scripts are essentially ideas, thoughts, or meanings evoked by a text. Scripts can be activated lexically and inferentially, i.e.: by presuppositions, inferences and implicatures. All three can activate or evoke a script through implicit activation (Attardo, 2020: 125). Consider the example discussed by Attardo (2020: 124–125): “I drove to Dallas with my wife.” In this text, the word *drive* lexically activates the script of a “vehicle”, while *Dallas* activates at least the scripts of “city” and “Texas”. Inferentially, the text triggers the script of “married man” and de-activates the script of a “bachelor.”

Regarding (1a), Overlapping is to be understood as the coexistence of two senses or two interpretations within the same text (Attardo, 1994: 203). In relation to (1b), Raskin (1985: 108) refers to a local antonymy between scripts within a particular discourse. Thus, Overlapping and Oppositeness allow us to distinguish humor from other pragmatic phenomena: for example, non-humorous metaphors activate two overlapping scripts but these scripts are not in opposition to each other in the same text. Notably, the scripts in opposition may be related to different levels of abstraction. All SOs can be reduced to three highly abstract binary oppositions: actual/non-actual; normal/abnormal, and possible/impossible. Therefore, in each of the tweets classified as humorous, it is possible to find one of these three abstract oppositions. Moreover, each text instantiates these high-level SOs into text-specific local oppositions (i.e., concrete instantiation of oppositions in the text). Attardo et al. (2002) also introduced an intermediate level of abstraction useful to connect the local SO to the abstract opposition. The example (2) illustrates these concepts.

(2) G. Conte: *Occhio ragazzi, Salvini ha trovato il modo per risolvere i problemi dei giovani. Tutti a fare il militare!*

Hey guys, Salvini has found a way to solve the problems of young people. Everyone, join the army!

In (2), at the concrete-textual level, two scripts are opposed: complex, modern, specific problems of young people vs. simplistic solution (cf. military service). The abstract-level opposition is between Real vs. Unreal or also Good vs. Bad. In (3), the humorous interpretation is also supported by linguistic markers (Burger & van



<!-- page 0007 -->

Mulken, 2017). We observe the presence of an exclamation mark (Attardo 2000) together with the emphatic discourse marker *Occhio* (Eng. ‘Pay attention/hey’). These linguistic and textual elements, which support the humorous interpretation, belong to the Language Knowledge Resource, covering all aspects of the text’s verbal formulation (Attardo & Raskin, 1991). From a communicative perspective, (2) can be classified as aggressive humor, with the target of the humorous attack – the “butt” of the humorous text (Attardo, 1994) – being the Italian politician Matteo Salvini.

Therefore, SO was the criterion adopted in the annotation task to distinguish tweets containing humor from the others. In this study, the remaining five knowledge resources stay in the background — an outcome that reflects their conceptual nature. As Attardo (2020: 138) noted, each knowledge resource may be thought of as a collection of tools to analyze a specific aspect of a humorous text.

Additionally, GTVH accounts for register humor, that is a type of “humor caused by incongruity originating in the clash between two registers” (Attardo, 1994: 230–231). Each register and code (i.e., language varieties associated with a specific situation, topic, social role, or social aspect) activates a script that can be in contrast with a script activated by another register. The use of registers as triggers of humor is well described by Attardo (1994: 230–253) and Burger and van Mulken (2017).

### Humor Functions: A Taxonomy

This section outlines the communicative functions of humor, namely the effects and goals the writer pursues through humorous segments (Attardo, 1994: 322–330; Martin et al., 2003). The communicative functions of humor were identified drawing on Stewart (2011), Mendiburo-Seguel et al. (2022), and recent pragmatics research on implicit meanings in political discourse on Twitter (Garassino et al., 2022). Therefore, five functions were identified, i.e., Self-deprecating humor, Aggressive humor, Affiliative humor, Defensive humor, (Self-)Enhancing humor. For each of these functions, we provide a description, accompanied by an example.

Self-deprecating (SDP): the politician humorously targets themselves or their own group/party by referring to real or stereotypical flaws, errors, or shortcomings (Martin et al., 2003). See (3), where Orlando offered a mock admission of guilt.

(3) A. Orlando: *@utente1 Bisogna difendere Blair? Ho sbagliato anche stavolta! Sorry!*

@user1 Should we defend Blair? I was wrong again this time! Sorry!

Aggressive (AGGR): humor directed at attacking or mocking individuals, ideas, political parties, or groups. Such humor can enhance the speaker’s image by presenting them as more intelligent or dominant (Billig, 2005). Consider (4), where Serracchiani used AGGR to criticize, via irony, the actions of the right-wing coalition (represented by two politicians, Meloni and Salvini, who have very different opinions on sanctions against Russia).



<!-- page 0008 -->

(4) D. Serracchiani: *Meloni smentisce Salvini: le sanzioni funzionano. Questa è la coalizione unita!*

Meloni contradicts Salvini by saying that sanctions work. This is the united coalition!

Affiliative (AFF): Friendly and relaxed humor intended to build connection with voters or readers. Even when seemingly aggressive in tone, it fosters closeness and reciprocity (Martin et al., 2003). In (5), Sgarbi – a well-known Italian public personality and politician – reproduced on X a mockingly discourteous conversation he had with a voter:

(5) V. Sgarbi: *“Professore, ho tutti i suoi libri nella lista. Da leggere.” E leggili, stronzo! (con affetto, chiaramente) 😅*

Professor, I have all your books on my list. To be read.” And read them, asshole! (With love, obviously) 😅.

(Self-)Enhancing (SEN): humor that underscores the positive traits and abilities of the speaker, their party, or its leader. For example, the metaphor in (6) is used by Ronzulli to praise the president of her party (the Forza Italia Party).

(6) L. Ronzulli: *Il leone ha ruggito ancora!! #forzaitalia #forzaPresidente*

The lion roared again!! #forzaitalia #forzaPresidente.

Defensive (DEF): Humor used to counter attacks from political rivals by discrediting them comically. It serves as a protective strategy. This function was introduced, although absent in Martin et al. (2003)’s model, because it has been identified as a strategic function in several studies on linguistic implicit meanings in Italian politicians’ speeches (e.g., Cominetti et al., 2024). Consider the positive irony (Attardo, 2020: 388) in (7): a negative judgement (‘look how bad they are’) is used to imply a positive comment (cf. they are not bad). This strategy is used to ridicule the accusation made by those who criticized the bank lending system:

(7) L. Marattin: *Sono soldi che costoro - ma guarda un po’ che cattivi - prima o poi rivogliono indietro, con una remunerazione rapportata al rischio che corrono.*

It’s money that these people want back sooner or later - and look how bad they are -, with a remuneration proportional to the risk they run.

These definitions were integrated into the annotation codebook provided to human annotators to carry out the described tasks (see the online Appendix). Along with examples, they were also used in the prompts for LLMs (“Selected LLMs” section).



<!-- page 0009 -->

## Corpus

The original dataset is composed of 7,552 tweets (automatically extracted), published during the 2022 election campaign (from 25 August to 25 September 2022) by 38 Italian politicians. They were selected to ensure maximum balance among the represented parties and coalitions. Automatic extraction occurred, prior to Twitter’s transition to X, through Tweepy (Roesslein, 2025), an open-source Python Library, that provided a wrapper for the Twitter API.[^1] All tweets in the dataset were previously annotated by an expert annotator (EXP, an Italian PhD student specializing in the linguistics of humor and political discourse) to discriminate humorous tweets from non-humorous tweets. Humorous tweets were classified according to the criteria in Sect. 4.1. Humor markers were also considered, based on Attardo (2000) and Burger and van Mulken (2017). Following this annotation process, 200 tweets were selected for this study: 90 tweets classified as humorous and 110 as non-humorous by EXP. The corpus is available in the online Appendix.

### Selected LLMs

The LLMs examined in this study are GPT-4o and LLaMA-3.3 70b-Instruct (henceforth LLaMA-3.3). GPT-4o (OpenAI, 2025) was a natural choice, given its status as one of the most widely used and investigated commercial LLMs. Typically accessed via the ChatGPT interface, GPT-4o has demonstrated strong performance across a variety of linguistic and pragmatic oriented tasks, including speech act recognition and annotation (Yu et al., 2024; Su & Ye, 2025).

To enable a more robust triangulation of results involving LLMs and to “test other kinds of system descriptions that could match the profile information of human evaluators” (Goes et al., 2023), we also included a second model, LLaMA-3.3 (Grattafiori et al., 2024). Unlike GPT-4o, LLaMA-3.3 is an open-source model, making it particularly appealing for research contexts grounded in Open Science. In this study, LLaMA-3.3 was accessed via the Hugging Face web interface (https://huggingface.co). Regarding the differences between the two models, two main aspects should be considered: accuracy of results and adherence to scientific and ethical standards. In terms of accuracy, GPT-4o shows better results than LLaMA-3.3 in some tasks, such as the annotation of speech acts in corpus pragmatics (Brocca et al., 2026). Given scientific and ethical standards, a key issue is reproducibility (Brocca et al., 2026). Since annotation is a process that should yield consistent results over time, reproducibility is essential. While OpenAI adopts a comparatively less transparent policy regarding model updates and training data, LLaMA provides more open documentation. In particular, running a smaller LLM locally ensures reliance on a fixed model over time, thereby producing outputs that are easier to reproduce.

[^1]: The Twitter API (Application Programming Interface) is a toolset that allows researchers to automatically retrieve and analyze Twitter data.



<!-- page 0010 -->

## Annotation Process

The annotation process consisted of two tasks, presented in Task 1 (Humor Detection) and Task 2 (Humor Functions’ Annotation). Four annotators were involved: two human coders and two LLMs (GPT-4o and LLaMA-3.3). The first human annotator (expert, EXP) served as the baseline against which all other annotations were evaluated. The second human annotator (novice, NOV) is an Italian Master’s student in Linguistics with no prior expertise in humor studies. She was trained exclusively through a codebook containing theoretical information and examples. The human annotators entered their annotations in Excel spreadsheets, following the guidelines described in the codebook. Table 1 provides an overview of the annotation procedure.

### Task 1 (Humor Detection)

As described, 200 tweets were randomly selected from the corpus annotated by EXP: 90 labeled as humorous and 110 as non-humorous. These data were subsequently annotated by the NOV annotator and by the LLMs in order to evaluate agreement on the humor vs. non-humor task. For Task 1, two annotation labels were used: Humor and Non-Humor. The unit of analysis was the tweet. Tweets labeled as humorous were treated as such regardless of the specific types of humor they contained or the number of humorous instances present. For example, a tweet with two puns was classified as humorous in the same way as a tweet containing a single pun, since both display a humorous communicative mode. Before the LLMs performed Task 1, all hyperlinks were removed from the tweets in order to prevent potential processing biases (e.g., issues with reading links).

### Task 2 (Humor Functions’ Annotation)

The second task was conducted on 90 tweets previously classified as humorous by EXP. Each tweet was assigned a single label corresponding to the main communicative function of humor, as defined in “Humor Functions: A Taxonomy” section. Restricting annotation to one label per tweet (see Graham et al., 2016) reduced the likelihood of multiple decisions and thus minimized potential disagreement, albeit at the cost of reduced granularity. Nevertheless, we considered this trade-off acceptable for an exploratory study. An additional NA label covered cases of annotator uncertainty.

**Table 1** Distribution of data and annotators for each annotation task

| Task | Data | Annotators |
|---|---|---|
| 1. Recognizing humorous vs. non-humorous tweets | 200 tweets | EXP, NOV, GPT-4o, LLaMA-3.3 |
| 2. Recognizing functions of humor | 90 humorous tweets | EXP, NOV, GPT-4o, LLaMA-3.3 |



<!-- page 0011 -->

### Prompt Creation

The prompts that were used to gather data from the two LLMs followed a *few-shot* prompting strategy (Brown et al., 2020), which is a prompt that provides the model with several examples, enabling it to generalize patterns with minimal data. Specifically, the prompt included examples of Italian political tweets that were not part of the main analysis dataset. The prompts are available in the online Appendix.

For the first research question (RQ1), the initial prompt provided the models with a definition of humor (see “Humorous vs. Non-humorous Tweets” section), along with several examples illustrating what qualifies as humorous or non-humorous according to the definition. The second prompt fine-tuned the information already provided to the LLMs with the help of further examples (each potentially associated with a different pragmatic function of humor). The third prompt presented the 200 target examples from the corpus in batches of ten, to avoid exceeding prompt length limits (see also Yu et al., 2024), for classification.

A similar prompting strategy was used for the second research question (RQ2). The prompts for RQ2 were more complex, as they aimed to instruct the models to identify the communicative functions of humor using categories examined in “Humor Functions: A Taxonomy” section.

## Analysis

### Quantitative Analysis

#### The Distribution of Humor and Humor Functions

In this section, we explore the distribution of humorous versus non-humorous tweets as well as the distribution of communicative functions, based on annotations provided by the EXP annotator. This choice is justified by the fact that EXP serves as the benchmark against which we will evaluate the performance of both human and LLM annotators in “Inter-rater Reliability” section.

Based on EXP’s annotation, 90 tweets were selected as humorous and 110 as non-humorous. As shown in Fig. 1, among these humorous tweets, the most frequent communicative function identified by EXP was “Aggressive” (AGGR), which accounted for the vast majority of cases (71 occurrences). The remaining functions were much less common: “Affiliative” (AFF) humor appeared in only 12 tweets, while “Defensive” (DEF) (1), “Self-deprecating “(SDP) (4), and “(Self-)Enhancing” (SEN) (2) were only marginally attested.

#### Inter-rater Reliability

Due to the design of this study, which aims to assess whether LLMs can be reliable annotators and research assistants, we relied on measures of inter-rater agreement, assessing how much LLMs agree (or not) with a human expert. We begin by examining their ability to distinguish between humorous and non-humorous tweets. From a



<!-- page 0012 -->

[Figure: Bar chart showing distribution of communicative functions of humour (EXP). Y-axis: Count. X-axis labels: aff, aggr, def, sdp, sen. The “aggr” bar is highest, followed by “aff”, then “sdp”, “sen”, and “def”.]

**Fig. 1** The distribution of the communicative functions of humor in the dataset according to EXP ($\chi^2(4) = 199.22$, p < .0001)

descriptive standpoint, this can be initially explored through the confusion matrices in Fig. 2, which show all instances of agreement and disagreement between annotators for each category. Generally, when interpreting the matrices, the darker the color of a tile, the higher the frequency of the corresponding combination.

As shown in Fig. 2, it is immediately apparent that all annotator pairs reached a considerable level of agreement. For example, in the upper-left matrix, when EXP labeled a tweet as humorous, NOV agreed in 83 cases and disagreed in 7. Conversely, when EXP labeled a tweet as non-humorous, NOV concurred in 89 cases, with 21 cases of disagreement.

The counts provided in Fig. 2 reflect only raw (or observed) agreement (Artstein, 2017), which can be misleading, as they do not account for accidental agreement (i.e., a potential agreement among annotators attributable solely to chance). To address this, inter-rater agreement is typically evaluated using indices such as *Cohen’s kappa* and *Gwet’s AC1*.

Both measures are conceptually similar. However, they differ in how expected agreement is calculated (Hoek & Scholman, 2017; Vach & Gerke, 2023). Cohen’s kappa estimates expected agreement from the marginal probabilities that each annotator uses a given category (Artstein, 2017; Artstein & Poesio, 2008; Hoek & Scholman, 2017). In contrast, Gwet’s AC1 adjusts the expected agreement to reduce



<!-- page 0013 -->

[Figure: Three confusion matrices comparing EXP with NOV, GPT, and Llama for identification of non-humor/humor tweets. NOV vs EXP matrix: non-humor/non-humor 89, non-humor/humor 7, humor/non-humor 21, humor/humor 83. GPT vs EXP matrix: 101, 16, 9, 74. Llama vs EXP matrix: 101, 24, 9, 66.]

**Fig. 2** Confusion matrices displaying the frequency of (dis)agreed cases for each annotation pair regarding the identification of (non-)humorous tweets

**Table 2** Inter-rater agreement indices. Identification of the humorous (versus non-humorous) tweets among the different pairs of annotators (EXP representing the benchmark)

|  | EXP / NOV | EXP / GPT-4o | EXP / LLaMA-3.3 |
|---|---|---|---|
| Cohen’s kappa | 0.72<br>($z = 10.3$, $p < .001$) | 0.75<br>($z = 10.6$, $p < .001$) | 0.66<br>($z = 9.47$, $p < .001$) |
| *Gwet’s AC1* | 0.86<br>(SE = 0.05, $p < .001$) | 0.87<br>(SE = 0.05, $p < .001$) | 0.83<br>(SE = 0.05, $p < .001$) |

sensitivity to skewed category distributions (Hoek & Scholman, 2017), making it particularly suitable for corpus linguistics where it is usual that some categories occur frequently whereas others are rare. This is particularly relevant for assessing the agreement on the functions of humor (see Fig. 1), where one function, “aggressive”



<!-- page 0014 -->

[Figure: Three confusion matrix heatmaps for annotation pairs. Top-left: NOV vs EXP with labels sen, sdp, na, def, aggr, aff. Top-right: GPT vs EXP with labels sen, sdp, def, aggr, aff. Bottom: Llama vs EXP with labels sen, sdp, def, aggr, aff. Visible counts include high agreement on aggr (62, 53, 54) and aff (10, 9, 7).]

**Fig. 3** Confusion matrices displaying the frequency of (dis)agreed cases for each annotation pair regarding the functions of humor (aff = affiliative; aggr = aggressive; def = defensive; sdp = self-deprecating; sen = self-enhancing)

humor, clearly dominates while the others are much less common. Table 2 reports the results regarding the identification of humorous versus non-humorous tweets.

Overall, following the interpretation of Cohen’s kappa proposed by Landis and Koch (1977: 165), where values between 0.61 and 0.80 indicate “substantial agreement” and values above 0.81 reflect “almost perfect” agreement, all annotator pairs show relatively high levels of agreement. Notably, the EXP and GPT-4o pair yields the most consistent result, even (slightly) outperforming the human-human pair. These findings are corroborated by Gwet’s AC1 scores, which are also generally higher than Cohen’s kappa. However, as with Cohen’s kappa, no universally accepted standard exists for interpreting these values.

Regarding the ability to discriminate between the different functions of humor (see “Humor Functions: A Taxonomy” section), the confusion matrices in Fig. 3 report all the cases of (dis)agreement for each annotation pair.



<!-- page 0015 -->

**Table 3** Inter-rater agreement indices. Identification of the functions of humorous tweets among the different pairs of annotators (EXP representing the benchmark)

|  | EXP / NOV | EXP / GPT-4o | EXP / LLaMA-3.3 |
|---|---|---|---|
| Cohen’s kappa | 0.62<br>($z = 9.17$, $p < .001$) | 0.37<br>($z = 5.53$, $p < .001$) | 0.33<br>($z = 5.15$, $p < .001$) |
| Gwet’s AC1 | 0.83<br>(SE = 0.04, $p < .001$) | 0.70<br>(SE = 0.06, $p < .001$) | 0.69<br>(SE = 0.06, $p < .001$) |

Unlike the data in Fig. 2, the results in Fig. 3 reveal clearer differences between the human–human pair and the human–LLM pairs, as the annotations produced by GPT-4o and LLaMA-3.3 exhibit greater variability. Table 3 presents the corresponding Cohen’s kappa scores.

As is common in studies involving pragmatic annotation (Brocca et al., 2026; Garassino et al., 2022; Spooren & Degand, 2010), the annotation of communicative functions of humor, owing to its inherent subjectivity and vagueness, yields considerably lower agreement values than those reported in Table 2.

Regarding Cohen’s kappa, only the human annotator pair achieved a level of “substantial” agreement. The EXP-LLMs pairs, by contrast, reached at best a “fair” agreement (0.21–0.40, according to Landis & Koch, 1977). Due to skewed distribution of the data (see Fig. 2), the results from Gwet’s AC1 may provide a more reliable and less biased assessment in this case. Indeed, these results may show a more optimistic picture. However, in this case as well, the human-human pair achieved a higher agreement score.

In “Qualitative Results” section, we will examine the cases in which human annotators and LLMs agree or disagree.

## Qualitative Results

Considering Task 1, the highest level of agreement between the LLM-driven annotation and the expert annotator was found in tweets containing clear semantic cues, such as unexpected vocabulary within the given context, emojis, or other conventional humor markers. In (8), the use of *ebbene* (“well”) adopts an elevated, slightly formal register that contrasts with the trivial situation described. This incongruity, reinforced by the laughing emoji, signals the humorous intent of the tweet (Yus, 2025).

| Tweet | Human annotators | LLMs |
|---|---|---|
| (8) V. Sgarbi: *Ebbene sì, mi è arrivata la bolletta.* 😅<br>Well, yes, the electric bill has come due for me😅 | humor | humor |

As observed in “Quantitative Analysis” section, instances of disagreement between human–human and human–LLM pairs tend to follow different patterns. In this section, we examine these cases in greater detail, focusing specifically on situations in which GPT-4o and LLaMA-3.3 converged on the same choice, in contrast with both NOV and EXP. As Figs. 2 and 3 illustrate, disagreements also occur within the human–human pair as well as between the two LLMs. Since our main aim is to compare human and LLM annotations, we will not address these latter cases here.



<!-- page 0016 -->

In (9–10), there is agreement among human annotators on the humorous interpretation but both LLMs classified them as non-humorous:

| Tweet | Human annotators | LLMs |
|---|---|---|
| (9) E. Letta: *La “moderata” #Meloni annuncia che cambieranno la #Costituzione da soli.*<br>The “moderate” #Meloni announces that they will change the #Constitution alone. | humor | non-humor |
| (10) V. Sgarbi: *Monumenti nell’incuria a Calderara di Reno, dove governa la Sinistra. Altro che ‘buon governo’.*<br>Calderara di Reno’s abandoned monuments—despite years of left-wing rule. So much for ‘good governance’. | humor | non-humor |

In (9–10), two ironic utterances are marked by the use of distancing quotation marks, namely: *la “moderata” Meloni* (“moderate” #Meloni) and ‘*buon governo*’ (‘good governance’). In (9), the positive Italian adjective *moderata* is incongruous and inappropriate in relation to the (following) co-text, where it is mentioned that the government intends to modify the Italian Constitution without considering the Parliament, thus behaving in an authoritarian way. Something similar occurs in (10): *buon governo* (‘good governance’) is an inappropriate expression to refer to an administration that has left the city’s main monuments in a state of neglect.

Notably, the misinterpretation of the LLMs seems to depend on the interpretation of quotation marks as markers of reported discourse, rather than as pragmatic cues prompting the reader to infer a non-prototypic reading of the linguistic content (Gutzmann & Stei, 2011), i.e., one that frames the quoted material as inappropriate and inconsistent with its context.

Interestingly, (11) represents a situation where human annotators interpret it as humorous, but the LLMs disagree. For clarity, Marattin refers to the slogan “burn private jets, not the planet”.

| Tweet | Human annotators | LLMs |
|---|---|---|
| (11) L. Marattin: *In attesa che lo stesso slogan abbia “proprietà” al posto di “jet” (è solo questione di tempo, visti i soggetti), una riflessione: al 31/12/2021 risultano 133 jet privati registrati fiscalmente in Italia. Sicuramente abolendoli si risolve il problema dell’ambiente nel mondo.*<br>While we wait for the same slogan to change from “property” to “jet” (it’s only a matter of time, given the subjects), a thought: as of December 31, 2021, there were 133 private jets registered for tax purposes in Italy. Abolishing them would certainly solve the global environmental problem. | humor | humor (LLaMA-3.3)<br>non-humor (GPT-4o) |

In (11), the final statement is a case of irony (a type of humor): the reader must imply the opposite of what is asserted.[^2] Interestingly, the humorous tone, in addition to the two human annotators, is only picked up by LLaMA and not by GPT-4o, which classifies the tweet as non-humorous. Probably the absence of humor markers (e.g., emojis, punctuation marks, typographical characters) may have influenced the misin-

[^2]: (11) is a reply to a criticism targeted to Marattin’s party leader, regarding the use of private flights.



<!-- page 0017 -->

terpretation of (12) by GPT-4o. In the following examples, we discuss cases in which human annotators disagree with LLMs about the functions of humor.

| Tweet | Human annotators | LLMs |
|---|---|---|
| (12) G. Crosetto: @utente1 😂😂😂*tana che?? Era l’unico partito di opposizione!* 😂😂<br>@user1 😂😂😂 How so?? It was the only opposition party! 😂😂 | aggressive | affiliative (GPT-4o)<br>aggressive (LLaMA-3.3) |
| (13) V. Sgarbi: *Gli italiani incazzati votano i moderati.*<br>Pissed-off Italians votes for the moderates | affiliative | aggressive |

In (12), Crosetto mocks another user, employing multiple face-with-tears emojis that reinforce the derisive tone. Example (12) is clearly aggressive, as recognized by the human annotators and LLaMA, but not by GPT-4o, which may have misinterpreted the emojis’ function, i.e., as an expression of affiliation. This example also shows the disagreement between the two LLMs. In (13), the Italian adjective *incazzati* (‘pissed-off’) is a dysphemism that may have influenced LLMs to interpret (13) as aggressive. However, the tweet is used with a playful intent: Sgarbi intends to create a paradox between being “pissed-off” citizens and voting for the moderates. This latter expression also activates a humorous pun (Hempelmann & Miller, 2017: 97): *moderati* (‘moderates’) indicates both calm, rational people and the political representatives of Sgarbi’s party *Noi Moderati* (‘We, the Moderates’). In (13), any form of aggression is merely simulated.

Considering (12)-(13), LLMs seem to focus on the explicit and lexical component of the text also including the use of emojis, not implementing the complex inferential reasoning that would have led to a correct interpretation of the message and the communicative purposes that the authors of the tweets aimed to achieve. When tweets require inferential reasoning, human annotators appear to provide more reliable evaluations (even accounting for occasional errors). This advantage may also stem from human annotators’ greater familiarity with the context of Italian politics and the dynamics of the 2022 elections.

## Discussion

Two tasks were carried out by two human annotators (one expert and one novice) and two LLMs (GPT-4o and LLaMA-3.3). Task 1 focused on recognizing humorous and non-humorous tweets, while Task 2 involved annotating humorous tweets according to five labels representing different humor functions.

In Task 1, the tested LLMs demonstrated high inter-rater agreement with the expert annotator, with GPT-4o slightly outperforming the novice annotator.

In Task 2, LLMs performance reached only moderate agreement with the baseline provided by the expert annotator. Inter-rater agreement on the functions of humor (RQ2) was lower than in Task 1, suggesting that LLMs find classifying humor types more challenging than simply detecting humor. Non-aligning annotations in this second task followed identifiable patterns, as the models tended to rely on superficial linguistic cues.



<!-- page 0018 -->

The results of both tasks align with previous findings on the limited pragmatic competence of LLMs (Brocca et al., 2026; Brocca et al., in review; Garassino et al., 2025; Kabbara & Cheung, 2022; Sieker & Zarrieß, 2023). These studies indicate that models may rely on lexical cues when annotating, rather than demonstrating a true pragmatic human-like understanding of pragmatic categories. These results allow us to answer the research questions as follows:

RQ1: When prompted with the instructions described in “Prompt Creation” section, LLMs are able to detect humor with considerable effectiveness in the given corpus of tweets.

RQ2: The annotation of communicative functions of humor shows only moderate agreement with the baseline established by the expert annotator.

In sum, for humor-detection tasks in which lexical and semantic cues may be relevant, such as distinguishing humorous from non-humorous content (Task 1), LLMs can reach and in some cases slightly exceed a novice-level of humor interpretation. By contrast, tasks such as Task 2 cannot be resolved on the basis of semantic cues alone, as they require pragmatic reasoning capable of identifying the illocutionary force of the message and ensuring coherence with the relevant context, which is not always recoverable from a single tweet. Such a task is intrinsically characterized by a higher degree of subjectivity, which results in low inter-rater agreement even among human annotators (Garassino et al., 2022), and it could not be reliably solved by the LLMs tested in this study.

Despite their limitations, the tested LLMs offer notable advantages: they can streamline annotation processes, reduce time and costs, mitigate errors arising from human annotator fatigue, and remain accessible to linguists without programming experience.

## Conclusion

This study corroborates earlier findings showing that LLMs performance largely depends on the recognition of lexical and semantic patterns, whether acquired during training or supplied through prompting. While this pattern-based strategy proved sufficient to classify many tweets with relatively high accuracy, the results also confirm that the two LLMs examined (GPT-4o and LLaMA-3.3-70B) are best suited as support tools in the initial stages of pragmatic corpus annotation, rather than as substitutes for human interpretation when deeper pragmatic or cultural dimensions of humor are involved. In particular, GPT-4o and LLaMA-3.3-70B demonstrate substantial effectiveness in reducing the overall time required for corpus annotation, while still yielding accurate results. Furthermore, the training times associated with the LLMs examined are markedly shorter than those demanded of human annotators, who must first undergo extensive familiarization with annotation codebooks. The main limitation of the study is the absence of a “true” gold standard. Annotations produced by an expert were used as a reference; however, a robust gold standard would require inter-rater agreement among multiple experts and a formal consensus procedure. This limitation prevented the use of standard evaluation measures such as the F1 score. Another challenge concerns there construction of the social and interactional context



<!-- page 0019 -->

necessary for humor interpretation. Short-term improvements may be achieved by systematically incorporating co-text, while broader extensions should consider multimodal humor, including images and GIFs. Further testing should prioritise LLaMA, which presents fewer issues related to reproducibility and scientific ethics, and aim to improve performance in the annotation of pragmatic phenomena through parameter adjustment based on alignment with a gold standard. In addition, experimentation with different prompting strategies, as well as alternative approaches involving model fine-tuning (e.g., Fuoli et al., 2025), may further enhance performance in the annotation of such phenomena.

**Supplementary Information** The online version contains supplementary material available at https://doi.org/10.1007/s41701-026-00235-7.

**Author Contributions** Antonio Bianco: Investigation, Resources, Data Curation, Writing - Original Draft; Antonio Bianco wrote: “Automatic Analysis of Humor” (together with Davide Garassino); “Humorous vs. Non-humorous Tweets”; “Humor Functions: A Taxonomy”; “Qualitative Results”. Nicola Brocca: Conceptualization, Methodology, Software, Investigation, Writing Original Draft, Review & Editing, Supervision: Nicola Brocca wrote: “Introduction”, “Challenges in Pragmatic Annotation”, “Technology-assisted Pragmatic Annotation”, “Discussion”, “Conclusion”. Davide Garassino: Conceptualization, Methodology, Formal analysis, Investigation, Data Curation, Writing Original Draft, Review & Editing, Supervision; Davide Garassino wrote: “Automatic Analysis of Humor” (together with Antonio Bianco), Corpus, Selected LLMs, Annotation Process, Prompt Creation, Qualitative Results.

**Funding** Open access funding provided by University of Innsbruck and Medical University of Innsbruck. Open access funding provided by University of Innsbruck.

**Data Availability** The following data are available at: https://doi.org/10.17605/OSF.IO/WPCR6 A. An Excel file containing annotations of 200 tweets by four annotators (two human and two LLMs). B. An Excel file containing annotations of 90 humorous tweets by the same four annotators. C. A file with the two prompts provided to the LLMs. D. The codebooks used by human annotators. E. The R script used for data processing and analysis.

## Declarations

**Competing interest** The authors declare no competing interests.

**Ethics Approval** The authors confirm that the research was conducted in accordance with relevant institutional and international guidelines, and that there are no ethical issues associated with this work.

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.



<!-- page 0020 -->

## References

Artstein, R. (2017). Inter-annotator agreement. In N. Ide & J. Pustejovsky (Eds.), *Handbook of linguistic annotation* (pp. 297–314). Springer. https://doi.org/10.1007/978-94-024-0881-2_11

Artstein, R., & Poesio, M. (2008). Inter-coder agreement for computational linguistics. *Computational Linguistics, 34*(4), 555–596.

Attardo, S. (1994). *Linguistic theories of humor*. Mouton de Gruyter.

Attardo, S. (2000). Irony markers and functions: Towards a goal-oriented theory of irony and its processing. *Rask, 12*(1), 3–20.

Attardo, S. (2020). *The linguistics of humor*. Oxford University Press.

Attardo, S., Hempelmann, C. F., & Di Maio, S. (2002). Script oppositions and logical mechanisms: Modeling incongruities and their resolutions. *Humor: International Journal of Humor Research, 15*(1), 3–46.

Attardo, S., & Raskin, V. (1991). Script theory revisited: Joke similarity and joke representation model. *Humor: International Journal of Humor Research, 4*(3–4), 239–347.

Baker, P. (2023). *Chatgpt. For dummies*. John Wiley & Sons Inc.

Bianchi, C. (Ed.). (2004). *The semantics/pragmatics distinction*. CSLI Publications.

Billig, M. (2005). *Laughter and ridicule: Towards a social critique of humor*. Sage.

Binsted, K. (2006). Computational humor. *IEEE Intelligent Systems, 21*(2), 59–69. https://doi.org/10.1109/MIS.2006.22

Brocca, N., Nuzzo, E., & Wang, J. (2026). AI-driven speech act annotation: ChatGPT achieves the highest accuracy, while LLaMA and LadderWeb provide stable results. *AI-Linguistica*.

Brocca, N., Nuzzo E., & Wang J. (under review). Machine Learning for Pragmatic Annotation: Comparing Supervised and Pre-Trained Models in Speech Act Tagging

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., & Amodei, D. (2020). Language models are few-shot learners. *arXiv*. https://doi.org/10.48550/arXiv.2005.14165

Burger, C., & van Mulken, M. (2017). Humor markers. In S. Attardo (Ed.), *The Routledge handbook of language and humor* (pp. 385–399). Routledge.

Carvalho, P., Sarmento, L., Silva, M. J., & De Oliveira, E. (2009). Clues for detecting irony in user-generated contents: Oh... it’s so easy:-). In *Proceedings of the 1st International CIKM Workshop on Topic-Sentiment Analysis for Mass Opinion* (pp. 53–56). ACM.

Cavasso, L., & Taboada, M. (2021). A corpus analysis of online news comments using the appraisal framework. *Journal of Corpora and Discourse Studies, 4*, 1–38.

Chiruzzo, L., Castro, S., Etcheverry, M., Garat, D., Prada, J. J., & Rosá, A. (2019, September 24). Overview of HAHA at IberLEF 2019: Humor analysis based on human annotation. In *Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2019)*, Bilbao, Spain. http://ceur-ws.org/Vol-2421/HAHA_paper1.pdf

Cominetti, F., Gregori, L., Lombardi Vallauri, E., & Panunzi, A. (2024). IMPAQTS: A multimodal corpus of parliamentary and other political speeches in Italy (1946–2023), annotated with implicit strategies. In *Proceedings of the IV Workshop on Creating, Analysing, and Increasing Accessibility of Parliamentary Corpora (ParlaCLARIN) @ LREC-COLING 2024* (pp. 101–109). ELRA & ICCL.

Dynel, M. (2009). Beyond a joke: Types of conversational humour. *Language and Linguistics Compass, 3*(5), 1284–1299.

Fuoli, M., Huang, W., Littlemore, J., Turner, S., & Wilding, E. (2025). Metaphor identification using large language models: A comparison of RAG, prompt engineering, and fine-tuning. *arXiv*, 1–17. https://doi.org/10.48550/arXiv.2509.24866

Garassino, D., Brocca, N., & Masia, V. (2022). Is implicit communication quantifiable? A corpus-based analysis of British and Italian political tweets. *Journal of Pragmatics, 194*, 9–22. https://doi.org/10.1016/j.pragma.2022.03.024

Garassino, D., Brocca, N., & Masia, V. (2025). ChatGPT for President! Presupposed content in politicians versus GPT-generated texts. *Applied Corpus Linguistics, 5*(3), 100156. https://doi.org/10.1016/j.acorp.2025.100156

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), e2305016120. https://doi.org/10.1073/pnas.2305016120



<!-- page 0021 -->

Goes, F., Volpe, M., Sawicki, P., Grzes, M., & Watson, J. (2023). Pushing GPT’s creativity to its limits: Alternative uses and Torrance tests. In *Proceedings of the 14th International Conference for Computational Creativity (ICCC 2023).* https://figshare.le.ac.uk/articles/conference_contribution/Pushing_GPT_s_Creativity_to_Its_Limits_Alternative_Uses_and_Torrance_Tests/24324436

Graham, T., Jackson, D., & Broersma, M. (2016). New platform, old habits? Candidates’ use of Twitter during the 2010 British and Dutch general election campaigns. *New Media & Society, 18*(5), 765–783. https://doi.org/10.1177/1461444814546728

Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Vaughan, A., Yang, A., Fan, A., Goyal, A., Hartshorn, A., Mitra, A., Koreneve, A., & Hinsvark, A. (2024). & others. The LLaMA 3 herd of models. *arXiv.* https://arxiv.org/abs/2407.21783.

Gutzmann, D., & Stei, E. (2011). How quotation marks what people do with words. *Journal of Pragmatics, 43*(10), 2650–2663. https://doi.org/10.1016/j.pragma.2011.03.010

Hamilton, K., Longo, L., & Bozic, B. (2024). GPT-assisted annotation of rhetorical and linguistic features for interpretable propaganda technique detection in news text. In *Companion Proceedings of the ACM Web Conference 2024 (WWW ’24)* (pp. 1431–1440). ACM. https://doi.org/10.1145/3589335.3651909

Hempelmann, C. F., & Miller, T. (2017). Puns: Taxonomy and Phonology. In S. Attardo (Ed.), *The Routledge Handbook of Language and Humor* (pp. 95–108). Routledge.

Hoek, J., & Scholman, M. (2017). Evaluating discourse annotation: Some recent insights and new approaches. In *Proceedings of the 13th Joint ISO-ACL Workshop on Interoperable Semantic Annotation (ISA-13)* (pp. 1–13). https://aclanthology.org/W17-7401

Jentzsch, S., & Kersting, K. (2023). ChatGPT is fun, but it is not funny! Humor is still challenging large language models. In *Proceedings of the 13th Workshop on Computational Approaches to Subjectivity, Sentiment, & Social Media Analysis* (pp. 325–340).

Joseph, B. (2008). The editor’s department: Last scene of all… *Language 84,* 686–690.

Kabbara, J., & Cheung, J. C. K. (2022). Investigating the performance of transformer-based NLI models on presuppositional inferences. In *Proceedings of the 29th International Conference on Computational Linguistics* (pp. 779–785). International Committee on Computational Linguistics.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174.

Ma, B., Li, Y., Zhou, W., Gong, Z., Liu, Y. J., Jasinskaja, K., Friedrich, A., Hirschberg, J., Kreuter, F., & Plank, B. (2025). Pragmatics in the era of large language models: A survey on datasets, evaluation, opportunities and challenges. *arXiv.* https://arxiv.org/abs/2502.12378

Martin, R. A., Puhlik-Doris, P., Larsen, G., Gray, J., & Weir, K. (2003). Individual differences in uses of humor and their relation to psychological well-being: Development of the Humor Styles Questionnaire. *Journal of Research in Personality, 37*(1), 48–75. https://doi.org/10.1016/S0092-6566(02)00534-2

Mendiburo-Seguel, A., Alenda, S., Ford, T. E., Olah, A. R., Navia, P. D., & Argüello-Gutiérrez, C. (2022). #funnypoliticians: How do political figures use humor on Twitter? *Frontiers in Sociology, 7,* 788742. https://doi.org/10.3389/fsoc.2022.788742

O’Keeffe, A. (2018). Corpus-based function-to-form approaches. In A. Jucker, K. P. Schneider, & W. Bublitz (Eds.), *Methods in pragmatics* (Handbooks of Pragmatics 10, pp. 587–618). De Gruyter Mouton. https://doi.org/10.1515/9783110424928-023

OpenAI (2025). ChatGPT-4o [Large language model]. https://openai.com/chatgpt

Ostyakova, L., Smilga, V., Petukhova, K., Molchanova, M., & Kornev, D. (2023). ChatGPT vs. crowdsourcing vs. experts: Annotating open-domain conversations with speech functions. In *Proceedings of the 24th Annual Meeting of the Special Interest Group on Discourse and Dialogue* (pp. 242–254). Association for Computational Linguistics.

Quan, K., Ramakrishnan, P., & Chin, J. (2025). Can AI take a joke—or make one? A study of humor generation and recognition in LLMs. In *Proceedings of the 2025 Conference on Creativity and Cognition (C&C ’25),* (pp. 431–437). Association for Computing Machinery.

Raskin, V. (1985). *Semantic mechanisms of humor.* Reidel.

Roesslein, J. (2025). Tweepy (Version 4.12.0). *Zenodo.* https://doi.org/10.5281/zenodo.7296886. [Computer software].

Scott-Phillips, T. C. (2017). Pragmatics and the aims of language evolution. *Psychonomic Bulletin & Review, 24*(1), 186–189. https://doi.org/10.3758/s13423-016-1061-2

Settaluri, L. S., Doshi, M., Kalyan, T. P., Bhattacharyya, P., Murthy, R., & Dabre, R. (2024). PUB: A pragmatics understanding benchmark for assessing LLMs’ pragmatics capabilities. *arXiv.* https://arxiv.org/abs/2401.07078



<!-- page 0022 -->

Sieker, J., & Zarrieß, S. (2023). When your language model cannot even do determiners right: Probing for anti-presuppositions and the maximize presupposition! principle. In *Proceedings of the 6th Black-boxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP* (pp. 180–198). Association for Computational Linguistics.

Spooren, W., & Degand, L. (2010). Coding coherence relations: Reliability and validity. *Corpus Linguistics and Linguistic Theory, 6*(2), 241–266. https://doi.org/10.1515/cllt.2010.009

Stewart, P. A. (2011). The influence of self-and other-deprecatory humor on presidential candidate evaluation during the 2008 US election. *Social Science Information, 50*(2), 201–222.

Su, H., & Ye, J. (2025). Large language models for automating fine-grained speech act annotation: A critical evaluation of GPT-4o and DeepSeek. *Corpus Pragmatics*. https://doi.org/10.1007/s41701-025-0020-w

Vach, W., & Gerke, O. (2023). Gwet’s AC1 is not a substitute for Cohen’s kappa: A comparison of basic properties. *MethodsX, 10*, 102212. https://doi.org/10.1016/j.mex.2023.102212

Weisser, M. (2015). Speech act annotation. In K. Aijmer, & C. Rühlemann (Eds.), *Corpus pragmatics: A handbook* (pp. 84–110). Cambridge University Press.

Weisser, M. (2016). DART – The dialogue annotation and research tool. *Corpus Linguistics and Linguistic Theory, 12*(2), 355–388. https://doi.org/10.1515/cllt-2014-0051

Weisser, M. (2018). *How to do corpus pragmatics on pragmatically annotated data: Speech acts and beyond*. John Benjamins.

Xu, Z., Yuan, S., Chen, L., & Yang, D. (2024). A good pun is its own reward: Can Large Language Models understand puns? In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 11766–11782). Association for Computational Linguistics.

Yu, D. (2025). Towards LLM-assisted move annotation: Leveraging ChatGPT-4 to analyse the genre structure of CEO statements in corporate social responsibility reports. *English for Specific Purposes, 78*, 33–49. https://doi.org/10.1016/j.esp.2024.11.003

Yu, D., Li, L., Su, H., & Fuoli, M. (2024). Assessing the potential of LLM-assisted annotation for corpus-based pragmatics and discourse analysis: The case of apology. *International Journal of Corpus Linguistics, 29*(4), 534–561. https://doi.org/10.1075/ijcl.23087.yu

Yus, F. (2025). *Emoji Pragmatics*. Palgrave MacMillan.

Zangari, A., Marcuzzo, M., Albarelli, A., Taher Pilehvar, M. (2025). Pun Unintended: LLMs and the Illusion of Humor Understanding. *arXiv:2509.12158*. (21.12.2025).

Zhao, T., & Kawahara, T. (2019). Joint dialog act segmentation and recognition in human conversations using attention to dialog context. *Computer Speech & Language, 57*, 108–127. https://doi.org/10.1016/j.csl.2019.03.001

Zhu, Y., Zhang, P., Haq, E. U., Hui, P., & Tyson, G. (2023). Can ChatGPT reproduce human-generated labels? A study of social computing tasks. *arXiv*. https://doi.org/10.48550/arXiv.2304.10145

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
