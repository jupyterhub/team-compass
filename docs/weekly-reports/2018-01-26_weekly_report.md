# JupyterHub and BinderHub Team Meeting

**Goal: Continuous improvement.**

*The detailed sections are for organization of team information, communication consistency, and are designed to motivate the team's next actions.*

#### Opening Date: 01 Jan 2018

#### Closing Date: 29 Jan 2018

#### Next monthly meeting: [February 8, 2018 6pm Zurich time](https://github.com/jupyterhub/team-compass/issues/14)

[Link to prior week's virtual meeting report](https://github.com/jupyterhub/team-compass/tree/master/docs/weekly-reports)

---
## Actions

## 1. Help or discussion needed; Agenda Items for Monthly Meeting

*Items that you wish to raise for team input. Include Project Name.*
-
-

### 1.1 Open PRs

-
-

### 1.2 Open issues

- [Highlighting binders of note?](https://github.com/jupyterhub/binder/issues/49)
    - Chris gives Jessica access to GA
    - starting point for this is popular repos from GA


## 2. Decisions needed

-
-

## 3. Next actions (team)

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
-
-

---

# News, Information, and Thanks

## 4. Team Metrics

*Generated GitHub reports summary*

[Link to JupyterHub/Binder PR metrics](https://github.com/willingc/pulse_news/blob/master/2018-01-09_jupyterhub.md)

## 5. Team News and Informational items

*Share items (partnerships, important conversations, design considerations, something fun, something that annoyed you). If you have it, please link to a GitHub issue)*

- February 2018 Video Call scheduled for February 8, 2018 6pm Zurich time. [Details](https://github.com/jupyterhub/team-compass/issues/14)
- Chatted with Sylvain + Loic in France, they're interested in a JupyterHub for French unis.
    - French HPC/Loic have spent some effort in setting up something that looks very much like binder, interested in maybe using binder/jupyterhub
    - Hosting on OVH (something like google cloud/AWS but more Euro).
    - Some 'JupyterHub federation' similar to berkeley MOOC work
- Prepared a draft blog post (blog.jupyter.org) for the MyBinder browser extension.
    - try to avoid conflicts with other posts
    - to get a list of other posts ask steering council/mailing list to find out what other sub-projects are doing
    - raise as an issue on the weekly Jupyter meeting under communications (Carol) **COMPLETED**

### 5.1 Organization highlights

*Communications, Social Media, Conferences, Outreach*

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

### 5.2 BinderHub projects

*BinderHub, mybinder-deploy, helm charts, binder-examples*

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

*JupyterHub, authenticators, spawners, configurable-http-proxy, zero to jupyterhub*

- Working with Matthew Rocklin on [daskernetes](https://github.com/yuvipanda/daskernetes) that helps integrate kubernetes + dask for use on z2jh. They have a demo on 6th.
-
- [Team-Compass](https://github.com/jupyterhub/team-compass) added to track our virtual meetings and team metrics
    - [open issue and PR totals by repo](https://github.com/jupyterhub/team-compass#issues-and-pr-tracking)
    - list of team members begun - please add yourself to the README
- Work this weekend and next week on updating Ansible deployment with nbgrader and AWS for Cal Poly Data Science course
- JupyterHub session cookie implemented (https://github.com/jupyterhub/jupyterhub/pull/1577)
- external OAuth (and token auditing) almost ready: https://github.com/jupyterhub/jupyterhub/pull/1590
- http://github.com/yuvipanda/jupyterhub-ltiauthenticator exists, can integrate with Blackboard / Canvas / EdX / etc

### 5.4 Related projects

*repo2docker, nbgrader, others*

- part of making a repo2docker release a pypi account was created (mybinderteam), ask Tim to share password/login via lastpass if you are interested. It should be connected to the gmail account as well. ([#136](https://github.com/jupyter/repo2docker/issues/136#issuecomment-343586238))
- sphinx-gallery PR is now merged https://github.com/sphinx-gallery/sphinx-gallery/pull/244
    - huge PR!
    - can we reuse a running pod for the same user instead of launching a new one?
        - there is an issue somewhere on exactly this topic, add link


## 6. Thanks, Things to Celebrate, and anything else

-
-

---

# Notes about this document

- Monthly team meeting agenda items should be placed in section 1.

---
**Do not edit below**

*Outline template for meetings*

## Actions

- 1. Help or discussion needed; Agenda Items for Monthly Meeting
        - 1.1 Open PRs
        - 1.2 Open issues

- 2. Decisions needed

- 3. Next actions (team)


## News, Information, and Thanks

- 4. Team Metrics
- 5. Team News and Informational items
        - 5.1 Organization highlights
        - 5.2 BinderHub projects
        - 5.3 JupyterHub projects
        - 5.4 Related projects (repo2docker, nbgrader, others)

- 6. Thanks, Things to Celebrate, and anything else
