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

feats = []
for x, gs in groups.items():
    u = unary_union(gs).simplify(0.003, preserve_topology=True)
    if u.is_empty: continue
    feats.append({'type': 'Feature', 'properties': {'id': x, 'v': names.get(x, '?'), 'n': vmap.get(x)}, 'geometry': rnd(u)})
json.dump({'type': 'FeatureCollection', 'features': feats}, open(D + 'netzgebiete.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))

CODE = {"Baden-Württemberg": "BW", "Bayern": "BY", "Berlin": "BE", "Brandenburg": "BB", "Bremen": "HB", "Hamburg": "HH", "Hessen": "HE",
        "Mecklenburg-Vorpommern": "MV", "Niedersachsen": "NI", "Nordrhein-Westfalen": "NW", "Rheinland-Pfalz": "RP", "Saarland": "SL",
        "Sachsen": "SN", "Sachsen-Anhalt": "ST", "Schleswig-Holstein": "SH", "Thüringen": "TH"}
lg = defaultdict(list)
for gi in range(len(G)):
    if isinstance(d.LAN[gi], str) and d.LAN[gi] in CODE: lg[d.LAN[gi]].append(G[gi])
lf = [{'type': 'Feature', 'properties': {'n': k, 'c': CODE.get(k, k)}, 'geometry': rnd(unary_union(v).simplify(0.003, preserve_topology=True))} for k, v in lg.items()]
json.dump({'type': 'FeatureCollection', 'features': lf}, open(D + 'laender.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))
inatlas = sum(1 for f in feats if f['properties']['n'])
print('Gebiete', len(feats), 'davon im Atlas', inatlas, 'Gemeinden ohne Stichprobe', sum(1 for gi in range(len(G)) if not votes[gi]))
print('Größe', os.path.getsize(D + 'netzgebiete.geojson') // 1024, 'KB', os.path.getsize(D + 'laender.geojson') // 1024, 'KB')
