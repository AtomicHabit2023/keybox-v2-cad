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

## E-002 — Blue-shield orientation / U-catch pass-through terminology

**Status: CONTROLLING**

For CAD-003 and all later work:

- The blue shield is the protective partition separating the tenant key space from the lock/shield zone adjacent to the service channel.
- With the current 65 mm key-space + 25 mm lock-zone allocation, the nominal shield partition is a **constant-X Y-Z plane at X = 65 mm**.
- `BLUE_SHIELD_FRONT_SETBACK` means the **leading edge of that partition measured along +Y compartment depth**.
- A constant-Y X-Z wall spanning the compartment is **not** the intended primary blue shield and must not be used as the CAD-003 pass-through reference.
- The U-catch is intentionally required to **cross the X = 65 mm shield partition through a local laser-cut opening/relief** and then enter the protected lock zone to engage the XG-07A hook.
- Therefore CAD-003 must not try to keep the U-catch entirely on one side of the shield. The intended condition is: the moving U-catch passes through the local opening without touching the **remaining shield material / opening edges**.
- The U-catch opening is a **local Y-Z relief in the constant-X shield**, derived from the portion of the moving catch envelope that actually intersects the 1.2 mm shield slab during the 0–90° door motion, plus the required clearance.
- The `CATCH_SWEEP_CLEAR = 4.0 mm` requirement applies to the minimum distance between the moving U-catch and the **boundary of the laser-cut opening / remaining shield material**, not to the distance from the U-catch to an uncut full shield plane.
- If a clearance measurement is taken against an uncut shield where the catch is supposed to pass through, that measurement is not an acceptance check; the correct acceptance check is clearance to the local relief edges after the opening is modeled.
- Do not project the complete 0–90° catch sweep onto the shield; that creates an artificially huge opening and defeats the protective function.

Reason: the corrected-axis CAD-003 rerun followed an earlier design-authority wording error and produced a 119 mm wide constant-Y relief, wider than the 90 mm compartment pitch. The master specification instead defines a 65 mm tenant key space, a 25 mm lock/shield zone, a shield front setback along depth, and a local U-catch pass-through.
