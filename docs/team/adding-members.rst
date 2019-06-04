======================================
Adding and onboarding new team members
======================================

This page contains information about adding new team members and onboarding
them.

Adding a new team members
=========================

For someone to become a team member, they should already be a consistent,
positive, productive member of the community. Newcomers are encouraged to
become team members, but after they've shown a sustained interest in
engaging with the community. Moreover, team members should be interested in
**continuing their engagement** over a long-ish period of time, generally
putting in more time and effort than non-team members. This doesn't have to
mean contributing code - it can be assisting others in forums/issues, reviewing
pull requests, participating in team meetings, etc.

Any new team members must be "championed" by a pre-existing team member. This
is a person who recommends that the new person be invited to join the team.
This process takes the following steps:

1. The champion should first discuss internally with team members to get buy-
   in and ensure that there's general consensus before officially starting
   the process.
2. If there seems to be team consensus,
   the champion contacts the potential new team member and ask if they are
   interested. Don't forget to run them by the :ref:`binder-team-responsibilities`
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
member of the team. Copy and paste the checklist below into a new GitHub
issue and follow each step. Once all steps are completed, we can close the
issue and the team member is now ready to go!

.. code-block:: markdown

   **Membership**

   - [ ] Add them to the [binderhub google group](https://groups.google.com/forum/#!forum/binderhub-dev)
   - [ ] Add them to the [binderhub team in the github organization](https://github.com/orgs/jupyterhub/teams/binder-team)
   
   **Permissions**

   - [ ] Make sure they have permissions on the [google cloud projects](https://console.cloud.google.com/home/dashboard?project=binder-prod)
         (binder-prod, binder-staging, binder-sandbox)
   - [ ] Add them as collaborators on the repo2docker and BinderHub PyPI packages
   - [ ] Add them to the [jupyterhub team google drive](https://drive.google.com/drive/folders/0B8VZ4vaOYWZ3a2dyeEp6NzBKbnM?usp=sharing)
   
   **Learning**

   - [ ] provide an overview of areas where they can contribute? (e.g. docs, discourse / twitter, tackling issues, ...) 
   - [ ] overview of pr process? (e.g. when is it appropriate to merge a pr that you have reviewed? or what to expect when a pr of yours is being reviewed)
   
   **Community**

   - [ ] Add them to the [jupyterhub or binderhub team yaml files](https://github.com/jupyterhub/team-compass/tree/5d014f3af161e3abcf79c7adfb77620607929d77/docs/team)
   - [ ] Tell people in Discourse + Twitter about our awesome new community member
