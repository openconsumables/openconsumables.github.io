# Electric scooters

One page per scooter, generated from `data/openscoot/units/*.yml`. Each page lists the replacement tires that fit, with provenance for every claim.

The data layer is best-effort coverage. A unit with no measurements still has a page if at least one verifiable source supports its existence and at least one tire claim. Measurement upgrades a row from `manufacturer-claim` to `measured`; it does not gate publishing.

See [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema and how to add or correct an entry.

## Current entries

- [Xiaomi M365](xiaomi-m365.md)
- [Xiaomi Mi Electric Scooter 3](xiaomi-mi-electric-scooter-3.md)
- [Segway-Ninebot KickScooter Max G30](ninebot-max-g30.md)

Gaps in coverage are intentional and visible: an entry that references an unknown scooter or tire will render the link as `(no entry)`. Pull requests welcome.
