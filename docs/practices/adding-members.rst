======================================
Adding and onboarding new team members
======================================

This page contains information about adding new team members and onboarding
them.

What to consider when adding a team member
==========================================

We have a few teams within the JupyterHub community, with varying degrees of
expectations and responsibilities.

For someone to join a team, they should be a consistent,
positive, productive member of the community.
Moreover, team members should be interested in
**continuing their engagement** over a long-ish period of time.

They should:

- Be familiar with `our Team Practices and Policies <../practices/index>`_
- Be willing to commit to `the responsibilities that come with team membership <../practices/responsibilities>`_

Process for adding team members
===============================

Any new team members must be "championed" by a pre-existing team member. This
is a person who recommends that the new person be invited to join the team.
This process takes the following steps:

1. The champion should first discuss internally with team members to get buy-
   in and ensure that there's general consensus before officially starting
   the process.
2. If there seems to be team consensus,
   the champion contacts the potential new team member and ask if they are
   interested. Don't forget to run them by the responsibilities in the :doc:`../team/structure`
   page to make sure they understand what they're signing up for.
   If so, then move to the next step.
3. The champion opens a new issue in the `team compass repository <https://github.com/jupyterhub/team-compass>`_.
   The issue should state your support of the new team member, discuss why
   you think they are great and why they should join the team.
4. This issue should stay open for around 10 days to give members of the team
   a chance to weigh in their thoughts (and support!).
5. If there are no objections that haven't been resolved, the new team member
   is welcomed into the community as an official team member!
6. Finally, make sure to follow the steps in :ref:`onboarding`.

.. _onboarding:

Onboarding a new team member
============================

Once a new team member has joined, there are a number of things to take care
of in order to make sure they're in a position to be a productive and happy
member of the team. These sections cover what to do!

The onboarding checklist
------------------------

Copy and paste the checklist below into a new GitHub
issue and follow each step. Once all steps are completed, we can close the
issue and the team member is now ready to go!

.. code-block:: md
   
   **Things the new team member needs**
   - [ ] A gmail account (for GKE credentials + Google team drive)
   - [ ] A [PyPI account](https://pypi.org) (for PyPI access)
   - [ ] A [Discourse account](https://discourse.jupyter.org)
   
   **Membership**
   
   - [ ] Add them to the [binderhub google group](https://groups.google.com/forum/#!forum/binder-team)
   - [ ] Add them to the [binderhub team in the github organization](https://github.com/orgs/jupyterhub/teams/binder-team)
   - [ ] Add them to the [Discourse jupyterhub group](https://discourse.jupyter.org/g/jupyterhub-team)
   
   **Permissions**
   
   - [ ] Make sure they have permissions on the [google cloud projects](https://console.cloud.google.com/home/dashboard?project=binder-prod)
         (binder-prod, binder-staging, binder-sandbox)
   - [ ] Add them as collaborators on the repo2docker and BinderHub PyPI packages
   - [ ] Add them to the [jupyterhub team google drive](https://drive.google.com/drive/folders/0B8VZ4vaOYWZ3a2dyeEp6NzBKbnM?usp=sharing)

   **Learning**
   
   - [ ] Send them [a short onboarding message](https://jupyterhub-team-compass.readthedocs.io/team/adding-members.html#an-official-onboarding-message)
   
   **Community**
   
   - [ ] Add them to the [jupyterhub or binderhub team yaml files](https://github.com/jupyterhub/team-compass/tree/5d014f3af161e3abcf79c7adfb77620607929d77/docs/team)
   - [ ] Tell people in Discourse + Twitter about our awesome new community member

An official onboarding message
------------------------------

The last thing to do after all of the boxes have been checked is to send the
person a message saying "welcome to the team!" This has two goals: one is
to give a friendly welcome to our new member and make it "official", the other
is to provide them some guidance and helpful information to get started. Here
is a template message to send. It checks off all of the boxes in the
"learning" section above.

.. code-block:: md

   Hello <name>, and welcome to the JupyterHub team! 🎉🎉🎉
   
   We are really excited for you to join the community. To help you get started,
   check out the [jupyterhub team member guide](https://jupyterhub-team-compass.readthedocs.io/en/latest/team/member-guide.html)
   as well as the [BinderHub team responsibilities](https://jupyterhub-team-compass.readthedocs.io/en/latest/binder/governance.html#team-responsibilities)
   page.

   If you've got any questions or would just like to chat, don't hesitate to
   reach out to folks on the Gitter channels or on Discourse!
   
