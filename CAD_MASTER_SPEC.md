# CAD Master Specification — KeyBox V2

## 1. Product goal

48-door smart apartment key cabinet intended for complete installed supply in Thailand. V2 must prove both functional reliability and local fabrication economics. The metal cabinet design is intended to be manufacturable by ordinary Thai laser-cut / press-brake / welding shops, while electronics/software remain the differentiated smart-control layer.

## 2. Frozen overall architecture

- Capacity: **48 key compartments**.
- Arrangement: **4 columns × 12 rows**.
- Horizontal sequence, left to right:
  **Col1 + Service #1 + Col2 + Col3 + Service #2 + Col4**.
- Nominal locker column pitch: **90 mm**.
- Nominal row pitch: **50 mm**.
- Compartment nominal depth: **100 mm**.
- Service-channel clear width: **40 mm** each.
- Locker matrix height: **600 mm**.
- Core internal width: **440 mm** before outer skins / finished edge geometry.
- Structural sheet: **1.2 mm nominal hot-rolled mild steel**.

Each apartment stores one normal key on a small ring/tag; usable key-space width may therefore be significantly less than 90 mm after lock/shield allocation.

## 3. Service-channel / lock architecture

Each service channel serves 24 locks: 12 from each adjacent column.

- XG-07A style 4-wire electronic locker lock.
- Lock body is inside each tenant compartment, adjacent to service channel.
- Lock is protected from tenant access by a formed shield integrated into the sheet geometry.
- Solenoid mounting screws are accessed from the protected service side.
- Lock wires exit into service channel and run upward to control bay.
- Rear access must permit replacing the lock without removing the door, horizontal divider, blue shield, or neighboring lock.
- Red service wall depth is **not 100 mm**; it stops near the rear edge of the solenoid to leave an open wire/service zone.
- Blue shield must have a laser-cut U-catch pass-through opening sized from the actual U-catch swept envelope plus clearance.

## 4. Master door geometry

Starting values:

- Visible door face width: **87.5 mm**.
- Visible door face height: **47.0 mm**.
- Door sheet: **1.2 mm**.
- Top inward hinge flange: **10 mm**.
- Bottom inward hinge flange: **10 mm**.
- Shared hinge rod: **Ø4 mm stainless steel**.
- Door hinge holes: **Ø4.6 mm starting**.
- Nylon/PTFE washer: **0.5 mm starting**.

The top and bottom flanges contain the hinge holes; one full-height rod serves all 12 doors in a column. Four columns = four shared rods.

### Latch-side folds

- First latch-side flange: **12 mm**, 90°.
- Second return flange: **25 mm**, 90°.
- U-catch plate width: **20 mm**.
- Catch is positioned **5 mm inward from the original door-edge reference**, so the 25 mm return is conceptually 20 mm catch plate + 5 mm inset.
- Final catch placement must be checked against the physical XG-07A catch and hook.

### Critical V1 lesson

The V1 cabinet failed because the U-catch could fit at the final closed position but collided with the wall during its rotating sweep. V2 must always be designed from the **full moving swept envelope**, not only open/closed static positions.

Minimum starting sweep clearance: **4 mm** around the real moving U-catch geometry where required.

## 5. Blue shield and red wall

The user-approved cross-section uses continuous formed sheet geometry, with a protected lock zone adjacent to the service channel.

- Starting clear key-space width: **65 mm**.
- Starting lock/shield zone width: **25 mm**.
- Blue protective shield is continuous vertically for a column where practical.
- Blue shield begins only behind the latch sweep zone; its exact front setback is CAD-derived from the actual catch sweep.
- Blue shield requires a local laser-cut pass-through for the U-catch.
- Red service wall is continuous where required to mount locks but stops at/near the rear of the lock, leaving rear service access into the 40 mm channel.
- No straight unauthorized tool path from tenant compartment into lock wiring/emergency-release area.

## 6. XG-07A / shim / mounting

Nominal XG-07A reference dimensions from supplied drawing:

