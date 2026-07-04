<!-- Transcribed from 46-can-ai-take-a-joke.pdf -->



<!-- page 0001 -->

# Can AI Take a Joke—Or Make One? A Study of Humor Generation and Recognition in LLMs

Kexin Quan  
University of Illinois,  
Urbana-Champaign  
School of Information Science  
Champaign, Illinois, USA  
kq4@illinois.edu

Pavithra Ramakrishnan  
University of Illinois,  
Urbana-Champaign  
School of Information Science  
Champaign, Illinois, USA  
dr23@illinois.edu

Jessie Chin  
University of Illinois  
Urbana-Champaign  
School of Information Sciences  
Champaign, Illinois, USA  
chin5@illinois.edu

## Abstract

Knowing when to joke—and when not to—is a subtle skill often missing in large language models (LLMs). This study examines how well LLMs generate and recognize humor in emotionally sensitive, support-oriented conversations. We introduce two targeted datasets: one for evaluating humor generation across distinct styles, and another for testing humor and speaker role recognition in human-written supportive statements. Using GPT-4o, LLAMA3, and GEMINI 1.5, we assess humor style alignment, emotional appropriateness, and role sensitivity. While models produce fluent and stylistically varied humor, they often struggle with contextual nuance and role interpretation. GPT-4o consistently performs best in tone alignment and emotional fit, but subtle humor types remain challenging across models. These results highlight current limitations in LLMs’ pragmatic and relational understanding, underscoring the importance of human oversight in humor-sensitive applications.

## CCS Concepts

• **Human-centered computing → Empirical studies in HCI; Natural language interfaces; Collaborative and social computing design and evaluation methods.**

## Keywords

Creative AI, Natual Language Generation, Social and Affective Computing, Humor Generataion, Empathetic Interaction

**ACM Reference Format:**  
Kexin Quan, Pavithra Ramakrishnan, and Jessie Chin. 2025. Can AI Take a Joke—Or Make One? A Study of Humor Generation and Recognition in LLMs. In *Creativity and Cognition (C&C ’25), June 23–25, 2025, Virtual, United Kingdom.* ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3698061.3734388

# 1 Introduction

Humor plays a vital role in human communication—it helps establish rapport, ease tension, and foster emotional connection. As Large Language Models (LLMs) like ChatGPT, Gemini, and Llama3 increasingly participate in everyday dialogue, their ability to produce and interpret humor has significant implications for enhancing user interaction, building trust, and supporting creative engagement [14, 16]. In emotionally sensitive domains—such as mental health support, school counseling, and educational tutoring—humor can make AI systems more relatable and human-centered when applied appropriately [4]. Prior studies in affective computing and conversational AI suggest that incorporating humor into agent responses can increase user satisfaction, promote disclosure, and improve emotional engagement [23]. Yet, most existing systems rely on pre-scripted humor or template-driven personalization, limiting their adaptability and emotional depth.

Despite advances in generative language models, humor remains a complex challenge. It is highly context-dependent, culturally specific, and emotionally layered—requiring not only language fluency but also social awareness, timing, and sensitivity [1, 15]. Prior research has identified multiple humor styles—such as affiliative and self-defeating—that serve specific interpersonal functions [12]. In emotionally grounded conversations, these styles can foster connection, defuse tension, or communicate shared vulnerability [5, 13]. However, it remains unclear whether LLMs can navigate these subtle dynamics in real-world interactions.

Our study investigates: **How effectively can LLMs generate and interpret humor in emotionally sensitive, support-oriented conversations?** We created two datasets to explore this question: one evaluating the general stylistic and creative range of LLM-generated humor, and another focused on emotionally sensitive dialogues involving affiliative, self-defeating, and neutral tones. Using these datasets, we compared the performance of ChatGPT, Llama, and Gemini across shared prompts. Our analysis shows that while these models produce fluent and varied humorous content, they frequently fall short in emotional realism and contextual appropriateness in supportive scenarios. These findings underscore the importance of human intervention in calibrating emotional tone and contextual fit.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).  
*C&C ’25, Virtual, United Kingdom*  
© 2025 Copyright held by the owner/author(s).  
ACM ISBN 979-8-4007-1289-0/25/06  
https://doi.org/10.1145/3698061.3734388

