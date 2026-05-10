# CLAUDE.md

See [AGENTS.md](./AGENTS.md) for the repo overview, layout, defaults, and style rules.

## Claude's role here

This is the public docs site, not the R&D workspace. Claude's job here is editorial:

1. **Read AGENTS.md first.** Do not act on assumptions about scope.
2. **Edit existing pages over creating new ones.** The `nav` block in `mkdocs.yml` is the source of truth for site shape.
3. **Don't pull in private R&D content.** Raw measurements, supplier names, pre-spec drafts, and engineer-outreach material live in the R&D repo and stay there until explicitly cleared.
4. **Keep the strategic framing in the parent project's AGENTS.md.** This repo describes the project; it does not redefine it.

## When Claude should ask

- Before adding a new top-level nav section.
- Before promoting any draft from R&D to public-facing material.
- Before changing the strategic positioning captured on `docs/project/overview.md` or `docs/project/concept.md` (these mirror the parent project's strategy doc).
