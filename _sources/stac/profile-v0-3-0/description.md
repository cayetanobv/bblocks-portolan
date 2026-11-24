# Portolan STAC Profile (v0.3.0)

A [Portolan](https://github.com/portolan-sdi/portolan-spec) catalog is a directory of STAC metadata and cloud-native geospatial data, served from plain object storage and consumable with zero infrastructure. This Building Block wraps the Portolan STAC profile so that it can be validated, documented, and composed with other Building Blocks.

The Building Block does not redefine the profile. Three artifacts remain the sources of record:

- The schema: `https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json`.
- The profile text, including the normative table of STAC extensions Portolan composes: [`stac/README.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/stac/README.md) in portolan-spec.
- The specification: [`specs/portolan/core.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/specs/portolan/core.md) and [`specs/portolan/formats.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/specs/portolan/formats.md).

## Scope

Catalog and Collection. The block is a profile of the STAC Collection Building Block (`isProfileOf: ogc.contrib.stac.collection`). Items inherit conformance from their collection and do not declare the profile. The v0.3.0 schema has a branch for Items, which the rashid validator applies; this block does not cover Items yet.

## What the schema enforces

The Portolan schema encodes the structural requirements that STAC core leaves optional. Among them:

- Every Catalog and Collection has a non-empty `title` and `description`. Every `child` and `item` link carries a `title`.
- Every asset has `href`, a media `type`, and at least one `role`. An absolute asset href that does not use `https`, such as `s3://`, needs an `https` URL in the asset's `alternate` field.
- A data asset href links to one file: it contains no `*` and no `[`.
- A PMTiles asset has the `visual` role.
- `partition:glob` is an absolute URL that clients can list, so its scheme is not `http` or `https`.
- Classes of a classified raster sit in `classification:classes` on the asset for a single-band raster and on the band in `bands` for a multiband raster. Every class has a `title`. A class list in the legacy `raster:bands` fails.
- Every Collection declares `providers` with at least one `producer` and a `host` reachable through `url` or `email`.
- Collection `license` is never the deprecated `proprietary`.
- Every `bbox` contains only in-range WGS84 coordinates.
- Every Catalog and Collection links its `AGENTS.md` with `rel: "agents"` and its `README.md` with `rel: "describedby"`.

The format rules skip assets with the `source` role.

## What tooling checks

Some rules cannot be expressed in JSON Schema. The [rashid](https://github.com/portolan-sdi/rashid) validator checks them: the host provider is exactly one and listed last, the SPDX identifier is valid, a collection whose producer and host differ is a mirror and links its source, `file:checksum` is a multihash and matches the bytes, range requests work on the assets, and the file-level format rules hold. Declaring the profile in `stac_extensions` is a claim of conformance. An object conforms when it passes rashid.

This block runs rashid itself on its examples and tests, through the rashid validator plugin described below. File and live checks need the published catalog and stay outside the block for now.

## What the SHACL shapes check

Some of the rules the schema leaves to tooling can be read from the metadata of one document. `shapes.shacl` checks those on the RDF that the JSON-LD context produces, so any SHACL tool can apply them, not only rashid:

| Rule | Requirement | Same check in rashid | Level |
|---|---|---|---|
| `license` is an SPDX identifier or `other` | `PORTO-CORE-059` | `PTL-LIC-001` | error |
| `license: other` has a `rel: license` link | `PORTO-CORE-059` | `PTL-LIC-002` | error |
| A logo link (`rel: icon`) has a title | `PORTO-CORE-076` | `PTL-LNK-008` | warning |

The SPDX list is rashid's, so the two give the same answer. `scripts/spdx_shacl_list.py` regenerates it. The test files `license-not-spdx-fail.json` and `license-other-without-link-fail.json` pass the JSON Schema and fail only these shapes. `icon-link-without-title.json` passes with a warning.

The block's `context.jsonld` maps the `type` values `Catalog` and `Collection` to the STAC ontology classes, so the shapes, and the STAC core shapes, find their targets. Rules on assets and providers, such as exactly one host provider listed last, need the STAC contexts to map those objects first.

## What the rashid plugin checks

The register declares an OGC [validator plugin](https://ogcincubator.github.io/bblocks-docs/create/validation#validator-plugins), in `plugins/portolan-rashid`, that runs rashid on each example and test file of this block. The block opts in with a `role: validation` resource in `bblock.json` that names the Portolan v0.3.0 schema. The plugin then runs rashid 0.4.0, the release portolan-spec pins for v0.3.0.

rashid validates a whole catalog, so the plugin writes each document into a minimal catalog with stub `AGENTS.md` and `README.md` files and keeps only rashid's findings on that document. It runs rashid's metadata rules offline, without file or live checks, and leaves out link resolution (`PTL-LNK-006`), which needs the real tree. Each finding is reported with its rashid check and its Portolan requirement. rashid errors fail the block, warnings and notes do not.

Every negative test fails in rashid on the rule it was written to break:

| Test file | rashid check | Requirement |
|---|---|---|
| `class-without-title-fail.json` | `PTL-CLS-002` | `PORTO-FMT-052` |
| `classes-in-raster-bands-fail.json` | `PTL-CLS-005` | `PORTO-FMT-050` |
| `classes-on-asset-of-multiband-raster-fail.json` | `PTL-CLS-005` | `PORTO-FMT-050` |
| `data-asset-href-glob-fail.json` | `PTL-AST-012` | `PORTO-FMT-065` |
| `license-not-spdx-fail.json` | `PTL-LIC-001` | `PORTO-CORE-059` |
| `license-other-without-link-fail.json` | `PTL-LIC-002` | `PORTO-CORE-059` |
| `missing-agents-link-fail.json` | `PTL-FIL-002` | `PORTO-CORE-061` |
| `mirror-without-via-fail.json` | `PTL-PRO-001` | `PORTO-CORE-053` |
| `partition-glob-https-fail.json` | `PTL-PRT-002` | `PORTO-FMT-064` |
| `pmtiles-asset-without-visual-role-fail.json` | `PTL-AST-009` | `PORTO-FMT-062` |
| `proprietary-license-fail.json` | `PTL-LIC-003` | `PORTO-CORE-060` |
| `s3-asset-href-fail.json` | `PTL-AST-002` | `PORTO-CORE-087` |

`mirror-without-via-fail.json` is the Boston example without its `via` link. City of Boston is its producer and Portolan SDI its host, so it is a mirror and needs one. The JSON Schema and the SHACL shapes pass it. Only the plugin fails it.

rashid also checks rules no schema or shape here can, such as the mirror rules: it is how the classified raster example's missing `via` link was found. The examples and valid tests pass with warnings for SHOULD rules, such as assets without `file:checksum`.

## STAC extensions

Portolan reuses established extensions rather than adding `portolan:` fields. The profile pins 17 upstream `stac-extensions` schemas plus the Portolan [partition extension](https://github.com/portolan-sdi/stac-partition-extension), each with a requirement level and the condition under which it applies. Seven of them exist as Building Blocks in [`bblocks-stac`](https://ogcincubator.github.io/bblocks-stac/) at the version Portolan pins, and are declared as dependencies here: Classification v2.0.0, Datacube v2.3.0, File Info v2.1.0, Raster v2.0.0, Scientific Citation v1.0.0, Themes v1.0.0, and Versioning Indicators v1.2.0. The others are referenced by schema URL until a Building Block exists for each.

## Examples

The catalog, vector, tabular, and raster examples are copies of files in the [Portolan reference catalog](https://github.com/portolan-sdi/portolan-spec/tree/v0.3.0/examples/catalog/portolan-reference) at the `v0.3.0` tag. The classified raster and partitioned examples come from [`stac/examples`](https://github.com/portolan-sdi/portolan-spec/tree/v0.3.0/stac/examples). Relative hrefs in them point into those trees.

The classified raster example differs from its source in one way. GEP is its producer and Portolan SDI its host, which makes it a mirror, and a mirror needs a `rel: via` link and `updated` (PORTO-CORE-053 and PORTO-CORE-057). The source file has neither ([portolan-spec#281](https://github.com/portolan-sdi/portolan-spec/issues/281)). Our copy, and the test files built from it, add a `via` link to the GEP site and `updated`. The patch goes once the spec fixes its example.

The negative tests in `tests/` each change one field of an example so that it breaks exactly one rule.

## Versioning

The Building Block version follows the Portolan specification version. This block wraps v0.3.0, released on 17 November 2026. The `portolan.stac.profile` block points to this one while v0.3.0 is the latest version, and the `portolan.stac.profile-v0-2-0` block checks objects that declare v0.2.0. Earlier schema versions stay published at their own URLs.
