"""Plain-text rendering of a check report."""

from __future__ import annotations

import re
from collections import Counter

from .check import Report

_INDEX = re.compile(r"(?<=/)\d+(?=/|:|$)")


def _pattern(problem) -> str:
    """Group problems that differ only by list index, e.g. links/3 and links/7."""
    return _INDEX.sub("N", str(problem))


def render(report: Report, show_all: bool = False, top: int = 10) -> str:
    s = report.as_dict()["summary"]
    lines = [
        report.target,
        f"  block     {report.block} (Portolan {report.published_version or 'unknown'}) from {report.register}",
        f"  checked   {s['objects']} objects {_counts(s['types'])} in {report.seconds:.1f}s",
    ]
    if report.item_links:
        lines.append(f"            {report.item_links} item links not checked (the block covers catalogs and collections)")
    lines.append(f"  declares  {_counts(s['declared_versions'], bare=True)}")
    if s["fetch_errors"]:
        lines.append(f"  errors    {s['fetch_errors']} objects could not be fetched or checked")
    if "conform_to_declared" in s:
        lines.append(f"  conform to the version they declare:  {s['conform_to_declared']}/{s['objects']}")
    if "pass_published" in s:
        lines.append(f"  pass the block as published ({report.published_version}): {s['pass_published']}/{s['objects']}")

    for key, title in (("declared", "against the declared version"),
                       ("published", f"against the published block ({report.published_version})")):
        counter: Counter[str] = Counter()
        for obj in report.objects:
            for problem in getattr(obj, key) or []:
                counter[_pattern(problem)] += 1
        if counter:
            lines.append("")
            lines.append(f"  Most common problems {title}:")
            for text, n in counter.most_common(None if show_all else top):
                lines.append(f"    {n:5d}  {text}")

    failing = [o for o in report.objects if not o.ok(report.mode)]
    if failing:
        lines.append("")
        lines.append(f"  Failing objects ({len(failing)}):")
        for obj in failing if show_all else failing[:5]:
            lines.append(f"    FAIL {obj.type or '?'} {obj.url}")
            if obj.error:
                lines.append(f"         {obj.error}")
            problems = obj.declared if report.mode != "published" else obj.published
            for problem in (problems or []) if show_all else (problems or [])[:4]:
                lines.append(f"         {problem}")
        if not show_all and len(failing) > 5:
            lines.append(f"    … {len(failing) - 5} more; use --all or --json to see every object")
    lines.append("")
    lines.append("  RESULT " + ("PASS" if report.ok else "FAIL"))
    return "\n".join(lines)


def _counts(counts: dict[str, int], bare: bool = False) -> str:
    text = ", ".join(f"{k} {v}" if bare else f"{v} {k}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
    return text if bare else f"({text})"
