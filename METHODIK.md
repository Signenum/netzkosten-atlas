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

1. Abfrage bei VNBdigital, welcher Netzbetreiber an einem Punkt die Mittelspannung betreibt, für ein Raster von 0,06° × 0,09° (ca. 6,7 × 6,3 km) über Deutschland, zusätzlich für einen Punkt in jeder Gemeinde ab 20.000 Einwohnern (rund 9.400 Punkte) und – seit Überarbeitung im November 2026 – für einen inneren Punkt in **jeder** Gemeinde (10.978) sowie drei weitere, möglichst weit verteilte Punkte in Gemeinden, deren Zuordnung beim Abgleich unsicher war (insgesamt rund 24.000 Punkte).
2. Jede Gemeinde (VG250-EW, BKG) wird dem Netzbetreiber mit den meisten gewichteten Treffern zugeordnet (innerer Gemeindepunkt ×4, Zusatzpunkte ×2, Rasterpunkte ×1). Nur wo VNBdigital für keinen Punkt der Gemeinde einen Mittelspannungsbetreiber liefert (rund 165 Gemeinden), gilt der nächstgelegene Punkt.
3. Die Gemeinden werden je Netzbetreiber zu einer Fläche zusammengefasst und vereinfacht.

Folgen: Gemeinden, die sich mehrere Netzbetreiber teilen, erscheinen nur beim überwiegenden; Netzgebiete, die nur Teile einer Gemeinde umfassen, können fehlen. Als Plausibilitätsprüfung diente die gemeindescharfe MaStR-Auswertung im Energiewende-Dashboard von Mathias Bock (energiewende-dashboard.org); deren Daten sind nicht übernommen, sie dienten nur dazu, Gemeinden für zusätzliche Abfragen auszuwählen. Die Zuordnung je Gemeinde steht in `data/gemeinde_vnb.csv`.

## 6. Aktualisierung

`src/` enthält die Skripte:

- `nap26_data.py`, `nap_data.py`: aus den NAP-Dokumenten übertragene Werte (2026 bzw. 2024)
- `ne25.json`, `ne.json`, `ne27.json`, `bkz.json`: Preisblatt-Werte mit Quelle und Stand
- `build_eval.py`: erzeugt die Excel-Auswertung
- `add_nne_sheet.py`: Blatt „NNE_Entwicklung“
- `prep_vg250.py`: bereitet die VG250-Gemeinden vor (aus [dimfalk/vg250](https://github.com/dimfalk/vg250), `data/vg250.rda`)
- `geo/stichproben_raw.txt` + `geo/decode_raw.py`: Ergebnisse der VNBdigital-Abfrage (Raster + Stützpunkte, Netzbetreiber-IDs) → `res.json`, `names.json`
- `geo/res_gem.json`: Ergebnisse der Gemeindeabfrage (Nov. 2026): `r<i>` innerer Punkt der Gemeinde i (Reihenfolge wie `gem.pkl`), `e<i>_<k>` Zusatzpunkte; Werte = VNBdigital-IDs, mehrere mit `|`
- `geo/vnbmap.json`: geprüfte Zuordnung VNBdigital-ID → Netzbetreiber im Atlas
- `build_geo.py`: Netzgebiete aus Stichproben und Gemeindegrenzen
- `export_csv.py`: CSV-Dateien in `data/`
- `fehlliste.py`: Liste fehlender Preisblätter
- `export_map.py` + `map_template.html`: erzeugt `index.html`

Reihenfolge: `prep_vg250.py` → `geo/decode_raw.py` → `build_geo.py` → `build_eval.py` → `add_nne_sheet.py` → Excel-Formeln neu berechnen (z. B. LibreOffice) → `export_map.py` → `export_csv.py`. Benötigt Python 3.11+ mit pandas, openpyxl, shapely, numpy (und rdata für `prep_vg250.py`).
