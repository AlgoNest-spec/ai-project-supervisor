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

Run from this directory with Python 3:

```console
python scripts/validate_scenario.py
```

The example is fictional and requires no external services.



## Long-running tasks

For a long-running project, define a verifiable finish line and keep the continuation summary current. Codex versions that support [Goals](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) can use /goal to persist the objective across turns. On other hosts, track the same objective in the task board and handoff summary.

In a tested Codex heartbeat setup, an approximately five-hour rolling-limit renewal can retrigger work and let the active Goal guide continuation. This is setup/version-dependent: verify the active Goal, heartbeat, and budget before resuming. The Skill does not guarantee a wakeup or renewal interval. See the [continuity and heartbeat summary template](references/supervisor-contract.md#continuity-and-heartbeat).

Example Codex goal:

> Deliver the reviewed project package against the acceptance criteria. Keep the task board and continuation summary current, resume from verified checkpoints after a heartbeat wakeup, deduplicate work, stay within the existing scope and retry budget, and stop if approval or user input is required.



## License

No license has been applied. See LICENSE_RECOMMENDATION.md for the options to review before reuse.
