"""Walk a static STAC catalog from its root through child links."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Any, Iterator
from urllib.parse import urljoin, urlparse

from .fetch import Fetcher


@dataclass
class Node:
    """One fetched catalog or collection, or the error that stopped us fetching it."""

    url: str
    doc: Any = None
    error: str | None = None
    item_links: int = 0
    children: list[str] = field(default_factory=list)


def _allowed(url: str, root_scheme: str) -> bool:
    """Links may go to http(s) from anywhere, and to local files only from a local root.

    A remote catalog must not make the client read files on the machine running it.
    """
    scheme = urlparse(url).scheme
    if scheme in ("http", "https"):
        return True
    return scheme == "file" and root_scheme == "file"


def _links(doc: Any, rel: str, base: str, root_scheme: str = "https") -> list[str]:
    if not isinstance(doc, dict):
        return []
    urls = [
        urljoin(base, link["href"])
        for link in doc.get("links") or []
        if isinstance(link, dict) and link.get("rel") == rel and isinstance(link.get("href"), str)
    ]
    return [u for u in urls if _allowed(u, root_scheme)]


def crawl(root: str, fetch: Fetcher, max_objects: int = 1000, workers: int = 8) -> Iterator[Node]:
    """Yield catalogs and collections breadth first, fetching up to `workers` at a time.

    Items are not fetched: the profile block covers catalogs and collections. Their links
    are counted so a report can say how many were left out.
    """
    seen: set[str] = set()
    queue = [root]
    emitted = 0
    root_scheme = urlparse(root).scheme

    def load(url: str) -> Node:
        try:
            doc = fetch(url)
        except Exception as exc:  # report the failure and keep walking
            return Node(url=url, error=f"could not fetch: {exc}")
        children = [c for c in _links(doc, "child", url, root_scheme) if _fetchable(c)]
        return Node(url=url, doc=doc, item_links=len(_links(doc, "item", url, root_scheme)),
                    children=children)

    def _fetchable(link: str) -> bool:
        """Apply the scheme rule to the URL actually fetched, after any --local mapping."""
        try:
            return _allowed(fetch.resolve(link), root_scheme)
        except ValueError:
            return False

    with ThreadPoolExecutor(max_workers=workers) as pool:
        while queue and emitted < max_objects:
            batch: list[str] = []
            while queue and len(batch) < min(workers * 4, max_objects - emitted):
                url = queue.pop(0)
                if url not in seen:
                    seen.add(url)
                    batch.append(url)
            for node in pool.map(load, batch):
                emitted += 1
                queue.extend(child for child in node.children if child not in seen)
                yield node
