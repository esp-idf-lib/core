# Managing `esp-idf-lib/core`

<!-- vim-markdown-toc GFM -->

* [Requirements](#requirements)
* [`Rakefile`](#rakefile)
    * [Generating README.md](#generating-readmemd)
    * [Running commands in each component](#running-commands-in-each-component)
    * [Releasing a component](#releasing-a-component)
    * [Cleaning files](#cleaning-files)
* [`gh` 101](#gh-101)
    * [Authentication](#authentication)
    * [Basics](#basics)
    * [Listing workflows](#listing-workflows)
    * [Running workflows](#running-workflows)

<!-- vim-markdown-toc -->

## Requirements

* ruby
* [bundler](https://bundler.io/)
* git
* [gh](https://cli.github.com/)

This repository is the core repository of all components. The repository has
all the components as sub-modules.

Clone the repository.

```console
git clone git@github.com:esp-idf-lib/core.git
```

Update the sub-modules.

```console
git submodule update --init --recursive
```

Run `bundler`.

```console
bundle install
```

The operational workflows extensively use `rake` and `gh`.

* Run `rake` command in the top-level directory of `esp-idf-lib` repository.
* Run `gh` in the repository you are working on.

Read [`gh` 101](#gh-101) section first if you are not familiar with `gh` CLI.

> [!TIP]
> Create an alias command to type less when executing `bundle exec`, such as
> `alias be='bundle exec'`.

## `Rakefile`

`Rakefile` is a ruby version of `Makefile`. The `Rakefile` and files under
`rakelib` implements operations to manage the repository.

### Generating README.md

Run `docs:readme` target to generate `README.md` from `README.md.erb`.
`README.md.erb` is the template to generate `README.md`.

> [!CAUTION]
> Do NOT edit `README.md`. Edit `README.md.erb` instead.

> [!NOTE]
> A workflow verifies `README.md` is up-to-date. If not, the test fails.

```console
bundle exec rake docs:readme
```

The above command outputs the generated markdown to standard out.

A typical workflow to update `README.md`:

1. Edit `README.md.erb`
1. Generate `README.md` with `docs:readme` target
1. Commit `README.md` and `README.md.erb`

```console
# edit the README.md.erb, NOT README.md
vim README.md.erb

# update README.md
bundle exec rake docs:readme > README.md

# commit them
git add README.md README.md.erb
git commit -m "update README"
```

Use `docs:readme:html` target to generate HTML version of `README.md` for review in
a browser.

```console
bundle exec docs:readme:html > README.html
firefox README.htnml
rm README.html
```

> [!CAUTION]
> Do NOT commit `README.html`.

### Running commands in each component

Use `submodule:each` target, which runs a shell file in each component. The
following command runs `status.sh` in each component.

```sh
# status.sh
git status
```

```console
bundle exec rake 'submodule:each[status.sh]'
```

> [!NOTE]
> The file is executed in a component directory. The working directory is
> `components/${COMPONENT_NAME}`.

> [!TIP]
> `NAME` environment variable is set to the component name so that you can use
> it in the script.

### Releasing a component

Run `release` target to release a component. `release` target will:

* Increment version string in `.eil.yml` and `idf_component.yml`
* Commit the changes to `main` branch
* Push to `origin`
* Create release

`release` targets requires two arguments, name of the component and which part
of the version should be incremented. The following example increments `patch`
version of `esp_idf_lib_helpers` component.

```console
bundle execc rake 'release[esp_idf_lib_helpers,patch]'
```

> [!CAUTION]
> Quote the argument to avoid shell expansion.

When the release is created, a GitHub Action workflows will:

* publish the documentation
* publish the component on ESP Component Registry

Now, the release is published.

### Cleaning files

Run `clean` target to clean all the unnecessary files, such as build files of
examples.

```console
bundle exec rake clean
```

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
> When the working directory is not in the repository, use `--repo es-idf-lib/${REPO_NAME}`.

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
