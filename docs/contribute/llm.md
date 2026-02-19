(llm-policy)=

# Generative AI/LLM Contribution Policy

Short answer: If you (a human) didn't write the code or documentation or comment, please don't submit it to us.

## Policy

1. Do not ever submit code or documentation to JupyterHub that _you did not write_. Tool-assisted coding and automation leaves some gray area that is open to interpretation, but **if you are not comfortable saying the words "I wrote this," do not submit it to us.**
2. Do not ever include verbatim output of an LLM in a comment or PR description.
   When communicating with humans, use your own words.
   If you didn't take the time to write it, it is rude to expect any other human to take any time to read it.
3. Deterministic automated code changes (dependencies, linter auto-fixes, refactor tools, etc.) are fine (great, even!).
4. We will not add AGENTS.md or CLAUDE.md to our repos, as that would be an implicit endorsement of the use of tools that are harmful to community software projects like JupyterHub.

## Why?

Some relevant facts:

- LLMs are the primary driver of a flood of low-quality pull requests, often without disclosure, straining the worldwide open source maintainer load.
- LLMs, at least as operated by organizations like Anthropic, Google, Microsoft, OpenAI, and others are an ongoing environmental and financial catastrophe.
  Using these tools—in any capacity, but especially supporting them financially—contributes to their rapidly escalating harm.
- All such large models—including self-hosted "open weights" models—are unethically (and in some cases illegally) trained on stripping credit and license information from source material.
  While this may turn out to be legal fair use in some jurisdictions, it is certainly against the community spirit of the material they are trained on.
  If anyone ever produces an "ethically trained" LLM for code, we can reconsider this point, but it does not exist and arguably is not possible.


### To summarize

LLMs as they are today, and fundamental to their design, cause numerous material harms, both to the world at large and to community software in particular, and their use will not be endorsed by the JupyterHub project.

As such, we are opposed to all LLM-generated contributions to JupyterHub.
