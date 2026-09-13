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

**Status:** READY / RELEASED

### Scope

- Preserve the approved CAD-001 sheet-metal door unchanged.
- Model the actual XG-07A U-catch from the supplied dimensions, not a bounding block.
- Catch plate reference: 20 mm × 36.5 mm × 1.5 mm.
- Catch loop projection reference: approximately 26 mm.
- Mount the catch on the 25 mm hidden return with the approved **5 mm inward edge inset**.
- Verify static closed-position geometry and record exact catch placement relative to the door/folds.
- Keep the model parametric where repeated/functional dimensions are involved.

### Do not build yet

- Blue shield.
- XG-07A lock body.
- Red service wall.
- Shim.
- Hinge rod.
- Patterned rows or columns.

### Stop gate / evidence

Save the Fusion checkpoint; provide front/top/isometric views and machine-readable catch dimensions/placement; update `CAD_LOG.md`; create `handoff/CAD-002.json` with `READY_FOR_DESIGN_REVIEW`; push branch `cad/CAD-002`; stop for design-authority review.

Static fit in CAD-002 does **not** approve the moving sweep. Full U-catch swept-envelope validation belongs to CAD-003.

---

## CAD-003 — Blue shield + true U-catch sweep

**Status:** BLOCKED by CAD-002 approval

Planned scope: add blue shield geometry, rotate door through operational range, calculate/check real swept envelope, and create only the minimum pass-through/relief needed with starting 4 mm safety allowance.

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
