# JupyterHub team guide
      
This page holds resources for members of the JupyterHub and Binder teams.
They're meant to guide team members to be happy, productive members of the
team!

## What are the team resources?
   
There are a few resources that are particularly useful for team members. Here's
a quick list to get you started.
   
* [**The JupyterHub Team Compass**](https://jupyterhub-team-compass.readthedocs.io/en/latest/contributing.html)
  is a repository with lots of information about team-related things. It has
  development tips, information about team meetings, milestones and roadmaps,
  etc.
* [**The JupyterHub Team Compass issues**](https://github.com/jupyterhub/team-compass/issues)
  are where we often discuss specific, actionable things related to the *team*
  (e.g., discussing whether to change something in the team-compass repo).
* **The JupyterHub gitter channels** are used to have synchronous conversation
  for several projects. If a conversation will likely span multiple hours,
  or is relevant to many people, consider opening a thread in Discourse or
  the `team-compass` repository instead. Here are the relevant Gitters:

    * [The JupyterHub Gitter](https://gitter.im/jupyterhub/jupyterhub) is for
      discussing JupyterHub, Z2JH, TLJH, etc.
    * [The Binder Gitter](https://gitter.im/jupyterhub/binder) is for
      discussion with Binder users about how to use Binder.
    * [The mybinder.org-deploy gitter](https://gitter.im/jupyterhub/mybinder.org-deploy)
      is for discussion around **operating myinder.org**.

* [**The mybinder SRE guide**](https://mybinder-sre.readthedocs.io/en/latest/)
  is a set of resources for running mybinder.org. It contains tips, snippets,
  lessons-learned etc for running a large, public kubernetes cluster.
* [**The JupyterHub Team Google Drive**](https://drive.google.com/drive/u/1/folders/0B8VZ4vaOYWZ3X29KTzZSemlNSG8)
  is a place to store documents, presentations, images, etc that are useful to
  the team. You can put whatever you'd like here, just try to keep it organized :-)

## How can I help?
   
As a member of the team, you are encouraged to continue
helping in the same ways that you already have. Your contributions to
documentation, code, etc are always welcome, along with anything in the
["how can I contribute"](https://jupyterhub-team-compass.readthedocs.io/en/latest/contributing.html)
guide in the team-compass.
   
Don't forget that, as a member of the team, you're representing the community
when you interact with people (online and offline). Try to keep a friendly, positive
attitude, and be welcoming and helpful in bringing others into the community
and answering their questions.
   
### Are there any specific responsibilies?
   
We don't want team membership to
be a big burden (many of us have one or more other jobs too!) but there are
a few things that you should do as a new team member:
   
1. **"Watch" the [team compass repository](https://github.com/jupyterhub/team-compass)**
   so that you're notified when team conversations are happening.
2. **Semi-regularly attend team meetings**. You can find a calendar of upcoming
   meetings [on the team meetings page](https://jupyterhub-team-compass.readthedocs.io/en/latest/meetings.html).
3. **Follow the [Binder team responsibilities](https://jupyterhub-team-compass.readthedocs.io/en/latest/binder/governance.html#team-responsibilities) guidelines**.
   While this is scoped for the Binder team, it is a good rubric to follow for
   JupyterHub as well.
   
## When should I merge a pull request?

As a team member, you're encouraged to help others contribute to the project
by reviewing their code, guiding them towards making a contribution and
improving it, and ultimately merging their contribution into the project.

Having merge rights is both a privilege and a responsibility - please be
thoughtful when using it! To that extent, here are a few guidelines when
deciding to merge things into one of our repositories:

* **Use your best judgment**. As a member of the JupyterHub teams, we trust
  your judgment, and we ask you to use your best judgment in deciding when to
  take an action.
* **Make sure it's quality code**. We know this is somewhat subjective, but
  ensure that the code is well-organized and thoughtfully-written, that any
  new features are documented, and that it abides by best-practices in Python,
  JavaScript, etc.
* **Make sure there are tests**. We try not to merge any new features (or
  bugfixes!) without adding tests for them. It's easy to consider something
  minor-enough that it doesn't warrant a test, but try to avoid doing this!
  Adding tests usually only takes a moment, and our future selves will thank
  us for it later.
* **Make sure there's been enough time for discussion**. We're an open
  community with an inclusive decision-making process. This means that
  sometimes we need to slow down to make sure others have a chance to
  review and provide their thoughts on changes. There's no hard rule for
  this, but try to make sure people have a chance to weigh in. Consider
  pinging people that you think might be interested in a question, and
  give it a few extra days before merging if you think a topic will be
  complex enough to warrant discussion.
* **Don't be afraid to merge!** We know this is a bit counter-intuitive
  given what we just said, but don't be afraid to merge new code. If you
  think a change is really complex or potentially controversial, give it
  some time, but for most changes it is fine to just go ahead and merge.
  Again, we trust your judgment, and we don't want these guidelines to become
  a burden that slows down development.
  
