
# Portolan STAC Profile (Schema)

`portolan.stac.profile` *v0.3.0*

A STAC Catalog or Collection that conforms to the latest Portolan specification, now v0.3.0. It points to the block of that version, such as portolan.stac.profile-v0-3-0. Reference this block to follow new Portolan versions, or a versioned block to stay on one.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Portolan STAC Profile

A [Portolan](https://github.com/portolan-sdi/portolan-spec) catalog is a directory of STAC metadata and cloud-native geospatial data, served from plain object storage and consumable with zero infrastructure.

This block always checks against the **latest** Portolan version, now **v0.3.0**. It adds no rules of its own: its schema points to the block of that version. Reference it to follow new Portolan versions as they are released.

To stay on one version, reference a versioned block instead, as the STAC Building Blocks do:

| Block | Portolan version |
|---|---|
| `portolan.stac.profile-v0-3-0` | v0.3.0, released on 17 November 2026 (current) |
| `portolan.stac.profile-v0-2-0` | v0.2.0, released on 28 August 2026 |

The rules each version enforces, its test files and the differences between versions are documented in the versioned blocks. Like them, this block is checked by the rashid validator plugin, with the rashid release that matches the latest version. The examples here are those of the v0.3.0 block.

## Examples

### Root catalog
The root of the Portolan reference catalog. A Catalog declares the profile schema in
`stac_extensions`, carries a `title` and `description`, gives every `child` link a title,
and links its `AGENTS.md` (`rel: agents`) and `README.md` (`rel: describedby`). It also
links a logo (`rel: icon`) and its translations (`rel: alternate`, Language extension).

#### json
```json
{
  "type": "Catalog",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "portolan-reference",
  "title": "Portolan Reference Catalog",
  "description": "A mixed reference catalog exercising every major case in the Portolan v0.1 specification with real, openly licensed data pulled from its original upstream sources, vector polygons and points, raster, tabular, mirror provenance, nested catalogs and flat collections.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "child",
      "href": "./reference/catalog.json",
      "type": "application/json",
      "title": "Reference Basemaps"
    },
    {
      "rel": "child",
      "href": "./boundaries/catalog.json",
      "type": "application/json",
      "title": "Administrative Boundaries"
    },
    {
      "rel": "child",
      "href": "./mirror/catalog.json",
      "type": "application/json",
      "title": "Mirrored Collections"
    },
    {
      "rel": "child",
      "href": "./raster/catalog.json",
      "type": "application/json",
      "title": "Raster Data"
    },
    {
      "rel": "child",
      "href": "./tabular/catalog.json",
      "type": "application/json",
      "title": "Tabular Data"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "icon",
      "href": "./_assets/portolan-logo.png",
      "type": "image/png",
      "title": "Portolan SDI"
    },
    {
      "rel": "alternate",
      "href": "./ar/catalog.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-11-14T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "العربية",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Catalog",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "portolan-reference",
  "title": "Portolan Reference Catalog",
  "description": "A mixed reference catalog exercising every major case in the Portolan v0.1 specification with real, openly licensed data pulled from its original upstream sources, vector polygons and points, raster, tabular, mirror provenance, nested catalogs and flat collections.",
  "links": [
    {
      "rel": "root",
      "href": "./catalog.json",
      "type": "application/json"
    },
    {
      "rel": "child",
      "href": "./reference/catalog.json",
      "type": "application/json",
      "title": "Reference Basemaps"
    },
    {
      "rel": "child",
      "href": "./boundaries/catalog.json",
      "type": "application/json",
      "title": "Administrative Boundaries"
    },
    {
      "rel": "child",
      "href": "./mirror/catalog.json",
      "type": "application/json",
      "title": "Mirrored Collections"
    },
    {
      "rel": "child",
      "href": "./raster/catalog.json",
      "type": "application/json",
      "title": "Raster Data"
    },
    {
      "rel": "child",
      "href": "./tabular/catalog.json",
      "type": "application/json",
      "title": "Tabular Data"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "icon",
      "href": "./_assets/portolan-logo.png",
      "type": "image/png",
      "title": "Portolan SDI"
    },
    {
      "rel": "alternate",
      "href": "./ar/catalog.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-11-14T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .

<file:///github/workspace/portolan-reference> a stac:Catalog ;
    dct:description "A mixed reference catalog exercising every major case in the Portolan v0.1 specification with real, openly licensed data pulled from its original upstream sources, vector polygons and points, raster, tabular, mirror provenance, nested catalogs and flat collections." ;
    dct:title "Portolan Reference Catalog" ;
    rdfs:seeAlso [ rdfs:label "Tabular Data" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <file:///github/workspace/tabular/catalog.json> ],
        [ rdfs:label "Human-readable documentation" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ],
        [ rdfs:label "Reference Basemaps" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <file:///github/workspace/reference/catalog.json> ],
        [ rdfs:label "Administrative Boundaries" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <file:///github/workspace/boundaries/catalog.json> ],
        [ rdfs:label "Mirrored Collections" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <file:///github/workspace/mirror/catalog.json> ],
        [ rdfs:label "Arabic" ;
            dct:language "ar" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <file:///github/workspace/ar/catalog.json> ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///github/workspace/catalog.json> ],
        [ rdfs:label "Raster Data" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/child> ;
            oa:hasTarget <file:///github/workspace/raster/catalog.json> ],
        [ rdfs:label "Portolan SDI" ;
            dct:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/icon> ;
            oa:hasTarget <file:///github/workspace/_assets/portolan-logo.png> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/language/v1.0.0/schema.json" ;
    stac:version "1.1.0" .


```


### Vector collection (GeoParquet with PMTiles)
City of Boston open space. The GeoParquet asset carries `file:size` and `file:checksum`.
The PMTiles asset has the `visual` role and is also exposed through a `rel: pmtiles` link
(Web Map Links extension). `table:columns` documents the schema with a description for
every column.

#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "boundaries/boston-open-space",
  "title": "Boston Open Space",
  "description": "City of Boston open spaces and parks, playgrounds, athletic fields, conservation land, and cemeteries, 1,012 polygons from the City of Boston GIS open data platform. Official primary source, republished as cloud-native GeoParquet with a PMTiles visualization and MapLibre styles.",
  "license": "PDDL-1.0",
  "keywords": [
    "open-space",
    "parks",
    "boston",
    "recreation",
    "boundaries"
  ],
  "providers": [
    {
      "name": "City of Boston",
      "url": "https://data.boston.gov",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -71.190913,
          42.227891,
          -70.874864,
          42.396534
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-01-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "fid",
      "type": "bigint",
      "description": "Feature id that GDAL assigned when the generator read the source layer. Unique in this file. It is not an upstream key."
    },
    {
      "name": "OBJECTID",
      "type": "integer",
      "description": "Esri object ID that ArcGIS assigns to each row of the source layer. Unique in this file."
    },
    {
      "name": "SITE_NAME",
      "type": "varchar",
      "description": "Best-known or official site name. Multi-parcel sites carry Roman numeral suffixes, Stony Brook Reservation I and II."
    },
    {
      "name": "OWNERSHIP",
      "type": "varchar",
      "description": "Fee owner where known. City of Boston, Commonwealth of Massachusetts, private owners, and agency abbreviations like BRA and BNAN."
    },
    {
      "name": "PROTECTION",
      "type": "varchar",
      "description": "Slash-separated legal protection instruments. A97 is Article 97 of the Massachusetts Constitution, the strongest. Free text, match with LIKE."
    },
    {
      "name": "TYPECODE",
      "type": "integer",
      "description": "Numeric open space type 1 through 7. Disagrees with TypeLong on about 13 rows, treat TypeLong as closer to intent."
    },
    {
      "name": "DISTRICT",
      "type": "varchar",
      "description": "Planning district per the city's open space plan, not the official neighborhood boundaries. Includes the non-spatial value Multi-District."
    },
    {
      "name": "ACRES",
      "type": "double",
      "description": "Official area in acres of the open-space portion, the figure to use instead of computing geometry area."
    },
    {
      "name": "ADDRESS",
      "type": "varchar",
      "description": "Street address if known, null for 589 rows."
    },
    {
      "name": "ZonAgg",
      "type": "varchar",
      "description": "Aggregated zoning district, for example Open Space District."
    },
    {
      "name": "TypeLong",
      "type": "varchar",
      "description": "Open space type as text, with minor spelling variants worth normalizing before grouping."
    },
    {
      "name": "OS_Own_Jur",
      "type": "varchar",
      "description": "The entity holding the open-space rights. BPRD, DCR, the Boston Conservation Commission, or None."
    },
    {
      "name": "OS_Mngmnt",
      "type": "varchar",
      "description": "Managing entity only when it differs from OS_Own_Jur. Null means the steward manages it, not missing data."
    },
    {
      "name": "POS",
      "type": "varchar",
      "description": "Protected open space flag. X permanently protected, N not."
    },
    {
      "name": "PA",
      "type": "varchar",
      "description": "Public access flag. X accessible, A by appointment, N no or unknown access."
    },
    {
      "name": "ALT_NAME",
      "type": "varchar",
      "description": "Official, previous, or colloquial alternate names."
    },
    {
      "name": "AgncyJuris",
      "type": "varchar",
      "description": "Agency of jurisdiction for government-owned unprotected sites. Sparsely populated by design."
    },
    {
      "name": "ShapeSTAre",
      "type": "double",
      "description": "ArcGIS-computed area in square meters from the source State Plane geometry."
    },
    {
      "name": "ShapeSTLen",
      "type": "double",
      "description": "ArcGIS-computed perimeter in meters."
    },
    {
      "name": "geom",
      "type": "geometry",
      "description": "Site geometry, WGS84 longitude and latitude."
    },
    {
      "name": "bbox",
      "type": "struct(xmin double, ymin double, xmax double, ymax double)",
      "description": "Per-feature bounding box struct, the GeoParquet covering."
    }
  ],
  "table:primary_geometry": "geom",
  "table:row_count": 1012,
  "assets": {
    "data": {
      "href": "./boston-open-space.parquet",
      "type": "application/vnd.apache.parquet",
      "title": "Boston Open Space (GeoParquet)",
      "roles": [
        "data"
      ],
      "file:size": 1188770,
      "file:checksum": "122012852a6892d9f47810b6ad54959b22b840bdfbb118b136a25cc6dd7da41d3cff",
      "proj:code": "EPSG:4326",
      "description": "The 1,012 open space polygons with their attribute columns, in WGS84 longitude and latitude."
    },
    "visual": {
      "href": "./boston-open-space.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Boston Open Space (PMTiles)",
      "roles": [
        "visual"
      ],
      "file:size": 989217,
      "file:checksum": "1220db3d459dc821db7adf739ad0afee9682a3b94f8d467c564c343dcb159a2b3281",
      "description": "Vector tiles of the open space polygons for web maps, in one layer named boston-open-space."
    },
    "style-types": {
      "href": "./styles/types.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Open space by type",
      "roles": [
        "style",
        "default"
      ],
      "file:size": 1224,
      "file:checksum": "1220b1762e9d48bd88b6901687f255ac37fb6afc3618f46f2e4d8a569f4b9df5bfcc",
      "description": "TypeLong separates parks, parkways and reservations, cemeteries, urban wilds, malls and plazas, and community gardens."
    },
    "style-labeled": {
      "href": "./styles/labeled.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Types with site names",
      "roles": [
        "style"
      ],
      "file:size": 1586,
      "file:checksum": "12200ce7dcdabc5683bbd6348a8fee0d83b23c47a48cf03557d9eef73d5085a9d2ca",
      "description": "The type colouring with a SITE_NAME label per site."
    },
    "style-acreage": {
      "href": "./styles/acreage.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Acreage in four classes",
      "roles": [
        "style"
      ],
      "file:size": 828,
      "file:checksum": "122092647db9cb1290d34a8b4675e8e13548c4f45e6d2c26589726232bd0bb23d710",
      "description": "ACRES binned at one, ten, and one hundred acres, light to dark green, from pocket parks through Franklin Park's 392 acres."
    },
    "style-ownership": {
      "href": "./styles/ownership.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Who owns it",
      "roles": [
        "style"
      ],
      "file:size": 1363,
      "file:checksum": "1220430bfc3a3f3572e0156f3ce1ca91dbbdd6f1f2b360bf4f237ed8a26071a7fed5",
      "description": "OWNERSHIP from the catalog palette, city, Commonwealth, federal, and the 214 privately owned sites side by side."
    },
    "style-protection": {
      "href": "./styles/protection.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Permanently protected or not",
      "roles": [
        "style"
      ],
      "file:size": 1122,
      "file:checksum": "122029441a7dbf26793f87185cb67a1ee3e5055d271a6550c1cffad5b8fdaa349078",
      "description": "The POS flag, deep green where protection is permanent under Article 97 or a conservation restriction, gray where it is not. The inner match relabels the raw X and N codes so the legend a client derives from the outer match reads in plain words."
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview thumbnail over a light basemap. © OpenStreetMap contributors © CARTO.",
      "roles": [
        "thumbnail"
      ],
      "file:size": 377459,
      "file:checksum": "122061292d50d6b52d5452897669fe629173564b49f0d2538de5605331a323299fb0",
      "description": "A PNG map of the open space polygons over a light basemap."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "pmtiles",
      "href": "./boston-open-space.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Web map tiles",
      "pmtiles:layers": [
        "boston-open-space"
      ]
    },
    {
      "rel": "via",
      "href": "https://bostonopendata-boston.opendata.arcgis.com/datasets/2868d370c55d4d458d4ae2224ef8cddd_7",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/boundaries/boston-open-space/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "العربية",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "boundaries/boston-open-space",
  "title": "Boston Open Space",
  "description": "City of Boston open spaces and parks, playgrounds, athletic fields, conservation land, and cemeteries, 1,012 polygons from the City of Boston GIS open data platform. Official primary source, republished as cloud-native GeoParquet with a PMTiles visualization and MapLibre styles.",
  "license": "PDDL-1.0",
  "keywords": [
    "open-space",
    "parks",
    "boston",
    "recreation",
    "boundaries"
  ],
  "providers": [
    {
      "name": "City of Boston",
      "url": "https://data.boston.gov",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -71.190913,
          42.227891,
          -70.874864,
          42.396534
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-01-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "fid",
      "type": "bigint",
      "description": "Feature id that GDAL assigned when the generator read the source layer. Unique in this file. It is not an upstream key."
    },
    {
      "name": "OBJECTID",
      "type": "integer",
      "description": "Esri object ID that ArcGIS assigns to each row of the source layer. Unique in this file."
    },
    {
      "name": "SITE_NAME",
      "type": "varchar",
      "description": "Best-known or official site name. Multi-parcel sites carry Roman numeral suffixes, Stony Brook Reservation I and II."
    },
    {
      "name": "OWNERSHIP",
      "type": "varchar",
      "description": "Fee owner where known. City of Boston, Commonwealth of Massachusetts, private owners, and agency abbreviations like BRA and BNAN."
    },
    {
      "name": "PROTECTION",
      "type": "varchar",
      "description": "Slash-separated legal protection instruments. A97 is Article 97 of the Massachusetts Constitution, the strongest. Free text, match with LIKE."
    },
    {
      "name": "TYPECODE",
      "type": "integer",
      "description": "Numeric open space type 1 through 7. Disagrees with TypeLong on about 13 rows, treat TypeLong as closer to intent."
    },
    {
      "name": "DISTRICT",
      "type": "varchar",
      "description": "Planning district per the city's open space plan, not the official neighborhood boundaries. Includes the non-spatial value Multi-District."
    },
    {
      "name": "ACRES",
      "type": "double",
      "description": "Official area in acres of the open-space portion, the figure to use instead of computing geometry area."
    },
    {
      "name": "ADDRESS",
      "type": "varchar",
      "description": "Street address if known, null for 589 rows."
    },
    {
      "name": "ZonAgg",
      "type": "varchar",
      "description": "Aggregated zoning district, for example Open Space District."
    },
    {
      "name": "TypeLong",
      "type": "varchar",
      "description": "Open space type as text, with minor spelling variants worth normalizing before grouping."
    },
    {
      "name": "OS_Own_Jur",
      "type": "varchar",
      "description": "The entity holding the open-space rights. BPRD, DCR, the Boston Conservation Commission, or None."
    },
    {
      "name": "OS_Mngmnt",
      "type": "varchar",
      "description": "Managing entity only when it differs from OS_Own_Jur. Null means the steward manages it, not missing data."
    },
    {
      "name": "POS",
      "type": "varchar",
      "description": "Protected open space flag. X permanently protected, N not."
    },
    {
      "name": "PA",
      "type": "varchar",
      "description": "Public access flag. X accessible, A by appointment, N no or unknown access."
    },
    {
      "name": "ALT_NAME",
      "type": "varchar",
      "description": "Official, previous, or colloquial alternate names."
    },
    {
      "name": "AgncyJuris",
      "type": "varchar",
      "description": "Agency of jurisdiction for government-owned unprotected sites. Sparsely populated by design."
    },
    {
      "name": "ShapeSTAre",
      "type": "double",
      "description": "ArcGIS-computed area in square meters from the source State Plane geometry."
    },
    {
      "name": "ShapeSTLen",
      "type": "double",
      "description": "ArcGIS-computed perimeter in meters."
    },
    {
      "name": "geom",
      "type": "geometry",
      "description": "Site geometry, WGS84 longitude and latitude."
    },
    {
      "name": "bbox",
      "type": "struct(xmin double, ymin double, xmax double, ymax double)",
      "description": "Per-feature bounding box struct, the GeoParquet covering."
    }
  ],
  "table:primary_geometry": "geom",
  "table:row_count": 1012,
  "assets": {
    "data": {
      "href": "./boston-open-space.parquet",
      "type": "application/vnd.apache.parquet",
      "title": "Boston Open Space (GeoParquet)",
      "roles": [
        "data"
      ],
      "file:size": 1188770,
      "file:checksum": "122012852a6892d9f47810b6ad54959b22b840bdfbb118b136a25cc6dd7da41d3cff",
      "proj:code": "EPSG:4326",
      "description": "The 1,012 open space polygons with their attribute columns, in WGS84 longitude and latitude."
    },
    "visual": {
      "href": "./boston-open-space.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Boston Open Space (PMTiles)",
      "roles": [
        "visual"
      ],
      "file:size": 989217,
      "file:checksum": "1220db3d459dc821db7adf739ad0afee9682a3b94f8d467c564c343dcb159a2b3281",
      "description": "Vector tiles of the open space polygons for web maps, in one layer named boston-open-space."
    },
    "style-types": {
      "href": "./styles/types.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Open space by type",
      "roles": [
        "style",
        "default"
      ],
      "file:size": 1224,
      "file:checksum": "1220b1762e9d48bd88b6901687f255ac37fb6afc3618f46f2e4d8a569f4b9df5bfcc",
      "description": "TypeLong separates parks, parkways and reservations, cemeteries, urban wilds, malls and plazas, and community gardens."
    },
    "style-labeled": {
      "href": "./styles/labeled.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Types with site names",
      "roles": [
        "style"
      ],
      "file:size": 1586,
      "file:checksum": "12200ce7dcdabc5683bbd6348a8fee0d83b23c47a48cf03557d9eef73d5085a9d2ca",
      "description": "The type colouring with a SITE_NAME label per site."
    },
    "style-acreage": {
      "href": "./styles/acreage.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Acreage in four classes",
      "roles": [
        "style"
      ],
      "file:size": 828,
      "file:checksum": "122092647db9cb1290d34a8b4675e8e13548c4f45e6d2c26589726232bd0bb23d710",
      "description": "ACRES binned at one, ten, and one hundred acres, light to dark green, from pocket parks through Franklin Park's 392 acres."
    },
    "style-ownership": {
      "href": "./styles/ownership.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Who owns it",
      "roles": [
        "style"
      ],
      "file:size": 1363,
      "file:checksum": "1220430bfc3a3f3572e0156f3ce1ca91dbbdd6f1f2b360bf4f237ed8a26071a7fed5",
      "description": "OWNERSHIP from the catalog palette, city, Commonwealth, federal, and the 214 privately owned sites side by side."
    },
    "style-protection": {
      "href": "./styles/protection.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Permanently protected or not",
      "roles": [
        "style"
      ],
      "file:size": 1122,
      "file:checksum": "122029441a7dbf26793f87185cb67a1ee3e5055d271a6550c1cffad5b8fdaa349078",
      "description": "The POS flag, deep green where protection is permanent under Article 97 or a conservation restriction, gray where it is not. The inner match relabels the raw X and N codes so the legend a client derives from the outer match reads in plain words."
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview thumbnail over a light basemap. \u00a9 OpenStreetMap contributors \u00a9 CARTO.",
      "roles": [
        "thumbnail"
      ],
      "file:size": 377459,
      "file:checksum": "122061292d50d6b52d5452897669fe629173564b49f0d2538de5605331a323299fb0",
      "description": "A PNG map of the open space polygons over a light basemap."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "pmtiles",
      "href": "./boston-open-space.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Web map tiles",
      "pmtiles:layers": [
        "boston-open-space"
      ]
    },
    {
      "rel": "via",
      "href": "https://bostonopendata-boston.opendata.arcgis.com/datasets/2868d370c55d4d458d4ae2224ef8cddd_7",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/boundaries/boston-open-space/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <table:> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <pmtiles:> .
@prefix ns5: <file:> .
@prefix ns6: <proj:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/boundaries/boston-open-space> a stac:Collection ;
    dct:description "City of Boston open spaces and parks, playgrounds, athletic fields, conservation land, and cemeteries, 1,012 polygons from the City of Boston GIS open data platform. Official primary source, republished as cloud-native GeoParquet with a PMTiles visualization and MapLibre styles." ;
    dct:extent [ ] ;
    dct:license "PDDL-1.0" ;
    dct:subject "boston",
        "boundaries",
        "open-space",
        "parks",
        "recreation" ;
    dct:title "Boston Open Space" ;
    rdfs:seeAlso [ dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///catalog.json> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns3:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ],
        [ rdfs:label "Arabic" ;
            dct:language "ar" ;
            dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <file:///ar/boundaries/boston-open-space/collection.json> ],
        [ rdfs:label "Web map tiles" ;
            dct:type "application/vnd.pmtiles" ;
            ns3:relation <http://www.iana.org/assignments/relation/pmtiles> ;
            oa:hasTarget <file:///github/workspace/boston-open-space.pmtiles> ;
            ns4:layers "boston-open-space" ],
        [ rdfs:label "Original source" ;
            dct:type "text/html" ;
            ns3:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://bostonopendata-boston.opendata.arcgis.com/datasets/2868d370c55d4d458d4ae2224ef8cddd_7> ],
        [ dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ rdfs:label "Human-readable documentation" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns3:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ] ;
    stac:hasAsset [ ns1:data <file:///github/workspace/boston-open-space.parquet> ;
            ns1:style-acreage <file:///github/workspace/styles/acreage.json> ;
            ns1:style-labeled <file:///github/workspace/styles/labeled.json> ;
            ns1:style-ownership <file:///github/workspace/styles/ownership.json> ;
            ns1:style-protection <file:///github/workspace/styles/protection.json> ;
            ns1:style-types <file:///github/workspace/styles/types.json> ;
            ns1:thumbnail <file:///github/workspace/thumbnail.png> ;
            ns1:visual <file:///github/workspace/boston-open-space.pmtiles> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/language/v1.0.0/schema.json",
        "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json",
        "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json" ;
    stac:hasProvider [ ],
        [ ] ;
    stac:version "1.1.0" ;
    ns2:columns [ a <file:///github/workspace/varchar> ;
            dct:description "Official, previous, or colloquial alternate names." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Agency of jurisdiction for government-owned unprotected sites. Sparsely populated by design." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Planning district per the city's open space plan, not the official neighborhood boundaries. Includes the non-spatial value Multi-District." ],
        [ a <file:///github/workspace/bigint> ;
            dct:description "Feature id that GDAL assigned when the generator read the source layer. Unique in this file. It is not an upstream key." ],
        [ a <file:///github/workspace/double> ;
            dct:description "Official area in acres of the open-space portion, the figure to use instead of computing geometry area." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Managing entity only when it differs from OS_Own_Jur. Null means the steward manages it, not missing data." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Public access flag. X accessible, A by appointment, N no or unknown access." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Protected open space flag. X permanently protected, N not." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Fee owner where known. City of Boston, Commonwealth of Massachusetts, private owners, and agency abbreviations like BRA and BNAN." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Street address if known, null for 589 rows." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Best-known or official site name. Multi-parcel sites carry Roman numeral suffixes, Stony Brook Reservation I and II." ],
        [ a <file:///github/workspace/double> ;
            dct:description "ArcGIS-computed area in square meters from the source State Plane geometry." ],
        [ a <file:///github/workspace/integer> ;
            dct:description "Esri object ID that ArcGIS assigns to each row of the source layer. Unique in this file." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "The entity holding the open-space rights. BPRD, DCR, the Boston Conservation Commission, or None." ],
        [ dct:description "Per-feature bounding box struct, the GeoParquet covering." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Open space type as text, with minor spelling variants worth normalizing before grouping." ],
        [ a <file:///github/workspace/geometry> ;
            dct:description "Site geometry, WGS84 longitude and latitude." ],
        [ a <file:///github/workspace/double> ;
            dct:description "ArcGIS-computed perimeter in meters." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Aggregated zoning district, for example Open Space District." ],
        [ a <file:///github/workspace/integer> ;
            dct:description "Numeric open space type 1 through 7. Disagrees with TypeLong on about 13 rows, treat TypeLong as closer to intent." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Slash-separated legal protection instruments. A97 is Article 97 of the Massachusetts Constitution, the strongest. Free text, match with LIKE." ] ;
    ns2:primary_geometry "geom" ;
    ns2:row_count 1012 .

<file:///github/workspace/boston-open-space.parquet> ns5:checksum "122012852a6892d9f47810b6ad54959b22b840bdfbb118b136a25cc6dd7da41d3cff" ;
    ns5:size 1188770 ;
    dct:description "The 1,012 open space polygons with their attribute columns, in WGS84 longitude and latitude." ;
    dct:format "application/vnd.apache.parquet" ;
    dct:title "Boston Open Space (GeoParquet)" ;
    stac:hasAssetroles "data"^^<xsd:string> ;
    ns6:code "EPSG:4326" .

<file:///github/workspace/styles/acreage.json> ns5:checksum "122092647db9cb1290d34a8b4675e8e13548c4f45e6d2c26589726232bd0bb23d710" ;
    ns5:size 828 ;
    dct:description "ACRES binned at one, ten, and one hundred acres, light to dark green, from pocket parks through Franklin Park's 392 acres." ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Acreage in four classes" ;
    stac:hasAssetroles "style"^^<xsd:string> .

<file:///github/workspace/styles/labeled.json> ns5:checksum "12200ce7dcdabc5683bbd6348a8fee0d83b23c47a48cf03557d9eef73d5085a9d2ca" ;
    ns5:size 1586 ;
    dct:description "The type colouring with a SITE_NAME label per site." ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Types with site names" ;
    stac:hasAssetroles "style"^^<xsd:string> .

<file:///github/workspace/styles/ownership.json> ns5:checksum "1220430bfc3a3f3572e0156f3ce1ca91dbbdd6f1f2b360bf4f237ed8a26071a7fed5" ;
    ns5:size 1363 ;
    dct:description "OWNERSHIP from the catalog palette, city, Commonwealth, federal, and the 214 privately owned sites side by side." ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Who owns it" ;
    stac:hasAssetroles "style"^^<xsd:string> .

<file:///github/workspace/styles/protection.json> ns5:checksum "122029441a7dbf26793f87185cb67a1ee3e5055d271a6550c1cffad5b8fdaa349078" ;
    ns5:size 1122 ;
    dct:description "The POS flag, deep green where protection is permanent under Article 97 or a conservation restriction, gray where it is not. The inner match relabels the raw X and N codes so the legend a client derives from the outer match reads in plain words." ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Permanently protected or not" ;
    stac:hasAssetroles "style"^^<xsd:string> .

<file:///github/workspace/styles/types.json> ns5:checksum "1220b1762e9d48bd88b6901687f255ac37fb6afc3618f46f2e4d8a569f4b9df5bfcc" ;
    ns5:size 1224 ;
    dct:description "TypeLong separates parks, parkways and reservations, cemeteries, urban wilds, malls and plazas, and community gardens." ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Open space by type" ;
    stac:hasAssetroles "default"^^<xsd:string>,
        "style"^^<xsd:string> .

<file:///github/workspace/thumbnail.png> ns5:checksum "122061292d50d6b52d5452897669fe629173564b49f0d2538de5605331a323299fb0" ;
    ns5:size 377459 ;
    dct:description "A PNG map of the open space polygons over a light basemap." ;
    dct:format "image/png" ;
    dct:title "Preview thumbnail over a light basemap. © OpenStreetMap contributors © CARTO." ;
    stac:hasAssetroles "thumbnail"^^<xsd:string> .

<file:///github/workspace/boston-open-space.pmtiles> ns5:checksum "1220db3d459dc821db7adf739ad0afee9682a3b94f8d467c564c343dcb159a2b3281" ;
    ns5:size 989217 ;
    dct:description "Vector tiles of the open space polygons for web maps, in one layer named boston-open-space." ;
    dct:format "application/vnd.pmtiles" ;
    dct:title "Boston Open Space (PMTiles)" ;
    stac:hasAssetroles "visual"^^<xsd:string> .


```


### Tabular collection
Eurostat electricity prices. A Parquet table with no geometry column. The column schema
is the primary handle for consumers and agents.

#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/attribution/v0.1.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "tabular/eurostat-electricity-prices",
  "title": "Eurostat Electricity Prices for Household Consumers",
  "description": "Semi-annual electricity prices for household consumers across European countries by consumption band, tax component, and currency, Eurostat table nrg_pc_204. Non-geospatial companion table, join key is the country code column geo (NUTS-0), converted to cloud-native Parquet.",
  "license": "CC-BY-4.0",
  "keywords": [
    "energy",
    "electricity",
    "prices",
    "eurostat",
    "tabular"
  ],
  "providers": [
    {
      "name": "Eurostat",
      "url": "https://ec.europa.eu/eurostat",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -31.5,
          34.0,
          46.5,
          71.5
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2007-01-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "DATAFLOW",
      "type": "varchar",
      "description": "Eurostat dataflow identifier, the constant ESTAT nrg_pc_204 version 1.0."
    },
    {
      "name": "LAST UPDATE",
      "type": "timestamp",
      "description": "Frozen at one 2019 timestamp for every row of this snapshot while the data runs to 2025. Unreliable, do not derive freshness from it."
    },
    {
      "name": "freq",
      "type": "varchar",
      "description": "Observation frequency, the constant S for semi-annual. S1 is January to June, S2 is July to December."
    },
    {
      "name": "siec",
      "type": "varchar",
      "description": "Energy product code, the constant E7000 for electricity."
    },
    {
      "name": "nrg_cons",
      "type": "varchar",
      "description": "Annual consumption band. KWH_LT1000, KWH1000-2499, KWH2500-4999 the headline household band, KWH5000-14999, KWH_GE15000, and TOT_KWH the weighted all-band average that exists only from 2017-S2."
    },
    {
      "name": "unit",
      "type": "varchar",
      "description": "Unit of measure, the constant KWH. Prices are per kilowatt-hour."
    },
    {
      "name": "tax",
      "type": "varchar",
      "description": "Tax level. X_TAX excludes all taxes and levies, X_VAT excludes VAT and recoverable taxes, I_TAX includes everything a household pays."
    },
    {
      "name": "currency",
      "type": "varchar",
      "description": "EUR, NAC for national currency, or PPS purchasing power standard. NAC equals EUR in the euro area."
    },
    {
      "name": "geo",
      "type": "varchar",
      "description": "Reporting country as a Eurostat NUTS-0 code, ISO 3166-1 alpha-2 except EL for Greece and UK for the United Kingdom, plus the aggregates EU27_2020 and EA. The join key to a geometry Collection."
    },
    {
      "name": "TIME_PERIOD",
      "type": "varchar",
      "description": "Reference semester as a string, 2025-S2. Fixed format, so string ordering and MAX work."
    },
    {
      "name": "OBS_VALUE",
      "type": "double",
      "description": "The observed electricity price in the stated currency per kilowatt-hour."
    },
    {
      "name": "OBS_FLAG",
      "type": "varchar",
      "description": "Observation status, e estimated, p provisional, d definition differs, null for 98 percent of rows."
    },
    {
      "name": "CONF_STATUS",
      "type": "varchar",
      "description": "Confidentiality status, entirely null in this snapshot."
    }
  ],
  "table:row_count": 65466,
  "assets": {
    "data": {
      "href": "./eurostat-electricity-prices.parquet",
      "type": "application/vnd.apache.parquet",
      "title": "Eurostat Electricity Prices for Household Consumers (Parquet)",
      "roles": [
        "data"
      ],
      "file:size": 162919,
      "file:checksum": "122051a96f8677c374f6b54cb6e876dcf6af33bc2982b52c9445d0c9a857240b6477",
      "description": "The rows of Eurostat table nrg_pc_204, one price for each country or country group, half year, consumption band, tax level, and currency."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "via",
      "href": "https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/tabular/eurostat-electricity-prices/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "attribution": "Source, Eurostat",
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "العربية",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json",
    "https://stac-extensions.github.io/attribution/v0.1.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "tabular/eurostat-electricity-prices",
  "title": "Eurostat Electricity Prices for Household Consumers",
  "description": "Semi-annual electricity prices for household consumers across European countries by consumption band, tax component, and currency, Eurostat table nrg_pc_204. Non-geospatial companion table, join key is the country code column geo (NUTS-0), converted to cloud-native Parquet.",
  "license": "CC-BY-4.0",
  "keywords": [
    "energy",
    "electricity",
    "prices",
    "eurostat",
    "tabular"
  ],
  "providers": [
    {
      "name": "Eurostat",
      "url": "https://ec.europa.eu/eurostat",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -31.5,
          34.0,
          46.5,
          71.5
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2007-01-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "DATAFLOW",
      "type": "varchar",
      "description": "Eurostat dataflow identifier, the constant ESTAT nrg_pc_204 version 1.0."
    },
    {
      "name": "LAST UPDATE",
      "type": "timestamp",
      "description": "Frozen at one 2019 timestamp for every row of this snapshot while the data runs to 2025. Unreliable, do not derive freshness from it."
    },
    {
      "name": "freq",
      "type": "varchar",
      "description": "Observation frequency, the constant S for semi-annual. S1 is January to June, S2 is July to December."
    },
    {
      "name": "siec",
      "type": "varchar",
      "description": "Energy product code, the constant E7000 for electricity."
    },
    {
      "name": "nrg_cons",
      "type": "varchar",
      "description": "Annual consumption band. KWH_LT1000, KWH1000-2499, KWH2500-4999 the headline household band, KWH5000-14999, KWH_GE15000, and TOT_KWH the weighted all-band average that exists only from 2017-S2."
    },
    {
      "name": "unit",
      "type": "varchar",
      "description": "Unit of measure, the constant KWH. Prices are per kilowatt-hour."
    },
    {
      "name": "tax",
      "type": "varchar",
      "description": "Tax level. X_TAX excludes all taxes and levies, X_VAT excludes VAT and recoverable taxes, I_TAX includes everything a household pays."
    },
    {
      "name": "currency",
      "type": "varchar",
      "description": "EUR, NAC for national currency, or PPS purchasing power standard. NAC equals EUR in the euro area."
    },
    {
      "name": "geo",
      "type": "varchar",
      "description": "Reporting country as a Eurostat NUTS-0 code, ISO 3166-1 alpha-2 except EL for Greece and UK for the United Kingdom, plus the aggregates EU27_2020 and EA. The join key to a geometry Collection."
    },
    {
      "name": "TIME_PERIOD",
      "type": "varchar",
      "description": "Reference semester as a string, 2025-S2. Fixed format, so string ordering and MAX work."
    },
    {
      "name": "OBS_VALUE",
      "type": "double",
      "description": "The observed electricity price in the stated currency per kilowatt-hour."
    },
    {
      "name": "OBS_FLAG",
      "type": "varchar",
      "description": "Observation status, e estimated, p provisional, d definition differs, null for 98 percent of rows."
    },
    {
      "name": "CONF_STATUS",
      "type": "varchar",
      "description": "Confidentiality status, entirely null in this snapshot."
    }
  ],
  "table:row_count": 65466,
  "assets": {
    "data": {
      "href": "./eurostat-electricity-prices.parquet",
      "type": "application/vnd.apache.parquet",
      "title": "Eurostat Electricity Prices for Household Consumers (Parquet)",
      "roles": [
        "data"
      ],
      "file:size": 162919,
      "file:checksum": "122051a96f8677c374f6b54cb6e876dcf6af33bc2982b52c9445d0c9a857240b6477",
      "description": "The rows of Eurostat table nrg_pc_204, one price for each country or country group, half year, consumption band, tax level, and currency."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "via",
      "href": "https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/tabular/eurostat-electricity-prices/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "attribution": "Source, Eurostat",
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <file:> .
@prefix ns3: <table:> .
@prefix ns4: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/tabular/eurostat-electricity-prices> a stac:Collection ;
    dct:description "Semi-annual electricity prices for household consumers across European countries by consumption band, tax component, and currency, Eurostat table nrg_pc_204. Non-geospatial companion table, join key is the country code column geo (NUTS-0), converted to cloud-native Parquet." ;
    dct:extent [ ] ;
    dct:license "CC-BY-4.0" ;
    dct:subject "electricity",
        "energy",
        "eurostat",
        "prices",
        "tabular" ;
    dct:title "Eurostat Electricity Prices for Household Consumers" ;
    rdfs:seeAlso [ rdfs:label "Original source" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_204/default/table> ],
        [ rdfs:label "Arabic" ;
            dct:language "ar" ;
            dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <file:///ar/tabular/eurostat-electricity-prices/collection.json> ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///catalog.json> ],
        [ rdfs:label "Human-readable documentation" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ] ;
    stac:hasAsset [ ns4:data <file:///github/workspace/eurostat-electricity-prices.parquet> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/attribution/v0.1.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/language/v1.0.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json" ;
    stac:hasProvider [ ],
        [ ] ;
    stac:version "1.1.0" ;
    ns3:columns [ a <file:///github/workspace/varchar> ;
            dct:description "Unit of measure, the constant KWH. Prices are per kilowatt-hour." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Confidentiality status, entirely null in this snapshot." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "EUR, NAC for national currency, or PPS purchasing power standard. NAC equals EUR in the euro area." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Annual consumption band. KWH_LT1000, KWH1000-2499, KWH2500-4999 the headline household band, KWH5000-14999, KWH_GE15000, and TOT_KWH the weighted all-band average that exists only from 2017-S2." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Observation status, e estimated, p provisional, d definition differs, null for 98 percent of rows." ],
        [ a <file:///github/workspace/timestamp> ;
            dct:description "Frozen at one 2019 timestamp for every row of this snapshot while the data runs to 2025. Unreliable, do not derive freshness from it." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Tax level. X_TAX excludes all taxes and levies, X_VAT excludes VAT and recoverable taxes, I_TAX includes everything a household pays." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Observation frequency, the constant S for semi-annual. S1 is January to June, S2 is July to December." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Eurostat dataflow identifier, the constant ESTAT nrg_pc_204 version 1.0." ],
        [ a <file:///github/workspace/double> ;
            dct:description "The observed electricity price in the stated currency per kilowatt-hour." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Energy product code, the constant E7000 for electricity." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Reference semester as a string, 2025-S2. Fixed format, so string ordering and MAX work." ],
        [ a <file:///github/workspace/varchar> ;
            dct:description "Reporting country as a Eurostat NUTS-0 code, ISO 3166-1 alpha-2 except EL for Greece and UK for the United Kingdom, plus the aggregates EU27_2020 and EA. The join key to a geometry Collection." ] ;
    ns3:row_count 65466 .

<file:///github/workspace/eurostat-electricity-prices.parquet> ns2:checksum "122051a96f8677c374f6b54cb6e876dcf6af33bc2982b52c9445d0c9a857240b6477" ;
    ns2:size 162919 ;
    dct:description "The rows of Eurostat table nrg_pc_204, one price for each country or country group, half year, consumption band, tax level, and currency." ;
    dct:format "application/vnd.apache.parquet" ;
    dct:title "Eurostat Electricity Prices for Household Consumers (Parquet)" ;
    stac:hasAssetroles "data"^^<xsd:string> .


```


### Raster collection (Cloud-Optimized GeoTIFF)
A sample COG collection with a `data` asset, the `source` file it was converted from, and
a thumbnail. Projection metadata uses the Projection extension.

#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "raster/sample-cog",
  "title": "Sample Raster COG",
  "description": "A small 3-band Cloud Optimized GeoTIFF used to exercise the raster path end to end, rasterio's RGB.byte.tif test fixture, derived from USGS Landsat 7 imagery over Andros Island in the Bahamas. Optimized to a COG with per-band statistics, minimum, maximum, mean, and standard deviation, embedded in the header, in UTM zone 18N (EPSG:32618).",
  "license": "CC0-1.0",
  "keywords": [
    "raster",
    "cog",
    "sample",
    "rgb",
    "geotiff"
  ],
  "providers": [
    {
      "name": "rasterio",
      "url": "https://github.com/rasterio/rasterio",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -78.95865,
          23.564991,
          -76.574924,
          25.550874
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1999-04-15T00:00:00Z",
          null
        ]
      ]
    }
  },
  "assets": {
    "data": {
      "href": "./sample-cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Sample Raster COG (COG)",
      "roles": [
        "data"
      ],
      "file:size": 1054493,
      "file:checksum": "1220b2e1aa393fe37dc26e516b13c8f4fb3b1e99efd01a6661c894a5e840201c8c96",
      "bands": [
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 44.396,
            "stddev": 58.4784,
            "valid_percent": 67.4572
          }
        },
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 65.9922,
            "stddev": 58.2068,
            "valid_percent": 67.4572
          }
        },
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 71.3248,
            "stddev": 60.8373,
            "valid_percent": 67.4572
          }
        }
      ],
      "proj:code": "EPSG:32618",
      "description": "The 3-band 8-bit RGB image in UTM zone 18N, with band statistics in its header."
    },
    "source": {
      "href": "https://raw.githubusercontent.com/rasterio/rasterio/main/tests/data/RGB.byte.tif",
      "type": "image/tiff",
      "title": "rasterio RGB.byte.tif test fixture (GeoTIFF)",
      "roles": [
        "source"
      ],
      "file:size": 1745956,
      "file:checksum": "1220d7cbe932c7ed74a627706a9e9df99f706df3e5abc7d45a49e9d00677a6b09eb4",
      "description": "The rasterio RGB.byte.tif test image, the 3-band 8-bit GeoTIFF that the COG is made from."
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview thumbnail over a light basemap. © OpenStreetMap contributors © CARTO.",
      "roles": [
        "thumbnail"
      ],
      "file:size": 243153,
      "file:checksum": "12203f05e92e5b77ab80d92d7e319053dfa48f00ce72d05f8c7251959b88dbd57971",
      "description": "A PNG of the image over a light basemap."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "via",
      "href": "https://github.com/rasterio/rasterio/blob/main/tests/data/RGB.byte.tif",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/raster/sample-cog/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "العربية",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v2.0.0/schema.json",
    "https://stac-extensions.github.io/language/v1.0.0/schema.json"
  ],
  "id": "raster/sample-cog",
  "title": "Sample Raster COG",
  "description": "A small 3-band Cloud Optimized GeoTIFF used to exercise the raster path end to end, rasterio's RGB.byte.tif test fixture, derived from USGS Landsat 7 imagery over Andros Island in the Bahamas. Optimized to a COG with per-band statistics, minimum, maximum, mean, and standard deviation, embedded in the header, in UTM zone 18N (EPSG:32618).",
  "license": "CC0-1.0",
  "keywords": [
    "raster",
    "cog",
    "sample",
    "rgb",
    "geotiff"
  ],
  "providers": [
    {
      "name": "rasterio",
      "url": "https://github.com/rasterio/rasterio",
      "roles": [
        "producer",
        "licensor"
      ]
    },
    {
      "name": "Portolan SDI",
      "url": "https://github.com/portolan-sdi",
      "email": "portolan@googlegroups.com",
      "roles": [
        "host"
      ]
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -78.95865,
          23.564991,
          -76.574924,
          25.550874
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "1999-04-15T00:00:00Z",
          null
        ]
      ]
    }
  },
  "assets": {
    "data": {
      "href": "./sample-cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Sample Raster COG (COG)",
      "roles": [
        "data"
      ],
      "file:size": 1054493,
      "file:checksum": "1220b2e1aa393fe37dc26e516b13c8f4fb3b1e99efd01a6661c894a5e840201c8c96",
      "bands": [
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 44.396,
            "stddev": 58.4784,
            "valid_percent": 67.4572
          }
        },
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 65.9922,
            "stddev": 58.2068,
            "valid_percent": 67.4572
          }
        },
        {
          "data_type": "uint8",
          "statistics": {
            "minimum": 1.0,
            "maximum": 255.0,
            "mean": 71.3248,
            "stddev": 60.8373,
            "valid_percent": 67.4572
          }
        }
      ],
      "proj:code": "EPSG:32618",
      "description": "The 3-band 8-bit RGB image in UTM zone 18N, with band statistics in its header."
    },
    "source": {
      "href": "https://raw.githubusercontent.com/rasterio/rasterio/main/tests/data/RGB.byte.tif",
      "type": "image/tiff",
      "title": "rasterio RGB.byte.tif test fixture (GeoTIFF)",
      "roles": [
        "source"
      ],
      "file:size": 1745956,
      "file:checksum": "1220d7cbe932c7ed74a627706a9e9df99f706df3e5abc7d45a49e9d00677a6b09eb4",
      "description": "The rasterio RGB.byte.tif test image, the 3-band 8-bit GeoTIFF that the COG is made from."
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview thumbnail over a light basemap. \u00a9 OpenStreetMap contributors \u00a9 CARTO.",
      "roles": [
        "thumbnail"
      ],
      "file:size": 243153,
      "file:checksum": "12203f05e92e5b77ab80d92d7e319053dfa48f00ce72d05f8c7251959b88dbd57971",
      "description": "A PNG of the image over a light basemap."
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "via",
      "href": "https://github.com/rasterio/rasterio/blob/main/tests/data/RGB.byte.tif",
      "type": "text/html",
      "title": "Original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents",
      "hreflang": "en"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation",
      "hreflang": "en"
    },
    {
      "rel": "alternate",
      "href": "../../ar/raster/sample-cog/collection.json",
      "type": "application/json",
      "title": "Arabic",
      "hreflang": "ar"
    }
  ],
  "updated": "2026-07-21T00:00:00Z",
  "language": {
    "code": "en",
    "name": "English"
  },
  "languages": [
    {
      "code": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "alternate": "Arabic",
      "dir": "rtl"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <file:> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix ns4: <proj:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/raster/sample-cog> a stac:Collection ;
    dct:description "A small 3-band Cloud Optimized GeoTIFF used to exercise the raster path end to end, rasterio's RGB.byte.tif test fixture, derived from USGS Landsat 7 imagery over Andros Island in the Bahamas. Optimized to a COG with per-band statistics, minimum, maximum, mean, and standard deviation, embedded in the header, in UTM zone 18N (EPSG:32618)." ;
    dct:extent [ ] ;
    dct:license "CC0-1.0" ;
    dct:subject "cog",
        "geotiff",
        "raster",
        "rgb",
        "sample" ;
    dct:title "Sample Raster COG" ;
    rdfs:seeAlso [ dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///catalog.json> ],
        [ rdfs:label "Arabic" ;
            dct:language "ar" ;
            dct:type "application/json" ;
            ns3:relation <http://www.iana.org/assignments/relation/alternate> ;
            oa:hasTarget <file:///ar/raster/sample-cog/collection.json> ],
        [ rdfs:label "Human-readable documentation" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns3:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:language "en" ;
            dct:type "text/markdown" ;
            ns3:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ],
        [ rdfs:label "Original source" ;
            dct:type "text/html" ;
            ns3:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://github.com/rasterio/rasterio/blob/main/tests/data/RGB.byte.tif> ] ;
    stac:hasAsset [ ns1:data <file:///github/workspace/sample-cog.tif> ;
            ns1:source <https://raw.githubusercontent.com/rasterio/rasterio/main/tests/data/RGB.byte.tif> ;
            ns1:thumbnail <file:///github/workspace/thumbnail.png> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/language/v1.0.0/schema.json",
        "https://stac-extensions.github.io/projection/v2.0.0/schema.json" ;
    stac:hasProvider [ ],
        [ ] ;
    stac:version "1.1.0" .

<file:///github/workspace/sample-cog.tif> ns2:checksum "1220b2e1aa393fe37dc26e516b13c8f4fb3b1e99efd01a6661c894a5e840201c8c96" ;
    ns2:size 1054493 ;
    dct:description "The 3-band 8-bit RGB image in UTM zone 18N, with band statistics in its header." ;
    dct:format "image/tiff; application=geotiff; profile=cloud-optimized" ;
    dct:title "Sample Raster COG (COG)" ;
    ns1:bands [ ns1:data_type "uint8" ;
            ns1:statistics [ ns1:maximum 2.55e+02 ;
                    ns1:mean 7.13248e+01 ;
                    ns1:minimum 1e+00 ;
                    ns1:stddev 6.08373e+01 ;
                    ns1:valid_percent 6.74572e+01 ] ],
        [ ns1:data_type "uint8" ;
            ns1:statistics [ ns1:maximum 2.55e+02 ;
                    ns1:mean 4.4396e+01 ;
                    ns1:minimum 1e+00 ;
                    ns1:stddev 5.84784e+01 ;
                    ns1:valid_percent 6.74572e+01 ] ],
        [ ns1:data_type "uint8" ;
            ns1:statistics [ ns1:maximum 2.55e+02 ;
                    ns1:mean 6.59922e+01 ;
                    ns1:minimum 1e+00 ;
                    ns1:stddev 5.82068e+01 ;
                    ns1:valid_percent 6.74572e+01 ] ] ;
    stac:hasAssetroles "data"^^<xsd:string> ;
    ns4:code "EPSG:32618" .

<file:///github/workspace/thumbnail.png> ns2:checksum "12203f05e92e5b77ab80d92d7e319053dfa48f00ce72d05f8c7251959b88dbd57971" ;
    ns2:size 243153 ;
    dct:description "A PNG of the image over a light basemap." ;
    dct:format "image/png" ;
    dct:title "Preview thumbnail over a light basemap. © OpenStreetMap contributors © CARTO." ;
    stac:hasAssetroles "thumbnail"^^<xsd:string> .

<https://raw.githubusercontent.com/rasterio/rasterio/main/tests/data/RGB.byte.tif> ns2:checksum "1220d7cbe932c7ed74a627706a9e9df99f706df3e5abc7d45a49e9d00677a6b09eb4" ;
    ns2:size 1745956 ;
    dct:description "The rasterio RGB.byte.tif test image, the 3-band 8-bit GeoTIFF that the COG is made from." ;
    dct:format "image/tiff" ;
    dct:title "rasterio RGB.byte.tif test fixture (GeoTIFF)" ;
    stac:hasAssetroles "source"^^<xsd:string> .


```


### Classified raster collection
Flood classification over Valencia, October 2024. The raster has one band, so its classes
sit in `classification:classes` on the data asset (Classification extension). Every class
has a `title`, and the class whose value equals the asset `nodata` is marked `nodata: true`.

#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ],
  "id": "valencia-2024",
  "title": "Flood classification, Valencia, Spain, October 2024 (GEP SAR Features, Sentinel-1)",
  "description": "Flood classification over Valencia and l'Albufera after the 29 October 2024 DANA, from the GEP SAR Features service using Sentinel-1 backscatter and coherence. It is a single-COG collection with one discrete uint8 band with an embedded color table, 20 m, EPSG:32630. The raster has one band, so the class list sits on the asset, and each color_hint matches the color table entry for its value.",
  "license": "other",
  "updated": "2026-11-24T00:00:00Z",
  "keywords": [
    "flood",
    "Sentinel-1",
    "SAR",
    "Valencia",
    "DANA"
  ],
  "providers": [
    {
      "name": "Geohazards TEP (GEP)",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://geohazards-tep.eu/"
    },
    {
      "name": "Portolan SDI",
      "roles": [
        "processor",
        "host"
      ],
      "url": "https://github.com/portolan-sdi"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -0.62,
          39.12,
          0.03,
          39.63
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2024-10-07T00:00:00Z",
          "2024-10-31T23:59:59Z"
        ]
      ]
    }
  },
  "assets": {
    "data": {
      "href": "./sar-features-flood-spain-cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Flood classification (COG)",
      "description": "Discrete uint8 COG with an embedded color table and embedded band statistics. Value 0 is nodata and draws transparent.",
      "roles": [
        "data"
      ],
      "data_type": "uint8",
      "nodata": 0,
      "classification:classes": [
        {
          "value": 0,
          "name": "other",
          "title": "Other",
          "nodata": true
        },
        {
          "value": 1,
          "name": "urban",
          "title": "Urban",
          "color_hint": "000000"
        },
        {
          "value": 2,
          "name": "permanent-water",
          "title": "Permanent water",
          "color_hint": "0000FF"
        },
        {
          "value": 3,
          "name": "bare-soil-flood",
          "title": "Flooded bare soil",
          "color_hint": "00FF00"
        },
        {
          "value": 4,
          "name": "urban-flood",
          "title": "Flooded urban area",
          "color_hint": "00FFFF"
        }
      ]
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview drawn from the embedded color table",
      "roles": [
        "thumbnail"
      ]
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "license",
      "href": "./LICENSE.html",
      "type": "text/html",
      "title": "Terms of use"
    },
    {
      "rel": "via",
      "href": "https://geohazards-tep.eu/",
      "type": "text/html",
      "title": "Geohazards Exploitation Platform (GEP), the original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://stac-extensions.github.io/classification/v2.0.0/schema.json"
  ],
  "id": "valencia-2024",
  "title": "Flood classification, Valencia, Spain, October 2024 (GEP SAR Features, Sentinel-1)",
  "description": "Flood classification over Valencia and l'Albufera after the 29 October 2024 DANA, from the GEP SAR Features service using Sentinel-1 backscatter and coherence. It is a single-COG collection with one discrete uint8 band with an embedded color table, 20 m, EPSG:32630. The raster has one band, so the class list sits on the asset, and each color_hint matches the color table entry for its value.",
  "license": "other",
  "updated": "2026-11-24T00:00:00Z",
  "keywords": [
    "flood",
    "Sentinel-1",
    "SAR",
    "Valencia",
    "DANA"
  ],
  "providers": [
    {
      "name": "Geohazards TEP (GEP)",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://geohazards-tep.eu/"
    },
    {
      "name": "Portolan SDI",
      "roles": [
        "processor",
        "host"
      ],
      "url": "https://github.com/portolan-sdi"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -0.62,
          39.12,
          0.03,
          39.63
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2024-10-07T00:00:00Z",
          "2024-10-31T23:59:59Z"
        ]
      ]
    }
  },
  "assets": {
    "data": {
      "href": "./sar-features-flood-spain-cog.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Flood classification (COG)",
      "description": "Discrete uint8 COG with an embedded color table and embedded band statistics. Value 0 is nodata and draws transparent.",
      "roles": [
        "data"
      ],
      "data_type": "uint8",
      "nodata": 0,
      "classification:classes": [
        {
          "value": 0,
          "name": "other",
          "title": "Other",
          "nodata": true
        },
        {
          "value": 1,
          "name": "urban",
          "title": "Urban",
          "color_hint": "000000"
        },
        {
          "value": 2,
          "name": "permanent-water",
          "title": "Permanent water",
          "color_hint": "0000FF"
        },
        {
          "value": 3,
          "name": "bare-soil-flood",
          "title": "Flooded bare soil",
          "color_hint": "00FF00"
        },
        {
          "value": 4,
          "name": "urban-flood",
          "title": "Flooded urban area",
          "color_hint": "00FFFF"
        }
      ]
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview drawn from the embedded color table",
      "roles": [
        "thumbnail"
      ]
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "license",
      "href": "./LICENSE.html",
      "type": "text/html",
      "title": "Terms of use"
    },
    {
      "rel": "via",
      "href": "https://geohazards-tep.eu/",
      "type": "text/html",
      "title": "Geohazards Exploitation Platform (GEP), the original source"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <classification:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/valencia-2024> a stac:Collection ;
    dct:description "Flood classification over Valencia and l'Albufera after the 29 October 2024 DANA, from the GEP SAR Features service using Sentinel-1 backscatter and coherence. It is a single-COG collection with one discrete uint8 band with an embedded color table, 20 m, EPSG:32630. The raster has one band, so the class list sits on the asset, and each color_hint matches the color table entry for its value." ;
    dct:extent [ ] ;
    dct:license "other" ;
    dct:subject "DANA",
        "SAR",
        "Sentinel-1",
        "Valencia",
        "flood" ;
    dct:title "Flood classification, Valencia, Spain, October 2024 (GEP SAR Features, Sentinel-1)" ;
    rdfs:seeAlso [ rdfs:label "Human-readable documentation" ;
            dct:type "text/markdown" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ],
        [ rdfs:label "Geohazards Exploitation Platform (GEP), the original source" ;
            dct:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://geohazards-tep.eu/> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:type "text/markdown" ;
            ns2:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ],
        [ dct:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ dct:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ rdfs:label "Terms of use" ;
            dct:type "text/html" ;
            ns2:relation <http://www.iana.org/assignments/relation/license> ;
            oa:hasTarget <file:///github/workspace/LICENSE.html> ] ;
    stac:hasAsset [ ns1:data <file:///github/workspace/sar-features-flood-spain-cog.tif> ;
            ns1:thumbnail <file:///github/workspace/thumbnail.png> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/classification/v2.0.0/schema.json" ;
    stac:hasProvider [ ],
        [ ] ;
    stac:version "1.1.0" .

<file:///github/workspace/sar-features-flood-spain-cog.tif> ns3:classes [ dct:title "Flooded urban area" ;
            ns1:color_hint "00FFFF" ;
            ns1:name "urban-flood" ;
            ns1:value 4 ],
        [ dct:title "Permanent water" ;
            ns1:color_hint "0000FF" ;
            ns1:name "permanent-water" ;
            ns1:value 2 ],
        [ dct:title "Other" ;
            ns1:name "other" ;
            ns1:nodata true ;
            ns1:value 0 ],
        [ dct:title "Flooded bare soil" ;
            ns1:color_hint "00FF00" ;
            ns1:name "bare-soil-flood" ;
            ns1:value 3 ],
        [ dct:title "Urban" ;
            ns1:color_hint "000000" ;
            ns1:name "urban" ;
            ns1:value 1 ] ;
    dct:description "Discrete uint8 COG with an embedded color table and embedded band statistics. Value 0 is nodata and draws transparent." ;
    dct:format "image/tiff; application=geotiff; profile=cloud-optimized" ;
    dct:title "Flood classification (COG)" ;
    ns1:data_type "uint8" ;
    ns1:nodata 0 ;
    stac:hasAssetroles "data"^^<xsd:string> .

<file:///github/workspace/thumbnail.png> dct:format "image/png" ;
    dct:title "Preview drawn from the embedded color table" ;
    stac:hasAssetroles "thumbnail"^^<xsd:string> .


```


### Partitioned vector collection
Buildings of Andalusia, one GeoParquet file per province. `partition:glob` is an absolute
`s3://` URL that clients can list (Portolan partition extension). The PMTiles asset has the
`visual` role and the glob is the GeoParquet data it renders.

#### json
```json
{
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://schemas.portolan-sdi.org/incubating/partition/v1.0.0/schema.json",
    "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json"
  ],
  "id": "buildings",
  "title": "Buildings of Andalusia",
  "description": "Building footprints for Andalusia, Spain, partitioned by province into one GeoParquet file per province. All partitions can be read at once with the glob pattern `s3://example-bucket/andalusia/buildings/*/*.parquet`.",
  "license": "CC-BY-4.0",
  "updated": "2026-07-15T09:30:00Z",
  "keywords": [
    "buildings",
    "footprints",
    "cadastre",
    "andalusia"
  ],
  "partition:scheme": "directory",
  "partition:strategy": "attribute",
  "partition:keys": [
    {
      "name": "province",
      "type": "string",
      "description": "Province of Andalusia, one GeoParquet file per province"
    }
  ],
  "partition:file_count": 8,
  "partition:glob": "s3://example-bucket/andalusia/buildings/*/*.parquet",
  "providers": [
    {
      "name": "Dirección General del Catastro",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://www.catastro.hacienda.gob.es"
    },
    {
      "name": "Portolan SDI",
      "roles": [
        "processor",
        "host"
      ],
      "url": "https://github.com/portolan-sdi"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.523,
          35.938,
          -1.63,
          38.729
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-06-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "building_id",
      "type": "string",
      "description": "Cadastral reference of the building, unique across all partitions."
    },
    {
      "name": "provincia",
      "type": "string",
      "description": "Province name, the partition key; every file holds one province."
    },
    {
      "name": "height_m",
      "type": "float",
      "description": "Building height in metres, null where the cadastre records none."
    },
    {
      "name": "geometry",
      "type": "binary",
      "description": "Building footprint as WKB, EPSG:4326."
    }
  ],
  "assets": {
    "visual": {
      "href": "./buildings.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Buildings (PMTiles)",
      "roles": [
        "visual"
      ],
      "file:size": 268435456,
      "file:checksum": "1220d5a8e1b4c7f0a3d6e9b2c5f8a1d4e7b0c3f6a9d2e5b8c1f4a7d0e3b6c9f2a5d8"
    },
    "style-default": {
      "href": "./styles/default.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Default MapLibre style",
      "roles": [
        "style",
        "default"
      ],
      "file:size": 2304,
      "file:checksum": "12207b0e3d6c9f2a5b8e1d4c7f0a3b6e9d2c5f8b1e4a7d0c3f6b9e2a5d8c1f4b7e09"
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview rendered with the default style",
      "roles": [
        "thumbnail"
      ],
      "file:size": 138204,
      "file:checksum": "1220a6d9c2f5b8e1a4d7c0f3b6a9e2d5c8f1b4e7a0d3c6f9b2e5a8d1c4f7b0e3a6d9"
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "./buildings-sevilla/item.json",
      "type": "application/geo+json",
      "title": "Buildings — Seville province"
    },
    {
      "rel": "pmtiles",
      "href": "./buildings.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Web map tiles",
      "pmtiles:layers": [
        "buildings"
      ]
    },
    {
      "rel": "via",
      "href": "https://www.catastro.hacienda.gob.es/webinspire/index.html",
      "type": "text/html",
      "title": "Original source (Spanish Cadastre INSPIRE services)"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld",
  "type": "Collection",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
    "https://schemas.portolan-sdi.org/incubating/partition/v1.0.0/schema.json",
    "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json",
    "https://stac-extensions.github.io/file/v2.1.0/schema.json",
    "https://stac-extensions.github.io/table/v1.2.0/schema.json"
  ],
  "id": "buildings",
  "title": "Buildings of Andalusia",
  "description": "Building footprints for Andalusia, Spain, partitioned by province into one GeoParquet file per province. All partitions can be read at once with the glob pattern `s3://example-bucket/andalusia/buildings/*/*.parquet`.",
  "license": "CC-BY-4.0",
  "updated": "2026-07-15T09:30:00Z",
  "keywords": [
    "buildings",
    "footprints",
    "cadastre",
    "andalusia"
  ],
  "partition:scheme": "directory",
  "partition:strategy": "attribute",
  "partition:keys": [
    {
      "name": "province",
      "type": "string",
      "description": "Province of Andalusia, one GeoParquet file per province"
    }
  ],
  "partition:file_count": 8,
  "partition:glob": "s3://example-bucket/andalusia/buildings/*/*.parquet",
  "providers": [
    {
      "name": "Direcci\u00f3n General del Catastro",
      "roles": [
        "producer",
        "licensor"
      ],
      "url": "https://www.catastro.hacienda.gob.es"
    },
    {
      "name": "Portolan SDI",
      "roles": [
        "processor",
        "host"
      ],
      "url": "https://github.com/portolan-sdi"
    }
  ],
  "extent": {
    "spatial": {
      "bbox": [
        [
          -7.523,
          35.938,
          -1.63,
          38.729
        ]
      ]
    },
    "temporal": {
      "interval": [
        [
          "2025-06-01T00:00:00Z",
          null
        ]
      ]
    }
  },
  "table:columns": [
    {
      "name": "building_id",
      "type": "string",
      "description": "Cadastral reference of the building, unique across all partitions."
    },
    {
      "name": "provincia",
      "type": "string",
      "description": "Province name, the partition key; every file holds one province."
    },
    {
      "name": "height_m",
      "type": "float",
      "description": "Building height in metres, null where the cadastre records none."
    },
    {
      "name": "geometry",
      "type": "binary",
      "description": "Building footprint as WKB, EPSG:4326."
    }
  ],
  "assets": {
    "visual": {
      "href": "./buildings.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Buildings (PMTiles)",
      "roles": [
        "visual"
      ],
      "file:size": 268435456,
      "file:checksum": "1220d5a8e1b4c7f0a3d6e9b2c5f8a1d4e7b0c3f6a9d2e5b8c1f4a7d0e3b6c9f2a5d8"
    },
    "style-default": {
      "href": "./styles/default.json",
      "type": "application/vnd.mapbox.style+json",
      "title": "Default MapLibre style",
      "roles": [
        "style",
        "default"
      ],
      "file:size": 2304,
      "file:checksum": "12207b0e3d6c9f2a5b8e1d4c7f0a3b6e9d2c5f8b1e4a7d0c3f6b9e2a5d8c1f4b7e09"
    },
    "thumbnail": {
      "href": "./thumbnail.png",
      "type": "image/png",
      "title": "Preview rendered with the default style",
      "roles": [
        "thumbnail"
      ],
      "file:size": 138204,
      "file:checksum": "1220a6d9c2f5b8e1a4d7c0f3b6a9e2d5c8f1b4e7a0d3c6f9b2e5a8d1c4f7b0e3a6d9"
    }
  },
  "links": [
    {
      "rel": "root",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "parent",
      "href": "../catalog.json",
      "type": "application/json"
    },
    {
      "rel": "item",
      "href": "./buildings-sevilla/item.json",
      "type": "application/geo+json",
      "title": "Buildings \u2014 Seville province"
    },
    {
      "rel": "pmtiles",
      "href": "./buildings.pmtiles",
      "type": "application/vnd.pmtiles",
      "title": "Web map tiles",
      "pmtiles:layers": [
        "buildings"
      ]
    },
    {
      "rel": "via",
      "href": "https://www.catastro.hacienda.gob.es/webinspire/index.html",
      "type": "text/html",
      "title": "Original source (Spanish Cadastre INSPIRE services)"
    },
    {
      "rel": "agents",
      "href": "./AGENTS.md",
      "type": "text/markdown",
      "title": "Guidance for AI agents"
    },
    {
      "rel": "describedby",
      "href": "./README.md",
      "type": "text/markdown",
      "title": "Human-readable documentation"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <partition:> .
@prefix ns3: <pmtiles:> .
@prefix ns4: <https://w3id.org/ogc/stac/assets/> .
@prefix ns5: <file:> .
@prefix ns6: <table:> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/buildings> a stac:Collection ;
    dct:description "Building footprints for Andalusia, Spain, partitioned by province into one GeoParquet file per province. All partitions can be read at once with the glob pattern `s3://example-bucket/andalusia/buildings/*/*.parquet`." ;
    dct:extent [ ] ;
    dct:license "CC-BY-4.0" ;
    dct:subject "andalusia",
        "buildings",
        "cadastre",
        "footprints" ;
    dct:title "Buildings of Andalusia" ;
    rdfs:seeAlso [ rdfs:label "Human-readable documentation" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <file:///github/workspace/README.md> ],
        [ rdfs:label "Original source (Spanish Cadastre INSPIRE services)" ;
            dct:type "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://www.catastro.hacienda.gob.es/webinspire/index.html> ],
        [ rdfs:label "Web map tiles" ;
            dct:type "application/vnd.pmtiles" ;
            ns1:relation <http://www.iana.org/assignments/relation/pmtiles> ;
            oa:hasTarget <file:///github/workspace/buildings.pmtiles> ;
            ns3:layers "buildings" ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/root> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ dct:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/parent> ;
            oa:hasTarget <file:///github/catalog.json> ],
        [ rdfs:label "Guidance for AI agents" ;
            dct:type "text/markdown" ;
            ns1:relation <http://www.iana.org/assignments/relation/agents> ;
            oa:hasTarget <file:///github/workspace/AGENTS.md> ],
        [ rdfs:label "Buildings — Seville province" ;
            dct:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <file:///github/workspace/buildings-sevilla/item.json> ] ;
    stac:hasAsset [ ns4:style-default <file:///github/workspace/styles/default.json> ;
            ns4:thumbnail <file:///github/workspace/thumbnail.png> ;
            ns4:visual <file:///github/workspace/buildings.pmtiles> ] ;
    stac:hasExtension "https://schemas.portolan-sdi.org/incubating/partition/v1.0.0/schema.json",
        "https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json",
        "https://stac-extensions.github.io/file/v2.1.0/schema.json",
        "https://stac-extensions.github.io/table/v1.2.0/schema.json",
        "https://stac-extensions.github.io/web-map-links/v1.3.0/schema.json" ;
    stac:hasProvider [ ],
        [ ] ;
    stac:version "1.1.0" ;
    ns2:file_count 8 ;
    ns2:glob "s3://example-bucket/andalusia/buildings/*/*.parquet" ;
    ns2:keys [ a <file:///github/workspace/string> ;
            dct:description "Province of Andalusia, one GeoParquet file per province" ] ;
    ns2:scheme "directory" ;
    ns2:strategy "attribute" ;
    ns6:columns [ a <file:///github/workspace/binary> ;
            dct:description "Building footprint as WKB, EPSG:4326." ],
        [ a <file:///github/workspace/string> ;
            dct:description "Cadastral reference of the building, unique across all partitions." ],
        [ a <file:///github/workspace/string> ;
            dct:description "Province name, the partition key; every file holds one province." ],
        [ a <file:///github/workspace/float> ;
            dct:description "Building height in metres, null where the cadastre records none." ] .

<file:///github/workspace/styles/default.json> ns5:checksum "12207b0e3d6c9f2a5b8e1d4c7f0a3b6e9d2c5f8b1e4a7d0c3f6b9e2a5d8c1f4b7e09" ;
    ns5:size 2304 ;
    dct:format "application/vnd.mapbox.style+json" ;
    dct:title "Default MapLibre style" ;
    stac:hasAssetroles "default"^^<xsd:string>,
        "style"^^<xsd:string> .

<file:///github/workspace/thumbnail.png> ns5:checksum "1220a6d9c2f5b8e1a4d7c0f3b6a9e2d5c8f1b4e7a0d3c6f9b2e5a8d1c4f7b0e3a6d9" ;
    ns5:size 138204 ;
    dct:format "image/png" ;
    dct:title "Preview rendered with the default style" ;
    stac:hasAssetroles "thumbnail"^^<xsd:string> .

<file:///github/workspace/buildings.pmtiles> ns5:checksum "1220d5a8e1b4c7f0a3d6e9b2c5f8a1d4e7b0c3f6a9d2e5b8c1f4a7d0e3b6c9f2a5d8" ;
    ns5:size 268435456 ;
    dct:format "application/vnd.pmtiles" ;
    dct:title "Buildings (PMTiles)" ;
    stac:hasAssetroles "visual"^^<xsd:string> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Portolan STAC Profile
description: A STAC Catalog or Collection that conforms to the latest Portolan specification,
  now v0.3.0. This block points to the block of that version; when a new Portolan
  version is released, it moves to the new versioned block.
allOf:
- $ref: https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile-v0-3-0/schema.yaml
x-bblocks-metadata:
  itemIdentifier: portolan.stac.profile
  register: https://cayetanobv.github.io/bblocks-portolan/build/register.json
  version: 0.3.0
  dateOfLastChange: '2026-11-24'

```

Links to the schema:

* YAML version: [schema.yaml](https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/schema.json)
* JSON version: [schema.json](https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "stac_extensions": "stac:hasExtension",
    "type": "@type",
    "id": "@id",
    "extent": "dct:extent",
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "start_datetime": {
      "@id": "stac:start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:end_datetime",
      "@type": "xsd:dateTime"
    },
    "license": "dct:license",
    "providers": "stac:hasProvider",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "href": "@id",
        "type": "dct:format",
        "roles": {
          "@id": "stac:hasAssetroles",
          "@type": "xsd:string",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "media_type": "dct:format",
    "Catalog": "stac:Catalog",
    "Collection": "stac:Collection",
    "stac": "https://w3id.org/ogc/stac/core/",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cayetanobv.github.io/bblocks-portolan/build/annotated/stac/profile/context.jsonld)

## Sources

* [Portolan STAC Profile v0.3.0](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/stac/README.md)
* [Portolan Specification v0.3.0, Core](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/specs/portolan/core.md)
* [Portolan Specification v0.3.0, Formats](https://github.com/portolan-sdi/portolan-spec/blob/v0.3.0/specs/portolan/formats.md)
* [Portolan schema v0.3.0](https://schemas.portolan-sdi.org/portolan/v0.3.0/schema.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/cayetanobv/bblocks-portolan](https://github.com/cayetanobv/bblocks-portolan)
* Path: `_sources/stac/profile`

