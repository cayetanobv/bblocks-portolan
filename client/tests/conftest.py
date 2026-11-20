import json
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
BLOCK_DIR = REPO / "_sources" / "stac" / "profile"
EXAMPLES = sorted((BLOCK_DIR / "examples").glob("*.json"))
TEST_FILES = sorted((BLOCK_DIR / "tests").glob("*.json"))


def load(path: Path):
    return json.loads(path.read_text())


@pytest.fixture(scope="session")
def published():
    """Fetcher and validator for the published portolan.stac.profile block (network)."""
    from portolan_bblocks import DEFAULT_BLOCK, DEFAULT_REGISTER
    from portolan_bblocks.fetch import Fetcher
    from portolan_bblocks.validator import BlockValidator, load_block

    fetch = Fetcher()
    return fetch, BlockValidator(load_block(DEFAULT_REGISTER, DEFAULT_BLOCK, fetch), fetch)
