"""HELIMAC rev K – model wirnika współosiowego (od nowa).
BEM (element łopaty + pęd w pierścieniach), straty końcowe Prandtla,
wirnik dolny w zwężonej strudze górnego (Landgrebe), wpływ dolnego na górny.
Profil: NACA 23012-podobny, Re ~ 1e6, powierzchnia kompozytowa (realistyczne cd0).
"""
import numpy as np

RHO0 = 1.225
G = 9.81

# --- profil -------------------------------------------------------------
A0 = 5.8                      # 1/rad (z poprawką na skończony Re i grubość)
AL0 = np.radians(-1.2)
CLMAX = 1.30
def polar(al):
    cl = A0 * (al - AL0)
    cd = 0.0100 - 0.0035 * cl + 0.0120 * cl ** 2       # cd0 0,0100 – łopata wykonana (nie gładki model)
    # przeciągnięcie: ograniczenie cl, gwałtowny wzrost cd
    st = np.abs(cl) > CLMAX
    cd = np.where(st, cd + 0.6 * (np.abs(cl) - CLMAX), cd)
    cl = np.clip(cl, -CLMAX, CLMAX)
    return cl, cd


class Blade:
    def __init__(s, R=2.25, r0=0.30, c_root=0.18, c_tip=0.12, r_taper=1.0, twist=-12.0, nb=2):
        s.R, s.r0, s.cr, s.ct, s.rt, s.tw, s.nb = R, r0, c_root, c_tip, r_taper, twist, nb

    def chord(s, r):
        r = np.asarray(r, float)
        return np.where(r <= s.rt, s.cr, s.cr + (s.ct - s.cr) * (r - s.rt) / (s.R - s.rt))

    def solidity(s):  # ważona ciągiem (r^2)
        r = np.linspace(s.r0, s.R, 400)
        return s.nb * np.trapezoid(s.chord(r) * r ** 2, r) / (np.pi * s.R * np.trapezoid(r ** 2, r))


def bem(b, th75, Om, rho=RHO0, lam_ext=None, n=150, it=400):
    R = b.R
    r = np.linspace(b.r0 + 0.01, R - 0.002, n); dr = r[1] - r[0]; x = r / R
    c = b.chord(r); sig = b.nb * c / (np.pi * R)
    th = np.radians(th75 + b.tw * (x - 0.75))
    le = np.zeros_like(r) if lam_ext is None else lam_ext(r)
    lam = le + 0.06
    for _ in range(it):
        phi = np.arctan2(lam, x)
        f = b.nb / 2 * (1 - x) / (x * np.maximum(np.sin(phi), 1e-3))
        F = np.maximum(2 / np.pi * np.arccos(np.exp(-np.clip(f, 0, 50))), 0.03)
        cl, cd = polar(th - phi)
        # bilans pędu w pierścieniu: dT = 4 pi r rho F v (v + v_ext)  <->  dT = nb/2 rho U^2 c cl
        q = sig * cl * x / (8 * F)
        li = -le / 2 + np.sqrt((le / 2) ** 2 + np.maximum(q, 1e-10))
        lam = 0.75 * lam + 0.25 * (li + le)
    phi = np.arctan2(lam, x); cl, cd = polar(th - phi)
    U2 = (Om * R) ** 2 * (x ** 2 + lam ** 2)
    dL = 0.5 * rho * U2 * c * cl; dD = 0.5 * rho * U2 * c * cd
    dT = b.nb * (dL * np.cos(phi) - dD * np.sin(phi))
    dQ = b.nb * (dL * np.sin(phi) + dD * np.cos(phi)) * r
    dQ0 = b.nb * dD * np.cos(phi) * r                     # moment oporu profilowego
    T = dT.sum() * dr; Q = dQ.sum() * dr
    return dict(T=T, Q=Q, P=Q * Om, P0=dQ0.sum() * dr * Om, r=r, x=x, lam=lam, li=lam - le, cl=cl, cd=cd,
                al=np.degrees(th - phi), dT=dT, c=c)


def coax(bu, bl, thu, thl, Om, rho=RHO0, zsp=0.40):
    R = bu.R
    kc = 0.78 + 0.22 * np.exp(-4 * zsp / R)          # zwężenie strugi górnego na wys. dolnego
    kv = 2 - np.exp(-4 * zsp / R)                    # przyspieszenie strugi (1 → 2 v_i)
    up = bem(bu, thu, Om, rho)
    lo = None
    for _ in range(3):
        lu, xu = up["li"], up["x"]
        def ext(r, lu=lu, xu=xu):
            xs = r / (bl.R * kc)
            v = np.interp(xs, xu, lu, left=lu[0], right=0.0) * kv / kc ** 0
            return np.where(xs <= 1.0, v, 0.0)
        lo = bem(bl, thl, Om, rho, ext)
        dl = 0.06 * np.mean(lo["li"])                # oddziaływanie dolnego na górny (indukcja w górę strugi)
        up = bem(bu, thu, Om, rho, lambda r: np.full_like(r, dl))
    return up, lo


def trim(bu, bl, Om, W, rho=RHO0, th0=(9.0, 10.0)):
    """kąty łopat dające ciąg = W i równowagę momentów (brak obrotu)."""
    thu, thl = th0
    for _ in range(30):
        up, lo = coax(bu, bl, thu, thl, Om, rho)
        e = np.array([W - (up["T"] + lo["T"]), lo["Q"] - up["Q"]])
        if abs(e[0]) < 0.3 and abs(e[1]) < 0.05: break
        J = np.zeros((2, 2)); d = 0.05
        for j, (a, b_) in enumerate([(thu + d, thl), (thu, thl + d)]):
            u2, l2 = coax(bu, bl, a, b_, Om, rho)
            J[0, j] = ((u2["T"] + l2["T"]) - (up["T"] + lo["T"])) / d
            J[1, j] = -((l2["Q"] - u2["Q"]) - (lo["Q"] - up["Q"])) / d
        dx = np.linalg.solve(J, e); thu += dx[0]; thl += dx[1]
    P = up["P"] + lo["P"]
    A = np.pi * bu.R ** 2
    Pid = W ** 1.5 / np.sqrt(2 * rho * A)
    return dict(thu=thu, thl=thl, Tu=up["T"], Tl=lo["T"], Qu=up["Q"], Ql=lo["Q"], P=P, P0=up["P0"] + lo["P0"],
                FM=Pid / P, clmax=max(up["cl"].max(), lo["cl"].max()), up=up, lo=lo)


def ff_power(W, V, Ph, P0h, R, Vt, rho=RHO0, f_eq=0.65, ka=1.15):
    """moc w locie poziomym (metoda energetyczna skalibrowana zawisem BEM).
    f_eq – powierzchnia oporu szkodliwego [m2] (pilot siedzący + rama + napęd)."""
    A = np.pi * R ** 2
    vh = np.sqrt(W / (2 * rho * A))
    Pi_h = Ph - P0h
    kappa = Pi_h / (W * vh)                      # współczynnik strat indukowanych z BEM
    # Glauert: v_i w locie
    vi = vh
    for _ in range(100):
        vi = 0.5 * vi + 0.5 * vh ** 2 / np.sqrt(V ** 2 + vi ** 2)
    mu = V / Vt
    Pi = kappa * W * vi
    P0 = P0h * (1 + 4.65 * mu ** 2)
    Pp = 0.5 * rho * f_eq * V ** 3
    return Pi + P0 + Pp
