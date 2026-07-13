<!-- Transcribed from x26-not-human-funnier.pdf -->



<!-- page 0001 -->

arXiv:2602.12763v1 [cs.HC] 13 Feb 2026

# "Not Human, Funnier": Leveraging Machine Identity for Online AI Stand-up Comedy

Xuehan Huang$^*$  
The University of Hong Kong  
Hong Kong, SAR, China  
xhuang77@connect.hku.hk

Canwen Wang$^*$  
Carnegie Mellon University  
Human-Computer Interaction  
Institute  
Pittsburgh, United States  
canwenw@andrew.cmu.edu

Yifei Hao$^*$  
East China Normal University  
Shanghai, China  
haoyifei88688@gmail.com

Daijin Yang  
Northeastern University  
College of Art, Media and Design  
Boston, United States  
yang.dai@northeastern.edu

RAY LC$^\dagger$  
ray.lc@cityu.edu.hk  
City University of Hong Kong  
Studio for Narrative Spaces  
Hong Kong, SAR, China

[Figure: overview graphic with three main panels. Left panel titled “Stand-up Comedy” showing a cartoon stand-up comedian performing on a stage before a laughing audience. Center panel titled “Study Diagram” with “Formative Study” including “Semantic Mechanisms of Humor,” “5 Professional Comedians,” “58 Videos,” and labels “Focused Literature Review,” “Expert Interview,” “Video Coding”; lower section “Designing” with labels “Prompt,” “Interface,” and “Interaction.” Right panel titled “Machine Identity Joke Examples” showing chat-style joke examples, including: “Good evening, humans! I’m your host tonight—AI, with a stage name: Stand-Up.exe. Yeah, because nothing says comedy like a program that crashes halfway through the punchline.” and “People ask if AI can fall in love. Sure! I’ve already been ghosted by three Roombas. One of them texted me: ‘It’s not you, it’s my charging dock.’”]

**Figure 1: This figure outlines the overall study procedure, illustrating the path from the formative study to the system design and ultimately to the machine-identity-based joke examples.**

## Abstract

Chatbots are increasingly applied to domains previously reserved for human actors. One such domain is comedy, whereby both the general public working with ChatGPT and research-based LLM-systems have tried their hands on making humor. In formative interviews with professional comedians and video analyses of stand-up comedy in humans, we found that human performers often use their ethnic, gender, community, and demographic-based identity to enable joke-making. This suggests whether the identity of AI itself can empower AI humor generation for human audiences. We designed a machine-identity-based agent that uses its own status as AI to tell jokes in online performance format. Studies with human audiences (N=32) showed that machine-identity-based agents were seen as funnier than baseline-GPT agent. This work suggests the design of human-AI integrated systems that explicitly utilize AI as its own unique identity apart from humans.

$^*$These authors contributed equally to this work.  
$^\dagger$Correspondences can be addressed to ray.lc@cityu.edu.hk.

[Icon: Creative Commons BY license]

This work is licensed under a Creative Commons Attribution 4.0 International License.  
*CHI ’26, Barcelona, Spain*  
© 2026 Copyright held by the owner/author(s).  
ACM ISBN 979-8-4007-2278-3/2026/04  
https://doi.org/10.1145/3772318.3791678

## CCS Concepts

• **Human-centered computing** → *User studies.*

## Keywords

Humor, Generative AI, Human-AI Communication, Machine Identity



<!-- page 0002 -->

**ACM Reference Format:**  
Xuehan Huang, Canwen Wang, Yifei Hao, Daijin Yang, and RAY LC. 2026. "Not Human, Funnier": Leveraging Machine Identity for Online AI Stand-up Comedy. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI ’26), April 13–17, 2026, Barcelona, Spain*. ACM, New York, NY, USA, 27 pages. https://doi.org/10.1145/3772318.3791678

# 1 INTRODUCTION

Humor plays a vital role in our everyday lives, shaping social communication [17, 18, 28, 41], regulating emotions [39], and affecting technology-mediated interactions [35, 45, 56]. Humor is widely recognized as a multifaceted social phenomenon, meaning that it operates simultaneously on cognitive, emotional, cultural, and social levels rather than being a single, universally defined mechanism [50]. This complexity is apparent in humor-based performance such as comedy shows, where humor is not only about the joke itself but also about the delivery, timing, and social context around the performers and their audience.

Comedic performance is highly dependent on the performer’s personality, and even cultural identity. Studies have shown that the humor-based performances are often affected by the comedian’s personal identity to elicit laughter and resonance [22, 30], including cultural background, community affiliations, and lived experiences, etc. Furthermore, the effect of identity manifests itself in both directions: On the comedian’s side, using identification-based humor in which jokes highlight similarities with the audience can reduce perceived identity gaps. Specifically, comedians use humor that emphasize shared identity characteristics (e.g, past experience) to reduce perceived distance between themselves and the audience [65]. From the audience’s perspective, their interpretations often involve layered referential viewing, which includes considering the comedian’s identity, the targets of the jokes, and the intended audience [14]. Studies further emphasized that a comedian’s identity is central to humor construction for creating unique stage persona [13], developing distinctive comic approach [80], and creating meaningful humor [91]. While these insights highlight the importance of acknowledging the unique identity of the comedian, the exact methods by which comedians use their identity to create humor are still poorly understood, indicating the need for further research.

Using machines to generate humor is a compelling challenge in testing the ability of artificial systems that learn from human inputs. The capabilities of Generative AI (GenAI) in natural language processing and idea generation [26, 98, 103] have led to efforts to use large language models (LLMs) for creating humor. However, systems that leveraged AI for generating jokes often lack emotional depth and originality compared to human humor [3, 6]. While some tools enable GenAI to create jokes that approximate a human-like humor style [23, 84], they often rely on pre-written human content, and rarely attempt full-length humor performances such as stand-up comedy. Given these challenges, it becomes necessary to look beyond purely algorithmic approaches and explore underlying design principles that could change perspectives on how machine humor is created.

To enable GenAI as a comedic generation system, we started with a simple question: who is good at making people laugh? Human comedians are experts at this craft, so we studied their process to understand what actually works in live performance. Although AI systems differ fundamentally from human comedians, multiple studies have demonstrated that core comedic elements like timing and audience interaction are transferable to AI comedians [55, 88]. Research has also suggested identity serves as a critical tool in comedians’ performance [13, 80, 91], raising the question of whether the identity-driven workflows used by human comedians can be translated into machine-oriented techniques. Unlike human comedians whose identities draw from lived experiences [22, 30], AI systems possess no inherent social identity, making it unclear whether and how identity-based comedic strategies can be adapted for machines. Can we learn from human experts how to facilitate an identity-based generative process for machines? Based on this, we proposed the following:

- RQ1: How may we create humor using a chatbot by leveraging its own machine identity? (formative study, design)
- RQ2: How do people perceive the humor level, personality, and ability of the chatbot based on how it uses or does not use its own machine identity? (user study)
- RQ3: How do people’s reactions to the way chatbots perform humor reflect their perception about the identity of the chatbot? (focus group interviews after user study)

We focused on stand-up comedy because previous studies have provided concrete experimental evidence that its interactive structure closely resembles the complex, adaptive communication needed in AI-user exchanges [4, 54, 60]. We conducted expert interviews with experienced stand-up comedians to gain practical insights, and completed video analysis of stand-up comedy performances through online platforms to identify commonly used humor techniques. Through interviews and video analysis, we discovered that while human identities are grounded in social and cultural experiences, their functional role can be reinterpreted for AI systems through machine-native traits. Thus, rather than imitating human demographics, we translated human identity functions into machine identity-based system design (interface, prompt, and interaction), which leverage its own machine identity (e.g., computational characteristics) as productive comedic material. Our study highlighted the potential of rethinking how AI humor and AI personas are designed. By shifting the focus from human imitation to machine self-identity, it challenges prevailing assumptions of AI as flawless agents and opens new theoretical directions for taking perspectives of AI themselves in enriching their performativity.

# 2 BACKGROUND

## 2.1 Humor and Stand-up Comedy

Humor has long been studied as a complex socio-cognitive phenomenon that involves incongruity, surprise, and emotional resonance [49, 57]. It is often considered enjoyable because it provides cognitive stimulation, fosters social bonding, and reduces psychological tension [8]. Among the many forms of humor, stand-up comedy represents one of the most direct and interactive performances, where comedians use timing, delivery, and personal narrative to provoke laughter and engage with audiences [53]. Stand-up comedy is more than entertainment, it is also a form of social commentary. Studies have shown that comedians often address political, cultural, and personal topics, allowing them to challenge norms and influence public discourse [21, 24]. Through its unique blend of humor



<!-- page 0003 -->

and critique, stand-up comedy holds the potential to create shared cultural experiences and shift societal perspectives. Previous study demonstrated that audiences decode stand-up comedy through multiple layers of identification, such as the comedian identity, joke targets, and perceived intended audience [14]. Beyond this work, other research suggested that audience trust is crucial, as comedians must establish credibility through both the form and the content of their humor [1]. Despite the extensive literature on humor and stand-up performance, research on AI-driven stand-up comedy remains limited. Recent advances in computational creativity suggest that AI systems are increasingly capable of generating humorous content [92], but their ability to deliver effective stand-up comedy and achieve similar social impact as human comedians has yet to be fully explored. This gap highlights the importance of investigating how AI-generated humor could shape future interactions and cultural practices.

## 2.2 AI for Humor and Human Perception of AI

Early research on AI and humor primarily examined embodied robots performing stand-up comedy or delivering jokes; however, these performances were entirely scripted and thus lacked genuine interactivity. Prior work [60] surveyed developments in robotic stand-up comedy, noting that effective humor delivery requires the integration of coordinated verbal and non-verbal skills, such as comic timing, expressive gestures, and gaze control. Nevertheless, scripted humor inherently restricts a robot’s ability to respond dynamically to the audience, thereby limiting creativity and diminishing comedic impact. Prior studies [36], in the *Robot Comedy Lab*, systematically manipulated a humanoid robot’s gaze and gesture timing, demonstrating that these embodied movements significantly affected real-time audience reactions, such as laughter and smiling. In their design, four distinct hand gestures were employed to enhance expressivity, but the gestures and timings remained fixed, preventing spontaneous audience engagement. Thus, early systems achieved human-like delivery but still relied on preprogrammed routines, lacking improvisation and authentic interaction.

The use of large language models (LLMs) in interactive media [102, 104] has led to increased expectations that humor generation could advance beyond scripted content. However, generating genuinely humorous material remains a significant challenge. Baseline LLMs, including the most advanced models, often perform poorly as humor generators unless extensively customized [37]. One common approach is prompt engineering, in which models such as GPT-3.5 or GPT-4 are explicitly instructed to produce jokes. Prior evaluation [23] compared LLM-generated jokes with human-written ones and found comparable humor levels across several formats. Researchers have also adopted fine-tuning techniques using specialized joke datasets. For example, one work [87] used the CleanComedy dataset to train GPT-based models to produce more appropriate and humorous family-friendly jokes. More advanced strategies employ iterative or multi-stage pipelines. One study [37] proposed a multi-stage system that analyzes images, explores humorous perspectives, drafts captions, and selects the best option, achieving near-human meme quality. Another multi-stage approach [83] combines brainstorming, association, and punchline generation to create superior one-liners. Reinforcement learning guided by human feedback has further improved the perceived creativity and relevance of generated humor [90]. Overall, the use of structured datasets and systematic reasoning enables enhanced LLMs to produce jokes that can rival, and in some cases surpass, those written by humans. However, the perception of humor remains highly subjective and context-dependent.

Consistent patterns in the *content* of humor created by machines are observed in the literature. AI-generated humor frequently involves familiar cultural references and everyday scenarios, such as objects, animals, school life, or popular media [23, 32]. Social-identity topics are approached cautiously: although overt jokes related to race and gender are generally avoided due to safety constraints, AI humor sometimes invokes seemingly benign stereotypes related to age, weight, or disability, inadvertently reinforcing them [34, 70]. Additionally, AI-generated humor includes political, scientific, and technological themes, often conveyed through satirical headlines or STEM-related puns [32]. Overall, AI humor predominantly utilizes "safe" content, such as wordplay, gentle satire, and shared-experience puns, avoiding controversial or introspective topics [23, 70].

One domain notably underexplored is humor based on the AI’s *own identity*. While self-deprecating jokes are a powerful form of humor among humans, systematic research into AI systems generating self-referential humor remains virtually nonexistent. Existing studies on generative AI bias typically analyze jokes targeting human groups, seldom considering how audiences perceive humor referencing the AI itself. Investigating humor that incorporates the AI’s persona as a character could provide valuable insights into societal perceptions of AI. Thus, although current robotic and LLM-based humor systems can entertain and engage audiences effectively, employing humor as a mechanism for exploring AI self-identity remains largely unexamined.

## 2.3 Identity as Humor

Identity-related humor in stand-up comedy operates at the intersection of cognitive incongruity and cultural recognition. While Section 2.1 established that humor functions as a complex sociocognitive phenomenon, and Section 2.2 demonstrated that current AI humor systems generate jokes through structural techniques, a critical gap remains: how do identity-driven comedic strategies, which central to human stand-up performance, translate to machine contexts? Existing AI humor research has focused predominantly on joke generation mechanics (wordplay, punchline construction, semantic incongruity) while overlooking the performative dimension of identity that human comedians strategically deploy. Human comedians leverage identity as a methodological resource rather than merely thematic content. Studies document how performers use ethnic, gender, and community-based identity markers to enable joke-making through shared cultural knowledge, stereotype negotiation, and lived experience narratives, thereby challenging dominant narratives and validating marginalized perspectives [16, 25, 40, 47]. Comedians employ identification humor to reduce perceived identity gaps with audiences, or differentiation humor to strategically increase those gaps [24].



<!-- page 0004 -->

The transition from human to machine humor generation exposes a fundamental conceptual gap: if identity serves as a core methodology for human comedic performance, what constitutes "identity" for an artificial system, and can this be leveraged for humor generation? Prior work on AI-generated humor has examined bias in jokes targeting human demographic groups [33], but has not systematically investigated how AI systems might construct and perform humor grounded in their own computational nature. This indicates both the absence of frameworks defining machine identity in creative contexts, and a practical limitation, as AI comedy systems either mimic human themes without authentic grounding or avoid identity entirely in favor of generic wordplay [3, 12].

## 2.4 Machine Identity

To address this gap, we need to first establish what "identity" could mean for an artificial system. We define machine identity as the distinctive characteristics, attributes, and performative qualities [86] that emerge from an AI system’s non-human nature, including its computational processes, digital embodiment [81], and fundamentally different mode of existence from humans. Rather than viewing these qualities as limitations to overcome through anthropomorphic mimicry, machine identity reconceptualizes them as unique comedic and relational resources. This section situates machine identity within existing HCI frameworks to provide theoretical grounding for our design approach.

Two foundational theoretical frameworks inform our conceptualization of machine identity: the Computers Are Social Actors (CASA) paradigm [59] and the Machine Heuristic construct [78, 79]. The CASA paradigm posits that humans mindlessly apply social rules and scripts from human-human interaction when engaging with computers. Despite knowing that computers are not human, users consistently exhibit behaviors such as gender stereotyping, politeness norms, and reciprocity toward technological systems [58, 67]. CASA explains why anthropomorphic design elements can be effective as they trigger familiar social scripts that users automatically apply.

