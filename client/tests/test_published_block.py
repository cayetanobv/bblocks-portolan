"""Tests against the published register: the block's own examples and test files."""

import json
import shutil

import pytest

from conftest import EXAMPLES, TEST_FILES, load
from portolan_bblocks import DEFAULT_REGISTER
from portolan_bblocks.check import check_catalog
from portolan_bblocks.cli import main

pytestmark = pytest.mark.network

# Field each *-fail.json test file breaks. Every problem reported must be on that field.
EXPECTED_FIELD = {
    "missing-agents-link-fail": "links",
    "proprietary-license-fail": "license",
    "s3-asset-href-fail": "assets/data",
    "data-asset-href-glob-fail": "assets/data/href",
    "pmtiles-asset-without-visual-role-fail": "assets/visual/roles",
    "partition-glob-https-fail": "partition:glob",
    "classes-in-raster-bands-fail": "assets/data/raster:bands",
    "class-without-title-fail": "assets/data/classification:classes/1",
    "classes-on-asset-of-multiband-raster-fail": "assets/data",
}


def test_block_wraps_portolan_v030(published):
    _, validator = published
    assert validator.identifier == "portolan.stac.profile"
    assert validator.portolan_version == "v0.3.0"


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda p: p.stem)
def test_examples_pass(published, path):
    _, validator = published
    assert validator.validate(load(path)) == []


@pytest.mark.parametrize("path", [p for p in TEST_FILES if not p.stem.endswith("-fail")], ids=lambda p: p.stem)
def test_valid_test_files_pass(published, path):
    _, validator = published
    assert validator.validate(load(path)) == []


# Fail files that break a rule only the block's SHACL shapes check, with the requirement each
# breaks. They pass the JSON Schema, which is all this client checks.
SHACL_ONLY = {
    "license-not-spdx-fail": "PORTO-CORE-059",
    "license-other-without-link-fail": "PORTO-CORE-059",
}


def test_every_fail_file_has_an_expected_field():
    assert {p.stem for p in TEST_FILES if p.stem.endswith("-fail")} == set(EXPECTED_FIELD) | set(SHACL_ONLY)


@pytest.mark.parametrize("name", sorted(SHACL_ONLY))
def test_shacl_only_fail_files_pass_the_json_schema(published, name):
    _, validator = published
    assert validator.validate(load(next(p for p in TEST_FILES if p.stem == name))) == []


@pytest.mark.parametrize("name", sorted(EXPECTED_FIELD))
def test_fail_files_fail_on_their_field(published, name):
    _, validator = published
    problems = validator.validate(load(next(p for p in TEST_FILES if p.stem == name)))
    assert problems, f"{name} should fail"
    assert all(p.path.startswith(EXPECTED_FIELD[name]) for p in problems), [str(p) for p in problems]


def test_declared_version_uses_that_versions_rules(published):
    """An s3:// href with an https alternate is valid in v0.3.0 but not in v0.2.0."""
    _, validator = published
    path = next(p for p in TEST_FILES if p.stem == "s3-asset-href-with-https-alternate")
    doc = json.loads(path.read_text().replace("portolan/v0.3.0/schema.json", "portolan/v0.2.0/schema.json"))
    declared = validator.validate(doc, portolan_version="v0.2.0")
    assert declared and all(p.path.startswith("assets/data") for p in declared)
    published_problems = validator.validate(doc)
    assert [p.path for p in published_problems] == ["stac_extensions"]


def make_catalog(tmp_path):
    """A local catalog whose children are the block's collection examples."""
    root = load(next(p for p in EXAMPLES if p.stem == "catalog"))
    collections = [p for p in EXAMPLES if p.stem != "catalog"]
    root["links"] = [l for l in root["links"] if l["rel"] != "child"] + [
        {"rel": "child", "href": f"./{p.stem}/collection.json", "type": "application/json", "title": p.stem}
        for p in collections
    ]
    (tmp_path / "catalog.json").write_text(json.dumps(root))
    for p in collections:
        (tmp_path / p.stem).mkdir()
        shutil.copy(p, tmp_path / p.stem / "collection.json")
    return tmp_path / "catalog.json"


def test_check_catalog_end_to_end(published, tmp_path):
    fetch, validator = published
    report = check_catalog(str(make_catalog(tmp_path)), validator, fetch, DEFAULT_REGISTER)
    assert report.ok
    assert len(report.objects) == len(EXAMPLES)
    assert report.as_dict()["summary"]["conform_to_declared"] == len(EXAMPLES)


def test_cli_exit_codes(tmp_path, capsys):
    good = make_catalog(tmp_path)
    assert main(["check", str(good)]) == 0
    bad = next(p for p in TEST_FILES if p.stem == "proprietary-license-fail")
    assert main(["validate", str(bad), "--json", str(tmp_path / "r.json")]) == 1
    report = json.loads((tmp_path / "r.json").read_text())
    assert report["objects"][0]["declared"][0]["path"] == "license"
    assert "RESULT FAIL" in capsys.readouterr().out


def test_latest_and_v030_blocks_agree():
    """portolan.stac.profile points to portolan.stac.profile-v0-3-0 while v0.3.0 is the latest version."""
    from conftest import _block_validator

    _, v030 = _block_validator("portolan.stac.profile-v0-3-0")
    assert v030.portolan_version == "v0.3.0"
    for path in EXAMPLES + TEST_FILES:
        assert [str(p) for p in v030.validate(load(path))] == [str(p) for p in published_validator().validate(load(path))]


_latest = []


def published_validator():
    from conftest import _block_validator

    if not _latest:
        _latest.append(_block_validator("portolan.stac.profile")[1])
    return _latest[0]
