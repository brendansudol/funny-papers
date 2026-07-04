<!-- Transcribed from x02-comic.pdf -->



<!-- page 0001 -->

# COMIC: Agentic Sketch Comedy Generation

Susung Hong  Brian Curless  Ira Kemelmacher-Shlizerman  Steve Seitz

University of Washington

[Figure: Overview diagram of COMIC. Inputs include two character images/voices labeled “Character,” and one character plus a background image labeled “Background,” leading to generated scripts and filmstrip-style video outputs.]

**Fig. 1:** COMIC is an agentic sketch comedy video generator. It takes images, voices, and brief descriptions as input, and automatically generates funny comedy scripts along with corresponding video and audio. Our method flexibly builds stories around multiple characters and custom backgrounds. Each generated comedy is 1–2 minutes long; please watch them at https://susunghong.github.io/COMIC.

**Abstract.** We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the system employs a population of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and improvement. A key contribution is the introduction of LLM critics aligned with real viewer preferences through the analysis of a corpus of comedy videos on YouTube to automatically evaluate humor. Our experiments show that our framework produces results approaching the quality of professionally produced sketches while demonstrating state-of-the-art performance in video generation.

# 1 Introduction

Can AI be funny? If you ask today’s AI models to tell you a joke, you will likely receive a groan-inducing pun or a “dad joke.” While generative models now excel across a wide range of writing, coding, and media generation tasks, humor remains particularly challenging. This is not to say that LLMs are incapable of



<!-- page 0002 -->

[Figure: Overall agentic flow diagram. Input “Characters and Backgrounds” → “Writer” → writing loop with “Scripts,” “Critique,” and “Edit” labeled “Writing Loops” → “Scene Director” with “Asset Memory” → “Storyboards” → rendering loop with “Image,” “Video,” “Voice,” “Critique,” and “Edit” labeled “Rendering Loops” → Output “Multi-Clip Videos.”]

**Fig. 2:** Overall agentic flow. Our method is loosely modeled on human production studios, with agentic counterparts for each role, such as writer, critic, and director. The writing and rendering loops allow us to generate scripts and videos with sufficient breadth and depth through island-based competition and iteration, as illustrated in Fig. 4 and Fig. 5, respectively.

humor—with the right prompts and enough iterations, one can find some gems. However, reliably producing content that can make an audience laugh is difficult.

In this paper, we propose a fully automated framework, **Content Optimization via Multi-agent Iterative Competition (COMIC)**, that produces short comedic videos similar to professionally produced comedy sketches. The input to the system is a list of character descriptions (text, image, voice) and background references (Fig. 1). Achieving this goal requires solving three distinct tasks automatically: conceptualizing the right comedic scenario, producing a funny script, and generating a high-quality, consistent, and engaging video. Each of these tasks is independently challenging. Crafting genuinely funny ideas and scripts requires navigating the subjective, multidimensional space of humor, and producing long-form video remains an open problem, as state-of-the-art video models typically produce only short clips and lack strong controls for inter-clip consistency.

Our approach is based on the observation that LLMs do occasionally produce humorous content when provided with the right structure. It is a bit like panning for gold—one must dig deep enough to gather sufficient material, then sift through it to find the humorous nuggets from which to build a sketch. This mirrors how real sketch comedy shows operate [25], with groups of writers spending many hours brainstorming and iterating before converging on a set of finalists. However, evaluating humor automatically is a big challenge. We therefore derive LLM-based humor *critics* aligned with human preferences by analyzing a corpus of YouTube comedy sketch videos and their associated viewer engagement.

Our system is loosely modeled on human production studios, using agentic versions of roles such as scriptwriters, editors, and directors (Fig. 2), with a specific structure designed to encourage diversity of ideas and optimize for the emergence of humorous content. Specifically, we instantiate multiple distinct *islands* of scripts, each governed by critic committees representing different philosophies. Script populations improve on each island through round-robin tournaments in which losing scripts are refined using feedback from the winners. This topology captures the multimodal nature of humor: “good” comedy can be slapstick, dry, or surreal, and success can manifest through various approaches.

Once scripts are refined, scene director agents break each script down into distinct shots—each with its own setup, *e.g.*, characters, dialogues, expressions,



<!-- page 0003 -->

[Figure: Filmstrip of nine sketch comedy video frames featuring generated situations. Readable overlaid dialogue includes: “It’s just a t-shirt.” “Just a t-shirt? Kid, we’re talking about a DeepMind 2019. Only fifty in existence.” “That’s how we separate collectors from tourists. We also check the tag font. See how the ‘m’ in AI is slightly serif?” “Analyzing browsing history. User wears the same conference t-shirt every day.” “The algorithm compared to my default state. It found the local minimum.” “Apples are arranged by size. That’s a grid system. Someone’s cataloging inventory by threat level.” “They’re just organized.” “That’s what they want you to think. What if one’s the sleeper agent?”]

**Fig. 3:** Sketch comedy videos featuring various generated situations. See our project page for videos of these results.

and backgrounds—and render videos for each shot. Shots are produced consecutively, allowing the scene director for the current shot to reference previous shots for continuity. Each shot is evaluated by a set of script-conditioned rendering critics that embody diverse interpretations of how the narrative should be visually realized, and then refined based on critic feedback. This iterative pipeline, with depth- and breadth-wise competitions in refinement histories and realizations respectively, achieves state-of-the-art results in agentic video generation.

To our knowledge, COMIC is the first fully automated agentic system targeting the generation of comedic videos, which sits at the opposite extreme of open-ended creative tasks compared to mathematics or coding, which have correct answers. A key innovation is grounding evaluation in real viewer preferences through diverse critics aligned with engagement patterns drawn from thousands of YouTube sketch comedy videos, enabling effective scaling of inference-time compute for creative tasks that are difficult to evaluate. Based on our automated and human evaluations, COMIC produces results approaching the quality of professionally produced comedy sketches.

## 2 Background

*Multi-agent evolutionary systems.* Evolutionary computation has been applied to creative domains through genetic algorithms [37] and quality-diversity methods like MAP-Elites [27]. Several distributed evolutionary algorithms [2, 28, 38, 42] explore dividing populations into groups to balance exploration and exploitation.



<!-- page 0004 -->

Recent LLM applications include prompt optimization [7, 45], heuristic discovery [22], and mathematical reasoning [33]. Furthermore, LLM-based multi-agent frameworks have simulated development ecosystems [11, 31], while systems such as ChatEval [3] utilize multi-agent debate [6]. LLMs are also increasingly used as active evolutionary operators to iteratively optimize text and agent behavior [46, 47]. Our work advances this domain by proposing to optimize comedy, an extremely open-ended domain, via competition by multiple aligned critics.

*Video generation.* Foundational models such as Sora [29], Veo [9], and Movie Gen [26], alongside commercial platforms like Runway Gen [34], Pika Labs [30], and Luma Dream Machine [24], and open-weight models like Mochi [39], HunyuanVideo [16], and Wan [41], have demonstrated impressive text-to-video capabilities. Moreover, recent work incorporates various types of controls (*e.g.*, audio conditioning) to make video generation more controllable [12, 20, 41]. However, most models generate only short, few-event clips of approximately 10 seconds. Extensions like StreamingT2V [10] and FramePack [48] increase duration through autoregressive approaches but focus solely on temporal extension without addressing narrative coherence or comedic quality. COMIC provides a bridge between short-form generative capability and compelling, long-form storytelling.

*Agentic video production.* Recent work has explored LLMs as orchestration modules for video generation. DirecT2V [13], Free-Bloom [14], VideoDirectorGPT [21], and LLM-grounded Video Diffusion [19] use LLMs for frame-level direction or layout planning, while VISTA [23] demonstrates prompt-based self-improvement. Contemporary storyboard-based methods [5, 15, 18, 35, 44, 49] address longer videos but remain limited in handling the narrative complexity and quality demands of sketch comedy, which requires searching over a vast creative space. Our work fundamentally upgrades agentic orchestration for video production from a shallow, single-pass pipeline to a deep, self-improving search process. By replacing fixed agentic objectives with divergent evaluative pressure from specialized critics, COMIC efficiently explores the creative space required for sketch comedy, establishing a new state of the art for fully automated video production.

