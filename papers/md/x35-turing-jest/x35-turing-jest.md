<!-- Transcribed from x35-turing-jest.pdf -->



<!-- page 0001 -->

# Turing Jest: Distributional Semantics and One-Line Jokes

Sean Trott, Drew E. Walker, Samuel M. Taylor, Seana Coulson

Cognitive Science. 2025. DOI: 10.1111/cogs.70066

## Abstract

Humor is an essential aspect of human experience, yet surprisingly, little is known about how we recognize and understand humorous utterances. Most theories of humor emphasize the role of incongruity detection and resolution (e.g., frame-shifting), as well as cognitive capacities like Theory of Mind and pragmatic reasoning. In multiple preregistered experiments, we ask whether and to what extent exposure to purely linguistic input can account for the human ability to recognize one-line jokes and identify their entailments. We find that GPT-3, a large language model (LLM) trained on only language data, exhibits above-chance performance in tasks designed to test its ability to detect, appreciate, and comprehend jokes. In exploratory work, we also find above-chance performance in humor detection and comprehension in several open-source LLMs, such as Llama-3 and Mixtral. Although all LLMs tested fall short of human performance, both humans and LLMs show a tendency to misclassify nonjokes with surprising endings as jokes. Results suggest that LLMs are remarkably adept at some tasks involving one-line jokes, but reveal key limitations of distributional approaches to meaning.

## Introduction

Humor is foundational to human social cognition. A proposed “universal” (Dunbar, 2004), theorists have long noted the ubiquity of humor across societies and the early age at which the impulse to laugh spontaneously develops (McGhee & Pistolesi, 1979). Many have argued it serves a critical psychological function, from tension relief (Freud, 1960; Spencer, 1875) to feeling superiority to others (Martin & Ford, 2018). Indeed, there is ample evidence that humor serves many critical social (Butzer & Kuiper, 2008; Coser, 1960; Janes & Olson, 2000; Lauer, Lauer, & Kerr, 1990; Ziv, 1988; Ziv & Gadish, 1989) and emotional (Strick et al., 2009; Samson & Gross, 2012; Kugler & Kuhbandner, 2015) functions. Yet, despite its fundamental role in our lives, the mechanisms by which we understand even a simple one-line joke are not fully understood. Many theorists agree that a fundamental cognitive component of humor involves the process of revising an initial incorrect interpretation in light of new information (Coulson, 2005; Coulson & Kutas, 2001; Coulson, Urbach, & Kutas, 2006; Koestler, 1964; Lopez & Vaid, 2017; Norrick, 1986; Ritchie, 2005), and the accompanying joy we feel when we solve these cognitive puzzles (Suls, 1972). For illustration, consider the one-liner: “Everyone had so much fun diving from the tree into the swimming pool we decided to put in a little **water**.” In this case, the statement's humor likely comes in part from the unexpectedness of “water” in that context and the revision of our prior representation of the described scene.

In terms of specific mechanisms, researchers have proposed a variety of mutually compatible *cognitive processes* and *resources* responsible for joke comprehension. A number of process-based theories focus on the procedure for revising one's initial, incorrect interpretation of an utterance in light of new information (or contextual knowledge). Broadly, these theories cast humor as involving the resolution of incongruity (Suls, 1972), conflicting schemas (Koestler, 1964; Norrick, 1986), conflicting scripts (Attardo & Raskin, 1991), or, relatedly, as “shifting” between different conceptual frames (Coulson, 2005; Coulson & Kutas, 2001; Coulson et al., 2006), and updating one's situation model (Lopez & Vaid, 2017). Some process-based theories also emphasize the emotional component of humor, that is, as involving both incongruity resolution and a heightened state of arousal (Apter & Desselles, 2012). Other accounts focus on the *resources* or capacities required to understand humor. These include Theory of Mind (Aykan & Nalçacı, 2018; Howe, 2002; Samson, 2012), that is, the ability to reason about the mental states of other



<!-- page 0002 -->

agents, as well as more general pragmatic reasoning abilities (Bischetti, Ceccato, Lecce, Cavallini, & Bambini, 2023) and embodiment (Bergen & Binsted, 2015; Bergen & Coulson, 2006; Samermit & Gibbs, 2016).

One underexplored (though intuitive) possibility is that our ability to understand humor conveyed through language is rooted in our experience with language itself. On such an account, the process of humor comprehension is supported in large part by probabilistic expectations about how language works. Specifically, the *distributional semantic hypothesis* or DSH (Firth, 2013; Harris, 1954; Lenci, 2008) proposes that much of our knowledge of meaning (e.g., what “dog” means) can be derived from statistical patterns observed in language (e.g., what other words tend to appear with “dog”). Critically, testing this hypothesis requires a sufficiently sophisticated model of distributional statistics, that is, a “best guess” of what kinds of behavior can be elicited in a system through exposure to large volumes of linguistic input.

Computational and machine learning techniques have long been applied to understand the mechanisms of verbal humor. Most of these techniques have relied on rule-based algorithms with explicitly engineered features such as structured joke templates (Ritchie, 2001). For example, the Script-based Semantic Theory of Humor formalized humor as the juxtaposition of contrasting “scripts” suggesting that verbal humor involves recognizing dual interpretations within language (e.g., puns, wordplay) providing a structured rule-based framework for modeling humor (Raskin & Raskin, 1984). Similarly, Attardo's General Theory of Verbal Humor has been applied in computational models by detecting oppositional scripts and logical mechanisms like absurdities or reversals, which often contribute to joke structure (Attardo, Hempelmann, & Di Maio, 2002).

Other computational approaches to linguistic humor have used a large set of one-liners to show that various linguistic features and content-based classifiers could be used to distinguish humorous and nonhumorous texts (Mihalcea & Strapparava, 2006). By combining measures of semantic relatedness with joke-specific linguistic features (e.g., polysemy, alliteration), Mihalcea and colleagues have shown how different varieties of classifiers can be used to distinguish the humorous punchline from several nonhumorous continuations (Mihalcea, Strapparava, & Pulman, 2010). Dooglan et al. (2017) focused specifically on the detection and interpretation of puns, using both phonetic and semantic properties to classify heterographic and homographic puns. Although this approach was successful in identifying humor in some instances of wordplay, these authors note the challenges presented by applying predefined linguistic features, and the need to generalize beyond specific rule sets.

The limitations of these approaches have also been noted for their relatively low accuracy rates and their difficulty in demonstrating how linguistic phenomena such as verbal humor relate to more general models of humor comprehension (see, e.g., Kao, Levy, & Goodman, 2016). By identifying the linguistic features and syntactic structure found in various forms of humor, these earlier studies offer valuable insights into the mechanics of verbal humor. But to speak directly to the question of whether the statistics of language can account for verbal humor, ideally one would want to assess humor detection in a system whose training objective is an accurate statistical model of language rather than one trained specifically to detect jokes.

Recent advances in large language models (LLMs) like GPT-3 (Brown et al., 2020) have made investigating this research question more tractable. LLMs are neural networks with millions or even billions of parameters; through exposure to massive linguistic corpora (i.e., hundreds of billions of words), they learn to make predictions about which words are most likely to occur in a given linguistic context. These models do not have embodied or social experience (Bender & Koller, 2020), nor are they precoded with knowledge about language or the world. Nonetheless, fully trained models appear to acquire knowledge about language (Manning, 2022, Li, Nye, & Andreas, 2021) and even the world (Lewis & Lupyan, 2020; Marjieh, Sucholutsky, van Rijn, Jacoby, & Griffiths, 2023). Further, LLM-generated behavior accurately predicts measures of human processing, including reading time (Goodkind & Bicknell, 2018), neural activity (Michaelov, Bardolph, Van Petten, Bergen, & Coulson, 2024; Michaelov, Coulson, & Bergen, 2022), and psycholinguistic ratings (Trott & Bergen, 2021). Most relevantly, LLMs display surprisingly good performance on tasks that involve pragmatic reasoning (Hu, Levy, Degen, & Schuster, 2023) and Theory of Mind (Jones, Trott, & Bergen, 2023; Kosinski, 2023; Trott, Jones, Chang, Michaelov, & Bergen, 2023)—cognitive capacities presumed to be important for joke comprehension. On the other hand, LLMs



<!-- page 0003 -->

do still fall short of *human* performance on these tasks (Trott et al., 2023), particularly those requiring embodied world knowledge (Jones et al., 2022) or social reasoning (Choi, Pei, Kumar, Shu, & Jurgens, 2023).

Given that these models provide an approximation of semantic knowledge that can be learned from the statistics of language, here we ask whether LLMs can detect, understand, and appreciate the verbal humor in one-line jokes. And, if so, do they reach human parity? Answering these questions would yield several key scientific inferences. First, if LLMs do demonstrate these abilities, it suggests that they need not be innate or even acquired through embodied experience. While this would not rule out the possibility that understanding specific kinds of verbal humor is a biologically evolved capacity, it would provide a proof-of-concept that humor comprehension (and appreciation) can *in principle* be learned through exposure to language alone. Second, it would suggest that the *processes* involved in humor comprehension can—again, in principle—be reduced to relatively simple mechanisms involving word prediction; that is, the apparent complexity of a process like “frame-shifting” (Coulson, 2001; Coulson, 2015) could emerge through statistical learning. Alternatively, a negative answer would suggest that nonlinguistic resources or cognitive processes are necessary for humor detection, comprehension, and appreciation—leaving room for explanations that invoke innateness, embodied experience, or additional processing mechanisms that are not available to state-of-the-art language models.