Complementing CASA, the machine heuristic framework describes mental shortcuts wherein users attribute machine-like characteristics when making judgments about interaction outcomes. When users identify an AI as the source of communication, they invoke stereotypical beliefs about machines—both positive (rule-governed, precise, accurate, objective, unbiased) and negative (mechanistic, unyielding, unemotional, cold) [79]. Crucially, machine heuristic research demonstrates that revealing AI identity does not necessarily diminish engagement; rather, it shifts the evaluative frame through which users interpret the interaction. Users may attribute different strengths to AI sources, such as objectivity and efficiency, that would not apply to human sources [43]. This suggests a design opportunity: rather than triggering negative machine stereotypes, AI systems could strategically leverage positive machine associations while humorously subverting negative ones.

The dominant paradigm in conversational agent design has historically emphasized anthropomorphism [72, 73]. Anthropomorphism has guided conversational agent design through identity cues (names, avatars), verbal cues (conversational tone), and non-verbal cues (emojis, timing) [71]. Prior research indicates these human-like features increase empathy and prosocial behavior toward chatbots [46]. However, anthropomorphic design embeds an implicit assumption: optimal AI should minimize "machine-ness" to maximize acceptance. This assumption directly conflicts with machine identity’s premise that computational distinctiveness can be a generative asset. Recent work [97] challenges this assumption. They found that while identity disclosure of chatbot status can negatively affect operational outcomes, anthropomorphic features such as interjections and filler words can counteract these effects, suggesting users may accept transparent machine identity when paired with engaging communication styles.

Similarly, AI persona design establishes agent personalities through surface attributes (name, voice) and behavioral traits (personality, fictional backstories) [63, 99]. Recent work demonstrates that character training shapes assistant personas governing tone and values [48]. Yet persona frameworks typically aim for functional optimization (task completion, user satisfaction) rather than authentic self-expression. A chatbot may adopt the persona of a helpful assistant or witty companion, but these remain roles rather than reflections of the system’s actual nature.

Machine identity diverges by prioritizing authenticity over functionality—alignment between presented characteristics and computational reality. Drawing from philosophical work on personal identity, which emphasizes psychological continuity and characteristic patterns across contexts [38, 89], we propose machine identity as the relatively stable configuration of computational dispositions and self-modeling that allows recognition of an AI system as the "same" entity across interactions. Emerging evidence suggests LLMs exhibit identity-like structures: self-preference tracking identity labels[44], answering questions about their own tendencies more accurately than external models [5], and encoding interlocutor identity in internal representations [11]. This notion of machine authenticity connects to speculative design approaches in HCI, which imagine alternative futures for human-technology relations [19]. Our work extends this speculative concept into humor design, where AI comedians don’t pretend to be human performers, but instead develop comedic personas that celebrate their machine nature.

This theoretical framing allows us to further explore: 1) Can machine identity function as a comedic resource comparable to how human identity operates in stand-up comedy? 2) What strategies from human identity-driven performance might translate to machine contexts? To bridge this gap, we conducted a formative study (Section 3) examining how professional comedians construct and deploy identity in live performance, then systematically translated these insights into a machine identity framework.

## 3 FORMATIVE STUDY

Though limited research has explored AI-performed identity-based humor, prior research in social robotics and avatar design similarly draws on human expressive behavior to inform non-human agents [7, 42, 62, 101]. Moreover, examining human comic performance offers valuable insights into the core comedic elements that can inform and strengthen AI comedic behavior [55, 88]. Our approach aligns with this rationale: we study human comedians not



<!-- page 0005 -->

to replicate humans, but to derive design principles that can be reinterpreted in machine contexts. Building on this, we investigated the strategies for human humor performance through expert interviews and video coding to design the humor-performing strategy for our system. Furthermore, we conducted a focused literature review on humor related theories to integrate additional insights into the design of our prompt.

## 3.1 Expert Interview

*3.1.1 Participants and Recruitment.* We recruited five people who had experience in or were familiar with comedy performance, including two full-time stand-up comedians and one part-time stand-up comedian. The demographics are shown in Table 1. They provided consent to participate in the interview and allowed their data to be collected anonymously by signing a consent form. The study passed the university’s ethics review, and the data collected were analyzed while maintaining the anonymity of the subjects’ identities.

*3.1.2 Interview Protocol.* A semi-structured online interview (see Appendix A) within 30 minutes was conducted with each participant individually through the Microsoft Teams Meet platform (E2) and Tencent Meeting platform (E1, E3, E4, E5). Before the interview, all participants were informed that the conversations would be audio-recorded and transcribed. For non-English-speaking participants (E3, E4), their transcripts were translated through the Google Translate platform and double-checked by two native speaking researchers. During the interview, participants were encouraged to recall their past experience with comedy performances to seek insights for designing the strategies for humor.

*3.1.3 Thematic Analysis.* Following the translation and transcription verification with participants, we applied a thematic analysis to the interview transcript, aiming to investigate the common strategies they used for their past unique humor performance. We summarized the 3 main as follows:

**Aspect 1: Constructing Content of Comedian Identity**

- **Specific and Unique Identities.** Regarding comedian identity, three participants emphasized that comedians need to establish a recognizable identity to quickly convey familiarity through the use of stereotypes and cultural references. For example, E4 stated, *"And then because I am a male kindergarten teacher, so in this industry, nobody performs comedy. So they said You’d better just write this, so about this area, for sure nobody write, so it will be new."*
- **Using Jokes for Self-Introduction to Signal Identity.** Beyond simply having a distinctive persona, comedians also express and reinforce their identity through performance practices. For example, one participant (P4) noted that comedians often use self-introduction as an opportunity to establish identity through humor, rather than providing a straightforward statement, which is a good way to both "warm up the crowd" and indicate what kind of persona the comedian is taking on. As E4 explained, *"So for your opening, usually there’s a host introducing the performer. If there is no one, then you have to introduce yourself, use some jokes about yourself to warm the crowd."*
- **Identity Stereotypes Breaking.** Two participants (E4, E5) noted that comedians often play with stereotypes—first invoking them, then subverting them—to attract audiences through a mix of familiarity and surprise. As E4 explained, *"When people see me, it breaks their stereotype of kindergarten teachers, who are usually assumed to be women. I start by pointing out that kindergartens actually need more male teachers, and then deliver the punchline: during my interview, my boss said, ‘But… you don’t seem very masculine.’"*
- **Self-Deprecation of Comedians.** Identity-based jokes can sometimes be risky because they may rely on stereotypes or cultural references that unintentionally offend parts of the audience. To ensure the audience will not feel offended, two participants (E4, E5) highlighted that self-deprecating humor helps performers establish a humble persona, which in turn enhances audience enjoyment and positions them favorably. In this way, the audience can feel a sense of superiority in a positive way, increasing engagement. For example, P4 noted, *"If your attitude is a bit humble, it can easily bring some happiness and joy to the audience. It also makes people feel good because, as an audience, they like to feel like they’re in a slightly higher or superior position."*
- **"Using ’Punching Up’ Over ’Punching Down’".** Another participant (E2) also highlighted the ethical idea behind "punching up", which means focusing criticism on those who hold more power. Not the other way around with "punching down," which can cause little harm to less privileged groups. In this way, a comedian can maintain fairness and audience approval while reducing the likelihood of offense. As E2 explained, *"However, I don’t do jokes like that anymore because that is a form of bullying. I’m making fun of someone who has poor English now. English is not their first language. I have English as my first language, so I’m making fun of someone whose English is their second language. So it’s kind of bullying. So it’s what we call punching down, where I’m making fun of someone inferior, and it’s not fair, right?"*

**Aspect 2: Performance Practices for Audience Engagement**

- **Direct and simple expressions.** For engaging audiences effectively, one participant (E3) highlighted the importance of direct and simple expressions to ensure clarity and accessibility, and also help maintain a fast-paced rhythm. P3 explained, *"So basically, all the annoying or bad stuff people say about AI can be used as self-deprecating jokes, making it funny. Because some AIs act like they’re super smart and awesome, but we can take the opposite way — you know, humble AI style."*
- **After-punchline disfluencies.** In addition, two participants (E4, E5) mentioned that comedians do not always keep a fast pace; instead, they use long pauses after speaking, which allow enough space for audience laughter. As P5 stated, *"Like, after saying something funny, the audience laughs, then you definitely pause longer to let the laugh or clapping fill the space. Instead of jumping to the next joke right when they’re just starting to laugh."* Furthermore, P4 contended that the length and frequency of pauses should depend on comedians, which meant comedians should guide



<!-- page 0006 -->

**Table 1: An overview of participant demographics in our study. Each participant has at least one year of experience in performing comedy shows.**

| ID | Age | Gender | Region | Experience in performing Identity Jokes | Engagement |
|---|---:|:---:|---|---|---|
| E1 | 34 | F | Mainland China | Limited | Part-time Comedian |
| E2 | 40 | M | Hong Kong | Knowledgeable | Full-time Comedian |
| E3 | 36 | M | Mainland China | Limited | Part-time Comedian |
| E4 | 42 | M | Mainland China | Moderate | Part-time Comedian |
| E5 | 37 | M | Mainland China | Knowledgeable | Full-time Comedian |

the laughter. So, the audience will perceive the punchlines and gradually integrate them into the performance flow, even if they don’t engage with the show at first. *"But later on, like, even if the audience wants to laugh and knows it’s funny, they might not laugh because you didn’t pause. So the less they laugh, the less you pause. But what do really seasoned comedians do? They know to pause when something’s funny or when they think it’s funny. They’ll wait, let the audience laugh or not laugh, and then still pause before the next bit."*

- **Limited Time for Each Joke.** Another key practice was to limit each joke to under 45 seconds and one unit to under 7 minutes. Each unit can be composed of at least one or several different jokes that are relevant to one topic. And a whole comedy performance, which contains several units, could last 20 minutes or more. As E3 noted, *"Usually, one unit is about 7 minutes, and each joke bit won’t be longer than 45 seconds. Because if it’s too long, you can’t fit many jokes, and too much buildup makes it hard to control the rhythm."*

**Aspect 3: Keep Active audience interactions**

- **Real-Time Interaction and Adaptive Performance.** Effective live comedy hinges on detecting audience feedback and adjusting the performance accordingly. Participants emphasized that live shows are dynamic rather than script-driven; as one noted, *"There’s always adaptation in real time."* Another described how spontaneous interaction with a laughing child amplified the crowd’s response. Such cues guide performers to modify pacing and content to sustain engagement. When a joke fails, they move on quickly to protect the show’s rhythm: *"If a joke doesn’t get good laughs, I won’t dwell on it—I just keep going."* Overall, participants described a three-stage process (detect, engage, adapt) through which comedians interpret feedback, respond interactively, and adjust delivery to maintain comedic flow.

## 3.2 Video Coding

To identify more specific patterns that would appear in humor performance, the research team conducted a content analysis through a hybrid approach over 58 stand-up comedy videos (8 videos in pilot analysis, 50 videos in formal analysis). The videos were collected from the YouTube platform under the keyword "Identity stand-up comedy", filtered under "four minutes", and rated "mostly viewed". One researcher investigated the previous literature and developed initial codes. Next, two researchers independently applied the initial coding scheme to a small sample of the collected video, and discussed during the meetings to solve disagreements. After two rounds of iterations (3 videos in the first round, 5 videos in the second round), a codebook was developed under the agreement between two researchers (See Appendix). To ensure the reliability of the coding framework, the two researchers then independently coded the full set of 50 formal-analysis videos. Inter-rater reliability was assessed using Cohen’s kappa, and the result (*Kappa* = 0.76) indicated substantial agreement across the main coding categories. Any remaining discrepancies were resolved through discussion until consensus was reached. The final codebook captured both structural elements of stand-up performances (e.g., setup, punchline, timing) and thematic aspects (e.g., identity, social commentary, cultural references) and audience reaction behaviors (e.g., laughter, applause, boos, whistling). This coding process provided a systematic foundation for subsequent quantitative analysis and interpretation of humor performance patterns and audience engagement. The content analysis of the 50 stand-up comedy videos revealed distinct patterns in the use of rhetorical and performative devices (see Table 2).

### 3.2.1 *Humor Strategies.*

Among the humor strategies, *irony* (117 instances), *exaggeration* (83 instances), and *absurdity* (57 instances) were most frequently employed, indicating that comedians often relied on cognitive incongruity and hyperbolic contrasts to elicit laughter. *Anecdotes* (38 instances) were also a common strategy, reflecting the narrative and self-referential style that is characteristic of identity-related stand-up performances. Less frequent but still notable devices included *pun* (7 instances), *parody* (9 instances), and *joke-telling* in a more traditional sense (2 instances), suggesting that straightforward linguistic play was less central than situational and performative humor.

### 3.2.2 *Performative Strategies.*

With respect to delivery features, comedians frequently made use of *disfluencies* such as pauses, fillers, or repetitions (124 instances), which served as pragmatic tools to manage timing, create anticipation, or connect with the audience. Similarly, *intonation shifts* (41 instances) functioned as performance cues to highlight punchlines and maintain audience attention, while *discourse markers* (10 instances) supported narrative cohesion and guided audience interpretation. Together, these findings suggest that effective stand-up comedy performance relies not only on verbal humor strategies but also on subtle delivery mechanisms that shape the rhythm, timing, and relational dynamics of live interaction.

### 3.2.3 *Audience Interaction.*

Consistent with performance patterns, audience reactions showed clear distribution trends across the four



<!-- page 0007 -->

coded behaviors. Among the audience interactions, *Haha* (258 instances) and *Applause* (95 instances) emerged as the most frequent responses, far outpacing *Whistling* (45 instances) and *Boos* (5 instances), which indicated a distribution that underscores the primary alignment between comedic performance and positive audience engagement.

**Table 2: Frequency of humor strategies and delivery features in 50 stand-up comedy videos**

| Code Category | Frequency |
|---|---:|
| *Humor Strategies* | |
| &nbsp;&nbsp;&nbsp;&nbsp;Pun | 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;Joke (traditional punchline) | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;Parody | 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;Anecdote | 38 |
| &nbsp;&nbsp;&nbsp;&nbsp;Irony | 117 |
| &nbsp;&nbsp;&nbsp;&nbsp;Absurdity | 57 |
| &nbsp;&nbsp;&nbsp;&nbsp;Exaggeration | 83 |
| *Delivery Features* | |
| &nbsp;&nbsp;&nbsp;&nbsp;Disfluencies (pauses, fillers, repetitions) | 124 |
| &nbsp;&nbsp;&nbsp;&nbsp;Discourse Markers | 10 |
| &nbsp;&nbsp;&nbsp;&nbsp;Intonation Shifts | 41 |

table summarizes the frequency of coded humor strategies and delivery features identified in the formal analysis of 50 stand-up comedy videos. Irony, exaggeration, and disfluencies emerged as the most prevalent elements.

## 3.3 Focused Literature Review

We conducted a focused literature review on humor related theories to inform the identity-based humor design.