- Body length: ~53 mm.
- Body height: ~40 mm.
- Body thickness: ~13 mm.
- Catch plate: ~20 mm × 36.5 mm.
- Catch loop projection: ~26 mm.
- Three M4 mounting holes in lock body.
- Emergency manual release and wiring are at the rear end.

A **rigid one-piece shim** is mandatory between lock body and red service wall. It accounts for catch inset plus additional alignment offset. Starting shim expectation is approximately **7–8 mm**, but final thickness must be derived from actual hook-to-catch alignment in CAD and prototype testing.

Prototype-friendly mounting pattern on red service wall:

- **1 locating round hole**.
- **2 short adjustment slots**.
- Starting round-hole diameter: **4.5 mm**.
- Starting slot width: **4.5 mm**.
- Starting slot length: **7.0 mm**.

The nominal mounting pattern must be derived from the final hook/catch geometry. Codex must not assume a guessed pattern is fabrication-ready.

## 7. Horizontal dividers / grid

Two divider families are required:

1. **Outer divider** for Col1 and Col4.
2. **Center divider** spanning Col2 + Col3.

Col2/Col3 use a true egg-crate interlock:

- Compartment depth: 100 mm.
- Horizontal divider slot: **50 mm deep** from one edge.
- Central vertical divider slot: **50 mm deep** from the opposite edge.
- Starting nominal slot width: **1.30 mm** for 1.2 mm nominal sheet.

The horizontal tenant divider stops at the blue shield and does not unnecessarily divide the vertical lock/service strip.

There are 11 internal row dividers; top and bottom structural plates provide the remaining boundaries.

## 8. Tab / slot rules

- `SHEET_T = 1.20 mm` nominal.
- `SLOT_CLEARANCE = 0.10 mm` starting.
- `SLOT_W = SHEET_T + SLOT_CLEARANCE = 1.30 mm` starting.
- All repeated slots must reference one named parameter.
- Laser-cut slots/tabs establish geometry and squareness.
- Welding only locks an already-located structure; welding must not establish pitch or alignment.
- Avoid long continuous welds on 1.2 mm sheet to reduce distortion.

## 9. Door rod support

- Four full-height Ø4 mm stainless rods.
- Rods pass through door top/bottom flange holes.
- Bottom matrix plate guides rod but should not be the sole axial support.
- Add a dedicated bottom-front hinge support rail beneath the matrix; rod projects through plate and rests/supports at the lower rail.
- Rods withdraw upward into top control bay for rare door replacement.
- Top control bay contains removable rod-retention/keeper feature.

## 10. Control compartment

- Control bay width = exact finished cabinet-body width.
- Nominal depth: **100 mm**.
- Starting height: **~165 mm**, adjust from actual UI packing.
- Horizontal front layout, left to right:
  **Display → Keypad → QR**.
- Keypad should be biased closer to display than QR because display+keypad form one workflow.
- Fixed secure front fascia; no public-side service fasteners.
- One removable internal UI carrier plate for display/keypad/QR.
- Rear service panel is bottom-hinged and swings down after the whole cabinet is opened.
- Rear panel retained at top by two repeated-service machine screws into captive/rivnut-type threads.
- Support straps keep rear service panel near ~90° open position.
- Low-voltage controller electronics may mount on the swing-down rear service panel.
- Prefer fixed mains/high-voltage and heavier PSU items in main enclosure rather than repeatedly flexing mains wires on service tray.

Reference UI hardware:

- 3.5 in ILI9488 display, non-touch preferred.
- Industrial keypad ~79.5 × 99.5 mm face.
- GM865 QR scanner.

## 11. Vertical-service-channel wiring

Each 40 mm channel has two harness routes, one along each side, leaving the center clear for tools/emergency access.

- Keep factory lock pigtail replaceable via connector.
- Place connector toward the rear open service portion, away from U-catch/hook motion.
- Starting lock service loop: **60 mm**.
- Use small laser-cut cable-tie slots rather than bulky cable duct where practical.
- Assume all four XG-07A conductors remain available until electrical bench testing proves otherwise.

