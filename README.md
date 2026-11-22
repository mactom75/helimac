<p align="center">
  <a href="https://helimac.pl/en/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="website/assets/img/logo-dark-600.webp">
      <img src="website/assets/img/logo-600.png" alt="HELIMAC" width="420">
    </picture>
  </a>
</p>

<p align="center"><b>Open-source single-seat electric helicopter</b><br>
coaxial rotors · weight-shift control · 400 V electric drive · built in the open</p>

<p align="center">
  🇬🇧 English · <a href="README.pl.md">🇵🇱 Polski</a> · 🌐 <a href="https://helimac.pl/en/">helimac.pl</a> · ▶️ <a href="https://www.youtube.com/@Helimac-pl">YouTube</a> · ☕ <a href="https://buycoffee.to/helimac">Support</a>
</p>

---

## Start here

| I want to… | Go to |
|---|---|
| 👀 **see the design** | [Design rev J2](docs/design-rev-J2.md) · [parameters](docs/parameters.md) · [website](https://helimac.pl/en/) |
| 📦 **download the files** | [Latest release (4 ZIP packages)](../../releases/latest) · [browse production files](production/) — drawings, DXF, STEP, STL, KiCad, Gerbers |
| 🛠️ **help build it** | [Open tasks (Issues)](../../issues) · [Discussions](../../discussions) · [How to contribute](CONTRIBUTING.md) |
| ▶️ **follow the build** | [YouTube @Helimac-pl](https://www.youtube.com/@Helimac-pl) · [build log](BUILD_LOG.md) · [roadmap](ROADMAP.md) |
| ☕ **support the project** | [buycoffee.to/helimac](https://buycoffee.to/helimac) — every coffee goes to parts and dynamometer tests |

> ⚠️ **Prototype in design — not an approved aircraft.** All values are calculated, not yet measured. Read [SAFETY.md](SAFETY.md) before building anything.

<p align="center">
  <a href="hardware/README.md#drive-unit-rev-j2"><img src="website/assets/img/cad/01-naped-izometria-1400.webp" alt="HELIMAC drive unit — CAD model rev J2" width="640"></a><br>
  <sub>Drive unit rev J2: motor, cycloidal transmission 10:1, reversing gearbox and rotor hubs (CAD model)</sub>
</p>

## What is HELIMAC?

A light, single-seat helicopter with a fully electric drive, designed openly with contributors from around the world. Every drawing, calculation, piece of software, test result — and mistake — is published here.

The name combines **HELI**copter and **MAC**iąg — the surname of the founder, **Tomasz Maciąg** from Bydgoszcz, Poland. It continues his original **HeliMac** project (2013–2015), now redesigned from scratch with the help of AI tools. **[Read the story →](ABOUT.md)**

Target category: single-seat ultralight helicopter, MTOM ≤ 300 kg ([Annex I to Regulation (EU) 2018/1139](docs/regulations.md) — national rules instead of EASA certification).

## Current design — rev J2

| | |
|---|---|
| Configuration | coaxial, 2 × 2-blade rotors Ø 4.5 m, 500 rpm, no tail rotor |
| Control | direction by pilot weight shift (no cyclic) · collective by electric actuators · yaw by upper/lower collective difference |
| Pilot | up to 110 kg |
| Take-off mass | 225.2 kg (machine without battery 74.9 kg, battery 40.3 kg) |
| Hover power | 20.7 kW |
| Drive | outer-rotor PMSM motor (≈ 21 kW hover) → cycloidal transmission 10:1 → reversing bevel gearbox |
| Electronics | in-house SiC inverter **MC-P** rev D1 (KiCad) · control board **MC-C** in design |
| Battery | 112S Li-ion, ≈ 400 V |
| Flight time (calc.) | ≈ 14 min hover / ≈ 25 min mixed (200 Wh/kg cells) |
| **Current stage** | **Stage 1 — drive + power supply** → dynamometer 395 N·m / 30 min, then 50 h |

## What's where

| Folder | Inside |
|---|---|
| [production/](production/) | **ready-to-make files** rev J2 — 4 ZIP packages (J1 drive, J2 blades, J3 frame & seat, MC-P inverter) |
| [hardware/](hardware/) | assembly overviews with CAD graphics: frame, seat, rotor head & controls, blades, transmission, motor |
| [electronics/](electronics/) | MC-P inverter, MC-C controller, battery + BMS, avionics |
| [docs/](docs/) | design revision, parameters, regulations, [graphics (PDF)](docs/graphics/) |
| [calc/](calc/) | performance calculator (Python) |
| [firmware/](firmware/) | software (to come) |

## Get involved

We especially welcome aircraft structural engineers, rotor and flight-dynamics specialists, power-electronics and battery engineers, helicopter pilots, aircraft mechanics, makers with 3D printers and CNC, and people who know light-aircraft rules in their country.

1. **Say hello** in [Discussions](../../discussions).
2. **Pick a task** from [Issues](../../issues) — e.g. [#1 400 V inverter review](../../issues/1) or [#6 calculator](../../issues/6) (good first issue).
3. **Read** [CONTRIBUTING.md](CONTRIBUTING.md) and [SAFETY.md](SAFETY.md).

English is the main project language; Polish is equally welcome.

## Licences

Hardware: [CERN-OHL-S-2.0](LICENSES/CERN-OHL-S-2.0.txt) · Software: [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) · Documentation: [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt) · The HELIMAC name and logo are not covered by these licences ([branding/](branding/)). Provided **without any warranty** — see [LICENSE](LICENSE).

---

**Founder & maintainer:** Tomasz Maciąg · Bydgoszcz, Poland · [helimac.pl](https://helimac.pl/en/)
