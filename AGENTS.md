# AGENTS.md — KeyBox V2 CAD operating contract

This repository is a controlled CAD collaboration between:

- **ChatGPT** — project designer and design authority.
- **Codex** — CAD execution agent operating Autodesk Fusion 360 through Fusion MCP.
- **Owner** — final business/product owner and physical-world operator; should only be asked for decisions that genuinely require human judgment, measurements, purchases, fabrication, or approval of material/product tradeoffs.

## Read order before every CAD task

1. `AGENTS.md`
2. `CAD_REVIEW_PROTOCOL.md`
3. latest applicable `reviews/*_CORRECTION.md` or `reviews/*_RESULT.md`
4. `CAD_MASTER_SPEC.md`
5. `PARAMETERS.json`
6. `DESIGN_DECISIONS.md`
7. `CAD_TASKS.md`
8. latest entries in `CAD_LOG.md`

If any documents conflict, the **latest explicit design-authority correction/result for that task wins**. Do not silently reconcile contradictions.

## Hard rules

- Never redesign a requirement without an explicit design-authority instruction.
- Never call geometry approved merely because Fusion accepted it.
- Never pattern the full 48-door cabinet before the master-cell gates are approved.
- Use named parameters for repeated functional dimensions.
- Keep critical folded parts as real sheet-metal geometry whenever Fusion supports it.
- Preserve checkpoints before risky changes.
- Do not use the superseded inaccurate Phase-2 latch reference geometry as fabrication geometry.
- `87.5 × 47.0 mm` is the **maximum complete formed door envelope**. The uninterrupted planar center face is derived.

## Branch / handoff workflow

For each new CAD stage after CAD-001 closure:

1. Synchronize `main` through the KeyBox Git Bridge.
2. Work on branch `cad/CAD-###` (for example `cad/CAD-002`).
3. Modify Fusion only within the current task scope.
4. At the stop gate, save Fusion and generate the required evidence.
5. Update `CAD_LOG.md` and create/update `handoff/CAD-###.json` with status `READY_FOR_DESIGN_REVIEW`.
6. Stage and commit only the task/evidence/handoff files intended for review.
7. Push the task branch using the **KeyBox Git Bridge MCP**, not direct shell/network Git inside the Codex sandbox.
8. Stop CAD work while awaiting design-authority response.

The design authority will review the pushed branch/PR and write `reviews/CAD-###_RESULT.md` with one of:

- `APPROVED`
- `CHANGES_REQUIRED`
- `HUMAN_DECISION_REQUIRED`

After the result becomes available, pull it through the Git Bridge. Proceed only as instructed.

## Human escalation rule

Do not involve the owner merely to relay text between Codex and ChatGPT. Escalate only when the answer requires something the two agents cannot establish from CAD/repository evidence, such as a physical measurement, shop capability, cost quote, hardware sample, installation constraint, or a product/business tradeoff.

## Git safety

Use only the tools exposed by `tools/keybox_git_bridge/server.py` for network Git operations. The bridge is intentionally restricted to this repository and intentionally blocks direct pushes to `main`.
