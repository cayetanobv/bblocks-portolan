# portolan-bblocks

Check Portolan catalogs against the Portolan OGC Building Blocks.

The register in this repository publishes the block `portolan.stac.profile`. This client loads that block from the register with the OGC [`bblocks_client`](https://github.com/ogcincubator/bblocks-client-python) library, walks a catalog from its root, and checks every catalog and collection it finds. It checks JSON conformance only: what the STAC metadata shows. Checksums, range requests, file internals and Items need [rashid](https://github.com/portolan-sdi/rashid), which remains the authority on Portolan conformance.

## Install

Python 3.10 or newer.

```bash
cd client
python3 -m venv .venv
.venv/bin/pip install -e ".[test]"
```

With uv: `uv run --project client portolan-bblocks …`.

## Check a catalog

```bash
portolan-bblocks check https://data.source.coop/nlebovits/pergamino-ide/catalog.json
portolan-bblocks check ./my-catalog/catalog.json --json report.json
portolan-bblocks check --config catalogs.yaml
```

Each object is checked twice:

- **declared**: against the block with the Portolan schema of the version the object declares in `stac_extensions`. This is the conformance answer.
- **published**: against the block as published (today Portolan v0.3.0). This shows what an older catalog must change to upgrade.

The command exits with 0 when every object conforms to the version it declares, and 1 otherwise. `--against published` makes the published block decide instead. `--all` lists every problem, and `--json FILE` writes the full report.

Sample output:

```
https://pub-1e760dc850cb4a5aa5f8afb77713f8cd.r2.dev/catalog.json
  block     portolan.stac.profile (Portolan v0.3.0) from https://cayetanobv.github.io/bblocks-portolan/build/register.json
  checked   4 objects (3 Collection, 1 Catalog) in 2.1s
  declares  v0.2.0 4
  conform to the version they declare:  4/4
  pass the block as published (v0.3.0): 0/4

  Most common problems against the published block (v0.3.0):
        4  stac_extensions: no entry matches {"const":"https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json"}
        1  partition:glob: "https://…/tiles/h3_cell=*/*.parquet" must not match {"pattern":"^[Hh][Tt][Tt][Pp][Ss]?://"}

  RESULT PASS
```

## Check single documents

```bash
portolan-bblocks validate collection.json https://example.org/catalog.json
```

## Use another register or block

```bash
portolan-bblocks check CATALOG --register https://example.org/bblocks/build/register.json --block example.national-profile
portolan-bblocks blocks --imports --filter stac
```

A block in another register that builds on `portolan.stac.profile` works the same way: the client follows that register's imports to find it.

## Test unpublished changes to the register

Build the register locally with `./build.sh` at the repository root, then add `--local`:

```bash
portolan-bblocks check CATALOG --local
```

The client then reads `build-local/register.json` and maps its `http://localhost:9090/register/` URLs to files in the checkout.

## Tests

```bash
.venv/bin/pytest -m "not network"   # offline unit tests
.venv/bin/pytest                    # also the tests that use the published register
```

The network tests check that every example in `_sources/` passes, that every `*-fail.json` test file fails on the field it targets, and that a local catalog made of the examples passes end to end.

Tests for a block that is not published yet skip themselves. To run them against the local build, run `./build.sh` at the repository root, then `PORTOLAN_BBLOCKS_LOCAL=1 .venv/bin/pytest`.
