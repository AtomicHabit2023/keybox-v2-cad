# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The latest constant-X rerun is directionally correct, but the reported **3.40037 mm** value must be interpreted correctly before changing geometry.

The U-catch is intentionally supposed to cross the blue-shield partition at `X = 65.0 mm` through a **local laser-cut Y-Z opening**, then enter the protected lock zone and engage the XG-07A hook. Therefore the design goal is **not** to keep the U-catch 4 mm away from the whole shield plane.

The governing 4.0 mm clearance is the minimum distance between the moving U-catch and the **boundary of the modeled local opening / remaining shield material** throughout the door sweep.

If the reported 3.40037 mm was measured to an uncut/full shield slab at a location where the U-catch is supposed to pass through, that is not a valid acceptance measurement and must not be solved merely by moving the shield backward. First model/confirm the intended local pass-through relief, then measure clearance to its edges.

## Frozen geometry — do not change

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm`.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm`.
- Hinge axis direction = Z.
- Blue-shield partition nominal plane = `X = 65.0 mm`.
- CAD-001 door and CAD-002 U-catch remain unchanged.

## Required correction / verification

1. Keep the constant-X Y-Z blue-shield partition at nominal `X = 65.0 mm`.
2. Keep the frozen 5 mm / 5 mm hinge axis and approved U-catch unchanged.
3. Explicitly model the local Y-Z laser-cut pass-through through which the U-catch crosses the 1.2 mm shield slab on its way into the lock zone.
4. Derive that relief only from the portion of the moving U-catch envelope that intersects or approaches the shield slab during 0°–90° motion; do not project the entire sweep.
5. Measure minimum distance from the moving U-catch to the **opening edges / remaining shield material**, not to the removed opening volume or to an uncut full shield plane.
6. Required minimum edge clearance = `CATCH_SWEEP_CLEAR = 4.0 mm`; target >=4.5 mm for review robustness where practical.
7. Adjust `BLUE_SHIELD_FRONT_SETBACK` along +Y only if the modeled opening-edge clearance actually requires it. Do not automatically move the shield rearward based solely on the old 3.40037 mm full-plane measurement.
8. Preserve as much front shielding as possible and keep the opening local enough that it does not create a direct tenant tool path into wiring/emergency-release areas.
9. Re-evaluate 0°, 15°, 30°, 45°, 60°, 75°, and 90° and report the local opening Y/Z extents, front-setback Y, closest angle, and minimum clearance to the opening boundary / remaining shield.
10. If the required opening consumes essentially the whole 25 mm lock/shield zone or cannot maintain >=4.0 mm edge clearance without compromising security, stop with `HUMAN_DECISION_REQUIRED`.
11. Otherwise regenerate evidence, update `CAD_LOG.md` and `handoff/CAD-003.json` to `READY_FOR_DESIGN_REVIEW`, push `cad/CAD-003`, and stop.
12. Do not start CAD-004.

## Acceptance checks

- Frozen 5 mm / 5 mm hinge axis preserved.
- Blue shield remains the constant-X service-side partition at nominal X = 65 mm.
- U-catch intentionally crosses through a local Y-Z laser-cut opening into the lock zone.
- Clearance is measured to the opening edges / remaining shield material.
- Final measured minimum edge clearance >=4.0 mm; review target >=4.5 mm where practical.
- Opening remains local and security shielding is preserved.
- CAD-001 and CAD-002 remain unchanged and healthy.
- No CAD-004 geometry is added.

## Hold

CAD-004 remains blocked until this corrected CAD-003 evidence is reviewed and approved.
