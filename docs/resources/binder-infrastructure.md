# `mybinder.org` infrastructure

The `mybinder.org` service has some dedicated infrastructure that is unique to this service.
We describe the major pieces below:

## The Binder SRE guide

[**The mybinder SRE guide**](https://mybinder-sre.readthedocs.io/en/latest/)
is a set of resources for running mybinder.org.
It contains tips, snippets, lessons-learned etc for running a large, public kubernetes cluster.

## The `mybinder.org` domain

The `mybinder.org` domain is owned by Chris Holdgraf ([@choldgraf](https://github.com/choldgraf)).
The registrar for this domain is [BlueHost](https://bluehost.com).
The email address with contact information for the domain is `binder-team@googlegroups.com`.

```{admonition} TODO
In the future we wish to transfer ownership of this domain away from Chris's personal account.
However, it is unclear what is the best way to do this right now, and so we are waiting for clarification from the Jupyter project at-large about how the project itself can own mybinder.org instead of Chris. We also plan to use a contact email for this domain that has fewer people on it than the entire team, but are using `binder-team@googlegroups.com` as a stop-gap measure for now to increase our bus factor.
```

## DNS entries for `mybinder.org`

The DNS for `mybinder.org` is handled by [CloudFlare](https://www.cloudflare.com/), by a central Jupyter account.

(shared:gcp)=
## Google Cloud Platform (GCP) Project

The Binder Team uses a GCP project with id [`binderhub-288415`](https://console.cloud.google.com/home/dashboard?project=binderhub-288415) to host `gke.mybinder.org` and top level federation services at `mybinder.org`. The `binderhub-288415` GCP project resides in the GCP organization [`jupyter.org`](https://console.cloud.google.com/iam-admin/iam?organizationId=920697752286).

The `binderhub-288415` GCP project is currently funded by a grant from Google, as represented as GCP credits. The credits belong to billing account belonging to the GCP organization `jupyter.org`, as can be seen [under its billing section](https://console.cloud.google.com/billing?organizationId=920697752286).

## Other cloud deployments in the federation

There are a number of other cloud deployments in the BinderHub federation, but these are not centrally managed by the Binder Team.
Instead, they are managed by the individuals and organizations that represent each of the BinderHubs in the federation.
