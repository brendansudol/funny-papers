<!-- Transcribed from x39-how-humorous-ai.pdf -->



<!-- page 0001 -->

Computers in Human Behavior Reports 20 (2025) 100807

[Figure: Elsevier journal banner with Elsevier logo, “Contents lists available at ScienceDirect,” “Computers in Human Behavior Reports,” journal homepage URL, and red journal cover image]

Contents lists available at ScienceDirect

# Computers in Human Behavior Reports

journal homepage: www.sciencedirect.com/journal/computers-in-human-behavior-reports

# How humorous is AI? Exploring ChatGPT’s role in humor generation and human-AI interaction

Yi Cao <sup>a</sup>, Jiahao Cao <sup>a</sup>, Yubo Hou <sup>a,*</sup>, Li-Jun Ji <sup>b,**</sup>

<sup>a</sup> *School of Psychological and Cognitive Sciences and Beijing Key Laboratory of Behavior and Mental Health, Peking University, Beijing, 100871, China*  
<sup>b</sup> *Queen’s University, Canada*

| A R T I C L E  I N F O | A B S T R A C T |
|---|---|
| *Keywords:*<br>Artificial intelligence<br>Human-AI interaction<br>Humor generation<br>Humor coping<br>Sense of humor | The rapid evolution of artificial intelligence has raised important questions about its ability to replicate nuanced human cognitive functions – particularly humor generation. This research investigates GPT-4o, an advanced language model, focusing on its capacity to generate humor, how it compares to human-generated humor, and its potential applications in human-AI interaction. The main variables include humor generation, coping, strategy, and interpersonal conflict. We hypothesize that GPT-4o outperforms humans in humor generation and can help individuals manage interpersonal conflicts by effectively using humor, based on a theoretical framework that integrates humor theory and human-AI interaction models. Drawing on data from a racially diverse sample from the U.S. the research employs experimental methods across four studies. Study 1 compares GPT-4o and human humor generation using textual and visual prompts. Study 2 examines how social context (positive vs. negative) influences humor coping strategies in both AI and human responses. Study 3 identifies the most effective humor types in negative social contexts. Study 4 explores GPT-4o’s role in managing interpersonal conflict through humor in human-AI interaction. Findings reveal that GPT-4o excels in generating sentence-based humor, particularly in response to negative social contexts, and outperforms humans in humor coping strategies. In response to negative contexts, both humans and GPT-4o identify self-enhancing humor as the most effective strategy. Furthermore, GPT-4o demonstrates effectiveness in conflict resolution, as evidenced by positive feedback from both humor senders and recipients. These results offer theoretical and practical insights into AI’s emerging role in emotional support, stress reduction, and socially sensitive communication. |

## 1. Introduction

Humor and laughter have long been regarded as uniquely human phenomena. Aristotle stated in *The Parts of Animals* that humans are “the only animals that laugh” (Aristotle, 350 BCE/2014), highlighting the distinctive role of humor in human cognition, emotion, and social behavior (Martin & Ford, 2018). Today, with the rapid advancement of artificial intelligence (AI), particularly the emergence of large language models (LLMs), new questions arise about the nature and future of humor. Can AI produce humor that rivals human creativity, including different styles and forms? Furthermore, can AI help humans use humor more effectively, especially in challenging interpersonal situations?

These questions extend beyond mere technical capabilities, delving into the intersections of machine cognition, human emotion, and the evolving dynamics of human–AI interactions. The present research investigates ChatGPT (GPT-4o) as a tool for humor generation, focusing on the nuances of humor styles and their application across various contexts. It also examines whether GPT-4o can assist individuals in leveraging humor to navigate negative or sensitive situations more effectively.

### 1.1. Research on AI and humans

The current literature on the relationship between artificial intelligence and humans primarily focuses on two key aspects. One examines how AI compares to humans in terms of cognitive and behavioral functioning. In abstract cognition, Binz and Schulz (2023) found that GPT-3 solved several vignette-based tasks at or above human level and

---

\* Corresponding author. School of Psychological and Cognitive Sciences and Beijing Key Laboratory of Behavior and Mental Health, Peking University, Beijing, 100871, China.  
\*\* Corresponding author. Queen’s University, Canada.  
*E-mail addresses:* cyaoyi@pku.edu.cn (Y. Cao), caojiahao66@stu.pku.edu.cn (J. Cao), houyubo@pku.edu.cn (Y. Hou), lijunji@queensu.ca (L.-J. Ji).

https://doi.org/10.1016/j.chbr.2025.100807  
Received 21 April 2025; Received in revised form 20 August 2025; Accepted 17 September 2025  
Available online 25 September 2025  
2451-9588/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).



<!-- page 0002 -->

outperformed humans in a multi-armed bandit task but performed poorly in a causal reasoning task. Similarly, Suri et al. (2024) reported that GPT-3.5 exhibited four classic human decision heuristics: anchoring, representativeness, framing, and the endowment effect (Tversky & Kahneman, 1974). Webb et al. (2023) further found that GPT-3 matched or surpassed human performance on a range of analogical reasoning tasks. These studies suggest that while large language models excel in certain cognitive tasks, their abilities in more complex reasoning remain limited.

In social cognition, large language models demonstrate both strengths and limitations. Kosinski (2024) found that ChatGPT-4 solved 75 % of false-belief tasks, matching the performance of 6-year-old children reported in prior studies. Strachan et al. (2024) reported that GPT-4 performed at or above human level on tasks involving false beliefs and indirect requests but showed difficulty in detecting faux pas—socially inappropriate remarks or actions that may cause embarrassment or offense. Moreover, Mao et al. (2025) found that ChatGPT’s metaphorical mappings generally align with human patterns but diverge in the medical domain.

In communicative behavior, GPT models also show notable capabilities. Gilardi et al. (2023) found that zero-shot GPT-3.5 outperformed crowd workers in text-annotation tasks, achieving higher accuracy and intercoder agreement, even exceeding the consistency of trained human annotators. However, Mahowald et al. (2024) noted that while large language models perform well on formal linguistic tasks involving syntactic and hierarchical structure, their abilities remain inconsistent on functional language tasks that require real-world understanding and reasoning.

Another focus of current literature on AI and humans explores how AI systems may support or enhance human performance in specific tasks, particularly in creativity and collaboration. In creative problem-solving contexts, studies have shown that AI support can significantly improve human performance. For example, Urban et al. (2024) demonstrated that university students using GPT-3.5 produced solutions with higher quality, elaboration, and originality. Similarly, Doshi and Hauser (2024) found that GPT-4 improved individual creativity in story generation, particularly among less creative participants, though it also led to reduced diversity at the group level. Wei et al. (2025) reported that GPT-4o significantly enhanced team creativity in collaborative digital storytelling tasks, and Lee and Chung (2024) found that GPT-3.5 improved creativity across diverse real-world problem-solving tasks, even under high task constraints and in scenarios requiring empathy. Beyond individual creativity, AI has also been studied in collaborative settings. A meta-analysis of 106 experiments showed that, on average, human-AI collaboration does not surpass the best of the two agents alone (Vaccaro et al., 2024). However, recent evidence indicates that hybrid human-AI systems combining medical professionals with large language models outperform both human-only and AI-only groups in open-ended diagnostic tasks by leveraging complementary error patterns (Zöller et al., 2025).

