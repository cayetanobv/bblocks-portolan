# Portolan building blocks

> **Work in progress.** This register started on 8 September 2026 and is under active development. Block identifiers, schemas, and the register URL can change before the first stable release. The Portolan specification itself is pre-1.0. Do not depend on `bblocks://portolan.*` identifiers in production yet. The schema of record, `https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json`, is stable at its versioned URL.

[OGC Building Blocks](https://ogcincubator.github.io/bblocks-docs/) for the [Portolan specification](https://github.com/portolan-sdi/portolan-spec).

Portolan is an open-source specification for publishing geospatial data at any scale. A catalog is a static STAC catalog on plain object storage, with cloud-native assets and documentation for people and agents. This register wraps the published Portolan artifacts as building blocks so that they can be validated, documented, and composed with other blocks in the OGC ecosystem. It does not redefine them. The schema of record stays at `https://schemas.portolan-sdi.org/portolan/<version>/schema.json`, the profile text stays in [`stac/README.md`](https://github.com/portolan-sdi/portolan-spec/blob/main/stac/README.md), and [rashid](https://github.com/portolan-sdi/rashid) checks the rules a schema cannot express.

Register: https://cayetanobv.github.io/bblocks-portolan/

## Blocks

| Identifier | Wraps | Status |
|---|---|---|
| `portolan.stac.profile` | The latest Portolan STAC profile, now v0.3.0. It points to the block of that version; reference it to follow new versions. | under-development |
| `portolan.stac.profile-v0-3-0` | Portolan STAC profile v0.3.0. A STAC Catalog or Collection that conforms to the Portolan specification. Profile of `ogc.contrib.stac.collection`. | under-development |
| `portolan.stac.profile-v0-2-0` | Portolan STAC profile v0.2.0, the version most published catalogs declare. Its test files show the rules that changed in v0.3.0. | under-development |

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

## Check catalogs

The [`client/`](client/) folder holds `portolan-bblocks`, a command-line client that loads a block from this register with OGC's `bblocks_client` library, walks a Portolan catalog and checks every catalog and collection against it:

```bash
cd client && python3 -m venv .venv && .venv/bin/pip install -e .
.venv/bin/portolan-bblocks check https://data.source.coop/nlebovits/pergamino-ide/catalog.json
```

It checks JSON conformance only. [rashid](https://github.com/portolan-sdi/rashid) remains the authority on full Portolan conformance. See [`client/README.md`](client/README.md).

## Build locally

Docker is required.

```bash
./build.sh   # runs ghcr.io/opengeospatial/bblocks-postprocess (pinned, override with BBP_IMAGE_TAG), writes build-local/
./view.sh    # serves the register viewer at http://localhost:9090/register/
```

The validation report is written to `build-local/tests/report.html`. Examples must pass. Files in `tests/` whose name ends in `-fail` must fail.

The first local build asks before it installs the rashid validator plugin. Answer `y`, or pass `--skip-permissions true` to the postprocess image. CI skips the prompt.

## How the blocks validate

Each example and test file goes through three layers:

1. **JSON Schema.** STAC, plus the Portolan schema of the block's version. It checks structure, such as an asset without a media type.
2. **JSON-LD and SHACL.** The JSON-LD context turns the document into RDF, and `shapes.shacl` checks rules the schema leaves to tooling, such as an SPDX licence identifier. Any SHACL tool can apply these shapes.
3. **The rashid validator plugin.** [`plugins/portolan-rashid`](plugins/portolan-rashid) runs [rashid](https://github.com/portolan-sdi/rashid)'s metadata rules on the document, through OGC's [validator plugin](https://ogcincubator.github.io/bblocks-docs/create/validation#validator-plugins) mechanism. It catches rules that compare parts of a document, such as a mirror without a `via` link. Each block names its Portolan version in a `role: validation` resource, and the plugin runs the rashid release portolan-spec pins for that version: 0.1.8 for v0.2.0, 0.4.0 for v0.3.0.

rashid's file and live checks, which need the published catalog, are not part of the build. [`SECURITY.md`](SECURITY.md) lists the code a build runs.

## Layout

```
bblocks-config.yaml        register name, identifier prefix, imports, license
_sources/<path>/           one directory per block; the path becomes the identifier
  bblock.json              metadata and dependencies
  schema.yaml              JSON Schema, may $ref other blocks with bblocks://
  examples.yaml            examples, validated on every build
  description.md           documentation
  tests/*-fail.json        negative fixtures
  context.jsonld           JSON-LD context for the semantic uplift
  shapes.shacl             SHACL shapes run on the uplifted RDF
plugins/portolan-rashid/   validator plugin that runs rashid on examples and tests
build/                     generated on push by GitHub Actions; do not edit
```

Template and tooling: [opengeospatial/bblock-template](https://github.com/opengeospatial/bblock-template) and its [USAGE.md](https://github.com/opengeospatial/bblock-template/blob/master/USAGE.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
