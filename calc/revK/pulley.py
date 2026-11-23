"""Koło pasowe 8M ze szprychami frezowanymi z Al 7075-T6 – dobór liczby szprych."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
import numpy as np, json
DLIM=0.10e-3
E7=71.7e9; RHO=2810; SIG_A=70e6      # dopuszczalna amplituda zmęczeniowa (3e7 cykli, z karbem)
def design(z, b_belt, Q, Te, N, r_hub=0.040, web=0.012):
    dp=z*8e-3/np.pi; R=dp/2-3.4e-3          # promień dna zębów
    W=b_belt+2*1.5e-3                       # szerokość wieńca z obrzeżami 1,5 mm
    T1=Te*1.4; q=T1/R                       # nacisk promieniowy pasa [N/m] po stronie czynnej
    L=2*np.pi*R/N                           # rozpiętość wieńca między szprychami
    best=None
    for tr in np.arange(2.0e-3,30e-3,0.25e-3):   # grubość wieńca pod zębami
        I=W*tr**3/12; Wb=W*tr**2/6
        k=1.0 if N>=6 else (1.15 if N==5 else 1.35)   # krzywizna i obciążenie częściowe przy rzadkich szprychach
        M=k*q*L**2/12; d=k*q*L**4/(384*E7*I)
        if M/Wb<=SIG_A and d<=DLIM: best=(tr,M/Wb,d); break
    if best is None: return dict(N=N,masa=float("nan"))
    tr,sr,dr=best
    l=R-tr-r_hub
    Ft=Q/(R*N)*2.0                          # siła obwodowa na szprychę (2× – nierównomierny udział)
    Fr=2*(T1+Te*0.4)/N*1.5                  # składowa od wypadkowej pasa
    for bs in np.arange(4e-3,30e-3,0.5e-3): # szerokość szprychy w płaszczyźnie koła
        Ws=web*bs**2/6; A=web*bs
        s=Ft*l/2/Ws+Fr/A
        if s<=SIG_A: break
    m_rim=RHO*(2*np.pi*(R+tr/2)*W*tr + 2*np.pi*R*b_belt*1.7e-3*0.5)   # wieniec + zęby
    m_sp=RHO*N*bs*web*l*1.1
    m_hub=RHO*np.pi*(r_hub**2-0.026**2)*0.040
    return dict(N=N,tr=tr*1e3,sig_rim=sr/1e6,ugiecie_um=dr*1e6,b_szprychy=bs*1e3,sig_sp=s/1e6,masa=m_rim+m_sp+m_hub,m_wieniec=m_rim,m_szprychy=m_sp,m_piasta=m_hub)
res={}
for name,z,b,Q,Te in (('120T (stopnie końcowe)',120,36e-3,251.7,1673),('90T (stopień 1)',90,21e-3,43.25*3/0.985,1132)):
    rows=[design(z,b,Q,Te,N) for N in (3,4,5,6,8,10,12)]
    res[name]=rows
    print(name)
    for r in rows: print({k:round(v,2) for k,v in r.items()})
    # pełna tarcza dla porównania
json.dump(res,open(os.path.join(RES, 'pulley.json'), 'w'),indent=1,ensure_ascii=False)
