import json
import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
BLOCK_DIR = REPO / "_sources" / "stac" / "profile-v0-3-0"
EXAMPLES = sorted((BLOCK_DIR / "examples").glob("*.json"))
TEST_FILES = sorted((BLOCK_DIR / "tests").glob("*.json"))

V020_ID = "portolan.stac.profile-v0-2-0"
V020_DIR = REPO / "_sources" / "stac" / "profile-v0-2-0"
V020_EXAMPLES = sorted((V020_DIR / "examples").glob("*.json"))
V020_TEST_FILES = sorted((V020_DIR / "tests").glob("*.json"))

# PORTOLAN_BBLOCKS_LOCAL=1 runs the network tests against build-local/ (after ./build.sh)
# instead of the published register, to test blocks before they are merged.
LOCAL = os.environ.get("PORTOLAN_BBLOCKS_LOCAL") == "1"


def load(path: Path):
    return json.loads(path.read_text())


def _register_and_fetcher():
    from portolan_bblocks import DEFAULT_REGISTER
    from portolan_bblocks.cli import LOCAL_BASE
    from portolan_bblocks.fetch import Fetcher

    if LOCAL:
        return (REPO / "build-local" / "register.json").as_uri(), Fetcher([(LOCAL_BASE, REPO.as_uri() + "/")])
    return DEFAULT_REGISTER, Fetcher()


def _block_validator(block_id: str):
    from portolan_bblocks.validator import BlockNotFound, BlockValidator, load_block

    register, fetch = _register_and_fetcher()
    try:
        return fetch, BlockValidator(load_block(register, block_id, fetch), fetch)
    except BlockNotFound:
        pytest.skip(f"{block_id} is not published yet (set PORTOLAN_BBLOCKS_LOCAL=1 to test the local build)")


@pytest.fixture(scope="session")
def published():
    """Fetcher and validator for the portolan.stac.profile block (network)."""
    from portolan_bblocks import DEFAULT_BLOCK

    return _block_validator(DEFAULT_BLOCK)


@pytest.fixture(scope="session")
def published_v020():
    """Fetcher and validator for the portolan.stac.profile-v0-2-0 block (network)."""
    return _block_validator(V020_ID)
