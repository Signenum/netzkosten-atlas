"""Netzgebiete (Mittelspannung) aus Stichproben-Abfragen + VG250-Gemeindegrenzen.

Eingaben (Ordner geo/):
  gem.pkl      – VG250-Gemeinden (BKG, dl-de/by-2-0): (DataFrame[GEM,KRS,LAN,EWZ,KFL], [shapely-Geometrien])
  grid.json    – Raster-Parameter + Maske + Stützpunkte (Gemeinden >= 20.000 EW)
  res.json     – Ergebnis je Punkt: {"g<k>"|"p<i>": "vnbId|vnbId"}
  names.json   – {vnbId: Name laut VNBdigital}
  vnbmap.json  – {vnbId: Anzeigename im Atlas} (geprüfte Zuordnung)
Ausgabe: geo/netzgebiete.geojson, geo/laender.geojson, geo/gemeinde_vnb.csv
"""
import json, pickle, csv, sys, os
from collections import defaultdict
import numpy as np
from shapely.geometry import Point, mapping
from shapely.ops import unary_union
from shapely.strtree import STRtree

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo') + '/'
d, G = pickle.load(open(D + 'gem.pkl', 'rb'))
grid = json.load(open(D + 'grid.json'))
res = json.load(open(D + 'res.json'))
names = json.load(open(D + 'names.json'))
vmap = json.load(open(D + 'vnbmap.json'))
_ex = json.load(open(os.path.join(os.path.dirname(D[:-1]), 'extra_vnb.json'), encoding='utf-8'))
vmap.update({v['id']: v['disp'] for v in _ex.values() if v.get('id')})

tree = STRtree(G)
votes = defaultdict(lambda: defaultdict(float))
pts = []  # (lon, lat, ids) for nearest fallback
for k, v in res.items():
    ids = [x for x in v.split('|') if x]
    if k[0] == 'g':
        i = int(k[1:]); r, c = divmod(i, grid['C'])
        lat = grid['lat0'] + r * grid['dl']; lon = grid['lon0'] + c * grid['dn']
        if not ids: continue
        pts.append((lon, lat, ids))
        hit = tree.query(Point(lon, lat), predicate='within')
        for gi in hit:
            for x in ids: votes[gi][x] += 1 / len(ids)
    else:
        gi = int(k[1:])
        for x in ids: votes[gi][x] += 3 / len(ids)  # Stützpunkt in der Gemeinde selbst zählt stärker
P = np.array([(p[0], p[1]) for p in pts])
assign = {}
for gi in range(len(G)):
    if votes[gi]:
        assign[gi] = max(votes[gi].items(), key=lambda t: t[1])[0]
    else:  # keine Stichprobe in der Gemeinde: nächster Rasterpunkt
        rp = G[gi].representative_point()
        dist = (P[:, 0] - rp.x) ** 2 * 0.4 + (P[:, 1] - rp.y) ** 2
        assign[gi] = pts[int(dist.argmin())][2][0]

with open(D + 'gemeinde_vnb.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['Gemeinde', 'Kreis', 'Land', 'VNB_ID_VNBdigital', 'VNB_Name', 'im_Atlas_als', 'Stichproben'])
    for gi in range(len(G)):
        x = assign[gi]
        w.writerow([d.GEM[gi], d.KRS[gi], d.LAN[gi], x, names.get(x, ''), vmap.get(x, ''), round(sum(votes[gi].values()), 1)])

groups = defaultdict(list)
for gi, x in assign.items(): groups[x].append(G[gi])

def rnd(geom, nd=4):
    m = mapping(geom)
    def r(c):
        if isinstance(c[0], (float, int)): return [round(c[0], nd), round(c[1], nd)]
        return [r(e) for e in c]
    return {'type': m['type'], 'coordinates': r(m['coordinates'])}

import shapely
keys = list(groups)
dis = [unary_union(groups[x]) for x in keys]
try:  # gemeinsame Vereinfachung: Nachbargebiete teilen sich exakt dieselbe Grenzlinie (keine Spalten)
    simp = list(shapely.coverage_simplify(dis, 0.003))
except Exception as e:
    print('coverage_simplify fehlgeschlagen, Einzelvereinfachung:', e)
    simp = [g.simplify(0.003, preserve_topology=True) for g in dis]
stats = defaultdict(lambda: [0, 0, set()])
for gi, x in assign.items():
    st = stats[x]; st[0] += 1
    st[1] += int(d.EWZ[gi]) if d.EWZ[gi] == d.EWZ[gi] else 0
    if isinstance(d.LAN[gi], str): st[2].add(d.LAN[gi])
feats = []
for x, u in zip(keys, simp):
    if u.is_empty: continue
    g, e, l = stats[x]
    feats.append({'type': 'Feature', 'properties': {'id': x, 'v': names.get(x, '?'), 'n': vmap.get(x), 'g': g, 'e': e, 'l': sorted(l)}, 'geometry': rnd(u)})
json.dump({'type': 'FeatureCollection', 'features': feats}, open(D + 'netzgebiete.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))

CODE = {"Baden-Württemberg": "BW", "Bayern": "BY", "Berlin": "BE", "Brandenburg": "BB", "Bremen": "HB", "Hamburg": "HH", "Hessen": "HE",
        "Mecklenburg-Vorpommern": "MV", "Niedersachsen": "NI", "Nordrhein-Westfalen": "NW", "Rheinland-Pfalz": "RP", "Saarland": "SL",
        "Sachsen": "SN", "Sachsen-Anhalt": "ST", "Schleswig-Holstein": "SH", "Thüringen": "TH"}
lg = defaultdict(list)
for gi in range(len(G)):
    if isinstance(d.LAN[gi], str) and d.LAN[gi] in CODE: lg[d.LAN[gi]].append(G[gi])
_lk = list(lg); _lu = list(shapely.coverage_simplify([unary_union(lg[k]) for k in _lk], 0.003))
lf = [{'type': 'Feature', 'properties': {'n': k, 'c': CODE.get(k, k)}, 'geometry': rnd(u)} for k, u in zip(_lk, _lu)]
json.dump({'type': 'FeatureCollection', 'features': lf}, open(D + 'laender.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))
inatlas = sum(1 for f in feats if f['properties']['n'])
print('Gebiete', len(feats), 'davon im Atlas', inatlas, 'Gemeinden ohne Stichprobe', sum(1 for gi in range(len(G)) if not votes[gi]))
print('Größe', os.path.getsize(D + 'netzgebiete.geojson') // 1024, 'KB', os.path.getsize(D + 'laender.geojson') // 1024, 'KB')
