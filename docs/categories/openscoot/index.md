# Electric scooters

Working name: **OpenScoot**. The third category in the Open Consumables device knowledge graph.

## What's here

- **[Units](units/index.md)**, the scooters themselves, with replacement tires, brake wear parts, tubes, and grip tape listed by interface.
- **[Tires](tires/index.md)**, OEM and aftermarket pneumatic, tubeless self-healing, and solid honeycomb formats, with the scooters they fit.
- **[Brake pads](pads/index.md)**, disc-brake pads for pad-bearing scooter calipers, with drum shoes kept separate.
- **[Drum brake shoes](shoes/index.md)**, front-drum friction assemblies for the Segway-Ninebot Max G30 family.
- **[Inner tubes](tubes/index.md)**, replacement tubes for tubed pneumatic tires in the Xiaomi 8.5-inch slot.
- **[Rotors](rotors/index.md)**, disc-brake rotors keyed to diameter and bolt pattern.
- **[Grip tape](grip-tape/index.md)**, pre-cut adhesive foot mats for scooter deck profiles.

## Status

**Reference layer only.** OpenScoot is a deferred measurement subproject; activation depends on OpenBrush producing a published measured baseline first. Until then, this category exists as a knowledge-graph stub: provenance-tagged compatibility data sourced from manufacturer pages and aftermarket listings, with no project measurement claims.

Coverage is intentionally small: the Xiaomi 8.5-inch family (M365, Mi Electric Scooter 3) and the Segway-Ninebot Max G30 10-inch slot, with a handful of tire, tube, brake-pad, drum-brake, rotor, and grip-tape entries. Pull requests welcome; see [the data README](https://github.com/openconsumables/openconsumables.github.io/blob/master/data/README.md) for the schema.

## Scope

**In scope** for the reference layer:

- Chinese-IoT cluster consumer e-scooters (Xiaomi, Segway-Ninebot)
- the wheel / axle / rim interface between scooter and tire
- ETRTO / imperial size, tire type (pneumatic, self-healing, solid honeycomb), tubed vs tubeless, as disclosed by the manufacturer or marketplace
- the caliper / pad interface for stock disc-brake scooters, as disclosed by the manufacturer, repair communities, or marketplace listings
- the drum / shoe interface for stock drum-brake scooters, as disclosed by the manufacturer, repair communities, or marketplace listings
- inner tubes for tubed pneumatic tires, keyed to the same axle / wheel-mount slot as the matching tire
- brake discs / rotors where diameter and bolt-pattern claims are discoverable
- pre-cut adhesive deck grip tape / foot mats where sellers identify a scooter-specific deck profile

**Out of scope** at this stage:

- ride-quality, range, top-speed, or climb-angle claims
- independent verification of motor power, weight, or wheel-size specs (manufacturer claims only, until measured)
- battery packs (different regulatory and safety regime; deferred per the subproject scope notes)
- generic rolls of skateboard or non-slip tape that require trimming by the buyer
- decorative deck skins where the compatibility surface is mainly aesthetic
- tubes for tubeless self-healing tires unless the unit has an explicit tubed conversion entry
- hydraulic brake upgrades and non-OEM caliper conversions
- repair parts: hinges, dashboards, fenders, lights, levers
- Western-brand scooters (Hiboy, Apollo, Gotrax, Unagi): fail the ecosystem-selection prerequisite

## A note on tire sizing

E-scooter tires sit between motorcycle and bicycle tire industries with no formal standards body for the segment. ETRTO size codes (e.g. 50-134 for 8.5x2) do apply to pneumatic e-scooter tires and are useful for cross-reference, but the broader compatibility profile (load rating for ~25 km/h e-scooter use, valve geometry, tubed vs tubeless on a non-bicycle rim) is not standardized. The slots defined here capture hub geometry on the scooter side; the tire entries capture the contact-patch side. A pair of scooters with the same axle slot can theoretically accept the same tire-on-rim assembly.

Wheel diameter is part of the slot identity. 8.5-inch and 10-inch wheels are different axles by definition.
