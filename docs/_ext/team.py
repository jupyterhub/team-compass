"""Generate HTML Contributors tables for team pages"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

from pathlib import Path

import pandas as pd
from yaml import safe_load


class TeamDirective(SphinxDirective):
    has_content = True

    def run(self) -> list:
        path_data = Path(__file__).parent.parent / "_data"
        print(path_data)
        path_contributor_data = path_data / "contributors-jupyterhub.yaml"
        contributors = safe_load(path_contributor_data.read_text())
        keyvals = pd.read_csv(path_data / "contributor_key.csv", index_col=0)

        active_contributor_html_cards = []

        team_titles = {
            "council": "JupyterHub Council",
            "health": "JupyterHealth",
            "maintainers": "Maintainers",
            "mybinder": "mybinder.org operators",
        }

        for contributor in contributors:
            if contributor.get("status", "active") == "inactive":
                continue

            # Pull out the contribution image
            contributions = []
            for contribution in contributor["contributions"].split(","):
                contribution = contribution.strip()
                if contribution in keyvals.index:
                    contribution = keyvals.loc[contribution]["image"]
                contributions.append(contribution)
            contributions = ", ".join(contributions)

            teams = []
            for team in contributor.get("teams") or []:
                teams.append(f"{team_titles.get(team, team)}")
            teams = ", ".join(teams)

            # We use Bootstrap's column wrapping,
            # read more at https://getbootstrap.com/docs/5.0/layout/columns/#column-wrapping.
            # The coloumn has a margin,
            # read more at https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding.
            # We use Bootstrap's card,
            # read more at https://getbootstrap.com/docs/5.3/components/card/.
            # The card must have h-100 for equal height,
            # as mentioned at https://getbootstrap.com/docs/5.3/components/card/#grid-cards.
            active_contributor_html_cards.append(
                f"""<div class="col mb-sm-2">
    <a href="https://github.com/{contributor["handle"]}">
        <div class="card h-100 text-center">
            <div class="card-header">
                <strong>{contributor["name"]}</strong>
            </div>
            <img src="https://github.com/{contributor["handle"]}.png?size=125" class="card-img-top" alt="Profile photo of {contributor["name"]}">
            <div class="card-body">
                <p class="card-text"><a href="https://github.com/{contributor["handle"]}">@{contributor["handle"]}</a></p>
                <p class="card-text">{contributions}</p>
                <p class="card-text"><strong>{teams}</strong></p>
            </div>
            <div class="card-footer">
                {contributor["affiliation"]}
            </div>
        </div>
    </a>
</div>"""
            )

        active_contributor_html = f"""<div class="container">
  <div class="row row-cols-1 row-cols-md-3">
    {"".join(active_contributor_html_cards)}
  </div>
</div>"""

        return [nodes.raw("", active_contributor_html, format="html")]


def setup(app: object) -> dict:
    app.add_directive("team", TeamDirective)
