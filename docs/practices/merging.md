# Merging and reviewing practices

Our team practices should encourage transparency and collaboration, and reviewing one another's work is a great way to ensure that we share context and knowledge, and improve the codebase.
Our goals are to balance inclusive and transparent team practices with the reality that we are all asynchronous and don't want to pay a large coordination penalty for every change and decision.

**All changes to a JupyterHub repository should happen via Pull Requests**.
Any exceptions to this should be explicitly listed in team documentation.

## Guidelines for merging pull requests

- **Default to action**. We are an asynchronous and part-time team with a high level of trust for team members.
  It's OK if we accidentally merge something that introduces a mistake or a bug, we can always change it later.
  Default to moving forward if you believe it is the right time to merge something.
- **Use your best judgment**. We do not provide many strict rules and technical barriers because we trust team members to use their best judgment in reviewing and merging work.
  Do your best to live up to our team values and practices, and recognize that we all make mistakes.
- **Link to discussions and context**. Almost any change should first be proposed in an issue, or in another space that is accessible to non-coders (like a forum post).
  A Pull Request should link to (and optionally close) any other locations where discussion happened.
- **Include others**. Actively invite participation and comments from others, especially if you think they are interested in the proposed change.
  Go out of your way to make it easy for others to participate, and make your best effort at incorporating suggestions and feedback from others.
- **Don't surprise people**. We pay a team penalty when somebody changes something that wouldn't be expected, especially if it is unwelcome.
  We should provide enough discussion and context sharing so that every team member understands the rationale for a change, even if they may not personally agree with it.

## When to merge a pull request

- **Obvious and simple improvements** can be merged by any member of the {team}`Maintainer Team` even if it does not have a review.
  For example, clear bug fixes, typo corrections, etc.
  We recommend leaving PRs open for at least one working day, but if you really wish to self-merge, go for it.
- **Straightforward and non-controversial PRs** with at least one approval from a {team}`Maintainer Team` member and no objections may be merged by anybody, anytime.
  **Self-merging is encouraged** in these cases.
- **Complex or potentially controversial PRs** may be merged with at least one approval from a {team}`Maintainer Team` member, no objections from any team member, and after has been open for around five working days.
  Use your best judgment for how long to wait to ensure inclusive decision making process.
  The more complex, the more time you should give people.
  The more people agree, the more quickly you can safely merge.
- **Changes to team policies** may be merged with at least two approvals from {team}`Steering Council` members`, no objections from any team member, and has been open for around five working days (follow the same guidelines as the guideline above).
- **Proposals without consensus** may be merged if the {team}`Steering Council` has majority agreement to merge, and if there have been at least five working days to discuss.

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
  minor-enough that it doesn't warrant a test, but try to avoid doing this!
  Adding tests usually only takes a moment, and our future selves will thank
  us for it later.
- **There is documentation**. If we're changing or adding functionality, ensure that there is documentation describing the change to others.
  Functionality that isn't document is much less discoverable and maintainable.
- **There's been enough time for discussion**. We're an open
  community with an inclusive decision-making process. This means that
  sometimes we need to slow down to make sure others have a chance to
  review and provide their thoughts on changes. There's no hard rule for
  this, but try to make sure people have a chance to weigh in. Consider
  pinging people that you think might be interested in a question, and
  give it a few extra days before merging if you think a topic will be
  complex enough to warrant discussion.
- **Don't be afraid to merge!** We know this is a bit counter-intuitive
  given what we just said, but don't be afraid to merge new code. If you
  think a change is really complex or potentially controversial, give it
  some time, but for most changes it is fine to just go ahead and merge.
  Again, we trust your judgment, and we don't want these guidelines to become
  a burden that slows down development.
