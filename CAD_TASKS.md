# CAD Tasks — KeyBox V2

## CAD-001 — Rebuild master door cell, folds only

**Status:** APPROVED

### Approved baseline

- Reference cell: 90 × 50 × 100 mm.
- Complete formed door envelope: **87.5 × 12.0 × 47.0 mm**.
- Derived uninterrupted planar front region: approximately **84.8 × 41.6 mm**.
- Door sheet: 1.2 mm.
- Top inward hinge flange: 10 mm.
- Bottom inward hinge flange: 10 mm.
- First latch-side flange: 12 mm at 90°.
- Second latch-side return flange: 25 mm at 90°.
- Starting sheet-metal rule: 1.2 mm thickness, 1.5 mm inside bend radius, K-factor 0.42.
- Four required bends healthy; flat pattern healthy.

`87.5 × 47.0 mm` remains the **maximum complete formed door envelope**, not the uninterrupted planar center face.

See `reviews/CAD-001_RESULT.md` for the controlling approval.

---

## CAD-002 — Real U-catch on approved door

**Status:** APPROVED

### Approved geometry

- Preserve the approved CAD-001 sheet-metal door unchanged.
- Catch plate: **20.0 × 34.5 × 1.5 mm**.
- Two catch mounting holes: **Ø4.2 mm**, **25.0 ±0.2 mm** vertical center-to-center.
- U-loop rod diameter: **3.0 mm**.
- Two projecting U-loop legs arranged **horizontally left-right in plate front view**.
- Owner-measured rod outside-to-outside width: **17.0 mm**, giving **14.0 mm center-to-center** and **11.0 mm inside clear spacing**.
- Catch loop projection: **26 ±1 mm** from the plate.
- Catch mounted on the 25 mm hidden return with the approved **5.0 mm inward edge inset**.
- Approved door remains unchanged and healthy.

See `reviews/CAD-002_RESULT.md` for the controlling approval.

---

## CAD-003 — Blue shield + true U-catch sweep

**Status:** CHANGES REQUIRED / L-SHIELD REBUILD RELEASED — see `reviews/CAD-003_RESULT.md` and `DESIGN_ERRATA.md` E-002

### Frozen hinge axis

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm` from the hinge-side door edge.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm` behind the front-face plane.
- Axis direction = Z.
- Ø4.6 mm door guide holes centered on this axis for the Ø4.0 mm shared hinge rod reference.

### Controlling shield form

- Tenant key-space width: **65 mm**.
- Lock/shield-zone width: **25 mm**.
- Blue shield is a formed **L-section**, not a small frame.
- Side partition: constant-X Y-Z sheet at nominal **X = 65 mm**, running rearward from a CAD-derived front setback toward the compartment rear.
- Front return: short constant-Y X-Z face at the side partition's leading edge, turning toward the service-channel side across the **25 mm lock zone**.
- U-catch passage: local **horizontal slot/notch in the front return**, sized from the real moving U-catch envelope plus at least **4 mm** clearance.
- `BLUE_SHIELD_FRONT_SETBACK` is the Y position of the front return / leading bend.
- The side partition remains continuous/solid except for only minimum proven transition relief.
- Do **not** use the rejected four-web rectangular frame or the superseded full-width constant-Y wall / 119 mm relief.

### Corrected scope

- Preserve approved CAD-001 door and CAD-002 U-catch unchanged.
- Keep the frozen 5 mm / 5 mm hinge axis.
- Rebuild the CAD-003 shield reference as one lightweight 1.2 mm L-shaped formed sheet segment for the master row:
  - side leg at X=65 mm;
  - side leg extends from `BLUE_SHIELD_FRONT_SETBACK` rearward toward Y=100 mm;
  - front return at the leading edge spans nominally X=65..90 mm.
- Model the U-catch slot/notch in the front return, not as a freestanding frame around the catch.
- Evaluate motion at 0°, 15°, 30°, 45°, 60°, 75°, and 90°.
- Derive both the front setback and the smallest practical front-return slot/notch from the moving catch envelope.
- Measure clearance to slot/notch edges and any nearby side-partition/bend metal.
- Minimum required moving clearance = **4.0 mm**; review target >=4.5 mm where practical.
- Keep maximum protective metal and avoid a straight tenant tool path toward wiring/emergency-release areas.

### Do not build yet

- XG-07A lock body.
- Shim.
- Red service wall.
- Final/full hinge hardware beyond the lightweight axis/reference needed for the corrected motion study.
- Patterned rows or columns.

### Stop gate / evidence

Correct only CAD-003. Save a new Fusion checkpoint; provide an isolated clear view of the full L-shaped shield segment plus front/top/isometric and 0°/15°/30°/45°/60°/75°/90° motion evidence; report front setback, front-return span, slot/notch X/Z extents, governing edge/corner, closest angle, and minimum clearance; update `CAD_LOG.md`; update `handoff/CAD-003.json` with `READY_FOR_DESIGN_REVIEW`; push branch `cad/CAD-003`; stop for design-authority review.

---

## CAD-004 — XG-07A + shim + red wall

**Status:** BLOCKED

Planned scope: build actual lock reference from drawing/measurements, derive shim thickness from hook/catch alignment, add red wall, and implement 1 round locating hole + 2 short adjustment slots.

---

## CAD-005 — Master-cell serviceability validation

**Status:** BLOCKED

Planned scope: prove rear removal/reinstallation of lock+shim, emergency-release access, wiring clearance, tenant anti-tamper separation, and zero motion interference.

---

## CAD-006 — Replicate to grid and structural architecture

**Status:** BLOCKED until master cell approved

Planned scope: only after CAD-001 through CAD-005 pass, pattern approved geometry into 4×12 structure, create outer/center divider families, service channels, shared rods, control bay, rear structural frame, wall supports, and master-lock geometry.
