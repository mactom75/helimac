# HELIMAC design — revision J2 (2026-11-21)

**Status:** current design revision. Revisions H / H1 are withdrawn.
Rev J was created when the standard pilot mass was raised from 90 kg to **110 kg** (height 1.70–1.90 m).

## CAD graphics

Rendered views and sections from the rev J2 CAD model: [drive unit](../hardware/README.md#drive-unit-rev-j2) · [motor](../hardware/motor/README.md) · [cycloidal transmission](../hardware/transmission/README.md) · [blades](../hardware/blades/README.md) · [MC-P inverter](../electronics/mc-p-inverter/README.md). Also shown on [helimac.pl](https://helimac.pl/en/#drive).

## Key figures

| Quantity | Rev J2 | Rev H (for reference) |
|---|---|---|
| Configuration | coaxial, two rotors Ø 4.5 m, 500 rpm | same |
| Rotor heights above ground | lower 2395 mm / upper 2785 mm | −25 mm |
| Empty machine mass | 74.9 kg | 69.7 kg |
| Battery | 40.3 kg | same |
| Take-off mass | 225.2 kg (rotor design limit 225.3 kg — margin 0.1 kg) | — |
| Hover power (rotor) | 20.7 kW, FM 0.805 | 17.4 kW |
| Flight time vs. rev H | × 0.84 | — |
| Flight time, 200 Wh/kg cells | ≈ 14 / 25 min | — |
| Flight time, Amprius cells | ≈ 20 / 35 min | — |

> Any further mass increase requires the rotor to be recalculated.

## Changes rev H → J2

| Assembly | Change | Δ mass |
|---|---|---|
| Cycloidal transmission | 20 mm cams, K 75×83×20 cages, NKI 10/20 rollers (36 pcs), housing +14 mm, oil 0.90 l, 2 × NF-A8 PWM fans in the swashplate ring | +0.95 kg |
| Motor | 56 mm stack (280 laminations), 8 turns, 8 × Ø 0.63 mm, magnets 25 × 11.2 × 5 mm, shaft +6 mm | +0.6 kg |
| Bearings | RB11020 (110×160×20); 6210-2RS1 + 7210 BEP (upper hub); planet cages K15×19×17; mast 323 mm, drive +5 mm | +1.5 kg |
| Blades | chord 198 → 125.4 mm, θ0.75R upper 9.69° / lower 10.43°, 4.25 kg each | +0.95 kg |
| Frame | CFRP legs Ø 45 × 2.5 (sockets Ø 40 g6), side safety factor 1.80 | +0.64 kg |
| Seat | battery 50 mm aft, footrest 450 mm, XL harness | +0.34 kg |
| Swashplate, lower collective | ring 95 mm high, C10/C11 +6 mm, C13 links +19 mm, C07 rod 832 mm | +0.05 kg |
| Inverter | MC-P rev D1 with C3M0016120K | 0 |
| 400 V wiring | DC 25 mm², fuse and contactor ≥ 125 A | +0.2 kg |

## Bearing life (% of rev H)

| Bearing | Life |
|---|---|
| Cam cages | 169 % |
| NKI 10/20 rollers | ≈ 170 % |
| RB11020 | 225 % (≈ 17 800 h) |
| Planet cages K15×19×17 | 290 % (≈ 990 h) |
| 6210 | 296 % |
| 7210 | 280 % |
| HK5025 (unchanged) | 33 % (≈ 32 000 h) |
| 61818 (unchanged) | 59 % (≈ 175 000 h) |
| 61812 (unchanged) | ≈ 98 % |

## Verification results (calculated)

- **Transmission:** torque hover 395 N·m / climb 472 N·m; capacity ≈ 530 / 720 N·m; Hertz stress ≈ 1100 MPa; cage L10 ≈ 1100 h (replace every 500 h).
- **Oil temperature:** ≈ 76 °C at 20 °C ambient, ≈ 96 °C at 40 °C (with fans); PT100 warning at 105 °C.
- **Motor:** ≈ 57 A in hover, 11.4 A/mm² (limit 11.6), copper losses × 1.24, back-EMF ≈ 220 V (112S pack unchanged).
- **Inverter:** junction ≈ 99 °C in hover at 40 °C — see [MC-P](../electronics/mc-p-inverter/README.md).
- **Blades:** ultimate stress ≤ 600 MPa; flap frequency 1.46 /rev, lead-lag 2.42 /rev, divergence margin 5.8.
- **Seat:** harness karabiner 7.2 kN ultimate; stresses 367 / 398 / 250 MPa (allowable 500 / 540).

## Design decisions (technical)

- Motor: radial-flux motor kept. An axial-flux (YASA-type) motor was analysed at ≈ 25 kW / 4970 rpm and rejected — net mass change from +0.8 kg to −1.3 kg, flight-time gain a few seconds or negative.
- Halbach magnets and active vibration control in MC-C: not implemented.

## Tests planned

- Powertrain dynamometer: 395 N·m for 30 min (oil must stay ≤ 100 °C); stage-1 target 50 h on the dynamometer.
- Blade modal test.
- Tethered rotor spin-up.
