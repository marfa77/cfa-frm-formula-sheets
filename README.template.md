# cfa-frm-formula-sheets

[![PyPI](https://img.shields.io/pypi/v/cfa-frm-formula-sheets.svg)](https://pypi.org/project/cfa-frm-formula-sheets/)

Install: `pip install cfa-frm-formula-sheets`

Open, machine-readable **formula reference for CFA Level I, CFA Level II and FRM Part I** — {{N}} formulas ({{COUNTS}}) in LaTeX with plain-language variable definitions and "when used" notes, organised by the **official topic areas** published by CFA Institute and GARP. Includes the **official topic weights** with source links (checked 2026-10-12).

**Browse rendered formulas (KaTeX):** https://marfa77.github.io/cfa-frm-formula-sheets/ · Markdown: [`FORMULAS.md`](FORMULAS.md)

- `data/formulas.json` / `.csv` — fields: `id, exam, topic, name, latex, variables, when_used, topic_source_url, source_checked, uniprep2go_url`
- `data/topic_weights.json` / `.csv` — official exam weights per topic, each with `source_url`
- `schema/formulas.schema.json` — JSON Schema · `scripts/validate.py` — schema, CSV sync, topic-name check against official tables, numeric spot-checks (annuity, duration, BSM/put–call parity, delta, binomial, Gordon, swap rate, GARCH, normal ES), URL checks

## Official topic weights

{{WEIGHTS}}
Weights are copied exactly as published; where an official page did not state a session, `session` is `null`. GARP's 2026 Learning Objectives (with weights) are behind a form, so the FRM rows use GARP's latest publicly downloadable PDF (2023) and say so.

## Usage

```python
import json, urllib.request
url = "https://raw.githubusercontent.com/marfa77/cfa-frm-formula-sheets/main/data/formulas.json"
F = json.load(urllib.request.urlopen(url))["entries"]
print([f["name"] for f in F if f["exam"] == "FRM Part I" and f["topic"] == "Valuation and Risk Models"])
```

Formulas are standard textbook finance math in common notation; check the official curriculum for notation and conventions. Validate: `pip install jsonschema && python scripts/validate.py`.

## Study with it

- CFA Level I: [CFA Level I formula reference deck](https://uniprep2go.study/decks/cfa-level-1-formula-reference-2026)
- CFA Level II: [CFA Level II formula reference deck](https://uniprep2go.study/decks/cfa-level-2-formula-reference-2026)
- FRM Part I: [FRM Part I Anki deck](https://uniprep2go.study/decks/frm-part-1-anki-deck)

## Contributing

Edit `scripts/build_data.py` (source of truth), then run `python scripts/build_data.py && python scripts/make_docs.py && python scripts/validate.py`. Corrections welcome.

## How to cite

> UniPrep2Go (2026). *cfa-frm-formula-sheets: Formula reference for CFA Level I, Level II and FRM Part I* (v1.0.0) [Data set]. https://github.com/marfa77/cfa-frm-formula-sheets

See `CITATION.cff`. A Zenodo DOI will be added after archival.

## License

Data (`data/`, `FORMULAS.md`, docs content): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code (`scripts/`, `schema/`): MIT.

## Disclaimer

Independent study aid; not affiliated with or endorsed by CFA Institute or GARP. CFA® and FRM® are trademarks of their respective owners.
