# KeyBox V2 CAD

Shared design workspace for the 48-door KeyBox V2 mechanical/CAD project.

## Working model

- **ChatGPT**: project designer / design authority. Maintains requirements, parameters, design decisions, review gates, corrections, and approvals.
- **Codex**: CAD execution agent. Uses Fusion 360 through MCP to build, measure, test, and report the actual model.
- **Fusion 360**: authoritative geometric/interference environment.
- **GitHub**: shared source of truth and agent-to-agent handoff channel.
- **Owner**: product/business owner and physical-world operator; should not be used as a routine message courier between ChatGPT and Codex.

## Read these first

1. `AGENTS.md`
2. `CAD_REVIEW_PROTOCOL.md`
3. latest applicable files under `reviews/`
4. `CAD_MASTER_SPEC.md`
5. `PARAMETERS.json`
6. `DESIGN_DECISIONS.md`
7. `CAD_TASKS.md`
8. `CAD_LOG.md`

## Direct agent workflow

From CAD-002 onward, Codex works on one task branch such as `cad/CAD-002`, saves Fusion evidence, writes `handoff/CAD-002.json`, commits and pushes through the restricted **KeyBox Git Bridge MCP**, and stops at the review gate.

ChatGPT reviews the pushed branch/PR and returns one of `APPROVED`, `CHANGES_REQUIRED`, or `HUMAN_DECISION_REQUIRED` in `reviews/CAD-###_RESULT.md`.

The owner is asked only when a physical measurement, fabrication-shop fact, purchase/cost fact, installation constraint, or product/business tradeoff genuinely requires a human decision.

See `CAD_REVIEW_PROTOCOL.md` for the full contract.

## KeyBox Git Bridge MCP

`tools/keybox_git_bridge/` contains a restricted local MCP server for Git fetch/pull/branch/stage/commit/push operations. It runs in the normal Windows user context so Git can use the owner's existing SSH setup, while Codex never receives direct access to the private SSH key. Direct pushes to `main` are blocked by the bridge.

## Current CAD status

- Phase-1 parameter/reference geometry was successfully created in Fusion 360.
- The earlier Phase-2 master latch reference was geometrically inaccurate and is **superseded**.
- CAD-001 has been restored to the correct baseline: maximum complete formed door envelope `87.5 × 47.0 mm`; the planar center face is derived (restored baseline about `84.8 × 41.6 mm`).
- CAD-002 remains blocked until CAD-001's final evidence checkpoint is explicitly approved.

## Manufacturing philosophy

Design for ordinary Thai laser-cut / press-brake / welding shops, not specialized tooling. Keep the product parametric, self-jigging, low-part-count, serviceable, and inexpensive to fabricate. Critical repeated dimensions must come from named parameters, never duplicated hard-coded values.
