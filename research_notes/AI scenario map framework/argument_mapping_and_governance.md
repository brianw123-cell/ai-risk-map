# Methods for fair representation, structure, and anti-capture governance of a public AI scenario map

Research notes, current as of 9 October 2026. Written for a non-specialist. Every factual claim carries a link. Anything labelled "Inference" is the researcher's reasoning, not a sourced fact.

Note on scope: Emad Mostaque's proposal on the Moonshots podcast (7 Oct 2026) was not independently checked here; these notes take the brief's description of it as given.

## 1. Argument-mapping tools and formats: what works for a lay audience?

### Takeaway
Pro/con trees (Kialo, ProCon.org) and plain-text argument maps (Argdown) give structure, but open voting on how strong an argument is gives little useful signal. Live debate formats show audiences can shift, but the results are noisy and depend on performance. For a lay audience the format that works best is a short, curated pro/con layout with named sources. Open-ended trees that keep branching do not.

### Cited Findings
- Kialo is a structured debate platform built as a tree: a thesis at the top, with pro and con claims underneath, and each claim can have its own pros and cons beneath it — [Wikipedia: Kialo](https://en.wikipedia.org/wiki/Kialo)
- Kialo's "Perspectives" feature shows how supporters and opponents of a thesis, moderators and individual contributors each rated the "Impact" of an argument — [Wikipedia: Kialo](https://en.wikipedia.org/wiki/Kialo)
- An informal user critique (an opinion, not a study) said there is "not much signal" in Kialo's impact voting. The same user said Kialo helps beginners find their way around an argument but is unreliable for actually understanding one — [EA Forum answer on argument mapping](https://ea.greaterwrong.com/posts/HmYfoKW6FuyFHmwcJ/why-is-argument-mapping-not-more-common-in-ea-rationality/answer/9FdPRr45LNtMWJipX)
- Argdown is a Markdown-style plain-text syntax, created in 2014, for writing argument structures. It exports pro/con lists and graph-style argument maps — [Argdown syntax docs](https://argdown.org/syntax/); [Argdown first example](https://argdown.org/guide/a-first-example); [PLDB: Argdown](https://pldb.io/concepts/argdown.html)
- Argdown is maintained in connection with the DebateLab at KIT (Karlsruhe Institute of Technology), which works on computational argument analysis — [DebateLab KIT](https://debatelab.philosophie.kit.edu/26_104.php)
- ProCon.org presents "sourced pros and cons of debatable issues", compiled by research staff and editors, and says it takes no positions on its topics. It has been owned by Encyclopaedia Britannica since 29 May 2020 — [ProCon FAQ (archived URL, now redirects to Britannica)](https://www.procon.org/faqs/); [Wikipedia: ProCon.org](https://en.wikipedia.org/wiki/ProCon.org)
- ProCon admits that even layout choices can be read as political signals. For example, it explains that pros go on the left only because "pro-con" is the usual word order — [ProCon FAQ](https://www.procon.org/faqs/)
- Outside reviewers rate ProCon well: Common Sense Education calls it "meticulously sourced and cited", and Media Bias/Fact Check rates it "least biased" — [Common Sense Education](https://www.commonsense.org/education/reviews/proconorg); [Media Bias/Fact Check](https://mediabiasfactcheck.com/procon-org/)
- Munk Debate on AI (Toronto, 22 June 2023). The motion was "AI research and development poses an existential threat", with Bengio and Tegmark for it and LeCun and Mitchell against. Before the debate 67% of the audience favoured the motion and 92% said they were open to changing their minds. A commentator reported a closing vote of 61/39, but the voting system reportedly failed and votes were collected afterwards by email, so the shift may be noise — [GreaterWrong post on the Munk debate](https://www.greaterwrong.com/posts/CA7iLZHNT5xbLK59Y/did-bengio-and-tegmark-lose-a-debate-about-ai-x-risk-against)
- The same commentator, who leans toward taking AI risk seriously, felt the side with weaker arguments "came across quite convincing". That is an opinion, but it shows that debate formats reward performance — [GreaterWrong post](https://www.greaterwrong.com/posts/CA7iLZHNT5xbLK59Y)

### Inferences
- Design pattern: use a fixed, shallow template for each scenario. That means a one-line scenario statement, then "the worried case" and "the optimistic case" (each a few bullets plus a quote), then "where they actually disagree" (the cruxes), then probabilities if they exist, then a triage tag. ProCon's fixed two-column layout is the closest working model for a lay reader. Kialo's open, unlimited tree is better suited to back-office drafting.
- Design pattern: write the map in a plain-text structured format such as Argdown, YAML or Markdown, and keep it under version control. Then every change can be compared line by line, and anyone can fork or audit the map.
- Avoid crowd "impact" voting on argument strength on the public site. It gives a weak signal and invites brigading (see section 2).
- Avoid debate-style "who won" scoring. Audience votes measure persuasion and performance, not whether a claim is true.

### Gaps
- I found no rigorous user study comparing Kialo-style trees with flat pro/con layouts for lay comprehension.
- I could not access ProCon's current methodology page (Britannica returned 403), so I could not confirm its rules for verbatim quoting or source credibility ratings.
- Intelligence Squared's audience-shift scoring method was not researched in detail.

## 2. Bridging-based and consensus-finding systems: how they surface agreement and resist brigading

### Takeaway
Polis and Community Notes both count agreement only when it comes from people who normally disagree. This "bridging" rule is the strongest known defence against one camp taking over. Both systems can still be gamed by coordinated accounts. Both also rely on judgement calls by moderators that are rarely disclosed. Deliberative polls give higher-quality input, but they are expensive.

### Cited Findings
**Polis / vTaiwan**
- In Polis, participants write short statements (under 140 characters) and vote agree, disagree or pass on statements written by others. An algorithm sorts participants into opinion clusters and picks out "consensus statements" that all the clusters agree on, along with divisive statements — [Computational Democracy Project: Polis](https://compdemocracy.org/Polis/)
- Polis has no reply button. Audrey Tang has argued that this leaves "no room for troll to grow", because anyone who disagrees has to post a separate, standalone statement — [Audrey Tang speech transcript](https://archive.tw/speech/433959); [Scrapbox summary of Tang interview](https://scrapbox.io/nishio-en/How_the_discussion_on_Uber_has_evolved_in_vTaiwan)
- vTaiwan Uber case (2015): about 3,000 participants took part over four weeks. The points of consensus they produced set the agenda for a live-streamed stakeholder meeting, and the process later fed into regulation. Because Polis shows how each group views other groups' statements, people were pushed to write statements with broader appeal — [Shareable](https://www.shareable.net/open-data-hactivists-help-taipei-craft-regulatory-response-to-uber/); [Scrapbox summary](https://scrapbox.io/nishio-en/How_the_discussion_on_Uber_has_evolved_in_vTaiwan); [Taiwan News](https://www.taiwannews.com.tw/en/news/6245845)
- Tang says vTaiwan asked about concrete cases rather than broad ideological questions. On Uber, that meant asking about the specific service rather than "extractive economy versus sharing economy" — [Audrey Tang speech](https://archive.tw/speech/617989)
- Caveat: most of the vTaiwan detail comes from Tang's own accounts. I found no independent evaluation of whether the no-reply design actually reduced trolling — [search notes; Tang speeches above](https://archive.tw/speech/635516)

**Anthropic + CIP Collective Constitutional AI (2023)**
- About 1,000 representative US adults, recruited via PureSpectrum, submitted 1,127 statements and cast 38,252 votes on Polis. Polis found two opinion groups — [Anthropic: Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)
- CIP moderated alone against predefined criteria, removing hateful, duplicate, irrelevant and infeasible statements. That left 275 statements. The authors admit some removals were subjective and that "reasonable people can disagree" — [Anthropic: CCAI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)
- A statement was kept only if it passed a consensus threshold within both opinion groups. Statements that split the groups were dropped. For example, "prioritize the collective/common good over individual rights" and "prioritize individual liberty over collective welfare" were both excluded — [Anthropic: CCAI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)
- Turning public statements into usable principles took subjective mapping and merging. The authors say they are "not sure" they got the balance right between faithfulness to the public and technical usefulness — [Anthropic: CCAI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)

**Community Notes bridging algorithm**
- Community Notes uses matrix factorization: predicted rating = global baseline + rater term + note term + (rater viewpoint factor x note viewpoint factor). If a note is liked by only one camp, the viewpoint term "explains away" its ratings and its helpfulness score (the note intercept) stays low. A note is shown publicly only if that intercept is at least about 0.40 — [Wojcik et al., Birdwatch paper](https://arxiv.org/pdf/2210.15723); [COMMUNITYNOTES dataset paper](https://arxiv.org/pdf/2510.24810)
- The viewpoint factor is learned from rating patterns. It is not trained on any political dataset, and it need not line up with left versus right — [GreaterWrong explainer](https://www.greaterwrong.com/posts/sx9wTyCp5kgy8xGac/community-notes-by-x)
- The general idea of "bridging-based ranking", which rewards content that people across divides agree on, is set out in Ovadya and Thorburn's paper on bridging systems — [Bridging Systems (arXiv 2301.09976)](https://arxiv.org/pdf/2301.09976)
- Known weaknesses: a 2025 simulation study found that more than 40% of genuinely helpful notes go unpublished, and that a coordinated 5 to 20% of bad raters can strategically suppress targeted helpful notes — [Truong et al., "Community Notes are Vulnerable to Rater Bias and Manipulation"](https://arxiv.org/pdf/2511.02615)
- A 2026 paper reports that adversaries who place accounts strategically across the viewpoint space can fake consensus: up to 10.7% of lower-quality notes could be pushed over the threshold with fewer than 10 ratings. It also describes a "population sample filtering" mitigation deployed on X. (The arXiv date on this paper looks unusual, so verify before relying on it) — [Gaming Consensus (arXiv 2607.01824)](https://arxiv.org/pdf/2607.01824)
- Facebook and TikTok have adopted versions of the same Community Notes algorithm in the US — [Truong et al.](https://arxiv.org/html/2511.02615v1)

**Collective Intelligence Project (CIP)**
- CIP ran "alignment assemblies" in 2023 and 2024 with OpenAI, Anthropic and the UK AI Safety Institute, all of whom committed to taking public input into account — [CIP 2024 site](https://2024.cip.org/)
- CIP's "Global Dialogues" collects values and preferences from around the world to inform model development and policy. In 2024 it engaged about 1,200 participants across 68 countries. The data is released through a "Global Dialogues Challenge", and CIP works with Prolific and Remesh — [CIP Global Dialogues](https://www.cip.org/global-dialogues); [CIP 2024 Annual Report](https://2024.cip.org/2024_Annual_Report_CIP.pdf); [Prolific case study](https://www.prolific.com/resources/how-the-collective-intelligence-project-is-democratizing-ai-development-with-global-human-perspectives)

**Deliberative polling (Stanford Deliberative Democracy Lab)**
- In 2023, Meta's Community Forum with Stanford engaged 1,545 participants in scientific samples from Brazil, Germany, Spain and the US. An October 2024 forum on AI agents involved about 1,000 people from India, Turkey, Nigeria, Saudi Arabia and South Africa — [Stanford FSI: second forum results](https://fsi.stanford.edu/node/37677); [Stanford FSI: Meta Community Forum results](https://fsi.stanford.edu/node/36099)
- Findings from the 2024 forum included conditional support for AI agents remembering past conversations, but only with transparency and user controls, and a preference for culturally tailored agents — [Stanford FSI](https://fsi.stanford.edu/node/37677)
- An industry-wide deliberative forum on AI agents was planned for fall 2025, with Cohere, Meta, Oracle and PayPal taking part and CIP advising. I found no published results — [Stanford FSI: industry-wide forum](https://fsi.stanford.edu/node/38009)

### Inferences
- Design pattern, "bridged agreement" badges: for each scenario, ask a balanced panel of worried and optimistic raters to vote on short statements, Polis-style. Show only statements that both camps endorse as "common ground". This is the clearest existing defence against one side capturing the map. Polis already supports it out of the box.
- Design pattern, no replies: use agree/disagree/pass plus "write your own statement", not comment threads. Threads invite pile-ons.
- Design pattern, disclose moderation: CCAI shows that moderation and merging are where hidden judgement creeps in. Publish every removed statement along with the reason it was removed.
- Bridging can be gamed by fake accounts spread across both camps. Pair it with identity or recruitment controls, such as a recruited representative panel like CCAI's PureSpectrum sample or Stanford's scientific samples, rather than an open signup.
- Bridging also has a known bias toward bland statements: genuinely contested but important claims get filtered out (see the CCAI exclusions). So the map should show both what bridges and what divides. Polis reports both.

### Gaps
- X's official Community Notes documentation page returned an error (HTTP 402), so the details here come from academic papers rather than X's own docs.
- I could not find CIP's published 2025 Global Dialogues findings.
- I found no national citizens' assembly specifically on AI with published results in this pass.
- I did not research the 2024 to 2026 uses of Polis-like tools specifically for AI-risk scenario framing (as opposed to AI behaviour rules).

## 3. Steelmanning, Ideological Turing Tests, sign-off, adversarial collaboration, double crux

### Takeaway
The strongest check on fairness is to have each camp test or approve how its own view is stated. The Ideological Turing Test now has a published, measurable version. Adversarial collaboration on AI risk has been tried: it sharpened where the two sides disagree but barely changed anyone's mind. Double crux works between practised people but often fails to find a single shared crux.

### Cited Findings
- Bryan Caplan's Ideological Turing Test: you pass if you can state the other side's view well enough that its own holders cannot tell you apart from a real believer — [LessWrong: Ideological Turing Tests](https://www.lesswrong.com/w/ideological-turing-tests)
- A 2025 empirical version (Brand et al.) tested 200 UK participants on three polarizing topics. A participant "passed" if opponents rated their version of the other side's argument as favourably as the arguments from their own side. The study found high mutual understanding, and people who passed were less likely to see opponents as ignorant, immoral or irrational — [Brand et al., PMC12519043](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12519043/)
- Kahneman's adversarial collaboration: researchers on opposing sides agree in advance on the tests that would settle the dispute, then run them with a neutral arbiter (Barbara Mellers in the 2001 study with Hertwig). Kahneman developed it as an answer to "angry science", where critics attack a caricature of the other side's position — [Psychological Science: Mellers, Hertwig, Kahneman 2001](https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00350/); [Wharton PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2001---do-frequency-representations-eliminate-conjunction-effects.pdf); [Rethinking65 on Kahneman](https://rethinking65.com/the-nobel-prize-winning-professor-who-liked-to-collaborate-with-his-adversaries)
- The Kahneman-Killingsworth collaboration on income and happiness concluded that both sides were partly right and partly wrong — [Rethinking65](https://rethinking65.com/the-nobel-prize-winning-professor-who-liked-to-collaborate-with-his-adversaries)
- The Forecasting Research Institute's adversarial collaboration on AI risk ("Roots of Disagreement", April to May 2023) is the closest precedent to this project. The 11 "skeptics" were 9 superforecasters and 2 experts; the "concerned" side were domain experts. Median forecasts for AI-caused existential catastrophe by 2100 were 20% (concerned) and 0.12% (skeptics). The two groups identified short-term "crux" questions resolving by 2030 but did not substantially update toward each other. The best crux was expected to close the gap by only about 1 percentage point. Over 1,000 years, though, their estimates of "severe negative effects" were much closer, at 30% versus 40%. The project was funded by Open Philanthropy, and some participants on the concerned side were referred by Open Philanthropy staff — [EA Forum: Results from an Adversarial Collaboration on AI Risk (FRI)](https://forum.effectivealtruism.org/posts/orhjaZ3AJMHzDzckZ/results-from-an-adversarial-collaboration-on-ai-risk-fri)
- Double crux (CFAR): find a belief that, if it changed, would flip both people's conclusions. It is meant to be collaborative rather than adversarial — [LessWrong: Double Crux](https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-resolving-disagreement)
- Criticism of double crux: true double cruxes are rare on questions where reasonable people differ, and discussions often go all the way down to basic philosophy. Even supporters say single cruxes are useful without a shared one — [Contra double crux](https://www.greaterwrong.com/posts/nm6XuC9CzNBrthpPB/contra-double-crux); [Musings on double crux](https://www.lesswrong.com/posts/T3nb24aZf7d5S2Lnm/musings-on-double-crux-and-productive-disagreement); [CFAR staff comment](https://www.lesswrong.com/lw/o6p/double_crux_a_strategy_for_resolving_disagreement/divl)

### Inferences
- Design pattern, "own-camp sign-off": for each scenario, the worried statement must be approved by at least two named people from the worried camp, and the optimistic statement by two from the optimistic camp. Show who signed off and when. The FRI and Kahneman models both depend on each side accepting the framing before anything else happens.
- Design pattern, "blind ITT check": have members of each camp draft the *other* side's case, then have that side's members score it blind against a version written by a real believer, as in Brand et al. Publish pass rates. That gives a public, measurable fairness score for each scenario.
- Design pattern, a "cruxes" field for every scenario: list the two or three factual questions that would move each side, with resolution dates where possible (FRI's 2030-resolving questions are a model). This converts arguments into things the public and policymakers can watch.
- Set expectations: FRI shows that even well-run collaborations rarely produce convergence. The map's goal should be to make disagreement legible, not to resolve it.
- Disclose funders and recruitment channels for every panel. FRI's Open Philanthropy funding and referral channel is the kind of detail critics will look for.

### Gaps
- I found no public project that runs a formal "each camp signs its own summary" process at scale for AI. The closest analogues are IPCC author responses and the AI Safety Report's dissent notes (sections 4 and 5).
- The FRI full report PDF (forecastingresearch.org/s/AIcollaboration.pdf) was not fetched directly. The figures above come from FRI's own forum post.

## 4. Sourcing quotes fairly: selection, dating, cherry-picking, handling dissent

### Takeaway
The best existing rules come from Wikipedia: weight each view by how prominent it is in reliable sources, attribute opinions to named sources, and "describe disputes, do not engage in them". From the International AI Safety Report: say where there is consensus and where there isn't, and record lasting dissent explicitly. Balance-rating services like AllSides add a further method, multi-partisan panels plus blind surveys.

### Cited Findings
- Wikipedia NPOV: represent views "in proportion to the prominence of each viewpoint" in reliable sources. Tiny-minority views generally don't belong except in articles devoted to them. Undue weight can come from volume of text, placement, juxtaposition or imagery, not just from inclusion — [Wikipedia: Neutral point of view](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- Wikipedia: opinions "should not be stated in Wikipedia's voice" and must be attributed to specific sources. Avoid vague attributions like "many people think". Uncontested facts are stated directly — [Wikipedia: NPOV](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- Wikipedia "aims to describe disputes, but not engage in them", and prefers summarizing arguments to quoting heated participants — [Wikipedia: NPOV](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- The International AI Safety Report's principles require writers to state where consensus exists and to "acknowledge where and why there is disagreement in the wider expert community", presented objectively. Where differences persist, "dissenting views can be noted in the report" — [UK Gov: Principles and procedures](https://www.gov.uk/government/publications/international-scientific-report-on-advanced-ai-safety-expert-advisory-panel-and-principles-and-procedures/international-scientific-report-on-advanced-ai-safety-principles-and-procedures)
- The Interim AI Safety Report concluded that experts "continue to disagree on several questions, minor and major". It says the report does not represent the views of any individual writer or supporting government, and does not endorse any policy approach — [Interim Report (arXiv 2412.05282)](https://arxiv.org/pdf/2412.05282)
- The AI Safety Report now publishes interim "Key Updates" (October and November 2025) between full reports. This is a precedent for dated, incremental updates — [First Key Update (arXiv 2510.13653)](https://arxiv.org/pdf/2510.13653); [Second Key Update (arXiv 2511.19863)](https://arxiv.org/pdf/2511.19863); [Report publications](https://internationalaisafetyreport.org/publications)
- AllSides combines (a) multi-partisan editorial panels of six to nine reviewers from left, centre and right, each scoring from -6 to +6 with the scores averaged, with (b) "Blind Bias Surveys" in which people rate content with the branding stripped off (for example, 2,115 respondents in 2020). Blind surveys are described as its most robust method. AllSides admits that bias "is in the eye of the beholder" and that its ratings change over time — [AllSides: Media bias rating methods](https://www.allsides.com/media-bias/media-bias-rating-methods); [AllSides Editorial Reviews](https://www.allsides.com/media-bias/media-bias-rating-methods/editorial-reviews); [AllSides Blind Bias Survey 2020](https://www.allsides.com/sites/default/files/Blind%20Bias%20Survey%20-%20AllSides%20-%20August%202020.pdf)

### Inferences
- Design pattern, quote rules: (1) primary statements only: the person's own paper, testimony, post or interview, with a link; (2) every quote dated, with a "may be out of date" flag after something like 18 months; (3) give each quoted person a right of reply or a right to swap in a quote they prefer, which works like sign-off at the individual level; (4) quote people at their strongest and most recent, not their most viral line.
- Design pattern, "map voice" vs "attributed voice": state settled facts (benchmark results, dates) plainly in the map's own voice. Put every probability and every judgement in a named person's or group's voice. This is Wikipedia's attribution rule.
- Design pattern, blind check on summaries: borrow AllSides' blind survey idea. Show a sample of worried and optimistic readers each scenario summary with the source names removed, and ask whether it leans one way.
- Use the AI Safety Report's consensus / disagreement / dissent-note layering as the backbone structure for each scenario.

### Gaps
- The text of specific dissent notes in the 2025 and 2026 International AI Safety Reports was not checked, so I cannot say how often the dissent mechanism has actually been used.
- I did not verify Ground News's methodology.
- Wikipedia's documented failure modes (edit wars, capture of contested articles) were not sourced in this pass beyond the policy text itself.

## 5. Governance and update models that resist capture

### Takeaway
The IPCC is the strongest model: open reviewer registration, a written response to every comment, and publication of drafts, comments and responses after release. Combine that with version control and a public changelog, balanced advisory panels, recruited rather than open-signup raters, and funding disclosure. No single mechanism is enough on its own.

### Cited Findings
- IPCC review runs in stages: experts review a first draft; experts and governments review a second draft and a draft Summary for Policymakers at the same time; then governments approve that summary line by line in plenary — [IPCC Review Process fact sheet](https://www.ipcc.ch/site/assets/uploads/2024/04/IPCCFactSheet_ReviewProcess.pdf)
- Every IPCC review comment gets a written author response. After publication, the IPCC releases the drafts, the comments and the responses. Expert reviewers are credited by name — [IPCC Review Process fact sheet](https://www.ipcc.ch/site/assets/uploads/2024/04/IPCCFactSheet_ReviewProcess.pdf); [IPCC: What is an Expert Reviewer](https://www.ipcc.ch/site/assets/uploads/2024/04/IPCCFactSheet_ExpertReviewer.pdf)
- IPCC reviewer registration is broad: registrants are accepted unless they fail to show relevant qualifications (in AR5, self-declaration was enough) — [IPCC AR6 review fact sheet](https://www.ipcc.ch/site/assets/uploads/2021/07/AR6_FS_review_process.pdf); [IPCC FS review process (older)](https://www.ipcc.ch/site/assets/uploads/2018/02/FS_review_process.pdf)
- An example of a published comment archive is the IPCC 2019 Refinement — [IPCC-NGGIP comments page](https://www.ipcc-nggip.iges.or.jp/public/2019rf/comments.html)
- International AI Safety Report: the Chair holds final responsibility, the Expert Advisory Panel gives technical feedback only, and procedures call for a process "inclusive of experts across a breadth of views" — [UK Gov: Principles and procedures](https://www.gov.uk/government/publications/international-scientific-report-on-advanced-ai-safety-expert-advisory-panel-and-principles-and-procedures/international-scientific-report-on-advanced-ai-safety-principles-and-procedures); [Interim Report](https://arxiv.org/pdf/2412.05282)
- ProCon says it is a nonprofit with "no government affiliations" (before 2020) and is now owned by Britannica. Ownership changes are a governance event a map should disclose — [ProCon About](https://www.procon.org/about-us/); [Wikipedia: ProCon.org](https://en.wikipedia.org/wiki/ProCon.org)
- AllSides openly says it rates content only and does not factor in ownership or funding, though it shows them on source pages — [AllSides methods](https://www.allsides.com/media-bias/media-bias-rating-methods)
- Polis exports raw data and publishes reports in real time, so outsiders can audit results — [Computational Democracy Project: Polis](https://compdemocracy.org/Polis/)
- Community Notes' open-source algorithm and public data meant outside researchers could find manipulation weaknesses, which then led to a deployed fix — [Gaming Consensus](https://arxiv.org/pdf/2607.01824); [Truong et al.](https://arxiv.org/pdf/2511.02615)

### Inferences
- Design pattern, an IPCC-lite review cycle: publish a draft scenario, open a review window, answer every comment in writing, then publish the final version along with all comments and responses. Credit reviewers by name, or by pseudonym if they ask.
- Design pattern, a version-controlled source of truth: keep the whole map as structured files in a public Git repository. Each scenario has a version number, a "last reviewed" date and a changelog entry explaining what changed and why. Releases follow a fixed schedule (quarterly, like the AI Safety Report's Key Updates), with emergency updates flagged.
- Design pattern, a paired editorial board: every editorial role is held in pairs, one from each camp, with a neutral chair who has no vote on content and only rules on process. This mirrors the AllSides left/centre/right panels and Kahneman's neutral arbiter.
- Design pattern, funding firewall: publish every funder above a threshold, and cap any single funder's share. Note that Open Philanthropy funded the FRI collaboration, and that many AI-risk evidence sources share funders. Critics on the optimistic side will look for this.
- Design pattern, open data and forkability: under an open licence, if one camp believes the map has been captured, it can fork the data and publish its own version. The threat of a fork is itself a check on capture.
- Use recruited, representative panels (as in CCAI and Stanford) for any public rating, not open signup, so that bridging metrics cannot be brigaded.

### Gaps
- I did not research Wikipedia's ArbCom/dispute governance or its documented cases of capture in this pass.
- I found no AI-specific public map that has publicly documented an anti-capture governance model.

## 6. Common failure modes: false balance, framing effects, scope creep

### Takeaway
"Balance" can itself be a bias. Two-sided presentation made climate science look more contested than it was. The fix is due weight plus clear probability ranges, not equal space. Framing leaks through layout and word choice. Scope creep is controlled by fixed inclusion criteria and by bridging-style filters that drop statements that are low-salience or merely duplicates.

### Cited Findings
- Boykoff and Boykoff (2004) studied US prestige press coverage of global warming from 1988 to 2002 (636 articles randomly sampled from 3,543). They found that the journalistic norm of balance "leads to biased coverage" of the human role in warming and of action on it. The authors said they were not measuring left/right bias but informational distortion — [Boykoff & Boykoff 2004, CU Boulder record](https://experts.colorado.edu/display/pubid_94928); [SSRC MediaWell citation](https://mediawell.ssrc.org/citation/balance-as-bias-global-warming-and-the-us-prestige-press/); [FAIR summary](https://fair.org/home/journalistic-balance-as-global-warming-bias/)
- Later experimental work, summarized in a literature review, found that balanced coverage reduces confidence in a scientific consensus and increases perceived uncertainty — [DOCA: Balance (Climate and Environment Coverage)](https://www.hope.uzh.ch/doca/article/view/2o)
- Wikipedia: where a scientific consensus exists, presenting an opposing view without regard to due weight can make an issue look "more controversial than it is". Fringe views should be "clearly described as such" and "should not be legitimized through comparison to accepted academic scholarship" — [Wikipedia: NPOV](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view)
- Framing through layout: ProCon admits that even putting pros on the left can be read as a political signal — [ProCon FAQ](https://www.procon.org/faqs/)
- AI risk is a case where expert disagreement is genuinely huge, not fringe versus consensus. In FRI's study the median estimates were 20% versus 0.12% for existential catastrophe by 2100. The International AI Safety Report says experts disagree on questions "minor and major" — [FRI results](https://forum.effectivealtruism.org/posts/orhjaZ3AJMHzDzckZ/results-from-an-adversarial-collaboration-on-ai-risk-fri); [Interim Report](https://arxiv.org/pdf/2412.05282)
- Bridging filters can drop important but contested statements. CCAI excluded both "collective good over individual rights" and its opposite because neither bridged — [Anthropic: CCAI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)
- Community Notes shows that bridging precision has a cost: in simulations, more than 40% of genuinely helpful notes were never published — [Truong et al.](https://arxiv.org/pdf/2511.02615)
- vTaiwan kept the scope tight by asking about concrete cases rather than ideological abstractions — [Audrey Tang speech](https://archive.tw/speech/617989)
- CCAI handled scope by deduplicating and merging statements to keep its output similar in size to Anthropic's 58-principle constitution — [Anthropic: CCAI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)

### Inferences
- AI risk is not like climate science in 2004. On many AI scenarios there is no consensus to protect, so two-sided presentation is appropriate. The risk lies in the other direction: giving equal visual weight to a scenario only a handful of people take seriously. Design pattern: tag each scenario with "how many credible people hold each view", for example by citing surveys or forecast aggregates, and size or order scenarios by that, not alphabetically or by drama.
- Design pattern, a "weight of opinion" bar: instead of equal columns, show the distribution of expert and forecaster probability estimates where they exist. This answers false balance without the map's editors picking a winner.
- Design pattern, fixed inclusion criteria for adding a scenario: (1) a named, credible proponent has written it up publicly, (2) it is meaningfully distinct from existing scenarios, (3) it passes a bridging vote from both camps that it "deserves a slot". Cap the top-level list at a fixed number (for example 12 to 20) and nest variants underneath. This answers scope creep.
- Design pattern, framing controls: randomize or alternate which side appears first or on the left; use neutral scenario names agreed by both camps; avoid emotive imagery. Wikipedia lists imagery and placement as sources of undue weight.
- Keep a visible "contested / did not bridge" section so that the bridging filter does not silently hide the most important disagreements.

### Gaps
- I found no study measuring framing effects specifically in AI-risk communication formats (for example, whether worried-first versus optimistic-first ordering changes reader views).
- I found no published inclusion criteria from other AI scenario catalogues to compare against.
