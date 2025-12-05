---
title: September 2023
---

# Discussion and plans for Maintenance of the JupyterHub GitHub org

Date: 2023-09-29

Context: [team-compass #680](https://github.com/jupyterhub/team-compass/issues/680) following up from [September Collab Cafe discussion](https://jupyterhub-team-compass.readthedocs.io/en/latest/meetings/collab-cafe/2023.html#lowest-level-of-maintenance-for-jupyterhub-org-project-s)

Participants:

- Sarah Gibson
- Yuvi Panda
- Erik Sundell (consideRatio)
- Min

Facilitator: Sumana Harihareswara ([external consultant](https://www.changeset.nyc/))

To consider and develop:

- Some strategies and processes for maintaining multiple repositories in the JupyterHub organisation
- Some levels of maintainership we want to commit to
- The archetypes of repositories that fit into the maintainership levels (Some example archetypes come from Mozilla/Open Tech Strategies research; [version 2 of their findings](https://opentechstrategies.com/archetypes-files/open-source-archetypes-v2.pdf) is less detailed and not as easy to use as [version 1](https://blog.jwf.io/wp-content/uploads/2020/11/Open-Source-Archetypes-Mozilla-Open-Tech-Strategies-May-2018.pdf))
- To sketch some proposals to be asynchronously discussed/voted on afterwards

Discussion notes:

Erik mentions: having clearer expectations would help him worry less & work more efficiently, be more comfortable.

Sumana's summary: consensus (obvious) path forward
<https://github.com/jupyterhub/team-compass/issues/519> one org carries a particular level of 'branding' that implies a certain standards, create a second org with different standards, structure that conveys level of maintenance, likelihood of releases/PR review etc. Question: consider this approach that most people agree with?

Erik: Onboard, but it will be stressful if it doesn't come with clear expactations on how to use it. Set it up sufficiently clear so that 'breaking changes' don't occur

Min: 1st order prob: repos at variety of expectations within JH org currently. Need to communicate mult levels of expectations clearly. Not currently being done!

2nd order prob: \[choice of implementation approaches available, e.g., labels, orgs.\]

Yuvi: agrees. jh-contrib org would be easy next step. Also need to clarify how GitHub works \[?\] re namespacing

useful frame: BELONGING & validation. Personal experience: Yuvi's repo moving into JH org: marker, could say to self, "I am a part of JH community". Namespacing -> REAL social effects. Can say "I am a core contributor to JupyterHub". FLOSS communities need to grow to survive/persist, to make up for attrition. Thus, Yuvi has erred in favor of helping contributors get their work into the JH org.

If we have the mentorship bandwidth to help with this approach, it works! But we don't always have that. lti-authenticator as example, fell through the cracks, and other people had to pick up the pieces

how does one believe/perceive they are part of JH community? there are levels to it.... Very important to Yuvi; let's not just propagate our own assumptions to others' experiences

suggests: guidelines/criteria: what it means for a repo to be \[here\] vs \[there\], tie to maintenance levels? people who are committed over a period of time? + pathway for things to go from one to the other AND VICE VERSA; we can prevent perception of lower prestige in one versus the other

important for people contributing to JH-contrib stuff to FEEL as much as possible equals to people in JH \[main\]

the ceremony of getting The Commit Bit is meaningful to individuals. Underappreciated in JupyterHub. Yuvi would like an equivalent to <https://www.mediawiki.org/wiki/How_to_become_a_MediaWiki_hacker>

More people are now reliant on JH/Jupyter than in the past. Let's celebrate this as a result of success! So we could in fact add a new org called JH Core (or something else), for things that need to be held to a new standard. Promote the essential, higher level of care stuff for a stricter set of requirements. Not rejecting anything for "not being good enough". Emotionally + logistically easier.

Sumana: Whom else ought to be consulted on this decision?

- Simon (manics)
- Georgiana (georgianaelena)
- the Council (collective authority on JupyterHub)
- the people currently maintaining or contributing to repos that may be moved

Erik: might also still be room for both jh-contrib type org AND a new jh-critical org, to make a place for encouraging enthusiastic new folks to be seen, commit, collaborate, etc. breeding ground, 0 expectations

Min & Sumana: some levels to consider:

1. user expectations
1. contributor expectations
1. maintainer expectations
1. funder expectations
1. legal compliance???? expectations

Potential approaches:

1. Create "jh-contrib" org
1. Use tags/labels/etc in our existing single org
1. Create "jh-critical" org

Erik: wants to make sure he will still get notified about relevant issues/questions, but not cast that scope too wide (and this affects implementation choice).

Min: when a repo might not be meeting expectations, let's not stress out its maintainer, or Erik! All that's in this one org used to be 1 repo, and Min could keep up with all of it, daily. We're now at a level where we, as a team, are collectively responsible. No one individual is responsible for everything. Expectations are on the PERSON level as well! \[others agree with this point\] If you see a gap, raise an issue that the expectations are not being met, but it's not necessarily YOUR JOB, Erik, Yuvi, or Sarah, to get that gap FIXED. Standards can still be high!

Sumana: medical example  - Switch by Heath brothers?? group/team care, not personal continuity of care

Sarah: there are some repos that everyone needs to worry about

How do we bring people into those packages? My commit history is all docs/no tech early on.... let's give people ramps in ... new contributor onboarding into essential/critical repositories, even if they are not commit bit holders

also, definition of contributor vs maintainer vs councilmember is fuzzy!

Prior art:

What wikimedia did in the past. 2003 - mediawiki didn't have a name, was just undifferentiated scripts. Ori talked about the parser 'growing organically like mold on a shower curtain'. Eventually, cell differentiation into organs happened - we developed 'tiers'. Here is 'mediawiki-core', and that is a 'unified piece of software', and there is a 'high bar' for getting stuff into it. 120 known maintained extensions, and 60 were things that ran on wikimedia servers and so they had to meet higher standards (for security, etc) (<https://www.mediawiki.org/wiki/Writing_an_extension_for_deployment>). Core idea of 'who gets to commit to mediawiki-core' is a high bar. As a community metric, WMF wanted to make it easier for people to make social spaces - to feel encouragement, to be able to do things together, feel validation and belongingness, in a space with similar levels of technical infrastructure, but with **far less gatekeeping**. In the wikimedia ecosystem, there's the API to mw - tremendous amount of softwware that volunteers wrote in that world, was 'other stuff', not core PHP code. Javascript that ran on userscripts, and individual users can 'add on' when you log in to mediawiki ("Gadgets" or User Scripts). There's a central repository for that. What are the tiers that support gadgest? Look at what are the standards for *enabling default gadgets*. Things that interact with API (tools & bots), some are more 'canon' and some are not (IABot for example). We can look at what are the guidelines for adoption.

Other prior art is:

- Checklist for getting an extension deployed on Wikimedia <https://www.mediawiki.org/wiki/Writing_an_extension_for_deployment>
- <https://cran.r-project.org/web/packages/policies.html> CRAN guidelines
- CNCF "Graduation" criteria <https://github.com/cncf/toc/blob/main/process/graduation_criteria.md>
- Debian guidelines for package acceptance, including tiers (default install)
- Addon guidelines in browser stores such as Chrome and Firefox, what they want / need for promotion/marketing, 'verified', etc
- 7 grade system for 'how maintained is this system of software' in the packaging ecosystem (SPDX standard)
- Carpentries has [incubator](https://carpentries-incubator.org)
- CNCF incubation graduation criteria (link below), e.g., "evidence of usage at least 3 independent people/places", "# of active committers"

What are our maintenance criteria / expectations?

- documentation
- clear procedures for changelog, releases
- standards like pre-commit / auto-formatting
- We have some [_suggested_  standards](https://jupyterhub-team-compass.readthedocs.io/en/latest/practices/repository-code-standards.html)
- jupyterhub [repo template](https://github.com/jupyterhub/jupyterhub-python-repo-template)
- security vulnerability upkeep \[prior art: [Tidelift lifter agreement](https://support.tidelift.com/hc/en-us/articles/4406288074260-Lifter-tasks-overview#lifter-tasks-overview-0-0)\]

Next steps:

- Follow up on support tiers at e.g. wikimedia & other prior art
- Try to figure out what our buckets should be (probably 2-3!) Sumana suggests timeboxing at 5 hours total work
- Yuvi owns this, Sarah is advising/helping, Yuvi will report back next Friday Oct 6th, via the GitHub issue <https://github.com/jupyterhub/team-compass/issues/519>
- Sarah: update <https://github.com/jupyterhub/team-compass/issues/519> and <https://github.com/jupyterhub/team-compass/issues/680> with link to these notes.
