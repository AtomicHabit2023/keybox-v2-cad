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
