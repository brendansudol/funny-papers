<!-- Transcribed from x11-rjokes-last-laugh.pdf -->



<!-- page 0001 -->

# Humor Detection: A Transformer Gets the Last Laugh

**Orion Weller**  
Computer Science Department  
Brigham Young University  
`orionw@byu.edu`

**Kevin Seppi**  
Computer Science Department  
Brigham Young University  
`kseppi@byu.edu`

## Abstract

Much previous work has been done in attempting to identify humor in text. In this paper we extend that capability by proposing a new task: assessing whether or not a joke is humorous. We present a novel way of approaching this problem by building a model that learns to identify humorous jokes based on ratings gleaned from Reddit pages, consisting of almost 16,000 labeled instances. Using these ratings to determine the level of humor, we then employ a Transformer architecture for its advantages in learning from sentence context. We demonstrate the effectiveness of this approach and show results that are comparable to human performance. We further demonstrate our model’s increased capabilities on humor identification problems, such as the previously created datasets for short jokes and puns. These experiments show that this method outperforms all previous work done on these tasks, with an F-measure of 93.1% for the Puns dataset and 98.6% on the Short Jokes dataset.

## 1 Introduction

Recent advances in natural language processing and neural network architecture have allowed for widespread application of these methods in Text Summarization (Liu et al., 2018), Natural Language Generation (Bahuleyan, 2018), and Text Classification (Yang et al., 2016). Such advances have enabled scientists to study common language practices. One such area, humor, has garnered focus in classification (Zhang and Liu, 2014; Chen and Soo, 2018), generation (He et al., 2019; Valitutti et al., 2013), and in social media (Raz, 2012).

The next question then is, what makes a joke humorous? Although humor is a universal construct, there is a wide variety between what each individual may find humorous. We attempt to focus on a subset of the population where we can quantitatively measure reactions: the popular Reddit r/Jokes thread. This forum is highly popular - with tens of thousands of jokes being posted monthly and over 16 million members. Although larger joke datasets exist, the r/Jokes thread is unparalleled in the amount of rated jokes it contains. To the best of our knowledge there is no comparable source of rated jokes in any other language. These Reddit posts consist of the body of the joke, the punchline, and the number of reactions or *upvotes*. Although this type of humor may only be most enjoyable to a subset of the population, it is an effective way to measure responses to jokes in a large group setting.^1

What enables us to perform such an analysis are the recent improvements in neural network architecture for natural language processing. These breakthroughs started with the Convolutional Neural Network (LeCun et al., 1998) and have recently included the inception (Bahdanau et al., 2015) and progress of the Attention mechanism (Luong et al., 2015; Xu et al., 2015), and the Transformer architecture (Vaswani et al., 2017).

## 2 Related Work

In the related work of joke identification, we find a myriad of methods employed over the years: statistical and N-gram analysis (Taylor and Mazlack, 2004), Regression Trees (Purandare and Litman, 2006), Word2Vec combined with K-NN Human Centric Features (Yang et al., 2015), and Convolutional Neural Networks (Chen and Soo, 2018).

This previous research has gone into many settings where humor takes place. Chen and Soo (2018) studied audience laughter compared to textual transcripts in order to identify jokes in conversation, while much work has also gone into us-

---

^1 See the thread (of varied and not safe for work content) at this link. We do not endorse these jokes.

*Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*  
*and the 9th International Joint Conference on Natural Language Processing, pages 3621–3625,*  
Hong Kong, China, November 3–7, 2019. ©2019 Association for Computational Linguistics



<!-- page 0002 -->

| Body | Punchline | Score |
|---|---|---|
| Man, I was so tired last night; I had a dream I was a<br>muffler... | and I woke up ex-<br>hausted | 276 |
| I told my teenage niece to go get me a newspaper...<br>She laughed at me, and said, ”Oh uncle you’re so<br>old. Just use my phone.” | So I slammed her<br>phone against the<br>wall to kill a spider. | 28315 |

Table 1: Example format of the Reddit Jokes dataset

ing and creating datasets like the Pun of the Day (Yang et al., 2015), 16000 One-liners (Mihalcea and Strapparava, 2005), and even Ted Talks (Chen and Soo, 2018).

## 3 Data