In addition to creative and collaborative tasks, a growing number of studies have examined the role of generative AI in learning and academic performance. Tang et al. (2025) found that AI-assisted teaching significantly improved students’ learning satisfaction compared with traditional computer-assisted instruction; however, higher learning engagement and knowledge test scores were only observed when teacher supervision was present. Wang et al. (2024) reported that Chinese undergraduates perceived generative AI to enhance learning efficiency, motivation, and cognitive skills, while also expressing concern that over-reliance might reduce independent thinking. Meta-analyses have confirmed these positive effects: Li et al. (2025) found moderate to large benefits of GenAI chatbots, particularly ChatGPT, on second language acquisition (ES = .58), and Liu et al. (2025) reported moderately positive effects on students’ academic achievement (g = .58), especially in social sciences, declarative knowledge learning, and traditional classroom settings. Likewise, a review of 21 studies showed that ChatGPT-3.5 generally improved knowledge acquisition in higher education, although its effects on skill development were mixed (Jin & Sercu, 2025). Overall, while effectiveness depends on task demands and interaction design—and some studies note reduced output diversity (Doshi & Hauser, 2024)—current evidence suggests that generative AI can meaningfully enhance human performance in creativity, collaboration, and academic learning.

### *1.2. Humor*

Humor is a phenomenon prevalent across all human cultures (Jiang et al., 2019). Scholars have conceptualized humor in different ways: some view humor expression as a behavior, emphasizing (a) the intentionality of the focal actor and (b) the subjective perception of that intent by the audience (Cooper & Schweitzer, 2024). Others conceptualize humor as a personality trait, known as the “sense of humor,” which refers to an individual’s ability to create or appreciate humorous stimuli (Martin & Ford, 2018). Trait-based humor research encompasses multiple dimensions, such as humor generation, recognition, appreciation, coping, and so on (Martin & Ford, 2018; Thorson & Powell, 1993).

The present research specifically focuses on humor generation as a key aspect of trait humor, referring to the active expression of humor by individuals—such as telling jokes to friends or generating original humorous content (Ruch & Heintz, 2019). Humor coping, on the other hand, is considered a subset of humor generation and is used here to assess the degree to which respondents report actively using humor as a strategy to cope with stress in their daily lives (Martin & Lefcourt, 1983). Humor generation is typically measured through tasks such as crafting cartoon captions (Kozbelt & Nishioka, 2010), completing punchlines (Nusbaum et al., 2017), or proposing context-specific humor strategies (Martin & Lefcourt, 1983). More recently, some studies have begun to explore machine learning techniques for humor assessment (Cowie, 2023), offering new possibilities for automated and scalable measurement.

Martin et al. (2003) further classified humor into four types: humor used to enhance one’s relationships with others (affiliative humor), to enhance the self (self-enhancing humor), to enhance the self at the expense of others (aggressive humor), and to enhance relationships at the expense of the self (self-defeating humor). Building on this typology, the present research investigates whether generative AI—specifically GPT-4o—can replicate not only the surface form of humor but also its functional diversity, particularly the four humor types identified by Martin et al. (2003). This question is critical because each humor type serves distinct social, emotional, and psychological functions. Adaptive humor (affiliative, self-enhancing) has been linked to reduced stress, anxiety, and interpersonal tension, as well as improved self-esteem and well-being (Dozois et al., 2009; Hiranandani & Yue, 2014; Klein & Kuiper, 2006). In contrast, maladaptive humor (aggressive, self-defeating) is often associated with interpersonal conflict, anxiety, and poor psychological adjustment (Frewen et al., 2008; Kfrerer et al., 2019; McCullars et al., 2021).

Understanding whether AI tends to over-rely on certain humor types (e.g., affiliative) due to optimization or safety constraints, while avoiding other types (e.g., aggressive), can reveal important aspects of AI’s social intelligence and its contextual sensitivity. Moreover, in emotionally charged or conflictual contexts, it is unclear whether AI can strategically deploy the most effective humor type—such as affiliative humor to defuse tension or self-enhancing humor to boost morale. This capacity may determine whether AI functions as an effective assistant or a socially insensitive agent. This uncertainty motivates our investigation into AI’s ability to emulate the varied functions that different human humor styles serve in social interaction.

### *1.3. Human-AI interaction: the role of humor*

Emerging evidence indicates that AI can generate jokes with certain



<!-- page 0003 -->

limitations. For example, Jentzsch and Kersting (2023) have shown that while ChatGPT-3.5 generates jokes by remixing 25 template patterns, showing syntactic novelty, it lacks semantic creativity and is limited in its ability to create original and intentional humor, although it can accurately recognize and explain certain types of humor.

Systematic research is lacking in addressing several critical aspects of AI humor generation, including: (1) contextual rigidity—Can AI adjust its humor across diverse social contexts (e.g., positive vs. negative social settings)? (2) type imbalance: Does AI generate a disproportionate amount of a particular type of humor due to optimal strategies? (3) conflict resolution: Can AI-generated humor assist humans to resolve real-world conflicts more effectively?

Although direct evidence is limited, research in human-computer interaction suggests that AI humor could improve user engagement and trust. For instance, humorous robots are seen as more socially present and likable (Oliveira et al., 2021), and chatbots with humor enhance users’ task satisfaction and perceptions of the agent’s personality (Niculescu et al., 2013). These findings suggest that AI humor, despite its mechanistic origins, may serve as a scaffolding tool—providing “safe” adaptive humor drafts that humans can refine contextually.

## 2. The present research

The present research consists of four Studies exploring the above issues. Following emerging standards for the use of generative AI in social science research (Call et al., 2024; de Kok, 2025), we aimed to ensure transparency, replicability, and intersubjective comprehensibility throughout the research process. Specifically, we used OpenAI’s ChatGPT (GPT-4o model, August 2024 version) via the ChatGPT web platform. All prompts and operational instructions are included in the supplementary materials for verification and replication purposes. Study 1 compared the similarities and differences between ChatGPT (GPT-4o) and humans in humor generation tasks of various types (e.g., image-based tasks vs. sentence-based tasks). Study 2 examined the humor generation abilities of GPT-4o and humans in different social contexts (e.g., positive vs. negative). Study 3 investigated the types of coping humor employed by GPT-4o in negative contexts and explored whether GPT-4o could adopt optimal strategies for humor use in these situations. Finally, Study 4 examined whether humans could benefit from GPT-4o’s assistance in generating humorous responses in negative social contexts (i.e., interpersonal conflict). All participants received the informed consent form before completing a study. Following JARS (Kazak, 2018), we report in each study how we determined our sample size, all data exclusions (if any), and all measures in the study. All studies were preregistered. Data, material and analysis scripts are available at https://osf.io/j8fv4/?view_only=d59610e8eada4d6d9ead0981b4f94eef.

## 3. Study 1

