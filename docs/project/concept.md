# The open consumables concept

Mass-market hardware ecosystems often produce accidental open-hardware compatibility standards, **without anyone declaring them as standards**. The aftermarket discovers and maps them first; communities reverse-engineer and adapter-build; sometimes a measured baseline eventually gets published.

Open Consumables sits in that last step.

## The two paths to an accidental standard

### Path A: Regulatory-anchored (Chinese-IoT cluster)

CCC certification, GB / GB/T standards, NMPA filings, and CCEP labels print engineering model codes onto product labels and into searchable filings. Combined with engineering-flat brand naming (sequential codes like `MES60x` for Xiaomi sonic toothbrushes, `M365` for Xiaomi scooters) and a concentrated Shenzhen aftermarket that adopts those codes as fitment identifiers, this produces a buyer-side compatibility taxonomy that is already in active use, just not formalized, not measured, and not documented anywhere.

Brands in this cluster: Xiaomi, Mijia, Soocas, Oclean, Bitvae, Roborock, Smartmi, Viomi, Dreame, NIU, and similar.

Western brands generally beat this with marketing names and deliberate fragmentation. They fail the convergence test.

### Path B: Community-anchored (hobby-maker cluster)

Hobbyist and maker communities reverse-engineer, measure, document, and converge informally. The aftermarket tracks community vocabulary, adapters proliferate, sometimes a CAD repository or wiki becomes the de facto reference.

Examples: MX-compatible mechanical keyboard switches, E3D V6 / MK8 3D printer nozzle profiles, FPV drone motor-mount hole patterns, RC battery connectors (XT60, XT90), VESA mounts, Tuya module clones.

**Why our active work is mostly Path A:** Path B categories have usually already been documented by the community that converged on the standard. KbdFans, Thingiverse, the FPV community wiki, manufacturer-published RC connector catalogues already do the measurement-and-documentation work. Our value-add lives in the gap between "de facto standard exists" and "measured baseline published". For Path B that gap is mostly closed; for Path A it is mostly open.

## The existing-layer check

A category that passes our criteria can still be a poor fit if a **mature reference layer already publishes the spec / geometry / interface** that we would otherwise document. In that case we'd duplicate existing work without adding value.

The reference layer can come from either source:

- **Industry-published**: ISO, ANSI, ETRTO, DOT, JIS, GB, NSF, etc. Decades-deep spec systems.
- **Community-converged**: an active hobbyist or maker community that has already measured, documented, and published a de facto standard.

The check:

> Does either an industry-published or community-converged reference layer already cover this category's consumables?

If yes, we defer to it.

## Reference models we look up to

- **USB-C, VESA, MX-compatible, QMK**, aspirational. None happened by accident; all required either standards-body work or a sustained community effort over years.
- **ISO fasteners, generic pharma equivalents, hospital procurement catalogs**, realistic near-term mechanic. Substitutability of supply, not network effects.

We do not assume USB-C-style network effects. Toothbrush heads do not connect to other toothbrush heads. The realistic outcome is a baseline buyers, reviewers, and small aftermarket producers can voluntarily reference.

## Baselines, not standards

The output of our R&D phase is a **dated measured baseline**, not a stewarded standard. A baseline is a snapshot of measured geometry and tolerances that anyone can voluntarily reference. It does not imply that we maintain it forever, certify products against it, or run a governance process.

This reframing lowers the bar on the artifact: a snapshot one person with calipers and a methodology can credibly produce, not a multi-year governance commitment.

Stewardship is a separate decision the project may or may not take on later. For now, it is explicitly out of scope.
