# Card specification for the AI Risk Map

Every scenario card is one Markdown file in this folder. The risk map web page is generated from these files, so the format must be exact. Model your card on `control-bad-loss-of-control.md` (a bad scenario) and `health-good-medical-progress.md` (a good scenario). Read both before writing.

## Front matter (exact keys, exact allowed values)

```
---
id: <filename without .md>
name: <neutral name both sides would accept>
domain: <one of: Health and biology | Work and income | Science, energy and environment | Information and democracy | Security and infrastructure | Power and governance | Daily life, mind and meaning | Control of advanced AI | none>
direction: <good | bad | neutral>
layer: <pathway | end-state>
mechanism: [<any of: misuse, malfunction, loss-of-control, systemic>]
mit_domain: "<MIT AI Risk Repository domain code and name, or none (benefit)>"
quadrants: [<any of: gradual-shared, gradual-concentrated, fast-shared, fast-concentrated>]
triage: <act-now | prepare-and-watch | enforcement-problem | covered-communicate | communicate>
confidence: <very-low | low | medium | high | very-high>
summary: "<the same one sentence as 'In one sentence' below, in double quotes>"
status: draft
last_reviewed: 2026-10-09
---
```

Quadrants are the big-picture view: how fast AI arrives (gradual "normal technology" vs fast transformation) crossed with whether control and benefits stay broadly shared or become concentrated (or lost).

## Body sections, in this order, with these exact headings

`# <Name>`, then `**In one sentence:** ...`, then an optional `**Design note:** ...` if the two-sided format needed adjusting, then:

- `## Preconditions`
- `## Timing and reversibility` (earliest plausible date, speed, reversibility)
- `## The case that this happens` (for good cards: "(optimistic)"; for bad cards this is the worried side). One or two short attributed excerpts, then `**Plain summary (needs sign-off from this side):**`
- `## The case that it doesn't` (the other side, same format)
- `## Common ground`
- `## Cruxes` (2 or 3 numbered questions, each ending with *Check: <source and date>*)
- `## Probability estimates` (a table: Source | Who | Question or claim | Estimate | Date | Scorable? or Type). If none exists, write **No published estimate** and list the closest related numbers.
- `## Evidence confidence` (bold level, then one or two sentences why)
- `## Signposts` (3 to 5 numbered, each with a threshold)
- `## Evidence so far`
- `## Existing coverage` (laws and rules that already apply, and whether enforced)
- `## Triage` (the four steps below, reasoning shown, then `**Result: ...**` and `**Communication note:** ...`)
- `## Related scenarios` (use the names of other scenarios on the map)
- `## Sources` (numbered list: title, publisher, date, URL. Every source linked in the card appears here.)
- `## Sign-off record` (both sides "not yet reviewed"; changelog line "2026-10-09 first draft")

## The four-step triage rule

1. Is the harmful path already illegal or regulated? If yes and enforced: `covered-communicate`. If rules exist but enforcement is weak: `enforcement-problem`.
2. Is there an action both camps accept, or that works acceptably across the whole scenario set? If yes: `act-now`.
3. Is it severe, hard to reverse, with at least one credible published estimate placing it within about ten years, but no agreed action? If yes: `prepare-and-watch`, tied to specific signposts.
4. Otherwise: `communicate`, naming the purpose (correct a misconception, set expectations, help people prepare or benefit).

For good scenarios, flip the question: what is blocking this, and does removing the block need policy?

## The 18 scenarios on the map

| Domain | Good direction | Bad direction |
|---|---|---|
| Health and biology | Medical progress compressed into years (done) | AI-assisted biological or chemical attack |
| Work and income | Broad productivity gains and cheaper goods | Mass job loss and widening inequality (done) |
| Science, energy and environment | Faster discovery and cheaper clean energy | AI's energy and resource demand outpaces its gains |
| Information and democracy | Better shared understanding and forecasting | Manipulation, fraud and collapse of trust |
| Security and infrastructure | Defenders gain the advantage | Cheap large-scale cyberattacks and critical-system failures |
| Power and governance | Wider access and more accountable institutions | Concentrated power or AI-enabled surveillance |
| Daily life, mind and meaning | Personal tutors, care and freed time | Over-reliance, lost skills and unhealthy AI companions |
| Control of advanced AI | Powerful AI that stays aligned and overseeable | Loss of control over advanced AI (done) |
| Outside any domain | AI disappoints (done) | Unknown, combined and slow-building risks |

## Hard rules

- **Never invent a quote, number, date or source.** If you cannot verify something, leave it out or mark it "(unverified)".
- **Quotes:** at most two per side, each under 15 words, from a named person, linked to where it was said. Otherwise paraphrase with attribution ("Bengio argues that ..."). The person who signs off for each side will choose the final quotes.
- **Name real proponents on both sides.** Prefer people with standing (researchers, officials, practitioners) over commentators. Each side's case should be one its own proponents would recognize as fair.
- **Link every factual claim** inline and list it under Sources. Prefer primary sources: studies, official reports, company disclosures, court filings. Mark secondary coverage "(secondary)".
- **Plain language** for a general reader. Define jargon on first use.
- **No em dashes** anywhere. Use commas, periods or parentheses.
- **Current as of October 2026.** Give dates for every figure.
- Never publish a probability of your own. Report other people's numbers with who, wording and date.
