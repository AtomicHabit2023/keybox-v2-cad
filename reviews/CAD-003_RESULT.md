# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

Owner visual review of the latest Fusion placement checkpoint confirms CAD-003 is **still physically wrong**. The shield/reference geometry visibly projects outside the one 90 × 50 × 100 mm master cell, including a large plate hanging below/outside the cell. Therefore the current placement is invalid and no sweep result from it is meaningful.

The previous correction focused on matching the +550 mm occurrence transform. That was necessary but not sufficient. The remaining failure is now treated as a local-axis/orientation/in-context construction problem.

## Frozen geometry — do not change

- CAD-001 approved door.
- CAD-002 approved U-catch.
- 90 × 50 × 100 mm master-cell physical envelope.
- 65 mm tenant key space / 25 mm lock-zone allocation.
- 1.2 mm blue shield.
- 5 mm / 5 mm frozen hinge axis.
- E-002 physical L-shield concept: long side partition + short front return/cap + local U-catch slot.

## Required correction — rebuild from physical cell faces, not coordinate assumptions

1. Read `DESIGN_ERRATA.md` E-002, E-003 and **E-004**.
2. Stop using copied occurrence transforms or assumed root/local X/Y/Z directions as the primary construction method.
3. Hide/suppress the current incorrect CAD-003 shield bodies. Do not alter CAD-001/CAD-002.
4. Use the actual approved 90 × 50 × 100 reference-cell faces as in-context datums:
   - front face = the face at the approved door;
   - service-side face = the cell side adjacent to the approved U-catch/latch;
   - rear face = the face 100 mm behind the front;
   - top/bottom faces = the 50 mm row-height boundaries.
5. Create the side-partition construction plane exactly **25.0 mm inward from the actual service-side face**. Do not type `X=65` into root coordinates; 25 mm inward from the physical service-side face is the controlling construction.
6. Build first an **un-notched raw L-shield only**:
   - 1.2 mm side leg on that offset plane;
   - side leg bounded vertically by the actual top/bottom row faces;
   - side leg bounded rearward by the actual rear face;
   - front edge at a provisional setback near the catch sweep zone;
   - 90° front return from that leading edge toward the actual service-side face, nominal 25 mm span.
7. Do **not** cut the U-catch slot and do **not** run a sweep yet.
8. Produce a placement checkpoint with only the physical reference cell, approved door, approved U-catch and raw un-notched L-shield visible.
9. Validate measured extents before proceeding:
   - shield height no greater than the 50 mm row envelope except sheet/bend tolerance;
   - shield width across the lock zone about 25 mm maximum plus bend/sheet envelope;
   - shield side-leg depth no greater than 100 mm;
   - every shield body lies within the physical master-cell envelope next to the U-catch, not below/above/outside it.
10. Also produce an isolated raw-shield view. It must visibly look like one substantial L-shaped protective sheet, not a tiny frame and not giant plates.
11. **Stop at this visual placement gate. Do not run the sweep and do not push READY_FOR_DESIGN_REVIEW yet.** Wait for owner/design-authority visual confirmation.
12. Only after that confirmation will the U-catch slot and sweep be released.
13. Do not start CAD-004.

## Current acceptance gate

For the next Codex pass, success means only this:

- one physically plausible raw L-shield;
- anchored to real cell faces;
- inside the same 90 × 50 × 100 cell as door/catch;
- correct 25 mm inward partition position from the actual service-side face;
- no material hanging below/above/outside the cell;
- no slot yet;
- no sweep yet;
- no CAD-004.

CAD-003 remains blocked at the visual geometry gate until the owner/design authority confirms this raw shield placement.