# Making releases

To make a new release, we should be able to follow the project's RELEASE.md
file. Since these files can get outdated, its good to refer to this document and
our [template project's RELEASE.md file] from time to time to keep it updated.

## Release ambitions

- To document and automate the release process well enough for repository
  maintainers to have the agency to make regular releases.
- To follow a versioning scheme such as [SemVer 2], where we update the
  MAJOR.MINOR.PATCH versions according to the versioning scheme.
- To maintain changelogs, and update them for each release.
- To keep release practices across projects updated by upstreaming release
  practice improvements from individual projects to the [template project]'s
  files and the [team-compass project]'s documentation, and to to downstream
  updates from there to other projects.

## Release practices

### Changelog updates with `github-activity`

We look to have our changelogs summarize most pull requests that has been
merged, we use `github-activity` to help us with this.

#### Create PR list with `github-activity`

1. `pip install -U github-activity`

   Get the latest version.

2. `git checkout main`, `git pull`, `git remote -v`, and `git log`

   Ensure you will work against the latest changelog file and that
   github-activity will be able to inspect the latest git tags locally.

   The remote and log commands are to help you check you didn't just update
   against a remote fork.

3. `github-activity --heading-level=3`

   First acquire a preliminary list of pull requests, then revise labels and
   titles of pull requests, then acquire a final list of pull requests to update
   the changelog with.

   1. Revise PR labels

      PRs listed under `Other merged PRs` doesn't have a label to make it listed
      in another category. If you think they should be, visit the PR and add a
      suitable label to it.

   2. Revise PR titles

      PR titles should describe the change made for readers of a changelog.
      Check if there is a PR title that is worth updating.

      As an example, in the jupyterhub/oauthenticator projects its relevant for
      users to know if a change affected a specific authenticator class they
      use. Due to that, we've tried to let that be captured in the title, such
      as `[GitHub] Fix ...`.

   3. Revise final list

      Some pull requests could be seen as irrelevant to list, for example we
      could opt to omit automatic updates to the versions of pre-commit hooks or
      github actions.

#### Create a changelog entry

1. Come up with the new version number

   Assuming we are using [SemVer 2] as a versioning scheme, we should:

   - increment the major version if a breaking change has been made
   - increment the minor version if a new features has been added
   - increment the patch version if a bug has been fixed

2. Update the changelog file

   - Add the previously generated PR list.
   - Align formatting with previous releases.
   - Add a preliminary release date.
   - At least for major releases, lead with a manually written summary.

3. Open a pull request

   Make a commit named like `Add changelog for 1.2.3` and open a PR with it
   titled the same.

4. Ready for release

   With a changelog PR approved, you can self-merge it and make a release
   according to the project's RELEASE.md file. Before merging, update the
   preliminary release date if needed, or add a commit doing it before using
   `tbump`.

### Version updates with `tbump`

Our RELEASE.md files often describes how to use `tbump` to update version
strings in files such as `_version.py` in a commit, tag the commit, and push it.

Projects configure `tbump` via `pyproject.toml` to update the project's specific
files containing a version reference, such as `_version.py`, `setup.py`, and
`package.json`.

The [template project's pyproject.toml file] provides an example on how to
configure `tbump`, and the [template project's RELEASE.md file] provides an on
how to use it.

### Publishing to PyPI

Publishing a release to PyPI should be automatic as soon as a git tag is pushed.
A git tag is typically pushed by the use of `tbump` according to a RELEASE.md
file, and the automation to publish to PyPI is typically done by a GitHub
workflow named `release.yaml`.

The [template project's .github/workflows/release.yaml file] and the [template
project's RELEASE.md file] can be inspected for more details about this.

### Publishing to conda-forge

Publishing a release to conda-forge should be managed by a dedicated feedstock
GitHub repository, and the RELEASE.md file should link to it for reference as
done in the [template project's RELEASE.md file].

[semver 2]: https://semver.org/
[`github-activity`]: https://github.com/executablebooks/github-activity
[template project]: https://github.com/jupyterhub/jupyterhub-python-repo-template
[team-compass project]: https://github.com/jupyterhub/team-compass
[template project's release.md file]: https://github.com/jupyterhub/jupyterhub-python-repo-template/blob/main/RELEASE.md
[template project's pyproject.toml file]: https://github.com/jupyterhub/jupyterhub-python-repo-template/blob/main/pyproject.toml
[template project's .github/workflows/release.yaml file]: https://github.com/jupyterhub/jupyterhub-python-repo-template/blob/main/.github/workflows/release.yaml