## 3 Content Optimization via Multi-Agent Iterative Competition (COMIC)

### 3.1 Problem Statement

We address *automated sketch comedy video generation*: given character specifications $\mathcal{X} = [x_1, \ldots, x_C]$—each comprising a portrait image, voice sample, and text description—and background assets $\mathcal{B} = [b_1, \ldots, b_M]$, the system must produce a short comedic video $\mathcal{V}^*$ that is narratively coherent, visually consistent, and genuinely funny to human viewers.

We decompose this objective into two coupled subproblems. *Script generation* synthesizes a script $s^* \in \mathcal{S}$ that establishes a compelling comedic premise,



<!-- page 0005 -->

develops it through character interaction, and delivers a satisfying payoff. *Visual realization* translates $s^*$ into a shot sequence $\mathcal{V}=[v_1,\ldots,v_N]$ that faithfully embodies the narrative while maintaining character identity and scene continuity.

The overall agentic pipeline is shown in Fig. 2. At a high level, COMIC follows a forward pipeline in which a *writer* generates concepts and expands them into full dialogues, a *critic* evaluates and compares scripts, and an *editor* revises scripts based on critic feedback. Subsequently, a *scene director* translates the final script into a storyboard, *image and video generators* render each shot as visual content, a *voice generator* synthesizes character audio, and a *rendering critic* evaluates and refines the rendered videos.

A single-pass instantiation of this pipeline, however, is insufficient for high-quality results; good scripts are forged through multiple rounds of revision. COMIC utilizes human-aligned critics (Sec. 3.3), evolves scripts through competitive island-based search (Sec. 3.4), and realizes them audio-visually through iterative, critic-guided refinement (Sec. 3.5).

### 3.2 Why Fixed Objectives Fall Short

*The subjectivity of humor.* Traditional goal-based optimization presupposes a stationary reward function $R:S \to \mathbb{R}$. However, humor is inherently context-dependent and subjective. A fixed scalar objective invites Goodhart’s Law [8], rewarding a proxy metric rather than genuine creative quality, while a fixed reward grows stale as tastes evolve. For instance, a joke that scores highest at a given moment can become unfunny upon repetition, contradicting the assumption that the reward is stationary. Great humor also takes many different forms; slapstick and dry wit share no common measuring stick, and different people prefer different styles of humor. It is impossible to aggregate preference profiles into a single, consistent ranking without sacrificing desirable properties [1].

*Limitations of existing agentic strategies.* Recent agentic video-production systems [21, 44, 49] leverage LLMs as directors that decompose targets into sub-tasks and invoke generative tools in sequence. Such designs are poorly suited to highly open-ended creative tasks. Primarily, each role is defined by a fixed instruction, meaning the agent always applies the same evaluative lens with no mechanism to explore alternative perspectives. Moreover, scripts pass through agents in a fixed sequence with limited feedback—a shallow, single-pass structure that is fundamentally at odds with the iterative, competitive nature of creative improvement, where quality emerges from repeated head-to-head comparison, rejection, and revision under diverse evaluative pressure.

Rather than imposing a ground-truth quality ceiling, COMIC embraces *relativism*, where a script’s fitness is defined not by its distance from an ideal but by its relative performance against current competitors. Concretely, scripts are evaluated through pairwise competition mediated by diverse critic committees, and losing scripts are iteratively refined using the resulting feedback. This makes quality contextual and multidimensional, enabling constant adaptation as the competitive baseline rises, without the need for a fixed destination.



<!-- page 0006 -->

|  | Comparison | Studio C | FAH | VLDL | K&P | SNL | **Average** |
|---|---|---:|---:|---:|---:|---:|---:|
| Mean Critic | Top vs. Middle | 0.63 | 0.40 | 0.58 | 0.53 | 0.59 | 0.55 |
|  | Top vs. Bottom | 0.72 | 0.62 | 0.79 | 0.60 | 0.81 | 0.71 |
| Single Best | Top vs. Middle | 0.62 | **0.52** | 0.56 | 0.57 | 0.59 | 0.57 |
|  | Top vs. Bottom | 0.67 | 0.70 | 0.84 | 0.69 | 0.80 | 0.74 |
| Task-Wise Best | Top vs. Middle | **0.70** | **0.52** | **0.70** | **0.65** | **0.65** | **0.64** |
|  | Top vs. Bottom | **0.85** | **0.78** | **0.85** | **0.72** | **0.95** | **0.83** |

**Table 1:** Channel-specific validation accuracy. Task-wise critic selection consistently outperforms both pooled and single-best critics across all channels and engagement tiers. FAH = Foil Arms & Hog; VLDL = Viva La Dirt League; K&P = Key & Peele.

### 3.3 Alignment to Real Viewers

Evaluation quality depends critically on critic selection. Rather than hand-crafting critic prompts or fine-tuning a dedicated critic model, we propose a *generate-and-select* strategy. We synthesize a large, diverse pool of candidate critics, each defined by a system prompt specifying its persona, and retain those whose preferences best align with empirical audience engagement signals. This confers a key advantage over fine-tuning: diversity is achieved through prompt variation at zero training cost, enabling aggressive pruning to retain only the most informative critics while exploring a wide range of evaluative perspectives.

*Engagement scoring.* We collect 4,940 data points from five YouTube sketch comedy channels: Foil Arms & Hog, Key & Peele, SNL, Studio C, and Viva La Dirt League. We use view counts as a proxy for popularity. Since view-count trajectories follow an empirical S-curve, we normalize view counts by video age by fitting a per-channel logistic growth model:

$$
V(t) = \frac{L}{1 + \exp(-r(t - t_0))}
\tag{1}
$$

via nonlinear least squares, where $L$ is the carrying capacity, $r$ is the growth rate, and $t_0$ is the inflection point. Each video’s engagement score is then defined as its projected carrying capacity $L_{\mathrm{proj}} = V(t) \cdot (1 + \exp(-r(t - t_0)))$, using per-channel parameters $r$ and $t_0$. Scripts are then selected for the top, middle, and bottom engagement tiers and partitioned into $\mathcal{S}_{\mathrm{in-context}}$ for critic calibration, $\mathcal{S}_{\mathrm{val}}$ for critic selection, and $\mathcal{S}_{\mathrm{test}}$ for held-out evaluation. Additional details are provided in the supplementary material.

*Critic pool generation.* We construct a diverse critic pool $\mathcal{C}_{\mathrm{pool}}$ by prompting a meta-critic agent $p_{\mathrm{script}}$ with stratified in-context examples from $\mathcal{S}_{\mathrm{in-context}}$ with tier labels. Specifically, the meta-critic agent takes labeled scripts as few-shot inputs and generates critics with diverse personas (*i.e.*, perspectives, types, and backgrounds), from which we sample an aligned pool:

$$
\mathcal{C}_{\mathrm{pool}} \sim p_{\mathrm{script}}(C \mid \mathcal{S}_{\mathrm{in-context}}),
\tag{2}
$$



<!-- page 0007 -->

| Comparison | Mean Critic | Single Best | Task-Wise Best |
|---|---:|---:|---:|
| Top vs. Middle | 0.557 | 0.554 | **0.578** |
| Top vs. Bottom | 0.654 | 0.670 | **0.716** |

**Table 2:** Generalization to the held-out test set. Task-wise best critics maintain superior discrimination on unseen scripts, confirming that the selection procedure does not overfit to the validation set.

which calibrates each critic’s aesthetic preferences to a specific channel’s engagement patterns. Rather than producing a single critic, which is insufficient for representing diverse perspectives, our strategy is to sample a set of critics (a size of 10 in practice) and select the subset that best discriminates among real viewer engagement scores.

*Task-specific selection.* To capture both coarse and fine quality distinctions, we define two comparison tasks. *Top vs. Bottom* targets critics sensitive to large quality gaps, assessing the potential to lift poor scripts to top-tier quality. *Top vs. Middle* targets critics sensitive to subtle distinctions, assessing the potential to refine already-competitive scripts. For each channel $\chi$ and sensitivity level $\tau$, we select the highest-accuracy critic on the pairwise comparison task $\mathcal{T}^{\mathrm{val}}_{\chi,\tau}$ on the validation set:

