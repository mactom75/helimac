import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from helimac_calc import Design, air_density  # noqa: E402


def test_isa_sea_level_density():
    assert math.isclose(air_density(0), 1.225, rel_tol=2e-3)


def test_density_drops_with_altitude():
    assert air_density(1000) < air_density(0)


def test_ideal_power_matches_formula():
    d = Design(mtom_kg=300, rotor_d_m=6.5)
    expected = d.thrust_n ** 1.5 / math.sqrt(2 * d.rho * d.disk_area)
    assert math.isclose(d.ideal_power_w, expected, rel_tol=1e-9)


def test_bigger_rotor_needs_less_power():
    assert Design(rotor_d_m=7.0).hover_electric_power_w < Design(rotor_d_m=6.0).hover_electric_power_w


def test_endurance_scales_with_battery():
    a, b = Design(battery_kwh=10), Design(battery_kwh=20)
    assert math.isclose(b.hover_endurance_min, 2 * a.hover_endurance_min, rel_tol=1e-9)


def test_rev_j2_rotor_power_matches_design_doc():
    # rev J2 design document: hover rotor power 20.7 kW at 225.2 kg, D 4.5 m, FM 0.805
    d = Design()
    assert math.isclose(d.rotor_power_w / 1000, 20.7, abs_tol=0.3)
