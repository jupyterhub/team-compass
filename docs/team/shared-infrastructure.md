# Our Shared Infrastructure

There are a few services and infrastructure that the JupyterHub team has access to.
Some of these are useful for our development workflows, while others are used as a part of services that we run.

## GitHub

We have [a GitHub organization](https://github.com/jupyterhub/) for hosting all of our code repositories.
This organization is where we do most of the code-related work for the project, and where we have discussions and coordination.

## Image registry on quay.io

We have [a quay.io organization](https://quay.io/organization/jupyterhub) for hosting Docker images.
This is used for the repo2docker base image.
If you do not have access to this organization and require it, ask a team member to add you.

## Image registry on DockerHub

We have [a DockerHub organization](https://hub.docker.com/r/jupyterhub/jupyterhub/) for hosting Docker images.
BinderHub and JupyterHub images are pushed to DockerHub as that still works, though we are considering publishing these images to use quay.io as well.
If you do not have access to this organization and require it, ask a team member to add you.

## `mybinder.org` infrastructure

The `mybinder.org` service has a few pieces related to the domain that are described below:

### Ownership of the `mybinder.org` domain

The `mybinder.org` domain is owned by Chris Holdgraf ([@choldgraf](https://github.com/choldgraf)).
The registrar for this domain is [BlueHost](https://bluehost.com).
The email address with contact information for the domain is `binder-team@googlegroups.com`.

```{admonition} TODO
In the future we wish to transfer ownership of this domain away from Chris's personal account.
However, it is unclear what is the best way to do this right now, and so we are waiting for clarification from the Jupyter project at-large about how the project itself can own mybinder.org instead of Chris. We also plan to use a contact email for this domain that has fewer people on it than the entire team, but are using `binder-team@googlegroups.com` as a stop-gap measure for now to increase our bus factor.
```

### DNS entries for `mybinder.org`

The DNS for `mybinder.org` is handled by [CloudFlare](https://www.cloudflare.com/), by a central Jupyter account.

(shared:gcp)=
### Google Cloud Project

The Binder Team uses a Google Cloud Project called `binderhub`.
This project runs the BinderHub deployment that is found at `gke.mybinder.org`.
The project is currently funded from a grant from Google.

### Other cloud deployments in the federation

There are a number of other cloud deployments in the BinderHub federation, but these are not centrally managed by the Binder Team.
Instead, they are managed by the individuals and organizations that represent each of the BinderHubs in the federation.