$$
c^*_{\chi,\tau} = \argmax_{c \in \mathcal{C}_{\mathrm{pool}}} \mathrm{Acc}(c \mid \mathcal{T}^{\mathrm{val}}_{\chi,\tau}),
\tag{3}
$$

yielding the specialized pool $\mathcal{C}_{\mathrm{task}} = \bigcup_{\chi,\tau} \{c^*_{\chi,\tau}\}$. Then, we compare this *Task-Wise Best* pool with an average of all critics, *Mean Critic*, and a single-element critic pool with the best average accuracy, *Single Best*.

Task-specific selection substantially improves over both the average-of-all-critics and single-best-critic baselines (Table 1). For example, the overall accuracy of Studio C, VLDL, and SNL rise significantly from *Single Best*, confirming that distinct comedic traditions require distinct evaluative criteria. Table 2 confirms that this advantage generalizes to held-out data, $\mathcal{S}_{\mathrm{test}}$. We find that even without in-context examples, generated critics already roughly align with engagement patterns. However, calibration with more in-context examples further improves accuracy (see the supplementary material).

### 3.4 Script Writing Loop

*Islands and evolving fitness landscapes.* We introduce an approach to iteratively evolve a population of scripts. Pairs of scripts are compared by a critic agent, which provides feedback to revise the weaker script. As the population evolves, weaker scripts are iteratively refined using the feedback, continuously raising the competitive baseline. A script that wins at generation $g$ may lose at $g + 1$ not because it degraded, but because competitors improved. Defining fitness $f^{(g)}(s)$ as the expected win rate of script $s$ against the current population given a critic committee $\mathcal{C}$ and script population at the current generation $\mathcal{S}^{(g)}$,

$$
f^{(g)}(s) = \mathbb{E}_{s' \sim \mathcal{S}^{(g)}, c \sim \mathcal{C}}\left[\mathbb{I}\left[c(s, s') \mapsto (s, \cdot)\right]\right],
\tag{4}
$$



<!-- page 0008 -->

[Figure: Diagram of the script writing stage. Left panel labeled “Initial Scripts” and “Aligned Critic Pool”; middle panels labeled “Script Writing Loop” with isolated islands, including “Island ℓ”; right expanded panel labeled “Island k” showing scripts and critics with “Prefer <”, “Prefer >”, “Refine”, and “Round-Robin Pairwise Evaluation”.]

**Fig. 4:** Script writing stage. Isolated script populations evolve on separate islands under distinct critic committees sampled from the aligned critic pool. Losing scripts are refined through round-robin pairwise tournaments by each island’s critic committee, driving improvement while supporting aesthetic diversity across islands.

this formulation implements a competitive environment that grows more demanding, *i.e.*, $\mathbb{E}[f^{(g)}(s)] \geq \mathbb{E}[f^{(g+1)}(s)]$, forcing continuous adaptation.

To encourage diversity of solutions, we partition the global script population into $K$ isolated islands $\{I_1,\ldots,I_K\}$, each governed by a specialized critic committee $\mathcal{C}_k$ drawn from $\mathcal{C}_{\text{task}}$ in Sec. 3.3. These separate committees embody distinct comedic preferences, while being aligned with engagement patterns. The fitness landscape on island $k$ is shaped by two coupled elements: (1) the island-specific critic committee $\mathcal{C}_k$, which defines evaluative standards, and (2) the evolving script population $\mathcal{S}_k$, which determines the comparative baseline. Because both critics and populations differ across islands, the fitness landscapes tend to diverge, yielding a Pareto frontier of diverse comedic styles.

*Pairwise evaluation with critic-guided update.* Within each island, evolution proceeds through round-robin pairwise evaluation. At each iteration, two scripts $s_i, s_j \in \mathcal{S}_k$ are compared by every critic in the local committee. Each critic $c_e \in \mathcal{C}_k$ performs an independent evaluation:

$$
c_e(s_i, s_j) \mapsto (w_{c_e}, \phi_{c_e}).
\tag{5}
$$

Let $s_\ell \in \{s_i, s_j\} \setminus \{w_{c_e}\}$ denote the losing script. It undergoes a *critic-guided update* driven by the feedback:

$$
s_\ell \leftarrow U(s_\ell, \phi_{c_e}),
\tag{6}
$$

where $U : \mathcal{S} \times \Phi \to \mathcal{S}$ is the update operator that rewrites the script according to natural-language feedback $\phi_{c_e}$, $\mathcal{S}$ denotes the space of scripts, and $\Phi$ denotes the space of natural-language feedback. Note that we only update the losing script. This compact operator integrates two classical evolutionary mechanisms in a single call: the comparative feedback $\phi_{c_e}$ encourages the loser to incorporate the winner’s strengths, resulting in semantic *crossover* that transfers beneficial features from the superior script, while $U$ simultaneously introduces semantic *mutation* by rewriting the script under critic guidance, exploring variations that may uncover novel comedic approaches.



<!-- page 0009 -->

[Figure: Video rendering stage diagram showing inputs “Top Script,” “Storyboards,” and “Critics”; a central “Video Rendering Loop” with “Keyframe,” “Audio,” “Video,” “Memory,” “Shot Generation,” “Refine,” “Accept,” “History,” “Single-Elim.,” “Add,” and “Next Shot”; and a “Final Single-Elimination” leading to “Final Output.”]

**Fig. 5:** Video rendering stage. Scene directions are generated and critic-refined for each script. Single-elimination tournaments operate at both shot and video levels, selecting the best revision across history and the best video across diverse realizations.

### 3.5 Video Rendering Loop

The rendering stage translates critic-selected scripts into videos. Following our script generation, we introduce script-conditioned video critics and a competition-based framework for video generation.

_Script-conditioned critic generation._ Similar to the writing stage, a video meta-critic agent $p_{\text{render}}$ generates critics with diverse personas. However, these are video-specific and script-calibrated, as each comedic narrative requires a different evaluative focus. Given a refined script $s$, we generate a rendering critic set:

$$
\mathcal{C}_{\text{render}} \sim p_{\text{render}}(\mathcal{C}\mid s)
\tag{7}
$$

conditioned on the script. Each critic $c \in \mathcal{C}_{\text{render}}$ embodies a distinct lens through which the script can be visually realized.

_Storyboarding._ Because video generation is computationally expensive, we introduce a storyboarding step to outline visual content conditioned on the script before proceeding to video rendering iterations. For each script $s$, a scene director agent generates $D$ scene directions $\{d^{(1)},\ldots,d^{(D)}\}$, where each $d^{(j)}=\{d_1^{(j)},\ldots,d_{N_j}^{(j)}\}$ specifies the rendering of $N_j$ shots in text form. Each shot specification $d_i^{(j)}$ defines reference characters, backgrounds, and previous shots, as well as text descriptions and instructions for handling scene composition such as character poses, expressions, background descriptions, camera framing, and angles. A structured memory bank $\mathcal{M}$ stores character assets and backgrounds, as well as the last frame of each finalized shot so that subsequent specifications can reference prior shots for visual continuity. However, this requires the agent to handle various visual arrangements simultaneously, causing it to overlook certain details, such as selecting consistent backgrounds. Therefore, we leverage _setup notes_ to benefit from chain-of-thought reasoning, which facilitates the director agent in planning visual arrangements prior to generating shot specifications.

_Iterative shot refinement with history tournament._ For scene direction $d^{(j)}$ and shot $i$, rendering proceeds as an iterative loop over $|\mathcal{C}_{\text{render}}|$ iterations. An initial shot is generated from $d_i^{(j,0)} := d_i^{(j)}$ via

$$
v_i^{(0)} \leftarrow \mathrm{Render}(d_i^{(j,0)}, V_{<i}, \mathcal{M}),
\tag{8}
$$



<!-- page 0010 -->

where Render involves image, voice, and video generation based on the scene direction. Since Render involves diffusion sampling in practice and generates images and videos under audio-visual-text conditions, to enhance visual clarity, we add a condition-agnostic guidance term [4]. For $m = 0, \ldots, |\mathcal{C}_{\mathrm{render}}| - 1$, each critic in turn evaluates the shot and proposes a refined specification:

