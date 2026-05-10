# Compatibility and head families

A "head family" is a set of heads and handles that share a mechanical interface tightly enough to interchange in practice. We document families using the **vocabulary buyers already use**, which means handle-level codes for the Chinese-IoT cluster.

## Naming

Public-facing baselines follow this pattern:

> `Open Consumables Toothbrush Head Interface: <profile> Baseline, <date>`

Examples:

- `Open Consumables Toothbrush Head Interface: T-Series Profile, 2026-Q3 Baseline`

We use **profile** to mean "our measured compatibility target," not "an official manufacturer standard." Baselines are dated snapshots, not living standards.

We do **not** publish `Toothbrush Head Interface v1` as a broad cross-family spec. There isn't enough cross-family measurement evidence to justify that, and a number-stable name would imply ongoing stewardship we have not signed up for.

## Why anchor on handle codes, not internal head SKUs

Aftermarket sellers tag replacement heads by **handle product code** (`MES601`, `MES603`, `MES606`), not by Xiaomi's internal head SKU (`MBS301`, etc.). The internal head SKUs are mostly invisible to marketplace search.

Naming our baselines after handle codes plugs straight into the search terms buyers already use. Naming them after internal head SKUs floats above buyers' heads.

## Active families under measurement

### Xiaomi T-series

Pilot family. Handle anchor codes appear on the device label and in CCC filings.

| Handle code | Common product names | Status |
|-------------|---------------------|--------|
| `MES601` | T100, T300 | Most-bought aftermarket target |
| `MES603` | T500 | Track 13 found multi-factory convergence; needs Batch A confirmation |
| `MES606` | T700, related | Aftermarket vocabulary widely used |

Open question, gating the first published baseline: do HOVEY/Meihong's T500 socket, Meitianlai/Ledi's T500 socket, and the official Xiaomi DDYST01SKS socket actually match within tolerance? Three samples decide whether the convergence is mechanical or marketing.

## Families documented but not yet measured

| Ecosystem | Anchor | Why deferred |
|-----------|--------|--------------|
| Soocas | Sequential model codes | Awaiting Xiaomi pilot to land a published baseline first |
| Oclean | Sequential model codes | Same |
| Bitvae | Sequential model codes | Same |

## What gets measured

For each family:

- shaft geometry (length, diameter, taper)
- anti-rotation feature
- retention force (axial pull-out)
- vibration coupler geometry
- bore tolerances
- material identification where load-bearing

Methodology is disclosed alongside results. GB/T 40362-2021 (5 N or 15 N axial, 0.05 N m or 0.15 N m torque) is the reconciliation point for retention thresholds.

## What we don't claim

- That a measured baseline is what the manufacturer intends. It's what we measured.
- That a baseline applies to anything outside the dated samples we measured.
- That heads claimed compatible with a baseline are actually compatible. Anyone can self-test against the published methodology.
