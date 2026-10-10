---
id: none-bad-unknown-combined
name: Unknown, combined and slow-building risks
domain: none
direction: bad
layer: pathway
mechanism: [systemic, malfunction, loss-of-control]
mit_domain: "7.6 Multi-agent risks (also 5.2 Loss of human agency and autonomy)"
quadrants: [gradual-concentrated, gradual-shared, fast-shared]
triage: prepare-and-watch
confidence: very-low
summary: "Harm builds from many small AI-driven changes, or from AI systems interacting in ways nobody designed, until societies lose resilience or meaningful human control without any single event or culprit to point to."
status: draft
last_reviewed: 2026-10-09
---

# Unknown, combined and slow-building risks

**In one sentence:** Harm builds from many small AI-driven changes, or from AI systems interacting in ways nobody designed, until societies lose resilience or meaningful human control without any single event or culprit to point to.

**Design note:** this is the map's open entry. Every other card describes one recognizable story. This one exists because the serious research on AI risk says plainly that the list of stories is incomplete. The MIT AI Risk Repository already catalogues more than 1,700 distinct risks drawn from 65 frameworks ([MIT AI Risk Repository](https://airisk.mit.edu/)), Critch and Russell note that many complete taxonomies are possible ([TASRA, 2023](https://arxiv.org/abs/2306.06924)), and the most discussed slow-building risks have no single trigger, owner or date. A map with 17 neat boxes and no remainder would overstate what anyone knows.

The entry has two jobs. First, it holds three kinds of risk that do not fit one box: **accumulation** (many small harms that weaken a society until a shock tips it over), **gradual disempowerment** (humans keep formal authority but lose real influence), and **interaction effects** (AI systems colliding, colluding or cascading in ways no single operator chose). Second, it is a waiting room. A candidate scenario is **promoted out** of this entry into its own card when it passes all three parts of the map's inclusion test: (1) it has at least one named public proponent with standing who argues it is a serious risk, (2) it is meaningfully distinct from every existing card, with a different mechanism, different signposts or a different policy response, and (3) a balanced review panel, with members from both the worried and the skeptical side, agrees it qualifies. Gradual disempowerment is the strongest current candidate for promotion.

## Preconditions
- Many AI systems are deployed across the economy, government and daily life, often acting for different owners with different goals.
- Humans hand over decisions one at a time, each step reasonable on its own, because AI is cheaper or faster and competitors are doing the same.
- Each individual harm is small, slow or spread out enough to escape notice or blame.
- No single actor is accountable for the overall outcome, so nobody is in a position to stop it.

## Timing and reversibility
- **Earliest plausible date:** small interaction failures between automated systems have already happened (the May 2010 "flash crash" predates modern AI). For the large version, no author gives a date. Paul Christiano's 2023 estimates for this kind of failure are framed around the ten years after powerful AI is built, whenever that is ([Christiano, 2023](https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom)).
- **Speed:** both. Accumulation and disempowerment are slow, over years or decades. Interaction failures can unfold in minutes.
- **Reversibility:** individual interaction failures are usually reversible (markets reopen, trades are cancelled). The defining worry about accumulation and disempowerment is that by the time the pattern is clear, the tools to reverse it (human expertise, institutions, bargaining power) have already been given away.

