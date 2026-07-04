# A Robot Walks into a Bar: Can Language Models Serve as Creativity Support Tools for Comedy? An Evaluation of LLMs’ Humour Alignment with Comedians

**Piotr W. Mirowski, Juliette Love, Kory Mathewson, Shakir Mohamed** — FAccT 2024 · Guide entry #41 (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2405.20956) · [local PDF](../pdfs/41-robot-walks-into-bar.pdf) · [full markdown](../md/41-robot-walks-into-bar/41-robot-walks-into-bar.md) · [extract](../extracts/41-robot-walks-into-bar.json)

## TL;DR
The paper reports a mixed-method HCI study with 20 professional comedians who used ChatGPT-3.5, GPT-4, or Google Bard powered by Gemini Pro during AI x Comedy workshops. The central quantitative result is that LLMs scored only a mediocre Creativity Support Index for comedy writing: μ = 54.6, σ = 18.1. Qualitatively, comedians found LLMs useful for drafts and structure but criticized them as bland, over-moderated, culturally narrow, and weak at the lived context that makes comedy work.

## Problem & Motivation
The authors study whether widely available instruction-tuned LLMs can serve as creativity support tools for comedy. Comedy is a difficult test case because it often relies on incongruity, context, audience knowledge, delivery, identity, and edgy or offensive language used for satire or “punching up.” The paper begins from four hypotheses: LLMs may produce stereotyped language, censor comedy through safety filtering, miss context, and homogenise creative outputs.

## Approach
The study recruited comedians who perform live and already use AI in their artistic process. Each 3-hour workshop included a comedy-writing session, surveys, and a focus group. Participants were encouraged to use LLMs in whatever way might create material they would be comfortable presenting in a comedy context, including generating, rating, detecting, or explaining jokes; co-writing; translating; or rewriting previous material. The authors then measured user experience with Likert questions and the Creativity Support Index, and analyzed focus-group transcripts using constant comparison analysis.

## Data & Experimental Setup
There were 20 professional comedians: 10 in person at the Edinburgh Festival Fringe 2023 and 10 online across three later workshops. The writing exercise lasted around 45 minutes. In the first workshop, participants used ChatGPT-3.5 through a plain text interface similar to ChatGPT. In the online workshops, participants used their preferred accounts: ChatGPT-3.5, GPT-4, and Google Bard powered by Gemini Pro. Languages used during writing included German, Dutch, English, French, Hindi, Swedish, and Tamil. The collected study data consisted of writing-session outputs, individual survey responses, and focus-group transcripts.

## Results
The average Creativity Support Index was μ = 54.6, σ = 18.1, which the authors describe as mediocre; they note that CSI of 90 is excellent and 50 is mediocre. They did not observe a significant change between August 2023 and December 2023: August had μ = 50, σ = 15.8, while December had μ = 60, σ = 19.6. Survey responses suggested that comedians mostly enjoyed writing with AI, but views were mixed on ownership, helpfulness, expressivity, surprise, collaboration, and ease of writing. Most participants did not feel pride in the material or feel it was unique. Six participants described outputs as “bland” or “generic.” In the focus groups, comedians said LLMs could generate first drafts and structure quickly, but that the human writer still supplied the humor. Moderation was a major negative result: participants said safety filtering blocked sexually suggestive material, dark humor, offensive jokes, and discussions tied to marginalized identities.

## Takeaways
- For comedy, LLMs may be more useful as fast brainstorming or structuring tools than as joke writers.
- Evaluating humor tools only by output text misses performer concerns about audience, delivery, identity, and venue.
- Global safety alignment can conflict with comedy practices, especially satire, reclaimed language, and minority perspectives.
- Builders of comedy-writing systems should consider community-based alignment, user control over moderation, and clearer data provenance.
- Comedians were concerned about copyrighted training data, possible plagiarism, licensing, compensation, and underrepresentation in model training data.

## Limitations & Caveats
The sample was small and deliberately recruited from comedians already using AI, which the authors say likely biased the findings. The study did not collect demographic data because of anonymity requirements. Some questionnaire wording and focus-group prompts may have biased responses. The models were common instruction-tuned chat tools, and the authors note that more complex prompting strategies could have produced better outputs.
