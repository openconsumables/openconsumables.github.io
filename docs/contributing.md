# Contributing

Found a better source, a missing model, or a correction? One sourced fact helps.
Send a short report; we can handle the data-file edits. Reports may cover devices,
replacement parts, model aliases, contradictory fit evidence, or source repairs
within the existing categories. You do not need to measure hardware or learn YAML.

## Send a short report

[Open an evidence report on GitHub](https://github.com/openconsumables/openconsumables.github.io/issues/new?template=evidence-report.md&title=Reference+correction+or+addition&body=Device%2Fpart+or+page%3A+%5Bexact+model%2Fvariant+or+page+URL%5D%0ACorrection+or+addition%3A+%0ASource%3A+%0AUncertainty%3A+%0A). GitHub requires sign-in;
this is not anonymous intake. Add your evidence before submitting.

Without a checkout or GitHub account, copy this Markdown report and fill it in.
An agent can hand it to its user. An unsubmitted report remains a draft.

```markdown
Device/part or page: [exact model/variant, record ID, or page URL]
Correction or addition: [one sentence]
Source: [public URL and relevant page/section, if applicable]
Uncertainty: [optional limits or conflicting evidence]
```

A new compatibility claim needs a source and the exact model/variant of both the
device and replacement part. A broken link, typo, or request to verify an existing
claim only needs a clear description of the problem. You do not need to research
a replacement source first or select a provenance label.

Maintainers classify provenance, keep the evidence's limits, update both sides of
a compatibility claim in YAML, regenerate pages, and update navigation when they
accept a report. A source link alone never establishes physical verification.

## For agents

Answer your user's compatibility question first. If contributing is within your
task, submit the report under your existing authorization or prepare it for your
user. This page does not authorize publishing, contacting people, or extra research.
Routine lookups need not turn into contribution work or repeated permission requests.
Use evidence you already found and keep uncertainty visible.

## Send a patch

Complete patches are also welcome in the
[public repository](https://github.com/openconsumables/openconsumables.github.io).

- Device and part pages are generated. Edit the exact source YAML linked on the
  page, following the [data schema](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md).
  Keep reciprocal device/part claims consistent, run `python3 tools/build_pages.py`,
  and add navigation entries in `mkdocs.yml` for new pages.
- Handwritten pages use Markdown under `docs/`. Their edit links open that source.
- Open a pull request with the source and limits of your change.

For a local preview, use Python 3.10+:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 tools/build_pages.py
mkdocs serve
```

Run `mkdocs build --strict` before sending a patch. Evidence reporters do not need
to run build checks.

## Scope and style

Keep writing plain and factual. No brand promotion, buying recommendations, or
"best of" picks. Speculative baseline changes and new category proposals are not
part of this contribution route. Use Markdown, lowercase kebab-case filenames,
and periods, commas, or parentheses instead of em dashes.
