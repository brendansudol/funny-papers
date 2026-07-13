# Eigentaste: A Constant Time Collaborative Filtering Algorithm

**Ken Goldberg, Theresa Roeder, Dhruv Gupta, Chris Perkins** — Information Retrieval 4(2):133-151 · Guide entry Part 4 (audience-modeling anchor) (Part 4 - Evaluation Methodology)

[paper page](https://eigentaste.berkeley.edu/about.html) · [local PDF](../pdfs/x23-eigentaste-jester.pdf) · [full markdown](../md/x23-eigentaste-jester/x23-eigentaste-jester.md) · [extract](../extracts/x23-eigentaste-jester.json)

## TL;DR
Eigentaste is a collaborative filtering algorithm for recommending jokes using a shared gauge set of ratings, PCA, offline clustering, and online lookup. On the Jester joke-rating data, it matched the best nearest-neighbor accuracy reported in the paper, NMAE 0.187, while reducing online recommendation time to 3.22 msec per user.

## Problem & Motivation
The paper asks whether an automated system can recommend funny jokes, a hard information-retrieval problem because humor criteria are difficult to formalize. Standard nearest-neighbor collaborative filtering methods compare a new user to the existing user database, so their online computation grows with the number of users. The authors want a recommender that remains accurate but serves recommendations in constant online time as the database grows.

## Approach
Eigentaste uses universal queries: every user rates the same gauge set of items during profiling. This creates a dense submatrix of ratings, unlike user-selected ratings matrices with many null values. Ratings are real-valued on a continuous bar over [-10,+10], then normalized by item mean and standard deviation. The algorithm computes the gauge-item correlation matrix, applies PCA, projects users into a low-dimensional eigenspace, and clusters them offline. For Jester, the paper uses the first two principal components and recursive rectangular clustering in the eigenplane. Each cluster stores a lookup table of non-gauge jokes sorted by cluster mean rating. Online, a new user rates the gauge jokes, is projected into the eigenplane, assigned to a cluster, and receives lookup-table recommendations.

## Data & Experimental Setup
The implementation is Jester, an online joke recommender. The initial 40 jokes came from friends and newsgroups, with an effort to avoid highly offensive jokes. Jester 1.0 used 20 gauge jokes and later 70 total jokes; Jester 2.0 used 10 gauge jokes and 100 total jokes. Since March 1999, Jester collected approximately 2,500,000 ratings from 57,000 users. The experiments use 18,000 random users from this sample, split into disjoint training and test sets. The dataset has 10 gauge jokes, 90 non-gauge jokes, and an average of 46 ratings per user. Accuracy is measured with Normalized Mean Absolute Error (NMAE), MAE divided by the full rating range.

## Results
POP, the global-mean baseline, obtained NMAE 0.203. 1-NN was worse, with NMAE 0.238 in the results text. q-NN improved as more neighbors were used, reaching the lowest NMAE of 0.187 at approximately 80 nearest neighbors; the paper describes this as about 8% better than POP. Eigentaste also achieved NMAE 0.187. In timing, scanning 8853 training users for 1-NN took 31.64 seconds, and finding the nearest neighbor plus predictions for one test user took 438 msec. Eigentaste’s offline work for 8853 training users took 29.59 seconds, including 444 msec for eigenvectors/eigenvalues and 298 msec for clusters and predictions. Its online projection and lookup took 3.22 msec per user.

## Takeaways
- A dense common gauge set can turn collaborative filtering into an offline modeling problem with fast online serving.
- On this joke-rating task, Eigentaste preserved the best reported NMAE of nearest-neighbor methods while being two orders of magnitude faster online.
- Single-neighbor recommendations were noisy and worse than the global mean baseline.
- For humor systems, the paper shows personalization can be based entirely on numerical ratings without modeling joke semantics.

## Limitations & Caveats
The authors note that universal queries may be less effective than user-selected queries depending on the domain. Gauge-set selection is left for future work. The continuous rating-bar interface is argued to have advantages, but the paper says more research is needed. Random-prediction analyses in the appendix give NMAE 0.333 for uniform ratings and 0.282 for a normal model, suggesting substantial room for better accuracy.
