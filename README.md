# 🚁 HELIMAC

**Open-source single-seat electric helicopter**

🇬🇧 English · [🇵🇱 Polski](README.pl.md)

> ⚠️ **Early concept stage.** Nothing in this repository is yet a verified, buildable design. Read [SAFETY.md](SAFETY.md) before anything else.

---

## About

**HELIMAC** is an international, open-source project to design and build a light, single-seat helicopter with a fully electric powertrain.

The name combines **HELI**copter and **MAC**iąg — the surname of the project's founder, **Tomasz Maciąg** from Bydgoszcz, Poland.

### Goals

- Design a single-seat electric helicopter openly, together with contributors from around the world.
- Aim for the ultralight category of **Annex I to Regulation (EU) 2018/1139** (single-seat helicopter, MTOM ≤ 300 kg), which falls under national rules rather than EASA certification — see [docs/regulations.md](docs/regulations.md).
- Use parts and processes available to a well-equipped workshop.
- Publish everything: drawings, calculations, software, test results — and mistakes.

## Current status

Files and specifications are published **progressively, as the design and the vehicle are built**.

- Progress: [BUILD_LOG.md](BUILD_LOG.md)
- Current design parameters: [docs/parameters.md](docs/parameters.md)
- Plan: [ROADMAP.md](ROADMAP.md)
- Early-estimate tool (hover power, endurance, rotor size): [calc/](calc/)

## Repository layout

```
helimac/
├── BUILD_LOG.md          progress log
├── docs/                 parameters, regulations, design decisions
├── calc/                 calculations and tools (Python) + tests
├── hardware/             mechanical design (CAD, drawings, BOM)
│   ├── frame/  main-rotor/  tail-rotor/  transmission/  landing-gear/
├── electronics/          powertrain, battery + BMS, avionics
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

## Communication

| Channel | Use it for |
|---|---|
| **Discussions** | ideas, questions, technical discussions, introductions |
| **Issues** | specific tasks, errors in calculations/docs, change proposals |
| **Pull Requests** | contributing files |
| **Releases** | downloadable file packages (drawings, PDFs, BOM) per version |

## Licences

| What | Licence |
|---|---|
| Hardware (CAD, drawings, schematics, BOM) | [CERN-OHL-S-2.0](LICENSES/CERN-OHL-S-2.0.txt) |
| Software (`calc/`, `firmware/`) | [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) |
| Documentation (`docs/`, `.md` files) | [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt) |

See [LICENSE](LICENSE). Provided **without any warranty**.

---

**Founder & maintainer:** Tomasz Maciąg · Bydgoszcz, Poland
