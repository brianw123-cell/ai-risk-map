---
id: security-good-defenders-advantage
name: Defenders gain the advantage
domain: Security and infrastructure
direction: good
layer: pathway
mechanism: [misuse, systemic]
mit_domain: "none (benefit)"
quadrants: [gradual-shared, fast-shared]
triage: act-now
confidence: medium
summary: "AI tilts cybersecurity toward defense, because finding and fixing software flaws becomes fast and cheap enough that most bugs are patched before attackers can use them."
status: draft
last_reviewed: 2026-10-09
---

# Defenders gain the advantage

**In one sentence:** AI tilts cybersecurity toward defense, because finding and fixing software flaws becomes fast and cheap enough that most bugs are patched before attackers can use them.

**Design note:** for a good-direction card, "worried" means worried this won't happen or is oversold. Here the worried side mostly agrees AI finds bugs well. Its doubt is about whether fixes reach real systems fast enough, so this card separates **finding** flaws from **fixing** them.

## Preconditions
- AI keeps getting better at finding software vulnerabilities (flaws an attacker can use to break in), and defenders get the strongest tools at least as early as attackers do.
- Fixing keeps pace with finding: volunteer maintainers of open-source software, vendors and patch pipelines can absorb the volume of AI-found bugs.
- Organizations actually install patches and retire old, unsupported equipment such as routers and VPN boxes.
- New code written with AI help ships with fewer flaws than the code it replaces.

