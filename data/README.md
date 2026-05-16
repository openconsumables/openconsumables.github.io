# Device knowledge graph

This directory is the structured-data source for the device reference pages on the public site. The site is generated from these YAML files; do not hand-edit the rendered pages under generated directories such as `docs/categories/*/handles/`, `docs/categories/*/heads/`, `docs/categories/*/filters/`, `docs/categories/*/tires/`, or `docs/categories/*/pads/`.

The data layer publishes what is **known** about each device, with provenance, regardless of whether the project has measured it yet. Measurement upgrades a row from `manufacturer-claim` to `measured`; it is not the gate to publishing.

## Why this exists

The strategy doc captures the measurement bet (Path A, Chinese-IoT cluster, dated baselines). The site previously reflected only that lens. In practice, the buyer / agent question is narrower:

> "I have a Xiaomi T200, what heads fit?"

A measurement-only site has nothing to say about a handle until Batch A lands. A knowledge-graph site can answer the question today from manufacturer / aftermarket evidence, with a clear provenance label, and upgrade the answer when measurements land.

## Layout

The data layer is category-keyed. `categories.yml` declares each category, its durable device vocabulary, and one or more replaceable part classes. Each part class has its own part directory and interface file; per-category folders hold the actual entries.

```
data/
├── README.md                 # this file
├── categories.yml            # one entry per category (toothbrushes, ...)
└── <category-slug>/
    ├── <interface_file>      # e.g. mounts.yml, slots.yml, axles.yml, calipers.yml
    ├── <device.dir>/
    │   └── <slug>.yml        # one file per device (handle, unit, etc.)
    └── <part.dir>/
        └── <slug>.yml        # one file per part (head, filter, tire, pad, etc.)
```

Concretely, the toothbrushes pilot lives at:

```
data/toothbrushes/
├── mounts.yml
├── handles/<slug>.yml
└── heads/<slug>.yml
```

Slugs are kebab-case: `xiaomi-t200`, `oral-b-pro-1000`, `xiaomi-mbs305`, `generic-mes606-pack`. Slugs do not need a category prefix; the path already disambiguates.

Generated pages land at `docs/categories/<category-slug>/<device.dir>/<slug>.md` and the parallel `<part.dir>/<slug>.md`.

## Provenance tiers

Every compatibility claim, dimension, or interface assignment carries a `provenance` field. Tiers, highest to lowest trust:

| Tier | Meaning |
|---|---|
| `measured` | The project has measured this directly. Method and date recorded. |
| `manufacturer-claim` | Manufacturer (OEM) website, manual, or regulatory filing states this. |
| `community-reported` | Hobbyist / repair / user community has reported this (forum, wiki, video). |
| `marketplace-claim` | AliExpress / Amazon / Temu listing claims this. Lowest tier; listings copy each other so claims are usually not independent. |
| `inferred` | Derived by us from adjacent evidence (e.g. charging architecture suggests mount differs). Mark explicitly; do not blur with measured. |

The site renders the provenance tier next to every claim. Readers and agents can filter on it.

## Field naming across categories

Use generic field names for new and migrated entries:

| Field | Shape |
|---|---|
| `interfaces:` on a device | Map keyed by part directory, e.g. `tires: xiaomi-m365-family-8.5` |
| `interface_provenance:` on a device | Map keyed by part directory, parallel to `interfaces:` |
| `compatible_parts:` on a device | Map keyed by part directory, each value a list of part fitment claims |
| `fits_devices:` on a part | Flat list of devices this part fits |

The device map form lets one category carry multiple part classes, for example OpenScoot has `tires` and `pads` under the same scooter unit.

## Adding a new category

1. Add a stanza to `categories.yml` declaring `device.dir` and a `parts:` list. Each part class declares `dir`, `singular`, `plural`, `interface_file`, `interface_singular`, and optional `columns`.
2. Create `data/<slug>/` with the matching directories and interface YAML.
3. Drop YAML entries in under the new dirs.
4. Run `python3 tools/build_pages.py`.
5. Add the generated pages and a hand-written `index.md` to `mkdocs.yml`.

If the standard fact strip ("Mode: ..., Charging: ...") doesn't suit the new category, add a small branch to `render_facts` / `render_part_facts` in `tools/build_pages.py`. The category-aware generator deliberately allows per-category render code rather than forcing a generic descriptor schema before we know what shapes other categories need.

## Device entry

