# HELIMAC — production files (rev J2)

Polska wersja: [README.pl.md](README.pl.md)

Everything needed to manufacture the current design (rev J2, pilot up to 110 kg, MTOW 225 kg): drawings, DXF cutting files, STEP models, 3D-print STL files, blade CNC data, and the complete KiCad project of the MC-P inverter with Gerbers, BOM and placement files.

> ⚠️ **Prototype, not an approved aircraft.** All values are calculated, not yet measured. Read [SAFETY.md](../SAFETY.md) before building anything. Build and test in stages: drive on the test bench first (395 N·m / 30 min, then 50 h), then tethered rotor tests, then uncrewed flights. Have drawings and the 400 V electronics reviewed by qualified engineers before you make parts.

## Download

The four ZIP files are complete packages, including the STEP and STL files:

| Package | Contents | File |
|---|---|---|
| **J1 – Drive unit rev J2** | motor, cycloidal transmission 10:1, reversing bevel gearbox, rotor hubs, upper collective, bearings | [HELIMAC_J1_drive_revJ2.zip](downloads/HELIMAC_J1_drive_revJ2.zip) (32 MB) |
| **J2 – Rotor blades rev J** | 4 blades (lower D + mirrored upper G), 3D-printed ASA cores, jigs, CNC sections | [HELIMAC_J2_blades_revJ.zip](downloads/HELIMAC_J2_blades_revJ.zip) (16 MB) |
| **J3 – Frame, seat, air-guide ring, lower collective rev J2** | frame, seat with harness points, PK ring segments, lower collective | [HELIMAC_J3_frame_seat_revJ2.zip](downloads/HELIMAC_J3_frame_seat_revJ2.zip) (0.6 MB) |
| **MC-P – 3-phase SiC inverter rev D1** | KiCad 7 project, Gerbers, BOM, CPL, schematic, mechanical drawing, STEP | [HELIMAC_MC-P_inverter_revD1.zip](downloads/HELIMAC_MC-P_inverter_revD1.zip) (2.6 MB) |

To download a ZIP, open its link and click **Download raw file** (↓). To get the whole repository, use **Code → Download ZIP** on the main page.

The drawings, DXF, Gerber and KiCad files are also in the folders below, so you can browse them on GitHub. Each STEP and STL set is only in its ZIP; the drive assembly STEP alone is 107 MB.

Documentation language: Polish (drawings, notes, file names). Part numbers are consistent across all packages: K = column, P = cycloidal transmission, N = reversing gearbox / upper hub, S = motor, C = collective, R = frame/seat, PK = air-guide ring, L/W/J = blade segments, blade drawings, jigs.

## Mechanical — [mechanical/](mechanical/)

### J1 – Drive unit rev J2 — [J1-drive-revJ2/](mechanical/J1-drive-revJ2/)
- `drawings/ZS-00_zlozeniowy_revJ.pdf` — general assembly with full parts list (materials, quantities, standard parts, bearings).
- `drawings/Helimac_revJ_rysunki_czesci.pdf` — part drawings: dimensions, tolerances, heat treatment, surface finish.
- `drawings/MT_rysunki_montazowe_revJ.pdf` — assembly sequence drawings (motor, transmission, hubs, column, frame interface).
- `drawings/ECN-J01…`, `ECN-J03…` — change notes rev H → J → J2 (110 kg pilot, bearings).
- `dxf/` — 2D cutting files with material and quantity in the file name: motor laminations S01/S02 (NO20 0.20 mm, 280 + 280 pcs; order 285 + 285), cycloidal cams P01 (100Cr6), plates and rings (Al 7075-T651), shims (CuSn8), coupling insert P11.
- ZIP only: `step/` — 41 part models and the complete drive assembly `ZESPOL_Helimac_naped_revJ.step`.