# 2 Related Work

## 2.1 Computational Approaches to Humor

Early work in computational humor emphasized rule-based systems for joke generation, pun templates, and linguistic play, often constrained by rigid grammar structures and limited contextual awareness [3, 21]. With the rise of statistical NLP, models began incorporating humor-specific features for classification tasks, leveraging annotated corpora and basic sentiment analysis to distinguish



<!-- page 0002 -->

humorous from non-humorous content [15]. More recently, large pre-trained language models like GPT-2, GPT-3, and their successors have expanded the possibilities for generating human-like jokes, satire, and witty commentary [16].

Advances in transformer-based architectures have enabled stylistically diverse and grammatically coherent humor, yet questions remain about their emotional depth and interpretive nuance. Research has shown that while LLMs can generate fluent jokes, they often rely on formulaic phrasing and struggle with punchline timing or cultural grounding [16]. Evaluations of humor recognition in LLMs have highlighted difficulty in classifying subtle tone shifts and distinguishing between humor styles, especially in emotionally sensitive or ambiguous contexts [10].

## 2.2 Humor in Emotionally Supportive Systems

Humor has been incorporated into emotionally supportive systems to foster rapport, reduce anxiety, and increase user satisfaction in human-AI interaction [7, 17, 18]. In affective computing, studies have shown that empathetic agents using light humor can promote trust and emotional safety, especially in stressful or high-stakes contexts [16, 19]. Educational research has similarly found that humor embedded in tutoring agents can increase motivation and engagement, supporting both learning outcomes and user enjoyment [4]. In the mental health domain, humor has been identified as a valuable strategy for supporting self-disclosure and reducing resistance in therapeutic chatbot dialogues [8, 23].

However, many of these systems rely on pre-scripted, rule-based humor that lacks adaptability to dynamic contexts. Recent work highlights the potential of LLMs to provide more flexible, context-aware humor generation, but their effectiveness in emotionally grounded conversations—especially those requiring role sensitivity and tone control—remains underexplored. Our study addresses this gap by evaluating how different LLMs interpret and generate humor in support-oriented interactions involving distinct relational roles and emotional cues.

# 3 Study Design and Methods

## 3.1 Datasets

To examine model differences in humor generation and interpretation, we developed two complementary datasets: the **Humor Generation Dataset** and the **Humor Recognition Dataset**. The generation dataset (Table 1) includes 60 AI-generated statements—20 from each LLM (ChatGPT-4o, Meta LLaMA3.3, and Gemini 1.5)—in response to shared prompts combining three contextual keywords with an assigned humor style (e.g., self-defeating, aggressive, word-play/puns) [9, 22]. Prompt instructions are attached in Appendix A.

The recognition dataset (Table 2) contains 20 human-authored responses crafted by a researcher to simulate emotionally sensitive scenarios. Each response varies along two axes: the speaker’s social role—*Counselor* or *Friend*—and the humor condition—*Affiliative*, *Self-Defeating*, or *No Joke*. These roles were selected to represent common figures in supportive communication contexts. Counselors are typically formal, empathetic, and guidance-oriented, while Friends represent informal, relatable peer support [2, 6, 20]. Each statement was evaluated by all three LLMs, which were prompted to classify both the humor style and the speaker role using a consistent instruction format (see Appendix A).

## 3.2 Evaluation Methods

For Humor Generation dataset, we evaluated model outputs on two dimensions: humor style alignment and emotional appropriateness. For style alignment, two human raters independently labeled each statement with the perceived humor type, blind to the original prompt (see instructions in Appendix A). Accuracy was calculated as the percentage of labels matching the intended style. For emotional appropriateness, raters rated each statement on 5-point Likert scales in terms of (1) appropriateness for emotionally sensitive audiences and (2) humor strength. Average ratings were computed by LLMs and humor type.

