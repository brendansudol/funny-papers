# The Theater Stage as Laboratory: Review of Real-Time Comedy LLM Systems for Live Performance

**Piotr Mirowski, Boyd Branch, Kory Mathewson** — CHum 2025 · Guide entry #43 (Part 5 - Situated & Live Humor)

[paper page](https://arxiv.org/abs/2501.08474) · [local PDF](../pdfs/43-theater-stage-laboratory.pdf) · [full markdown](../md/43-theater-stage-laboratory/43-theater-stage-laboratory.md) · [extract](../extracts/43-theater-stage-laboratory.json)

## TL;DR
This position and review paper argues that live comedy performance is an unusually strong laboratory for evaluating AI humor systems. Its central claim is not a benchmark result: the paper reports no new quantitative experiment, but argues that improvised comedy exposes issues that offline or crowd-sourced evaluation misses, especially embodiment, timing, audience interaction, and human interpretation of AI absurdity.

## Problem & Motivation
The authors start from the view that humor is often treated as a hard test for artificial intelligence and that many comedy practitioners remain skeptical of AI’s comedic potential. They argue that computational humor is usually evaluated in settings that lack the stakes and context of actual comedy: an audience expecting to be entertained, performers adapting in real time, and reviewers judging the whole event. Live comedy, especially improvisation, offers a richer test because it includes timing, cultural context, audience feedback, and the possibility of failure in a socially accepted theatrical setting.

## Approach
The paper is a literature and performance review, organized around live AI comedy systems rather than a new model. It surveys robot stand-up, human-versus-AI comedy shows, comedy Turing tests, deepfake-driven performance, AI-assisted improv, virtual reality improv, and AI-supported theatrical writing. From these examples, the authors identify three sets of challenges: embodiment and anthropomorphism; liveness, timing, and utility in performance; and human interpretation of seemingly absurd AI-generated language. They also propose evaluating AI comedy as a creativity support tool for comedians rather than only as an adversary competing with humans.

## Data & Experimental Setup
The paper does not introduce a dataset or run a controlled experiment. It notes that earlier HumanMachine work trained general conversational models on OpenSubtitles and combined language models with speech recognition, text-to-speech, and robot control. The review covers many performance settings, including Nao robot comedy, Improbotics cyborg actors receiving AI lines through earpieces or augmented-reality glasses, AI-supported rap battles and roasts, PowerPoint karaoke slide generation, Dramatron-supported scripts, VR improv, Discord prompt battles, multilingual improv using speech recognition and machine translation, and deepfake-based comedy installations.

## Results
There are no benchmark scores, no human preference percentages, and no system ranking in this paper. The main “result” is an argued framework: live performance reveals evaluation issues that static text judgments do not. The paper highlights that Improbotics performers reported struggling with slow AI timing and delays, and perceived that audiences preferred timely responses to higher-quality but delayed responses. It also notes that audience reception of robot comedy may confound novelty with comedic quality.

## Takeaways
- Evaluate humor systems where humor is actually consumed: in front of audiences, with timing pressure and context.
- For live AI comedy, latency and turn-taking can matter as much as the linguistic quality of generated lines.
- Human-in-the-loop curation can turn AI dialogue generation into a “writer’s room” rather than a fully autonomous chatbot.
- Adversarial “human versus AI” formats are theatrically useful, but the authors prefer a collaborative creativity-support framing.
- Useful evaluation signals include audience laughter, audience and performer surveys, chat interaction in online shows, focus groups with comedians, and creativity support metrics.

## Limitations & Caveats
The paper is a position paper and review, not an empirical comparison. Some humor formats, such as memes, films, and pre-written comedic videos, do not naturally fit live or improvised evaluation. The authors also caution that crowd-sourced evaluation can lack context and evaluator buy-in, while live performance itself introduces confounds such as novelty, venue constraints, and audience expectations.
