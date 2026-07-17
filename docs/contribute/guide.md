# Welcome to the JupyterHub: Contributor Onboarding Guide

Welcome to JupyterHub!

This guide will help get you started as a contributor through a series of self-paced activities.
By the end, you'll have a good understanding of the project,how to contribute, and how to engage with our community.

JupyterHub is a multifaceted piece of infrastructure which can be used in many ways.
It is used in academic institutions as a key piece of infrastructure 
to bring interactive computing environments to learners. 

These can be Jupyter Notebooks, RStudio Sessions, marimo, etc., or any interactive web page environment.
JupyterHub supports a range of deployment options, from simple single-server setups to distributed environments managed by tools such as Docker, Kubernetes, system services or cloud infrastructure.While it doesn't have to be run with kubernetes, you'll find many production deployments use kubernetes.

JupyterHub is a low-level piece of critical infrastructure for many large scale computational learning environments worldwide. 

JupyterHub is also a collection of opinionated distributions of this infrastructure, for example [Zero to JupyterHub with Kubernetes](https://z2jh.jupyter.org/) 
and [The Littlest JupyterHub](https://tljh.jupyter.org/). 
If you have needs for bringing web-based interactive computing services to your learners, JupyterHub might be the right piece of kit for you. 
JupyterHub also provides the foundation for the [mybinder.org](https://mybinder.org/) ad hoc Jupyter environment service.

## Step 1: Understand Our Mission and Project Vision

- Read our [Project Overview](https://jupyterhub.readthedocs.io/en/stable/index.html) 
- **Activity:** Reflect on how our mission aligns with your interests and goals, share those reflections in your "Hello Jupyter Hub" note (Template Below)
- **Activity:** Familiarize yourself with JupyterHub [(the software) documentation](https://jupyterhub.readthedocs.io) and JupyterHub (the project) documentation [called the Team Compass](https://jupyterhub-team-compass.readthedocs.io)

## Step 2: Read Case Studies and see how people are using JupyterHub

- See how others are deploying JupyterHub in our [Gallery of Deployments](https://jupyterhub.readthedocs.io/en/stable/reference/gallery-jhub-deployments.html)
- Have a read through of the case studies and see the many ways JupyterHub is enabling learning, science and creativity globally.

## Step 3: Set Up Your Environment and/ or deploy your first JupyterHub
The first thing you should do is to determine what *type* of JupyterHub deployment will eventually meet your requirements:

- [The Littlest Jupyterhub](https://tljh.jupyter.org/en/latest/index.html) is useful in a small-scale setting, with few users and running on bare metal or a VM. For instance, in a small research setting with a few collaborators. It is not appropriate for larger (multiple tens or more users), long running and scalable deployments.

- [Zero to Jupyterhub](https://z2jh.jupyter.org/) allows better handling of authentication, scaling for many users, and runs natively on kubernetes.  This type of deployment would be appropriate for larger institutions that will be running Jupyterhub as a service, like in an educational, large-scale reserarch or enterprise setting with a dedicated SRE team.

- [JupyterHub the Hard Way](https://github.com/jupyterhub/jupyterhub-the-hard-way/tree/master) will have you deploy a JupyterHub from scratch, and give you a sense of the various parts of JupyterHub and how they interconnect. This resource explains the various components of JupyterHub and takes you through the manual process of interconnecting them. As you step through JupyterHub the hard way, submit any issues or challenges you encounter to the repo as issues (bugs) or pull requests (fixes). This is more useful as a learning tool, rather than the base for a long-running deployment.

Even if you're planning on a larger, Zero to Jupyterhub deployment, it might make sense to spin up Option 1 (The Littlest JupyterHub) to get a feel for how things are deployed.

Since there are many ways to deploy JupyterHub, from bare metal to kubernetes in the cloud, each with different tradeoffs and capabilities, we also recommend perusing the [Technical Overview](https://jupyterhub.readthedocs.io/en/stable/reference/technical-overview.html) to start.


### Option 1 - Deploy The Littlest JupyterHub

_If you're interested in installing or administering a JupyterHub the Littlest JupyterHub will help you stand up your first JupyterHub and get to know what is possible!_

- Explore [The Littlest JupyterHub](https://tljh.jupyter.org/en/latest/index.html) 
- **Activity:** Try to deploy your first Littlest JupyterHub. A good first platform option is a VM on Google Cloud, as it will provide you with free credits to deploy your first Littlest JupyterHub. While the overall layout of Google Cloud is subject to constant change, you should be able to deploy your first hub within 30 mins. Feel free to play with the many options, and look them up if you are unfamiliar with them. 

### Option 2 - Deploy Z2JH

_This option is for a user familiar with Kubernetes and perhaps a regular user of Kubernetes. It can help you get-started with JupyterHub. If you're not familiar with Kubernetes then Option #1 or #3 are probably better suited._

- Explore [Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/)
- **Activity** Create a k8s cluster on the platform of your choice (bare-metal or cloud), and deploy Zero to JupyterHub to that kubernetes cluster as a Helm chart.

### Option 3 - Development Environment Setup

_If you're interested in making development contributions, this will help you get started._

- Follow our [Development Environment Setup Guide](https://jupyterhub.readthedocs.io/en/latest/contributing/setup.html) (15-20 minutes)
- Run the test suite in your environment.
- Work through [JupyterHub The Hard Way](https://github.com/jupyterhub/jupyterhub-the-hard-way/tree/master) with the various components.
- **Activity:** Submit a PR to the Development Environment Setup Guide page for any setup problems you encounter in your environment.


## Step 4: Explore the Codebase and Team Compass

- Review our [Technical Overview](https://jupyterhub.readthedocs.io/en/stable/reference/technical-overview.html) 
- Familiarize yourself with the [Team Compass](https://compass.hub.jupyter.org/), our way of articulating how our community tries to "sail together". Notable sections to review are [Policies and Standards](https://compass.hub.jupyter.org/index-team_policies/) and our articulation of [Team Responsibilities](https://compass.hub.jupyter.org/team/structure/#expectations-of-all-team-members).


## Step 5: Engage with the Community

Get yourself connected with the JupyterHub community online. There
are a few places where we have conversations and discussion.

- Check out the [Jupyter Forum](https://discourse.jupyter.org/) and [Jupyter Hub Category](https://discourse.jupyter.org/c/jupyterhub/10) on the forum. Discoourse is the general watering hole for
the Jupyter community. The JupyterHub team uses this for most conversation, and tries to keep its repositories focused around more actionable items.
Review a few of the recent posts and familiarize yourself with the community and its conversations.

- Join our [Zulip Chat](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub) and introduce yourself. 
This platform is for in-person conversation. In general, if conversations last beyond a few seconds, we highly encourage you
to open a thread in the [JupyterHub Discourse page](https://discourse.jupyter.org) instead!

- Attend a community meeting (schedule in [Team Compass](https://compass.hub.jupyter.org/meetings/))It takes place once a month, and is open to anybody who would like to attend. We try to use this as an opportunity to sync-up and connect with the community.

- Attend a community collaboration café (schedule in Team Compass, [Jupyter Community Calendar](https://discourse.jupyter.org/t/jupyter-community-calendar/2485)) The collaboration café takes place on the first and third week of the month.

- Have a look at open issues on [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub/issues) or [jupyterhub/team-compass](https://github.com/jupyterhub/team-compass)


## Engagement Checklist

If you're excited about our project and want to stay involved, here are some next steps:

- [ ] Attend a JupyterHub Collaboration Café meeting (schedule in [Team Compass](https://compass.hub.jupyter.org/meetings/))
- [ ] [Browse and subscribe to JupyterHub's Discourse](https://discourse.jupyter.org/c/jupyterhub/)
- [ ] Subscribe to the [Project Jupyter Zulip](https://jupyter.zulipchat.com/) and [#jupyterhub](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub) Channel for project updates and introduce yourself
- [ ] Complete your first documentation [pull request](https://jupyterhub.readthedocs.io/en/stable/contributing/docs.html)
- [ ] Become familiar with the contributor guide
- [ ] Help another new contributor in the forums or Zulip channel

As a reminder, we expect all members of the JupyterHub community to adhere to the
[Jupyter Code of Conduct][link_coc] in these conversations.

## Step 6: Understand the Contribution Process

JupyterHub is an open community made up of people all over the world.
We invite participation of all forms - whether that be contributing
code, advice, documentation, support, or just a friendly face!

- Read our [Contributing Guide](https://jupyterhub.readthedocs.io/en/stable/contributing/index.html)

- **Challenge:** Identify one area where you think you could contribute to improve JupyterHub (code, documentation, testing, design, etc.) and add it to your introduction on Zulip.

## Step 7: Make Your First Contribution

_As you test out howtos and tutorials, or use the documentation, we welcome contributions which update or fix issues you find in the docs._

- Going through the documentation and [Team Compass](https://github.com/jupyterhub/team-compass), have you found anything that needs updating / improving? 
- Follow our [Step-by-Step Contribution Guide](https://jupyterhub.readthedocs.io/en/stable/contributing/index.html) to submit your first pull request 

If you'd like to start getting involved with JupyterHub projects,
here are a few resources to get you started.

## Do I really have something to contribute to JupyterHub?

Absolutely ✅. There are always ways to contribute to this community!

If you'd prefer not to write code, you can help out the JupyterHub community by
providing feedback in issues, participating in the [JupyterHub Discourse](https://discourse.jupyter.org),
sharing your experience with JupyterHub tools in an issue, improving documentation,
helping others with their problems, telling others about JupyterHub tools, and
coming to monthly meetings. There are lots of others ways to contribute without writing code -
we are happy to have any and all contributions!

If you'd like to write code, and have experience in some of the tools that JupyterHub uses
(e.g., shared infrastructure, dev-ops, kubernetes), then we would love your support in keeping
these tools a useful resource for the community. Try finding the
[![Help Wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][link_helpwanted] tag
in a repository and please ping a JupyterHub team member if you'd like any assistance!

If you don't have experience in these topics, then **contributing to JupyterHub is a great way to learn**.
The JupyterHub community works hard to share its knowledge of both JupyterHub tools and the
general problems that they try to solve, and we'd be happy to help you out.
If you're not sure where to start, look for the [![Good First Issue](https://img.shields.io/badge/-good%20first%20issue-blueviolet.svg)][link_goodfirstissue]
tag to begin your journey  learning about the JupyterHub stack.

## Contributing through GitHub

[git][link_git] is a really useful tool for version control.
[GitHub][link_github] sits on top of git and supports collaborative and distributed working.

You'll use [Markdown][markdown] to chat in issues and pull requests on GitHub.
You can think of Markdown as a few little symbols around your text that will allow GitHub
to render the text with formatting.
For example you could write words as bold (`**bold**`), or in italics (`*italics*`),
or as a [link][rick_roll] (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another webpage.

GitHub has a helpful page on
[getting started with writing and formatting Markdown on GitHub][writing_formatting_github].

## Generative AI (LLM) contributions

If you're thinking of using "AI" tools to contribute, make sure to check our ["Generative AI" / Large Language Model Contribution Policy](#llm-policy) first.

## Find issues to work on

If you'd like to make contributions to one of the JupyterHub repositories (this can
be either contributing code, commenting on issues, reviewing pull requests, or improving
documentation), we recommend checking out the **issue tags** to find issues that
are a good place to start.

The JupyterHub team tries to use tags to signal different *types* of issues. Two that you
might be interested in are **help wanted**, and **good first issue**. [GitHub Issues Search](https://github.com/issues)
can be used to quickly search across all of the issues in a GitHub organization that match
one of these tags. Here are a few links below to help you get started:

* [![Help Wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][link_helpwanted] *These issues contain a task that a member of the team has determined we need additional help with.*

* [![Good First Issue](https://img.shields.io/badge/-good%20first%20issue-blueviolet.svg)][link_goodfirstissue] *These issues contain a task that a member of the team thinks could be a good entry point to the project.*


## Guidelines to getting a Pull Request merged

These are not strict rules, but recommended guidelines from the JupyterHub maintainers to help make your contribution process as smooth and effective as possible for both you and the community.
- **Create a PR as early as possible**, marking it with `[WIP]` while
 This helps prevent duplicated work, allows maintainers to give early feedback on design or API changes, and can attract collaborators to work with you.
- **Keep your PR focused.**
  The best PRs address a single issue or feature.
  If you end up changing multiple things, please open separate PRs for the different conceptual changes.
- **Add tests to your code.**
  Contributions should come with appropriate tests and all continuous intergration (CI) checks must pass before the PR can be merged.
  PRs will not be merged if tests are failing.
- **Apply [PEP8](https://www.python.org/dev/peps/pep-0008/)** principles, but no need to be overly strict. Most of our repos have automatic formatting via [pre-commit](https://pre-commit.com/)
 Aim for consistency with the existing JupyterHub codebase. If you’re unsure, feel free to ask for guidance.
- **Use merge commits** instead of merge-by-squashing/-rebasing.
  This makes it easier to find all changes since the last deployment `git log --merges --pretty=format:"%h %<(10,trunc)%an %<(15)%ar %s" <deployed-revision>..` and your PR easier to review.
- **Make it clear when your PR is ready for review.**
  Prefix the title of your pull request (PR) with `[MRG]` if the contribution is complete and should be subjected to a detailed review. 

- **Link the issue you're working on.**
  Including a link to the issue your pull request seeks to address so collaborators and reviewers can easily understand the context, track progress and provide more effective feedback on your contribution.
  
- **Use commit messages to describe _why_ you are proposing the changes you are proposing.** 
#a great example of a commit message#

- **Try to not rush changes** (the definition of rush depends on how big your changes are).
  JupyterHub is maintained by a global community of contributors, many of whom are volunteers. Reviews may take time, so please be patient.
  Wait patiently for a reviewer to merge the PR.
  (Remember that **someone else** must merge your PR, even if you have the admin rights to do so.)


## Help contributing to a specific repository

Note that JupyterHub works on many different kinds of technology. The kind of tech you'll
use (as well as the set-up and skill needed to work on that tech) will depend on the
repository that you're working with. For example, the [Zero to JupyterHub for Kubernetes](https://github.com/jupyterhub/zero-to-jupyterhub-k8s)
repository will touch on aspects of dev-ops and cloud infrastructure.

To get oriented with a specific repository's needs and process around making new
contributions, look for a **repository-specific contributing guide**. This often
comes in the form of a **`CONTRIBUTING.md`** file, or a section of the documentation.

For example, [here is the `CONTRIBUTING.md` file for Zero to JupyterHub](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/main/CONTRIBUTING.md).
Note that it covers some of the tools you'll need for testing and developing the code,
which are not necessarily needed for the *other* JupyterHub repositories.

**Are the contributing docs unclear or misleading?** Then please let us know! We try to
make this documentation as helpful as possible, but we often don't have the perspective of
a new member to the community. Your input is extremely valuable in making it easy for others
to join the JupyterHub community!

## Additional Resources

- [Reference Docs](https://jupyterhub.readthedocs.io): Learn about the technical capabilities. 
Learn how to install, configure, deploy and manage JupyterHub.

- The [Jupyterhub Team Compass](https://compass.hub.jupyter.org/): Learn about our community structure and governance.This includes a contributor guide, project plans, meeting notes and development processes.

- [Code of Conduct](https://jupyter.org/governance/conduct/code-of-conduct/): Understand our community standards.

- [Project Roadmap](https://jupyterhub.readthedocs.io/en/stable/contributing/roadmap.html):We use the roadmap to develop a shared understanding of the project's vision and direction amongst the community of users, contributors, and maintainers. This is a great place to get a feel for what the maintainers are thinking about for the short, medium, and long term future of the project.

- [Subsystems of JupyterHub](https://jupyterhub.readthedocs.io/en/stable/#subsystems)
This page explains some of the design principles behind JupyterHub. Its a good place to understand why the team have made the decisions that they have along the way!

- [Common developer tasks and how-tos](https://jupyterhub.readthedocs.io/en/stable/howto/index.html)
Some notes on running tests, buildpack dependencies, creating a release, and keeping the pip files up to date.

## Thank you!

You're awesome. 👋🏻😊🦄

<br>

*&mdash; Based on contributing guidelines from the [STEMMRoleModels][link_stemmrolemodels] project.*


[link_helpwanted]: https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+user%3Ajupyterhub+archived%3Afalse+label%3A%22help+wanted%22+sort%3Aupdated-desc+
[link_goodfirstissue]: https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+user%3Ajupyterhub+archived%3Afalse+label%3A%22good+first+issue%22+sort%3Aupdated-desc+
[link_coc]: https://github.com/jupyter/governance/blob/main/docs/conduct/code_of_conduct.md
[link_git]: https://git-scm.com
[link_github]: https://github.com/jupyter/governance/blob/main/docs/conduct/code_of_conduct.md
[link_signupinstructions]: https://help.github.com/articles/signing-up-for-a-new-github-account
[link_stemmrolemodels]: https://github.com/KirstieJane/STEMMRoleModels
[markdown]: https://daringfireball.net/projects/markdown
[rick_roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[writing_formatting_github]: https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github

