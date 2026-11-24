"""OGC Building Blocks validator plugin that runs rashid on Portolan examples and tests.

rashid (https://github.com/portolan-sdi/rashid) is the Portolan conformance validator. It checks
rules that JSON Schema and SHACL cannot express, such as whether a collection is a mirror and
then carries a ``via`` link. This plugin runs rashid's metadata rules on each example and test
file of a Portolan building block and reports the findings in the block's validation report.

How it works:

- A block opts in with a ``role: validation`` resource in ``bblock.json`` whose ``conformsTo`` is
  ``RASHID`` and whose ``ref`` is the Portolan schema URL of the version to check, for example
  ``https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json``.
- Each rashid release checks one Portolan version, the newest it knows. bblocks-config.yaml
  installs this package once per rashid pin, each in its own virtualenv, and each copy only
  handles the blocks whose Portolan version matches its rashid.
- rashid validates a catalog tree, not a single document. The plugin writes the document into a
  minimal synthetic catalog (a root catalog, AGENTS.md and README.md stubs) and keeps only the
  findings on that document. Checks that need the real tree, such as link resolution, are left
  out. File and live checks are off: the first version checks metadata only.

The plugin follows the contract in
https://ogcincubator.github.io/bblocks-docs/create/validation#validator-plugins.
"""

from __future__ import annotations

import importlib.metadata
import json
import re
import tempfile
from pathlib import Path

# conformsTo value that marks the validation resource this plugin reads.
RASHID = "https://github.com/portolan-sdi/rashid"

# Portolan version checked by rashid releases that predate rashid.api.newest_profile_version.
# portolan-spec pins rashid 0.1.8 at its v0.2.0 tag, and rashid 0.1.8 bundles the v0.2.0 schema.
_LEGACY_TARGETS = {"0.1.8": "v0.2.0"}

# Checks that need the real catalog tree, which the synthetic tree cannot stand in for.
TREE_CHECKS = frozenset({
    "PTL-LNK-006",  # every link resolves to a file in the tree
})

_VERSION_IN_URL = re.compile(r"/portolan/(v\d+\.\d+\.\d+)/schema\.json$")

# Stub Markdown with the sections rashid looks for in a README.md (PORTO-CORE-063).
_STUB_MARKDOWN = "# Stub\n\nStub description.\n\n## License\n\nCC0-1.0\n\n## Provenance\n\nStub.\n"


def rashid_version() -> str:
    return importlib.metadata.version("rashid")


def rashid_target() -> str | None:
    """Portolan version whose rules the installed rashid applies, or None if unknown."""
    try:
        from rashid.api import newest_profile_version
    except ImportError:
        return _LEGACY_TARGETS.get(rashid_version())
    return newest_profile_version()


def requested_version(context) -> str | None:
    """Portolan version the block asks rashid to check, from its validation resources."""
    for resource in getattr(context, "validation_resources", None) or []:
        if resource.get("conformsTo") == RASHID:
            match = _VERSION_IN_URL.search(str(resource.get("ref", "")))
            if match:
                return match.group(1)
    return None


def _portolan_uris(doc: dict) -> list[str]:
    return [e for e in doc.get("stac_extensions") or [] if isinstance(e, str) and "/portolan/" in e]


def _write_tree(root: Path, doc: dict) -> str:
    """Write a synthetic catalog around the document. Returns the document's path in the tree."""
    for directory in (root, root / "collection"):
        directory.mkdir(exist_ok=True)
        (directory / "AGENTS.md").write_text(_STUB_MARKDOWN)
        (directory / "README.md").write_text(_STUB_MARKDOWN)
    if doc.get("type") == "Catalog":
        (root / "catalog.json").write_text(json.dumps(doc))
        return "catalog.json"
    synthetic_root = {
        "type": "Catalog",
        "stac_version": doc.get("stac_version", "1.1.0"),
        "stac_extensions": _portolan_uris(doc),
        "id": "synthetic-root",
        "title": "Synthetic root",
        "description": "Root catalog written by the validator plugin around the document under test.",
        "links": [
            {"rel": "root", "href": "./catalog.json", "type": "application/json"},
            {"rel": "child", "href": "./collection/collection.json", "type": "application/json", "title": "Document"},
            {"rel": "agents", "href": "./AGENTS.md", "type": "text/markdown"},
            {"rel": "describedby", "href": "./README.md", "type": "text/markdown"},
        ],
    }
    (root / "catalog.json").write_text(json.dumps(synthetic_root))
    (root / "collection" / "collection.json").write_text(json.dumps(doc))
    return "collection/collection.json"


def _run_rashid(catalog: Path):
    from rashid import validate

    try:
        from rashid import ValidationOptions
    except ImportError:  # rashid < 0.4 takes the options as keyword arguments
        return validate(catalog, data=False, live=False)
    return validate(catalog, options=ValidationOptions(data=False, live=False))


def _spec_ids(rule_id: str) -> tuple[str, ...]:
    from rashid.registry import CHECKS

    check = CHECKS.get(rule_id)
    return tuple(getattr(check, "spec_ids", ()) or ())


def _severity(finding) -> str:
    value = str(getattr(finding.severity, "value", finding.severity)).lower()
    return value if value in ("error", "warning", "info") else "info"


def check_document(doc: dict) -> list[dict]:
    """Run rashid on one Catalog or Collection and return plugin entries for its findings."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        target = _write_tree(root, doc)
        report = _run_rashid(root / "catalog.json")
    entries = []
    for finding in report.findings:
        if finding.path != target or finding.rule_id in TREE_CHECKS:
            continue
        spec_ids = _spec_ids(finding.rule_id)
        requirement = f" ({', '.join(spec_ids)})" if spec_ids else ""
        payload = {"subsection": f"rashid {rashid_version()}", "rule": finding.rule_id, "requirements": list(spec_ids)}
        if finding.json_pointer:
            payload["jsonPointer"] = finding.json_pointer
        entries.append({
            "message": f"{finding.rule_id}: {finding.message}{requirement}",
            "severity": _severity(finding),
            "payload": payload,
        })
    return entries


class RashidValidator:
    """Runs rashid's metadata rules on the JSON examples and tests of Portolan building blocks."""

    mime_types = ["application/json"]
    file_extensions = [".json"]

    def validate(self, meta):
        context = getattr(meta, "context", None)
        version = requested_version(context)
        if version is None:
            return None  # the block did not opt in
        target = rashid_target()
        if target != version:
            return None  # another copy of this plugin, with the matching rashid pin, handles it

        try:
            doc = json.loads(Path(meta.input_path).read_text())
        except (OSError, ValueError) as exc:
            return [{"message": f"rashid: could not read {meta.display_filename} as JSON: {exc}", "severity": "error"}]
        if not isinstance(doc, dict) or doc.get("type") not in ("Catalog", "Collection"):
            return None  # rashid checks catalogs and collections; items are not covered by these blocks

        entries = check_document(doc)
        errors = sum(1 for e in entries if e["severity"] == "error")
        warnings = sum(1 for e in entries if e["severity"] == "warning")
        summary = {
            "message": f"rashid {rashid_version()} checked {meta.display_filename} against Portolan {version} "
                       f"(metadata rules): {errors} errors, {warnings} warnings",
            "severity": "info",
            "payload": {"subsection": f"rashid {rashid_version()}"},
        }
        return [summary, *entries]
