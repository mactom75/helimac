# Contributing to HELIMAC

Thank you for your interest! Every contribution counts — from fixing a typo to designing the transmission.
*Po polsku też możesz pisać — Polish is welcome everywhere in the project.*

## Where to post

- **Question, idea, open discussion** → [Discussions](../../discussions)
- **Specific task, error, change proposal** → [Issues](../../issues) (choose a template)
- **Ready changes to files** → Pull Request

## Project files

- **CAD:** the project is designed in **Onshape**. Each assembly README links to its public Onshape document; the repository holds exports: `.step` (3D) and `.pdf` drawings, plus `.dxf` where needed for cutting. Contributions from other CAD tools are welcome as `.step` + `.pdf`.
- **Electronics:** designed in **KiCad** — include the KiCad project, Gerbers, BOM, pick-and-place and a PDF of the schematic.
- **Calculations:** Python in `calc/` (with a test), or a spreadsheet plus a PDF describing the assumptions.
- **Units:** SI (metres, kilograms, newtons, watts).
- **Large files** (> 50 MB, videos, scans) — attach them to a Release.
- Each subfolder in `hardware/` and `electronics/` has a `README.md` — update the file list and status there.

## Pull Request steps

1. Fork and create a branch, e.g. `frame/motor-mount`.
2. Describe the change (the template helps). Add a [BUILD_LOG.md](BUILD_LOG.md) entry for notable progress.
3. Changes affecting flight safety need review by at least one person with relevant expertise.

## Licensing of contributions

By contributing you agree to release your contribution under the project licences (see [LICENSE](LICENSE)).

## Conduct

The [Code of Conduct](CODE_OF_CONDUCT.md) applies.
