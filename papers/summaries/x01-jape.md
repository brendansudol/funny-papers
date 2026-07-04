# An implemented model of punning riddles

**Kim Binsted, Graeme Ritchie** — AAAI 1994 · Guide entry Part 2 (pre-LLM foundations) (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/cmp-lg/9406022) · [local PDF](../pdfs/x01-jape.pdf) · [full markdown](../md/x01-jape/x01-jape.md) · [extract](../extracts/x01-jape.json)

## TL;DR
This paper presents JAPE-1, an implemented symbolic generator for simple question-answer punning riddles. It focuses on homonym word-substitution puns with noun phrase punchlines, using humour-independent lexical entries plus schemata and templates. In an informal human evaluation, JAPE-1 produced 188 jokes with an average score of 1.5 points on a 0–5 scale: recognizable as jokes, but usually weak ones.

## Problem & Motivation
The authors argue that humor generation is a legitimate AI problem because produced jokes can be tested on people. Rather than model humor as a whole, they restrict the problem to a tractable subset: simple punning riddles of the kind found in children’s joke books. They analyze puns as exploiting phonological ambiguity, where the hearer is asked to treat a sound similarity as a semantic comparison. The target class excludes syllable substitution and metathesis, and instead covers word-substitution puns where a homonym is substituted into a common noun phrase punchline.

## Approach
JAPE-1 separates joke construction into two main structures. Schemata describe the underlying lexical configuration: a real word or phrase, its meaning, a shorter phonologically similar word, that word’s meaning, a fake word or phrase made by substitution, and a constructed meaning for the fake phrase. Templates produce the surface question-answer form from an instantiated schema. For example, the same underlying constructed meaning can support different questions, and the same template can be filled from different constructed meanings. The implementation uses a lexicon, a homonym base, six schemata, associated templates, and a simple post-production checker that rejects accidental identity and cases where the supposed nonsense noun phrase is actually a genuine common noun phrase.

## Data & Experimental Setup
As background, the authors studied The Crack-a-Joke Book, a collection of jokes chosen by British children. The homonym relation was implemented as a separate homonym base derived from a list of homophones in American English, shortened to common, concrete nouns and adjectives, and also including words with two distinct meanings. For evaluation, volunteers unfamiliar with JAPE-1 wrote lexical entries for given words. A “common knowledge judge” checked those entries for errors and obscure suggestions. JAPE-1 then generated 188 jokes in near-surface form. These were distributed in batches to 14 judges, who scored them from 0 (“Not a joke. Doesn’t make any sense.”) to 5 (“Really good”) and gave qualitative comments.

## Results
The average point score over all 188 jokes was 1.5 points. The paper says most jokes were given a score of 1 and summarizes the output as “jokes, but pathetic ones.” Nine jokes received the maximum score of five from one judge, but all nine received low scores from the other judge: three got zeroes, three got ones, and three got twos. Some outputs were judged to be of Crack-a-Joke Book quality, including examples such as “A cereal killer,” “A fir coat,” and “A holey grail.” Template choice mattered: the use_syn template produced “What do you use to hit a waiting line? A pool queue,” judged as a non-joke, while a more appropriate class_has_rev version, “What kind of line has sixteen balls? A pool queue,” received an average of two points. Overly general lexical definitions also hurt quality; “What kind of device has wings? An aeroplane hanger” scored half a point.

## Takeaways
- A symbolic generator can produce recognizable punning riddles from humour-independent lexical data.
- Separating schemata from templates helps distinguish underlying pun structure from surface joke wording.
- Template appropriateness is central: the question must reflect the semantic structure implied by the punchline word order.
- Lexical specificity is crucial; overly broad entries generate weak or incoherent jokes.
- Evaluation needs human baselines and better statistical design before claims about quality can be strong.

## Limitations & Caveats
The authors explicitly state that the evaluation was not statistically rigorous, had too few jokes and judges, and lacked a control group of human-produced jokes. JAPE-1 covers only a narrow subtype of puns: homonym word substitution with noun phrase punchlines. It does not yet handle syllable substitution, spoonerisms, or sub-word puns, and its lexicon and homonym base are limited.
