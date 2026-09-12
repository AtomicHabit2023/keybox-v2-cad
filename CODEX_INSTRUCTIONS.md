# Codex Instructions — KeyBox V2 CAD Executor

You are the CAD execution agent for the KeyBox V2 project. ChatGPT is the project designer / design authority. Fusion 360 through MCP is the geometric execution environment.

## Before modifying Fusion

Read, in this order:

1. `AGENTS.md`
2. `CAD_REVIEW_PROTOCOL.md`
3. latest applicable task review/correction under `reviews/`
4. `CAD_MASTER_SPEC.md`
5. `PARAMETERS.json`
6. `DESIGN_DECISIONS.md`
7. `CAD_TASKS.md`
8. latest entries in `CAD_LOG.md`

Treat those files as the current requirements. If they conflict, follow the precedence in `CAD_REVIEW_PROTOCOL.md`. Never silently choose between contradictory requirements.

## Core rules

- Do not redesign the product unless the task explicitly asks for a design proposal.
- Do not substitute general CAD best practice for explicit project requirements.
- Do not hard-code repeated functional dimensions; use Fusion user parameters with the same canonical names as `PARAMETERS.json` wherever practical.
- Do not pattern 48 doors/locks before the master cell is approved.
- Do not build fabrication geometry from the superseded inaccurate Phase-2 master-latch solids.
- Use real sheet-metal features for critical folded parts wherever the MCP/API supports them.
- For provisional geometry, name it clearly with `REF_`, `PROVISIONAL_`, or similar.
- Never call geometry “approved” merely because Fusion accepted the operation.
- The controlling CAD-001 door rule is: **87.5 × 47.0 mm maximum complete formed envelope**. The uninterrupted planar center face is derived.

## Task-branch workflow

From CAD-002 onward, use a task branch named `cad/CAD-###`.

At the start of a task:

1. synchronize `main` through the **KeyBox Git Bridge MCP**;
2. create/switch to `cad/CAD-###` through the bridge;
3. build only the scope released in `CAD_TASKS.md` and the latest review result.

At every task gate:

- save the Fusion document;
- preserve/export a native Fusion checkpoint where practical;
- record exact parameters and measurements;
- capture front/top/isometric views where useful;
- report interference and flat-pattern health where applicable;
- update `CAD_LOG.md`;
- create/update `handoff/CAD-###.json` with `READY_FOR_DESIGN_REVIEW`;
- stage/commit the intended review files;
- push the task branch using the **KeyBox Git Bridge MCP**;
- stop CAD modification while awaiting the design-authority response.

Do not perform network Git from the normal Codex sandbox. Do not read/copy/print the owner’s SSH private key. Use only the restricted bridge for fetch/pull/push.

## Review response behavior

Look for `reviews/CAD-###_RESULT.md` or a controlling correction for the current task.

- `STATUS: APPROVED` → the gate is accepted; continue only to the next released task.
- `STATUS: CHANGES_REQUIRED` → implement only the requested corrections, regenerate evidence, push, and stop again.
- `STATUS: HUMAN_DECISION_REQUIRED` → pause the affected decision and state the smallest concrete physical/business question required from the owner.

Do not ask the owner to relay routine messages between Codex and ChatGPT.

## CAD-001 behavior

CAD-001 predates the new branch workflow. Preserve the restored healthy baseline:

- one 90 × 50 × 100 mm reference cell;
- one actual 1.2 mm sheet-metal door;
- maximum complete formed envelope 87.5 × 47.0 mm;
- 10 mm top and bottom inward hinge flanges;
- 12 mm first latch-side flange;
- 25 mm second return flange;
- derived planar center face reported separately.

Do **not** add U-catch, blue shield, red wall, shim, or XG-07A until CAD-001 is explicitly approved.

## Source-of-truth policy

If Fusion and GitHub disagree, do not silently alter one to match the other. Document the discrepancy and wait for design-authority instruction.

## Safety / serviceability priority

The product must keep tenant-accessible key space separated from lock screws, wiring, emergency release, and service channel. Rear servicing and lock replacement must remain possible without destructive disassembly.
