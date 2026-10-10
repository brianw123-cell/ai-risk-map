---
id: health-bad-bio-chem-attack
name: AI-assisted biological or chemical attack
domain: Health and biology
direction: bad
layer: end-state
mechanism: [misuse]
mit_domain: "4.2 Cyberattacks, weapon development or use, and mass harm"
quadrants: [gradual-shared, fast-shared]
triage: enforcement-problem
confidence: low
summary: "Someone who wants to cause mass casualties uses AI to close the gap between wanting to build a biological or chemical weapon and being able to, and carries out an attack that kills far more people than they could have reached without it."
status: draft
last_reviewed: 2026-10-09
---

# AI-assisted biological or chemical attack

**In one sentence:** Someone who wants to cause mass casualties uses AI to close the gap between wanting to build a biological or chemical weapon and being able to, and carries out an attack that kills far more people than they could have reached without it.

**Design note:** the two sides here are not "this would be bad" versus "this would be fine." Everyone agrees it would be catastrophic. They disagree about whether AI meaningfully changes who can do it. The word for the thing being argued about is **uplift**: the extra help an AI gives someone compared with what they could already get from a search engine, a textbook and a library. The question is never whether AI can describe a dangerous process, because so can a textbook.

## Preconditions
- An AI system gives real uplift on the steps that are actually hard, not just on the steps that are already in textbooks.
- The person gets past the physical stages too: obtaining genetic material or chemical precursors, doing the laboratory work, producing enough of the agent, and dispersing it.
- Safeguards fail or are routed around, through jailbreaks, pretexting, models released without safeguards, or an insider.
- Someone wants to do it. Mass-casualty intent is rare, and this precondition is doing more work in the overall probability than any capability question.

