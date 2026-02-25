(llm-policy)=

# Generative AI/LLM Contribution Policy

We ask that all contributions (through issues and pull requests) are made by a human who is willing to take accountability for the code, documentation, or comment they submit.
In short: LLM-generated contributions are not accepted.

## Principles

We, the JupyterHub community, value:

* **human co-creation**: we are proud to collaborate with developers, researchers, educators, and infrastructure specialists across our global community.
  * We respect **their copyright** over their work and appreciate their shared investment in the scientific open source ecosystem by licensing the materials under the [BSD 3-Clause "New" or "Revised" License](https://github.com/jupyterhub/jupyterhub/blob/main/LICENSE).
  * We respect the **time** taken to read and review contributions, maintaining a high standard and supportive community engagement.
* **security**: JupyterHub is trusted infrastructure for hundreds of thousands of users and we prioritize keeping their data, code, and personal configuration information secure.
* **veracity**: beyond security, we ensure our tools do what we think they do, and that we respect accuracy in communications within and beyond the scientific open source ecosystem.
* **our global society**: we seek to minimise environmental impact and human exploitation in the development and deployment of JupyterHub infrastructure.

## Our concerns

Large language models (LLMs), the primary underlying technology used in "Generative AI" products, are:

* contributing to rapid **over-burdening** of the reviewing capacity for many open source projects. [REF]
* trained on very large datasets, and all widely used models do not respect the licenses (or lack thereof) of this input data. [REF]
* in many cases trained by people who are underpaid and exposed to traumatic content without appropriate support.
  See Wired's article from 2024: [The Low-Paid Humans Behind AI’s Smarts Ask Biden to Free Them From "Modern Day Slavery"](https://www.wired.com/story/low-paid-humans-ai-biden-modern-day-slavery)
* consuming very large amounts of energy and potable water, both during their training phases and as they being used to generate outputs. See the MIT Technology Review's summaries of the literature at their [Super Topic: AI and our energy future](https://www.technologyreview.com/supertopic/ai-energy-package/).
* generating output that may not be able to be covered by our licenses and copyright, at least in the United States. [US Copyright guidance](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)

## Policy

1. Only submit code or documentation to JupyterHub that you wrote and that you understand.
    * We have chosen this requirement given our concerns around **copyright**, **reviewer burden**, and to maintain **auditable accountability** for the **veracity** of our work.
    * We leave the interpretation of this request to you: tool-assisted coding and automation leaves some gray areas and we recognize that everyone has different perspectives on the use of various tools for supporting their open source contributions.
    * Always make sure you are comfortable saying "I wrote this" before submitting code or a comment.
    * We strongly endorse using deterministic tools to check and improve the quality of your code, such as automated code dependency updates, linter auto-fixes, refactor tools, etc.
2. Communicate in issue and pull request threads in your own words.
  Please do not use the verbatim output of an LLM in conversation with our user, reviewer and maintainer community.
    * We have chosen this requirement given our priority to **value human co-creation**.
3. Will will not include or accept supporting resources in `AGENTS.md`, `CLAUDE.md` or similar files to our repos as we prefer human contributors follow the [contribution guidelines](guide.md) that already exist.
   If present, these files shall only include instructions to _prevent_ generating contributions.
    * If it is not clear how to contribute to JupyterHub, we encourage you to ask questions in our [Zulip channel](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub) or on [Discourse](https://discourse.jupyter.org/c/jupyterhub/10).

## Alignment and agreement

The [JupyterHub team](https://compass.hub.jupyter.org/team/) is diverse and passionate.
We do not all hold the same perspectives around the differential - and different - harms and benefits that can come from the training and deployment of large language models. 

In our creation of this policy we sought to maximise our interpersonal alignment, compromising where appropriate to reach agreement on an actionable policy.
