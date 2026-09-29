# Supervisor operating contract

## Task brief template

```text
Task ID:
Goal:
Why it matters:
Inputs and source of truth:
Included scope:
Excluded scope:
Dependencies:
Deliverable and format:
Acceptance criteria:
Constraints and approval boundaries:
Report as: COMPLETE | BLOCKED | NEEDS_DECISION
Evidence/artifact links:
Assumptions and unresolved questions:
```

## Task record

Track a stable task ID; owner; executor and reviewer where applicable; dependency IDs; canonical input/plan identity; state; attempt count; last progress time; heartbeat if available; artifact location and integrity evidence; acceptance result; and failure/block reason. Store artifact paths relative to an approved project root where possible. Keep immutable attempt history when retrying.

## Parallelism and staffing

- Parallelize tasks only when dependencies are satisfied and their outputs do not require shared mutable state.
- Give tasks with overlapping scope one clear owner; assign a reviewer independently.
- Select agents based on demonstrated task capability, needed tools/context, and the least additional access required. Do not infer model capabilities that were not supplied or observed.
- If no dispatch interface exists, output the plan and task briefs as proposed assignments. Never state that agents were started, monitored, or completed work.

## Dependency and continuation rule

Reject cycles before dispatch. Start a task only if each required predecessor is accepted and its own input and permission checks pass. When a prerequisite fails, block descendants but retain independent branches. Do not reuse an artifact if its source identity, version, or acceptance status differs.

## Independent review

The reviewer should receive the acceptance criteria, relevant source evidence, and the executor's artifact. Ask the reviewer to identify errors and missing evidence, not merely endorse the result. Record `ACCEPT`, `REVISE`, `REJECT`, or `INCONCLUSIVE` with reasons. The executor may address review findings, but the reviewer verifies the correction.

## Monitoring and escalation

Use progress changes and artifacts to measure work; heartbeat alone is liveness only. Check existing task status before restarting or replacing a worker. Apply bounded retries with backoff. Escalate authorization questions, unresolved material conflicts, repeated deterministic failures, exhausted retries, and changes to scope or acceptance criteria. Continue safe independent work while blocked items wait.


## Continuity and heartbeat

For work that may span turns or execution windows, keep a compact continuation summary next to the task board or in the host's supported persistent-goal workflow. Update it after meaningful progress and before yielding control. Include:

```text
Goal: the durable end state and constraints
Acceptance evidence: what must exist or pass before completion
Current status: overall state and timestamp/checkpoint
Task board: stable IDs, owners, states, dependencies
Completed and reviewed: artifact locations and review decisions
In progress: current attempt, last verified result, next step
Blocked or uncertain: cause, evidence, input needed
Retries/budget: attempts used and remaining bounded allowance
Decisions: durable choices and unresolved conflicts
Next safe action: one concrete action whose dependencies are ready
Approval boundaries: actions that still require the user
Dispatch/heartbeat: workers actually active; observed heartbeat and next expected check if available
```

A Codex Goal, where available, is a thread-scoped completion contract. Define the outcome, verification evidence, constraints, allowed scope, iteration policy, and blocked stop condition. Use the host's documented lifecycle controls; do not tell the model to start a Goal if it is unavailable or requires user input. The task board and continuation summary remain necessary because a Goal does not replace task ownership, artifact tracking, or reviewer decisions.

Treat heartbeat as a liveness signal or scheduled wakeup only. In a tested Codex heartbeat setup, a heartbeat can retrigger work after an approximately five-hour rolling limit renews, and an active Goal can guide continuation. This is an observed setup/version-dependent behavior, not a guarantee across Codex versions or other hosts. Verify the active Goal, actual wakeup, and current budget before resuming. A wakeup is not evidence that delegated work completed. Reconcile actual task/artifact state, deduplicate before dispatch, and continue only within the existing scope, retry limits, and authorization boundaries.

If no automatic continuation occurs, leave the summary ready for a later manual resume. Never claim that a task will auto-resume solely because a heartbeat was configured.
