# CAD Execution / Review Log — KeyBox V2

## 2026-09-12 — Workspace initialized

- GitHub repository established as shared design/CAD handoff channel.
- ChatGPT designated project designer / design authority.
- Codex designated CAD execution agent through Fusion MCP.
- Fusion 360 remains authoritative geometric/interference environment.

### Existing Fusion status

- Phase-1 parametric reference model successfully created and user parameters verified in Fusion.
- Earlier Phase-2 master latch cell ran technically but was visually/geometrically inaccurate.
- That earlier Phase-2 cell is **superseded and must not be used as the basis of final CAD**.

### Current approved next action

Run **CAD-001** from `CAD_TASKS.md`: rebuild only the master cell + actual sheet-metal door + top/bottom hinge flanges + 12 mm first latch fold + 25 mm return fold.

Stop after those folds are measured and visually verified. Do not add U-catch or lock until design-authority review.

### Known validation priorities

- Correct coordinate/orientation mapping.
- Real sheet-metal bends rather than crude extruded blocks.
- No corner self-intersection.
- Finished door face remains 87.5 × 47.0 mm.
- All repeated dimensions driven from named parameters.

## 2026-09-12 — CAD-001 folds completed; awaiting design review

- Connected Codex to the Autodesk Fusion MCP endpoint at `http://127.0.0.1:27182/mcp`.
- Active Fusion document: `KeyBox_V2_Phase1_Reference`.
- Preserved the superseded `01_MASTER_LATCH_CELL` geometry unchanged and hidden for review.
- Created a separate `CAD001_REFERENCE_CELL` envelope at the `MASTER_CELL_SHIFT_X = 550 mm` review offset.
- Created `02_CAD001_MASTER_DOOR_FOLDS` as a true sheet-metal component.
- Created sheet-metal rule `KEYBOX_V2_CAD001_1P2MM (Convert)` with:
  - thickness: 1.2 mm;
  - inside bend radius: 1.5 mm;
  - K-factor: 0.42;
  - relief width: 2.0 mm;
  - relief depth: 3.5 mm.
- Created four healthy 90-degree bend features:
  - `BEND_TOP_INWARD_90` — 10 mm top hinge flange;
  - `BEND_BOTTOM_INWARD_90` — 10 mm bottom hinge flange;
  - `BEND_LATCH_FIRST_90` — 12 mm first latch-side flange;
  - `BEND_LATCH_RETURN_90` — 25 mm hidden return.
- Final formed envelope measured 87.5 mm wide × 12.0 mm deep × 47.0 mm high, with local bounds X = 0.0–87.5 mm, Y = 0.0–12.0 mm, and Z = 1.5–48.5 mm inside the 90 × 50 × 100 mm reference cell.
- The 87.5 × 47.0 mm door-face requirement was interpreted as the finished front projection including the bend zones. The largest uninterrupted planar region between bend tangencies measures 84.8 × 41.6 mm. This interpretation requires design-authority confirmation before CAD-002.
- The top, bottom, and latch-side flanges all project inward toward positive compartment depth.
- Both latch-side intersections use a 3.5 mm boundary cutback, with the rule supplying 2.0 mm × 3.5 mm bend relief. Visual inspection found no impossible corner overlap.
- Sheet-metal validation passed: one valid sheet-metal body, four healthy bend features, eight cylindrical bend faces, and a successfully generated flat pattern.
- Flat-pattern bounding size measured 119.995752 × 62.495752 × 1.2 mm. This is review evidence only, not a released manufacturing blank.
- Review images:
  - `evidence/CAD001/CAD001_front.png`
  - `evidence/CAD001/CAD001_top.png`
  - `evidence/CAD001/CAD001_isometric.png`
