# Managing `esp-idf-lib/core`

<!-- vim-markdown-toc GFM -->

* [Requirements](#requirements)
* [Repository layout](#repository-layout)
* [`tools/cli.py`](#toolsclipy)
    * [Generating `README.md` and `STATUS.md`](#generating-readmemd-and-statusmd)
    * [Running commands in each component](#running-commands-in-each-component)
    * [Releasing a component](#releasing-a-component)
    * [Cleaning files](#cleaning-files)
* [Validation](#validation)
* [`gh` 101](#gh-101)
    * [Authentication](#authentication)
    * [Basics](#basics)
    * [Listing workflows](#listing-workflows)
    * [Running workflows](#running-workflows)

<!-- vim-markdown-toc -->

## Requirements

* python 3.11 or later
* git
* [gh](https://cli.github.com/)

Install the python packages once:

```console
python3 -m venv .venv
. .venv/bin/activate
pip install -r tools/requirements.txt
```

> [!NOTE]
> Every command below is run from the top-level directory of the repository.
> Activate the virtual environment first, or call `.venv/bin/python` explicitly.

## Repository layout

This repository is the core repository of all components. The repository has
all the components as sub-modules.

Clone the repository and update the sub-modules.

```console
git clone git@github.com:esp-idf-lib/core.git
cd core
git submodule update --init
```

The files that matter for the tooling:

| Path | Purpose |
|------|---------|
| `components/` | component sub-modules |
| `groups.yml` | component groups used by the generated documents |
| `persons.yml` | contributors and their components |
| `tools/cli.py` | command line interface |
| `tools/eil.py` | data model: components, groups, persons |
| `tools/templates/` | Jinja2 templates of the generated documents |
| `docs/` | the Sphinx site published to GitHub Pages |

## `tools/cli.py`

All operations are sub-commands of `tools/cli.py`. Show the implemented
commands with:

```console
python tools/cli.py --help
```

```text
docs readme          # Generate README.md
docs status          # Generate STATUS.md
docs check           # Fail when a generated document is out of date
docs html            # Generate HTML version of README.md for review
validate             # Validate persons.yml
list                 # List all the component names
clean                # Remove build files of examples
components update    # Update one component, or all of them with --all
components each      # Run a shell script in each component directory
release              # Release a component
release-all          # Release all components
```

Every command accepts `--root`, the path to the repository; by default it is
the current directory.

### Generating `README.md` and `STATUS.md`

`README.md` and `STATUS.md` are generated from `tools/templates/README.md.j2`
and `tools/templates/STATUS.md.j2`.

> [!CAUTION]
> Do NOT edit `README.md` or `STATUS.md`. Edit the templates instead.

> [!NOTE]
> A workflow verifies that the generated documents are up-to-date. If they are
> not, the test fails.

Generate a document to standard output:

```console
python tools/cli.py docs readme
```

A typical workflow to update `README.md`:

1. Edit `tools/templates/README.md.j2`
1. Generate `README.md` in place
1. Commit `README.md` and the template

```console
# edit the template, NOT README.md
vim tools/templates/README.md.j2

# update README.md
python tools/cli.py docs readme --write

# commit them
git add README.md tools/templates/README.md.j2
git commit -m "update README"
```

The same applies to `STATUS.md` and `tools/templates/STATUS.md.j2`:

```console
python tools/cli.py docs status --write
```

Use the `html` sub-command to review the result in a browser:

```console
python tools/cli.py docs html > README.html
firefox README.html
rm README.html
```

> [!CAUTION]
> Do NOT commit `README.html`.

`docs check` regenerates both documents in memory and compares them with the
committed files. It prints a unified diff and exits with a non-zero status when
a document is stale, so it is suitable for CI:

```console
python tools/cli.py docs check
```

### Running commands in each component

Use `components each`, which runs a shell script in each component directory.
The following command runs `status.sh` in each component.

```sh
# status.sh
git status
```

```console
python tools/cli.py components each status.sh
```

> [!NOTE]
> The file is executed in a component directory. The working directory is
> `components/${COMPONENT_NAME}`.

> [!TIP]
> `NAME` environment variable is set to the component name so that you can use
> it in the script.

Use `components update` to switch a component to `main` and pull it. Pass
`--all` to update every component.

```console
python tools/cli.py components update i2cdev
python tools/cli.py components update --all
```

### Releasing a component

Run `release` to release a component. It:

* increments the version in `.eil.yml` and `idf_component.yml`
* commits the changes to the `main` branch
* pushes to `origin`
* creates a release with `gh release create`

The command takes the component name and the part of the version to increment:
`major`, `minor`, or `patch`. The following example increments the `patch`
version of the `esp_idf_lib_helpers` component.

```console
python tools/cli.py release esp_idf_lib_helpers patch
```

Use `--dry-run` to see the new version without touching the repository:

```console
python tools/cli.py release esp_idf_lib_helpers patch --dry-run
```

When the release is created, GitHub Actions workflows of the component:

* publish the documentation
* publish the component on the ESP Component Registry

Now, the release is published.

Use `release-all` to release every component. It accepts the same `part` and
`--dry-run`.

```console
python tools/cli.py release-all patch
```

> [!CAUTION]
> `release-all` releases all the components, which is rarely what you want.
> Check the list of components with `python tools/cli.py list` first.

### Cleaning files

Run `clean` to remove build files of examples.

```console
python tools/cli.py clean
```

Use `--dry-run` to see what would be removed.

## Validation

```console
python tools/cli.py validate      # persons.yml
python tools/cli.py docs check    # README.md and STATUS.md
python -m pytest tools/tests -q   # tests of the tooling
```

All three are run by the `Validate` workflow on every push and pull request.

## `gh` 101

This section explains basic `gh` commands. See
[the manual](https://cli.github.com/manual/gh) for reference.

### Authentication

Permission at the organization level is needed to manage the repository.
Ask @trombik to obtain one.

All the `gh` command requires authentication. Authenticate yourself with the
following command.

```console
echo 'your_token' | gh auth login --with-token
```

> [!NOTE]
> Replace `your_token` with the token.

### Basics

`gh` automates many operations with GitHub. It can create issues, releases,
run workflows, among others.

> [!NOTE]
> Change the directory to the repository directory and run `gh` command.
> When the working directory is not in the repository, use `--repo esp-idf-lib/${REPO_NAME}`.

```console
cd components/esp_idf_lib_helpers

# opens the repository page in a browser
gh browse
```

### Listing workflows

```console
gh workflow ls
```

### Running workflows

```console
gh workflow run "Publish the component to ESP Component Registry"
```

> [!NOTE]
> The workflow must have `workflow_dispatch` enabled.

See also:

* [Manually running a workflow](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)
* [workflow_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch)