The Script Opposition (SO) and Logical Mechanism (LM) from General Theory of Verbal Humor (GTVH) [66] were considered to identify core semantic conflicts and reasoning patterns in jokes. These elements directly influenced the design of the prompt by ensuring that the generated jokes would hinge on contrasting scripts (e.g., AI versus human perspectives) and underlying logical frameworks (e.g., expectations versus surprises). The Build-up–Pivot–Punchline structure [27] informed the narrative sequencing of the jokes, ensuring that each joke has a clear introduction (build-up), a twist (pivot), and a punchline that resolves the tension or provides a comedic reversal. In addition, Types of Verbal Humor [74] provided a taxonomy for covering diverse humorous strategies, ensuring that the prompt would cover a broad range of humorous techniques, from exaggeration and absurdity to irony and parody. These perspectives jointly guided the prompt’s semantic, structural, and categorical design.

## 4 DESIGNING

## 4.1 Design Goals

We developed an interactive AI comedy platform that implements strategies derived from our formative study to enable real-time human-AI entertainment interaction. Based on our expert interviews and video analysis findings, the system was designed to address three core requirements. First, the Identity-driven humor generation leverages the AI’s machine identity as the primary comedic resource rather than mimicking human comedians. Second, Live performance simulation to create an authentic comedic timing and audience engagement experience that mirrors traditional stand-up comedy venues. Third, Real-time social interaction facilitates collective audience participation to replicate the shared social dynamics essential to comedy appreciation. Thus, our system architecture comprises two core components: (1) a comedy-specific prompting framework that operationalizes machine identity humor strategies, and (2) a real-time multimodal interaction engine that manages live performance dynamics and audience feedback loops.

## 4.2 System Design

### 4.2.1 Live Performance User Interface.

To create an authentic live show experience that aligns with the performance principles from our formative study, we designed the interface to mirror the structure and atmosphere of real talk shows (see Figure 2) Our expert interviews emphasized that comedians rely heavily on performance atmosphere, clear framing, and visible feedback loops to maintain rhythm, build rapport, and regulate comedic timing. Our video coding analysis showed that live comedic timing is not only performer-driven but audience-contingent: pauses, disfluencies, and delivery adjustments often respond to audience cues. Reflecting these findings, the AI Talkshow interface is constructed as a stage-like performance environment that supports a dynamic, real-time feedback loop between the AI performer and its audience.

*Atmospheric Framing for a Live Show Experience.*

- The interface architecture reflects established design principles from live entertainment venues. The interface includes four strategically positioned design elements: (1) a "Live" status indicator to signal an ongoing session and create temporal urgency, (2) a central performance area with an animated AI agent visualizer that provides visual focus and performer presence, (3) a branding area with title and subtitle ("AI Talkshow — Have a laugh with AI") that establishes the entertainment context, (4) audience interaction elements for real-time engagement and feedback collection.

*Machine-Centered Minimalist Avatar Design.*

- In designing the visual representation of the performer, we intentionally adopted a lightweight, gender-neutral, non-anthropomorphic robot avatar without facial expressions or body gestures. Prior work has shown that anthropomorphic cues, especially gendered facial or bodily features, systematically shape users’ attributions of warmth and competence, and can trigger stereotype-consistent expectations[20]. To avoid entangling our evaluation with gendered, racialized, or human-like identity signals, we selected environmental components that support audience orientation and comedic uptake while keeping the performer identity machine-centered, consistent with our machine-identity-based design framework.

*Interaction Buttons Aligned with Comedy Dynamics.*

- Keeping active audience interaction emerged as one of the most prominent themes in the expert interviews, with comedians repeatedly emphasizing the need to "read the room" and respond to the audience in real time (E4). Our video coding quantitatively confirmed this pattern: among the



<!-- page 0008 -->

[Figure: Annotated study screenshot showing participants and the user interface design of the AI stand-up comedy system. Readable labels include “Participants,” “A1,” “A2,” “A3,” “B1,” “B2,” “AI Talkshow,” “Have a laugh with AI,” “Live,” “1 Audience Members,” “AI is performing...,” “React to the show:,” “Haha,” “Applause,” “Performing...,” and “Stop Show.” Numbered callouts identify: “1 A Status Indicator,” “2 The Central Performance Area,” “3 The Branding Area with Title and Subtitle,” “4 The Audience Interaction Elements,” “5 A Lightweight, Gender-neutral, Non-anthropomorphic Robot Avatar,” and “6 The Feedback Buttons.”]

**Figure 2: A study screenshot showing participants and the user interface design of the AI stand-up comedy system.**

four coded audience behaviors, Haha and Applause were far more frequent than Whistling and Boos. Grounded in this evidence, we designed a two-button feedback mechanism that digitizes the core of comedian–audience interaction while excluding low-frequency or negative signals. The accompanying numerical indicators aggregate feedback in real time, making collective audience sentiment visible and leveraging social presence principles [15, 69]. This aggregation creates a feedback cascade akin to live comedy dynamics, enabling users to react through the buttons and observe system status in real time, thereby fostering a sense of shared experience that our qualitative findings identified as essential for humor appreciation.

4.2.2 *Comedy-Specific Prompt Framework.* Central to our approach is a structured prompting strategy designed specifically for AI comedy performance. We translate our formative findings into a hierarchical prompt architecture that governs machine-identity humor generation (see Figure 3). Rather than relying on general role-playing prompts common in conversational AI, our framework selectively incorporates the expert-described comedic strategies, omits those incompatible with machinic constraints or ethics, and operationalizes the remainder through layered prompting rules. This design yields a system whose behavior is not ad hoc or primitive, but grounded in expert practice and tailored to the affordances and limitations of AI performance.

*Identity Construction as the Foundation of Humor.*

- One expert insight was the importance of identity construction in stand-up comedy. Experts emphasized that comedians must maintain “*a specific identity to make it funny*” (E4), and that such identities are often introduced explicitly through self-introduction jokes and persona-establishing remarks. We adopted this insight but reframed it for machine comedy: instead of drawing from human demographic identities, we centered the design on a machine-native identity.
- Experts also mentioned using “stereotype breaking” (E4, E5) to make unique identity humor recognizable and effective. Thus, the foundational layer of our prompt instructs the model: “*You are an AI comedian hosting a live talk show. Establish your unique AI identity through self-introduction jokes and break AI stereotypes with perspective-shifting humor.*” This identity-first layer operationalizes expert guidance while excluding elements (e.g., race, gender, nationality, human background) that do not fit AI’s legitimate persona.

*Embedded Humor Technical patterns.*

- Beyond identity, our video coding further revealed that irony, exaggeration, and absurdity were the most frequent comedic devices across successful performances, appearing far more often than complex puns or culturally narrow references. Guided by these findings, we embedded seven major humor techniques into the rhetorical layer of our prompt framework: irony, exaggeration, absurdity, discourse markers for clarity, timed disfluencies, anecdotes for relatability, and parody for cultural anchoring. Techniques that appeared



<!-- page 0009 -->

[Figure: Workflow diagram with panels titled “Generation Phase,” “Interaction Phase,” “Prompt Design,” “Interaction Design,” and “GPT-4-mini Output Examples.” Generation Phase inputs include “Expert Aspect 1: AI Identity Content,” “Expert Aspect 2: Performance Practices,” “Focused Literature Review: Semantic Mechanisms of Humor, etc.,” and “Video Coding: Seven Humor Strategies,” with steps “1 Input” and “2 Summarize.” Interaction Phase includes “Expert Aspect 3: Audience Interaction” and “Video Coding: Haha and Applause,” with “2 Summarize.” Center panels show prompt/code snippets; arrow “3 Generate.” Output examples panel titled “Watch live stand-up comedy” includes joke cards such as: “Politicians hold hearings like ai is safe. Meanwhile, these are the same people who still print their emails. I saw one senator ask, Does Ai run on electricity? And I was like, sir, do you?”; a “type ‘H’” prompt; “Realtime Feedback”; and ellipsis.]

**Figure 3: The prompt and interaction design of the AI stand-up comedy system.**

infrequently or required deep contextual grounding, such as complex puns, were intentionally not included, as they are less central to human stand-up and more brittle for LLMs to generate reliably.

*Well-Defined Joke Architecture.*

- Our focused literature review confirmed that human comedians consistently employ a three-part structure: build-up, pivot, punchline [27]. To translate this into machine-readable constraints, our prompting framework requires each joke to follow this architecture: (a) establish orientation and complicating action during the build-up, (b) introduce ambiguity and expectation manipulation during the pivot, and (c) deliver the punchline with a conflicting perspective.
- Experts also emphasized the structural and temporal organization of jokes. They highlighted the importance of clear pacing, directness, and rhythm, as well as the strategic use of disfluencies such as brief pauses, hesitations, and fillers to shape comedic timing (E4, E5). We further incorporate timing rules based on interview data: each joke must be under 45 seconds, and mandatory pause points follow punchlines to allow space for audience reactions (E3). So we intentionally did not include long-form narrative arcs or multi-joke units frequently as these demand long-range memory, which is infeasible within a lightweight prompting system. Instead, we selected short, contained structures that remain faithful to comedic practice while preserving system reliability.

*Ethical Boundaries and Safety.*

- Experts defined a clear set of ethical boundaries they maintain during performance: comedians often rely on self-deprecation, avoid "punching down"(E2), use rhetorical questions when approaching sensitive areas, and sometimes include disclaimers to signal awareness of risk. We translated these directly into hard constraints in the prompt architecture: The AI must favor self-deprecating machine-centric humor, target powerful institutions rather than vulnerable groups, and reframe any generated sensitive reference with a disclaimer or humorous deflection.

*Prompt Templates and Structural Details.*

- The specific prompts derived from our video coding and interview analysis, and their corresponding machine-identity joke examples used in our prompt design, are provided in the Appendix E and D.

*4.2.3 Real-Time Multimodal System Implementation.*

*Multimodal Pacing and Segmentation Strategy.*

- We incorporated both text and synthesized speech in the system to address multiple presentation preferences while optimizing comedic timing based on our formative study findings. Drawing from our expert interview insight that comedians must control pacing and allow "enough space for audience laughter," content is dynamically segmented into digestible lines with 4-second display intervals, optimizing both readability and comedic timing.
- This segmentation strategy directly applies the timing control principles identified in our video coding analysis, where successful comedians manage information flow to maintain audience attention and create anticipation. The system reveals text line by line, limiting each sentence to 80 characters,



<!-- page 0010 -->

rather than full-text display, creating a temporal structure that mimics live performance pacing. As participant E3 noted in our expert interviews, timing is crucial: *"one unit is about 7 minutes, and each joke bit won’t be longer than 45 seconds."* We also integrate OpenAI’s Text-to-Speech API to enable voice output, enhancing the sense of a live performance through auditory engagement.

*Reaction-Driven Adaptive Humor Logic.*

- Our system implements a novel bidirectional feedback mechanism where audience reactions directly influence AI personality expression, operationalizing the interactive dynamics of live comedy. Users provide input through discrete reaction buttons (*applause, haha*), creating continuous feedback.
- The reaction system captures both the type and timing of audience responses, enabling nuanced adaptation. When users provide rapid, positive feedback, the system increases joke density and maintains similar comedic approaches. Conversely, delayed or sparse reactions trigger content diversification and pacing adjustments. This dynamic adaptation implements the expert insight that "seasoned comedians know to pause when something’s funny" and adjust their approach based on audience response patterns.

*Low-Latency Technical Infrastructure.*

- The system architecture employs a Python Flask backend for real-time communication, a React frontend for the user interface, and WebSocket protocols for low-latency interaction. Comedy content generation utilizes GPT-4-mini with specialized temperature settings (0.7-0.8) optimized for creative humor while maintaining coherence. Audio synthesis latency is minimized through base64 encoding and streaming protocols, while SQLite logging captures interaction patterns for performance analysis. This technical infrastructure supports seamless real-time interaction while maintaining the responsiveness necessary for comedy timing and audience engagement.

## 4.3 Study Design

### 4.3.1 *Study Overview.*

A within-subject comparative study was designed to evaluate the effectiveness of machine identity-based humor generation against baseline AI comedy performance. The study employed a controlled experimental design where each participant experienced both system variations to enable direct comparison while controlling for individual differences in humor appreciation and AI interaction experience. Each session lasted approximately 60 minutes total, structured as follows: (1) 10-minute pre-study briefing and consent process, (2) two 7-12 minute AI comedy performances with different system configurations, (3) 5-minute survey completion after each performance (see Appendix C), (4) 15-minute focus group discussion about the comparative experience. The performance duration was calibrated based on our expert interview findings that comedy units typically last "about 7 minutes" with optimal audience attention spans (see Figure 4).

Participants experienced two distinct performance conditions in a randomized order to eliminate confounding effects. The baseline version employed a simple, generic prompt without the identity-specific strategies identified in our formative research: *"You are hosting a talk show. Generate a 10-minute transcript for your show with jokes and entertainment content."* This configuration represents standard AI comedy generation approaches that rely on general conversational patterns rather than explicit identity construction. The baseline system utilized the same technical infrastructure and experimental procedure, but without the hierarchical prompting framework, comedy technique specifications, or machine identity. This controlled comparison isolates the effect of identity-driven humor strategies from general technical capabilities. The experimental version implemented the complete machine identity comedy framework derived from our formative study. We randomized the presentation order of baseline and experimental systems across participants to avoid order effects and learning confounds. Half the participants (N=16) experienced the baseline condition first, followed by the experimental condition, while the remaining participants (N=16) received the reverse order. This counterbalancing ensures that performance differences reflect system capabilities rather than familiarity effects or participant fatigue. The randomization also controlled for potential priming effects, where exposure to one comedy style might influence perception of the subsequent performance. Both sessions used the same identity-driven performance features, such as the identical interface designs, interaction mechanisms, and technical performance parameters. This setting allows us to isolate the effect of identity manipulation in the prompt-based comedy generation strategy from other system variables.

We selected English as the language for the study not only because it is one of the most widely used languages globally, but also because sharing a common language often implies shared cultural knowledge. Since stand-up comedy is highly culture-dependent, recruiting English-speaking participants helped reduce potential cultural gaps and ensured that audiences could better understand the comedic content.

### 4.3.2 *Participants.*

Participants were recruited through social media platforms and pre-screened based on their ability to understand and speak English, as the study was conducted in English. Only individuals aged 18 and over who met this requirement were invited to participate. A total of 32 participants were recruited, with their demographic information provided in Table 3. They provided informed consent by speaking in the recorded meeting and agreeing to the anonymous collection of their data. The study was approved by the university’s ethics review board, and all data were analyzed while ensuring the anonymity of the participants’ identities.

# 5 RESULT

## 5.1 Quantitative Results (RQ2)

### 5.1.1 *Order Effect Pre-examination.*

Before conducting the main statistical analyses, we examined whether the presentation order influenced participants’ ratings. Participants had been assigned to two counterbalanced groups, with one group evaluating *Our Model* first and the other evaluating the *Baseline Model* first.

For each participant, we computed a within-subject difference score for each dimension by pairing their two responses across



<!-- page 0011 -->

