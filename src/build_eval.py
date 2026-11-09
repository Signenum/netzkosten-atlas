import os
import json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meta import META, key
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
from openpyxl.comments import Comment

D = os.path.dirname(os.path.abspath(__file__)) + '/'
exec(open(D + 'nap_data.py').read())          # -> R (NAP 2024)
R24 = R
exec(open(D + 'nap26_data.py').read())        # -> R26 (NAP 2026)
_have26 = {(key(r[0]), r[2]) for r in R26}
R = []; EDN = []
for r in R26:
    if r[2] == 'HöS/HS': continue   # HöS/HS-UW nicht in die Kennwerte (ÜNB-Schnittstelle)
    R.append(r); EDN.append('NAP 2026')
for r in R24:
    r = list(r)
    if r[4] == 'Anlage' and r[6] == 'UW' and r[2] == 'HS': r[2] = 'HS/MS'
    if (key(r[0]), r[2]) in _have26: continue
    if key(r[0]) in ('edis_bb', 'edis_mv'): continue   # NAP 2026 der E.DIS ist gesamt ausgewiesen
    R.append(tuple(r)); EDN.append('NAP 2024 (Fallback)')
NE = json.load(open(D + 'ne.json'))
BKZ = json.load(open(D + 'bkz.json'))
NAPSRC = json.load(open(D + 'napsrc.json')) if __import__('os').path.exists(D + 'napsrc.json') else {}
NAPSRC26 = json.load(open(D + 'napsrc26.json'))
FIND = open(D + 'findings.txt').read() if __import__('os').path.exists(D + 'findings.txt') else ''

PRIMARY_BL = {"NW/RP/NI": "NW", "SN/ST/BB/TH": "ST", "BB/MV": "BB"}
LEVELS = ["HS", "HS/MS", "MS", "MS/NS", "NS"]

def disp(n): return META[key(n)][0]
def bl(n): return META[key(n)][1]
def typ(n): return META[key(n)][2]
def bl1(n): b = bl(n); return PRIMARY_BL.get(b, b)

# ---------- styles ----------
F = Font(name='Arial', size=10)
FB = Font(name='Arial', size=10, bold=True)
FH = Font(name='Arial', size=10, bold=True, color='FFFFFF')
FT = Font(name='Arial', size=14, bold=True)
FIN = Font(name='Arial', size=10, color='0000FF')      # hardcoded inputs
FLINK = Font(name='Arial', size=10, color='008000')    # links to other sheets
FGREY = Font(name='Arial', size=9, italic=True, color='666666')
HFILL = PatternFill('solid', fgColor='1F4E78')
SFILL = PatternFill('solid', fgColor='DDEBF7')
YFILL = PatternFill('solid', fgColor='FFFF00')
thin = Side(style='thin', color='BFBFBF')
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WR = Alignment(wrap_text=True, vertical='top')
CEN = Alignment(horizontal='center', vertical='center', wrap_text=True)

wb = Workbook()

def header(ws, row, labels, widths=None):
    for i, t in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=t)
        c.font = FH; c.fill = HFILL; c.alignment = CEN; c.border = BOX
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[L(i)].width = w
    ws.row_dimensions[row].height = 42

def put(ws, r, c, v, font=F, fmt=None, fill=None):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font; cell.border = BOX
    if fmt: cell.number_format = fmt
    if fill: cell.fill = fill
    return cell

# ======================= Übersicht (filled at the end) =======================
wsU = wb.active; wsU.title = 'Übersicht'

