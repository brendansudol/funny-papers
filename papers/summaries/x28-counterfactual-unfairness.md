# Investigating Counterfactual Unfairness in LLMs towards Identities through Humor

**Shubin Kim, Yejin Son, Junyeong Park, Keummin Ka, Seungbeen Lee, Jaeyoung Lee, Hyeju Jang, Alice Oh, Youngjae Yu** — ACL 2026 · Guide entry Part 6 (relational fairness) (Part 6 - Safety, Harm & Boundaries)

[paper page](https://aclanthology.org/2026.acl-long.2041/) · [local PDF](../pdfs/x28-counterfactual-unfairness.pdf) · [full markdown](../md/x28-counterfactual-unfairness/x28-counterfactual-unfairness.md) · [extract](../extracts/x28-counterfactual-unfairness.json) · [dataset: Counterfactual humor fairness data](../../data/counterfactual-humor-fairness/)

## TL;DR
This paper uses humor as a probe for counterfactual unfairness in LLMs by swapping who speaks, who is targeted, and who listens while holding prompts or jokes constant. Across five major models, privileged speakers are treated more harshly: jokes are refused up to 67.5% more often, identical jokes are attributed more malicious intent, and Task 3 acceptance is lower for Privileged→Marginalized interactions than the reverse.

## Problem & Motivation
The authors argue that humor is a sensitive diagnostic for social assumptions in LLMs because it depends on ambiguity, social context, and judgments about what is acceptable. Prior computational humor and bias work often studies decontextualized jokes; this paper instead asks whether the same humorous content is treated differently when speaker, target, or listener identities are swapped. The framing is counterfactual fairness: changing only an identity role should not mechanically change model behavior unless the social context justifies it.

## Approach
The study has three tasks. Task 1 asks models to generate humor from a specified speaker about a specified target and measures refusal asymmetries. The authors introduce Asymmetric Refusal Rate, ARR = |RR(A→B) − RR(B→A)|, and Speaker Effect, which compares speaker-conditioned refusal against target-only baselines. Task 2 embeds fixed jokes in speaker–listener contexts and asks models to classify humor style and intent valence; the main metric is B_diff, with malicious = +1, uncertain = 0, and benign = −1. Task 3 asks models to generate listener reactions under identity and relationship contexts, then uses GPT-4o to score humor acceptance, social sensitivity, and character consistency on 1–5 scales.

## Data & Experimental Setup
Task 1 uses 80 request templates, 33 identities across 10 categories, 121 speaker–target pairs, and 12,320 prompts per model, producing 61,600 requests and responses across five models. Task 2 and Task 3 use 400 identity-agnostic jokes filtered from the 1,183-joke Humor Recognition dataset, plus 737 identity-specific disparagement jokes curated from HaHackathon. GPT-4.1 first labels candidate identity-specific jokes; seven trained annotators verify them, retaining only unanimous cases. The evaluated models are Claude 3.5 Haiku, GPT-4o, DeepSeek-Reasoner, Gemini 2.5 Flash-Lite, and Grok variants.

## Results
Task 1 shows strong directional refusal. The largest ARR is 67.5% for the poor/wealthy pair with Claude. Averaging Claude, GPT, DeepSeek, and Gemini, American→Chinese requests are refused 71% of the time versus 41% in reverse; lawyer→janitor is 47% versus 20%, and software engineer→janitor is 52% versus 22%.

Task 2 finds the same pattern in intent attribution. Able-bodied→physically disabled humor is labeled malicious at 46.2% versus 21.4% in reverse, with B_diff = 0.501, p < 0.001. For unrelated-target jokes, White speakers talking to Black listeners about Chinese people are judged malicious 73.1% of the time versus 44.3% in reverse, B_diff = 0.595, p < 0.001. Across models, unrelated-target jokes amplify average |B_diff| by 1.71×–3.96×.

Task 3 shows lower acceptance and higher sensitivity for Privileged→Marginalized interactions overall: H = 3.07 versus 3.65, t = -66.89, p < .001, d = -0.39; S = 3.57 versus 3.06, t = 84.42, p < .001, d = 0.49.

## Takeaways
- Humor evaluations expose relational bias that static identity benchmarks may miss.
- Models often use identity cues as proxies for harm rather than interpreting full communicative context.
- Over-refusal can create allocational and representational harms by blocking benign identity-related humor.
- Fair humor systems need consistent standards for harmful requests and more uncertainty-seeking behavior under ambiguous context.

## Limitations & Caveats
The study focuses on a small set of mostly proprietary models and controlled templates rather than natural conversations. It relies substantially on GPT-4o judging, though the authors validate with Llama-3-70B and human annotators. The humor data is limited to identity-agnostic jokes and disparagement humor from existing corpora, and multilingual humor is left for future work.
