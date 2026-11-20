"""Unit tests that need no network."""

import json

from jsonschema import Draft202012Validator

from portolan_bblocks.crawl import crawl
from portolan_bblocks.fetch import Fetcher, to_url
from portolan_bblocks.validator import declared_portolan_version, relevant_leaves, to_problem

# A small schema with the same shape as the block: an anyOf of STAC base schemas and a
# oneOf of Portolan branches per object type.
SCHEMA = {
    "allOf": [
        {"anyOf": [
            {"properties": {"type": {"const": "Collection"}}, "required": ["extent"]},
            {"properties": {"type": {"const": "Catalog"}}},
        ]},
        {"oneOf": [
            {"properties": {"type": {"const": "Catalog"}}, "required": ["title"]},
            {"properties": {"type": {"const": "Collection"}, "license": {"not": {"const": "proprietary"}},
                            "links": {"contains": {"properties": {"rel": {"const": "agents"}}}}},
             "required": ["title", "license"]},
            {"properties": {"type": {"const": "Feature"}}, "required": ["assets"]},
        ]},
    ]
}
VALIDATOR = Draft202012Validator(SCHEMA)


def problems(doc):
    return sorted({str(to_problem(leaf)) for e in VALIDATOR.iter_errors(doc) for leaf in relevant_leaves(e, doc)})


def test_valid_collection_has_no_problems():
    doc = {"type": "Collection", "extent": {}, "title": "t", "license": "CC-BY-4.0", "links": [{"rel": "agents"}]}
    assert problems(doc) == []


def test_only_the_branch_for_the_object_type_is_reported():
    doc = {"type": "Collection", "extent": {}, "title": "t", "license": "proprietary", "links": [{"rel": "agents"}]}
    found = problems(doc)
    assert len(found) == 1 and found[0].startswith("license:")
    assert not any("Catalog" in p or "Feature" in p or "assets" in p for p in found)


def test_contains_failure_names_the_missing_entry():
    doc = {"type": "Collection", "extent": {}, "title": "t", "license": "MIT", "links": [{"rel": "root"}]}
    assert problems(doc) == ['links: no entry matches {"properties":{"rel":{"const":"agents"}}}']


def test_catalog_errors_come_from_the_catalog_branches():
    assert problems({"type": "Catalog"}) == ["(root): 'title' is a required property"]


def test_unknown_type_keeps_every_branch():
    assert len(problems({"type": "Something"})) > 1


def test_declared_portolan_version():
    doc = {"stac_extensions": ["https://stac-extensions.github.io/file/v2.1.0/schema.json",
                               "https://schemas.portolan-sdi.org/portolan/v0.2.0/schema.json"]}
    assert declared_portolan_version(doc) == "v0.2.0"
    assert declared_portolan_version({"stac_extensions": []}) is None
    assert declared_portolan_version([]) is None


def test_fetcher_maps_prefixes_and_reads_yaml(tmp_path):
    (tmp_path / "a.yaml").write_text("name: block\nversion: 1\n")
    fetch = Fetcher([("http://localhost:9090/register/", tmp_path.as_uri() + "/")])
    assert fetch("http://localhost:9090/register/a.yaml") == {"name": "block", "version": 1}


def write(path, doc):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc))


def test_crawl_follows_children_counts_items_and_reports_broken_links(tmp_path):
    write(tmp_path / "catalog.json", {"type": "Catalog", "links": [
        {"rel": "child", "href": "./a/collection.json"},
        {"rel": "child", "href": "./sub/catalog.json"},
        {"rel": "child", "href": "./missing/collection.json"},
    ]})
    write(tmp_path / "a" / "collection.json", {"type": "Collection", "links": [
        {"rel": "item", "href": "./i1.json"}, {"rel": "item", "href": "./i2.json"},
        {"rel": "parent", "href": "../catalog.json"},
    ]})
    write(tmp_path / "sub" / "catalog.json", {"type": "Catalog", "links": [
        {"rel": "child", "href": "../a/collection.json"},  # already seen: not fetched twice
    ]})
    nodes = list(crawl(to_url(str(tmp_path / "catalog.json")), Fetcher()))
    by_name = {n.url.split(str(tmp_path))[-1]: n for n in nodes}
    assert set(by_name) == {"/catalog.json", "/a/collection.json", "/sub/catalog.json", "/missing/collection.json"}
    assert by_name["/a/collection.json"].item_links == 2
    assert by_name["/missing/collection.json"].error.startswith("could not fetch")


def test_remote_catalog_cannot_lead_to_local_files():
    from portolan_bblocks.crawl import _links

    doc = {"links": [{"rel": "child", "href": "file:///etc/passwd"},
                     {"rel": "child", "href": "./a/collection.json"},
                     {"rel": "child", "href": "ftp://example.org/x.json"}]}
    remote = _links(doc, "child", "https://example.org/catalog.json", root_scheme="https")
    assert remote == ["https://example.org/a/collection.json"]
    local = _links(doc, "child", "file:///data/catalog.json", root_scheme="file")
    assert local == ["file:///etc/passwd", "file:///data/a/collection.json"]


def test_fetcher_rejects_other_schemes():
    import pytest

    with pytest.raises(ValueError):
        Fetcher()("ftp://example.org/catalog.json")


def test_crawl_stops_at_max_objects(tmp_path):
    write(tmp_path / "catalog.json", {"type": "Catalog", "links": [
        {"rel": "child", "href": f"./c{i}.json"} for i in range(10)]})
    for i in range(10):
        write(tmp_path / f"c{i}.json", {"type": "Collection", "links": []})
    assert len(list(crawl(to_url(str(tmp_path / "catalog.json")), Fetcher(), max_objects=4))) == 4
