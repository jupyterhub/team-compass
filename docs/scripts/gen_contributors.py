"""Generate HTML Contributors tables for team pages
"""
import pandas as pd
import os
import os.path as op
from ruamel import yaml

# Variables
N_PER_ROW = 4

# Init
path_data = op.join(op.dirname(op.abspath(__file__)), "..", "team")
yaml = yaml.YAML()
keyvals = pd.read_csv(op.join(path_data, "contributor_key.csv"), index_col=0)

template_start = '<td align="center" class="contrib_entry"><a href="{HANDLE_URL}"><img src="{AVATAR_URL}" class="headshot" alt="{NAME}" /><br /><p class="name"><b>{NAME}</b></p></a><p class="contrib_affiliation">{AFFILIATION}</p>'
template_contributions = '<p class="contributions">{CONTRIBUTIONS}</p></td>'
template = (
    template_start
    + '<a href="binder/governance.html#team-roles"><p class="team team-{TEAM}">team {TEAM}</p></a>'
    + template_contributions
)


def _generate_contributors(contributors, keys):
    """Generate an HTML list of contributors, given a dataframe of their information."""
    s = ['<table class="docutils contributors">', '<tr class="row-even">']
    for ix, person in contributors.iterrows():
        if ix % N_PER_ROW == 0 and ix != 0:
            s += ['</tr><tr class="row-even">']

        # Build contrib text
        this_contrib = person["contributions"].split(",")
        contrib_text = []
        for contrib in this_contrib:
            if contrib in keys.index:
                text = keyvals.loc[contrib, "image"]
                desc = keyvals.loc[contrib, "description"]
                contrib_text += [
                    '<span title={TOOLTIP} class="contribs">{CONTRIB}</span>'.format(
                        TOOLTIP=desc, CONTRIB=text
                    )
                ]
            else:
                contrib_text += [
                    '<span class="contribs contribs_text">{CONTRIB}</span>'.format(
                        CONTRIB=contrib
                    )
                ]

        contrib_text = '<span class="contribs">,</span>'.join(contrib_text)

        # Find user gravatar url
        avatar_url = "https://github.com/{HANDLE}.png?size=200".format(
            HANDLE=person["handle"].lstrip("@")
        )

        # Add user
        format_dict = dict(
            HANDLE=person["handle"],
            HANDLE_URL="https://github.com/{HANDLE}".format(
                HANDLE=person["handle"].lstrip("@")
            ),
            AFFILIATION=person["affiliation"],
            AVATAR_URL=avatar_url,
            NAME=person["name"],
            CONTRIBUTIONS=contrib_text,
            TEAM=person["team"],
        )

        # Render
        s += [template.format(**format_dict)]
    s += ["</table>"]
    final_text = [".. raw:: html", ""]
    for line in s:
        final_text += ["   " + line]
    final_text = "\n".join(final_text)
    return final_text


contributor_file = op.join(path_data, "contributors-jupyterhub.yaml")
with open(contributor_file, "r") as ff:
    data = yaml.load(ff)
people = pd.DataFrame(data)
table = _generate_contributors(people, keyvals)
new_name = os.path.splitext(contributor_file)[0]
with open(new_name + ".txt", "w") as ff:
    ff.write(table)
