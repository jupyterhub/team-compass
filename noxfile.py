"""
This is a low entry point for novice contributors to the documentation.
"""

import os.path

import nox

nox.options.reuse_existing_virtualenvs = True

DOCS_DIR = "docs"

@nox.session(default=False)
def build(session):
    session.install("-r", os.path.join(DOCS_DIR, "requirements.txt"))
    with session.chdir(DOCS_DIR):
        session.run("jupyter", "book", "build", "--ci", "--html")

@nox.session(default=False)
def start(session):
    session.install("-r", os.path.join(DOCS_DIR, "requirements.txt"))
    with session.chdir(DOCS_DIR):
        session.run("jupyter", "book", "start")