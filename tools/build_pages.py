"""Generate device and part reference pages for every category in data/categories.yml.

Run manually:

    python3 tools/build_pages.py

For each category, expects:

    data/<slug>/<device.dir>/*.yml    one file per device (e.g. handle, unit)
    data/<slug>/<part.dir>/*.yml      one file per part (e.g. head, filter)
    data/<slug>/<interface.file>      mount / slot / interface profiles

Output goes to:

    docs/categories/<slug>/<device.dir>/*.md
    docs/categories/<slug>/<part.dir>/*.md

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


REQUIRED_CATEGORY_PATHS = (
    ("device", "dir"),
    ("part", "dir"),
    ("interface", "file"),
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
    return raw


def load_category_data(cfg: dict) -> tuple[dict, dict, dict]:
    slug = cfg["slug"]
    cat_dir = DATA / slug
    interface_file = cat_dir / cfg["interface"]["file"]
    interfaces = (
        yaml.safe_load(interface_file.read_text(encoding="utf-8")) or {}
        if interface_file.exists()
        else {}
    )
    devices = {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in (cat_dir / cfg["device"]["dir"]).glob("*.yml")
    }
    parts = {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in (cat_dir / cfg["part"]["dir"]).glob("*.yml")
    }
    return interfaces, devices, parts


def part_link(part_id: str, parts: dict, cfg: dict) -> str:
    part = parts.get(part_id)
    if not part:
        return f"`{part_id}` (no entry)"
    label = part.get("model") or (part.get("aliases") or [part_id])[0]
    brand = part.get("brand") or "Generic"
    return f"[{brand} {label}](../{cfg['part']['dir']}/{part_id}.md)"


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


def render_part_facts(part: dict, cfg: dict) -> list[str]:
    facts: list[str] = []
    facts.append("OEM" if part.get("oem") else "Generic / clone")
    if part.get("clones_of"):
        facts.append(f"Clones: `{part['clones_of']}`")
    if cfg["slug"] == "toothbrushes":
        facts.append(f"Bristle: {part.get('bristle', 'unknown')}")
    if cfg["slug"] == "openair":
        if part.get("hepa_grade"):
            facts.append(f"HEPA: {part['hepa_grade']}")
        if part.get("media"):
            facts.append(f"Media: {part['media']}")
        if part.get("lifespan_months"):
            facts.append(f"Lifespan: ~{part['lifespan_months']} months")
    if cfg["slug"] == "openscoot":
        if part.get("size_etrto"):
            facts.append(f"Size (ETRTO): {part['size_etrto']}")
        if part.get("tire_type"):
            facts.append(f"Type: {part['tire_type']}")
        if part.get("tube"):
            facts.append(f"Tube: {part['tube']}")
        if part.get("tread_pattern"):
            facts.append(f"Tread: {part['tread_pattern']}")
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


def render_device(device: dict, interfaces: dict, parts: dict, cfg: dict) -> str:
    interface_key = device.get("interface") or device.get("mount")
    interface = interfaces.get(interface_key or "", {})
    interface_label = interface.get(
        "display_name", interface_key or "pending measurement"
    )
    interface_singular = cfg["interface"]["singular"]

    out = [GENERATED_BANNER]
    out.append(f"# {device['brand']} {device['model']}")
    out.append("")

    facts = render_facts(device, cfg)
    interface_prov = lookup_provenance(
        device.get("interface_provenance") or device.get("mount_provenance"),
        f"{cfg['slug']} device {device.get('id', '?')}: interface_provenance",
    )
    facts.append(f"{interface_singular}: **{interface_label}** ({interface_prov})")
    if device.get("released"):
        facts.append(f"Released: {device['released']}")
    if device.get("status"):
        facts.append(f"Status: {device['status']}")
    out.append(" · ".join(facts))
    out.append("")

    if device.get("aliases"):
        out.append(f"Also sold as: {', '.join(device['aliases'])}")
        out.append("")

    section_label = cfg["device"].get("section_label", cfg["part"]["plural"])
    extra_columns = cfg.get("part_columns", [])
    column_labels = cfg.get("part_column_labels", {})

    out.append(f"## {section_label}")
    out.append("")
    part_singular = cfg["part"]["singular"]
    headers = [
        part_singular,
        "OEM",
        *[column_labels.get(c, c.replace("_", " ").title()) for c in extra_columns],
        "Provenance",
        "Measured?",
    ]
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "---|" * len(headers))

    device_id = device.get("id", "?")
    compat_key = "compatible_parts" if "compatible_parts" in device else "compatible_heads"
    for c in device.get(compat_key, []) or []:
        if "id" not in c:
            ERRORS.append(
                f"{cfg['slug']} device {device_id}: {compat_key} entry missing id: {c}"
            )
            continue
        part = parts.get(c["id"])
        oem = "?" if part is None else ("OEM" if part.get("oem") else "Generic")
        measured = "?" if part is None else ("Yes" if part.get("measurements") else "No")
        col_values = [part_column_value(part, col) for col in extra_columns]
        provenance = lookup_provenance(
            c.get("provenance"),
            f"{cfg['slug']} device {device_id} -> part {c['id']}",
        )
        row = [part_link(c["id"], parts, cfg), oem, *col_values, provenance, measured]
        out.append("| " + " | ".join(row) + " |")
    out.append("")

    if interface and interface.get("display_name"):
        out.append(f"## {interface_singular}: {interface['display_name']}")
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


def render_part(part: dict, devices: dict, cfg: dict) -> str:
    out = [GENERATED_BANNER]
    brand = part.get("brand") or "Generic"
    model = part.get("model") or (part.get("aliases") or ["(unbranded)"])[0]
    out.append(f"# {brand} {model}")
    out.append("")

    facts = render_part_facts(part, cfg)
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
    fits_key = "fits_devices" if "fits_devices" in part else "fits_handles"
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
        part_dir = PAGES_ROOT / slug / cfg["part"]["dir"]
        device_dir.mkdir(parents=True, exist_ok=True)
        part_dir.mkdir(parents=True, exist_ok=True)

        for did, d in devices.items():
            (device_dir / f"{did}.md").write_text(
                render_device(d, interfaces, parts, cfg), encoding="utf-8"
            )
            print(f"wrote {slug}/{cfg['device']['dir']}/{did}.md")

        for pid, p in parts.items():
            (part_dir / f"{pid}.md").write_text(
                render_part(p, devices, cfg), encoding="utf-8"
            )
            print(f"wrote {slug}/{cfg['part']['dir']}/{pid}.md")

    if ERRORS:
        print(f"\n{len(ERRORS)} data error(s):", file=sys.stderr)
        for e in ERRORS:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
