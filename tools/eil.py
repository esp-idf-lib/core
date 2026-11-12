"""Data model for the `esp-idf-lib/core` repository.

Read-only view over what the Ruby `eil` gem provides:

* `groups.yml` — component groups
* `components/*/.eil.yml` — component metadata (components are git submodules)
* `persons.yml` — contributors
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ORG = "esp-idf-lib"
GITHUB_URL = "https://github.com"
GITHUB_PAGES_URL = "https://esp-idf-lib.github.io"
ESP_COMPONENT_REGISTRY_URL = "https://components.espressif.com"

# Attributes a record in `persons.yml` may have.
PERSON_ATTRIBUTES = ("name", "gh_id", "email", "url", "full_name")


class CoreError(Exception):
    """Raised when the repository cannot be read or validated."""


class Core:
    """The core repository."""

    def __init__(self, root: Path) -> None:
        self.root = Path(root).resolve()
        self._components: list[Component] | None = None
        self._persons: list[Person] | None = None
        self._groups: list[dict] | None = None

    # -- groups ---------------------------------------------------------

    @property
    def groups(self) -> list[dict]:
        if self._groups is None:
            self._groups = yaml.safe_load((self.root / "groups.yml").read_text(encoding="utf-8"))
        return self._groups

    def components_of(self, group: str) -> list[Component]:
        return [c for c in self.components if c.group_of(group)]

    # -- components -----------------------------------------------------

    @property
    def components(self) -> list[Component]:
        if self._components is None:
            self._components = [Component(self, name) for name in self._submodule_names()]
        return self._components

    def component(self, name: str) -> Component:
        for component in self.components:
            if component.name == name:
                return component
        raise CoreError(f"component `{name}` cannot be found")

    def _submodule_names(self) -> list[str]:
        """Component names taken from `git submodule`, sorted.

        `git submodule` prints one line per submodule, for example:

            7ec0409fac45d422db4741f609ded503d020c4b6 components/ads111x (1.1.15)

        An uninitialized submodule starts with `-` instead of the revision; the
        path is in the second field in both cases.
        """
        try:
            result = subprocess.run(
                ["git", "submodule"],
                cwd=self.root,
                capture_output=True,
                text=True,
                check=True,
            )
        except (OSError, subprocess.CalledProcessError) as error:
            raise CoreError(f"cannot list submodules: {error}") from error
        names = set()
        for line in result.stdout.splitlines():
            fields = line.split()
            if len(fields) < 2 or not fields[1].startswith("components/"):
                continue
            names.add(Path(fields[1]).name)
        if not names:
            raise CoreError(f"no components found in {self.root}")
        return sorted(names)

    # -- persons --------------------------------------------------------

    @property
    def persons(self) -> list[Person]:
        if self._persons is None:
            raw = yaml.safe_load((self.root / "persons.yml").read_text(encoding="utf-8"))
            # Same ordering as the Ruby implementation: by full name, falling
            # back to the short name.
            raw.sort(key=lambda p: p.get("full_name") or p["name"])
            self._persons = [Person(self, data) for data in raw]
        return self._persons

    def validate(self) -> list[str]:
        """Problems found in `persons.yml`, empty when the file is fine.

        Port of `spec/persons_yml_spec.rb`.
        """
        errors = []
        path = self.root / "persons.yml"
        if not path.exists():
            return [f"{path.name} does not exist"]
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            return [f"{path.name} must be an array of persons"]
        if not all(isinstance(record, dict) and "name" in record for record in raw):
            errors.append(f"{path.name}: every record must have a name")
        names = [record.get("name") for record in raw if isinstance(record, dict)]
        duplicates = sorted({name for name in names if names.count(name) > 1})
        if duplicates:
            errors.append(f"{path.name}: duplicate names: {', '.join(duplicates)}")
        unknown = sorted({key for record in raw if isinstance(record, dict) for key in record} - set(PERSON_ATTRIBUTES))
        if unknown:
            errors.append(f"{path.name}: unknown attributes: {', '.join(unknown)}")
        return errors


@dataclass
class Component:
    """A component in `components/<name>`, a git submodule."""

    core: Core
    name: str
    _eil: dict | None = field(default=None, repr=False)

    @property
    def path(self) -> Path:
        return self.core.root / "components" / self.name

    @property
    def eil(self) -> dict:
        if self._eil is None:
            self._eil = yaml.safe_load((self.path / ".eil.yml").read_text(encoding="utf-8"))
        return self._eil

    @property
    def description(self) -> str:
        return self.eil["description"]

    @property
    def version(self) -> str:
        return self.eil["version"]

    @property
    def groups(self) -> list[str]:
        return self.eil["groups"]

    def group_of(self, group: str) -> bool:
        return group in self.groups

    @property
    def contributors(self) -> list[str]:
        return [record["name"] for record in self.eil.get("copyrights", [])]

    def contributed_by(self, name: str) -> bool:
        return name in self.contributors

    # -- URLs -----------------------------------------------------------

    @property
    def fqdn(self) -> str:
        return f"{ORG}/{self.name}"

    @property
    def repo_url(self) -> str:
        return f"{GITHUB_URL}/{self.fqdn}"

    @property
    def doc_url(self) -> str:
        return f"{GITHUB_PAGES_URL}/{self.name}"

    @property
    def issues_url(self) -> str:
        return f"{self.repo_url}/issues"

    @property
    def esp_component_url(self) -> str:
        return f"{ESP_COMPONENT_REGISTRY_URL}/components/{self.fqdn}"

    # -- badges ---------------------------------------------------------

    def workflow_url(self, workflow_file: str) -> str:
        return f"{self.repo_url}/actions/workflows/{workflow_file}"

    def badge(self, workflow_file: str) -> str:
        name = workflow_file.split(".")[0]
        return f"[![{name}]({self.workflow_url(workflow_file)}/badge.svg)]({self.workflow_url(workflow_file)})"

    @property
    def badge_esp_component_registry(self) -> str:
        return f"[![Component Registry]({self.esp_component_url}/badge.svg)]({self.esp_component_url})"


@dataclass
class Person:
    """A contributor from `persons.yml`."""

    core: Core
    data: dict

    @property
    def name(self) -> str:
        return self.data["name"]

    @property
    def full_name(self) -> str | None:
        return self.data.get("full_name")

    @property
    def gh_id(self) -> str | None:
        return self.data.get("gh_id")

    @property
    def url(self) -> str | None:
        return self.data.get("url")

    @property
    def credit(self) -> str:
        """Name, linked to GitHub or to a personal URL when known."""
        name = self.full_name or self.name
        url = f"{GITHUB_URL}/{self.gh_id}" if self.gh_id else self.url
        return f"[{name}]({url})" if url else name

    @property
    def contribution(self) -> str:
        """Component names the person contributed to, as inline code."""
        return " ".join(f"`{c.name}`" for c in self.core.components if c.contributed_by(self.name))
