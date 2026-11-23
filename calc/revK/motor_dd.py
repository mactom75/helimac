"""HELIMAC rev K – wymiarowanie silnika z wirnikiem zewnętrznym, napęd bezpośredni (500 obr/min).
Model analityczny: obwód magnetyczny (Carter), uzwojenie skupione, straty Cu i Fe, masa, ciepło.
Wynik do sprawdzenia MES w etapie 2."""
import numpy as np

MU0 = 4e-7 * np.pi
RHO_CU = 8900; RHO_FE = 7650; RHO_PM = 7500; RHO_AL = 2700
RES_CU100 = 2.25e-8          # Ω·m przy ~100 °C


def kw_conc(Q, p):
    """współczynnik uzwojenia (skupione, dwuwarstwowe) dla harmonicznej roboczej p."""
    # rozkład gwiazdy żłobkowej: q = Q/(3*2p)
    al = 2 * np.pi * p / Q                       # kąt elektryczny między żłobkami
    kp = abs(np.sin(al / 2))                     # skrót (cewka na 1 ząb: rozpiętość = 1 żłobek)
    # współczynnik strefowy przez sumę fazorów cewek jednej fazy (algorytm gwiazdy)
    ang = (np.arange(Q) * al) % (2 * np.pi)
    # przypisanie do faz: strefy 60° (A, -C, B, -A, C, -B)
    zone = (np.floor(ang / (np.pi / 3))).astype(int) % 6
    phA = np.where(zone == 0, 1, np.where(zone == 3, -1, 0))
    v = np.sum(phA * np.exp(1j * ang)) / np.sum(np.abs(phA))
    return kp * abs(v)


def design(D=0.40, L=0.030, Q=48, p=22, hm=4.0e-3, g=1.0e-3, Br=1.22, A_rms=28e3, J=5.0e6,
           Bt=1.55, By=1.40, kf=0.42, rpm=500, alpha=0.83, T_req=None):
    """D – średnica szczeliny (zewn. stojana) [m]; zwraca słownik parametrów."""
    kw = kw_conc(Q, p)
    tau_s = np.pi * D / Q; tau_p = np.pi * D / (2 * p)
    bo = 2.5e-3                                   # otwarcie żłobka
    kc = tau_s / (tau_s - (bo ** 2 / (5 * g + bo)) )  # Carter
    mur = 1.05
    Bg = 0.95 * Br * hm / (hm + mur * g * kc)    # 0,95 – rozproszenie
    B1 = 4 / np.pi * Bg * np.sin(alpha * np.pi / 2)
    sigma = B1 * A_rms * kw / np.sqrt(2)          # Pa – naprężenie styczne
    T = sigma * np.pi * D * L * D / 2
    # stojan (wewnątrz)
    bt = Bg * tau_s / Bt
    ws = tau_s - bt
    hs = A_rms * np.pi * D / (Q * ws * kf * J)    # głębokość żłobka (prostokąt – przybliżenie)
    phi_p = Bg * alpha * tau_p * L
    hys = phi_p / (2 * By * L)
    hyr = phi_p / (2 * 1.5 * L)
    Ds_in = D - 2 * (hs + 1.0e-3) - 2 * hys        # 1 mm stopka zęba
    # masy
    m_teeth = RHO_FE * L * Q * bt * (hs + 1e-3)
    m_ys = RHO_FE * L * np.pi * (Ds_in + hys) * hys
    m_fe_st = m_teeth + m_ys
    Dr = D + 2 * g
    m_pm = RHO_PM * L * np.pi * (Dr + hm) * hm * alpha
    m_yr = RHO_FE * L * np.pi * (Dr + 2 * hm + hyr) * hyr
    MLT = 2 * L + 2.4 * (bt + ws / 2) * 1.0 + 2 * 0.004   # średnia długość zwoju
    V_cu = Q * ws * hs * kf * MLT / 2
    m_cu = RHO_CU * V_cu
    # konstrukcja: tarcza wirnika (Al, otwarta – szprychy) + piasta stojana (Al) + łożyska
    m_rot_struct = RHO_AL * (np.pi * (Dr / 2) ** 2 * 0.0025 * 0.45 + np.pi * Dr * 0.004 * 0.012)
    m_st_struct = RHO_AL * np.pi * ((Ds_in / 2) ** 2 - 0.035 ** 2) * 0.006 * 0.40 + 0.25
    m_bear = 0.0                                   # łożyska liczone z piastą wirnika
    m_tot = m_fe_st + m_pm + m_yr + m_cu + m_rot_struct + m_st_struct
    # straty
    P_cu = RES_CU100 * J ** 2 * V_cu
    f = p * rpm / 60
    pfe = lambda B: 0.016 * f * B ** 2 + 3.5e-5 * f ** 2 * B ** 2   # NO20 [W/kg]
    P_fe = 1.3 * (m_teeth * pfe(Bt) + m_ys * pfe(By))                # 1,3 – obróbka, harmoniczne
    P_out = T * rpm * np.pi / 30
    eta = P_out / (P_out + P_cu + P_fe + 0.004 * P_out)               # +0,4 % mech./magnesy
    # chłodzenie: strumień ciepła przez powierzchnię wewnętrzną stojana + czoła uzwojeń (przepływ z wirnika)
    A_cool = np.pi * Ds_in * L * 1.0 + 2 * np.pi * D * (hs + hys) * 0.8
    q = (P_cu + P_fe) / A_cool
    return dict(D=D, L=L, Q=Q, p=p, kw=kw, Bg=Bg, B1=B1, sigma=sigma, T=T, hs=hs, bt=bt, ws=ws, hys=hys, hyr=hyr,
                Ds_in=Ds_in, m_fe=m_fe_st, m_pm=m_pm, m_yr=m_yr, m_cu=m_cu, m_struct=m_rot_struct + m_st_struct,
                m=m_tot, P_cu=P_cu, P_fe=P_fe, eta=eta, f=f, q=q, A_cool=A_cool, Dout=Dr + 2 * hm + 2 * hyr)


def size_for(T_req, D, **kw):
    """długość pakietu dla wymaganego momentu (ciągłego)."""
    d1 = design(D=D, L=0.01, **kw)
    L = T_req / d1["T"] * 0.01
    return design(D=D, L=L, **kw)