We gathered jokes from a variety of sources, each covering a different type of humor. These datasets include jokes of multiple sentences (the Short Jokes dataset), jokes with only one sentence (the Puns dataset), and more mixed jokes (the Reddit dataset). We have made our code and datasets open source for others to use.[^2]

### 3.1 Reddit

Our Reddit data was gathered using Reddit’s public API, collecting the most recent jokes. Every time the scraper ran, it also updated the upvote score of the previously gathered jokes. This data collection occurred every hour through the months of March and April 2019. Since the data was already split into body and punchline sections from Reddit, we created separate datasets containing the body of the joke exclusively and the punchline of the joke exclusively. Additionally, we created a dataset that combined the body and punchline together.

Some sample jokes are shown in Table 1, above. The distribution of joke scores varies wildly, ranging from 0 to 136,354 upvotes. We found that there is a major jump between the 0-200 upvote range and the 200 range and onwards, with only 6% of jokes scoring between 200-20,000. We used this natural divide as the cutoff to decide what qualified as a funny joke, giving us 13884 not-funny jokes and 2025 funny jokes.

### 3.2 Short Jokes

The Short Jokes dataset, found on Kaggle, contains 231,657 short jokes scraped from various joke websites with lengths ranging from 10 to 200 characters. The previous work by Chen and Soo (2018) combined this dataset with the WMT16 English news crawl. Although their exact combined dataset is not publicly available, we used the same method and news crawl source to create a similar dataset. We built this new Short Jokes dataset by extracting sentences from the WMT16 news crawl that had the same distribution of words and characters as the jokes in the Short Jokes dataset on Kaggle[^3]. This was in order to match the two halves (jokes and non-jokes) as closely as possible.

### 3.3 Pun of the Day

This dataset was scraped by Yang et al. (2015) and contains 16001 puns and 16002 not-punny sentences. We gratefully acknowledge their help in putting together and giving us use of this dataset. These puns were constructed from the Pun of the Day website while the negative samples were gathered from news websites.

## 4 Methods

In this section we will discuss the methods and model used in our experiments.

### 4.1 Our Model

We have chosen to use the pre-trained BERT (Devlin et al., 2018) as the base of our model. BERT is a multi-layer bidirectional Transformer encoder and was initially trained on a 3.3 billion word corpus. The model can be fined-tuned with another additional output layer for a multitude of other tasks. We chose to use this Transformer based model as our initial platform because of its success at recognizing and attending to the most important words in both sentence and paragraph structures.

In Figure 1, originally designed by Vaswani et al. (2017), we see the architecture of a Transformer model: the initial input goes up through an encoder, which has two parts: a multi-headed

[^2]: Our code and datasets are publicly available at this link.

[^3]: The Short Jokes dataset from Kaggle is available here.



<!-- page 0003 -->

[Figure: Transformer model architecture diagram with encoder and decoder stacks. Readable labels include Output Probabilities, Softmax, Linear, Add & Norm, Feed Forward, Multi-Head Attention, Masked Multi-Head Attention, Positional Encoding, Input Embedding, Output Embedding, Inputs, Outputs (shifted right), and N×.]

Figure 1: Transformer Model Architecture

self attention layer, followed by a feed-forward network. It then outputs the information into the decoder, which includes the previously mentioned layers, plus an additional masked attention step. Afterwards, it is transformed through a softmax into the output. This model’s success is in large part due to the Transformer’s self-attention layers.

We chose a learning rate of 2e-05 and a max sequence length of 128. We trained the model for a maximum of 7 epochs, creating checkpoints along the way.

## 4.2 Training

Since our data was unbalanced we decided to upsample the humorous jokes in training. We split the dataset into a 75/25 percent split, stratifying with the labels. We then upsampled the minority class in the training set until it reached an even 50 percent. This helped our model learn in a more balanced way despite the uneven amount of non-humorous jokes. Our validation and test sets were composed of the remaining 25%, downsampling the data into a 50/50 class split so that the accuracy metric could be balanced and easily understood.

To show how our model compares to the previous work done, we also test on the Short Joke and Pun datasets mentioned in the Data section. For these datasets we will use the metrics (Accuracy, Precision, Recall, and F1 Score) designated in Chen and Soo (2018) as a comparison. We use

