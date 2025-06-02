"""A nox configuration file so that we can build the documentation easily with nox.
- see the README.md for information about nox.
- ref: https://nox.thea.codes/en/stable/
"""
import nox

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "dirhtml", "docs", "docs/_build/html"]

@nox.session()
def docs(session):
    session.install("-r", "docs/requirements.txt")
    if "live" in session.posargs:
        # Add relative paths to this if we ever need to ignore them
        AUTOBUILD_IGNORE = [
          "docs/_data",
          "docs/_build",
        ]
        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])
        cmd.extend(build_command)
        session.run(*cmd)
    else:
        session.run("sphinx-build", *build_command)
