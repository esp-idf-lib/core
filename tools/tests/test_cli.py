from pathlib import Path

import pytest

from cli import DOCUMENTS, bump_version, main, render_document, write_version
from conftest import ROOT
from eil import Core


@pytest.fixture(scope="module")
def core() -> Core:
    return Core(ROOT)


@pytest.mark.parametrize("name", sorted(DOCUMENTS))
def test_generated_document_is_committed(core, name):
    _, filename = DOCUMENTS[name]
    assert render_document(name, core) == (core.root / filename).read_text(encoding="utf-8")


def test_docs_check_passes():
    assert main(["--root", str(ROOT), "docs", "check"]) == 0


def test_validate_passes():
    assert main(["--root", str(ROOT), "validate"]) == 0


def test_list_prints_every_component(capsys):
    assert main(["--root", str(ROOT), "list"]) == 0
    names = capsys.readouterr().out.split()
    assert len(names) == len(Core(ROOT).components)


@pytest.mark.parametrize(
    ("version", "part", "expected"),
    [
        ("1.2.3", "major", "2.0.0"),
        ("1.2.3", "minor", "1.3.0"),
        ("1.2.3", "patch", "1.2.4"),
        ("0.0.1", "patch", "0.0.2"),
        ("1.9.9", "minor", "1.10.0"),
    ],
)
def test_bump_version(version, part, expected):
    assert bump_version(version, part) == expected


def test_bump_version_rejects_unknown_part():
    with pytest.raises(ValueError):
        bump_version("1.2.3", "huge")


def test_write_version_updates_only_version(tmp_path: Path):
    path = tmp_path / ".eil.yml"
    path.write_text("---\nname: foo\nversion: 1.2.3\ndepends:\n  - log\n", encoding="utf-8")
    write_version(path, "1.2.4")
    assert path.read_text(encoding="utf-8") == "---\nname: foo\nversion: 1.2.4\ndepends:\n  - log\n"


def test_write_version_requires_version_key(tmp_path: Path):
    path = tmp_path / ".eil.yml"
    path.write_text("---\nname: foo\n", encoding="utf-8")
    with pytest.raises(Exception):
        write_version(path, "1.2.4")


def test_release_dry_run_does_not_touch_repository(capsys):
    before = (ROOT / "components" / "i2cdev" / ".eil.yml").read_text(encoding="utf-8")
    assert main(["--root", str(ROOT), "release", "i2cdev", "patch", "--dry-run"]) == 0
    after = (ROOT / "components" / "i2cdev" / ".eil.yml").read_text(encoding="utf-8")
    assert before == after
    assert "i2cdev:" in capsys.readouterr().out


def test_unknown_component_returns_error(capsys):
    assert main(["--root", str(ROOT), "release", "no-such-component", "patch", "--dry-run"]) == 1
    assert "cannot be found" in capsys.readouterr().err
