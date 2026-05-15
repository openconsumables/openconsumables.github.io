# Categories

Open Consumables works one **measurement** programme at a time. The pilot is electric toothbrush heads. The public **reference layer** (the device knowledge graph: per-device pages with provenance-tagged compatibility) extends to other categories ahead of measurement, so an agent searching "replacement for my Xiaomi 3H" lands somewhere useful.

## Active

| Category | Working name | Stage |
|----------|--------------|-------|
| [Electric toothbrush heads](toothbrushes/index.md) | OpenBrush | Phase 2: physical measurement |
| [Air purifier filters](openair/index.md) | OpenAir | Reference layer only (no measurement programme) |

## Deferred

The categories below are scaffolded as placeholders. None have reference-layer or measurement coverage yet. Each measurement programme activates only after the pilot has produced a published measured baseline AND the category has been explicitly chosen as the next step.

| Category | Working name | Why it's a candidate |
|----------|--------------|----------------------|
| Water purifier cartridges | OpenWater | Multi-stage scope (PP / carbon / RO); each stage may need its own profile |
| Robot vacuum consumables | OpenVac | Heterogeneous mix (4-5 classes per device); widest scope |
| Electric razor heads | OpenShave | Tightest scope; potential fast second proof-of-pattern |
| Electric scooter parts | OpenScoot | Strong M365 / Pro / Essential / 4-series anchor; battery packs out of scope |
| Humidifier filters / wicks | OpenMist | Lowest priority; aftermarket may be too thin |

## Why this list and not a longer one

Each category passes three gates:

1. **Category-fit**, spec is complete, buyer has opted out of choice, rebuyability beats novelty.
2. **Existing-layer check**, no mature industry or community reference layer already documents the geometry. (This rules out bicycles, motorcycles, mechanical keyboards, 3D printer nozzles, RC connectors.)
3. **Ecosystem-selection prerequisite**, for the convergence-led wedge, a discoverable buyer-side compatibility anchor must already exist. (This rules out Oral-B, Sonicare, most Western IoT brands for the convergence path.)

Categories that don't pass all three are out of scope, even when they superficially look like good candidates.

See [the concept](../project/concept.md) for the underlying framing.
