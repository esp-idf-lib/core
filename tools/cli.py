#!/usr/bin/env python3
"""Command line interface for the `esp-idf-lib/core` repository.

Replaces the Ruby tooling (`Rakefile` and `rakelib/`). Run it from the
top-level directory of the repository:

    python tools/cli.py docs readme          # print README.md
    python tools/cli.py docs readme --write  # update README.md in place
    python tools/cli.py docs status          # print STATUS.md
    python tools/cli.py docs check           # fail when a document is stale
    python tools/cli.py docs html            # print README.md as HTML
    python tools/cli.py validate             # check persons.yml
    python tools/cli.py list                 # list component names
    python tools/cli.py clean                # remove build files of examples
    python tools/cli.py components update i2cdev
    python tools/cli.py components update --all
    python tools/cli.py components each script.sh
    python tools/cli.py release i2cdev patch
    python tools/cli.py release-all patch
"""

from __future__ import annotations

import argparse
import difflib
import os
import shutil
import subprocess
import sys
from pathlib import Path

import jinja2

from eil import Core, CoreError, Component

TEMPLATES = Path(__file__).resolve().parent / "templates"

# Documents generated from templates: command name -> (template, output file).
DOCUMENTS = {
    "readme": ("README.md.j2", "README.md"),
    "status": ("STATUS.md.j2", "STATUS.md"),
}

# Directories removed by `clean`, relative to a component directory.
CLEAN_PATTERNS = (
    "examples/*/build",
    "examples/*/sdkconfig",
    "examples/*/sdkconfig.old",
)


def environment() -> jinja2.Environment:
    """Jinja2 environment that trims block tags like ERB's `trim_mode: "<>"`.

    With `trim_blocks`, a line that holds only `{% ... %}` disappears
    completely, which is what `<% ... %>` does in the Ruby implementation.
    """
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TEMPLATES)),
        trim_blocks=True,
        lstrip_blocks=False,
        keep_trailing_newline=True,
        undefined=jinja2.StrictUndefined,
    )


def render_document(name: str, core: Core) -> str:
    template, _ = DOCUMENTS[name]
    return environment().get_template(template).render(
        core=core,
        groups=core.groups,
        persons=core.persons,
    )


