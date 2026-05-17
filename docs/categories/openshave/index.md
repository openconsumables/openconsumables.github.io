# Electric shavers

Working name: **OpenShave**. The fourth category in the Open Consumables device knowledge graph.

## What's here

- **[Units](units/index.md)**, the shaver bodies themselves, with replacement heads or cassettes listed by mount family.
- **[Heads](heads/index.md)**, OEM and aftermarket rotary three-blade head modules, with the shavers they fit.
- **[Foil cassettes](cassettes/index.md)**, reciprocating multi-blade cassettes for foil shavers (Xiaomi Mi 5-Blade family).

## Status

**Reference layer only.** OpenShave is not yet an active measurement subproject; activation depends on OpenBrush producing a published measured baseline first. Until then, this category exists as a knowledge-graph stub: provenance-tagged compatibility data sourced from manufacturer pages and aftermarket listings, with no project measurement claims.

The proposed first-baseline target if OpenShave does activate is the Xiaomi / Mijia S300 / S500 / S500C rotary 3-blade head family, with ENCHEN BR-1 as the strongest alternative. The synthesis behind that recommendation lives in the R&D workspace and is not republished here.

Coverage is intentionally small: rotary 3-blade families across Xiaomi / Mijia, ENCHEN, Soocas, ShowSee, and Riwa, plus a single foil cassette family (Xiaomi Mi 5-Blade). Cleaning-station cartridges are out of scope for now; most Chinese-IoT shavers in the desk-pass mapping do not have a cleaning dock. Pull requests welcome; see [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema.

## Scope

**In scope** for the reference layer:

- Chinese-IoT cluster consumer electric shavers (Xiaomi / Mijia, Soocas, ShowSee, ENCHEN, Riwa)
- the mechanical head-mount interface between body and replacement head, including drive socket / shaft geometry, latch / magnetic retention, and cutter-pod outer envelope as identification dimensions
- rotary three-blade heads, tracked under the `heads` part class
- reciprocating foil cassettes (Xiaomi Mi 5-Blade family), tracked under the separate `cassettes` part class
- buyer-visible device codes, head codes, and aftermarket fitment vocabulary, where the manufacturer or marketplace surfaces them

**Out of scope** at this stage:

- shave quality, wet / dry performance, motor power, battery life, irritation claims, styling preferences
- independent verification of head count, head type, or material claims (manufacturer / marketplace copy only, until measured)
- Western-brand shavers (Philips Norelco, Braun, Panasonic, Remington): fail the ecosystem-selection prerequisite
- non-shaving attachments (nose trimmers, sideburn trimmers, cleansing brushes, blackhead brushes, combs)
- cleaning station / dock cartridges until a dedicated slice ships
- battery packs, motor electronics, app integration, and any clone-ready geometry

## A note on head-mount families

Rotary three-blade shavers from different brands look similar but do not necessarily share a head mount. The OpenShave reference layer uses family-specific working slot names (`xiaomi-mijia-s300-s500-rotary`, `enchen-br1-rotary`, `riwa-ra-rotary`, etc.) rather than a single "rotary 3-blade universal" class because cross-brand convergence is not strong enough to justify a single class at this stage.

Within a brand, marketplaces sometimes group several device codes under one replacement head ("S300 / S500 / MJTXD01SKS 通用机头", "Fit for SOOCAS S3 S5"). Those cross-fit claims are usually `marketplace-claim` until corroborated by a manufacturer accessory page or measurement.

Some seller titles also encode mechanical clues that have not yet been measured. Two examples that recur in the desk evidence:

- The phrases `五角形转轴口` and `内5角` ("five-sided drive-socket / shaft-mouth") in Xiaomi S300 / S500 listings.
- The phrase `四瓣旋转式接口` ("four-petal rotary interface") in Riwa RA-5505 aftermarket listings.

Both are preserved in the slot notes as measurement targets. They are not republished here as geometry claims.
