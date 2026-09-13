# Design Errata — KeyBox V2

This file records controlling corrections that have not yet been fully folded back into every older narrative document.

## E-001 — Door size terminology

**Status: CONTROLLING**

For CAD-001 and all later work:

- `87.5 × 47.0 mm` is the **maximum complete formed door envelope** in the cabinet front plane.
- It is **not** the uninterrupted planar center-face size.
- The uninterrupted planar center face is derived from sheet thickness, bend radius, bend tangency and corner-relief geometry.
- The restored CAD-001 baseline measured approximately **84.8 × 41.6 mm** for the uninterrupted planar region; that value is evidence, not a controlling parameter.
- Canonical parameter names are `DOOR_ENVELOPE_W` and `DOOR_ENVELOPE_H`.
- Older references to `DOOR_FACE_W` / `DOOR_FACE_H` are legacy aliases and must not be interpreted as planar-face dimensions.

Reason: forcing the planar center face to 87.5 × 47.0 mm made the formed envelope approximately 90.2 × 52.4 mm and violated the 90 × 50 mm cell pitch.

## E-002 — Blue-shield physical form / U-catch pass-through

**Status: CONTROLLING**

The CAD-003 blue shield is **not** a small four-web rectangular frame around an opening. That representation is rejected.

The intended shield is a formed **L-section** protecting the lock zone:

1. **Side partition** — a 1.2 mm vertical sheet on the constant-X Y-Z plane at nominal `X = 65 mm`, separating the 65 mm tenant key space from the 25 mm lock/shield zone. In the one-row master-cell study it extends rearward from `BLUE_SHIELD_FRONT_SETBACK` toward the compartment rear (`Y ≈ COMP_DEPTH`). In the final cabinet this shielding is vertically continuous for the column where practical.
2. **Front return / front shield face** — at the side partition's leading edge, the sheet turns approximately 90° toward the service-channel side, creating a short constant-Y X-Z face across the lock zone. For CAD-003 use a nominal span equal to `LOCK_ZONE_W = 25 mm` (approximately X = 65..90 mm) as a lightweight reference; final termination will be reconciled with the red service wall in CAD-004.
3. **U-catch passage** — the U-catch must intentionally pass through a **local horizontal slot/notch cut in this front return**, then enter the protected lock zone and engage the XG-07A hook. The slot is derived from the portion of the real moving U-catch envelope that crosses the front return, plus `CATCH_SWEEP_CLEAR = 4.0 mm` minimum clearance to the remaining metal.
4. The slot/notch may be open toward the side-partition/bend edge if the real sweep requires it; do not force a fully enclosed rectangular window if that would collide with the catch. Preserve the maximum practical shield metal around the actual sweep.
5. The long side partition should remain solid except for only the minimum local bend/transition relief proven necessary by the motion study. Do not replace the whole shield with four tiny web bodies around the slot.

`BLUE_SHIELD_FRONT_SETBACK` means the Y position of the L-section's front return / leading bend. It is derived from the door/U-catch sweep while keeping the shield as far forward as practical for anti-tamper protection.

The governing CAD-003 acceptance measurement is clearance between the moving U-catch and the **edges of the slot/notch in the front return and any nearby remaining side-partition/bend metal** throughout 0–90° motion.

Rejected interpretations:

- a full constant-Y wall across the entire 90 mm compartment with a 119 mm projected relief;
- a small freestanding rectangular frame around the opening;
- measuring the catch only against an uncut side-partition plane where it is intended to cross the front return.

Reason: the physical design intent is a continuous protective partition with a short front cap/return over the 25 mm lock zone. The U-catch crosses that front cap through a localized laser-cut slot on its way into the XG-07A hook.

## E-003 — Master-cell occurrence transform / physical placement

**Status: CONTROLLING**

All CAD-003 geometry belonging to the master cell must use the **same occurrence transform as the approved CAD-001 door and CAD-002 U-catch**.

- The approved CAD-001 door and CAD-002 U-catch are both placed at the existing **+550 mm review/master-cell X occurrence transform**.
- Dimensions such as `BLUE_SHIELD_PARTITION_X = 65 mm` are **local master-cell dimensions**, not root/global Fusion-document coordinates.
- The blue shield must therefore be created inside, or transformed with, the same master-cell occurrence frame so that its local X=65 mm plane physically sits beside the approved door and U-catch.
- A shield built at root/global X=65 mm while the door/catch remain at the +550 mm occurrence is invalid even if the shield's local dimensions are numerically correct.
- Before any sweep or clearance work, show one combined isometric view with only the approved door, approved U-catch, reference cell, and blue shield visible. The shield must visibly occupy the intended 25 mm lock zone in the **same cell** as the catch.
- CAD-003 must not claim `READY_FOR_DESIGN_REVIEW` until both the isolated shield view and combined master-cell view confirm correct physical placement.

Reason: the latest L-shield rebuild reports local X=65 mm but the Fusion view shows the new shield geometry physically separated from the approved door/catch, consistent with a root/local occurrence-transform mismatch.

## E-004 — CAD-003 must be anchored to physical master-cell faces

**Status: CONTROLLING**

The latest placement attempt still produces grossly incorrect geometry even after copying the +550 mm occurrence transform. Therefore CAD-003 must stop relying on assumed X/Y/Z orientation or copied transforms as the primary placement method.

Use the **actual visible faces of the approved 90 × 50 × 100 mm master-cell reference** as the construction datum:

- Identify the **front face** physically by the approved door location.
- Identify the **service-side face** physically by the approved U-catch/latch side.
- Identify the **rear face** as the face 100 mm behind the front face.
- Identify the **top and bottom row faces** as the 50 mm row-height boundaries.
- Define the blue-shield side partition as a plane **25.0 mm inward from the actual service-side cell face**. This is physically equivalent to the intended 65/25 mm split, regardless of global axis naming.
- The shield side leg must be bounded by the actual top/bottom row faces and by the actual rear face. No shield material may extend above, below, outside the service-side face, or beyond the rear of the master cell except the nominal 1.2 mm sheet thickness/bend envelope.
- Create the front return from the side-partition leading edge **toward the actual service-side face** for a nominal 25 mm span. Do not infer its direction from a global X sign.
- Use the approved door/U-catch geometry itself to establish which side of the return faces the closing catch.

Before any slot or sweep work, the raw un-notched L-shield must pass a visual/bounding-box gate:

- overall row height ≈ 50 mm maximum;
- width occupied across the lock zone ≈ 25 mm maximum plus bend/sheet envelope;
- depth of the side leg ≤ 100 mm and equals rear-face minus front-setback;
- the entire L-shield sits inside the one physical master cell next to the U-catch.

If any plate appears hundreds of millimetres long, hangs below the cell, rises above the row, or projects outside the 90 × 50 × 100 reference cell, placement/orientation is wrong and CAD-003 must stop before sweep analysis.

Reason: visual review showed a large plate hanging outside the master cell after the transform-only correction, proving that transform equality alone does not guarantee matching local-axis orientation or correct in-context placement.