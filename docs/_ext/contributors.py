"""Generate HTML Contributors tables for team pages
"""
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

from pathlib import Path
from textwrap import dedent, indent

import pandas as pd
from yaml import safe_load

class ContributorsDirective(SphinxDirective):
    has_content = True

    def run(self) -> list:
        path_data = Path(__file__).parent.parent / "_data"
        path_contributor_data = path_data / "contributors-jupyterhub.yaml"
        contributors = safe_load(path_contributor_data.read_text())
        keyvals = pd.read_csv(path_data / "contributor_key.csv", index_col=0)

        # snippet = dedent("""
        #     .. grid:: 1 2 3 3
        #     :gutter: 3
        #     :class-container: contributor-grid
        #     """)

        # inactive_contributors = []

        # team_titles = {
        #     "council": "JupyterHub Council",
        #     "health": "JupyterHealth",
        #     "maintainers": "Maintainers",
        #     "mybinder": "mybinder.org operators",
        # }

        # inactive_contributors = []
        # for contributor in contributors:
        #     if contributor.get("status", "active") == "inactive":
        #         inactive_contributors.append(contributor)
        #         continue


        #     # Pull out the contribution image
        #     contributions = []
        #     for contribution in contributor["contributions"].split(','):
        #         contribution = contribution.strip()
        #         if contribution in keyvals.index:
        #             contribution = keyvals.loc[contribution]["image"]
        #         contributions.append(contribution)
        #     contributions = ", ".join(contributions)

        #     teams = []
        #     for team in contributor.get("teams") or []:
        #         teams.append(f"**{team_titles.get(team, team)}**")
        #     teams = ", ".join(teams)

        #     # Create the card rST. Needs to be indented underneath its parent
        #     snippet += indent(
        #         dedent(
        #             f"""

        #     .. grid-item-card::
        #     :class-header: bg-light
        #     :text-align: center
        #     :link: https://github.com/{contributor["handle"]}

        #     **{contributor["name"]}**

        #     ^^^

        #     .. image:: https://github.com/{contributor["handle"]}.png?size=125

        #     `@{contributor["handle"]} <https://github.com/{contributor["handle"]}>`_

        #     {contributions}

        #     {teams}

        #     +++
        #     {contributor["affiliation"]}
        #     """
        #         ),
        #         "   ",
        #     )

        # # team_titles = {
        # #     "council": "JupyterHub Council",
        # #     "maintainers": "Maintainers",
        # #     "mybinder": "mybinder.org operators",
        # #     "inactive": "Inactive team members",
        # # }
        # # # make sure we know what the teams are
        # # assert set(teams).issubset(set(team_titles))


        # def _short_contributor(contributor):
        #     return f'**{contributor["name"]}** (`@{contributor["handle"]} <https://github.com/{contributor["handle"]}>`_)'


        # # TODO: if we want separate lists for each team

        # # for name, title in team_titles.items():
        # #     team_members = teams.get(name, [])
        # #     if not team_members:
        # #         continue
        # #     snippet += f"\n{title}\n{'~' * len(title)}\n\n"
        # #     snippet += ", ".join(map(_short_contributor, team_members))
        # #     snippet += "\n\n"
        # #
        # # # Add text about inactive contributors
        # #

        # inactive = "Inactive Team members"
        # snippet += f"\n{inactive}\n{'^' * len(inactive)}\n\n"
        # snippet += ", ".join(map(_short_contributor, inactive_contributors))

        # # Write a snippet that we will include in our docs
        # path_output_contributor_data.write_text(snippet + "\n")

        return [nodes.raw("", "<h2>Hello</h2>", format='html')]

def setup(app: object) -> dict:
    app.add_directive("contributors", ContributorsDirective)