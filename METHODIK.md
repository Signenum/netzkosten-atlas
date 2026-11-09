# Methodik

## 1. Netzausbau-Kennwerte (Netzausbaupläne)

Quelle sind die Netzausbaupläne (NAP) nach § 14d EnWG, veröffentlicht auf VNBdigital. Grundlage ist der **NAP 2026** (Veröffentlichung Oktober/November 2026) mit der Standardtabelle je Netzebene:

| Netzebene | Art | Einheit |
|---|---|---|
| HS (110 kV) | Leitung | km |
| HS/MS | Umspannwerk | Anzahl |
| MS | Leitung | km |
| MS/NS | Ortsnetzstation | Anzahl |
| NS | Leitung | km |

Zeiträume: T5 = 2025–2030, T10 = 2031–2035, Z = 2036–2045. Der NAP 2026 enthält nur **netzdimensionierenden Ausbau** (ohne reinen 1:1-Ersatz).

Kennwert je VNB und Netzebene:

- Leitungen: `€/m = Σ Mio. € × 1.000 ÷ Σ km` über T5 + T10 (bis 2035). Nur wenn dort keine Mengen stehen, wird der Zielnetz-Zeitraum Z verwendet.
- Ortsnetzstationen: `T€ je Station`, Umspannwerke: `Mio. € je Standortmaßnahme`.

Wo ein Netzbetreiber im NAP 2026 für eine Netzebene keine Werte ausweist, wird je Netzebene der **NAP 2024** als Fallback verwendet (in den Daten als „NAP 2024 (Fallback)“ markiert). Die Netzbetreiber grenzen unterschiedlich ab (Trassen- vs. Stromkreis-km, Umspannwerke vs. Transformatoren, Rundung). Die Kennwerte sind daher Indikatoren, keine Ausschreibungspreise.

## 2. Netzentgelte

Aus den Preisblättern der Netzbetreiber (Jahresleistungspreissystem für Entnahme mit Leistungsmessung), je Netzebene: Leistungspreis (LP) und Arbeitspreis (AP), jeweils unter und ab 2.500 Benutzungsstunden.

Plausibilitätsprüfung jedes Werts: `LP≥ ≈ LP< + 2.500 h × (AP< − AP≥)` (Stetigkeit bei 2.500 h nach StromNEV, Anlage 4).

Referenzkunden (netto, ohne Umlagen, Konzessionsabgabe, Stromsteuer, USt.):

- **MS**: 1 MW, 4.000 h/a → `ct/kWh = LP≥ ÷ 40 + AP≥`
- **NS mit Leistungsmessung**: 100 kW, 1.600 h/a → Tarif unter 2.500 h

2026 ist durch den Bundeszuschuss zu den Übertragungsnetzkosten (6,5 Mrd. €) gesenkt. Die Werte für 2027 stammen aus den vorläufigen Preisblättern vom 15.10.2026; der Zuschuss soll 2027 auf rund 5,5 Mrd. € sinken.

## 3. Baukostenzuschuss (BKZ)

Verwendet wird der veröffentlichte BKZ für die Mittelspannung (Stand 2026). Wo keiner veröffentlicht ist, dient der **Leistungspreis ≥ 2.500 h 2026 der Mittelspannung** als Proxy. Hintergrund: Nach dem BNetzA-Positionspapier (BK8, November 2024) ergibt sich der BKZ oberhalb der Niederspannung aus dem Durchschnitt dieses Leistungspreises der letzten fünf Jahre. Bei Netzbetreibern mit beiden Werten liegt der veröffentlichte BKZ im Median etwa auf Höhe des Leistungspreises 2026, im Einzelfall aber beim 0,5- bis 1,4-Fachen.

## 4. Gesamtindex

Für jede Kennzahl (MS-Leitung, NS-Leitung, Ortsnetzstation, Umspannwerk, BKZ MS, Netzentgelt MS) wird der Perzentilrang innerhalb aller VNB mit Wert gebildet (0 = günstigster, 1 = teuerster). Der Gesamtindex ist der Mittelwert der verfügbaren Perzentilränge, nur bei mindestens drei Kennzahlen. Kategorie: ≤ 0,33 günstig, > 0,67 teuer. Bundeslandwerte sind ungewichtete Mittel.

## 5. Netzgebiete

Es gibt keinen offenen, bundesweiten Datensatz der Netzgebietsgrenzen. Die Karte nähert die **Mittelspannungs-Netzgebiete** auf Gemeindeebene:

1. Abfrage bei VNBdigital, welcher Netzbetreiber an einem Punkt die Mittelspannung betreibt, für ein Raster von 0,06° × 0,09° (ca. 6,7 × 6,3 km) über Deutschland und zusätzlich für einen Punkt in jeder Gemeinde ab 20.000 Einwohnern (insgesamt rund 9.400 Punkte, November 2026).
2. Jede Gemeinde (VG250-EW, BKG) wird dem Netzbetreiber mit den meisten Treffern zugeordnet. Gemeinden ohne Rasterpunkt erhalten den Netzbetreiber des nächstgelegenen Punkts.
3. Die Gemeinden werden je Netzbetreiber zu einer Fläche zusammengefasst und vereinfacht.

Folgen: Gemeinden, die sich mehrere Netzbetreiber teilen, erscheinen nur beim überwiegenden; kleine Netzgebiete unterhalb der Rasterweite können fehlen. Die Zuordnung je Gemeinde steht in `data/gemeinde_vnb.csv`.

## 6. Aktualisierung

`src/` enthält die Skripte:

- `nap26_data.py`, `nap_data.py`: aus den NAP-Dokumenten übertragene Werte (2026 bzw. 2024)
- `ne25.json`, `ne.json`, `ne27.json`, `bkz.json`: Preisblatt-Werte mit Quelle und Stand
- `build_eval.py`: erzeugt die Excel-Auswertung
- `add_nne_sheet.py`: Blatt „NNE_Entwicklung“
- `build_geo.py`: Netzgebiete aus Stichproben und Gemeindegrenzen
- `export_map.py` + `map_template.html`: erzeugt `index.html`
