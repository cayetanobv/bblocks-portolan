"""Validate STAC documents against a building block loaded with the OGC bblocks client."""

from __future__ import annotations

import json
import re
import threading
from dataclasses import dataclass
from typing import Any, Iterable, Iterator

from jsonschema import ValidationError
from jsonschema.validators import validator_for
from ogc.bblocks.register import BuildingBlockSummary, load_register
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

from .fetch import Fetcher

PORTOLAN_SCHEMA = re.compile(r"^https://schemas\.portolan-sdi\.org/portolan/(v\d+\.\d+\.\d+)/schema\.json$")
PORTOLAN_SCHEMA_URL = "https://schemas.portolan-sdi.org/portolan/{version}/schema.json"
DOC_TYPES = ("Catalog", "Collection", "Feature")


class BlockNotFound(LookupError):
    pass


@dataclass(frozen=True)
class Problem:
    """One broken rule: where in the document, what is wrong, and which schema rule says so."""

    path: str
    message: str
    schema_path: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def declared_portolan_version(doc: Any) -> str | None:
    """The Portolan version an object declares in stac_extensions, such as 'v0.3.0'."""
    if not isinstance(doc, dict):
        return None
    for ext in doc.get("stac_extensions") or []:
        if isinstance(ext, str) and (m := PORTOLAN_SCHEMA.match(ext)):
            return m.group(1)
    return None


def load_block(register_url: str, block_id: str, fetch: Fetcher) -> BuildingBlockSummary:
    """Find a block by identifier, loading imported registers only when needed."""
    register = load_register(register_url, load_dependencies=False, yaml_loader=fetch)
    block = register.get_item_summary(block_id)
    if block is None:
        register = load_register(register_url, load_dependencies=True, yaml_loader=fetch)
        block = register.get_item_summary(block_id)
    if block is None:
        raise BlockNotFound(f"{block_id} is not in {register_url} or the registers it imports")
    return block


class BlockValidator:
    """Validate documents against one building block.

    `validate(doc)` uses the block as published. `validate(doc, portolan_version="v0.2.0")`
    uses the same block with the Portolan schema of record swapped for that version, which
    checks an object against the Portolan version it declares.
    """

    def __init__(self, block: BuildingBlockSummary, fetch: Fetcher):
        self.block = block
        self.fetch = fetch
        self.schema = block.resolved_schema
        if not self.schema:
            raise ValueError(f"{block.item_identifier} has no JSON schema")
        self._validators: dict[str | None, Any] = {}
        self._lock = threading.Lock()
        self._published_portolan: set[str] = set()
        self.validate({})  # resolve remote references once and learn the Portolan version

    @property
    def identifier(self) -> str:
        return self.block.item_identifier

    @property
    def portolan_version(self) -> str | None:
        """The Portolan version the published block validates against."""
        versions = sorted(self._published_portolan)
        return versions[-1] if versions else None

    def _validator(self, portolan_version: str | None):
        with self._lock:
            if portolan_version in self._validators:
                return self._validators[portolan_version]

        def retrieve(uri: str) -> Resource:
            match = PORTOLAN_SCHEMA.match(uri)
            if match and portolan_version is None:
                self._published_portolan.add(match.group(1))
            if match and portolan_version and match.group(1) != portolan_version:
                uri = PORTOLAN_SCHEMA_URL.format(version=portolan_version)
            return Resource.from_contents(self.fetch(uri), default_specification=DRAFT202012)

        cls = validator_for(self.schema)
        validator = cls(self.schema, registry=Registry(retrieve=retrieve))
        with self._lock:
            self._validators[portolan_version] = validator
        return validator

    def validate(self, doc: Any, portolan_version: str | None = None) -> list[Problem]:
        errors = self._validator(portolan_version).iter_errors(doc)
        seen: dict[tuple[str, str], Problem] = {}
        for error in errors:
            for leaf in relevant_leaves(error, doc):
                problem = to_problem(leaf)
                seen.setdefault((problem.path, problem.message), problem)
        return sorted(seen.values(), key=lambda p: (p.path, p.message))


# --- error handling -------------------------------------------------------------------


def _descendants(error: ValidationError) -> Iterator[ValidationError]:
    if not error.context:
        yield error
        return
    for sub in error.context:
        yield from _descendants(sub)


def _is_type_mismatch(error: ValidationError) -> bool:
    """A leaf that only says the document is another STAC type (Catalog vs Collection)."""
    return (
        list(error.absolute_path) == ["type"]
        and error.validator in ("const", "enum")
        and error.instance in DOC_TYPES
    )


def relevant_leaves(error: ValidationError, doc: Any) -> Iterator[ValidationError]:
    """Most specific errors, skipping anyOf/oneOf branches meant for another object type.

    The Portolan schema is a oneOf of Catalog, Collection and Item; the block adds an anyOf
    of the STAC Collection and Catalog schemas. Branches that fail because `type` is wrong
    say nothing useful about the document, so they are dropped when another branch fits.
    """
    if not error.context:
        yield error
        return
    branches: dict[Any, list[ValidationError]] = {}
    for sub in error.context:
        key = sub.relative_schema_path[0] if sub.relative_schema_path else None
        branches.setdefault(key, []).append(sub)
    fitting = {
        key: subs
        for key, subs in branches.items()
        if not any(_is_type_mismatch(leaf) for sub in subs for leaf in _descendants(sub))
    }
    for subs in (fitting or branches).values():
        for sub in subs:
            yield from relevant_leaves(sub, doc)


def _compact(value: Any, limit: int = 120) -> str:
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def to_problem(error: ValidationError) -> Problem:
    path = "/".join(str(p) for p in error.absolute_path) or "(root)"
    schema_path = "/".join(str(p) for p in error.absolute_schema_path)
    if error.validator == "contains":
        message = f"no entry matches {_compact(error.validator_value)}"
    elif error.validator == "not":
        message = f"{_compact(error.instance, 80)} must not match {_compact(error.validator_value)}"
    else:
        message = error.message
    message = " ".join(message.split())
    if len(message) > 220:
        message = message[:219] + "…"
    return Problem(path=path, message=message, schema_path=schema_path)


def problems_text(problems: Iterable[Problem]) -> list[str]:
    return [str(p) for p in problems]
