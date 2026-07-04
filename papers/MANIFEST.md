# Paper Library Manifest

Companion library for [humor-and-llms-field-guide.md](../humor-and-llms-field-guide.md). Regenerated 2026-07-03 by `scripts/build_manifest.py` from [papers.json](papers.json) (the machine-readable source of truth).

**86 entries**: 80 converted, 6 no open PDF.

Layout:

- `papers/pdfs/<key>.pdf` — downloaded paper PDFs
- `papers/md/<key>/<key>.md` — combined Markdown transcription (per-page files in `papers/md/<key>/pages/`, per-page API usage in `papers/md/<key>/manifest.jsonl`)
- `papers/runs/<key>.progress.jsonl` — conversion progress logs
- `papers/extracts/<key>.json` — structured extract (tasks, datasets, models, theories, headline numbers); `papers/summaries/<key>.md` — one-page summary; cross-paper views in [ANALYSIS.md](ANALYSIS.md)

Pipeline: `scripts/download_papers.py` -> `scripts/convert_papers.py` (uses `../pdf-to-md`) -> `scripts/build_manifest.py`. All steps are resumable; to add a missing paper, drop the PDF into `papers/pdfs/` with the right key and rerun the last two steps.

## Theory Foundations

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | [Semantic Mechanisms of Humor (Script-based Semantic Theory of Humor)](https://link.springer.com/book/10.1007/978-94-009-6472-3) | 1985 | Reidel/Springer (book) | — | — | — | no open PDF Book; no open-access PDF. |
| T2 | The General Theory of Verbal Humor (GTVH) | 1991 | HUMOR 4:293-347; expanded in Attardo, Linguistic Theories of Humor (1994) | — | — | — | no open PDF Paywalled journal article / book; no open-access PDF. |
| T3 | [Inside Jokes: Using Humor to Reverse-Engineer the Mind](https://mitpress.mit.edu/9780262518697/inside-jokes/) | 2011 | MIT Press (book) | — | — | — | no open PDF Book; no open-access PDF. |
| T4 | [The Linguistic Analysis of Jokes](https://www.routledge.com/The-Linguistic-Analysis-of-Jokes/Ritchie/p/book/9781138008731) | 2004 | Routledge (book) | — | — | — | no open PDF Book; no open-access PDF. |
| T5 | Incongruity-Resolution & Appropriate Incongruity | 1972 | Book chapters (Suls two-stage model; Oring, Engaging Humor) | — | — | — | no open PDF Book chapters; no open-access PDF. |
| T6 | [Benign Violations: Making Immoral Behavior Funny](https://journals.sagepub.com/doi/10.1177/0956797610376073) | 2010 | Psychological Science | [pdf (9p)](pdfs/t6-benign-violation.pdf) | [md](md/t6-benign-violation/t6-benign-violation.md) | [1-pager](summaries/t6-benign-violation.md) | Author-hosted copy; journal version is paywalled. Distance follow-ups (2012, 2014) are paywalled and not downloaded. |
| Theory (also worth knowing) | [Jokes and the Logic of the Cognitive Unconscious](https://dspace.mit.edu/handle/1721.1/6300) | 1980 | MIT AI Memo 603 | [pdf (25p)](pdfs/x15-minsky-jokes.pdf) | [md](md/x15-minsky-jokes/x15-minsky-jokes.md) | [1-pager](summaries/x15-minsky-jokes.md) | Only 'Also worth knowing' theory item with an open PDF (MIT DSpace). Other items in that list (Coulson, Martin, HSQ, Provine, Berger, Dikkers, classical works) are books/paywalled. |

## Part 1 - Explaining & Understanding Jokes

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #1 | [Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest](https://arxiv.org/abs/2209.06293) | 2023 | ACL 2023 | [pdf (25p)](pdfs/01-androids-electric-sheep.pdf) | [md](md/01-androids-electric-sheep/01-androids-electric-sheep.md) | [1-pager](summaries/01-androids-electric-sheep.md) |  |
| #2 | [ChatGPT is fun, but it is not funny! Humor is still challenging LLMs](https://arxiv.org/abs/2306.04563) | 2023 | WASSA 2023 | [pdf (16p)](pdfs/02-chatgpt-fun-not-funny.pdf) | [md](md/02-chatgpt-fun-not-funny/02-chatgpt-fun-not-funny.md) | [1-pager](summaries/02-chatgpt-fun-not-funny.md) |  |
| #3 | [Which LLMs Get the Joke? Probing Non-STEM Reasoning Abilities with HumorBench](https://arxiv.org/abs/2507.21476) | 2025 | arXiv:2507.21476 | [pdf (14p)](pdfs/03-humorbench.pdf) | [md](md/03-humorbench/03-humorbench.md) | [1-pager](summaries/03-humorbench.md) |  |
| #4 | [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://arxiv.org/abs/2509.12158) | 2025 | EMNLP 2025 | [pdf (36p)](pdfs/04-pun-unintended.pdf) | [md](md/04-pun-unintended/04-pun-unintended.md) | [1-pager](summaries/04-pun-unintended.md) |  |
| #5 | [Comparing Apples to Oranges: LLM Humour Understanding from Traditional Puns to Topical Jokes](https://arxiv.org/abs/2507.13335) | 2025 | EMNLP Findings 2025 | [pdf (17p)](pdfs/05-apples-to-oranges.pdf) | [md](md/05-apples-to-oranges/05-apples-to-oranges.md) | [1-pager](summaries/05-apples-to-oranges.md) |  |
| #6 | ["A good pun is its own reword": Can Large Language Models Understand Puns?](https://aclanthology.org/2024.emnlp-main.657/) | 2024 | EMNLP 2024 | [pdf (17p)](pdfs/06-good-pun-own-reword.pdf) | [md](md/06-good-pun-own-reword/06-good-pun-own-reword.md) | [1-pager](summaries/06-good-pun-own-reword.md) |  |
| #7 | [ExPUNations: Augmenting Puns with Keywords and Explanations](https://arxiv.org/abs/2210.13513) | 2022 | EMNLP 2022 | [pdf (16p)](pdfs/07-expunations.pdf) | [md](md/07-expunations/07-expunations.md) | [1-pager](summaries/07-expunations.md) |  |
| #8 | ["What do you call a dog that is incontrovertibly true? Dogma": Testing LLM Generalization through Humor (Phunny)](https://aclanthology.org/2025.acl-long.1117/) | 2025 | ACL 2025 | [pdf (16p)](pdfs/08-phunny.pdf) | [md](md/08-phunny/08-phunny.md) | [1-pager](summaries/08-phunny.md) |  |
| #9 | [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](https://arxiv.org/abs/2412.05315) | 2025 | CHum 2025 | [pdf (9p)](pdfs/09-text-not-all-you-need.pdf) | [md](md/09-text-not-all-you-need/09-text-not-all-you-need.md) | [1-pager](summaries/09-text-not-all-you-need.md) |  |

## Part 2 - Generating Jokes

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #10 | [Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM](https://aclanthology.org/2024.findings-acl.51/) | 2024 | Findings of ACL 2024 | [pdf (13p)](pdfs/10-joke-master-pun-curriculum.pdf) | [md](md/10-joke-master-pun-curriculum/10-joke-master-pun-curriculum.md) | [1-pager](summaries/10-joke-master-pun-curriculum.md) |  |
| #11 | [Let's Think Outside the Box: Leap-of-Thought in LLMs with Creative Humor Generation (CLoT)](https://arxiv.org/abs/2312.02439) | 2024 | CVPR 2024 | [pdf (41p)](pdfs/11-clot-leap-of-thought.pdf) | [md](md/11-clot-leap-of-thought/11-clot-leap-of-thought.md) | [1-pager](summaries/11-clot-leap-of-thought.md) |  |
| #12 | [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps (LoL)](https://arxiv.org/abs/2410.10370) | 2025 | ICLR 2025 | [pdf (25p)](pdfs/12-lol-thought-leaps.pdf) | [md](md/12-lol-thought-leaps/12-lol-thought-leaps.md) | [1-pager](summaries/12-lol-thought-leaps.md) |  |
| #13 | [HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation](https://arxiv.org/abs/2604.09629) | 2026 | arXiv:2604.09629 | [pdf (26p)](pdfs/13-humorgen-persona-distillation.pdf) | [md](md/13-humorgen-persona-distillation/13-humorgen-persona-distillation.md) | [1-pager](summaries/13-humorgen-persona-distillation.md) |  |
| #14 | [AI Humor Generation: Cognitive, Social and Creative Skills for Effective Humor](https://arxiv.org/abs/2502.07981) | 2025 | arXiv:2502.07981 | [pdf (18p)](pdfs/14-ai-humor-generation-skills.pdf) | [md](md/14-ai-humor-generation-skills/14-ai-humor-generation-skills.md) | [1-pager](summaries/14-ai-humor-generation-skills.md) |  |
| #15 | [Small But Funny: A Feedback-Driven Approach to Humor Distillation](https://arxiv.org/abs/2402.18113) | 2024 | ACL 2024 | [pdf (12p)](pdfs/15-small-but-funny.pdf) | [md](md/15-small-but-funny/15-small-but-funny.md) | [1-pager](summaries/15-small-but-funny.md) |  |
| #16 | [Humor Mechanics: Advancing Humor Generation with Multistep Reasoning](https://computationalcreativity.net/iccc24/papers/ICCC24_paper_128.pdf) | 2024 | ICCC 2024 | [pdf (11p)](pdfs/16-humor-mechanics-multistep.pdf) | [md](md/16-humor-mechanics-multistep/16-humor-mechanics-multistep.md) | [1-pager](summaries/16-humor-mechanics-multistep.md) |  |
| #17 | [Witscript 3: A Hybrid AI System for Improvising Jokes in a Conversation](https://arxiv.org/abs/2301.02695) | 2023 | arXiv:2301.02695 | [pdf (5p)](pdfs/17-witscript-3.pdf) | [md](md/17-witscript-3/17-witscript-3.md) | [1-pager](summaries/17-witscript-3.md) |  |
| #18 | [Grounded Satirical Generation with RAG](https://arxiv.org/abs/2605.10853) | 2026 | arXiv:2605.10853 | [pdf (10p)](pdfs/18-grounded-satire-rag.pdf) | [md](md/18-grounded-satire-rag/18-grounded-satire-rag.md) | [1-pager](summaries/18-grounded-satire-rag.md) |  |
| #19 | [Jokeasy: Exploring Human-AI Collaboration in Thematic Joke Generation](https://arxiv.org/abs/2602.09496) | 2026 | IASDR 2025 (arXiv:2602.09496) | [pdf (19p)](pdfs/19-jokeasy.pdf) | [md](md/19-jokeasy/19-jokeasy.md) | [1-pager](summaries/19-jokeasy.md) |  |
| #20 | [Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation](https://arxiv.org/abs/2602.14770) | 2026 | arXiv:2602.14770 | [pdf (18p)](pdfs/20-multi-agent-comedy-club.pdf) | [md](md/20-multi-agent-comedy-club/20-multi-agent-comedy-club.md) | [1-pager](summaries/20-multi-agent-comedy-club.md) |  |
| Part 2 (also in this cluster) | [COMIC: Content Optimization via Multi-agent Iterative Competition](https://arxiv.org/abs/2603.11048) | 2026 | arXiv:2603.11048 | [pdf (24p)](pdfs/x02-comic.pdf) | [md](md/x02-comic/x02-comic.md) | [1-pager](summaries/x02-comic.md) |  |
| Part 2 (also in this cluster) | [OpenMic: multi-agent Chinese stand-up generation](https://arxiv.org/abs/2601.08288) | 2026 | arXiv:2601.08288 | [pdf (14p)](pdfs/x03-openmic.pdf) | [md](md/x03-openmic/x03-openmic.md) | [1-pager](summaries/x03-openmic.md) |  |
| Part 2 (pre-LLM foundations) | [An implemented model of punning riddles (JAPE)](https://arxiv.org/abs/cmp-lg/9406022) | 1994 | AAAI 1994 | [pdf (6p)](pdfs/x01-jape.pdf) | [md](md/x01-jape/x01-jape.md) | [1-pager](summaries/x01-jape.md) |  |
| #21 | [One Does Not Simply Meme Alone: Co-Creativity Between LLMs and Humans](https://arxiv.org/abs/2501.11433) | 2025 | IUI 2025 | [pdf (11p)](pdfs/21-meme-co-creativity.pdf) | [md](md/21-meme-co-creativity/21-meme-co-creativity.md) | [1-pager](summaries/21-meme-co-creativity.md) |  |
| #17 (companion) | [Can AI Make Us Laugh? Comparing Jokes Generated by Witscript and a Human Expert](https://aclanthology.org/2025.chum-1.8/) | 2025 | CHum 2025 | [pdf (8p)](pdfs/x08-can-ai-make-us-laugh.pdf) | [md](md/x08-can-ai-make-us-laugh/x08-can-ai-make-us-laugh.md) | [1-pager](summaries/x08-can-ai-make-us-laugh.md) |  |

## Part 3 - Multimodal & Visual Humor

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #22 | [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://arxiv.org/abs/2406.10522) | 2024 | NeurIPS 2024 (D&B) | [pdf (22p)](pdfs/22-caption-preferences.pdf) | [md](md/22-caption-preferences/22-caption-preferences.md) | [1-pager](summaries/22-caption-preferences.md) |  |
| #23 | [Bridging the Creativity Understanding Gap: Small-Scale Human Alignment Enables Expert-Level Humor Ranking](https://arxiv.org/abs/2502.20356) | 2025 | EMNLP Findings 2025 | [pdf (15p)](pdfs/23-creativity-understanding-gap.pdf) | [md](md/23-creativity-understanding-gap/23-creativity-understanding-gap.md) | [1-pager](summaries/23-creativity-understanding-gap.md) |  |
| #24 | [Learning to Think Like a Cartoon Captionist: Incongruity-Resolution Supervision for Multimodal Humor Understanding](https://arxiv.org/abs/2604.15210) | 2026 | arXiv:2604.15210 | [pdf (38p)](pdfs/24-irs-cartoon-captionist.pdf) | [md](md/24-irs-cartoon-captionist/24-irs-cartoon-captionist.md) | [1-pager](summaries/24-irs-cartoon-captionist.md) |  |
| #25 | [HumorDB: Can AI Understand Graphical Humor? (earlier arXiv title: Is AI Fun? HumorDB)](https://arxiv.org/abs/2406.13564) | 2025 | ICCV 2025 | [pdf (17p)](pdfs/25-humordb.pdf) | [md](md/25-humordb/25-humordb.md) | [1-pager](summaries/25-humordb.md) |  |
| #26 | [YesBut: A High-Quality Annotated Multimodal Dataset for Evaluating Satire Comprehension of VLMs](https://arxiv.org/abs/2409.13592) | 2024 | EMNLP 2024 | [pdf (18p)](pdfs/26-yesbut.pdf) | [md](md/26-yesbut/26-yesbut.md) | [1-pager](summaries/26-yesbut.md) |  |
| #27 | [BottleHumor: Self-Informed Humor Explanation using the Information Bottleneck Principle](https://arxiv.org/abs/2502.18331) | 2025 | Findings of ACL 2025 | [pdf (22p)](pdfs/27-bottlehumor.pdf) | [md](md/27-bottlehumor/27-bottlehumor.md) | [1-pager](summaries/27-bottlehumor.md) |  |
| Part 3 (also in this section) | [Humor in Pixels: Benchmarking Large Multimodal Models Understanding of Online Comics (PixelHumor)](https://arxiv.org/abs/2509.12248) | 2025 | EMNLP Findings 2025 | [pdf (27p)](pdfs/x04-pixelhumor.pdf) | [md](md/x04-pixelhumor/x04-pixelhumor.md) | [1-pager](summaries/x04-pixelhumor.md) |  |
| Part 3 (also in this section) | [MemeReaCon: meme understanding with image, post and comments](https://arxiv.org/abs/2505.17433) | 2025 | EMNLP 2025 | [pdf (21p)](pdfs/x05-memereacon.pdf) | [md](md/x05-memereacon/x05-memereacon.md) | [1-pager](summaries/x05-memereacon.md) |  |
| Part 3 (video humor) | [Can Language Models Laugh at YouTube Short-form Videos? (ExFunTube)](https://arxiv.org/abs/2310.14159) | 2023 | EMNLP 2023 | [pdf (20p)](pdfs/x06-exfuntube.pdf) | [md](md/x06-exfuntube/x06-exfuntube.md) | [1-pager](summaries/x06-exfuntube.md) |  |
| Part 3 (video humor) | [v-HUB: minimally verbal video humor understanding benchmark](https://arxiv.org/abs/2509.25773) | 2025 | arXiv:2509.25773 | [pdf (24p)](pdfs/x07-vhub.pdf) | [md](md/x07-vhub/x07-vhub.md) | [1-pager](summaries/x07-vhub.md) |  |
| #28 | [HUMORCHAIN: Theory-Guided Multi-Stage Reasoning for Interpretable Multimodal Humor Generation](https://arxiv.org/abs/2511.21732) | 2026 | CVPR 2026 | [pdf (22p)](pdfs/28-humorchain.pdf) | [md](md/28-humorchain/28-humorchain.md) | [1-pager](summaries/28-humorchain.md) |  |
| #29 | [On the Wings of Imagination: Conflicting Script-based Multi-role Framework for Humor Caption Generation (HOMER)](https://arxiv.org/abs/2602.06423) | 2026 | ICLR 2026 | [pdf (29p)](pdfs/29-homer.pdf) | [md](md/29-homer/29-homer.md) | [1-pager](summaries/29-homer.md) | Verify phrase split across line wrap in PDF text layer; title confirmed manually. |
| #30 | [Culture-Aware Humorous Captioning: Multimodal Humor Generation across Cultural Contexts](https://arxiv.org/abs/2604.18091) | 2026 | arXiv:2604.18091 | [pdf (18p)](pdfs/30-culture-aware-captioning.pdf) | [md](md/30-culture-aware-captioning/30-culture-aware-captioning.md) | [1-pager](summaries/30-culture-aware-captioning.md) |  |

## Part 4 - Evaluation Methodology

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #31 | [How Funny is ChatGPT? A Comparison of Human- and A.I.-Produced Jokes](https://doi.org/10.1371/journal.pone.0305364) | 2024 | PLOS One 2024 | [pdf (13p)](pdfs/31-how-funny-is-chatgpt.pdf) | [md](md/31-how-funny-is-chatgpt/31-how-funny-is-chatgpt.md) | [1-pager](summaries/31-how-funny-is-chatgpt.md) |  |
| #32 | [Crowd Score: A Method for the Evaluation of Jokes using Large Language Models](https://arxiv.org/abs/2212.11214) | 2022 | arXiv:2212.11214 | [pdf (11p)](pdfs/32-crowd-score.pdf) | [md](md/32-crowd-score/32-crowd-score.md) | [1-pager](summaries/32-crowd-score.md) |  |
| #33 | [Is GPT-4 Good Enough to Evaluate Jokes?](https://computationalcreativity.net/iccc23/papers/ICCC-2023_paper_89.pdf) | 2023 | ICCC 2023 | [pdf (5p)](pdfs/33-gpt4-evaluate-jokes.pdf) | [md](md/33-gpt4-evaluate-jokes/33-gpt4-evaluate-jokes.md) | [1-pager](summaries/33-gpt4-evaluate-jokes.md) |  |
| #34 | [Cards Against LLMs: Benchmarking Humor Alignment in Large Language Models](https://aclanthology.org/2026.chum-1.4/) | 2026 | CHum 2026 | [pdf (14p)](pdfs/34-cards-against-llms.pdf) | [md](md/34-cards-against-llms/34-cards-against-llms.md) | [1-pager](summaries/34-cards-against-llms.md) |  |
| #35 | [HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation](https://arxiv.org/abs/2604.19786) | 2026 | arXiv:2604.19786 | [pdf (41p)](pdfs/35-humorrank.pdf) | [md](md/35-humorrank/35-humorrank.md) | [1-pager](summaries/35-humorrank.md) |  |
| #36 | [Who Laughs with Whom? Disentangling Humor Preferences across User Clusters and LLMs](https://arxiv.org/abs/2601.03103) | 2026 | arXiv:2601.03103 | [pdf (21p)](pdfs/36-who-laughs-with-whom.pdf) | [md](md/36-who-laughs-with-whom/36-who-laughs-with-whom.md) | [1-pager](summaries/36-who-laughs-with-whom.md) |  |
| #37 | [From Punchlines to Predictions: A Metric to Assess LLM Performance in Identifying Humor in Stand-Up Comedy](https://arxiv.org/abs/2504.09049) | 2025 | CMCL 2025 | [pdf (11p)](pdfs/37-punchlines-to-predictions.pdf) | [md](md/37-punchlines-to-predictions/37-punchlines-to-predictions.md) | [1-pager](summaries/37-punchlines-to-predictions.md) |  |
| #38 | [Assessing the Capabilities of LLMs in Humor: A Multi-dimensional Analysis of Oogiri Generation and Evaluation](https://arxiv.org/abs/2511.09133) | 2026 | AAAI 2026 | [pdf (21p)](pdfs/38-oogiri-multidimensional.pdf) | [md](md/38-oogiri-multidimensional/38-oogiri-multidimensional.md) | [1-pager](summaries/38-oogiri-multidimensional.md) |  |
| #39 | [Oogiri-Master: Benchmarking Humor Understanding via Oogiri](https://arxiv.org/abs/2512.21494) | 2025 | arXiv:2512.21494 | [pdf (12p)](pdfs/39-oogiri-master.pdf) | [md](md/39-oogiri-master/39-oogiri-master.md) | [1-pager](summaries/39-oogiri-master.md) |  |
| #40 | [One Joke to Rule them All? On the (Im)possibility of Generalizing Humor Detection](https://aclanthology.org/2026.chum-1.1/) | 2026 | CHum 2026 | [pdf (28p)](pdfs/40-one-joke-to-rule-them-all.pdf) | [md](md/40-one-joke-to-rule-them-all/40-one-joke-to-rule-them-all.md) | [1-pager](summaries/40-one-joke-to-rule-them-all.md) |  |

## Part 5 - Situated & Live Humor

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #41 | [A Robot Walks into a Bar: Can Language Models Serve as Creativity Support Tools for Comedy?](https://arxiv.org/abs/2405.20956) | 2024 | FAccT 2024 | [pdf (15p)](pdfs/41-robot-walks-into-bar.pdf) | [md](md/41-robot-walks-into-bar/41-robot-walks-into-bar.md) | [1-pager](summaries/41-robot-walks-into-bar.md) |  |
| #42 | [Designing and Evaluating Dialogue LLMs for Co-Creative Improvised Theatre](https://arxiv.org/abs/2405.07111) | 2024 | arXiv:2405.07111 | [pdf (13p)](pdfs/42-improvised-theatre-llms.pdf) | [md](md/42-improvised-theatre-llms/42-improvised-theatre-llms.md) | [1-pager](summaries/42-improvised-theatre-llms.md) |  |
| #43 | [The Theater Stage as Laboratory: Review of Real-Time Comedy LLM Systems for Live Performance](https://arxiv.org/abs/2501.08474) | 2025 | CHum 2025 | [pdf (8p)](pdfs/43-theater-stage-laboratory.pdf) | [md](md/43-theater-stage-laboratory/43-theater-stage-laboratory.md) | [1-pager](summaries/43-theater-stage-laboratory.md) |  |
| #44 | [StandUp4AI: A New Multilingual Dataset for Humor Detection in Stand-up Comedy Videos](https://arxiv.org/abs/2505.18903) | 2025 | arXiv:2505.18903 | [pdf (8p)](pdfs/44-standup4ai.pdf) | [md](md/44-standup4ai/44-standup4ai.md) | [1-pager](summaries/44-standup4ai.md) |  |
| #45 | [Not All Jokes Land: Evaluating LLMs' Understanding of Workplace Humor](https://arxiv.org/abs/2506.01819) | 2025 | arXiv:2506.01819 | [pdf (8p)](pdfs/45-not-all-jokes-land.pdf) | [md](md/45-not-all-jokes-land/45-not-all-jokes-land.md) | [1-pager](summaries/45-not-all-jokes-land.md) |  |
| #46 | [Can AI Take a Joke - Or Make One? A Study of Humor Generation and Recognition in LLMs](https://dl.acm.org/doi/10.1145/3698061.3734388) | 2025 | Creativity & Cognition 2025 | [pdf (7p)](pdfs/46-can-ai-take-a-joke.pdf) | [md](md/46-can-ai-take-a-joke/46-can-ai-take-a-joke.md) | [1-pager](summaries/46-can-ai-take-a-joke.md) | Bot-walled for scripted clients; downloaded manually in browser. |

## Part 6 - Safety, Harm & Boundaries

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #47 | [Engagement Undermines Safety: How Stereotypes and Toxicity Shape Humor in Language Models](https://arxiv.org/abs/2510.18454) | 2026 | EACL 2026 | [pdf (19p)](pdfs/47-engagement-undermines-safety.pdf) | [md](md/47-engagement-undermines-safety/47-engagement-undermines-safety.md) | [1-pager](summaries/47-engagement-undermines-safety.md) |  |
| #48 | [Harm or Humor: A Multimodal, Multilingual Benchmark for Overt and Covert Harmful Humor](https://arxiv.org/abs/2603.17759) | 2026 | arXiv:2603.17759 | [pdf (19p)](pdfs/48-harm-or-humor.pdf) | [md](md/48-harm-or-humor/48-harm-or-humor.md) | [1-pager](summaries/48-harm-or-humor.md) |  |
| #49 | [Using Humor to Bypass Safety Guardrails in Large Language Models](https://aclanthology.org/2025.llmsec-1.3/) | 2025 | LLMSEC 2025 | [pdf (9p)](pdfs/49-humor-bypass-guardrails.pdf) | [md](md/49-humor-bypass-guardrails/49-humor-bypass-guardrails.md) | [1-pager](summaries/49-humor-bypass-guardrails.md) |  |

## Part 7 - Cross-Cultural & Translation

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #50 | [Chumor 1.0: A Truly Funny and Challenging Chinese Humor Understanding Dataset from Ruo Zhi Ba](https://arxiv.org/abs/2406.12754) | 2024 | arXiv:2406.12754 | [pdf (13p)](pdfs/50-chumor.pdf) | [md](md/50-chumor/50-chumor.md) | [1-pager](summaries/50-chumor.md) |  |
| #50 (2.0) | [Chumor 2.0: Towards Benchmarking Chinese Humor Understanding](https://arxiv.org/abs/2412.17729) | 2025 | ACL Findings 2025 (arXiv:2412.17729) | [pdf (18p)](pdfs/50b-chumor-2.pdf) | [md](md/50b-chumor-2/50b-chumor-2.md) | [1-pager](summaries/50b-chumor-2.md) |  |
| #51 | [CFunModel: A "Funny" Language Model Capable of Chinese Humor Generation and Processing](https://arxiv.org/abs/2503.20417) | 2025 | arXiv:2503.20417 | [pdf (9p)](pdfs/51-cfunmodel.pdf) | [md](md/51-cfunmodel/51-cfunmodel.md) | [1-pager](summaries/51-cfunmodel.md) |  |
| #52 | [Pun2Pun: Benchmarking LLMs on Textual-Visual Chinese-English Pun Translation](https://aclanthology.org/2025.acl-srw.23/) | 2025 | ACL 2025 SRW | [pdf (24p)](pdfs/52-pun2pun.pdf) | [md](md/52-pun2pun/52-pun2pun.md) | [1-pager](summaries/52-pun2pun.md) |  |
| #53 | [Psychology-Driven Enhancement of Humour Translation](https://arxiv.org/abs/2507.09259) | 2025 | arXiv:2507.09259 | [pdf (16p)](pdfs/53-psychology-driven-translation.pdf) | [md](md/53-psychology-driven-translation/53-psychology-driven-translation.md) | [1-pager](summaries/53-psychology-driven-translation.md) |  |
| #54 | [Not Funny Anymore: LLM Judges Confuse Literal Similarity for Humor in Translated Jokes](https://openreview.net/forum?id=fdrM652upk) | 2026 | LM4UC @ AAAI 2026 | [pdf (7p)](pdfs/54-not-funny-anymore.pdf) | [md](md/54-not-funny-anymore/54-not-funny-anymore.md) | [1-pager](summaries/54-not-funny-anymore.md) | Bot-walled for scripted clients; downloaded manually in browser. |
| #55 | [Jokes or Gibberish? Humor Retention in Translation: NMT vs. LLM](https://www.mdpi.com/2673-6470/5/4/49) | 2025 | Digital (MDPI) 5(4):49 | [pdf (16p)](pdfs/55-jokes-or-gibberish.pdf) | [md](md/55-jokes-or-gibberish/55-jokes-or-gibberish.md) | [1-pager](summaries/55-jokes-or-gibberish.md) | Bot-walled for scripted clients; downloaded manually in browser. |

## Part 8 - Datasets & Shared Tasks

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #56 | [Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models](https://arxiv.org/abs/2403.00794) | 2024 | ACL 2024 | [pdf (15p)](pdfs/56-getting-serious-unfunny.pdf) | [md](md/56-getting-serious-unfunny/56-getting-serious-unfunny.md) | [1-pager](summaries/56-getting-serious-unfunny.md) |  |
| #57 | SemEval-2026 Task 1: MWAHAHA - Models Write Automatic Humor And Humans Annotate | 2026 | SemEval-2026 | — | — | — | no open PDF Task-overview paper not yet published (SemEval-2026 proceedings pending as of July 2026). |
| Part 8 (pre-LLM anchor) | [SemEval-2021 Task 7: HaHackathon, Detecting and Rating Humor and Offense](https://aclanthology.org/2021.semeval-1.9/) | 2021 | SemEval-2021 | [pdf (15p)](pdfs/x09-hahackathon.pdf) | [md](md/x09-hahackathon/x09-hahackathon.md) | [1-pager](summaries/x09-hahackathon.md) |  |
| Part 8 (pre-LLM anchor) | [SemEval-2020 Task 7: Assessing Humor in Edited News Headlines (Humicroedit & FunLines)](https://aclanthology.org/2020.semeval-1.7/) | 2020 | SemEval-2020 | [pdf (13p)](pdfs/x10-humicroedit.pdf) | [md](md/x10-humicroedit/x10-humicroedit.md) | [1-pager](summaries/x10-humicroedit.md) |  |
| Part 8 (pre-LLM anchor) | [Humor Detection: A Transformer Gets the Last Laugh (rJokes)](https://aclanthology.org/D19-1372/) | 2019 | EMNLP 2019 | [pdf (5p)](pdfs/x11-rjokes-last-laugh.pdf) | [md](md/x11-rjokes-last-laugh/x11-rjokes-last-laugh.md) | [1-pager](summaries/x11-rjokes-last-laugh.md) | The companion rJokes corpus paper (LREC 2020) is not downloaded separately. |
| Part 8 (pre-LLM anchor) | [UR-FUNNY: A Multimodal Language Dataset for Understanding Humor](https://aclanthology.org/D19-1211/) | 2019 | EMNLP 2019 | [pdf (11p)](pdfs/x12-ur-funny.pdf) | [md](md/x12-ur-funny/x12-ur-funny.md) | [1-pager](summaries/x12-ur-funny.md) |  |
| Part 8 (also) | [Re-defining Humor Data Objects for AI Humor Research](https://arxiv.org/abs/2605.25171) | 2026 | arXiv:2605.25171 | [pdf (10p)](pdfs/x13-redefining-humor-data.pdf) | [md](md/x13-redefining-humor-data/x13-redefining-humor-data.md) | [1-pager](summaries/x13-redefining-humor-data.md) |  |

## Part 9 - Surveys & Resources

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #58 | [Who's Laughing Now? An Overview of Computational Humour Generation and Explanation](https://arxiv.org/abs/2509.21175) | 2025 | INLG 2025 | [pdf (15p)](pdfs/58-whos-laughing-now.pdf) | [md](md/58-whos-laughing-now/58-whos-laughing-now.md) | [1-pager](summaries/58-whos-laughing-now.md) |  |
| #59 | [Large Language Models for Subjective Language Understanding: A Survey](https://arxiv.org/abs/2508.07959) | 2025 | arXiv:2508.07959 | [pdf (50p)](pdfs/59-subjective-language-survey.pdf) | [md](md/59-subjective-language-survey/59-subjective-language-survey.md) | [1-pager](summaries/59-subjective-language-survey.md) |  |
| #60 | [A Survey of Pun Generation: Datasets, Evaluations and Methodologies](https://arxiv.org/abs/2507.04793) | 2025 | arXiv:2507.04793 | [pdf (22p)](pdfs/60-pun-generation-survey.pdf) | [md](md/60-pun-generation-survey/60-pun-generation-survey.md) | [1-pager](summaries/60-pun-generation-survey.md) |  |
| #61 | [A Survey on Approaches to Computational Humor Generation](https://aclanthology.org/2020.latechclfl-1.4/) | 2020 | LaTeCH-CLfL 2020 | [pdf (13p)](pdfs/61-humor-generation-survey-2020.pdf) | [md](md/61-humor-generation-survey-2020/61-humor-generation-survey-2020.md) | [1-pager](summaries/61-humor-generation-survey-2020.md) |  |
| #62 | [Computational Humor Modeling: A Survey on the State of the Art](https://dl.acm.org/doi/10.1145/3778357) | 2026 | ACM Computing Surveys 58(7):177 | [pdf (38p)](pdfs/62-humor-modeling-survey.pdf) | [md](md/62-humor-modeling-survey/62-humor-modeling-survey.md) | [1-pager](summaries/62-humor-modeling-survey.md) | ACM DL; likely paywalled/bot-blocked. |

## Adjacent - Sarcasm & Humor Styles

| Ref | Paper | Year | Venue | PDF | Markdown | Summary | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| #63 | [SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding](https://arxiv.org/abs/2408.11319) | 2024 | arXiv:2408.11319 | [pdf (18p)](pdfs/63-sarcasmbench.pdf) | [md](md/63-sarcasmbench/63-sarcasmbench.md) | [1-pager](summaries/63-sarcasmbench.md) |  |
| #64 | [Is Sarcasm Detection a Step-by-Step Reasoning Process in Large Language Models?](https://arxiv.org/abs/2407.12725) | 2025 | AAAI 2025 | [pdf (17p)](pdfs/64-sarcasm-step-by-step.pdf) | [md](md/64-sarcasm-step-by-step/64-sarcasm-step-by-step.md) | [1-pager](summaries/64-sarcasm-step-by-step.md) |  |
| #65 | [A Two-Model Approach for Humour Style Recognition](https://arxiv.org/abs/2410.12842) | 2024 | arXiv:2410.12842 | [pdf (16p)](pdfs/65-humour-style-recognition.pdf) | [md](md/65-humour-style-recognition/65-humour-style-recognition.md) | [1-pager](summaries/65-humour-style-recognition.md) |  |

## Not in the library (and why)

- **T1 — Semantic Mechanisms of Humor (Script-based Semantic Theory of Humor)**: Book; no open-access PDF.
- **T2 — The General Theory of Verbal Humor (GTVH)**: Paywalled journal article / book; no open-access PDF.
- **T3 — Inside Jokes: Using Humor to Reverse-Engineer the Mind**: Book; no open-access PDF.
- **T4 — The Linguistic Analysis of Jokes**: Book; no open-access PDF.
- **T5 — Incongruity-Resolution & Appropriate Incongruity**: Book chapters; no open-access PDF.
- **#57 — SemEval-2026 Task 1: MWAHAHA - Models Write Automatic Humor And Humans Annotate**: Task-overview paper not yet published (SemEval-2026 proceedings pending as of July 2026).

