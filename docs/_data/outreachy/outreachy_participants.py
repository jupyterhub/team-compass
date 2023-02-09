import json
from datetime import datetime
from pathlib import Path
from textwrap import dedent

import jsonschema
from jsonschema import validate

# Set filepath to participants data file
data_path = Path(__file__).resolve().parent
participants_data_file = data_path.joinpath("outreachy_participants.json")
participants_schema_file = data_path.joinpath("outreachy_participants.schema.json")
output_path = data_path.joinpath("outreachy_participants.txt")

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

markdown = ""

for cohort in participants_data:
    # Sort interns into alphabetical order
    cohort["interns"] = sorted(cohort["interns"], key=lambda x: x["name"])

    # Sort community members into alphabetical order
    cohort["community_members"] = sorted(cohort["community_members"], key=lambda x: x["name"])

    # Begin MyST definition of grid with cards
    grid_md = dedent(
        """
        #### Interns

        `````{{grid}} 1 2 3 3
        :gutter: 3
        :class-container: contributor-grid

        {intern_card_md}
        `````

        #### Community members

        `````{{grid}} 1 2 3 3
        :gutter: 3
        :class-container: contributor-grid

        {member_card_md}
        `````
    """
    )

    # Add cards to the grid for each intern
    intern_card_md = ""
    for intern in cohort["interns"]:
        intern_card_md += dedent(
            f"""
            ````{{grid-item-card}}
            :class-header: bg-light
            :text-align: center

            **{intern['name']}**

            ^^^

            ```{{image}} https://github.com/{intern['github_handle']}.png?size=125
            ```

            [@{intern['github_handle']}](https://github.com/{intern['github_handle']})

            +++
            {f"[Read their blog!]({intern['blog_url']})" if "blog_url" in intern.keys() else ""}
            ````
        """
        )

    # Add cards to the grid for each community member
    member_card_md = ""
    for member in cohort["community_members"]:
        member_card_md += dedent(
            f"""
            ````{{grid-item-card}}
            :class-header: bg-light
            :text-align: center

            **{member['name']}**

            ^^^

            ```{{image}} https://github.com/{member['github_handle']}.png?size=125
            ```

            [@{member['github_handle']}](https://github.com/{member['github_handle']})

            +++
            {', '.join(member['roles'])}
            ````
        """
        )

    # Add the markdown for the sphinx design cards into the grid and add cohort
    # year as title
    grid_md = grid_md.format(intern_card_md=intern_card_md, member_card_md=member_card_md)
    final_md = f"### {cohort['round']}\n" + grid_md
    markdown += final_md

output_path.write_text(markdown + "\n")