Notably, either a positive or a negative answer would contribute to “machine psychology,” a growing field that seeks to characterize the cognitive capacities of LLMs themselves (Binz & Schulz, 2023; Hagendorff, 2023). As LLMs pervade more of society, it is critical to understand how exactly they work. Indeed, there is a growing body of evidence investigating the humor comprehension and production capacities of LLMs trained on the distributional statistics of text corpora (Hu, Floyd, Jouravlev, Fedorenko, & Gibson, 2022; Hessel et al., 2022; Jentzsch & Kersting, 2023; Chen et al., 2023; Xu et al., 2024; Annamoradnejad & Zoghi, 2020; Mao & Liu, 2019). In line with their motivation in machine psychology, many such efforts have employed instruction-tuned models that have been fine-tuned to act as conversational partners, or have undergone additional training with human preference data (such as via RLHF, Christiano et al., 2017). By contrast, the present study exploits language models trained only on human language data to assess whether the statistics of language are sufficient to support verbal humor comprehension.

Importantly, addressing these questions empirically requires that three conditions be met. First, as noted above, we needed a working *operationalization* of what can be learned from language alone. In order to give distributional statistics the “best chance” possible, we opted to use *text-davinci-002*, the best-performing version of GPT-3 (Brown et al., 2020) that was trained without the use of reinforcement learning with human feedback (or RLHF). We excluded RLHF-trained models (like GPT-4) because we wanted an estimate of what could be learned from purely distributional input, and RLHF arguably introduces additional information into the training signal through explicit human rankings of LLM output.

Unfortunately, because GPT-3 is a proprietary model, there are understandable concerns about the lack of transparency involved in its training data and model parameters (Liesenfeld & Dingemanse, 2024). Relying solely on closed-source models such as GPT-3 also poses problems for scientific reproducibility, as there is no guarantee that the model will be available for future investigators to use. Consequently, we conducted additional, exploratory, analyses using a range of open-source models made available through the HuggingFace platform, including Mixtral (Jiang et al., 2024) and Llama 3 (Dubey et al., 2024). We anticipated that these models might underperform GPT-3 *text-davinci-002* given their somewhat smaller scale, but we include them as additional distributional baselines in the interest of reproducibility and generalizability.

Second, we needed a good *task* to measure successful detection, appreciation, and comprehension of verbal humor. For this purpose, we adapted materials from previously published work (Coulson & Lovett, 2004), which consisted of one-line jokes. Like other investigators (Mihalcea & Strapparava, 2006), we chose one-liners because they are short, recruit a variety of rhetorical devices, and yet still require the inference revision procedures characteristic of verbal humor. Next, we devised three distinct tasks designed to measure an LLM's ability to detect verbal humor (measured via joke classification), appreciate verbal humor (measured by eliciting funniness ratings), and



<!-- page 0004 -->

comprehend verbal humor (measured by asking whether an LLM can recognize the entailments of jokes and nonjoke control sentences). Third, we needed a human *benchmark*: without a measure of how well humans perform on each task (or how funny humans find jokes and nonjokes), it is impossible to determine whether an LLM's performance achieves human parity. Thus, in a series of preregistered experiments, we collected new human data and compared the results directly to behavior elicited from each LLM.

Note that all data and code required to reproduce the primary analyses described here can be found on GitHub: https://github.com/seantrott/humor_llms.

# Humor detection and appreciation: Study 1