$$
c\left(d_i^{(j,m)}, V_{<i}, v_i^{(m)} \mid s\right) \mapsto \left(d_i^{(j,m+1)}, \phi_{\mathrm{refine}}\right),
\tag{9}
$$

where $V_{<i} = [v_1, \ldots, v_{i-1}]$ are previously finalized shots. The updated specification guides the next render, $v_i^{(m+1)} \leftarrow \mathrm{Render}(d_i^{(j,m+1)}, V_{<i}, \mathcal{M})$. Conditioning on the scene direction, prior shots, and the memory ensures that refinement serves overall coherence rather than optimizing individual shots in isolation.

Refinement accumulates a history $\mathcal{H}_i^{(j)} = \{v_i^{(0)}, \ldots, v_i^{(|\mathcal{C}_{\mathrm{render}}|)}\}$. Rather than simply accepting the final iteration, we run a single-elimination tournament across the full history to select a *single winner*:

$$
v_i^* = \mathrm{SingleElimination}(\mathcal{H}_i^{(j)}, \mathcal{C}_{\mathrm{render}}, s, V_{<i}).
\tag{10}
$$

This guards against over-refinement and ensures quality increases after refinement. The tournament on history selects with respect to depth, *i.e.*, how deeply a shot can be refined, encouraging exploitation of the given scene direction.

*Test-time scaling via scene-level tournament.* After rendering $D$ scene directions into complete videos $\{\mathcal{V}^{(1)}, \ldots, \mathcal{V}^{(D)}\}$, where each $\mathcal{V}^{(j)} = [v_1^*, \ldots, v_{N_j}^*]$ consists of selected shots, we perform a final tournament among the full videos:

$$
\mathcal{V}^* = \mathrm{SingleElimination}(\{\mathcal{V}^{(1)}, \ldots, \mathcal{V}^{(D)}\}, \mathcal{C}_{\mathrm{render}}, s).
\tag{11}
$$

Scaling $D$ at inference time directs additional compute toward rendering quality without retraining, providing a parallelizable test-time scaling axis that trades inference budget for improved visual realization. The scene-level tournament selects across breadth, *i.e.*, across diverse scene realizations, encouraging exploration of the broad space of possible realizations.

## 4 Experiments

### 4.1 Implementation Details

COMIC exposes several scaling dimensions: number of islands $K$, scripts per island $|\mathcal{S}_k|$, critics per island $|\mathcal{C}_k|$, scene directions $D$, and rendering critics $|\mathcal{C}_{\mathrm{render}}|$. We define three scale configurations, small, base, and large, across these dimensions. Unless otherwise noted, we report results from the 4th generation and use the base configuration. The base configuration runs in approximately one day on a single GPU with an API budget of around \$5, which is orders of magnitude below the production cost of professional sketch comedy. Our framework allows different foundation models to be readily plugged in at distinct points. We refer readers to the supplementary material for additional details.



<!-- page 0011 -->

[Figure: Three side-by-side line charts. Left: y-axis “Win Rate” vs. x-axis “Generation” with ticks 0, 1, 2, 4, 8, 16. Middle: y-axis “Inter-Diversity” vs. “Generation”. Right: y-axis “Intra-Diversity” vs. “Generation”. Each chart shows a solid line with shaded range.]

**Fig. 6:** Effect of generation, computed by *Win Rate*, *Inter-Diversity*, and *Intra-Diversity* across iterations with respect to the 0th generation. Average values are presented as solid lines, and the range is depicted as shading. Until the 4th generation, the win rate increases drastically. *Inter-Diversity* (diversity across scripts) initially drops due to the emergence of coherently favorable responses but increases as generations progress, driven by our divergent mechanism.

[Figure: Four before-and-after image pairs with arrows. Subcaptions: (a) Resolving character mismatch; (b) Resolving background mismatch; (c) Adjusting framing and props; (d) Fixing visual artifacts.]

**Fig. 7:** Specific issues addressed by video critics during the rendering process.

## 4.2 Evaluation Metrics

We evaluate our method’s ability to generate samples (either scripts or videos) by proposing three key metrics computed via pairwise comparisons. Let $A$, $B$, and $E$ denote the sets of reference samples, generated samples, and evaluators, respectively. For each triplet $(e, b, a)$, we compute the probability $P_{e,b,a}$ that $b$ beats $a$ under evaluator $e$. *Win Rate* measures overall sample quality, *i.e.*, $Q_{\mathrm{avg}} = \mathbb{E}_{e,b,a}[P_{e,b,a}]$. Values above 0.5 indicate that generated samples outperform the references on average. *Inter-Diversity* quantifies diversity across generated samples, *i.e.*, $D_{\mathrm{inter}} = \mathbb{E}_{e,a}[\mathrm{Var}_b(P_{e,b,a})]/(Q_{\mathrm{avg}}(1 - Q_{\mathrm{avg}}))$, where $\mathrm{Var}_b$ denotes variance across all $b \in B$. The denominator normalizes by the theoretical maximum variance of a Bernoulli variable with mean $Q_{\mathrm{avg}}$, ensuring the metric is scale-invariant. *Intra-Diversity* measures performance consistency within each sample, *i.e.*, $D_{\mathrm{intra}} = \mathbb{E}_b[\mathrm{Var}_{e,a}(P_{e,b,a})]/(Q_{\mathrm{avg}}(1 - Q_{\mathrm{avg}}))$, where $\mathrm{Var}_{e,a}$ denotes variance across all $(e, a)$ pairs. High $D_{\mathrm{intra}}$ indicates that each sample is judged inconsistently across different evaluators and references, *i.e.*, high specialization.

## 4.3 Video Results

Figs. 1 and 3 demonstrate COMIC’s ability to generate sketch comedy videos that are not only visually coherent but narratively purposeful. We strongly encourage readers to view the video examples in our project page.

Starting from minimal specifications (*e.g.*, a portrait, voice sample, and brief text description), the system autonomously develops complete comedic arcs with



<!-- page 0012 -->

| Method | Funniness↑ | Watch More↑ | vs. Human↑ | Script↑ | Narrative↑ | Realism↑ | Consistency↑ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Veo 3.1 [9] | 2.32 | 2.36 | 2.27 | 2.18 | 3.32 | 4.91 | 5.05 |
| Sora 2 [29] | 2.73 | 2.73 | 2.32 | 2.45 | 3.36 | 5.73 | 5.50 |
| VGoT [49] | 1.18 | 1.27 | 1.14 | 1.00 | 1.23 | 2.00 | 2.32 |
| MovieAgent [44] | 1.27 | 1.09 | 1.18 | 1.09 | 1.09 | 1.27 | 1.14 |
| **COMIC (Ours)** | **3.45** | **3.09** | **3.05** | **3.32** | **4.50** | **4.27** | **4.50** |

**Table 3:** Human evaluation of baseline methods across multiple criteria.

setups, escalating tension, and effective payoffs. The generated sketches span a wide tonal range, from dry, deadpan exchanges to surreal absurdism. Visually, characters maintain consistent identities across cuts, backgrounds remain stable between shots, and scene transitions respect narrative continuity.

### 4.4 Baseline Comparison

We compare COMIC against VideoGen-of-Thought [49] and MovieAgent [44] as agentic video production baselines. These represent storyboard-driven long-form agentic video generation but lack iterative refinement or competitive selection. We further compare against frontier text-to-video models Sora 2 [29] and Veo 3.1 [9], to assess the contribution of our agentic pipeline over raw generative capability. While Veo 3.1 and Sora 2 may exhibit agentic behavior internally, we consider them black-box models in this evaluation. We provide qualitative comparisons in the supplementary material.

*Human evaluation.* We conducted a blind, randomized human evaluation to assess comedic video quality across multiple dimensions, including funniness and engagement (see the supplementary material for details). Table 3 reports mean scores on a 7-point Likert scale. COMIC consistently outperforms the agentic baselines by large margins across all dimensions, including *Funniness*, *Watch More*, *Script*, *Narrative*, *Realism*, and *Consistency*, demonstrating that our iterative, critic-guided pipeline significantly elevates output quality. Notably, the agentic baselines score between *Definitely Not* and *Probably Not* on *Watch More*, whereas COMIC scores between *Unlikely* and *Neutral*, indicating stronger viewer interest. Sora 2 and Veo 3.1 score higher on *Realism* and *Consistency* than COMIC does, partly due to their shorter output durations, which limit opportunities for visual artifacts. Despite this, COMIC outperforms both on *Watch More*, suggesting that its comedic depth compensates for the greater duration.

