.. _binder-subdomains:

Subdomains on mybinder.org
==========================

The following section describes how the project allocates sub-domains of
mybinder.org to other BinderHubs.

There are other subdomains of mybinder.org which are used by the project itself
which this document says nothing about how or why those are allocated.

Allocating a subdomain of mybinder.org serves the purpose of:

- making the BinderHub it points to easier to discover;
- letting the user know which BinderHub they are being served by; and
- recognising the BinderHub and its operators as a supporter of the project.

Names should be short and memorable. They should reflect the name of the entity
operating the BinderHub. For example a hub operated by "Rubber Duck Inc" should
use their preferred company name acronym or `rubberduck.mybinder.org`. It
should not be `woodenhorse.mybinder.org` or something similarly unrelated.

The following paragraphs describe the spirit and "should do's" under which
Project Binder will consider allocating a sub-domain to a BinderHub.

Project Binder expects that organisations of the following kind will want to
apply for a sub-domain and become partners of the Binder project:

- cloud providers
- universities
- research labs
- government agencies

The BinderHub should be open to the general public, not require any logins,
not contain tracking beyond the level of the general mybinder.org site, and
give no preference to certain repositories or workloads.

The BinderHub should closely track the versions of software deployed on the
main mybinder.org cluster so that repositories that work on one BinderHub also
work on others.

The BinderHub should maintain the look and feel of a stock BinderHub. A subtle
mention of who is operating this hub and/or sponsoring the resources is welcome.
The hub should not include adverts, cryptominers or other malware in pages it
serves.

The operator has to be committed to and able to operate a public BinderHub for a
significant amount of time (at least a few months).

The mission of the operator should be aligned with the mission of the Binder
Project laid out in :ref:`binder-governance`. By allocating a sub-domain the
project wants to recognise those who publicly support the project in order
to advance our mission.

If the BinderHub stops being functional, or is deemed to not behave in an
acceptable way, the subdomain may be reclaimed at any time, redirecting back
to the root mybinder.org.

If you would like to obtain a sub-domain that points at your public BinderHub
please `open a new issue on our repository <https://github.com/jupyterhub/team-compass/issues/new>`_
mentioning who you are, what you do and where we can find your BinderHub.

We look forward to new partnerships and your interest in helping advance the
mission of Project Binder.
