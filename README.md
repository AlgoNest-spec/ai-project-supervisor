# AI Project Supervisor

An independently installable [Agent Skill](SKILL.md) for leading multi-agent projects from planning and delegation through review and delivery.

## What it does

- Turns a broad goal into tasks with owners, dependencies, deliverables, and acceptance criteria.
- Assigns work according to the agents and capabilities actually available.
- Gives each contributor a clear task brief and a review standard.
- Coordinates parallel work, checkpoints, bounded retries, and progress updates.
- Reviews evidence, works through conflicting results, and integrates accepted work.
- States clearly when the host platform cannot dispatch or monitor other agents.

The skill provides a supervision method. Actual agent dispatch and monitoring depend on the AI platform where it is used.

## Install

Install or copy this complete ai-project-supervisor directory using the skill-loading method supported by your AI agent. Keep the directory structure intact so the reference guide, example, and validator remain available.

## How to use it

1. Start a project task and describe the outcome, constraints, deadlines, and what a successful delivery looks like.
2. Tell the supervisor which agents or delegation tools are available, if the platform does not expose them automatically.
3. Ask it to propose the task plan, dependencies, and acceptance criteria before work begins.
4. Have it delegate tasks using the tools available in that environment. Review any decision or external action it flags for your approval.
5. Ask for progress updates or a final delivery summary. The supervisor should distinguish reviewed, completed work from pending or blocked tasks.

Example prompt:

> Lead a product-launch project with a research agent, a prototype builder, a writer, and an independent reviewer. First propose the work plan, dependencies, and acceptance criteria. Then delegate tasks using the tools available in this environment, track progress, resolve conflicting evidence, and deliver an integrated launch plan. If you cannot dispatch agents here, give me ready-to-send task briefs instead. Do not claim work is complete until its deliverable has been reviewed.

See the [supervisor contract](references/supervisor-contract.md) and [synthetic team scenario](examples/project-team-scenario.json).

## Validate the example

With Python 3, run from this directory: python scripts/validate_scenario.py

The example is fictional and requires no external services.

## License

No license has been applied. See LICENSE_RECOMMENDATION.md for the options to review before reuse.
