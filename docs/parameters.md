# Design parameters

Current design snapshot — **rev J2 (2026-11-21)**. Details: [design-rev-J2.md](design-rev-J2.md). SI units.

Status: 💭 idea · 📐 calculated · 🧪 measured · ✅ approved

| Parameter | Value | Status | Source / rationale |
|---|---|---|---|
| Seats | 1 | ✅ | project goal |
| Pilot mass (standard) | 110 kg, height 1.70–1.90 m | ✅ | owner decision, rev J |
| Take-off mass | 225.2 kg (rotor limit 225.3 kg) | 📐 | mass budget rev J2 |
| Empty machine mass | 74.9 kg | 📐 | mass budget rev J2 |
| Rotor configuration | coaxial, 2 rotors | ✅ | |
| Rotor diameter | 4.5 m | 📐 | |
| Rotor speed | 500 rpm | 📐 | |
| Rotor heights above ground | lower 2395 / upper 2785 mm | 📐 | rev J2 |
| Blade chord / mass | 125.4 mm / 4.25 kg | 📐 | rev J2 |
| Motor | radial flux, ≈ 25 kW at ≈ 4970 rpm | 📐 | axial-flux alternative rejected |
| Transmission | cycloidal | 📐 | |
| Transmission torque (hover / climb) | 395 / 472 N·m | 📐 | |
| Inverter | MC-P rev D1, SiC C3M0016120K | 📐 | [MC-P](../electronics/mc-p-inverter/README.md) |
| Battery | 40.3 kg, 112S, ≈ 400 V | 📐 | |
| Hover power (rotor) | 20.7 kW, FM 0.805 | 📐 | `calc/helimac_calc.py` |
| Flight time | ≈ 14 / 25 min (200 Wh/kg cells) | 📐 | |
| Emergency / recovery system | — | 💭 | |

## Change history

| Date | Parameter | Was → Now | Reason |
|---|---|---|---|
| 2026-11-21 | Pilot mass | 90 → 110 kg | rev J |
| 2026-11-21 | Empty mass | 69.7 → 74.9 kg | rev J / J2 changes |
| 2026-11-21 | Hover power | 17.4 → 20.7 kW | higher take-off mass |
| 2026-11-21 | Blade chord | 198 → 125.4 mm | rev J |
