"""HELIMAC rev K – masa łopaty z budowy przekroju (kompozyt: rdzeń z pianki PMI, dźwigar D z UD węgla,
pokrycie ±45° węgiel, obciążnik noska do środka ciężkości 25 % cięciwy, końcówka – masa bezwładnościowa)."""
import numpy as np

RHO_UD, RHO_FOAM, RHO_BAL = 1550, 52, 11300     # UD CFRP, Rohacell 51, ołów/wolfram (ołów)
SKIN_AREAL = 0.60                               # kg/m2 – 2 warstwy ±45° 200 g/m2 + żywica
ERO = 0.04                                      # kg/m – taśma przeciwerozyjna
SIG_UD = 250e6                                  # Pa – dopuszczalne zmęczeniowo dla UD (z zapasem)


def section(c, A_sp):
    """masa liniowa [kg/m] i położenie środka ciężkości (ułamek cięciwy) przy dźwigarze A_sp [m2]."""
    m_skin = SKIN_AREAL * 2.04 * c; x_skin = 0.42
    m_foam = RHO_FOAM * 0.082 * c ** 2; x_foam = 0.45
    m_sp = RHO_UD * A_sp; x_sp = 0.14
    m_ero = ERO; x_ero = 0.02
    m0 = m_skin + m_foam + m_sp + m_ero
    xc = (m_skin * x_skin + m_foam * x_foam + m_sp * x_sp + m_ero * x_ero) / m0
    # obciążnik w nosku (x = 0,05) dla środka ciężkości na 0,25
    m_bal = max(0.0, m0 * (xc - 0.25) / (0.25 - 0.05))
    return m0 + m_bal, m_bal


def blade(R, r0, chord, Om, T_blade, J_req_blade=0.0, n=60, root_fit=0.35, r_tip_mass=None):
    """zwraca słownik: masa, bezwładność, siła odśrodkowa, masa końcówki."""
    r = np.linspace(r0, R, n); dr = r[1] - r[0]
    c = chord(r)
    # dźwigar: zginanie od zmiany ciągu ±50 % (podmuch, manewr) przy sztywnej piaście + siła odśrodkowa
    M_root = 0.5 * T_blade * 0.70 * (R - r0)
    h = 0.12 * c * 0.80                                    # wysokość efektywna pasów
    F_b = M_root * np.clip((R - r) / (R - r0), 0, 1) ** 2 / h  # siła w pasie
    A_sp = np.maximum(F_b / SIG_UD * 2, 40e-6)               # 2 pasy (górny i dolny)
    lam = np.zeros(n); bal = np.zeros(n)
    for _ in range(3):
        for i in range(n):
            lam[i], bal[i] = section(c[i], A_sp[i])
        CF = Om ** 2 * np.array([np.sum((lam * r)[i:]) * dr for i in range(n)])
        A_sp = np.maximum(A_sp, CF / SIG_UD + F_b / SIG_UD * 2)
    m_dist = np.sum(lam) * dr
    J_dist = np.sum(lam * r ** 2) * dr + root_fit * r0 ** 2
    rt = r_tip_mass or (R - 0.10)
    m_tip = max(0.0, (J_req_blade - J_dist) / rt ** 2)
    m = m_dist + root_fit + m_tip
    J = J_dist + m_tip * rt ** 2
    CF_root = Om ** 2 * (np.sum(lam * r) * dr + m_tip * rt)
    return dict(m=m, m_dist=m_dist, m_tip=m_tip, J=J, CF=CF_root, lam_root=lam[0], lam_tip=lam[-1],
                A_sp_root=A_sp[0] * 1e6, bal=np.sum(bal) * dr, M_root=M_root)
