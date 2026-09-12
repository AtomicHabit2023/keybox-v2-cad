# CAD Review Protocol — ChatGPT ↔ Codex

Purpose: remove the owner from routine message relaying while preserving explicit design-control gates.

## Roles

**Codex / Fusion executor** builds and measures the CAD. It does not invent design requirements.

**ChatGPT / design authority** reviews evidence against the specification, issues corrections, approves gates, and releases the next task.

**Owner** is involved only for physical-world facts or real product/business choices that cannot be resolved from the repository and Fusion model.

## Task branches

Use one branch per CAD stage:

`cad/CAD-001`, `cad/CAD-002`, `cad/CAD-003`, ...

Do not mix two CAD stages in one branch unless the design authority explicitly says so.

## Review handoff file

At each stop gate, Codex writes:

`handoff/CAD-###.json`

Recommended schema:

```json
{
  "task": "CAD-002",
  "status": "READY_FOR_DESIGN_REVIEW",
  "branch": "cad/CAD-002",
  "fusion_document": "KeyBox_V2_CAD002_UCatch",
  "head_sha": "<filled after commit if practical>",
  "summary": "What was built",
  "evidence": [
    "evidence/CAD002/front.png",
    "evidence/CAD002/top.png",
    "evidence/CAD002/isometric.png",
    "evidence/CAD002/MEASUREMENTS.json"
  ],
  "checks": {
    "sheet_metal_health": "PASS",
    "interference": "PASS/FAIL/NOT_APPLICABLE",
    "flat_pattern": "PASS/FAIL/NOT_APPLICABLE"
  },
  "deviations": [],
  "questions_for_design_authority": []
}
```

After writing the handoff, Codex commits and pushes the task branch using the KeyBox Git Bridge MCP and stops modifying Fusion.

## Pull-request review gate

A review PR should be titled:

`[CAD-###] <short task name>`

Base branch: `main`

Head branch: `cad/CAD-###`

The PR is the design-review container. It must include the Fusion checkpoint where practical, screenshots, machine-readable measurements, updated `CAD_LOG.md`, and the handoff JSON.

## Design-authority response

The design authority reviews the branch/PR against the current source of truth and writes:

`reviews/CAD-###_RESULT.md`

The first non-heading line must be one of:

`STATUS: APPROVED`

`STATUS: CHANGES_REQUIRED`

`STATUS: HUMAN_DECISION_REQUIRED`

### APPROVED

- The gate is accepted.
- The design authority may merge the PR.
- The next CAD task may be released/unblocked.

### CHANGES_REQUIRED

- The result file must state exact corrections and acceptance checks.
- Codex modifies only the current task branch, regenerates evidence, pushes, and returns to the review gate.

### HUMAN_DECISION_REQUIRED

- The result file states the smallest concrete question that needs the owner.
- Codex and ChatGPT pause only the affected decision; unrelated approved work should not be reopened.

## Source-of-truth precedence

For a given task, use this order:

1. latest `reviews/CAD-###_CORRECTION.md` or `reviews/CAD-###_RESULT.md` explicitly marked controlling;
2. `DESIGN_ERRATA.md`;
3. `CAD_MASTER_SPEC.md`;
4. `PARAMETERS.json`;
5. `DESIGN_DECISIONS.md`;
6. `CAD_TASKS.md`;
7. `CAD_LOG.md` and evidence notes.

If a lower-priority document conflicts with a higher-priority one, log it and follow the higher-priority instruction.

## Current CAD-001 migration note

CAD-001 began before this branch/PR protocol existed. Finish its corrected baseline and evidence checkpoint without redoing healthy geometry. From **CAD-002 onward**, use this protocol by default.

## No-courier principle

The owner should not have to copy routine review messages between agents. Codex communicates through task branches/handoff files; ChatGPT communicates through PR reviews and `reviews/CAD-###_RESULT.md`. The owner is reserved for real-world facts and decisions.
