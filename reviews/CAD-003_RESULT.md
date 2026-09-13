# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The owner has resolved the prior hinge-axis decision. CAD-003 is **not yet approved** because the submitted sweep used the wrong shield-front orientation and the old provisional hinge axis, but the corrected rerun is now fully specified.

## Frozen hinge-axis definition

Use the shared door hinge axis as follows:

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm` from the hinge-side door edge,
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm` behind the front-face plane,
- axis direction = Z,
- Ø4.6 mm door guide holes centered on this axis,
- Ø4.0 mm hinge rod remains the hardware reference.

These values are now controlling project parameters and are no longer TBD.

## Required CAD-003 correction

Correct only CAD-003 while preserving approved CAD-001 and CAD-002 geometry unchanged:

1. Replace the provisional sweep axis with the frozen 5.0 mm / 5.0 mm Z axis above.
2. Rebuild the blue shield **front** as an X-Z face at a derived constant-Y position. The U-catch projects along Y, so the pass-through/relief must be cut in this constant-Y front face.
3. Derive the shield-front Y setback and the relief/opening from the real moving U-catch envelope, not from the closed position alone.
4. Keep at least `CATCH_SWEEP_CLEAR = 4.0 mm` minimum clearance at the closest moving approach.
5. Re-evaluate 0°, 15°, 30°, 45°, 60°, 75°, and 90°. A conservative sampled-angle method is acceptable; a true swept-body method is preferred if reliable.
6. Record the frozen hinge-axis coordinates, shield-front constant-Y position, opening width and height, closest angle, and measured minimum clearance.
7. Preserve the approved door and U-catch without redesign.
8. Do not add XG-07A lock body, shim, red wall, final/full hinge hardware, or patterned rows/columns.
9. Regenerate front/top/isometric and sweep evidence, update `CAD_LOG.md` and `handoff/CAD-003.json` to `READY_FOR_DESIGN_REVIEW`, push `cad/CAD-003`, and stop.

## Acceptance checks

- Hinge axis uses the frozen 5.0 mm edge offset and 5.0 mm front/depth offset.
- Shield front is a constant-Y X-Z face, not the previous constant-X Y-Z side plane.
- Relief is derived from the moving catch envelope.
- Minimum moving clearance is at least 4.0 mm.
- CAD-001 and CAD-002 remain unchanged and healthy.
- No CAD-004 geometry is added.

## Hold

CAD-004 remains blocked until the corrected CAD-003 evidence is reviewed and approved.
