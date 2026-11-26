# HELIMAC rev K — design update 26 Nov 2026

Drive, rotor, collective control and inverter. Continues [design-rev-K.md](design-rev-K.md).
Drawings and graphics: [graphics/revK/2026-11-26/](graphics/revK/2026-11-26/) · blade templates: [hardware/blades/revK-templates/](../hardware/blades/revK-templates/).

> **All values are calculated (FEM, BEM, strength), not measured.** Measurements will follow on the dynamometer (stage 1) and the rotor test stand.
>
> **Status:** motor B is **approved** (decisions D19, D19a). Rotor airfoil and speed, belt drive, collective control, hub, actuator mounting, collective rings and inverter (D20–D26) are **recommendations awaiting the owner's approval**.

## 1. Key figures (26 Nov 2026, calculated)

| Parameter | Value |
|---|---|
| Machine without battery | ≈ 43.4 kg (rev J2: 74.9 kg) |
| Battery | 40 kg, 112S, 403 V, ≈ 8 kWh |
| Pilot (design) | 110 kg |
| Take-off mass | ≈ 193 kg |
| Rotors | 2 coaxial, counter-rotating, Ø 4.5 m, 500 rpm, 2 blades each |
| Hover power | ≈ 16–16.6 kW |
| Power at 1.3 g, hot day | ≈ 25 kW (26.2 kW at the motor shaft) |
| Motor | 30 kW continuous, 10 000 rpm, ≈ 6 kg |
| Flight time | hover ≈ 21 min, mixed ≈ 28–29 min (rev K of 23 Nov: 19.7 / 25.8 min) |

## 2. Motor B — 30 kW, 10 000 rpm, Halbach magnets (D19, D19a — approved)

- Outer-rotor motor: a rotating cup with magnets around the stationary wound stator.
- **Halbach array** (4 segments per pole) focuses the field inwards, so the rotor needs no steel back-iron. Rotor cup Al 7075 with fan blades.
- 18 slots / 16 poles, electrical frequency 1333 Hz.
- Outer diameter 214 mm, stack 24 mm.
- FEM: **28.5 N·m at 84 A**, torque ripple 2.2 %; losses ≈ 810 W, efficiency ≈ 97 %.
- Magnets N48SH, blocks 9 × 6 × 7.9 mm, 192 pcs; three magnetisation directions: radial, tangential and 45° diagonal (diagonal made to order).
- Winding: 9 turns per coil, bundle 45 × Ø 0.5 mm, star connection.
- Bearings 2 × 6206-2Z/C3; the lower bearing moved into the spider above the pulley.
- Mass ≈ 6 kg (previous motor 7.1 kg).

Graphics: `01a`–`01c` (magnetic field, torque and back-EMF from FEM), `02a`, `02b` (data sheet).

## 3. Rotor — airfoil and speed (D20 — recommendation)

- 13 airfoils compared; for each, 380–620 rpm, several chords and twists (566 variants).
- Choice: **VR-7 with a 4° up-turned trailing-edge tab** — the tab reduces the blade pitching moment almost threefold, so the actuators work less.
- Flat optimum 470–530 rpm; **500 rpm** chosen (tip speed 118 m/s, quiet).
- Versus NACA 23012: ≈ 3 % less power, ≈ 1.4 min longer flight.

Graphics: `02c`, `02d`.

## 4. Blades (drawings ŁOP-01…03)

- Chord 150 mm up to 1 m from the rotor axis, tapering to 102 mm at the tip; twist −8°; mass **2.04 kg**.
- Foam core; carbon "D" spar with unidirectional caps (up to 12 plies); ±45° carbon skin; **tungsten tip mass 0.665 kg** (energy store for autorotation).
- Prototype: XPS/EPS core cut with a hot wire, epoxy only. Series: CNC-milled PU foam.
- Upper-rotor blades are the mirror image of the lower ones → two moulds.
- Hot-wire templates (DXF, left/right, r = 450 / 1000 / 1600 / 2230 mm) and the airfoil coordinates: [hardware/blades/revK-templates/](../hardware/blades/revK-templates/).

## 5. Belt drive 20:1 (D21 — recommendation)

- Carbon-cord toothed belts 8M, two stages: **24/96 (4:1)**, then **2 × 24/120 (5:1)**.
- Speeds: motor 10 000 → intermediate shafts 2500 → rotors 500 rpm.
- A pair of spur gears reverses one intermediate shaft → counter-rotating rotors.
- Stage-1 belt speed 32 m/s (allowed 33 m/s).
- Motor mounted upside down above the belts, 212 mm from the rotor axis (previously 258 mm).
- **One-way clutch** (CSK35) lets the rotors autorotate when the motor stops.
- Mass 8.55 kg; collision check in every belt plane: 0 collisions.

