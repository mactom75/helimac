# HELIMAC Build Log · Dziennik budowy

Project progress — newest entries first. Entries may be in English and/or Polish.
*Postępy projektu — najnowsze wpisy na górze. Wpisy po angielsku i/lub po polsku.*

---

## 2026-11-22 — Graphics PDFs, blade chord clarified

- PDF sheets with CAD graphics, A3 sketches (drive section, inverter wiring) and motor FEM plots in [docs/graphics/](docs/graphics/).
- Blade chord (rev J): 198 mm constant to r = 1 m, linear taper to 125.4 mm at the tip — "198 → 125.4" means root → tip, not a change between revisions.

## 2026-11-22 — Production files rev J2 published

- New folder [production/](production/) with four ZIP packages ready to download: **J1** drive unit rev J2 (drawings, 18 DXF cutting files, 41 STEP parts + full assembly), **J2** rotor blades rev J (drawings, CNC sections, STL for cores and jigs), **J3** frame, seat, PK ring, lower collective rev J2 (drawings, STEP, STL), **MC-P** inverter rev D1 (KiCad 7 project, Gerbers, BOM, CPL, schematic, mechanical drawing).
- MC-P sources updated to rev D1: Q1–Q6 = C3M0016120K (16 mΩ) in the schematic and PCB; schematic PDF regenerated.
- Frame layout is being recalculated — frame tubes not to be made yet.

## 2026-11-22 — Website helimac.pl

- Project website launched at [helimac.pl](https://helimac.pl/) (Polish) and [helimac.pl/en](https://helimac.pl/en/) (English), hosted on GitHub Pages from `website/`.
- Design idea stated: inspired by Dr. Franz Schöffmann's backpack helicopter — radical simplicity, weight-shift piloting like a hang glider, easy transport.
- Controls: direction by weight shift (rigid hubs, no cyclic); collective via 5 electric actuators (2 upper rotor, 3 lower rotor), no swashplate; yaw by differential pitch.

## 2026-11-22 — CAD graphics rev J2

- 14 graphics from the rev J2 CAD model added to the assembly pages: drive unit, motor, cycloidal transmission, blades (3D-printed core segments), MC-P inverter.

## 2026-11-22 — Public repository

- HELIMAC published as an open-source project on GitHub.

## 2026-11-21 — Design rev J2 (pilot 110 kg)

- Standard pilot mass raised to 110 kg → new design revision J, then J2 (bearings ≥ 100 % of rev H life).
- Take-off mass 225.2 kg, hover power 20.7 kW. Details: [docs/design-rev-J2.md](docs/design-rev-J2.md).
- Inverter MC-P: compact rev D (215 × 116 mm, −40 % area), then rev D1 with C3M0016120K SiC MOSFETs.
- Inverter cooling: 2 × NF-A8 PWM across the fins (one fan was insufficient).

## 2026-11-18 — Project start

- Build order: **stage 1 = powertrain + power supply** (target: 50 h on the dynamometer); frame, collective and blades in stage 2.
- Electronics (MC-P inverter, MC-C controller, AV avionics) designed in-house.

---

<!--
Entry template / Szablon wpisu:

## YYYY-MM-DD — Title

- Done:
- New / changed files:
- Problems / lessons learned:
- Photos: (link to folder or Release)

**Next:**
-->