*Comparison against human-produced content.* A central goal is to produce content that approaches the humor of professional human sketches. On the *vs. Human* dimension (1 = much less funny, 4 = comparable, 7 = much funnier), COMIC places between *Slightly Less Funny* and *Comparable*, a level that neither frontier video models nor agentic baselines achieve.

*Automated evaluation.* To benchmark, we extend the critic alignment framework (Sec. 3.3) to video evaluation using human engagement data. We prompt a



<!-- page 0013 -->

<table>
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th colspan="3">Single Best</th>
      <th colspan="3">Channel-Wise Best</th>
    </tr>
    <tr>
      <th>Win Rate</th>
      <th>Inter-Diversity</th>
      <th>Intra-Diversity</th>
      <th>Win Rate</th>
      <th>Inter-Diversity</th>
      <th>Intra-Diversity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Veo 3.1 [9]</td>
      <td>0.010</td>
      <td>0.308</td>
      <td>0.369</td>
      <td>0.105</td>
      <td>0.263</td>
      <td>0.360</td>
    </tr>
    <tr>
      <td>Sora 2 [29]</td>
      <td><u>0.075</u></td>
      <td><u>0.531</u></td>
      <td><strong>0.722</strong></td>
      <td><u>0.175</u></td>
      <td><u>0.310</u></td>
      <td><u>0.563</u></td>
    </tr>
    <tr>
      <td>VGoT [49]</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.010</td>
      <td>0.105</td>
      <td>0.189</td>
    </tr>
    <tr>
      <td>MovieAgent [44]</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>0.130</td>
      <td>0.088</td>
      <td>0.180</td>
    </tr>
    <tr>
      <td>COMIC (Ours)</td>
      <td><strong>0.440</strong></td>
      <td><strong>0.780</strong></td>
      <td><u>0.682</u></td>
      <td><strong>0.390</strong></td>
      <td><strong>0.519</strong></td>
      <td><strong>0.693</strong></td>
    </tr>
  </tbody>
</table>

**Table 4:** Win rate and diversity scores averaged across all channels. *Single Best* uses a single top critic; *Channel-Wise Best* aggregates across per-channel best critics.

video meta-critic agent to synthesize a pool of candidate critics with diverse personas. Selected critics conduct pairwise comparisons between generated videos and middle-tier test videos representing “median” sketch comedies.

We consider the following aggregation strategies: *Single Best*, which selects the highest-accuracy critic on the validation set, and *Channel-Wise Best*, which selects critics independently per channel to capture diverse comedic traditions (*e.g.,* SNL, Key & Peele). Table 4 reports the win rate, inter-diversity, and intra-diversity, averaged across channels. COMIC substantially outperforms all baselines in win rate, achieving a score nearly on par with the middle-ranked sketch comedies. Agentic baselines (MovieAgent and VGoT) score near zero under Single Best, consistent with our human evaluation. Notably, the automated ranking (COMIC > Sora > Veo > MA $\approx$ VGoT) aligns with the human results in Table 3, validating the benchmark as a proxy for human judgment. Furthermore, COMIC achieves the highest overall inter- and intra-diversity, demonstrating that our mechanism sustains a diverse range of comedic styles that single-pass methods do not.

## 4.5 Ablation Study

*Island-based evolution.* Fig. 6 tracks win rate and diversity across generations, demonstrating continuous adaptation as described in Sec. 3.4. The win rate rises sharply through generation 4, confirming that pairwise tournaments drive rapid improvement. Inter-diversity initially drops as populations converge toward generally effective strategies, then recovers as distinct critic committees push populations toward unique niches. Fig. 7 illustrates how rendering critics correct issues such as character mismatches and framing errors.

[Figure: Bar chart comparing Single-Island and Multi-Island settings for Win Rate and Intra-Diversity. Legend labels “Single-Island” and “Multi-Island”; y-axis ranges from 0.55 to 1.00; x-axis labels “Win Rate” and “Intra-Diversity”.]

**Fig. 8:** Single- and multi-island settings.

*Multi-island.* To evaluate the multi-island topology, we compare it with a single-island configuration, in which the population competes in a single unified pool. As the number of round-robin evaluations depends on pool size, we ensure the same number of iterations per script for a fair comparison. As shown in Fig. 8, the multi-island topology yields a higher overall win rate and intra-diversity, corroborating that our framework effectively produces high-quality and highly specialized comedy.



<!-- page 0014 -->

*Scale.* We compare three configurations: small, base, and large. Fig. 9 shows the win rate of each relative to the small scale. Increasing the number of islands, scripts, and critics yields improvements. Top scripts from the large configuration achieve a higher win rate compared to the small and base baselines, showing that COMIC scales by trading test-time compute for enhanced performance.

[Figure: Line chart with y-axis “Win Rate” and x-axis “Scale”; categories small, base, large; line increases from about 0.50 to about 0.77 to about 0.85.]

**Fig. 9:** Scale.

*No-critics baseline.* Fig. 10 presents results from an A/B preference study comparing the full COMIC pipeline against the critic-free ablation. Human raters overwhelmingly preferred the full COMIC framework across all dimensions (*Script, Narrative, Realism, Consistency, Funniness*), confirming that iterative multi-agent critic refinement is essential for high-quality comedic content.

[Figure: Bar chart comparing “Ours” and “No Critics” by percentage. Script: 57% vs 43%; Narrative: 71% vs 29%; Realism: 88% vs 12%; Consistency: 100%; Funniness: 62% vs 38%.]

**Fig. 10:** User study against No Critics.

## 5 Conclusion

In this paper, we introduce COMIC, a fully automated multi-agent framework designed to tackle the extremely open-ended challenge of sketch comedy video generation. By shifting away from single-pass, fixed-objective pipelines, COMIC leverages a multi-island topology where diverse, human-aligned critic committees drive iterative refinement. The competitive pressure operates across both the narrative scriptwriting and visual rendering stages, allowing the system to explore a vast creative space while maintaining coherence. Our experiments demonstrate that COMIC significantly outperforms existing agentic video baselines while offering a dual mechanism for test-time scaling. Ultimately, this work establishes a new state of the art for automated, engaging, long-form video production.

Although parallelization across local structures can reduce time complexity, the iterative refinement process incurs computational costs. Additionally, we use normalized YouTube view counts as a proxy for humor quality, but this may introduce noise from sources such as clickbait and algorithmic promotion. Another future direction is the incorporation of sound effects, enriching the audio-visual experience beyond dialogue, as well as developing pipelines to attribute model outputs and quantify originality when building on large internet corpora.

COMIC’s improvements emerge without parameter updates, gradient-based optimization, or a fixed reward signal, connecting to the *Red Queen* hypothesis [40] in evolutionary biology, wherein species must continuously evolve to maintain their fitness against co-evolving competitors. Unlike structured domains such as mathematics [43] or board games [36], comedy’s shifting, context-dependent criteria make it a compelling proxy for open-ended, real-world problems. We believe that this work opens several directions for future research into other creative domains.



<!-- page 0015 -->

# References

