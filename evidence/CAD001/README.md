# CAD-001 Review Checkpoint

This folder contains the saved review package for the KeyBox V2 master-door folds stop gate.

## Contents

- `KeyBox_V2_CAD001_MasterDoor.f3d` — native Fusion archive checkpoint.
- `CAD001_front.png` — Fusion front review view.
- `CAD001_top.png` — Fusion top review view.
- `CAD001_isometric.png` — Fusion isometric review view.
- `CAD001_MEASUREMENTS.json` — exact MCP/API measurements and feature-health results.

## Geometry created

- Reference cell envelope: 90 × 50 × 100 mm.
- Formed door projection: 87.5 × 47.0 mm.
- Sheet thickness: 1.2 mm.
- Top and bottom inward hinge flanges: 10 mm each.
- First latch-side inward flange: 12 mm.
- Second latch-side return: 25 mm.
- Four 90-degree Join By Bend features using R1.5 mm and K-factor 0.42.
- Corner treatment: 3.5 mm boundary cutback with 2.0 mm rule relief width.
- Valid Fusion flat pattern generated.

## Assumptions requiring review

- Local +Y is the inward compartment direction.
- The 87.5 × 47.0 mm requirement is treated as the complete formed front projection, including bend zones. The largest uninterrupted planar front region between bend tangencies is 84.8 × 41.6 mm.
- The formed door is vertically centered in the 50 mm cell, giving 1.5 mm nominal clearance at each edge of the formed projection.
- The 12 mm and 25 mm latch dimensions are treated as formed-envelope distances from the original door-edge reference.
- The current bend relief is a review starting point. Shop-specific relief shape and bend allowance must be calibrated before fabrication release.
- Join By Bend is a Fusion preview API in this Fusion build; the checkpoint is accepted only as review geometry because all four bend features are healthy and the flat pattern computes successfully.

## Stop gate

No U-catch, shield, service wall, XG-07A lock, shim, hinge rod, or patterned copies were created. CAD-002 remains blocked pending design-authority approval.
