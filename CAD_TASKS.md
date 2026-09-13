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

**Status:** CHANGES REQUIRED / SIDE-SHIELD RERUN RELEASED — see `reviews/CAD-003_RESULT.md` and `DESIGN_ERRATA.md` E-002

### Frozen hinge axis

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm` from the hinge-side door edge.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm` behind the front-face plane.
- Axis direction = Z.
- Ø4.6 mm door guide holes centered on this axis for the Ø4.0 mm shared hinge rod reference.

### Controlling shield interpretation

- Tenant key-space width: **65 mm**.
- Lock/shield-zone width: **25 mm**.
- Nominal blue-shield partition: **constant-X Y-Z plane at X = 65 mm**.
- `BLUE_SHIELD_FRONT_SETBACK` is the shield's leading edge along **+Y compartment depth**.
- The U-catch pass-through is a local **Y-Z relief** in this partition.
- Do **not** use the superseded constant-Y X-Z wall / 119 mm relief interpretation.

### Corrected scope

- Preserve the approved CAD-001 door and approved CAD-002 U-catch unchanged.
- Keep the frozen 5 mm / 5 mm hinge axis.
- Model only the lightweight constant-X blue-shield partition needed for the sweep study.
- Evaluate 0°, 15°, 30°, 45°, 60°, 75°, and 90°.
- Derive the local Y-Z relief from only the moving catch geometry that intersects/approaches the 1.2 mm shield slab at X = 65 mm, plus at least **4 mm safety allowance**.
- Derive `BLUE_SHIELD_FRONT_SETBACK` along Y while preserving as much protective front material as practical.
- Report shield X, front-setback Y, opening Y range/depth, opening Z range/height, closest angle, and minimum clearance.
- If a secure local opening cannot be achieved inside the intended 90 mm cell / 25 mm lock zone, stop with `HUMAN_DECISION_REQUIRED` rather than enlarging the opening or redesigning CAD-001/CAD-002.

### Do not build yet

- XG-07A lock body.
- Shim.
- Red service wall.
- Final/full hinge hardware beyond the lightweight axis/reference needed for the corrected motion study.
- Patterned rows or columns.

### Stop gate / evidence

Correct only CAD-003. Save a new Fusion checkpoint; provide front/top/isometric views plus motion/interference evidence at 0°, 15°, 30°, 45°, 60°, 75°, and 90°; update `CAD_LOG.md`; update `handoff/CAD-003.json` with `READY_FOR_DESIGN_REVIEW`; push branch `cad/CAD-003`; stop for design-authority review.

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
