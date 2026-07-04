# AI Humor Generation: Cognitive, Social and Creative Skills for Effective Humor

**Sean Kim, Lydia B. Chilton** — arXiv:2502.07981 · Guide entry #14 (Part 2 - Generating Jokes)

[paper page](https://arxiv.org/abs/2502.07981) · [local PDF](../pdfs/14-ai-humor-generation-skills.pdf) · [full markdown](../md/14-ai-humor-generation-skills/14-ai-humor-generation-skills.md) · [extract](../extracts/14-ai-humor-generation-skills.json)

## TL;DR
The paper introduces HumorSkills, a multi-step LLM/VLM system for generating Gen Z-style humorous captions for images. In a human rating study, HumorSkills was rated significantly funnier than GPT-4o with prompt engineering and nearly tied with the top five upvoted Instagram comments: it was only 0.08 points lower on a 5-point scale, with p=0.053.

## Problem & Motivation
The authors ask whether AI humor improves when a system is given skills that resemble those used by human humorists: noticing visual details, finding relatable social conflicts, generating multiple angles, and modeling a specific audience. They focus on one constrained but socially important humor genre: Instagram image captions for Gen Z humor fans. This setting provides images as setups, captions as punchlines, and an audience with recognizable tastes, slang, and shared cultural references.

## Approach
HumorSkills takes an image and returns five captions. First, GPT-4o performs visual detail extraction, describing subjects, actions, background elements, expressions, and notable visual oddities. Second, GPT-4o performs visual humor ideation, identifying humorous visual contrasts or potential joke targets. Third, GPT-4o generates narrative and conflict extrapolations grounded in common Gen Z experiences such as school, work, family, relationships, student loans, and social interactions. Fourth, a fine-tuned GPT-3.5 model generates 30 captions: 15 based mainly on the visual details and humor ideation, and 15 that also incorporate the external narratives. Finally, a GPT-4o-based Gen Z humor ranking agent ranks the 30 captions by humor, relatability, and fit to the image, returning the top five.

## Data & Experimental Setup
The main study used 20 images from 8 popular Instagram humor captioning accounts. For each image, raters saw 15 captions: the top 5 most upvoted Instagram comments, 5 GPT-4o captions, and 5 HumorSkills captions. Captions were rated from 1 to 5, where 1 was “not funny,” 3 was “somewhat funny,” and 5 was “very funny.” The survey had 32 respondents and 6015 observations. The authors also tested out-of-domain images: 30 randomly selected images from the Flickr Image Dataset and 30 museum art images, split as 15 from The MoMA and 15 from The Met. Those studies compared only HumorSkills against GPT-4o.

## Results
On the target Instagram caption task, HumorSkills averaged 2.27 out of 5. GPT-4o was 0.213 points lower, significant at p<0.0001; Table 1 reports a HumorSkill intercept of 2.273 and a GPT-4o coefficient of -0.213. Top Instagram captions were only 0.08 points higher than HumorSkills, with p=0.053, so the paper concludes HumorSkills was not statistically less funny than the top human captions. On Flickr camera-roll-style images, HumorSkills scored 2.19 vs. 1.9 for GPT-4o, a 0.291-point gain; the text reports p=0.022 and Table 2 reports P>|z| as 0.000. On museum art, HumorSkills scored 2.18 vs. 2.00 for GPT-4o, reported as a 0.18-point gain with p=0.023; Table 3 reports a coefficient of 0.175 and P>|z| of 0.000.

## Takeaways
- Targeting a specific audience matters: fine-tuning helped HumorSkills use Gen Z slang and references such as Minecraft, GTA, Snapchat, and “adhd.”
- Narrative extrapolation helped turn visually unrelatable images into jokes about relatable conflicts such as healthcare, chargers, student loans, or relationships.
- Visual detail extraction and humor ideation helped the system choose sharper joke targets than the baseline in several qualitative examples.
- For builders, the paper suggests that chaining specialized humor skills can outperform a single prompt to a strong VLM.
- For evaluators, the study shows the need for audience-specific human ratings because humor ratings have high variance and broad humor ability is not tested by one genre.

## Limitations & Caveats
The work studies only Gen Z Instagram-style caption humor, a genre that often rewards absurdity and already provides the setup as an image. It does not test standup, written jokes with setup and punchline, or insider humor among friends. The GPT-4o baseline used a simple prompt, and the authors note that stronger prompts or multiple generations might close the gap. No ablation study establishes which HumorSkills component mattered most.
