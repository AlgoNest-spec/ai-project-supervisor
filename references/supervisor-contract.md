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