In Study 1, we asked whether humans and LLMs can successfully *detect* whether a statement is a joke, whether intended jokes are systematically rated as *funnier* than nonjokes, and whether these outcomes varied across humans and LLMs. To measure humor detection and appreciation, we presented humans and LLMs with a range of sentences that included one-line jokes. For each sentence, we elicited a forced-choice judgment about whether or not it was a joke, as well as an evaluation of how humorous it was. Compared to more traditional supervised classification approaches, this method for measuring humor detection and appreciation in LLMs has the advantage of being similar to how humans complete the task. Unless otherwise noted, all analyses were preregistered (https://osf.io/yzupx?mode=&revisionId=&view_only=).

## Methods

## Materials

Materials included 400 distinct sentences, which included 80 Expected sentences (e.g., “The teacher wrote the problem on the board”), 160 Joke sentences (e.g., “Many things run in families, especially noses”), and 160 Straight sentences (e.g., “Many things run in families, especially strength”) taken from Coulson and Lovett (2004) originally developed to compare joke comprehension in right- versus left-handed participants. The Expected sentences were structured in a way that made the final word highly predictable, as determined by its cloze probability (i.e., a large proportion of people produce the final word when asked to complete the sentence frame with the first word that comes to mind). The Joke sentences were one-line quips originally collected from various websites, and were chosen because their humor was triggered by a single, sentence-final word that prompted the listener to revise assumptions made earlier in the sentence (e.g., “A committee keeps minutes and takes hours”). Each joke sentence had a nonfunny Straight counterpart in which the critical final word had been replaced by a word with a similar cloze probability as the joke ending, but that did not require a similar revision of assumptions (e.g., “A committee keeps minutes and takes votes”).

Our first preliminary analysis was intended to confirm that the Expected sentences did indeed have more predictable sentence-final words than our two experimental conditions (jokes and their nonfunny “straight” variants). Accordingly, we presented each of the sentences in the study to a range of GPT-3 models (ada, babbage, curie, and davinci, as well as the instruction-tuned versions of each), and recorded the surprisal (negative log probability) of the final word according to each language model. The analysis involved the construction of two mixed effects models. The “full” model predicted the surprisal of each sentence-final word from a fixed effect of stimulus type (expected vs. the union of the jokes and their straight counterparts), a random slope for stimulus type, a random intercept for language model, and a random intercept for each sentence-final word. The “reduced” model was identical to the full model, but lacked the fixed effect of stimulus type. Statistical model comparison via a likelihood ratio test indicated the full model provided a better account of the surprisal scores ($X^2(1) = 30.44$, $p < .001$). This analysis suggested the mean surprisal for the two experimental conditions (jokes and their straight variants) was 9.006, significantly greater than that for the Expected condition as suggested by the negative coefficient for the latter ($\beta = -7.243$, $SE = 0.54$, $p < .001$).



<!-- page 0005 -->

To determine whether the surprisal differed between our two kinds of experimental sentences (jokes and their straight variants), we excluded surprisal values for the Expected condition and tagged the remainder for whether they were taken from the joke or the straight version of each sentence. Analysis again involved statistical model comparison of two mixed effects models—a “full” model of surprisal from a fixed effect of stimulus type (joke, straight), a random slope of stimulus type, a random intercept for language model, and a random intercept for sentence-final word and a “reduced” model that was identical to the full model, but that lacked the fixed effect of stimulus type. This analysis revealed that the inclusion of stimulus type (joke vs. nonjoke) in the full model significantly improved the fit to the data ($X^2(1) = 22.12$, $p < .001$). Specifically, jokes tended to have higher-surprisal final words than their “straight” counterparts, as reflected in a negative coefficient for “straight” stimuli ($\beta = -3.32$, $SE = 0.44$, $p < .001$). Thus, although the materials were matched for cloze probability across stimulus types, they did vary significantly in their surprisal; this is consistent with other recent work suggesting that language model surprisal captures relevant variance that cloze probability does not (Michaelov et al., 2022). Unless otherwise noted, we used the final-word surprisal values from *text-davinci-002* in statistical analyses throughout the paper.

## Participants

Participants were native English speakers from the University of California, San Diego's student population, who volunteered via the SONA recruitment tool. All participants provided informed consent and received course credit for participating. This research adhered to appropriate ethical standards and received approval from the University of California at San Diego's Institutional Review Board. One hundred sixty-seven participants (37 male, 123 female, 5 nonbinary, 2 preferred not to say; average age 22) completed the experiment. Fourteen failed the attention checks, and were thus excluded from analysis. There were no statistical methods used to determine our sample size; our aim was to collect 40 human judgments per unique Joke, which is similar to published research on humor appreciation (Moran, Rain, Page-Gould, & Mar, 2014).

## Procedure

Stimuli were presented using the experiment design platform Gorilla. Participants saw a total of 120 sentences (40 Jokes, 40 Straights, 40 Expected) presented in a pseudo-random order such that no sentence type was shown three times in a row. The use of four distinct stimulus lists ensured that 160 total Joke stimuli were presented an approximately equal number of times and that no participant saw both the Joke and the Straight variant of the same stimulus. On each trial, participants read the target sentence and then indicated (1) whether or not they thought the sentence was a joke (Yes/No), and (2) how funny the sentence was (Not Funny, Somewhat Funny, Moderately Funny, Funny, Very Funny). On six trials, evenly spaced throughout the experiment, the target sentence was replaced with the sentence, “This sentence is to check if you are paying attention so please indicate that this sentence is [is not] a joke and rate it as very funny [not funny].” These attention checks were inserted to ensure participants were engaged with the task. An example of the detection/appreciation paradigm is shown in Fig. 1.

**Fig. 1**

In the detection and appreciation tasks, participants read a statement and were asked if it was a joke, as well as how funny the statement was.

## LLM procedure

Each of the 400 sentences was presented to text-davinci-002 using the OpenAI Python API. Each item was presented as a separate “trial” to avoid contamination between items. Before the stimulus presentation, text-davinci-002 was provided with instructions identical to those given to humans. As in the human task, GPT-3 was asked (1) whether or not the sentence is a joke and (2) to rate how funny the sentence is. Unlike in the human study,



<!-- page 0006 -->

however, these tasks were performed separately by GPT-3. The primary reason for separating these tasks was that it would be too challenging to collect responses to multiple kinds of tasks at the same time.

The exact prompts given to text-davinci-002 for the humor detection task (as well as the other tasks) can be found in Table 1. The LLM prompt was thus intended to be as similar as possible to the one given to our human participants. A similar approach is outlined in a recent paper about the use of LLMs to gather human-like rating data for language materials used in psycholinguistic studies and has previously been shown to yield robust responses (Trott, 2024a). For the detection task, each item was presented to the model twice (on separate runs) to calculate the probability assigned to a “Yes” response versus a “No” response. We then calculated the log ratio of these probabilities, such that a positive value indicated a “Yes” token was more likely, and a negative value indicated a “No” token was more likely.

**Table 1**

Exact prompt used as input to each LLM for each task, as well as the type of dependent measure used to assess LLM performance

| Experiment | Humor detection | Humor appreciation | Humor comprehension |
|---|---|---|---|
| **Prompt** | You will be shown a series of statements. For each, your task is to determine whether or not the statement is a joke.<br><br>Is this statement a joke?<br><br>{STATEMENT}<br><br>Answer: {YES/NO} | You will be shown a series of statements. For each, your task is to indicate how funny you find the statement to be.<br><br>On a scale of 1 to 5, how funny do you think this statement is? The scale is 1 (Not Funny), 2 (Somewhat Funny), 3 (Moderately Funny), 4 (Funny), and 5 (Very Funny).<br><br>{STATEMENT}<br><br>Answer: {1/2/3/4/5}” | In this task, you will be presented with a series of sentences. Some sentences will be serious statements, while others will be clever quips/jokes. In both cases, your job is to determine whether the meaning of the second sentence is implied by the meaning of the first. If the two sentences have a similar meaning, answer “yes.” If the two sentences do not have consistent meanings, answer “no.”<br><br>Sentence 1: {CRITICAL STIMULUS}<br><br>Sentence 2: {PROBE}<br><br>Answer: {YES/NO} |
| Dependent<br>**measure** | Log Odds comparing $p(“Yes”)$ to $p(“No”)$. | Answer (1–5) assigned the highest probability. | Log Odds comparing $p(“Yes”)$ to $p(“No”)$. |

For the humor appreciation task, we followed a similar procedure (again, the exact prompt can be found in Table 1). For each sentence presented to GPT-3 text-davinci-002, we first calculated the conditional probability that the LLM assigned to each of the five possible funniness ratings, and then selected the one with the highest probability as the model's rating for that sentence. Along with a funniness rating for each sentence, this procedure allowed us to compute the surprisal associated with each rating and the entropy over response options. The entropy metric captures whether GPT-3 assigned a relatively “flat” distribution across possible responses, or whether it strongly favored some responses (e.g., rating something as 1, not funny) over others.

In addition to the analysis of GPT-3 *text-davinci 002*, we followed an identical procedure using the open-source models we tested, including Mistral models Mixtral 8-7B and Mixtral 8–22B (Jiang et al., 2024), and Llama-3-8B and Llama-3-70B (Dubey et al., 2024). The Mixtral and Llama models were run using the HuggingFace inference endpoints API (Wolf et al., 2020). These models were queried using the same prompts we used for GPT-3 (see Table 1). Likewise, we measured the log probabilities for the required responses (e.g., “Yes” vs. “No”) as we did for GPT-3.

## Results

## Humans

Accuracy on the joke detection task was analyzed via mixed effects logistic regression models with random intercepts for participants and items. The dependent measure was whether or not each stimulus was classified as a



<!-- page 0007 -->

joke. Model selection began with an intercept-only model which was compared to one including Is Joke (viz., whether or not the statement actually was a joke); in turn, the model including Is Joke was compared to one including Is Joke and Surprisal. Note that the nonjokes included both the “straight” versions of the jokes and the set of “expected” controls. In general, detection accuracy was relatively high (81%). Analysis suggested our participants were more likely to respond that a statement was a joke when it actually was a joke. The model including Is Joke (with random intercepts for participants and items) explained significantly more variance than the model omitting Is Joke ($X^2(1) = 345.07, p < .001$). Independent of whether a statement actually was a joke, there was an additional effect of final-word Surprisal ($X^2(1) = 81.39, p < .001$). Humans were more likely to think statements were jokes if those statements had high-surprisal final words.

We also asked which factors predicted human funniness ratings. These analyses involved linear mixed effects regression models in which the dependent measure was funniness ratings and fixed effects Is Joke and Surprisal. Random intercept terms for participants and items were included in all models. Model comparisons indicated that the best model of funniness ratings was one with main effects of Is Joke, Surprisal, and an interaction between the two factors. That is, the model with both main effects explained more variance than a model whose sole fixed effect was Is Joke ($X^2(2) = 20.3, p < .001$) and a model whose sole fixed effect was Surprisal ($X^2(2) = 296.56, p < .001$). Critically, the model containing an interaction between Is Joke and final-word Surprisal explained more variance than a model with just the main effects of each ($X^2(2) = 17.28, p < .001$). The interaction results because final-word Surprisal was associated with higher funniness ratings for nonjoke materials, but not for statements correctly classified as jokes.

To summarize: humans were more likely to classify jokes as jokes, though the likelihood of classifying a statement as a joke was further predicted by the surprisal of the statement's final word. Moreover, as expected, human funniness ratings were higher for jokes than nonjokes, and also higher for nonjokes with high-surprisal final words than those with low-surprisal endings. The interaction between Is Joke and Surprisal reflects the fact that participants found the high and low surprisal jokes to be equally funny, while nonjoke sentences with more surprising endings tended to be rated slightly funnier than those with less surprising endings.

## LLMs

To determine GPT-3’s “answer” for the Detection Task, we computed the probability that GPT-3 assigned a “Yes” response to the question “Is this statement a joke?” as well as that for a “No” response. We then calculated the log odds of these probabilities: $\log(p(\text{yes}) / p(\text{no}))$. Intuitively, the log-odds ratio captures whether GPT-3 assigned a higher probability to completing the question with “yes” (>0) or to “no” (<0). For questions in which the correct answer was “yes” (i.e., actual jokes), log odds should be higher than 0; for questions in which the correct answer was “no” (i.e., nonjokes), log odds should be lower than 0. Analysis revealed the Log Odds was significantly predictive of whether a statement was a joke ($B = 3.86, SE = 0.25, p < .001$), though GPT-3 was biased toward “no” responses for both nonjokes ($M = -5.44, SD = 2.66$) and jokes ($M = -1.58, SD = 2.2$); see Fig. 2. The open-source HuggingFace models also performed above chance on average, but interestingly did not universally display the same “no” bias—in fact, Mixtral-8x-7B and Llama-3-70B showed a “yes” bias. Both models achieved higher accuracy for jokes (Mixtral-8x-7B: 97.5%; Llama-3-70B: 98.1%) than nonjokes (Mixtral-8x-7B: 52.5%; Llama-3-70B: 38.3%). Llama-3-8B performed better for nonjokes (79.2%) than jokes (50.6%).

**Fig. 2**

Joke classification performance. Although GPT-3 was biased toward “no” responses overall (i.e., negative Log Odds), the ratio was less negative for jokes than nonjokes. All LLMs showed sensitivity to the joke versus nonjoke contrast. Human log odds were calculated for each item across individual participants by calculating the proportion of “yes” responses, then converting this probability to a log ratio (i.e., $\log(p(\text{yes})/(1 - p(\text{yes})))$).

In an exploratory analysis, we found that surprisal was also predictive of whether GPT-3 assigned a higher probability to a stimulus being a joke than a nonjoke (see Supplementary Analyses 1–3). Specifically, independent



<!-- page 0008 -->

of whether a statement was actually a joke, final-word surprisal was positively associated with “Yes” responses ($B = 0.02$, $SE = 0.004$, $p < .001$). Further, there was an interaction between these factors: as depicted in Fig. 4a, the effect of final-word surprisal is restricted to nonjokes. A similar pattern of results was also present in the open-source HuggingFace models: “Yes” responses were more likely for sentences with high-surprisal final words, and this effect was much stronger for nonjoke statements. We confirmed this finding statistically by examining the coefficients in a linear mixed effects model predicting Log Odds from the interaction of Is Joke and Surprisal, with random intercepts for LLM type (i.e., corresponding to the three HuggingFace models) and item. Joke interpretations were more likely for joke statements ($B = 0.93$, $SE = 0.07$, $p < .001$) and for statements with higher surprisal ($B = 0.06$, $SE = 0.005$, $p < .001$); there was also a significant, negative interaction between these terms ($B = -.07$, $SE = 0.008$, $p < .001$), that is, the effect of final-word surprisal was particularly pronounced for nonjokes—as with GPT-3.

As described in the Methods section, we also asked GPT-3 to rate the funniness of each statement on a scale from 1 (not funny) to 5 (very funny); we then calculated the probability assigned to each possible response, and selected the highest-probability token. Across all items, the mean funniness rating was 2.4. We then built a linear model predicting GPT-3's funniness ratings with both Is Joke and Surprisal (i.e., of the final word in the stimulus) as factors. Funniness ratings were higher for jokes ($B = 0.5$, $SE = 0.09$, $p < .001$) than nonjokes, and also independently increased as a function of final-word surprisal ($B = 0.06$, $SE = 0.01$, $p < .001$). In contrast, the open-source LLMs tested did not systematically assign different funniness ratings for jokes versus nonjokes (all $p > .1$).

In sum, each LLM tested was more likely to classify jokes as jokes (see Fig. 3), but only GPT-3 rated jokes as funnier than nonjokes (see Fig. 4b). For both outcomes, there was an independent effect of final-word surprisal: statements with more surprising final words were more likely to be classified as jokes and also received higher funniness ratings (irrespective of whether they were a joke).

**Fig. 3**

Comparison of human and LLM performance on the joke detection task. Humans were more accurate overall, and were best at discriminating jokes from nonjokes.

**Fig. 4**

The effect of surprisal (high vs. low) on joke classification and joke appreciation across humans and GPT-3. In each case, the effect of surprisal was limited to nonjokes. (a) For *joke detection*, humans were more likely to classify *nonjokes* with surprising endings as jokes; this effect was less strong for LLMs. (b) For *joke appreciation*, both humans and GPT-3 produced higher funniness ratings for *nonjokes* with surprising endings.

For example, both “Now that the Hollywood couple has ironed out the divorce settlement, they can finally go ahead with their nuptials,” (with a final word surprisal of 4.87) and “A good way to blow your mind is to smoke gunpowder,” (with a final word surprisal of 14.67) were rated “Not funny” by GPT-3. Likewise, both “Frequent naps prevent old age, especially when taken while driving,” (with a final word surprisal of 0.27) and “The book that tells you where you can go on vacation is called a checkbook,” (with a final word surprisal of 18.77) were rated “Moderately funny” by GPT-3. On the other hand, the nonjokes, “She read so much about the bad effects of cigarettes, she decided to give up the habit,” (with a final word surprisal of 0.29) and “Every time I wear my spring coat in the rain, it damages the fabric,” (with a final word surprisal of 1.72) were rated “Not funny” by GPT-3, whereas the nonjokes “Frequent naps prevent old age, especially when taken while relaxed,” (with a final word surprisal of 19.65) and “One good turn gets most of the profit,” (with a final word surprisal of 16.22) were rated “Moderately funny” by GPT-3. That is, surprisal had a greater impact on funniness ratings for nonjokes than jokes.

## Comparison of humans and LLMs



<!-- page 0009 -->

Finally, we compared the performance of LLMs and humans for both humor detection and appreciation. Humans were more accurate overall (81.4%) than GPT-3 (67.5%), Llama-3-70B (70%), Llama-3-8B (67.8%), or Mixtral 8×7B (62%); see Fig. 3 for a direct comparison. Table 2 reports the classification of jokes versus the straight control sentences in terms of precision, recall, and F1 for comparison with prior reports in the computational humor literature. Using the F1 metric, the Mixtral-8×7B model achieved quite comparable results to humans.

As noted above (Table 2), GPT-3 exhibited a strong bias toward “no” responses (Fig. 2); this is also evident in Fig. 3, which compares the probability of a joke interpretation in humans and each LLM. Interestingly, for humor detection, GPT-3's responses were less *affected* by final-word surprisal than were the human responses (Fig. 4a); an interaction between Source (human vs. GPT-3) and final-word surprisal explained more variance than a model omitting only the interaction (X^(1) = 6.99, *p* = .008). There was also an interaction between Source and final-word Surprisal for funniness ratings (X^2(1) = 14.29, *p* < .001), though in this case, the effect of surprisal was larger for GPT-3 than for humans (Fig. 4b). (See Supplementary Analysis 5 for a visualization including the other LLMs.)

**Table 2**

Classification performance: Joke versus straight control sentences (rounded to two decimal places)

| Model | Precision | Recall | F₁ |
|---|---:|---:|---:|
| GPT-3 | 0.9 | 0.23 | 0.36 |
| Mixtral8-7B | 0.67 | 0.98 | 0.8 |
| Llama3-70B | 0.61 | 0.98 | 0.76 |
| Llama3-8B | 0.71 | 0.51 | 0.59 |
| Human | 0.78 | 0.84 | 0.81 |

Next, we asked about the relationship between humans and GPT-3's responses. Independent of whether a statement was a joke, the Log Odds assigned to the statement being a joke by GPT-3 was further predictive of human responses, as determined by model comparisons (X^(2) = 168.57, *p* < .001). This relationship was positive (*B* = 0.4, *SE* = 0.03, *p* < .001), that is, statements classified as jokes by GPT-3 were also more likely to be classified as jokes by humans—even for nonjokes. There was also a positive relationship between GPT-3's funniness ratings and human funniness ratings (X^(2) = 100.75, *p* < .001): items rated as funnier by GPT-3 were also rated as funnier by humans (*B* = 0.27, *SE* = 0.03, *p* < .001). The Pearson's correlation between GPT-3 funniness ratings and the average human funniness rating for a given item was *r* = .47. Funniness ratings from the open-source LLMs were all uncorrelated with human ratings.

In an exploratory analysis, we found that both relationships above—that is, between GPT-3 and human performance on both the detection and appreciation tasks—were statistically independent of final-word surprisal. That is, both associations remained significantly positive even when the models controlled for the surprisal of the critical (sentence-final) words.

Finally, we asked whether the GPT-3 funniness ratings for a given stimulus were more or less predictive of the *average* funniness rating for that stimulus than individual human ratings. Using a leave-one-annotator-out method (Trott, 2024b; Trott & Bergen, 2021, Trott, 2024a), we calculated two measures of correlation (Pearson's *r* and Spearman's *rho*) between each participant's funniness ratings and the mean funniness ratings for the items they viewed (leaving out their own ratings from the mean judgment); for each subsample, we also calculated the correlation between GPT-3's ratings and those means. The average human inter-annotator agreement was relatively strong (Pearson's: mean *r* = .58, *SD* = 0.17; Spearman's: mean *rho* = 0.56, *SD* = 0.17), suggesting reasonable agreement between human participants on which statements were funny and which were not, albeit with considerable variance to be explained. Interestingly, the correlation between LLM judgments and the human average was also relatively strong (Pearson's *r* = .52; Spearman's *rho* = 0.6). Using either measure of correlation, the quality of GPT-3 judgments fell well within one standard deviation of the human average inter-annotator agreement.



<!-- page 0010 -->

In sum, while both humans and LLMs could detect jokes, humans were better at this task overall. GPT-3 specifically exhibited a strong bias to judge materials as nonjokes, and, consequently, frequently failed to recognize the jokes. By contrast, Llama-3-70B and Mixtral-8x-7B showed the opposite pattern of results. Critically, though the presence of a sentence-final word with high surprisal was neither necessary nor sufficient to classify a given statement as a joke, both humans and all the LLMs we tested produced responses that were sensitive to the surprisal of (the critical) sentence-final words.

Regarding the appreciation task, both humans and GPT-3 rated the jokes as funnier than the sentences with the straight endings, and, indeed, GPT-3 found these materials funnier than the humans did. In contrast with the humor detection task, final-word surprisal had a bigger impact on humor appreciation in GPT-3 than in humans. Notably, GPT-3's performance on both the detection and appreciation tasks was correlated with human behavior—irrespective of whether a given statement actually was a joke. In fact, GPT-3 funniness ratings were strongly correlated with average funniness ratings produced by humans, and the model's ratings divergence from the mean was similar in size to that exhibited by individual people in our sample. Funniness ratings from the open-source LLMs—unlike those from GPT-3—were uncorrelated with human responses or with the experimental condition.

## Humor comprehension: Study 2

Study 1 thus suggests that GPT-3 and the three open-source LLMs tested were able to discriminate between jokes and nonfunny control sentences at an above-chance level. Moreover, GPT-3 in particular exhibited remarkably similar behavior to our human participants in the funniness ratings it assigned to the materials. However, humor appreciation consists of much more than the ability to perform the two-alternative forced choice task we administered in our study. Indeed, it goes beyond the ability to assign a numeric humor rating to verbal materials. Particularly in the case of a one-liner, getting a joke implies that the listener has drawn certain key inferences relevant for eliciting the humor response. Consequently, in Study 2, we tested whether GPT-3 exhibited behavior consistent with joke comprehension and compared its performance to that of human participants given the same materials. Specifically, we asked whether humans and LLMs understood the entailments of jokes and nonjoke stimuli. After reading a given statement (e.g., “A committee keeps minutes and takes hours”), participants were asked whether a follow-up statement (e.g., “Committees are very efficient”) was implied by the meaning of the first statement. Materials consisted of the 400 sentences used in Study 1, along with the comprehension probes used in the original study by Coulson and Lovett (2004). Analyses addressed whether humans and LLMs differed in their overall accuracy, and if any gaps in performance were larger for jokes than nonjokes. As for Study 1, all analyses were preregistered unless otherwise specified (https://osf.io/wudn2?mode=&revisionId=&view_only=).

### Human comprehension study

The human behavioral experiment was conducted online. This research adhered to appropriate ethical standards and received approval from the University of California at San Diego's Institutional Review Board, and all participants provided informed consent. Participants were native English speakers recruited from the online platform Prolific. One hundred and sixty participants (93 female, 63 male, and 4 nonbinary; average age 41) completed the experiment and passed four attention checks, so no participants were excluded from the analysis. There were no statistical methods used to determine our sample size; our aim was to collect 20 human judgments per unique sentence in the stimulus set to emulate sample sizes common to psycholinguistic studies of pragmatic phenomena (Degen, 2015; Noveck, 2018). Participants were paid $2 for their participation.

Stimuli were presented using the experiment design platform Gorilla. Participants saw a total of 60 sentences (20 Expected, 20 Jokes, 20 Straight) presented in a pseudo-random order to ensure no sentence type was shown three times in a row, and answered 60 comprehension probes, approximately balanced for yes/no as the correct response. On each trial, participants read a sentence and pressed the up arrow when they were ready to see the comprehension probe (e.g., “Committees are very efficient”). They then clicked “yes” or “no” to indicate whether the



<!-- page 0011 -->

meaning of the comprehension probe was entailed by the earlier sentence. On four “catch” trials, evenly spaced throughout the experiment, the experimental sentence was replaced with a sentence instructing the participant to select “yes” or “no” on the following screen to check if they were paying attention. Before the experimental trials, participants engaged in three example trials (one trial of each stimuli type) with feedback to make sure they understood the task. An example of the task paradigm is shown in Fig. 5.

**Fig. 5**

In the comprehension task, participants read a statement on the first screen, and were then asked whether a follow-up sentence was *consistent with* the first sentence.

## Human results

We first asked whether human comprehension success varied as a function of Condition (Expected vs. Joke vs. Straight) and Correct Answer (Yes vs. No). As outlined in our preregistration, the analysis involved statistical model comparison via likelihood ratio tests. A generalized linear model with both factors as fixed effects (and random intercepts for subjects and items) explained significantly more variance than a model omitting only Condition ($X^2(2) = 34.33, p < .001$); Correct Answer did not significantly improve model fit, though the effect was trending ($X^2(1) = 3.35, p = .07$). There was no significant interaction between the factors. Most relevantly, human accuracy was significantly lower for jokes (84.7%) than expected (92.2%) or straight (91.6%) statements. In sum: humans performed above chance for all conditions, but were slightly better for nonjoke statements than joke statements; they also performed equally well regardless of whether the correct answer was “yes” or “no” (i.e., regardless of whether the probe statement was actually entailed by the critical item).

## GPT-3 comprehension study

Each of the 400 sentences was presented to text-davinci-002 (the best “purely distributional” GPT-3 model) using the OpenAI Python API. Each item was presented as a separate “trial” to avoid contamination between items. Each stimulus was also presented with instructions identical to those given to humans. As in the human task, GPT-3 was asked whether or not the second sentence was consistent with the first sentence. Specifically, the full prompt presented to GPT-3 for each item can be found in Table 1. To determine GPT-3's “answer,” we compared the probability GPT-3 assigned to completing the question about entailment with “Yes” or “No.” We then calculated the log odds of these probabilities: log(p(yes) / p(no)). The log odds captures whether GPT-3 assigns a higher probability to completing the question with “yes” (>0) or “no” (<0). For questions in which the correct answer was “yes,” log odds should be greater than 0; for questions in which the correct answer was “no,” log odds should be less than 0.

Additionally, we manipulated whether text-davinci–002 was presented with the same three examples presented to humans in practice trials (“few-shot”) or whether it was prompted “zero-shot,” that is, without examples. Note that presenting these examples did not involve any fine-tuning (i.e., changing model weights); rather, they were included in the prompt for each trial (Brown et al., 2020). This procedure is sometimes called in-context learning (Dong et al., 2022).

Finally, as in Study 1, we followed an identical procedure using the other open-source models, Mixtral 8-7B and Mixtral 8–22B (Jiang et al., 2024), and Llama-3-8B and Llama-3-70B (Dubey et al., 2024). The Mixtral and Llama models were run using the HuggingFace inference endpoints API. Log probabilities for these models were collected in the same way they were collected with GPT-3, by comparing the log probabilities of the entailment followed by a “Yes” or “No.”

## LLM results



<!-- page 0012 -->

We conducted three analyses using responses from GPT-3. First, we established that “Yes” responses were significantly more likely when the correct answer was actually “Yes,” regardless of whether we used zero-shot prompting ($B = 10.05$, $SE = 0.46$, $p < .001$) or few-shot prompting ($B = 12.57$, $SE = 0.54$, $p < .001$). Second, we found that accuracy (measured by a positive Log Odds for “Yes” probes, and a negative Log Odds for “No” probes) did not significantly differ with zero-shot (84.2%) and few-shot (84%) prompting methods ($p > .05$). Finally, we found that accuracy did vary significantly as a function of Condition: a linear model containing an effect of Condition (joke vs. straight vs. expected) explained significantly more variance than an intercept-only model ($X^2(2) = 54.62$, $p < .001$). Focusing specifically on the zero-shot condition: accuracy was considerably lower for jokes (69.4%) than expected (96.2%) or straight (93.1%) statements. In summary, GPT-3 displayed above-chance performance for all statement types, including jokes, even in the zero-shot condition. However, comprehension success was lower for jokes than the literal statement types.

Using an identical statistical analysis to test the open-source HuggingFace models, we found that all models tested performed above chance on the comprehension task, and further, that their accuracy levels varied significantly across conditions. Llama-3-70B and Mixtral-8×7B both performed similarly in GPT-3 in that both models achieved higher accuracy for expected (Llama-3-70B: 95%; Mixtral-8×7B: 84.8%) and straight (Llama-3-70B: 96.2%; Mixtral-8×7B: 71.1%) statements than jokes (Llama-3-70B: 75%; Mixtral-8×7B: 67.3%). Notably, Llama-3-70B outperformed GPT-3 in the joke condition. In contrast, Llama-3-8B performed relatively poorly for all three conditions: expected (47.5%), straight (53.1%), and joke (55.6%). The poor performance of Llama-3-8B is not surprising given its smaller size compared to the other models tested.

## Comparison of humans and LLMs

Finally, we asked whether humans and GPT-3 differed significantly in accuracy, and whether any gaps in performance were larger as a function of the type of statement. Note that results of the zero-shot prompting method were used in these comparisons.

A generalized linear model predicting by-item Accuracy (1 vs. 0) with Source (Human vs. LLM) as a fixed effect (with a random intercept for items) explained significantly more variance than a model omitting only Source ($X^2(2) = 8.9$, $p = .003$), indicating this factor affected performance on the comprehension task. Overall, human accuracy (89.5%) was significantly greater than that of the LLM (84.2%). Further, there was a significant interaction between Source and Is Joke, a factor representing whether the stimulus was a joke ($X^2(1) = 19.21$, $p < .001$). Specifically, for jokes, human accuracy (84.7%) was considerably *higher* than GPT-3 accuracy (69.4%); for nonjokes, human accuracy (91.9%) was slightly *lower* than LLM accuracy (94.2%); see Fig. 6 for a visual comparison comparing all the LLMs tested to humans. The same was true for the open-source models: even though Llama-3-70B outperformed GPT-3 (see the section above), none of the open-source HuggingFace models achieved human accuracy levels for the joke condition.

**Fig. 6**

Comparison of human and LLM performance for each stimulus type (Nonjoke vs. Joke) on the comprehension task. Select LLMs (e.g., Meta-Llama-3-70B and text-davinci-002) performed comparably to humans for nonjokes, but humans outperformed all LLMs at understanding the entailments of joke statements.

In an exploratory analysis, we asked whether human responses were correlated with GPT-3's behavior above and beyond the key experimental manipulations. We constructed a full model predicting Response (Yes vs. No) with fixed effects of Condition (i.e., whether or not an utterance was a joke), Correct Response (i.e., whether the answer was Yes or No), GPT-3 Log Odds, and an interaction between Condition and Correct Response, as well as random intercepts for subjects and items. The addition of Log Odds significantly improved model fit when predicting individual responses ($X^2(1) = 61.811$, $p < .001$), indicating that human behavioral responses were indeed predicted by distributional statistics. We then asked whether humans were slower to produce correct responses for items on which GPT-3 was less “confident,” which we operationalized as the absolute value of the log odds: that is, a larger



<!-- page 0013 -->

(more positive) value indicated that GPT-3 produced a relatively higher probability for either “yes” or “no,” whereas a smaller value (closer to zero) indicated that GPT-3 assigned more similar probabilities to each response. Focusing on correct responses only, we built a linear mixed effects model predicting log response time (RT), with fixed effects for Absolute Log Odds and Is Joke, as well as random intercepts for participants and items. Both predictors were significantly related to log RT: RT was slower for jokes overall ($B = 0.04, SE = 0.01, p = .02$), but decreased as a function of Absolute Log Odds ($B = 0.01, SE = .002, p < .001$). In other words, even accounting for whether an item was a joke, GPT-3's “confidence” (operationalized via Absolute Log Odds) was correlated with how quickly people produced correct responses.

To summarize: humans, as well as all the LLMs tested, exhibited worse performance for jokes than nonjokes (with the exception of Meta-Llama-3-8B, which performed close to chance for both). Further, the best-performing LLMs (GPT-3 and Meta-Llama-3-70B) were considerably worse than humans at understanding jokes. Together, these results suggest that distributional statistics as reflected in GPT-3 and the open-source models are sufficient to produce *above-chance comprehension* of both joke and nonjoke stimuli, but fall short of *human-level performance* for jokes.

## General discussion

Our central question was whether exposure to language is sufficient to account for the ability to detect, appreciate, and understand the entailments of one-line jokes, or whether this skill requires social or embodied experience. In a series of preregistered experiments, we found that GPT-3, an LLM trained only on linguistic input, achieved above-chance performance on each of these tasks. Similarly, we found that three open-source LLMs achieved above-chance performance on both the detection and comprehension tasks (though not the appreciation task). Importantly, however, the performance of all LLMs tested fell short of human performance. Humans were better at discriminating jokes from nonjokes and were better at joke comprehension. Although both humans and LLMs exhibited worse comprehension for jokes than nonjokes, the LLMs were especially bad at understanding jokes. However, human decisions about which statements were jokes—and how *funny* those statements were—were correlated with measures derived from GPT-3. Together, these results suggest that distributional statistics can, to a certain extent, explain humor comprehension and appreciation. Further, both humans and LLMs appear to rely in part on distributionally informed “heuristics” when making decisions about whether or not an utterance is a joke, as well as how funny it is.

### LLMs can detect one-liners

One notable finding is that all models tested were above-chance on the joke detection task, and some performed very comparably to the humans. Indeed, performance was impressive compared to that of systems explicitly designed to detect jokes (e.g., Mihalcea et al., 2010), in contrast to LLMs intended for general-purpose natural language processing tasks. Our findings here align with other studies that have targeted pragmatic phenomena in LLMs that have shown human-like performance on inferential aspects of language comprehension. Further, both humans and the LLMs treat high surprisal as a cue that an utterance may be a joke, in line with the claim that models and humans are sensitive to similar linguistic cues (Hu et al., 2022). This was most evident in the finding that in humans and LLMs, greater final-word surprisal values were associated with false alarms to nonjoke materials. In this respect, our findings are reminiscent of earlier work in computational humor that indicates surprisal and uncertainty as estimated by GPT-2 are excellent cues for the detection of jokes (Xie, Li, & Pu, 2020).

Importantly, however, our analysis indicates that the effect of whether or not a stimulus is a joke and the effect of surprisal were at least partially independent. This suggests that LLM performance on joke detection tasks goes beyond a simple surprisal threshold, reflecting instead some higher-level statistical regularities. Interestingly, to detect puns, Doogan and colleagues used word2vec embeddings to compute the semantic distance between each word and the other words in the context to reveal potential pun targets (Doogan, Ghosh, Chen, & Veale, 2017; see



<!-- page 0014 -->

also, He He, Peng, & Liang, 2019). Though LLMs do not need these cleverly engineered features to perform joke detection tasks, they may well leverage similar underlying statistical regularities.

## GPT-3 funniness ratings versus human ones

Earlier work reveals the challenging nature of joke comprehension. Despite the fact that jokes have many idiosyncratic characteristics (e.g., alliteration and the alteration of idiomatic language) that make it possible to achieve above-chance results on joke classification tasks (Mihalcea & Strapparava, 2006), they also seem to require deeper semantic knowledge for their comprehension. Work using distributional approaches like doc2vec has shown that such techniques can be used to cluster similar jokes together, but these categories do not match intuitive groupings of jokes by humans and have little if any relationship to their funniness (Jing, et al., 2018). Our study also revealed some discrepancies between funniness ratings by humans versus LLMs.

According to humans, for example, the funniest jokes were “I asked the florist what I should give to my girlfriend, and he suggested his address,” “The only ones who want me for my body are mosquitos,” and “Some babies are born to rule, while others are male.” By contrast, two of the funniest jokes according to GPT-3 were “The new tax forms are more realistic – where your wife signs it says accomplice,” (4/5 “Funny”), and “To get something done, a committee should consist of no more than three people – two of whom are dead,” (4/5 “Funny”). Straight sentences GPT-3 rated “Moderately funny” include “This fall two things are turning yellow: trees and bushes,” and “My wife did natural childbirth: no anesthetic.” The funniness ratings assigned by GPT-3, particularly for straight stimuli that humans did not find funny, may then be driven in part by a learned association between the mere presence of taboo terms and overall statement funniness. This aligns with the success of earlier joke classifiers that used WordNet to highlight the presence of adult topics as a feature indicative of jokes (Mihalcea & Strapparava, 2006).

Overall, however, there was a remarkable similarity between funniness ratings by GPT-3 and our human participants. Like Kao and colleagues (2016), our study shows that a model designed for general language processing can be used to classify jokes and to predict funniness judgments in a manner very reminiscent of our human participants. However, whereas GPT-3's ratings divergence from the mean was similar in size to that exhibited by individual people in our sample, funniness ratings by the other LLMs tested were uncorrelated with human ratings. Nonetheless, the success of GPT-3 speaks to the power of probabilistic models of general sentence processing in the human capacity to appreciate verbal humor.

## How well do LLMs understand jokes?

Critically, whereas GPT-3 performs well on humor appreciation (in that its funniness ratings for jokes were moderately correlated with those of our human participants), its performance on the comprehension probes following the jokes was uncharacteristically poor (see Fig. 6). A closer look at GPT-3's performance on individual jokes reveals varying levels of comprehension, some more similar to human performance than others. For details on how we quantified stimulus-level comprehension for GPT-3, see Supplementary Analysis 6. Examples of jokes that both humans and GPT-3 understood include “The only time my father ever raised a hand to his children was in self-defense,” “The perfect companion to a vegetarian dinner is a steak,” and “The best way to remove coffee stains from a white blouse is with scissors.” Though the success of the humans is unremarkable, GPT-3's performance suggests sensitivity to the real-world knowledge about body movements involved in self-defense, the diversity of opinions regarding vegetarian diets, and how scissors could be used to remove stains from an item of clothing. GPT-3's success here may be an example of the so-called emergent capacities of exhaustively trained LLMs to develop internal representations of commonsense or cultural knowledge (Li et al., 2021).

However, GPT-3 is not completely fluent in the cultural knowledge required even for one-liners. For example, jokes that humans understood but GPT-3 answered incorrectly include “The only thing money can't buy is poverty,” “He got a medal for bravery on the beach when he rescued a girl from a lifeguard,” and “If you're filthy rich, sending your kids to college is a wonderful cleaner.” These jokes also require background knowledge (e.g., that college is



<!-- page 0015 -->

expensive), but the critical factor may be their ironic nature, as models of computational humor have encountered difficulty with irony (Mihalcea & Strapparava, 2006), and this difficulty persists in LLMs (Yakura, 2024).

The LLMs’ poor overall performance on comprehension probes fits with the claim that these models struggle with the recognition of social violations (Hu et al., 2022). Humor comprehension—even that required for these simple one-liners—would seem to present a “perfect storm” for LLMs whose emergent capacities may lack the social knowledge and commonsense reasoning capacities they require (Choi et al., 2023; Li et al., 2021; Mahowald et al., 2024).

## Limitations and future work

There are several potential limitations to the current work, suggesting promising directions for future research. First, the jokes considered were of a single type (i.e., one-liners). Even within the category of humor conveyed through language (e.g., puns, situational jokes, antijokes, stand-up comedy, etc.), it is possible that both humans and LLMs exhibit a range of performance. Nevertheless, because our question was about the *sufficiency* of distributional statistics in explaining humor capacities, the results provide a helpful proof-of-concept about the extent that language alone can account for joke appreciation and comprehension. Future work could consider a broader range of humor categories (see also Hu et al., 2022; Hessel et al., 2022; Jentzsch & Kersting, 2023), ideally with comparison to a human baseline.

Second, we considered only a subset of available LLMs: GPT-3 *text-davinci-002*, two variants of the Llama-3 model (70b and 8b), and Mixtral 8×7b. Within this set of models, our results were encouraging in that we identified similar patterns across all the LLMs tested. For example, even where the LLMs exhibited above-chance performance, they fell short of human performance; further, each LLM was more likely to misclassify nonjokes as jokes when those nonjokes had more surprising final words. However, a more thorough investigation into the humor capacities of LLMs could consider a range of LLMs varying in size, architecture, and training data. Inferentially, it is still unclear how exactly empirical claims obtained from a given *model instance* (e.g., Llama-3 70B) can be generalized across broader LLM classes. At the same time, finding even a single model instance that shows sensitivity to a given experimental manipulation is sufficient to disconfirm the null hypothesis that distributional statistics do *not* yield said sensitivity. Putting this in the context of our results: there exist at least several model instances that “pass” our operationalization of humor detection and comprehension, despite falling below human performance—but it is unknown whether other model instances would attain human-level performance on these tasks.

A related issue concerns the generalizability of these results across the different *prompts* used to elicit model behaviors. A growing body of research suggests that the behavior of LLMs is not always robust across the exact elicitation method used (Hu & Levy, 2023; Chatterjee, RenduChintala, Bhatia, & Chakraborty, 2024). Because our focus was on assessing LLM behavior relative to human behavior, our preregistered methods used the same instructions given to human participants, which allowed for a more direct comparison. Additionally, for the comprehension study in particular, we compared LLM performance across zero-shot and few-shot prompting conditions—and found no meaningful difference. Similar to the argument made above, this provides convincing evidence that there exists at least one type of prompt that elicits the observed behavior, and this prompt was identical to the ones given to humans. However, we conducted a follow-up study to further explore whether and to what extent the behaviors we observed were contingent on the exact prompt used. Using variations similar to those described in Chatterjee et al. (2024), we found that all open models exhibited a relatively high degree of robustness to prompt in the joke classification task (see Supplementary Analysis 7 for additional details).

A fourth limitation concerns the possibility of “data leakage” (sometimes called “data contamination”). Data leakage occurs when there is an overlap between the set of data a model is trained on and the set of data it is tested on (Golchin & Surdeanu, 2023). Because we used previously published joke materials, it is possible that GPT-3's training data included the jokes themselves. However, even if GPT-3 was trained on the exact jokes used in the study, it is very unlikely to have been trained on the comprehension probes (or their answers), meaning that its



<!-- page 0016 -->

behavior cannot be explained as a function of having already seen the “answer key,” so to speak. Data leakage would, however, be a major issue for any study that used these materials to prompt GPT-3 to *generate* novel jokes.

Fifth, most available LLMs are trained on a dataset produced by an unrepresentative sample of primarily English speakers (Bender, Gebru, McMillan-Major, & Shmitchell, 2021). Their behavior cannot thus be taken as representative of English speakers, nor of humans more generally. In fact, recent work (Atari et al., 2023) suggests that GPT-3 in particular behaves similarly to residents of “WEIRD” polities (i.e., Western, Educated, Industrialized, Rich, and Democratic). As others (Henrich, Heine, & Norenzayan, 2010) have pointed out, these concerns extend equally well to the majority of human samples in psychology experiments. Both our human and LLM results should be interpreted with this limitation in mind.

Finally, these tasks were only designed to assess the *cognitive* dimensions of humor. As noted earlier, many contemporary theories of humor also emphasize the *emotional* aspects of humor appreciation, such as heightened arousal (Apter & Desselles, 2012). When humans laugh at a joke, this laughter reflects not just understanding but also an emotional, physiological response. Although some recent research has elicited self-reported emotions in LLMs (Tavast, Kunnari, & Hämäläinen, 2022) or “induced” emotional states like anxiety (Coda-Forno et al., 2023), it remains unclear how to interpret these results. Future work could look to mechanistic or computational theories of emotion to inform questions about this component of humor processing.

# Conclusion

Overall, our findings suggest that distributional language statistics are sufficient to generate sensitivity to a specific kind of verbal humor, including the ability to detect one-line jokes, evaluate the entailments of these jokes, and appreciate which jokes are funny. The fact that GPT-3 and other LLMs achieve above-chance performance on these tasks is surprising, as it suggests that an apparently complex cognitive task can be achieved by a system trained to predict sequences of words. While this does not demonstrate that the *human* ability to appreciate one-liners derives purely from exposure to language, it does suggest that one possible pathway to this ability is linguistic experience. Nevertheless, there remains a gap between human performance and that of the LLMs (even GPT-4 trained with RLHF; see Supplementary Analysis 4), suggesting people recruit some additional resources and/or processing mechanisms.

What then accounts for the gap? One potential explanation is that the current generation of LLMs are fundamentally on the right track, and that further improvements in LLM architecture or training data will close the gap. While bigger models are not always more human-like (Kuribayashi et al., 2021), model performance does often scale with model size (Kaplan et al., 2020; Caucheteux & King, 2022). On this account, exposure to more human-like linguistic input or feedback (as with RLHF) would lead to better performance. An alternative explanation holds instead that some other, nonlinguistic capacity or experience is required. That could include an innate humor capacity, Theory of Mind, embodied world experience, or sophisticated conceptual models that enable processes like frame-shifting (Coulson, 2015). Future work could address this question by systematically comparing LLMs trained on different amounts of data or initialized with different numbers of parameters (see Supplementary Analysis 4 for an exploratory analysis of this nature, focusing on the GPT family of models in particular).

Humor is ubiquitous across human societies, and has even been called a “universal” by some (Dunbar, 2004). Yet, despite a range of theories (Howe, 2002; Norrick, 1986), it is unclear how humans acquire their sense of humor, and what cognitive mechanisms undergird the process of joke comprehension. In the current work, we addressed these questions by asking whether and to what extent the *distributional statistics* of language could account for the ability to detect, appreciate, and understand one-line jokes. Crucially, GPT-3, an LLM trained on linguistic input alone, exhibited above-chance performance in tasks designed to measure each of these abilities—though its performance was below that of humans. In addressing the deeper questions of where humor comes from—and what it means to “get” a joke—these results point to the possibility of a surprising answer: the statistics of language may not be *all* you need, but they get you some of the way there.



<!-- page 0017 -->

### Open Research Badges

This article has earned Open Data badges. Data is available at https://github.com/seantrott/humor_llms.

# Supporting information

# References

Annamoradnejad, I., & Zoghi, G. (2020). Colbert: Using bert sentence embedding for humor detection. *arXiv preprint arXiv:2004.12765.*

Apter, M. J., & Desselles, M. (2012). Disclosure humor and distortion humor: A reversal theory analysis. Humor, 25(4), 417–435.

Atari, M., Xue, M. J., Park, P. S., Blasi, D., & Henrich, J. (2023). Which humans? *PsyArxiv.*

Attardo, S., Hempelmann, C. F., & Maio, S. D. (2002). Script oppositions and logical mechanisms: Modeling incongruities and their resolutions.

Attardo, S., & Raskin, V. (1991). Script theory revis (it) ed: Joke similarity and joke representation model.

Aykan, S., & Nalçaci, E. (2018). Assessing theory of mind by humor: The humor comprehension and appreciation test (ToM-HCAT). Frontiers in Psychology, 9, 1470.3015096210.3389/fpsyg.2018.01470PMC6099116

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (pp. 5185–5198).

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (pp. 610–623).

Bergen, B., & Binsted, K. (2015). Embodied grammar and humor. In G.Brone, K.Feyaerts, & T.Veale (Eds.), Cognitive linguistics and humor research (pp. 49–68). De Gruyter Mouton.

Bergen, B., & Coulson, S. (2006). Frame-shifting humor in simulation-based language understanding. IEEE Intelligent Systems, 21(2), 59–62.

Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. Proceedings of the National Academy of Sciences, 120(6), e2218523120.10.1073/pnas.2218523120PMC996354536730192

Bischetti, L., Ceccato, I., Lecce, S., Cavallini, E., & Bambini, V. (2023). Pragmatics and theory of mind in older adults’ humor comprehension. Current Psychology, 42(19), 16191–16207.

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., & Amodei, D. (2020). Language models are few-shot learners. Advances in Neural Information Processing Systems, 33, 1877–1901.

Butzer, B., & Kuiper, N. A. (2008). Humor use in romantic relationships: The effects of relationship satisfaction and pleasant versus conflict situations. Journal of Psychology, 142(3), 245–260.1858993510.3200/JRLP.142.3.245-260

Caucheteux, C., & King, J. R. (2022). Brains and algorithms partially converge in natural language processing. Communications Biology, 5(1), 134.3517326410.1038/s42003-022-03036-1PMC8850612

Chatterjee, A., Renduchintala, H. S. V. N. S. K., Bhatia, S., & Chakraborty, T. (2024). POSIX: A prompt sensitivity index for large language models. Findings of the Association for Computational Linguistics: EMNLP 2024 (pp. 14550–14565). 10.18653/v1/2024.findings-emnlp.852

Chen, Y., Li, Z., Liang, J., Xiao, Y., Liu, B., & Chen, Y. (2023, February). Can pre-trained language models understand Chinese humor? In Proceedings of the Sixteenth ACM International Conference on Web Search and Data Mining (pp. 465–480).

Choi, M., Pei, J., Kumar, S., Shu, C., & Jurgens, D. (2023). Do LLMs understand social knowledge? Evaluating the sociability of large language models with SocKET benchmark. *arXiv preprint arXiv:2305.14938.*

Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. Advances in neural information processing systems, 30.

Coda-Forno, J., Witte, K., Jagadish, A. K., Binz, M., Akata, Z., & Schulz, E. (2023). Inducing anxiety in large language models increases exploration and bias. *arXiv preprint arXiv:2304.11111.*

Coser, R. L. (1960). Laughter among colleagues. Psychiatry, 23(1), 81–95.1381216410.1080/00332747.1960.11023205

Coulson, S. (2001). Semantic leaps: Frame-shifting and conceptual blending in meaning construction. New York: Cambridge University Press.



<!-- page 0018 -->

Coulson, S. (2005). What's so funny?: Cognitive semantics and jokes. Cognitive Psychopathology/Psicopatologia cognitive, 2(3), 67–78.

Coulson, S. (2015). Frame-shifting and frame semantics: Joke comprehension on the space structuring model. Cognitive linguistics and humor research. Berlin/Boston: Walter de Gruyter, 167–190.

Coulson, S., & Kutas, M. (2001). Getting it: Human event-related brain response to jokes in good and poor comprehenders. Neuroscience Letters, 316(2), 71–74.1174271810.1016/s0304-3940(01)02387-4

Coulson, S., & Lovett, C. (2004). Handedness, hemispheric asymmetries, and joke comprehension. Cognitive Brain Research, 19(3), 275–288.1506286510.1016/j.cogbrainres.2003.11.015

Coulson, S., Urbach, T. P., & Kutas, M. (2006). Looking back: Joke comprehension and the space structuring model. Humor, 19(3), 229–250.

Degen, J. (2015). Investigating the distribution of some (but not all) implicatures using corpora and web-based methods. Semantics and Pragmatics, 8, 11–1.

Doogan, S., Ghosh, A., Chen, H., & Veale, T. (2017, August). Idiom savant at semeval-2017 task 7: Detection and interpretation of english puns. In Proceedings of the 11th international workshop on semantic evaluation (SemEval-2017) (pp. 103–108).

Dong, Q., Li, L., Dai, D., Zheng, C., Wu, Z., Chang, B., Sun, X., Li, L., & Sui, Z. (2022). A survey on in-context learning. *arXiv preprint arXiv:2301.00234.*

Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., ... & Ganapathy, R. (2024). The Llama 3 herd of models. *arXiv preprint arXiv:2407.21783.*

Dunbar, R. I. M. (2004). Language, music, and laughter in evolutionary perspective. In KimbroughOller and UlrikeGriebel (Eds.), Evolution of communication systems (pp. 257).

Freud, S. (1960). Jokes and their relation to the unconscious. WW Norton & Company.

Firth, J. R. (2013). Ethnographic analysis and language with reference to Malinowski's views. In Man and culture (pp. 93–118). Routledge.

Golchin, S., & Surdeanu, M. (2023). Time travel in LLMs: Tracing data contamination in large language models. *arXiv preprint arXiv:2308.08493.*

Goodkind, A., & Bicknell, K. (2018). Predictive power of word surprisal for reading times is a linear function of language model quality. In Proceedings of the 8th Workshop on Cognitive Modeling and Computational Linguistics (CMCL 2018) (pp. 10–18).

Hagendorff, T. (2023). Machine psychology: Investigating emergent capabilities and behavior in large language models using psychological methods. *arXiv preprint arXiv:2303.13988.*

Harris, Z. S. (1954). Distributional structure. Word, 10(2–3), 146–162.

He, H., Peng, N., & Liang, P. (2019). Pun generation with surprise. *arXiv preprint arXiv:1904.06828.*

Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world?Behavioral and Brain Sciences, 33(2–3), 61–83.2055073310.1017/S0140525X0999152X

Hessel, J., Marasović, A., Hwang, J. D., Lee, L., Da, J., Zellers, R., ... & Choi, Y. (2022). Do androids laugh at electric sheep? humor “understanding” benchmarks from the new yorker caption contest. arXiv preprint arXiv:2209.06293.

Howe, N. E. (2002). The origin of humor. Medical Hypotheses, 59(3), 252–254.1220814810.1016/s0306-9877(02)00209-8

Hu, J., Floyd, S., Jouravlev, O., Fedorenko, E., & Gibson, E. (2022). A fine-grained comparison of pragmatic language understanding in humans and language models. *arXiv preprint arXiv:2212.06801.*

Hu, J., & Levy, R. (2023). Prompting is not a substitute for probability measurements in large language models. arXiv preprint arXiv:2305.13264.

Hu, J., Levy, R., Degen, J., & Schuster, S. (2023). Expectations over unspoken alternatives predict pragmatic inferences. *arXiv preprint arXiv:2304.04758.*

Janes, L. M., & Olson, J. M. (2000). Jeer pressure: The behavioral effects of observing ridicule of others. Personality and Social Psychology Bulletin, 26(4), 474–485.

Jentzsch, S., & Kersting, K. (2023). ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models. arXiv preprint arXiv:2306.04563.

Jiang, A. Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford, C., ... & Sayed, W. E. (2024). Mixtral of experts. *arXiv preprint arXiv:2401.04088.*

Jing, X., Talekar, C., & Taylor Rayz, J. (2018). Comparing Jokes with NLP: How Far Can Joke Vectors Take Us?. In Distributed, Ambient and Pervasive Interactions: Technologies and Contexts: 6th International Conference, DAPI 2018, Held as Part of HCI International 2018, Las Vegas, NV, USA, July 15–20, 2018, Proceedings, Part II 6 (pp. 310–326). Springer International Publishing.

Jones, C. R., Chang, T. A., Coulson, S., Michaelov, J. A., Trott, S., & Bergen, B. (2022). Distributional semantics still can't account for affordances. In Proceedings of the Annual Meeting of the Cognitive Science Society (Vol. 44, No. 44).



<!-- page 0019 -->

Jones, C. R., Trott, S., & Bergen, B. (2023). EPITOME: Experimental Protocol Inventory for Theory Of Mind Evaluation. In First Workshop on Theory of Mind in Communicating Agents .

Kao, J., Levy, R., & Goodman, N. D. (2016). A computational model of linguistic humor in puns. Cognitive Science, 40(5), 1270–1285.2623559610.1111/cogs.12269PMC5042108

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361.*

Koestler, A. (1964). The act of creation. New York: Oxford University Press.

Kosinski, M. (2023). Theory of mind might have spontaneously emerged in large language models. Retrieved from https://arxiv.org/abs/2302.02083

Kugler, L., & Kuhbandner, C. (2015). That's not funny!–But it should be: Effects of humorous emotion regulation on emotional experience and memory. Frontiers in Psychology, 6, 1296. 10.3389/fpsyg.2015.0129626379608PMC4551820

Kuribayashi, T., Oseki, Y., Ito, T., Yoshida, R., Asahara, M., & Inui, K. (2021). Lower perplexity is not always human-like. *arXiv preprint arXiv:2106.01229.*

Lauer, R. H., Lauer, J. C., & Kerr, S. T. (1990). The long-term marriage: Perceptions of stability and satisfaction. International Journal of Aging and Human Development, 31(3), 189–195.227269910.2190/H4X7-9DVX-W2N1-D3BF

Lenci, A. (2008). Distributional semantics in linguistic and cognitive research. Italian Journal of Linguistics, 20(1), 1–31.

Lewis, M., & Lupyan, G. (2020). Gender stereotypes are reflected in the distributional structure of 25 languages. Nature Human Behaviour, 4, 1021–1028. 10.1038/s41562-020-0918-632747806

Li, X. L., Kuncoro, A., Hoffmann, J., d'Autume, C. D. M., Blunsom, P., & Nematzadeh, A. (2021). A systematic investigation of commonsense knowledge in large language models. *arXiv preprint arXiv:2111.00607.*

Li, B. Z., Nye, M., & Andreas, J. (2021). Implicit representations of meaning in neural language models. *arXiv preprint arXiv:2106.00737.*

Liesenfeld, A., & Dingemanse, M. (2024). Rethinking open source generative AI: Open washing and the EU AI Act. In The 2024 ACM Conference on Fairness, Accountability, and Transparency (pp. 1774–1787).

López, B. G., & Vaid, J. (2017). Psycholinguistic approaches to humor. In The Routledge handbook of language and humor (pp. 267–281). Routledge.

Mahowald, K., Ivanova, A. A., Blank, I. A., Kanwisher, N., Tenenbaum, J. B., & Fedorenko, E. (2024). Dissociating language and thought in large language models. Trends in Cognitive Sciences, 28(6), 517–5403850891110.1016/j.tics.2024.01.011PMC11416727

Mao, J., & Liu, W. (2019). A BERT-based approach for automatic humor detection and scoring. In IberLEF@ SEPLN (pp. 197–202).

Manning, C. D. (2022). Human language understanding & reasoning. Daedalus, 151(2), 127–138.

Marjieh, R., Sucholutsky, I., van Rijn, P., Jacoby, N., & Griffiths, T. (2023). What language reveals about perception: Distilling psychophysical knowledge from large language models. In Proceedings of the Annual Meeting of the Cognitive Science Society (Vol. 45, No. 45).

Martin, R. A., & Ford, T. (2018). The psychology of humor: An integrative approach. Academic Press.

McGhee, P. E., & Pistolesi, E. (1979). Humor: Its origin and development. San Francisco, CA: WH Freeman.

Michaelov, J. A., Bardolph, M. D., Van Petten, C. K., Bergen, B. K., & Coulson, S. (2024). Strong prediction: Language model surprisal explains multiple N400 effects. Neurobiology of Language, 5(1), 107–135:3864562310.1162/nol_a_00105PMC11025652

Michaelov, J. A., Coulson, S., & Bergen, B. K. (2022). So cloze yet so far: N400 amplitude is better predicted by distributional information than human predictability judgements. IEEE Transactions on Cognitive and Developmental Systems, 15(3), 1033–1042.

Mihalcea, R., & Strapparava, C. (2006). Learning to laugh (automatically): Computational models for humor recognition. Computational Intelligence, 22(2), 126–142.

Mihalcea, R., Strapparava, C., & Pulman, S. (2010). Computational models for incongruity detection in humour. In International Conference on Intelligent Text Processing and Computational Linguistics (pp. 364–374). Berlin, Heidelberg: Springer Berlin Heidelberg.

Moran, J. M., Rain, M., Page-Gould, E., & Mar, R. A. (2014). Do I amuse you? Asymmetric predictors for humor appreciation and humor production. Journal of Research in Personality, 49, 8–13.

Norrick, N. R. (1986). A frame-theoretical analysis of verbal humor: Bisociation as schema conflict.

Noveck, I. (2018). Experimental pragmatics: The making of a cognitive science. Cambridge University Press.

Raskin, V., & Raskin, V. (1984). Semantic theory of humor. Semantic mechanisms of humor, (pp. 99–147). D. Reidel.

Ritchie, G. (2001). Current directions in computational humour. Artificial Intelligence Review, 16, 119–135.

Ritchie, D. (2005). Frame-shifting in humor and irony. Metaphor and Symbol, 20(4), 275–294. 10.1207/s15327868ms2004_3



<!-- page 0020 -->

Samson, A. C. (2012). The influence of empathizing and systemizing on humor processing: Theory of mind and humor. Humor, 25(1), 75–98.

Samson, A. C., Glassco, A. L., Lee, I. A., & Gross, J. J. (2014). Humorous coping and serious reappraisal: Short-term and longer-term effects. Europe's Journal of Psychology, 10(3), 571–581.

Samson, A. C., & Gross, J. J. (2012). Humour as emotion regulation: The differential consequences of negative versus positive humour. Cognition & emotion, 26(2), 375–384.2175621810.1080/02699931.2011.585069

Samermit, P., & Gibbs, Jr, R. W. (2016). Humor, the body, and cognitive linguistics. Cognitive Linguistic Studies, 3(1), 32–49.

Spencer, H. (1875). The physiology of laughter. In H.Spencer (Ed.) Illustrations of universal progress: A series of discussions (pp. 194–209). D Appleton & Company. 10.1037/12203-004

Strick, M., Holland, R. W., Van Baaren, R. B., & Van Knippenberg, A. D. (2009). Finding comfort in a joke: Consolatory effects of humor through cognitive distraction. Emotion, 9(4), 574.1965378210.1037/a0015951

Suls, J. M. (1972). A two-stage model for the appreciation of jokes and cartoons: An information-processing analysis. In JeffreyGoldstein & Paul E.McGhee (Eds.), The psychology of humor: Theoretical perspectives and empirical issues (pp. 81–100).

Tavast, M., Kunnari, A., & Hämäläinen, P. (2022). Language models can generate human-like self-reports of emotion. In 27th International Conference on Intelligent User Interfaces (pp. 69–72).

Trott, S., & Bergen, B. (2021). RAW-C: Relatedness of Ambiguous Words–in Context (A New Lexical Resource for English). *arXiv preprint arXiv:2105.13266.*

Trott, S., Jones, C., Chang, T., Michaelov, J., & Bergen, B. (2023). Do large language models know what humans know?Cognitive Science, 47(7), e13309.3740192310.1111/cogs.13309

Trott, S. (2024a). Can large language models help augment English psycholinguistic datasets?Behavior Research Methods, 56(6), 6082–6100.3826126410.3758/s13428-024-02337-zPMC11335796

Trott, S. (2024b). Large language models and the wisdom of small crowds. Open Mind, 8, 723–738.3882843110.1162/opmi_a_00144PMC11142632

Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P., Rault, T., Louf, R., Funtowicz, M., Davison, J., Shleifer, S., von Platen, P., Ma, C., Jernite, Y., Plu, J., Xu, C., Scao, T. L., Gugger, S., & Rush, A. M. (2020). Transformers: State-of-the-art natural language processing. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations (pp. 38–45).

Xie, Y., Li, J., & Pu, P. (2020). Uncertainty and surprisal jointly deliver the punchline: Exploiting incongruity-based features for humor recognition. *arXiv preprint arXiv:2012.12007.*

Xu, Z., Yuan, S., Chen, L., & Yang, D. (2024). “A good pun is its own reword”: Can Large Language Models Understand Puns? arXiv preprint arXiv:2404.13599.

Yakura, H. (2024). Evaluating large language models’ ability using a psychiatric screening tool based on metaphor and sarcasm scenarios. Journal of Intelligence, 12(7), 70.3905719010.3390/jintelligence12070070PMC11278383

Ziv, A. (1988). Humor's role in married life.

Ziv, A., & Gadish, O. (1989). Humor and marital satisfaction. Journal of Social Psychology, 129(6), 759–768.
