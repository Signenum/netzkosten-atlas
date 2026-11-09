import os
import json,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meta import key,META
from openpyxl import load_workbook
from openpyxl.styles import Font,PatternFill
D = os.path.dirname(os.path.abspath(__file__)) + '/'
f=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Netzkosten_Auswertung_Deutschland.xlsx'); wb=load_workbook(f)
if 'NNE_Entwicklung' in wb.sheetnames: del wb['NNE_Entwicklung']
ws=wb.create_sheet('NNE_Entwicklung')
ws['A1']='Netzentgelte (Jahresleistungspreissystem, RLM) 2025 → 2026 → 2027 vorläufig'; ws['A1'].font=Font(bold=True,size=13)
ws['A2']='Referenz = LP≥2500/40 + AP≥2500 (1 MW, 4.000 h) in ct/kWh. 2026 inkl. Bundeszuschuss ÜNB-Kosten (6,5 Mrd. €); 2027 vorläufig (15.10.2026), Zuschuss ca. 5,5 Mrd. €.'
H=['VNB','Netzebene','Jahr','LP<2500 €/kW·a','AP<2500 ct/kWh','LP≥2500 €/kW·a','AP≥2500 ct/kWh','Referenz ct/kWh','Stand','Quelle']
for i,h in enumerate(H,1):
    c=ws.cell(4,i,h); c.font=Font(bold=True,color='FFFFFF'); c.fill=PatternFill('solid',fgColor='1F5F55')
r=5
for yr,fn in (('2025','ne25.json'),('2026','ne.json'),('2027 vorl.','ne27.json')):
    for n,v in json.load(open(D+fn)).items():
        for ne in ('HS','HS/MS','MS','MS/NS','NS'):
            t=v.get(ne)
            if not isinstance(t,list): continue
            ws.append([META[key(n)][0],ne,yr,*t,f'=F{r}/40+G{r}',v.get('stand',''),v.get('src','')]); r+=1
L=r-1
ws.cell(4,12,'Übersicht MS – Referenz ct/kWh').font=Font(bold=True)
for i,h in enumerate(['VNB','2025','2026','2027 vorl.','Δ 25→26','Δ 26→27'],12): ws.cell(5,i,h).font=Font(bold=True)
names=sorted({META[key(n)][0] for n in json.load(open(D+'ne.json'))},key=str.lower)
for j,n in enumerate(names,6):
    ws.cell(j,12,n)
    for k,yr in enumerate(['2025','2026','2027 vorl.']):
        ws.cell(j,13+k,f'=IFERROR(AVERAGEIFS($H$5:$H${L},$A$5:$A${L},$L{j},$B$5:$B${L},"MS",$C$5:$C${L},"{yr}"),"")').number_format='0.00'
    ws.cell(j,16,f'=IF(OR(M{j}="",N{j}=""),"",N{j}/M{j}-1)').number_format='+0%;-0%'
    ws.cell(j,17,f'=IF(OR(N{j}="",O{j}=""),"",O{j}/N{j}-1)').number_format='+0%;-0%'
for c in 'DEFGH':
    for row in ws[f'{c}5:{c}{L}']: row[0].number_format='0.00'
for col,w in zip('ABCDEFGHIJKLMNOPQ',[30,8,10,10,10,10,10,10,18,40,2,30,8,8,10,9,9]): ws.column_dimensions[col].width=w
wb.save(f); print('nne sheet',L-4)
