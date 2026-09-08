# Portolan STAC Profile

A [Portolan](https://github.com/portolan-sdi/portolan-spec) catalog is a directory of STAC metadata and cloud-native geospatial data, served from plain object storage and consumable with zero infrastructure. This Building Block wraps the Portolan STAC profile so that it can be validated, documented, and composed with other Building Blocks.

The Building Block does not redefine the profile. Three artifacts remain the sources of record:

- The schema: `https://schemas.portolan-sdi.org/portolan/v0.2.0/schema.json`.
- The profile text, including the normative table of STAC extensions Portolan composes: [`stac/README.md`](https://github.com/portolan-sdi/portolan-spec/blob/main/stac/README.md) in portolan-spec.
- The specification: [`specs/portolan/core.md`](https://github.com/portolan-sdi/portolan-spec/blob/main/specs/portolan/core.md) and [`specs/portolan/formats.md`](https://github.com/portolan-sdi/portolan-spec/blob/main/specs/portolan/formats.md).

## Scope

Catalog and Collection. Items inherit conformance from their collection and do not declare the profile.

## What the schema enforces

The Portolan schema encodes the structural requirements that STAC core leaves optional. Among them:

- Every Catalog and Collection has a non-empty `title` and `description`. Every `child` and `item` link carries a `title`.
- Every asset has `href`, a media `type`, and at least one `role`. Absolute asset hrefs use `https`. Bucket schemes such as `s3://` are rejected.
- Every Collection declares `providers` with at least one `producer` and a `host` reachable through `url` or `email`.
- Collection `license` is never the deprecated `proprietary`.
- Every `bbox` contains only in-range WGS84 coordinates.
- Every Catalog and Collection links its `AGENTS.md` with `rel: "agents"` and its `README.md` with `rel: "describedby"`.

## What tooling checks

Some rules cannot be expressed in JSON Schema. The [rashid](https://github.com/portolan-sdi/rashid) validator checks them: the host provider is exactly one and listed last, the SPDX identifier is valid, `file:checksum` is a multihash and matches the bytes, and range requests work on the assets. Declaring the profile in `stac_extensions` is a claim of conformance. An object conforms when it passes rashid.

## STAC extensions

Portolan reuses established extensions rather than adding `portolan:` fields. The profile pins 13 upstream `stac-extensions` schemas plus the Portolan [partition extension](https://github.com/portolan-sdi/stac-partition-extension), each with a requirement level and the condition under which it applies. Two of them, Raster and Themes, exist as Building Blocks in [`bblocks-stac`](https://ogcincubator.github.io/bblocks-stac/) and are declared as dependencies here. The others are referenced by schema URL until a Building Block exists for each.

## Examples

The examples are copies of files in the [Portolan reference catalog](https://github.com/portolan-sdi/portolan-spec/tree/main/examples/catalog/portolan-reference), taken on 8 September 2026. Relative hrefs in them point into that catalog.

## Versioning

The Building Block version follows the Portolan specification version. This block wraps v0.2.0, released on 28 August 2026. Earlier schema versions stay published at their own URLs.
