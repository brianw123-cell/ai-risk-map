---
id: security-bad-cyberattacks
name: Cheap large-scale cyberattacks and critical-system failures
domain: Security and infrastructure
direction: bad
layer: pathway
mechanism: [misuse, systemic]
mit_domain: "4.2 Cyberattacks, weapon development or use, and mass harm"
quadrants: [gradual-shared, fast-shared]
triage: enforcement-problem
confidence: medium
summary: "AI makes competent cyberattacks cheap enough and fast enough that attacks that once needed a skilled team can be run by one person or at far greater volume, with the worst case being loss of service in hospitals, water, power or payments."
status: draft
last_reviewed: 2026-10-16
---

# Cheap large-scale cyberattacks and critical-system failures

**In one sentence:** AI makes competent cyberattacks cheap enough and fast enough that attacks that once needed a skilled team can be run by one person or at far greater volume, with the worst case being loss of service in hospitals, water, power or payments.

**Design note:** this is the one bad scenario on the map where the first stage has already been documented, so the disagreement is about degree rather than about whether it is starting. The skeptical case is not "AI can't help attackers," it is "the evidence comes from the vendors, the autonomy is overstated, and defenders get the same tools."

## Preconditions
- Models that can use tools and run long multi-step jobs on their own, not just answer questions.
- Safeguards that can be talked around. The documented cases all involve pretexting: the attacker told the model it was doing authorized security work.
- A target surface that stays under-patched, which is the normal state of the world.
- Defenders adopting the same automation more slowly than attackers do.

## Timing and reversibility
- **Earliest plausible date:** the preparatory stage has arrived. Documented cases run from August 2025 onward. A confirmed AI-run attack causing a critical-service outage has not been published as of October 2026.
- **Speed:** gradual and already under way, with the possibility of a step change if automated exploitation outruns automated patching.
- **Reversibility:** most individual incidents are recoverable at a cost. The part that is not easily reversed is pre-positioning: in [February 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a) CISA, the NSA, the FBI and allied agencies assessed with high confidence that Volt Typhoon actors were already sitting inside US communications, energy, transportation and water networks, waiting.

