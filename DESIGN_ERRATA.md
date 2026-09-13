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