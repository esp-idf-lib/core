# Managing `esp-idf-lib/core`

<!-- vim-markdown-toc GFM -->

* [Requirements](#requirements)
* [`Rakefile`](#rakefile)
    * [Generating README.md](#generating-readmemd)
    * [Releasing a component](#releasing-a-component)
    * [Cleaning files](#cleaning-files)
* [`gh` 101](#gh-101)
    * [Authentication](#authentication)
    * [Basics](#basics)
    * [Listing workflows](#listing-workflows)
    * [Running workflows](#running-workflows)

<!-- vim-markdown-toc -->

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

The operational workflows extensively use `rake` and `gh`.

* Run `rake` command in the top-level directory of `esp-idf-lib` repository.
* Run `gh` in the repository you are working on.

Read [`gh` 101](#gh-101) section first if you are not familiar with `gh` CLI.

## Requirements

* ruby
* [bundler](https://bundler.io/)
* git
* [gh](https://cli.github.com/)

```sh
bundle install
```

> [!TIP]
> Create an alias command to type less when executing `bundle exec`, such as
> `be='bundle exec'`.

## `Rakefile`

`Rakefile` is a ruby version of `Makefile`. The `Rakefile` and files under
`rakelib` implements operations to manage the repository.

### Generating README.md

Run `readme` target generates `README.md` from `README.md.erb`.
`README.md.erb` is the template to generate `README.md`.

> [!CAUTION]
> Do NOT edit `README.md`. Edit `README.md.erb` instead.

```sh
bundle exec rake readme
```

The above command outputs the generated markdown to standard out.

A typical workflow to update `README.md`:

1. Edit `README.md.erb`
1. Generate `README.md` with `readme` target
1. Commit `README.md` and `README.md.erb`

```sh
vim README.md.erb
bundle exec rake readme > README.md
git add README.md README.md.erb
git commit -m "update README"
```

Use `readme:html` target to generate HTML version of `README.md` for review in
a browser.

```sh
bundle exec readme:html > README.html
firefox README.htnml
rm README.html
```

> [!CAUTION]
> Do NOT commit `README.html`.

### Releasing a component

Run `release` target to release a component. `release` target will:

* Create a release branch `release/$MAJOR.$MINOR.$PATH`
* Increment version string in `.eil.yml` and `idf_component.yml`
* Commit the changes to the branch
* Push the branch to `origin`

`release` targets requires two arguments, name of the component and which part
of the version should be incremented. The following example increments `patch`
version of `esp_idf_lib_helpers` component.

```sh
bundle execc rake 'release[esp_idf_lib_helpers,patch]'
```

> [!CAUTION]
> Quote the argument to avoid shell expansion.

1. Open the repository page in a browser.
2. Create a PR to merge the branch
3. Merge it when the checks pass

Create a release from the branch:

```sh
gh release create `bin/eil-q version` --notes "Release `bin/eil-q version`" --title "Release `bin/eil-q version`"
```

> [!NOTE]
> `bin/eil-q` is a script to query `.eil.uml`. All repositories have it.

GitHub Action workflows will:

* publish the documentation
* publish the component on ESP Component Registry

Done.

### Cleaning files

Run `clean` target to clean all the unnecessary files, such as build files of
examples.

```sh
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
echo echo 'your_token' | gh auth login --with-token
```

> [!NOTE]
> Replace `your_token` with the token.

### Basics

`gh` automates many operations with GitHub. It can create issues, releases,
run workflows, among others.

> [!NOTE]
> Change the directory to the repository directory and run `gh` command.
> When the working directory is not in the repository, use `--repo es-idf-lib/${REPO_NAME}`.

```sh
cd components/esp_idf_lib_helpers

# opens the repository page in a browser
gh browse
```

### Listing workflows

```sh
gh workflow ls
```

### Running workflows

```sh
gh workflow run "Publish the component to ESP Component Registry"
```

> [!NOTE]
> The workflow must have `workflow_dispatch` enabled.

See also:

* [Manually running a workflow](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)
* [workflow_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch)
