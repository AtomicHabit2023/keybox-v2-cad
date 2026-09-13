# CAD-002 evidence — real U-catch on approved door

Fusion checkpoint: `KeyBox_V2_CAD002_UCatch`

## Built

- Preserved `02_CAD001_MASTER_DOOR_FOLDS` unchanged.
- Added `03_CAD002_XG07A_UCATCH` as a separate grounded component for the static closed-position gate.
- Modeled a 20.0 × 36.5 × 1.5 mm catch plate plus a round-rod U loop with two projecting legs and a distal bridge; this replaces the superseded crude single-block reference.
- Mounted the plate on the outer face of the 25 mm hidden return. The plate spans local X = 62.5–82.5 mm, leaving the required 5.0 mm inset from the original door-edge reference at X = 87.5 mm.
- Centered the 36.5 mm plate vertically at Z = 25.0 mm, giving Z = 6.75–43.25 mm.
- Set the loop's furthest point 26.0 mm from the plate outer face.

## Verification

- CAD-001 door: one sheet-metal body, 10 unchanged healthy features, no unhealthy features, flat pattern still present.
- Door formed envelope remains 87.5 × 12.0 × 47.0 mm.
- Catch and door occurrence transforms match at the 550 mm review offset.
- Static mounting contact is at Y = 12.0 mm on the hidden return.
- No blue shield, lock body, red wall, shim, hinge rod, or patterned copies were added.
- No motion or swept-envelope approval is claimed; that remains CAD-003.

## Evidence files

- `CAD002_front.png`
- `CAD002_top.png`
- `CAD002_isometric.png`
- `CAD002_MEASUREMENTS.json`
- `KeyBox_V2_CAD002_UCatch.f3d`

## Review item

The repository supplies the plate dimensions, 26 mm loop projection, 5 mm inset, and the existing 3 mm loop-diameter parameter, but does not state the loop leg-center spacing. A provisional named parameter, `UCATCH_LOOP_LEG_SPACING = 12 mm`, is used and must be confirmed against the physical or fully dimensioned XG-07A catch before fabrication use.