### J2 – Rotor blades rev J — [J2-blades-revJ/](mechanical/J2-blades-revJ/)
- `00_SPIS_ZESTAWU_LOPATY_Helimac_revJ.pdf` — package index; `Helimac_WL-01_lopaty_dokumentacja_revJ.pdf` — manufacturing process: cores, carbon layup, balancing, root, inspection.
- `01_RYSUNKI/` — blade drawings W-00…W-05, lower (D) and upper (G, mirrored).
- `03_DANE_CNC/` — outer section coordinates (CSV) for D and G, clamping plate W-07 (DXF).
- `04_ANALIZA/` — DY-02 coaxial rotor analysis (performance, loads, vibration, Campbell diagram).
- `05_INTERFEJS_PIASTY/` — hub interface drawings (P07, N05, C03, C04).
- ZIP only: `02_STL_DO_DRUKU/` — ASA core segments L00–L09, lay-up beds J1, angle gauges J2, root drilling jig J3, for D and G.

### J3 – Frame, seat, PK ring, lower collective rev J2 — [J3-frame-seat-revJ2/](mechanical/J3-frame-seat-revJ2/)
- `01_RYSUNKI/Helimac_R_rysunki_rama_kolektyw_revJ.pdf` — frame, seat, lower collective drawings.
- ECN-J02, ECN-J03 — change notes.
- ZIP only: `02_STEP/` (frame and seat assemblies, parts, servo, inverter envelope), `03_STL_PK_DO_DRUKU/` (air-guide ring in 6 printable segments).
- ⚠️ **The frame layout may change.** A new layout (hang-glider style front triangle and a single rear leg) is being calculated. Do not make frame tubes yet; the seat and collective parts are not affected.

## Electronics — [electronics/](electronics/)

### MC-P – 3-phase SiC inverter rev D1 — [MC-P-inverter-revD1/](electronics/MC-P-inverter-revD1/)
400 V DC, 6 × SiC MOSFET C3M0016120K (1200 V, 16 mΩ), isolated gate drivers with DESAT short-circuit protection. Board: 215 × 116 mm, 4 layers, 2 oz copper.
- `kicad/` — KiCad 7 project (`MC-P.kicad_pro`, schematic, routed PCB, design rules with 400 V clearances, custom footprints in `lib/`).
- `fabrication/` — Gerbers and drill files (`gerber/` and ZIP), BOM and pick-and-place files (`*_BOM_*.csv`, `*_CPL_*.csv`, LCSC part numbers), fabrication and assembly notes `CZYTAJ_produkcja_i_montaz_revD1.txt`.
- `docs/` — schematic PDF, mechanical drawing (heatsink, clips, mounting), copper layer prints, 3D model `MC-P.step`, renders, DRC report, heatsink calculation.
- Fabrication: 4 layers, 1.6 mm, FR-4 TG155+, 2 oz outer and inner copper, ENIG, electrical test. Through-hole SiC transistors go on the bottom side, metal tab down onto the heatsink (AlN/Al₂O₃ pad + paste, spring clip). Film capacitors C61–C64 and M5 terminals are fitted by hand.
- Before powering: 1.5 kV DC hipot (400 V side vs. low-voltage side and heatsink, < 1 mA), first power-up from a current-limited supply.
- The control board MC-C is still in design ([../electronics/mc-c-controller/](../electronics/mc-c-controller/)).

## Open items (not yet in these files)
- New frame layout (see J3).
- Collective on the lower rotor: being decided whether it keeps variable pitch (currently 3 servos) — affects the lower collective parts in J3.
- MC-C control board, battery pack and BMS.
- Onshape source models will be linked when published.

## Licence
Hardware: CERN-OHL-S-2.0 · Documentation: CC-BY-SA-4.0 · © Tomasz Maciąg and HELIMAC contributors. The HELIMAC name and logo are not covered by these licences ([branding/](../branding/)).

Questions and corrections: [Issues](https://github.com/mactom75/helimac/issues) / [Discussions](https://github.com/mactom75/helimac/discussions).
