# Project overview

Open Consumables is a measurement archive for everyday hardware. The output is a small set of dated, measured baselines for the mechanical interfaces buyers care about, published so anyone can keep buying, printing, or batch-producing to fit.

## What we do

- **Reference**: maintain a device-level knowledge graph for the categories we cover (one page per handle, one per head, with per-claim provenance). Best-effort coverage; community contributions welcome. A device has a page whether we have measured it yet or not.
- **Measure**: pick a consumable category with an undocumented de facto compatibility standard, take real measurements with disclosed methodology. Measurement upgrades a claim's provenance from "manufacturer" or "marketplace" to "measured by us."
- **Publish**: release dated baselines as plain markdown, CAD where useful, and reference data buyers and aftermarket producers can verify.
- **Freeze**: a baseline is a snapshot, not a moving target. New baseline, new date.

## What we don't do

- **Manufacture or certify**: we describe what already exists in the wild.
- **Curate or pick winners**: we don't decide which brand is the "right" one.
- **Steward standards**: we publish baselines, not ongoing governance regimes.
- **Build network-effect platforms**: substitutability of supply is the goal, not lock-in to our spec.

## Categories we work on

A category only qualifies if all three are true:

1. **The spec is complete.** Geometry, material, mechanical interface, measurable performance capture what buyers care about. If value lives in fit, taste, feel, or fashion, it's out of scope.
2. **The buyer has opted out of choice.** Either institutionally (procurement, hospitals) or self-imposed (rebuy what worked last time).
3. **Rebuyability beats novelty.** The buyer wants the same thing in ten years more than they want a new version this year.

**Pass**: toothbrush heads, air filters, water filters, vacuum consumables, fasteners, generic OTC consumables, hospital consumables.

**Fail**: pants, cosmetics, food, fashion, anything where the value is the act of choosing.

## How adoption is supposed to work

Three plausible adoption mechanics, in order of how much weight they carry near-term:

1. **Rebuyability** (consumer wedge): buyers who've already chosen what they want and want to buy the same thing in five and ten years.
2. **Convergence** (manufacturer + aftermarket wedge): aftermarket vocabulary already exists for many Chinese-IoT brands. We formalize and measure what's already in active use.
3. **Procurement** (institutional wedge): buyers who write specs into RFPs. Already how hospital consumables work. Phase 4+ question.

We bet on (1) and (2) during R&D. We do not assume USB-C-style network-effect adoption.

## Status

Pre-product. The pilot category is electric toothbrush heads. Most categories are scaffolded but not yet active. See [Categories](../categories/index.md) for current work.
