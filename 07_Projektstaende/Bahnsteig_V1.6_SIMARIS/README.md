# Bahnsteig 50 Hz Elektroplanung - V1.6 SIMARIS

Stand 04.11.2026. Gesicherte Arbeitsprobe mit einem tatsächlich ausgeführten SIMARIS-Netzlauf. Die technische Gesamtplanung ist wegen fehlender realer Grundlagen weiterhin nicht abgeschlossen.

## Aktueller Einstieg

1. `09_SIMARIS/SIMARIS_V16_Netzansichten_Lesefassung.pdf`: drei vergrößerte Ausschnitte der nativen Geräte-, Lastfluss- und Kurzschlussansicht für das Gespräch. Original mit Schriftfeld unverändert unter `Nativer_Export/Bahnsteig_V16_SIMARIS.pdf` (5 Seiten).
2. `09_SIMARIS/SIMARIS_V16_Nativer_Berechnungsbericht.pdf`: echte SIMARIS-Projektdokumentation, 12 Seiten, aus dem nativen RTF über Word als PDF gespeichert.
3. `09_SIMARIS/SIMARIS_V16_Native_Selektivitaet.pdf`: echter Kennlinienexport, 5 Seiten. Die Bewertungsfelder sind leer; kein bestätigter Gesamtselektivitätsnachweis.
4. `09_SIMARIS/Bahnsteig_V16_SIMARIS.sdx`: bearbeitbares Rechenprojekt; `.sx` ist der zusätzliche Austauschstand. `SIMARIS_V16_Netzplan.dwg` ist der native CAD-Export der Kurzschlussansicht, in BricsCAD V26 tatsächlich geöffnet.
5. `09_SIMARIS/SIMARIS_ERGEBNISSE.md`: Annahmen, echte Auswahl, Ergebnisse, Vergleich mit V1.5 und offene Nachweise. `SIMARIS_Ergebnisvergleich.csv` ist die aktuelle kompakte Ergebnistabelle.
6. `BERICHT_GRUNDLAGE.md` und `VORSTELLUNGSGESPRAECH.md`: deutsche Grundlage und kurzer Ablauf für die spätere Vorstellung.

## Ergebnis und Einordnung

Zwei native Ersatzlasten A/B mit je 102 W, je sechs vorhandenen Leuchten zugeordnet. SIMARIS design 27.0.1 dimensionierte das Modell; Messages [0]. Kumulativer Spannungsfall A/B 0,596 / 0,649 %. Minimaler L-PE-/L-N-Fehlerstrom am Endpunkt 59,029 / 54,374 A. Dies sind bestätigte Modellergebnisse bei angenommenen Netzdaten.

Autoauswahl: Einspeisesicherung 25 A gG; Abgänge B1 A, 10 kA, mit je einem RCD Typ A, 25 A / 30 mA. Diese Geräte sind Kandidaten, nicht zur Ausführung freigegeben. Besonders offen: Quellenbemessung 20 A gegenüber automatisch gewählter 25-A-Sicherung, LED-Einschaltstrom, reale Verlegung, Selektivität und Bahn-PA/SPD.

## Erhaltene Licht- und CAD-Planung

Die zwölf Relux-Leuchten, RDF, Lageplan, Überdachung und ursprünglichen Sicherungen bleiben bytegleich zu V1.5. 120 x 4 m Bahnsteig, Dach X45 bis X75, 8 x 18,5 W + 4 x 14 W = 204 W. Relux-Ergebnis Em 18,1 lx, Emin 7,96 lx, Emax 37 lx, U0 0,44. Kein neuer Geometrieeingriff und deshalb keine neue Lichtrechnung in V1.6.

`02_CAD` und `08_Webberechnung` enthalten bewusst auch die älteren V1.3-/V1.5-Zeichnungen und ELEK-Ergebnisse. Deren B20/B6-Entwurf ist HISTORISCH und entspricht nicht der neuen SIMARIS-Auswahl. Die aktuellen elektrischen Daten stehen unter `09_SIMARIS`; die historischen Dateien wurden nicht umgeschrieben. Auch die bisherigen XLSX-Dateien sind historische Modellvergleiche.

## Qualität, Kosten und Fortsetzung

Verified / Preliminary / Missing sind in `PRUEFSTATUS.csv` getrennt. `PRUEFPROTOKOLL.json` enthält die tatsächlich ausgeführten Dateiprüfungen. SHA256-Manifest erlaubt den späteren Bytevergleich. Keine zusätzliche Zahlung und kein kostenpflichtiger ELEK-/SIMARIS-Professional-Plan aktiviert. SIMARIS wurde mit der vom Benutzer freigegebenen Installation bereitgestellt. Quellen und verwendete Skills: `QUELLEN.md`.

Für die Fortsetzung zuerst `FORTSETZUNG.md` lesen. Kein Neuaufbau der zwölf Relux-Leuchten erforderlich.
