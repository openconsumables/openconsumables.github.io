# AGENTS.md

Guidance for AI agents (Claude, Codex, or otherwise) working in this repository.

## What this repo is

The **public documentation site** for Open Consumables. MkDocs Material, deployed to GitHub Pages on push to `main`.

Live site: <https://openconsumables.github.io/docs/>

This repo is deliberately separate from the R&D repo. The R&D repo contains research briefs, raw measurements, working notes, supplier names, and pre-publication drafts. This repo holds only material that has been cleared for the public.

## Repo layout

```
docs/                          # markdown sources for the site
├── index.md
├── project/
│   ├── overview.md
│   └── concept.md
├── categories/
│   ├── index.md
│   └── toothbrushes/
│       ├── index.md
│       ├── ecosystem.md
│       ├── compatibility.md
│       ├── handles/           # GENERATED from data/handles/*.yml
│       │   ├── index.md       # hand-written entrypoint
│       │   └── <slug>.md      # generated; do not hand-edit
│       └── heads/             # GENERATED from data/heads/*.yml
│           ├── index.md
│           └── <slug>.md
data/                          # device knowledge graph; source of truth for handle/head pages
├── README.md                  # schema, provenance tiers, contribution guidance
├── mounts.yml                 # mount / interface profiles
├── handles/<slug>.yml         # one file per handle
└── heads/<slug>.yml           # one file per head (OEM or generic)
tools/
└── build_pages.py             # YAML -> markdown generator; run after editing data/
mkdocs.yml                     # site configuration; nav is the source of truth for site shape
requirements.txt               # pinned deps for local builds and CI
.github/workflows/deploy.yml   # GitHub Pages build and deploy on push to main
```

The `data/` layer is the device knowledge graph: best-effort coverage of handles and heads with per-claim provenance. Read `data/README.md` for the schema and tiers.

## Default behavior

1. **Edit existing markdown under `docs/`** rather than creating new top-level structure. The `nav` block in `mkdocs.yml` is the source of truth for site shape.
2. **Don't introduce content from the R&D repo** without checking. Pre-spec drafts, raw measurements, supplier names, and engineer-outreach material stay private until explicitly cleared.
3. **Keep the writing voice plain and measured.** No marketing voice. No standards-body language unless the project has actually committed to stewarding a standard (it hasn't).
4. **Run `mkdocs build --strict` before pushing** when a change adds or moves pages. CI runs strict mode and will fail on broken links.

## Style

- Markdown-first. Avoid raw HTML.
- Lowercase, kebab-case filenames (`xiaomi-t300-handle.md`).
- Date prefixes only for time-bound notes.
- No em dashes. Use commas, parentheses, periods, or colons.
- Plain English, short Anglo-Saxon words over Latinate.
- Don't echo the question back; don't pad with rule-of-three lists.

## Adding a page

1. Create the markdown file under the appropriate `docs/` subdirectory.
2. Add it to the `nav` block in `mkdocs.yml`.
3. Verify with `mkdocs serve` locally.
4. Run `mkdocs build --strict` to catch broken links before pushing.

## Adding a handle or head (knowledge graph)

1. Add a YAML file under `data/handles/` or `data/heads/` following the schema in `data/README.md`. Every compatibility claim needs a `provenance` and a `source`.
2. Run `python tools/build_pages.py` to regenerate the markdown pages.
3. Add the new generated page to the `nav` block in `mkdocs.yml`.
4. `mkdocs build --strict` to validate.

Do not hand-edit files under `docs/categories/*/handles/` or `docs/categories/*/heads/` other than the `index.md` entrypoints. They are overwritten on every build.

## Adding a category

A new category subsection lives at `docs/categories/<name>/index.md` plus topic pages alongside.

Before adding a category, check that:

- It passes the [category-fit gates](docs/project/overview.md). The project is pre-product; most categories are deferred.
- The nav entry under `mkdocs.yml` mirrors the directory structure.

The full activation rules and deferred roster live in the parent project's [AGENTS.md](https://github.com/openconsumables/openconsumables/blob/main/AGENTS.md). Do not invent a new category from this repo.

## What this repo is not

- Not the R&D workspace. Don't paste in raw measurements, supplier names, or pre-spec drafts.
- Not a blog. There is no `posts/` or news section yet, and adding one needs an explicit decision.
- Not the place to register opinions about which brand is "best." We measure; we don't curate.
- Not a price comparison or affiliate site. The data layer captures device facts and compatibility, not pack sizes, prices, or buying recommendations.

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

GitHub Pages must be configured for this repo with **Source: GitHub Actions** under Settings, Pages.

## Local environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

`.venv/` and `site/` are gitignored.
