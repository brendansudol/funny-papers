# SemEval-2021 Task 7: HaHackathon, Detecting and Rating Humor and Offense

**J.A. Meaney, Steven R. Wilson, Luis Chiruzzo, Adam Lopez, Walid Magdy** — SemEval-2021 · Guide entry Part 8 (pre-LLM anchor) (Part 8 - Datasets & Shared Tasks)

[paper page](https://aclanthology.org/2021.semeval-1.9/) · [local PDF](../pdfs/x09-hahackathon.pdf) · [full markdown](../md/x09-hahackathon/x09-hahackathon.md) · [extract](../extracts/x09-hahackathon.json) · [dataset: HaHackathon (SemEval-2021 Task 7)](../../data/hahackathon/)

## TL;DR
HaHackathon is the SemEval-2021 Task 7 overview paper for a shared task combining humor and offense detection/rating. It introduces a 10,000-text English dataset from Twitter and the Kaggle Short Jokes dataset, with 20 annotations per text. The strongest humor detection system reached F1 0.9854, but humor controversy was much harder, with the best F1 only 0.6302.

## Problem & Motivation
The task addresses humor as a subjective phenomenon that can also provoke offense. Participants had to detect whether a text was intended to be humorous, predict its average humor rating, predict whether humor ratings were controversial, and predict its offense rating. The paper frames this as useful for downstream settings such as content moderation and human-computer interaction, while emphasizing that humor and offense judgments vary across audiences.

## Approach
The organizers created four subtasks: Task 1a humor detection, Task 1b humor rating regression, Task 1c humor controversy detection, and Task 2 offense rating regression. Humor controversy was defined as whether the variance in humor ratings exceeded the median variance in the training set, with median s² = 1.79. The organizers also supplied benchmark systems: Naive Bayes with bag-of-words for classification, support vector regression with TF-IDF for regression, and a BERT-base baseline trained for one epoch with batch size 16 and learning rate 5e-5.

## Data & Experimental Setup
The dataset contains 10,000 English texts: 80% from Twitter and 20% from the Kaggle Short Jokes dataset. Twitter data were selected from US-based humorous and non-humorous accounts, while Kaggle items helped ensure humorous, traditional setup/punchline, and potentially offensive examples. Each text was annotated by 20 Prolific annotators, with 5 annotators from each age group: 18-25, 26-40, 41-55, and 56-70. The final dataset was split 80:10:10 into training, development, and test sets. Data statistics report 6179 humorous vs. 3821 non-humorous texts, 3052 controversial vs. 3017 non-controversial humorous texts, and 5754 texts with offense rating higher than 0.

## Results
Task 1a attracted 58 submissions; PALI ranked first with F1 0.9854 and accuracy 0.9820, beating the BERT baseline F1 0.9283 by 0.0571. Task 1b attracted 50 submissions; abcbpc achieved the best humor-rating RMSE, 0.4959, lower than the BERT baseline 0.8000 by 0.3041. Task 1c attracted 36 submissions; PALI led by F1 with 0.6302, only 0.0070 above the BERT baseline F1 0.6232, showing the difficulty of controversy prediction. Task 2 attracted 48 submissions; DeepBlueAI achieved the best offense-rating RMSE, 0.4120, lower than the BERT baseline 0.5769 by 0.1649. The paper also reports Krippendorff’s α of 0.736 for class label, 0.124 for humor rating, and 0.518 for offense rating.

## Takeaways
- Pre-trained transformer models dominated the leaderboard, usually with ensembling or adaptation techniques.
- Multi-task learning often helped, consistent with reported correlations among humor, offense, and controversy labels.
- Humor detection was highly solvable on this benchmark, but predicting disagreement among annotators remained difficult.
- Systems performed better on Kaggle texts for humor subtasks, while offense RMSE was much lower on Twitter texts because the offense-rating distributions differed.
- Error analysis suggests irony and sarcasm remain problematic for both human labels and model predictions.

## Limitations & Caveats
Humor ratings had low agreement, so controversy labels were built on a noisy subjective signal. The dataset is US English by design, limiting claims about other cultures or language communities. Kaggle and Twitter subsets differ in sampling and label distributions, and several top teams did not provide detailed system descriptions.
