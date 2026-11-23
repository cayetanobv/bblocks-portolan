"""Print the SPDX identifiers rashid accepts, as a SHACL sh:in list body.

The licence shape in _sources/stac/profile-v0-3-0/shapes.shacl checks against the same list
as rashid's PTL-LIC-001, so the two cannot disagree. Regenerate when rashid updates its list:

    pip install "rashid @ git+https://github.com/portolan-sdi/rashid@v0.4.0"
    python scripts/spdx_shacl_list.py
"""

from rashid.api import SPDX_LICENSE_IDS

for spdx_id in sorted(SPDX_LICENSE_IDS):
    print(f'        "{spdx_id}"')