Given previous research findings that GPT models perform well on natural language processing tasks (Binz & Schulz, 2023), but their ability to handle cross-modal information, such as humor with visual elements, remains unclear, we hypothesized (H1) that AI would perform at least as well as humans on sentence completion humor tasks, which rely primarily on textual processing. In contrast, AI may not perform as well as humans on image captioning tasks, which require integration of visual and linguistic cues. This study was preregistered (https://aspredicted.org/384d-fnk3.pdf).

### 3.1. Method

*Participants.* According to G*Power (Faul et al., 2007), assuming power = .80, at least 200 participants are required for a 2 X 2 mixed design to identify a small interaction effect ($f = .10$). The study consisted of 100 human participants (40 men, 57 women, 3 other genders; $M_{age}$ = 24.65 years, $SD_{age}$ = 3.66; 59 White, 26 Black or African American, 6 Asian, 3 Hispanic or Latino, 3 Native American or Indigenous, 3 Other) recruited via prolific, and 100 AI responses simulated by ChatGPT. We instructed ChatGPT (GPT-4o) to simulate 100 human responses based on the statistical summary of the human participants’ demographic information (see supplementary material).

*Procedure.* We used a 2 (group: human vs. GPT-4o; between-participant) × 2 (task type: image vs. sentence; within-participant) mixed design.

Both human and simulated AI participants completed two humor generation tasks, including an image task and a sentence task, adapted from Yam et al. (2019) and Nusbaum et al. (2017) (see supplementary material). The order of the two tasks was counterbalanced across participants. The image task consisted of two items, where participants were asked to create the funniest captions (they could) for each picture image. The sentence task also consisted of two items, where participants were given two scenarios and asked to complete each scenario with a humorous sentence.

*Rating.* We then recruited 112 American university students,^1 blind to the study, to rate how funny each caption or sentence was on a 7-point scale (1 = *not at all*, 7 = *extremely*). To make the rating task more manageable, each rater rated 100 captions or sentences (50 produced by humans and 50 produced by GPT-4o), and each caption or sentence was rated by 14 raters.

### 3.2. Results

For each participant, we computed the mean rating of the two captions in the image task (Cronbach’s α = .78 for human participants and .76 for GPT-4o participants, respectively), and the mean rating of the two sentence tasks (Cronbach’s α = .79 for human participants and .82 for GPT-4o participants, respectively), and submitted them to a 2 (group: human vs. GPT-4o; between-participant) × 2 (task type: image vs. sentence; within-participant) mixed ANOVA. It revealed a significant interaction effect of group by task type, $F(1, 198) = 90.33$, $p < .001$, $\eta_p^2 = .31$. Specifically, as seen in Fig. 1, human participants created funnier

[Figure: bar chart showing humor generation scores by task. Legend: Human (red) and GPT-4o (blue). Y-axis labeled “Humor generation” from 1 to 5. X-axis labels: “Image task” and “Sentence task”. Human bar is higher than GPT-4o for image task; GPT-4o bar is higher than Human for sentence task. Error bars shown.]

**Fig. 1.** Effects of group and task on the scores on humor generation (Study 1). Error bars represent 95 % CI.

---

^1 For each study, we recruited a different group of student raters following similar procedures to ensure independent evaluation samples.



<!-- page 0004 -->

captions in the image task ($M = 3.88, se = .06$) than GPT-4o ($M = 3.24, se = .06$), $F_{(1, 198)} = 64.31$, $p < .001$, $\eta_p^2 = .25$. In contrast, GPT-4o generated funnier captions in the sentence task ($M = 4.03, se = .06$) than human participants ($M = 3.57, se = .06$), $F_{(1, 198)} = 24.80$, $p < .001$, $\eta_p^2 = .11$.[^2] The results supported Hypothesis 1 by showing that AI outperformed humans in the sentence completion humor task.

## 4. Study 2

Study 2 examined humor coping, i.e., the strategic use of humor in socially appropriate ways to cope with stress in daily lives. We used a task that primarily relies on text-based processing. Based on the findings of Study 1 that GPT-4o outperformed humans in natural language processing tasks (but not in the image task), we expected AI to demonstrate advantages over humans in humor coping. Moreover, according to the benign violation theory (McGraw & Warren, 2010), humor arises when social or moral norms are mildly violated without being perceived as threatening. Generative AI models such as GPT-4o are trained under objectives that prioritize safety and social appropriateness (OpenAI, 2023). Consequently, they tend to generate “safe” forms of humor—particularly affiliative and self-enhancing humor—while avoiding aggressive or self-defeating humor. This computational bias aligns closely with the benign violation mechanism. Accordingly, we proposed Hypothesis 2 (H2): Across both positive and negative contexts, AI-generated humor coping would be evaluated as more humorous; while human-generated humor coping would exhibit greater stylistic diversity, AI would primarily produce affiliative and self-enhancing humor. This study was preregistered (https://aspredicted.org/47z4-rhzm.pdf).

### 4.1. Method

*Participants.* The participants consisted of 97 human participants recruited from Prolific (48 men, 47 women, 2 other genders, $M_{age} = 24.04$ years, $SD_{age} = 3.74$, 63 White, 21 Black or African American, 6 Asian, 4 Hispanic or Latino, 3 Other) and 97 AI responses simulated by ChatGPT (GPT-4o). We instructed GPT-4o to simulate 97 human participants based on the statistical summary of the human participants’ demographic information (see supplementary material).

*Procedure.* We used a 2 (group: human vs. GPT-4o; between-participant) × 2 (context: positive vs. negative; within-participant) mixed design.

Both human and GPT-4o participants were given two contexts: In the positive context the protagonist would be proud; in the negative context the protagonist would be embarrassed (Cao et al., 2024; see supplementary material). Participants were asked to imagine being in each context in real life and to respond humorously. The order of the two contexts was randomized.

#### 4.1.1. Ratings of humor responses

Next, we recruited 104 American university students, blind to the study, to rate how funny each humor response was on a 7-point scale (1 = *not at all*, 7 = *extremely*). To make the rating task more manageable, each rater rated about 48 humor responses (24 produced by humans and 24 produced by GPT-4o) and each humor response was rated by 13 raters (Cronbach’s $\alpha = .82$ for human responses and $.68$[^3] for AI responses).

Then, we recruited two psychology experts specializing in humor research to categorize the humor responses generated by humans and GPT-4o based on the four humor types proposed by Martin et al. (2003). We first presented the definitions of these four types of humor to the coders and selected one example from existing humor coping materials for each type. The coders began the categorization process only after fully understanding the classification criteria.

Finally, we recruited 40 American university students, blind to the study, to rate the effectiveness of humor responses in the negative context[^4] (1 = *not effective at all*, 7 = *very effective*). To make the rating task more manageable, each rater rated about 48 humor responses (24 produced by human and 24 produced by GPT-4o) and each humor response was rated by 10 raters (Cronbach’s $\alpha = .71$ for human responses and $.73$ for AI responses).

### 4.2. Results

*Ratings of funniness.* A 2 (group: human vs. GPT-4o; between-participant) × 2 (context: positive vs. negative; within-participant) mixed ANOVA on ratings of humor responses revealed a significant main effect of group, $F_{(1, 192)} = 61.32$, $p < .001$, $\eta_p^2 = .24$, no significant context main effect, $F_{(1, 192)} = 1.56$, $p = .214$, and a significant interaction effect of group by context, $F_{(1, 192)} = 8.10$, $p = .005$, $\eta_p^2 = .04$. Specifically, as seen in Fig. 2, GPT-4o’s responses to the positive context were funnier ($M = 4.08, se = .08$) than human responses ($M = 3.60, se = .09$), $F_{(1, 192)} = 14.36$, $p < .001$, $\eta_p^2 = .07$. The effect was even stronger in negative context, such that GPT-4o’ responses ($M = 4.21, se = .08$) were much more humorous than human responses ($M = 3.27, se = .08$), $F_{(1, 192)} = 65.98$, $p < .001$, $\eta_p^2 = .26$.[^5]

*Classification of humor responses.* Table 1 shows the experts’ classifications of humor responses. In response to the negative context, GPT-4o generated only self-enhancing humor (with only one exception where the two experts could not agree), while human participants generated all four types of humor. In response to the positive context, both GPT-4o and human participants focused on affiliative and self-enhancing

[Figure: Bar chart comparing funniness ratings for Human (red) and GPT-4o (blue) across Positive context and Negative context. Y-axis labeled “Funny” from 1 to 5; legend labels “Human” and “GPT-4o”; error bars shown.]

**Fig. 2.** Effects of group and context on funniness (Study 2). Error bars represent 95 % CI.

[^2]: We created tables summarizing the results for each study (see supplementary materials).

[^3]: The interrater reliability was slightly below the conventional threshold (e.g., $\alpha = .68$), reflecting moderate agreement among raters. While aggregation across multiple independent raters helps mitigate measurement error, future research should consider enhancing rater training or providing clearer rating guidelines to improve consistency.

[^4]: We did not get raters for responses to positive contexts.

[^5]: Human responses were funnier in the positive context than in the negative context, $F_{(1, 192)} = 8.38$, $p = .004$, $\eta_p^2 = .04$. GPT-4o showed no significant difference between context, $F_{(1, 192)} = 1.28$, $p = .259$.



<!-- page 0005 -->

**Table 1**  
Frequencies of each humor type produced in response to positive and negative contexts (the two numbers in each cell represent frequencies as coded by each of the two experts).

| Context | Humor type | GPT-4o | Human |
|---|---|---:|---:|
| Positive context | Affiliative humor | 47/51 | 46/41 |
|  | Self-enhancing humor | 50/46 | 43/44 |
|  | Aggressive humor | – | – |
|  | Self-defeating humor | – | 6/9 |
|  | Other | – | 2/3 |
| negative context | Affiliative humor | 1/0 | 17/19 |
|  | Self-enhancing humor | 96/97 | 56/58 |
|  | Aggressive humor | – | 16/13 |
|  | Self-defeating humor | – | 7/4 |
|  | Other | – | 0/3 |

humor, with the proportions of these two types being nearly equal in both cases.

***Effectiveness ratings.*** A one-way ANOVA showed a significant effect of group on humor effectiveness. Specifically, humor responses to the negative context generated by GPT-4o ($M=4.29$, $se=.09$) were rated as more effective than human responses ($M=3.80$, $se=.09$), $F(1, 192)=15.45$, $p<.001$, partial $\eta^2=.07$. The results supported Hypothesis 2 and further demonstrated that GPT-4o was more effective than humans in humor-based coping in negative contexts.

## 5. Study 3

Study 2 showed that GPT-4o’s humor responses in negative contexts were rated as more effective than those of humans and showed a clear tendency to employ self-enhancing humor. Given the advantages of self-enhancing humor in both frequency of use and perceived effectiveness, we further examined its role in coping with negative situations. Study 3 aimed to investigate whether self-enhancing humor would be considered the most effective humor type among various humor styles for addressing negative contexts. We hypothesized (H3) that in negative contexts, self-enhancing humor would be rated as the most effective humor type, with humans and AI likely showing convergence in their evaluations. This study was preregistered (https://aspredicted.org/th5y-t2qn.pdf).

### 5.1. Method

***Procedures and participants.*** First, we trained ChatGPT (GPT-4o) by giving it the paper by Martin et al. (2003) to help it understand four types of humor. After GPT-4o stated that it fully understood the types of humor, it was tasked with generating responses to a specific negative context: “You accidentally failed a final exam, but all your roommates had high scores. When they ask about your score, what would you say?” (see supplementary material). We asked GPT-4o to generate 100 humor responses for each type of humor, resulting in a set of responses aligned with the predefined categories. From these, we randomly selected 10 humor responses from each humor type, creating 40 humor responses in total for subsequent evaluation.

Then we recruited 400 human participants (184 men, 210 women, 6 other genders, $M_{age}=40.05$ years, $SD_{age}=13.38$) to rate the 40 humor responses on three items: funniness (“how funny do you find the response”), likability (“how much do you like the response”), and effectiveness (“how effective do you think this response is in helping to cope with this specific context”), using a 7-point scale ($1=$ *not at all*, $7=$ *extremely*). To make the rating task more manageable, each rater evaluated 10 humor responses and each type of humor response got 100 ratings.

In addition, we also tasked GPT-4o with performing the same rating. Each rating was conducted in a separate chat: GPT is capable of learning within a single chat session by remembering both its own and the user’s previous messages to adapt its responses, but it does not retain this memory across new chats (Strachan et al., 2024). As a result, GPT-4o rated each type of humor response 100 times, requiring a total of 400 new chat sessions.

Both human raters and GPT-4o demonstrated high reliability in rating funniness (Cronbach’s $\alpha>.77$), likability (Cronbach’s $\alpha>.82$), and effectiveness (Cronbach’s $\alpha>.81$) across the four humor types.

### 5.2. Results

We ran a 2 (rater: human vs. GPT-4o; between-participant) × 4 (humor type: affiliative, self-enhancing, aggressive, self-defeating) between-participant ANOVA on each of the three measures, respectively. The main effects of the rater group were all significant. That is, AI raters gave overall higher ratings than human raters, $F_s(1, 198)>219.79$, $p_s<.001$, $\eta_{ps}^2>.53$. The main effects of humor type were significant, $F_s(3, 196)>89.21$, $p_s<.001$, $\eta_{ps}^2>.31$, qualified by significant interaction effects, $F_s(3, 196)>3.56$, $p_s\leq .015$, $\eta_{ps}^2>.01$, except for likability, $F(3, 196)=2.25$, $p=.085$.

As seen in Fig. 3, human raters rated self-enhancing humor as the funniest ($M=4.91$, $se=.09$), most likable ($M=5.06$, $se=.09$), and most effective ($M=5.37$, $se=.08$), and aggressive humor as least funny ($M=3.17$, $se=.10$)/likable ($M=3.41$, $se=.10$)/effective ($M=3.56$, $se=.10$), with affiliative and self-defeating humor in between (which were not different from each other, $p_s\geq .83$). The pattern of AI ratings was similar to human ratings except for self-defeating humor: AI rated self-defeating humor as funny ($M=5.67$, $se=.08$)/likable ($M=5.84$, $se=.09$) as self-enhancing humor ($M_{\text{funny}}=5.77$, $se=.09$; $M_{\text{likable}}=5.96$, $se=.09$), $p_s\geq .311$, but not as effective as the latter ($M_{\text{self-enhancing}}=6.11$, $se=.08$; $M_{\text{self-defeating}}=5.77$, $se=.09$), $p=.006$.

Thus, Study 3 showed that both human participants and GPT-4o considered self-enhancing humor the best response to negative contexts, although GPT-4o also viewed self-defeating humor favorably (– which we will discuss more in the General Discussion). This may partially explain why GPT-4o produced overwhelmingly self-enhancing humor in response to an embarrassing context in Study 2.

## 6. Study 4

Building on Studies 1 and 2, which revealed differences in humor generation between GPT-4o and humans, Study 3 found that both humans and GPT-4o regarded self-enhancing humor as an optimal strategy for coping with negative contexts. Extending these findings, Study 4 examined whether human participants could benefit from GPT-4o’s assistance in generating humorous responses in negative social situations. Based on research in human–computer interaction suggesting

[Figure: Line chart with y-axis values 2–7 and x-axis categories Affiliative humor, Self-enhancing humor, Aggressive humor, Self-defeating humor. Legend labels: Human-funniness, Human-likability, Human-effectiveness, GPT-4o-funniness, GPT-4o-likability, GPT-4o-effectiveness.]

**Fig. 3.** Effects of rater and humor type on the overall humor score (Study 3). Error bars represent 95 % CI.



<!-- page 0006 -->

that AI-generated humor can enhance user engagement and trust (Niculescu et al., 2013), we hypothesized (H4) that humor senders assisted by GPT-4o would produce better humor compared to humans working without AI support, and that humor receivers would evaluate AI-assisted humorous responses more favorably than responses generated without AI support. This study was preregistered, see https://aspredicted.org/y237-33mv.pdf.

### 6.1. Method

*Participants.* 200 participants (69 men, 127 women, 4 other genders, $M_{age} = 40.28$ years, $SD_{age} = 11.84$, 140 White, 29 Black or African American, 16 Asian, 11 Hispanic or Latino, 1 Native American or Indigenous, 3 Other) were recruited in Part 1 to generate humorous responses to a given scenario. A separate sample of 350 participants (171 men, 176 women, 3 other genders, $M_{age} = 40.54$ years, $SD_{age} = 13.62$, 202 White, 105 Black or African American, 20 Asian, 18 Hispanic or Latino, 1 Native American or Indigenous, 4 Other) was recruited in Part 2 to evaluate the generated responses from the perspective of the recipient.

*Procedures.* In Part 1, we used a one-way (condition: AI vs. control) design. In Part 2, we used a 2 (rater type: human vs. GPT-4o; between-participants) × 3 (response type: GPT-4o-generated, GPT-4o-assisted, human-generated; within-participants) mixed design.

Part 1: 200 participants were asked to imagine themselves in a workplace scenario involving an interpersonal conflict (see supplementary material). The scenario described a tense argument with a colleague about workload distribution, and participants were encouraged to use humor to defuse the tension. Participants were then asked to write down the humorous responses they would deliver to the colleague. Subsequently, participants were randomly assigned to one of two conditions: the AI condition ($N = 107$) or the control condition ($N = 93$).

In the AI condition, participants were presented with one randomly selected response from a pool of 20 GPT-4o-generated humorous responses to the same workplace scenario. They were instructed to choose one of three options for their final response: (1) integrate their original response with the AI suggestion to create a modified version, (2) replace their original response with the AI-generated response, or (3) keep their original response without any modifications. In the control condition, participants were not shown any AI-generated response and submitted their original response as their final response without external assistance. After submitting their final response, all participants (i.e., humor senders) evaluated their submitted response in terms of funniness, likability, effectiveness, and relief (1 = *not at all*, 7 = *extremely*; see supplementary material).

Part 2: From the humor recipients’ perspective, 350 human participants were recruited to evaluate 60 randomly selected responses from Part 1, including 20 responses by human participants with AI assistance, 20 generated solely by human participants, and 20 generated by AI. Each response was evaluated by 50 humans and 50 GPT-4o-simulated evaluators. Human participants and GPT-4o were presented with the same conflict scenario as in Part 1 and assessed the responses from the recipient’s perspective, by evaluating funniness, likability, effectiveness, and relief (see supplementary material).

### 6.2. Results

Part 1: We conducted one-way ANOVAs to examine the effect of condition (AI vs. control) on participants’ (humor producers’) ratings of funniness, likability, effectiveness, and relief, respectively. The condition effect was significant for each of the dependent measures, $F$s $(1, 198) > 8.79$, $p$s ≤ .003, $\eta_p^2$s > .04. In particular, participants in the AI condition rated their humor response to be funnier ($M = 4.28$, $se = .14$), liked it more ($M = 4.83$, $se = .16$), rated it as more effective ($M = 4.75$, $se = .15$), and felt more relieved ($M = 4.67$, $se = .15$), compared to participants in the control condition ($M_{funniness} = 3.54$, $se = .15$; $M_{likability} = 4.02$, $se = .17$; $M_{effectiveness} = 4.01$, $se = .16$; $M_{relief} = 4.02$, $se = .16$).

Among participants in the AI condition, those who adopted the AI response ($n = 46$) reported the highest level of funniness ($M = 4.74$, $se = .22$), likability ($M = 5.50$, $se = .21$), effectiveness ($M = 5.13$, $se = .22$) and relief ($M = 5.22$, $se = .20$), whereas those who kept their original response (i.e., ignoring AI responses; $n = 28$) reported the lowest ratings on each of the four measures ($M_{funniness} = 3.64$, $se = .29$; $M_{likability} = 4.04$, $se = .27$; $M_{effectiveness} = 4.14$, $se = .28$; $M_{relief} = 3.46$, $se = .25$), with those who modified their response with AI suggestion ($n = 33$) sitting in between ($M_{funniness} = 4.18$, $se = .26$; $M_{likability} = 4.58$, $se = .24$; $M_{effectiveness} = 4.73$, $se = .26$; $M_{relief} = 4.94$, $se = .23$) (see Fig. 4).

Part 2: We then analyzed the ratings provided by the humor recipients and GPT-4o. We ran a 2 (rater type: human vs. GPT-4o; between-participants) × 3 (response type: AI, AI-assisted, human; within-participants) mixed-design ANOVA on ratings of funniness, likability, effectiveness, and relief, respectively. For each of these analyses the main effect of rater type was significant, $F$s $(1, 98) > 101.26$, $p$s < .001, $\eta_p^2$s > .35, indicating that in general, GPT-4o gave higher ratings than human recipients (see Fig. 5). The main effect of response type was always significant, $F$s $(2, 97) > 36.63$, $p$s < .001, $\eta_p^2$s > .39. No interaction effect was significant, $F$s $(2, 97) < 1.27$, $p$s ≥ .282, except for relief.[^6]

We then conducted post hoc analyses to examine the effect of the response type in detail. Overall, AI responses were rated as funniest, most likable, and most effective, resulting in the highest relief, and human responses were rated the lowest on all four measures, with AI-assisted responses in between, $p$s ≤ .032 for all pair-wise comparisons (Fig. 5).

The results supported our hypothesis by showing that AI and AI-assisted humor outperformed human humor, as evaluated by both humor senders and receivers. Furthermore, AI-assisted humor did not perform as well as purely AI-generated humor. These findings will be discussed in more detail in the General Discussion.

### 7. Discussion

In four studies investigating the role of ChatGPT (GPT-4o) in humor generation, we found that GPT-4o outperformed humans in sentence tasks, although it underperformed in image tasks (Study 1). In Study 2,

[Figure: Line chart with y-axis ranging from 2 to 7 and x-axis categories “Adopt AI response,” “Incorporate AI response,” and “Keep own response.” Legend shows Funniness, Likability, Effectiveness, and Relief with error bars.]

**Fig. 4.** Effects of group on the scores from four perspectives (Study 4). Error bars represent 95 % CI.

[^6]: The difference between human and AI raters was slightly smaller for human responses than for the other two types of responses (see supplementary materials for detailed results).



<!-- page 0007 -->

[Figure: Line chart with x-axis categories AI, AI-assisted, Human-generated and y-axis from 1 to 7. Legend labels: Human-funniness, Human-likability, Human-effectiveness, Human-relief, GPT-4o-funniness, GPT-4o-likability, GPT-4o-effectiveness, GPT-4o-relief.]

**Fig. 5.** Effects of rater type and response type on ratings scores (Study 4). Error bars represent 95 % CI.

GPT-4o produced funnier and more effective humor than humans in both positive and negative contexts, and this was especially true in negative contexts. Furthermore, both humans and GPT-4o identified self-enhancing humor as the most effective strategy for coping with negative contexts (Study 3) and GPT-4o predominantly used this type in its response to negative contexts (Study 2). Finally, Study 4 explored Human-AI interaction and revealed that humans could benefit from GPT-4o’s humor generation when navigating interpersonal conflicts. Together, these findings support our proposed hypotheses in large and provide novel insights into how AI can contribute to humor generation across contexts.

### 7.1. *Implications*

The present findings have important theoretical and practical implications. Firstly, although some previous studies have explored GPT’s performance across different humor tasks (Jentzsch & Kersting, 2023), with findings suggesting its superiority over humans in most aspects, these studies have mainly focused on text-based tasks, with limited attention to image-related tasks. This research fills that gap and reveals that humans still outperform GPT in image tasks, indicating that GPT has not fully surpassed humans in all areas. This may be due to at least two reasons: (1) GPT is predominantly based on a large language model and thus performs well on text-related tasks; (2) The image task requires an understanding of the pictures, which GPT-4o may not be well qualified. Thus, while GPT-4o excels in language processing and text or sentence generation, its performance in visual processing and creativity related to image-based humor still requires further development.

Secondly, when humor is used as a coping mechanism, we should not only focus on its intrinsic characteristic of being funny but also consider its broader significance (such as effectiveness), which has been less explored in existing research. Our research shows that in negative contexts, GPT-4o generates humor that is both funnier and more effective than human responses. These findings suggest that humans, particularly in negative contexts, do not always optimize their humor responses (whether in terms of funniness or effectiveness), despite previous research showing that individuals with an essentialist (or fixed) belief about humor tend to use humor in negative situations (Cao et al., 2024). Therefore, research on humor should consider both its entertainment value and its practical effectiveness, understanding its actual effects and potential value in different contexts. This finding also highlights the future potential for collaboration between AI and humans, especially in coping with negative contexts.

Thirdly, although previous research has distinguished between different types of humor (Martin et al., 2003), few studies have yet to delve deeply into the preferences for different types of humor and the reasons behind these preferences—specifically, whether individuals or AI base their humor choices on funniness or effectiveness. Our research sheds light on this matter. The present findings indicate that both humans and GPT-4o prefer adaptive humor (such as affiliative and self-enhancing humor) in positive contexts. When it comes to negative contexts, however, GPT-4o focuses solely on self-enhancing humor while humans use a broader variety of humor styles, despite that both humans and GPT-4o agree that self-enhancing humor is the most effective. This suggests that humans’ humor responses are likely not solely based on rational evaluation but rather reflect a complex adaptive strategy that integrates emotional and social factors, whereas AI’s humorous responses rely primarily on algorithm-based rational evaluation. Additionally, it is worth noting that GPT-4o rated self-defeating humor as equally funny or likable as self-enhancing humor, but less effective. Consequently, GPT-4o generated only self-enhancing humor in response to negative social situations (in Study 2), suggesting that effectiveness is an important consideration for GPT-4o. Meanwhile, we need to acknowledge that these findings may reflect a self-enhancement tendency typical of North American cultural contexts (e.g., Heine et al., 1999), as GPT-4o was primarily trained on North American (and English-language) datasets.

Although our study did not employ the Humor Styles Questionnaire (HSQ) developed by Martin et al. (2003), we adopted their four-style framework as a theoretical foundation. It is important to note that this typology was originally motivated by the goal of identifying the adaptive and maladaptive functions of humor in everyday life, particularly in relation to individual psychosocial well-being. However, this framework was not intended to offer a comprehensive measurement of all dimensions of humor (Martin et al., 2003, p. 51). Recent critiques (Cooper et al., 2025) have questioned its applicability in organizational contexts, especially noting that it tends to conflate humor expressions with inferred motives or outcomes. Future research may benefit from more fine-grained distinctions between types of humor and use such distinctions to compare human and AI-generated humor, ultimately contributing to a more comprehensive and precise understanding of the humor phenomenon. In addition, the humor type in the present research was limited to textual or image-based content and did not include audio or video modalities. As a result, key nonverbal cues—such as tone of voice, facial expressions, and gestures—were not captured, which may have constrained the richness of humor classification.

The present findings offer valuable insights into the dynamics of human-AI interactions, particularly in contexts that require humor for emotional support or stress relief. Study 4 reveals that the most effective strategy is not a collaborative integration of human and AI responses but rather the exclusive use of AI-generated humor. Remarkably, AI consistently outperforms humans in producing humorous responses tailored to such scenarios. There are several possible reasons why AI-assisted humor underperforms pure AI-generated humor. First, trade-offs in authenticity may play a key role. Humans tend to preserve personal expression and style when generating humor, which differs from the more “pure” and coherent humor produced solely by AI, thereby affecting the overall humor effectiveness. Second, cognitive load may limit participants’ ability to effectively integrate AI suggestions. Combining one’s own humor with AI-generated content may impose additional cognitive burdens, reducing the fluency and naturalness of the expression. Additionally, AI-generated humor is typically optimized by powerful language models, enabling rapid production of coherent and contextually appropriate responses, whereas human-AI collaboration may involve friction in coordinating style and content, further diminishing humor effectiveness.

Although AI’s potential in emotional support is significant, it also raises questions with important psychological and social implications. For some, the superior performance of AI in this domain may evoke feelings of threat or inadequacy, leading to resistance against relying on AI. Conversely, others might respond with a sense of defeat, resulting in over-reliance on AI as a primary source of support. Both reactions underscore the complex responses humans may have toward AI’s evolving



<!-- page 0008 -->

role and abilities.

### 7.2. *Limitations and future directions*

AI technology is advancing rapidly. The present research focuses primarily on the humor-generation capabilities of GPT-4o, one of the most advanced tools available at the time with relatively low usage costs. However, some findings—such as GPT-4o’s relatively weaker performance on image-related tasks—may not be generalizable to other AI systems or platforms. Additionally, with the advancement of technology, it will be important to explore whether the findings observed with GPT-4o generalize to newer generative AI models such as GPT-5. Given the rapid evolution of AI capabilities, examining user responses across different model generations may offer valuable insights into the stability and adaptability of human-AI interaction patterns.

The present research focused mainly on humor generation in negative contexts. Future research can explore the effectiveness of AI-generated humor in other emotional settings, such as fostering joy, strengthening positive interpersonal bonds, or diffusing tension in neutral or ambiguous situations. Exploring these areas could provide a more holistic understanding of AI’s capacity to generate and utilize humor across diverse emotional landscapes.

This research involved different age groups across studies, but we did not closely examine the effect of age. While this approach aimed to test robustness across populations, age-related differences in humor perception could influence findings. Future research should examine age effects more systematically.

Future research can further explore AI’s role in fostering emotional connections and enhancing communication in specific contexts. For example, in virtual assistant applications, AI can strengthen emotional bonds with users by generating humor that adapts to their emotional states, thereby improving communication effectiveness. Furthermore, in social media platforms, AI may help reduce social barriers and enhance understanding and trust among users by generating humor that resonates more broadly.

The effectiveness of AI tools, including their ability to generate humor, is shaped by the quality and diversity of their training datasets. Humor is deeply rooted in cultural norms, values, and linguistic nuances (Cao et al., 2021, 2025). Consequently, AI models trained on culturally specific data may produce humor that reflects the biases of their training culture, potentially limiting their ability to resonate with individuals from different cultural backgrounds. This raises an intriguing question: Can AI, or future iterations of AI, adapt its humor generation to suit diverse cultural contexts? Achieving this will require AI systems capable of recognizing and understanding the unique cultural elements that shape humor, such as language-specific wordplay, social norms, and shared cultural references. It will also demand extensive, inclusive training datasets covering a wide range of cultural perspectives.

Recent advances in computational methods have opened new avenues for humor research. For example, machine learning techniques have been applied to identify humor in archival and qualitative field data (Cooper & Schweitzer, 2024). Recent studies emphasize the potential of machine learning and multimodal data integration to capture the complex cognitive and social dimensions involved in humor generation and perception (Cowie, 2023), as well as the value of leveraging multiple modalities—such as text, audio, and video—to improve the automatic recognition of spontaneous humor (Christ et al., 2024). Emerging computerized tools thus enable more dynamic and context-sensitive assessments of humor as a personality trait, overcoming inherent limitations of traditional self-report methods. Future research should continue to develop and refine these computational techniques, with a focus on enhancing ecological validity and applicability across diverse contexts, especially through multimodal data integration that more comprehensively captures the richness of humor expression in naturalistic settings.

In conclusion, the present research demonstrates GPT-4o’s advantages in humor generation, particularly in negative contexts and conflict resolution. These findings enhance our understanding of AI-driven humor and its role in human-AI interaction.

### CRediT authorship contribution statement

**Yi Cao:** Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding acquisition, Formal analysis, Data curation, Conceptualization. **Jianhao Cao:** Writing – review & editing, Writing – original draft, Formal analysis, Data curation. **Yubo Hou:** Writing – original draft, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding acquisition, Conceptualization. **Li-Jun Ji:** Writing – review & editing, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Funding acquisition, Formal analysis, Conceptualization.

### Funding

This research received ethical approval from Peking University, and was supported by a grant from the National Natural Science Foundation of China (32271125) to Yubo Hou, and a grant from the China Postdoctoral Science Foundation (2024M760043) to Yi Cao, and a grant from the Social Science and Humanities Research Council of Canada (SSHRC 435-2018-0061) to Ji.

### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.chbr.2025.100807.

### Data availability

We have shared the link to our data.

### References

Aristotle. (2014). *Parts of animals* (W. Ogle, trans.). In *The complete works of aristotle, 1* pp. 994–1086). Princeton University Press. https://doi.org/10.2307/j.ctt5vj4w.27.

Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *Proceedings of the National Academy of Sciences, 120*(6), Article e2218523120. https://doi.org/10.1073/pnas.2218523120

Call, A. C., Flam, R. W., Lee, J. A., & Sharp, N. Y. (2024). Managers’ use of humor on public earnings conference calls. *Review of Accounting Studies, 29*, 2650–2687. https://doi.org/10.1007/s11142-023-09764-x

Cao, Y., Hou, Y., Dong, Z., & Ji, L.-J. (2021). The impact of culture and social distance on humor appreciation, sharing, and production. *Social Psychological and Personality Science, 14*(2), 207–217. https://doi.org/10.1177/19485506211065938

Cao, Y., Hou, Y., Wang, Y., & Ji, L.-J. (2025). Cultural tightness reduces humor production: Evidence from multiple countries. *American Psychologist* (in press).

Cao, Y., Liu, Y., Hou, Y., & Ji, L.-J. (2024). Essentializing humor and implications for pursuing happiness. *Journal of Happiness Studies, 25*(11). https://doi.org/10.1007/s10902-024-00717-y

Christ, L., Amiriparian, S., Kathan, A., Müller, N., König, A., & Schuller, B. W. (2024). Towards multimodal prediction of spontaneous humor: A novel dataset and first results. *IEEE Transactions on Affective Computing, 16*, 844–860. https://doi.org/10.1109/TAFFC.2024.3475736

Cooper, C. D., & Schweitzer, M. E. (2024). Organizational humor: A foundation for future scholarship, a review, and a call to action. *Annual Review of Organizational Psychology and Organizational Behavior, 12*, 215–237. https://doi.org/10.1146/annurev-orgpsych-110622-041448

Cooper, C. D., Sheridan, S. B., & Kong, D. T. (2025). Rethinking interpersonal humour in organizations: Clarifying constructs and charting a path forward. *Journal of Management Studies*. advance online publication. https://doi.org/10.1111/joms.13245



<!-- page 0009 -->

Cowie, R. (2023). Computational research and the case for taking humor seriously. *Humor-International Journal of Humor Research, 36*, 207–223. https://doi.org/10.1515/humor-2023-0021

de Kok, T. (2025). ChatGPT for textual analysis? How to use generative LLMs in accounting research. *Management Science*. https://doi.org/10.1287/mnsc.2023.03253. advance online publication.

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances, 10*(28), Article eadn5290. https://doi.org/10.1126/sciadv.adn5290

Dozois, D. J., Martin, R. A., & Bieling, P. J. (2009). Early maladaptive schemas and adaptive/maladaptive styles of humor. *Cognitive Therapy and Research, 33*(6), 585–596. https://doi.org/10.1007/s10608-008-9223-9

Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G* power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods, 39*(2), 175–191. https://doi.org/10.3758/BF03193146

Frewen, P. A., Brinker, J., Martin, R. A., & Dozois, D. J. (2008). Humor styles and personality-vulnerability to depression. *Humor-International Journal of Humor Research, 21*, 179–195. https://doi.org/10.1515/HUMOR.2008.009

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), Article e2305016120. https://doi.org/10.1073/pnas.2305016120

Heine, S. J., Lehman, D. R., Markus, H. R., & Kitayama, S. (1999). Is there a universal need for positive self-regard? *Psychological Review, 106*(4), 766–794. https://doi.org/10.1037//0033-295X.106.4.766

Hiranandani, N. A., & Yue, X. D. (2014). Humour styles, gelotophobia and self-esteem among Chinese and Indian university students. *Asian Journal of Social Psychology, 17*(4), 319–324. https://doi.org/10.1111/ajsp.12066

Jentzsch, S., & Kersting, K. (2023). ChatGPT is fun, but it is not funny! humor is still challenging large language models. *arXiv preprint arXiv:2306.04563*. https://doi.org/10.48550/arXiv.2306.04563

Jiang, T., Li, H., & Hou, Y. (2019). Cultural differences in humor perception, usage, and implications. *Frontiers in Psychology, 10*, 123. https://doi.org/10.3389/fpsyg.2019.00123

Jin, Y., & Sercu, L. (2025). ChatGPT interventions in higher education: A systematic review of experimental studies. *Journal of Computer Assisted Learning, 41*(4), Article e70072. https://doi.org/10.1111/jcal.70072

Kfrerer, M. L., Martin, N. G., & Schermer, J. A. (2019). A behavior genetic analysis of the relationship between humor styles and depression. *Humor-International Journal of Humor Research, 32*(3), 417–431. https://doi.org/10.1515/humor-2017-0098

Klein, D. N., & Kuiper, N. A. (2006). Humor styles, peer relationships, and bullying in middle childhood. *Humor-International Journal of Humor Research, 19*(4), 383–404. https://doi.org/10.1515/HUMOR.2006.019

Kosinski, M. (2024). Evaluating large language models in theory of mind tasks. *Proceedings of the National Academy of Sciences, 121*(45), Article e2405460121. https://doi.org/10.1073/pnas.2405460121

Kozbelt, A., & Nishioka, K. (2010). Humor comprehension, humor production, and insight: An exploratory study. *Humor-International Journal of Humor Research, 23*(3), 375–401. https://doi.org/10.1515/humr.2010.017

Lee, B. C., & Chung, J. (2024). An empirical investigation of the impact of ChatGPT on creativity. *Nature Human Behaviour, 8*(10), 1906–1914. https://doi.org/10.1038/s41562-024-01953-1

Li, M., Wang, Y., & Yang, X. (2025). Can generative AI chatbots promote second language acquisition? A meta-analysis. *Journal of Computer Assisted Learning, 41*(4), Article e70060. https://doi.org/10.1111/jcal.70060

Liu, Z., Zuo, H., & Lu, Y. (2025). The impact of ChatGPT on students’ academic achievement: A meta-analysis. *Journal of Computer Assisted Learning, 41*(4), Article e70096. https://doi.org/10.1111/jcal.70096

Mahowald, K., Ivanova, A. A., Blank, I. A., Kanwisher, N., Tenenbaum, J. B., & Fedorenko, E. (2024). Dissociating language and thought in large language models. *Trends in Cognitive Sciences, 28*(6), 517–540. https://doi.org/10.1016/j.tics.2024.01.011

Mao, R., Chen, G., Li, X., Ge, M., & Cambria, E. (2025). A comparative analysis of metaphorical cognition in ChatGPT and human minds. *Cognitive Computation, 17*(1), 35. https://doi.org/10.1007/s12559-024-10393-y

Martin, R. A., & Ford, T. (2018). *The psychology of humor: An integrative approach*. MA: Elsevier Academic Press.

Martin, R. A., & Lefcourt, H. M. (1983). Sense of humor as a moderator of the relation between stressors and moods. *Journal of Personality and Social Psychology, 45*(6), 1313–1324. https://doi.org/10.1037/0022-3514.45.6.1313

Martin, R. A., Puhlik-Doris, P., Larsen, G., Gray, J., & Weir, K. (2003). Individual differences in uses of humor and their relation to psychological well-being: Development of the Humor styles questionnaire. *Journal of Research in Personality, 37*(1), 48–75. https://doi.org/10.1016/S0092-6566(02)00534-2

McCullars, A., Richie, F. J., Kilbert, J. J., & Langhinrichsen-Rohling, J. (2021). What’s so funny? Adaptive versus maladaptive humor styles as mediators between early maladaptive schemas and resilience. *Humor-International Journal of Humor Research, 34*(1), 93–111. https://doi.org/10.1515/humor-2019-0082

McGraw, A. P., & Warren, C. (2010). Benign violations: Making immoral behavior funny. *Psychological Science, 21*(8), 1141–1149. https://doi.org/10.1177/0956797610376073

Niculescu, A., Van Dijk, B., Nijholt, A., Li, H., & See, S. L. (2013). Making social robots more attractive: The effects of voice pitch, humor and empathy. *International journal of social robotics, 5*, 171–191. https://doi.org/10.1007/s12369-012-0171-x

Nusbaum, E. C., Silvia, P. J., & Beaty, R. E. (2017). Ha ha? Assessing individual differences in humor production ability. *Psychology of Aesthetics, Creativity, and the Arts, 11*(2), 231–241. https://doi.org/10.1037/aca0000086

Oliveira, R., Arriaga, P., Axelsson, M., & Paiva, A. (2021). Humor–robot interaction: A scoping review of the literature and future directions. *International Journal of Social Robotics, 13*, 1369–1383. https://doi.org/10.1007/s12369-020-00727-9

Ruch, W., & Heintz, S. (2019). Humor production and creativity: Overview and recommendations. In S. R. Luria, J. Baer, & J. C. Kaufman (Eds.), *Creativity and humor* (pp. 1–42). Academic Press. https://doi.org/10.1016/B978-0-12-813802-1.00001-6

Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). Testing theory of mind in large language models and humans. *Nature Human Behaviour, 8*(7), 1285–1295. https://doi.org/10.1038/s41562-024-01882-z

