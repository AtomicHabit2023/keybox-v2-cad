# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

The latest Codex check is now measuring the **correct thing**: the moving U-catch against the boundary / remaining metal of the explicitly modeled local Y-Z pass-through in the blue shield at `X = 65.0 mm`.

The governing opening-edge clearance is **3.40037 mm at 0°**, below the required 4.0 mm minimum by **0.59963 mm**.

This is a small local-relief sizing issue, not a product-level problem and not an owner decision. Do **not** move the whole shield or alter CAD-001/CAD-002.

## Frozen geometry — do not change

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm`.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm`.
- Hinge axis direction = Z.
- Blue-shield partition nominal plane = `X = 65.0 mm`.
- CAD-001 door and CAD-002 U-catch remain unchanged.

## Required CAD-003 correction

1. Keep the current local Y-Z pass-through concept in the `X = 65 mm` shield.
2. At the 0° governing condition, identify **which specific opening boundary edge** (front/rear Y edge, top/bottom Z edge, or local corner) produces the 3.40037 mm minimum distance.
3. Enlarge **only that governing local boundary** in the direction needed to increase clearance. Do not enlarge unrelated edges and do not move the whole shield.
4. Required minimum clearance is 4.0 mm. For review robustness, target **>= 4.5 mm** at the governing point.
5. Starting correction magnitude may be about **1.1 mm** (0.59963 mm shortfall + ~0.5 mm review margin), but Fusion measurement governs; if geometry is non-linear, fine-tune the local edge until >=4.5 mm is measured.
6. Preserve maximum surrounding shield metal. The opening must remain local and must not create an unnecessary straight tool path into the lock wiring/emergency-release area.
7. Re-evaluate 0°, 15°, 30°, 45°, 60°, 75°, and 90°.
8. Report in the evidence:
   - final opening Y range/depth,
   - final opening Z range/height,
   - which edge/corner governed,
   - closest angle,
   - final minimum edge clearance,
   - confirmation that CAD-001/CAD-002 and the 5/5 mm hinge axis are unchanged.
9. If a local <=~1-2 mm opening-edge adjustment achieves >=4.0 mm without compromising shielding, regenerate evidence, set handoff to `READY_FOR_DESIGN_REVIEW`, push `cad/CAD-003`, and stop.
10. If substantially larger relief is required or shielding/security is compromised, stop with `HUMAN_DECISION_REQUIRED`.
11. Do not start CAD-004.

## Acceptance checks

- Local pass-through explicitly modeled in constant-X shield at X=65 mm.
- U-catch intentionally crosses the opening into the lock zone.
- Clearance measured to opening edges / remaining shield material.
- Final minimum edge clearance >=4.0 mm; review target >=4.5 mm.
- Only the governing local edge/corner is adjusted as much as necessary.
- Frozen 5 mm / 5 mm hinge axis preserved.
- CAD-001 and CAD-002 unchanged and healthy.
- No CAD-004 geometry added.

## Hold

CAD-004 remains blocked until the corrected CAD-003 evidence is reviewed and approved.
