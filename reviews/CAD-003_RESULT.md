# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The corrected rerun successfully used the frozen 5.0 mm / 5.0 mm hinge axis, but CAD-003 is **not approved yet**.

The submitted rerun created a constant-Y X-Z shield face at Y = 43.5 mm with a 119 x 43 mm relief extending from X = -39 mm to X = 80 mm. That opening is wider than the 90 mm compartment pitch and therefore cannot represent the intended local protective shield geometry.

This exposed a design-authority interpretation error in the previous rerun instruction: the project master specification describes the blue shield as the protective partition between the 65 mm key space and the 25 mm lock/shield zone adjacent to the service channel, with a CAD-derived **front setback along depth** and a local U-catch pass-through. Its primary shield plane is therefore a constant-X Y-Z partition, not a full constant-Y front wall.

The previous constant-Y instruction is superseded by this result and by `DESIGN_ERRATA.md` E-002.

## Frozen hinge-axis definition — remains approved

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm` from the hinge-side door edge.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm` behind the front-face plane.
- Axis direction = Z.
- Ø4.6 mm guide holes centered on that axis for the Ø4.0 mm rod reference.

Do not change the hinge axis in the next rerun.

## Correct blue-shield interpretation

Use the existing master-cell width allocation:

- `KEY_SPACE_W = 65.0 mm`
- `LOCK_ZONE_W = 25.0 mm`
- nominal blue-shield partition plane: `X = KEY_SPACE_W = 65.0 mm`
- sheet thickness: 1.2 mm, extending into the lock-zone side unless Fusion construction requires an equivalent centered reference.

The term `BLUE_SHIELD_FRONT_SETBACK` means the **leading edge of this constant-X shield along +Y compartment depth**. It does not mean a separate constant-Y wall across the whole compartment.

## Required CAD-003 rerun

Correct only CAD-003 while preserving approved CAD-001 and CAD-002 geometry unchanged:

1. Keep the frozen hinge axis at local X = 5.0 mm, Y = 5.0 mm, direction Z.
2. Replace the 119 mm constant-Y shield-front concept with a lightweight constant-X Y-Z blue-shield partition at nominal X = 65.0 mm.
3. Evaluate the moving U-catch at 0°, 15°, 30°, 45°, 60°, 75°, and 90°.
4. Derive the **local Y-Z pass-through opening from the part of the moving U-catch envelope that actually intersects or approaches the 1.2 mm shield slab at X = 65 mm**. Do not project the entire 0–90° sweep onto the shield plane.
5. Add at least `CATCH_SWEEP_CLEAR = 4.0 mm` around the relevant moving envelope at the shield.
6. Derive `BLUE_SHIELD_FRONT_SETBACK` along Y from the corrected sweep. Preserve as much front shielding as possible while guaranteeing motion clearance.
7. Report: shield X position, front-setback Y, opening Y range/depth, opening Z range/height, closest door angle, and minimum measured clearance.
8. If the required opening consumes essentially the whole 25 mm lock/shield zone, creates an unavoidable straight tenant tool path, or cannot maintain 4 mm clearance, stop with `HUMAN_DECISION_REQUIRED`; do not enlarge the opening outside the 90 mm cell or redesign CAD-001/CAD-002 silently.
9. Do not add XG-07A lock body, shim, red wall, final hinge hardware, or patterned rows/columns.
10. Regenerate the review evidence, update `CAD_LOG.md` and `handoff/CAD-003.json` to `READY_FOR_DESIGN_REVIEW`, push `cad/CAD-003`, and stop.

## Acceptance checks

- Frozen 5 mm / 5 mm hinge axis preserved.
- Blue shield represented as the service-side partition at nominal X = 65 mm.
- `BLUE_SHIELD_FRONT_SETBACK` is a Y-direction leading-edge setback.
- Relief/opening is a local Y-Z opening derived only from the catch envelope at the shield, not the full sweep projection.
- Opening remains geometrically local to the 90 mm cell / 25 mm lock zone.
- Minimum moving clearance is at least 4.0 mm.
- CAD-001 and CAD-002 remain unchanged and healthy.
- No CAD-004 geometry is added.

## Hold

CAD-004 remains blocked until the corrected CAD-003 shield/sweep geometry is approved.