- No U-catch, shield, service wall, lock, shim, hinge rod, or patterned copies were added.
- Stop gate reached. CAD-002 remains blocked pending design-authority approval.
- Assumptions used for CAD-001:
  - component local +Y is inward toward the tenant compartment;
  - the door is vertically centered in the 50 mm reference cell, leaving 1.5 mm nominal clearance above and below the 47 mm formed projection;
  - the 12 mm and 25 mm latch dimensions are formed-envelope distances from the original door-edge reference;
  - the initial corner treatment uses the specified 3.5 mm boundary cutback and the rule's 2.0 mm relief width; final shop-specific relief shape remains subject to bend-coupon and fabrication review;
  - the Fusion Join By Bend preview API is acceptable for this checkpoint because it produced four healthy parametric bend features and a valid flat pattern.
- Saved the active Fusion document as `KeyBox_V2_CAD001_MasterDoor` in the `KeyBox System` Fusion folder. Saved state was verified with `isModified = false`.
- Exported the native Fusion archive checkpoint to `evidence/CAD001/KeyBox_V2_CAD001_MasterDoor.f3d`.
- Exact machine-readable measurements are stored in `evidence/CAD001/CAD001_MEASUREMENTS.json`; execution and review notes are stored in `evidence/CAD001/README.md`.

## 2026-09-13 — CAD-001 final baseline restored; ready for design review

- A later CAD-001R attempt incorrectly forced the uninterrupted planar face to 87.5 x 47.0 mm, producing an oversized formed envelope of approximately 90.2 x 52.4 mm. That attempt was abandoned and is not final evidence.
- Restored the original, physically correct CAD-001 baseline in which 87.5 x 47.0 mm controls the complete formed front-plane envelope.
- Confirmed the restored formed envelope as 87.5 mm wide x 12.0 mm deep x 47.0 mm high.
- Confirmed the derived uninterrupted planar region as approximately 84.8 x 41.6 mm.
- Retained four healthy inward 90-degree bends, a valid sheet-metal body, and a healthy flat pattern.
- Confirmed fit within the 90 x 50 mm cell pitch, leaving 2.5 mm nominal horizontal gap and 3.0 mm nominal vertical gap.
- Created the final review package at `evidence/CAD001_FINAL/`, including front, top, and isometric views; machine-readable measurements; notes; and the saved native `.f3d` checkpoint.
- No Fusion geometry was modified while preparing the final evidence package.
- CAD-002 remains blocked and was not started.

## 2026-09-13 — CAD-002 real U-catch completed; ready for design review

- Synchronized `main` after `reviews/CAD-001_RESULT.md` approved CAD-001 and explicitly released CAD-002.
- Created task branch `cad/CAD-002` and saved a separate Fusion checkpoint as `KeyBox_V2_CAD002_UCatch`, preserving the approved CAD-001 document and door geometry.
- Preserved `02_CAD001_MASTER_DOOR_FOLDS` as one unchanged sheet-metal body with 10 healthy features and its flat pattern present.
- Added `03_CAD002_XG07A_UCATCH` as a separate grounded component at the same 550 mm occurrence transform as the approved door.
- Modeled the catch as a 20.0 × 36.5 × 1.5 mm plate plus a round 3.0 mm rod U loop made from two projecting legs and a distal bridge, rather than the superseded crude bounding block.
- Mounted the plate on the outer face of the 25 mm hidden return. Local plate bounds are X = 62.5–82.5 mm, Y = 12.0–13.5 mm, and Z = 6.75–43.25 mm.
- Verified the approved 5.0 mm inward inset from the original door-edge reference at X = 87.5 mm to the plate edge at X = 82.5 mm.
- Verified the loop's furthest point projects 26.0 mm from the plate outer face, from Y = 13.5 mm to Y = 39.5 mm.
- Added named parameter `UCATCH_LOOP_LEG_SPACING = 12 mm` as an explicitly provisional dimension because the repository does not state the physical catch's leg-center spacing; design-authority confirmation is requested before fabrication use.
- Generated fresh front, top, and isometric screenshots, machine-readable measurements, notes, and a native `.f3d` checkpoint under `evidence/CAD002/`.
- Did not add a blue shield, XG-07A lock body, red service wall, shim, hinge rod, or patterned copies.
- Did not perform or claim swept-motion approval; that work remains CAD-003.
- Stop gate reached with `handoff/CAD-002.json` set to `READY_FOR_DESIGN_REVIEW`.
