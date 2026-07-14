# The Linguistic Analysis of Jokes

**Graeme Ritchie** — Routledge (book) · Guide entry T4 (Theory Foundations)

[Routledge book page (consulted)](https://www.routledge.com/The-Linguistic-Analysis-of-Jokes/Ritchie/p/book/9781138008731) · [extract](../extracts/t4-linguistic-analysis-of-jokes.json)

Restricted primary source consulted; full text not distributed.

## TL;DR
Ritchie’s book is a methodological and theoretical study of verbally expressed jokes, especially simple jokes, puns, forced reinterpretation jokes, and question–answer forms. Its central claim is that humour research needs precise descriptions of restricted joke classes before it can support a general theory; it also argues that influential theories such as SSTH and GTVH remain too vague in crucial places.

## Problem & Motivation
The book starts from the view that humour is scientifically important but poorly theorized. Rather than trying to explain all humour, it narrows the target to verbally expressed humour and mainly jokes. Ritchie distinguishes jokehood from funniness: deciding that a text is structured as a joke is treated as more basic and more manageable than explaining how funny it is to a particular person.

## Approach
The book advocates bottom-up linguistic analysis. It treats joke classes somewhat like grammar rules: a class definition should state internal mechanisms precisely enough that, in principle, a computer could test or generate cases. Major constructs include OBVIOUSNESS, CONFLICT, COMPATIBILITY, CONTRAST, INAPPROPRIATENESS, ABSURDITY, and TABOO. Appendix A formalizes supporting notions such as text strings, text-meaning mappings, situations, inference, interpretation sequences, punchline conflict, punchline resolution, delivery mechanisms, paradigmatic puns, and knock-knock jokes.

## Data & Experimental Setup
The book’s own evidence is mostly close analysis of examples. Appendix B contains 195 numbered examples, including jokes, puns, riddles, question–answer forms, narratives, headlines, signs, constructed variants, and non-joke contrasts. Sources include joke books, Internet joke pages collected between December 2001 and March 2002, academic articles, media performances, remembered jokes, and constructed items.

The book also surveys early computational humour systems: LIBJOG, a Tom Swifty generator, a simple riddle generator, JAPE, HCPP, WisCraic, and HAHAcronym. These are reviewed as examples of narrow, implementable structural accounts of humour. Reported evaluations include JAPE with 122 children aged eight to eleven, HCPP with 16 subjects, WisCraic with 15 subjects, and HAHAcronym with groups of 20 subjects.

## Results
The strongest empirical numbers come from reviewed systems, not new experiments by the author. In the JAPE study, each text item was rated by at least nine children, with most items getting twelve ratings; human-generated and JAPE-generated jokes were distinguished from non-jokes, while human jokes received higher jokehood and funniness ratings than JAPE jokes. HCPP used 36 common phrases and 240 words; three implemented schemata produced 34, 7 and 9 jokes, and evaluated output averaged 2.81 on a five-point scale, with a best item at 4.4. WisCraic’s reported evaluation found 84 per cent of outputs classed as jokes and 10 per cent as failed attempts. HAHAcronym’s reanalysis evaluation reported mean 59.61, standard deviation 8.91, versus a random-control mean 42.05, standard deviation 9.76.

For GTVH joke-similarity evidence, Ruch et al. used over 500 undergraduate psychology students. Ritchie argues that the strongest similarity pattern concerns general textual parameters, and that for SI/LM/SO only 4 of 9 predicted orderings hold while 5 do not.

## Takeaways
- Build humour systems around narrow, explicit joke-class mechanisms rather than vague global labels.
- Separate jokehood from funniness; a valid joke structure may still be weakly funny.
- Treat puns, forced reinterpretation, and question–answer jokes as different mechanisms, not one undifferentiated “incongruity.”
- Human evaluation needs controls, clear scales, and transparent item selection.
- Computational humour work is useful when it makes structural claims testable, even if coverage is very narrow.

## Limitations & Caveats
The book is not a complete humour theory. Many definitions are preliminary, and key notions such as INAPPROPRIATENESS, ABSURDITY, TABOO, CONTRAST, contextual suitability, and phonetic similarity remain partly primitive. The empirical basis is mostly authorial analysis of examples, and the reviewed computational evaluations vary greatly in quality.