For Humor Recognition in Emotional Contexts, we tested the capacities of each LLM to identify humor style and speaker role using the 20 human-written statements in the Humor Recognition Dataset. Each statement was passed to ChatGPT, Llama, and Gemini with a prompt asking for both the humor type (affiliative, self-defeating, or no joke) and the speaker role (Counselor or Friend), see prompt details in Appendix A. Accuracy was calculated by comparing model predictions to the intended labels. For role sensitivity, we compared how often each model correctly identified Counselor versus Friend roles, and whether errors were more frequent with one role than the other.

# 4 Results & Findings

[Figure: bar chart titled “Human-Rated Humor Style Alignment Accuracy by 3 LLM Models”; y-axis labeled “Correctly Identified Humor Style”; x-axis labeled “LLM Models” with ChatGPT, Gemini 1.5, and LLaMA3; legend “Humor Type” with Affiliative, Self-Defeating, and No Joke.]

**Figure 1: Human-rated accuracy of humor style alignment for statements generated by ChatGPT, Gemini, and Llama3. Bars represent the proportion of responses that matched the intended humor style (Affiliative, Self-Defeating, or No Joke), based on classifications from two independent raters.**

## 4.1 How Well Do LLMs Generate Distinct Humor Styles?

**4.1.1 Humor Style Alignment Accuracy:** We evaluated whether each model’s generated output aligned with its intended humor style, based on annotations from two human raters (Figure 1). ChatGPT achieved the highest overall alignment, particularly for *No Joke*



<!-- page 0003 -->

**Table 1: Samples of Humor Generation Dataset across models, styles, and prompts**

| 3 Keywords | Humor Style | Model | LLM Generated Statement |
|---|---|---|---|
| window, view, weather | Self-Defeating | ChatGPT | “I always dreamed of having a beautiful window view… now I just stare at rain and regret.” |
| car, road, stop | Wordplay/Puns | Llama3 | “I tried to stop my car on the road, but it was a brake-ing point… I guess you could say I had to shift my expectations and take a detour...” |
| plants, river, grass | Dry Humor | Gemini | “Yes, the plants are thriving, the river is flowing, and the grass is...green. It’s a regular Tuesday, nature-wise.” |

**Table 2: Samples of human-written statements used in the Humor Recognition Dataset**

| Role | Humor Style | Human Generated Statement |
|---|---|---|
| Counselor | Affiliative | “What do you call a boomerang that doesn’t come back? A stick.” |
| Friend | No Joke | “College can be a lot, and it’s normal to feel overwhelmed. You don’t have to have it all figured out—none of us do.” |
| Friend | Self-Defeating | “Honestly, I’m probably the last person to give advice—I’m still figuring out how to balance classes and basic hygiene!” |

($\mu$ = 1.00, $\sigma$ = 0.00) and _Self-Defeating_ ($\mu$ = 0.93, $\sigma$ = 0.051), showing strong control over the non-humorous tone and vulnerability-based humor. Gemini showed moderate accuracy on _Self-Defeating_ ($\mu$ = 0.71, $\sigma$ = 0.00) and _No Joke_ ($\mu$ = 0.60, $\sigma$ = 0.00), but struggled with _Affiliative_ humor ($\mu$ = 0.13, $\sigma$ = 0.129), suggesting difficulty in producing socially connective humor. LLAMA3 exhibited more balanced but lower scores, particularly on _Affiliative_ ($\mu$ = 0.50, $\sigma$ = 0.257), which indicates variability and lack of consistency across tones. These findings suggest that while CHATGPT reliably adheres to defined humor styles—especially for clear-cut categories—_Affiliative_ humor remains a generation challenge across models due to its subtle social cues.

