---
id: power-good-wider-access
name: Wider access and more accountable institutions
domain: Power and governance
direction: good
layer: pathway
mechanism: [systemic]
mit_domain: "none (benefit)"
quadrants: [gradual-shared, fast-shared]
triage: act-now
confidence: low
summary: "Capable AI becomes cheap and openly available enough that people, small organizations and poorer countries can use and adapt it themselves, and governments use it to listen to citizens and explain their decisions, spreading power rather than concentrating it."
status: draft
last_reviewed: 2026-10-09
---

# Wider access and more accountable institutions

**In one sentence:** Capable AI becomes cheap and openly available enough that people, small organizations and poorer countries can use and adapt it themselves, and governments use it to listen to citizens and explain their decisions, spreading power rather than concentrating it.

**Design note:** for a good-direction card, "worried" means worried this won't happen or is oversold, not worried that it will. A separate argument, that releasing powerful open models helps bad actors, belongs on the misuse cards ("AI-assisted biological or chemical attack," "Cheap large-scale cyberattacks and critical-system failures"). This card asks only whether wider access actually spreads power. "Open-weight" means a model whose trained parameters (weights) are published so anyone can download, run and modify it.

## Preconditions
- The cost of a given level of AI capability keeps falling, so last year's frontier runs on cheap hardware.
- Some developers keep releasing strong open-weight models under permissive licenses.
- People in poorer countries get internet access, devices and AI tools that work in their languages.
- Low-cost uses in schools, farms and public services are shown to work in real trials, then funded at scale.
- Governments commit to act on what AI-assisted public consultation finds, rather than treating it as optional.