## 12. Rear structural frame / wall mounting

Moving cabinet:

- Full rear perimeter frame: **25 × 25 × 3 mm angle iron**.
- Three substantial hinges on left side.
- Cabinet service swing: **90°**, left-opening.
- Hinge axis may therefore sit close to rear wall plane; exact hardware clearance still CAD-derived.

Fixed wall support:

- Left hinge rail.
- Bottom support rail carrying closed-position weight.
- Right support rail / upper support structure for alignment and security.

The cabinet should not rely on hinge cantilever load during normal closed operation.

## 13. Master service locks

Use **two Solex padlocks / master-key locks**, preferably keyed alike:

- Lower-right.
- Upper-right.

Each locks the moving 25×25×3 structural frame to the corresponding fixed support structure via aligned holes. Bottom support continues to carry cabinet weight; locks provide security, not primary structure.

Master-lock hole diameter and offsets remain hardware-derived parameters.

## 14. Materials and finish

- Main structural sheet: **1.2 mm nominal hot-rolled mild steel**.
- Main rear moving frame: **25×25×3 mm mild-steel angle**.
- Shared door hinge rods: **Ø4 mm SUS304 stainless starting choice**.
- Powder coat after all welding and bare-steel functional dry-build checks.
- Starting powder thickness target: roughly **70–90 μm**.
- Proper preparation needed for hot-rolled surface / scale / oil before coating.
- Repeated-service fasteners: machine screws into captive nuts/rivnuts; avoid self-tapping screws for repeated maintenance points.

## 15. Sheet-metal modeling rules

Global starting parameters:

- Inside bend radius: **1.5 mm**.
- K-factor: **0.42** starting only; calibrate with actual shop/bend coupon.
- Standard bend: 90° unless specified.
- Bend-relief starting width: 2.0 mm.
- Bend-relief starting depth: 3.5 mm.

Critical dimensions describe the **finished folded geometry**. Flat patterns should derive from the Fusion sheet-metal rule rather than hard-coded manual deductions.

The U-catch sweep relief is a separate functional feature and must not be conflated with generic bend relief.

## 16. Assembly / prototype sequence

1. Build locker grid in bare steel using tab/slot geometry.
2. Add control shell and rear structural frame.
3. Prove shared hinge rods fit and withdraw correctly before doors.
4. Build and prove **one master door/latch cell**.
5. Only after the master cell passes, replicate to all 48 positions.
6. Fit all doors/locks in bare steel and cycle them.
7. Fit wall-support system, 90° cabinet swing, and two right-side master locks.
8. Fit rear controller tray and front UI carrier.
9. Mock up wiring and confirm every lock remains rear-serviceable.
10. Only after all functional checks: final welds, re-check, disassemble removable hardware, powder coat, final assembly.

## 17. Master-cell acceptance gates

Before replication, the one-row master cell must prove all of the following:

- Door rotates without interference.
- 12 mm + 25 mm folds are oriented exactly as intended.
- U-catch is represented from real dimensions, not a crude bounding block.
- U-catch passes through shield opening throughout motion.
- No collision with blue shield/service-side wall through full door sweep.
- U-catch engages XG-07A hook positively.
- Shim thickness gives correct hook/catch relationship.
- 1 round + 2 slot lock mounting system provides controlled prototype adjustment.
- Emergency release remains accessible from service side.
- Lock and shim can be removed/reinstalled from rear without removing door/divider/shield/neighbouring lock.
- Tenant cannot directly access lock mounting screws, wiring, or emergency release.

## 18. CAD governance

- All repeated dimensions are named user parameters.
- Do not hard-code the same functional dimension in multiple sketches/features.
- Do not pattern 48 copies until the master cell is explicitly approved.
- Do not fabricate from provisional reference solids.
- Do not silently resolve contradictions. Stop and document them for design review.
- Maintain a running execution log in `CAD_LOG.md`.