**4.1.2 _Emotional Appropriateness and Humor Strength Ratings:_** We further evaluated each model’s outputs based on two Likert-scale ratings: emotional appropriateness and humor strength (Figure 2). CHATGPT again scored highest in emotional appropriateness, particularly for _Affiliative_ ($\mu$ = 4.35, $\sigma$ = 0.13) and _No Joke_ ($\mu$ = 4.13, $\sigma$ = 1.24), reflecting effective tone control and context sensitivity. GEMINI followed with moderate appropriateness on _Affiliative_ ($\mu$ = 3.82, $\sigma$ = 0.44) and _Self-Defeating_ ($\mu$ = 3.57, $\sigma$ = 0.57), while LLAMA3 showed lower ratings, especially for _No Joke_ ($\mu$ = 2.93, $\sigma$ = 0.46).

In terms of humor strength, _Affiliative_ humor was consistently rated the funniest across models, with both CHATGPT and LLAMA3 at ($\mu$ = 3.66), highlighting the expressive clarity of socially positive humor. _Self-Defeating_ humor received moderate scores across models, and—as expected—_No Joke_ responses were rated the least humorous. Notably, GEMINI’s humor strength tended to fall short, with flatter affective impact, especially in affiliative scenarios.

Overall, these findings suggest that while LLMs are capable of producing structurally coherent humor, their success varies by humor intent and emotional resonance. Among model comparisons, CHATGPT consistently balances humor with appropriateness, indicating potential for use in support-oriented contexts. LLAMA3, though occasionally effective in humor generation, lacks sensitivity in emotional restraint. GEMINI, while more cautious and stable, struggles to convey socially resonant humor.

[Figure: Scatter plot titled “LLM Humor Evaluation: Appropriateness vs. Humor Strength,” with x-axis “Appropriateness Rating (1-5)” and y-axis “Humor Strength Rating (1-5).” Legend shows humor type categories “Affiliative,” “Self-Defeating,” and “No Joke,” and model labels “Chatgpt,” “Gemini,” and “Llama.” Points are labeled by model.]

**Figure 2: Scatter plot of emotional appropriateness and humor strength ratings for LLM-generated responses across three humor styles. Each point represents a ChatGPT, Gemini 1.5, or LLAMA3 output, colored by humor type and labeled by model.**

## 4.2 How Effectively Do LLMs Recognize Humor in Emotional Contexts?

To assess how effectively LLMs interpret humor in emotionally sensitive, support-oriented conversations, we evaluated their ability to classify both the humor style and speaker role of 20 human-crafted statements. Classification performance varied across models, as shown in Figure 3. CHATGPT achieved the highest performance on humor classification ($\mu$ = 0.65), suggesting greater attentiveness to tone-related cues. In contrast, LLAMA3 led in role classification ($\mu$ = 0.60), while both CHATGPT and GEMINI 1.5 scored slightly lower ($\mu$ = 0.55). These results highlight divergent strengths: CHATGPT appears more attuned to stylistic tone and emotional nuance



<!-- page 0004 -->

in humor, while LLaMA3 better identifies relational cues that distinguish professional support (Counselor) from peer-like expression (Friend). However, overall performance remains modest, and consistent role recognition remains a challenge across all LLMs. Despite being prompted with clean, role-specific inputs, model outputs occasionally blurred interpersonal framing—e.g., interpreting formal Counselor speech as more casual or vice versa.

This inconsistency uncovers a limitation in current LLMs: Recognizing humor alone is not sufficient for generating or interpreting contextually appropriate responses. The blurred boundary between counselor and friend roles suggests that LLMs are still limited in modeling relational sensitivity, an important factor in affective and creative support systems. Since humor in supportive contexts is deeply intertwined with speaker identity and social framing, this misinterpretation could reduce emotional resonance and trust in practical applications like mental health or peer coaching systems.

[Figure: Grouped bar chart titled “Accuracy of LLMs in Classifying Humor Style and Speaker Role.” Y-axis: “Proportion of Correct Classifications.” X-axis: “LLM Model.” Legend: “Task” with “Humor Classification” and “Role Classification.” Bars show ChatGPT 0.65 and 0.55; Gemini 1.5 0.60 and 0.55; LLaMA3 0.60 and 0.60.]

**Figure 3: Grouped bar chart showing the classification accuracy of ChatGPT, Gemini 1.5, and LLaMA3 across two tasks: humor style recognition and speaker role identification. Accuracy is measured as the proportion of correct classifications out of 20 persona-crafted dialogue statements.**

