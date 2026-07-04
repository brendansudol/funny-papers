# Humor Detection: A Transformer Gets the Last Laugh

**Orion Weller, Kevin Seppi** — EMNLP 2019 · Guide entry Part 8 (pre-LLM anchor) (Part 8 - Datasets & Shared Tasks)

[paper page](https://aclanthology.org/D19-1372/) · [local PDF](../pdfs/x11-rjokes-last-laugh.pdf) · [full markdown](../md/x11-rjokes-last-laugh/x11-rjokes-last-laugh.md) · [extract](../extracts/x11-rjokes-last-laugh.json) · [dataset: rJokes corpus](../../data/rjokes/)

## TL;DR
Weller and Seppi introduce a humor assessment setup that uses Reddit r/Jokes upvotes as labels and fine-tunes a BERT-based Transformer to classify jokes as funny or not funny. On the full Reddit test set, the Transformer reached 0.724 accuracy, beating their CNN baseline at 0.688 and a general-population Mechanical Turk majority-vote baseline at 0.663. The same Transformer approach also reports strong joke-vs-non-joke transfer results: F1 0.931 on Pun of the Day and 0.986 on Short Jokes.

## Problem & Motivation
Prior humor work often focused on recognizing whether a text is a joke. This paper asks a narrower and harder question: given something that is already a joke, can a model assess whether it is humorous? The authors use Reddit r/Jokes because it provides a large audience reaction signal through upvotes, with tens of thousands of jokes posted monthly and over 16 million members. They frame this as learning humor for a specific subset of the population rather than discovering an absolute truth about humor.

## Approach
The authors collect Reddit jokes through Reddit’s public API, preserving the body and punchline fields and repeatedly updating upvote scores. They create three versions of the Reddit task: body only, punchline only, and full joke. Scores ranged from 0 to 136,354 upvotes; because they found a major jump between the 0-200 upvote range and higher scores, they used 200 upvotes as the humor cutoff, yielding 13884 not-funny jokes and 2025 funny jokes. The model is based on pre-trained BERT, with an additional output layer for classification. It uses a learning rate of 2e-05, maximum sequence length 128, and training for up to 7 epochs.

## Data & Experimental Setup
The Reddit data was collected hourly during March and April 2019. The authors use a 75/25 stratified split, upsample the humorous class in the training set until the classes are balanced, and downsample validation/test data to a 50/50 class split. Baselines include a CNN with Highway Layers and a human baseline from 199 Amazon Mechanical Turk participants, each rating an average of 30 jokes. They also evaluate on a recreated Short Jokes identification dataset based on 231,657 Kaggle short jokes plus WMT16 English news sentences, and on Pun of the Day, which contains 16001 puns and 16002 not-punny sentences.

## Results
On Reddit, the Transformer beats the CNN and human baseline on all three input variants. Body-only accuracy is 0.661 for the Transformer, 0.651 for CNN, and 0.493 for Human (General). Punchline-only accuracy is 0.692 for the Transformer, 0.684 for CNN, and 0.592 for Human (General). Full-joke accuracy is 0.724 for the Transformer, 0.688 for CNN, and 0.663 for Human (General). On Pun of the Day, the Transformer obtains Accuracy 0.930, Precision 0.930, Recall 0.931, and F1 0.931; the strongest previous CNN+F+HN row has Accuracy 0.894 and F1 0.901. On Short Jokes Identification, the Transformer reports 0.986 for Accuracy, Precision, Recall, and F1, compared with CNN+F+HN at Accuracy 0.906 and F1 0.924.

## Takeaways
- Reddit upvotes can serve as a large-scale, audience-specific humor signal, but the audience is not general.
- Punchlines are more predictive than bodies across both models and human raters.
- A Transformer trained for Reddit joke humor assessment transfers well to joke and pun identification.
- For humor systems, evaluating “is this funny?” and “is this a joke?” are different tasks.

## Limitations & Caveats
The authors emphasize that humor is subjective and that defining an absolute truth value for a joke’s humor is challenging, if not impossible. The labels reflect Reddit r/Jokes users, and the paper notes that the source contains varied and not safe for work content that the authors do not endorse. The Short Jokes comparison also relies on a recreated dataset because the exact combined dataset used in prior work was not publicly available.
