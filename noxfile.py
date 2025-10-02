import glob
import os.path

import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session(python="3.13", default=False)
def docs(session):
    """
    Build the documentation.
    """
    sphinx_config_files = glob.glob("./docs/**/conf.py", recursive=True)
    sphinx_config = sphinx_config_files[0]
    source_dir = os.path.dirname(sphinx_config)
    if source_dir.find("source") == -1:
        output_dir = os.path.join(source_dir, "_build/html")
    else:
        output_dir = os.path.join(os.path.dirname(source_dir), "_build/html")

    doc_build_default_args = ["-b", "dirhtml", source_dir, output_dir]

    session.install("-r", os.path.join(source_dir, "requirements.txt"))

    if "live" in session.posargs or (
        session.interactive and "only-build" not in session.posargs
    ):
        # For live preview, sphinx-autobuild is used.
        # To avoid sphinx-autobuild be missing,
        # sphinx-autobuild is installed explicitly.
        session.install("sphinx-autobuild")
        cmd = ["sphinx-autobuild"]

        # Add relative paths to this if we ever need to ignore them
        AUTOBUILD_IGNORE = [output_dir]

        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])

        cmd.extend(doc_build_default_args)
        session.run(*cmd)
    else:
        session.run("sphinx-build", *doc_build_default_args)
