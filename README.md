# The AI Risk Map

A public map of the major ways AI could go, good and bad. Each scenario gets a card where the worried side and the optimistic side make their case, every published probability is shown with its source and wording, and each scenario is sorted into what needs a policy response and what needs public communication. The map never publishes a probability of its own.

**Live site:** https://ai-risk-map.vercel.app

Inspired by a proposal Emad Mostaque made on the Moonshots podcast (7 October 2026).

## What's here

- `cards/` holds the 18 scenario cards across eight domains, each with a good and a bad version, plus "AI disappoints" and an open "unknown and combined risks" entry. `cards/_CARD_SPEC.md` defines the 17 fields every card carries.
- `reports/AI scenario map framework.md` is the research report behind the framework.
- `research_notes/` holds the five sourced research notes: risk catalogs, forecasting and disagreement, argument mapping and governance, benefits and scenario methods, and funding and partners.
- `site/` is the published site: the map plus three infographics.
- `build/` holds the Python scripts that turn the cards into the site. One optional styling input comes from a separate project, so a rebuild here uses default styles.

## License

Content is licensed under [CC BY 4.0](LICENSE). Copy it, adapt it, and credit the source.
