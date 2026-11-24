# portolan-bblocks-rashid

An OGC Building Blocks [validator plugin](https://ogcincubator.github.io/bblocks-docs/create/validation#validator-plugins) that runs the [rashid](https://github.com/portolan-sdi/rashid) Portolan validator on each JSON example and test file of a Portolan building block. Findings appear in the Plugin section of the block's validation report. rashid errors fail the block.

## How a block opts in

Add a `role: validation` resource to `bblock.json` that names the Portolan schema of the version to check:

```json
"resources": [
  {
    "role": "validation",
    "ref": "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "format": "application/schema+json",
    "conformsTo": "https://github.com/portolan-sdi/rashid",
    "title": "Portolan v0.3.0 rules checked by the rashid validator plugin"
  }
]
```

## One copy per rashid pin

A rashid release checks one Portolan version, the newest it knows. `bblocks-config.yaml` installs this package once per rashid pin, each in its own virtualenv, and each copy handles only the blocks whose resource names its version:

| Portolan | rashid | Why |
|---|---|---|
| v0.2.0 | 0.1.8 | pinned by portolan-spec at its `v0.2.0` tag; bundles the v0.2.0 schema |
| v0.3.0 | 0.4.0 | pinned by portolan-spec at its `v0.3.0` tag; applies the v0.3.0 rules |

A block whose version no copy matches gets no rashid results. Add a pin to `bblocks-config.yaml`, and to `_LEGACY_TARGETS` in the module if that rashid release predates `rashid.api.newest_profile_version`.

## What it checks

rashid validates a whole catalog tree. The plugin writes each document into a minimal catalog with stub `AGENTS.md` and `README.md` files, runs rashid with file and live checks off, and keeps only the findings on that document. Link resolution (`PTL-LNK-006`) is left out because it needs the real tree. Catalogs and Collections are checked; other JSON files are skipped.
