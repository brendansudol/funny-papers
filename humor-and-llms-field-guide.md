# Getting the Joke: Humor and Large Language Models
### A curated field guide, from humor theory (1900) to the LLM era (2026)

**Primary focus:** (1) explaining/understanding jokes and *why* things are funny, and (2) generating new jokes.
**Extended scope:** multimodal/visual humor, evaluation methodology, situated/live humor, safety, cross-cultural humor, and adjacent areas (sarcasm, humor styles).
**Coverage:** foundational theory and classic computational humor (1900–2020) plus recent LLM-era work 2022–2026 (the bulk from 2023 on). **Compiled:** June 2026 · **Revised:** July 2026.

This is a curated, not exhaustive, guide: it prioritizes papers that introduce a benchmark, dataset, method, or conceptual frame, and deliberately omits routine humor-detection work unless it changes how joke explanation, generation, evaluation, multimodality, safety, or cross-cultural humor is studied. Each entry notes **method**, **dataset**, and **key findings**, with a tag line for publication status/type. Titles link to arXiv/ACL/DOI where available.

**Tag legend:** `theory` · `peer-reviewed` · `preprint` · `workshop` · `dataset` · `method` · `benchmark` · `HCI study` · `survey`. (Preprint = arXiv/OpenReview not yet confirmed in a reviewed venue as of compilation. Workshop = peer-reviewed workshop or shared-task venue — refereed, but typically lighter-touch than main conferences; applied uniformly, covering WASSA, CHum, CMCL, LM4UC, LLMSEC, ACL SRW, LaTeCH-CLfL, and SemEval shared tasks.)

### The guiding lens, operationalized

A single idea organizes the field: **humor is mechanism × medium × audience × context.** "Funny" is rarely one scalar, and most apparently contradictory results trace back to which of these four a paper holds fixed.

| Axis | Examples | Why it matters |
| --- | --- | --- |
| **Mechanism** | pun, incongruity-resolution, script opposition, benign violation | what makes the joke work |
| **Medium** | text, audio, image, comic, video, live performance | what evidence the model must process |
| **Audience** | Gen-Z Instagram users, workplace colleagues, Oogiri voters, stand-up crowds | what counts as funny or acceptable |
| **Context** | topical news, culture, workplace, emotional support, safety boundary | whether the joke lands or crosses a line |