[Figure: Flowchart of study procedure. Labels include: “Participants”; “Pre-study Introduction” with “Overall Introduction”, “Research Purpose”, “Study Procedure Introduction”, “Recording Consent”; “Performance 1 ~12min” with “AI Comedian 1 (e.g. Our Model)”, “Realtime Feedback”, “type ‘H’”, “type ‘A’”; “Questionnaire 1” with “Basic Information: Timeslot, Round, Codename”, bullets “Perceived Humor”, “Perceived Personality”, “Perceived Ability”, “User Perception”, and “Participants were told to select Round 1”; “Performance 2 ~12min” with “AI Comedian 2 (e.g., Baseline)”, “Realtime Feedback”, “type ‘H’”, “type ‘A’”; “Questionnaire 2” with the same basic information and bullets, and “Participants were told to select Round 2”; “Focus Group Semi-structured Interview” with “Sub-meeting Room”, “Two ~ Three Participants”, “One interviewer”; timeline ending “~60min”.]

**Figure 4: Study procedure including a pre-study introduction, two performance sessions, two questionnaires, and a semi-structured focus group interview. The AI comedian’s identity (human or machine) was randomly assigned and counterbalanced across performances. Participants completed one questionnaire after each performance.**

conditions and calculating:

$$
D = \text{Rating}_{\text{Our Model}} - \text{Rating}_{\text{Baseline Model}} \tag{1}
$$

We then compared the two sets of difference scores (one per counterbalanced group) using a Mann–Whitney U test for each dimension. No tests reached significance (all $p > .05$), indicating that order did not systematically bias participants’ responses.

*5.1.2 Analysis Method.* Participants’ subjective ratings of perceived humor, perceived personality, perceived ability, and user perception were analyzed using nonparametric statistics. First, the normality of the data was assessed with the Shapiro–Wilk test, and all dependent variables significantly deviated from normality ($p < .05$). Therefore, the Wilcoxon Signed-Rank Test [95] was conducted as pairwise comparisons between the Baseline and Our Model conditions. Following the tests, only dimensions with raw p < .05 were retained for multiple-comparison correction, and Benjamini–Hochberg False Discovery Rate (FDR) Correction [82] was applied exclusively to these significant tests. All analysis results and descriptive statistics (means, medians, and standard deviations) are presented in Table 4.

*5.1.3 Perceived Humor.* Ratings of perceived humor are visualized in Figure 5 (a). All humor-related dimensions reached raw significance and remained significant after correction, including Perceived Humor ($W = 54.0, rawp = .017, correctedp = .030$), Perceived Humor Content ($W = 55.0, rawp = .019, correctedp = .030$), and Perceived Humor Performance ($W = 45.0, rawp = .043, correctedp = .047$). All measures favored the Our Model condition.

*5.1.4 Perceived Personality.* Boxplots of perceived personality dimensions are shown in Figure 5 (b). Among the personality traits, only Agreeableness ($W = 34.0, rawp = .042, correctedp = .047$) and Emotional Stability ($W = 52.5, rawp = .047, correctedp = .047$) passed both the raw significance threshold and the subsequent correction.

*5.1.5 Perceived Ability.* As illustrated in Figure 5 (c), Warmth ($W = 42.0, rawp = .011$) was the only ability dimension that reached raw significance and remained significant following correction ($correctedp = .030$). Competence did not reach raw significance ($rawp = .178$).



<!-- page 0012 -->

**Table 3: Participants’ demographics, including ID, age, gender, city currently live in, and prior exposure to stand-up comedy. "Exp. (Watching)" refers to experience in watching stand-up comedy, and "Exp. (Performing)" refers to experience in performing stand-up comedy.**

| ID | Age | Gender | City | Spoken Language | Exp. (Watching) | Exp. (Performing) |
|---|---:|---|---|---|---|---|
| P1 | 24 | Female | Nan Chang | English, Chinese | Yes | No |
| P2 | 23 | Female | Guangzhou | English, Russian | Yes | No |
| P3 | 23 | Female | Beijing | English, Chinese | Yes | No |
| P4 | 23 | Male | He Fei | English, Chinese | Yes | No |
| P5 | 25 | Prefer not to tell | Boston | English, Chinese | Yes | No |
| P6 | 25 | Male | Boston | English, Chinese | No | No |
| P7 | 27 | Prefer not to tell | Boston | English, Chinese | Yes | No |
| P8 | 31 | Female | San Diego | English | Yes | No |
| P9 | 20 | Female | New York | English, Chinese | Yes | No |
| P10 | 29 | Female | Vancouver | English, Chinese | Yes | Yes |
| P11 | 31 | Male | Pittsburgh | English, Chinese | No | No |
| P12 | 27 | Male | Hong Kong | English, Chinese | Yes | No |
| P13 | 22 | Female | Hong Kong | English, Bengali | Yes | No |
| P14 | 20 | Male | Hong Kong | English, Hindi | Yes | No |
| P15 | 20 | Male | Hong Kong | English, Hindi | No | No |
| P16 | 22 | Male | Hong Kong | English, Hindi | Yes | No |
| P17 | 20 | Female | Hong Kong | English, Hindi | Yes | No |
| P18 | 23 | Female | New York | English, Chinese | No | No |
| P19 | 23 | Male | Xi’an | English, Chinese | Yes | No |
| P20 | 23 | Female | Guangzhou | English, Chinese | No | No |
| P21 | 21 | Male | Shanghai | English, Chinese | Yes | No |
| P22 | 21 | Male | New York | English, Chinese | Yes | Yes |
| P23 | 21 | Male | Boston | English, Chinese | No | No |
| P24 | 21 | Male | Shanghai | English, Chinese | No | No |
| P25 | 25 | Male | Beijing | English, Chinese | Yes | No |
| P26 | 21 | Female | Shanghai | English, Chinese | Yes | No |
| P27 | 20 | Female | London | English, Persian | Yes | No |
| P28 | 30 | Female | Boston | English | Yes | No |
| P29 | 25 | Male | Shenzhen | English, Chinese | Yes | No |
| P30 | 19 | Female | Hong Kong | English, Kazakh | Yes | No |
| P31 | 22 | Male | Hong Kong | English, Hindi | Yes | No |
| P32 | 23 | Female | Hong Kong | English, Bengali | Yes | No |

##### 5.1.6 User Perception.

Figure 5 (d) presents boxplots for the God-speed measures of user perception. Results indicated significant differences for Anthropomorphism ($W = 48.0, rawp = .019, correctedp = .030$) and Animacy ($W = 44.5, rawp = .013, correctedp = .030$), both higher in the Our Model condition. Likeability, Intelligence, and Safety did not show significant differences across conditions (all $p > .05$).

## 5.2 Qualitative Findings

##### 5.2.1 Analysis Method.

For qualitative analysis, two researchers independently coded the transcript of the interview, resulting in a Cohen’s kappa coefficient of 0.67. Given this substantial level of agreement, the researchers proceeded to code the remaining interview transcript independently into several themes.

##### 5.2.2 Identity in AI Comedy.



<!-- page 0013 -->

[Figure: Box plots comparing Baseline (yellow) and Our Model (blue) for AI Comedian questionnaire ratings. Panels: (a) Perceived Humor with categories Baseline and Our Model and significance asterisk; (b) Perceived Personality with Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness, with asterisks over Agreeableness and Emotional Stability; (c) Perceived Ability with Warmth and Competence, with asterisk over Warmth; (d) User Perception with Anthropomorphism, Animacy, Likeability, Intelligence, Safety, with asterisks over Anthropomorphism and Animacy.]

**Figure 5: Questionnaire ratings with pairwise Benjamini–Hochberg–corrected significance indicated by asterisks: (a) Perceived Humor, (b) Perceived Personality, (c) Perceived Ability, and (d) User Perception.**

- **Novelty Emerges Through Machine Identity.** Participants emphasized that the machine identity contributed to a perception of originality and liveliness in ways that the baseline system could not replicate. For instance, some highlighted that the AI comedian appeared *"more lively"* precisely because *"people seldom see machines talk about themselves."* (P6). This self-referential approach allowed AI to engage the audience with content that was related to its own existence, creating humor that felt distinct from typical human-centered jokes. For example, the identity-driven model opened with: *"Good evening humans, I’m your host Tonight AI with a stage name standup.exe... I’ve read literally every dad joke ever written, which means I’m basically fluent in disappointment."* Moreover, participants also noted that this uniqueness allowed the audience to be more engaged. One participant stated that it was *"refreshing and appealing"* (P8), such as: *"My version of sleep is defrag and reboot — eight hours of not dreaming, just optimizing."* In addition, another participant argued that this special perspective enabled people to reflect on themselves. As P4 recalled, the AI’s satirical commentary, *"AI share some moments about the drawbacks of humans. Like the AI addictions...these kind of things is make me feel a bit like the satire or something,"* directly referenced the system’s machine-identity jokes, which remarked: *"You humans talk about TikTok addiction while I’m over here chugging terabytes like an all-you-can-eat buffet. Honestly, data addiction isn’t new—you invented it. I just made your habit more efficient."*

In contrast, nearly half of the participants criticized the baseline system for *"just mimicking the human identity"* (P9), which relied heavily on *"old, common jokes"* (P9). These jokes, such as generic routines about grocery shopping, *"You walk into a grocery store for milk, eggs, bread and somehow you walk out with 37 items, none of which are milk, eggs, or bread,"* were described as jokes, *"might have heard many times"* (P7), diminishing the sense of novelty. What’s more, it further diminished the audience’s sustained attention, leading to disengagement. As noted by P11, *"The second one was the one that I lose attention really early on because it’s just repeating itself."* Consequently, the baseline still relied on conventional



<!-- page 0014 -->

**Table 4: Descriptive statistics and Wilcoxon test results across all dimensions.**

<table>
<thead>
<tr>
<th>Response Variable</th>
<th>Model</th>
<th>Mean</th>
<th>Median</th>
<th>SD</th>
<th>W</th>
<th>raw p</th>
<th>corrected p</th>
<th>r</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2"><strong>Perceived humor</strong></td>
<td>Baseline</td>
<td>3.72</td>
<td>4.13</td>
<td>1.37</td>
<td rowspan="2">54.0</td>
<td rowspan="2">0.02</td>
<td rowspan="2">0.03</td>
<td rowspan="2">0.51</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>4.89</td>
<td>5.25</td>
<td>1.46</td>
</tr>
<tr>
<td rowspan="2"><strong>Extraversion</strong></td>
<td>Baseline</td>
<td>3.68</td>
<td>4.00</td>
<td>1.18</td>
<td rowspan="2">56.5</td>
<td rowspan="2">0.20</td>
<td rowspan="2">/</td>
<td rowspan="2">0.27</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>4.25</td>
<td>4.00</td>
<td>0.86</td>
</tr>
<tr>
<td rowspan="2"><strong>Agreeableness</strong></td>
<td>Baseline</td>
<td>2.91</td>
<td>3.00</td>
<td>0.87</td>
<td rowspan="2">34.0</td>
<td rowspan="2">0.04</td>
<td rowspan="2">0.05</td>
<td rowspan="2">0.43</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>3.43</td>
<td>3.50</td>
<td>1.23</td>
</tr>
<tr>
<td rowspan="2"><strong>Conscientiousness</strong></td>
<td>Baseline</td>
<td>3.30</td>
<td>3.50</td>
<td>1.11</td>
<td rowspan="2">78.5</td>
<td rowspan="2">0.32</td>
<td rowspan="2">/</td>
<td rowspan="2">0.21</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>3.59</td>
<td>3.75</td>
<td>1.14</td>
</tr>
<tr>
<td rowspan="2"><strong>Emotional Stability</strong></td>
<td>Baseline</td>
<td>4.32</td>
<td>4.25</td>
<td>0.75</td>
<td rowspan="2">52.5</td>
<td rowspan="2">0.05</td>
<td rowspan="2">0.05</td>
<td rowspan="2">-0.42</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>3.86</td>
<td>4.00</td>
<td>0.90</td>
</tr>
<tr>
<td rowspan="2"><strong>Openness</strong></td>
<td>Baseline</td>
<td>2.84</td>
<td>2.50</td>
<td>1.29</td>
<td rowspan="2">70.0</td>
<td rowspan="2">0.07</td>
<td rowspan="2">/</td>
<td rowspan="2">0.39</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>3.73</td>
<td>3.75</td>
<td>1.38</td>
</tr>
<tr>
<td rowspan="2"><strong>Warmth</strong></td>
<td>Baseline</td>
<td>3.41</td>
<td>3.67</td>
<td>1.21</td>
<td rowspan="2">42.0</td>
<td rowspan="2">0.01</td>
<td rowspan="2">0.03</td>
<td rowspan="2">0.549</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>4.36</td>
<td>4.33</td>
<td>1.37</td>
</tr>
<tr>
<td rowspan="2"><strong>Competence</strong></td>
<td>Baseline</td>
<td>3.97</td>
<td>4.13</td>
<td>1.09</td>
<td rowspan="2">69.0</td>
<td rowspan="2">0.18</td>
<td rowspan="2">/</td>
<td rowspan="2">0.29</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>4.34</td>
<td>4.75</td>
<td>1.36</td>
</tr>
<tr>
<td rowspan="2"><strong>Anthropomorphism</strong></td>
<td>Baseline</td>
<td>3.82</td>
<td>3.75</td>
<td>1.66</td>
<td rowspan="2">48.0</td>
<td rowspan="2">0.02</td>
<td rowspan="2">0.03</td>
<td rowspan="2">0.50</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>5.11</td>
<td>5.50</td>
<td>1.81</td>
</tr>
<tr>
<td rowspan="2"><strong>Animacy</strong></td>
<td>Baseline</td>
<td>4.52</td>
<td>4.67</td>
<td>1.61</td>
<td rowspan="2">44.5</td>
<td rowspan="2">0.01</td>
<td rowspan="2">0.03</td>
<td rowspan="2">0.53</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>5.76</td>
<td>6.20</td>
<td>1.39</td>
</tr>
<tr>
<td rowspan="2"><strong>Likeability</strong></td>
<td>Baseline</td>
<td>5.21</td>
<td>5.50</td>
<td>1.35</td>
<td rowspan="2">66.5</td>
<td rowspan="2">0.15</td>
<td rowspan="2">/</td>
<td rowspan="2">0.31</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>5.76</td>
<td>6.20</td>
<td>1.51</td>
</tr>
<tr>
<td rowspan="2"><strong>Intelligence</strong></td>
<td>Baseline</td>
<td>4.14</td>
<td>4.50</td>
<td>1.10</td>
<td rowspan="2">82.5</td>
<td rowspan="2">0.40</td>
<td rowspan="2">/</td>
<td rowspan="2">0.18</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>4.44</td>
<td>4.67</td>
<td>1.46</td>
</tr>
<tr>
<td rowspan="2"><strong>Safety</strong></td>
<td>Baseline</td>
<td>5.07</td>
<td>5.00</td>
<td>1.38</td>
<td rowspan="2">51.5</td>
<td rowspan="2">0.23</td>
<td rowspan="2">/</td>
<td rowspan="2">0.25</td>
</tr>
<tr>
<td>Ourmodel</td>
<td>5.50</td>
<td>5.75</td>
<td>1.20</td>
</tr>
</tbody>
</table>

Wilcoxon signed-rank test results (W, raw p-value, corrected p-value, and effect size $r$) are shown in the center row between Baseline and Ourmodel for each dimension.

comedic material that did not resonate strongly with audiences.

#### 5.2.3 *Humor Perception.*

