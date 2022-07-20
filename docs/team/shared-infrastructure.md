# Shared accounts and infrastructure

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

## Documentation and ReadTheDocs

In general the JupyterHub team encourages the use of [ReadTheDocs](https://readthedocs.org).
This is a service that hosts documentation stored in online repositories.

For example, you can find the JupyterHub documentation at [jupyterhub.readthedocs.io](https://jupyterhub.readthedocs.io).
And the JupyterHub ReadTheDocs dashboard is at [readthedocs.org/projects/jupyterhub/](https://readthedocs.org/projects/jupyterhub/).

To get access to a documentation page for a JupyterHub repository, you'll need to be added by someone with the right privileges.
New users may be added by an admin via the {guilabel}`Admin` -> {guilabel}`Maintainers` menu.

In addition, ReadTheDocs offers [Pull Request previews](https://docs.readthedocs.io/en/stable/pull-requests.html) for changes to documentation, which may be enabled via the instructions [on this page](https://docs.readthedocs.io/en/stable/pull-requests.html).

## Figma page for designing images and logos

We have a [JupyterHub Figma Project](https://www.figma.com/file/20E31Z8TV1HLvDPn3ckTRR/Jupyter-Design-Assets?node-id=0%3A1) that can be used to quickly generate logos and images for use in our tools and documentation.
This is available to anybody with the link to edit, and you can ask in the team compass if you'd like to be added as an administrator.

It contains a variety of design assets from many projects, here's a preview below.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2F20E31Z8TV1HLvDPn3ckTRR%2FJupyter-Design-Assets%3Fnode-id%3D0%253A1" allowfullscreen></iframe>


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
### Google Cloud Platform (GCP) Project

The Binder Team uses a GCP project with id [`binderhub-288415`](https://console.cloud.google.com/home/dashboard?project=binderhub-288415) to host `gke.mybinder.org` and top level federation services at `mybinder.org`. The `binderhub-288415` GCP project resides in the GCP organization [`jupyter.org`](https://console.cloud.google.com/iam-admin/iam?organizationId=920697752286).

The `binderhub-288415` GCP project is currently funded by a grant from Google, as represented as GCP credits. The credits belong to billing account belonging to the GCP organization `jupyter.org`, as can be seen [under its billing section](https://console.cloud.google.com/billing?organizationId=920697752286).

### Other cloud deployments in the federation

There are a number of other cloud deployments in the BinderHub federation, but these are not centrally managed by the Binder Team.
Instead, they are managed by the individuals and organizations that represent each of the BinderHubs in the federation.
