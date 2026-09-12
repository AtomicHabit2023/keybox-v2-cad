# CAD-001 Design Review

**Review status:** CHANGES REQUIRED  
**Design authority:** ChatGPT / project-design conversation  
**Reviewed checkpoint:** `93bb356aac7aac63e48f8a53af0fcd691be8e168`  
**CAD-002:** BLOCKED until CAD-001R is re-reviewed and approved.

## What is accepted from the checkpoint

The following parts of CAD-001 are accepted as the correct direction and should be preserved unless the required correction forces a rebuild:

- one true Fusion sheet-metal body;
- 1.2 mm hot-rolled-steel design thickness;
- starting sheet-metal rule R1.5 mm / K-factor 0.42;
- 10 mm top inward hinge flange;
- 10 mm bottom inward hinge flange;
- 12 mm first latch-side inward flange;
- 25 mm second latch-side return;
- all four bends at 90 degrees and directed inward toward the tenant compartment;
- current corner relief is acceptable as a prototype starting point, subject to later fabrication calibration;
- flat pattern generation is healthy;
- no U-catch, shield, lock, shim, hinge rod, or 48-copy pattern was added before the stop gate.

## Required correction

The checkpoint interpreted `DOOR_FACE_W = 87.5 mm` and `DOOR_FACE_H = 47.0 mm` as the **complete formed front projection including bend zones**. That is not the approved design intent.

**Approved definition:**

`DOOR_FACE_W = 87.5 mm` and `DOOR_FACE_H = 47.0 mm` are the dimensions of the **flat planar visible front face between the bend tangency/bend-start lines**.

The current checkpoint reports the largest uninterrupted planar front region as only **84.8 × 41.6 mm**, so CAD-001 does not yet satisfy the approved door-face requirement.

## CAD-001R instruction

Revise only the master door/folds geometry so that:

1. the planar visible front face measures **87.5 mm wide × 47.0 mm high** between the bend-start/tangency boundaries;
2. the 10 mm top and bottom flanges remain inward;
3. the 12 mm first latch flange remains inward;
4. the 25 mm second return remains the hidden return that will later carry the U-catch;
5. the body remains valid sheet metal and still produces a valid flat pattern;
6. no bend or relief self-intersects;
7. after correcting the planar face, measure the **actual formed overall envelope** and report it separately;
8. compare that formed envelope against the **90 mm × 50 mm cell pitch**. If any formed portion would interfere with the neighboring row/column or violate the intended door gaps, **STOP and report the conflict; do not change the approved 87.5 × 47.0 planar-face dimensions without design-authority approval**;
9. do not add U-catch, blue shield, red wall, XG-07A, shim, hinge rod, or any patterned copies.

## Dimension terminology to use from now on

- **Door face:** flat planar front face between bend tangencies; target 87.5 × 47.0 mm.
- **Formed envelope:** maximum outside bounds of the complete folded door; this is a reported/check dimension, not the definition of `DOOR_FACE_W/H`.
- **Cell pitch:** 90 × 50 mm structural pitch; formed envelope must be checked against it.

## Review gate for CAD-001R

Return for review with:

- front / top / isometric screenshots;
- exact planar-face measurement;
- exact formed-envelope measurement;
- sheet-metal feature health;
- flat-pattern health;
- explicit clearance/interference statement relative to the 90 × 50 mm cell pitch;
- updated `.f3d` checkpoint and machine-readable measurement file.

Do **not** start CAD-002 until this review file is superseded by an explicit `CAD-001 APPROVED` decision.
