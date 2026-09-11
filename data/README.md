# Device knowledge graph

This directory is the structured-data source for the device reference pages on the public site. The site is generated from these YAML files; do not hand-edit the rendered pages under generated directories such as `docs/categories/*/handles/`, `docs/categories/*/heads/`, `docs/categories/*/filters/`, `docs/categories/*/tires/`, `docs/categories/*/pads/`, `docs/categories/*/rotors/`, `docs/categories/*/tubes/`, `docs/categories/*/shoes/`, or `docs/categories/*/grip-tape/`.

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

The site renders the provenance tier and the recorded source next to each compatibility claim. A source link documents who makes the claim; it does not turn it into a project measurement. Entries with `last_reviewed` show when their sources were reviewed. That date is not a product release date or a guarantee of local stock.

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

These examples reflect the current records; seller claims remain seller claims.
T200C is not a verified alias for T200.

```yaml
id: xiaomi-t200
brand: Xiaomi
family: Mijia
model: T200
aliases:
- Mijia Sonic Electric Toothbrush T200
aftermarket_anchor: MES606
type: electric
mode: sonic
charging: usb-c
status: unknown
released: 2022
interfaces:
  heads: xiaomi-mes606-family
interface_provenance:
  heads: inferred
compatible_parts:
  heads:
  - id: xiaomi-mbs305
    provenance: marketplace-claim
    source: https://24h.pchome.com.tw/prod/DMBABO-A900H3U88
  - id: generic-mes606-pack
    provenance: marketplace-claim
    source: https://mall.iopenmall.tw/005758/index.php?action=product_detail&prod_no=P0575800305305
sources:
- https://24h.pchome.com.tw/prod/DMALG2-A900JGT0Z
- https://24h.pchome.com.tw/prod/DMBABO-A900H3U88
notes: |
  Retailer evidence identifies T200 as MES606 with USB-C charging. PChome
  lists MBS305 specifically for T200. The former numeric Xiaomi store link
  could not be verified, so the head fit is marketplace-claim. T200C is often
  co-listed by sellers but is not treated here as a verified identical handle.
  Charging architecture alone does not establish socket compatibility.
last_reviewed: '2026-09-11'
```

## Head entry

```yaml
id: xiaomi-mbs305
brand: Xiaomi
family: Mijia
model: MBS305
aliases:
- Mijia sonic electric toothbrush head, T200/T200C
oem: true
clones_of: null
sold_as: []
bristle: unknown
variant: standard
fits_devices:
- id: xiaomi-t200
  provenance: marketplace-claim
  source: https://24h.pchome.com.tw/prod/DMBABO-A900H3U88
measurements: null
sources:
- https://24h.pchome.com.tw/prod/DMBABO-A900H3U88
- https://bigmi.vn/bo-3-dau-chai-thay-the-xiaomi-mijia-sonic-t200c/
notes: |
  Multiple retailer pages identify the OEM-labelled T200 head as MBS305.
  PChome names both the code and T200 fit, but a current Xiaomi specification
  page has not been recovered. OEM identity and fit remain seller claims;
  no dimensions or head weight are published as project measurements.
last_reviewed: '2026-09-11'
```

For a generic head, use `oem: false`, record observed seller names in `sold_as`,
and use `clones_of: null` unless the OEM analogue is supported by evidence.
Each `fits_devices` claim still needs its own source and provenance.

## Mount profile

```yaml
xiaomi-mes606-family:
  display_name: "Xiaomi MES606 family"
  aftermarket_aliases: [MES606]
  charging: usb-c
  status: unmeasured
  baseline: null
  notes: |
    Working hypothesis for the T200/MES606 interface. Charging architecture
    alone does not establish socket compatibility. T200C identity is unresolved.
```

## Adding additional part classes

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
    - dir: rotors
      singular: Rotor
      plural: Replacement rotors
      interface_file: rotor_mounts.yml
      interface_singular: Rotor mount
      columns: [rotor_diameter_mm, bolt_pattern]
```

The reciprocal field on each part remains a flat `fits_devices:` list because the part's directory already identifies its class.

## Adding an entry

One sourced fact is enough. Use the [contribution guide](../docs/contributing.md)
to send a GitHub issue or prepare a copyable report without a checkout or account.
Missing devices and parts, corrections, aliases, better sources, and contradictory
fit evidence within existing categories are welcome. Broken links, typos, and
requests to verify existing claims need no replacement source.

Complete patches are welcome too. Maintainers classify evidence and preserve its
limits, update reciprocal `compatible_parts` and `fits_devices` claims, regenerate
with `python3 tools/build_pages.py`, and update navigation for new pages. Run
`mkdocs build --strict` for a patch. Automated schema validation is not yet in place.
A source link alone does not establish physical verification.

No buying recommendations, brand opinions, unsourced fit claims, or marketing copy.
