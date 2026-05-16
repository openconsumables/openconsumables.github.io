"""Generate device and part reference pages for every category in data/categories.yml.

Run manually:

    python3 tools/build_pages.py

For each category, expects:

    data/<slug>/<device.dir>/*.yml    one file per device (e.g. handle, unit)
    data/<slug>/<part.dir>/*.yml      one file per part class item
    data/<slug>/<interface_file>      interface profiles for each part class

Output goes to:

    docs/categories/<slug>/<device.dir>/*.md
    docs/categories/<slug>/<part.dir>/*.md for every part class

Pages declare themselves generated at the top. Do not hand-edit them.

Category-specific fact rendering (e.g. Mode/Charging for toothbrush handles,
Bristle for toothbrush heads) is driven by per-category render helpers below.
When adding a category, add its config to data/categories.yml and add a small
render block here if the standard fact set doesn't fit.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not installed; pip install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PAGES_ROOT = ROOT / "docs" / "categories"

GENERATED_BANNER = (
    "<!-- generated from data/. Do not hand-edit; run tools/build_pages.py -->\n"
)

PROVENANCE_LABEL = {
    "measured": "Measured",
    "manufacturer-claim": "Manufacturer claim",
    "community-reported": "Community report",
    "marketplace-claim": "Marketplace listing",
    "inferred": "Inferred",
}

ERRORS: list[str] = []


def lookup_provenance(value: str | None, where: str) -> str:
    if value is None:
        ERRORS.append(f"{where}: missing provenance")
        return "?"
    if value not in PROVENANCE_LABEL:
        ERRORS.append(f"{where}: unknown provenance {value!r}")
        return value
    return PROVENANCE_LABEL[value]


REQUIRED_CATEGORY_PATHS = (("device", "dir"),)

REQUIRED_PART_KEYS = (
    "dir",
    "singular",
    "plural",
    "interface_file",
    "interface_singular",
)


def load_categories() -> dict[str, dict]:
    path = DATA / "categories.yml"
    if not path.exists():
        sys.exit(f"missing {path}; add it before running the generator")
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    for slug, cfg in raw.items():
        cfg["slug"] = slug
        for keys in REQUIRED_CATEGORY_PATHS:
            node: Any = cfg
            for k in keys:
                if not isinstance(node, dict) or k not in node:
                    sys.exit(f"category {slug}: missing {'.'.join(keys)} in categories.yml")
                node = node[k]
        if not isinstance(cfg.get("parts"), list) or not cfg["parts"]:
            sys.exit(f"category {slug}: missing non-empty parts list in categories.yml")
        seen_dirs: set[str] = set()
        for part_cfg in cfg["parts"]:
            if not isinstance(part_cfg, dict):
                sys.exit(f"category {slug}: part class is not a mapping")
            for key in REQUIRED_PART_KEYS:
                if key not in part_cfg:
                    sys.exit(f"category {slug}: part class missing {key}")
            if part_cfg["dir"] in seen_dirs:
                sys.exit(f"category {slug}: duplicate part dir {part_cfg['dir']}")
            seen_dirs.add(part_cfg["dir"])
    return raw


def load_category_data(cfg: dict) -> tuple[dict, dict, dict]:
    slug = cfg["slug"]
    cat_dir = DATA / slug
    interfaces = {}
    parts = {}
    for part_cfg in cfg["parts"]:
        part_dir = part_cfg["dir"]
        interface_file = cat_dir / part_cfg["interface_file"]
        interfaces[part_dir] = (
            yaml.safe_load(interface_file.read_text(encoding="utf-8")) or {}
            if interface_file.exists()
            else {}
        )
        parts[part_dir] = {
            p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
            for p in (cat_dir / part_dir).glob("*.yml")
        }
    devices = {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in (cat_dir / cfg["device"]["dir"]).glob("*.yml")
    }
    return interfaces, devices, parts


def part_link(part_id: str, parts: dict, part_cfg: dict) -> str:
    part = parts.get(part_id)
    if not part:
        return f"`{part_id}` (no entry)"
    label = part.get("model") or (part.get("aliases") or [part_id])[0]
    brand = part.get("brand") or "Generic"
    return f"[{brand} {label}](../{part_cfg['dir']}/{part_id}.md)"


def device_link(device_id: str, devices: dict, cfg: dict) -> str:
    device = devices.get(device_id)
    if not device:
        return f"`{device_id}` (no entry)"
    brand = device.get("brand") or ""
    model = device.get("model") or device_id
    label = f"{brand} {model}".strip()
    return f"[{label}](../{cfg['device']['dir']}/{device_id}.md)"


def render_facts(device: dict, cfg: dict) -> list[str]:
    """Return the inline fact list shown under the H1, category-aware."""
    facts: list[str] = []
    slug = cfg["slug"]
    if slug == "toothbrushes":
        if device.get("aftermarket_anchor"):
            facts.append(f"Aftermarket code: `{device['aftermarket_anchor']}`")
        facts.append(f"Mode: {device.get('mode', 'unknown')}")
        facts.append(f"Charging: {device.get('charging', 'unknown')}")
    elif slug == "openair":
        if device.get("aftermarket_anchor"):
            facts.append(f"Aftermarket code: `{device['aftermarket_anchor']}`")
        if device.get("cadr_m3h"):
            facts.append(f"CADR: {device['cadr_m3h']} m³/h")
        if device.get("room_size_m2"):
            facts.append(f"Room rating: {device['room_size_m2']} m²")
        if device.get("filter_stages"):
            facts.append(f"Stages: {device['filter_stages']}")
    elif slug == "openscoot":
        if device.get("aftermarket_anchor"):
            facts.append(f"Aftermarket code: `{device['aftermarket_anchor']}`")
        if device.get("wheel_size_in"):
            facts.append(f"Wheel: {device['wheel_size_in']}\"")
        if device.get("motor_w"):
            facts.append(f"Motor: {device['motor_w']} W")
        if device.get("weight_class_kg"):
            facts.append(f"Weight: ~{device['weight_class_kg']} kg")
    else:
        if device.get("aftermarket_anchor"):
            facts.append(f"Aftermarket code: `{device['aftermarket_anchor']}`")
    return facts


def render_part_facts(part: dict, cfg: dict, part_cfg: dict) -> list[str]:
    facts: list[str] = []
    facts.append("OEM" if part.get("oem") else "Generic / clone")
    if part.get("clones_of"):
        facts.append(f"Clones: `{part['clones_of']}`")
    part_dir = part_cfg["dir"]
    if cfg["slug"] == "toothbrushes":
        facts.append(f"Bristle: {part.get('bristle', 'unknown')}")
    if cfg["slug"] == "openair":
        if part.get("hepa_grade"):
            facts.append(f"HEPA: {part['hepa_grade']}")
        if part.get("media"):
            facts.append(f"Media: {part['media']}")
        if part.get("lifespan_months"):
            facts.append(f"Lifespan: ~{part['lifespan_months']} months")
    if cfg["slug"] == "openscoot" and part_dir == "tires":
        if part.get("size_etrto"):
            facts.append(f"Size (ETRTO): {part['size_etrto']}")
        if part.get("tire_type"):
            facts.append(f"Type: {part['tire_type']}")
        if part.get("tube"):
            facts.append(f"Tube: {part['tube']}")
        if part.get("tread_pattern"):
            facts.append(f"Tread: {part['tread_pattern']}")
    if cfg["slug"] == "openscoot" and part_dir == "pads":
        if part.get("mount_pattern"):
            facts.append(f"Caliper mount: {part['mount_pattern']}")
        if part.get("pad_compound"):
            facts.append(f"Compound: {part['pad_compound']}")
    if cfg["slug"] == "openscoot" and part_dir == "rotors":
        if part.get("rotor_diameter_mm"):
            facts.append(f"Diameter: {part['rotor_diameter_mm']} mm")
        if part.get("bolt_pattern"):
            facts.append(f"Bolt pattern: {part['bolt_pattern']}")
    if part.get("variant"):
        facts.append(f"Variant: {part['variant']}")
    return facts


def part_column_value(part: dict | None, column: str) -> str:
    if part is None:
        return "?"
    value = part.get(column)
    if value is None:
        return "?"
    return str(value)


def compatibility_entries(device: dict, part_cfg: dict) -> list[dict]:
    part_dir = part_cfg["dir"]
    raw = device.get("compatible_parts")
    if isinstance(raw, dict):
        return raw.get(part_dir, []) or []
    return []


def interface_assignment(device: dict, part_cfg: dict) -> tuple[str | None, str | None]:
    part_dir = part_cfg["dir"]
    interfaces = device.get("interfaces")
    if isinstance(interfaces, dict):
        interface_key = interfaces.get(part_dir)
    else:
        interface_key = device.get("interface") or device.get("mount")

    provenances = device.get("interface_provenance")
    if isinstance(provenances, dict):
        provenance = provenances.get(part_dir)
    else:
        provenance = device.get("interface_provenance") or device.get("mount_provenance")
    return interface_key, provenance


def render_device(device: dict, interfaces: dict, parts: dict, cfg: dict) -> str:
    out = [GENERATED_BANNER]
    out.append(f"# {device['brand']} {device['model']}")
    out.append("")

    facts = render_facts(device, cfg)
    if device.get("released"):
        facts.append(f"Released: {device['released']}")
    if device.get("status"):
        facts.append(f"Status: {device['status']}")
    out.append(" · ".join(facts))
    out.append("")

    if device.get("aliases"):
        out.append(f"Also sold as: {', '.join(device['aliases'])}")
        out.append("")

    device_id = device.get("id", "?")
    for part_cfg in cfg["parts"]:
        part_dir = part_cfg["dir"]
        entries = compatibility_entries(device, part_cfg)
        interface_key, interface_provenance = interface_assignment(device, part_cfg)
        interface = interfaces.get(part_dir, {}).get(interface_key or "", {})

        if not entries and not interface_key:
            continue

        section_label = cfg["device"].get("section_label", part_cfg["plural"])
        extra_columns = part_cfg.get("columns", [])
        column_labels = part_cfg.get("column_labels", {})

        out.append(f"## {section_label}")
        out.append("")
        part_singular = part_cfg["singular"]
        headers = [
            part_singular,
            "OEM",
            *[column_labels.get(c, c.replace("_", " ").title()) for c in extra_columns],
            "Provenance",
            "Measured?",
        ]
        out.append("| " + " | ".join(headers) + " |")
        out.append("|" + "---|" * len(headers))

        for c in entries:
            if "id" not in c:
                ERRORS.append(
                    f"{cfg['slug']} device {device_id}: {part_dir} entry missing id: {c}"
                )
                continue
            part = parts.get(part_dir, {}).get(c["id"])
            oem = "?" if part is None else ("OEM" if part.get("oem") else "Generic")
            measured = "?" if part is None else ("Yes" if part.get("measurements") else "No")
            col_values = [part_column_value(part, col) for col in extra_columns]
            provenance = lookup_provenance(
                c.get("provenance"),
                f"{cfg['slug']} device {device_id} -> {part_dir} part {c['id']}",
            )
            row = [
                part_link(c["id"], parts.get(part_dir, {}), part_cfg),
                oem,
                *col_values,
                provenance,
                measured,
            ]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

        interface_singular = part_cfg["interface_singular"]
        if interface_key:
            interface_label = interface.get(
                "display_name", interface_key or "pending measurement"
            )
            interface_prov = lookup_provenance(
                interface_provenance,
                f"{cfg['slug']} device {device_id}: {part_dir} interface_provenance",
            )
            out.append(f"## {interface_singular}: {interface_label}")
            out.append("")
            out.append(f"Provenance: **{interface_prov}**")
        elif interface and interface.get("display_name"):
            out.append(f"## {interface_singular}: {interface['display_name']}")
            out.append("")
        out.append("")
        out.append(f"Status: **{interface.get('status', 'unknown')}**")
        if interface.get("notes"):
            out.append("")
            out.append(interface["notes"].strip())
        out.append("")

    if device.get("notes"):
        out.append("## Notes")
        out.append("")
        out.append(device["notes"].strip())
        out.append("")

    if device.get("sources"):
        out.append("## Sources")
        out.append("")
        for s in device["sources"]:
            out.append(f"- <{s}>")
        out.append("")

    return "\n".join(out)


def render_part(part: dict, devices: dict, cfg: dict, part_cfg: dict) -> str:
    out = [GENERATED_BANNER]
    brand = part.get("brand") or "Generic"
    model = part.get("model") or (part.get("aliases") or ["(unbranded)"])[0]
    out.append(f"# {brand} {model}")
    out.append("")

    facts = render_part_facts(part, cfg, part_cfg)
    out.append(" · ".join(facts))
    out.append("")

    if part.get("aliases"):
        out.append(f"Also sold as: {', '.join(part['aliases'])}")
        out.append("")
    if part.get("sold_as"):
        out.append(f"Brand names seen: {', '.join(part['sold_as'])}")
        out.append("")

    out.append(f"## Fits {cfg['device']['plural'].lower()}")
    out.append("")
    out.append(f"| {cfg['device']['singular']} | Provenance |")
    out.append("|---|---|")
    part_id = part.get("id", "?")
    fits_key = "fits_devices"
    for f in part.get(fits_key, []) or []:
        if "id" not in f:
            ERRORS.append(
                f"{cfg['slug']} part {part_id}: {fits_key} entry missing id: {f}"
            )
            continue
        provenance = lookup_provenance(
            f.get("provenance"),
            f"{cfg['slug']} part {part_id} -> device {f['id']}",
        )
        out.append(f"| {device_link(f['id'], devices, cfg)} | {provenance} |")
    out.append("")

    if part.get("measurements"):
        out.append("## Measurements")
        out.append("")
        for k, v in part["measurements"].items():
            out.append(f"- **{k}**: {v}")
        out.append("")

    if part.get("notes"):
        out.append("## Notes")
        out.append("")
        out.append(part["notes"].strip())
        out.append("")

    if part.get("sources"):
        out.append("## Sources")
        out.append("")
        for s in part["sources"]:
            out.append(f"- <{s}>")
        out.append("")

    return "\n".join(out)


def main() -> None:
    categories = load_categories()
    if not categories:
        sys.exit("data/categories.yml is empty or missing")

    for slug, cfg in categories.items():
        interfaces, devices, parts = load_category_data(cfg)
        device_dir = PAGES_ROOT / slug / cfg["device"]["dir"]
        device_dir.mkdir(parents=True, exist_ok=True)

        for did, d in devices.items():
            (device_dir / f"{did}.md").write_text(
                render_device(d, interfaces, parts, cfg), encoding="utf-8"
            )
            print(f"wrote {slug}/{cfg['device']['dir']}/{did}.md")

        for part_cfg in cfg["parts"]:
            part_dir_name = part_cfg["dir"]
            part_dir = PAGES_ROOT / slug / part_dir_name
            part_dir.mkdir(parents=True, exist_ok=True)
            for pid, p in parts.get(part_dir_name, {}).items():
                (part_dir / f"{pid}.md").write_text(
                    render_part(p, devices, cfg, part_cfg), encoding="utf-8"
                )
                print(f"wrote {slug}/{part_dir_name}/{pid}.md")

    if ERRORS:
        print(f"\n{len(ERRORS)} data error(s):", file=sys.stderr)
        for e in ERRORS:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
