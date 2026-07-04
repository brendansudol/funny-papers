# CFunModel: A "Funny" Language Model Capable of Chinese Humor Generation and Processing

**Zhenghan Yu, Xinyu Hu, Xiaojun Wan** — arXiv:2503.20417 · Guide entry #51 (Part 7 - Cross-Cultural & Translation)

[paper page](https://arxiv.org/abs/2503.20417) · [local PDF](../pdfs/51-cfunmodel.pdf) · [full markdown](../md/51-cfunmodel/51-cfunmodel.md) · [extract](../extracts/51-cfunmodel.json) · [dataset: CFunSet](../../data/cfunset/)

## TL;DR
CFunModel introduces CFunSet, a Chinese humor-related multi-task dataset with over 160,000 samples, and uses it to supervised fine-tune Qwen2.5-7B-Instruct into a humor-specialized model. The main quantitative result is that CFunModel beats the tested LLM baselines on crosstalk response selection and humor recognition, reaching 91.70% accuracy on CrossDial-Dougen, 88.99% on CrossDial-Penggen, and 85.98% on HumorWB.

## Problem & Motivation
The paper argues that LLMs still struggle with Chinese humor because humor depends on cultural context, specialized knowledge, and creativity, while existing Chinese humor datasets are limited and usually focus on only one task. The authors aim to build a broader resource and a model that can handle both humor understanding and humor generation. Targeted tasks include Humor Recognition, Crosstalk Response Selection, Joke Generation/Continuation, Humor Explanation, and Crosstalk Generation/Continuation.

## Approach
The authors build CFunSet by aggregating and cleaning several Chinese humor resources and adding jokes collected from Tieba—JokeBar. Qwen2.5-7B-Instruct is used during data processing to filter Tieba texts for joke-like content and to extract keywords or themes from CCL2019-Chinese-Humor-Computation jokes. Each CFunSet example is formatted as an instruction, an input, and an output. CFunModel is then created by supervised fine-tuning Qwen2.5-7B-Instruct on CFunSet for 2 epochs, with learning rate 2e-5 and batch size 128, using four A40 GPUs.

## Data & Experimental Setup
CFunSet contains over 160,000 samples and includes over 20,000 jokes from Tieba—JokeBar. Other sources include CrossDial, Chumor 2.0, HumorWB, Chinese-Humor-Sentiment, Crosstalk-Generation, and CCL-2019-Chinese-Humor-Computation. For HumorWB, the paper manually creates a split of 4,200 training samples and 1,091 test samples. For CrossDial, evaluation uses 4,664 Dougen response-selection test samples and 2,688 Penggen response-selection test samples. Baselines include GPT-4o, GPT-4o mini, DeepSeek-V3, and Qwen2.5-7B-Instruct; Table 3 also reports ERNIE and RoBERTa results from Huang et al. (2022). Accuracy is used for recognition and response selection; joke and crosstalk generation are evaluated through case studies.

## Results
On CrossDial-Dougen, CFunModel scores 91.70 accuracy, beating ERNIE at 84.54 by 7.16 points, DeepSeek-V3 at 83.66 by 8.04 points, GPT-4o at 79.67 by 12.03 points, GPT-4o mini at 74.14 by 17.56 points, and Qwen2.5-7B-Instruct at 24.74 by 66.96 points. On CrossDial-Penggen, CFunModel scores 88.99, beating DeepSeek-V3 at 78.16 by 10.83 points, RoBERTa at 76.19 by 12.80 points, GPT-4o at 73.88 by 15.11 points, GPT-4o mini at 67.45 by 21.54 points, and Qwen2.5-7B-Instruct at 20.87 by 68.12 points. On HumorWB, CFunModel scores 85.98, ahead of DeepSeek-V3 at 85.15 by 0.83 points, GPT-4o mini at 84.78 by 1.20 points, GPT-4o at 83.41 by 2.57 points, and Qwen2.5-7B-Instruct at 79.56 by 6.42 points. In qualitative examples, the paper reports that CFunModel produces more coherent and humorous jokes and stronger crosstalk scripts than Qwen2.5-7B-Instruct.

## Takeaways
- Multi-task supervised fine-tuning on Chinese humor data substantially improves Qwen2.5-7B-Instruct on CrossDial response selection.
- Humor recognition improves more modestly, with CFunModel only 0.83 points above DeepSeek-V3 on HumorWB.
- The paper treats Chinese humor as a mixture of recognition, explanation, response selection, and open-ended generation rather than a single benchmark task.
- For builders of humor systems, CFunSet is the main artifact: it supplies instruction-formatted data across jokes, crosstalk, explanations, and social-media humor.

## Limitations & Caveats
The paper’s explicit limitation is that Tieba-JokeBar data may still contain misspellings, grammatical errors, and incorrect punctuation. Open-ended generation is assessed only by case studies, with no reported human ratings. The paper also states that CFunModel was evaluated with temperature 0, while the baseline comparison setup used temperature 1.
