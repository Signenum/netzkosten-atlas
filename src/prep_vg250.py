"""VG250-Gemeinden für build_geo.py vorbereiten.

Quelle: © GeoBasis-DE / BKG, VG250-EW (dl-de/by-2-0), als R-Datensatz aufbereitet in
https://github.com/dimfalk/vg250 (data/vg250.rda, EPSG:4326).
Aufruf: python prep_vg250.py pfad/zu/vg250.rda   -> geo/gem.pkl
Benötigt: pip install rdata shapely pandas
"""
import sys, os, pickle
import numpy as np, rdata
from shapely.geometry import Polygon, MultiPolygon

def geom(x):
    if isinstance(x, list) and x and isinstance(x[0], np.ndarray):
        return Polygon(x[0], x[1:])
    ps = []
    for p in x:
        if isinstance(p, list) and p and isinstance(p[0], np.ndarray): ps.append(Polygon(p[0], p[1:]))
        elif isinstance(p, np.ndarray): ps.append(Polygon(p))
    return MultiPolygon(ps) if len(ps) > 1 else ps[0]

d = rdata.conversion.convert(rdata.parser.parse_file(sys.argv[1]), default_encoding='utf8')['vg250']
G = [geom(x).buffer(0) for x in d['geom']]
d = d.drop(columns=['geom']).reset_index(drop=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo', 'gem.pkl')
pickle.dump((d, G), open(out, 'wb'))
print(len(G), 'Gemeinden ->', out)
