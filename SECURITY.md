# Security policy

Building this register runs code: the OGC postprocessor, and the validator plugin this repository declares. This file says how to report a problem and what this repository can vouch for. It follows the structure in the OGC Blocks [security guidance](https://ogcincubator.github.io/bblocks-docs/create/security).

## Reporting a problem

Report a suspected security issue privately, through GitHub's [private vulnerability reporting](https://github.com/cayetanobv/bblocks-portolan/security/advisories/new) for this repository. Don't open a public issue.

Include:

- the affected building block identifier, such as `portolan.stac.profile-v0-3-0`;
- the plugin, import or workflow declaration involved, if any;
- whether the issue could reach registers that import this one.

## Scope

In scope, because this repository maintains them:

- the building block sources under `_sources/`;
- the validator plugin under `plugins/portolan-rashid/` and its declarations under `plugins.validators` in `bblocks-config.yaml`;
- the GitHub Actions workflows under `.github/workflows/`;
- the Python client under `client/`.

Out of scope, because this repository can't vouch for them:

- the imported registers listed under `imports` in `bblocks-config.yaml` (the OGC main register and `@ogc/stac`), and everything they import in turn. Imports resolve by URL at build time and are not pinned;
- the OGC postprocessor and its workflows (`opengeospatial/bblocks-postprocess`);
- [rashid](https://github.com/portolan-sdi/rashid), which the plugin installs. Report rashid issues to its maintainers.

## Code that runs during a build

The register declares no transforms and no build plugins. It declares one validator plugin, installed twice:

| Entry | Installs | Runs on |
|---|---|---|
| 1 | `./plugins/portolan-rashid` and `rashid` at tag `v0.1.8` | blocks that check Portolan v0.2.0 |
| 2 | `./plugins/portolan-rashid` and `rashid` at tag `v0.4.0` | blocks that check Portolan v0.3.0 |

The plugin reads each example and test file, writes a temporary catalog around it and runs rashid's metadata rules offline. It reads no secrets and writes nothing outside its temporary directory. In CI it runs with the access the postprocessing job has. Its virtualenv keeps its dependencies apart from the postprocessor's but is not a security boundary.

Review any change to `plugins/`, to `plugins.validators` or to the rashid pins with the same care as any other code in this repository. Pin rashid to a release tag, never to a branch.
