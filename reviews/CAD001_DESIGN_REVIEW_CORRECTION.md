# CAD-001 Design Review Correction — Envelope vs planar face

## Status
The previous review instruction that required an uninterrupted planar front face of **87.5 × 47.0 mm** is **rescinded**.

## Reason
CAD-001R demonstrated that keeping the planar face at 87.5 × 47.0 mm produces a formed overall envelope of about **90.2 × 52.4 mm**. That exceeds the 90 × 50 mm cell pitch and therefore violates the required inter-door clearance.

The original CAD-001 interpretation was physically correct for the cabinet layout:

- **DOOR_ENVELOPE_W = 87.5 mm**
- **DOOR_ENVELOPE_H = 47.0 mm**

These are the maximum formed front-projection dimensions of the complete bent door, not the uninterrupted planar center panel.

With R1.5 mm and 1.2 mm sheet, the corresponding uninterrupted planar region was measured at about **84.8 × 41.6 mm**. That is acceptable; it is a derived consequence of the bend radii and is not itself the controlling cabinet-fit dimension.

## Required action
1. Stop CAD-001R before committing it as an approved replacement.
2. Restore/retain the original CAD-001 formed-envelope geometry where the complete door fits within 87.5 × 47.0 mm.
3. Keep the 10 mm top/bottom inward hinge flanges, 12 mm first latch flange, 25 mm return, R1.5 mm, K=0.42 starting rule, and the existing healthy sheet-metal topology.
4. Treat the planar front-panel size as a **derived** value, not a fixed requirement.
5. Do not start CAD-002 until this correction is acknowledged and the CAD-001 checkpoint is confirmed as the active baseline.

## Parameter naming correction
To avoid recurrence, use these meanings going forward:

- `DOOR_ENVELOPE_W = 87.5 mm`
- `DOOR_ENVELOPE_H = 47.0 mm`
- `DOOR_PLANAR_W = derived`
- `DOOR_PLANAR_H = derived`

The controlling requirement for cabinet fit is the **formed overall envelope** because the 90 × 50 mm cell pitch must retain the intended nominal gaps.