# ======================= Parameter =======================
wsP = wb.create_sheet('Parameter')
wsP.column_dimensions['A'].width = 46; wsP.column_dimensions['B'].width = 14; wsP.column_dimensions['C'].width = 70
wsP['A1'] = 'Parameter der Auswertung (gelb = änderbar)'; wsP['A1'].font = FT
params = [
    (3, 'Referenzkunde MS – Leistung [kW]', 1000, 'Typischer Gewerbe-/Speicher-/Ladepark-Anschluss in der Mittelspannung'),
    (4, 'Referenzkunde MS – Benutzungsdauer [h/a]', 4000, '≥ 2.500 h → Tarifzone „hohe Benutzungsdauer"'),
    (6, 'Referenzkunde NS-RLM – Leistung [kW]', 100, 'Gewerbe mit Leistungsmessung in der Niederspannung'),
    (7, 'Referenzkunde NS-RLM – Benutzungsdauer [h/a]', 1600, '< 2.500 h → Tarifzone „niedrige Benutzungsdauer"'),
    (9, 'Referenzkunde HS – Leistung [kW]', 10000, 'Industrie/Rechenzentrum in der Hochspannung'),
    (10, 'Referenzkunde HS – Benutzungsdauer [h/a]', 6000, ''),
    (12, 'Grenze Benutzungsdauer [h/a]', 2500, 'StromNEV-Systematik: Jahresleistungspreissystem'),
    (14, 'Schwelle Kategorie „günstig" (Index ≤)', 0.33, 'Index = mittlerer Perzentilrang über alle verfügbaren Kennzahlen (0 = günstigster, 1 = teuerster)'),
    (15, 'Schwelle Kategorie „teuer" (Index >)', 0.67, ''),
    (16, 'Mindestanzahl Kennzahlen für Gesamtindex', 3, 'VNB mit weniger Kennzahlen erhalten keinen Gesamtindex'),
]
for r, lab, val, note in params:
    wsP.cell(row=r, column=1, value=lab).font = F
    c = wsP.cell(row=r, column=2, value=val); c.font = FIN; c.fill = YFILL; c.border = BOX
    wsP.cell(row=r, column=3, value=note).font = FGREY
P_MS, H_MS, P_NS, H_NS, P_HS, H_HS, H_LIM = 'Parameter!$B$3', 'Parameter!$B$4', 'Parameter!$B$6', 'Parameter!$B$7', 'Parameter!$B$9', 'Parameter!$B$10', 'Parameter!$B$12'
TH_LO, TH_HI, MINK = 'Parameter!$B$14', 'Parameter!$B$15', 'Parameter!$B$16'

# ======================= Netzentgelte =======================
wsN = wb.create_sheet('Netzentgelte')
wsN['A1'] = 'Netzentgelte Strom 2026 – Jahresleistungspreissystem (RLM), netto'; wsN['A1'].font = FT
wsN['A2'] = 'LP in €/kW·a, AP in ct/kWh. Blaue Zahlen = Werte aus dem Preisblatt des VNB (Quelle je Zeile). Referenzkunden-Kosten werden aus Blatt „Parameter" berechnet.'; wsN['A2'].font = FGREY
cols = ['VNB', 'Bundesland', 'Netztyp', 'Stand']
for lv in LEVELS:
    cols += [f'{lv}\nLP <2500h', f'{lv}\nAP <2500h', f'{lv}\nLP ≥2500h', f'{lv}\nAP ≥2500h']
cols += ['Ref. MS\n€/a', 'Ref. MS\nct/kWh', 'Ref. NS-RLM\nct/kWh', 'Ref. HS\nct/kWh', 'Quelle']
header(wsN, 4, cols, [34, 10, 8, 16] + [8.5] * 20 + [12, 10, 11, 10, 60])
def lvcol(lv, j):  # j: 0..3
    return 5 + LEVELS.index(lv) * 4 + j
ne_rows = {}
r = 5
for name in sorted(NE, key=lambda n: disp(n).lower()):
    v = NE[name]; dn = disp(name)
    put(wsN, r, 1, dn); put(wsN, r, 2, bl(name)); put(wsN, r, 3, typ(name)); put(wsN, r, 4, v.get('stand', ''))
    for lv in LEVELS:
        x = v.get(lv)
        for j in range(4):
            val = x[j] if x and x[j] is not None else None
            put(wsN, r, lvcol(lv, j), val, FIN, '0.00')
    def refc(lv, P, H):
        a, b, c_, d = [f'{L(lvcol(lv, j))}{r}' for j in range(4)]
        return (f'IF({H}>={H_LIM},IF(COUNT({c_},{d})<2,"",{c_}*{P}+{d}/100*{P}*{H}),'
                f'IF(COUNT({a},{b})<2,"",{a}*{P}+{b}/100*{P}*{H}))')
    cM = 25
    put(wsN, r, cM, '=' + refc('MS', P_MS, H_MS), F, '#,##0')
    put(wsN, r, cM + 1, f'=IF({L(cM)}{r}="","",{L(cM)}{r}/({P_MS}*{H_MS})*100)', F, '0.00')
    put(wsN, r, cM + 2, f'=IFERROR(({refc("NS", P_NS, H_NS)})/({P_NS}*{H_NS})*100,"")', F, '0.00')
    put(wsN, r, cM + 3, f'=IFERROR(({refc("HS", P_HS, H_HS)})/({P_HS}*{H_HS})*100,"")', F, '0.00')
    put(wsN, r, cM + 4, v.get('src', ''))
    ne_rows[dn] = r; r += 1