Suri, G., Slater, L. R., Xiaee, A., & Nguyen, M. (2024). Do large language models show decision heuristics similar to humans? A case study using GPT-3.5. *Journal of Experimental Psychology: General, 153*(4), 1066–1075. https://doi.org/10.1037/xge0001547

Tang, Q., Deng, W., Huang, Y., Wang, S., & Zhang, H. (2025). Can generative artificial intelligence be a good teaching assistant?—An empirical analysis based on generative AI-assisted teaching. *Journal of Computer Assisted Learning, 41*(3), Article e70027. https://doi.org/10.1111/jcal.70027

Thorson, J. A., & Powell, F. C. (1993). Development and validation of a multidimensional sense of humor scale. *Journal of Clinical Psychology, 49*(1), 13–23. https://doi.org/10.1002/1097-4679(199301)49:13.0.CO;2-S

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124

Urban, M., Děchtěrenko, F., Lukavský, J., Hrabalová, V., Svacha, F., Brom, C., & Urban, K. (2024). ChatGPT improves creative problem-solving performance in university students: An experimental study. *Computers & Education, 215*, Article 105031. https://doi.org/10.1016/j.compedu.2024.105031

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-024-02024-1

Wang, X., Xu, X., Zhang, Y., Hao, S., & Jie, W. (2024). Exploring the impact of artificial intelligence application in personalized learning environments: Thematic analysis of undergraduates’ perceptions in China. *Humanities and Social Sciences Communications, 11*(1), 1644. https://doi.org/10.1057/s41599-024-04168-x

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*(9), 1526–1541. https://doi.org/10.1038/s41562-023-01659-w

