# HELIMAC Build Log · Dziennik budowy

Project progress — newest entries first. Entries may be in English and/or Polish.
*Postępy projektu — najnowsze wpisy na górze. Wpisy po angielsku i/lub po polsku.*

---

## 2026-11-22 — Website helimac.pl

- Project website launched at [helimac.pl](https://helimac.pl/) (Polish) and [helimac.pl/en](https://helimac.pl/en/) (English), hosted on GitHub Pages from `website/`.
- Design idea stated: inspired by Dr. Franz Schöffmann's backpack helicopter — radical simplicity, weight-shift piloting like a hang glider, easy transport.
- Controls: direction by weight shift (rigid hubs, no cyclic); collective via electric actuators, no swashplate; yaw by differential pitch.

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
