# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

Owner visual review of the latest Fusion model confirms the rebuilt L-shield is still physically wrong **in placement**, even though Codex reports the intended local L-section dimensions.

The most likely failure is a coordinate-frame / occurrence-transform mismatch:

- the approved CAD-001 door and CAD-002 U-catch are placed at the established **+550 mm master-cell review occurrence transform**;
- the latest CAD-003 log describes the shield only at local/root `X = 65 mm` and does not confirm the same +550 mm occurrence transform;
- in Fusion, the new shield geometry appears physically separated from the approved door/catch instead of occupying the same master cell.

Therefore the current sweep and clearance evidence is invalid regardless of the reported local dimensions. Correct physical placement must be proven **before** any further sweep tuning.

## Frozen geometry — do not change

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm`.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm`.
- Hinge axis direction = Z.
- CAD-001 door and CAD-002 U-catch remain unchanged.
- Tenant key-space allocation = 65 mm.
- Lock/shield-zone allocation = 25 mm.
- Physical shield form remains the E-002 L-section: long side partition + short front return/cap + local U-catch slot.

## Required correction — placement first, sweep later

1. Read `DESIGN_ERRATA.md` E-002 and E-003 before touching Fusion.
2. Do **not** redesign the L-section dimensions yet.
3. Inspect the occurrence/component transforms of `02_CAD001_MASTER_DOOR...` and `03_CAD002_XG07A_UCATCH...` and record the exact transform used by the approved master cell (expected +550 mm review X offset).
4. Recreate or move `04_CAD003_BLUE_SHIELD...` so it uses the **same occurrence transform / parent coordinate frame** as the approved door and catch.
5. Interpret `X = 65 mm`, `Y = BLUE_SHIELD_FRONT_SETBACK`, and all other CAD-003 shield dimensions as **local master-cell coordinates** inside that occurrence frame.
6. Hide superseded `01_MASTER_LATCH_CELL` / old analysis references if they visually obscure the review. Do not delete approved evidence.
7. Before running any sweep, generate a **combined placement checkpoint** showing only:
   - reference 90 × 50 × 100 master cell,
   - approved CAD-001 door,
   - approved CAD-002 U-catch,
   - corrected CAD-003 L-shield.
8. In that view, the long side partition must visibly sit **inside the same 90 mm cell**, 25 mm from the service-side edge (local X=65 mm), and the front return must be physically in front of the future lock zone where the U-catch can pass through its slot.
9. Also generate an isolated shield view showing the full long side leg and short front return.
10. If the combined placement view is not visually correct, stop and fix placement only. Do not perform clearance measurements on separated geometry.
11. Only after placement is correct, rerun 0°, 15°, 30°, 45°, 60°, 75°, and 90° and measure clearance to the slot/opening edges and nearby remaining shield metal.
12. Update evidence/handoff only after the combined placement and sweep both pass. Push `cad/CAD-003` and stop. Do not start CAD-004.

## Acceptance checks

- Shield, door, and U-catch visibly occupy the **same master cell**.
- Shield uses same master-cell occurrence transform as CAD-001/CAD-002.
- Local shield X=65 mm corresponds physically to the 65/25 mm key-space/lock-zone split.
- Isolated shield visibly reads as a long L-shaped protective sheet, not a small frame.
- Front return contains only the local U-catch slot/notch.
- U-catch passes through the front-return slot into the lock zone without collision.
- Minimum moving clearance >=4.0 mm; target >=4.5 mm where practical.
- No CAD-004 geometry added.

## Hold

CAD-004 remains blocked until the shield is first proven in the correct master-cell coordinate frame and the corrected sweep evidence passes.