NE_LAST = r - 1
wsN.freeze_panes = 'E5'
wsN.cell(row=r + 1, column=1, value='Hinweise: wesernetz nur Zone ≥2.500 h, vorläufig 2026; Westfalen Weser Netz und Mainfranken vorläufig; WEMAG-Spaltenzuordnung aus Layout abgeleitet. Plausibilitätsprüfung LP≥ ≈ LP< + 2.500 h × (AP< − AP≥) für alle Zeilen bestanden (Abweichung < 3 €/kW).').font = FGREY

# ======================= BKZ =======================
wsB = wb.create_sheet('BKZ')
wsB['A1'] = 'Baukostenzuschuss (BKZ) 2026 in €/kW netto'; wsB['A1'].font = FT
wsB['A2'] = ('BNetzA-Positionspapier BK8 (11/2024): BKZ = Ø der Leistungspreise ≥2.500 h der letzten 5 Jahre der Anschlussebene. '
             'Wo kein BKZ veröffentlicht/gefunden: Proxy = LP ≥2.500 h 2026 der MS (Netzentgelte). Proxy = Einjahreswert, daher nur Näherung.'); wsB['A2'].font = FGREY
bcols = ['VNB', 'Bundesland', 'HS', 'HS/MS', 'MS', 'MS/NS', 'NS', 'Proxy MS\n(LP≥ 2026)', 'BKZ MS\nverwendet', 'Basis', 'Hinweis', 'Quelle']
header(wsB, 4, bcols, [34, 10, 9, 9, 9, 9, 9, 11, 11, 13, 50, 60])
bkz_names = {}
for n in BKZ: bkz_names.setdefault(disp(n), []).append(('B', n))
for n in NE: bkz_names.setdefault(disp(n), []).append(('N', n))
bkz_rows = {}
r = 5
msc = L(lvcol('MS', 2))
for dn in sorted(bkz_names, key=str.lower):
    srcs = bkz_names[dn]
    b = next((BKZ[n] for t, n in srcs if t == 'B'), None)
    some = srcs[0][1]
    put(wsB, r, 1, dn); put(wsB, r, 2, bl(some))
    for j, lv in enumerate(LEVELS):
        put(wsB, r, 3 + j, (b or {}).get(lv), FIN, '0.00')
    put(wsB, r, 8, f'=IFERROR(IF(INDEX(Netzentgelte!${msc}$5:${msc}${NE_LAST},MATCH(A{r},Netzentgelte!$A$5:$A${NE_LAST},0))="","",INDEX(Netzentgelte!${msc}$5:${msc}${NE_LAST},MATCH(A{r},Netzentgelte!$A$5:$A${NE_LAST},0))),"")', FLINK, '0.00')
    put(wsB, r, 9, f'=IF(ISNUMBER(E{r}),E{r},IF(ISNUMBER(H{r}),H{r},""))', F, '0.00')
    put(wsB, r, 10, f'=IF(ISNUMBER(E{r}),"veröffentlicht",IF(ISNUMBER(H{r}),"Proxy LP≥",""))')
    put(wsB, r, 11, (b or {}).get('note', ''))
    put(wsB, r, 12, (b or {}).get('src', ''))
    bkz_rows[dn] = r; r += 1
BKZ_LAST = r - 1
wsB.freeze_panes = 'C5'
wsB.cell(row=r + 1, column=1, value='Ohne eindeutige Ebenenzuordnung (nicht ausgewertet): EWE NETZ 71,71 / 71,27 / 31,03 €/kW; Pfalzwerke 58,47 / 109,82 / 111,76 / 109,27 / 102,06 €/kW. ÜNB-Referenz (Turn 1): HöS 96,91, HöS/HS 113,15 €/kW. Energienetze Mittelrhein in €/kVA (≈ €/kW bei cos φ = 1).').font = FGREY

# ======================= NAP Rohdaten =======================
wsR = wb.create_sheet('NAP_Rohdaten')
wsR['A1'] = 'Netzausbaupläne (NAP) nach § 14d EnWG – aggregierte Mengen & geschätzte Kosten je Netzebene und Zeitraum'; wsR['A1'].font = FT
wsR['A2'] = 'NAP 2026: T5 = 2025–2030, T10 = 2031–2035, Z = 2036–2045; nur netzdimensionierender Ausbau (ohne reinen 1:1-Ersatz). NAP 2024 nur als Fallback, wo der NAP 2026 für eine Netzebene keine Werte enthält (T5 = bis 2028, T10 = 2029–2033, inkl. Ersatz). Quelle: VNBdigital, NAP-Dokument je VNB.'; wsR['A2'].font = FGREY
header(wsR, 4, ['VNB', 'NAP-Bezeichnung', 'NAP-Datum', 'Netzebene', 'Zeitraum', 'Art', 'Menge', 'Einheit', 'Kosten\nMio. €', 'spez. Kosten', 'Einheit spez.', 'Ausgabe'],
       [34, 40, 11, 9, 9, 9, 10, 8, 10, 11, 12, 18])
