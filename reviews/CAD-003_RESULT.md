# CAD-003 Design Authority Result

STATUS: HUMAN_DECISION_REQUIRED

## Decision

CAD-003 is **not approved yet**. The evidence shows that Codex completed a sampled sweep and produced a lightweight shield reference, but the current analysis does not yet represent the intended physical blue-shield/front-pass-through geometry and it uses an unfrozen hinge axis.

## Issue 1 — blue-shield front plane is modeled in the wrong orientation

The approved coordinate convention in the CAD evidence is:

- X = door width,
- Y = compartment depth / U-catch projection direction,
- Z = door height.

The approved U-catch projects from the catch plate along +Y. Therefore the blue shield **front** that the U-catch must pass through must be represented by an X-Z plane at a constant Y position (with its relief/opening cut in that front face).

The submitted CAD-003 evidence instead places the shield on `fixedPlaneLocalX = 50 mm`, spanning Y-Z. That is a side/divider plane, not the front pass-through plane described by the design. The reported 11.80053 mm minimum distance therefore does not validate the real U-catch-through-shield-front motion.

## Issue 2 — hinge axis is still provisional / unfrozen

The sweep was performed about local `X = 0, Y = 0`, direction Z. However `HINGE_AXIS_FRONT_OFFSET` and `HINGE_AXIS_EDGE_OFFSET` are still TBD in the project parameters. The true U-catch swept envelope depends directly on this axis location, so CAD-003 cannot be approved as a true physical sweep until the shared Ø4 mm hinge-rod axis is frozen.

## Owner/design-authority decision required

Recommended starting hinge-axis definition for the 10 mm inward top/bottom door flanges:

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm` from the hinge-side door edge,
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm` behind the front-face plane,
- axis direction = Z,
- Ø4.6 mm door guide holes centered on that axis.

This centers the rod within the 10 mm inward flange in depth and leaves symmetric nominal material around the Ø4.6 guide hole at the hinge-side corner. The owner must approve or change these two offsets before Codex reruns the motion study.

## What remains valid from the submitted CAD-003 work

- CAD-001 door and CAD-002 U-catch were preserved unchanged.
- Seven motion samples were generated at 0, 15, 30, 45, 60, 75, and 90 degrees.
- No CAD-004 hardware was added.
- The lightweight-reference / sampled-angle workflow is acceptable for the corrected rerun.

## Required rerun after hinge-axis decision

After the hinge-axis offsets are frozen, correct CAD-003 only:

1. use the frozen Z hinge axis;
2. rebuild the blue shield **front** as an X-Z face at a derived constant-Y setback;
3. derive the U-catch relief/opening from the moving swept envelope plus at least 4.0 mm clearance;
4. remeasure the minimum clearance at the required sample angles;
5. record the shield-front Y position, opening width/height, closest angle, and minimum clearance;
6. preserve approved CAD-001/CAD-002 geometry;
7. push corrected `cad/CAD-003` and stop.

CAD-004 remains blocked.
