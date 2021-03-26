---
name: "⏰ Time for release"
about: Coordinate the release of Z2JH and dependencies 
labels: release-pulse
title: "Time for release - {{ date | date('dddd, MMMM Do') }}"
---

This is a release reminder to help JupyterHub team members coordinate a new Z2JH release. This issue will be closed at the end of the week.

## Dependencies
Z2JH dependencies that might need a release too.

### OAuthenticator
Commits since latest version:
{{INSERT LATEST OAUTHENTICATOR COMMITS HERE}}

**Make a release** ([release instructions](https://github.com/jupyterhub/oauthenticator/blob/master/RELEASE.md))
- [ ] A new release has been made :tada:
- [ ] No new PRs had been merged, or a release isn't warranted for some reason

### Kubespawner
:eight_pointed_black_star: Commits since latest version:
{{INSERT LATEST KUBESPAWNER COMMITS HERE}}

:eight_pointed_black_star: **Make a release** ([release instructions](https://github.com/jupyterhub/kubespawner/blob/master/RELEASE.md))
- [ ] A new release has been made :tada:
- [ ] No new PRs had been merged, or a release isn't warranted for some reason

### Configurable-Http-Proxy
:eight_pointed_black_star: Commits since latest version:
{{INSERT LATEST CHP COMMITS HERE}}

:eight_pointed_black_star: **Make a release** ([release instructions](https://github.com/jupyterhub/configurable-http-proxy/blob/main/RELEASE.md))
- [ ] A new release has been made :tada:
- [ ] No new PRs had been merged, or a release isn't warranted for some reason

## Z2JH
Details and checklist to help coordinate the next Z2JH release.

### Details
Details about current state of Z2JH.

- **Latest version:**
{{INSERT LATEST RELEASE HERE}}

- **Commits since latest version:**
{{INSERT LATEST COMMITS HERE}}

- **Currently open PRs:**
{{INSERT PRS HERE}}

### Make a release ([release instructions](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/master/RELEASE.md#release-process))
- [ ] **Changelog**
- [ ] **Tag pushed**
