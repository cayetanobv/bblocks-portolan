# Portolan STAC Profile (v0.2.0)

This block checks objects against the Portolan specification **v0.2.0**, released on 28 August 2026. Most published Portolan catalogs declare this version. The current version is in the `portolan.stac.profile` block.

The block does not redefine the profile. The sources of record are:

- The schema: `https://schemas.portolan-sdi.org/portolan/v0.2.0/schema.json`.
- The profile text: [`stac/README.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.2.0/stac/README.md) at the `v0.2.0` tag.
- The specification: [`core.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.2.0/specs/portolan/core.md) and [`formats.md`](https://github.com/portolan-sdi/portolan-spec/blob/v0.2.0/specs/portolan/formats.md) at the same tag.

## Why a block per version

The STAC Building Blocks keep one base block and a thin block per STAC version that builds on it, because STAC versions add rules. Portolan versions also change rules: a v0.2.0 object fails v0.3.0, which requires the v0.3.0 schema in `stac_extensions`. So this block stands on its own. It composes the STAC Collection block with the v0.2.0 schema, and does not build on `portolan.stac.profile`.

## Differences from v0.3.0

The test files show the rules that differ between the two versions:

| Rule | v0.2.0 | v0.3.0 | Test file here |
|---|---|---|---|
| Absolute asset `href` with a scheme other than `https` (such as `s3://`) | Fails, even with an `https` alternate | Passes with an `https` URL in `alternate` | `s3-asset-href-with-https-alternate-fail.json` |
| Data asset `href` with `*` or `[` | Passes | Fails | `data-asset-href-glob.json` |
| PMTiles asset without the `visual` role | Passes | Fails | `pmtiles-asset-without-visual-role.json` |
| `partition:glob` with `https` | Passes | Fails | the partitioned example |
| Classes of a classified raster | Not checked | Placement and `title` checked | none |

The rules both versions share are tested by `missing-agents-link-fail.json`, `proprietary-license-fail.json` and `s3-asset-href-fail.json`.

## What the SHACL shapes check

The v0.2.0 schema, like the v0.3.0 one, leaves the SPDX identifier and the licence link for `other` to tooling. `shapes.shacl` checks those, and the logo title recommendation, on the RDF that the JSON-LD context produces. The shapes and requirements are the same as in v0.3.0:

| Rule | Requirement | Same check in rashid | Level |
|---|---|---|---|
| `license` is an SPDX identifier or `other` | `PORTO-CORE-059` | `PTL-LIC-001` | error |
| `license: other` has a `rel: license` link | `PORTO-CORE-059` | `PTL-LIC-002` | error |
| A logo link (`rel: icon`) has a title | `PORTO-CORE-076` | `PTL-LNK-008` | warning |

`license-not-spdx-fail.json` and `license-other-without-link-fail.json` pass the JSON Schema and fail only these shapes. `license-other-with-link.json` passes. `icon-link-without-title.json` passes with a warning. The block's `context.jsonld` maps the `type` values `Catalog` and `Collection` to the STAC ontology classes so that the shapes find their targets.

## What the rashid plugin checks

The register's [rashid](https://github.com/portolan-sdi/rashid) validator plugin also runs on this block. Each rashid release checks one Portolan version, the newest it knows, and rashid 0.4.0 applies the v0.3.0 rules. So for this block the plugin runs rashid 0.1.8, the release portolan-spec pins at its `v0.2.0` tag, which bundles the v0.2.0 schema. The block's `role: validation` resource in `bblock.json` names the v0.2.0 schema, and the copy of the plugin installed with rashid 0.1.8 is the one that handles it.

With rashid 0.1.8, the v0.2.0 rules hold: `data-asset-href-glob.json` and `pmtiles-asset-without-visual-role.json` pass, and `s3-asset-href-with-https-alternate-fail.json` fails. Every negative test fails on the rule it was written to break:

| Test file | rashid check | Requirement |
|---|---|---|
| `license-not-spdx-fail.json` | `PTL-LIC-001` | `PORTO-CORE-059` |
| `license-other-without-link-fail.json` | `PTL-LIC-002` | `PORTO-CORE-059` |
| `missing-agents-link-fail.json` | `PTL-FIL-002` | `PORTO-CORE-061` |
| `proprietary-license-fail.json` | `PTL-LIC-003` | `PORTO-CORE-060` |
| `s3-asset-href-fail.json` | `PTL-AST-002` | `PORTO-CORE-023` |
| `s3-asset-href-with-https-alternate-fail.json` | `PTL-AST-002` | `PORTO-CORE-023` |

The plugin runs rashid's metadata rules only, offline, on a minimal catalog written around each document. The `portolan.stac.profile-v0-3-0` block describes how.

## STAC extensions

v0.2.0 pins 13 upstream `stac-extensions` schemas plus the Portolan partition extension. Five of them exist as Building Blocks in [`bblocks-stac`](https://ogcincubator.github.io/bblocks-stac/) at the pinned version and are declared as dependencies: File Info v2.1.0, Raster v2.0.0, Scientific Citation v1.0.0, Themes v1.0.0 and Versioning Indicators v1.2.0.

## Examples

The catalog, vector, tabular and raster examples are copies of files in the [Portolan reference catalog](https://github.com/portolan-sdi/portolan-spec/tree/v0.2.0/examples/catalog/portolan-reference) at the `v0.2.0` tag. The partitioned example comes from [`stac/examples`](https://github.com/portolan-sdi/portolan-spec/tree/v0.2.0/stac/examples). The test files each change one field of the vector example, except `icon-link-without-title.json`, which removes the logo title from the catalog example.

As with the current block, rules the schema cannot express are checked by [rashid](https://github.com/portolan-sdi/rashid).
