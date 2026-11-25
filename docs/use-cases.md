# Using the Portolan building blocks

Validation in CI is one use of these blocks. The [OGC Building Blocks documentation](https://ogcincubator.github.io/bblocks-docs/) describes several more. This page maps them to Portolan and says, for each one, what works today and what still needs work.

Status as of 24 November 2026.

## 1. Validation

*OGC docs: [Quality control for a standard](https://ogcincubator.github.io/bblocks-docs/usecases/usecases#quality-control-for-a-standard).*

- **Publishers** check a catalog before they publish it, with the [`portolan-bblocks`](../client/README.md) client (`portolan-bblocks check <catalog URL>`) or with any JSON Schema or SHACL tool pointed at a block. No rashid install is needed for those layers.
- **Registries and hosting platforms** can use a block as an acceptance gate: a catalog is accepted when it conforms to `portolan.stac.profile-v0-3-0`.
- **Specification maintainers** get every example and negative test checked on each build, by three layers: the JSON Schema, SHACL shapes on the JSON-LD graph, and the rashid validator plugin. See [How the blocks validate](../README.md#how-the-blocks-validate).

**Today:** the client checks real catalogs against the JSON Schema. Running the SHACL shapes and rashid on real catalogs from the client is planned. [rashid](https://github.com/portolan-sdi/rashid) stays the authority on full conformance, including the file and live checks.

## 2. Profiles built on Portolan

*OGC docs: [Profiling a standard](https://ogcincubator.github.io/bblocks-docs/usecases/usecases#profiling-a-standard), [Designing reusable infrastructure](https://ogcincubator.github.io/bblocks-docs/usecases/usecases#designing-reusable-infrastructure).*

A national SDI, an agency or a project can define its own profile on top of Portolan and write only its additional rules:

```yaml
# schema.yaml of a hypothetical profile block
allOf:
  - $ref: bblocks://portolan.stac.profile-v0-3-0
  - properties:
      keywords:
        contains:
          enum: [inspire-hydrography, inspire-transport]
```

The profile inherits every Portolan, STAC and STAC extension rule, the SHACL shapes and the rashid checks of the block it builds on. Its own examples and negative tests are validated the same way. A profile is a block in another register that imports this one. Nothing in this repository changes.

**Today:** possible now. There is no example profile yet.

## 3. Linked data and knowledge graphs

*OGC docs: [Linked Data](https://ogcincubator.github.io/bblocks-docs/use/linked-data), [Semantic uplift](https://ogcincubator.github.io/bblocks-docs/create/semantic-uplift).*

The JSON-LD context turns a Portolan Catalog or Collection into RDF: its title becomes `dct:title`, its licence `dct:license`, its links `rdfs:seeAlso` nodes typed by IANA relation. That RDF can be loaded into a triplestore (the postprocess tool can push a register to a SPARQL endpoint) and queried with other OGC and DCAT data.

**Today:** limited by the STAC contexts in [bblocks-stac](https://github.com/ogcincubator/bblocks-stac), which map assets to a single link and providers to empty nodes. Richer asset and provider contexts upstream would make most of a Portolan collection queryable.

## 4. Transforms

*OGC docs: [Transforms](https://ogcincubator.github.io/bblocks-docs/create/transforms).*

A block can publish conversions, written in jq, SPARQL, Python and other languages, that clients discover from the register and run as ready-made adapters. The build runs each transform on the block's examples, so the outputs are tested.

A natural transform for Portolan is **Portolan Collection to a DCAT or GeoDCAT dataset**, so that data catalogues can harvest Portolan catalogs.

**Today:** no transform is published yet. OGC's Python client does not run transforms, so a consumer runs them itself.

## 5. AI agents

*OGC docs: [AI readiness](https://ogcincubator.github.io/bblocks-docs/usecases/ai-readiness), [Discovering relevant OGC standards](https://ogcincubator.github.io/bblocks-docs/usecases/usecases#discovering-relevant-ogc-standards), [the meta-register](https://ogcincubator.github.io/bblocks-docs/use/finding#the-meta-register-catalog-cross-register-search). Agent skill: [bblocks-consuming](https://github.com/ogcincubator/ogc-llm-skills/tree/main/skills/bblocks/consuming).*

| Use | How it works | For Portolan |
|---|---|---|
| Discovery | The OGC meta-register indexes registers and offers keyword and semantic search, a REST API and an MCP server for agents. | An agent asking how to publish a cloud-native catalog can find these blocks. The register is not indexed in the meta-register yet. |
| Grounding | Small, identified blocks with examples and negative tests give an agent a compact, authoritative context instead of a long specification. | An agent writing a `collection.json` uses the examples and `-fail` tests as the edges of what is valid. |
| Verification loop | The agent generates content, a block validates it, the agent fixes it. The output is checked, not just plausible. | Portolan catalogs already carry `AGENTS.md` guidance for agents, which could point to the block to validate against. A small MCP tool around the client would make the loop one call. |

## Next steps

In order of value for the effort:

1. **Index the register in the OGC meta-register**, so that agents and people find it through search and MCP. The meta-register is run by OGC.
2. **Close the agent loop**: a validation tool for agents (an MCP tool or a skill) built on the client, and a pointer to the block in Portolan's `AGENTS.md` guidance.
3. **Publish a Portolan to GeoDCAT transform.**
4. **Publish an example profile on top of Portolan**, for a real SDI.

The meta-register and the AI readiness use case are marked as in development and first draft in the OGC documentation, so their details may change.
