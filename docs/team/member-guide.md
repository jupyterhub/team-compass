# JupyterHub and Binder team guide

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

### General policy about communication channels

We are trying to organize our discussions in order to help both contributors and
maintainers find and choose the right communication channels and have a positive experience :-)

In this respect, we are using:
1. GitHub issues for specific discussions related to changing a repository's content
(e.g. feature requests, bug reports).
2. The [Discourse forum](http://discourse.jupyter.org/) for general discussions, support
questions, or just as a place where we can inspire each other.

To support our effors in organizing the communication channels and make the
transition easier for both developers and users, we have plugged into the repositories
of the JupyterHub organization a [support bot](https://github.com/jupyterhub/.github/blob/master/.github/support.yml).
The bot will post a short and sweet message to inform the contributor about our communication policy
and will then close the issue. This support bot will act each time the `support` label is added
to an issue. Don't worry if you mistakenly label an issue as `support`. The action is reversible
and removing the label will reopen the issue.

We kindly encourage everybody to use the bot, if during this transition phase, any issues that
should be on Discourse, are opened on GitHub.

## How can I help?

As a member of the team, you are encouraged to continue
helping in the same ways that you already have. Your contributions to
documentation, code, etc are always welcome, along with anything in the
["how can I contribute"](https://jupyterhub-team-compass.readthedocs.io/en/latest/contributing.html)
guide in the team-compass. If you're on the Binder team, then check out
[the Binder team responsibilities](https://jupyterhub-team-compass.readthedocs.io/en/latest/binder/governance.html#team-responsibilities)
page for more information.

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
4. **Commit at least 6 months to team membership**. Training and mentoring new
   team members is an investment by the existing team, hence team
   membership requires commitment from both sides. Beyond 6 months, if active
   team membership is no longer possible for you, you can always
   join the green team!
5. **Let us know if you'll be unavailable** or out of town for an extended period
   of time. It's no problem if you need to focus on other things for a bit, but it's
   helpful for the team to know who will be around.
   To do so, [open an issue in the team-compass](https://github.com/jupyterhub/team-compass/issues/new).
   If it's something you'd rather not mention to the public then
   send an email to one of the team members letting them know, and they
   can communicate it to the others.

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

## Periodic team check-ins

We want team membership to be an opportunity to grow and have an impact, not
a burden or a time sink. While we ask for a minimum 6 month commitment when
you join a JupyterHub or Binder team, we don't expect this commitment to
last forever.

We try to conduct regular "check-ins" for team members approximately once every 6 months.
The goal is to make sure that you're happy in your current position with the JupyterHub project,
and discuss whether you'd like to continue in your current role, transition to
a different role, or transition to the green team.

These check-ins happen via GitHub issues on the team compass repository,
here's the issue text to use:

```
Title: Team check-in for choldgraf
Body:

Hello <username>, this is a [team check-in](<link to this docs page>) for your JupyterHub team status.
Please respond below if you're interested in either:

* Continuing in your current role
* Moving to a new role
* Moving to the green team

There's no pressure one way or another, this is just to check that you're still
comfortable with the role and responsibilities for your current position.
```

There's no pressure or expectation associated with these check-ins, their goal
is to make sure that team members have an opportunity to voice their perspective
and choose their next steps within the community.

If you decide to change team status, we'll make a PR either to the
[BinderHub team data page](https://github.com/jupyterhub/team-compass/blob/master/docs/team/contributors-binder.yaml)
or the [JupyterHub team data page](https://github.com/jupyterhub/team-compass/blob/master/docs/team/contributors-jupyterhub.yaml).
Either way, we'll update the latest time that you had a check-in.

### If a team member doesn't respond to a check-in

Sometimes team members aren't able to respond to check-ins. This is no problem -
other duties, life, vacation, etc often get in the way. In this case,
we'll try to reach out with the following steps.

- First, we'll ping team members in their check-in issue to maximize likelihood of notifications
- After 7 days, we'll ping the issue again with a "maybe you missed this" comment
- After 14 days, we'll send an email
- After 21 days, we'll send a follow-up email to double-check your availability.
- After 30 days if you haven't responded, we'll move you to the green team
- You can move back into another team whenever you like - just reach out and we'll revert the change.
