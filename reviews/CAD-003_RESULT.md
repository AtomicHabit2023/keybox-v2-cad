# CAD-003 Design Authority Result

STATUS: CHANGES_REQUIRED

## Decision

Owner visual review of the isolated `04_CAD003_BLUE_SHIELD...` component confirms the current CAD-003 shield representation is physically wrong. It appears as a small freestanding rectangular frame around an opening. That is **not** the agreed shield architecture and must not be refined further.

The earlier 3.40037 mm opening-edge result is therefore not an approval path for the current geometry. Rebuild the shield reference first, then repeat the sweep/clearance study against the correct formed shield.

## Frozen geometry — do not change

- `HINGE_AXIS_EDGE_OFFSET = 5.0 mm`.
- `HINGE_AXIS_FRONT_OFFSET = 5.0 mm`.
- Hinge axis direction = Z.
- CAD-001 door and CAD-002 U-catch remain unchanged.
- Tenant key-space allocation = 65 mm.
- Lock/shield-zone allocation = 25 mm.

## Correct physical blue-shield architecture

The blue shield is a formed **L-section**:

1. **Long side partition** — 1.2 mm sheet on the constant-X Y-Z plane at nominal `X = 65 mm`, extending rearward from a CAD-derived front leading edge toward the compartment rear (`Y ≈ 100 mm` in the one-row master-cell reference).
2. **Short front return / cap** — at that leading edge the sheet bends approximately 90° toward the service-channel side, making a constant-Y X-Z front face across the 25 mm lock zone, nominally from X≈65 to X≈90 mm for CAD-003 reference purposes.
3. **U-catch pass-through** — a local horizontal laser-cut slot/notch belongs in this **front return/cap**, because the closing U-catch must cross that face to enter the protected lock zone and engage the XG-07A hook.
4. The long side partition should remain substantially solid. Only the minimum bend/transition relief proven necessary by the real sweep is permitted.
5. The slot/notch may open into the side-partition/bend edge if the true sweep demands it. Do not force a closed rectangular window if that creates collision or removes unnecessary shielding.

The rejected component consisting only of small web bodies around the opening is not the blue shield.

## Required CAD-003 rebuild

1. Delete/suppress only the incorrect CAD-003 shield reference geometry; preserve CAD-001/CAD-002 and sweep source geometry.
2. Build one lightweight 1.2 mm L-shaped shield segment for the master row using the current sheet-metal/bend rules where practical.
3. Set the side leg at `X = 65 mm`.
4. Let the side leg run from `BLUE_SHIELD_FRONT_SETBACK` rearward toward `COMP_DEPTH = 100 mm`.
5. At the front leading edge, create a 90° front return toward the service side with nominal span `LOCK_ZONE_W = 25 mm` (approximately X=65..90 mm).
6. Compute the U-catch motion at 0°, 15°, 30°, 45°, 60°, 75°, and 90° about the frozen 5/5 mm hinge axis.
7. Derive the front setback and the smallest practical **horizontal slot/notch in the front return** from only the moving catch volume that crosses/approaches this front return.
8. Require >=4.0 mm clearance to the slot/notch edges and any adjacent bend/side-partition metal; target >=4.5 mm where practical.
9. Preserve maximum shield metal and avoid an unnecessary direct tool path toward future lock wiring/emergency-release areas.
10. Generate a clear isolated shield screenshot showing the whole L-shaped shield segment, not merely the slot frame.
11. Regenerate front/top/isometric and all seven sweep views; report front setback Y, front-return span, slot/notch X/Z extents, governing edge/corner, closest angle, and final minimum clearance.
12. Update `CAD_LOG.md` and `handoff/CAD-003.json` only when this rebuilt geometry passes; push `cad/CAD-003`; stop.
13. Do not start CAD-004.

## Acceptance checks

- Isolated shield visibly reads as a long L-shaped protective sheet: long side partition + short front return.
- No freestanding rectangular-frame substitute.
- Front return covers the lock-zone front except for the local U-catch slot/notch.
- U-catch crosses the front-return slot into the lock zone without collision.
- Minimum moving clearance >=4.0 mm; target >=4.5 mm where practical.
- Frozen hinge axis, CAD-001 door, and CAD-002 catch unchanged.
- No CAD-004 geometry added.

## Hold

CAD-004 remains blocked until this corrected physical shield is reviewed and approved.