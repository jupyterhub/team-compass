# Shared accounts and infrastructure

There are a few services and infrastructure that the JupyterHub team has access to.
Some of these are useful for our development workflows, while others are used as a part of services that we run.

## GitHub

We have [a GitHub organization](https://github.com/jupyterhub/) for hosting all of our code repositories.
This organization is where we do most of the code-related work for the project, and where we have discussions and coordination.

## Google Drive

We have a [**JupyterHub Team Google Drive**](https://drive.google.com/drive/u/1/folders/0B8VZ4vaOYWZ3X29KTzZSemlNSG8) to store documents, presentations, images, etc that are useful to the team.
You can put whatever you'd like here, just try to keep it organized :-)

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

See [](binder-infrastructure.md) for more details.
