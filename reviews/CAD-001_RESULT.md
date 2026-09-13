# CAD-001 Design Authority Result

STATUS: APPROVED

## Decision

CAD-001 is approved as the master-door folded baseline.

The review evidence confirms:

- complete formed door envelope: **87.5 × 12.0 × 47.0 mm**;
- fit within the **90 × 50 mm** cell pitch with nominal gaps of **2.5 mm horizontal** and **3.0 mm vertical**;
- derived uninterrupted planar front region: approximately **84.8 × 41.6 mm**;
- 1.2 mm sheet-metal body is valid;
- four required 90-degree bends are healthy and oriented correctly;
- R1.5 mm / K0.42 starting sheet-metal rule is preserved;
- bend relief remains parametric;
- flat pattern generates successfully;
- no U-catch, shield, service wall, lock, shim, hinge rod, or patterned copies were added;
- CAD-002 was not started before this approval.

The abandoned oversized CAD-001R interpretation remains superseded and must not be reused.

## Release

**CAD-002 is RELEASED.**

Codex may proceed with `CAD-002 — Real U-catch on approved door` after synchronizing `main` and creating/switching to branch `cad/CAD-002`.

CAD-002 scope is limited to:

1. preserve the approved CAD-001 sheet-metal door unchanged;
2. model the actual XG-07A U-catch from the supplied dimensions, not a crude bounding block;
3. mount the catch on the 25 mm hidden return with the approved **5 mm inward edge inset**;
4. verify static closed-position geometry and report exact catch position relative to the door and latch-side folds;
5. do **not** add the blue shield, XG-07A lock body, red service wall, shim, hinge rod, or 48-door pattern yet;
6. save the Fusion checkpoint, create CAD-002 evidence and `handoff/CAD-002.json`, push the task branch, then stop for review.

## CAD-002 review emphasis

The catch plate/loop must match the supplied reference dimensions (20 mm × 36.5 mm plate, 1.5 mm plate thickness, approximately 26 mm loop projection) and its mounting orientation must remain compatible with the later full swept-envelope test. Static fit alone is not approval for motion; the motion test belongs to CAD-003.