## Timing and reversibility
- **Earliest plausible date:** the capability side of this is partly here already. OpenAI said it was treating its [ChatGPT agent](https://openai.com/index/chatgpt-agent-system-card/) as "High" capability in biology and chemistry under its Preparedness Framework in July 2025, and Anthropic activated its [ASL-3 safeguards](https://www.anthropic.com/news/activating-asl3-protections) in May 2025. Both companies said they were acting as a precaution and had not established that the threshold was crossed.
- **Speed:** an attack is an event, not a trend. There is no ramp to watch, which is what makes this scenario different from most others on the map.
- **Reversibility:** a chemical attack is terrible but bounded in place and time. A transmissible biological agent is the tail that cannot be recalled, which is why this scenario gets attention disproportionate to its estimated probability.

## The case that this happens
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- Jassi Pannu, a physician and senior scholar at the Johns Hopkins Center for Health Security, told a House subcommittee in [December 2025](https://www.congress.gov/119/meeting/house/118773/witnesses/HHRG-119-IF02-Wstate-PannuJ-20251217.pdf) that "AI uplift increases the number of users capable of carrying out a bioweapons attack."
- The [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary), chaired by Yoshua Bengio and published 3 February 2026, records that in 2025 developers shipped models with extra safeguards because they "could not exclude the possibility that these models could assist novices in developing such weapons."

**Plain summary (needs sign-off from this side):** The knowledge barrier is falling fast and measurably. Models now outperform expert virologists on at least one specialist test, and a [February 2026 study](https://arxiv.org/abs/2602.23329) of novices answering dual-use biology questions found the group with model access was 4.16 times more accurate than the internet-only group, beating human experts on three of four benchmarks, with 89.6% of participants reporting little difficulty getting the information despite safeguards. The companies building these systems are not disputing this: all three major developers restricted models in 2025 on biological grounds. Separately from chatbots, [biological design models](https://www.congress.gov/119/meeting/house/118773/witnesses/HHRG-119-IF02-Wstate-PannuJ-20251217.pdf) are being released, sometimes without basic safety assessment, that can design novel viral components and craft sequences that evade the screening software meant to catch them. The attack itself only has to work once, and the measure that would most reduce the risk, mandatory screening of synthetic DNA orders, has been sitting unfinished in the US executive branch since 2025.

## The case that it doesn't
- RAND's red-team study of [January 2024](https://www.rand.org/pubs/research_reports/RRA2977-2.html) (Christopher Mouton, Caleb Lucas and Ella Guest) found no statistically significant difference in the viability of attack plans produced with and without model access, and concluded that this kind of planning lies "beyond the capability frontier of LLMs as assistive tools."
- Aidan Peppin, Anka Reuel, Stephen Casper and co-authors, in ["The Reality of AI and Biorisk"](https://arxiv.org/abs/2412.01946) (ACM FAccT, June 2025), found the existing body of work "nascent, often speculative in nature, or limited" in method and transparency, and concluded that current systems do not pose an immediate risk.

**Plain summary (needs sign-off from this side):** Benchmarks measure answering questions, and nobody has ever been killed by a correctly answered question. The only randomized trial that put people in a laboratory, [Active Site's eight-week study](https://arxiv.org/abs/2602.16703) of 153 novices published in February 2026, found 5.2% of the group with model access completed the full workflow against 6.6% of the internet-only group, a difference that was not statistically significant (P = 0.759). Participants in both arms rated YouTube more useful than any of the models, and the models in the assisted arm had safeguards removed. Forecasters who had predicted a 27% completion rate for the assisted group were wrong by a factor of five. Physical skill, materials and equipment are the constraint, and text does not transmit physical skill. Treating every capability result as near-term catastrophe risk also carries its own cost: it is being used to argue for restricting the same biology tools that are producing medical progress.

## Common ground
- Benchmark performance is real and rising. Models match or beat expert virologists on at least one specialist test, which was not true in 2023.
- No measured uplift at the wet-lab step has yet been demonstrated in a randomized trial ([Active Site, February 2026](https://arxiv.org/abs/2602.16703)).
- Both trials tested novices. Neither tested trained scientists, who are the group most likely to be helped to a dangerous degree.
- Material barriers matter and are poorly understood. The [2026 safety report](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) says it "remains difficult to assess the degree to which material barriers continue to constrain actors."
- Both sides support screening of synthetic DNA orders. The skeptics support it because the physical step is where the real barrier is, and the worried side supports it because it is the one chokepoint that does not depend on predicting model capability.

## Cruxes
1. **Does measured laboratory uplift appear once the trial is rerun with 2026-era agentic models and cloud-lab access?** The negative result is specific to mid-2025 models and human hands. *Check: replication of the Active Site trial, 2027 to 2028.*
2. **Is the binding constraint knowledge or materials?** If mandatory synthesis screening passes and the risk estimates of both camps fall, materials were the constraint. If screening-evasion by sequence design defeats it, knowledge was. *Check: US screening legislation and OSTP framework, 2027.*
3. **Do models without safeguards reach the level the safeguarded frontier models are now restricted at?** Safeguards only matter if the unrestricted alternative is worse. *Check: International AI Safety Report, 2027 edition.*

## Probability estimates

| Source | Who | Question or claim | Estimate | Date | Scorable? |
|---|---|---|---|---|---|
| [FRI](https://forecastingresearch.substack.com/p/forecasting-biosecurity-risks-from) | 46 biosecurity and biology experts | Chance of a human-caused epidemic killing over 100,000 people, in 2028 | 0.3% (median) | Jul 2025 | Yes, by 2028 |
| Same | Same | Same, if AI matched a top virologist team on the Virology Capabilities Test | 1.5% (median) | Jul 2025 | Conditional |
| Same | Same | Same, if AI enabled 50% of non-experts to synthesize influenza | 1.25% (median) | Jul 2025 | Conditional |
| Same | Same | Same, with anti-jailbreak measures plus required screening by synthesis providers | 0.4% (median) | Jul 2025 | Conditional |
| [FRI](https://forecastingresearch.substack.com/p/how-well-did-superforecasters-and) | 30 superforecasters, 30 biosecurity experts, 17 virologists | Human-caused outbreak causing 100,000+ deaths or $1 trillion damage in 2028, before and after seeing the wet-lab trial results | 0.3% fell to 0.2% (median) | Feb 2026 | Yes, by 2028 |
| Same | The 15 most accurate forecasters in that group | Same | 0.18% fell to 0.10% | Feb 2026 | Yes, by 2028 |
| Same | Same panel | Same, under a hypothetical fivefold uplift | 0.7% (median) | Feb 2026 | Conditional |
| Same | Same panel | Share of the model-assisted group that would complete the full laboratory workflow | 27% predicted (median) against 5.2% actual | Feb 2026 | Resolved, badly |

**Read these with care:** every number here is an annual probability of an epidemic from any human cause, not specifically an AI-assisted one, so AI is the conditioning variable rather than the subject. The last row is the most useful line in the table: the same expert groups whose conditional estimates drive the worried case overestimated real-world performance by a factor of five when a result could be checked.

## Evidence confidence
**Low.** Two randomized trials point in opposite directions because they measure different things, one answering questions and one doing laboratory work, and both tested only novices. Every published probability is conditional, and the one prediction that got scored was badly wrong.

## Signposts
1. A replication of a wet-lab trial using 2026-era agentic models, with cloud-lab access, shows a statistically significant completion gap.
2. OSTP publishes the replacement nucleic acid synthesis screening framework with the enforcement mechanism required by [Executive Order 14292](https://www.whitehouse.gov/presidential-actions/2025/05/improving-the-safety-and-security-of-biological-research/), which was due 90 days after 5 May 2025 and was still outstanding as of [September 2026](https://www.everycrsreport.com/reports/IF13269.html).
3. Congress enacts universal screening of synthetic nucleic acid orders, binding providers that do not take federal funding.
4. A developer reports a safeguard failure in which a user obtained end-to-end weapons-relevant help, rather than isolated facts. Anthropic reported users circumventing its biosafety safeguards in September 2026, describing them as working scientists.
5. A biological design model is released with a capability on a published list of capabilities of concern, with no safety assessment.

## Evidence so far
- [RAND, January 2024](https://www.rand.org/pubs/research_reports/RRA2977-2.html): red-team exercise, no measurable change in the operational risk of an attack from the then-current generation of models.
- [Peppin, Reuel, Casper and others, June 2025](https://arxiv.org/abs/2412.01946): review of the field, no immediate risk from current systems, methods immature.
- Anthropic [activated ASL-3](https://www.anthropic.com/news/activating-asl3-protections) safeguards in May 2025 as a precaution, saying it could not rule out chemical, biological, radiological and nuclear risk thresholds. OpenAI treated [ChatGPT agent](https://openai.com/index/chatgpt-agent-system-card/) as High capability in biology and chemistry in July 2025 on the same precautionary basis.
- [Active Site randomized trial, February 2026](https://arxiv.org/abs/2602.16703): 153 novices, eight weeks, no significant difference in completing the full workflow, a non-significant trend toward faster progress through intermediate steps (pooled estimate 1.4 times, 95% credible interval 0.74 to 2.62).
- [Scale AI and SecureBio study, February 2026](https://arxiv.org/abs/2602.23329): novices with model access 4.16 times more accurate on dual-use biology questions than internet-only controls, beating experts on three of four benchmarks.
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary), 3 February 2026: models can provide information relevant to biological and chemical weapons development, with substantial uncertainty about real-world uplift and material barriers.
- A June 2026 open letter to Congress calling for mandatory screening of synthetic nucleic acid orders was signed by the heads of OpenAI, Anthropic, Google DeepMind and Microsoft AI, along with Nobel laureates and US synthesis providers ([CRS](https://www.everycrsreport.com/reports/IF13269.html), September 2026).

## Existing coverage
Developing, producing, stockpiling or using these weapons is already prohibited by treaty. The [Biological Weapons Convention](https://disarmament.unoda.org/biological-weapons/) was the first treaty to ban an entire category of weapons of mass destruction, but it has no verification organization and relies on a network of cooperating bodies. The [Chemical Weapons Convention](https://www.opcw.org/chemical-weapons-convention) is stronger: 193 states, an implementing body in the OPCW, routine monitoring of listed chemicals, and challenge inspections on an "any time, anywhere" basis. Neither treaty reaches a lone actor, and neither mentions AI.

The gap is the digital-to-physical barrier. The 2024 US Framework for Nucleic Acid Synthesis Screening made screening a condition of federal research funding, so it does not bind commercial providers that take no federal money. More than 30 leading providers screen voluntarily. [Executive Order 14292](https://www.whitehouse.gov/presidential-actions/2025/05/improving-the-safety-and-security-of-biological-research/) (5 May 2025) ordered OSTP to replace the framework within 90 days and add an enforcement mechanism; [CRS reported in September 2026](https://www.everycrsreport.com/reports/IF13269.html) that it had not been updated, leaving providers without regulatory clarity. Bills are pending, including H.R. 3029, which has passed the House, and S. 3741. Free screening tools exist independently of regulation, including [SecureDNA](https://securedna.org/). Model-level safeguards are entirely voluntary: developers may report safety evaluation results to the US Center for AI Standards and Innovation, and [no law requires it](https://www.congress.gov/119/meeting/house/118773/witnesses/HHRG-119-IF02-Wstate-PannuJ-20251217.pdf).

## Triage
1. **Covered by law and enforced?** Covered, yes. Enforced, partly. The weapons themselves are banned by two treaties, one of which has real inspection powers. The step where AI actually changes something, the supply of synthetic genetic material, is governed by a framework that binds only federally funded buyers, with the replacement and its enforcement mechanism more than a year overdue.
2. **An action both camps accept?** Yes, and it is the same action: make screening of synthetic nucleic acid orders and customers mandatory for all providers. The skeptics support it because the physical barrier is the one they believe is doing the work, and the worried side supports it because it does not require winning the argument about model capability first. Frontier developers asked for it themselves in June 2026.
3. *(Not reached.)*

**Result: Enforcement problem.** The rules and the agreed fix both exist. What is missing is a published framework, a statute that covers providers outside federal funding, and an agency told to enforce it.

**Communication note:** Two randomized trials gave opposite-looking answers and both are being quoted selectively. The honest version is that AI has clearly reduced the knowledge barrier and has not yet been shown to reduce the laboratory barrier, that the people who were asked to predict the laboratory result were wrong by a factor of five in the alarming direction, and that the one measure nearly everyone agrees on has been stuck in an unfinished rulemaking since 2025. Do not let the disagreement about probability hide the agreement about what to do.

## Related scenarios
- Opposite in the same domain: "Medical progress compressed into years" (the same biology capabilities, used well).
- Same mechanism, different domain: "Cheap large-scale cyberattacks and critical-system failures."
- Raised by: "Loss of control over advanced AI" (safeguards assume a system that can be constrained).
- Reduced by: "AI disappoints."

## Sources
1. International AI Safety Report 2026, executive summary, chaired by Yoshua Bengio, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-executive-summary
2. Jassi Pannu, testimony before the US House Committee on Energy and Commerce, Subcommittee on Oversight and Investigations, "Examining Biosecurity at the Intersection of AI and Biology," 17 December 2025. https://www.congress.gov/119/meeting/house/118773/witnesses/HHRG-119-IF02-Wstate-PannuJ-20251217.pdf
3. Christopher A. Mouton, Caleb Lucas and Ella Guest, "The Operational Risks of AI in Large-Scale Biological Attacks," RAND Corporation, 25 January 2024. https://www.rand.org/pubs/research_reports/RRA2977-2.html
4. Aidan Peppin, Anka Reuel, Stephen Casper and others, "The Reality of AI and Biorisk," ACM Conference on Fairness, Accountability and Transparency, June 2025 (preprint December 2024). https://arxiv.org/abs/2412.01946
5. Shen Zhou Hong and others (Active Site), "Measuring Mid-2025 LLM-Assistance on Novice Performance in Biology," arXiv preprint, 18 February 2026. https://arxiv.org/abs/2602.16703
6. Chen Bo Calvin Zhang and others (Scale AI and SecureBio), "LLM Novice Uplift on Dual-Use, In Silico Biology Tasks," arXiv preprint, 26 February 2026. https://arxiv.org/abs/2602.23329
7. Forecasting Research Institute, "Forecasting biosecurity risks from large language models and the efficacy of safeguards," 1 July 2025. https://forecastingresearch.substack.com/p/forecasting-biosecurity-risks-from
8. Jamie Parry, Bridget Williams, Zack Devlin-Foltz and Matt Reynolds, "How Well Did Superforecasters and Experts Predict Wet Lab Skill Uplift from LLMs?", Forecasting Research Institute, 19 February 2026. https://forecastingresearch.substack.com/p/how-well-did-superforecasters-and
9. Anthropic, "Activating AI Safety Level 3 Protections," 22 May 2025. https://www.anthropic.com/news/activating-asl3-protections
10. OpenAI, "ChatGPT agent System Card," July 2025. https://openai.com/index/chatgpt-agent-system-card/
11. Congressional Research Service, "Artificial Intelligence and Biosecurity Issues," In Focus IF13269, updated 15 September 2026. https://www.everycrsreport.com/reports/IF13269.html
12. UN Office for Disarmament Affairs, "Biological Weapons Convention." https://disarmament.unoda.org/biological-weapons/
13. Organisation for the Prohibition of Chemical Weapons, "Chemical Weapons Convention." https://www.opcw.org/chemical-weapons-convention
14. Executive Order 14292, "Improving the Safety and Security of Biological Research," 5 May 2025. https://www.whitehouse.gov/presidential-actions/2025/05/improving-the-safety-and-security-of-biological-research/
15. SecureDNA Foundation, screening service. https://securedna.org/

## Sign-off record
- Worried case: not yet reviewed.
- Optimistic case: not yet reviewed.
- Changelog: 2026-10-09 first draft.
