# Portolan Building Blocks

OGC Building Blocks for the [Portolan specification](https://github.com/portolan-sdi/portolan-spec):
the Portolan STAC profile and the STAC extensions Portolan defines.


Portolan is an open specification for cloud-native geospatial data catalogs. Every Portolan
catalog is a static STAC catalog on plain HTTPS object storage, with cloud-native assets and
guidance files that both people and AI agents read.

This register wraps the published Portolan artifacts as Building Blocks. It does not redefine
them. The schema of record is `https://schemas.portolan-sdi.org/portolan/<version>/schema.json`,
the profile text lives in `portolan-spec/stac/README.md`, and rules the schema cannot express are
checked by the [rashid](https://github.com/portolan-sdi/rashid) validator.


## Building Blocks

### `portolan.stac.profile` — Portolan STAC Profile

**Type:** schema

A STAC Catalog or Collection that conforms to the Portolan specification v0.2.0: cloud-native assets on plain HTTPS object storage, a pinned set of STAC extensions, and AGENTS.md and README.md links on every catalog and collection.

