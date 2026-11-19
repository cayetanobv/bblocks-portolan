# Portolan STAC Profile

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

Some rules cannot be expressed in JSON Schema. The [rashid](https://github.com/portolan-sdi/rashid) validator checks them: the host provider is exactly one and listed last, the SPDX identifier is valid, `file:checksum` is a multihash and matches the bytes, range requests work on the assets, and the file-level format rules hold. Declaring the profile in `stac_extensions` is a claim of conformance. An object conforms when it passes rashid.

## STAC extensions

Portolan reuses established extensions rather than adding `portolan:` fields. The profile pins 17 upstream `stac-extensions` schemas plus the Portolan [partition extension](https://github.com/portolan-sdi/stac-partition-extension), each with a requirement level and the condition under which it applies. Seven of them exist as Building Blocks in [`bblocks-stac`](https://ogcincubator.github.io/bblocks-stac/) at the version Portolan pins, and are declared as dependencies here: Classification v2.0.0, Datacube v2.3.0, File Info v2.1.0, Raster v2.0.0, Scientific Citation v1.0.0, Themes v1.0.0, and Versioning Indicators v1.2.0. The others are referenced by schema URL until a Building Block exists for each.

## Examples

The catalog, vector, tabular, and raster examples are copies of files in the [Portolan reference catalog](https://github.com/portolan-sdi/portolan-spec/tree/v0.3.0/examples/catalog/portolan-reference) at the `v0.3.0` tag. The classified raster and partitioned examples come from [`stac/examples`](https://github.com/portolan-sdi/portolan-spec/tree/v0.3.0/stac/examples). Relative hrefs in them point into those trees.

The negative tests in `tests/` each change one field of an example so that it breaks exactly one rule.

## Versioning

The Building Block version follows the Portolan specification version. This block wraps v0.3.0, released on 17 November 2026. Earlier schema versions stay published at their own URLs.
