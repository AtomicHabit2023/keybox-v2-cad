# CAD-002 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The prior `HUMAN_DECISION_REQUIRED` hold is resolved by the owner's physical measurement and drawing review. CAD-002 is **not yet approved** because the current U-catch model has two geometric errors that must be corrected before CAD-003.

## Owner-confirmed / drawing-confirmed corrections

1. **Catch plate size**
   - Correct plate size: **20.0 x 34.5 x 1.5 mm**.
   - The current 20.0 x 36.5 x 1.5 mm plate is wrong.

2. **U-loop orientation**
   - The two parallel **3.0 mm diameter** projecting legs are arranged **horizontally left-right in the plate front view**, not vertically.
   - In the KeyBox CAD coordinate convention used in CAD-002, the two leg centerlines must therefore be separated along the plate-width / X direction and share the same Z centerline.
   - Projection remains perpendicular to the plate along compartment depth / Y.

3. **U-loop spacing from physical measurement**
   - Owner measured **17.0 mm outside-to-outside** across the two parallel 3.0 mm rods.
   - Therefore the controlling leg center-to-center spacing is **14.0 mm**.
   - Derived inside clear spacing is **11.0 mm**.
   - Replace the provisional 12.0 mm spacing with **14.0 mm**.

4. **Mounting holes**
   - Model the two **Ø4.2 mm** catch mounting holes shown in the supplied XG-07A drawing.
   - Their vertical center-to-center spacing is **25.0 ±0.2 mm** per the drawing.

5. **Dimensions that remain unchanged**
   - Plate width: 20.0 mm.
   - Plate thickness: 1.5 mm.
   - U-loop rod diameter: 3.0 mm.
   - Loop projection from the plate: **26 ±1 mm**.
   - Catch location on the 25 mm hidden return: **5.0 mm inward edge inset**.
   - Approved CAD-001 door geometry must remain unchanged.

## Required CAD-002 correction

Modify only the U-catch component on branch `cad/CAD-002`:

- change plate height from 36.5 mm to 34.5 mm;
- rotate/rebuild the U-loop so the two projecting legs are horizontally separated in front view;
- set leg center spacing to 14.0 mm;
- add the two Ø4.2 mounting holes at 25.0 mm vertical center spacing;
- preserve the 26 mm projection, 3 mm rod diameter, 5 mm inward inset, and approved door baseline;
- regenerate front/top/isometric evidence and machine-readable measurements;
- update `handoff/CAD-002.json` to `READY_FOR_DESIGN_REVIEW` with no provisional loop-spacing deviation;
- push the corrected `cad/CAD-002` branch and stop.

## Acceptance checks

- Plate = **20.0 x 34.5 x 1.5 mm**.
- 2 x Ø4.2 mounting holes, 25.0 mm vertical center-to-center.
- Two Ø3.0 projecting legs are horizontal left-right in front view.
- Outside-to-outside across rods = **17.0 mm**.
- Center-to-center across rods = **14.0 mm**.
- Inside clear spacing = **11.0 mm**.
- Projection = **26 mm nominal**.
- 5.0 mm inward edge inset preserved.
- CAD-001 door remains unchanged and healthy.
- No blue shield, lock body, red wall, shim, hinge rod, motion study, or 48-door pattern is added.

## Hold

CAD-003 remains blocked until the corrected CAD-002 evidence is reviewed and approved.