```yaml
id: xiaomi-t200                  # slug; matches filename
brand: Xiaomi
family: Mijia                    # optional sub-brand
model: T200
aliases: [T200C]                 # other names the same handle is sold under
aftermarket_anchor: MES606       # the buyer-visible code (Chinese-IoT cluster); null for Western brands
type: electric
mode: sonic                      # sonic | rotating-oscillating | manual
charging: usb-c                  # usb-c | inductive | proprietary | none
status: current                  # current | discontinued | unknown
released: 2022                   # year, optional
interfaces:
  heads: xiaomi-mes606-family    # FK to the part class interface file
interface_provenance:
  heads: inferred                # how we know the interface assignment
compatible_parts:
  heads:
    - id: xiaomi-mbs305
      provenance: manufacturer-claim
      source: "https://www.mi.com/shop/buy?product_id=1222100087"
sources:                         # general references for the entry itself
  - https://www.gizmochina.com/2022/05/31/...
notes: |
  T200 and T200C are sold as separate SKUs but share the same handle code (MES606)
  and use USB-C charging. Likely a distinct mount family from the inductive T-series.
```

## Head entry

```yaml
id: xiaomi-mbs305
brand: Xiaomi
family: Mijia
model: MBS305
aliases: []
oem: true                        # true for manufacturer originals; false for generics / clones
clones_of: null                  # if oem: false, the OEM head this clones (slug); null if no clear analog
sold_as: []                      # for generic heads, the brand names it appears under
bristle: medium                  # soft | medium | hard | varies | unknown
variant: standard                # standard | sensitive | whitening | kid | etc.
fits_devices:
  - id: xiaomi-t200
    provenance: manufacturer-claim
    source: "https://www.mi.com/shop/buy?product_id=1222100087"
measurements: null               # filled in when measured
sources: []
notes: |
  Head SKU MBS305 is weakly attested in marketplaces (sellers use the handle
  code MES606 instead). Treat the code as plausible until corroborated against
  an official Xiaomi spec page.
```

For a generic / clone head:

```yaml
id: generic-mes606-pack
brand: null                      # often unbranded or shifting white-label brands
family: null
model: null
aliases: ["MES606 heads", "Xiaomi T200 compatible heads"]
oem: false
clones_of: xiaomi-mbs305         # the OEM analog; null if unclear
sold_as: ["AOREMON", "AIBOFENG", "Niceeshop", "(many)"]
fits_devices:
  - id: xiaomi-t200
    provenance: marketplace-claim
    source: "AliExpress listings keyed on 'MES606 head'"
```

## Mount profile

```yaml
# mounts.yml
xiaomi-mes606-family:
  display_name: "Xiaomi MES606 family"
  aftermarket_aliases: [MES606]      # what AliExpress sellers search for
  charging: usb-c                    # architectural feature
  status: unmeasured                 # unmeasured | partial | measured | published-baseline
  baseline: null                     # link to published baseline when one exists
  notes: |
    T200 and T200C handles. USB-C charging architecture, likely distinct from
    the inductive MES601/MES602/MES604 family on socket geometry.
```

## Adding a second part class

A category can have multiple part classes. Add a new item under `parts:` in `data/categories.yml`, create its interface file and part directory, then add a matching key to device `interfaces:`, `interface_provenance:`, and `compatible_parts:` where that device supports the new class.

Example, abbreviated:

```yaml
openscoot:
  display_name: Electric scooters
  device:
    dir: units
    singular: Scooter
    plural: Electric scooters
  parts:
    - dir: tires
      singular: Tire
      plural: Replacement tires
      interface_file: axles.yml
      interface_singular: Axle / wheel mount
      columns: [size_etrto, tire_type]
    - dir: pads
      singular: Brake pad
      plural: Brake pads
      interface_file: calipers.yml
      interface_singular: Caliper mount
      columns: [mount_pattern, pad_compound]
```

The reciprocal field on each part remains a flat `fits_devices:` list because the part's directory already identifies its class.

## Adding an entry

The data layer is best-effort. Anyone can open a PR adding a YAML file. CI validates against the schema (TODO). Until then, hand-validate against `README.md` examples.

What we want:

- New handles or heads, OEM or generic, with at least one verifiable source per compatibility claim
- Corrections to existing entries, with the new source
- Upgrades from `manufacturer-claim` to `measured` once the project measures something

What we do not want:

- "Best of" picks, brand opinions, taste calls (handle finish, bristle stiffness preference, packaging)
- Unsourced compatibility claims
- Marketing copy