Graphics: `04_przekladnia_PP-01…03`.

## 6. Collective pitch control (D22 — recommendation)

- Both rotors have variable pitch: the rotors are belt-coupled (always the same speed), so thrust and yaw are controlled only by blade pitch — two tasks need two independent angles.
- Pitch at 3/4 radius: mechanical range −2° … +15°; hover 8.9° (upper) / 9.7° (lower); autorotation ≈ 2.7°; yaw: ±0.6° difference gives ±40 N·m.
- Actuators: 5 × STS3250 (2 upper rotor, 3 lower). Blade pitch-link force 114 N (design). Transition to autorotation (7° change) ≈ 0.07 s.
- **Fail-safe tendency:** aerodynamic and centrifugal forces reduce blade pitch — if the control fails, the blades move towards autorotation.
- Note: drawings SK-01 and SK-02 still show a joint radius of 100 mm; the correct radius is **116.6 mm at 31°** (see MS and TS).

Graphics: `05_sterowanie_skokiem_SK-01…03`.

## 7. Hub and blade attachment (D23 — recommendation)

- The blade pitches on a spindle machined in one piece with the hub body (Al 7075).
- Bearings: 2 × HK4020 needle bearings + 51107 thrust bearing (carries the centrifugal force). No elastomers.
- Blade held in a fork by 2 pins Ø 12 — removal in about 5 min.
- Centrifugal force per blade: 7.4 kN at 500 rpm, 9.8 kN at 575 rpm.
- Pre-cone 4.3°: in hover the blade root is almost free of bending.
- Mass 1.9 kg per rotor.

Graphics: `06_piasta_PD-01…03`.

## 8. Actuator mounting and collision check (D24 — recommendation)

- 3D collision check of 35 parts with rotation and full control travel: **0 collisions, minimum clearance 9.5 mm**.
- Upper-rotor actuators moved below the pulley onto frame W1 (previously they hit the rotating pulley).
- Lowest point of the drive: 2044 mm above ground.
- Lower-rotor actuators sit in cradles W2 on the spider above the belts.

Graphics: `07_montaz_silownikow_MS-01…03`.

## 9. Collective rings (D25 — recommendation)

The actuators are stationary and the blades rotate, so the motion is passed from a stationary to a rotating part. The rings only slide vertically (±9 mm) — no tilting, because there is no cyclic control.

- Lower rotor: stationary ring + thin-section bearing CSXA047 + rotating ring guided on keys on the shaft; 0.5 kg.
- Upper rotor: stationary-to-rotating transfer in a housing with 2 × 7201 B bearings at the bottom of the control rod.

Graphics: `08_tarcze_skoku_TS-01…02`.

## 10. Inverter (D26 — recommendation)

- **MC-P rev D1 fits motor B without PCB changes.** To change: current sensors (±150 A version) and firmware (16 poles, 32 kHz switching, field weakening).
- Hover 48 A, losses 210 W, junction ≈ 78 °C; 1.3 g on a hot day 74 A, briefly ≈ 127 °C.
- Cooling: heatsink with vertical fins in the rotor downwash (9–10 m/s) + 2 fans for ground running and as a reserve.
- Mounted on the battery box, behind the rear leg; mass with cables 2.23 kg.

Graphics: `09_falownik_FL-01…03`.

## 11. Mass changes on 26 Nov (from 44.3 kg on 23 Nov)

| Change | kg |
|---|---|
| Motor B (6.1 kg, lower bearing in the spider) instead of 7.1 kg | −1.2 |
| Belt drive 20:1 with spider (8.55 kg) instead of 7.5 + 0.6 | +0.45 |
| VR-7 blades, 4 × 2.04 kg instead of 4 × 2.21 kg | −0.67 |
| Hubs with blade grips (2 × 1.88 kg) instead of 2.8 kg | +0.96 |
| Collective ring with CSXA047 instead of 61822 | −0.1 |
| Inverter with cables (2.23 kg) instead of 2.6 kg | −0.37 |
| **Total** | **−0.93 → ≈ 43.4 kg** |

## 12. To check before building

- Blade natural frequencies and flutter (Campbell diagram) for the new 150/102 mm chord.
- Drawing ŁOP-01: change the pre-cone to 4.3° and check the tip clearance between the two rotors.
- Belt widths: confirm with the belt maker's selection software.
- Dynamometer: losses and temperatures of motor B and the inverter; 30 min test at 26 kW.
- Rotor test stand: thrust, power, blade angles and pitch-link forces.
- Drawings SK-01 and SK-02: correct the joint radius to 116.6 mm at 31°.
