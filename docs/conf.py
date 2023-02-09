#!/usr/bin/env python3

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.mathjax",
    "sphinxext.rediraffe",
    "myst_parser",
]
templates_path = []
source_suffix = [".rst", ".md"]
root_doc = "index"

# General information about the project.
project = "Team Compass"
copyright = "2022, JupyterHub Team and Binder Team"
author = "JupyterHub Team and Binder Team"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output ----------------------------------------------
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_theme_options = {
    "use_edit_page_button": True,
    "analytics": {
        "google_analytics_id": "UA-101904940-3",
    },
    "github_url": "https://github.com/jupyterhub/team-compass",
    "twitter_url": "https://twitter.com/projectjupyter",
    "icon_links": [
        {
            "name": "JupyterHub Forum Topic",
            "url": "https://discourse.jupyter.org/c/jupyterhub/10",
            "icon": "fab fa-discourse",
        }
    ],
}

html_context = {
    "github_user": "jupyterhub",
    "github_repo": "team-compass",
    "github_version": "main",
    "doc_path": "docs",
    "source_suffix": source_suffix,
}

# -- MyST Markdown configuration ----------------------------------------
# ref: https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "linkify",
]

# Only linkify URLs that start with schema
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#linkify
myst_linkify_fuzzy_links = False

# -- Update contributor lists --------------------------------------------

from subprocess import run

run(["python", "_data/contributors/gen_contributors.py"], check=True)
run(["python", "_data/outreachy/outreachy_participants.py"], check=True)

# -- Options for the rediraffe extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-rediraffe#readme
#
# This extensions help us relocated content without breaking links. If a
# document is moved internally, a redirect like should be configured below to
# help us not break links.
#
rediraffe_branch = "main"
rediraffe_redirects = {
    # Redirects added 2022-11-25
    # ref: https://github.com/jupyterhub/team-compass/pull/587
    "building-blocks/index": "index-team_policies",
    "building-blocks/readme-badges": "practices/readme-badges",
    "contribute/index": "index-team_guides",
    "index-team_governance": "index-team_policies",
    "milestones": "resources/milestones",
    "talking": "practices/talking",
    "team/adding-members": "practices/adding-members",
    "team/community-strategy": "resources/community-strategy",
    "team/member-guide": "index-team_policies",
    "team/repository-code-standards": "practices/repository-code-standards",
    "team/shared-infrastructure": "resources/shared-infrastructure",

    # Redirects added 2022-11-28
    # ref: https://github.com/jupyterhub/team-compass/pull/593
    "practices/talking": "practices/external-communication",

    # Add additional redirects below if you relocate documents
    # "old/folder/old-file": "new-folder/new-file",
}

def setup(app):
    # So that we can label and reference with {team}
    app.add_crossref_type("team", "team")
