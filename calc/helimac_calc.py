#!/usr/bin/env python3
"""
Helimac – wstępny kalkulator osiągów (teoria strumieniowa / momentum theory).

To jest narzędzie do WSTĘPNEGO doboru parametrów (rozmiar wirnika, moc, bateria).
NIE zastępuje analizy BEMT/CFD, prób na stanowisku ani oceny konstruktora.

Użycie:
    python3 calc/helimac_calc.py                 # wariant bazowy
    python3 calc/helimac_calc.py --mtom 300 --d 6.5 --bat-kwh 16
    python3 calc/helimac_calc.py --sweep         # tabela dla różnych średnic wirnika

Licencja: GPL-3.0-or-later
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

G = 9.80665  # m/s^2


def air_density(altitude_m: float = 0.0, temp_offset_c: float = 0.0) -> float:
    """Gęstość powietrza wg atmosfery wzorcowej ISA (troposfera) z odchyłką temperatury."""
    t0 = 288.15
    lapse = 0.0065
    t = t0 - lapse * altitude_m
    p = 101325.0 * (t / t0) ** 5.25588
    return p / (287.053 * (t + temp_offset_c))


@dataclass
class Design:
    mtom_kg: float = 300.0          # masa startowa [kg] – limit Aneksu I dla 1-os. śmigłowca
    rotor_d_m: float = 6.5          # średnica wirnika głównego [m]
    figure_of_merit: float = 0.70   # sprawność aerodynamiczna wirnika w zawisie (0.6–0.78)
    tail_power_frac: float = 0.10   # udział mocy wirnika ogonowego / antymomentu
    drive_eff: float = 0.90         # silnik + sterownik + przekładnia
    battery_kwh: float = 16.0       # energia nominalna pakietu [kWh]
    usable_frac: float = 0.80       # użyteczna część energii (rezerwa + degradacja)
    reserve_min: float = 5.0        # rezerwa lądowania [min]
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
        """Obciążenie powierzchni wirnika [N/m^2]."""
        return self.thrust_n / self.disk_area

    @property
    def induced_velocity(self) -> float:
        """Prędkość indukowana w zawisie [m/s]."""
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
    lines = [
        "=== Helimac – wstępne osiągi w zawisie (teoria strumieniowa) ===",
        f"MTOM                         : {d.mtom_kg:8.1f} kg",
        f"Średnica wirnika             : {d.rotor_d_m:8.2f} m  (pow. {d.disk_area:.1f} m²)",
        f"Gęstość powietrza            : {d.rho:8.4f} kg/m³ (wys. {d.altitude_m:.0f} m, ΔT {d.temp_offset_c:+.0f} °C)",
        f"Obciążenie pow. wirnika      : {d.disk_loading:8.1f} N/m²",
        f"Prędkość indukowana          : {d.induced_velocity:8.2f} m/s",
        f"Moc idealna                  : {d.ideal_power_w/1000:8.1f} kW",
        f"Moc wirnika (FM={d.figure_of_merit:.2f})        : {d.rotor_power_w/1000:8.1f} kW",
        f"Moc na wale (+ogon {d.tail_power_frac:.0%})      : {d.hover_shaft_power_w/1000:8.1f} kW",
        f"Moc elektryczna (η={d.drive_eff:.2f})     : {d.hover_electric_power_w/1000:8.1f} kW",
        f"Bateria                      : {d.battery_kwh:8.1f} kWh (użyteczne {d.usable_frac:.0%})",
        f"Czas zawisu (cała en. użyt.) : {d.hover_endurance_min:8.1f} min",
        f"Czas zawisu minus rezerwa    : {d.endurance_minus_reserve_min:8.1f} min (rezerwa {d.reserve_min:.0f} min)",
        "",
        "UWAGA: wynik orientacyjny. Lot postępowy przy ~60–80 km/h zwykle wymaga",
        "mniej mocy niż zawis; manewry, wiatr i wysoka temperatura – więcej.",
    ]
    return "\n".join(lines)


def sweep(base: Design) -> str:
    rows = ["  D [m] | obc. [N/m²] | P_el [kW] | zawis [min]", "-" * 50]
    for d_m in [5.5, 6.0, 6.5, 7.0, 7.5]:
        d = Design(**{**base.__dict__, "rotor_d_m": d_m})
        rows.append(
            f"  {d_m:5.1f} | {d.disk_loading:11.1f} | {d.hover_electric_power_w/1000:9.1f} | {d.hover_endurance_min:11.1f}"
        )
    return "\n".join(rows)


def main() -> None:
    p = argparse.ArgumentParser(description="Helimac – kalkulator osiągów w zawisie")
    p.add_argument("--mtom", type=float, default=300.0, help="masa startowa [kg]")
    p.add_argument("--d", type=float, default=6.5, help="średnica wirnika [m]")
    p.add_argument("--fm", type=float, default=0.70, help="figure of merit")
    p.add_argument("--bat-kwh", type=float, default=16.0, help="energia baterii [kWh]")
    p.add_argument("--alt", type=float, default=0.0, help="wysokość gęstościowa [m]")
    p.add_argument("--dt", type=float, default=0.0, help="odchyłka temp. od ISA [°C]")
    p.add_argument("--sweep", action="store_true", help="tabela dla różnych średnic")
    a = p.parse_args()

    d = Design(mtom_kg=a.mtom, rotor_d_m=a.d, figure_of_merit=a.fm,
               battery_kwh=a.bat_kwh, altitude_m=a.alt, temp_offset_c=a.dt)
    print(report(d))
    if a.sweep:
        print()
        print(sweep(d))


if __name__ == "__main__":
    main()
