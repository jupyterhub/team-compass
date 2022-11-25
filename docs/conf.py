#!/usr/bin/env python3

# -- General configuration ------------------------------------------------
extensions = ["sphinx_copybutton", "sphinx_design", "sphinx.ext.mathjax", "myst_parser"]
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

# -- Update contributor lists --------------------------------------------

from subprocess import run

run(["python", "_data/contributors/gen_contributors.py"], check=True)
