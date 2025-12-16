# Team communication and user support

We organize our discussions in order to help both contributors and
maintainers find and choose the right communication channels and have a positive experience :-)

## Types of discussions

We break down team discussions into two broad categories:

1. **For specific discussions related to changing a repository's content** we use GitHub issues in the repository where they are most relevant. For example, feature requests, bug reports.
2. **For general discussion, support questions, feedback, etc**, use [the Jupyter forum](https://discourse.jupyter.org/).

## How to get in touch with the JupyterHub Council

There are two recommended ways to send communications to the @team-steering-council:

1. **Open an issue in our [Team Compass](https://github.com/jupyterhub/team-compass/issues)**. We use this as a space for team discussion of all kinds, and JupyterHub Council members are expected to monitor these issues. **This is the preferred space for most team conversation**.
2. **Send an e-mail to [`jupyterhub-team-council@googlegroups.com`](mailto:jupyterhub-team-council@googlegroups.com)**. This is a shared inbox that we use for people that prefer non-public or e-mail communication instead of GitHub issues.

## Chat

We use some chat channels to have synchronous conversation across projects.
Jupyter has recently adopted Zulip for chat, to replace the old Gitter/Matrix chat rooms.
If a conversation will likely span multiple hours, or is relevant to many people, consider opening a thread in Discourse or the `team-compass` repository instead.
Here are the relevant chat links:

* [The Jupyter Zulip](https://jupyter.zulipchat.com) is where Jupyter-related chat is taking place.
  You can use topics to thread conversations on particular areas.

* [The JupyterHub channel](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub) is for
  discussing JupyterHub, Binder, Z2JH, TLJH, etc.

## Support bot

To support our efforts in organizing the communication channels and make the
transition easier for both developers and users, we have plugged into the repositories
of the JupyterHub organization a [support bot](https://github.com/jupyterhub/.github/blob/main/.github/support.yml).

---
Currently, the bot will only check the following repositories:
* [binderhub](https://github.com/jupyterhub/binderhub)
* [jupyterhub](https://github.com/jupyterhub/jupyterhub)
* [the-littlest-jupyterhub](https://github.com/jupyterhub/the-littlest-jupyterhub)
---

**To trigger the support bot on an issue**, add the `support` label to an issue.
The bot will post a short and sweet message to inform the contributor about our communication policy
and will then close the issue. This support bot will act each time the `support` label is added
to an issue. Don't worry if you mistakenly label an issue as `support`. The action is reversible
and removing the label will reopen the issue.

We kindly encourage everybody to use the bot, if during this transition phase, any issues that
should be on Discourse, are opened on GitHub.
