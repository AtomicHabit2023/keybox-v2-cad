# KeyBox V2 CAD

Shared design workspace for the 48-door KeyBox V2 mechanical/CAD project.

## Working model

- **ChatGPT**: project designer / design authority. Maintains requirements, parameters, design decisions, review gates, and acceptance criteria.
- **Codex**: CAD execution agent. Uses Fusion 360 through MCP to build, measure, test, and report the actual model.
- **Fusion 360**: authoritative geometric model and interference-check environment.
- **GitHub**: shared source of truth for requirements, tasks, logs, and review results.

Codex must not invent mechanical requirements when the specification is ambiguous. It should stop, document the ambiguity, and request a design decision.

## Read these first

1. `CODEX_INSTRUCTIONS.md`
2. `CAD_MASTER_SPEC.md`
3. `PARAMETERS.json`
4. `DESIGN_DECISIONS.md`
5. `CAD_TASKS.md`

`CAD_LOG.md` is the running execution/review log.

## Current CAD status

Phase-1 parameter/reference geometry was successfully created in Fusion 360, but the earlier Phase-2 master latch cell was geometrically inaccurate and is **superseded**. Do not build on that Phase-2 cell.

The next approved work is **CAD-001: rebuild one master door/latch cell step-by-step, stopping after the door and its 12 mm + 25 mm latch-side folds for design review before adding the U-catch or lock**.

## Manufacturing philosophy

Design for ordinary Thai laser-cut / press-brake / welding shops, not specialized tooling. Keep the product parametric, self-jigging, low-part-count, serviceable, and inexpensive to fabricate. Critical repeated dimensions must come from named parameters, never duplicated hard-coded values.
