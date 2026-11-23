# Design parameters

Current design: **rev K — in design (2026-11-23)**. Details: [design-rev-K.md](design-rev-K.md), calculations: [calc/revK/](../calc/revK/). SI units. All values calculated, not measured.

## Rev K vs rev J2

| Parameter | rev J2 (archive) | **rev K (current)** |
|---|---|---|
| Machine without battery | 74.9 kg | **≈ 48.5 kg** (target ≈ 44 kg) |
| Battery | 40.3 kg | **40 kg** (112S4P Li-ion, ≈ 8 kWh) |
| Take-off mass (pilot 110 kg) | 225.2 kg | **≈ 198 kg** |
| Hover power (rotors) | 21.4 kW (re-checked; was 20.7) | **17.8 kW**, FM 0.77 |
| Minimum cruise power | ≈ 14 kW | **11.7 kW** at 16 m/s |
| Flight time hover / mixed | 15.5 / 20.5 min (re-checked; was 14 / 25) | **≈ 19 / 25 min** |
| Transmission | cycloidal 10:1 + bevel reversing gearbox, oil | **toothed-belt 12:1**, carbon cord, no oil |
| Motor | 4970 rpm, 56 mm stack, 8 turns | **6000 rpm, 50 mm stack, 7 turns** (same laminations and magnets) |
| Blades | 4.25 kg, ASA core; chord 198 → 125.4 mm | **≈ 2.5 kg**, PMI foam core + carbon D-spar; chord 170 → 115 mm |
| Frame | CFRP tripod | **3 Al 7075-T6 tubes** (front Ø40×1.5 ×2, rear Ø50×2) |
| Rotor heights | 2395 / 2785 mm | **2350 / 2730 mm** |
| Rotors | coaxial, 2 × 2 blades, Ø 4.5 m, 500 rpm | unchanged |
| Controls | weight shift, 5 collective actuators | unchanged |
| Inverter | MC-P rev D1 | unchanged (current) |

## Rev J2 — detailed parameters (archive)

Snapshot of rev J2 (2026-11-21), kept for history. Details: [design-rev-J2.md](design-rev-J2.md).

Status: 💭 idea · 📐 calculated · 🧪 measured · ✅ approved

| Parameter | Value | Status | Source / rationale |
|---|---|---|---|
| Seats | 1 | ✅ | project goal |
| Pilot mass (standard) | 110 kg, height 1.70–1.90 m | ✅ | owner decision, rev J |
| Take-off mass | 225.2 kg (rotor limit 225.3 kg) | 📐 | mass budget rev J2 |
| Machine mass without battery / with battery | 74.9 kg / 115.2 kg (battery 40.3 kg) | 📐 | mass budget rev J2 |
| Rotor configuration | coaxial, 2 rotors | ✅ | |
| Rotor diameter | 4.5 m | 📐 | |
| Rotor speed | 500 rpm | 📐 | |
| Rotor heights above ground | lower 2395 / upper 2785 mm | 📐 | rev J2 (tripod frame); may change after the D12 frame layout is recalculated |
| Blade chord | 198 mm constant from r = 330 to 1000 mm, linear taper to 125.4 mm at the tip (r = 2250 mm) | 📐 | rev J2 |
| Blade twist / mass | −12° per radius (≈ 10° along the blade) / 4.25 kg | 📐 | rev J2 |
| Motor | radial flux, outer rotor, 24 slots / 20 poles; ≈ 20.6 kW hover, ≈ 24.6 kW climb, ≈ 27 kW peak at 4970 rpm | 📐 | axial-flux alternative rejected |
| Transmission | cycloidal 10:1, two 20 mm cams | 📐 | |
| Transmission torque (hover / climb) | 395 / 472 N·m | 📐 | |
| Collective actuators | 5 × Feetech STS3250, collective only: upper rotor 2 (shared lever → Ø12 carbon rod in column/mast → spider → 2 links; channels A + B), lower rotor 3 (stationary ring → Ø330 bearing → rotating ring → 2 links; 2 × A + 1 × B) | ✅ | owner, 2026-11-22 |
| Inverter | MC-P rev D1, SiC C3M0016120K | 📐 | [MC-P](../electronics/mc-p-inverter/README.md) |
| Battery | 40.3 kg, 112S, ≈ 400 V | 📐 | |
| Hover power (rotor) | 20.7 kW, FM 0.805 | 📐 | `calc/helimac_calc.py` |
| Flight time (hover / mixed) | pilot 110 kg: ≈ 14 / 25 min; pilot 90 kg: ≈ 16 / 27–28 min (200 Wh/kg cells; mixed = 30 % hover, 70 % cruise) | 📐 | BEM rev J2 |
| Take-off mass with 90 kg pilot | 205.2 kg, hover power 18.2 kW | 📐 | BEM rev J2 |
| Emergency / recovery system | — | 💭 | |

## Change history

| Date | Parameter | Was → Now | Reason |
|---|---|---|---|
| 2026-11-23 | Design revision | rev J2 → **rev K**: belt drive, foam-core blades, Al frame; machine 74.9 → ≈ 48.5 kg | mass target ≈ 40 kg (decision D14), recalculated from scratch |
| 2026-11-23 | rev J2 re-check | hover 20.7 → 21.4 kW; flight time 14 / 25 → 15.5 / 20.5 min | rev K model applied to rev J2 |
| 2026-11-21 | Pilot mass | 90 → 110 kg | rev J |
| 2026-11-21 | Mass without battery | 69.7 → 74.9 kg | rev J / J2 changes |
| 2026-11-21 | Hover power | 17.4 → 20.7 kW | higher take-off mass |
| 2026-11-21 | Blade chord | root 180 → 198 mm, tip 114 → 125.4 mm (+10 %) | rev J |
