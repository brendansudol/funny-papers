# The Iron(ic) Melting Pot: Reviewing Human Evaluation in Humour, Irony and Sarcasm Generation

**Tyler Loakman, Aaron Maladry, Chenghua Lin** — Findings of EMNLP 2023 · Guide entry Part 4 (human-evaluation review) (Part 4 - Evaluation Methodology & Whether LLMs Are Actually Funny)

[paper page](https://aclanthology.org/2023.findings-emnlp.444/) · [local PDF](../pdfs/x36-ironic-melting-pot.pdf) · [full markdown](../md/x36-ironic-melting-pot/x36-ironic-melting-pot.md) · [extract](../extracts/x36-ironic-melting-pot.json)

## TL;DR
This position/survey paper argues that human evaluation of humour, irony, and sarcasm generation needs much more transparent reporting because judgments depend strongly on evaluator demographics and background knowledge. In a critical survey of 17 recent generation papers with human evaluation, only 7 of 17 reported any demographic information, and none reported evaluator age, gender, or social class.

## Problem & Motivation
Human evaluation is widely treated as the gold standard for Natural Language Generation, especially where automatic metrics correlate poorly with human judgments. The paper argues that this is not enough for subjective language forms such as humour, irony, and sarcasm. These forms often require shared cultural, political, religious, gendered, or contextual knowledge, so different evaluator panels may legitimately judge the same output differently. The authors therefore focus on whether recent NLG papers report enough about evaluator panels and procedures to make their results transparent and replicable.

## Approach
The paper first explains why humour, irony, and sarcasm are particularly sensitive to evaluator variables. It discusses humour through incongruity and examples involving political and gendered knowledge; irony through violations of factual, social, or contextual expectations; and sarcasm as aggressive or ridiculing verbal irony. It then conducts a critical survey of ACL Anthology papers from *ACL, EMNLP, COLING, LREC, INLG, and CoNLL between 2018 and 2023. Papers were found by matching title stems: “hum-”, “sarc-”, “iron-”, “fun-”, “jok-”, and “pun-”.

## Data & Experimental Setup
The initial search yielded 259 papers. After excluding shared-task submissions, 135 remained: 22 generation papers, 108 detection papers, and 5 “other” papers. The authors then excluded 4 generation papers that were surveys or dataset papers where human evaluation was performed on non-computationally generated examples. They report a final set of 18 generation papers, all but 1 of which contained human evaluation, leaving 17 papers for the reporting-transparency analysis.

The survey checks whether papers report evaluator demographics, including language proficiency, location/nationality, age, gender, education, and social class. It also checks reporting of recruitment, compensation, inter-annotator agreement, and training materials.

## Results
Reporting was sparse. Only 7 of 17 papers reported any evaluator demographic information (<42%). Language proficiency and location/nationality were each reported by 4 papers (<24%). Education was reported by 1 paper (<6%). Age, gender, and social class were reported by 0 papers (0%).

For evaluation logistics, 12 of 17 papers reported recruitment (<71%), 5 reported compensation (<30%), 9 reported IAA (<53%), and 4 reported training materials (<24%). All 12 papers that reported recruitment used crowdsourcing platforms: 9 used Amazon Mechanical Turk, 2 used Prolific Academic, and 1 did not name the platform. Among papers reporting compensation, pay ranged from approximately 9.23 USD to 20 USD per hour.

## Takeaways
- Human evaluation of humour systems should report who the evaluators are, not just aggregate scores.
- Demographics are not necessarily noise; disagreement can reveal perspectivist differences in humour, irony, and sarcasm perception.
- Crowdsourcing is common in this area, so papers should report recruitment filters, compensation, training, and agreement.
- The authors recommend an “evaluation statement” covering logistics, demographics, definitions, training materials, and agreement studies.
- Builders of humour systems should avoid treating one uncharacterized evaluator pool as a universal gold standard.

## Limitations & Caveats
The survey is limited to 2018–2023 and to selected ACL Anthology venues, yielding a small set of generation papers. It focuses on generation rather than detection or dataset annotation, though the authors argue the same concerns apply there too. The paper provides aggregate counts but not a full per-paper coding table or coding-agreement procedure for the survey itself.
