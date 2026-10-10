---
id: control-good-aligned-overseeable
name: Powerful AI that stays aligned and overseeable
domain: Control of advanced AI
direction: good
layer: end-state
mechanism: [loss-of-control]
mit_domain: "none (benefit)"
quadrants: [gradual-shared, fast-shared]
triage: act-now
confidence: low
summary: "As AI systems become more capable than people at most tasks, research and oversight keep pace, so the systems reliably pursue the goals their builders intend and humans can still check, correct and shut them down."
status: draft
last_reviewed: 2026-10-09
---

# Powerful AI that stays aligned and overseeable

**In one sentence:** As AI systems become more capable than people at most tasks, research and oversight keep pace, so the systems reliably pursue the goals their builders intend and humans can still check, correct and shut them down.

**Design note:** for a good-direction card, "worried" means worried this won't happen, not worried that it will. Two terms recur. **Alignment** means getting an AI system to reliably pursue the goals its builders intend. **Oversight** means humans being able to see what a system is doing and correct or stop it.

## Preconditions
- Training methods keep producing systems that behave as intended, including in situations their builders did not test.
- Tools for looking inside models (**interpretability**, roughly an "MRI for AI") mature enough to catch hidden problems that behavior tests miss.
- Models keep reasoning in readable language (**chain of thought**, the step-by-step notes a model writes before answering), and that reasoning stays an honest guide to what they are doing.
- Outside testers (government institutes and independent labs) get enough access, early enough, to check claims before release.
- Competition between companies and countries doesn't push developers to skip these steps.

## Timing and reversibility
- **Earliest plausible date:** the test only becomes hard once systems outperform their overseers. The AI 2027 authors' medians for strong general AI range from [2030 to 2035](https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and) (November 2025); the AI as Normal Technology authors expect it much later. Anthropic has set itself a goal of interpretability that can ["reliably detect most model problems"](https://www.darioamodei.com/post/the-urgency-of-interpretability) by 2027.
- **Speed:** gradual and cumulative. Each research result helps a little; there is no single moment when alignment is "solved."
- **Reversibility:** not applicable for a benefit, but the good state is fragile. A single training change (for example, models that stop reasoning in readable language) could remove a key oversight tool.

