# Portolan STAC Profile

A [Portolan](https://github.com/portolan-sdi/portolan-spec) catalog is a directory of STAC metadata and cloud-native geospatial data, served from plain object storage and consumable with zero infrastructure.

This block always checks against the **latest** Portolan version, now **v0.3.0**. It adds no rules of its own: its schema points to the block of that version. Reference it to follow new Portolan versions as they are released.

To stay on one version, reference a versioned block instead, as the STAC Building Blocks do:

| Block | Portolan version |
|---|---|
| `portolan.stac.profile-v0-3-0` | v0.3.0, released on 17 November 2026 (current) |
| `portolan.stac.profile-v0-2-0` | v0.2.0, released on 28 August 2026 |

The rules each version enforces, its test files and the differences between versions are documented in the versioned blocks. Like them, this block is checked by the rashid validator plugin, with the rashid release that matches the latest version. The examples here are those of the v0.3.0 block.