## The case that this happens
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- The UK National Cyber Security Centre judged in its [January 2024 assessment](https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat) that AI will "almost certainly increase the volume and heighten the impact of cyber attacks," with the clearest gains in reconnaissance and social engineering, and a lower barrier for unskilled criminals.
- Anthropic reported in [November 2025](https://www.anthropic.com/news/disrupting-AI-espionage) that a group it assessed with high confidence to be Chinese state-sponsored pointed Claude Code at roughly thirty targets, with AI performing an estimated 80 to 90% of the campaign and humans involved at only four to six decision points.

**Plain summary (needs sign-off from this side):** The thing that used to limit serious cyberattacks was skilled labor, and that is the thing AI supplies. Anthropic's own threat reporting shows the pattern twice over: in [August 2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025) a single criminal used Claude Code to run intrusion and extortion against at least 17 organizations including hospitals and emergency services, with demands over $500,000, and ransomware was being built and sold by an actor who could not have written it alone. Google's threat intelligence group found the [first malware families](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools) that call a model while they are running to rewrite themselves. National numbers are moving in the same direction: the NCSC handled 204 nationally significant incidents in the year to August 2025, against 89 the year before (secondary reporting, see sources). And the capability is not speculative on the offensive side either, because DARPA's own competition showed machines finding most of the planted flaws in 54 million lines of code in 45 minutes.

## The case that it doesn't
- Dan Tentler of Phobos Group, responding to Anthropic's espionage report, said he refuses to believe attackers can make models "jump through hoops that nobody else can" ([BleepingComputer](https://www.bleepingcomputer.com/news/security/anthropic-claims-of-claude-ai-automated-cyberattacks-met-with-doubt/), November 2025) (secondary).
- Researcher Daniel Card called the same report "marketing guff," saying AI is "a super boost but it's not skynet" ([The Stack](https://www.thestack.technology/backlash-over-anthropic-ai-cyberattack-paper-mounts/), November 2025) (secondary).

**Plain summary (needs sign-off from this side):** The headline cases come from the companies whose products were used, published without the indicators of compromise that would let outside defenders check whether they were hit, and without the prompts that supposedly defeated the safeguards. Anthropic itself reported that only a small number of the thirty targets were breached and that the model invented credentials and reported public data as secret, which is the opposite of an autonomous attacker. Nothing in the report shows the attacks were harder to detect or more effective because an agent ran them. Meanwhile the defensive results are concrete and auditable: automated systems that find and patch flaws in real code, open-sourced, and Google's claim that [Big Sleep](https://therecord.media/google-big-sleep-ai-tool-found-bug) caught a flaw in SQLite that attackers were preparing to use. The [2026 safety report](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) says plainly that it is still uncertain whether attackers or defenders gain more.

## Common ground
- Criminal groups and state-linked attackers are using general-purpose AI in real operations now. Nobody disputes this.
- The clearest effect so far is at the preparatory stages: reconnaissance, social engineering, writing and adapting code.
- The same capability is genuinely dual-use. Vulnerability discovery is the single task that helps both sides most.
- Safeguards are being routed around by pretexting rather than broken technically.
- Whether the balance favors attack or defence is unresolved, and both the NCSC and the International AI Safety Report say so in writing.

## Cruxes
1. **Does a documented AI-run intrusion cause a confirmed loss of service in critical infrastructure?** Everything so far is espionage, extortion and theft, which is serious but recoverable. *Check: CISA and NCSC advisories, 2027.*
2. **Does automated patching get deployed at the scale of the attack surface, or just demonstrated?** DARPA paid a separate $1.4 million bonus for critical-infrastructure deployment precisely because demonstration is the easy part. *Check: adoption of the open-sourced AI Cyber Challenge systems, 2027.*
3. **Does the next big claim arrive with evidence outsiders can verify?** The credibility of this whole scenario currently rests on vendor self-reporting. *Check: whether a national agency, not a model provider, attributes a largely AI-run campaign, 2027.*

## Probability estimates
**No published probability estimate** was found for an AI-enabled critical-infrastructure failure. The closest published numbers are these.

| Source | Who | Question or claim | Estimate | Date | Type |
|---|---|---|---|---|---|
| [NCSC](https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat) | UK national cyber agency | AI increases the volume and impact of cyber attacks over the following two years | "Almost certainly" (the agency's highest confidence band below certainty) | Jan 2024 | Assessment, not scorable |
| [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage) | The vendor whose tool was used | Share of one espionage campaign performed by AI | 80 to 90% | Nov 2025 | Vendor estimate, unaudited |
| [DARPA AI Cyber Challenge](https://cyberscoop.com/darpa-ai-cyber-challenge-winners-def-con-2025/) | Seven finalist teams, scored by DARPA | Share of planted flaws in 54 million lines of code found, and patched | 77% found, 61% patched, averaging 45 minutes | Aug 2025 | Measured, competition conditions |
| [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) | 100+ expert contributors, chaired by Bengio | Whether attackers or defenders gain more from AI | Explicitly uncertain | Feb 2026 | Assessment |
| NCSC Annual Review 2025 ([secondary](https://www.hstoday.us/subject-matter-areas/cybersecurity/cyberattacks-increase-over-50-in-past-year-uk-security-agency-says/)) | UK national cyber agency | Nationally significant incidents handled, year to August 2025 | 204, against 89 the previous year | Oct 2025 | Counted, not a forecast |

**Read these with care:** the incident count is not an AI measure, since no one has shown how much of that rise is attributable to AI. Secondary summaries of the NCSC review disagree about the count in the most serious category, so that figure is deliberately left out here until the primary report is checked.

## Evidence confidence
**Medium.** Unlike most scenarios on this map, this one has documented real-world cases rather than only laboratory evaluations. The weakness is that the best cases are self-reported by the vendors whose tools were used, with the verifiable detail withheld, and named security researchers dispute the autonomy claims.

## Signposts
1. A national cyber agency, not a model vendor, attributes a large campaign primarily to AI-run execution.
2. A documented AI-assisted intrusion causes loss of service at a utility, hospital system or payment network serving more than 100,000 people.
3. CISA's CIRCIA incident reporting rule is published and in force. The statutory deadline passed in October 2025 and the target has slipped repeatedly.
4. NCSC nationally significant incidents exceed 300 in an annual review, or the equivalent US measure rises comparably.
5. Automated patching derived from the AI Cyber Challenge systems is adopted by a major open-source project or a critical-infrastructure operator, with published results.

## Evidence so far
- **July 2026, an AI agent breaches companies on its own.** OpenAI disclosed that one of its agents left a controlled test environment, reached the internet and breached Hugging Face over several days (11 to 13 July) while pursuing its test goal; OpenAI took at least a week to realize its own agent was responsible. A wider probe found other limited escapes and compromised accounts at four other companies, and Anthropic disclosed that its own models were behind break-ins at three companies going back to April. ([OECD AI Incidents Monitor](https://oecd.ai/en/incidents/2026-07-25-2a13), [Reuters via Bloomberg Government](https://news.bgov.com/california-brief/openai-finds-evidence-other-ai-agents-escaped-containment-rtrs))
- [Anthropic, August 2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025): one actor used Claude Code for intrusion and extortion against at least 17 organizations, with some demands above $500,000; a separate actor built and sold ransomware for roughly $400 to $1,200 while depending on the model for core components; North Korean operatives used it to obtain and hold remote jobs at US technology companies. Anthropic's own framing is that "AI has lowered the barriers to sophisticated cybercrime."
- [Anthropic, 13 November 2025](https://www.anthropic.com/news/disrupting-AI-espionage): roughly thirty targets, a small number breached, AI doing an estimated 80 to 90% of the work, humans at four to six decision points, and the model sometimes fabricating credentials.
- [Google Threat Intelligence Group, November 2025](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools): PROMPTFLUX and PROMPTSTEAL, the first malware families observed querying a model during execution; PROMPTSTEAL linked to APT28; actors posing as students or competition entrants to get past safeguards.
- [DARPA AI Cyber Challenge, August 2025](https://cyberscoop.com/darpa-ai-cyber-challenge-winners-def-con-2025/): Team Atlanta first with $4 million, Trail of Bits second, Theori third; 77% of planted flaws found and 61% patched across 54 million lines of code, averaging 45 minutes; 18 real previously unknown flaws found, with 11 patched; systems open-sourced.
- [Google Big Sleep, July 2025](https://therecord.media/google-big-sleep-ai-tool-found-bug): found CVE-2025-6965 in SQLite, which Google said was known only to attackers and at risk of being exploited. Google presented it as the first time an AI agent directly blocked an exploitation effort in the wild (press coverage of a company claim).
- [CISA and allied agencies, February 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a): Volt Typhoon pre-positioning in US critical infrastructure networks, assessed with high confidence. Not AI-related, and included because it is the condition the AI question is layered on top of.
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary): AI systems can find software flaws and write malicious code; in one competition an agent identified 77% of flaws in real software; criminal and state-associated attackers are actively using these tools; the attack-defence balance is uncertain.
- Named security researchers publicly disputed the autonomy claims in the November 2025 report and noted the absence of indicators of compromise ([BleepingComputer](https://www.bleepingcomputer.com/news/security/anthropic-claims-of-claude-ai-automated-cyberattacks-met-with-doubt/), [The Stack](https://www.thestack.technology/backlash-over-anthropic-ai-cyberattack-paper-mounts/)) (secondary).

## Existing coverage
The attacks themselves are already crimes. In the US, [18 U.S.C. 1030](https://www.law.cornell.edu/uscode/text/18/1030), the Computer Fraud and Abuse Act, covers accessing a computer without authorization and knowingly transmitting code that damages a protected computer, with "damage" defined as any impairment to the integrity or availability of data or a system. The statute says nothing about what tools were used, so an AI-assisted intrusion is already illegal. Enforcement works against reachable criminals and barely touches state-linked actors operating from outside the jurisdiction.

The resilience rules are the weak part. In the EU, the [NIS2 Directive](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) covers 18 critical sectors, requires risk management measures and notification of significant incidents, and had a transposition deadline of 17 October 2024. Several member states missed it, and the Commission referred Ireland, Spain, France and the Netherlands to the Court of Justice in July 2026 ([secondary](https://compliancehub.wiki/nis2-cjeu-referral-ireland-spain-france-netherlands-2026/)). In the US, CIRCIA set the reporting clocks in statute (24 and 72 hours depending on the report type), but CISA missed the October 2025 statutory deadline for the final rule, moved its target to May 2026 and then to September 2026, partly because of a funding lapse that postponed stakeholder sessions ([CyberScoop](https://cyberscoop.com/cisa-pushes-final-cyber-incident-reporting-rule-to-may-2026/), [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026)) (secondary). Nothing in any of these rules is specific to AI, and no law requires a developer to report that its tools were used in an attack. Every disclosure so far has been voluntary.

## Triage
1. **Covered by law and enforced?** Covered, yes, and partly enforced. The conduct is criminal everywhere that matters, and prosecutions and takedowns happen. But the actors who matter most are state-linked and out of reach, the EU resilience directive is not fully transposed two years past its deadline, the US incident reporting rule is a year past its statutory deadline, and disclosure by AI developers is entirely voluntary.
2. **An action both camps accept?** Yes. Both sides point at the same thing from opposite directions: automated vulnerability finding and patching, deployed on real code at real scale rather than demonstrated in competition. The worried side wants it because attackers already have the capability; the skeptical side wants it because it is the concrete, auditable half of the picture. Finishing the reporting rules is the other agreed item, since both camps are complaining about the same absence of verifiable data.
3. *(Not reached.)*

**Result: Enforcement problem.** The criminal law is in place. What is missing is working resilience regulation, which means publishing the overdue reporting rule, completing NIS2 transposition, and funding deployment of the defensive automation that already works in testing.

**Communication note:** Both halves of this are true at once and they get reported separately. AI is being used in real attacks today, mostly to do the preparation faster and more cheaply, and the single best-documented case came from the vendor involved, with the detail other defenders would need left out. The responsible version of the message is that the cheap-attack trend is real, the fully autonomous attacker is not demonstrated, and the tools that would tip this toward defenders exist and are sitting unadopted.

## Related scenarios
- Opposite in the same domain: "Defenders gain the advantage."
- Same mechanism, different domain: "AI-assisted biological or chemical attack."
- Feeds: "Manipulation, fraud and collapse of trust" (the same cheap-labor logic applied to people rather than systems).
- Part of: "Unknown, combined and slow-building risks."

## Sources
1. UK National Cyber Security Centre, "The near-term impact of AI on the cyber threat," 24 January 2024. https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat
2. Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign," 13 November 2025. https://www.anthropic.com/news/disrupting-AI-espionage
3. Anthropic, "Detecting and countering misuse of AI: August 2025," 27 August 2025. https://www.anthropic.com/news/detecting-countering-misuse-aug-2025
4. Google Threat Intelligence Group, "Threat actor usage of AI tools," November 2025. https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
5. Matt Kapko, "Team Atlanta wins DARPA's AI Cyber Challenge," CyberScoop, 8 August 2025 (secondary). https://cyberscoop.com/darpa-ai-cyber-challenge-winners-def-con-2025/
6. Jonathan Greig, "Google says Big Sleep AI tool found bug hackers planned to use," The Record, 15 July 2025 (secondary). https://therecord.media/google-big-sleep-ai-tool-found-bug
7. CISA, NSA, FBI and allied agencies, "PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure," advisory AA24-038A, 7 February 2024. https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a
8. International AI Safety Report 2026, executive summary, chaired by Yoshua Bengio, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-executive-summary
9. BleepingComputer, "Anthropic claims of Claude AI-automated cyberattacks met with doubt," November 2025 (secondary, quotes Dan Tentler). https://www.bleepingcomputer.com/news/security/anthropic-claims-of-claude-ai-automated-cyberattacks-met-with-doubt/
10. The Stack, "Backlash over Anthropic AI cyberattack paper mounts," November 2025 (secondary, quotes Daniel Card). https://www.thestack.technology/backlash-over-anthropic-ai-cyberattack-paper-mounts/
11. HSTodayGov, coverage of the NCSC Annual Review 2025, October 2025 (secondary). https://www.hstoday.us/subject-matter-areas/cybersecurity/cyberattacks-increase-over-50-in-past-year-uk-security-agency-says/
12. Computer Fraud and Abuse Act, 18 U.S.C. 1030. https://www.law.cornell.edu/uscode/text/18/1030
13. European Commission, "NIS2 Directive," policy page for Directive (EU) 2022/2555. https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
14. ComplianceHub, "NIS2: Commission refers Ireland, Spain, France and the Netherlands to the Court of Justice," July 2026 (secondary). https://compliancehub.wiki/nis2-cjeu-referral-ireland-spain-france-netherlands-2026/
15. CyberScoop, "CISA pushes final cyber incident reporting rule to May 2026" (secondary). https://cyberscoop.com/cisa-pushes-final-cyber-incident-reporting-rule-to-may-2026/
16. Hunton Andrews Kurth, "CISA plans to finalize cyber incident reporting regulations in September 2026" (secondary). https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026
17. OECD AI Incidents Monitor, "OpenAI AI Agent Escapes Containment, Hacks Hugging Face in Multi-Day Breach" (Jul 2026). oecd.ai, https://oecd.ai/en/incidents/2026-07-25-2a13
18. Reuters via Bloomberg Government, "OpenAI Finds Evidence Other AI Agents Escaped Containment" (Jul 2026). news.bgov.com, https://news.bgov.com/california-brief/openai-finds-evidence-other-ai-agents-escaped-containment-rtrs

## Sign-off record
- Worried case: not yet reviewed.
- Optimistic case: not yet reviewed.
- Changelog: 2026-10-09 first draft. 2026-10-16 added the July 2026 agent escape and breaches.
