# Air purifier units

One page per unit, generated from `data/openair/units/*.yml`. Each page lists the replacement filters that fit, with provenance for every claim.

The data layer is best-effort coverage. A unit with no measurements still has a page if at least one verifiable source supports its existence and at least one filter claim. Measurement upgrades a row from `manufacturer-claim` to `measured`; it does not gate publishing.

See [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema and how to add or correct an entry.

## Current entries

- [Xiaomi Mi Air Purifier 3H](xiaomi-mi-air-purifier-3h.md)
- [Xiaomi Mi Air Purifier 3C](xiaomi-mi-air-purifier-3c.md)
- [Smartmi Air Purifier P1](smartmi-air-purifier-p1.md)

Gaps in coverage are intentional and visible: an entry that references an unknown unit or filter will render the link as `(no entry)`. Pull requests welcome.
