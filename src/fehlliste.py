"""Erzeugt ../data/fehlende_preisblaetter.csv: welche Preisblätter fehlen, sortiert nach versorgten Einwohnern."""
import os, json, sys, csv
S = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, S)
from meta import key, META
ng = json.load(open(S + 'geo/netzgebiete.geojson'))
n = lambda fn: {META[key(x)][0]: v for x, v in json.load(open(S + fn)).items()}
n26, n25, n27, bk = n('ne.json'), n('ne25.json'), n('ne27.json'), n('bkz.json')
atlas = {}; other = []
for f in ng['features']:
    p = f['properties']
    if p['n']:
        a = atlas.setdefault(p['n'], [0, set()]); a[0] += p['e']; a[1].update(p['l'])
    else:
        other.append((p['e'], p['v'], ', '.join(p['l'])))
for name, *_ in [(v[0],) for v in META.values()]:
    atlas.setdefault(name, [0, set()])
rows = []
for name, (e, l) in atlas.items():
    if name.startswith('E.DIS Netz –'): continue
    miss = []
    if name not in n26: miss.append('Netzentgelte 2026')
    if name not in bk or 'MS' not in bk[name]: miss.append('BKZ MS (veröffentlicht)')
    if name not in n25: miss.append('Netzentgelte 2025')
    if name not in n27: miss.append('Netzentgelte 2027 vorläufig')
    if miss: rows.append(('im Atlas', name, ', '.join(sorted(l)), e, '; '.join(miss)))
for e, v, l in other:
    rows.append(('noch nicht im Atlas', v, l, e, 'Netzentgelte 2026; BKZ MS'))
prio = lambda r: (0 if 'Netzentgelte 2026' in r[4] else 1, -r[3])
rows.sort(key=prio)
with open(os.path.join(S, '..', 'data', 'fehlende_preisblaetter.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['Status', 'Netzbetreiber', 'Bundesland', 'Einwohner_im_Netzgebiet', 'fehlt'])
    w.writerows(rows)
print(len(rows), 'Einträge')
