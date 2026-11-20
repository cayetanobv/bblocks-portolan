"""Cached, thread-safe fetching of JSON and YAML documents from URLs or local paths."""

from __future__ import annotations

import json
import threading
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import url2pathname

import yaml

USER_AGENT = "portolan-bblocks/0.1 (+https://github.com/cayetanobv/bblocks-portolan)"


def to_url(target: str) -> str:
    """Turn a local path into a file:// URL; leave URLs unchanged."""
    if urlparse(target).scheme in ("http", "https", "file"):
        return target
    return Path(target).expanduser().resolve().as_uri()


class Fetcher:
    """Fetch documents once and keep them in memory.

    `mappings` rewrites URL prefixes before fetching, for example to serve a local
    register build whose URLs point at http://localhost:9090/register/.
    """

    def __init__(self, mappings: list[tuple[str, str]] | None = None, timeout: float = 60):
        self.mappings = list(mappings or [])
        self.timeout = timeout
        self._cache: dict[str, Any] = {}
        self._lock = threading.Lock()

    def resolve(self, url: str) -> str:
        for prefix, replacement in self.mappings:
            if url.startswith(prefix):
                mapped = replacement + url[len(prefix):]
                if urlparse(replacement).scheme == "file":
                    base = Path(url2pathname(urlparse(replacement).path)).resolve()
                    target = Path(url2pathname(urlparse(mapped).path)).resolve()
                    if not target.is_relative_to(base):
                        raise ValueError(f"{url} maps outside {base}")
                    return target.as_uri()
                return mapped
        return url

    def __call__(self, url: str) -> Any:
        with self._lock:
            if url in self._cache:
                return self._cache[url]
        data = self._load(self.resolve(url))
        with self._lock:
            self._cache[url] = data
        return data

    def _load(self, url: str) -> Any:
        if urlparse(url).scheme not in ("http", "https", "file"):
            raise ValueError(f"unsupported URL scheme: {url}")
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            text = response.read().decode("utf-8")
        stripped = text.lstrip()
        if stripped.startswith(("{", "[")):
            return json.loads(text)
        return yaml.safe_load(text)
