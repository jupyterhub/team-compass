(collab-cafe:facilitator-checklist)=
# Facilitator Checklist for Collaboration Cafes

This document provides a list of actions for a facilitator to take, and when, when running a Collaboration Cafe.

All links for running the cafe will be in a GitHub issue that should be created [after the previous meeting](collab-cafe:facilitator-checklist:after).

## Before the Meeting

**1 week before:**

- Post a comment on the issue in the Team Compass repo reminding folk that the meeting is one week away
- _TBA: Any updates to announcements posted in other spaces, e.g., Discourse, Zulip, Mastodon, etc._

**1 day before:**

- Post a comment on the issue in the Team Compass repo reminding folk that the meeting is the next day
- _TBA: Any updates to announcements posted in other spaces, e.g., Discourse, Zulip, Mastodon, etc._

## During the Meeting

```{admonition} Jitsi tip
:class: tip
If you join the jitsi link a few minutes before the meeting starts, you'll see a "Waiting for the Moderator to start the meeting" message. You can claim moderator status by signing in (using GitHub will suffice). You can then manage breakout rooms and such.
```

- Welcome everyone and remind them that the meeting is being held under [Jupyter's Code of Conduct](https://jupyter.org/governance/conduct/code_of_conduct.html)
- Encourage attendees to sign their name into the shared document and add any agenda items they'd like to discuss
- Ask for a volunteer to act as the primary note taker, but emphasise that notes are collaborative and all attendees should add to them, especially when dealing with complex topics
- Work your way through the shared document, starting with intros and celebrations before moving into the main agenda
    - Try to ensure everybody who wishes to gets an opportunity to speak. Keep an eye on the Raised Hands in the meeting.
    - Try to keep an eye on timing so that all the topics can be covered without overrunning. This may mean interrupting some discussions and suggesting they be continued asynchronously (Zulip, Discourse, or GitHub are good places to point folk to).
    - Make sure to leave time for any questions before moving into the next agenda item.
- To close out the meeting, thank everyone for attending and remind them of the timezone of the next meeting.

(collab-cafe:facilitator-checklist:after)=
## After the Meeting

- Archive the shared document into the Team Compass repo
    - https://github.com/jupyterhub/team-compass/tree/main/docs/meetings/collab-cafe
        - 1 file per year
        - The files have the meeting notes in reverse chronological order - so paste the new notes in the top of the file!
        - Copy the attendee list, celebrations (if not empty) and the agenda
        - Run the file through [md-format with GitHub Flavoured Markdown support](https://pypi.org/project/mdformat/) and tweak any remaining formatting so that the file will render nicely
        - Open a PR that will close the issue related to the past meeting
- Setup for the next month's meeting
    - Clear the shared document of topics and notes
    - Update the date, time and time converter link in the info box at the top of the shared document
    - [Open a new meeting issue](https://github.com/jupyterhub/team-compass/issues/new?assignees=&labels=&projects=&template=collab_cafe.md&title=JupyterHub+and+Binder+Collab+Cafe+%7C+%5BMonth%2C+Year%5D) and populate with the information you just updated in the shared document
    - _TBA: Advertise in other places, e.g., Discourse, Zulip, Mastodon, etc._
