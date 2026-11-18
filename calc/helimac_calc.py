#!/usr/bin/env python3
"""
HELIMAC – early performance estimator (momentum theory).

For EARLY sizing only (rotor size, power, battery).
It does NOT replace BEMT/CFD analysis, bench tests or engineering judgement.

Usage:
    python3 calc/helimac_calc.py                 # baseline
    python3 calc/helimac_calc.py --mtom 300 --d 6.5 --bat-kwh 16
    python3 calc/helimac_calc.py --sweep         # table for several rotor diameters

Licence: GPL-3.0-or-later
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 9.80665  # m/s^2


def air_density(altitude_m: float = 0.0, temp_offset_c: float = 0.0) -> float:
    """Air density, ISA troposphere, with optional temperature offset."""
    t0 = 288.15
    lapse = 0.0065
    t = t0 - lapse * altitude_m
    p = 101325.0 * (t / t0) ** 5.25588
    return p / (287.053 * (t + temp_offset_c))


@dataclass
class Design:
    mtom_kg: float = 300.0          # take-off mass [kg] – Annex I limit for single-seat helicopter
    rotor_d_m: float = 6.5          # main rotor diameter [m]
    figure_of_merit: float = 0.70   # rotor hover efficiency (0.6–0.78)
    tail_power_frac: float = 0.10   # tail rotor / anti-torque power fraction
    drive_eff: float = 0.90         # motor + controller + gearbox
    battery_kwh: float = 16.0       # nominal pack energy [kWh]
    usable_frac: float = 0.80       # usable fraction (margin + ageing)
    reserve_min: float = 5.0        # landing reserve [min]
    altitude_m: float = 0.0
    temp_offset_c: float = 0.0

    @property
    def disk_area(self) -> float:
        return math.pi * (self.rotor_d_m / 2) ** 2

    @property
    def thrust_n(self) -> float:
        return self.mtom_kg * G

    @property
    def rho(self) -> float:
        return air_density(self.altitude_m, self.temp_offset_c)

    @property
    def disk_loading(self) -> float:
        """Disk loading [N/m^2]."""
        return self.thrust_n / self.disk_area

    @property
    def induced_velocity(self) -> float:
        """Induced velocity in hover [m/s]."""
        return math.sqrt(self.thrust_n / (2 * self.rho * self.disk_area))

    @property
    def ideal_power_w(self) -> float:
        return self.thrust_n * self.induced_velocity

    @property
    def rotor_power_w(self) -> float:
        return self.ideal_power_w / self.figure_of_merit

    @property
    def hover_shaft_power_w(self) -> float:
        return self.rotor_power_w * (1 + self.tail_power_frac)

    @property
    def hover_electric_power_w(self) -> float:
        return self.hover_shaft_power_w / self.drive_eff

    @property
    def hover_endurance_min(self) -> float:
        usable_wh = self.battery_kwh * 1000 * self.usable_frac
        return usable_wh / self.hover_electric_power_w * 60

    @property
    def endurance_minus_reserve_min(self) -> float:
        return max(0.0, self.hover_endurance_min - self.reserve_min)


def report(d: Design) -> str:
    rows = [
        ("MTOM", f"{d.mtom_kg:.1f} kg"),
        ("Rotor diameter", f"{d.rotor_d_m:.2f} m (disk {d.disk_area:.1f} m²)"),
        ("Air density", f"{d.rho:.4f} kg/m³ (alt {d.altitude_m:.0f} m, ΔT {d.temp_offset_c:+.0f} °C)"),
        ("Disk loading", f"{d.disk_loading:.1f} N/m²"),
        ("Induced velocity", f"{d.induced_velocity:.2f} m/s"),
        ("Ideal power", f"{d.ideal_power_w/1000:.1f} kW"),
        (f"Rotor power (FM {d.figure_of_merit:.2f})", f"{d.rotor_power_w/1000:.1f} kW"),
        (f"Shaft power (+tail {d.tail_power_frac:.0%})", f"{d.hover_shaft_power_w/1000:.1f} kW"),
        (f"Electrical power (eff {d.drive_eff:.2f})", f"{d.hover_electric_power_w/1000:.1f} kW"),
        ("Battery", f"{d.battery_kwh:.1f} kWh ({d.usable_frac:.0%} usable)"),
        ("Hover time (all usable)", f"{d.hover_endurance_min:.1f} min"),
        ("Hover time minus reserve", f"{d.endurance_minus_reserve_min:.1f} min (reserve {d.reserve_min:.0f} min)"),
    ]
    lines = ["=== HELIMAC – early hover performance (momentum theory) ==="]
    lines += [f"{k:<30}: {v}" for k, v in rows]
    lines += ["", "NOTE: rough estimate. Forward flight at ~60–80 km/h usually needs",
              "less power than hover; manoeuvres, wind and heat need more."]
    return "\n".join(lines)


def sweep(base: Design) -> str:
    rows = ["  D [m] | DL [N/m²] | P_el [kW] | hover [min]", "-" * 48]
    for d_m in [5.5, 6.0, 6.5, 7.0, 7.5]:
        d = Design(**{**base.__dict__, "rotor_d_m": d_m})
        rows.append(
            f"  {d_m:5.1f} | {d.disk_loading:9.1f} | {d.hover_electric_power_w/1000:9.1f} | {d.hover_endurance_min:11.1f}"
        )
    return "\n".join(rows)


def main() -> None:
    p = argparse.ArgumentParser(description="HELIMAC – hover performance estimator")
    p.add_argument("--mtom", type=float, default=300.0, help="take-off mass [kg]")
    p.add_argument("--d", type=float, default=6.5, help="rotor diameter [m]")
    p.add_argument("--fm", type=float, default=0.70, help="figure of merit")
    p.add_argument("--bat-kwh", type=float, default=16.0, help="battery energy [kWh]")
    p.add_argument("--alt", type=float, default=0.0, help="altitude [m]")
    p.add_argument("--dt", type=float, default=0.0, help="temperature offset from ISA [°C]")
    p.add_argument("--sweep", action="store_true", help="table for several diameters")
    a = p.parse_args()

    d = Design(mtom_kg=a.mtom, rotor_d_m=a.d, figure_of_merit=a.fm,
               battery_kwh=a.bat_kwh, altitude_m=a.alt, temp_offset_c=a.dt)
    print(report(d))
    if a.sweep:
        print()
        print(sweep(d))


if __name__ == "__main__":
    main()
