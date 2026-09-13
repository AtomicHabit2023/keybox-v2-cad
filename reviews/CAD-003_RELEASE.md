# CAD-003 Design Authority Release

STATUS: READY / RELEASED

## Purpose

Validate the real moving path of the already-approved CAD-001 door + CAD-002 U-catch and derive the minimum blue-shield front relief that cannot repeat the V1 collision failure.

## Preserve unchanged

- CAD-001 formed door baseline.
- CAD-002 U-catch geometry and placement.
- 20.0 x 34.5 x 1.5 mm catch plate.
- 2 x Ø4.2 mounting holes at 25.0 mm vertical centers.
- Horizontal Ø3.0 loop legs at 14.0 mm centers (17.0 mm outside width, 11.0 mm clear inside).
- 26 mm nominal loop projection.
- 5.0 mm catch edge inset.

## Token-efficient CAD procedure

1. Synchronize refreshed `main`, then create/switch to `cad/CAD-003`.
2. Save a new Fusion checkpoint before changing geometry.
3. Use only a lightweight construction hinge axis / reference needed to rotate the approved door. Do not build the final full-height hinge system in this task.
4. Keep the blue shield lightweight and parametric: only the front/adjacent geometry required to evaluate tenant protection and U-catch passage. Do not add cosmetic details, tabs, fasteners, or downstream lock hardware yet.
5. Evaluate the door/U-catch motion from closed to 90 degrees open. At minimum record interference/clearance at 0, 15, 30, 45, 60, 75, and 90 degrees. Use a true swept-body/envelope method if Fusion can generate it reliably without damaging the approved geometry; otherwise use the sampled-angle union/envelope conservatively and state the method.
6. Derive the blue-shield front opening/relief from the moving U-catch envelope plus `CATCH_SWEEP_CLEAR = 4.0 mm` minimum safety allowance. The shield must not be sized only from the static closed position.
7. Report the closest moving approach, its door angle, measured clearance, relief/opening dimensions, and the reference hinge-axis offsets used for the analysis.
8. If the required 4 mm moving clearance cannot be achieved without a major change to approved door/catch geometry, stop and return `HUMAN_DECISION_REQUIRED`; do not redesign CAD-001 or CAD-002 silently.

## Do not build

- XG-07A lock body.
- Shim.
- Red service wall.
- Final/full hinge hardware.
- 48-door pattern or other rows/columns.

## Stop gate

Save the Fusion checkpoint; generate front/top/isometric evidence plus representative sweep-angle views and machine-readable clearance measurements; update `CAD_LOG.md`; create `handoff/CAD-003.json` with `READY_FOR_DESIGN_REVIEW`; push `cad/CAD-003`; stop.
