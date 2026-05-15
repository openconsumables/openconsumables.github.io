# Air purifiers

Working name: **OpenAir**. The second category in the Open Consumables device knowledge graph.

## What's here

- **[Units](units/index.md)**, the air purifiers themselves, with replacement filters listed by slot.
- **[Filters](filters/index.md)**, OEM and generic cartridges, with the units they fit.

## Status

**Reference layer only.** OpenAir is not yet an active measurement subproject; activation depends on OpenBrush producing a published measured baseline. Until then, this category exists as a knowledge-graph stub: provenance-tagged compatibility data sourced from manufacturer pages and aftermarket listings, with no project measurement claims.

Coverage is intentionally small: a Xiaomi 3-family slot (3H, 3C, plus the OEM HEPA / anti-formaldehyde cartridges and a generic clone catch-all) and a Smartmi P1 slot for contrast. Pull requests welcome; see [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema.

## Scope

**In scope** for the reference layer:

- consumer Chinese-IoT cluster air purifiers (Xiaomi, Smartmi, Viomi, Roidmi, Deerma, Airdog)
- the mechanical filter-slot interface between unit and cartridge
- HEPA grade, media composition, and filter-stage architecture as disclosed by the manufacturer

**Out of scope** at this stage:

- particulate-removal performance benchmarks
- CADR independent verification (manufacturer claims only, until measured)
- Western-brand purifiers (Dyson, Levoit, Coway, Honeywell): fail the ecosystem-selection prerequisite
- the purifier motor, controller, sensor calibration, or app integration
