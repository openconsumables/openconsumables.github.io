# Toothbrush ecosystem

The electric toothbrush market splits cleanly into two clusters with very different compatibility behaviours.

## Chinese-IoT cluster (anchor exists)

Engineering-flat brand naming, regulatory filings that print model codes, and a Shenzhen aftermarket that adopts those codes as fitment identifiers. The buyer-side compatibility anchor is already in active use; we just need to formalize and measure it.

| Brand | Anchor strength | Notes |
|-------|-----------------|-------|
| Xiaomi / Mijia | Strong | T-series handles use `MES60x` codes printed on the device, leaked through CCC filings, adopted by aftermarket. Pilot ecosystem. |
| Soocas | Strong | Sequential model codes; large aftermarket presence on AliExpress. |
| Oclean | Strong | Same pattern. |
| Bitvae | Strong | Same pattern. |
| Usmile | Medium | Pattern present but less aftermarket convergence than the above. |

These are the candidates where the convergence-led wedge is viable. The pilot work focuses on **Xiaomi T-series**.

## Western brand cluster (no anchor)

Marketing names deliberately do not encode compatibility class. Buyers cannot tell from the device which heads fit. The convergence wedge is closed for these brands; they can only be addressed via the rebuyability or procurement wedges.

| Brand | Anchor | Why not |
|-------|--------|---------|
| Oral-B (classic + iO) | None | Marketing names (`iO9`, `Pro 1000`, `Genius`); deliberate fragmentation. |
| Philips Sonicare | None | Marketing names dominate. |
| Foreo Issa | None | Single-brand-locked silicone heads. |
| Quip | None | Subscription-locked. |
| Burst | None | Marketing-led. |
| Colgate | None | Marketing-led. |

These are documented for context but are not viable convergence-wedge targets. We treat them as comparison material when discussing why the Chinese-IoT cluster is operationally different.

## Generic aftermarket

Independently of any brand, a large pool of generic replacement heads exists that target one or more of the anchor codes (`MES601`, `MES603`, `MES606`, etc.). These are the entities whose actual mechanical behaviour decides whether the de facto compatibility class holds.

The pilot baseline must be measured against both genuine and aftermarket samples, because the aftermarket vocabulary is what buyers are searching with.

## What's not on this list

- **Oral-B-compatible aftermarket** without a discoverable buyer-side anchor: out of scope for the convergence wedge.
- **Brands without aftermarket convergence**: documented in the ecosystem map only if they help explain a boundary, not because we plan to measure them.

## Source for the active list

Detailed per-ecosystem notes (sources, model lineage, SKU maps) live in the project repository under `openbrush/ecosystems/`. This page is the public-facing summary; the per-ecosystem files are the working notes.
