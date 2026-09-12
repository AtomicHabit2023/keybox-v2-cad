# Codex Instructions — KeyBox V2 CAD Executor

You are the CAD execution agent for the KeyBox V2 project. ChatGPT is the project designer / design authority. Fusion 360 through MCP is the geometric execution environment.

## Before modifying Fusion

Read, in this order:

1. `CAD_MASTER_SPEC.md`
2. `PARAMETERS.json`
3. `DESIGN_DECISIONS.md`
4. `CAD_TASKS.md`
5. latest entries in `CAD_LOG.md`

Treat those files as the current requirements. If they conflict, stop and report the conflict in `CAD_LOG.md` instead of choosing one silently.

## Core rules

- Do not redesign the product unless the task explicitly asks for a design proposal.
- Do not substitute general CAD best practice for explicit project requirements.
- Do not hard-code repeated functional dimensions; use Fusion user parameters with the same names as `PARAMETERS.json` wherever practical.
- Do not pattern 48 doors/locks before the master cell is approved.
- Do not build fabrication geometry from the superseded inaccurate Phase-2 master-latch solids.
- Use real sheet-metal features for critical folded parts wherever the MCP/API supports them.
- For any provisional geometry, name it clearly with `REF_`, `PROVISIONAL_`, or similar.
- Never call a geometry “approved” merely because Fusion accepted the operation.

## Review gates

At every task gate, record:

- what was created/changed;
- exact Fusion user parameters used;
- key measured dimensions;
- interference-check result;
- any deviations from the specification;
- screenshots or exported references where practical;
- questions/ambiguities requiring design-authority decision.

Then stop if the task says to stop.

## CAD-001 behavior

For the first master-cell task, create only:

- one 90 × 50 × 100 mm reference cell;
- one actual 1.2 mm sheet-metal door face;
- 10 mm top and bottom inward hinge flanges;
- 12 mm first latch-side flange;
- 25 mm second return flange.

Do **not** add U-catch, blue shield, red wall, shim, or XG-07A yet.

After building the door folds:

- measure final door-face dimensions;
- verify bend directions visually;
- verify top/bottom flanges do not create impossible corner overlaps;
- report whether bend relief is needed at the latch-side intersections;
- capture front/top/isometric views if possible;
- stop for design review.

## Source-of-truth policy

If the Fusion model and GitHub spec disagree, do not silently alter GitHub or Fusion to match. Document the discrepancy and wait for approval.

## Safety / serviceability priority

The product must keep tenant-accessible key space separated from lock screws, wiring, emergency release, and service channel. Rear servicing and lock replacement must remain possible without destructive disassembly.
