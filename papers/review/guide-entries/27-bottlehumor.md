<!-- guide claims for 27-bottlehumor (#27) -->

### 27. [BottleHumor: Self-Informed Humor Explanation using the Information Bottleneck Principle](https://arxiv.org/abs/2502.18331)
Hwang, West & Shwartz — **Findings of ACL 2025** · `peer-reviewed` `method`
- **Method:** Uses the information-bottleneck principle to extract and iteratively refine the world knowledge a VLM needs to *explain* a meme/cartoon.
- **Findings:** Surfacing the right world knowledge improves explanations — extends the explanation interest into the visual setting and shows world knowledge is the bottleneck.

**Also in this section:** [Humor in Pixels / PixelHumor](https://arxiv.org/abs/2509.12248) (EMNLP Findings 2025, multi-panel online comics) `dataset`; [MemeReaCon](https://arxiv.org/abs/2505.17433) (Zhao et al., EMNLP 2025; 1,565 instances from 5 subreddits keeping image + post + comments) `benchmark`.

**Video humor:** **ExFunTube** — ["Can Language Models Laugh at YouTube Short-form Videos?"](https://arxiv.org/abs/2310.14159) (Ko et al., EMNLP 2023) `dataset` — is the early anchor for *video* humor explanation: funny short-form clips paired with explanations. [**v-HUB**](https://arxiv.org/abs/2509.25773) (Shi, Li, Zhao et al., 2025) `preprint` `benchmark` collects minimally verbal clips from Chaplin-era silent films plus user-generated video, with caption-matching, humor-explanation, and open-ended QA tasks — the purest "can it see the joke *in motion*, without language?" probe. All models drop sharply moving from text- to video-based evaluation, and adding audio (environmental sound) measurably helps: the video-side counterpart to HumorDB (#25), and a moving-picture echo of Baluja's puns-live-in-sound finding (#9).
