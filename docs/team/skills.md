# Skills and ways to contribute

There are many ways that you can contribute to the JupyterHub / Binder projects.
This page attempts to provide some pathways for community members to learn and
apply their skills to the team.

## Where to start?

The short answer to this question is: it depends :-)  there are many
different ways to contribute to the JupyterHub community - technical, mentorship,
communications, community work, and documentation are just a few. You can either
apply your skills to help out, or use it as an opportunity to learn something new!

## A few general ways to help out

* Look through the issues in a repository, and help respond to issues that haven't been addressed already
* Guide conversation in issues so that they get closer to having a clear, actionable path forward
* For general questions about using JupyterHub, assist the person and then improve the documentation
  so that the answer is easier to find.
* For issues labeled "bug" try to clarify what is going on, and reproduce the bug on your machine
* For issues with reproducible bugs, in a PR write a test that will fail because of the bug.
* For issues with reproducible bugs, in a PR fix the bug and make sure that the test passes.
* For issues that describe new features, engage in conversation in the issue to define an actionable
  path forward.
* For issues that describe new features and with a clear path forward, open a PR that implements
  some or all of the feature.

## Things to know about JupyterHub

This section provides a combination of "skills that are helpful to learn in order
to contribute", as well as "ways you can contribute if you have these skills".

### JupyterHub-specific knowledge

- **JupyterHub component architecture**. JupyterHub is the underlying tool of many
  sub-projects in the JupyterHub/Binder ecosystem, and it's good to undertand its
  structure. This will make it easier to identify what to work on, what folks are
  talking about, and what repo might be the place to look at for a given task.
- **Code structure of the JupyterHub repository**. Familiarizing yourself with the code structure of
  JupyterHub will help you navigate the repository, and help others to do so as well.
  There is currently no single place that documents this (if you'd like to create a
  PR to add it, we'd love to help! [Here's an issue to discuss](https://github.com/jupyterhub/jupyterhub/issues/3080)).
- **Traitlets configuration**. JupyterHub uses [a tool called traitlets](https://traitlets.readthedocs.io/en/stable/)
  for configuration. You should familiarize yourself with Traitlets as well as the
  specific configuration values for JupyterHub. The traitlets documentation could be
  improved, if you're interested in helping out, [see this issue](https://github.com/jupyterhub/team-compass/issues/300).
- **YAML Configuration**. JupyterHub uses YAML, a way of structuring text as configuration
  files, in order to control the behavior of many tools in the JupyterHub ecosystem (as
  well as to configure CI/CD infrastructure). [Here is a quick primer on YAML](https://github.com/darvid/trine/wiki/YAML-Primer).
- **Testing infrastructure**. JupyterHub projects generally use [pytest](https://docs.pytest.org/en/stable/)
  for testing. However, some projects involve more complex tests than you'd normally find
  in a Python project. For example, mocking HTTP servers, or infrastructure that runs in the cloud.

### Server infrastructure

- **HTTP and REST APIs**. These are the ways in which services, extensions, and some
  authenticators interact with a JupyterHub.
- **tornado / asyncio**. JupyterHub uses these tools in order to send messages across
  JupyterHub infrastructure (e.g., between JupyterHub processes and user servers).

### UI/UX

- **HTML, CSS, and Jinja**. HTML and CSS are used to generate user-facing pages throughout
  JupyterHub. Jinja is a templating engine that allows you to create HTML pages with
  variables inserted into them for customization.
- **Javascript**. Some dynamic content on JupyterHub pages (or via extensions) uses
  Javascript to control the page's behavior.
* **UX/UI knowledge**. Aside from specific *implementations* of JupyterHub interfaces
  (which generally use HTML), it is also helpful to know about the structure and design
  of user interfaces, and considering the user experience as well.

### Deployment Infrastructure

- **Python**. Most JupyterHub projects are distributed as Python packages on [Pypi](https://pypi.org/). Packages are often installed in [virtual Python environments](https://docs.python-guide.org/dev/virtualenvs/) or [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- **Docker**. JupyterHub uses Docker throughout its projects to provide environments that
  both JupyterHub and other communities can deploy. Docker is a core part of the Kubernetes
  deployments of JupyterHub, and can also be used to control user environments in a JupyterHub.
- **Kubernetes basics**. A popular way to run JupyterHub is by using Kubernetes, a
  framework for orchestrating cloud infrastructure that is flexible and vendor-agnostic.
  Some projects of JupyterHub (in particular, [JupyterHub for Kubernetes](https://z2jh.jupyter.org),
  [Kubespawner](https://jupyterhub-kubespawner.readthedocs.io/en/latest/), and
  [BinderHub](https://binderhub.readthedocs.io/)) all use Kubernetes for their infrastructure.

### Community infrastructure

* **Technical Writing**. Every tool in the JupyterHub ecosystem is documented, and needs
  clear, concise, well-structured information to help others learn and use it. Any
  contributions that improve documentation are appreciated.
* **Issue guidance and triage**. Almost all enhancements to JupyterHub tools begin with
  an issue. They are the most common point of interaction with the broader community.
  To improve the content of our issues and facilitate improvements in JupyterHub, it is
  important to be a good listener, and to engage with others sharing their perspective.

## A note on complexity of tasks

Depth/expertise required for certain kinds of tasks can be hard to nail down and not at
all obvious. If you'd like to make a contribution and you're not sure where to start,
a good rule of thumb is to open an issue or reach out to another team member to help
you scope the work you'd like to do, and to set expectations.

## Links

* The [UC Berkeley JupyterHubs documentation](https://docs.datahub.berkeley.edu/en/latest/pre-reqs.html)
  has a similar scope and set of information.
