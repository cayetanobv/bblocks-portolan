# Portolan building blocks

> **Work in progress.** This register started on 8 September 2026 and is under active development. Block identifiers, schemas, and the register URL can change before the first stable release. The Portolan specification itself is pre-1.0. Do not depend on `bblocks://portolan.*` identifiers in production yet. The schema of record, `https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json`, is stable at its versioned URL.

[OGC Building Blocks](https://ogcincubator.github.io/bblocks-docs/) for the [Portolan specification](https://github.com/portolan-sdi/portolan-spec).

Portolan is an open-source specification for publishing geospatial data at any scale. A catalog is a static STAC catalog on plain object storage, with cloud-native assets and documentation for people and agents. This register wraps the published Portolan artifacts as building blocks so that they can be validated, documented, and composed with other blocks in the OGC ecosystem. It does not redefine them. The schema of record stays at `https://schemas.portolan-sdi.org/portolan/<version>/schema.json`, the profile text stays in [`stac/README.md`](https://github.com/portolan-sdi/portolan-spec/blob/main/stac/README.md), and [rashid](https://github.com/portolan-sdi/rashid) checks the rules a schema cannot express.

Register: https://cayetanobv.github.io/bblocks-portolan/

## Blocks

| Identifier | Wraps | Status |
|---|---|---|
| `portolan.stac.profile` | Portolan STAC profile v0.3.0. A STAC Catalog or Collection that conforms to the Portolan specification. Profile of `ogc.contrib.stac.collection`. | under-development |

The profile block depends on `ogc.contrib.stac.collection` and on the extension blocks in [bblocks-stac](https://ogcincubator.github.io/bblocks-stac/) (imported as `@ogc/stac`) that match a version Portolan pins: classification, datacube, file, raster, scientific, themes, and version. The other STAC extensions Portolan composes are referenced by schema URL until a block exists for each.

## Use the blocks

Validate a document against the profile with the annotated schema:

```
https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/schema.json
```

Reference the block from another register by adding this register to `imports` in `bblocks-config.yaml`:

```yaml
imports:
  - default
  - https://cayetanobv.github.io/bblocks-portolan/build/register.json
```

Then use `$ref: bblocks://portolan.stac.profile` in a schema.

## Build locally

Docker is required.

```bash
./build.sh   # runs ghcr.io/opengeospatial/bblocks-postprocess (pinned, override with BBP_IMAGE_TAG), writes build-local/
./view.sh    # serves the register viewer at http://localhost:9090/register/
```

The validation report is written to `build-local/tests/report.html`. Examples must pass. Files in `tests/` whose name ends in `-fail` must fail.

## Layout

```
bblocks-config.yaml        register name, identifier prefix, imports, license
_sources/<path>/           one directory per block; the path becomes the identifier
  bblock.json              metadata and dependencies
  schema.yaml              JSON Schema, may $ref other blocks with bblocks://
  examples.yaml            examples, validated on every build
  description.md           documentation
  tests/*-fail.json        negative fixtures
build/                     generated on push by GitHub Actions; do not edit
```

Template and tooling: [opengeospatial/bblock-template](https://github.com/opengeospatial/bblock-template) and its [USAGE.md](https://github.com/opengeospatial/bblock-template/blob/master/USAGE.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