## Timing and reversibility
- **Earliest plausible date:** already partly here. Open models matching the frontier of 6 to 12 months earlier run on a single consumer graphics card ([Epoch AI, August 2025](https://epoch.ai/data-insights/consumer-gpu-model-gap)).
- **Speed:** slow-building for institutions and poorer countries; fast for model access among people already online.
- **Reversibility:** partly reversible in the bad direction. Weights already released cannot be recalled, but a handful of firms decide whether future frontier-class models are released openly, and that can change with one company decision.

## The case that this happens (optimistic)
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- Mark Zuckerberg, Meta CEO, argued in July 2024 that open-source AI ensures "that power isn't concentrated in the hands of a small number of companies" ([Meta, July 2024](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)).
- Tessler and colleagues at Google DeepMind found that an AI mediator helped groups of UK participants find common ground, with its statements preferred to those of human mediators ([Science, October 2024](https://doi.org/10.1126/science.adq2852)).

**Plain summary (needs sign-off from this side):** The cost of AI at a fixed level of capability has fallen by orders of magnitude in two years. Free models from Meta, DeepSeek, Alibaba (Qwen) and Mistral come within months of the best closed systems, and anyone can run, inspect and adapt them, including governments with sensitive data they cannot send to an outside vendor ([White House, July 2025](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)). The early uses in poorer countries are striking: a six-week AI tutoring program in Nigeria produced nearly two years of typical learning. AI can also make it practical for governments to hear from thousands of citizens and summarize where they agree, as Taiwan's vTaiwan process did with Polis. Cheap intelligence is a leveler, like cheap printing or the mobile phone.

## The case that it doesn't (worried this is oversold)
- David Gray Widder, Meredith Whittaker and Sarah Myers West argue that claims about "open" AI, by "frequently eliding scrutiny of substantial industry concentration," hide who controls the computing, data and labor needed to build it ([Nature, November 2024](https://www.nature.com/articles/s41586-024-08141-1)).
- Taiwanese legislator Jason Hsu called vTaiwan "a tiger without teeth" because the government is not required to follow its outcomes ([MIT Technology Review, August 2018](https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/)).

**Plain summary (needs sign-off from this side):** Downloading a model is not the same as having power. Training frontier systems takes chips, data centers and money that only a few companies and two countries have, and "open" releases are a business choice those companies can reverse, as Meta has signaled. Usage of AI tracks national income closely, and 2.2 billion people are still offline. Pilot results, like the Nigeria trial, are promising but small and short. AI-assisted deliberation works in experiments, but governments stay free to ignore the results, which can turn consultation into a show of openness rather than a transfer of power. Access may be broad but shallow while control stays narrow.

## Common ground
- The price of a fixed level of AI capability has fallen very fast ([Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report); [Epoch AI, March 2025](https://epoch.ai/data-insights/llm-inference-price-trends)).
- Open-weight models trail the best closed models by months to about a year, not by many years ([Epoch AI, November 2024](https://epoch.ai/blog/open-models-report)).
- Building frontier models remains concentrated in a few firms and countries ([Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)).
- AI use is much lower in poorer countries ([Anthropic, September 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)).
- AI-assisted deliberation can work in controlled settings. Whether it changes decisions depends on institutions, not on the software.

## Cruxes
1. **Does the open-weight lag stay under about a year as frontier training costs keep rising?** If the best open models fall further behind, wide access means access to second-tier tools. *Check: Epoch AI open-model and consumer-GPU analyses, 2027.*
2. **Does the AI usage gap between rich and poor countries narrow?** *Check: Anthropic Economic Index geographic reports and ITU Facts and Figures, late 2027.*
3. **Do low-cost uses like the Nigeria tutoring program keep their effects when run at national scale and over a full school year?** *Check: World Bank follow-up evaluations, 2027 to 2028.*

## Probability estimates
**No published estimate** of the probability that AI spreads power and makes institutions more accountable was found. The closest numbers are measurements of access, not forecasts:

| Source | Who | Question or claim | Estimate | Date | Type |
|---|---|---|---|---|---|
| [Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) | Stanford HAI | Fall in inference cost for a model at GPT-3.5 level, Nov 2022 to Oct 2024 | Over 280-fold | 2025 | Measurement |
| [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends) | Epoch AI | Yearly fall in price at constant capability, across benchmarks | 9x to 900x a year (40x for GPT-4 level on PhD science questions) | Mar 2025 | Measurement, trend may not persist |
| [Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) | Stanford HAI | Performance gap between top open-weight and closed models on some benchmarks | Narrowed from 8% to 1.7% in a year | 2025 | Measurement |
| [Epoch AI](https://epoch.ai/blog/open-models-report) | Cottier, You, Martemianova, Owen | How far the best open models lag the best closed models | 5 to 22 months on benchmarks; about one year overall | Nov 2024 | Measurement |
| [Epoch AI](https://epoch.ai/data-insights/consumer-gpu-model-gap) | Epoch AI | How far models that run on one consumer GPU lag the frontier | 6 to 12 months | Aug 2025 | Measurement |
| [Anthropic Economic Index](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) | Anthropic | Claude use per working-age person vs. income per person, across countries | 1% higher income goes with 0.7% higher use | Sep 2025 | Measurement, one company's data |

## Evidence confidence
**Low.** Falling costs and the spread of open models are well measured. Evidence that access translates into wider power, better outcomes in poorer countries, or more accountable government rests on a few promising trials and case studies, mostly short and small.

## Signposts
1. Epoch AI's next measurement of the consumer-GPU lag stays at 12 months or less.
2. Two or more of the four main open-weight developers (Meta, DeepSeek, Alibaba's Qwen team, Mistral) release no new frontier-class open model for 12 months.
3. Anthropic's AI Usage Index for Nigeria and India rises above 0.5 (0.2 and 0.27 in September 2025).
4. The ITU's count of people offline falls below 2 billion (2.2 billion in 2025).
5. A national government or large city commits in advance, in law or regulation, to respond formally to the consensus findings of an AI-assisted public deliberation.

## Evidence so far
- **Falling costs:** inference cost at GPT-3.5 level fell over 280-fold between November 2022 and October 2024; hardware costs fell about 30% a year and energy efficiency improved about 40% a year ([Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)).
- **Spread of open models:** Meta reported Llama passed one billion downloads ([Meta, March 2025](https://about.fb.com/news/2025/03/celebrating-1-billion-downloads-llama/)). DeepSeek released R1 under the permissive MIT license, reporting performance comparable to OpenAI's o1 on math, code and reasoning (ahead on some benchmarks, behind on others), plus smaller versions from 1.5 billion to 70 billion parameters built on Qwen and Llama ([DeepSeek, January 2025](https://github.com/deepseek-ai/DeepSeek-R1); [Nature, September 2025](https://www.nature.com/articles/s41586-025-09422-z)). Mistral released Mistral 7B under the Apache 2.0 license in 2023 ([Mistral AI, September 2023](https://mistral.ai/news/announcing-mistral-7b)).
- **Signs of retreat:** in July 2025 Zuckerberg wrote that Meta will need to be "careful about what we choose to open source" ([Meta, July 2025](https://www.meta.com/superintelligence/)).
- **Concentration of the means to build AI:** US private AI investment was $285.9 billion in 2025, more than 23 times China's, and the US hosts 5,427 data centers, more than ten times any other country ([Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)). TSMC makes roughly 70 to 80% of leading-edge chip revenue, and academic research uses about 1% of the compute of the largest industry model ([AI Now Institute, September 2023](https://ainowinstitute.org/publications/compute-and-ai)).
- **Usage gap:** Anthropic's AI Usage Index (usage relative to working-age population) was 7 for Israel and 3.62 for the US, against 0.27 for India and 0.2 for Nigeria. Anthropic warns AI's benefits "may concentrate in already-rich regions" ([Anthropic, September 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)). About 2.2 billion people were offline in 2025, mostly in low- and middle-income countries ([ITU, November 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/)).
- **Education:** a World Bank randomized trial in Nigeria gave secondary students six weeks of AI-assisted English tutoring in mid-2024 and found gains of about 0.3 standard deviations, "nearly two years of typical learning," outperforming 80% of comparable interventions in a database of trials from developing countries ([World Bank, January 2025](https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria); [working paper](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)).
- **Agriculture:** Digital Green's Farmer.Chat assistant had answered over 300,000 questions from more than 15,000 farmers in four countries by late 2024. These are usage figures reported by the developers, not measured effects on harvests or income ([arXiv, September 2024](https://arxiv.org/abs/2409.08916)).
- **Deliberation:** in experiments with 5,734 UK participants, an AI mediator's group statements were preferred to those of human mediators and rated more informative, clear and unbiased; results replicated in a virtual citizens' assembly with a representative UK sample ([Tessler et al., Science, October 2024](https://doi.org/10.1126/science.adq2852)). The Collective Intelligence Project's first Global Dialogues pilot reached about 1,200 people in 68 countries ([CIP 2024 Annual Report](https://2024.cip.org/2024_Annual_Report_CIP.pdf)).
- **Government follow-through:** Taiwan's vTaiwan Polis consultation on Uber drew about 3,000 participants in 2015, and the government agreed in 2016 to ratify the consensus points ([Shareable, July 2016](https://www.shareable.net/open-data-hactivists-help-taipei-craft-regulatory-response-to-uber/)). By 2018 vTaiwan reported 26 cases, 80% leading to "decisive government action," but it was not binding, was used mostly for digital-economy issues, and one bill drafted through it was later withdrawn ([MIT Technology Review, August 2018](https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/)).

## Existing coverage
No law blocks wider access; current policy in the US and EU mostly favors open models. The EU AI Act exempts general-purpose models released under a free and open-source license, with public weights, from some documentation duties, but not from copyright and training-data summary duties, and not if the model poses systemic risk ([EU AI Act, Article 53](https://artificialintelligenceact.eu/article/53/)). The US AI Action Plan says the government "should create a supportive environment for open models" and recommends wider compute access for startups and academics through the National AI Research Resource pilot ([White House, July 2025](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)). No law found requires a government to respond to the results of AI-assisted public consultation.

## Triage
*(Flipped for a good scenario: what is blocking it, and does removing the block need policy?)*
1. **Is it blocked by law?** No. The blocks are concentration of chips, data centers and money; the choice by a few firms whether to keep releasing open weights; missing connectivity and devices; and institutions that are not bound to act on public input.
2. **An action both sides accept?** **Yes, a narrow one.** The two camps disagree on whether open weights spread power, and a third group disputes releasing powerful weights at all. But both the optimists and the skeptics on this card would accept rigorous, published evaluation before governments and donors scale AI in schools, farms and public services, as the Nigeria trial did: optimists because it proves the case and attracts funding, skeptics because it separates real gains from shallow access. Publicly funded compute access for researchers is already US policy and is broadly accepted, though critics would add competition measures that optimists may not.
3. *(Skipped.)*

**Result: Policy, act now** on evaluation before scale (randomized trials with published results for AI in public services and development programs). **Communicate** to correct the idea that free downloads alone mean shared power.

**Communication note:** The cost of using AI is collapsing and strong free models exist, which is real and new. Who builds the frontier, who is online, and whether governments act on what citizens say are separate questions, and on those the evidence is thin. Point people to the uses with trial evidence, like the Nigeria tutoring result, and be plain that most other claims are still pilots.

## Related scenarios
- Opposite in the same domain: "Concentrated power or AI-enabled surveillance."
- Combines with: "Personal tutors, care and freed time" (the tutoring evidence); "Better shared understanding and forecasting" (AI-assisted deliberation); "Broad productivity gains and cheaper goods" (falling costs).
- Tension with: "AI-assisted biological or chemical attack" and "Cheap large-scale cyberattacks and critical-system failures" (the same open access, misused).
- Reduced by: "AI disappoints."

## Sources
1. Epoch AI, data insight on the capability gap between models that run on a consumer GPU and frontier models, 15 August 2025. https://epoch.ai/data-insights/consumer-gpu-model-gap
2. Zuckerberg, M., "Open Source AI Is the Path Forward," Meta, 23 July 2024 (updated January 2025). https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/
3. Tessler, M. H. et al., "AI can help humans find common ground in democratic deliberation," Science 386(6719), 18 October 2024. https://doi.org/10.1126/science.adq2852
4. Widder, D. G., Whittaker, M. and West, S. M., "Why 'open' AI systems are actually closed, and why this matters," Nature, 27 November 2024. https://www.nature.com/articles/s41586-024-08141-1
5. Horton, C., "The simple but ingenious system Taiwan uses to crowdsource its laws," MIT Technology Review, 21 August 2018. https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/
6. Stanford HAI, The 2025 AI Index Report, 2025. https://hai.stanford.edu/ai-index/2025-ai-index-report
7. Epoch AI, data insight on LLM inference price trends, 12 March 2025. https://epoch.ai/data-insights/llm-inference-price-trends
8. Cottier, B., You, J., Martemianova, N. and Owen, D., report on open-weight versus closed models, Epoch AI, 4 November 2024. https://epoch.ai/blog/open-models-report
9. Stanford HAI, The 2026 AI Index Report, 2026. https://hai.stanford.edu/ai-index/2026-ai-index-report
10. Anthropic, Anthropic Economic Index report, September 2025, 15 September 2025. https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
11. Meta Newsroom, announcement of one billion Llama downloads, 18 March 2025 (updated December 2025). https://about.fb.com/news/2025/03/celebrating-1-billion-downloads-llama/
12. DeepSeek, DeepSeek-R1 model repository and technical summary, January 2025. https://github.com/deepseek-ai/DeepSeek-R1
13. Guo, D. et al., "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning," Nature, 17 September 2025. https://www.nature.com/articles/s41586-025-09422-z
14. Mistral AI, "Mistral 7B," 27 September 2023. https://mistral.ai/news/announcing-mistral-7b
15. Zuckerberg, M., letter on personal superintelligence, Meta, 30 July 2025. https://www.meta.com/superintelligence/
16. Vipra, J. and West, S. M., "Computational Power and AI," AI Now Institute, 27 September 2023. https://ainowinstitute.org/publications/compute-and-ai
17. International Telecommunication Union, "Facts and Figures 2025," November 2025. https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/
18. De Simone, M. E., Tiberti, F., Mosuro, W., Manolio, F., Barron, M. and Dikoru, E., "From chalkboards to chatbots: Transforming learning in Nigeria," World Bank Blogs, 9 January 2025. https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria
19. World Bank, "From Chalkboards to Chatbots: Evaluating the Impact of Generative AI on Learning Outcomes in Nigeria," policy research working paper, 2025. https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324
20. Singh, N. et al. (Digital Green), "Farmer.Chat: Scaling AI-Powered Agricultural Services for Smallholder Farmers," arXiv 2409.08916, September 2024. https://arxiv.org/abs/2409.08916
21. Collective Intelligence Project, 2024 Annual Report. https://2024.cip.org/2024_Annual_Report_CIP.pdf
22. Bergren, A., article on vTaiwan and the regulatory response to Uber, Shareable, 6 July 2016. https://www.shareable.net/open-data-hactivists-help-taipei-craft-regulatory-response-to-uber/
23. EU Artificial Intelligence Act, Article 53, "Obligations for Providers of General-Purpose AI Models" (unofficial consolidated text). https://artificialintelligenceact.eu/article/53/
24. The White House, "America's AI Action Plan," July 2025. https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf

## Sign-off record
- Optimistic case: not yet reviewed.
- Worried case: not yet reviewed.
- Changelog: 2026-10-09 first draft.
