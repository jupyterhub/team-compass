# Readme Badges

These are example badges in Markdown that we typically put just below the header
of the README.md file of the repository. See for example
[jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner). Most of the
badges get the image representing the badge itself from
[shields.io](https://shields.io).



## About shields.io

The badges is typically customized by passing query string parameters, to better
understand these lets consider the most complicated badge in this list, the Helm
chart badges.

The Helm chart badges are constructed on
`https://img.shields.io/badge/dynamic/json.svg` as a foundation along with a set
of query strings.

```
label=stable
url=https://jupyterhub.github.io/helm-chart/info.json
query=$.jupyterhub.stable
colorB=orange
logo=helm
```

In this case, the badge is customized to fetch json data from an URL and fetch
the specific section in the json data as defined by the query. Here is the final
result.

`https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm`

Note that we specified a color for this badge, often that is automatically
assigned based on the the SemVer version, where something versioned 1.0.0 will
become blue while something versioned 0.9.0 would be orange. This was not
automatically determined for the Helm chart badge so it was explicitly
specified.



## Badges

### Build

[![Documentation build status](https://img.shields.io/readthedocs/jupyterhub?logo=read-the-docs)](https://jupyterhub.readthedocs.org/en/latest/)
```markdown
[![Documentation build status](https://img.shields.io/readthedocs/jupyterhub?logo=read-the-docs)](https://jupyterhub.readthedocs.org/en/latest/)
```


[![CircleCI build status](https://img.shields.io/circleci/build/github/jupyterhub/jupyterhub?logo=circleci)](https://circleci.com/gh/jupyterhub/jupyterhub)
```markdown
[![CircleCI build status](https://img.shields.io/circleci/build/github/jupyterhub/jupyterhub?logo=circleci)](https://circleci.com/gh/jupyterhub/jupyterhub)
```


[![TravisCI build status](https://img.shields.io/travis/jupyterhub/jupyterhub/master?logo=travis)](https://travis-ci.org/jupyterhub/jupyterhub)
```markdown
[![TravisCI build status](https://img.shields.io/travis/jupyterhub/jupyterhub/master?logo=travis)](https://travis-ci.org/jupyterhub/jupyterhub)
```


[![AzurePipelines build status](https://img.shields.io/azure-devops/build/jupyter/repo2docker/1?logo=azure-pipelines)](https://dev.azure.com/jupyter/repo2docker/_build)
```markdown
[![AzurePipelines build status](https://img.shields.io/azure-devops/build/jupyter/repo2docker/1?logo=azure-pipelines)](https://dev.azure.com/jupyter/repo2docker/_build)
```


[![DockerHub build status](https://img.shields.io/docker/build/jupyterhub/jupyterhub?logo=docker&label=build)](https://hub.docker.com/r/jupyterhub/jupyterhub/tags)
```markdown
[![DockerHub build status](https://img.shields.io/docker/build/jupyterhub/jupyterhub?logo=docker&label=build)](https://hub.docker.com/r/jupyterhub/jupyterhub/tags)
```


[![Test coverage of code](https://codecov.io/gh/jupyterhub/jupyterhub/branch/master/graph/badge.svg)](https://codecov.io/gh/jupyterhub/jupyterhub)
```markdown
[![Test coverage of code](https://codecov.io/gh/jupyterhub/jupyterhub/branch/master/graph/badge.svg)](https://codecov.io/gh/jupyterhub/jupyterhub)
```



### Package

[![Latest PyPI version](https://img.shields.io/pypi/v/jupyterhub?logo=pypi)](https://pypi.python.org/pypi/jupyterhub)
```markdown
[![Latest PyPI version](https://img.shields.io/pypi/v/jupyterhub?logo=pypi)](https://pypi.python.org/pypi/jupyterhub)
```


[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/jupyterhub?logo=conda-forge)](https://anaconda.org/conda-forge/jupyterhub)
```markdown
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/jupyterhub?logo=conda-forge)](https://anaconda.org/conda-forge/jupyterhub)
```


[![Latest npm version](https://img.shields.io/npm/v/configurable-http-proxy?logo=npm)](https://www.npmjs.com/package/configurable-http-proxy)
```markdown
[![Latest npm version](https://img.shields.io/npm/v/configurable-http-proxy?logo=npm)](https://www.npmjs.com/package/configurable-http-proxy)
```


[![Latest stable release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```markdown
[![Latest stable release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```


[![Latest pre-release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=pre&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.pre&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```markdown
[![Latest pre-release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=pre&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.pre&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```


[![Latest development release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=dev&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.latest&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```markdown
[![Latest development release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=dev&url=https://jupyterhub.github.io/helm-chart/info.json&query=$.jupyterhub.latest&colorB=orange&logo=helm)](https://jupyterhub.github.io/helm-chart/)
```


### Community

[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/jupyterhub/issues)
```markdown
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/jupyterhub/issues)
```


[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)
```markdown
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)
```


[![Gitter](https://img.shields.io/badge/social_chat-gitter-blue?logo=gitter)](https://gitter.im/jupyterhub/jupyterhub)
```markdown
[![Gitter](https://img.shields.io/badge/social_chat-gitter-blue?logo=gitter)](https://gitter.im/jupyterhub/jupyterhub)
```
