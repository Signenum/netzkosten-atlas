"""Exportiert die Daten der Auswertung als CSV nach ../data/ (nach build_eval.py, add_nne_sheet.py und Neuberechnung der Excel-Formeln)."""
import os, json, sys, csv, shutil
import pandas as pd
S = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, S)
from meta import key, META
OUT = os.path.join(S, '..', 'data') + '/'
X = os.path.join(S, '..', 'Netzkosten_Auswertung_Deutschland.xlsx')
os.makedirs(OUT, exist_ok=True)

g = pd.read_excel(X, sheet_name='Ranking', header=3)
g = g[g.iloc[:, 0].astype(str).str.len() < 60]
g.columns = [str(c).replace('\n', ' ') for c in g.columns]
g.to_csv(OUT + 'vnb_kennwerte.csv', index=False, encoding='utf-8')

raw = pd.read_excel(X, sheet_name='NAP_Rohdaten', header=3)
raw.columns = [str(c).replace('\n', ' ') for c in raw.columns]
raw.dropna(how='all').to_csv(OUT + 'nap_rohdaten.csv', index=False, encoding='utf-8')

with open(OUT + 'netzentgelte.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['VNB', 'Jahr', 'Netzebene', 'LP_unter_2500h_EUR_kW_a', 'AP_unter_2500h_ct_kWh', 'LP_ab_2500h_EUR_kW_a', 'AP_ab_2500h_ct_kWh', 'Stand', 'Quelle'])
    for yr, fn in (('2025', 'ne25.json'), ('2026', 'ne.json'), ('2027 vorläufig', 'ne27.json')):
        for n, v in json.load(open(S + fn)).items():
            for ne in ('HS', 'HS/MS', 'MS', 'MS/NS', 'NS'):
                t = v.get(ne)
                if isinstance(t, list): w.writerow([META[key(n)][0], yr, ne, *t, v.get('stand', ''), v.get('src', '')])

with open(OUT + 'bkz.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['VNB', 'Netzebene', 'BKZ_EUR_kW', 'Stand', 'Quelle'])
    for n, v in json.load(open(S + 'bkz.json')).items():
        for ne in ('HS', 'HS/MS', 'MS', 'MS/NS', 'NS'):
            if isinstance(v.get(ne), (int, float)): w.writerow([META[key(n)][0], ne, v[ne], v.get('stand', ''), v.get('src', '')])

for fn in ('netzgebiete.geojson', 'gemeinde_vnb.csv', 'laender.geojson'):
    p = S + 'geo/' + fn
    if os.path.exists(p): shutil.copy(p, OUT + fn)
print('CSV exportiert nach', os.path.abspath(OUT))
