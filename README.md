# Open Consumables, public docs

The public documentation site for [Open Consumables](https://github.com/openconsumables): measured baselines for everyday hardware.

Live site: <https://openconsumables.github.io/docs/>

## What's in this repo

- `docs/` (markdown sources for the site
- `mkdocs.yml`) site configuration
- `.github/workflows/deploy.yml` (GitHub Pages build and deploy
- `requirements.txt`) pinned Python deps for local builds and CI

The R&D content (research tracks, ecosystem maps, raw measurements, CAD) lives in a separate repository. This repo holds only what is intended to be public.

## Local development

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://localhost:8000>. The site rebuilds on save.

To verify a clean build matching CI:

```bash
mkdocs build --strict
```

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

GitHub Pages must be configured for this repo with **Source: GitHub Actions** under Settings → Pages.

## Contributing

See the [contributing page](https://openconsumables.github.io/docs/contributing/) on the live site.

## License

Documentation released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Any code samples under MIT.
