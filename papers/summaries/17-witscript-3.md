# Witscript 3: A Hybrid AI System for Improvising Jokes in a Conversation

**Joe Toplyn** — arXiv:2301.02695 · Guide entry #17 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2301.02695) · [local PDF](../pdfs/17-witscript-3.pdf) · [full markdown](../md/17-witscript-3/17-witscript-3.md) · [extract](../extracts/17-witscript-3.json)

## TL;DR
Witscript 3 is a neural-symbolic system for improvising jokes in conversation. It combines explicit joke-writing algorithms with GPT-3 text-davinci-002, generates three joke candidates using different mechanisms, and selects the candidate that seems funniest. In an AMT evaluation, Witscript 3 received the highest mean rating, 2.36, and its responses were judged to be jokes 44.1% of the time.

## Problem & Motivation
The paper targets contextually integrated conversational joke generation: a chatbot or social robot should be able to say something funny about what is happening in the moment. The author argues that high-quality conversational humor requires variety, including multiple joke production mechanisms, and that prior systems either lacked explicit humor algorithms or relied on only one mechanism. Witscript 3 extends Witscript and Witscript 2 by combining their wordplay and common-sense joke mechanisms with a third, proprietary mechanism.

## Approach
Witscript 3 is presented as a hybrid AI system. It is symbolic because it incorporates two humor algorithms: one derived from the Surprise Theory of Laughter, which represents a monologue-type joke as a topic, an angle, and a punch line, and the Basic Joke-Writing Algorithm, which selects a topic, topic handles, associations, a punch line, and an angle. It is neural because it uses OpenAI GPT-3 text-davinci-002, without fine-tuning, to execute many of those steps through prompt chaining.

Given a user sentence, Witscript 3 treats it as the joke topic. GPT-3 selects two conspicuous nouns, noun phrases, or named entities as topic handles, then generates associations for each. The system creates three punch line candidates: a wordplay candidate using NLP tools rather than GPT-3, a common-sense knowledge candidate using GPT-3, and a third candidate produced by a proprietary mechanism involving the topic handles. GPT-3 then generates an angle for each candidate and is prompted to decide which of the three joke candidates seems funniest.

## Data & Experimental Setup
The evaluation used 13 sentences selected from Amazon’s Topical-Chat dataset. The author sampled comments at random, selected the last or only complete sentence when it met criteria such as length of 20 words or less and at least two nouns, noun phrases, or named entities, and standardized spelling, capitalization, and punctuation.

Each input sentence received responses from three sources: the original Human Topical-Chat respondent, GPT-LOL, and Witscript 3. GPT-LOL is a baseline using text-davinci-002 with the prompt “You want to be funny. Respond to this: [The sentence],” temperature 0.7, and Top P 1.0. The 39 input-response pairs were randomized and rated by 15 AMT workers each, producing 585 ratings. Ratings used a 1–4 scale: not a joke, almost a joke, a joke, or a very good joke.

## Results
Witscript 3 outperformed both comparison sources. Its mean rating was 2.36, compared with 1.96 for GPT-LOL and 1.84 for Human responses; this is a 0.40 mean-rating advantage over GPT-LOL and 0.52 over Human. On the percentage of responses rated 3 or 4, Witscript 3 reached 44.1%, compared with 33.8% for GPT-LOL and 23.6% for Human responses. Thus Witscript 3 led GPT-LOL by 10.3 percentage points and Human by 20.5 percentage points on the paper’s joke-rate measure.

## Takeaways
- Prompt chaining lets the system decompose joke generation into editable steps rather than asking an LLM to produce a joke in one shot.
- Combining symbolic humor algorithms with GPT-3 produced better ratings than the GPT-LOL baseline that simply prompted GPT-3 to be funny.
- Multiple joke production mechanisms are central to the system’s claim of generating a more varied range of conversational jokes.
- For builders of humor systems, the paper’s evidence favors structured generation pipelines over bare prompting for this task.

## Limitations & Caveats
The evaluation is small, using 13 input sentences and 39 total input-response pairs. The human comparison is not a human joke-writing baseline, because the Topical-Chat workers were not trying especially to be funny. The third joke mechanism is proprietary and not specified. Witscript 3 was rated as a joke or very good joke 44.1% of the time, so consistency remains limited; the paper lists improved prompts, other LLMs, and additional mechanisms as future work.
