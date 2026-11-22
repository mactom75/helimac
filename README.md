# 🚁 HELIMAC

**Open-source single-seat electric helicopter**

🇬🇧 English · [🇵🇱 Polski](README.pl.md) · 🌐 **Website: [helimac.pl](https://helimac.pl/en/)**

> ⚠️ **Early concept stage.** Nothing in this repository is yet a verified, buildable design. Read [SAFETY.md](SAFETY.md) before anything else.

---

## About

**HELIMAC** is an international, open-source project to design and build a light, single-seat helicopter with a fully electric powertrain.

The name combines **HELI**copter and **MAC**iąg — the surname of the project's founder, **Tomasz Maciąg** from Bydgoszcz, Poland. It continues his original **HeliMac** project (2013–2015), now redesigned from scratch and developed with the help of AI tools. **[Read the story →](ABOUT.md)**

### Goals

- Design a single-seat electric helicopter openly, together with contributors from around the world.
- Aim for the ultralight category of **Annex I to Regulation (EU) 2018/1139** (single-seat helicopter, MTOM ≤ 300 kg), which falls under national rules rather than EASA certification — see [docs/regulations.md](docs/regulations.md).
- Use parts and processes available to a well-equipped workshop.
- Publish everything: drawings, calculations, software, test results — and mistakes.

## Current design — rev J2

| | |
|---|---|
| Configuration | coaxial, 2 rotors Ø 4.5 m, 500 rpm |
| Pilot | up to 110 kg |
| Take-off mass | 225.2 kg (empty machine 74.9 kg, battery 40.3 kg) |
| Hover power | 20.7 kW |
| Powertrain | radial-flux motor → cycloidal transmission; in-house SiC inverter MC-P |
| Battery | 112S, ≈ 400 V |
| Current stage | **Stage 1 — powertrain + power supply** (dynamometer) |

Full details: [docs/design-rev-J2.md](docs/design-rev-J2.md).

## Current status

Files and specifications are published **progressively, as the design and the vehicle are built**.

- Progress: [BUILD_LOG.md](BUILD_LOG.md)
- Current design parameters: [docs/parameters.md](docs/parameters.md)
- Plan: [ROADMAP.md](ROADMAP.md)
- **Production files** (drawings, DXF, STEP, STL, KiCad, Gerbers — ZIP downloads): [production/](production/)
- Early-estimate tool (hover power, endurance, rotor size): [calc/](calc/)

## Repository layout

```
helimac/
├── ABOUT.md              founder and project history
├── BUILD_LOG.md          progress log
├── docs/                 design revision, parameters, regulations
├── calc/                 calculations and tools (Python) + tests
├── production/           production packages rev J2 (ZIP downloads)
├── hardware/             mechanical design (CAD, drawings, BOM)
│   ├── frame/  seat/  rotor-head-and-controls/  blades/  transmission/  motor/
├── electronics/          MC-P inverter, MC-C controller, battery + BMS, avionics
├── firmware/             software (monitoring, displays, logging)
├── LICENSES/             full licence texts
└── .github/              issue/discussion templates, CI
```

## Get involved

1. **Say hello** in [Discussions → Introductions](../../discussions).
2. **Read** [CONTRIBUTING.md](CONTRIBUTING.md) and [SAFETY.md](SAFETY.md).
3. **Pick a task** from [Issues](../../issues) or propose your own.

We especially welcome: aircraft structural engineers, rotor and flight-dynamics specialists, power-electronics and battery engineers, helicopter pilots, aircraft mechanics, and people familiar with light-aircraft regulations in their country.

**Languages:** English is the main project language. Polish is equally welcome — write in whichever you're comfortable with.

## Follow the build

▶️ **YouTube:** [@Helimac-pl](https://www.youtube.com/@Helimac-pl) — build videos, tests and progress updates.

☕ **Support the build:** [buycoffee.to/helimac](https://buycoffee.to/helimac) — every coffee helps pay for parts and dynamometer tests.

## Communication

| Channel | Use it for |
|---|---|
| **Discussions** | ideas, questions, technical discussions, introductions |
| **Issues** | specific tasks, errors in calculations/docs, change proposals |
| **Pull Requests** | contributing files |
| **Releases** | downloadable file packages (drawings, PDFs, BOM) per version |
| **YouTube** | [@Helimac-pl](https://www.youtube.com/@Helimac-pl) — videos of the build and tests |
| **Support** | [buycoffee.to/helimac](https://buycoffee.to/helimac) — help pay for parts and tests |

## Licences

| What | Licence |
|---|---|
| Hardware (CAD, drawings, schematics, BOM) | [CERN-OHL-S-2.0](LICENSES/CERN-OHL-S-2.0.txt) |
| Software (`calc/`, `firmware/`) | [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) |
| Documentation (`docs/`, `.md` files) | [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt) |

See [LICENSE](LICENSE). Provided **without any warranty**.

---

**Founder & maintainer:** Tomasz Maciąg · Bydgoszcz, Poland
