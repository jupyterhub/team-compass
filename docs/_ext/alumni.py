"""Generate HTML Contributors tables for team pages"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

from pathlib import Path

from yaml import safe_load


class AlumniDirective(SphinxDirective):
    has_content = True

    def run(self) -> list:
        path_data = Path(__file__).parent.parent / "_data"
        print(path_data)
        path_contributor_data = path_data / "contributors-jupyterhub.yaml"
        contributors = safe_load(path_contributor_data.read_text())

        inactive_contributors_html_cards = []
        for contributor in contributors:
            if contributor.get("status", "active") == "inactive":
                # We use Bootstrap's column wrapping,
                # read more at https://getbootstrap.com/docs/5.0/layout/columns/#column-wrapping.
                # The coloumn has a margin,
                # read more at https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding.
                # We use Bootstrap's card,
                # read more at https://getbootstrap.com/docs/5.3/components/card/.
                # The card must have h-100 for equal height,
                # as mentioned at https://getbootstrap.com/docs/5.3/components/card/#grid-cards.
                inactive_contributors_html_cards.append(f"""<div class="col mb-sm-2">
    <a style="text-decoration: none;" href="https://github.com/{contributor["handle"]}">
        <div class="card h-100 text-center">
            <div class="card-header">
                <strong>{contributor["name"]}</strong>
            </div>
            <div class="card-body">
                <p class="card-text"><a href="https://github.com/{contributor["handle"]}">@{contributor["handle"]}</a></p>
            </div>
        </div>
    </a>
</div>""")

        inactive_contributors_html = f"""<div class="container">
  <div class="row row-cols-1 row-cols-md-3">
    {"".join(inactive_contributors_html_cards)}
  </div>
</div>"""

        return [nodes.raw("", inactive_contributors_html, format="html")]


def setup(app: object) -> dict:
    app.add_directive("alumni", AlumniDirective)
