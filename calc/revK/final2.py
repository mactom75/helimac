import os
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
import sizing as S, json
DET=dict(lopaty=9.86, silnik=8.6, przekladnia_pasowa=6.0, piasty=3.6, kolumna_waly_lozyska=4.25, sterowanie=1.8,
         falownik=2.0, instalacja_400V=1.5, awionika=1.0, rama=6.2, siedzisko_podnozek=2.5, mocowanie_akumulatora=0.8)
S.FIXED={}
S.mass_drive=lambda Q,T,CF: {k:v for k,v in DET.items() if k!='lopaty'}
S.ETA['belt']=0.97; S.ETA_CH=S.np.prod(list(S.ETA.values()))
o=S.run(rpm=500,c_root=0.17,c_tip=0.115,m_bat=40.0,m_empty0=sum(DET.values()))
r=dict(me=o['m_empty'],MTOW=o['MTOW'],Ph=o['P_h'],FM=o['FM'],Pc=o['P_c'],Ve=o['V_e'],th=o['t_h'],tm=o['t_mix'],Q=o['Q'],thu=o['thu'],thl=o['thl'],
       P13=o['P13hot'],cl13=o['cl13hot'],mb=o['m_blade'],J=o['J'],masses=o['masses'],Pff=list(o['Pff']))
print({k:(round(float(v),2) if not isinstance(v,(dict,list)) else '') for k,v in r.items()}); print({k:round(v,2) for k,v in r['masses'].items()})
json.dump(r,open(os.path.join(RES, 'final2.json'), 'w'),default=float,indent=1)
