# Weekly reports archive

This is an archive of weekly reports.

## 2018-02-05

### Actions

1. Help or discussion needed; Agenda Items for Monthly Meeting

- 1.1 Open PRs
  - [CH] We should discuss Matthias' PR about Federation, with the goal of having a clear path forward to merging! ([PR](https://github.com/jupyterhub/binderhub/pull/274))

- 1.2 Open issues
  - [CH] If anybody would like access to any of the accounts they don't have access to, please say so and we'll get you connected! (e.g. twitter, google analytics, pip rights, etc) [issue](https://github.com/jupyterhub/team-compass/issues/20)
  - [CH] From last meeting: come up with rough guidelines for blog post / communications (e.g. don't post too close to one another) ([issue](https://github.com/jupyterhub/team-compass/issues/22))
  - [CH] Discuss merging the BinderHub helm chart into JupyterHub + maybe some docs. ([issue](https://github.com/jupyterhub/binderhub/issues/435))

### Organization highlights

- Min + Chris are going to France for a Jupyter Days event! There will be a talk of some kind
- The organizers are interested in setting up a JupyterHub for a cluster of French universities, we'll hopefully work with them while we're there.

### Thanks, Things to Celebrate, and anything else

- Binder made it into Nature! Thanks to Carol + Tim for being awesome and representing the project :-) ([link](https://www.nature.com/articles/d41586-018-01322-9))
- The Berkeley Data 8 class connected their online textbook with Binder, and [twitter was really excited about it](https://twitter.com/choldgraf/status/956582139897630720)

## 2018-01-29

### Open issues

- [Highlighting binders of note?](https://github.com/jupyterhub/binder/issues/49)
    - Chris gives Jessica access to GA
    - starting point for this is popular repos from GA

### Next actions (team)

- Please add yourself to the [Team Organization list](https://github.com/jupyterhub/team-compass)
- Come up with rough guidelines for blog post / communications (e.g. don't post too close to one another)
- Figure out how to remove tracking all subdomains of mybinder.org on GA
- List all potential blogpost that should be publish and blog.jupyter.org create drafts for them with date ranges.
    - Binder browser extension (Matthias)
    - JuyterDays France (Sylvain, Loic?)
    - JupyterLab release (Brian)
    - What's new in Binder / Happy New Year (Chris H)
    - JupyterDays CFP (Brian/Fernando)
- Follow up on Matthias' suggestion to come up with a list of access/keys/etc. by repo/service/etc. so that where information is stored and who has access
    - Read the docs
    - PyPI
    - Analytics
- check out and improve the [ISSUE_TEMPLATE.md](https://github.com/jupyterhub/binder/blob/master/.github/ISSUE_TEMPLATE.md) for Binder vs binderhub issues. Proposed additions:
    - binder is for users
    - binderhub is about the software
- Review and improve step by step deployment checklist for mybinder-deploy
    - review which steps can be automated
    - Carol will create an incident report from my experience this morning. The goal is to increase confidence in deploy process for those that are not deploying on a regular basis. [COMPLETED]
    - when to deploy to mybinder after merging into binderhub (releases of binderhub would mitigate this)
    - review https://github.com/jupyterhub/mybinder.org-deploy/issues/225
    - can we create more visibility into what is working/not working when we made a deployment that isn't working

### Team News and Informational items

- February 2018 Video Call scheduled for February 8, 2018 6pm Zurich time. [Details](https://github.com/jupyterhub/team-compass/issues/14)
- Chatted with Sylvain + Loic in France, they're interested in a JupyterHub for French unis.
    - French HPC/Loic have spent some effort in setting up something that looks very much like binder, interested in maybe using binder/jupyterhub
    - Hosting on OVH (something like google cloud/AWS but more Euro).
    - Some 'JupyterHub federation' similar to berkeley MOOC work
- Prepared a draft blog post (blog.jupyter.org) for the MyBinder browser extension.
    - try to avoid conflicts with other posts
    - to get a list of other posts ask steering council/mailing list to find out what other sub-projects are doing
    - raise as an issue on the weekly Jupyter meeting under communications (Carol) **COMPLETED**

### Organization highlights

- [Reaching out to JOSS](https://github.com/openjournals/joss/issues/360) **COMPLETED**
  - Tim is reviewing a paper and will mention that it would have been nice to have a binder link
- Ask eLife if they want to fund a project to integrate with binder for their "archive to GitHub" idea?
  - https://github.com/elifesciences-publications
  - https://elifesciences.org/inside-elife/dbcb6949/forking-software-used-in-elife-papers-to-github
  - Tim will send a short email to Naomi to see what they think
- Jupyter Days event coming up in March in France.
    - Conversation with Sylvain and Loic
    - Date early March (5th??)
    - 300 to 500 attendees
    - Prepare a blog post annouce (ask Sylvain)
    - Chris might be in the area, Min will probably go, who else is interested?
- JupyterCon CFP website online (restricted access) let's not try to cram blog post too close to the CFP annouce.
- Hackathon with Data Carpentry at BIDS next week (Jan 9th and 10th), Chris H will work on Binder teaching material.

### BinderHub projects

- Security update for meltdownattack.com performed (Thanks Yuvi)
- Prod cluster scaled down to 3 nodes and switched from n1-standard class nodes (equal CPU + memory ratio) to n1-highmem (more memory than CPU) based on our usage metrics (as part of meltdownattack.com fix)
- npm refactor merged (yay @minrk! @rgbrk & other nteract folks)
- playground.mybinder.org now redirects to play.nteract.io (yay cross-promotion) (this was down for Chris H today. Others? (is down for me too, should check with nteract folks)) I just checked again and it's back up - CH
    - Works for Matthias, Tim, Chris. Is that exectuing on same machines as MyBinder.org ? (nope it's not)
- Working on fixing binder badge being blocked by privacy badger (https://github.com/jupyterhub/binderhub/issues/379)
    - our badge.svg is served from same host as some cookies we set which triggers a tracking warning
    - now served from static.mybinder.org/badge.svg but apparently still triggers warning
    - how to respect DNT headers?
    - fix that the GA cookies is set on *.mybinder.org not just the top domain
- Loading page PR is almost ready (https://github.com/jupyterhub/binderhub/pull/384)
    - this is better than watching a washing machine
    - Looks like Tony Stark Visor in his Iron Man suit.
    - Matthias has one concern about css animations power draining.
- Chris H will give a go at the BinderHub setup instructions w/ a more recent dev version to make sure they're still correct.
- Matthias will rebase the [Federation PR.](https://github.com/jupyterhub/binderhub/pull/274) Thoughts on it ?
    - lots of details to work out, but let's label it as a prototype
    - how do we keep versions in sync, how to handle when they are out-of-sync, etc
    - do we create a separate prototype service from mybinder.org
    - look into what the grant covers related to federation
    - which privacy policies apply when on a federated deployment
    - vision for federation blog post to see what others think?
        - make sure users see who is providing the CPU to them
    - step 1 before pushing the federation idea is to start having good releases that users can rely on
- More eyes on this deployment process proposal https://github.com/jupyterhub/mybinder.org-deploy/issues/225

### 5.3 JupyterHub projects

- Working with Matthew Rocklin on [daskernetes](https://github.com/yuvipanda/daskernetes) that helps integrate kubernetes + dask for use on z2jh. They have a demo on 6th.
- [Team-Compass](https://github.com/jupyterhub/team-compass) added to track our virtual meetings and team metrics
    - [open issue and PR totals by repo](https://github.com/jupyterhub/team-compass#issues-and-pr-tracking)
    - list of team members begun - please add yourself to the README
- Work this weekend and next week on updating Ansible deployment with nbgrader and AWS for Cal Poly Data Science course
- JupyterHub session cookie implemented (https://github.com/jupyterhub/jupyterhub/pull/1577)
- external OAuth (and token auditing) almost ready: https://github.com/jupyterhub/jupyterhub/pull/1590
- http://github.com/yuvipanda/jupyterhub-ltiauthenticator exists, can integrate with Blackboard / Canvas / EdX / etc

### Related projects

- part of making a repo2docker release a pypi account was created (mybinderteam), ask Tim to share password/login via lastpass if you are interested. It should be connected to the gmail account as well. ([#136](https://github.com/jupyter/repo2docker/issues/136#issuecomment-343586238))
- sphinx-gallery PR is now merged https://github.com/sphinx-gallery/sphinx-gallery/pull/244
    - huge PR!
    - can we reuse a running pod for the same user instead of launching a new one?
        - there is an issue somewhere on exactly this topic, add link

## 2017-12-25 

### Organization highlights

*Communications, Social Media, Conferences, Outreach*

- [Reaching out to JOSS](https://github.com/openjournals/joss/issues/360) **COMPLETED**

### BinderHub projects

- network firewalls/throttling landing on mybinder.org this week, so keep an eye out for issues
- KubeSpawner update

### JupyterHub projects

- KubeSpawner 0.7.1 release
- [Team-Compass](https://github.com/jupyterhub/team-compass) added to track our virtual meetings and team metrics 
    - [open issue and PR totals by repo](https://github.com/jupyterhub/team-compass#issues-and-pr-tracking)
    - list of team members begun - please add yourself to the README

### Related projects

- part of making a repo2docker release a pypi account was created (mybinderteam), ask Tim to share password/login via lastpass if you are interested. It should be connected to the gmail account as well. ([#136](https://github.com/jupyter/repo2docker/issues/136#issuecomment-343586238))


### Next actions (team)

- Please add yourself to the [Team Organization list](https://github.com/jupyterhub/team-compass)

### Thanks, Things to Celebrate, and anything else

- Thanks Tim for submitting a Moz Science mini grant proposal.
    - [Review and provide thoughts on Etherpad](https://public.etherpad-mozilla.org/p/moz-mini-grant-binder-2017) for a proposal Tim is thinking about submitting to Mozilla mini grant to fund ~3 one day events around “using binder to do cool things” in Europe.
    - [Moz Mini Grant](https://public.etherpad-mozilla.org/p/binder-moz-mini2017) submitted.
- Welcome Gladys Nalvarte to the team! Great to see you on board as an intern at Simula. Congrats on the PRs. Please let us know if you have questions :D
- Congrats to Yuvi Panda on his KubeCon talk!
- http://carreau.github.io/posts/31-open-in-binder-browser-extension.html !!!
- Congrats to the entire team for the very successful launch of mybinder.org and write up in Jupyter Blog and eLife.

## 2017-12-17

### Team News and Informational items

- Hired Gladys Nalvarte as intern at Simula. Getting to know the codebase, tools involved. Made a couple of PRs already! **Welcome Gladys! Please let us know if you have questions :D**

### Organization highlights

- Created new Twitter and Google group: **mybinderteam** **COMPLETED**
- Binder 2.0 blog posts nearly ready, Chris has been awesome wrangling this, lots of little things left to do, please help, https://github.com/jupyterhub/binder/issues/22 **COMPLETED**
- Tim is thinking about submitting a proposal to [Mozilla mini grant](https://science.mozilla.org/blog/2018-mini-grant-rfp/) to fund ~3 one day events around "using binder to do cool things" in Europe. [Etherpad with thoughts/details](https://public.etherpad-mozilla.org/p/moz-mini-grant-binder-2017) **REQUEST FOR INFORMATION**
- [Reaching out to JOSS](https://github.com/openjournals/joss/issues/360) **STATUS? Completed?**

### BinderHub projects

- network firewalls/throttling landing on mybinder.org this week, so keep an eye out for issues
- KubeSpawner update
- We need to get grafana back up and running for monitoring +1 (landed! https://grafana.mybinder.org) **COMPLETED?**

### JupyterHub projects

- KubeSpawner 0.7.1 release
- [Team-Compass](https://github.com/jupyterhub/team-compass) added to track our virtual meetings and team metrics 
    - [open issue and PR totals by repo](https://github.com/jupyterhub/team-compass#issues-and-pr-tracking)
    - list of team members begun - please add yourself to the README

### Related projects

- part of making a repo2docker release a pypi account was created (mybinderteam), ask Tim to share password/login via lastpass if you are interested. It should be connected to the gmail account as well. ([#136](https://github.com/jupyter/repo2docker/issues/136#issuecomment-343586238))

### Open issues

- [Review and provide thoughts on Etherpad](https://public.etherpad-mozilla.org/p/moz-mini-grant-binder-2017) for a proposal Tim is thinking about submitting to Mozilla mini grant to fund ~3 one day events around “using binder to do cool things” in Europe.
    - [Moz Mini Grant](https://public.etherpad-mozilla.org/p/binder-moz-mini2017) submitted.

### Next actions (team)

- Let's tweet from Jupyter (and give Ana an FYI) to publicize the browser extension for Firefox in [Matthias' blog post](http://carreau.github.io/posts/31-open-in-binder-browser-extension.html) **COMPLETED**
- Please add yourself to the [Team Organization list](https://github.com/jupyterhub/team-compass)

### Thanks, Things to Celebrate, and anything else

- Welcome Gladys Nalvarte to the team! Great to see you on board as an intern at Simula. Congrats on the PRs. Please let us know if you have questions :D
- Congrats to Yuvi Panda on his KubeCon talk!
- http://carreau.github.io/posts/31-open-in-binder-browser-extension.html !!!
- Congrats to the entire team for the very successful launch of mybinder.org and write up in Jupyter Blog and eLife.

## 2017-12-04

### Team News and Informational items

- Hired Gladys Nalvarte as intern at Simula. Getting to know the codebase, tools involved. Made a couple of PRs already!

### Organization highlights

- Created new Twitter and Google group: **mybinderteam**
- Binder 2.0 blog posts nearly ready, Chris has been awesome wrangling this, lots of little things left to do, please help, https://github.com/jupyterhub/binder/issues/22
- Tim is thinking about submitting a proposal to [Mozilla mini grant](https://science.mozilla.org/blog/2018-mini-grant-rfp/) to fund ~3 one day events around "using binder to do cool things" in Europe. [Etherpad with thoughts/details](https://public.etherpad-mozilla.org/p/moz-mini-grant-binder-2017)
- [Reaching out to JOSS](https://github.com/openjournals/joss/issues/360)

### BinderHub projects

- network firewalls/throttling landing on mybinder.org this week, so keep an eye out for issues
- KubeSpawner update
- We need to get grafana back up and running for monitoring +1 (landed! https://grafana.mybinder.org)

### JupyterHub projects

- KubeSpawner 0.7.1 release

### Related projects

- part of making a repo2docker release a pypi account was created (mybinderteam), ask Tim to share password/login via lastpass if you are interested. It should be connected to the gmail account as well. ([#136](https://github.com/jupyter/repo2docker/issues/136#issuecomment-343586238))

### Open issues

- https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/271 PyCon tutorials, Tim thinks this is in limbo, what is the plan? Deadline fast approaching. The tutorial deadline has passed (Carol) - **RESOLVED**.


### Next actions (team)

- Let's tweet from Jupyter (and give Ana an FYI) to publicize the browser extension for Firefox in [Matthias' blog post](http://carreau.github.io/posts/31-open-in-binder-browser-extension.html)

### Thanks, Things to Celebrate, and anything else

- http://carreau.github.io/posts/31-open-in-binder-browser-extension.html !!!
- Congrats to the entire team for the very successful launch of mybinder.org and write up in Jupyter Blog and eLife.

## 2017-11-26

### Organization highlights

- Created new Twitter and Google group: **mybinderteam**
- Binder 2.0 blog posts nearly ready, Chris has been awesome wrangling this, lots of little things left to do, please help, https://github.com/jupyterhub/binder/issues/22

### Open issues
- https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/271 PyCon tutorials, Tim thinks this is in limbo, what is the plan? Deadline fast approaching.

### Thanks, Things to Celebrate, and anything else

- http://carreau.github.io/posts/31-open-in-binder-browser-extension.html !!!