def run(command: list[str], cwd: Path) -> None:
    print(f"+ {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def bump_version(version: str, part: str) -> str:
    """Increment `version` (for example `1.2.3`) by `part`.

    `major` gives `2.0.0`, `minor` gives `1.3.0`, `patch` gives `1.2.4`.
    """
    major, minor, patch = (int(field) for field in version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"unknown version part: {part}")


def write_version(path: Path, version: str) -> None:
    """Rewrite the top-level `version:` key of a YAML file."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("version:"):
            lines[index] = f"version: {version}\n"
            break
    else:
        raise CoreError(f"no `version:` in {path}")
    path.write_text("".join(lines), encoding="utf-8")


# -- commands -----------------------------------------------------------


def command_docs(args: argparse.Namespace, core: Core) -> int:
    if args.docs_command == "check":
        stale = []
        for name, (_, filename) in DOCUMENTS.items():
            expected = render_document(name, core)
            committed = (core.root / filename).read_text(encoding="utf-8")
            if expected == committed:
                continue
            stale.append(filename)
            sys.stdout.writelines(
                difflib.unified_diff(
                    committed.splitlines(keepends=True),
                    expected.splitlines(keepends=True),
                    fromfile=f"{filename} (committed)",
                    tofile=f"{filename} (generated)",
                )
            )
        if stale:
            print(f"outdated: {', '.join(stale)}; run `python tools/cli.py docs readme --write`", file=sys.stderr)
            return 1
        return 0

    if args.docs_command == "html":
        try:
            import markdown
        except ImportError:
            print("`docs html` requires the `markdown` package", file=sys.stderr)
            return 2
        text = (core.root / "README.md").read_text(encoding="utf-8")
        print(markdown.markdown(text, extensions=["tables", "fenced_code"]))
        return 0

    text = render_document(args.docs_command, core)
    if args.write:
        (core.root / DOCUMENTS[args.docs_command][1]).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


def command_validate(args: argparse.Namespace, core: Core) -> int:
    errors = core.validate()
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


def command_list(args: argparse.Namespace, core: Core) -> int:
    for component in core.components:
        print(component.name)
    return 0


def command_clean(args: argparse.Namespace, core: Core) -> int:
    removed = 0
    for component in core.components:
        for pattern in CLEAN_PATTERNS:
            for path in component.path.glob(pattern):
                print(f"removing {path.relative_to(core.root)}")
                if args.dry_run:
                    continue
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
                removed += 1
    print(f"removed {removed} path(s)")
    return 0


def command_components(args: argparse.Namespace, core: Core) -> int:
    if args.components_command == "each":
        script = Path(args.file).resolve()
        if not script.is_file():
            print(f"no such file: {script}", file=sys.stderr)
            return 2
        for component in core.components:
            print(f"in {component.path.relative_to(core.root)}", flush=True)
            env = dict(os.environ, NAME=component.name)
            subprocess.run(["sh", str(script)], cwd=component.path, env=env, check=False)
        return 0

    names = [c.name for c in core.components] if args.all else [args.name]
    for name in names:
        component = core.component(name)
        print(f"in {component.path.relative_to(core.root)}", flush=True)
        run(["git", "checkout", "main"], cwd=component.path)
        run(["git", "pull"], cwd=component.path)
        common = component.path / "common"
        if common.is_dir():
            print(f"in {common.relative_to(core.root)}", flush=True)
            run(["git", "checkout", "main"], cwd=common)
            run(["git", "pull"], cwd=common)
    return 0


def release_component(component: Component, part: str, dry_run: bool) -> None:
    current = component.version
    new_version = bump_version(current, part)
    title = f"Release {new_version}"
    print(f"{component.name}: {current} -> {new_version}")
    if dry_run:
        return

    path = component.path
    try:
        run(["git", "checkout", "main"], cwd=path)
        write_version(path / ".eil.yml", new_version)
        write_version(path / "idf_component.yml", new_version)
        run(["git", "diff"], cwd=path)
        run(["git", "add", "."], cwd=path)
        run(["git", "commit", "-m", title], cwd=path)
        run(["git", "push"], cwd=path)
        run(["gh", "release", "create", new_version, "--notes", title, "--title", title], cwd=path)
        run(["git", "pull"], cwd=path)
    except (subprocess.CalledProcessError, CoreError):
        print(f"release of {component.name} failed, reverting", file=sys.stderr)
        subprocess.run(["git", "reset", "."], cwd=path, check=False)
        subprocess.run(["git", "checkout", "."], cwd=path, check=False)
        subprocess.run(["git", "checkout", "main"], cwd=path, check=False)
        raise


def command_release(args: argparse.Namespace, core: Core) -> int:
    if args.command == "release-all":
        for component in core.components:
            print(component.name)
            release_component(component, args.part, args.dry_run)
        return 0
    release_component(core.component(args.name), args.part, args.dry_run)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage the esp-idf-lib/core repository")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="path to the core repository (default: cwd)")
    commands = parser.add_subparsers(dest="command", required=True)

    docs = commands.add_parser("docs", help="generate documents")
    docs_commands = docs.add_subparsers(dest="docs_command", required=True)
    for name in DOCUMENTS:
        document = docs_commands.add_parser(name)
        document.add_argument("--write", action="store_true", help="write the file instead of printing it")
    docs_commands.add_parser("check")
    docs_commands.add_parser("html")

    commands.add_parser("validate", help="check persons.yml")
    commands.add_parser("list", help="list component names")

    clean = commands.add_parser("clean", help="remove build files of examples")
    clean.add_argument("--dry-run", action="store_true")

    components = commands.add_parser("components", help="operate on component submodules")
    components_commands = components.add_subparsers(dest="components_command", required=True)
    update = components_commands.add_parser("update")
    update.add_argument("name", nargs="?")
    update.add_argument("--all", action="store_true")
    each = components_commands.add_parser("each")
    each.add_argument("file")

    release = commands.add_parser("release", help="release a component")
    release.add_argument("name")
    release.add_argument("part", choices=("major", "minor", "patch"))
    release.add_argument("--dry-run", action="store_true")

    release_all = commands.add_parser("release-all", help="release every component")
    release_all.add_argument("part", choices=("major", "minor", "patch"))
    release_all.add_argument("--dry-run", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        core = Core(args.root)
        if args.command == "docs":
            return command_docs(args, core)
        if args.command == "validate":
            return command_validate(args, core)
        if args.command == "list":
            return command_list(args, core)
        if args.command == "clean":
            return command_clean(args, core)
        if args.command == "components":
            return command_components(args, core)
        if args.command == "release":
            return command_release(args, core)
        if args.command == "release-all":
            return command_release(args, core)
    except CoreError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