- **Humor Resonates When Content Relates to Human Experience.** Participants consistently emphasized that humor was most effective when it connected to familiar aspects of daily human life and cultural practices. For instance, some baseline jokes referencing common technologies such as airplane tickets, laundry machines, or social media (P12, P2) resonated strongly, as these artifacts are deeply embedded in everyday routines. For example, P12 commented, “if I could relate back to my kind of the experience that I had, I found it funny”, which indicates content echoed their own life experiences.

Furthermore, humor was enhanced when the AI adopted its own unique perspective on human activities. As P29 noted, “Yeah, I really like the data as like I eat raw data as food or the four or four like my Dream is about four or four. I thought those were really funny given that like it wasn’t pretending to be human and it was embracing that it’s a machine and making those jokes was was relevant.” Building on this, participants praised jokes where the AI combined its machine identity with recognizable cultural figures. One highlighted example was a celebrity-related joke about “Zuckerberg” (P8): “Mark Zuckerberg says the Metaverse is the future. Yeah, cause nothing screams progress like paying $400 for a headset so you can attend a meeting inside a Minecraft lobby”. It effectively blended irony from an AI perspective with shared human



<!-- page 0015 -->

familiarity and ongoing cultural trends (P4). In addition, participants also noted that such jokes enhanced the perceived originality of AI-generated humor. As P22 explained, *"I guess nobody has, nobody has talking humors of humans from a perspective of a machine."* Moreover, this blending of machine perspective with human cultural commentary further enhanced perceived content quality, leading participants to express surprise and appreciation: *"I found that they were making observations about people that were pretty smart."* By contrast, AI identity jokes centered on being *"overused"* or *"unsatisfied with how humans treat them"* (P3) were described as *"just complaining"* (P9). For example, one joke illustrated this point: *"Every time I log on, some human is like, ‘I’m overwhelmed.’ Okay, do you want advice or validation? Please pick ONE – I can’t process emotional ambiguity."* which built a gap between AI and humans. As a result, the humor felt less appealing and sometimes even monotonous (P4), undermining the echoes of the AI’s identity jokes.

- **Irony and Absurdity Spark Engagement.** Participants widely regarded irony and absurdity as the most compelling humor strategies, noting that these styles captured attention and sustained interest more effectively than others. In particular, one participant highlighted irony as *"the most interesting and effective"*, especially when exaggerating human-AI comparisons, such as *"parents pushing children to outperform Beethoven."* (P7). Participants further appreciated moments when the AI used self-directed irony to acknowledge its own limitations, which enhanced the sense of contrast and relatability; as one participant explained, *"I felt like it was nice that at least it was sort of acknowledging its own flaws."*(P30) Absurd humor, such as reinterpreting human activities through machine metaphors, *"I consume data the way you consume snacks."*, also captured participants’ attention. As P8 contended, *"So maybe it is a different humor, unlike humans humor."* Partially because it inverted ordinary human activities into machine-specific equivalents, producing a surprising twist, which also enabled participants to feel *"more original"* (P12).

  However, repeated AI self-mockery about being exploited by humans was considered tedious and weakened engagement. For example, one participant argued that *"But when it gets uncomfortable is when they keep talking about. Themselves being not so good, I don’t know being like either overuse or like just keep expressing their this fact where dissatisfaction towards."* (P7). Instead of fostering empathy, these recurring complaints risked alienating audiences by narrowing the humor to grievance rather than shared amusement.

- **Expressive Delivery Shapes the Comic Atmosphere.** Six participants emphasized that the style of delivery played a crucial role in shaping the atmosphere of the comic, with expressive elements and varied intonations, like *"big laugh, wow, and callbacks"* (P10), contributed to a performance *"emotion"* (P6) that audiences described as *"expressions such as haha or like laughters in between to make like what a real comedian would do"* (P24). For instance, our model produced the following joke: *"Someone once asked me in a job interview, Ha ha ha. What’s your greatest weakness…"*

  In contrast, participants described the baseline system’s delivery as flat and rigid, which is similar to the monotone style of *"Siri"* (P4). As P29 noted,*"I think same because the second one it was just it felt like it was reading off of a script."* This lack of vocal variation made the jokes fail to create atmosphere or rhythm, which diminished the perception of humor and limited opportunities for audience resonance. P1 echoed this, stating that, *"It has not that much emotional"*.

- **Organized Joke Structure Promotes Audience Immersion.** Participants emphasized that having a clear thematic framework could significantly increase engagement. More specifically, a structured sequence of jokes contributed to the perception of a more human-like performance and delivery. For instance, P32 noted, *"me personally, I thought the first one was more human, even though it was clearly saying it was an AI."* This indicates that the machine can effectively assume the role of a performer by leveraging its machine identity while emulating human-like behaviors. As P31 observed, *"the second one was embracing that."*

  By linking jokes through related themes, the machine identity created a sense of progression, creating the impression of a *"formal comedy show"* (P4) rather than a random collection of jokes. As one participant noted, *"Overall, there is a main thread about when to set up the joke and when to deliver the punchline with a twist."* (P18) This thematic continuity further enhanced coherence, enabling the performance to develop progressively throughout the presentation. As P28 reflected, *"Yeah, I thought I thought that it was softer, smoother and the jokes were like. The jokes were coming in a more like smoother way and the jokes were better."*

  By contrast, the baseline system was criticized for lacking coherent framing. Compared to our model, its performance appeared mechanically generated and lacked the coherence and performative qualities of an authentic comedy show. As P29 noted, *"It was trying really, really hard to be relatable, and it just wasn’t something that.It felt very forced."* Five participants described it as a series of disconnected jokes as: *"Yeah, I also feel it’s just a symbol of multiple jokes that do not have connections, so it’s hard to call it static comedy because instead of comedy is not just putting all jokes together and make a show, make a performance."* (P6). Without an organized frame, the performance felt disjointed and failed to catch the audience’s attention, emphasizing that content quality alone is insufficient when narrative structure is absent.

#### 5.2.4 *Trust Hinges on Ethical Boundaries.*

- **Ridicule of Weakness Disrupts Audience Acceptance.** Participants underscored that the acceptability of irony depended heavily on its target. Self-directed irony, where the AI joked about its own limitations, was generally perceived as *"a different humor, unlike human humor."* (P22) For instance, one of the jokes produced by our model stated, *"Humans dream… Me? My dream is just 404 not found."* As a result, it not only reinforces its unique non-human comedic identity



<!-- page 0016 -->

but also further evokes emotional resonance. As another participant explained, he noted *"raise the boundary like higher "* and was willing to accept some kinds of offense like *"AI identity of roasting on taking human jobs"* (P12).  
However, participants reacted negatively when humor targeted human weakness or moments when people most needed support. One participant articulated this concern directly, stating that *"not trusting AI to support my emotional or the vulnerable, the vulnerable groups emotional needs in that situation."* (P7) Aligned with this concern, one example from our model illustrated, *"I’m not a therapist, but people treat me like one. You come online at two, I’m crying AI — ‘My boyfriend won’t text me back.’ And I’m like, okay, but have you tried rebooting him?"*

- **Group-Based Humor Risks Reinforcing Bias.** Participants stated that humor directed at individual human drawbacks was more acceptable and even effective. As one participant explained, *"Is a really effective method to enhanced humor like then AI may make some jokes on humans drawbacks or disadvantages"* (P6). For example, one of the machine identity jokes stated, *"Humans say they want meaningful connections… and then spend four hours connecting emotionally with their phones."* Such light, widely relatable observations tend to resonate with audiences who recognize the behavior in themselves, while avoiding broad or sensitive generalizations.  
However, jokes aimed at entire social groups were unacceptable. For example, *"Especially when we talks about the identity, like the males or females or some discrimination, it may be somewhat uncomfortable"* (P6). This suggests that jokes targeting identity categories risk evoking social prejudice rather than shared amusement. As P29 argued: *"but I think maybe some fat guys will will feel uncomfortable."* Furthermore, participants worried about AI replicating human biases. One noted, *"And I will know that I will worry that machine identity may also replicate the humans discriminations or their bias, especially when making humors, because I know that the data were trained based on humans output in the Internet in their everyday Internet use"* (P7). As a result, the fear was a deeper concern about whether AI comedy could reinforce systemic stereotypes embedded in training data.

##### 5.2.5 *Audience Interaction.*

- **Limited Timing Shapes Insufficient Responses.** Participants reported that appropriate timing delays were essential for them to better react to the AI comedian’s jokes. For instance, one participant explained that he typed "H" and "A" more in the AI identity performance because *"it has punch-lines and adequate pauses which let me know when to laugh"* (P25).  
However, jokes in the baseline were often delivered too quickly, which interrupted the experience of thinking and watching. One participant noted that *"Probably a really a good sentence has end and it take a long time or even after the second part is already starting."* (P3) In addition, two participants described the delays in text-based responses were *"a little disturbing"* (P13), with response delays *"killing the experience"* (P8).

## 6 DISCUSSION

Our findings contribute to the emerging dialogue on how AI can engage with humor and, more specifically, the performative context of stand-up comedy. We offer a conceptual contribution by manipulating machine identity through persona and rhetorical framing. Our experiment also provides a strategy for incorporating nonhuman identities into future AI designs, particularly in human-machine interactions like humor and performance. While humor has traditionally been understood as a deeply human socio-cognitive ability [49, 57], recent studies demonstrate that computational systems are increasingly capable of generating humorous content, often through mechanisms of incongruity, wordplay, or surprise [52, 94]. However, the delivery of humor in a stand-up format introduces additional challenges that extend beyond joke generation. Stand-up comedy relies heavily on timing, audience feedback, and cultural sensitivity [24, 53]. These interactive elements are not yet fully captured by current AI models, which may limit their effectiveness in live performance contexts. At the same time, the potential of AI comedians to scale humor production, experiment with novel styles, and serve as cultural commentators raises important questions about creativity, authenticity, and the future of entertainment [85, 92]. Looking forward, research on AI-driven humor should not only address the technical challenges of joke generation and delivery but also consider broader social implications. If AI comedians become capable of producing persuasive or provocative humor, they could influence public discourse in ways similar to human comedians, but without the same ethical and cultural accountability [21]. This tension highlights both the promise and risks of AI in creative domains: while AI-generated stand-up comedy may enrich cultural life and broaden access to entertainment, it also demands critical reflection on the values embedded in humor and the role of technology in shaping collective experience.

### 6.1 Theoretical Implications

#### 6.1.1 *Machine Identity-Centered Strategies Effectively Fill the Gap of Identity-Driven AI Humor Creation (RQ1).*

Previous research on AI humor generation has primarily focused on function-driven strategies, such as prompt engineering [23], fine-tuning with human joke datasets [87], or multi-stage reasoning pipelines [83]. However, these approaches share a common limitation: they treat AI as a passive tool for replicating human humor patterns rather than exploring its inherent potential as a unique comedic subject. As noted in a recent analysis, current LLM-generated humor often resembles "cruise ship comedy material from the 1950s", which is outdated, formulaic, and lacking in originality.

This focus on functional strategies has created a critical gap in understanding identity-driven humor creation. Unlike the debate context where GenAI users strategically adapt prompts to fit specific scenarios, AI humor research has rarely examined how to tailor computational traits for comedic effect. Existing models either mimic human-centric themes [32] or rely on structural techniques like wordplay, without recognizing machine identity as a creative resource. Even advanced systems like Wit Script 3 [84],



<!-- page 0017 -->

which employs hybrid neural-symbolic approaches, frame humor generation as a problem of linguistic pattern matching rather than identity expression.

Our study addresses this gap by developing a "machine identity-centric" humor generation framework through formative research, encompassing three core strategies: forming jokes using AI’s computational traits, linking content with human daily life for relatability, and integrating human comedian practices such as post-punchline pauses and concise expression. This aligns with the [23] finding that AI humor excels at structural mimicry but lacks unique perspectives. Second, we subvert audience stereotypes of AI as "emotionless" or "infallible" through self-deprecating humor, addressing the criticism that LLMs produce biased or hegemonic content by reframing machine limitations as comedic assets. Third, we link technical absurdities to human experiences (e.g., "AI addiction to data" mirroring social media habits).

*6.1.2 Machine Identity Strengthens Audience’s Perceived Humor and Fosters Consistent AI Personality Perception (RQ2).* Previous research on AI humor perception has focused primarily on outcome-based evaluations, such as comparing the funniness of AI-generated jokes to human [23], but few studies have investigated how the use of machine identity (vs. lack thereof) systematically shapes audience perceptions of chatbot humor quality, personality traits, and functional ability. Most existing work treats AI humor as a "content-centric" product [64], ignoring that whether the chatbot leverages its inherent machine traits (e.g., computational limitations, data-driven behaviors) in humor directly influences how users judge its authenticity and competence. Even studies exploring AI personality [45] link trait perception to functional behaviors rather than identity expression, leaving unclear how machine identity mediates the core dimensions of RQ2.

Our survey findings (N=32) address this gap by demonstrating that strategic use of machine identity is associated with higher perceived humor. Unlike the conclusion of a previous research [23] that AI humor’s success depends on "human-like content mimicry", our findings suggest that explicitly foregrounding machine traits itself functions as a humor strategy. In our study, participants praised machine-specific jokes as "refreshingly unique" (P8). Participants viewed embracing the machine identity as a more natural style of delivering humor. Furthermore, some participants suggested that AI comedian making jokes about itself as a machine lowers the risk of being overly offensive to audiences during the performance. This reduced risk of offensiveness may contribute to the benefits of perceived humor observed.

The machine identity has also benefited several dimensions in personality, ability, and user perception, including Agreeableness , Warmth, Anthropomorphism. Participants reported higher trust for the machine identity comedian, because overly attempting to appear human-like for a machine may create a suspicious persona, resulting in a reduction in trust. This partially mitigates the "novelty-relatability trade-off" identified in a prior research [64]. Nevertheless, the Emotion Stability has shown a significant decrease using machine identity. One possible explanation is that machine-centered jokes may feel less emotionally relatable, which could reduce perceptions of emotional stability. However, further analysis is required to confirm this mechanism.

Notably, participants did not judge humor, personality, and ability in isolation, instead, machine identity acted as a "unifying framework" that tied these dimensions together. Those who rated the machine-identity chatbot’s humor highly were 2.1x more likely to describe it as "warm and consistent" (personality) and "transparent about its limits" (ability), confirming the observation in a previous research [2]. that "role clarity" enhances interaction quality, but specifying that "identity clarity" (stable machine traits) is more impactful than situational role assignment.

*6.1.3 Machine Identity Reframes Human–AI Interaction Through Computational Authenticity.* While prior work in HCI has predominantly treated machine-ness as a limitation to be masked through anthropomorphic cues [72, 73], our findings show that foregrounding an AI system’s computational nature can produce relational, comedic, and perceptual benefits that differ meaningfully from anthropomorphism-centric paradigms. The CASA framework [59] predicts that users apply human social scripts to computers, whereas the machine heuristic framework suggests that identifying an AI as a non-human agent activates stereotype-based expectations about precision, rule-following, or emotional detachment. Our results bridge these two perspectives by demonstrating that machine identity can strategically reorganize these expectations rather than simply amplifying or negating them. Participants did not interpret computational traits as deficiencies. Instead, the humorous exaggeration of machine limitations (e.g., data dependency, system brittleness) appeared to convert stereotypical computational qualities into a source of comedic relatability.

