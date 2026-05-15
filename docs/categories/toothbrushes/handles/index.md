# Toothbrush handles

One page per handle, generated from `data/handles/*.yml` in this repo. Each page lists the heads that fit, with provenance for every claim.

The data layer is best-effort coverage. A handle with no measurements still has a page if at least one verifiable source supports its existence and at least one head claim. Measurement upgrades the row from `manufacturer-claim` to `measured`; it does not gate publishing.

See [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/main/data/README.md) for the schema and how to add or correct an entry.

## Current entries

- [Xiaomi T200](xiaomi-t200.md)
- [Xiaomi T500](xiaomi-t500.md)
- [Oral-B Pro 1000](oral-b-pro-1000.md)

Gaps in coverage are intentional and visible: an entry that references an unknown handle or head will render the link as `(no entry)`. Pull requests welcome.