r = 5
for ri, rec in enumerate(R):
    v, d, lvl, per, art, m, u, mio = rec
    put(wsR, r, 1, disp(v)); put(wsR, r, 2, v); put(wsR, r, 3, d); put(wsR, r, 4, lvl); put(wsR, r, 5, per); put(wsR, r, 6, art)
    put(wsR, r, 7, m, FIN, '#,##0.0'); put(wsR, r, 8, u); put(wsR, r, 9, mio, FIN, '#,##0.00')
    put(wsR, r, 10, f'=IF(G{r}>0,IF(H{r}="km",I{r}*1000/G{r},I{r}*1000/G{r}),"")', F, '#,##0')
    put(wsR, r, 11, f'=IF(H{r}="km","€/m",IF(H{r}="UW","T€/UW","T€/Stück"))')
    put(wsR, r, 12, EDN[ri])
    r += 1
RL = r - 1
wsR.freeze_panes = 'B5'
wsR.auto_filter.ref = f'A4:L{RL}'

# ======================= NAP Kennwerte =======================
wsK = wb.create_sheet('NAP_Kennwerte')
wsK['A1'] = 'NAP-Kostenkennwerte je VNB (Basis: Zeiträume T5+T10, d. h. bis 2035 im NAP 2026; nur wenn dort keine Mengen: Zielnetz-Zeitraum)'; wsK['A1'].font = FT
wsK['A2'] = 'Leitungen: €/m = Mio. € × 1.000 / km. ONS: T€ je Ortsnetzstation. UW: Mio. € je Umspannwerk-Standortmaßnahme (HöS/HS bzw. HS/MS, je nach NAP).'; wsK['A2'].font = FGREY
kcols = ['VNB', 'Bundesland', 'Netztyp']
blocks = [('MS', 'Leitung', 'km', 'MS-Leitungen'), ('NS', 'Leitung', 'km', 'NS-Leitungen'), ('HS', 'Leitung', 'km', 'HS-Leitungen'),
          ('MS/NS', 'Anlage', 'ONS', 'Ortsnetzstationen'), ('HS/MS', 'Anlage', 'UW', 'Umspannwerke HS/MS')]
for lv, art, u, lab in blocks:
    unitlab = '€/m' if u == 'km' else ('T€/ONS' if u == 'ONS' else 'Mio. €/UW')
    kcols += [f'{lab}\nMenge', f'{lab}\nMio. €', f'{lab}\n{unitlab}', f'{lab}\nBasis']
header(wsK, 4, kcols, [34, 10, 8] + [9, 9, 9, 9] * 5)
RA, RD, RE, RN, RG, RH, RI = [f'NAP_Rohdaten!${c}$5:${c}${RL}' for c in 'ADEFGHI']
nap_names = sorted({disp(rec[0]) for rec in R}, key=str.lower)
k_rows = {}
r = 5
for dn in nap_names:
    some = next(rec[0] for rec in R if disp(rec[0]) == dn)
    put(wsK, r, 1, dn); put(wsK, r, 2, bl(some)); put(wsK, r, 3, typ(some))
    for bi, (lv, art, u, lab) in enumerate(blocks):
        c0 = 4 + bi * 4
        crit = f'{RA},$A{r},{RN},"{art}",{RH},"{u}"' + (f',{RD},"{lv}"' if lv else '')
        qT = f'SUMPRODUCT(SUMIFS({RG},{crit},{RE},{{"T5","T10"}}))'
        qZ = f'SUMIFS({RG},{crit},{RE},"Z")'
        cT = f'SUMPRODUCT(SUMIFS({RI},{crit},{RE},{{"T5","T10"}}))'
        cZ = f'SUMIFS({RI},{crit},{RE},"Z")'
        m, c, s, b = [f'{L(c0 + j)}{r}' for j in range(4)]
        put(wsK, r, c0, f'=IF({qT}>0,{qT},IF({qZ}>0,{qZ},""))', F, '#,##0')
        put(wsK, r, c0 + 1, f'=IF({m}="","",IF({qT}>0,{cT},{cZ}))', F, '#,##0.0')
        fac = '1000' if u != 'UW' else '1'
        fmt = '#,##0' if u != 'UW' else '0.0'
        put(wsK, r, c0 + 2, f'=IF({m}="","",{c}*{fac}/{m})', F, fmt)
        put(wsK, r, c0 + 3, f'=IF({m}="","",IF({qT}>0,"T5+T10","Zielnetz"))')
    eds = sorted({EDN[i][:8] for i, rec in enumerate(R) if disp(rec[0]) == dn}, reverse=True)
    put(wsK, r, 24, ' + '.join(eds))
    k_rows[dn] = r; r += 1
