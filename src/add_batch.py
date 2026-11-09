"""python add_batch.py batch.json  – Liste von {id, disp, typ, src, stand, MS, MS/NS, NS, HS/MS, HS, bkz?}"""
import sys, json, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
BL = {"Baden-Württemberg": "BW", "Bayern": "BY", "Berlin": "BE", "Brandenburg": "BB", "Bremen": "HB", "Hamburg": "HH", "Hessen": "HE",
      "Mecklenburg-Vorpommern": "MV", "Niedersachsen": "NI", "Nordrhein-Westfalen": "NW", "Rheinland-Pfalz": "RP", "Saarland": "SL",
      "Sachsen": "SN", "Sachsen-Anhalt": "ST", "Schleswig-Holstein": "SH", "Thüringen": "TH"}
todo = {x[0]: x for x in json.load(open(S + 'geo/todo_other.json', encoding='utf-8'))}
names = json.load(open(S + 'geo/names.json', encoding='utf-8'))
ex = json.load(open(S + 'extra_vnb.json', encoding='utf-8'))
ne = json.load(open(S + 'ne.json', encoding='utf-8')); bk = json.load(open(S + 'bkz.json', encoding='utf-8'))
for e in json.load(open(sys.argv[1], encoding='utf-8')):
    vid = e['id']; name = names[vid]
    lands = todo[vid][2].split('/') if vid in todo else []
    bl = '/'.join(BL[l] for l in lands) or e.get('bl', '?')
    ex[name] = {'disp': e['disp'], 'bl': bl, 'typ': e.get('typ', 'Stadt'), 'id': vid}
    rec = {'src': e['src'], 'stand': e.get('stand', '2026')}
    for lv in ('HS', 'HS/MS', 'MS', 'MS/NS', 'NS'):
        if lv in e:
            t = e[lv]; chk = t[0] + 25 * (t[1] - t[3]) - t[2]
            if abs(chk) > 1.5: print('WARN Plausibilität', e['disp'], lv, round(chk, 2))
            rec[lv] = t
    ne[name] = rec
    if 'bkz' in e: bk[name] = dict(e['bkz'], src=e.get('bkzsrc', e['src']))
    print('ok', e['disp'], bl)
for fn, d in (('extra_vnb.json', ex), ('ne.json', ne), ('bkz.json', bk)):
    json.dump(d, open(S + fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