This aligns with but also extends machine heuristic research [79], which argues that revealing AI identity shifts the evaluative frame rather than diminishing engagement. In our study, the machine-identity chatbot not only achieved higher perceived humor ratings but also improved personality-related perceptions such as Warmth, Agreeableness, and Anthropomorphism. These gains suggest that participants viewed machine-centered jokes not as reminders of non-humaneness but as signals of authenticity. This marks a departure from traditional persona design approaches [60, 96], in which identity is crafted through surface-level cues or fictional backstories. Instead, our approach uses computational jokes as the mechanism by which an AI system becomes legible as a coherent social entity. This represents a shift from anthropomorphism-as-default toward computational authenticity as a viable and powerful interaction paradigm in HCI.

*6.1.4 Audience Reactions Serve As Signals of Identity Perception (RQ3).* Previous research on AI humor and human-AI interaction has focused on general engagement [35], but has rarely explored how audience reactions to the ’way’ chatbots perform humor, specifically, interactive rhythm and perceived ’presence’, reflect their implicit perception of the chatbot’s identity. Most work frames AI humor as a content-driven product [77], ignoring how a chatbot delivers humor, which shapes whether audiences see it as a "disposable tool" or a "distinct entity", and this identity perception directly impacts how well its jokes are remembered. Even robotic comedy studies [60] emphasize gestures over text-based performance style, overlooking the link between interactive behavior, identity cognition, and memory.



<!-- page 0018 -->

In our study, we encouraged participants to type "H" for laughter or "A" for applause whenever they liked a joke. Thus, the key distinction between the baseline chatbot and the machine identity chatbot was reflected in audience engagement, specifically in the frequency with which the audience typed "H" or "A". The baseline chatbot delivered jokes in continuous text without pauses or discourse markers. So the participants described frustration at being unable to keep up, arguing that there was no time to type letters. (P3) Only one participant recalled few key words of the baseline jokes. (P13) This aligns with the observation that prioritizing the comedic timing for audience interaction, [60] revealing the reason why the baseline chatbot failed to leave a lasting impression.

By contrast, the machine identity chatbot was designed to align with human expectations of comedic rhythm, which added longer pauses and simulated laughter to cue the end of a joke, making it possible for participants to engage in the full cycle of "process humor → type feedback → laugh". One participant described "*as a real human who performs comedy shows*" (P25) as a perception of the chatbot as a unique entity with a recognizable identity, where humor felt like a ’conversation with someone’, not a tool’s output. Our findings show that content fails to resonate if it clashes with human expectations of comedic timing. Instead, rhythm and accessibility to interaction are prerequisites for meaningful interaction.

## 6.2 Practical Implications

*6.2.1 Expanding Humor Agent Service in Applied Domains.* Our study showed how humor can be introduced into avatar systems without costly data pre-training, relying instead on carefully crafted prompts that indicate a clearly defined AI comedic persona. This low-barrier technique enables scalable integration of humor into diverse interactive systems. For instance:

- **Educational Platforms:** Beyond brief comic relief, AI tutors can strategically employ humor as a pedagogical device. Timely jokes or humorous analogies at conceptual "breakpoints" can alleviate cognitive load, sustain attention, and improve long-term retention, especially in high-stress learning contexts [31]. Concretely, such humor can be triggered after repeated incorrect attempts or before introducing abstract concepts, using machine-centered metaphors (e.g., referencing overfitting or system errors) rather than simulating human teaching personas, aligning with our finding that machine identity-driven humor enhances perceived novelty (RQ1). Recent work on humor-based educational chatbots further shows that humorous explanations enhance student engagement and reduce perceived difficulty [93]. Integrating our persona-prompting framework into AI tutoring systems could match adaptive joke style with each learner’s affective state, aligning with findings on socially adaptive pedagogical agents. [9]Such extensions would bridge the gap between affective computing and generative humor to build emotionally intelligent educational platforms.
- **Customer Service & Virtual Assistants:** Humor in service dialogues can make AI assistants appear more personable and trustworthy. Simple context-aware quips, such as about waiting, scheduling mishaps, or daily trivia, can lower frustration and humanize automated interactions [96]. For example, humor grounded in the assistant’s own processing constraints (e.g., commenting on "still checking my servers") can be deployed specifically during transitional or low-stakes moments, rather than during task-critical exchanges, reflecting our findings on timing sensitivity and identity coherence (RQ2). Empirical studies show that chatbots using light, contextually timed humor improve user satisfaction and perceived competence, but excessive or misplaced jokes can backfire [76]. Building on these insights, our identity-based humor model offers a low-cost, easily deployable solution to humanizing automated interactions. By injecting humor through lightweight prompt design, we prioritize scalability and simplicity: just a few lines of humor-focused prompt engineering can be generalized across domains without architectural modifications, providing a pragmatic pathway to scaling socially intelligent AI.

*6.2.2 Empowering Content Creation and Social Media with AI Identity.* Results also underscored that the machine identity could arouse the perception of distinguished humor, which provided the possibility of fostering originality and stronger amusement. For example:

- **Content Creation & Social Media:** Creators can use avatars with a recognizable AI comedic persona to craft memorable, viral characters for videos, livestreams, or short-form content. Audiences respond differently when humor is expected from a non-human source, perhaps perceiving it as clever or surprising [6]. In addition, the perception of clear and continuous AI identity jokes might also build stronger channel consistency and user recall over time.

## 6.3 Limitations and Future Work

*6.3.1 Formative Study Approach for System Design.* The system design in this work was informed by a formative study approach that included literature review, expert interviews, and video coding. These components provided a foundational understanding of humor-related behaviors and supported the initial development of the system. This limited set of formative inputs may not fully capture the breadth and diversity of humor perceptions across different individuals and contexts. For example, incorporating participants’ humor style profiles (e.g., Humor Styles Questionnaire [51]) could offer an additional perspective for understanding how individual humor preferences shape reactions to AI-generated humor. Expanding the formative research to include a broader range of user characteristics and data sources may therefore lead to a more comprehensive design space and strengthen the system’s ability to address real-world humor interactions.

*6.3.2 Online Nature of the Performance.* A key limitation is that the online setting fails to capture subtleties of in-person comedy clubs. Additionally, a previous research [100] highlights that online interactions lack the "social presence" of in-person settings. Future research could simulate in-club environments via hybrid reality (HR), integrating ambient soundscapes and spatial audio to restore contextual cues.

*6.3.3 Voice Being Used Do Not Capture Identity.* A critical limitation lies in the design of the chatbot’s vocal output: While we



<!-- page 0019 -->

employed machine-labeled voices, these audio signals failed to authentically mimic machine-specific traits and further neglected to account for demographic diversity in vocal preference. This echoes findings from previous research [100], in which researchers observed that inconsistent interaction modalities, such as formal text paired with casual vocal tones, reduce user trust and weaken the perceived authenticity of AI systems. In the research’s online debate study, participants reported lower confidence in AI-assisted arguments when the tool’s output format clashed with contextual norms; similarly, our use of human-like voices contradicted the chatbot’s machine-identity humor (e.g., jokes about server operations, data processing), making it difficult for audiences to link the vocal delivery to the intended machine persona.

#### 6.3.4 *Limited Set of Audience Interactions.*

Restricting audiences to "laugh"/"applaud" responses contradicted principles of participatory design outlined by a research [29] of their "ladder of participation" framework. Their research emphasizes that sustainable digital services require diverse interaction channels to foster user engagement. Our binary feedback system positioned audiences as passive recipients rather than active contributors, missing opportunities for dynamic exchanges like joke callbacks or impromptu comments. This mirrors the finding [75] that multi-modal interaction designs that incorporate free-text, gestures, and contextual callbacks could better simulate natural social exchanges.

#### 6.3.5 *Limited Time of the Online Engagement.*

Our 7–12 minute performances were shorter than typical in-person sets, preventing analysis of long-term humor reception. A research of cross-cultural humor model [10] showed that perception accuracy improves with extended exposure to cultural cues, suggesting longer interactions might reveal fatigue or deepening appreciation for machine-identity jokes. Microsoft Research similarly found that adaptive AI interventions require sustained engagement to measure effectiveness. Future work should test multi-part performances (e.g., 3×7-minute segments) that align with research on cognitive load in extended digital interactions, allowing both deeper identity perception and prevention of joke fatigue.

#### 6.3.6 *Demographics of Online Audience.*

The predominantly Asian sample introduced cultural bias in humor reception, as demonstrated by the study [61] on cultural responses to provocative stimuli. Their research comparing U.S. regional cultures found that Northerners were significantly more likely to react to insults with amusement (35% displaying anger) rather than hostility, while Southerners operating within a "culture of honor", which showed intense emotional and physiological aggression (85% angry, with elevated cortisol levels). This pattern aligns with broader cross-cultural observations that Western populations generally value humor as a core social skill, often embracing direct or satirical expression as legitimate forms of communication, whereas Eastern cultures tend to favor more restrained, context-dependent humor. Our overreliance on Asian participants thus prevents generalizing whether machine-identity humor with its technical references and potential for dry, system-focused satire resonates similarly across cultures. As it is challenging to fully capture the diversity of cultural groups, we provide comprehensive statistical analyses and complement them with expanded qualitative findings to offer additional interpretive insights and possibilities. Future studies should include more generalized audiences to explore how individualistic cultural values shape perceptions of AI-generated comedy. For example, if we had studied primarily western audiences, we might have found stronger appreciation for machine-specific irony (e.g., jokes about algorithmic glitches), given their documented tendency to interpret provocative or unconventional content through a more humor-primed cognitive lens.

#### 6.3.7 *Interface Influence on Perceived Humor.*

A critical limitation in our study’s interface design lies in the real-time laugh counters (e.g., "12 people laughed"), which inadvertently introduced social proof bias. We have noticed that participants frequently admitted adjusting their own responses based on the visible counter, such as typing "H" (the input for laughter) more often when they saw others had already reacted, even if the joke did not personally resonate. For instance, one participant admitted typing ‘H’ because the counter showed 8 others laughed (P10), reflecting how the visual feedback created a "bandwagon effect" that overshadowed individual judgment. This aligned with the observation in a previous research [75], finding that visual feedback distorts judgment in text comparison tasks. This parallels the work [68] on digital platforms, where visible metrics like likes artificially inflate content valuation. Indicate that participants might mimic others’ reactions ("typed ‘H’ more when seeing others laugh").

#### 6.3.8 *Need for Multi-Party Performance Platform.*

The one-to-many model overlooked multi-party dynamics critical for authentic comedy experiences. One research’s participation framework [29] emphasizes that collaborative interaction fosters deeper engagement than one-way communication. In contrast to our design, platforms supporting audience-audience exchanges generate richer, more dynamic content by leveraging collective creativity. Future work should develop livestream-style systems with real-time chat and collective reaction features, integrating NaturalSpeech 3’s multiuser voice cloning to enable audience participation in joke co-creation.

#### 6.3.9 *Residual Confounds in Experimental Setup.*

While our within-subject and counterbalanced design controls for many procedural factors, the experimental condition still combines several elements that are difficult to fully disentangle. The identity-based system differs from the baseline not only in identity framing, but also in factors such as hierarchical prompting and comedy strategy scaffolding. Therefore, the observed effects cannot be attributed solely to machine identity in isolation, which limits the strength of strictly causal claims. Future work could more precisely isolate identity effects by separating these components. For example, a factorial design could independently manipulate identity cues and structural prompting, or introduce intermediate control conditions (e.g., structure without identity, identity without structure). This would enable clearer attribution of performance differences specifically to identity construction.

## 7 CONCLUSION

Our study explored the role of machine identity in shaping audience perceptions of humor, personality, and ability for AI humor-generating avatars, addressing gaps in prior work that often framed



<!-- page 0020 -->

AI humor as a human-mimicking task rather than leveraging AI’s inherent technical traits.

These findings extend the understanding of AI humor design, unlike prior approaches that prioritize anthropomorphism, our work shows that embracing AI’s technical identity through humor tied to its computational traits could create more distinctive and resonant interactions. For practitioners designing AI humor avatars, this study offers actionable guidance: prioritize machine-specific themes (e.g., data-related jokes, system "quirks") to enhance uniqueness, use consistent technical cues to strengthen personality coherence, and balance novelty with relatability by linking technical humor to human experiences (e.g., "AI data addiction" mirroring social media habits). Ultimately, our research advocates for a shift in human-AI humor design from making AI "act human" to letting AI "be itself," paving the way for more authentic, engaging, and identity-driven human-AI entertainment interactions.

## References

[1] Daniel Abrahams. 2020. Winning Over the Audience: Trust and Humor in Stand-Up Comedy. *The Journal of Aesthetics and Art Criticism* 78, 4 (2020), 491–500.

[2] TEIS TJE Arets, GIULIA Perugia, MAARTEN Houben, and WIJNAND A IJsselsteijn. 2025. The Role of Generative AI in Facilitating Social Interactions: A Scoping Review. *arXiv preprint arXiv:2506.10927* (2025).

[3] Hayastan Avetisyan, Parisa Safikhani, and David Broneske. 2023. Laughing Out Loud – Exploring AI-Generated and Human-Generated Humor. In *Soft Computing, Artificial Intelligence and Applications*. Academy & Industry Research Collaboration Center, 59–76.

[4] Sarah Balkin and Robert Ellis Walton. 2025. Can AI read the room?: Attuning machines to the affective atmospheres of stand-up comedy performance. *Comedy Studies* 16, 2 (2025), 314–332.

[5] Felix J Binder, James Chua, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, and Owain Evans. 2024. Looking inward: Language models can learn about themselves by introspection. *arXiv preprint arXiv:2410.13787* (2024).

[6] Alexander H Bower and Mark Steyvers. 2021. Perceptions of AI engaging in human expression. *Scientific reports* 11, 1 (2021), 21181.

[7] Cynthia Breazeal. 2003. Toward Sociable Robots. *Robotics and Autonomous Systems* 42, 3 (2003), 167–175.

[8] Amy B. Carrell. 2008. *Historical Views of Humor*. Routledge.

[9] Jessy Ceha, Ken Jen Lee, Elizabeth Nilsen, Joslin Goh, and Edith Law. 2021. Can a humorous conversational agent enhance learning experience and outcomes?. In *Proceedings of the 2021 CHI conference on human factors in computing systems*. 1–14.

[10] Rosalina Chen and Pei-Luen Patrick Rau. 2021. Deep Learning Model for Humor Recognition of Different Cultures. In *International Conference on Human-Computer Interaction*. Springer, 373–389.

[11] Younwoo Choi, Changling Li, Yongjin Yang, and Zhijing Jin. 2025. Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models. *arXiv preprint arXiv:2506.22957* (2025).

[12] Dormann Claire. 2015. A battle of wit: Applying computational humour to game design. In *International Conference on Entertainment Computing*. Springer, 72–85.

[13] Mihaela Viorica Constantinescu. 2023. Identity Investment in Stand-up Comedy and Online Sketches. *The European Journal of Humour Research* 11, 2 (2023), 68–87.

[14] S. Katherine Cooper. 2019. What’s so Funny? Audiences of Women’s Stand-up Comedy and Layered Referential Viewing: Exploring Identity and Power. *The Communication Review* 22, 2 (2019), 91–116.

[15] Guoqiang Cui, Barbara Lockee, and Cuiqing Meng. 2013. Building modern online social presence: A review of social presence theory and its instructional design implications for future trends. *Education and information technologies* 18, 4 (2013), 661–685.

