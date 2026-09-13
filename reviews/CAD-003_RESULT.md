# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The latest constant-X rerun is directionally correct and exposed a small, solvable clearance conflict rather than a product-level decision.

Codex reports the nominal blue-shield partition at `X = 65.0 mm` gives **3.40037 mm minimum moving clearance at 0°**, below the required `CATCH_SWEEP_CLEAR = 4.0 mm` by **0.59963 mm**.

This does **not** require owner escalation. Resolve it within CAD-003 by adjusting only the shield's Y-direction leading-edge setback / local relief while preserving the frozen hinge axis, approved door/catch, and nominal shield X position.

## Frozen geometry — do not change

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm`.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm`.
- Hinge axis direction = Z.
- Blue-shield partition nominal plane = `X = 65.0 mm`.
- CAD-001 door and CAD-002 U-catch remain unchanged.

## Required correction

1. Keep the constant-X Y-Z blue-shield partition at nominal `X = 65.0 mm`.
2. Keep the corrected local Y-Z U-catch relief concept; do not revert to the superseded 119 mm constant-Y wall/opening.
3. Increase `BLUE_SHIELD_FRONT_SETBACK` only along +Y as little as practical until the full sampled 0°–90° motion clears the shield by at least 4.0 mm.
4. For review robustness, target **at least 4.5 mm measured minimum clearance** rather than stopping numerically at exactly 4.000 mm. The governing fabrication requirement remains 4.0 mm minimum.
5. Start by moving the current shield leading edge rearward by approximately **1.1 mm** (0.59963 mm shortfall + ~0.5 mm review margin), then remeasure; derive/fine-tune the exact setback from Fusion rather than hard-coding the estimate if geometry makes the relationship non-linear.
6. Preserve as much front shielding as possible. Do not enlarge the opening or move the whole shield farther rearward than needed once the >=4.5 mm review target is achieved.
7. Re-evaluate 0°, 15°, 30°, 45°, 60°, 75°, and 90° and report the final front-setback Y, local opening Y/Z extents, closest angle, and measured minimum clearance.
8. If achieving >=4.0 mm still forces a major opening, essentially consumes the 25 mm lock/shield zone, or creates a straight tenant tool path, stop with `HUMAN_DECISION_REQUIRED`.
9. Otherwise regenerate evidence, update `CAD_LOG.md` and `handoff/CAD-003.json` to `READY_FOR_DESIGN_REVIEW`, push `cad/CAD-003`, and stop.
10. Do not start CAD-004.

## Acceptance checks

- Frozen 5 mm / 5 mm hinge axis preserved.
- Blue shield remains the constant-X service-side partition at nominal X = 65 mm.
- Only the local relief / Y-direction front setback is adjusted to solve the 3.40037 mm conflict.
- Final measured minimum clearance >= 4.0 mm; review target >= 4.5 mm.
- Front shielding is not reduced more than required.
- CAD-001 and CAD-002 remain unchanged and healthy.
- No CAD-004 geometry is added.

## Hold

CAD-004 remains blocked until this corrected CAD-003 evidence is reviewed and approved.
