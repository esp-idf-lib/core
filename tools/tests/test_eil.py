from pathlib import Path

import pytest

from conftest import ROOT
from eil import Core, Person


@pytest.fixture(scope="module")
def core() -> Core:
    return Core(ROOT)


def test_components_are_sorted_and_complete(core):
    names = [component.name for component in core.components]
    assert names == sorted(names)
    assert len(names) >= 90
    assert "i2cdev" in names
    assert "esp_idf_lib_helpers" in names


def test_component_metadata(core):
    component = core.component("i2cdev")
    assert component.description
    assert component.version.count(".") == 2
    assert component.repo_url == "https://github.com/esp-idf-lib/i2cdev"
    assert component.doc_url == "https://esp-idf-lib.github.io/i2cdev"
    assert component.esp_component_url == "https://components.espressif.com/components/esp-idf-lib/i2cdev"


def test_component_badges(core):
    component = core.component("i2cdev")
    assert component.badge("build.yml") == (
        "[![build](https://github.com/esp-idf-lib/i2cdev/actions/workflows/build.yml/badge.svg)]"
        "(https://github.com/esp-idf-lib/i2cdev/actions/workflows/build.yml)"
    )
    assert component.badge_esp_component_registry.startswith("[![Component Registry]")


def test_every_component_belongs_to_a_known_group(core):
    known = {group["name"] for group in core.groups}
    for component in core.components:
        assert component.groups, f"{component.name} has no group"
        assert set(component.groups) <= known, f"{component.name} has unknown group"


def test_every_group_has_components(core):
    for group in core.groups:
        assert core.components_of(group["name"]), f"group {group['name']} is empty"


def test_component_contributed_by(core):
    component = core.component("i2cdev")
    assert component.contributors
    assert component.contributed_by("UncleRus")
    assert not component.contributed_by("nobody-at-all")


def test_person_credit_with_gh_id(core):
    person = Person(core, {"name": "trombik", "full_name": "Tomoyuki Sakurai", "gh_id": "trombik"})
    assert person.credit == "[Tomoyuki Sakurai](https://github.com/trombik)"


def test_person_credit_with_url(core):
    person = Person(core, {"name": "somebody", "url": "https://example.com"})
    assert person.credit == "[somebody](https://example.com)"


def test_person_credit_without_link(core):
    person = Person(core, {"name": "zeroday"})
    assert person.credit == "zeroday"


def test_person_contribution_is_component_list(core):
    person = Person(core, {"name": "UncleRus"})
    contribution = person.contribution.split()
    assert "`i2cdev`" in contribution
    assert all(item.startswith("`") and item.endswith("`") for item in contribution)


def test_persons_sorted_by_full_name(core):
    keys = [(person.full_name or person.name) for person in core.persons]
    assert keys == sorted(keys)


def test_persons_yml_is_valid(core):
    assert core.validate() == []


def test_validate_detects_duplicates(tmp_path: Path):
    (tmp_path / "persons.yml").write_text(
        "- name: a\n- name: a\n", encoding="utf-8"
    )
    errors = Core(tmp_path).validate()
    assert any("duplicate" in error for error in errors)


def test_validate_detects_unknown_attribute(tmp_path: Path):
    (tmp_path / "persons.yml").write_text(
        "- name: a\n  nickname: b\n", encoding="utf-8"
    )
    errors = Core(tmp_path).validate()
    assert any("unknown attributes" in error for error in errors)


def test_validate_detects_missing_name(tmp_path: Path):
    (tmp_path / "persons.yml").write_text(
        "- full_name: A\n", encoding="utf-8"
    )
    errors = Core(tmp_path).validate()
    assert any("must have a name" in error for error in errors)


def test_validate_detects_non_list(tmp_path: Path):
    (tmp_path / "persons.yml").write_text("name: a\n", encoding="utf-8")
    errors = Core(tmp_path).validate()
    assert any("array" in error for error in errors)


def test_validate_detects_missing_file(tmp_path: Path):
    errors = Core(tmp_path).validate()
    assert any("does not exist" in error for error in errors)