| Method | Body | Punchline | Full |
|---|---:|---:|---:|
| CNN | 0.651 | 0.684 | 0.688 |
| Transformer | **0.661** | **0.692** | **0.724** |
| Human (General) | 0.493 | 0.592 | 0.663 |

Table 2: Results of Accuracy on Reddit Jokes dataset

the same model format as previously mentioned, trained on the Reddit dataset. We then immediately apply the model to predict on the Short Joke and Puns dataset, without further fine-tuning, in order to compare the model. However, because both the Puns and Short Joke datasets have large and balanced labels, we do so without the upsampling and downsampling steps used for the Reddit dataset.

# 5 Experiments

In this section we will introduce the baselines and models used in our experiments.

## 5.1 Baselines

In order to have fair baselines, we used the following two models: a CNN with Highway Layers as described by Chen and Soo (2018) and developed by Srivastava et al. (2015), and human performance from a study on Amazon’s Mechanical Turk. We wanted to have the general population rate these same jokes, thus showing the difference between a general audience and a specific subset of the population, in particular, Reddit r/Jokes users. Since the Reddit users obviously found these jokes humorous, this experiment would show whether or not a more general population agreed with those labels.

We had 199 unique participants rate an average of 30 jokes each with the prompt *”do you find this joke humorous?”* If the participant was evaluating a sample from a body or punchline only dataset we prefaced our question with a sentence explaining that context, for example: *”Below is the punchline of a joke. Based on this punchline, do you think you would find this joke humorous?”* Taking these labels, we used the most frequently chosen tag from a majority vote to calculate the percentages found in the *Human* section of Table 2.

## 5.2 Results

In Table 2, we see the results of our experiment with the Reddit dataset. We ran our models on



<!-- page 0004 -->

| Previous Work: | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Word2Vec+HCF | 0.797 | 0.776 | 0.836 | 0.705 |
| CNN | 0.867 | 0.880 | 0.859 | 0.869 |
| CNN+F | 0.892 | 0.886 | 0.907 | 0.896 |
| CNN+HN | 0.892 | 0.889 | 0.903 | 0.896 |
| CNN+F+HN | 0.894 | 0.866 | **0.940** | 0.901 |

| Our Methods: | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Transformer | **0.930** | **0.930** | 0.931 | **0.931** |

Table 3: Comparison of Methods on Pun of the Day Dataset. $HCF$ represents Human Centric Features, $F$ for increasing the number of filters, and $HN$ for the use of highway layers in the model. See (Chen and Soo, 2018; Yang et al., 2015) for more details regarding these acronyms.

the body of the joke exclusively, the punchline exclusively, and both parts together (labeled *full* in our table). On the full dataset we found that the Transformer achieved an accuracy of 72.4 percent on the hold out test set, while the CNN was in the high 60’s. We also note that the general human classification found 66.3% of the jokes to be humorous.

In order to understand what may be happening in the model, we used the body and punchline only datasets to see what part of the joke was most important for humor. We found that all of the models, including humans, relied more on the punchline of the joke in their predictions (Table 2). Thus, it seems that although both parts of the joke are needed for it to be humorous, the punchline carries higher weight than the body. We hypothesize that this is due to the variations found in the different joke bodies: some take paragraphs to set up the joke, while others are less than a sentence.

Our experiment with the Short Jokes dataset found the Transformer model’s accuracy and F1 score to be 0.986. This was a jump of 8 percent from the most recent work done with CNNs (Table 4).

| Method | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| CNN+F+HN | 0.906 | 0.902 | 0.946 | 0.924 |
| Transformer | **0.986** | 0.986 | 0.986 | 0.986 |

Table 4: Results on Short Jokes Identification

The results on the Pun of the Day dataset are shown in Table 3 above. It shows an accuracy of 93 percent, close to 4 percent greater accuracy than the best CNN model proposed. Although the CNN model used a variety of techniques to extract the best features from the dataset, we see that the self-attention layers found even greater success in pulling out the crucial features.

## 6 Discussion