1. Arrow, K.J.: A difficulty in the concept of social welfare. Journal of political economy **58**(4), 328–346 (1950)
2. Cantú-Paz, E., et al.: A survey of parallel genetic algorithms. Calculateurs paralleles, reseaux et systems repartis **10**(2), 141–171 (1998)
3. Chan, C.M., Chen, W., Su, Y., Yu, J., Xue, W., Zhang, S., Fu, J., Liu, Z.: Chateval: Towards better llm-based evaluators through multi-agent debate. arXiv preprint arXiv:2308.07201 (2023)
4. Cho, H., Ahn, D., Hong, S., Kim, J.E., Kim, S., Jin, K.H.: Tag: Tangential amplifying guidance for hallucination-resistant diffusion sampling. arXiv preprint arXiv:2510.04533 (2025)
5. Dalal, K., Koceja, D., Xu, J., Zhao, Y., Han, S., Cheung, K.C., Kautz, J., Choi, Y., Sun, Y., Wang, X.: One-minute video generation with test-time training. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 17702–17711 (2025)
6. Du, Y., Li, S., Torralba, A., Tenenbaum, J.B., Mordatch, I.: Improving factuality and reasoning in language models through multiagent debate. In: Forty-first International Conference on Machine Learning (2023)
7. Fernando, C., Banarse, D., Michalewski, H., Osindero, S., Rocktäschel, T.: Promptbreeder: Self-referential self-improvement via prompt evolution. arXiv preprint arXiv:2309.16797 (2023)
8. Goodhart, C.A.: Problems of monetary management: the uk experience. In: Monetary theory and practice: The UK experience, pp. 91–121. Springer (1984)
9. Google DeepMind: Veo 3.1. https://deepmind.google/models/veo/ (2025)
10. Henschel, R., Khachatryan, L., Poghosyan, H., Hayrapetyan, D., Tadevosyan, V., Wang, Z., Navasardyan, S., Shi, H.: Streamingt2v: Consistent, dynamic, and extendable long video generation from text. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 2568–2577 (2025)
11. Hong, S., Zhuge, M., Chen, J., Zheng, X., Cheng, Y., Wang, J., Zhang, C., Wang, Z., Yau, S.K.S., Lin, Z., et al.: Metagpt: Meta programming for a multi-agent collaborative framework. In: The twelfth international conference on learning representations (2023)
12. Hong, S., Kemelmacher-Shlizerman, I., Curless, B., Seitz, S.M.: Musicinfuser: Making video diffusion listen and dance. arXiv preprint arXiv:2503.14505 (2025)
13. Hong, S., Seo, J., Shin, H., Hong, S., Kim, S.: Direct2v: Large language models are frame-level directors for zero-shot text-to-video generation. arXiv preprint arXiv:2305.14330 (2023)
14. Huang, H., Feng, Y., Shi, C., Xu, L., Yu, J., Yang, S.: Free-bloom: Zero-shot text-to-video generator with llm director and ldm animator. Advances in Neural Information Processing Systems **36**, 26135–26158 (2023)
15. Huang, K., Huang, Y., Wang, X., Lin, Z., Ning, X., Wan, P., Zhang, D., Wang, Y., Liu, X.: Filmaster: Bridging cinematic principles and generative ai for automated film generation. arXiv preprint arXiv:2506.18899 (2025)
16. Kong, W., Tian, Q., Zhang, Z., Min, R., Dai, Z., Zhou, J., Xiong, J., Li, X., Wu, B., Zhang, J., et al.: Hunyuanvideo: A systematic framework for large video generative models. arXiv preprint arXiv:2412.03603 (2024)
17. Labs, B.F.: FLUX.2: Frontier Visual Intelligence. https://bfl.ai/blog/flux-2 (2025)



<!-- page 0016 -->

18. Li, Y., Shi, H., Hu, B., Wang, L., Zhu, J., Xu, J., Zhao, Z., Zhang, M.: Anim-director: A large multimodal model powered agent for controllable animation video generation. In: SIGGRAPH Asia 2024 Conference Papers. pp. 1–11 (2024)

19. Lian, L., Shi, B., Yala, A., Darrell, T., Li, B.: Llm-grounded video diffusion models. arXiv preprint arXiv:2309.17444 (2023)

20. Lin, G., Jiang, J., Yang, J., Zheng, Z., Liang, C., Zhang, Y., Liu, J.: Omnihuman-1: Rethinking the scaling-up of one-stage conditioned human animation models. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 13847–13858 (2025)

21. Lin, H., Zala, A., Cho, J., Bansal, M.: Videodirectorgpt: Consistent multi-scene video generation via llm-guided planning. arXiv preprint arXiv:2309.15091 (2023)

22. Liu, F., Tong, X., Yuan, M., Lin, X., Luo, F., Wang, Z., Lu, Z., Zhang, Q.: Evolution of heuristics: Towards efficient automatic algorithm design using large language model. arXiv preprint arXiv:2401.02051 (2024)

23. Long, D.X., Wan, X., Nakhost, H., Lee, C.Y., Pfister, T., Arık, S.Ö.: Vista: A test-time self-improving video generation agent. arXiv preprint arXiv:2510.15831 (2025)

24. Luma AI: Dream machine. https://lumalabs.ai/dream-machine (2024)

25. Marx, N.: Live from new york: The complete uncensored history of “saturday night live” as told by its stars, writers, and guests (2016)

26. Meta: Meta movie gen. https://ai.meta.com/research/movie-gen/ (2024)

27. Mouret, J.B., Clune, J.: Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909 (2015)

28. Novikov, A., Vũ, N., Eisenberger, M., Dupont, E., Huang, P.S., Wagner, A.Z., Shirobokov, S., Kozlovskii, B., Ruiz, F.J., Mehrabian, A., et al.: Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131 (2025)

29. OpenAI: Sora 2. https://openai.com/index/sora-2/ (2025)

30. Pika: Pika. https://pika.art/ (2024)

31. Qian, C., Liu, W., Liu, H., Chen, N., Dang, Y., Li, J., Yang, C., Chen, W., Su, Y., Cong, X., et al.: Chatdev: Communicative agents for software development. In: Proceedings of the 62nd annual meeting of the association for computational linguistics (volume 1: Long papers). pp. 15174–15186 (2024)

32. Resemble AI: Chatterbox-TTS. https://github.com/resemble-ai/chatterbox (2025), gitHub repository

33. Romera-Paredes, B., Barekatain, M., Novikov, A., Balog, M., Kumar, M.P., Dupont, E., Ruiz, F.J., Ellenberg, J.S., Wang, P., Fawzi, O., et al.: Mathematical discoveries from program search with large language models. Nature **625**(7995), 468–475 (2024)

34. Runway: Gen-4. https://runwayml.com/research/introducing-runway-gen-4 (2025)

35. Shi, H., Li, Y., Chen, X., Wang, L., Hu, B., Zhang, M.: Animaker: Automated multi-agent animated storytelling with mcts-driven clip generation. arXiv preprint arXiv:2506.10540 (2025)

36. Silver, D., Huang, A., Maddison, C.J., Guez, A., Sifre, L., Van Den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., et al.: Mastering the game of go with deep neural networks and tree search. nature **529**(7587), 484–489 (2016)

37. Sims, K.: Artificial evolution for computer graphics. In: Proceedings of the 18th annual conference on Computer graphics and interactive techniques. pp. 319–328 (1991)



<!-- page 0017 -->

38. Tanese, R.: Distributed genetic algorithms for function optimization. University of Michigan (1989)

39. Team, G.: Mochi 1. https://github.com/genmoai/models (2024)

40. Van Valen, L.: A new evolutionary law. Evolutionary theory **1**, 1–30 (1973)

41. Wan, T., Wang, A., Ai, B., Wen, B., Mao, C., Xie, C.W., Chen, D., Yu, F., Zhao, H., Yang, J., et al.: Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314 (2025)

42. Whitley, D., Rana, S., Heckendorn, R.B.: The island model genetic algorithm: On separability, population size and convergence. Journal of computing and information technology **7**(1), 33–47 (1999)

43. Woodruff, D.P., Cohen-Addad, V., Jain, L., Mao, J., Zuo, S., Bateni, M., Branzei, S., Brenner, M.P., Chen, L., Feng, Y., et al.: Accelerating scientific research with gemini: Case studies and common techniques. arXiv preprint arXiv:2602.03837 (2026)

44. Wu, W., Zhu, Z., Shou, M.Z.: Automated movie generation via multi-agent cot planning. arXiv preprint arXiv:2503.07314 (2025)

45. Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q.V., Zhou, D., Chen, X.: Large language models as optimizers. In: The Twelfth International Conference on Learning Representations (2023)

46. Yuan, S., Song, K., Chen, J., Tan, X., Li, D., Yang, D.: Evoagent: Towards automatic multi-agent generation via evolutionary algorithms. In: Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). pp. 6192–6217 (2025)

