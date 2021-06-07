from ghapi.all import GhApi
from datetime import date
from ghapi.actions import github_token
from packaging import version
from base64 import b64decode

def get_latest_tag(org, repo):
    tags = api.repos.list_tags(org, repo)
    versions = [tag.name for tag in tags]
    versions.sort(key=version.parse, reverse=True)
    return versions[0]

# On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
token = github_token() if "ACCESS_TOKEN" not in os.environ else os.environ["ACCESS_TOKEN"]

# Initialize the GH API
api = GhApi(token=token)

# The base template is defined here: https://github.com/jupyterhub/team-compass/blob/release-pulse-issue/.github/ISSUE_TEMPLATE/release-pulse.md
# It has placeholders for lists of PRs, commits and latests version and these will be automatically filled in below, then a new issue will be created.
template = api.repos.get_content("jupyterhub", "team-compass", ".github/ISSUE_TEMPLATE/release-pulse.md", "release-pulse-issue")
template = b64decode(template.content).decode("utf-8")

# This removes the header bracketed by ---
template = "---".join(template.split("---")[2:]).strip()

# Z2JH
latest_tag = get_latest_tag("jupyterhub", "zero-to-jupyterhub-k8s")
template = template.replace(
    "{{INSERT LATEST RELEASE HERE}}",
    latest_tag
)

unreleased_commits = f"https://github.com/jupyterhub/zero-to-jupyterhub-k8s/compare/{latest_tag}...master"
template = template.replace(
    "{{INSERT LATEST COMMITS HERE}}",
    unreleased_commits
)

pulls = api.pulls.list("jupyterhub", "zero-to-jupyterhub-k8s", state="open")
if pulls:
    need_merge = "\n".join([f"* [{pull.title}]({pull.html_url})" for pull in pulls])+ "\n\n"
template = template.replace(
    "{{INSERT PRS HERE}}",
    need_merge
)

# Dependencies
# OAuthenticator
latest_tag = get_latest_tag("jupyterhub", "oauthenticator")
unreleased_commits = f"https://github.com/jupyterhub/oauthenticator/compare/{latest_tag}...master"
template = template.replace(
    "{{INSERT LATEST OAUTHENTICATOR COMMITS HERE}}",
    unreleased_commits
)

# Kubespawner
latest_tag = get_latest_tag("jupyterhub", "kubespawner")
unreleased_commits = f"https://github.com/jupyterhub/kubespawner/compare/{latest_tag}...master"
template = template.replace(
    "{{INSERT LATEST KUBESPAWNER COMMITS HERE}}",
    unreleased_commits
)

# CHP
latest_tag = get_latest_tag("jupyterhub", "configurable-http-proxy")

unreleased_commits = f"https://github.com/jupyterhub/configurable-http-proxy/compare/{latest_tag}...main"
template = template.replace(
    "{{INSERT LATEST CHP COMMITS HERE}}",
    unreleased_commits
)

# Create an issue
resp = api.issues.create("jupyterhub", "team-compass", title=f"Time for release - {date.today():%b %d, %Y}", body=template, labels=["release-pulse"])
url = f"https://github.com/{resp.url.split('repos/')[-1]}"
print(f"Finished posting release issue to {url} !")
