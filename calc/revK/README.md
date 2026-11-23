# Rev K — design calculations

Licence: **GPL-3.0-or-later** (see [LICENSES/GPL-3.0-or-later.txt](../../LICENSES/GPL-3.0-or-later.txt)).
Results described in [docs/design-rev-K.md](../../docs/design-rev-K.md). All values are **calculated, not measured**. Comments in the scripts are in Polish.

| Script | What it does |
|---|---|
| `sizing.py` | design loop: mass ↔ power ↔ rotor ↔ drive ↔ battery (efficiencies, auxiliary power, usable energy) |
| `rotor.py` | coaxial rotor model: hover / forward-flight power, autorotation |
| `blade_mass.py` | blade mass from foam core, carbon spar and skin |
| `motor_dd.py` | direct-drive motor variant (500 rpm, no transmission) — sizing study used in the drive comparison |
| `variants.py` | compares drive variants → `results/variants.json` |
| `final2.py` | rev K design point after stage 2 (≈ 48.5 kg) → `results/final2.json` |
| `final3.py` | **current rev K design point** after weight reductions (≈ 43.7 kg, 8000 rpm motor, faster collective drop) → `results/final3.json` |
| `pulley.py` | 8M spoked pulleys, Al 7075-T6: number of spokes vs rim mass, deflection and fatigue → `results/pulley.json` |
| `stage2.py` | stage 2 checks (belts, spur pair, column, blade, pitch bearing, collective, frame) → `results/stage2.json` |

## Run

Requires Python 3 with NumPy. From any directory:

```bash
python3 calc/revK/variants.py   # must run first: stage2.py reads results/variants.json
python3 calc/revK/final2.py
python3 calc/revK/final3.py
python3 calc/revK/stage2.py
python3 calc/revK/pulley.py
```

The results in `results/` are reproduced exactly by these scripts (checked 2026-11-23).
