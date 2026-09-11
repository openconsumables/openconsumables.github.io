# Air purifiers

Working name: **OpenAir**. The second category in the Open Consumables device knowledge graph.

## What's here

- **[Units](units/index.md)**, the air purifiers themselves, with replacement filters listed by slot.
- **[Filters](filters/index.md)**, Manufacturer replacement cartridges, with the units they fit.

## Status

**Reference layer only.** OpenAir is not yet an active measurement subproject; activation depends on OpenBrush producing a published measured baseline. This category records provenance-tagged compatibility data sourced from manufacturer pages, with no project measurement claims.

Coverage includes distinct Xiaomi filter families and Smartmi entries. Each filter lists only the units supported by its cited source. A newer filter fitting an older purifier does not prove that the older filter fits the newer purifier. Conflicting manufacturer dimensions are kept as unresolved claims, rather than treated as measured equivalence. Pull requests welcome; see [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema.

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

## Missing a device or replacement part?

[Send a short report](https://github.com/openconsumables/openconsumables.github.io/issues/new?template=evidence-report.md&title=Missing+record%3A+openair&body=Device%2Fpart+or+page%3A+openair%3A+%5Bexact+model%2Fvariant+or+part+name%5D+%28https%3A%2F%2Fopenconsumables.org%2Fcategories%2Fopenair%2F%29%0ACorrection+or+addition%3A+%0ASource%3A+%0AUncertainty%3A+%0A) with the exact model code or part name.
Better sources and contradictory fit evidence are welcome too. For a dead link
or a claim that needs checking, just identify the problem.
GitHub requires sign-in; you can also [copy a report](../../contributing.md#send-a-short-report)
and prepare it for your user. Maintainers can handle the data-file edits.
