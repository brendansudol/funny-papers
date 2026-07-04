<!-- guide claims for x11-rjokes-last-laugh (Part 8 (pre-LLM anchor)) -->

### Pre-LLM dataset anchors (compact)
The classic resources the LLM-era work quietly stands on:
- **HaHackathon — SemEval-2021 Task 7** (Meaney, Wilson, Chiruzzo, Lopez & Magdy, 2021) `dataset` — jointly rated humor **and offense** (detection + rating). The original benchmark for the funny-vs-harmful boundary now central to Part 6.
- **Humicroedit & FunLines — SemEval-2020 Task 7** (Hossain, Krumm, Gamon & Kautz, 2019–2020) `dataset` — humor created via *minimal edits* to news headlines. The direct ancestor of MWAHAHA's headline setting, and the original minimal-pair humor-data idea that #56 modernizes with LLM "unfunning."
- **rJokes** (Weller & Seppi — "Humor Detection: A Transformer Gets the Last Laugh," EMNLP 2019; corpus paper LREC 2020) `dataset` — the large-scale Reddit joke corpus with upvote-derived humor degrees; still a standard detection/training source.
- **UR-FUNNY** (Hasan et al., EMNLP 2019) `dataset` — multimodal (text + audio + video) humor detection from TED talks; the precursor to the stand-up/video line (#44). Its sarcasm sibling is **MUStARD** (Castro et al., ACL 2019; cf. Adjacent) — from the same Castro/Mihalcea line that now runs MWAHAHA (#57).
