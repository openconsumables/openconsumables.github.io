# Contributing

This site is the public-facing documentation for Open Consumables. The R&D work happens in a separate (currently private) repository.

## What we accept here

- **Corrections to published material**: factual errors, broken links, typos.
- **Clarifying questions** filed as GitHub issues.
- **Measurement contributions**, where you've measured a sample using a published methodology and want to add a data point.

## What we don't accept yet

- Speculative additions to draft baselines (we're pre-spec).
- New category proposals (the deferred list is the roster; we activate one at a time).
- Brand promotion or curation (we measure, we don't pick winners).

## Editing pages

Every page has an "edit this page" link in the top right that opens the source markdown in GitHub.

For larger changes:

1. Fork the [docs repository](https://github.com/openconsumables/docs).
2. Edit markdown under `docs/`.
3. Open a PR.

## Local preview

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

The site rebuilds on save at <http://localhost:8000>.

## Style

- Markdown-first. No HTML unless a markdown extension can't reach.
- Lowercase, kebab-case filenames (`xiaomi-t300-handle.md`).
- Date prefixes only for time-bound notes (decision logs, dated baselines).
- Plain English. No marketing voice.
- Don't use em dashes. Use commas, parentheses, periods, or colons.