## Timing and reversibility
- **Earliest plausible date:** the finding side is already here (2025 to 2026). A measurable shift in real attack statistics would show up in annual threat reports for 2027 or 2028 at the earliest. Replacing legacy infrastructure takes a decade or more.
- **Speed:** uneven. Large, well-resourced organizations could see the benefit within a few years. Small firms, hospitals, local utilities and old industrial systems lag far behind. The UK National Cyber Security Centre calls this a ["digital divide"](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027) (May 2025).
- **Reversibility:** not applicable for a benefit. The relevant risk is that the advantage is temporary. Anthropic warns that it ["will not be long before such capabilities proliferate"](https://www.anthropic.com/glasswing) to attackers (April 2026).

## The case that this happens (optimistic)
*Short excerpts for orientation only. A person from this side will choose the final quotes at sign-off.*

- Jen Easterly, former director of the US Cybersecurity and Infrastructure Security Agency (CISA), argued in October 2025 that if AI is built and governed securely, it could ["tip the balance to the defenders and protectors"](https://www.theregister.com/2025/10/27/jen_easterly_ai_cybersecurity/), because most breaches trace back to flawed code that AI can find and fix (reported by The Register, secondary).
- DARPA's AI Cyber Challenge (AIxCC), a two-year US government competition, ended in August 2025 with AI systems that [found 86% of planted flaws and patched 68%](https://darpa.mil/news/2025/aixcc-results), at about $152 per task, and DARPA released all seven finalist systems as [free, open-source software](https://archive.aicyberchallenge.com/).

**Plain summary (needs sign-off from this side):** For decades attackers had the edge because they only need one flaw while defenders must find them all, and skilled bug hunters are scarce and expensive. AI changes the economics. Systems from DARPA's competition, Google, Anthropic and OpenAI now find serious, previously unknown flaws in heavily tested software in hours, often flaws that years of automated testing missed, and some write the fix too. Defenders own the code, so they can run these tools first and continuously, before release. The same tools can rewrite old code into safer forms that remove whole classes of bugs. If security is built in rather than bolted on, breaches become rare exceptions rather than a cost of doing business.

## The case that it doesn't (worried this is oversold)
- Heather Adkins (a Google security vice president), Gadi Evron and Bruce Schneier wrote in October 2025 that ["the cyberattack/cyberdefense balance has long skewed towards the attackers"](https://www.schneier.com/essays/archives/2025/10/autonomous-ai-hacking-and-the-future-of-cybersecurity.html), and that AI agents automating attacks could tip it further unless new AI-assisted defenses arrive. They leave open whether defense eventually wins.
- Patrick Garrity of the vulnerability-intelligence firm VulnCheck reviewed Anthropic's public ledger of AI-found bugs in September 2026 and concluded ["the receipts are starting to trickle in, they just don't reconcile"](https://www.vulncheck.com/blog/anthropic-glasswing-receipts): of 26,153 claimed findings, 202 were marked fixed.

**Plain summary (needs sign-off from this side):** Finding bugs was never the main bottleneck. Fixing them is. Open-source maintainers are often unpaid volunteers who are already overwhelmed, and some have asked AI companies to slow down. Even when a patch exists, many organizations take weeks or months to install it, and old devices never get patched at all. Attackers only need to use AI against the systems that fall behind, and they already are: attackers now often exploit flaws before a fix exists. The best tools are held by a few companies, and comparable tools will reach attackers within months. AI may raise the floor for well-run organizations while leaving the long tail more exposed than before.

## Common ground
- AI now finds real, serious, previously unknown vulnerabilities at a scale no human team can match. Neither side disputes this.
- Finding a flaw is not the same as fixing it, and fixing it is not the same as getting the fix installed everywhere.
- The same capability helps attackers. The [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers) (February 2026) says it is unclear whether AI benefits attackers or defenders more.
- Human review is still needed to weed out false reports and to judge severity.
- Unpatched and unsupported legacy systems are where the outcome will be decided.

## Cruxes
1. **Can fixing keep pace with finding?** If the share of AI-found, disclosed bugs that are actually fixed stays near one in ten, the optimistic case fails on the bottleneck. *Check: Anthropic's Glasswing ledger and VulnCheck's independent tally, mid-2027.*
2. **How long do defenders keep a head start?** Restricted models like Anthropic's Claude Mythos Preview give defenders early access, but the UK AI Security Institute found open-weight models (freely downloadable ones) only [4 to 7 months behind](https://www.aisi.gov.uk/) frontier closed models on cyber tasks. *Check: UK AISI and US CAISI joint evaluations, 2027.*
3. **Does the time between disclosure and exploitation turn back in defenders' favor?** Mandiant measured it at [63 days in 2018 and an estimated minus 7 days in 2025](https://helpnetsecurity.com/2026/03/24/mandiant-m-trends-2026-report/), meaning exploitation usually starts before a patch exists. *Check: Mandiant M-Trends 2028 (covering 2027).*

## Probability estimates
**No published estimate** of the probability that defenders gain a lasting net advantage was found. The closest related numbers:

| Source | Who | Question or claim | Estimate | Date | Type |
|---|---|---|---|---|---|
| [World Economic Forum, Global Cybersecurity Outlook 2024](https://www3.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2024.pdf) | Survey of business and cyber leaders | In the next two years, will generative AI give the overall cyber advantage to attackers or defenders? | 55.9% attackers, 35.1% balanced, 8.9% defenders | Jan 2024 | Opinion survey. Two-year horizon has passed; not formally scored |
| [UK NCSC](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027) | UK government intelligence assessment | Universal access to AI for cyber defense by 2027 | "Remote chance" | May 2025 | Official assessment on a fixed probability scale. Scorable 2027 |
| Same | Same | AI will make cyber intrusion more effective, raising frequency and intensity of threats | "Almost certain" | May 2025 | Same |
| Same | Same | Critical systems become more vulnerable to advanced attackers by 2027, if defenses lag | "Realistic possibility" | May 2025 | Same, conditional |
| [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary) | International expert panel chaired by Yoshua Bengio | Whether attackers or defenders benefit more | "Remains uncertain" (no number) | Feb 2026 | Consensus assessment |

**Read these with care:** the WEF survey predates every major result on this card. The NCSC uses a standard UK intelligence probability scale in which "remote chance" is the lowest band and "almost certain" the highest.

## Evidence confidence
**Medium** that AI is now a strong tool for finding and fixing bugs: there are measured competition results, company disclosures and an independent check. **Low** for the net advantage, which nobody has measured and which depends on patching behavior across millions of organizations.

## Signposts
1. Of AI-found vulnerabilities disclosed to open-source maintainers, more than half are confirmed fixed within 90 days (VulnCheck's September 2026 count was 202 fixed against 2,096 disclosed but not confirmed fixed).
2. Mandiant's average time-to-exploit turns positive again, meaning patches usually arrive before exploitation.
3. Exploited vulnerabilities fall below 25% of initial intrusion routes in Mandiant's annual report (32% in the 2026 edition).
4. The International AI Safety Report or the UK NCSC changes its wording from "uncertain" to defenders benefiting more.
5. Counter-signpost: a confirmed, largely AI-run intrusion campaign causes physical damage or a multi-day outage at critical infrastructure.

## Evidence so far
- **DARPA AI Cyber Challenge (August 2025):** finalists [found 54 of 63 planted vulnerabilities and patched 43](https://darpa.mil/news/2025/aixcc-results) across more than 54 million lines of code, averaging 45 minutes per patch and about $152 per task. They also found 18 real, unplanted vulnerabilities. Team Atlanta (Georgia Tech, Samsung Research, KAIST, POSTECH) won $4 million; Trail of Bits was second and Theori third. All seven systems are [open source](https://archive.aicyberchallenge.com/), and second-place [Buttercup runs on a laptop](https://blog.trailofbits.com/2025/08/08/buttercup-is-now-open-source/).
- **Google Big Sleep (July 2025):** Google says its AI agent found a SQLite database flaw (CVE-2025-6965) that was ["known only to threat actors"](https://blog.google/technology/safety-security/cybersecurity-updates-summer-2025/), and called this the first time an AI agent directly foiled an exploitation attempt. Google has not published who the attackers were (company claim).
- **Google DeepMind CodeMender (October 2025):** an agent that writes fixes; it had [upstreamed 72 security fixes](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/) to open-source projects, each reviewed by human researchers first.
- **OpenAI Aardvark (October 2025):** a GPT-5-based security agent that found open-source flaws, [ten of which received official CVE identifiers](https://openai.com/index/introducing-aardvark), later folded into Codex Security.
- **Anthropic (February 2026):** Claude Opus 4.6 found and validated [more than 500 high-severity vulnerabilities](https://www.anthropic.com/research/zero-days) in open-source projects with no special setup. Anthropic warned that standard 90-day disclosure windows may not survive the volume.
- **Anthropic Project Glasswing (April 2026):** a restricted model, Claude Mythos Preview, shared with launch partners (including Apple, Google, Microsoft, CrowdStrike and the Linux Foundation) and over 40 other organizations, plus [up to $100 million in usage credits and $4 million for open-source security groups](https://www.anthropic.com/glasswing). By May 2026, partners had found [more than 10,000 high- or critical-severity vulnerabilities](https://www.anthropic.com/news/glasswing-initial-update), but only 75 of about 530 disclosed open-source bugs were patched, and several maintainers said they were "severely capacity constrained" (company figures).
- **Independent check (September 2026):** VulnCheck found [202 fixed out of 26,153 claimed findings](https://www.vulncheck.com/blog/anthropic-glasswing-receipts), and maintainers rated 51.3% of findings critical or high where Claude rated 91.5%.
- **Security copilots:** an observational study of live security operations found adopters of a generative AI assistant (Microsoft Security Copilot) [resolved incidents 30.13% faster](https://arxiv.org/abs/2411.03116) after three months; the authors caution that this shows association, not proven cause (November 2024).
- **The offense side:** in November 2025 Anthropic reported that a group it assessed as Chinese state-sponsored used Claude to perform [80 to 90% of an espionage campaign](https://www.anthropic.com/news/disrupting-AI-espionage) against about 30 targets, succeeding in a small number. An autonomous system, XBOW, [topped HackerOne's US bug-bounty leaderboard](https://xbow.com/blog/top-1-how-xbow-did-it/) in June 2025.
- **The noise problem:** the widely used curl project [ended its bug bounty in January 2026](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/) because of a flood of low-quality, often AI-generated reports (secondary).
- **The patch gap:** Verizon's 2025 breach report found only about [54% of vulnerable edge devices were fully fixed during the year](https://www.techrepublic.com/article/news-verizon-data-breach-investigations-report-2025/), with a median of 32 days (secondary).

## Existing coverage
Hacking is already illegal almost everywhere, so the question for this good scenario is whether rules push defenders to use the benefit.
- **US federal agencies:** CISA's [Binding Operational Directive 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) (June 2026) sets risk-based patch deadlines and cites AI as narrowing the time defenders have. [BOD 26-02](https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices) (February 2026) requires agencies to remove unsupported edge devices by about August 2027. Both bind federal civilian agencies only, not private companies or local utilities.
- **EU:** the Cyber Resilience Act's [duty to report actively exploited vulnerabilities began on 11 September 2026](https://www.jonesday.com/en/insights/2026/07/eu-cyber-resilience-act-24hour-reporting-duties-start-september-11-2026), with most product security requirements applying from December 2027.
- **US policy:** the July 2025 AI Action Plan proposed an AI information-sharing and analysis center and secure-by-design AI for critical infrastructure, but was described as [heavy on cyber, light on implementation](https://www.csoonline.com/article/4027604/white-house-ai-plan-heavy-on-cyber-light-on-implementation.html) (secondary). Meanwhile CISA lost roughly a third of its staff in 2025 ([Axios](https://www.axios.com/2025/06/03/cisa-staff-layoffs-resignations-trump-cuts), secondary).
- **Enforcement:** strong for US federal networks, new and untested in the EU, and largely voluntary for private-sector patching elsewhere.

## Triage (flipped for a good scenario: what's blocking it, and does removing the block need policy?)
1. **Is it blocked by law?** No. The blocks are capacity and behavior: maintainers who can't keep up, organizations that patch slowly, and old equipment nobody replaces.
2. **An action both sides accept?** **Yes.** Fund and staff the fixing side: paid triage and patching capacity for critical open-source projects, patch deadlines and end-of-support replacement for critical infrastructure beyond federal agencies, and independent oversight of who gets early access to the strongest tools. Optimists want this to turn AI's discovery speed into real security. Skeptics say patching is exactly the bottleneck. Both lists point at the same spending.
3. *(Skipped, because step 2 applies.)*

**Result: Policy, act now** on fixing capacity and patch adoption, especially for critical infrastructure and open source. **Communicate** to set realistic expectations.

**Communication note:** "AI found 10,000 bugs" is a finding count, not a security improvement. The benefit is real only when fixes reach running systems, and today most do not yet. The window in which defenders hold the best tools may be months, not years.

## Related scenarios
- Opposite in the same domain: "Cheap large-scale cyberattacks and critical-system failures" (the same capability, used by attackers).
- Interacts with: "Concentrated power or AI-enabled surveillance" (a few companies decide who gets the strongest security tools).
- Interacts with: "Loss of control over advanced AI" (advanced hacking ability is one of the capabilities that would make an uncontrolled system dangerous).
- Reduced by: "AI disappoints."

## Sources
1. UK National Cyber Security Centre, "Impact of AI on cyber threat from now to 2027," 7 May 2025. https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027
2. Anthropic, "Project Glasswing," 7 April 2026 (updated 6 October 2026). Company figures. https://www.anthropic.com/glasswing
3. The Register, "Ex-CISA head thinks AI might fix code so fast we won't need security teams," 27 October 2025 (secondary, reporting Jen Easterly's remarks). https://www.theregister.com/2025/10/27/jen_easterly_ai_cybersecurity/
4. DARPA, AI Cyber Challenge (AIxCC) final competition results announcement, 8 August 2025. https://darpa.mil/news/2025/aixcc-results
5. DARPA AIxCC archive, open-source finalist systems and competition data, 2025. https://archive.aicyberchallenge.com/
6. Adkins, Evron and Schneier, "Autonomous AI Hacking and the Future of Cybersecurity," CSO Online, October 2025 (reposted on schneier.com). https://www.schneier.com/essays/archives/2025/10/autonomous-ai-hacking-and-the-future-of-cybersecurity.html
7. VulnCheck (Patrick Garrity), "The Anthropic Glasswing Receipts Are Starting to Trickle In," 8 September 2026. https://www.vulncheck.com/blog/anthropic-glasswing-receipts
8. International AI Safety Report 2026, Extended Summary for Policymakers, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers
9. International AI Safety Report 2026, Executive Summary, 3 February 2026. https://internationalaisafetyreport.org/publication/2026-report-executive-summary
10. UK AI Security Institute, home page and cyber evaluation of open-weight models, accessed October 2026. https://www.aisi.gov.uk/
11. Help Net Security, coverage of Mandiant M-Trends 2026, 24 March 2026 (secondary). https://helpnetsecurity.com/2026/03/24/mandiant-m-trends-2026-report/
12. World Economic Forum, Global Cybersecurity Outlook 2024, January 2024. https://www3.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2024.pdf
13. Trail of Bits, "Buttercup is now open source," 8 August 2025. https://blog.trailofbits.com/2025/08/08/buttercup-is-now-open-source/
14. Google (Kent Walker), summer 2025 cybersecurity updates blog post, 15 July 2025. Company claim. https://blog.google/technology/safety-security/cybersecurity-updates-summer-2025/
15. Google DeepMind, "Introducing CodeMender: an AI agent for code security," 6 October 2025. https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
16. OpenAI, "Introducing Aardvark: OpenAI's agentic security researcher," October 2025 (updated March 2026). https://openai.com/index/introducing-aardvark
17. Anthropic Frontier Red Team, "Evaluating and mitigating the growing risk of LLM-discovered 0-days," 5 February 2026. https://www.anthropic.com/research/zero-days
18. Anthropic, "Project Glasswing: an initial update," 22 May 2026. Company figures. https://www.anthropic.com/news/glasswing-initial-update
19. Bono, Grana and Xu, "Generative AI and Security Operations Center Productivity: Evidence from Live Operations," arXiv 2411.03116, November 2024. https://arxiv.org/abs/2411.03116
20. Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign," 13 November 2025. https://www.anthropic.com/news/disrupting-AI-espionage
21. XBOW, "Top 1: how XBOW did it," company blog, June 2025. Company claim. https://xbow.com/blog/top-1-how-xbow-did-it/
22. The Register, "Curl shutters bug bounty program to remove incentive for submitting AI slop," 21 January 2026 (secondary). https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/
23. TechRepublic, coverage of the Verizon 2025 Data Breach Investigations Report, April 2025 (secondary). https://www.techrepublic.com/article/news-verizon-data-breach-investigations-report-2025/
24. CISA, Binding Operational Directive 26-04, "Prioritizing Security Updates Based on Risk," 10 June 2026. https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
25. CISA, Binding Operational Directive 26-02, "Mitigating Risk From End-of-Support Edge Devices," 5 February 2026. https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices
26. Jones Day, "EU Cyber Resilience Act: 24-Hour Reporting Duties Start September 11, 2026," July 2026 (secondary, law firm summary). https://www.jonesday.com/en/insights/2026/07/eu-cyber-resilience-act-24hour-reporting-duties-start-september-11-2026
27. CSO Online, "White House AI plan heavy on cyber, light on implementation," July 2025 (secondary). https://www.csoonline.com/article/4027604/white-house-ai-plan-heavy-on-cyber-light-on-implementation.html
28. Axios, "One-third of top U.S. cyber force has left since Trump took office," 3 June 2025 (secondary). https://www.axios.com/2025/06/03/cisa-staff-layoffs-resignations-trump-cuts

## Sign-off record
- Optimistic case: not yet reviewed.
- Worried case: not yet reviewed.
- Changelog: 2026-10-09 first draft.
