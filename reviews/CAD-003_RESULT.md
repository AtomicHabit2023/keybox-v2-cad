# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

Owner visual review of the newest Fusion checkpoint confirms CAD-003 is **still physically wrong**.

The raw shield now sits near the master cell, but the geometry orientation is incorrect:

- the supposed 25 mm front return is visibly a **horizontal shelf/plate**;
- the side partition visibly extends far beyond the one-row height envelope;
- therefore the current body is not the agreed protective L-shield.

The correct shield is an L **in TOP/plan view**, made from two vertical faces. No slot or sweep work is authorized yet.

## Frozen geometry — do not change

- CAD-001 approved door.
- CAD-002 approved U-catch.
- 90 × 50 × 100 mm master-cell physical envelope.
- 65 mm tenant key space / 25 mm lock-zone allocation.
- 1.2 mm shield thickness.
- 5 mm / 5 mm frozen hinge axis.

## Required correction — vertical L placement only

1. Read `DESIGN_ERRATA.md` E-002 through **E-005**.
2. Hide/suppress the current incorrect CAD-003 raw shield. Preserve CAD-001/CAD-002.
3. Do not use sheet-metal bend tools for this next checkpoint if they risk another orientation error. Two simple 1.2 mm solid reference slabs are acceptable.
4. Build the **side partition as a vertical slab**:
   - located 25 mm inward from the actual service-side cell face;
   - bounded vertically between the actual bottom and top row faces (about 50 mm high);
   - extending in depth from a provisional front setback toward the actual rear face (never beyond the 100 mm cell depth).
5. Build the **front return as a second vertical slab**:
   - at the side partition's front leading edge;
   - extending from that partition toward the actual service-side face for about 25 mm;
   - bounded by the exact same bottom and top row faces (about 50 mm high).
6. The two slabs meet along a **vertical corner/bend line**. They must form an `L` when viewed from TOP.
7. The front return must **not** be horizontal. No shield body may rise above or hang below the 50 mm row envelope.
8. Do not cut the U-catch slot. Do not run any sweep. Do not push `READY_FOR_DESIGN_REVIEW`.
9. Show three placement screenshots only:
   - TOP view: obvious L footprint inside the 90 × 100 plan envelope;
   - FRONT view: front return is a vertical ~25 mm wide × ~50 mm high panel;
   - combined isometric: reference cell + approved door + approved U-catch + raw vertical L-shield.
10. Stop for owner/design-authority visual approval.
11. Do not start CAD-004.

## Current acceptance gate

The next checkpoint passes only if:

- both shield legs are vertical;
- their common corner line is vertical;
- TOP view clearly shows an L shape;
- both legs stay between the same 50 mm top/bottom row faces;
- side partition stays within the 100 mm depth;
- front return stays within the 25 mm lock-zone width;
- shield occupies the same physical master cell as the door/U-catch;
- no slot, sweep, or CAD-004 work has started.

CAD-003 remains blocked at the raw-geometry visual gate.