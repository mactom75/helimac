"""HELIMAC rev K – etap 2: wymiarowanie zespołów (pasy, koła, wały, kolumna, łożyska, łopata, piasta, rama,
sterowanie, akumulator, masa i środek ciężkości). Wyniki -> stage2.json"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
import numpy as np, json, rotor as RT, blade_mass as BM

G = 9.81
OUT = {}
# ---------------- punkt pracy (z etapu 1, akumulator 40 kg, D16) -----------------
F1 = json.load(open(os.path.join(RES, 'variants.json')))['pasowa']
MTOW = F1['MTOW']; W = MTOW * G
Q_h = F1['Q']                     # N·m – wirnik, zawis
P_h = F1['Ph']; P_max = F1['P13']  # zawis; 1,3 g gorący dzień
RPM = 500.0; Om = RPM * np.pi / 30
Q_max = P_max / 2 / Om            # N·m na wirnik – szczyt
Q_cont = 1.25 * Q_h
OUT['punkt_pracy'] = dict(MTOW=MTOW, Q_h=Q_h, Q_cont=Q_cont, Q_max=Q_max, P_h=P_h, P_max=P_max)

# ---------------- silnik (przekrój EM rev J2, pakiet 48 mm, 7 zwojów, MES 23.11) ----------------
N_TOT = 12.0; RPM_M = RPM * N_TOT; om_m = RPM_M * np.pi / 30
ETA_BELT = 0.97
Tm_h = 2 * Q_h / N_TOT / ETA_BELT; Tm_max = 2 * Q_max / N_TOT / ETA_BELT
KT = 29.78 / 55 * 0.96            # N·m/A (MES 2D × 0,96 efekty czołowe)
OUT['silnik'] = dict(rpm=RPM_M, pakiet_mm=48, zwoje=7, Tm_h=Tm_h, Tm_max=Tm_max, I_h=Tm_h / KT, I_max=Tm_max / KT,
                     SEM_LL=195.4 * 0.97, P_h_wal=Tm_h * om_m, KT=KT, T85_MES=45.19 * 0.96)

# ---------------- przekładnia pasowa ------------------------------------------------
PITCH = 8.0e-3
def dp(z): return z * PITCH / np.pi
st1 = dict(z1=30, z2=90, b=21); st2 = dict(z1=30, z2=120, b=36)
i1 = st1['z2'] / st1['z1']; i2 = st2['z2'] / st2['z1']
n_int = RPM_M / i1
res = {}
for name, st, T, n in (('stopien1', st1, Tm_max, RPM_M), ('stopien2', st2, Q_max / i2 / 0.985, n_int)):
    d1 = dp(st['z1']); Te = 2 * T / d1; v = np.pi * d1 * n / 60
    Ft = Te * 1.4   # siła na wał ≈ 1,4 Te (naciąg wstępny wg zaleceń dla pasów zębatych)
    res[name] = dict(z1=st['z1'], z2=st['z2'], d1=d1 * 1e3, d2=dp(st['z2']) * 1e3, b=st['b'], Te_max=Te, v=v,
                     P_max=T * n * np.pi / 30 / 1e3, F_wal=Ft)
res['przelozenie'] = i1 * i2
# para kół nawrotnych 1:1 na wałkach pośrednich – przenosi moment wirnika górnego / i2
Tg = Q_max / i2 / 0.985
m_g = 2.0; z_g = 50; b_g = 20e-3; d_g = m_g * z_g * 1e-3
Ft_g = 2 * Tg / d_g
Y = 0.41; Kv = 1.25
sig_b = Ft_g * Kv / (b_g * m_g * 1e-3 * Y)
# Hertz (stal 18CrNiMo7-6 nawęglana, 20°)
E = 210e9; nu = 0.3; alpha = np.radians(20)
r1 = d_g / 2 * np.sin(alpha); rho_eq = r1 / 2
sig_H = np.sqrt(Ft_g / (b_g * np.cos(alpha)) * 1 / rho_eq * E / (2 * np.pi * (1 - nu ** 2)))
res['kola_nawrotne'] = dict(m=m_g, z=z_g, d=d_g * 1e3, b=b_g * 1e3, T=Tg, Ft=Ft_g, sigma_F=sig_b / 1e6, sigma_H=sig_H / 1e6,
                            dop_F=500, dop_H=1450, n=n_int, v=np.pi * d_g * n_int / 60)
OUT['przekladnia'] = res

# ---------------- kolumna i wały --------------------------------------------------
# moment piasty sztywnej: przesunięcie środka ciężkości (balans ciała) ±0,12 m × ciężar + podmuch/manewr 1,5
M_hub = 1.5 * (0.12 * W) / 2 + 0.0      # na każdy wirnik (dzielą się po połowie)
# kolumna nieruchoma Al 7075-T6 (Ø70×4): zginanie od obu piast + ciąg, obrót łożyskami
def tube(D, t):
    d = D - 2 * t; I = np.pi * (D ** 4 - d ** 4) / 64; A = np.pi * (D ** 2 - d ** 2) / 4
    return A, I, I / (D / 2), 2 * I
Dc, tc = 0.070, 0.004
A, I, Wb, Jp = tube(Dc, tc)
M_col = 2 * M_hub + 0.0          # u podstawy (oba momenty sumują się przy przesunięciu ŚC)
sig_col = (M_col * 1.5) / Wb + 1.5 * W / A   # obciążenie niszczące 1,5
L_col = 0.62
OUT['kolumna'] = dict(D=Dc * 1e3, t=tc * 1e3, M_hub=M_hub, M_base=M_col, sigma_niszcz=sig_col / 1e6, Rp02=480,
                      zapas=480e6 / sig_col, masa=A * L_col * 2810)
# wał napędowy wirnika górnego wewnątrz kolumny (tylko moment): Ti-6Al-4V lub stal 42CrMo4 Ø50×2
Dt, tt = 0.052, 0.002
A2, I2, W2, Jp2 = tube(Dt, tt)
tau = 1.5 * Q_max * (Dt / 2) / Jp2
OUT['wal_gorny'] = dict(D=Dt * 1e3, t=tt * 1e3, material='Al 7075-T6', tau_niszcz=tau / 1e6, dop=290, zapas=290e6 / tau,
                        masa=A2 * 0.80 * 2810)
# tuleja wirnika dolnego (obraca się na kolumnie) – moment + mocowanie koła pasowego
OUT['tuleja_dolna'] = dict(D=90, t=2.5, masa=tube(0.090, 0.0025)[0] * 0.20 * 2810)

# łożyska: piasta górna i dolna – po 2 łożyska skośne na kolumnie (obciążenie: ciąg + moment piasty)
def L10_ball(C, P, n): return (C / P) ** 3 * 1e6 / (60 * n)
Tu = 0.61 * W; Tl = 0.39 * W
a_b = 0.060   # rozstaw łożysk piasty [m]
for nm, T, D in (('piasta_gorna', Tu, '7014 (70×110×20), para O'), ('piasta_dolna', Tl, '61814 + 7014 (70×110×20)')):
    Fr = M_hub / a_b; Fa = T
    P = 0.57 * Fr + 0.93 * Fa if Fa / max(Fr, 1) > 1.14 else Fr + 0.55 * Fa
    OUT[nm] = dict(lozyska=D, Fr=Fr, Fa=Fa, P=P, C=48.8e3, L10h=L10_ball(48.8e3, P, RPM), uwaga='obrót względny piast 2×500 obr/min dla górnej względem tulei' )

# ---------------- łopata: drgania i stateczność (przybliżenie belki wirującej) -------------
b = RT.Blade(R=2.25, r0=0.30, c_root=0.17, c_tip=0.115, r_taper=1.0, twist=-12.0)
blade = BM.blade(2.25, 0.30, b.chord, Om, (0.61 * W) / 2, F1['J'] / 4)
# sztywność zginania: pasy dźwigara (E_UD 125 GPa) + pokrycie ±45 (E 15 GPa w kierunku rozpiętości)
r = np.linspace(0.30, 2.25, 80); c = b.chord(r)
A_sp_root = blade['A_sp_root'] * 1e-6
A_sp = np.maximum(A_sp_root * ((2.25 - r) / 1.95) ** 1.5, 40e-6)
h = 0.12 * c * 0.8
EI_f = 125e9 * 2 * (A_sp / 2) * (h / 2) ** 2 + 15e9 * 0.0006 * 2.04 * c * (0.12 * c / 2) ** 2 * 0.5
EI_l = 125e9 * A_sp * (0.12 * c) ** 2 * 0.2 + 15e9 * 0.0006 * 2 * c * (0.35 * c) ** 2
GJ = 4 * (0.6 * c * 0.10 * c) ** 2 * 5e9 * 0.0006 / (1.3 * c)       # przekrój zamknięty dźwigara D (Bredt)
lam = np.array([BM.section(ci, ai)[0] for ci, ai in zip(c, A_sp)])
def rayleigh(EI, lam, r, Om, m_tip, r_tip, kind):
    # funkcja kształtu: wspornik (1. postać), Rayleigh z odśrodkowym usztywnieniem
    x = (r - r[0]) / (r[-1] - r[0]); L = r[-1] - r[0]
    phi = 1 - np.cos(np.pi * x / 2); dphi = np.pi / (2 * L) * np.sin(np.pi * x / 2); d2 = (np.pi / (2 * L)) ** 2 * np.cos(np.pi * x / 2)
    dr = r[1] - r[0]
    U_el = np.sum(EI * d2 ** 2) * dr
    CF = np.array([np.sum((lam * r)[i:]) * dr for i in range(len(r))]) * Om ** 2 + m_tip * r_tip * Om ** 2
    U_cf = np.sum(CF * dphi ** 2) * dr
    if kind == 'lag': U_cf -= Om ** 2 * (np.sum(lam * phi ** 2) * dr + m_tip)   # efekt „propelerowy” dla ruchu w płaszczyźnie
    T = np.sum(lam * phi ** 2) * dr + m_tip * 1.0
    w = np.sqrt(max(U_el + U_cf, 1e-6) / T)
    w0 = np.sqrt(U_el / T)
    return w / Om, w0 / (2 * np.pi)
nf, f0f = rayleigh(EI_f, lam, r, Om, blade['m_tip'], 2.15, 'flap')
nl, f0l = rayleigh(EI_l, lam, r, Om, blade['m_tip'], 2.15, 'lag')
# skręcanie: wspornik + moment propelerowy
I_th = np.sum(lam * (0.07 * c) ** 2 + lam * 0.0) * (r[1] - r[0]) * 1.0 + blade['m_tip'] * (0.02) ** 2
k_th = np.pi ** 2 / 4 * np.mean(GJ) / 1.95
nt = np.sqrt(k_th / I_th + Om ** 2) / Om
OUT['lopata'] = dict(masa=blade['m'], m_rozklad=blade['m_dist'], m_konc=blade['m_tip'], J=blade['J'], CF=blade['CF'],
                     A_dzwigar_nasada_mm2=blade['A_sp_root'], M_nasada=blade['M_root'], nu_mach=nf, nu_wplaszcz=nl, nu_skret=nt,
                     f0_mach=f0f, f0_wplaszcz=f0l, srodek_ciezk='≤ 25 % cięciwy (obciążnik w nosku, masa końcówki w nosku 10–15 %)',
                     precone=np.degrees(((0.61 * W) / 2 * 0.72 * 2.25) / (Om ** 2 * blade['J'])))
# naprężenie nasady (pasy UD): siła odśrodkowa + zginanie od zmiany ciągu
sig_root = blade['CF'] / A_sp_root + blade['M_root'] / (0.12 * 0.17 * 0.8) / (A_sp_root / 2)
OUT['lopata']['sigma_nasada_MPa'] = sig_root / 1e6
OUT['lopata']['dop_UD_MPa'] = 600
# okucie nasady: Al 7075, 2 sworznie Ø12 (ścinanie dwucięte) – CF × 1,5 × 1,5
F_ult = blade['CF'] * 1.5 * 1.5
tau_pin = F_ult / (2 * 2 * np.pi * 0.006 ** 2)
OUT['okucie'] = dict(F_niszcz=F_ult, tau_sworzen_MPa=tau_pin / 1e6, dop_MPa=0.6 * 1000, sworznie='2 × Ø12 h7, 42CrMo4 QT 1000 MPa')

# łożysko skoku (w uchwycie łopaty): siła odśrodkowa -> łożysko oporowe + 2 igiełkowe
OUT['lozysko_skoku'] = dict(Fa=blade['CF'], typ='oporowe kulkowe 51107 (C0 = 50 kN) + 2 × HK3020', C0=50e3, zapas_stat=50e3 / blade['CF'])

# ---------------- sterowanie: moment na osi skoku -------------------------------------
# moment propelerowy + aerodynamiczny (Cm) + tarcie łożyska oporowego
I_xx = np.sum(lam * (0.08 * c) ** 2) * (r[1] - r[0]) + blade['m_tip'] * 0.015 ** 2
M_prop = Om ** 2 * I_xx * np.sin(2 * np.radians(10)) / 2
M_fric = 0.004 * blade['CF'] * 0.030 / 2
M_aero = 0.5 * 1.225 * (0.75 * Om * 2.25) ** 2 * 0.15 ** 2 * 0.010 * 1.95   # Cm ≈ −0,010 (NACA 23012)
M_bl = M_prop + M_fric + M_aero
lever = 0.060
F_link = 2 * M_bl / lever      # 2 łopaty na wirnik
# siłownik STS3250: 4,9 N·m przy ramieniu 25 mm -> 196 N; przełożenie dźwigni 1:1
OUT['sterowanie'] = dict(M_os_skoku=M_bl, M_prop=M_prop, M_tarcie=M_fric, M_aero=M_aero, F_ciegno_wirnik=F_link,
                         silownik='STS3250: 4,9 N·m utyk, 1,57 N·m znam.; ramię 25 mm', F_silownik_znam=1.57 / 0.025,
                         gorny_2szt=2 * 1.57 / 0.025, dolny_3szt=3 * 1.57 / 0.025)

# ---------------- akumulator --------------------------------------------------------
cell = dict(nazwa='Molicel P50B 21700', Ah=5.0, V=3.6, m=0.070, I_cont=60)
S_, P_ = 112, 4
m_cells = S_ * P_ * cell['m']; E_cells = S_ * P_ * cell['Ah'] * cell['V'] / 1e3
OUT['akumulator'] = dict(uklad=f'{S_}S{P_}P', ogniwa=S_ * P_, m_ogniw=m_cells, E_kWh=E_cells, U_nom=S_ * 3.6, U_min=S_ * 3.0, U_max=S_ * 4.2,
                         m_pakietu=40.0, Wh_kg=E_cells * 1e3 / 40.0, I_h=P_h / 0.894 / (S_ * 3.6), I_max=P_max / 0.894 / (S_ * 3.4),
                         I_ogniwa_max=P_max / 0.894 / (S_ * 3.4) / P_, uwaga='2 pakiety po 56S4P (A i B) w szeregu, BMS w każdym, bezpiecznik 150 A')

# ---------------- rama: 3 rury Al 7075-T6 ------------------------------------------------
# węzeł górny (płyta napędu) na wys. 2,05 m nad ziemią w osi wirnika (x=0, y=0)
apex = np.array([0.0, 0.0, 2.05])
fl = np.array([1.20, 0.70, 0.0]); fr = np.array([1.20, -0.70, 0.0]); rr = np.array([-0.75, 0.0, 0.0])
legs = dict(przod_L=(fl, 0.040, 0.0015), przod_P=(fr, 0.040, 0.0015), tyl=(rr, 0.050, 0.0020))
# obciążenie lądowania 3 g (masa bez pilota zawieszona na węźle + pilot na siodełku przy nodze tylnej)
m_top = 30.0           # napęd + wirniki + kolumna (na węźle)
F_v = 3.0 * MTOW * G
# rozkład reakcji: statyka 3 podpór (punkt środka ciężkości ~ x=0,0)
Pts = np.array([fl[:2], fr[:2], rr[:2]])
Aeq = np.vstack([np.ones(3), Pts[:, 0], Pts[:, 1]])
Rz = np.linalg.solve(Aeq, [F_v, 0.0, 0.0])
frame = {}
m_frame = 0
for (nm, (p, D, t)), Rzi in zip(legs.items(), Rz):
    Lg = np.linalg.norm(apex - p); u = (apex - p) / Lg
    N = Rzi / u[2]
    A, I, Wb, _ = tube(D, t)
    K = 1.0
    Pcr = np.pi ** 2 * 71.7e9 * I / (K * Lg) ** 2
    m = A * Lg * 2810 * (1.12 if nm == 'tyl' else 1.0)
    m_frame += m
    frame[nm] = dict(L=Lg, D=D * 1e3, t=t * 1e3, N_3g=N, P_kr=Pcr, zapas_wyboczenie=Pcr / N, sigma=N / A / 1e6, masa=m)
# noga tylna: zginanie od siodełka (pilot 110 kg × 3 g, ramię 0,18 m od osi rury) + wygięcie (strzałka 0,10 m) × N
A, I, Wb, _ = tube(0.050, 0.002)
M_seat = 3 * 110 * G * 0.18
M_bow = frame['tyl']['N_3g'] * 0.10
frame['tyl']['M_zginanie'] = M_seat + M_bow
frame['tyl']['sigma_zg'] = (M_seat + M_bow) / Wb / 1e6
frame['tyl']['zapas_Rp'] = 480 / (frame['tyl']['sigma_zg'] + frame['tyl']['sigma'])
frame["wezly_stopy"] = 1.4; frame["tuleja_wzmacniajaca_siodelko"] = 0.2
frame['masa_rur'] = m_frame
frame["masa_razem"] = m_frame + 1.6
OUT['rama'] = frame

json.dump(OUT, open(os.path.join(RES, 'stage2.json'), 'w'), indent=1, default=float, ensure_ascii=False)
def pr(d, ind=0):
    for k, v in d.items():
        if isinstance(v, dict): print(' ' * ind + k); pr(v, ind + 2)
        else: print(' ' * ind + f'{k}: {round(v, 3) if isinstance(v, (int, float, np.floating)) else v}')
pr(OUT)
