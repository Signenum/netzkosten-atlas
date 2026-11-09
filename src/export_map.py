import os
import pandas as pd, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meta import key
f=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Netzkosten_Auswertung_Deutschland.xlsx')
g=pd.read_excel(f,sheet_name='Ranking',header=3)
g.columns=['VNB','BL','BL1','Typ','MS','NS','HS','ONS','UW','BKZ','Bb','NNE','NNENS']+list(g.columns[13:])
g=g[g.VNB.astype(str).str.len()<60]
idx=g.columns[20]; kat=g.columns[22]
raw=pd.read_excel(f,sheet_name='NAP_Rohdaten',header=3)
raw.columns=['VNB','Bez','Datum','NE','Per','Art','M','U','Mio','spez','u2','Ed']
napsrc=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/napsrc.json')); napsrc26=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/napsrc26.json'))
ne=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/ne.json')); bkz=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/bkz.json'))
from meta import META
srcne={META[key(n)][0]:(v.get('src'),v.get('stand')) for n,v in ne.items()}
srcb={META[key(n)][0]:v.get('src') for n,v in bkz.items()}
C=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/coords.json'))
out=[]
num=lambda x: None if pd.isna(x) else round(float(x),4)
for r in g.itertuples(index=False):
    if r.VNB not in C: print('nocoord',r.VNB); continue
    sub=raw[raw.VNB==r.VNB]
    nap=naped=napurl=None
    if len(sub):
        s26=sub[sub.Ed=='NAP 2026']
        row=(s26 if len(s26) else sub).iloc[0]
        nap=str(row.Datum); is26=len(s26)>0
        naped='Netzausbauplan 2026' + (' (teils NAP 2024)' if is26 and (sub.Ed!='NAP 2026').any() else '') if is26 else 'Netzausbauplan 2024'
        fid=(napsrc26 if is26 else napsrc).get(key(row.Bez))
        if fid: napurl='https://www.vnbdigital.de/gateway/files?serviceName=vnb&fileId='+fid
    out.append(dict(n=r.VNB,bl=r.BL1,bla=r.BL,t=r.Typ,lat=C.get(r.VNB,[51,10])[0],lon=C.get(r.VNB,[51,10])[1],ms=num(r.MS),ns=num(r.NS),hs=num(r.HS),ons=num(r.ONS),uw=num(r.UW),
        bkz=num(r.BKZ),bb=None if pd.isna(r.Bb) else r.Bb,nne=num(r.NNE),nnens=num(r.NNENS),idx=num(getattr(r,'_20') if False else g.loc[g.VNB==r.VNB,idx].iloc[0]),
        kat=None if pd.isna(g.loc[g.VNB==r.VNB,kat].iloc[0]) else g.loc[g.VNB==r.VNB,kat].iloc[0],
        nap=nap,naped=naped,napurl=napurl,srcne=srcne.get(r.VNB,(None,None))[0],stne=srcne.get(r.VNB,(None,None))[1],srcb=srcb.get(r.VNB)))
geo=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/geo/laender.geojson'))
ng=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/geo/netzgebiete.geojson'))
def area(r): return sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1))/2
def fixpoly(p): return [(r[::-1] if ((i==0 and area(r)>0) or (i>0 and area(r)<0)) else r) for i,r in enumerate(p)]
for ft in geo['features']+ng['features']:
    gg=ft['geometry']; gg['coordinates']=[fixpoly(p) for p in gg['coordinates']] if gg['type']=='MultiPolygon' else fixpoly(gg['coordinates'])
t=open(os.path.dirname(os.path.abspath(__file__))+'/map_template.html').read().replace('__N__',str(len(out))).replace('__DATA__',json.dumps(out,ensure_ascii=False,separators=(',',':'))).replace('__GEO__',json.dumps(geo,separators=(',',':'))).replace('__NG__',json.dumps(ng,ensure_ascii=False,separators=(',',':')))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'),'w').write(t); print(len(out))

# ---- Entwicklung: NAP 2024 vs 2026 + Investitionen je Zeitraum ----
exec(open(os.path.dirname(os.path.abspath(__file__))+'/nap_data.py').read()); R24=R
exec(open(os.path.dirname(os.path.abspath(__file__))+'/nap26_data.py').read())
from collections import defaultdict
def kenn(recs):
    acc=defaultdict(lambda:[0.0,0.0])
    for v,d,ne,per,art,m,u,mio in recs:
        if per not in ('T5','T10') or not m: continue
        if art=='Anlage' and u=='UW' and ne=='HS': ne='HS/MS'
        k={('MS','km'):'ms',('NS','km'):'ns',('HS','km'):'hs',('MS/NS','ONS'):'ons',('HS/MS','UW'):'uw'}.get((ne,u))
        if not k: continue
        a=acc[(META[key(v)][0],k)]; a[0]+=m; a[1]+=mio
    res=defaultdict(dict)
    for (n,k),(m,mio) in acc.items():
        if m>0: res[n][k]=round(mio*(1 if k=='uw' else 1000)/m,2)
    return res
k24=kenn([r for r in R24 if key(r[0]) not in ('edis_bb','edis_mv')])
# E.DIS 2024 gesamt aus beiden TNG
k24e=kenn([tuple(['E.DIS Netz']+list(r[1:])) for r in R24 if key(r[0]) in ('edis_bb','edis_mv')])
k24.update(k24e)
k26=kenn(R26)
inv=defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
for v,d,ne,per,art,m,u,mio in R26:
    inv[META[key(v)][0]][per][ne]+=mio
names={d['n'] for d in out}
DEV={n:{'a':k24.get(n,{}),'b':k26.get(n,{}),'inv':{p:{ne:round(x,2) for ne,x in dd.items()} for p,dd in inv.get(n,{}).items()}} for n in names}
t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')).read().replace('__DEV__',json.dumps(DEV,ensure_ascii=False,separators=(',',':')))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'),'w').write(t)
print('dev', sum(1 for n in DEV if DEV[n]['a'] and DEV[n]['b']))

NNE={}
for yr,fn in (('2025','ne25.json'),('2026','ne.json'),('2027','ne27.json')):
    for n,v in json.load(open(os.path.dirname(os.path.abspath(__file__))+'/'+fn)).items():
        d=META[key(n)][0]
        NNE.setdefault(d,{})[yr]={k:x for k,x in v.items() if isinstance(x,list)}
        NNE[d].setdefault('src',{})[yr]=v.get('src')
t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')).read().replace('__NNE__',json.dumps(NNE,ensure_ascii=False,separators=(',',':')))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'),'w').write(t)
print('nne',len(NNE),{y:sum(1 for d in NNE.values() if y in d) for y in ('2025','2026','2027')})

# Eigenständiges HTML-Dokument für das Repository (index.html) + Fragment für die Artifact-Veröffentlichung
_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
_t = open(_p).read()
if not _t.lstrip().lower().startswith('<!doctype'):
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atlas_fragment.html'), 'w').write(_t)
    _i = _t.index('</style>') + len('</style>')
    _t = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
          + _t[:_i] + '\n</head>\n<body>\n' + _t[_i:] + '\n</body>\n</html>\n')
    open(_p, 'w').write(_t)