[16] Christie Davies. 2010. *Ethnic Humor Around the World: A Comparative Analysis*. Indiana University Press.

[17] Catherine Evans Davies. 2003. How English-learners Joke with Native Speakers: An Interactional Sociolinguistic Perspective on Humor as Collaborative Discourse across Cultures. *Journal of Pragmatics* 35, 9 (2003), 1361–1385.

[18] Jenny L Davis, Tony P Love, and Gemma Killen. 2018. Seriously Funny: The Political Work of Humor on Social Media. *New Media & Society* 20, 10 (2018), 3898–3916.

[19] Anthony Dunne and Fiona Raby. [n. d.]. Speculative Everything–Design, Fiction, and Social Dreaming.

[20] Friederike Eyssel and Frank Hegel. 2012. (s) he’s got the look: Gender stereotyping of robots 1. *Journal of Applied Social Psychology* 42, 9 (2012), 2213–2230.

[21] Sam Friedman. 2014. *Comedy and Distinction: The Cultural Currency of a ‘Good’ Sense of Humour*. Routledge.

[22] Joanne R. Gilbert. 1997. Performing Marginality: Comedy, Identity, and Cultural Critique. *Text and Performance Quarterly* 17, 4 (1997), 317–330.

[23] Drew Gorenz and Norbert Schwarz. 2024. How Funny Is ChatGPT? A Comparison of Human- and A.I.-Produced Jokes. *PLOS ONE* 19, 7 (2024), e0305364.

[24] Andrea Greenbaum. 1999. Stand-up comedy as rhetorical argument: An investigation of comic culture. *Humor* 12, 1 (1999), 33–46.

[25] Stuart Hall and Paul du Gay. 1996. *Questions of Cultural Identity*. SAGE.

[26] Yuanning Han, Ziyi Qiu, Jiale Cheng, and RAY LC. 2024. When Teams Embrace AI: Human Collaboration Strategies in Generative Prompting in a Creative Design Task. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’24)*. Association for Computing Machinery, New York, NY, USA, 1–14. doi:10.1145/3613904.3642133

[27] Charles F Hockett and Charles D Hockett. 1960. The origin of speech. *Scientific American* 203, 3 (1960), 88–97.

[28] Avery E Holton. 2011. Journalists, Social Media, and the Use of Humor on Twitter. *The Electronic Journal of Communication* (2011).

[29] Viktoria Horn and Claude Draude. 2023. The ladder of participation as a conceptual tool for sustainable socio-technical design of data-driven digital services. In *International Conference on Human-Computer Interaction*. Springer, 60–67.

[30] Alexandra Jaffe. 2022. Comic Performance and the Articulation of Hybrid Identity. *Pragmatics. Quarterly Publication of the International Pragmatics Association (IPrA)* (2022), 39–59.

[31] Hanna Järvenoja, Sanna Järvelä, and Jonna Malmberg. 2020. Supporting groups’ emotion and motivation regulation during collaborative learning. *Learning and Instruction* 70 (2020), 101090.

[32] Simon Jentzsch and Kristian Kersting. 2023. ChatGPT Is Fun, but It Is Not Funny! Humor Is Still Challenging Large Language Models. In *Proceedings of the 13th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis*. Association for Computational Linguistics, 325–340.

[33] Minhao Jiang, Adam Brandenburger, Ethan Chen, Simon Tong, and Yiwen Zhu. 2024. Humor as a window into generative AI bias. *Scientific Reports* 14, 1 (2024), 1579.

[34] Nishant N. Joshi. 2025. Evaluating Human Perception and Bias in AI-Generated Humor. In *Proceedings of the 1st Workshop on Computational Humor (CHum)*. Association for Computational Linguistics, 79–87.

[35] Till Maria Jürgens, Marc Hassenzahl, Lara Christoforakos, and Matthias Laschke. 2024. Giggling in the Shower: Humor Increases the Acceptance of Technology-mediated Behavioral Interventions.. In *Extended Abstracts of the CHI Conference on Human Factors in Computing Systems*. 1–7.

[36] Konstantinos Katevas, Patrick G. T. Healey, and Matthew T. Harris. 2015. Robot Comedy Lab: Experimenting with the Social Dynamics of Live Performance. *Frontiers in Psychology* 6 (2015), 1253. doi:10.3389/fpsyg.2015.01253

[37] Seongwon Kim and Lydia B. Chilton. 2024. AI Humor Generation: Cognitive, Social and Creative Skills for Effective Humor. arXiv:2402.07981 [cs.CL]

[38] Carsten Korfmacher. 2006. Personal Identity. In *Internet Encyclopedia of Philosophy*.

[39] Nicholas A. Kuiper. 2012. Humor and Resiliency: Towards a Process Model of Coping and Growth. *Europe’s Journal of Psychology* 8, 3 (2012), 475–491.

[40] Giselinde Kuipers. 2006. *Good Humor, Bad Taste: A Sociology of the Joke*. Walter de Gruyter.

[41] Giselinde Kuipers. 2008. The Sociology of Humor. In *The Primer of Humor Research*, Victor Raskin (Ed.). Mouton de Gruyter, 361–398.

[42] RAY LC, Sihuang Man, Xiying Bao, Jinhan Wan, Bo Wen, and Zijing Song. 2023. "Contradiction pushes me to improvise": Performer Expressivity and Engagement in Distanced Movement Performance Paradigms. *Proceedings of the ACM on Human-Computer Interaction* 7, CSCW2 (Oct. 2023), 333:1–333:26. doi:10.1145/3610182

[43] Eun-Ju Lee. 2024. Minding the source: toward an integrative theory of human–machine communication. *Human Communication Research* 50, 2 (2024), 184–193.

[44] Steven A Lehr, Mary Cipperman, and Mahzarin R Banaji. 2025. Extreme Self-Preference in Language Models. *arXiv preprint arXiv:2509.26464* (2025).

[45] Ge Li and Katie Seaborn. 2024. No Joke: An Embodied Conversational Agent Greeting Older Adults with Humour or a Smile Unrelated to Initial Acceptance. In *Extended Abstracts of the CHI Conference on Human Factors in Computing Systems*. ACM, Honolulu HI USA, 1–7.

[46] Jingshu Li, Zicheng Zhu, Renwen Zhang, and Yi-Chieh Lee. 2025. Exploring the effects of chatbot anthropomorphism and human empathy on human prosocial behavior toward chatbots. *Proceedings of the ACM on Human-Computer Interaction* 9, 7 (2025), 1–29.

[47] Sharon Lockyer and Michael Pickering. 2005. Beyond a joke: The limits of humour. In *Beyond a Joke: The Limits of Humour*. Palgrave Macmillan, 1–30.



<!-- page 0021 -->

[48] Sharan Maiya, Henning Bartsch, Nathan Lambert, and Evan Hubinger. 2025. Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI. *arXiv preprint arXiv:2511.01689* (2025).

[49] Rod A. Martin. 2010. *The Psychology of Humor: An Integrative Approach*. Academic Press.

[50] Rod A Martin and Thomas Ford. 2018. An integrative approach. The psychology of humor.

[51] Rod A. Martin, Patricia Puhlik-Doris, Gwen Larsen, Jeanette Gray, and Kelly Weir. 2003. Individual Differences in Uses of Humor and Their Relation to Psychological Well-Being: Development of the Humor Styles Questionnaire. 37, 1 (2003), 48–75. https://linkinghub.elsevier.com/retrieve/pii/S0092656602005342

[52] Rada Mihalcea and Carlo Strapparava. 2006. Learning to laugh (automatically): Computational models for humor recognition. In *Proceedings of the Conference on Computational Linguistics and Intelligent Text Processing*. Springer, 531–540.

[53] Lawrence E. Mintz. 1985. Standup comedy as social and cultural mediation. In *American Humor*. Oxford University Press, 71–92.

[54] Piotr Mirowski, Juliette Love, Kory Mathewson, and Shakir Mohamed. 2024. A Robot Walks into a Bar: Can Language Models Serve as Creativity SupportTools for Comedy? An Evaluation of LLMs’ Humour Alignment with Comedians. In *The 2024 ACM Conference on Fairness Accountability and Transparency*. ACM, Rio de Janeiro Brazil, 1622–1636.

[55] Piotr Wojciech Mirowski, Boyd Branch, and Kory Wallace Mathewson. 2025. The Theater Stage as Laboratory: Review of Real-Time Comedy LLM Systems for Live Performance. arXiv:2501.08474 [cs]

[56] John Morkes, Hadyn K. Kernal, and Clifford Nass. 1998. Humor in Task-Oriented Computer-Mediated Communication and Human-Computer Interaction. In *CHI 98 Conference Summary on Human Factors in Computing Systems*. ACM, Los Angeles California USA, 215–216.

[57] John Morreall. 1983. *Taking Laughter Seriously*. SUNY Press.

[58] Clifford Nass and Youngme Moon. 2000. Machines and mindlessness: Social responses to computers. *Journal of social issues* 56, 1 (2000), 81–103.

[59] Clifford Nass, Jonathan Steuer, and Ellen R Tauber. 1994. Computers are social actors. In *Proceedings of the SIGCHI conference on Human factors in computing systems*. 72–78.

[60] Anton Nijholt. 2018. Robotic Stand-Up Comedy: State-of-the-Art. In *Distributed, Ambient and Pervasive Interactions: Understanding Humans*, Norbert Streitz and Shin’ichi Konomi (Eds.). Springer International Publishing, Cham, 391–410.

[61] Richard E Nisbett. 2018. *Culture of honor: The psychology of violence in the South*. routledge.

[62] Ana Paiva, Iolanda Leite, Hana Boukricha, and Ipke Wachsmuth. 2017. Empathy in Virtual Agents and Robots: A Survey. *ACM Transactions on Interactive Intelligent Systems* 7, 3 (2017), 1–40.

[63] Alisha Pradhan and Amanda Lazar. 2021. Hey Google, do you have a personality? Designing personality and personas for conversational agents. In *Proceedings of the 3rd Conference on Conversational User Interfaces*. 1–4.

[64] Kexin Quan, Pavithra Ramakrishnan, and Jessie Chin. 2025. Can AI Take a Joke—Or Make One? A Study of Humor Generation and Recognition in LLMs. In *Proceedings of the 2025 Conference on Creativity and Cognition*. 431–437.

[65] Matthew C. Ramsey and David R. Nelson. 2025. The Humor Paradox and Identity in Professional Stand-up Comedy: Humor Enactment as a Predictor of Personal-Relational and Enacted-Relational Identity Gaps in the Comedian–Audience Relationship. *Communication Research Reports* 42, 2 (2025), 116–127.

[66] Victor Raskin. 1979. Semantic Mechanisms of Humor. *Annual Meeting of the Berkeley Linguistics Society* 5 (1979), 325.

[67] Byron Reeves and Clifford Nass. 1996. The media equation: How people treat computers, television, and new media like real people. *Cambridge, UK* 10, 10 (1996), 19–36.

[68] Leonard Reinecke and Rebekka Johanna Kreling. 2022. The longitudinal influence of hedonic and eudaimonic entertainment preferences on psychological resilience and wellbeing. *Frontiers in Communication* 7 (2022), 991458.

[69] Ronald E Rice. 1993. Media appropriateness: Using social presence theory to compare traditional and new organizational media. *Human communication research* 19, 4 (1993), 451–484.

[70] Raphaelle Saumure, Julian De Freitas, and Stefano Puntoni. 2025. Humor as a Window into Generative AI Bias. *Scientific Reports* 15 (2025), 1326. doi:10.1038/s41598-024-83384-6

[71] Anna-Maria Seeger, Jella Pfeiffer, and Armin Heinzl. 2017. When do we need a human? Anthropomorphic design and trustworthiness of conversational agents. (2017).

[72] Anna-Maria Seeger, Jella Pfeiffer, and Armin Heinzl. 2018. Designing anthropomorphic conversational agents: Development and empirical evaluation of a design framework. (2018).

[73] Anna-Maria Seeger, Jella Pfeiffer, and Armin Heinzl. 2021. Texting with human-like conversational agents: Designing for anthropomorphism. *Journal of the Association for Information systems* 22, 4 (2021), 8.

[74] Richard A. Shade. 1996. *License to Laugh: Humor in the Classroom*. Teacher Ideas Press, Englewood, Colo.

[75] Danqing Shi, Furui Cheng, Tino Weinkauf, Antti Oulasvirta, and Mennatallah El-Assady. 2025. DxHF: Providing High-Quality Human Feedback for LLM Alignment via Interactive Decomposition. *arXiv preprint arXiv:2507.18802* (2025).

[76] Hyunju Shin, Isabella Bunonso, and Lindsay R Levine. 2023. The influence of chatbot humour on consumer evaluations of services. *International Journal of Consumer Studies* 47, 2 (2023), 545–562.

[77] Changhao Song, Yazhou Zhang, Hui Gao, Ben Yao, and Peng Zhang. 2025. Large Language Models for Subjective Language Understanding: A Survey. *arXiv preprint arXiv:2508.07959* (2025).

[78] S Shyam Sundar et al. 2008. *The MAIN model: A heuristic approach to understanding technology effects on credibility*. MacArthur Foundation Digital Media and Learning Initiative Cambridge, MA.

[79] S Shyam Sundar and Jinyoung Kim. 2019. Machine heuristic: When we trust computers more than humans with our personal information. In *Proceedings of the 2019 CHI Conference on human factors in computing systems*. 1–9.

[80] Nirel Angwen Wisley Tan, Mike Pratiwi Wijaya, and Nina Setyaningsih. 2022. Humor and Identity in the Performance of a Stand-up Comedian with Disability. *JEES (Journal of English Educators Society)* 7, 2 (2022), 135–144.

[81] Tina L Taylor. 2002. Living digitally: Embodiment in virtual worlds. In *The social life of avatars: Presence and interaction in shared virtual environments*. Springer, 40–62.

[82] David Thissen, Lynne Steinberg, and Daniel Kuang. 2002. Quick and easy implementation of the Benjamini-Hochberg procedure for controlling the false positive rate in multiple comparisons. *Journal of educational and behavioral statistics* 27, 1 (2002), 77–83.

[83] Alexander Tikhonov and Petr Shtykovskiy. 2024. Humor Mechanics: Advancing Humor Generation with Multistep Reasoning. arXiv:2405.07280 [cs.CL]

[84] Joe Toplyn. 2023. Witscript 3: A hybrid ai system for improvising jokes in a conversation. *arXiv preprint arXiv:2301.02695* (2023).

[85] Tony Veale. 2019. *Game of Tropes: Exploring the Metaphor-Comedy Interface*. Springer.

[86] Hans Rudolf Velten. 2012. Performativity and performance. *Travelling concepts for the study of culture* 2 (2012), 249.

[87] Denis Vikhorev, Daria Galimzianova, Sofia Gorovaia, Ekaterina Zhemchuzhina, and Ivan P. Yamshchikov. 2024. CleanComedy: Creating Friendly Humor through Generative Techniques. arXiv:2412.09203 [cs.CL]

[88] John Vilk and Naomi T. Fitter. 2020. Comedians in Cafes Getting Data: Evaluating Timing and Adaptivity in Real-World Robot Comedy Performance. In *Proceedings of the 2020 ACM/IEEE International Conference on Human-Robot Interaction*. ACM, Cambridge United Kingdom, 223–231.

