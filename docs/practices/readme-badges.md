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
url=https://hub.jupyter.org/helm-chart/info.json
query=$.jupyterhub.stable
colorB=orange
logo=helm
```

In this case, the badge is customized to fetch json data from an URL and fetch
the specific section in the json data as defined by the query. Here is the final
result.

```
https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm
```

Note that we specified a color for this badge, often that is automatically
assigned based on the the SemVer version, where something versioned 1.0.0 will
become blue while something versioned 0.9.0 would be orange. This was not
automatically determined for the Helm chart badge so it was explicitly
specified.



## Badges

### Build

[![Documentation build status](https://img.shields.io/readthedocs/jupyterhub?logo=read-the-docs)](https://jupyterhub.readthedocs.io/en/latest/)
```md
[![Documentation build status](https://img.shields.io/readthedocs/jupyterhub?logo=read-the-docs)](https://jupyterhub.readthedocs.io/en/latest/)
```


[![Test coverage of code](https://codecov.io/gh/jupyterhub/jupyterhub/branch/main/graph/badge.svg)](https://app.codecov.io/gh/jupyterhub/jupyterhub)
```md
[![Test coverage of code](https://codecov.io/gh/jupyterhub/jupyterhub/branch/main/graph/badge.svg)](https://app.codecov.io/gh/jupyterhub/jupyterhub)
```



### Package

[![Latest PyPI version](https://img.shields.io/pypi/v/jupyterhub?logo=pypi)](https://pypi.org/project/jupyterhub)
```md
[![Latest PyPI version](https://img.shields.io/pypi/v/jupyterhub?logo=pypi)](https://pypi.org/project/jupyterhub)
```


[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/jupyterhub?logo=conda-forge)](https://anaconda.org/conda-forge/jupyterhub)
```md
[![Latest conda-forge version](https://img.shields.io/conda/vn/conda-forge/jupyterhub?logo=conda-forge)](https://anaconda.org/conda-forge/jupyterhub)
```


[![Latest npm version](https://img.shields.io/npm/v/configurable-http-proxy?logo=npm)](https://www.npmjs.com/package/configurable-http-proxy)
```md
[![Latest npm version](https://img.shields.io/npm/v/configurable-http-proxy?logo=npm)](https://www.npmjs.com/package/configurable-http-proxy)
```


[![Latest stable release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```md
[![Latest stable release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=stable&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.stable&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```


[![Latest pre-release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=pre&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.pre&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```md
[![Latest pre-release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=pre&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.pre&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```


[![Latest development release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=dev&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.latest&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```md
[![Latest development release of the Helm chart](https://img.shields.io/badge/dynamic/json.svg?label=dev&url=https://hub.jupyter.org/helm-chart/info.json&query=$.jupyterhub.latest&colorB=orange&logo=helm)](https://hub.jupyter.org/helm-chart/)
```


### Community

[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/jupyterhub/issues)
```md
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/jupyterhub/issues)
```


[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub/10)
```md
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub/10)
```


[![Zulip](https://img.shields.io/badge/social_chat-zulip-blue?logo=zulip)](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub)
```md
[![Zulip](https://img.shields.io/badge/social_chat-zulip-blue?logo=zulip)](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub)
```