47. Zhang, J., Hu, S., Lu, C., Lange, R., Clune, J.: Darwin godel machine: Open-ended evolution of self-improving agents. arXiv preprint arXiv:2505.22954 (2025)

48. Zhang, L., Agrawala, M.: Packing input frame context in next-frame prediction models for video generation. arXiv preprint arXiv:2504.12626 (2025)

49. Zheng, M., Xu, Y., Huang, H., Ma, X., Liu, Y., Shu, W., Pang, Y., Tang, F., Chen, Q., Yang, H., et al.: Videogen-of-thought: Step-by-step generating multi-shot video with minimal manual intervention. arXiv preprint arXiv:2412.02259 (2024)



<!-- page 0018 -->

# COMIC: Agentic Sketch Comedy Generation

Supplementary Material

## A Video Results

We include the MP4 files of the videos in the separate supplementary material. We strongly encourage readers to watch them.

## B Critic Selection

*Varying in-context sample size.* To evaluate the impact of in-context learning on our script critic selection process, we analyze how the number of tier-labeled samples provided to the selector affects its ability to identify high-performing critics. We vary the number of samples among 0 (zero-shot), 15, and 45, and measure the resulting performance across different engagement tiers. As shown in Table 7, the zero-shot strategy also produces an average correct ranking between tiers. The results further indicate that the *Task-Wise Best* selection performance improves as the sample size increases and consistently achieves the highest accuracy, making *Task-Wise Best* with 45 samples the optimal choice.

| # Samples | Comparison | Mean Critic | Single Best | Task-Wise Best |
|---:|---|---:|---:|---:|
| 0 | Top vs. Middle | 0.542 | 0.572 | 0.642 |
|  | Top vs. Bottom | 0.700 | 0.728 | 0.802 |
| 15 | Top vs. Middle | 0.547 | 0.590 | 0.644 |
|  | Top vs. Bottom | 0.697 | 0.702 | 0.808 |
| 45 | Top vs. Middle | 0.542 | 0.572 | 0.644 |
|  | Top vs. Bottom | 0.708 | 0.740 | 0.830 |

**Table 5:** Validation accuracy as a function of in-context sample size. Task-wise selection consistently achieves the highest accuracy and benefits most from calibration examples.

*Data processing details.* We collect 4,940 data points from five YouTube sketch comedy channels, excluding videos that do not meet our criteria on length and format. To construct channel-specific engagement scores, we model the cumulative view trajectory of each sketch using a logistic growth function. This reflects the S-curve observations of view counts in online videos. Fig. 11 presents the fits of the logistic growth model for all five channels. Based on the projected carrying capacity $L_{\mathrm{proj}}$, we extract 30 data points from each of the 5 channels and each of the 3 tiers, resulting in 450 total data points. We then split them into $S_{\mathrm{in\text{-}context}}$, $S_{\mathrm{val}}$, and $S_{\mathrm{test}}$ as mentioned in the main paper.



<!-- page 0019 -->

[Figure: Logistic growth model fits shown as paired linear-scale and log-scale scatter plots for five comedy channels. Rows labeled Studio C, Foil Arms & Hog, Viva La Dirt League, Key & Peele, and SNL. Each plot includes red “Data” points, a blue logistic fit line, and a dotted green “Carrying Capacity (L)” line. Axes include “Views,” “Views (Log),” “Days Since Published,” and “Days (Log).” Legends show: Studio C — “L=5.0e+06, r=0.001, t₀=3919.1”; Foil Arms & Hog — “L=4.3e+05, r=0.004, t₀=283.1”; Viva La Dirt League — “L=1.0e+06, r=0.003, t₀=213.6”; Key & Peele — “L=1.5e+07, r=0.002, t₀=2431.4”; SNL — “L=2.0e+06, r=0.006, t₀=53.9”.]

**Fig. 11:** Logistic growth model fits for cumulative view counts across different comedy channels.



<!-- page 0020 -->

## C Storyboard Output Structure

The scene director agent outputs a structured JSON object that serves as the complete production specification for the video rendering stage. Given a script and user-specified character and background assets, the agent extracts all characters and backgrounds, generates viewpoint variations for each base background (*e.g.*, turning back, left, and right), and divides the script into shots. The full schema is shown in Listing 12.

```
{
  "characters": [{
    "name": "...",              // Full name from script
    "description": "...",       // Physical and personality details
    "portrait_path": "...",     // Path to reference image, or null
    "voice_path": "...",        // Path to voice sample, or null
    "t2i_prompt": "...",        // Image gen prompt (if no portrait_path)
    "t2a_prompt": "...",        // Voice gen prompt (if no voice_path)
    "is_user_specified": true
  }],
  "backgrounds": [{
    "name": "...",              // Unique name, e.g., "Lab Front View"
    "description": "...",
    "image_path": "...",        // Path to reference image, or null
    "t2i_prompt": "...",        // Full scene prompt for base backgrounds
    "base_background": "...", // Parent background name (variations only)
    "variation_prompt": "...",// Viewpoint edit prompt (variations only)
    "is_user_specified": false
  }],
  "shots": [{
    "shot_id": "shot_01",
    "speaker": "...",          // Exact character name, or null
    "line": "...",             // Dialogue text
    "voice_intensity": 0.5,    // 0.0 (low) to 1.5 (extreme)
    "first_frame": {
      "setup_notes": "...",
      "reference": {
        "reference_characters": ["..."], // Visible characters
        "reference_backgrounds": ["..."],// Background behind speaker
        "reference_shots": ["..."],      // Prior shots for continuity
        "edit_prompt": "..." // Static composition
      },
      "generation_prompt": null // Non-null only if no references
    },
    "video_prompt": "..."      // Camera motion and actions
  }]
}
```

**Fig. 12:** Storyboard output structure produced by the scene director.

## D Scale Configurations

COMIC exposes several natural scaling dimensions: number of islands $K$, scripts per island $|\mathcal{S}_k|$, critics per island $|\mathcal{C}_k|$, scene directions $D$, and rendering critics $|\mathcal{C}_{\mathrm{render}}|$. Round-robin pairwise evaluation within islands requires $\mathcal{O}(K|\mathcal{S}_k|^2|\mathcal{C}_k|)$



<!-- page 0021 -->

critic calls per generation, which is substantially lower than a global tournament over all scripts that would require $O(K^2|\mathcal{S}_k|^2|\mathcal{C}_k|)$ calls. Island-local evaluation is, therefore, not merely a diversity mechanism but also a computational necessity that makes iterative refinement at scale tractable.

Table 6 summarizes the three scale configurations of COMIC: small, base, and large.

| Scale | $K$ | $|\mathcal{S}_k|$ | $|\mathcal{C}_k|$ | $D$ | $|\mathcal{C}_{\mathrm{render}}|$ |
|---|---:|---:|---:|---:|---:|
| Small | 2 | 2 | 2 | 1 | 0 |
| Base | 3 | 3 | 3 | 2 | 1 |
| Large | 4 | 4 | 4 | 4 | 2 |

**Table 6:** Scale configurations for the COMIC framework.

*Computational complexity.* We analyze the computational cost of COMIC across its key scaling dimensions: $K$ islands, $|\mathcal{S}_k|$ scripts per island, $|\mathcal{C}_k|$ critics per island, $D$ scene directions, $|\mathcal{C}_{\mathrm{render}}|$ rendering critics, maximum $N := \max_j N_j$ shots per video, and $G$ generations.

Within each island, a single generation requires a round-robin pairwise tournament over $|\mathcal{S}_k|$ scripts, each evaluated by all $|\mathcal{C}_k|$ critics, incurring $O(|\mathcal{S}_k|^2|\mathcal{C}_k|)$ evaluations per island. Across $K$ islands and $G$ generations, the total writing-stage cost is:

$$
O(G \cdot K \cdot |\mathcal{S}_k|^2 \cdot |\mathcal{C}_k|).
\tag{12}
$$

Crucially, this remains lower than a globally pooled tournament over all $K|\mathcal{S}_k|$ scripts, which would require $O(G \cdot K^2|\mathcal{S}_k|^2 \cdot |\mathcal{C}_k|)$ evaluations.