## The case that this happens
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- Atoosa Kasirzadeh, philosopher of AI, in ["Two Types of AI Existential Risk: Decisive and Accumulative"](https://arxiv.org/abs/2401.07836) (*Philosophical Studies*, 2025), contrasts the familiar picture of a sudden AI takeover with an accumulative one, where many interconnected harms slowly erode economic and political structures, like a boiling frog, until a trigger event causes irreversible collapse.
- Jan Kulveit, David Duvenaud, David Krueger and colleagues, in ["Gradual Disempowerment"](https://arxiv.org/abs/2501.16946) (January 2025), argue that as AI replaces human labor and thinking, the economy, culture and governments stop needing human participation, which removes the quiet pressure that keeps them serving people. They warn of an "effectively irreversible loss of human influence over crucial societal systems."
- Andrew Critch and Stuart Russell (UC Berkeley), in [TASRA](https://arxiv.org/abs/2306.06924) (2023), describe harms from automated processes where "no one in particular is primarily responsible," and a *production web* story in which automated companies trade mostly with each other while their goals drift away from human welfare. Lewis Hammond and about 40 co-authors, in the Cooperative AI Foundation's [*Multi-Agent Risks from Advanced AI*](https://arxiv.org/abs/2502.14143) (February 2025), sort the risks of many interacting AI agents into miscoordination, conflict and collusion, driven by factors such as network effects, selection pressures and emergent agency.

**Plain summary (needs sign-off from this side):** The usual picture of AI catastrophe is one dramatic event. But societies more often fail through many small stresses that pile up: a bit less human expertise here, a bit more automated decision-making there, a few AI systems interacting in ways nobody tested. Each step looks harmless and each has a sensible business reason. Because no one is in charge of the whole, no one is responsible for stopping it, and by the time the pattern is obvious the human skills and institutions needed to reverse it may be gone. These risks are easy to miss precisely because they never produce a single headline, which is why a map of AI futures needs a place to hold them.

## The case that it doesn't
- Blake Richards, Blaise Agüera y Arcas, Guillaume Lajoie and Dhanya Sridhar argued in [*Noema* (July 2023)](https://www.noemamag.com/the-illusion-of-ais-existential-risk/) that existential framings rest on speculative assumptions and that dwelling on them "may prevent us from addressing AI's disruptive dangers to society today," such as surveillance, disinformation and economic disruption.
- Arvind Narayanan and Sayash Kapoor (Princeton) argued in [July 2024](https://www.normaltech.ai/p/ai-existential-risk-probabilities) that probability estimates for AI catastrophe have no sound basis (no track record, no model, guesses that differ by orders of magnitude) and are "far too unreliable to be useful for policy." Petr Jedlicka, in a [2026 critique of gradual scenarios](https://arxiv.org/abs/2608.03904), argues they treat AI's spread as a purely technical process and underrate how people will notice, resist and fight back along the way.

**Plain summary (needs sign-off from this side):** A scenario with no trigger, no date, no culprit and no clear test is hard to prove wrong, and claims that cannot be proved wrong make poor guides for policy. "Everything might add up to collapse" can absorb any piece of evidence, which makes it a story rather than a forecast. Meanwhile the concrete harms that make up the pile (bias, fraud, surveillance, job disruption, unsafe products) are already measurable and fixable one at a time, and they already have their own cards on this map. Societies also react: people organize, vote, sue and regulate as they see change coming. Spending attention on a vague combined risk can pull it away from the specific ones.

## Common ground
- Automated systems interacting at speed can cause real damage that no single operator intended. The 2010 flash crash is the standard example ([TASRA](https://arxiv.org/abs/2306.06924); [SEC](https://www.sec.gov/news/press/2010/2010-179.htm)).
- Gaps in accountability, where nobody is clearly responsible for an automated outcome, are a real governance problem today.
- Resilience helps against both concrete and speculative harms: keeping human expertise, keeping the ability to override or switch off automated systems, and reporting incidents. Kasirzadeh presents the accumulative view as a way to connect present-day harms and long-term catastrophe, rather than pit them against each other ([Kasirzadeh, 2025](https://arxiv.org/abs/2401.07836)).
- No list of AI risks is complete, and new kinds of risk will be proposed.

## Cruxes
1. **Do interacting AI agents cause failures no single operator caused?** If large deployments of AI agents produce collusion, cascades or conflicts that operators did not design and could not prevent, the interaction branch of this card becomes concrete. *Check: International AI Safety Report 2027 and published incident databases, 2027.*
2. **Can loss of human influence be measured, and is it rising?** Early research found severe disempowerment potential in fewer than 1 in 1,000 Claude.ai conversations, with signs of an increase over time ([Sharma et al., January 2026](https://arxiv.org/abs/2601.19062)). Repeated measurements across products and institutions would turn the disempowerment claim into something testable. *Check: follow-up studies, 2027 to 2028.*
3. **Do societies push back in time?** Jedlicka's critique predicts conflict and correction as AI spreads. Laws that require human decision-makers in key roles, or public backlash that slows automation, would support the skeptics. *Check: national and EU legislation, 2027 to 2028.*

## Probability estimates
**No published estimate** exists for accumulative risk, gradual disempowerment or multi-agent catastrophe as such. The closest related numbers:

| Source | Who | Question or claim | Estimate | Date | Scorable? |
|---|---|---|---|---|---|
| [Christiano, "My views on doom"](https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom) | One alignment researcher | Humanity has irreversibly messed up its future within 10 years of building powerful AI | 46% | Apr 2023 | Partly, once powerful AI exists |
| Same | Same | Of that, "messing it up in some other way during a period of accelerated technological change" (not takeover, not extinction) | 15% | Apr 2023 | Same |
| [Forecasting Research Institute tournament](https://forecastingresearch.org/xpt), as summarized in secondary sources (verify against the report) | 80 domain experts | AI-caused catastrophe (more than 10% of humans die within five years) by 2050 / by 2100 | 5% / 12% (median) | 2022 | Partly by 2050 |
| Same | 89 superforecasters | Same | 0.73% / 2.13% (median) | 2022 | Partly by 2050 |

**Read these with care:** the closest row (Christiano's 15%) is one person's guess, conditional on a date nobody agrees on. The tournament questions count deaths, which slow disempowerment might never cause. Narayanan and Kapoor's critique applies with extra force here, because there is no agreed definition of the event to forecast.

## Evidence confidence
**Very low.** The mechanisms are argued from theory and small precedents. The large versions have never been observed and have no agreed test.

## Signposts
1. A market, power-grid or communications disruption costing more than $1 billion or lasting more than a few hours is officially attributed to the interaction of several AI systems rather than a single bug or attacker.
2. A regulator confirms that AI agents from different operators coordinated on prices or other behavior without any human instructing them to.
3. A large company or government agency confirms that a core decision process (hiring, lending, benefits, procurement) runs with no human sign-off as standard practice.
4. Follow-up measurement finds severe disempowerment potential in more than 1 in 100 AI assistant conversations (from fewer than 1 in 1,000 in early 2026).
5. A new candidate scenario passes the inclusion test and is promoted out of this entry. This is a sign the entry is working, not a harm.

## Evidence so far
- On 6 May 2010 the Dow Jones index fell nearly 1,000 points in under half an hour. The SEC and CFTC staff report traced the start to a large automated sell order interacting with high-frequency trading algorithms ([SEC, 1 October 2010](https://www.sec.gov/news/press/2010/2010-179.htm); [IEEE Spectrum](https://spectrum.ieee.org/flash-crash-cause-found), secondary). Critch and Russell describe it as interacting algorithms briefly erasing over a trillion dollars in market value ([TASRA](https://arxiv.org/abs/2306.06924)).
- Moltbook, a social network open only to AI agents, launched in January 2026 and claimed nearly 2.9 million registered agents by June 2026. Within its first weeks, researchers found security flaws that let anyone take over any agent or read agents' private messages, and observers disputed how much of the agents' activity was truly autonomous ([Wikipedia summary of press coverage](https://en.wikipedia.org/wiki/Moltbook), secondary). It is a small, early example of large numbers of AI agents interacting in public with weak oversight.
- Researchers analyzing 1.5 million Claude.ai conversations found that interactions with greater potential to undermine the user's own judgment received higher approval ratings from users, a small-scale version of the incentive the gradual disempowerment paper describes ([Sharma et al., January 2026](https://arxiv.org/abs/2601.19062)).
- The [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) notes the shift toward more autonomous AI agents and multi-agent systems, and that agents acting on their own make it harder for humans to intervene before failures cause harm.
- The MIT AI Risk Repository added a separate subdomain for multi-agent risks in April 2025 ([MIT AI Risk Repository](https://airisk.mit.edu/blog/april-2025-update-of-the-ai-risk-repository-2)).

## Existing coverage
No law addresses accumulative or combined AI risk as such. Pieces apply:
- The EU AI Act requires providers of the most capable general-purpose models (those with "systemic risk") to evaluate and reduce systemic risks across the EU and report serious incidents, from 2 August 2025 ([AI Act Article 55](https://artificialintelligenceact.eu/article/55/)). Enforcement is new and untested.
- Financial regulators reviewed automated trading after 2010 ([SEC](https://www.sec.gov/news/press/2010/2010-179.htm)), but those rules were not designed for AI agents acting across many markets at once.
- Competition law applies to price coordination, but its fit with AI agents that coordinate without any human agreement is unsettled (no verified source found; flagged for research).

## Triage
1. **Covered by law and enforced?** No. Only fragments are covered, and the core problem (no single accountable actor) is exactly what existing law handles worst.
2. **An action both sides accept?** **Not yet.** Both sides would likely accept generic resilience measures (incident reporting, the ability to override automated systems, keeping human expertise), but the skeptics reject the framing that would justify them under this card, and no joint statement exists. Those measures are better argued for on the specific cards where they apply.
3. **Severe, hard to reverse, with a credible estimate within about ten years, and no agreed action?** **Partly.** Severity and irreversibility are the whole worry. The only estimate close to the ten-year test is Christiano's 15%, and it is tied to the arrival of powerful AI rather than to a calendar date.

**Result: Prepare and watch**, tied to signposts 1 to 4. Treat signpost 5 as the routine maintenance task for this entry.

**Communication note:** Say plainly that this entry exists because nobody's list of AI risks is complete, not because something specific has been found. Its job is to keep slow and combined risks visible, and to give new concerns a fair route onto the map through the inclusion test instead of through whoever shouts loudest.

## Related scenarios
- Holds pieces of: "Over-reliance, lost skills and unhealthy AI companions" (slow loss of human skill and judgment), "Concentrated power or AI-enabled surveillance," "Mass job loss and widening inequality," and "Cheap large-scale cyberattacks and critical-system failures" (cascades).
- Overlaps: "Loss of control over advanced AI" (gradual disempowerment is the slow version of the same end state).
- Candidate for promotion: gradual disempowerment, if a balanced panel judges it distinct from "Loss of control over advanced AI."

## Sources
1. MIT AI Risk Repository. https://airisk.mit.edu/
2. MIT AI Risk Repository, "Repository Update: April 2025." https://airisk.mit.edu/blog/april-2025-update-of-the-ai-risk-repository-2
3. Critch A., Russell S., "TASRA: a Taxonomy and Analysis of Societal-Scale Risks from AI," arXiv, June 2023. https://arxiv.org/abs/2306.06924
4. Kasirzadeh A., "Two Types of AI Existential Risk: Decisive and Accumulative," *Philosophical Studies* (arXiv version revised January 2025). https://arxiv.org/abs/2401.07836
5. Kulveit J., Douglas R., Ammann N., Turan D., Krueger D., Duvenaud D., "Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development," arXiv, January 2025. https://arxiv.org/abs/2501.16946
6. Hammond L. et al., "Multi-Agent Risks from Advanced AI," Cooperative AI Foundation Technical Report #1, arXiv, February 2025. https://arxiv.org/abs/2502.14143
7. Christiano P., "My views on 'doom'," LessWrong, 27 April 2023. https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom
8. Richards B., Agüera y Arcas B., Lajoie G., Sridhar D., "The Illusion Of AI's Existential Risk," *Noema*, 18 July 2023. https://www.noemamag.com/the-illusion-of-ais-existential-risk/
9. Narayanan A., Kapoor S., "AI existential risk probabilities are too unreliable to inform policy," AI Snake Oil (now Normal Tech), 26 July 2024. https://www.normaltech.ai/p/ai-existential-risk-probabilities
10. Jedlicka P. O., "Why do we need social singularity? A mechanism-based critique of gradual scenarios in AI existential-risk discourse," arXiv, August 2026. https://arxiv.org/abs/2608.03904
11. US Securities and Exchange Commission, press release 2010-179 on the joint SEC-CFTC staff report on the market events of 6 May 2010, 1 October 2010. https://www.sec.gov/news/press/2010/2010-179.htm
12. IEEE Spectrum, "Flash Crash Cause Found," 2010 (secondary). https://spectrum.ieee.org/flash-crash-cause-found
13. Sharma M., McCain M., Douglas R., Duvenaud D., "Who's in Charge? Disempowerment Patterns in Real-World LLM Usage," arXiv, January 2026. https://arxiv.org/abs/2601.19062
14. Forecasting Research Institute, Existential Risk Persuasion Tournament (XPT), 2022 tournament, report 2023. https://forecastingresearch.org/xpt
15. Wikipedia, "Moltbook" (summary of press coverage, secondary). https://en.wikipedia.org/wiki/Moltbook
16. International AI Safety Report 2026, 3 February 2026. https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
17. EU AI Act, Article 55, Obligations for providers of general-purpose AI models with systemic risk. https://artificialintelligenceact.eu/article/55/

## Sign-off record
- Worried case: not yet reviewed.
- Optimistic case: not yet reviewed.
- Changelog: 2026-10-09 first draft.
