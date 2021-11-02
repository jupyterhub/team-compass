# Repository Management and Code Standards

JupyterHub projects should take advantage of pre-commit and tools to help maintain consistent formatting within a repo to improve overall code quality, review efficiency, and readability of code.
Sensible use of pre-commit to run formatting tools and code linters can add consistency and improve maintainability.

## Preferred tools and pre-commit hooks

The team has found the following tools and their pre-commit hooks to be useful. The following pre-commit hooks can be added to any repo when convenient, though please communicate with anyone who has an open pull request if it will lead to major conflicts:

  - [black](https://black.readthedocs.io/)
  - [prettier](https://prettier.io/)
  - [flake8](https://flake8.pycqa.org/en/latest/)
  - **TODO: standard pre-commit hooks, such as isort, etc. (To be determined and listed here)**

## Applying to repos

When creating a new repo, please use any pre-commit hooks and tools that are useful.

When working with an existing repo, please balance the benefits of adding a tool or pre-commit hook with considerations such as
  - the amount of code churn
  - how it will improve code maintainability
  - the time it may add to CI runs.

## Configuration of a tool

In general using the default settings for tools is preferred, but use your judgment as to whether to apply a stricter or more lenient configuration for linting code.
Example configurations are in:

  - [JupyterHub](https://github.com/jupyterhub/jupyterhub/) (a large repository which was converted and therefore has a fairly lax configuration)
  - [nativeauthenticator](https://github.com/jupyterhub/nativeauthenticator) (a fairly strict configuration)

Other linters, autoformatters and tools can be added to other repos on an ad-hoc basis if it's not too disruptive- this is a good way to try out new tools.
In general, big changes should not be made to high profile repos without prior discussion.

## Proposing organization-wide use of a tool

If the new tool is useful across the organisation please propose it in a new team-compass GitHub issue, outlining the advantages and disadvantages.
