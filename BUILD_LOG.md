# HELIMAC Build Log · Dziennik budowy

Project progress — newest entries first. Entries may be in English and/or Polish.
*Postępy projektu — najnowsze wpisy na górze. Wpisy po angielsku i/lub po polsku.*

---

## 2026-11-23 — Rev K: recalculating the design from scratch

Rev J2 weighed 74.9 kg without the battery – too much. We recalculated the whole design from the beginning: mass, power, rotors, motor, transmission, controls, electronics and frame. Main changes: a toothed-belt drive instead of the cycloidal and bevel gearboxes (no oil, about 15 kg lighter), foam-core blades with a carbon-fibre spar (about 7 kg lighter), and a frame made of three aluminium tubes. Machine without battery: about 43.7 kg (−42 %), take-off mass about 194 kg, flight time about 20 min hovering and about 26 min in mixed flight. Next step: 3D model and drawings for rev K.

- Weight reductions applied the same day (48.5 → 43.7 kg): 8000 rpm motor with a 37 mm stack, belt drive 16:1 with 10-spoke milled pulleys, hubs integrated with blade grips, inverter heatsink in the rotor downwash, smaller blade tip masses with a faster automatic collective drop, carbon column, lighter seat, shorter 400 V cables.

- CAD graphics of the rev K concept model: complete machine, frame, drive unit, belt drive, 10-spoke pulley, blade, motor and 2D FEM — [docs/graphics/revK/](docs/graphics/revK/).
- New: [docs/design-rev-K.md](docs/design-rev-K.md), layout sketch [docs/graphics/HELIMAC_revK_szkic_ukladu.pdf](docs/graphics/HELIMAC_revK_szkic_ukladu.pdf), calculations [calc/revK/](calc/revK/).
- Rev J2 production packages J1–J3 are now archive (do not build); MC-P inverter rev D1 stays current.
- Rev J2 re-checked with the new model: hover 21.4 kW, flight time ≈ 15.5 / 20.5 min.

*PL: Rev J2 ważyła 74,9 kg bez akumulatora – za dużo. Przeliczyliśmy cały projekt od początku. Przekładnia pasowa zamiast cykloidalnej i stożkowej (bez oleju, ok. 15 kg mniej), łopaty z pianki z dźwigarem węglowym (ok. 7 kg mniej), rama z trzech rur aluminiowych. Maszyna bez akumulatora ok. 43,7 kg (−42 %), masa startowa ok. 194 kg, czas lotu ok. 20 / 26 min. Następny krok: model 3D i rysunki rev K.*

## 2026-11-22 — Drive unit mass corrected on ZS-00

- General assembly drawing ZS-00 (package J1): drive unit mass corrected from "approx. 27.7 kg" to **approx. 38.5 kg** (without blades and frame adapter), matching the parts list (rev H 35.4 kg + rev J/J2 changes +3.05 kg). With the frame adapter and two upper collective servos ≈ 40 kg; machine mass 74.9 kg unchanged.

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