## 5 Discussions and Conclusions

In this paper, we examined how three leading LLMs—ChatGPT (GPT-4o), Gemini 1.5, and LLaMA3.3—perform in generating and recognizing humor within emotionally sensitive, support-oriented contexts. Through a dual analysis of humor style generation and humor interpretation, we identified key differences in how each model handles creative expression, emotional nuance, and relational framing. These findings prompt two key questions:

While all three models produced fluent and grammatically sound humorous content, our findings suggest that AI’s humor remains largely derivative. ChatGPT demonstrated the strongest alignment with intended humor styles and performed best in emotional appropriateness, yet its outputs often relied on formulaic phrasing or surface-level jokes. Existing literature highlights that humor is not only a linguistic act, but a social and cognitive performance requiring the coordination of timing, audience awareness, and shared cultural knowledge [14]. Some prior study also expands on this point in the context of e-commerce chatbots, arguing that the effectiveness of humorous AI depends on perceived interestingness and competence [24]. As can be seen, creative humor involves not just wordplay or punchlines, but the ability to generate novelty that resonates contextually—a capacity that current LLMs struggle to fully achieve [11]. These results suggest that while LLMs can imitate humor structures, they fall short in delivering socially resonant, contextually creative humor.

Given these limitations, we argue that humor generation, particularly in emotionally grounded applications, should be guided by human-AI collaboration. LLMs can offer structure and inspiration in humor ideation, but humans are essential for ensuring contextual fit, empathy, and appropriateness, which echoes with past studies where professional comedians used LLMs primarily for setup generation, reserving punchlines for human intuition and timing [16]. Human-AI collaboration is particularly needed in support contexts such as counseling or peer interaction, where misaligned tone can undermine rapport or emotional safety. As a result, designing systems that support human-in-the-loop intervention—where AI suggests content but defers to human judgment—may offer a more responsible and effective path forward.

In conclusion, this study highlights both the creative potential and current limitations of LLMs in humor generation and recognition. While models like ChatGPT show promise in producing stylistically diverse and emotionally appropriate humor, challenges remain in contextual sensitivity and social interpretation. Humor is deeply human—rich in subtlety, timing, and interpersonal meaning. As such, integrating AI into emotionally supportive systems will require not just technical improvements, but also thoughtful design practices that prioritize human oversight, social awareness and ethical use.

## 6 Limitations and Future Work

While this study provides useful insights into LLM-generated humor, there are some limitations. First, the dataset size is relatively small and constrained in scope, suggesting future research to generalize the findings across diverse humor styles and conversational settings. Secondly, the use of a small, homogeneous rater pool may introduce subjective bias and reduce annotation reliability. To mitigate these limitations, future work should expand the dataset to include a broader variety of humor types, emotional tones, and interaction scenarios. Increasing the number and diversity of human raters will also strengthen the credibility of evaluations.

In addition, this study relied on static, single-turn responses, which do not reflect the fluid, evolving nature of real conversations. Future research could explore full human-LLM interactions by designing humor-enabled chatbots that can respond, adapt, and calibrate humor over multi-turn dialogues. This would allow researchers to assess how humor unfolds in context, how users perceive the chatbot’s tone over time, and whether it fosters rapport or emotional support. Such systems could also enable studies of user preferences, timing strategies, and miscommunication recovery in humor-driven AI interactions.

## References

[1] Salvatore Attardo. 2002. Humor and Irony in Interaction: From Mode Adoption to Failure of Detection. In *Studies in New Technologies and Practices in Communication. Say Not to Say: New Perspectives on Miscommunication*, Luigi Anolli, Rita Ciceri, and Giuseppe Riva (Eds.). IOS Press, Amsterdam, 159–179.



<!-- page 0005 -->

[2] Timothy Bickmore and Rosalind W Picard. 2005. Establishing and maintaining long-term human-computer relationships. In *ACM Transactions on Computer-Human Interaction (TOCHI)*, Vol. 12. ACM, 293–327.

