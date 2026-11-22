"""Tests for the portolan.stac.profile-v0-2-0 block: its examples, its test files, and the rules
that changed between Portolan v0.2.0 and v0.3.0."""

import pytest

from conftest import V020_EXAMPLES, V020_TEST_FILES, load

pytestmark = pytest.mark.network

# Field each *-fail.json test file breaks. Every problem reported must be on that field.
EXPECTED_FIELD = {
    "missing-agents-link-fail": "links",
    "proprietary-license-fail": "license",
    "s3-asset-href-fail": "assets/data",
    "s3-asset-href-with-https-alternate-fail": "assets/data",
}

# Valid test files that the v0.3.0 block rejects, and the field it rejects them on.
FAIL_IN_V030 = {
    "data-asset-href-glob": "assets/data/href",
    "pmtiles-asset-without-visual-role": "assets/visual/roles",
}


def by_name(name):
    return load(next(p for p in V020_TEST_FILES if p.stem == name))


def test_block_wraps_portolan_v020(published_v020):
    _, validator = published_v020
    assert validator.portolan_version == "v0.2.0"


@pytest.mark.parametrize("path", V020_EXAMPLES, ids=lambda p: p.stem)
def test_examples_pass(published_v020, path):
    _, validator = published_v020
    assert validator.validate(load(path)) == []


@pytest.mark.parametrize("path", [p for p in V020_TEST_FILES if not p.stem.endswith("-fail")], ids=lambda p: p.stem)
def test_valid_test_files_pass(published_v020, path):
    _, validator = published_v020
    assert validator.validate(load(path)) == []


def test_every_test_file_is_listed():
    stems = {p.stem for p in V020_TEST_FILES}
    assert {s for s in stems if s.endswith("-fail")} == set(EXPECTED_FIELD)
    assert {s for s in stems if not s.endswith("-fail")} == set(FAIL_IN_V030)


@pytest.mark.parametrize("name", sorted(EXPECTED_FIELD))
def test_fail_files_fail_on_their_field(published_v020, name):
    _, validator = published_v020
    problems = validator.validate(by_name(name))
    assert problems, f"{name} should fail"
    assert all(p.path.startswith(EXPECTED_FIELD[name]) for p in problems), [str(p) for p in problems]


@pytest.mark.parametrize("name", sorted(FAIL_IN_V030))
def test_rules_added_in_v030(published, name):
    """Valid in v0.2.0, invalid under the v0.3.0 rules on the field v0.3.0 added a rule for."""
    _, validator = published
    problems = validator.validate(by_name(name), portolan_version="v0.3.0")
    # The file declares v0.2.0, so v0.3.0 also asks for its own schema URL. That is not the rule under test.
    problems = [p for p in problems if p.path != "stac_extensions"]
    assert problems and all(p.path.startswith(FAIL_IN_V030[name]) for p in problems), [str(p) for p in problems]
