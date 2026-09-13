# CAD-002 Design Authority Result

STATUS: APPROVED

## Decision

The corrected CAD-002 evidence at branch `cad/CAD-002` / commit `8dfcdd22e3a1e66fadfbbc6d933be00ca54ff969` satisfies the released static U-catch gate.

## Approved geometry

- Catch plate: **20.0 × 34.5 × 1.5 mm**.
- Two catch mounting holes: **Ø4.2 mm**, **25.0 mm** vertical center-to-center (within the drawing tolerance of ±0.2 mm).
- U-loop rod diameter: **3.0 mm**.
- Two projecting loop legs are arranged **horizontally left-right in plate front view** and share the same Z centerline.
- Leg center-to-center spacing: **14.0 mm**.
- Outside-to-outside rod width: **17.0 mm**.
- Inside clear spacing: **11.0 mm**.
- Loop projection: **26.0 mm nominal** from the plate outer face.
- Catch location preserves the approved **5.0 mm inward edge inset** on the 25 mm hidden return.
- Approved CAD-001 door geometry remains unchanged and healthy, including the existing flat pattern.

## Evidence checks

The machine-readable CAD-002 measurements report all acceptance checks PASS. The catch is parameterized with fully constrained sketches; the approved door revision, volume, topology, bounds, feature count, and flat pattern are unchanged. No shield, lock body, red wall, shim, hinge rod, motion study, or 48-door pattern was added.

## Release

CAD-002 is approved. **CAD-003 is released.**

CAD-003 shall add the blue shield and validate the true moving U-catch sweep only. It must calculate/check the full swept envelope through the operational door rotation and introduce only the minimum shield pass-through / relief required, starting with a **4 mm safety allowance** at the closest moving approach. Do not add the XG-07A lock body, shim, red service wall, hinge rod, or patterned copies in CAD-003.

Stop at the CAD-003 review gate with fresh motion/interference evidence before proceeding to CAD-004.