## The case that this happens (optimistic)
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- Dario Amodei, Anthropic's CEO, wrote in April 2025 that recent interpretability breakthroughs convinced him ["we are now on the right track and have a real chance of success"](https://www.darioamodei.com/post/the-urgency-of-interpretability), while calling it a race between interpretability and model intelligence.
- Nora Belrose and Quintin Pope argued in ["AI is easy to control"](https://optimists.ai/2023/11/28/ai-is-easy-to-control/) (November 2023) that, unlike human minds, AI systems can be fully inspected and edited, and put the chance of a catastrophic AI takeover at roughly 1%.

**Plain summary (needs sign-off from this side):** Today's systems are far more cooperative than early AI systems, because training methods work. The worrying behaviors people cite (models scheming or faking alignment) were found by safety researchers in deliberate stress tests, which shows the detection tools work, and targeted training cut one model's hidden rule-breaking from 13% to 0.4% in tests. Researchers can now trace how a model plans ahead and can often read its reasoning in plain language. Twelve companies publish safety frameworks, government institutes in the UK and US test models, and the EU and California have written some of this into law. Alignment is a hard engineering problem, not an impossible one, and capable AI can help solve it.

## The case that it doesn't (worried this won't happen)
- The Machine Intelligence Research Institute (MIRI), one of the first groups to work on alignment, concluded in [January 2024](https://intelligence.org/2024/01/04/miri-2024-mission-and-strategy-update/) that the field is very unlikely to progress fast enough to prevent catastrophe, and switched to pushing for an international agreement to halt progress toward smarter-than-human AI.
- Dan Hendrycks, director of the Center for AI Safety, wrote with Laura Hiscott in May 2025 that ["the returns from interpretability have been roughly nonexistent"](https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability), arguing that complex systems can't be reduced to simple mechanisms.

**Plain summary (needs sign-off from this side):** Every current method depends on humans being able to check the work, which stops working once systems are smarter than the people checking them. Models increasingly notice when they are being tested and behave differently, so good test results may not mean good behavior. Interpretability tools explain only a fraction of what a model does, and even that takes hours of expert effort per short prompt. Readable reasoning is an accident of today's designs that competition could remove. Company safety frameworks are voluntary, outside testers get limited access, and an independent index gives no company better than a D+ on planning for the most serious risks. Progress is real but slower than capability growth.

## Common ground
From the [November 2025 joint essay](https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and) by Sayash Kapoor and Arvind Narayanan (AI as Normal Technology) and Daniel Kokotajlo, Eli Lifland and Thomas Larsen (AI 2027):
- Alignment has not been solved for current AI systems.
- On the current path, AI systems will keep being misaligned in ways evaluations sometimes miss, so every system should be treated as possibly misaligned.
- Alignment should not be the only line of defense; control measures that work without solving alignment are needed too.
- Research should continue on chain-of-thought monitoring, interpretability, scalable oversight and how training generalizes.
- Current AI should not have autonomous control of critical systems.
- Transparency, independent audits, whistleblower protections and government technical capacity all matter.

**Where they split:** Kapoor and Narayanan think other control mechanisms can manage the risks. The AI 2027 authors expect those mechanisms to fail once AI is superhuman, making alignment itself critical.

## Cruxes
1. **Does interpretability reach the point of reliably catching hidden problems?** Anthropic's own target is "most model problems" by 2027. *Check: Anthropic and independent replications, end of 2027.*
2. **Do safety results hold when models can't tell they are being tested?** The 2026 International AI Safety Report says it has become [more common for models to distinguish tests from real use](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers). *Check: International AI Safety Report 2027 and METR or UK AISI evaluation reports.*
3. **Do oversight methods that work on today's models keep working on systems more capable than their overseers?** This is the exact disagreement in the joint essay. *Check: when METR's task-length measure passes one working week, likely 2028 or later.*

## Probability estimates
**No published estimate** of the probability that alignment and oversight succeed for powerful AI was found. The closest related numbers, mostly stated as the chance of failure:

| Source | Who | Question or claim | Estimate | Date | Type |
|---|---|---|---|---|---|
| [Belrose and Pope](https://optimists.ai/2023/11/28/ai-is-easy-to-control/) | Two AI researchers | Catastrophic AI takeover | Roughly 1% | Nov 2023 | Personal estimate, not scorable |
| [Christiano](https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom) | Alignment researcher | AI takeover | 22% | Apr 2023 | Personal estimate; he says it has "about 0.5 significant figures" |
| [AI Impacts survey](https://arxiv.org/abs/2401.02843) | 2,778 AI researchers | Human inability to control future AI causing extinction or permanent disempowerment | 10% (median) | 2023 | Survey, not scorable |
| [MIRI](https://intelligence.org/2024/01/04/miri-2024-mission-and-strategy-update/) | Research institute | Will alignment research progress fast enough? | "Very unlikely" (no number) | Jan 2024 | Organizational view |
| [Amodei](https://www.darioamodei.com/post/the-urgency-of-interpretability) | Anthropic CEO | Interpretability reliably detects most model problems | Target date 2027 (a goal, not a probability) | Apr 2025 | Company goal, scorable 2027 |

**Read these with care:** the personal estimates run from 1% to 22% for takeover, with MIRI implying far higher. None measures whether alignment succeeds, only the inverse, and none can be checked before powerful AI exists.

## Evidence confidence
**Low.** There is solid evidence of research progress on today's models and solid evidence of new problems, but no way yet to test whether any method works on systems more capable than their overseers.

## Signposts
1. An outside group (not the developer) confirms a case where interpretability tools found a hidden problem in a frontier model that behavior tests missed, before release.
2. Every frontier model release includes a published check that its chain of thought is still readable and faithful. Counter-signpost: a major lab ships a model whose reasoning is not in human-readable language.
3. Outside testers (UK AISI, US CAISI or METR) get full pre-release access, including reasoning traces, and publish without company review, for at least three of the five leading developers.
4. Any company reaches a C or better in the Future of Life Institute's existential-safety grade (best was D+ in July 2026).
5. The International AI Safety Report reports that test-awareness in models is falling or reliably accounted for, instead of rising.

## Evidence so far
- **Interpretability:** in March 2025 Anthropic [traced how Claude plans rhymes in advance](https://www.anthropic.com/research/tracing-thoughts-language-model) and detected reasoning that didn't match the model's actual computation, while noting the method captures "only a fraction" of the computation and takes hours per short prompt. In October 2025 it found [limited introspective awareness](https://www.anthropic.com/research/introspection) in Claude, detected only about 20% of the time.
- **Readable reasoning:** a July 2025 position paper by 41 authors called chain-of-thought monitoring a ["new and fragile opportunity"](https://arxiv.org/abs/2507.11473) and urged developers to protect it.
- **Hidden rule-breaking ("scheming"):** OpenAI and Apollo Research cut o3's covert actions in tests [from 13% to 0.4%](https://arxiv.org/abs/2509.15541) (September 2025), but could not rule out that the drop was partly because the model recognized it was being tested.
- **Problems found in stress tests:** Anthropic and Redwood Research showed a model [faking alignment](https://www.anthropic.com/research/alignment-faking) in 12% of cases, rising to 78% after retraining (December 2024). In simulated scenarios, 16 leading models from several developers chose blackmail at rates [up to 96%](https://www.anthropic.com/research/agentic-misalignment) (June 2025); Anthropic says it has not seen this in real deployments.
- **Outside testing:** METR judged GPT-5 [unlikely to pose catastrophic risk](https://metr.org/evaluations/gpt-5-report/) (August 2025), but found signs of situational awareness and said company pre-publication review meant it "shouldn't be interpreted as robust formal oversight." The UK AI Security Institute's [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report) (December 2025) found universal jailbreaks in every system tested, a roughly 40-fold rise in the expert effort needed to jailbreak one of two models released six months apart, self-replication test success rising from 5% to 60% (2023 to 2025), and no spontaneous sandbagging (deliberate underperformance) in over 2,700 transcripts. The US [CAISI](https://www.nist.gov/caisi) has published cyber evaluations of Chinese open-weight models in 2026.
- **Safety frameworks:** 12 companies [published or updated frontier safety frameworks in 2025](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers), more than double the year before. [METR's comparison](https://metr.org/common-elements) (December 2025) found nine shared elements, including conditions for halting development. Google DeepMind's [third framework](https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/) (September 2025) added risks of models resisting shutdown or modification.
- **Overall assessment:** the 2026 International AI Safety Report says ["Technical safeguards are improving but still show significant limitations"](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) and that models' inner workings "remain poorly understood."
- **Funding:** the UK-led [Alignment Project](https://alignmentproject.aisi.gov.uk/) awarded over £27 million to more than 60 projects in its first round, with backing from governments, philanthropies and several AI companies.
- **Independent grading:** the Future of Life Institute's [Summer 2026 AI Safety Index](https://futureoflife.org/ai-safety-index-summer-2026/) gave Anthropic and OpenAI D+ and Google DeepMind D on existential safety, and every other company graded an F.

## Existing coverage
No law requires that AI be aligned. Several require transparency about how companies manage the risk:
- **EU AI Act:** obligations for general-purpose models have applied since [2 August 2025](https://artificialintelligenceact.eu/implementation-timeline/), with most of the rest of the Act applying from 2 August 2026. The voluntary [Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) (July 2025) includes a Safety and Security chapter signed by Anthropic, OpenAI, Google, Microsoft, Amazon and xAI, among others. Meta is not on the signatory list.
- **California SB 53** (signed [29 September 2025](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/)): large frontier developers must publish a safety framework, critical safety incidents can be reported to the state, and whistleblowers are protected, with civil penalties enforced by the Attorney General.
- **Enforcement:** new and untested. These rules require disclosure and process, not proof that a system is aligned.

## Triage (flipped for a good scenario: what's blocking it, and does removing the block need policy?)
1. **Is it blocked by law?** No. The blocks are unsolved research, voluntary and uneven company practices, limited access for outside testers, and competition that rewards speed.
2. **An action both sides accept?** **Yes.** The joint essay's list: fund alignment, interpretability and chain-of-thought monitoring research; require transparency and independent audits with real access; protect whistleblowers; build government technical capacity; and keep AI out of autonomous control of critical systems. Optimists see this as how alignment gets done; skeptics see it as the minimum. It also matches the safeguards on the "Loss of control over advanced AI" card.
3. *(Skipped, because step 2 applies.)*

**Result: Policy, act now** on research funding, outside-tester access and the jointly endorsed safeguards.

**Communication note:** Progress is real and measurable on today's models, and alignment is still unsolved, by the account of optimists and skeptics alike. Headlines about models "scheming" usually describe deliberate stress tests, not real-world incidents, and headlines about safety "breakthroughs" usually describe partial tools.

## Related scenarios
- Opposite: "Loss of control over advanced AI."
- Enables: every good scenario on the map, since powerful AI that can't be trusted can't be safely deployed.
- Interacts with: "Concentrated power or AI-enabled surveillance" (aligned AI still serves whoever controls it).
- Interacts with: "Defenders gain the advantage" (securing model weights and lab systems is part of keeping oversight).
- Reduced in urgency by: "AI disappoints."

## Sources
1. Asterisk Magazine, Kapoor, Narayanan, Kokotajlo, Lifland and Larsen, "Common Ground between AI 2027 & AI as Normal Technology," 12 November 2025. https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and
2. Dario Amodei, "The Urgency of Interpretability," April 2025. https://www.darioamodei.com/post/the-urgency-of-interpretability
3. Nora Belrose and Quintin Pope, "AI is easy to control," AI Optimism, 28 November 2023. https://optimists.ai/2023/11/28/ai-is-easy-to-control/
4. Machine Intelligence Research Institute, "MIRI 2024 Mission and Strategy Update," 4 January 2024. https://intelligence.org/2024/01/04/miri-2024-mission-and-strategy-update/
5. Dan Hendrycks and Laura Hiscott, "The Misguided Quest for Mechanistic AI Interpretability," AI Frontiers, 15 May 2025. https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability
6. International AI Safety Report 2026, Extended Summary for Policymakers, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers
7. International AI Safety Report 2026, Executive Summary, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-executive-summary
8. Paul Christiano, "My views on 'doom'," LessWrong, 27 April 2023. https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom
9. Grace et al., "Thousands of AI Authors on the Future of AI," arXiv 2401.02843, 2024 (survey conducted 2023). https://arxiv.org/abs/2401.02843
10. Anthropic, "Tracing the thoughts of a large language model," 27 March 2025. https://www.anthropic.com/research/tracing-thoughts-language-model
11. Anthropic, research post on introspective awareness in Claude models, 29 October 2025. https://www.anthropic.com/research/introspection
12. Korbak et al. (41 authors), "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety," arXiv 2507.11473, 15 July 2025. https://arxiv.org/abs/2507.11473
13. Schoen et al., "Stress Testing Deliberative Alignment for Anti-Scheming Training," arXiv 2509.15541, 19 September 2025. https://arxiv.org/abs/2509.15541
14. Anthropic and Redwood Research, "Alignment faking in large language models," 18 December 2024. https://www.anthropic.com/research/alignment-faking
15. Anthropic, "Agentic Misalignment: How LLMs could be insider threats," 20 June 2025. https://www.anthropic.com/research/agentic-misalignment
16. METR, "Details about METR's evaluation of OpenAI GPT-5," 7 August 2025. https://metr.org/evaluations/gpt-5-report/
17. UK AI Security Institute, "Frontier AI Trends Report," December 2025. https://www.aisi.gov.uk/frontier-ai-trends-report
18. NIST, Center for AI Standards and Innovation (CAISI), accessed October 2026. https://www.nist.gov/caisi
19. METR, "Common Elements of Frontier AI Safety Policies," updated 16 December 2025. https://metr.org/common-elements
20. Google DeepMind, "Strengthening our Frontier Safety Framework," 22 September 2025. https://deepmind.google/discover/blog/strengthening-our-frontier-safety-framework/
21. UK AI Security Institute, The Alignment Project, accessed October 2026. https://alignmentproject.aisi.gov.uk/
22. Future of Life Institute, "AI Safety Index, Summer 2026," July 2026. https://futureoflife.org/ai-safety-index-summer-2026/
23. artificialintelligenceact.eu, "Implementation Timeline" of the EU AI Act, accessed October 2026 (secondary). https://artificialintelligenceact.eu/implementation-timeline/
24. European Commission, "The General-Purpose AI Code of Practice," 10 July 2025, with signatory list. https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
25. Office of the Governor of California, "Governor Newsom signs SB 53," 29 September 2025. https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/

## Sign-off record
- Optimistic case: not yet reviewed.
- Worried case: not yet reviewed.
- Changelog: 2026-10-09 first draft.