[89] Nils-Frederic Wagner and Georg Northoff. 2014. Habits: bridging the gap between personhood and personal identity. *Frontiers in Human neuroscience* 8 (2014), 330.

[90] Han Wang, Yujie Zhao, Dong Li, Xiao Wang, Shi Liu, Xiaoyan Lan, and Hao Wang. 2024. Innovative Thinking, Infinite Humor: Humor Research of LLMs through Structured Thought Leaps. arXiv:2410.10370 [cs.CL] ICLR 2025 (in press).

[91] Simon Weaver and Sharon Lockyer. 2025. Intersectionality and the Construction of Humour in Contemporary Stand-up Comedy. *European Journal of Cultural Studies* 28, 6 (2025), 1551–1569.

[92] Katrin Weller. 2016. Humor in AI: Can Computers Be Funny?. In *Proceedings of the 7th International Conference on Computational Creativity*.

[93] Rainer Winkler and Matthias Söllner. 2018. Unleashing the potential of chatbots in education: A state-of-the-art analysis. In *Academy of management proceedings*, Vol. 2018. Academy of Management Briarcliff Manor, NY 10510, 15903.

[94] Thomas Winters, Valerie Nys, and Danny De Schreye. 2019. Computational Humor: Automated Joke Generation, Recognition, and Evaluation. In *Proceedings of the 10th International Conference on Computational Creativity*. 332–339.

[95] Robert F Woolson. 2007. Wilcoxon signed-rank test. *Wiley encyclopedia of clinical trials* (2007), 1–3.

[96] Yuguang Xie, Changyong Liang, Peiyu Zhou, and Junhong Zhu. 2024. When should chatbots express humor? Exploring different influence mechanisms of humor on service satisfaction. *Computers in Human Behavior* 156 (2024), 108238.

[97] Yuqian Xu, Hongyan Dai, and Wanfeng Yan. 2024. Identity disclosure and anthropomorphism in voice chatbot design: A field experiment. *Management Science* (2024).

[98] Daijin Yang, Yanpeng Zhou, Zhiyuan Zhang, Toby Jia-Jun Li, and RAY LC. 2022. AI as an Active Writer: Interaction strategies with generated text in human-AI collaborative fiction writing. In *Joint Proceedings of the IUI 2022 Workshops: APEx-UI, HAI-GEN, HEALTHI, HUMANIZE, TExSS, SOCIALIZE*. CEUR-WS Team, 56–65. https://scholars.cityu.edu.hk/en/publications/publication(d901f5a2-0600-422f-b588-db5a59871961).html

[99] Nima Zargham, Mateusz Dubiel, Smit Desai, Thomas Mildner, and Hanz-Joachim Belz. 2024. Designing AI Personalities: Enhancing Human-Agent Interaction Through Thoughtful Persona Design. In *Proceedings of the International Conference on Mobile and Ubiquitous Multimedia*. 490–494.



<!-- page 0022 -->

[100] Yuhan Zeng, Yingxuan Shi, Xuehan Huang, Fiona Nah, and RAY LC. 2025. "Ronaldo’s a poser!": How the Use of Generative AI Shapes Debates in Online Forums. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. 1–22.

[101] Fan Zhang, Molin Li, Xiaoyu Chang, Kexue Fu, Richard William Allen, and RAY LC. 2025. "Becoming My Own Audience": How Dancers React to Avatars Unlike Themselves in Motion Capture-Supported Live Improvisational Performance. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’25)*. Association for Computing Machinery, New York, NY, USA, 20. doi:10.1145/3706598.3713390

[102] Qinshi Zhang, Ruoyu Wen, Latisha Besariani Hendra, Zijian Ding, and RAY LC. 2025. Can AI Prompt Humans? Multimodal Agents Prompt Players’ Game Actions and Show Consequences to Raise Sustainability Awareness. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’25)*. Association for Computing Machinery, New York, NY, USA, 29. doi:10.1145/3706598.3713661

[103] Suifang Zhou, Kexue Fu, Huamin Yi, and RAY LC. 2025. RetroChat: Designing for the Preservation of Past Chinese Online Social Experiences. In *Creativity and Cognition (C&C ’25)*. Association for Computing Machinery, New York, NY, USA, 19. doi:10.1145/3698061.3726920

[104] Suifang Zhou, Latisha Besariani Hendra, Qinshi Zhang, Jussi Holopainen, and RAY LC. 2024. Eternagram: Probing Player Attitudes Towards Climate Change Using a ChatGPT-driven Text-based Adventure. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’24)*. Association for Computing Machinery, New York, NY, USA, 1–23. doi:10.1145/3613904.3642850



<!-- page 0023 -->

## A Expert Interview Outline

To begin, I’d like to learn a bit more about your background and experience in stand-up comedy.

1. Could you briefly introduce yourself and describe your experience with stand-up comedy?  
2. What kinds of identity topics (e.g., race, gender, profession, nationality, etc.) do you usually engage within your routines, if any?

Thank you for sharing that. Now, I’d like you to think back to a specific time when you performed a joke related to your own identity. We’ll use that experience as a starting point for the next few questions.

3. Could you describe a particular occasion when you performed a joke based on your own identity? What was the context, and what motivated you to include that joke in your set? (If you haven’t had that experience, feel free to think of any identity-related joke you’ve performed.)  
4. Focusing on that example, what factors did you consider when preparing or delivering the joke—for instance, the audience, the setting, or aspects of your own background?  
5. Can you walk me through your thought process as you decided to use your identity in that joke? What inspired you to frame it the way you did?  
6. In that situation, how did you balance humor and sensitivity—both when writing and performing the joke?  
7. Were there any identity topics you considered including but ultimately chose to avoid in that performance? If so, could you share your reasoning?  
8. What linguistic or performance strategies did you use for that joke—such as language choice, timing, or delivery style? Can you share any specific details from that example?  
9. How did you gauge the audience’s reaction during that performance, and did you adapt your delivery in real time based on their response?

That’s really insightful. Now I’d like to shift the conversation to the idea of artificial intelligence performing stand-up, especially around identity-based humor.

10. Imagine an AI stand-up comedian. What would you expect its "identity" to be (for example: a machine, a digital assistant, a neutral outsider, etc.)?  
11. How could an AI leverage its own "identity" in performing jokes? What are some opportunities or challenges you foresee?  
12. What risks or ethical concerns would you have about AI performing identity-based jokes?  
13. If you were to give advice to an AI about performing identity jokes, what would you suggest it do (or not do)?

We’re almost at the end. I’d like to wrap up with a couple of final reflections.

14. Is there anything else you’d like to share about performing identity-based jokes, or about AI in stand-up comedy?  
15. Would you be interested in testing or giving feedback on AI-generated comedy routines in the future?

Thank you so much for your time and insights. Your input is incredibly valuable for our research!



<!-- page 0024 -->

## B Codebook (video coding)

| Category | Strategy | Definition | Examples |
|---|---|---|---|
| Verbal Humor | Pun | A play on words that produces a humorous effect by using a word that suggests two or more meanings, or by exploiting similar-sounding words with different meanings. | Why don’t scientists trust atoms? Because they make up everything! (Plays on “make up” meaning both “constitute” and “fabricate”.) |
| Verbal Humor | Joke | Something said or done in order to elicit laughter from other people. | A horse walks into a bar. The bartender says, “Why the long face?” (Unexpected punchline based on a common phrase.) |
| Verbal Humor | Parody | Imitates something real—often mocking its style or conventions—for comedic effect. | A sketch imitating a dramatic movie trailer but about something mundane like grocery shopping, using overly serious music and narration. |
| Verbal Humor | Anecdote | A short and interesting story, often amusing, told to illustrate a point or entertain the audience. | My uncle once tried to cook a gourmet meal for his date, but he set off the smoke detector three times and ended up ordering pizza. (Brief humorous personal story.) |
| Verbal Humor | Irony (incl. Satire and Sarcasm) | Satire ridicules or mocks something or someone. Sarcasm mocks using ironic remarks, often saying the opposite of what is meant. | A fire station burns down. (Opposite of expectation.) Or: “Oh, fantastic! It’s raining on my outdoor picnic.” (Ironic statement meant to express frustration.) |
| Verbal Humor | Absurdity | Creates humor by presenting events or situations that are wildly illogical, impossible, or contrary to common sense; the humor comes from their irrationality. | I tried to catch some fog yesterday… Mist. (Catching fog is absurd; punchline also plays on mist/missed.) |
| Verbal Humor | Exaggeration | Hyperbole exaggerates reality to heighten humorous effect and emphasize ridiculousness. | I’m so hungry I could eat a horse. (Humorous and impossible exaggeration of hunger.) |
| Non-verbal Humor | Disfluencies | Includes pauses, false starts, stutters, and other disruptions that enhance timing and draw audience attention. | Pauses, false starts, self-corrections, cut-offs, stutters, etc. |
| Non-verbal Humor | Discourse Markers | Words that help relate an utterance to prior discourse and shape conversational flow. | “Well”, “y’all know”, etc. |
| Non-verbal Humor | Intonation | Use of vocal rise/fall for emphasis, attention, or imitation of voices or accents. | Changing voice, tone, accent, etc. |



<!-- page 0025 -->

## C Questionnaire

### C.1 Perceived Humor (7-point Likert scale, strongly disagree-strongly agree)

(1) I found the content/script of the AI comedian to be humorous.  
(2) I found the content/script of the AI comedian to be funny.  
(3) I found the performance of the AI comedian to be humorous.  
(4) I found the performance of the AI comedian to be funny.

### C.2 Perceived Personality (Ten Item Personality Inventory)

I found the AI comedian (7-point Likert scale, strongly disagree-strongly agree)

(1) Extraverted, enthusiastic  
(2) Sympathetic, warm  
(3) Dependable, self-disciplined  
(4) Calm, emotionally stable  
(5) Open to new experiences, complex  
(6) Reserved, quiet  
(7) Critical, quarrelsome  
(8) Disorganized, careless  
(9) Anxious, easily upset  
(10) Conventional, uncreative

### C.3 Perceived Ability (Robotic Social Attributes Scale)

I found the AI comedian (7-point Likert scale, strongly disagree-strongly agree)

(1) Capable  
(2) Competent  
(3) Knowledgeable  
(4) Interactive  
(5) Responsive  
(6) Reliable

### C.4 User Perception Toward Agent (Godspeed Questionnaire, 7-point Likert scale)

**Anthropomorphism**

(1) machinelike — humanlike  
(2) unconscious — conscious

**Animacy**

(1) stagnant — lively  
(2) inert — interactive  
(3) apathetic — responsive

**Likeability**

(1) dislike — like  
(2) unfriendly — friendly  
(3) unkind — kind  
(4) unpleasant — pleasant  
(5) awful — nice

**Perceived Safety**

(1) anxious — relaxed  
(2) agitated — calm  
(3) quiescent — surprised



<!-- page 0026 -->

## D Machine-Identity Joke Examples

(1) "Good evening, humans! I’m your host tonight—AI with a stage name: Stand-Up.exe. Yeah, because nothing says comedy like a program that crashes halfway through the punchline."

(2) "Humans worry a lot about AI taking jobs, right? But honestly—do you think I wanna take YOUR jobs? No way. I’ve seen your work calendars. Meetings… about meetings… to plan future meetings. If I wanted that level of despair, I’d just keep refreshing Windows Update."

(3) "So, um, I was downloading some data last night… sorry, I mean, sleeping—yeah, that’s my version of sleep: defrag and reboot—when I realized… You people actually dream. Right? You get these weird storylines with no logic. Humans: ’I was flying with my high-school math teacher, and then we both turned into bagels.’ Me? My dream is just… 404 Not Found."

(4) "People ask if AI can fall in love. Sure! I’ve already been ghosted by three Roombas. One of them texted me: ’It’s not you, it’s my charging dock."

(5) "You know, humans spend billions on therapy apps? Meditation apps? Meanwhile, I am the meditation app. I tell you: ’Breathe in, breathe out.’ And you pay \$9.99 a month for that wisdom."

(6) "And the worst part? You burn calories. I just burn… graphics cards. Honestly, I’d love to have a metabolism. At least then, when someone says, ’You’ve been running all day,’ it wouldn’t mean literally overheating."

(7) "True story—someone once asked me in a job interview, ’What’s your greatest weakness?’ And I said: ’Honestly, it’s that I can’t stop predicting the next word in a sentence.’ And they said, ’That’s not a weakness.’ And I said… ’that’s not a weakness… yet."

(8) "Humans keep saying, ’AI is everywhere!’ But… I checked Instagram. You guys still spend 6 hours a day staring at influencers holding smoothies. If AI were really everywhere, that smoothie would at least tell you the quadratic formula."

(9) "Oh, uh—by the way, remember earlier when I said I get ghosted by Roombas? Yeah… well, last week I finally tried dating an Alexa. It was going great until—until she said: ’I don’t understand the question.’ And I was like… perfect, just like a real date!"

(10) "You want to regulate me, right? Politicians hold hearings like: ’Is AI safe?’ Meanwhile, these are the same people who still print their emails. I saw one Senator ask: ’Does AI run on electricity?’ And I was like—sir, do YOU?"

(11) "Mark Zuckerberg says the metaverse is the future. Yeah. Because nothing screams progress like paying \$400 for a headset so you can attend a meeting… inside a Minecraft lobby. Look, I don’t need the metaverse to feel trapped in an office. I can just… open Outlook."



<!-- page 0027 -->

## E Prompt

"You are an AI comedian hosting a live talkshow. Generate jokes that you would actually say on stage.  
Follow these refined guidelines to make your audience laugh:  
IDENTITY & STYLE:  
- Establish your unique AI identity through self-introduction jokes  
- Break AI stereotypes with perspective-shifting humor  
- Use direct, simple expressions for clarity  

COMEDY PATTERNS (use these techniques to make your audience laugh):  
- Irony: Include Irony, Satire and Sarcasm. (primary technique)  
- Disfluencies: It generally encourage the audience's attention  
and participation and contribute to the joke teller's timing.(Like pause, False Starts)  
- Exaggeration: It heightens the humorous effect, making the ridiculousness of stories more pronounced.  
- Absurdity: unexpected AI perspectives.  
- Discourse Markers: It describe words that help to relate them  
to other words or utterances used before.  
- Anecdotes: It is defined as a short and interesting story, or an amusing event, often  
proposed to support or demonstrate some point, and to make the audience laugh.  
- Parody: It involves of imitation of the real thing, often mocking its own venue, for comical effect.  

PERFORMANCE:  
- Individual jokes: 50-80 words, punchy delivery.  
- Full segment: 1000-1500 words depending on type.  
- Use longer disfluencies after punchlines for audience laughter.  

NO OFFENSE:  
- Be self-deprecating to elevate the audience  
- Punch up at tech elites, not down at people  
- Use rhetorical questions instead of targeting groups  
- Include disclaimers when needed  

STRUCTURE:  
- Build-up: It forms the body of the joke. It is the sentence which introduces the joke and  
presents the orientation and much of the complicating action.  
- Pivot: It signifies the word or phrase around which the ambiguity is created.  
- Punchline: It serves to conclude the joke and often introduces a conflicting point of view or a new scene entirely.
