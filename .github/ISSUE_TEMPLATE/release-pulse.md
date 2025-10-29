---
name: "⏰ Time for release"
about: Coordinate the release of Z2JH and dependencies 
labels: release-pulse
title: "Time for release - {{ date | date('dddd, MMMM Do') }}"
---

This is a release reminder to help JupyterHub team members coordinate a new **Z2JH release**. This issue will be closed at the end of the week.

## Dependencies
Z2JH dependencies that might need a release too.

| Repository | Commits since latest version | Release Instructions |
| --- | --- |  --- |
| [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) | {{INSERT LATEST OAUTHENTICATOR COMMITS HERE}} | [RELEASE.md](https://github.com/jupyterhub/oauthenticator/blob/master/RELEASE.md) |
| [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | {{INSERT LATEST KUBESPAWNER COMMITS HERE}} | [RELEASE.md](https://github.com/jupyterhub/kubespawner/blob/master/RELEASE.md) |
| [jupyterhub/configurable-http-proxy](https://github.com/jupyterhub/configurable-http-proxy) | {{INSERT LATEST CHP COMMITS HERE}} | [RELEASE.md](https://github.com/jupyterhub/configurable-http-proxy/blob/main/RELEASE.md) |

### Make a release of dependencies

- **OAuthenticator**
    - [ ] A new release has been made 🎉
    - [ ] No new PRs had been merged, or a release isn't warranted for some reason
- **Kubespawner**
    - [ ] A new release has been made 🎉
    - [ ] No new PRs had been merged, or a release isn't warranted for some reason
- **Configurable-Http-Proxy**
    - [ ] A new release has been made 🎉
    - [ ] No new PRs had been merged, or a release isn't warranted for some reason

## Z2JH
Details and checklist to help coordinate the next Z2JH release.

### Details
Details about current state of Z2JH.

| Latest version | Commits since latest version |
| --- | --- |
| {{INSERT LATEST RELEASE HERE}} | {{INSERT LATEST COMMITS HERE}} |

**Currently open PRs:**
{{INSERT PRS HERE}}

### Make a release ([release instructions](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/master/RELEASE.md#release-process))
- [ ] **Changelog updated**
- [ ] **Tag pushed**
