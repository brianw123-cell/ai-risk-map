# Prior art: catalogs, repositories and assessments of AI risks and outcomes

Research date: 9 October 2026. Figures are dated where the source gives a date. Where a figure came from a secondary summary rather than the primary source, that is flagged.

## 1. MIT AI Risk Repository (MIT FutureTech / MIT AI Risk Initiative): structure, size, cadence, coding, and reuse as a backbone

### Takeaway
It is the largest open, coded catalog of AI risks (about 1,700+ risks from 65 to 74 frameworks, CC BY 4.0), with a two-axis taxonomy that could serve as the "risk side" backbone of a scenario map. It is a catalog of risks extracted from other people's papers, not a set of scenarios: it has no positive outcomes, no probabilities, no debate between sides, and no policy triage.

### Cited Findings
- Paper: Slattery, Saeri, Grundy and others, "The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks From Artificial Intelligence," arXiv 2408.12622. Authors from MIT FutureTech, the University of Queensland and other institutions. [arXiv](https://www.arxiv.org/pdf/2408.12622)
- Latest arXiv version is v3 (5 May 2026); the abstract now says "74 frameworks containing 1,725 distinct risks." Published in the journal Patterns (Cell Press), 2026, article 101517, under CC BY 4.0. [arXiv abstract page](https://arxiv.org/abs/2408.12622)
- Growth over time: first version (Aug 2024) described 777 risks from 43 taxonomies; a later version described 1,612 risks from 65 taxonomies. [arXiv](https://www.arxiv.org/pdf/2408.12622v1); [MIT FutureTech publication page](https://futuretech.mit.edu/publication/the-ai-risk-repository)
- The project site (as of Oct 2026) headlines "1,700+ AI risks from 65 frameworks." Note the mismatch with the paper's 74 frameworks; the site counter may lag the paper. [airisk.mit.edu](https://airisk.mit.edu/)
- Update history on the site: April 2025 update added 9 frameworks and about 600 risk entries, plus a multi-agent risks subdomain; Version 4 of the repository announced in a December 2025 post. [airisk.mit.edu](https://airisk.mit.edu/)
- Causal taxonomy codes each risk on three factors: entity (human or AI), intentionality (intentional or unintentional), timing (pre-deployment or post-deployment), with "other" options added in later versions for ambiguous cases. [arXiv](https://www.arxiv.org/pdf/2408.12622)
- Domain taxonomy has 7 domains: discrimination and toxicity; privacy and security; misinformation; malicious actors and misuse; human-computer interaction; socioeconomic and environmental harms; AI system safety, failures and limitations. Original version had 23 subdomains; later versions have 24 after a multi-agent subdomain was added. The 23 vs 24 count comes from a search-summary comparison of versions, not a direct read of the current paper. [arXiv](https://www.arxiv.org/pdf/2408.12622); [LongtermWiki entry](https://www.longtermwiki.com/knowledge-base/responses/epistemic-tools/tools/mit-ai-risk-repository)
- Data license is CC BY 4.0. Site is credited to MIT FutureTech; run by the MIT AI Risk Initiative. Funding is not stated on the site. [airisk.mit.edu](https://airisk.mit.edu/)
- Companion datasets launched 2025 to 2026: an AI Risk Mitigation Database and a draft Mitigation Taxonomy (13 frameworks); a governance mapping that in April 2026 classified over 1,000 documents from CSET's AGORA archive using LLMs; an Incident Tracker (major update 23 June 2025, June 2026 pilot comparing eight LLMs against expert reviewers); a "Navigator" tool linking datasets through shared taxonomies; FLARE-AI, an open-source flaw and incident reporting system; and an expert survey of 272 international AI experts ranking risks by severity, responsibility and vulnerability. [airisk.mit.edu](https://airisk.mit.edu/)
- The AI Incident Database already applies the MIT taxonomy to incidents, so the two datasets are cross-linked. [AIID MIT taxonomy page](https://incidentdatabase.ai/taxonomies/mit)

### Inferences
- Reusable as a backbone: yes, for the harms half. The CC BY 4.0 license allows reuse with attribution, and the 7-domain list is a sensible top-level menu for "bad" scenarios. Each scenario on the map could carry a pointer to the MIT domain and subdomain codes, which makes the map instantly interoperable with MIT's risk, mitigation, governance and incident datasets.
- What it does not do relative to the scenario-map concept: (a) the unit is a "risk statement" pulled from a document, not a coherent future scenario; (b) no positive or beneficial outcomes; (c) no "worried vs optimistic" framing or quoted case from each side; (d) no probability per risk (the 272-expert survey ranks severity, not likelihood); (e) no triage into policy response vs public communication, although the governance mapping gets partly toward "what policy already covers this."
- The sheer size (1,700+ entries) is the opposite of the "finite map" goal. A scenario map would need to cluster these into perhaps 20 to 40 scenarios, which is itself a contribution.

### Gaps
- I could not confirm the exact current subdomain list or count from the primary paper text.
- Funding sources for the MIT AI Risk Initiative were not found.
- Results and method of the 272-expert severity survey were not reviewed in detail.

## 2. AI Incident Database (Responsible AI Collaborative) and OECD AI Incidents and Hazards Monitor (AIM)

### Takeaway
Both track harms that have already happened (and, for OECD, "hazards" that nearly happened), so they are the evidence layer, not a scenario layer. They are useful for showing "this scenario has already started" with real examples, but neither looks forward, offers probabilities, presents positive outcomes, or pairs opposing views.

### Cited Findings
AI Incident Database (AIID)
- Describes itself as "dedicated to indexing the collective history of harms or near harms realized in the real world" by AI deployment. Run by the Responsible AI Collaborative, "an organization chartered to advance the AI Incident Database." [incidentdatabase.ai](https://incidentdatabase.ai/)
- Size: the most recent incident IDs are 1731 to 1733, dated 7 October 2026. The homepage gives no total count; incident IDs suggest roughly 1,700+ incidents, each grouping multiple news reports. [incidentdatabase.ai](https://incidentdatabase.ai/)
- Funding: founding sponsors listed are the WU Foundation (organization) and Partnership on AI (database), plus other grants and in-kind sponsors (Netlify, Cloudinary, Algolia). [incidentdatabase.ai](https://incidentdatabase.ai/)
- Definition: no fixed definition. Inclusion follows "a growing rule set defined in the Editor's Guide," borrowing from aviation, where an incident is a case in which "the risk of an accident substantially increases." [AIID criteria page](https://incidentdatabase.ai/research/1-criteria/)
- Classification: incidents are tagged with multiple taxonomies, including the MIT AI Risk Repository taxonomy. [AIID MIT taxonomy](https://incidentdatabase.ai/taxonomies/mit)
- License: not stated on the pages reviewed; a full-database download page and terms of use exist. [AIID criteria page](https://incidentdatabase.ai/research/1-criteria/)

OECD AI Incidents and Hazards Monitor (AIM)
- AI incident: an event where the development, use or malfunction of an AI system results in actual harm. AI hazard: an event that "could plausibly lead to an AI incident." Four harm categories: health; critical infrastructure; human, labour or IP rights; property, communities or environment. [OECD AIM methodology](https://oecd.ai/en/incidents-methodology)
- Severity ladder from the 2024 OECD definitions paper: incident, serious incident (death, serious health harm, irreversible infrastructure disruption, serious rights violations), and "AI disaster" (a serious incident that disrupts a community's or society's functioning). [OECD.AI Wonk blog](https://oecd.ai/en/wonk/defining-ai-incidents-and-hazards); [techUK summary](https://www.techuk.org/insights/news/oecd-incident-report-definitions-for-ai-incidents-and-related-terms)
- Data source: Event Registry, a news platform processing over 150,000 articles a day; LLMs classify AI-tagged events as incident, hazard, or unrelated. Fields per entry include title, summary, harm type, severity, affected stakeholders, country, and industry/sector. Runs daily. [OECD AIM methodology](https://oecd.ai/en/incidents-methodology)
- Volume: the methodology page gives conflicting figures, about 10 per day in one section and about 30 per day in another. [OECD AIM methodology](https://oecd.ai/en/incidents-methodology)
- Reuse: no open license stated; points to OECD general terms and conditions. [OECD AIM methodology](https://oecd.ai/en/incidents-methodology)
- Planned additions include an open submission process and court rulings / regulator decisions. [OECD AIM methodology, via search summary](https://oecd.ai/incidents-methodology)
- A 2026 arXiv paper proposes "a pragmatic classification framework for AI incident monitoring," indicating the classification approach is still evolving. [arXiv 2604.21412](https://arxiv.org/pdf/2604.21412)

Derivative project worth knowing
- GLOBAÏA's "AI Risks" project ("Mapping AI's costs, failures, and governance") curates 147 representative incidents since 2015 drawn from AIM and AIID, using OECD definitions and seven harm types. It has no scenarios, probabilities, positive outcomes or counter-views. [GLOBAÏA incident record](https://globaia.org/ai-risks/incidents/)

### Inferences
- The OECD "hazard" concept is the closest thing in these databases to a forward-looking scenario: it names plausible paths to harm. A scenario map could link each scenario to (a) matching past incidents and (b) matching hazards as "early warning signs."
- The OECD severity ladder (incident, serious incident, disaster) is a ready-made, government-backed scale the map could borrow for "how bad is the bad version."
- Neither database is a competitor; both are feeders. AIID's taxonomy cross-tagging with MIT means a map keyed to MIT codes gets incident links nearly for free.

### Gaps
- Exact total counts for AIID and AIM as of October 2026 were not found on the pages reviewed.
- AIID data license terms were not confirmed.

## 3. International AI Safety Report (2025, 2026 and Key Updates; chair Yoshua Bengio)

### Takeaway
This is the closest thing AI has to an IPCC-style assessment: 100+ experts, a 30+ country advisory panel, a summary for policymakers, and an explicit three-bucket risk scheme (misuse, malfunctions, systemic). It openly describes disagreement but does not give probabilities, does not cover benefits as scenarios, does not quote sides in their own words, and deliberately makes no policy recommendations.

### Cited Findings
- 2026 edition published 3 February 2026; over 100 independent experts; Expert Advisory Panel with representatives nominated by over 30 countries plus the EU, OECD and UN. [Extended Summary for Policymakers 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)
- First full report was published in January 2025; the 2026 report covers "notable developments since the publication of the first." [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)
- Formats: a three-page Executive Summary, an Extended Summary for Policymakers, and the full report. Organized around three questions: what can general-purpose AI do today, what emerging risks does it pose, and how can those risks be mitigated. [casrai.org guide](https://casrai.org/guides/international-ai-safety-report-2026); [official site](https://internationalaisafetyreport.org/)
- Risk categories and risks in the 2026 edition:
  - Misuse: AI-generated content and crime (scams, fraud, blackmail, extortion, defamation, non-consensual intimate imagery, child sexual abuse material); influence and manipulation; cyberattacks; biological and chemical risks.
  - Malfunctions: reliability problems (false information, flawed code, misleading medical advice) and loss of control.
  - Systemic: labour market impacts; risks to human autonomy (over-reliance, skill erosion, AI companions).
  [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)
- How it handles disagreement: names an "evidence dilemma" (acting on thin evidence risks bad policy; waiting risks exposure); says there is "substantial uncertainty" about the pace of progress; says researchers' views on loss of control "vary widely"; economists disagree on the size of labour market effects; whether AI favors attackers or defenders is an open question. A disclaimer says it does not necessarily reflect the views of the Chair, individual contributors or governments. [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)
- No policy recommendations: the report "does not recommend any policies." No probability estimates for risks; the percentages in it are benchmark results. [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)
- Interim "Key Updates": first on 15 October 2025 (capabilities and risk implications, e.g. leading systems completing over 60% of a real-world software engineering task set, up from about 40% at start of 2025); second on 25 November 2025 (technical safeguards and risk management, noting sophisticated attackers can often bypass current defenses). [Official Key Update page](https://internationalaisafetyreport.org/publication/first-key-update-capabilities-and-risk-implications); [Princeton CITP](https://citp.princeton.edu/news/2025/international-ai-safety-report-first-key-update-capabilities-and-risk-implications); [Australian Govt, second Key Update](https://www.industry.gov.au/publications/second-key-update-technical-safeguards-and-risk-management); [arXiv 2511.19863](https://arxiv.org/abs/2511.19863v1)
- License: Open Government Licence v3.0 except where otherwise stated; Crown copyright 2026; series number DSIT 2026/001 (the UK Department for Science, Innovation and Technology publishes it). [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)

### Inferences
- The three-bucket split (misuse, malfunction, systemic) is a strong candidate for the map's top-level grouping of bad scenarios because it is the internationally negotiated vocabulary governments already use.
- The report's choice to give no probabilities and no recommendations is the gap the scenario map would fill: probabilities "where they exist" and a policy-vs-communication triage. That also means the map would be making judgments the leading official assessment intentionally avoided, so it needs to be transparent about whose numbers and whose triage.
- The OGL v3.0 license allows reuse of the report's text with attribution, so the map could quote its summary language directly for each scenario's "state of evidence."

### Gaps
- I did not read the full 2026 report, so chapter-level structure and any section on benefits were not confirmed.
- No 2026 Key Updates (after February 2026) were found in this search; there may be some.

## 4. IPCC methodology as a model (SSPs, calibrated language, disagreement, SPM approval)

### Takeaway
The IPCC offers three transferable tools: a small set of named, contrasting future storylines (the five SSPs); a standard vocabulary for likelihood and confidence; and a line-by-line government approval process for the policymaker summary. The storylines and the calibrated vocabulary transfer well to an AI scenario map; the government approval process does not fit a non-specialist public project.

### Cited Findings
Shared Socioeconomic Pathways (SSPs)
- Five narratives "intended to span the range of plausible futures," first published in 2016, used in the CMIP6 modelling round. [Carbon Brief explainer](https://www.carbonbrief.org/explainer-how-shared-socioeconomic-pathways-explore-future-climate-change/)
- They are arranged on two axes, challenges to mitigation and challenges to adaptation. SSP1 "Sustainability, taking the green road" (low challenges on both); SSP5 "Fossil-fueled development, taking the highway" (high mitigation challenge, low adaptation challenge). Both SSP1 and SSP5 are relatively optimistic about human development; they differ mainly on energy path. [Carbon Brief explainer](https://www.carbonbrief.org/explainer-how-shared-socioeconomic-pathways-explore-future-climate-change/)
- The SSPs are baselines of how the world looks without climate policy, which lets researchers test policy against them. [Carbon Brief explainer](https://www.carbonbrief.org/explainer-how-shared-socioeconomic-pathways-explore-future-climate-change/)
- Our World in Data offers an interactive explorer of IPCC scenarios, an example of public-facing presentation. [Our World in Data](https://ourworldindata.org/explorers/ipcc-scenarios)

Calibrated uncertainty language
- The AR5 Guidance Note on Consistent Treatment of Uncertainties (Mastrandrea et al.) was finalized November 2010 and accepted by the IPCC in May 2011; published as a paper in Climatic Change 108(4):675-691 (2011). [IPCC guidance note PDF](https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf); [Springer](https://link.springer.com/article/10.1007/s10584-011-0178-6)
- Two separate metrics: confidence (very low, low, medium, high, very high), based on type, amount, quality and consistency of evidence plus degree of agreement; and likelihood, a probability, used only where evidence allows quantification. [IPCC guidance note PDF](https://www.ipcc.ch/site/assets/uploads/2018/05/uncertainty-guidance-note.pdf); [Springer](https://link.springer.com/article/10.1007/s10584-011-0178-6)
- AR6 likelihood terms: virtually certain 99 to 100%; extremely likely 95 to 100%; very likely 90 to 100%; likely 66 to 100%; more likely than not over 50%; about as likely as not 33 to 66%; unlikely 0 to 33%; very unlikely 0 to 10%; extremely unlikely 0 to 5%; exceptionally unlikely 0 to 1%. Calibrated terms are printed in italics. [IPCC AR6 WGI SPM draft](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_FOD_SPM.pdf); [Carbon Brief comparison](https://www.carbonbrief.org/ipcc-how-the-ar6-wg1-summary-for-policymakers-compares-to-its-predecessor); [Energy Education](https://energyeducation.ca/encyclopedia/Likelihood)
- The note urges authors to report on low-probability, high-impact tails (large magnitude, persistence, irreversibility). [Springer](https://link.springer.com/article/10.1007/s10584-011-0178-6)
- Known weaknesses: a 2022 Climatic Change article says the note is unclear about how to combine evidence and agreement into confidence levels. [White Rose eprint](https://eprints.whiterose.ac.uk/190055/1/s10584-022-03382-3.pdf)

Summary for Policymakers (SPM) process
- The SPM is approved line by line by government delegates in dialogue with authors; scientists are present to keep it consistent with the underlying report. Underlying chapters are only "accepted" (no line-by-line negotiation); the Synthesis Report is "adopted" section by section. [IPCC fact sheet](https://www.ipcc.ch/site/assets/uploads/2024/04/IPCCFactSheet_ApproveReports.pdf); [IPCC press release](https://www.ipcc.ch/2022/02/14/press-release-wgii-ar6-opening/)
- Criticism: Robert Stavins (AR5 lead author) described roughly 2,000 pages condensed to a 33-page SPM, with colleagues joking it was a "Summary by Policymakers." One participant's view. [Resources for the Future blog](https://www.resources.org/common-resources/is-the-ipcc-government-approval-process-broken/)

### Inferences
- What transfers to AI: (1) a handful of named storylines with plain-English nicknames, arranged on two axes, that span the plausible range including good futures (SSP1 is a good future); (2) the two-scale vocabulary, so every scenario can say "likely (66 to 100%), medium confidence" and readers learn the code once; (3) the rule that probabilities appear only where evidence supports them, which matches the "probabilities where they exist" design goal.
- What does not transfer: the government line-by-line approval needs a treaty body. A lightweight analogue would be a published review step where named people from both sides sign off that their side's case is fairly stated.
- Climate has physical models that produce probabilities; AI mostly has expert judgment and forecasting markets. The map should label AI probabilities as "expert/forecaster judgment" to avoid borrowing more authority than the numbers deserve.

### Gaps
- I could not open the IPCC guidance note PDFs directly (403 errors); the likelihood table above is confirmed via the AR6 SPM draft and secondary tables, not the note itself.
- IPCC procedures for recording minority views in chapters were not researched.

## 5. Other notable risk taxonomies and catalogs

### Takeaway
There are several well-known lists, each organized around harms from a single vantage point (a lab, a standards body, a regulator, a safety nonprofit). None covers benefits, none pairs both sides, and only the EU AI Act sorts things by required response, though that is legal compliance tiers, not public scenarios.

### Cited Findings
- Google DeepMind, Weidinger et al. (2021), "Ethical and social risks of harm from Language Models": 6 risk areas, 21 risks: discrimination, exclusion and toxicity; information hazards; misinformation harms; malicious uses; human-computer interaction harms; automation, access and environmental harms. [arXiv 2112.04359](https://arxiv.org/pdf/2112.04359); [DeepMind blog](https://deepmind.google/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/)
- Center for AI Safety, Hendrycks et al. (2023), "An Overview of Catastrophic AI Risks": 4 categories: malicious use, AI race, organizational risks, rogue AIs. MIT's summary maps these to intentional, environmental/structural, accidental and internal causes. [arXiv 2306.12001](https://arxiv.org/pdf/2306.12001); [MIT AI Risk blog](https://airisk.mit.edu/blog/an-overview-of-catastrophic-ai-risks)
- NIST AI 600-1, Generative AI Profile (July 2024): 12 risks "unique to or exacerbated by" generative AI, limited to risks with an existing empirical basis: CBRN information or capabilities; confabulation; dangerous, violent or hateful content; data privacy; environmental; human-AI configuration; information integrity; information security; intellectual property; obscene, degrading or abusive content; value chain and component integration; harmful bias and homogenization. Items 8 to 12 were supplied by the search tool from background knowledge and should be checked against the final NIST text. [NIST draft PDF](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf); [Modulos summary](https://docs.modulos.ai/frameworks/nist-ai-rmf/generative-ai-profile)
- EU AI Act risk tiers: unacceptable (banned, e.g. social scoring, emotion recognition at work or school); high (allowed with mandatory risk management, human oversight, documentation, registration; areas include employment, education, law enforcement, critical infrastructure, healthcare); limited (transparency duties, e.g. chatbots must disclose); minimal (spam filters, few rules). Classification turns on intended purpose, not the technology. Prohibitions applied from 2 February 2025; fines up to 7% of global turnover or EUR 35 million. Secondary sources only. [Forvis Mazars](https://forvismazars.com/ie/en/insights/news-opinions/eu-ai-act-different-risk-levels-of-ai-systems); [Ethyca](https://www.ethyca.com/the-eu-artificial-intelligence-act-ai-act)

### Inferences
- These lists overlap heavily and MIT has already absorbed most of them (DeepMind and CAIS are both among MIT's source frameworks, judging by MIT's blog coverage). The map does not need to reconcile them separately; the MIT codes do that.
- The EU AI Act is the only scheme that ties categories to a required response, which is a useful precedent for the map's triage column. But its tiers are about AI products and uses, not society-wide futures, so it cannot be copied directly.
- The CAIS "AI race" category and the International AI Safety Report's "systemic" category are where the most contested scenarios sit (economic disruption, concentration of power). These are exactly where a "both sides" format adds the most.

### Gaps
- UK AI Security Institute (AISI) publications, the Stanford AI Index, and the EU's "general-purpose AI with systemic risk" category were not researched in this pass.
- The official EU Commission AI Act page was not retrieved; tier descriptions rest on secondary sources.

## 6. Does anything already pair worried and optimistic views per scenario?

### Takeaway
I found nothing that does it systematically per scenario. The closest prior art is (a) the Forecasting Research Institute's Existential Risk Persuasion Tournament, which put probabilities from AI experts and superforecasters side by side after structured debate, and (b) the November 2025 joint essay by the "AI 2027" and "AI as Normal Technology" authors, which maps agreements and disagreements between two worldviews. Both cover one or two questions, not a full catalog.

### Cited Findings
- Existential Risk Persuasion Tournament (XPT), run June to October 2022 by the Forecasting Research Institute: 169 participants (89 superforecasters, 80 domain experts). Process: anonymous initial forecasts, public reasoning, adversarial collaboration with people who disagreed, then updates. [Freethink](https://www.freethink.com/robots-ai/ai-predictions-superforecasters?amp=1)
- XPT results: AI-caused extinction by 2100, experts median 3% vs superforecasters 0.38%; AI catastrophe (at least 10% of humans die within 5 years), experts 12% vs superforecasters 2.13%. [Freethink](https://www.freethink.com/robots-ai/ai-predictions-superforecasters?amp=1)
- Secondary reporting says the XPT was later published in the International Journal of Forecasting (2025) and found minimal convergence after four months of debate; not verified against the paper. [LongtermWiki XPT entry](https://www.longtermwiki.com/knowledge-base/responses/epistemic-tools/tools/xpt)
- "Common Ground between AI 2027 & AI as Normal Technology" (Asterisk, November 2025): the authors of the two opposing essays agree that before strong AGI, AI behaves mostly like a normal tool; that benchmarks are a poor proxy for real-world automation; and on governance priorities such as transparency, independent auditing, and preventing unmonitored recursive self-improvement. [Asterisk Magazine](https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and)
- The Normal Technology authors also publish a guide that directly compares the two worldviews. [normaltech.ai](https://www.normaltech.ai/i/173147197/concluding-thoughts)
- Commentators frame the split as a difference in worldview more than in concrete predictions, with "diffusion" (whether capability automatically becomes power) as the main crux. [AI Risks Substack](https://airisks.substack.com/p/on-different-worldviews-7c8)
- The International AI Safety Report describes disagreement (e.g. loss-of-control views "vary widely") but in its own neutral voice, not in each side's words. [Extended Summary 2026](https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers)

### Inferences
- The "both sides in their own words, per scenario" format appears to be genuinely unoccupied. That is the project's clearest point of difference.
- The XPT shows the main risk of the format: even after months of structured debate, the two groups barely moved. The map should present disagreement as stable and explain the crux, not promise convergence.
- The "Common Ground" essay is a good template for a scenario entry: what both sides agree on, where they split, and the single question that would settle it.
- A useful framing for the map's identity: MIT and OECD supply the risk inventory and evidence; the International AI Safety Report supplies the neutral state of evidence; XPT-style forecasts supply probabilities; the scenario map would be the first to put each side's case, the numbers, and a triage recommendation on one card per scenario, including the good futures.

### Gaps
- I did not search prediction platforms (Metaculus, Manifold) or debate platforms (e.g. Kialo) for per-scenario pro/con structures; these may hold partial prior art.
- I did not find any catalog of positive AI scenarios comparable in rigor to the risk catalogs; this was not searched for directly and is worth a dedicated pass.
