# CAD-003 blue shield and U-catch sweep evidence

Status: `READY_FOR_DESIGN_REVIEW`

The approved CAD-001 door and CAD-002 U-catch were preserved. CAD-003 adds only a lightweight fixed blue-shield reference and seven evidence-only U-catch sample copies. No XG-07A lock body, shim, red service wall, hinge rod, final hinge hardware, or pattern was added.

## Sweep method

Fusion temporary B-Rep copies of the approved U-catch plate, legs, and bridge were rotated about the lightweight vertical reference axis at local X = 0 mm, Y = 0 mm. Samples were measured at 0°, 15°, 30°, 45°, 60°, 75°, and 90°. Fusion's `MeasurementManager` measured minimum body-to-body distance from every rotated catch body to the fixed shield bodies.

The shield is a 1.2 mm four-web reference at local X = 50 mm. Its sweep-derived pass-through is 43 × 43 mm: local Y = 24–67 mm and Z = 3.5–46.5 mm. This leaves a continuous protective panel around the opening without added cosmetic or downstream geometry.

## Result

All seven sampled angles clear the shield by more than the required 4.0 mm safety allowance. The closest sampled approach is 11.80053 mm at 0°; the other samples increase from there. The full table, axis offsets, geometry bounds, and scope checks are in `CAD003_SWEEP_MEASUREMENTS.json`.

## Evidence

- `CAD003_front.png`, `CAD003_top.png`, and `CAD003_isometric.png` show the shield and representative 0°/45°/90° samples.
- `CAD003_sweep_0deg.png` through `CAD003_sweep_90deg.png` provide the required seven-angle motion record.
- `KeyBox_V2_CAD003_ShieldSweep.f3d` is the saved Fusion checkpoint.

The saved Fusion document is `KeyBox_V2_CAD003_ShieldSweep`. CAD-004 remains blocked pending design-authority approval.
