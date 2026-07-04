# Designing and Evaluating Dialogue LLMs for Co-Creative Improvised Theatre

**Boyd Branch, Piotr Mirowski, Kory Mathewson, Sophia Ppali, Alexandra Covaci** — arXiv:2405.07111 · Guide entry #42 (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2405.07111) · [local PDF](../pdfs/42-improvised-theatre-llms.pdf) · [full markdown](../md/42-improvised-theatre-llms/42-improvised-theatre-llms.md) · [extract](../extracts/42-improvised-theatre-llms.json)

## TL;DR
This paper reports a live deployment of dialogue LLMs in Improbotics performances at the 2023 Edinburgh Festival Fringe, where human actors improvised with AI-generated lines in front of audiences. The system used speech recognition, three LLMs, operator-entered context, and human curation; survey results show curiosity and excitement about AI as a creative tool, but audiences still perceived the AI as machine-like and often ignorant of scenes.

## Problem & Motivation
The authors use improvised theatre as a demanding testbed for multi-party conversational AI. Unlike single-user chat, improv requires rapidly tracking multiple speakers, changing roles, physical and social context, timing, and shared narrative assumptions. The goal was not only to test whether LLMs could contribute to live multi-party dialogue, but also to understand how performers and paying audiences respond when AI is visibly part of a professional comedy show.

## Approach
The team built a human-in-the-loop stage system. A single microphone captured live stage dialogue, which was transcribed using OpenAI Whisper; an operator could add character names, scene context, and prompt metadata through a custom interface. Three LLMs generated a continuous “AI Stream” of possible lines, and a curator selected lines on a tablet without knowing which model produced them. Selected lines were delivered through text-to-speech and an earpiece to a human “Cyborg” performer, or to a robot.

The authors also iteratively designed improv games with cast feedback. Formats included Speed Dating, Wedding Speech, Couples’ Therapy, Meet the Parents, Hero’s Journey, Improvised TED Talk, and Movie Pitch. Prompt buttons such as “more snarky” and “more punny” were added after rehearsal because generic helpful assistant behavior was not well suited to comic role-play.

## Data & Experimental Setup
The system was deployed across 26 unique Edinburgh Festival Fringe performances for over 1750 people, with various groups of 20 improvisers. Audience surveys produced 150 unique individual responses; all 150 answered the first 5 questions, while the remaining 15 questions averaged 109 unique responses. Actor surveys produced 21 individual responses. The authors also analyzed dialogue system logs from all 26 performances.

The three dialogue LLMs used in the live line stream were gpt-3.5-turbo, text-bison, and llama-2-13b-chat. The Llama 2 model was served locally; gpt-3.5-turbo and text-bison were remote services.

## Results
The models generated different numbers of lines because of temporary unavailability for remote models and processing speed for llama-2-13b-chat, but after normalising by generated-line counts, each LLM had a comparable chance of being selected by the curator.

Audience ratings were mixed. For Q12, the AI’s naturalness of communication averaged 33, “unique mind” averaged 45, and “machine-like appearance” averaged 64. For Q14, responses were rated “similar to a human” at avg: 53, “motivated toward mutual benefit with other actors” at avg: 64, and “ignorant of the scenes” at avg: 76. In Q9, 37% reported being more excited about using AI tools for creativity, while only 16% felt more optimistic about AI as storytellers. The paper also reports that 40 participants out of 150 enjoyed “watching the robot and humans create funny and entertaining stories together.”

## Takeaways
- Human-in-the-loop curation can make LLMs usable in live multi-party comedy, but it is not a substitute for robust turn-taking and context tracking.
- Audiences may value AI as a visible creative partner even when it fails to behave like a human improviser.
- Prompting for playful conflict, puns, and snark helped produce more stage-useful lines than generic helpful responses.
- For builders, latency, speech recognition errors, speaker tracking, and curator workload are central system constraints.

## Limitations & Caveats
The authors explicitly avoid statistically significant claims because the data were collected “in the wild” at a theatre festival. Survey response volume was low relative to attendance, no demographic data were collected, and the single-microphone speech recognition setup missed gestures, tone, and sometimes transcribed speech incorrectly. Human curation improved outputs but introduced delays and did not always select the most appropriate line.