K_LAST = r - 1
c = wsK.cell(row=4, column=24, value='Datenbasis'); c.font = FH; c.fill = HFILL; c.alignment = CEN
wsK.column_dimensions['X'].width = 20
wsK.freeze_panes = 'D5'

# ======================= Ranking =======================
wsG = wb.create_sheet('Ranking')
wsG['A1'] = 'Ranking: Wo sind Anschlüsse und Netzbau günstig, wo teuer? (Perzentilrang 0 = günstigster, 1 = teuerster VNB)'; wsG['A1'].font = FT
wsG['A2'] = ('Gesamtindex = Mittelwert der Perzentilränge aller verfügbaren Kennzahlen (MS-, NS-Leitung €/m, T€/ONS, Mio. €/UW, BKZ MS, Netzentgelt Ref. MS). '
             'Kennzahlen stammen per Formel aus den Blättern NAP_Kennwerte, BKZ, Netzentgelte.'); wsG['A2'].font = FGREY
all_names = sorted(set(nap_names) | set(ne_rows) | set(bkz_rows), key=str.lower)
gcols = ['VNB', 'Bundesland', 'BL (Schwer-\npunkt)', 'Netztyp',
         'MS-Leitung\n€/m', 'NS-Leitung\n€/m', 'HS-Leitung\n€/m', 'ONS\nT€/Stück', 'UW\nMio. €/UW', 'BKZ MS\n€/kW', 'BKZ-Basis',
         'Netzentgelt\nRef. MS ct/kWh', 'Netzentgelt\nRef. NS ct/kWh',
         'PR MS-Ltg', 'PR NS-Ltg', 'PR ONS', 'PR UW', 'PR BKZ', 'PR NNE MS', 'Anzahl\nKennzahlen', 'Gesamt-\nindex', 'Rang\n(1 = günstig)', 'Kategorie']
header(wsG, 4, gcols, [34, 11, 8, 8, 10, 10, 10, 10, 10, 9, 12, 12, 12, 8, 8, 8, 8, 8, 8, 9, 9, 9, 11])
G0 = 5; GL = G0 + len(all_names) - 1
def lk(sheet, col, last, r):
    rng = f"{sheet}!${col}$5:${col}${last}"; keyr = f"{sheet}!$A$5:$A${last}"
    return f'=IFERROR(IF(INDEX({rng},MATCH($A{r},{keyr},0))="","",INDEX({rng},MATCH($A{r},{keyr},0))),"")'
for i, dn in enumerate(all_names):
    r = G0 + i
    some = None
    for rec in R:
        if disp(rec[0]) == dn: some = rec[0]; break
    if some is None:
        for n in list(NE) + list(BKZ):
            if disp(n) == dn: some = n; break
    blv = bl(some)
    put(wsG, r, 1, dn); put(wsG, r, 2, blv); put(wsG, r, 3, PRIMARY_BL.get(blv, blv)); put(wsG, r, 4, typ(some))
    put(wsG, r, 5, lk('NAP_Kennwerte', L(6), K_LAST, r), FLINK, '#,##0')
    put(wsG, r, 6, lk('NAP_Kennwerte', L(10), K_LAST, r), FLINK, '#,##0')
    put(wsG, r, 7, lk('NAP_Kennwerte', L(14), K_LAST, r), FLINK, '#,##0')
    put(wsG, r, 8, lk('NAP_Kennwerte', L(18), K_LAST, r), FLINK, '#,##0')
    put(wsG, r, 9, lk('NAP_Kennwerte', L(22), K_LAST, r), FLINK, '0.0')
    put(wsG, r, 10, lk('BKZ', 'I', BKZ_LAST, r), FLINK, '0.0')
    put(wsG, r, 11, lk('BKZ', 'J', BKZ_LAST, r), FLINK)
    put(wsG, r, 12, lk('Netzentgelte', L(26), NE_LAST, r), FLINK, '0.00')
    put(wsG, r, 13, lk('Netzentgelte', L(27), NE_LAST, r), FLINK, '0.00')
    for j, src in enumerate([5, 6, 8, 9, 10, 12]):
        s = L(src)
        put(wsG, r, 14 + j, f'=IF(ISNUMBER({s}{r}),IF(COUNT({s}${G0}:{s}${GL})>1,PERCENTRANK({s}${G0}:{s}${GL},{s}{r}),""),"")', F, '0.00')
    put(wsG, r, 20, f'=COUNT(N{r}:S{r})', F, '0')
    put(wsG, r, 21, f'=IF(T{r}>={MINK},AVERAGE(N{r}:S{r}),"")', FB, '0.00')
    put(wsG, r, 22, f'=IF(ISNUMBER(U{r}),RANK(U{r},U${G0}:U${GL},1),"")', F, '0')
    put(wsG, r, 23, f'=IF(ISNUMBER(U{r}),IF(U{r}<={TH_LO},"günstig",IF(U{r}>{TH_HI},"teuer","mittel")),"")')
    # hidden helper cols for Top/Flop (value + tiny tie-break)
    for j, src in enumerate([5, 6, 8, 9, 10, 12, 21]):
        s = L(src)
        c = wsG.cell(row=r, column=26 + j, value=f'=IF(ISNUMBER({s}{r}),{s}{r}+ROW()/1000000000,"")'); c.font = F
