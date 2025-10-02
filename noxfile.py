import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(python="3.13", default=False)
def docs(session):
    """
    Build the documentation.
    """
    doc_build_default_args = ["-b", "dirhtml", "docs", "docs/_build/html"]

    session.install("-r", "docs/requirements.txt")

    if "live" in session.posargs or (
        session.interactive and "only-build" not in session.posargs
    ):
        # For live preview, sphinx-autobuild is used.
        # To avoid sphinx-autobuild be missing,
        # sphinx-autobuild is installed explicitly.
        session.install("sphinx-autobuild")
        cmd = ["sphinx-autobuild"]

        # Add relative paths to this if we ever need to ignore them
        AUTOBUILD_IGNORE = [
            "docs/_build",
        ]

        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])

        cmd.extend(doc_build_default_args)
        session.run(*cmd)
    else:
        session.run("sphinx-build", *doc_build_default_args)
