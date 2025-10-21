"""Generate HTML Outreachy tables for team pages"""

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

import json
from datetime import datetime
from pathlib import Path

import jsonschema
from jsonschema import validate


class OutreachyDirective(SphinxDirective):
    has_content = True

    def run(self) -> list:
        # Set filepath to participants data file
        data_path = Path(__file__).parent.parent / "_data"
        participants_data_file = data_path.joinpath("outreachy_participants.json")
        participants_schema_file = data_path.joinpath(
            "outreachy_participants.schema.json"
        )

        # Read in json defining Outreachy participants
        with open(participants_data_file) as f:
            participants_data = json.load(f)

        # Read in the JSON schema file
        with open(participants_schema_file) as f:
            participants_schema = json.load(f)

        # Validate the data against the schema
        try:
            validate(participants_data, participants_schema)
        except jsonschema.exceptions.ValidationError as err:
            raise err

        # Sort cohorts in reverse chronological order
        participants_data = sorted(
            participants_data,
            key=lambda x: datetime.strptime(x["round"], "%B, %Y").strftime("%Y-%m"),
            reverse=True,
        )

        all_cohort_nodes = []
        for cohort in participants_data:
            # Sort interns into alphabetical order
            cohort["interns"] = sorted(cohort["interns"], key=lambda x: x["name"])

            # Sort community members into alphabetical order
            cohort["community_members"] = sorted(
                cohort["community_members"], key=lambda x: x["name"]
            )

            # Add cards to the grid for each intern
            intern_html_cards = []
            for intern in cohort["interns"]:
                if "blog_url" in intern.keys():
                    first_name = intern["name"].split()[0]
                    card_footer = f"""<div class="card-footer">
    <a href="{intern["blog_url"]}">Read {first_name}'s blog!</a>
</div>"""
                else:
                    card_footer = ""
                intern_html_cards.append(
                    f"""<div class="col mb-sm-2">
    <a href="https://github.com/{intern["github_handle"]}">
        <div class="card h-100 text-center">
            <div class="card-header">
                <strong>{intern["name"]}</strong>
            </div>
            <img src="https://github.com/{intern["github_handle"]}.png?size=125" class="card-img-top" alt="Profile photo of {intern["name"]}">
            <div class="card-body">
                <p class="card-text"><a href="https://github.com/{intern["github_handle"]}">@{intern["github_handle"]}</a></p>
            </div>
            {card_footer}
        </div>
    </a>
</div>"""
                )

            # Add cards to the grid for each community member
            member_html_cards = []
            for member in cohort["community_members"]:
                member_html_cards.append(f"""<div class="col mb-sm-2">
    <a href="https://github.com/{member["github_handle"]}">
        <div class="card h-100 text-center">
            <div class="card-header">
                <strong>{member["name"]}</strong>
            </div>
            <img src="https://github.com/{member["github_handle"]}.png?size=125" class="card-img-top" alt="Profile photo of {member["name"]}">
            <div class="card-body">
                <p class="card-text"><a href="https://github.com/{member["github_handle"]}">@{member["github_handle"]}</a></p>
            </div>
            <div class="card-footer">
                {", ".join(member["roles"])}
            </div>
        </div>
    </a>
</div>""")

            intern_html = f"""<div class="container">
  <div class="row row-cols-1 row-cols-md-3">
    {"".join(intern_html_cards)}
  </div>
</div>"""

            members_html = f"""<div class="container">
  <div class="row row-cols-1 row-cols-md-3">
    {"".join(member_html_cards)}
  </div>
</div>"""

            all_cohort_nodes.extend(
                [
                    nodes.paragraph("", "", nodes.strong(text=cohort["round"])),
                    nodes.paragraph("", "", nodes.strong(text="Interns")),
                    nodes.raw("", intern_html, format="html"),
                    nodes.paragraph("", "", nodes.strong(text="Community members")),
                    nodes.raw("", members_html, format="html"),
                ]
            )

        return all_cohort_nodes


def setup(app: object) -> dict:
    app.add_directive("outreachy", OutreachyDirective)