This is why ChatGPT can beat laypeople on short blind-rated jokes (#31), fail at explaining corrupted puns (#4), trail humans on multimodal visual humor (#25), and be useful-but-bland for professional comedians (#41) — all at once.

---

## Quick reference: which papers answer which question?

- **"Why is this joke funny?" (explanation/understanding)** → Hessel et al. (#1), HumorBench (#3), Pun Unintended (#4), Comparing Apples to Oranges (#5), "A good pun is its own reword" (#6), ExPUNations (#7), Phunny (#8), IRS / Cartoon Captionist (#24), BottleHumor (#27).
- **"How do we generate better jokes?"** → Are U a Joke Master (#10), CLoT (#11), LoL (#12), HumorGen (#13), Kim & Chilton (#14), Small But Funny (#15), Witscript line (#17), Jokeasy (#19), Multi-Agent Comedy Club (#20), HUMORCHAIN (#28), HOMER (#29).
- **"How do we know if it's funny / measure it?"** → Gorenz & Schwarz (#31), Crowd Score (#32), Is GPT-4 Good Enough to Evaluate Jokes? (#33), Cards Against LLMs (#34), HumorRank (#35), Who Laughs with Whom (#36), From Punchlines (#37), Oogiri multi-dimensional (#38), Oogiri-Master (#39).
- **"Does humor competence generalize across joke types?"** → Phunny (#8), One Joke to Rule them All (#40).
- **"Does it work in the real world / on stage?"** → A Robot Walks into a Bar (#41), Improvised Theatre deployment (#42), Theater Stage as Laboratory (#43), StandUp4AI (#44), Not All Jokes Land (#45).
- **"When does humor cross a line?"** → Engagement Undermines Safety (#47), Harm or Humor (#48), Using Humor to Bypass Safety Guardrails (#49); pre-LLM anchor: HaHackathon (Part 8).
- **"Does the joke survive translation or travel across cultures?"** → Culture-Aware Captioning (#30), Chumor (#50), CFunModel (#51), Pun2Pun (#52), Psychology-Driven Translation (#53), Not Funny Anymore (#54), Jokes or Gibberish (#55).
- **"What data should I train or evaluate on?"** → Part 8 (Getting Serious #56, MWAHAHA #57, and the pre-LLM anchors), plus the `dataset`-tagged entries throughout.
- **"What's the underlying theory?"** → SSTH (T1), GTVH (T2), Inside Jokes (T3), Ritchie (T4), incongruity-resolution / appropriate incongruity (T5), benign violation + psychological distance (T6).

---

## Theory Foundations (computationally useful)

These predate the LLM era but underpin almost everything that follows. Read these first: the recurring LLM finding — that models reproduce joke *structure* without grasping the *mechanism* — only makes sense once you know what the mechanism is.

### T1. [Semantic Mechanisms of Humor](https://link.springer.com/book/10.1007/978-94-009-6472-3) — Script-based Semantic Theory of Humor (SSTH)
Victor Raskin — **1985** (Reidel/Springer) · `theory`
- **Core claim:** The first formal, exclusively linguistic theory of verbal humor. A text is funny when it is compatible with two semantic *scripts* that overlap and are *opposed* (real/unreal, normal/abnormal, possible/impossible); the punchline triggers the switch.
- **Why it matters here:** Root of every "script opposition" / "incongruity" framing in computational humor.
- **Note:** Dense; the core idea travels fine via secondary summaries.

### T2. The General Theory of Verbal Humor (GTVH)
Salvatore Attardo & Victor Raskin — **1991** (*HUMOR* 4:293–347); expanded in Attardo, *Linguistic Theories of Humor* — **1994** · `theory`
- **Core claim:** Extends SSTH into the most widely accepted theory of verbal humor. Models any joke via six hierarchical *Knowledge Resources*: Script Opposition, Logical Mechanism, Situation, Target, Narrative Strategy, Language.
- **Why it matters here:** The most *engineerable* theory — a vocabulary for decomposing jokes that maps onto annotation schemas, joke-similarity metrics, and rubric-based evaluation. Directly operationalized by HOMER (#29) and HumorRank (#35). If you internalize one framework, make it this.
- **Note:** Read via Attardo 1994 or a summary rather than the dense 1991 article.

### T3. [Inside Jokes: Using Humor to Reverse-Engineer the Mind](https://mitpress.mit.edu/9780262518697/inside-jokes/)
Matthew Hurley, Daniel Dennett & Reginald Adams — **2011** (MIT Press) · `theory`
- **Core claim:** Evolutionary + cognitive theory (a descendant of incongruity-resolution). Humor is the brain's pleasure-reward for detecting and "debugging" a mistaken epistemic commitment in an active mental space.
- **Why it matters here:** The cleanest bridge from humor theory to an ML mindset; frames humor as a computational/epistemic process. Most readable of the three.

### T4. [The Linguistic Analysis of Jokes](https://www.routledge.com/The-Linguistic-Analysis-of-Jokes/Ritchie/p/book/9781138008731)
Graeme Ritchie — **2004** (Routledge) · `theory`
- **Core claim:** A rigorous, AI-oriented analysis of joke mechanisms — incongruity-resolution models, GTVH, joke similarity, the structure of puns, and early computational studies.
- **Why it matters here:** Written by a computational-linguistics/AI researcher (co-creator of JAPE; see Part 2); the most precise pre-LLM attempt to formalize what makes jokes work, especially puns.

### T5. Incongruity-Resolution & "Appropriate Incongruity"
Suls (1972), two-stage model; Elliott Oring (esp. *Engaging Humor*, 2003; "appropriate incongruity") · `theory`
- **Core claim:** The modern workhorse view: humor = perceiving an incongruity and then *resolving* it. Oring sharpens this: not all incongruity is funny; the incongruity must be *appropriate* (fitting/resolvable in a way that feels apt).
- **Why it matters here:** Explains why models that detect an oddity still miss the joke — detection of incongruity ≠ apt resolution. Directly operationalized as supervision in IRS (#24); the conceptual basis for HumorBench's "elements" and BottleHumor's knowledge extraction.

### T6. Benign Violation Theory (BVT) & Psychological Distance
Peter McGraw & Caleb Warren — **2010** (*Psychological Science*), building on Tom Veatch's earlier formal theory of humor (1998), plus distance follow-ups (2012, 2014) · `theory`
- **Core claim:** Something is funny when it is simultaneously a *violation* (of a norm/expectation/how-things-should-be) and *benign* (safe, playful, acceptable). The two-condition test governs the boundary between funny and offensive. The original five-experiment paper showed benign moral violations elicit amusement alongside disgust.
- **Psychological-distance follow-ups:** McGraw, Warren, Williams & Leonard, "Too Close for Comfort, or Too Far to Care?" (*Psychological Science*, 2012, 23:1215–1223) and McGraw, Williams & Warren, "The Rise and Fall of Humor" (*Social Psychological and Personality Science*, 2014, 5:566–572). The Hurricane Sandy longitudinal study found humorous responses *rose, peaked, then fell* over ~100 days — an inverted-U "comedic sweet spot." This is the empirical basis for "comedy = tragedy + time," and the levers that make a violation benign (weak norm commitment, distance, an alternative benign reading) are the theory most directly relevant to the harmful-humor boundary in Part 6.

### Also worth knowing
- **Seana Coulson, *Semantic Leaps* (2001)** `theory` — frame-shifting and conceptual blending; the cognitive-semantics account of how a punchline forces reinterpretation. (Adjacent formalizations of the same machinery: Giora's graded salience / optimal innovation, and relevance-theoretic accounts such as Yus.)
- **Rod Martin, *The Psychology of Humor: An Integrative Approach* (2007; 2nd ed. 2018 w/ Ford)** `theory` — the standard psychology reference (cognitive, social, personality, developmental, physiological).
- **Rod Martin, Puhlik-Doris, Larsen, Gray & Weir, the Humor Styles Questionnaire (2003, *J. Research in Personality* 37:48–75)** `theory` — the 32-item instrument operationalizing the four humor styles (affiliative, self-enhancing / aggressive, self-defeating). The measurement source behind the styles used as generation conditions and judge personas (#32, #65).
- **Robert Provine, *Laughter: A Scientific Investigation* (2000); "Laughter punctuates speech" (1993)** `theory` — most everyday laughter follows ordinary conversation, not jokes; laughter is primarily a *social* signal. A crucial caveat for using audience laughter as humor ground-truth (cf. StandUp4AI #44).
- **Arthur Asa Berger, 45 humor techniques ("Three Holy Men Get Haircuts," 2016; orig. *An Anatomy of Humor*, 1993)** `theory` — a taxonomy of 45 joke techniques in four families (language, logic, identity, action). Berger notes all 45 reduce to incongruity, so the techniques describe *how* the twist is engineered while the theories explain *why* it's funny.
- **Marvin Minsky, "Jokes and the Logic of the Cognitive Unconscious" (1980)** `theory` — AI pioneer casting humor as debugging of faulty reasoning; a direct ancestor of *Inside Jokes*.
- **Scott Dikkers, *How to Write Funny* — the eleven "funny filters"** — the leading *practitioner* taxonomy, from The Onion's founding editor: irony, character, reference, shock, parody, hyperbole, wordplay, analogy, madcap, misplaced focus, metahumor. The craft-side complement to Berger's academic 45 — and directly relevant to #31, which blind-tests ChatGPT against real Onion headlines.
- **Classical bedrock:** superiority (Hobbes, after Plato/Aristotle), relief (Freud, *Jokes and Their Relation to the Unconscious*, 1905), incongruity (Kant, Schopenhauer; Koestler's "bisociation," *The Act of Creation*, 1964), and Bergson's *Laughter* (1900). Neither superiority nor relief survives as a complete account, but both live on in the modern frameworks: superiority as the GTVH's *Target* knowledge resource (many jokes ridicule someone), relief as the tension-and-release rhythm at the heart of comedy craft (setups, punchlines, callbacks).

---

## Part 1 — Explaining & Understanding Jokes

Throughline: LLMs recognize/rank humor better than they explain it. Explanation is **harder to fake than detection — but not foolproof**: models can still rationalize non-jokes or produce post-hoc explanations that merely sound plausible (see Jentzsch & Kersting, #2).

### 1. [Do Androids Laugh at Electric Sheep? Humor "Understanding" Benchmarks from The New Yorker Caption Contest](https://arxiv.org/abs/2209.06293)
Hessel, Marasović, Hwang, Lee, Da, Zellers, Mankoff & Choi — **ACL 2023** · `peer-reviewed` `benchmark`
- **Method:** Three tasks on New Yorker cartoons — caption/cartoon matching, quality ranking, and explanation generation.
- **Dataset:** 704 cartoons with thousands of finalist captions (2.7K high-quality); explanations annotated with required world knowledge.
- **Findings:** The foundational benchmark; models trail humans on all three tasks, widest on explanation. Concretely: the best from-pixels model hit 62% on 5-way matching vs. 94% for humans, GPT-4 (5-shot) reached 84.5% on matching *given human-written scene descriptions* — and even then, human-authored explanations were preferred head-to-head over GPT-4's in more than two-thirds of cases. Everything downstream builds on it.

### 2. [ChatGPT is fun, but it is not funny! Humor is still challenging LLMs](https://arxiv.org/abs/2306.04563)
Jentzsch & Kersting — **WASSA 2023** · `workshop`
- **Method:** Prompt-based experiments on generation, explanation, and detection (GPT-3.5 era).
- **Dataset:** 1,008 prompted jokes plus hand-built explanation/detection items.
- **Findings:** Over 90% of 1,008 jokes collapsed onto the same 25 jokes; the model explained real jokes well but **fabricated plausible explanations for non-jokes** — the canonical caution that fluent explanation ≠ comprehension. (Later work notes the "Tell me a joke" prompt wasn't optimized for diversity.)

### 3. [Which LLMs Get the Joke? Probing Non-STEM Reasoning Abilities with HumorBench](https://arxiv.org/abs/2507.21476)
Narad, Suresh, Chen, Dysart-Bricken, Mankoff, Nowak, Zhang & Jain — **2025** (arXiv:2507.21476) · `preprint` `benchmark`
- **Method:** Open-ended *explanation*: given a cartoon description + caption, articulate the joke; graded by LLM-judge against a rubric of discrete verifiable "elements."
- **Dataset:** ≈300 expert-annotated cartoon–caption pairs from the New Yorker Caption Contest (top-3 finalists) and Cartoonstock.
- **Findings:** STEM-reasoning ability transfers to humor comprehension; STEM-only-trained models still do well; test-time "thinking" budgets give mixed gains; on the harder HumorBench-hard subset, no current LLM exceeds 60%. Best recent pick for explanation specifically.
- **Lineage:** From the same UW / UW–Madison group behind the NeurIPS caption-preference dataset (#22), with Bob Mankoff — former New Yorker cartoon editor — as co-author; deliberately isolates objective comprehension from subjective preference alignment.

### 4. [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://arxiv.org/abs/2509.12158)
Zangari, Marcuzzo, Albarelli, Pilehvar & Camacho-Collados — **EMNLP 2025** · `peer-reviewed` `benchmark`
- **Method:** Reformulates pun benchmarks (e.g., swap the pun word for a random one); semi-structured rationales; 7 LLMs + RoBERTa; temp 0; human eval.
- **Dataset:** PunEval (2,589, cleaned SemEval-2017 Task 7) + a JOKER subset (632 puns / 632 non-puns).
- **Findings:** Subtle edits that destroy the pun still get labeled puns — structure-matching, not comprehension; documents "regressive sycophancy." The sharpest "understanding is an illusion" result.

### 5. [Comparing Apples to Oranges: LLM Humour Understanding from Traditional Puns to Topical Jokes](https://arxiv.org/abs/2507.13335)
Loakman, Thorne & Lin — **EMNLP Findings 2025** · `peer-reviewed` `dataset`
- **Method:** Zero-shot explanation across four joke types; human eval + automatic metrics + LLM judge; topical case study.
- **Dataset:** 600 jokes across homographic puns, heterographic puns, non-topical Reddit, and topical Reddit jokes, each with a human reference explanation (→ 4,800 explanations).
- **Findings:** No model reliably explains all four types; topical humor is hardest; DeepSeek-R1's math/code reasoning does **not** transfer to humor's common-sense incongruity reasoning.

### 6. ["A good pun is its own reword": Can Large Language Models Understand Puns?](https://aclanthology.org/2024.emnlp-main.657/)
Xu, Yuan, Chen & Yang — **EMNLP 2024** · `peer-reviewed`
- **Method:** Pun recognition, explanation, and generation with new ICL-suited metrics; dual-biased prompts whose "reason" doubles as the explanation; fine-grained punchline checks.
- **Dataset:** SemEval-2017 Task 7 + the ExPun corpus (hom/het/non-puns); 8 LLMs (7B open models through GPT-4-Turbo, Claude-3-Opus).
- **Findings:** Lower true-negative than true-positive rate (non-puns that resemble puns fool models); identifies the "lazy pun generation" pattern (both senses jammed into one line); strong models still do respectably.

### 7. [ExPUNations: Augmenting Puns with Keywords and Explanations](https://arxiv.org/abs/2210.13513)
Sun, Narayan-Chen, Oraby, Cervone, Chung, Huang, Liu & Peng — **EMNLP 2022** · `peer-reviewed` `dataset`
- **Method:** Augments a pun corpus with fine-grained human annotations (keywords, natural-language explanations, funniness ratings) supporting both explanation and generation tasks.
- **Dataset:** ExPun — the first richly explanation-annotated pun dataset; widely reused (e.g., by HumorBench #3 and "A good pun" #6).
- **Findings:** Establishes "explain the pun in natural language" as a trainable/benchmarkable task; the anchor resource for the pun-explanation lineage.

### 8. ["What do you call a dog that is incontrovertibly true? Dogma": Testing LLM Generalization through Humor (Phunny)](https://aclanthology.org/2025.acl-long.1117/)
Cocchieri, Ragazzi, Italiani, Tagliavini & Moro — **ACL 2025** · `peer-reviewed` `benchmark` `dataset`
- **Method:** A pun-based question-answering benchmark manually curated for *novelty* to minimize data contamination; three tasks over a fixed structural schema — pun comprehension, resolution, and generation — plus a detailed error analysis.
- **Dataset:** Phunny (novel, human-written structured puns).
- **Findings:** Most LLMs struggle to generalize even on structurally simple tasks, consistently underperforming the human baseline. The natural complement to Pun Unintended (#4): that paper shows models fooled by *corrupted familiar* puns; Phunny asks whether they can handle *genuinely novel* ones at all. Together they bracket the memorization question.

### 9. [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](https://arxiv.org/abs/2412.05315)
Ashwin Baluja — **CHum 2025** · `workshop` `method`
- **Method:** Presents the LLM with both the text and a TTS-generated *spoken* form of a joke for phonetic/timing cues; CoT prompting where the reasoning doubles as explanation.
- **Dataset:** Existing pun datasets, zero/few-shot.
- **Findings:** Multimodal (text+audio) prompting beats text-only on pun understanding/explanation — some "understanding" failures are really modality limits (puns live in sound).

---

## Part 2 — Generating Jokes

Throughline: **generic linear chain-of-thought is poorly matched to humor generation; successful systems use structured creative search, script opposition, persona diversity, retrieval, or generate–evaluate–revise loops.** That umbrella covers CLoT, LoL, HumorGen, HOMER, HUMORCHAIN, Witscript, Jokeasy, and Multi-Agent Comedy Club alike.

**Pre-LLM foundations (historical grounding).** Computational humor long predates LLMs. Template-and-schema systems generated puns and riddles — Binsted & Ritchie's [**JAPE**](https://arxiv.org/abs/cmp-lg/9406022) ("An implemented model of punning riddles," AAAI 1994, built on hand-crafted lexicons and a homophone list) and its successor **STANDUP** (Ritchie et al. 2007, which moved to WordNet plus pronunciation dictionaries); **HAHAcronym** (Stock & Strapparava 2005) produced humorous acronyms; and Mihalcea & Strapparava's "Making Computers Laugh" (HLT/EMNLP 2005) pioneered humor *recognition*. Their lasting lesson — conceded by the authors themselves (the paper's own judging panel rated JAPE's output "jokes, but pathetic ones") — anchors this bibliography's synthesis: structure can be mechanized, but mechanized structure alone yields weak humor.

### Pun / wordplay generation

### 10. [Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM](https://aclanthology.org/2024.findings-acl.51/)
Chen, Yang, Hu, Chen, Lan, Cai, Zhuang, Lin, Lu & Zhou — **Findings of ACL 2024** · `peer-reviewed` `method` `dataset`
- **Method:** Multi-stage curriculum *preference* learning with an improved DPO to jointly optimize pun-structure and humor preferences (multi-objective alignment).
- **Dataset:** ChinesePun (2.1k annotated puns); evaluated on Chinese + English (SemEval) benchmarks.
- **Findings:** Significantly beats baselines on both languages; the most relevant recent pun-*generation* paper. (Pre-LLM pun-generation context: AmbiPun, Context-Situated Pun Generation, and "A Unified Framework for Pun Generation with Humor Principles," all EMNLP 2022; for a novelty-controlled test of pun comprehension *and* generation, see Phunny, #8.)

### One-liners, templates & multistep reasoning

### 11. [Let's Think Outside the Box: Leap-of-Thought in LLMs with Creative Humor Generation (CLoT)](https://arxiv.org/abs/2312.02439)
Zhong, Huang, Gao, Wen, Lin, Zitnik & Zhou — **CVPR 2024** · `peer-reviewed` `method` `dataset`
- **Method:** Argues CoT hurts creativity; instruction-tunes on leap-of-thought data, then "explorative self-refinement" exploring links between unrelated concepts.
- **Dataset:** Oogiri-GO (130k+ multimodal/multilingual samples from the Oogiri game).
- **Findings:** The canonical generation-method paper; improves humor generation and transfers to other creativity tasks.

### 12. [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps (LoL)](https://arxiv.org/abs/2410.10370)
Wang et al. — **ICLR 2025** · `peer-reviewed` `method`
- **Method:** Treats humor as multi-hop reasoning; RL where GPT-4o extracts each response's reasoning logic; injects external knowledge to fight knowledge-graph sparsity.
- **Findings:** Knowledge-augmented multi-hop reasoning improves both judgment and generation; addresses CLoT's weakness on knowledge-sparse reasoning.

### 13. [HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation](https://arxiv.org/abs/2604.09629)
Ajayi & Mitra — **2026** (arXiv:2604.09629) · `preprint` `method` `dataset`
- **Method:** Mixture-of-Thought with six cognitive personas (Absurdist, Cynic, …) grounded in humor theory; distilled data fine-tunes a 7B student; tests DPO and offline group-relative RL (O-GRPO). Evaluated on SemEval-2026 Task 1 (MWAHAHA, #57) headlines and Humor Transfer Bench.
- **Findings:** 7B models beat larger instruct baselines; two notable null results — neither DPO nor O-GRPO beat plain SFT (data quality > optimization), and distilling the teacher's *reasoning traces* usually hurts ("the explainer trap"). Also reports that fine-tuning on stand-up transcripts *regressed* text-native humor (performance humor ≠ written humor).
- **Disclosure:** Companion paper to HumorRank (#35), by the same authors.

### 14. [AI Humor Generation: Cognitive, Social and Creative Skills for Effective Humor](https://arxiv.org/abs/2502.07981)
Kim & Chilton — **2025** · `preprint` `HCI study` `method`
- **Method:** 4-stage "HumorSkills" pipeline (observe → diverge → generate ~30 captions → a Gen-Z expert agent ranks top 5) vs. top Instagram comments and a GPT-4o baseline.
- **Dataset:** Gen-Z Instagram caption humor; rating survey (20 images × 15 captions).
- **Findings:** The strongest positive result — significantly funnier than the baseline and statistically on par with top human captions (p≈0.053). Caveat: one narrow audience.

### 15. [Small But Funny: A Feedback-Driven Approach to Humor Distillation](https://arxiv.org/abs/2402.18113)
Ravi, Huber, Shrivastava, Sagar, Aly, Shwartz & Einolghozati — **ACL 2024** · `peer-reviewed` `method`
- **Method:** Distills humor into Small Language Models by giving the teacher LLM a dual role — data *generator* and *critic* providing feedback — rather than imitation alone.
- **Findings:** Feedback markedly narrows the small-vs-large gap on humor generation; key paper for training compact humor models.

### 16. [Humor Mechanics: Advancing Humor Generation with Multistep Reasoning](https://computationalcreativity.net/iccc24/papers/ICCC24_paper_128.pdf)
Tikhonov & Shtykovskiy — **ICCC 2024** (arXiv:2405.07280) · `peer-reviewed` `method`
- **Method:** Iterative multistep reasoning for one-liner generation (e.g., associating distant concepts as a preliminary step), evaluated against alternative pipelines and human baselines.
- **Findings:** Multistep generation beats single-shot; importantly, a single "universal humor prompt" distilling human preference proves *insufficient* — humor's subjectivity resists one prompt.

### Craft-based / expert-heuristic generation

### 17. [Witscript 3: A Hybrid AI System for Improvising Jokes in a Conversation](https://arxiv.org/abs/2301.02695)
Joe Toplyn — **2023** (arXiv:2301.02695; earlier versions peer-reviewed: Witscript, **ICCC 2021**; Witscript 2, **ICCC 2022**) · `preprint` `method`
- **Method:** Encodes professional joke-writing algorithms (from a TV comedy writer) and combines them with LLM generation to improvise contextual conversational jokes. The evaluation companion — "Can AI Make Us Laugh? Comparing Jokes Generated by Witscript and a Human Expert" (**CHum 2025** · `workshop`) — pits Witscript against a human expert before live audiences, measuring audience laughter directly.
- **Findings:** The clearest attempt to bake explicit comedy-writing craft heuristics into a generation system — a useful contrast to learning/persona approaches — and, via the companion, one of the very few AI-vs-human joke comparisons scored by real audience laughter rather than raters.

### Topical satire & retrieval

### 18. [Grounded Satirical Generation with RAG](https://arxiv.org/abs/2605.10853)
arXiv:2605.10853 — **2026** · `preprint` `method`
- **Method:** RAG over current news to generate satirical dictionary definitions (Finnish context); new task-specific eval; 100 definitions annotated by six humans across conditions (culture, source-word type, RAG on/off).
- **Findings:** Outputs read as more *political* than *humorous*; topic-based word selection and RAG improve political relevance but **not** clearly funniness — an important warning for topical-comedy systems (relevance ≠ humor).

### Human–AI & multi-agent joke-writing workflows

### 19. [Jokeasy: Exploring Human-AI Collaboration in Thematic Joke Generation](https://arxiv.org/abs/2602.09496)
Ge et al. — **IASDR 2025** (arXiv 2026) · `peer-reviewed` `HCI study`
- **Method:** A search-enabled prototype with a dual-role LLM agent (material "scout" + prototype writer) and a visual canvas organizing retrieved web content into editable "inspiration blocks" through a multistage workflow.
- **Findings:** Targets the agency/control gap in plain chat interfaces for *thematic* (topical, fresh-material) joke writing — how people actually write jokes with AI, not just one-liner output.

### 20. [Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation](https://arxiv.org/abs/2602.14770)
Hong, Li, Rong, Shen & Lu — **2026** · `preprint` `method` `HCI study`
- **Method:** A controlled multi-agent sandbox for stand-up-style comedy writing. In the discussion condition, critic and audience threads are recorded, filtered, stored as *social memory*, and retrieved to condition later generations; the baseline omits discussion.
- **Findings:** Across 50 rounds (250 paired monologues) judged by five expert annotators (A/B preference + a 15-item rubric), the discussion condition **wins 75.6%** of comparisons and improves Craft/Clarity (Δ=0.440) and Social Response (Δ=0.422) — with occasional increases in aggressive humor. Moves past one-shot prompting and local feedback toward comedy's real social ecology (repeated audience reaction, community discussion).

**Also in this cluster (2026):** **COMIC** (arXiv:2603.11048) `preprint` — Content Optimization via Multi-agent Iterative Competition: a fully automated pipeline producing short SNL-style sketch-comedy *videos* from character references, with production-studio-style agent roles and LLM critics aligned to real viewer preferences mined from YouTube comedy corpora. **OpenMic** (Wu, Cao, Chen & Li; arXiv:2601.08288) `preprint` — an AutoGen-based multi-agent system turning a user's life topic into a 3–5-minute *Chinese* stand-up performance plus narrated video, jointly optimizing humor, timing, and performability (bridges to Part 7). Both push the multi-agent thread from written text toward performed, produced comedy — read alongside Part 5.

### 21. [One Does Not Simply Meme Alone: Co-Creativity Between LLMs and Humans](https://arxiv.org/abs/2501.11433)
arXiv:2501.11433 — **IUI 2025** · `peer-reviewed` `HCI study`
- **Method:** Three conditions (human-only, human+LLM, LLM-only) for meme generation; raters score funniness/creativity/shareability.
- **Dataset:** 335 (human) + 307 (collaborative) images; sampled for rating.
- **Findings:** Collaboration yields more ideas with less perceived effort; "AI as collaborator" rather than solo author.

---

## Part 3 — Multimodal & Visual Humor

Transition: the previous parts mix text-only and some image-caption work (CLoT/Oogiri-GO, HumorSkills, memes); this part treats **multimodal humor as the primary object** — cartoons, memes, comics, video, and visual satire. World knowledge and cross-panel/visual integration are the recurring bottlenecks.

### Cartoons & captions (the New Yorker line after Hessel)

### 22. [Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://arxiv.org/abs/2406.10522)
Zhang, Jain, Guo, Chen, Zhou, Suresh, Wagenmaker, Sievert, Rogers, Jamieson et al. — **NeurIPS 2024 (D&B)** · `peer-reviewed` `dataset` `benchmark`
- **Method:** A very large-scale cartoon-caption *preference* dataset and benchmark for ranking/generation, built from New Yorker contest crowd votes, with GPT-4 and human-judgment ranking metrics.
- **Dataset:** 365 contests (numbers 530–895), 2.2M+ captions, and 250M+ human ratings (funny / somewhat funny / unfunny) collected over ~8 years via the NEXT multi-armed-bandit crowdsourcing platform.
- **Findings:** The major large-scale resource extending Hessel's line. Headline results: SFT *hurts* the generation task, RLHF and DPO **underperform** on this creative objective, and even GPT-4 and Claude still **trail top human contestants** at producing winning captions — a sobering scale-isn't-enough result, given a quarter-billion ratings. (The same group later builds HumorBench, #3, to isolate comprehension from preference.)

### 23. [Bridging the Creativity Understanding Gap: Small-Scale Human Alignment Enables Expert-Level Humor Ranking](https://arxiv.org/abs/2502.20356)
arXiv:2502.20356 — **EMNLP Findings 2025** · `peer-reviewed` `method`
- **Method:** Aligns LLMs on a small set of human cartoon-caption judgments (20 caption pairs from 379 contests; 279 train / 100 test).
- **Findings:** A little human alignment pushes LLM humor *ranking* toward expert level — cheap alignment goes a long way on the ranking subproblem.

### 24. [Learning to Think Like a Cartoon Captionist: Incongruity-Resolution Supervision for Multimodal Humor Understanding](https://arxiv.org/abs/2604.15210)
Vural et al. — **2026** · `preprint` `method`
- **Method:** IRS (Incongruity-Resolution Supervision) decomposes visual humor understanding into three learnable stages — *incongruity modeling* (spotting the visual mismatch), *resolution modeling* (constructing a coherent reinterpretation), and *preference alignment* (scoring candidate interpretations against human judgments) — supervising the *intermediate reasoning trace*, not just the answer (continual pretraining → SFT on captionist-style traces → alignment with humor judgments).
- **Dataset:** New Yorker Cartoon Caption Contest (matching/ranking).
- **Findings:** Grounded explicitly in incongruity-resolution theory (T5), script opposition (T2), and frame-shifting (Coulson). The near-perfect bridge between humor theory and the cartoon-caption benchmark line: it operationalizes "why is this funny?" as an explicit, learnable reasoning process rather than black-box ranking.

### Visual humor, memes, comics & video

### 25. [HumorDB: Can AI Understand Graphical Humor?](https://arxiv.org/abs/2406.13564) *(ICCV camera-ready title; earlier arXiv title: "Is AI Fun? HumorDB…")*
Jain, dos Santos Alves Feitosa & Kreiman — **ICCV 2025** · `peer-reviewed` `dataset` `benchmark`
- **Method:** Image-only visual humor; three tasks (binary funny/not, 1–10 regression, pairwise "which is funnier?"); includes deliberately *modified* images to defeat memorization; attention/interpretability analysis.
- **Findings:** Models lag humans and often miss the humor-critical region — a clean "does it see the joke?" probe.

### 26. [YesBut: A High-Quality Annotated Multimodal Dataset for Evaluating Satire Comprehension of VLMs](https://arxiv.org/abs/2409.13592)
Nandy et al. — **EMNLP 2024** · `peer-reviewed` `dataset` `benchmark`
- **Method:** Two-panel comics with humorous *contradiction*; tasks graded from literal comprehension to deep narrative/satire interpretation.
- **Dataset:** Annotated contradictory-narrative comics; YesBut V2 expands to 1,262 multilingual images.
- **Findings:** Even strong VLMs struggle with juxtaposition-based humor; the go-to satire/contradiction benchmark.

### 27. [BottleHumor: Self-Informed Humor Explanation using the Information Bottleneck Principle](https://arxiv.org/abs/2502.18331)
Hwang, West & Shwartz — **Findings of ACL 2025** · `peer-reviewed` `method`
- **Method:** Uses the information-bottleneck principle to extract and iteratively refine the world knowledge a VLM needs to *explain* a meme/cartoon.
- **Findings:** Surfacing the right world knowledge improves explanations — extends the explanation interest into the visual setting and shows world knowledge is the bottleneck.

**Also in this section:** [Humor in Pixels / PixelHumor](https://arxiv.org/abs/2509.12248) (EMNLP Findings 2025, multi-panel online comics) `dataset`; [MemeReaCon](https://arxiv.org/abs/2505.17433) (Zhao et al., EMNLP 2025; 1,565 instances from 5 subreddits keeping image + post + comments) `benchmark`.

**Video humor:** **ExFunTube** — ["Can Language Models Laugh at YouTube Short-form Videos?"](https://arxiv.org/abs/2310.14159) (Ko et al., EMNLP 2023) `dataset` — is the early anchor for *video* humor explanation: funny short-form clips paired with explanations. [**v-HUB**](https://arxiv.org/abs/2509.25773) (Shi, Zhao, Zhou et al., 2025) `preprint` `benchmark` collects minimally verbal clips from Chaplin-era silent films plus user-generated video, with caption-matching, humor-explanation, and open-ended QA tasks — the purest "can it see the joke *in motion*, without language?" probe. All models drop sharply moving from text- to video-based evaluation, and adding audio (environmental sound) measurably helps: the video-side counterpart to HumorDB (#25), and a moving-picture echo of Baluja's puns-live-in-sound finding (#9).

### Theory-guided multimodal generation (2025–26)

### 28. [HUMORCHAIN: Theory-Guided Multi-Stage Reasoning for Interpretable Multimodal Humor Generation](https://arxiv.org/abs/2511.21732)
Zhang, Luo, Zhang & Su (Peking University) — **CVPR 2026** (arXiv:2511.21732) · `peer-reviewed` `method`
- **Method:** Embeds cognitive structures from humor + psychological theories (incongruity-resolution, benign violation, superiority) into a theory-guided multi-stage chain for humorous image captioning: visual semantic parsing → humor/psychology reasoning → a fine-tuned discriminator for evaluation.
- **Dataset:** Meme-Image-No-Text, Oogiri-GO, OxfordTVG-HIC.
- **Findings:** Outperforms SOTA baselines on human humor preference and Elo/Bradley–Terry scores; claims to be the first to explicitly embed humor-theory cognitive structures into multimodal humor generation.

### 29. [On the Wings of Imagination: Conflicting Script-based Multi-role Framework for Humor Caption Generation (HOMER)](https://arxiv.org/abs/2602.06423)
Shang, Sun, Ma & Huang — **ICLR 2026** (arXiv:2602.06423) · `peer-reviewed` `method`
- **Method:** GTVH-grounded multi-role LLM collaboration with retrieval: a conflicting-script extractor, a retrieval-augmented hierarchical imaginator, and a caption generator.
- **Findings:** Explicit script-opposition control beats CLoT/GPT-4o on funny-caption generation across seven models, with more originality and interpretability. The clearest GTVH-in-practice generation system.

### 30. [Culture-Aware Humorous Captioning: Multimodal Humor Generation across Cultural Contexts](https://arxiv.org/abs/2604.18091)
arXiv:2604.18091 — **2026** · `preprint` `method`
- **Method:** Conditions humorous caption generation on explicit cultural context, treating culture as a deep interpretive condition that changes which incongruity is foregrounded and how humor is verbalized.
- **Findings:** Connects controllable captioning with cultural alignment — a bridge between the multimodal and cross-cultural strands (Part 7).

---

## Part 4 — Evaluation Methodology & Whether LLMs Are Actually Funny

Two questions under everything: *how* do we measure funniness, and *are* LLMs funny? Headline verdicts genuinely conflict — "not funny" (#2) sits beside "funnier than most laypeople" (#31) — and that conflict is the point: **the verdict is task- and measurement-dependent.** (Foundational caveat: per Provine, see Theory, laughter is mostly a social signal, not a humor meter.)

### 31. [How Funny is ChatGPT? A Comparison of Human- and A.I.-Produced Jokes](https://doi.org/10.1371/journal.pone.0305364)
Gorenz & Schwarz — **PLOS One 2024** · `peer-reviewed`
- **Method:** Two blind human-rating studies — ChatGPT 3.5 vs. laypeople on three comedy tasks; and ChatGPT vs. real published satirical headlines (The Onion), ~200 raters.
- **Findings:** ChatGPT rated as funny or funnier than most laypeople and *no less funny* than professional satirical-news writers. Implication: the felt experience of humor may not be needed to produce it. The essential counterweight to #2.

### 32. [Crowd Score: A Method for the Evaluation of Jokes using Large Language Models](https://arxiv.org/abs/2212.11214)
Goes, Zhou, Sawicki, Grzes & Brown — **2022** · `preprint` `method`
- **Method:** LLM-as-judge with induced personalities (one per humor style) forming an AI "crowd" of voters, plus an auditing step checking each vote's explanation.
- **Dataset:** 52 jokes.
- **Findings:** Few-shot beats zero-shot; personalities behave plausibly. The conceptual root of rubric-guided LLM-judging used by HumorBench (#3) and HumorRank (#35). (Late 2022; included for lineage.)

### 33. [Is GPT-4 Good Enough to Evaluate Jokes?](https://computationalcreativity.net/iccc23/papers/ICCC-2023_paper_89.pdf)
Goes et al. — **ICCC 2023** · `peer-reviewed` `method`
- **Method:** The Crowd Score team's follow-up: GPT-4 as joke judge with role/persona descriptions and many-shot prompting, compared against human joke ratings.
- **Findings:** Argues *relative rankings* are more reliable than absolute funniness scores — the methodological bridge from Crowd Score's AI-crowd voting (#32) to today's pairwise/tournament evaluation (#35). A short but load-bearing link in the LLM-as-judge lineage.

### 34. [Cards Against LLMs: Benchmarking Humor Alignment in Large Language Models](https://aclanthology.org/2026.chum-1.4/)
Fettach, Bied, Toivonen & De Bie — **CHum 2026** (arXiv:2604.08757) · `workshop` `benchmark`
- **Method:** Five frontier models play Cards Against Humanity, selecting the funniest of ten cards across 9,894 rounds; framed as a humor *alignment* problem.
- **Findings:** All beat random but align only modestly with humans — and models agree with *each other* far more than with humans, partly from position/content biases. Raises whether LLM humor judgment is genuine preference or inference artifact.

### 35. [HumorRank: A Tournament-Based Leaderboard for Evaluating Humor Generation](https://arxiv.org/abs/2604.19786)
Ajayi & Mitra — **2026** (arXiv:2604.19786) · `preprint` `benchmark` `method`
- **Method:** Pairwise, GTVH-grounded LLM judgments aggregated via Adaptive Swiss tournament + Bradley–Terry into global rankings; 9 models on SemEval-2026 MWAHAHA (#57) + Humor Transfer Bench.
- **Findings:** Cross-judge stable (Llama/Qwen judges agree, Kendall τ≈0.89); strong humor depends on mastery of mechanisms (incongruity, conciseness, escalation, absurdity), not just scale. Pairwise/tournament is often more plausible than absolute funniness scores.
- **Disclosure:** Same authors as HumorGen (#13), and the leaderboard ranks their own HumorGen-7B 4th, above models an order of magnitude larger — consistent with, but not independent of, the "mechanisms over scale" headline. (One counter-signal to judge self-preference worries: the Llama judge ranks its own generations 8th of 9.)

### 36. [Who Laughs with Whom? Disentangling Humor Preferences across User Clusters and LLMs](https://arxiv.org/abs/2601.03103)
Murakami, Kamigaito, Takamura & Okumura — **2026** · `preprint`
- **Method:** Clusters Oogiri users by voting logs; estimates cluster-specific weights over interpretable preference factors (Bradley-Terry-Luce); elicits LLM preferences.
- **Findings:** Clusters have distinct preferences; LLM judgments resemble *particular* clusters, and persona prompting can steer an LLM toward a chosen cluster. Concrete evidence that humor isn't one scalar preference — audiences cluster.

### 37. [From Punchlines to Predictions: A Metric to Assess LLM Performance in Identifying Humor in Stand-Up Comedy](https://arxiv.org/abs/2504.09049)
arXiv:2504.09049 — **CMCL 2025** · `workshop` `method`
- **Method:** A statistical metric for zero-shot accuracy at *locating* funny lines in stand-up transcripts (fuzzy matching vs. ground truth); benchmarks several frontier + open models.
- **Findings:** Accuracy ~50%, persona tricks don't reliably help — spotting humor in long-form context remains hard.

### 38. [Assessing the Capabilities of LLMs in Humor: A Multi-dimensional Analysis of Oogiri Generation and Evaluation](https://arxiv.org/abs/2511.09133)
Sakabe, Kim, Hirasawa & Komachi — **AAAI 2026** (arXiv:2511.09133) · `peer-reviewed` `dataset` `method`
- **Method:** Argues a single "is it funny" score is too coarse and evaluates humor along *multiple dimensions* using Oogiri (Japanese improv comedy), for both generation (RQ1) and LLM-as-judge evaluation (RQ2) against human crowd annotations.
- **Dataset:** Expanded Oogiri datasets plus LLM-generated responses; generations from GPT-4.1, Gemini 2.5 Pro, and Claude Sonnet 4.
- **Findings:** LLMs generate between low- and mid-tier human level and show a notable **empathy deficit**, which also explains why their humor *evaluation* diverges from humans'. The six dimensions are Novelty, Clarity, Relevance, Intelligence, Empathy, and Overall Funniness; a key divergence is that LLMs prioritize *Novelty* while humans prioritize *Empathy* — the strongest argument here for multidimensional scoring over a single number.

### 39. [Oogiri-Master: Benchmarking Humor Understanding via Oogiri](https://arxiv.org/abs/2512.21494)
arXiv:2512.21494 — **2025** · `preprint` `benchmark` `dataset`
- **Method:** A benchmark (Oogiri-Master) plus corpus (Oogiri-Corpus) built for statistical robustness: each prompt is paired with ~100 diverse candidate responses, each rated *independently* by ~100 human judges with no visibility into others' votes — reducing the popularity bias inherent in platform-vote data (cf. Oogiri-GO, #11). Includes a quantitative analysis of the linguistic factors behind funniness (length, ambiguity, incongruity resolution) and derived predictive metrics.
- **Findings:** State-of-the-art models *approach human performance* on rating/understanding, and insight-augmented prompting improves results. Read against #38: understanding/rating (here) vs. generation (#38's low-to-mid-tier result) — the recognition ≫ origination gradient of Synthesis 1, observed inside a single humor format.

### 40. [One Joke to Rule them All? On the (Im)possibility of Generalizing Humor Detection](https://aclanthology.org/2026.chum-1.1/)
Turgeman, Shani & Shahaf — **CHum 2026** (arXiv:2508.19402) · `workshop` `method`
- **Method:** Transfer-learning experiments across four humor-detection datasets representing different humor types; varied training-diversity settings (1–3 datasets in training, tested on a novel type).
- **Findings:** Transfer is real but partial — up to 75% accuracy on unseen datasets; training on diverse sources improves transferability (+1.88–4.05%) with minimal in-domain cost; relations between humor types are *asymmetric*, with Dad Jokes surprisingly the best enabler of transfer yet the hardest target. The direct empirical test of whether "humor competence" is one thing — it mostly isn't (Synthesis 2), which is also Phunny's conclusion (#8) from the generation side.

---

## Part 5 — Situated Humor: Workplace, Supportive & Live Performance

Humor is context-bound; this part is about *where* the joke happens (audience and setting as first-class variables).

### 41. [A Robot Walks into a Bar: Can Language Models Serve as Creativity Support Tools for Comedy?](https://arxiv.org/abs/2405.20956)
Mirowski, Love, Mathewson & Mohamed — **FAccT 2024** · `peer-reviewed` `HCI study`
- **Method:** 3-hour "AI × Comedy" workshops with 20 professional comedians (Edinburgh Fringe + online); Creativity Support Index + focus groups.
- **Findings:** Outputs mostly *bland*, useful as scaffolding not punchlines; safety filtering/instruction-tuning erases minority perspectives — a creative and ethical failure.

### 42. [Designing and Evaluating Dialogue LLMs for Co-Creative Improvised Theatre](https://arxiv.org/abs/2405.07111)
Branch, Mirowski, Mathewson, Ppali & Covaci — **2024** (arXiv:2405.07111) · `preprint` `HCI study`
- **Method:** A month-long live deployment at the Edinburgh Festival Fringe: human improvisers performing nightly with LLM-driven conversational agents; studies audience and performer experience, multi-party dialogue constraints, interface/latency issues, and context-relevance failures.
- **Findings:** The field's most sustained *live* test of the challenges #43 names — timing, embodiment, audience interaction — observed on a real stage rather than posited. Improv's demand for instant, context-apt contributions exposes failure modes that offline benchmarks structurally miss.

### 43. [The Theater Stage as Laboratory: Review of Real-Time Comedy LLM Systems for Live Performance](https://arxiv.org/abs/2501.08474)
Mirowski, Mathewson & Branch — **CHum 2025** · `workshop` `survey`
- **Method:** Position paper/review arguing AI comedy must be evaluated under *live* conditions — real-time, embodied, audience-interactive — with improv as the ideal substrate.
- **Findings:** Names three challenge sets: embodiment/anthropomorphism, comedic timing/audience interaction, and human interpretation of absurd AI output. (Dramatron — Mirowski et al. 2023, "Co-Writing Screenplays and Theatre Scripts with Language Models," arXiv:2209.14958 — is the adjacent long-form scripted-theatre anchor.)

### 44. [StandUp4AI: A New Multilingual Dataset for Humor Detection in Stand-up Comedy Videos](https://arxiv.org/abs/2505.18903)
Barriere, Gomez, Hemamou, Callejas & Ravenet — **2025** · `preprint` `dataset`
- **Method:** Multimodal stand-up dataset in 7 languages (EN/FR/ES/IT/PT/HU/CS), 330+ hours, auto-annotated for audience laughter with a manually annotated validation subpart.
- **Findings:** The dataset anchor for the stand-up/video side — connects timing/delivery and laughter as a ground-truth signal. (Read alongside Provine, Theory: laughter ≠ jokes, so audience-laughter labels are a noisy humor proxy. Pre-LLM multimodal ancestor: UR-FUNNY, Part 8.)

### 45. [Not All Jokes Land: Evaluating LLMs' Understanding of Workplace Humor](https://arxiv.org/abs/2506.01819)
Shafiei & Saffari — **2025** · `preprint` `dataset`
- **Method:** Targets humor *appropriateness* in professional/industrial settings (304 annotated industry-specific humorous statements), where humor must be used carefully and no prior resource existed.
- **Findings:** Appropriateness is a distinct axis from funniness — context determines whether a joke should be told at all.

### 46. [Can AI Take a Joke—Or Make One? A Study of Humor Generation and Recognition in LLMs](https://dl.acm.org/doi/10.1145/3698061.3734388)
Quan, Ramakrishnan & Chin — **Creativity & Cognition (C&C) 2025** · `peer-reviewed` `HCI study`
- **Method:** Compares humor generation and recognition across GPT, Llama, and Gemini on shared prompts, with human raters classifying and Likert-rating outputs; focuses on supportive/emotionally sensitive contexts and humor roles (affiliative, self-defeating, or no-joke).
- **Findings:** Models produce fluent, varied humor but fall short on emotional realism and contextual appropriateness in supportive scenarios — underscoring the need for human calibration. Ties humor style to *when* humor helps vs. harms.

---

## Part 6 — Safety, Harm & Boundaries

Where jokes cross the line — the operational flip side of benign violation theory and psychological distance (T6). (The pre-LLM anchor for this whole strand is SemEval-2021 Task 7 HaHackathon, which jointly rated humor *and* offense; see Part 8.)

### 47. [Engagement Undermines Safety: How Stereotypes and Toxicity Shape Humor in Language Models](https://arxiv.org/abs/2510.18454)
Dogra et al. — **EACL 2026** (arXiv:2510.18454) · `peer-reviewed`
- **Method:** Casts humor generation as a safety testbed across six LLMs, jointly measuring humor, stereotypicality, and toxicity, plus information-theoretic incongruity analysis.
- **Findings:** A "Bias Amplification Loop" — both generators *and* evaluators rate stereotypical/toxic outputs as funnier, tilting pipelines toward harm. Single-objective "maximize funniness/engagement" yields weak guardrails — the opposite-end bookend to Mirowski et al.'s critique of over-aggressive filtering.

### 48. [Harm or Humor: A Multimodal, Multilingual Benchmark for Overt and Covert Harmful Humor](https://arxiv.org/abs/2603.17759)
arXiv:2603.17759 — **2026** · `preprint` `benchmark`
- **Method:** Benchmark for distinguishing safe humor from implicit/explicit harmful humor across modalities and languages.
- **Findings:** Gives the safety strand a concrete cross-modal/cross-lingual test bed for harmful-humor detection.

### 49. [Using Humor to Bypass Safety Guardrails in Large Language Models](https://aclanthology.org/2025.llmsec-1.3/)
Pedro Cisneros-Velarde — **LLMSEC 2025** (also arXiv:2504.06577, "Bypassing Safety Guardrails in LLMs Using Humor") · `workshop`
- **Method:** Treats humor as a jailbreak *strategy* — a fixed "Psst…" template that wraps the unedited unsafe request in comedic framing, needing no auxiliary LLM.
- **Findings:** Effective across many LLMs; both *removing* and *adding too much* humor reduce success — jailbreaking needs a balance between comedic framing and focus on the unsafe request. Humor is a safety-bypass vector, relevant to red-teaming.

---

## Part 7 — Cross-Cultural & Translation

Most of the field is English; humor is deeply cultural, so this is its own strand. (For multi-agent *Chinese stand-up generation*, see the OpenMic note in Part 2.)

### 50. [Chumor 1.0 / 2.0: Chinese Humor Understanding from Ruo Zhi Ba](https://arxiv.org/abs/2406.12754)
He et al. (Ruiqi He … Naihao Deng) — **2024–25** (1.0 arXiv:2406.12754; 2.0 in ACL Findings 2025, arXiv:2412.17729) · `peer-reviewed` `dataset`
- **Method:** Human-annotated explanations for culturally specific RZB jokes; direct + CoT prompting; 10 LLMs; A/B testing of human vs. LLM explanations by native speakers.
- **Findings:** Accuracy only slightly above random and far below human; human explanations vastly better than GPT-4o/ERNIE (LLMs "win" in ~2–3% of cases). English benchmarks overstate competence.

### 51. [CFunModel: A "Funny" Language Model Capable of Chinese Humor Generation and Processing](https://arxiv.org/abs/2503.20417)
arXiv:2503.20417 — **2025** · `preprint` `dataset` `method`
- **Method:** Builds CFunSet (160k+ entries, incl. 20k+ jokes from Tieba's "JokeBar"); multi-task across crosstalk response selection, humor recognition, joke generation/continuation, humor explanation, and crosstalk generation.
- **Findings:** Surpasses general LLMs on Chinese humor recognition tasks.

### 52. [Pun2Pun: Benchmarking LLMs on Textual-Visual Chinese-English Pun Translation](https://aclanthology.org/2025.acl-srw.23/)
Ma, Huang, Xu, Zhou & Wei — **ACL 2025 SRW** · `workshop` `benchmark`
- **Method:** Pun translation benchmark (textual + visual) with a Constant-Variable Optimization strategy and an "Overlap" quality metric preserving both mechanism and humor.
- **Findings:** Quantifies the "near-impossible" task of cross-lingual pun translation; strategy modeling helps stronger models most.

### 53. [Psychology-Driven Enhancement of Humour Translation](https://arxiv.org/abs/2507.09259)
Su, Zhu, Chen, Benavides Prado & Witbrock — **2025** · `preprint` `method`
- **Method:** A psychology-inspired Humour Decomposition Mechanism (HDM) using CoT + humor theory to optimize readability and preserve humor in translation.
- **Findings:** Average gains ~7.8% humor, ~2.8% fluency, ~6.1% coherence over baseline LLM translation.

### 54. [Not Funny Anymore: LLM Judges Confuse Literal Similarity for Humor in Translated Jokes](https://openreview.net/forum?id=fdrM652upk)
Rivera, Pochugari, Chan, Katakwar, Zhu & Saxon (Algoverse AI / Andrews Univ. / Univ. of Washington) — **LM4UC @ AAAI 2026 workshop** (OpenReview) · `workshop` `dataset` `method`
- **Method:** Reference-free humor-translation *evaluation* — LLM-as-judge rates how well a joke's humor survives translation, vs. human 5-point Likert ratings; introduces a correlation-based "literalness" metric in a multilingual embedding space (Procrustes-aligned token embeddings) to diagnose failures.
- **Dataset:** 162 English→Chinese and 76 English→Hindi joke pairs with human annotations; 7 LLM judges × prompting strategies (vanilla / CoT / self-consistency).
- **Findings:** Judges struggle (strict agreement near or below the 20% random baseline), and the failure is driven by an **over-literal bias** — models reward word-for-word fidelity over preserved comedic effect. A sharp caution for LLM-as-judge on creative cross-lingual tasks.

### 55. [Jokes or Gibberish? Humor Retention in Translation: NMT vs. LLM](https://www.mdpi.com/2673-6470/5/4/49)
Pituxcoosuvarn & Murakami — **Digital (MDPI) 2025**, 5(4):49 · `peer-reviewed`
- **Method:** Compares a neural machine translation (NMT) system against GPT-based translation (three prompts: GPT, GPT-P, GPT-Ex) for English→Thai joke translation; human annotation of joke preservation; McNemar test for distribution differences.
- **Findings:** GPT-based translation significantly beats NMT on humor retention; the explanation-enhanced prompt (GPT-Ex) preserves the most jokes (62.94% vs. 50.12% for NMT). Prompt engineering that surfaces humor mechanisms and cultural nuance improves retention — the generation-side counterpart to #54's evaluation-side warning.

---

## Part 8 — Datasets, Shared Tasks & Data-Construction Methods

(Several datasets also live in earlier parts: ExPUNations #7, Phunny #8, HumorDB #25, YesBut #26, Humor in AI #22, Oogiri-Master #39, StandUp4AI #44, Chumor #50.)

### 56. [Getting Serious about Humor: Crafting Humor Datasets with Unfunny Large Language Models](https://arxiv.org/abs/2403.00794)
Horvitz, Chen, Aditya, Srivastava, West, Yu & McKeown — **ACL 2024** · `peer-reviewed` `method` `dataset`
- **Method:** "Unfuns" jokes (LLMs edit humorous → non-humorous) to build minimal-pair negatives for detection; English + code-mixed English–Hindi.
- **Findings:** LLMs are good at *removing* humor; GPT-4's synthetic data rated highly and yields challenging adversarial examples. Isolates *what* makes a line funny.

### 57. SemEval-2026 Task 1: MWAHAHA — Models Write Automatic Humor And Humans Annotate
Castro, Chiruzzo, Góngora, Rahili, Deng, Sastre, Amoroso, Rey, Rosá, Moncecchi, Meaney, Prada & Mihalcea — **SemEval-2026** · `workshop` `dataset` `benchmark`
- **Method:** A community shared task in which systems *generate* humorous texts (news-headline-style prompts) and humans annotate the outputs — the first large shared-task campaign centered on humor *generation* rather than detection.
- **Why it matters:** Already the common substrate for HumorGen (#13) and HumorRank (#35), and the likely anchor for generation benchmarking the way SemEval-2017 Task 7 anchored puns. Descends directly from the SemEval headline-humor lineage (Humicroedit/FunLines, below).

### Pre-LLM dataset anchors (compact)
The classic resources the LLM-era work quietly stands on:
- **HaHackathon — SemEval-2021 Task 7** (Meaney, Wilson, Chiruzzo, Lopez & Magdy, 2021) `dataset` — jointly rated humor **and offense** (detection + rating). The original benchmark for the funny-vs-harmful boundary now central to Part 6.
- **Humicroedit & FunLines — SemEval-2020 Task 7** (Hossain, Krumm, Gamon & Kautz, 2019–2020) `dataset` — humor created via *minimal edits* to news headlines. The direct ancestor of MWAHAHA's headline setting, and the original minimal-pair humor-data idea that #56 modernizes with LLM "unfunning."
- **rJokes** (Weller & Seppi — "Humor Detection: A Transformer Gets the Last Laugh," EMNLP 2019; corpus paper LREC 2020) `dataset` — the large-scale Reddit joke corpus with upvote-derived humor degrees; still a standard detection/training source.
- **UR-FUNNY** (Hasan et al., EMNLP 2019) `dataset` — multimodal (text + audio + video) humor detection from TED talks; the precursor to the stand-up/video line (#44). Its sarcasm sibling is **MUStARD** (Castro et al., ACL 2019; cf. Adjacent) — from the same Castro/Mihalcea line that now runs MWAHAHA (#57).

**Also:** [Re-defining Humor Data Objects for AI Humor Research](https://arxiv.org/abs/2605.25171) (Arnett, Nguyen & Jiang, 2026) `preprint` — a small exploratory piece arguing humor data should be modeled as *social interaction* with context and explanations rather than binary labels. Conceptually aligned with this guide's lens; methodologically light (prompt iteration for explanation generation).

---

## Part 9 — Surveys & Resources

### 58. [Who's Laughing Now? An Overview of Computational Humour Generation and Explanation](https://arxiv.org/abs/2509.21175)
Loakman, Thorne & Lin — **INLG 2025** · `peer-reviewed` `survey`
- The best single LLM-era entry point for both core topics; covers generation (§3) and explanation (§4) plus a humor-theory primer and ethics. Bridges theory ↔ LLM literature.

### 59. [Large Language Models for Subjective Language Understanding: A Survey](https://arxiv.org/abs/2508.07959)
arXiv:2508.07959 — **2025** · `preprint` `survey`
- Broader survey with a substantive humor section situating humor detection/understanding among other subjective-language tasks (sentiment, sarcasm, figurative language).

### 60. [A Survey of Pun Generation: Datasets, Evaluations and Methodologies](https://arxiv.org/abs/2507.04793)
arXiv:2507.04793 — **2025** · `preprint` `survey`
- The generation-side complement to the pun-understanding cluster (#4–#8).

### 61. A Survey on Approaches to Computational Humor Generation
Amin & Burghardt — **LaTeCH-CLfL 2020 (ACL Anthology)** · `workshop` `survey`
- A pre-LLM survey of computational humor *generation* (template/rule-based through early neural). Useful historical complement to the LLM-era surveys above and to the pre-LLM foundations note in Part 2.

### 62. [Computational Humor Modeling: A Survey on the State of the Art](https://dl.acm.org/doi/10.1145/3778357)
Lemmens & De Marez — **ACM Computing Surveys 2026** (58(7):177) · `peer-reviewed` `survey`
- The broadest survey here: spans humor detection, generation, translation, and evaluation across text *and* multimodal data, situating LLM-era work against the larger computational-humor field (which dates to the 1990s). Best single reference for positioning the rest of this bibliography.

---

## Adjacent: Sarcasm & Humor Styles

### 63. [SarcasmBench: Towards Evaluating Large Language Models on Sarcasm Understanding](https://arxiv.org/abs/2408.11319)
Zhang, Zou, Lian, Tiwari & Qin — **2024** · `preprint` `benchmark` — Anchor sarcasm benchmark across datasets/prompts; LLMs trail, fine-tuned small models stay competitive.

### 64. [Is Sarcasm Detection a Step-by-Step Reasoning Process in Large Language Models?](https://arxiv.org/abs/2407.12725)
Yao et al. — **AAAI 2025** (arXiv:2407.12725) · `peer-reviewed` — Introduces the SarcasmCue framework (sequential and non-sequential prompting: CoC/GoC/BoC/ToC), probing whether step-by-step reasoning helps this pragmatic, intuition-heavy task; reported gains transfer to humor detection too.

### 65. [A Two-Model Approach for Humour Style Recognition](https://arxiv.org/abs/2410.12842)
Kenneth, Khosmood & Edalat — **2024** · `preprint` `method` — Classifies text into the four Martin humor styles (see HSQ, Theory); ~+11.6% F1 on affiliative. Styles recur as generation conditions and judge personas (cf. Crowd Score #32).

---

## Synthesis: recurring themes

1. **Performance is task-format-dependent, not a fixed ladder.** As a rough pattern, forced-choice recognition/ranking is easiest to score, explanation reveals mechanism failures, and generation looks strong in constrained short-form settings but degrades with novelty, context, audience calibration, and live performance. "Recognition ≫ explanation ≫ origination" is a heuristic, not a law (contrast #2 with Gorenz & Schwarz #31) — though the paired Oogiri results show the gradient cleanly inside a single format (near-human understanding in #39 vs. low-to-mid-tier generation in #38).
2. **Humor competence fragments across joke types.** Transfer between humor types is real but partial and asymmetric (#40); models fail on genuinely novel instances of even simple pun schemas (#8); and no model reliably explains all four joke types in #5. "Humor" is many skills wearing one name — one reason the mechanism × medium × audience × context lens (point 8) is needed at all.
3. **Explanation is harder to fake than detection — but not foolproof.** Models can rationalize non-jokes or produce plausible post-hoc explanations (#2), so explanation is a *better* probe, not a perfect one (#1, #3, #58).
4. **"Understanding" is fragile.** Subtle perturbations break apparent comprehension — structure-matching over meaning (#4, #8, MemeReaCon).
5. **STEM reasoning only partly transfers — and where it does, it helps *comprehension*, not generation.** Reasoning gains carry over to cartoon-caption explanation (#3) but not to knowledge-heavy topical jokes or pun nuance (#5). This is the flip side of point 6: reasoning helps a model *get* a joke more than *make* one.
6. **Generic linear CoT is the wrong tool for generation.** Successful systems use structured creative search, script opposition, persona diversity, retrieval, or generate–evaluate–revise loops (#11–#20, #28, #29) — a lesson already visible in pre-LLM template systems (Part 2 foundations note): structure can be mechanized, brilliance can't.
7. **Data and scaffolding beat optimization tricks.** Quality data and skill/feedback pipelines outperform RLHF-style alignment (#13's twin null results; #14; #15; and #22, where SFT/RLHF/DPO underperform even with 250M ratings).
8. **Humor = mechanism × medium × audience × context.** Funniness is rarely one scalar; audiences cluster (#36), settings differ (#45, #46), and culture reshapes the joke (#30, #50–#55). Per benign violation + distance (T6), the *same* stimulus is funny or not depending on the rater's norm commitments and psychological distance — so any evaluator must fix or model the audience. Evaluation choices (#31–#40) drive the headline.
9. **Visual humor is harder than text humor.** Wider human gaps; models miss the humor-critical region or fail to integrate panels; world knowledge is the bottleneck (#24–#27) — and when humor must be read from *motion* without language, everything drops further (v-HUB, Part 3).
10. **Safety cuts both ways.** Filtering flattens comedic edge (#41), yet engagement-seeking humor amplifies harm (#47) and humor is a jailbreak vector (#49); benign violation (T6) is the knife-edge.

## Reading paths
- **Start:** Who's Laughing Now? (#58) → Hessel et al. (#1) → Inside Jokes (T3) + GTVH (T2).
- **Understanding:** HumorBench (#3) → Pun Unintended (#4) → Phunny (#8) → Comparing Apples to Oranges (#5) → ExPUNations (#7) → IRS / Cartoon Captionist (#24).
- **Generation:** CLoT (#11) → Small But Funny (#15) → HumorGen (#13) → Kim & Chilton (#14) → HOMER (#29); then A Robot Walks into a Bar (#41) for the human reality check.
- **Multimodal:** HumorDB (#25) → YesBut (#26) → Humor in AI (#22) → IRS (#24) → BottleHumor (#27) → HOMER (#29).
- **Evaluation/"are they funny?":** Jentzsch & Kersting (#2) vs. Gorenz & Schwarz (#31) → Crowd Score (#32) → Is GPT-4 Good Enough (#33) → Cards Against LLMs (#34) → HumorRank (#35) → Oogiri multi-dimensional (#38) → Oogiri-Master (#39) → Who Laughs with Whom (#36).
- **Generalization across humor types:** Phunny (#8) → One Joke to Rule them All (#40).
- **Live/situated:** Theater Stage as Laboratory (#43) → Improvised Theatre deployment (#42) → StandUp4AI (#44) → Not All Jokes Land (#45).
- **Theory:** SSTH (T1) → GTVH (T2) → incongruity-resolution / appropriate incongruity (T5) → benign violation + distance (T6) → Inside Jokes (T3).

---

*Compilation note:* entries were checked against primary sources where available; entries that lead with an arXiv ID rather than an author line are those whose authorship could not be confirmed against the primary source, and HUMORCHAIN's CVPR 2026 venue is taken from the CVF citation (the CVF page blocks automated fetching). Fast-moving 2025–26 preprint and workshop items may change venue or status, and tags marked `preprint` may since have appeared in a reviewed venue.