Considering that a joke’s humor value is subjective, the results on the Reddit dataset are surprising. The model has used the context of the words to determine, with high probability, what an average Reddit r/Jokes viewer will find humorous. When we look at the general population’s opinion as well, we find a stark difference between their preferences and those of the Reddit users (Table 2). We would hypothesize that our model is learning the specific type of humor enjoyed by those who use the Reddit r/Jokes forum. This would suggest that humor can be learned for a specific subset of the population.

The model’s high accuracy and F1 scores on the Short Jokes and Pun of the Day dataset show the effectiveness of the model for transfer learning. This result is not terribly surprising. If the model can figure out which jokes are funny, it seems to be an easier task to tell when something isn’t a joke at all.

Although these results have high potential, defining the absolute truth value for a joke’s humor is a challenging, if not impossible task. However, these results indicate that, at least for a subset of the population, we can find and identify jokes that will be most humorous to them.

## 7 Conclusion

In this paper, we showed a method to define the measure of a joke’s humor. We explored the idea of using machine learning tools, specifically a Transformer neural network architecture, to discern what jokes are funny and what jokes are not. This proposed model does not require any human



<!-- page 0005 -->

interaction to determine, aside from the text of the joke itself, which jokes are humorous. This architecture can predict the level of humor for a specific audience to a higher degree than a general audience consensus. We also showed that this model has increased capability in joke identification as a result, with higher accuracy and F1 scores than previous work on this topic.

## References

Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural Machine Translation by Jointly Learning to Align and Translate. *International Conference on Learning Representations*.

Hareesh Bahuleyan. 2018. Natural Language Generation with Neural Variational Models. *arXiv e-prints*, page arXiv:1808.09012.

Peng-Yu Chen and Von-Wun Soo. 2018. Humor recognition using deep learning. *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*.

Jakob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *North American Chapter of the Association for Computational Linguistics*.

He He, Nanyun Peng, and Percy Liang. 2019. Pun generation with surprise. In *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, pages 1734–1744, Minneapolis, Minnesota. Association for Computational Linguistics.

Yann LeCun, Leon Bottou, Y Bengio, and Patrick Haffner. 1998. Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86:2278 – 2324.

Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. 2018. Generating Wikipedia by Summarizing Long Sequences. *International Conference on Learning Representations*.

Minh-Thang Luong, Hieu Pham, and Christopher D. Manning. 2015. Effective Approaches to Attention-based Neural Machine Translation. *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*, pages pages 1412 – 1421.

Rada Mihalcea and Carlo Strapparava. 2005. Making computers laugh: Investigations in automatic humor recognition. In *Proceedings of the Conference on Human Language Technology and Empirical Methods in Natural Language Processing*, HLT ’05, pages 531–538, Stroudsburg, PA, USA. Association for Computational Linguistics.

Amruta Purandare and Diane Litman. 2006. Humor: Prosody analysis and automatic recognition for f\*r\*j\*e\*n\*d\*s\*. *Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing*, pages 208–215.

Yishay Raz. 2012. Automatic humor classification on twitter. *Proceedings of the 2012 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Student Research Workshop*, pages 66–70.

Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber. 2015. Highway Networks. *arXiv e-prints*, page arXiv:1505.00387.

Julia M. Taylor and Lawrence J. Mazlack. 2004. Computationally recognizing wordplay in jokes. In *Proceedings of CogSci 2004*.

Alessandro Valitutti, Hannu Toivonen, Antoine Doucet, and Jukka M Toivanen. 2013. let everything turn well in your wife: Generation of adult humor using lexical constraints. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*, volume 2, pages 243–248.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All You Need. *31st Conference on Neural Information Processing Systems*, pages 17–21.

Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhutdinov, Richard Zemel, and Yoshua Bengio. 2015. Show, Attend and Tell: Neural Image Caption Generation with Visual Attention. *arXiv e-prints*, page arXiv:1502.03044.

Diyi Yang, Alon Lavie, Chris Dyer, and Eduard Hovy. 2015. Humor recognition and humor anchor extraction. *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*, pages 2367–2376.

Zichao Yang, Diyi Yang, Chris Dyer, Xiaodong He, Alexander J. Smola, and Eduard H. Hovy. 2016. Hierarchical attention networks for document classification. *HLT-NAACL*.

Renxian Zhang and Naishi Liu. 2014. Recognizing humor on twitter. In *Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management*, CIKM ’14, pages 889–898, New York, NY, USA. ACM.
