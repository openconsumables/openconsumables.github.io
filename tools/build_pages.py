"""Generate handle and head reference pages from data/*.yml.

Spike implementation. Not yet wired into the mkdocs build. Run manually:

    python tools/build_pages.py

Output goes to docs/categories/toothbrushes/handles/*.md and
docs/categories/toothbrushes/heads/*.md (overwritten). Pages declare themselves
generated at the top.

The data files under data/ are the source of truth. Do not hand-edit the
generated markdown.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not installed; pip install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
HANDLES_DIR = ROOT / "docs" / "categories" / "toothbrushes" / "handles"
HEADS_DIR = ROOT / "docs" / "categories" / "toothbrushes" / "heads"

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


def load_all() -> tuple[dict, dict, dict]:
    mounts = yaml.safe_load((DATA / "mounts.yml").read_text(encoding="utf-8")) or {}
    handles = {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in (DATA / "handles").glob("*.yml")
    }
    heads = {
        p.stem: yaml.safe_load(p.read_text(encoding="utf-8"))
        for p in (DATA / "heads").glob("*.yml")
    }
    return mounts, handles, heads


def head_link(head_id: str, heads: dict) -> str:
    head = heads.get(head_id)
    if not head:
        return f"`{head_id}` (no entry)"
    label = head.get("model") or (head.get("aliases") or [head_id])[0]
    brand = head.get("brand") or "Generic"
    return f"[{brand} {label}](../heads/{head_id}.md)"


def handle_link(handle_id: str, handles: dict) -> str:
    handle = handles.get(handle_id)
    if not handle:
        return f"`{handle_id}` (no entry)"
    brand = handle.get("brand") or ""
    model = handle.get("model") or handle_id
    label = f"{brand} {model}".strip()
    return f"[{label}](../handles/{handle_id}.md)"


def render_handle(handle: dict, mounts: dict, heads: dict) -> str:
    mount = mounts.get(handle.get("mount") or "", {})
    mount_label = mount.get("display_name", handle.get("mount") or "pending measurement")

    out = [GENERATED_BANNER]
    out.append(f"# {handle['brand']} {handle['model']}")
    out.append("")

    facts = []
    if handle.get("aftermarket_anchor"):
        facts.append(f"Aftermarket code: `{handle['aftermarket_anchor']}`")
    facts.append(f"Mode: {handle.get('mode', 'unknown')}")
    facts.append(f"Charging: {handle.get('charging', 'unknown')}")
    mount_prov = lookup_provenance(
        handle.get("mount_provenance"),
        f"handle {handle.get('id', '?')}: mount_provenance",
    )
    facts.append(f"Mount: **{mount_label}** ({mount_prov})")
    if handle.get("released"):
        facts.append(f"Released: {handle['released']}")
    if handle.get("status"):
        facts.append(f"Status: {handle['status']}")
    out.append(" · ".join(facts))
    out.append("")

    if handle.get("aliases"):
        out.append(f"Also sold as: {', '.join(handle['aliases'])}")
        out.append("")

    out.append("## Replacement heads")
    out.append("")
    out.append("| Head | OEM | Bristle | Provenance | Measured? |")
    out.append("|---|---|---|---|---|")
    handle_id = handle.get("id", "?")
    for c in handle.get("compatible_heads", []) or []:
        if "id" not in c:
            ERRORS.append(f"handle {handle_id}: compatible_heads entry missing id: {c}")
            continue
        head = heads.get(c["id"])
        if head is None:
            oem = bristle = measured = "?"
        else:
            measured = "Yes" if head.get("measurements") else "No"
            oem = "OEM" if head.get("oem") else "Generic"
            bristle = head.get("bristle", "?")
        provenance = lookup_provenance(
            c.get("provenance"),
            f"handle {handle_id} -> head {c['id']}",
        )
        out.append(
            f"| {head_link(c['id'], heads)} | {oem} | {bristle} | "
            f"{provenance} | {measured} |"
        )
    out.append("")

    if mount and mount.get("display_name"):
        out.append(f"## Mount: {mount['display_name']}")
        out.append("")
        out.append(f"Status: **{mount.get('status', 'unknown')}**")
        if mount.get("notes"):
            out.append("")
            out.append(mount["notes"].strip())
        out.append("")

    if handle.get("notes"):
        out.append("## Notes")
        out.append("")
        out.append(handle["notes"].strip())
        out.append("")

    if handle.get("sources"):
        out.append("## Sources")
        out.append("")
        for s in handle["sources"]:
            out.append(f"- <{s}>")
        out.append("")

    return "\n".join(out)


def render_head(head: dict, handles: dict) -> str:
    out = [GENERATED_BANNER]
    brand = head.get("brand") or "Generic"
    model = head.get("model") or (head.get("aliases") or ["(unbranded)"])[0]
    out.append(f"# {brand} {model}")
    out.append("")

    facts = []
    facts.append("OEM" if head.get("oem") else "Generic / clone")
    if head.get("clones_of"):
        facts.append(f"Clones: `{head['clones_of']}`")
    facts.append(f"Bristle: {head.get('bristle', 'unknown')}")
    if head.get("variant"):
        facts.append(f"Variant: {head['variant']}")
    out.append(" · ".join(facts))
    out.append("")

    if head.get("aliases"):
        out.append(f"Also sold as: {', '.join(head['aliases'])}")
        out.append("")
    if head.get("sold_as"):
        out.append(f"Brand names seen: {', '.join(head['sold_as'])}")
        out.append("")

    out.append("## Fits handles")
    out.append("")
    out.append("| Handle | Provenance |")
    out.append("|---|---|")
    head_id = head.get("id", "?")
    for f in head.get("fits_handles", []) or []:
        if "id" not in f:
            ERRORS.append(f"head {head_id}: fits_handles entry missing id: {f}")
            continue
        provenance = lookup_provenance(
            f.get("provenance"),
            f"head {head_id} -> handle {f['id']}",
        )
        out.append(f"| {handle_link(f['id'], handles)} | {provenance} |")
    out.append("")

    if head.get("measurements"):
        out.append("## Measurements")
        out.append("")
        for k, v in head["measurements"].items():
            out.append(f"- **{k}**: {v}")
        out.append("")

    if head.get("notes"):
        out.append("## Notes")
        out.append("")
        out.append(head["notes"].strip())
        out.append("")

    if head.get("sources"):
        out.append("## Sources")
        out.append("")
        for s in head["sources"]:
            out.append(f"- <{s}>")
        out.append("")

    return "\n".join(out)


def main() -> None:
    mounts, handles, heads = load_all()
    HANDLES_DIR.mkdir(parents=True, exist_ok=True)
    HEADS_DIR.mkdir(parents=True, exist_ok=True)

    for hid, h in handles.items():
        (HANDLES_DIR / f"{hid}.md").write_text(
            render_handle(h, mounts, heads), encoding="utf-8"
        )
        print(f"wrote handles/{hid}.md")

    for hid, h in heads.items():
        (HEADS_DIR / f"{hid}.md").write_text(
            render_head(h, handles), encoding="utf-8"
        )
        print(f"wrote heads/{hid}.md")

    if ERRORS:
        print(f"\n{len(ERRORS)} data error(s):", file=sys.stderr)
        for e in ERRORS:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
