# Pull request workflow

Our team practices should encourage transparency and collaboration, and reviewing one another's work is a great way to ensure that we share context and knowledge, and improve the codebase.
Our goals are to balance inclusive and transparent team practices with the reality that we are all asynchronous and don't want to pay a large coordination penalty for every change and decision.

**All changes to a JupyterHub repository should happen via Pull Requests**.
Any exceptions to this should be explicitly listed in team documentation.[^1]

[^1]: The only exception we can think of is when pushing a commit to `main` during a release, but we'll leave this open-ended just in case there are other cases where this is useful.

(prs:principles)=
## Principles to follow

- **Provide context**. Provide enough discussion and context sharing so that every team member understands the rationale for a change, even if they may not personally agree with it.
  The more complex or impactful a change is, the more time should be given to discuss and include the perspective of others.
- **Include others**. Actively invite participation and comments from others, especially if you think they are interested in the proposed change.
  Go out of your way to make it easy for others to participate, and make your best effort at incorporating suggestions and feedback from others.
  If a topic requires discussion, open an issue or a forum thread so that others can participate and align on an approach before diving into a code implementation.
  We often save a lot of time by having design-level discussion before we get to the Pull Request.
- **Link to discussions and context**. Almost any change should first be proposed in an issue, or in another space that is accessible to non-coders (like a forum post).
  A Pull Request should link to (and optionally close) any other locations where discussion happened.
  This gives each change more provenance and separates design from implementation.
- **Default to action**. We are an asynchronous and part-time team with a high level of trust for team members.
  It's OK if we accidentally merge something that introduces a mistake or a bug, we can always change it later.
  Default to moving forward if you believe it is the right time to merge something.
- **Use your best judgment**. We do not provide many strict rules and technical barriers because we trust team members to use their best judgment in reviewing and merging work.
  Do your best to live up to our team values and practices, and recognize that we all make mistakes.

## When to merge pull requests

- **Obvious and simple improvements** can be merged by any member of the {team}`Maintainer Team` even if it does not have a review.
  For example: clear bug fixes, typo corrections, etc.
  If it's straightforward, go ahead and merge it.
- **Straightforward and non-controversial PRs** with at least one approval from a {team}`Maintainer Team` member and no objections may be merged by anybody, anytime.
  If you approve the PR, go ahead and merge it!
  If you don't immediately merge it, provide a rationale for why not.
  If somebody else approves your PR and you think it's safe to merge, feel free to self-merge.
- **Complex or potentially controversial PRs** may be merged with at least one approval from a {team}`Maintainer Team` member, no objections from any team member, and after has been open for around five working days.
  Use your best judgment for how long to wait to ensure inclusive decision making process and be sure to [include others in discussion](prs:principles).
  The more complex, the more time you should give people.
  The more people agree, the more quickly you can safely merge.
- **Changes to team policies** may be merged with at least two approvals from {team}`JupyterHub Council` members, no objections from any team member, and has been open for around five working days (follow the same guidelines as above).
- **Proposals without consensus** may be merged if the {team}`JupyterHub Council` has majority agreement to merge, and if there have been at least five working days to discuss.

## What to look for in a review

As a team member, you're encouraged to help others contribute to the project
by reviewing their code, guiding them towards making a contribution and
improving it, and ultimately merging their contribution into the project.

Having merge rights is both a privilege and a responsibility - please be
thoughtful when using it! To that extent, here are a few guidelines when
deciding to merge things into one of our repositories:

- **It's quality code**. We know this is somewhat subjective, but
  ensure that the code is well-organized and thoughtfully-written, that any
  new features are documented, and that it abides by best-practices in Python,
  JavaScript, etc.
  Do not nit-pick stylistic preferences, but if you genuinely think there's a clear way to improve the code, please make suggestions.
- **There are tests and they pass**. We try not to merge any new features (or
  bugfixes!) without adding tests for them. It's easy to consider something
  minor enough that it doesn't warrant a test, but try to avoid doing this!
  Adding tests usually only takes a moment, and our future selves will thank
  us for it later.
- **There is documentation**. If we're changing or adding functionality, ensure that there is documentation describing the change to others.
  Functionality that isn't documented is much less discoverable and maintainable.
- **The code is secure**. We must avoid introducing changes that may lead to a security vulnerability.
  If your code is complicated please include comments to ensure future maintainers do not inadvertently introduce a new vulnerability.
- **There's been enough time for discussion**. We're an open
  community with an inclusive decision-making process. This means that
  sometimes we need to slow down to make sure others have a chance to
  review and provide their thoughts on changes. There's no hard rule for
  this, but try to make sure people have a chance to weigh in. Consider
  pinging people that you think might be interested in a question, and
  give it a few extra days before merging if you think a topic will be
  complex enough to warrant discussion.

That said, **don't be afraid to merge!** If you think a change is really complex or potentially controversial, give it some time, but for most changes it is fine to just go ahead and merge.
Again, we trust your judgment, and we don't want these guidelines to become a burden that slows down development.