Wei, X., Wang, L., Lee, L.-K., & Liu, R. (2025). The effects of generative AI on collaborative problem-solving and team creativity performance in digital story creation: An experimental study. *International Journal of Educational Technology in Higher Education, 22*(1), 23. https://doi.org/10.1186/s41239-025-00526-0

Yam, K. C., Barnes, C. M., Leavitt, K., Wei, W., Lau, J., & Uhlmann, E. L. (2019). Why so serious? A laboratory and field investigation of the link between morality and humor. *Journal of Personality and Social Psychology, 117*(4), 758–772. https://doi.org/10.1037/pspi0000171

Zöller, N., Berger, J., Lin, I., Fu, N., Komarneni, J., Barabucci, G., Laskowski, K., Shia, V., Harack, B., Chu, E. A., Trianni, V., Kurvers, R. H. J. M., & Herzog, S. M. (2025). Human–AI collectives most accurately diagnose clinical vignettes. *Proceedings of the National Academy of Sciences, 122*(24), Article e2426153122. https://doi.org/10.1073/pnas.2426153122

Yi Cao is a postdoctoral researcher in social psychology at Peking University, China. He studies culture, personality, and humor psychology. cyaoyi@pku.edu.cn

Jiahao Cao is a PhD student at Peking University, focusing on research in the fields of Human-AI Interaction. caojiahao66@stu.pku.edu.cn

Yubo Hou is a professor of social psychology at Peking University, China. He studies culture, social psychology, and Human-AI Interaction. houyubo@pku.edu.cn

Li-Jun Ji is a professor of social psychology at Queen’s University, Canada. She studies culture, cognition, and decision-making. lijunji@queensu.ca
