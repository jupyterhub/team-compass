"""Generate HTML Contributors tables for team pages
"""
import pandas as pd
import os
from pathlib import Path
from yaml import safe_load
from textwrap import dedent, indent

# Load data that we'll use for the table
path_data = Path(__file__).parent
path_contributor_data = path_data / "contributors-jupyterhub.yaml"
contributors = safe_load(path_contributor_data.read_text())
keyvals = pd.read_csv(path_data / "contributor_key.csv", index_col=0)

snippet = dedent("""
    .. grid:: 1 2 3 3
       :gutter: 3
       :class-container: contributor-grid
    """)

inactive_contributors = []
for contributor in contributors:
    if contributor["status"] == "inactive":
        inactive_contributors.append(contributor)
        continue

    # Pull out the contribution image
    contributions = []
    for contribution in contributor["contributions"].split(','):
        if contribution in keyvals.index:
            contribution = keyvals.loc[contribution]["image"]
        contributions.append(contribution)
    contributions = ", ".join(contributions)

    
    # Create the card rST. Needs to be indented underneath its parent
    snippet += indent(dedent(f"""

    .. grid-item-card::
       :class-header: bg-light
       :text-align: center
       :link: https://github.com/{contributor["handle"]}

       **{contributor["name"]}**

       ^^^
        
       .. image:: https://github.com/{contributor["handle"]}.png?size=125

       **@{contributor["handle"]}**
 
       {contributions}

       +++
       {contributor["affiliation"]}
    """), "   ")

# Add text about inactive contributors

snippet += "\n**Inactive Contributors**:\n\n"
for ii, contributor in enumerate(inactive_contributors):
    inactive_contributors[ii] = f'**{contributor["name"]}** `(@{contributor["handle"]}) <https://github.com/{contributor["handle"]}>`_'
snippet += ", ".join(inactive_contributors)

# Write a snippet that we will include in our docs
path_contributor_data.with_suffix(".txt").write_text(snippet)