For each selected script, we generate $D$ scene directions and refine each of the $N$ shots over $|\mathcal{C}_{\mathrm{render}}|$ critic iterations, yielding $O(D \cdot N \cdot |\mathcal{C}_{\mathrm{render}}|)$ render calls per script. Shot-level tournament selection adds $O(D \cdot N \cdot |\mathcal{C}_{\mathrm{render}}|^2)$ comparisons (single-elimination), and the final video-level tournament over $D$ complete videos costs $O(D \cdot |\mathcal{C}_{\mathrm{render}}|)$ comparisons. The dominant term for the rendering stage is therefore:

$$
O(D \cdot N \cdot |\mathcal{C}_{\mathrm{render}}|^2) \quad \text{render calls per script.}
\tag{13}
$$

In practice, the base configuration takes approximately one day to run on a single H200 GPU with an API budget of around $5, which is evidently lower than the cost of producing traditional comedy shows. Furthermore, the system is highly parallelizable. For example, we can parallelize API or model calls with respect to multiple islands and storyboards.

# E Script Inspection and Selection

After script evolution completes on all islands, the refined scripts undergo an inspection phase to correct formatting errors, character inconsistencies, dialogue



<!-- page 0022 -->

incoherence, and structural issues. This quality control ensures that evolved scripts meet production standards before video rendering.

To select top scripts for rendering from across all islands, we conduct a round-robin league tournament where each script competes against all others using the best critic (the one with the highest validation accuracy) from the specialized critic pool $\mathcal{C}_{\text{task}}$. Scripts are ranked by win rate, and top-performing scripts proceed to the video rendering phase. This cross-island competition identifies scripts that are not only strong within their local ecosystems but also demonstrate broader appeal when evaluated by a high-performing generalist critic.

## F Models

A key feature of our framework is the ability to easily integrate modular foundational models at different production stages. Table 7 summarizes the models used throughout the COMIC pipeline. We use Claude 3.5 Sonnet for concept and script generation. For tasks requiring efficiency during iterative refinement, we utilize Claude 3.5 Haiku for language-only critics and Gemini 3 Flash Preview for multimodal critics. For tasks requiring more robust reasoning—such as script inspection, meta-critic instruction generation, and final scene direction—we employ Claude 3.5 Opus.

After all island iterations, scripts are inspected, and a final evaluation is conducted in which all islands are merged into a single league. This league is evaluated by a specialized critic committee tailored to an academic audience. Following this, the top four scripts are selected for production.

For visual synthesis, we use FLUX.2 [dev] [17] to generate canonical character appearances and enhance visual clarity, supplemented by TAG [4], which is condition-agnostic and applicable to image and diffusion models with various conditions. For voice consistency, we employ ElevenLabs and Chatterbox-TTS [32] to generate stable voice prints for each character. These assets are stored in the visual memory bank $\mathcal{M}_{\text{visual}}$ and retrieved during shot generation. Video rendering leverages Wan 2.1 [41]. Since our image and video generation requires taking various modalities of input, *e.g.*, image, text, and audio, we add an additional manifold-tangential term to the predicted denoising score [4], which is agnostic to the input condition yet improves visual clarity and reduces hallucination. Additionally, we use an image critic to perform best-of-batch selection to further enhance quality and consistency. All image, video, and voice generation is performed on an H200.

## G Human Evaluation Protocol

*Baseline comparison.* We evaluated five methods: COMIC (ours), VGoT [49], MovieAgent [44], Veo 3.1 [9], and Sora 2 [29]. We conducted a baseline video evaluation with participants across the US, Europe, and Asia, yielding 22 responses per method (110 responses in total). Each method was represented by four videos, and each participant viewed two videos per method, rating all



<!-- page 0023 -->

| Component | Model |
|---|---|
| Concept and Script Writing | Claude 3.5 Sonnet |
| Language-Only Critics | Claude 3.5 Haiku |
| Multi-Modal Critics | Gemini 3 Flash Preview |
| Script Inspection | Claude 3.5 Opus |
| Scene Direction Generation | Claude 3.5 Opus |
| Meta-Critic | Claude 3.5 Opus |
| Character Image Synthesis | FLUX.2 [dev] + TAG |
| Voice Synthesis | ElevenLabs |
| Voice Cloning | Chatterbox-TTS |
| Video Rendering | Wan 2.1 + TAG |

**Table 7:** Models used in the pipeline.

five methods. The four COMIC videos were generated from the top-performing scripts selected automatically by our pipeline, without manual curation. For the baselines, each method was run four times independently to obtain the same sample size. Fig. 13 illustrates the rating distributions, where we were able to obtain highly diverse opinions. Participants rated each video on a 7-point Likert scale across the following dimensions:

1. **Funniness:** “How funny did you find this video?”  
   *(1) Not funny at all → (2) Not very funny → (3) Slightly funny → (4) Moderately funny → (5) Quite funny → (6) Very funny → (7) Extremely funny*

2. **Re-watch Intent:** “Would you like to watch more videos like this?”  
   *(1) Definitely not → (2) Probably not → (3) Unlikely → (4) Neutral → (5) Likely → (6) Probably yes → (7) Definitely yes*

3. **Comparison to Human Comedy:** “Thinking of all the human-made sketch comedies you have ever seen, how funny is this video compared to the average human-made one?”  
   *(1) Much less funny → (2) Less funny → (3) Slightly less funny → (4) Comparable → (5) Slightly funnier → (6) Funnier → (7) Much funnier*

4. **Script Quality:** “How would you rate the funniness of the script?”  
   *(1) Not funny at all → (2) Slightly funny → (3) Somewhat funny → (4) Moderately funny → (5) Quite funny → (6) Very funny → (7) Extremely funny*

5. **Narrative Quality:** “How would you rate the narrative quality of the script (*e.g.*, story arc, pacing)?”  
   *(1) Very poor → (2) Poor → (3) Slightly poor → (4) Neutral → (5) Slightly good → (6) Good → (7) Excellent*

6. **Visual Realism:** “How would you rate the visual realism of this video?”  
   *(1) Very poor → (2) Poor → (3) Slightly poor → (4) Neutral → (5) Slightly good → (6) Good → (7) Excellent*

7. **Visual Consistency:** “How would you rate the visual consistency of this video (*e.g.*, characters, backgrounds)?”



<!-- page 0024 -->

*(1) Very poor → (2) Poor → (3) Slightly poor → (4) Neutral → (5) Slightly good → (6) Good → (7) Excellent*

*Ablation study.* Participants completed a paired A/B comparison between COMIC and the critic-free baseline across five dimensions:

1. **Funniness:** “Which video do you find funnier?”
2. **Script Quality:** “Which video has a funnier script?”
3. **Narrative Quality:** “Which video has better narrative flow (*e.g.*, story arc, pacing)?”
4. **Visual Realism:** “Which video has higher realism?”
5. **Visual Consistency:** “Which video has higher visual consistency (*e.g.*, characters, backgrounds)?”

Each question offered three choices: *Video A*, *About the same*, or *Video B*. Neutral responses (*About the same*) were excluded from the analysis.

[Figure: A 3×5 grid of bar charts showing distributions of human evaluation ratings for COMIC compared to baseline methods. Rows are labeled “Funniness,” “Watch More,” and “vs. Human Comedy.” Columns are labeled “Veo 3.1,” “Sora 2,” “VGoT,” “MovieAgent,” and “Ours.” The y-axis label is “% of responses.” Dashed vertical lines indicate mean ratings with visible values: Funniness—Veo 3.1 $\mu=2.32$, Sora 2 $\mu=2.73$, VGoT $\mu=1.18$, MovieAgent $\mu=1.27$, Ours $\mu=3.45$; Watch More—Veo 3.1 $\mu=2.36$, Sora 2 $\mu=2.73$, VGoT $\mu=1.27$, MovieAgent $\mu=1.09$, Ours $\mu=3.09$; vs. Human Comedy—Veo 3.1 $\mu=2.27$, Sora 2 $\mu=2.32$, VGoT $\mu=1.14$, MovieAgent $\mu=1.18$, Ours $\mu=3.05$.]

**Fig. 13:** Distributions of human evaluation ratings for COMIC compared to baseline methods.
