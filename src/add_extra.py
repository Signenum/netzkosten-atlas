"""Neuen Netzbetreiber ohne NAP mit Preisblatt-Daten aufnehmen.
python add_extra.py <VNBdigital-ID> "<Anzeigename>" <BL> <Stadt|Fläche> '<json mit src, stand, MS:[4], MS/NS:[4], NS:[4], ...>' ['<bkz-json>']"""
import sys, json, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
vid, disp, bl, typ, ne = sys.argv[1:6]
names = json.load(open(S + 'geo/names.json', encoding='utf-8'))
name = names[vid]
ex = json.load(open(S + 'extra_vnb.json', encoding='utf-8'))
ex[name] = {'disp': disp, 'bl': bl, 'typ': typ, 'id': vid}
json.dump(ex, open(S + 'extra_vnb.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for fn, val in (('ne.json', ne), ('bkz.json', sys.argv[6] if len(sys.argv) > 6 else None)):
    if not val: continue
    d = json.load(open(S + fn, encoding='utf-8')); d[name] = json.loads(val)
    json.dump(d, open(S + fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', name, '->', disp)