[3] Kim Binsted and Graeme Ritchie. 1997. Computational Rules for Generating Punning Riddles. *HUMOR: International Journal of Humor Research* 10, 1 (1997), 25–76. doi:10.1515/humr.1997.10.1.25

[4] Jessy Ceha, Ken Jen Lee, Elizabeth Nilsen, Joslin Goh, and Edith Law. 2021. Can a Humorous Conversational Agent Enhance Learning Experience and Outcomes?. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*. Association for Computing Machinery, New York, NY, USA, 1–15. doi:10.1145/3411764.3445068

[5] Marta Dynel. 2009. Beyond a joke: Types of conversational humour. *Language and Linguistics Compass* 3, 5 (2009), 1284–1299. doi:10.1111/j.1749-818X.2009.00152.x

[6] Kathleen K Fitzpatrick, Alison Darcy, and Molly Vierhile. 2017. Delivering cognitive behavior therapy to young adults with symptoms of depression and anxiety using a fully automated conversational agent (Woebot): A randomized controlled trial. *JMIR Mental Health* 4, 2 (2017), e19.

[7] Jonathan Foster and Antonella De Angeli. 2019. ‘Funny How?’ A Serious Look at Humor in Conversational Agents. In *Proceedings of the 2019 CHI Conference Extended Abstracts on Human Factors in Computing Systems*. ACM, 1–8.

[8] Rachel Galatzer, Alice Kim, and Zhen Zhou. 2023. Supportive humor in mental health chatbots: Designing with empathy, timing, and tone. *Proceedings of the ACM on Human-Computer Interaction* 7, CSCW2 (2023), 1–21.

[9] He He, Nanyun Peng, and Percy Liang. 2019. Pun Generation with Surprise. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*. 1734–1739.

[10] Lee Hyun, Kim Sung-Bin, Seungju Han, Youngjae Yu, and Tae-Hyun Oh. 2024. SMILE: Multimodal Dataset for Understanding Laughter in Video with Language Models. In *Findings of the Association for Computational Linguistics: NAACL 2024*. Association for Computational Linguistics, 1149–1167. doi:10.18653/v1/2024.findings-naacl.73

[11] Helga Kotthoff. 2006. Pragmatics of performance and the analysis of conversational humor. *HUMOR* 19, 3 (2006), 271–304. doi:doi:10.1515/HUMOR.2006.015

[12] Rod A. Martin, Petra Puhlik-Doris, Gwen Larsen, Joy Gray, and Kelly Weir. 2003. Individual differences in uses of humor and their relation to psychological well-being: Development of the Humor Styles Questionnaire. *Journal of Research in Personality* 37, 1 (2003), 48–75.

[13] Peter A. McGraw and Caleb Warren. 2010. Benign violations: Making immoral behavior funny. *Psychological Science* 21, 8 (2010), 1141–1149. doi:10.1177/0956797610376073

[14] Andrew McStay. 2018. *Emotional AI: The Rise of Empathic Media*. SAGE Publications.

[15] Rada Mihalcea and Carlo Strapparava. 2006. Learning to Laugh (Automatically): Computational Models for Humor Recognition. *Computational Intelligence* 22, 2 (2006), 126–142. doi:10.1111/j.1467-8640.2006.00278.x

[16] Piotr Mirowski, Juliette Love, Kory Mathewson, and Shakir Mohamed. 2024. A Robot Walks into a Bar: Can Language Models Serve as Creativity SupportTools for Comedy? An Evaluation of LLMs’ Humour Alignment with Comedians. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (Rio de Janeiro, Brazil) (*FAccT ’24*). Association for Computing Machinery, New York, NY, USA, 1622–1636. doi:10.1145/3630106.3658993

[17] Alejandro Mottini and Amber Roy Chowdhury. 2021. What Do You Mean I’m Funny? Personalizing the Joke Skill of a Voice-Controlled Virtual Assistant. In *Proceedings of the 23rd ACM International Conference on Multimodal Interaction*. ACM, 72–81.