for j in range(7):
    wsG.column_dimensions[L(26 + j)].hidden = True
wsG.freeze_panes = 'B5'
wsG.auto_filter.ref = f'A4:W{GL}'
for col in ['E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'U']:
    wsG.conditional_formatting.add(f'{col}{G0}:{col}{GL}', ColorScaleRule(start_type='percentile', start_value=0, start_color='63BE7B',
                                   mid_type='percentile', mid_value=50, mid_color='FFEB84', end_type='percentile', end_value=100, end_color='F8696B'))
wsG.conditional_formatting.add(f'W{G0}:W{GL}', CellIsRule(operator='equal', formula=['"günstig"'], fill=PatternFill('solid', fgColor='C6EFCE')))
wsG.conditional_formatting.add(f'W{G0}:W{GL}', CellIsRule(operator='equal', formula=['"teuer"'], fill=PatternFill('solid', fgColor='FFC7CE')))
wsG.cell(row=GL + 2, column=1, value='PR = Perzentilrang innerhalb der VNB mit Wert (PERCENTRANK). Leere Zelle = keine Angabe im NAP/Preisblatt bzw. nicht abrufbar. Gesamtindex nur ab Mindestanzahl Kennzahlen (Parameter!B16).').font = FGREY

# ======================= Top/Flop =======================
wsT = wb.create_sheet('Top_Flop')
wsT['A1'] = 'Die 10 günstigsten und 10 teuersten VNB je Kennzahl (dynamisch aus Blatt „Ranking")'; wsT['A1'].font = FT
metrics = [('MS-Leitung €/m', 26, '#,##0'), ('NS-Leitung €/m', 27, '#,##0'), ('ONS T€/Stück', 28, '#,##0'), ('UW Mio. €/UW', 29, '0.0'),
           ('BKZ MS €/kW', 30, '0.0'), ('Netzentgelt Ref. MS ct/kWh', 31, '0.00'), ('Gesamtindex', 32, '0.00')]
row0 = 3
for mi, (lab, hc, fmt) in enumerate(metrics):
    base = row0 + mi * 14
    h = f'Ranking!${L(hc)}${G0}:${L(hc)}${GL}'
    nm = f'Ranking!$A${G0}:$A${GL}'
    blr = f'Ranking!$B${G0}:$B${GL}'
    for side, c0, fn in [('günstigste', 1, 'SMALL'), ('teuerste', 6, 'LARGE')]:
        t = wsT.cell(row=base, column=c0, value=f'{lab} – {side}'); t.font = FB; t.fill = SFILL
        for j, hl in enumerate(['#', 'VNB', 'BL', 'Wert']):
            c = wsT.cell(row=base + 1, column=c0 + j, value=hl); c.font = FH; c.fill = HFILL
        for k in range(1, 11):
            rr = base + 1 + k
            wsT.cell(row=rr, column=c0, value=k).font = F
            v = f'{fn}({h},{k})'
            wsT.cell(row=rr, column=c0 + 1, value=f'=IFERROR(INDEX({nm},MATCH({v},{h},0)),"")').font = F
            wsT.cell(row=rr, column=c0 + 2, value=f'=IFERROR(INDEX({blr},MATCH({v},{h},0)),"")').font = F
            c = wsT.cell(row=rr, column=c0 + 3, value=f'=IFERROR(ROUND({v},4),"")'); c.font = F; c.number_format = fmt
for c, w in zip('ABCDEFGHI', [4, 34, 10, 10, 3, 4, 34, 10, 10]):
    wsT.column_dimensions[c].width = w

# ======================= Bundesländer =======================
wsL = wb.create_sheet('Bundesländer')
wsL['A1'] = 'Regionale Auswertung nach Bundesland (Schwerpunkt-Bundesland des VNB)'; wsL['A1'].font = FT
wsL['A2'] = 'Ungewichtete Mittelwerte über die VNB mit Wert. Flächen-VNB über mehrere Länder: Westnetz → NW, MITNETZ → ST, E.DIS → BB.'; wsL['A2'].font = FGREY
BLN = [('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'), ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'),
       ('MV', 'Mecklenburg-Vorpommern'), ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'), ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'),
       ('SN', 'Sachsen'), ('ST', 'Sachsen-Anhalt'), ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen')]
header(wsL, 4, ['Kürzel', 'Bundesland', 'Anzahl VNB', 'Ø MS-Leitung\n€/m', 'Ø NS-Leitung\n€/m', 'Ø ONS\nT€/Stück', 'Ø BKZ MS\n€/kW', 'Ø Netzentgelt\nRef. MS ct/kWh', 'Ø Gesamt-\nindex', 'Rang Index\n(1 = günstig)'],
       [8, 26, 10, 12, 12, 11, 11, 14, 10, 11])
crit = f'Ranking!$C${G0}:$C${GL}'
for i, (k, n) in enumerate(BLN):
    r = 5 + i
    put(wsL, r, 1, k); put(wsL, r, 2, n)
    put(wsL, r, 3, f'=COUNTIF({crit},A{r})', F, '0')
    for j, col in enumerate(['E', 'F', 'H', 'J', 'L', 'U']):
        rng = f'Ranking!${col}${G0}:${col}${GL}'
        fmt = '0.00' if col in 'LU' else '#,##0'
        put(wsL, r, 4 + j, f'=IFERROR(AVERAGEIFS({rng},{crit},$A{r}),"")', F, fmt)
    put(wsL, r, 10, f'=IF(ISNUMBER(I{r}),RANK(I{r},$I$5:$I$20,1),"")', F, '0')
for col in 'DEFGHI':
    wsL.conditional_formatting.add(f'{col}5:{col}20', ColorScaleRule(start_type='min', start_color='63BE7B', mid_type='percentile', mid_value=50,
                                   mid_color='FFEB84', end_type='max', end_color='F8696B'))
wsL.cell(row=22, column=1, value='Achtung: in einigen Ländern nur 1–2 VNB mit Daten (siehe Spalte C) – dort ist der Ländermittelwert ein Einzelwert.').font = FGREY

# ======================= Quellen =======================
wsQ = wb.create_sheet('Quellen')
wsQ['A1'] = 'Quellen'; wsQ['A1'].font = FT
header(wsQ, 3, ['VNB', 'Datenart', 'Stand', 'Quelle / Fundstelle'], [36, 16, 14, 110])
r = 4
for name in sorted(NE, key=lambda n: disp(n).lower()):
    put(wsQ, r, 1, disp(name)); put(wsQ, r, 2, 'Netzentgelte 2026'); put(wsQ, r, 3, NE[name].get('stand', '')); put(wsQ, r, 4, NE[name].get('src', '')); r += 1
for name in sorted(BKZ, key=lambda n: disp(n).lower()):
    put(wsQ, r, 1, disp(name)); put(wsQ, r, 2, 'BKZ 2026'); put(wsQ, r, 3, BKZ[name].get('stand', '')); put(wsQ, r, 4, BKZ[name].get('src', '')); r += 1
seen = set()
for ri, rec in enumerate(R):
    sk = (disp(rec[0]), EDN[ri])
    if sk in seen: continue
    seen.add(sk)
    is26 = EDN[ri] == 'NAP 2026'
    s = (NAPSRC26 if is26 else NAPSRC).get(key(rec[0]), '')
    put(wsQ, r, 1, disp(rec[0])); put(wsQ, r, 2, 'Netzausbauplan 2026' if is26 else 'Netzausbauplan 2024 (Fallback)'); put(wsQ, r, 3, rec[1])
    put(wsQ, r, 4, 'VNBdigital (vnbdigital.de) – Netzausbauplan nach § 14d EnWG, aggregierte Tabellen' + (f'; Datei: https://www.vnbdigital.de/gateway/files?serviceName=vnb&fileId={s}' if s else '')); r += 1
r += 1
for t in ['BNetzA BK8: Positionspapier zur Erhebung von Baukostenzuschüssen (11/2024) – Leistungspreismodell.',
          'BGH, Beschl. v. 15.07.2025 – EnVR 1/24 (BKZ auch für Batteriespeicher zulässig).',
          '§ 14d EnWG (Netzausbaupläne der Verteilernetzbetreiber), § 17 StromNEV (Jahresleistungspreissystem, Grenze 2.500 h).']:
    wsQ.cell(row=r, column=1, value=t).font = F; r += 1

# ======================= Übersicht =======================
ws = wsU
ws.column_dimensions['A'].width = 130
ws['A1'] = 'Netzanschluss & Netzausbau in Deutschland – wo günstig, wo teuer?'; ws['A1'].font = FT
lines = [
    ('Fragestellung', FB),
    ('Vergleich der Kosten für Anschlüsse und Netzbau zwischen deutschen Verteilnetzbetreibern (VNB) anhand dreier Kostenarten: '
     '(1) Kostenkennwerte aus den Netzausbauplänen (NAP, § 14d EnWG), (2) Baukostenzuschüsse (BKZ) 2026, (3) Netzentgelte 2026.', F),
    ('', F),
    ('Aufbau der Datei', FB),
    ('Ranking – alle Kennzahlen je VNB, Perzentilränge, Gesamtindex & Kategorie (Farbskala grün = günstig, rot = teuer).', F),
    ('Top_Flop – je Kennzahl die 10 günstigsten und 10 teuersten VNB.   Bundesländer – Ländermittelwerte.', F),
    ('NAP_Kennwerte / NAP_Rohdaten – Mengen & Kosten aus den NAP-Tabellen.   BKZ / Netzentgelte – Preisblattwerte.   Parameter – Referenzkunden & Schwellen (gelb, änderbar).', F),
    ('Farbcode: blau = aus Quelle übernommene Eingabewerte, grün = Verweis auf anderes Blatt, schwarz = Formel.', F),
    ('', F),
    ('Wichtigste Ergebnisse (Stand der Datenerhebung 6. Nov. 2026)', FB),
]
for t in FIND.strip().split('\n'):
    if t.strip(): lines.append((t.strip(), F))
lines += [
    ('', F),
    ('Methodik & Grenzen', FB),
    ('• NAP-Kennwerte = geschätzte Gesamtkosten ÷ Menge je Netzebene (Zeiträume T5+T10 gepoolt, Basis NAP 2026 vom Okt./Nov. 2026 mit netzdimensionierendem Ausbau ohne reinen Ersatz; NAP 2024 nur als Fallback je Netzebene). Die VNB grenzen weiterhin unterschiedlich ab (Trassen- vs. Stromkreis-km, UW- vs. Trafo-Zählung, Rundungen) – Kennwerte sind daher Indikatoren, keine Ausschreibungspreise.', F),
    ('• Städtische Netze haben strukturell höhere €/m (Tiefbau, Oberflächen, Mehrfachkabel), ländliche Flächennetze niedrigere – deshalb Spalte „Netztyp" zum Filtern.', F),
    ('• BKZ folgt seit 2025 dem BNetzA-Leistungspreismodell (Ø LP ≥2.500 h über 5 Jahre); wo kein BKZ auffindbar war, wird der LP ≥2.500 h 2026 als Proxy genutzt (gekennzeichnet).', F),
    ('• Netzentgelte: Referenzkunde MS 1 MW / 4.000 h, NS-RLM 100 kW / 1.600 h (änderbar). Ohne Umlagen, Konzessionsabgabe, Messstellenbetrieb, USt.', F),
    ('• Abdeckung: NAP-pflichtige VNB (> 100.000 Kunden) mit auswertbarer Tabelle; Preisblätter einiger großer VNB (u. a. E.DIS, SH Netz, MITNETZ, Syna, LEW, Stromnetz Hamburg) waren nicht maschinell abrufbar und fehlen bei den Netzentgelten.', F),
]
for i, (t, f) in enumerate(lines):
    c = ws.cell(row=3 + i, column=1, value=t); c.font = f; c.alignment = Alignment(wrap_text=True, vertical='top')

for w in wb.worksheets:
    w.sheet_view.zoomScale = 90
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Netzkosten_Auswertung_Deutschland.xlsx')
wb.save(out); print(out, len(all_names), 'VNB', len(R), 'NAP-Zeilen')
