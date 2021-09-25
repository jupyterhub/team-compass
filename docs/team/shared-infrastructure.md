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

## Image registry on Dockerhub

We have [a DockerHub organization](https://hub.docker.com/r/jupyterhub/jupyterhub/) for hosting Docker images.
BinderHub and JupyterHub images are pushed to DockerHub as that still works, though we are considering publishing these images to use quay.io as well.
If you do not have access to this organization and require it, ask a team member to add you.

## Google Cloud Project

The Binder Team uses a Google Cloud Project called `binderhub`.
This project runs the BinderHub deployment that is found at `gke.mybinder.org`.
The project is currently funded from a grant from Google.
