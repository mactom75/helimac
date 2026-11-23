import os
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
import sizing as S, json
def md_belt(Q,T,CF): return dict(silnik=1.5+0.17*T, przekladnia=2.0+0.0075*2*Q, piasty=2*(0.5+0.08*CF), walki_kolumna=2.5+0.003*2*Q)
def md_cyc(Q,T,CF):
    Qt=2*Q
    return dict(silnik=1.5+0.17*T, przekladnia=0.8*11.0*(Qt/472)**0.8 + 5.0*(Qt/472)**0.8 + 1.8, piasty=2*(0.5+0.08*CF), walki_kolumna=2.5+0.003*2*Q)
res={}
for name,md,eb in (('pasowa',md_belt,0.97),('cykloidalna',md_cyc,0.94)):
    S.mass_drive=md; S.ETA['belt']=eb; S.ETA_CH=S.np.prod(list(S.ETA.values()))
    o=S.run(rpm=500,c_root=0.17,c_tip=0.115,m_bat=40.0)
    res[name]=dict(me=o['m_empty'],MTOW=o['MTOW'],Ph=o['P_h'],Pc=o['P_c'],th=o['t_h'],tm=o['t_mix'],Q=o['Q'],Tmot=o['T_mot'],P13=o['P13hot'],cl13=o['cl13hot'],masses=o['masses'],mb=o['m_blade'],J=o['J'],thu=o['thu'],thl=o['thl'])
    print(name,{k:(round(float(v),2) if not isinstance(v,dict) else {a:round(b,2) for a,b in v.items()}) for k,v in res[name].items()},flush=True)
json.dump(res,open(os.path.join(RES, 'variants.json'), 'w'),default=float,indent=1)
