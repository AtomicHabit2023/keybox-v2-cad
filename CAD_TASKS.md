# CAD Tasks — KeyBox V2

## CAD-001 — Rebuild master door cell, folds only

**Status:** RESTORED LOCALLY; awaiting final evidence checkpoint and design-authority review

### Goal
Create a correct one-row / one-column master-cell door in Fusion using actual sheet-metal features and the approved parameters. This replaces the inaccurate earlier Phase-2 latch reference geometry.

### Build only

- One 90 × 50 × 100 mm reference cell envelope.
- Complete **formed door envelope**: maximum 87.5 × 47.0 mm in the cabinet front plane.
- Door sheet: 1.2 mm.
- Top inward hinge flange: 10 mm.
- Bottom inward hinge flange: 10 mm.
- First latch-side flange: 12 mm at 90°.
- Second latch-side return flange: 25 mm at 90°.
- Use the project sheet-metal rule values: 1.2 mm thickness, 1.5 mm starting inside bend radius, K-factor 0.42 starting.

### Important dimensional rule

`87.5 × 47.0 mm` is the **maximum complete formed door envelope**, not the uninterrupted planar center face. The planar center face is a derived result of the bend geometry. The restored CAD-001 baseline measured approximately **84.8 × 41.6 mm** for that planar region; this is evidence, not a new controlling parameter.

### Do not build yet

- U-catch.
- Blue shield.
- Red service wall.
- XG-07A.
- Shim.
- Hinge rod.
- Patterned rows or columns.

### Acceptance checks

- Complete formed door envelope is no larger than 87.5 × 47.0 mm.
- The door fits inside the 90 × 50 mm pitch with the intended nominal gaps.
- Top and bottom hinge flanges point inward toward tenant compartment.
- 12 mm first latch flange points inward.
- 25 mm second return is oriented as agreed to create the hidden catch-mounting return.
- No impossible corner overlap between top/bottom hinge flanges and latch-side double fold.
- Exact bend-relief treatment is identified and remains parametric.
- Report the derived uninterrupted planar-face size separately from the formed envelope.
- Flat pattern generates successfully.
- Provide front, top, and isometric screenshots plus machine-readable measurements.

### Stop gate
Stop after the folds are correct and logged. Await explicit design-authority approval before CAD-002.

---

## CAD-002 — Real U-catch on approved door

**Status:** BLOCKED by CAD-001 approval

Planned scope: model the actual U-catch plate/loop from supplied XG-07A drawing, mount it to the 25 mm return with the 5 mm inward offset, and verify static closed geometry. Do not add shield yet.

---

## CAD-003 — Blue shield + true U-catch sweep

**Status:** BLOCKED

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