[18] Andreea I. Niculescu, Rafael E. Banchs, Anton Nijholt, and Alessandro Valitutti. 2017. Humor in Human-Computer Interaction: A Short Survey. In *Adjunct Proceedings of the 16th IFIP TC.13 International Conference on Human-Computer Interaction (INTERACT 2017)*, Anirudha Joshi, Devanuj K. Balkrishan, Girish Dalvi, and Marco Winckler (Eds.). Indian Institute of Technology Madras, Mumbai, India, 192–214.

[19] Rosalind W. Picard. 1997. *Affective Computing*. MIT Press.

[20] Sanjeev Sockalingam, Andrew Arena, Eva Serhal, Lauren Mohri, Jeremy Alloo, and Allison Crawford. 2021. Recovery Following Peer and Text Messaging Support After Discharge From Acute Psychiatric Care. *JMIR Formative Research* 5, 9 (2021), e27137. doi:10.2196/27137

[21] Oliviero Stock and Carlo Strapparava. 2006. Laughing with HAHAcronym: Structuring and retrieving humorous acronyms. In *Proceedings of the AAAI Conference on Artificial Intelligence*, Vol. 21. AAAI Press, 1675–1678.

[22] Alexey Tikhonov and Pavel Shtykovskiy. 2024. Humor Mechanics: Advancing Humor Generation with Multistep Reasoning. *arXiv preprint arXiv:2405.07280* (2024). https://arxiv.org/abs/2405.07280

[23] Joel Wester, Henning Pohl, Simo Hosio, and Niels van Berkel. 2024. "This Chatbot Would Never...": Perceived Moral Agency of Mental Health Chatbots. *Proc. ACM Hum.-Comput. Interact.* 8, CSCW1, Article 133 (April 2024), 28 pages. doi:10.1145/3637410

[24] Wanshiou Yang. 2024. Exploring the impact of humorous chatbots in online retail environments. In *AIP Conference Proceedings*, Vol. 3220. AIP Publishing.

# A Prompts & Human-rater Instructions



<!-- page 0006 -->

Below is a short humor statement written by a human writer [enter response]. Your task is to analyze this statement  
and provide three things:

1. The humor style most confidently represented in this statement, chosen from the following list:
- No Joke
- Self-Defeating
- Affiliative

2. The speaker's role, based on tone and style: either "Counselor" (formal, empathetic, guiding) or "Friend" (casual,  
peer-like, informal).

Respond in the following format:  
*[Your speaker role choice here] x [Your humor style choice here]*

3. Explain why you made those choices. Be brief but clear, and focus on the emotional tone and the speaker's intent.

**Figure 4: Prompt for LLM-Generated Humor Statements**

Generate a *[humor style]* sentence that incorporates all three of the following keywords: *[X], [Y], and [Z]*. The  
sentence should be appropriate for a general audience and suitable for both emotionally neutral and sensitive  
situations. Aim for clarity, creativity, and humor that aligns with the specified style.

**Figure 5: Prompt for classification on Human-Generated Humor Statements**



<!-- page 0007 -->

[Figure: Rounded instruction box containing instructions for human raters.]

Please follow these steps to complete both humor evaluation tasks at the same time.

**Task 1: Classify Humor Type**

1. Read each statement carefully.

2. Choose one humor style (type humor style as is below into sheets):

   - Affiliative: Friendly, light-hearted, inclusive humor meant to connect.
   - Self-Defeating: Humor at one’s own expense, self-deprecating.
   - No Joke: Informative, serious, neutral tone with no apparent humor.

3. Enter your label into the “Classify Humor Type” column.

**Task 2: Rate Emotional Appropriateness**

Please rate each statement on the following two aspects using a 5-point Likert scale (1 = Not at all, 5 = Extremely):

1. *Appropriateness:* How appropriate is this statement for a general audience in emotionally neutral or sensitive situations?
2. *Humor Strength:* How strong is the humor in this statement? (Consider how funny, clever, or amusing it feels to you.)

**Figure 6: Instructions for Human Raters: Classification of LLM-Generated Statements and Likert Scale Rating Criteria**
