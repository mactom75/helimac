# HELIMAC rev K — redesign from scratch (concept, stage 2)

Status: **in progress (23 Nov 2026)**. Rev K replaces rev J2. Do not manufacture rev J2 parts (`production/`, packages J1–J3). The MC-P rev D1 inverter stays.
All values are **calculated, not measured**. Calculation scripts: [`calc/revK/`](../calc/revK/).

## Why rev K
Rev J2 came out at 74.9 kg without battery. Most of this was the drive: the cycloidal gearbox plus the bevel reversing gearbox weighed about 20 kg, and the blades about 17 kg (3D-printed ASA cores). The owner set a target of about 40 kg without battery (decision D14), so the whole design was recalculated from the beginning: mass → power → rotor → motor → transmission → controls → electronics → frame.

## Main changes vs rev J2
| Area | rev J2 | rev K |
|---|---|---|
| Transmission | cycloidal 10:1 + bevel reversing gearbox, oil 0.9 l, 2 fans, air-guide ring | **toothed-belt drive 12:1** (carbon-cord 8M belts): motor → intermediate shaft → 1:1 spur pair reverses direction → two final belts to the coaxial shafts; no oil, efficiency ≈ 97 % |
| Blades | printed ASA core, 4.25 kg each | **PMI foam core, unidirectional carbon D-spar, ±45° carbon skin**, ≈ 2.5 kg each (incl. ≈ 0.9 kg tip mass for autorotation) |
| Motor | 24/20 outer rotor, 56 mm stack, 8 turns, 4970 rpm | same lamination and magnets, **50 mm stack, 7 turns, 6000 rpm** (FEM 2D checked at 48 mm: 29.8 N·m at 55 A, scaled to 50 mm) |
| Frame | CFRP tripod | **three Al 7075-T6 tubes**: two front legs forming a triangle (Ø40×1.5), one slightly curved rear leg (Ø50×2) carrying seat, footrest, battery and electronics |
| Machine without battery | 74.9 kg | **≈ 48.5 kg** (−35 %), path to ≈ 44 kg identified |

## Main parameters (pilot 110 kg, battery 40 kg, ISA sea level)
| Parameter | Value |
|---|---|
| Take-off mass | ≈ 198 kg |
| Rotors | 2 × 2 blades, coaxial counter-rotating, Ø 4.5 m, 500 rpm (tip 118 m/s), spacing 0.38 m |
| Blade | chord 170 mm to r = 1.0 m, taper to 115 mm at tip, twist −12°, NACA 23012-type section |
| Hover power (rotors) | 17.8 kW, figure of merit 0.77 |
| Power 1.3 g, hot day (35 °C, 500 m) | 27.0 kW |
| Minimum cruise power | 11.7 kW at 16 m/s |
| Rotor torque (hover) | 170 N·m per rotor |
| Motor | 6000 rpm, hover 29 N·m / 56 A, max 44 N·m / 85 A, back-EMF ≈ 200 V line-line |
| Battery | 112S4P Li-ion (448 × 21700 high-power cells), ≈ 403 V nominal, ≈ 8 kWh, 40 kg |
| Flight time | ≈ 19 min hover / ≈ 25 min mixed (30 % hover, 70 % cruise), landing at 20 % charge |
| Autorotation | rotor speed falls 500 → 425 rpm in 0.55 s after power loss; automatic collective drop; descent ≈ 6 m/s in forward flight at 16 m/s |
| Rotor heights | lower 2.35 m, upper 2.73 m above ground |
| Frame footprint | front feet 1.40 m apart, front-to-rear 1.95 m; frame apex 2.05 m |

## Checks done in stage 2
- Belts: max effective tension 1.13 kN (stage 1, 21 mm, 24 m/s) and 1.67 kN (final stages, 36 mm, 8 m/s) — widths to be confirmed with the belt maker's selection software.
- Reversing spur pair m 2, z 50, b 20 mm, case-hardened: bending 97 MPa, contact 540 MPa.
- Fixed column Al 7075-T6 Ø70×4: safety 11 against yield at ultimate load (hub moment from weight-shift control included).
- Blade: root spar stress 276 MPa (allowable 600 MPa); flap 1.25/rev, lag 1.38/rev, torsion > 10/rev; centre of gravity ≤ 25 % chord; centrifugal force 9.2 kN.
- Pitch bearing: thrust bearing static safety 5.4.
- Collective: pitch-axis moment ≈ 2.8 N·m per blade; 5 servos as before (2 upper, 3 lower) have enough rated force.
- Frame at 3 g landing: front legs buckling safety 2.9; rear leg bending 270 MPa, needs an internal sleeve at the seat (FEM check next).

## Next (stage 3)
CAD model and drawings, motor mechanical design (shaft, pulley, bearings), belt drive drawings, hub and blade drawings with lay-up, frame FEM and joints, battery pack (two 56S4P halves with BMS), mass and centre-of-gravity check, then production packages rev K.
