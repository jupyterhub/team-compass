import json
from datetime import datetime
from pathlib import Path
from textwrap import dedent

import jsonschema
from jsonschema import validate

# Set filepath to interns data file
data_path = Path(__file__).resolve().parent
interns_data_file = data_path.joinpath("outreachy_interns.json")
interns_schema_file = data_path.joinpath("outreachy_interns.schema.json")
output_path = data_path.joinpath("outreachy_interns.txt")

# Read in json defining Outreachy interns
with open(interns_data_file) as f:
    interns_data = json.load(f)

# Read in the JSON schema file
with open(interns_schema_file) as f:
    interns_schema = json.load(f)

# Validate the data against the schema
try:
    validate(interns_data, interns_schema)
except jsonschema.exceptions.ValidationError as err:
    raise err

# Sort cohorts in reverse chronological order
interns_data = sorted(
    interns_data,
    key=lambda x: datetime.strptime(x["round"], "%B, %Y").strftime("%Y-%m"),
    reverse=True,
)

markdown = ""

for cohort in interns_data:
    # Sort interns into alphabetical order
    cohort["interns"] = sorted(cohort["interns"], key=lambda x: x["name"])

    # Begin MyST definition of grid with cards
    grid_md = dedent(
        """
        `````{{grid}} 1 2 3 3
        :gutter: 3
        :class-container: contributor-grid

        {card_md}
        `````
    """
    )

    # Add cards to the grid for each intern
    card_md = ""
    for intern in cohort["interns"]:
        card_md += dedent(
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
            [Read their blog!]({intern['blog_url']})
            ````
        """
        )

    # Add the markdown for the sphinx design cards into the grid and add cohort
    # year as title
    grid_md = grid_md.format(card_md=card_md)
    final_md = f"### {cohort['round']}\n" + grid_md
    markdown += final_md

output_path.write_text(markdown + "\n")
