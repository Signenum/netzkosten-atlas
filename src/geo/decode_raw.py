"""Wandelt stichproben_raw.txt (aus der VNBdigital-Abfrage) in res.json + names.json um."""
import json, os, base64
D = os.path.dirname(os.path.abspath(__file__)) + '/'
txt = open(D + 'stichproben_raw.txt', encoding='utf-8').read()
parts = {}; cur = None
for line in txt.split('\n'):
    if line.startswith('### '): cur = line[4:].strip(); parts[cur] = []; continue
    if cur and line != '': parts[cur].append(line)
ids, names = [], {}
for l in parts['NAMES']:
    k, v = l.split('=', 1); ids.append(k); names[k] = v.strip()
def expand(s):
    out = []
    for tok in s.split(','):
        if '*' in tok: v, n = tok.rsplit('*', 1); out += [v] * int(n)
        else: out.append(tok)
    return [('|'.join(ids[int(x, 36)] for x in v.split('.')) if v and v != '?' else '') for v in out]
P = expand(parts['P'][0]); G = expand(parts['G'][0])
grid = json.load(open(D + 'grid.json'))
bits = []
for b in base64.b64decode(grid['mask']):
    bits += [(b >> (7 - i)) & 1 for i in range(8)]
gk = [k for k in range(grid['R'] * grid['C']) if bits[k]]
pk = [s.split(',')[0] for s in grid['pts'].split(';')]
print('names', len(ids), 'P', len(P), len(pk), 'G', len(G), len(gk))
assert len(P) == len(pk) and len(G) == len(gk)
res = {'g%d' % k: v for k, v in zip(gk, G)}
res.update({'p' + k: v for k, v in zip(pk, P)})
json.dump(res, open(D + 'res.json', 'w')); json.dump(names, open(D + 'names.json', 'w'), ensure_ascii=False, indent=0)
print('leer', sum(1 for v in res.values() if not v))
