# CAD-002 corrected U-catch review evidence

Status: READY_FOR_DESIGN_REVIEW

Controlling decision: reviews/CAD-002_RESULT.md, read from refreshed main at 1070e73 on 2026-09-13. This evidence supersedes the original CAD-002 package and its provisional spacing.

## Corrections and verification

- Plate: 20.0 x 34.5 x 1.5 mm; local X 62.5-82.5, Y 12.0-13.5, Z 7.75-42.25 mm.
- Two through-holes in the catch plate only: diameter 4.2 mm, vertical centers 25.0 mm apart (drawing tolerance +/-0.2 mm). Centers X 72.5, Z 12.5 and 37.5 mm. The approved door return was not drilled or modified.
- Two diameter 3.0 mm projecting legs: centers X 65.5 and 79.5 mm, both at Z 25.0 mm; axes parallel to Y. Horizontal center spacing 14.0 mm, outside width 17.0 mm, inside clear spacing 11.0 mm.
- Projection: 26.0 mm from plate outer face Y 13.5 to loop furthest Y 39.5 mm (drawing tolerance +/-1 mm).
- Original edge inset remains 5.0 mm from door-edge reference X 87.5 to plate edge X 82.5 mm.
- Catch occurrence transform matches the door at the original 550 mm X review offset and is grounded for static review.
- Rebuilt only the catch using six fully constrained sketches and six healthy extrusion/cut features. Functional dimensions and offsets reference named parameters.
- Door body revision is identical before and after correction: 947b7e2e-ea4f-4ad2-9d0f-8d0c880a28ae. Volume, 46 faces, 100 edges, one sheet-metal body, 10 healthy features, 87.5 x 12 x 47 mm bounds, and existing flat pattern are preserved.
- The four-body purchased-hardware reference retains simple cylindrical legs and distal bridge. Cosmetic welds and detailed bend-end refinements are outside this correction.

## Evidence

- CAD002_front.png: plate front view from the compartment side (+Y looking toward -Y), with Z vertical; shows horizontal loop orientation and both mounting holes.
- CAD002_top.png: view from +Z, showing loop projection and width.
- CAD002_isometric.png: assembled view from the compartment side.
- CAD002_MEASUREMENTS.json: fresh Fusion geometry measurements and acceptance assertions; all pass.
- KeyBox_V2_CAD002_UCatch.f3d: corrected native Fusion checkpoint.

The three images were visually inspected after export. The saved Fusion document is KeyBox_V2_CAD002_UCatch.

No provisional loop-spacing deviation remains. This is the static CAD-002 gate only. No shield, lock body, red wall, shim, hinge rod, motion study, or pattern was added. CAD-003 remains blocked pending design-authority approval.
