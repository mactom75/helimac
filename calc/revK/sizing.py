"""HELIMAC rev K – pętla projektowa: masa ↔ moc ↔ wirnik ↔ napęd ↔ akumulator."""
import numpy as np, rotor as RT, blade_mass as BM

G = 9.81
PILOT = 110.0
ETA = dict(motor=0.950, inv=0.980, belt=0.970, wire=0.990)
ETA_CH = np.prod(list(ETA.values()))
P_AUX = 150.0                       # W – MC-C, siłowniki, wentylator falownika, czujniki
E_SPEC = 200.0                      # Wh/kg – pakiet (ogniwa ok. 260 Wh/kg × 0,77)
USABLE = 0.80                       # wykorzystanie energii (lądowanie przy 20 % SoC)
T85 = 0.55                          # s – czas spadku obrotów do 85 % po zaniku mocy (jak rev J2)

FIXED = dict(sterowanie=1.5, falownik=2.0, instalacja_400V=1.5, awionika=1.0, rama=5.5, siedzisko_podnozek=2.5,
             mocowanie_akumulatora=0.8)


def mass_drive(Q_rot_cont, T_mot_cont, CF_kN):
    return dict(silnik=1.5 + 0.17 * T_mot_cont,
                przekladnia_pasowa=2.0 + 0.0075 * 2 * Q_rot_cont,
                piasty=2 * (0.5 + 0.08 * CF_kN),
                walki_kolumna=2.5 + 0.003 * 2 * Q_rot_cont)


def run(R=2.25, rpm=500, c_root=0.18, c_tip=0.12, r_taper=1.0, twist=-12.0, m_bat=35.0, r0=0.30,
        rpm_motor=5000, k_cont=1.25, verbose=False, m_empty0=42.0):
    Om = rpm * np.pi / 30
    b = RT.Blade(R=R, r0=r0, c_root=c_root, c_tip=c_tip, r_taper=r_taper, twist=twist)
    m_empty = m_empty0
    for it in range(8):
        W = (PILOT + m_bat + m_empty) * G
        h = RT.trim(b, b, Om, W)
        Q = h["Qu"]                       # moment jednego wirnika (zawis)
        Ph = h["P"]
        J_req = T85 * Ph / (0.139 * Om ** 2)          # wszystkie 4 łopaty
        bl = BM.blade(R, r0, b.chord, Om, h["Tu"] / 2, J_req / 4)
        Qc = k_cont * Q
        T_mot = 2 * Qc / (rpm_motor / rpm) / ETA["belt"]
        md = mass_drive(Qc, T_mot, bl["CF"] / 1e3)
        masses = dict(lopaty=4 * bl["m"], **md, **FIXED)
        m_new = sum(masses.values())
        if abs(m_new - m_empty) < 0.05: m_empty = m_new; break
        m_empty = m_new
    W = (PILOT + m_bat + m_empty) * G
    # lot postępowy
    V = np.arange(0, 31, 1.0)
    Pff = np.array([RT.ff_power(W, v, Ph, h["P0"], R, Om * R) for v in V])
    i_e = np.argmin(Pff[5:]) + 5
    P_bat_h = Ph / ETA_CH + P_AUX
    P_bat_c = Pff[i_e] / ETA_CH + P_AUX
    E = m_bat * E_SPEC * USABLE * 3600
    t_h = E / P_bat_h / 60
    t_mix = E / (0.3 * P_bat_h + 0.7 * P_bat_c) / 60
    # sprawdzenie zapasu przeciągnięcia: 1,3 g i gorący dzień (35 °C, 500 m n.p.m. – ρ = 1,09)
    hh = RT.trim(b, b, Om, 1.3 * W, rho=1.09)
    out = dict(R=R, rpm=rpm, c_root=c_root, c_tip=c_tip, m_bat=m_bat, m_empty=m_empty, MTOW=W / G, P_h=Ph, FM=h["FM"],
               thu=h["thu"], thl=h["thl"], Q=Q, sigma=b.solidity(), CTs=W / 2 / (RT.RHO0 * np.pi * R ** 2 * (Om * R) ** 2) / b.solidity(),
               cl13hot=hh["clmax"], P13hot=hh["P"], J=4 * bl["J"], m_blade=bl["m"], m_tip=bl["m_tip"], CF=bl["CF"],
               V_e=V[i_e], P_c=Pff[i_e], t_h=t_h, t_mix=t_mix, masses=masses, T_mot=T_mot, Pff=Pff, V=V, bl=bl, hover=h)
    return out
