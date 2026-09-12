# Design Decisions — KeyBox V2

This file records the **current approved decisions** and important superseded ideas so CAD execution does not regress to earlier concepts.

## Current approved decisions

- 48 compartments = 4 columns × 12 rows.
- Horizontal order: Col1 + SVC1 + Col2 + Col3 + SVC2 + Col4.
- 90 mm column pitch, 50 mm row pitch, 100 mm compartment depth, 40 mm service channel clear width.
- Structural sheet: 1.2 mm nominal **hot-rolled** mild steel.
- Starting slot width for tab/grid interlock: 1.30 mm = 1.20 + 0.10 mm allowance.
- Col2/Col3 use 50/50 mm half-depth egg-crate interlock through 100 mm depth.
- Col1/Col4 use separate outer-divider family.
- Shared full-height Ø4 mm hinge rod per column; 4 rods total.
- Door uses 10 mm top and bottom inward flanges with rod holes.
- Door face starting size: 87.5 × 47.0 mm.
- Latch side uses double 90° folds: 12 mm first flange + 25 mm return flange.
- U-catch is moved 5 mm inward from original door-edge reference.
- Catch sweep must be checked dynamically; V1 failed from swept-path collision.
- Blue protective shield is integrated into continuous formed sheet geometry and must have local U-catch pass-through relief/opening.
- Red service wall stops near lock rear; it is not full 100 mm deep.
- XG-07A lock requires one-piece shim between lock body and red wall.
- Prototype lock mounting: 1 round locating hole + 2 short adjustment slots.
- Two harness routes per 40 mm service channel, center kept clear.
- Control-bay UI layout: **Display → Keypad → QR**, horizontal.
- Control bay rear cover: bottom-hinged swing-down service panel; low-voltage controller electronics can mount to it.
- Moving cabinet rear structural frame: 25×25×3 mm angle iron.
- Main cabinet service opening: **90° to the left**, not 180°.
- Wall support architecture: fixed left hinge rail + bottom support rail + right support structure.
- Two Solex master locks on right side: upper-right and lower-right, preferably keyed alike.
- Bottom wall rail carries closed-position weight; master locks provide security, not primary structural support.
- Powder coat only after complete bare-steel functional dry-build passes.

## Superseded / rejected ideas

- 64-box target for this V2 cabinet — current cabinet design is 48 boxes.
- 6×8 layout — replaced by 4×12.
- Individual concealed pivot pins per door — rejected; returned to shared full-height rods.
- Separate bolt-on solenoid shield — superseded by integrated formed shield concept.
- Full-depth red service wall — rejected because it blocks rear wiring/service access.
- Full-depth blue shield to the front — rejected because it conflicts with double-fold/U-catch sweep.
- Whole service-wall front setback — rejected due security/open-gap concern.
- Four removable concrete-wall bolts as normal cabinet closure — rejected; fixed support rails restored.
- Custom vertical two-point master-lock linkage — rejected in favor of two simple Solex locks.
- 180° cabinet service swing — rejected because hinge offset becomes awkward; current requirement is 90°.
- Vertical UI stack — replaced by horizontal Display-Keypad-QR layout.
- Cold-rolled SPCC requirement — replaced by commonly available 1.2 mm hot-rolled mild steel.
- 1.4–1.5 mm tab-slot width — replaced by 1.30 mm starting slot width based on user V1 fabrication experience.
- Earlier Phase-2 Fusion master-latch reference geometry — geometrically inaccurate and must not be reused as the basis for final CAD.

## Process decision

ChatGPT remains design authority. Codex is CAD execution agent through Fusion MCP. Codex must not silently invent mechanical decisions. Every high-risk feature is built and reviewed incrementally before replication.
