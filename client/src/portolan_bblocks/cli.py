"""Command line: portolan-bblocks check | validate | blocks."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import yaml
from ogc.bblocks.register import load_register

from . import DEFAULT_BLOCK, DEFAULT_REGISTER, __version__
from .check import check_catalog, check_files
from .fetch import Fetcher
from .report import render
from .validator import BlockNotFound, BlockValidator, load_block

LOCAL_BASE = "http://localhost:9090/register/"


def _repo_root(start: Path) -> Path | None:
    for path in (start, *start.parents):
        if (path / "bblocks-config.yaml").exists():
            return path
    return None


def _setup(args) -> tuple[str, Fetcher]:
    """Pick the register and URL mappings from --register / --local."""
    mappings = []
    register = args.register
    if args.local:
        root = Path(args.repo).resolve() if args.repo else _repo_root(Path.cwd())
        if root is None or not (root / "build-local" / "register.json").exists():
            sys.exit("--local needs a register checkout with build-local/register.json; run ./build.sh first")
        register = (root / "build-local" / "register.json").as_uri()
        mappings.append((LOCAL_BASE, root.as_uri() + "/"))
    return register, Fetcher(mappings)


def _validator(args, register: str, fetch: Fetcher) -> BlockValidator:
    try:
        return BlockValidator(load_block(register, args.block, fetch), fetch)
    except BlockNotFound as exc:
        sys.exit(str(exc))


def _emit(reports, args) -> int:
    for report in reports:
        print(render(report, show_all=args.all))
        print()
    if args.json:
        payload = [r.as_dict() for r in reports]
        Path(args.json).write_text(json.dumps(payload[0] if len(payload) == 1 else payload, indent=1))
        print(f"wrote {args.json}")
    return 0 if all(r.ok for r in reports) else 1


def cmd_check(args) -> int:
    register, fetch = _setup(args)
    targets = list(args.targets)
    limits = {}
    if args.config:
        config = yaml.safe_load(Path(args.config).read_text()) or {}
        if not args.register_given and config.get("register"):
            register = config["register"]
        args.block = config.get("block", args.block) if args.block == DEFAULT_BLOCK else args.block
        for entry in config.get("catalogs") or []:
            targets.append(entry["url"])
            if entry.get("max"):
                limits[entry["url"]] = entry["max"]
    if not targets:
        sys.exit("give at least one catalog URL or path, or --config")
    validator = _validator(args, register, fetch)
    reports = [check_catalog(t, validator, fetch, register, mode=args.against,
                             max_objects=limits.get(t, args.max)) for t in targets]
    return _emit(reports, args)


def cmd_validate(args) -> int:
    register, fetch = _setup(args)
    validator = _validator(args, register, fetch)
    return _emit([check_files(args.files, validator, fetch, register, mode=args.against)], args)


def cmd_blocks(args) -> int:
    register_url, fetch = _setup(args)
    register = load_register(register_url, load_dependencies=args.imports, yaml_loader=fetch)
    registers = [register, *(register.imported_registers if args.imports else [])]
    for reg in registers:
        print(f"{reg.name}  ({reg.url})")
        for block in sorted(reg.bblocks.values(), key=lambda b: b.item_identifier):
            if args.filter and args.filter not in block.item_identifier:
                continue
            status = getattr(block.status, "value", block.status)
            print(f"  {block.item_identifier:55} {block.version or '':10} {status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--register", default=os.environ.get("PORTOLAN_BBLOCKS_REGISTER", DEFAULT_REGISTER),
                        help="register.json URL or path (default: the published Portolan register)")
    common.add_argument("--local", action="store_true",
                        help="use the local build (build-local/register.json) of the register checkout")
    common.add_argument("--repo", metavar="PATH",
                        help="register checkout for --local (default: found from the current directory)")

    checks = argparse.ArgumentParser(add_help=False)
    checks.add_argument("--block", default=DEFAULT_BLOCK, help=f"block identifier (default: {DEFAULT_BLOCK})")
    checks.add_argument("--against", choices=["both", "declared", "published"], default="both",
                        help="declared: the Portolan version each object declares; published: the block as "
                             "published; both (default): report both, pass/fail on declared")
    checks.add_argument("--json", metavar="FILE", help="write the full report as JSON")
    checks.add_argument("--all", action="store_true", help="list every problem and failing object")

    parser = argparse.ArgumentParser(prog="portolan-bblocks", description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("check", parents=[common, checks], help="walk catalogs and check every catalog and collection")
    p.add_argument("targets", nargs="*", help="root catalog URLs or paths")
    p.add_argument("--config", help="YAML file listing catalogs to check")
    p.add_argument("--max", type=int, default=1000, help="stop after this many objects per catalog (default 1000)")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("validate", parents=[common, checks], help="check single STAC documents, without walking")
    p.add_argument("files", nargs="+", help="STAC JSON files or URLs")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("blocks", parents=[common], help="list the blocks in the register")
    p.add_argument("--imports", action="store_true", help="also list blocks from imported registers")
    p.add_argument("--filter", help="only identifiers containing this text")
    p.set_defaults(func=cmd_blocks)
    return parser


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    args = build_parser().parse_args(argv)
    args.register_given = any(a == "--register" or a.startswith("--register=") for a in argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
