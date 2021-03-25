---
name: ":package: Time for release"
about: Coordinate the release of Z2JH and dependencies 
labels: release-pulse
title: "Time for release - {{ date | date('dddd, MMMM Do') }}"
---

This is a release reminder to help JupyterHub team members coordinate a new Z2JH release. This issue will be closed at the end of the week.

### Z2JH

**Latest version:**

{{INSERT LATEST RELEASE HERE}}

**Commits since latest version:**

{{INSERT LATEST COMMITS HERE}}

**PRs open:**

{{INSERT PRS HERE}}

### Dependencies

Z2JH dependencies that might need a release too.

#### OAuthenticator

**Commits since latest version:**

{{INSERT LATEST OAUTHENTICATOR COMMITS HERE}}

#### Kubespawner

{{INSERT LATEST KUBESPAWNER COMMITS HERE}}

#### Configurable-Http-Proxy

{{INSERT LATEST CHP COMMITS HERE}}
