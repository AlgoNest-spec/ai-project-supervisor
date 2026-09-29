"""Validate the self-contained, synthetic AI Project Supervisor scenario."""
from __future__ import annotations

import json
from pathlib import Path

SCENARIO = Path(__file__).parents[1] / "examples" / "project-team-scenario.json"

def main() -> None:
    scenario = json.loads(SCENARIO.read_text(encoding="utf-8"))
    tasks = {task["id"]: task for task in scenario["tasks"]}
    assert len(tasks) == len(scenario["tasks"]), "task IDs must be unique"
    assert all(dep in tasks for task in tasks.values() for dep in task["depends_on"]), "unknown dependency"

    indegree = {key: len(task["depends_on"]) for key, task in tasks.items()}
    children = {key: [] for key in tasks}
    for key, task in tasks.items():
        for dep in task["depends_on"]:
            children[dep].append(key)
    ready = [key for key, degree in indegree.items() if degree == 0]
    visited = 0
    while ready:
        done = ready.pop()
        visited += 1
        for child in children[done]:
            indegree[child] -= 1
            if indegree[child] == 0:
                ready.append(child)
    assert visited == len(tasks), "dependency graph contains a cycle"

    duplicate = scenario["duplicate_request"]
    assert duplicate["same_canonical_input_hash"]
    assert "do not launch duplicate" in duplicate["expected_action"]
    failure = scenario["failure"]
    assert failure["retry_limit"] == 1
    assert failure["independent_task_to_continue"] in tasks
    assert "unresolved" in scenario["conflict"]["expected_action"]
    assert scenario["expected_final_status"].startswith("INCOMPLETE")
    print("PASS: standalone supervisor scenario dependencies, deduplication, bounded retry, and conflict gate")

if __name__ == "__main__":
    main()
