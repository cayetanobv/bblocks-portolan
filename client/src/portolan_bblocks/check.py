"""Check catalogs and single documents against a building block."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Literal

from .crawl import crawl
from .fetch import Fetcher, to_url
from .validator import BlockValidator, Problem, declared_portolan_version

Mode = Literal["both", "declared", "published"]
NOT_DECLARED = Problem(
    path="stac_extensions",
    message="does not declare a Portolan schema (https://schemas.portolan-sdi.org/portolan/<version>/schema.json)",
    schema_path="",
)


@dataclass
class ObjectResult:
    url: str
    type: str | None = None
    id: str | None = None
    declared_version: str | None = None
    declared: list[Problem] | None = None   # against the version the object declares
    published: list[Problem] | None = None  # against the block as published
    error: str | None = None                # could not fetch or parse

    def ok(self, mode: Mode) -> bool:
        if self.error:
            return False
        if mode in ("both", "declared") and self.declared:
            return False
        if mode == "published" and self.published:
            return False
        return True

    def as_dict(self) -> dict[str, Any]:
        def plist(problems):
            if problems is None:
                return None
            return [{"path": p.path, "message": p.message, "schema_path": p.schema_path} for p in problems]

        return {
            "url": self.url, "type": self.type, "id": self.id,
            "declared_version": self.declared_version, "error": self.error,
            "declared": plist(self.declared), "published": plist(self.published),
        }


@dataclass
class Report:
    target: str
    block: str
    register: str
    mode: Mode
    published_version: str | None
    objects: list[ObjectResult] = field(default_factory=list)
    item_links: int = 0
    seconds: float = 0.0

    @property
    def ok(self) -> bool:
        return all(o.ok(self.mode) for o in self.objects) and bool(self.objects)

    def as_dict(self) -> dict[str, Any]:
        return {
            "target": self.target, "block": self.block, "register": self.register, "mode": self.mode,
            "published_portolan_version": self.published_version, "seconds": round(self.seconds, 2),
            "item_links_not_checked": self.item_links, "ok": self.ok,
            "summary": summarize(self),
            "objects": [o.as_dict() for o in self.objects],
        }


def check_document(doc: Any, url: str, validator: BlockValidator, mode: Mode) -> ObjectResult:
    result = ObjectResult(url=url)
    if not isinstance(doc, dict):
        result.error = "not a JSON object"
        return result
    result.type = doc.get("type")
    result.id = doc.get("id")
    result.declared_version = declared_portolan_version(doc)
    if mode in ("both", "published"):
        result.published = validator.validate(doc)
    if mode in ("both", "declared"):
        if result.declared_version is None:
            result.declared = [NOT_DECLARED]
        elif result.declared_version == validator.portolan_version and result.published is not None:
            result.declared = result.published
        else:
            try:
                result.declared = validator.validate(doc, portolan_version=result.declared_version)
            except Exception as exc:  # e.g. a version whose schema is not published
                result.error = f"cannot check {result.declared_version}: {exc}"
    return result


def check_catalog(target: str, validator: BlockValidator, fetch: Fetcher, register: str,
                  mode: Mode = "both", max_objects: int = 1000) -> Report:
    start = time.monotonic()
    report = Report(target=target, block=validator.identifier, register=register, mode=mode,
                    published_version=validator.portolan_version)
    for node in crawl(to_url(target), fetch, max_objects=max_objects):
        report.item_links += node.item_links
        if node.error:
            report.objects.append(ObjectResult(url=node.url, error=node.error))
        else:
            report.objects.append(check_document(node.doc, node.url, validator, mode))
    report.seconds = time.monotonic() - start
    return report


def check_files(targets: list[str], validator: BlockValidator, fetch: Fetcher, register: str,
                mode: Mode = "both") -> Report:
    start = time.monotonic()
    report = Report(target=", ".join(targets), block=validator.identifier, register=register,
                    mode=mode, published_version=validator.portolan_version)
    for target in targets:
        url = to_url(target)
        try:
            doc = fetch(url)
        except Exception as exc:
            report.objects.append(ObjectResult(url=url, error=f"could not fetch: {exc}"))
            continue
        report.objects.append(check_document(doc, url, validator, mode))
    report.seconds = time.monotonic() - start
    return report


def summarize(report: Report) -> dict[str, Any]:
    objs = report.objects
    versions: dict[str, int] = {}
    types: dict[str, int] = {}
    for o in objs:
        versions[o.declared_version or "none"] = versions.get(o.declared_version or "none", 0) + 1
        types[o.type or "unknown"] = types.get(o.type or "unknown", 0) + 1
    out: dict[str, Any] = {"objects": len(objs), "types": types, "declared_versions": versions,
                           "fetch_errors": sum(1 for o in objs if o.error)}
    if report.mode in ("both", "declared"):
        out["conform_to_declared"] = sum(1 for o in objs if not o.error and not o.declared)
    if report.mode in ("both", "published"):
        out["pass_published"] = sum(1 for o in objs if not o.error and not o.published)
    return out
