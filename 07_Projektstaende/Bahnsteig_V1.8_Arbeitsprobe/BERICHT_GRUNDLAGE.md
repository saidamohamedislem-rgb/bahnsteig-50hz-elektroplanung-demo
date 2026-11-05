# Bericht-Grundlage - Bahnsteig 50 Hz Elektroplanung

Mohamed Saida. V1.8, 05.11.2026. Stichpunktartige Materialsammlung für den späteren Bericht.

## Zielsetzung

Fiktive Arbeitsprobe für das Vorstellungsgespräch. Den Zusammenhang von Geometrie, Leuchten, Lichtberechnung, A/B-Stromkreisen, Netzrechnung und Dokumentation nachvollziehbar zeigen. Kein realer Bauauftrag; Messungen vor Ort sind für diesen Lernzweck nicht erforderlich.

## Ausgangssituation

Vorhandene V1.2-Relux-Datei mit zwölf Leuchten und bestehende CAD-Grundlagen. Originale gesichert. V1.3 ergänzt die koordinierte Stützen-/Trägergeometrie und enthält die neu berechnete Lichtausgabe. ELEK V1.5 ist ein historischer Vergleich. V1.6/V1.7 liefern das native SIMARIS-Ersatzlastmodell und die Formelmappe. V1.8 stellt aktuelle benannte Ausgaben und den Detailstromlaufplan zusammen.

## Planungsgrundlagen

- Bahnsteig 120 × 4 m, globale Koordinaten in Metern. Dach X45 bis X75, Y-0,5 bis Y4,5, Z4,75 bis Z5,00.
- Leuchten X5,15,...,115; Y2. L05 bis L08 Z4,3, übrige Z4,5. Achtmal 18,5 W und viermal 14 W, insgesamt 204 W.
- A: L01/03/05/07/09/11; B: L02/04/06/08/10/12. Je 102 W. A auf L1-N, B auf L2-N. Gemeinsame Einspeisung bleibt gemeinsamer Ausfallpunkt.
- Netzannahme 400/230 V, TN-S, 50 Hz, Ik1/Ik3 min 1,5 kA / max 3 kA, cos phi Last 0,95. Keine behaupteten Netzbetreiberwerte.

## Vorgehensweise

Originale erhalten, nur separate Arbeitsversionen bearbeiten. Im Relux-Modell ausschließlich die zusätzliche Stützen-/Trägergeometrie übernehmen, ohne Boden und Dach zu duplizieren. Leuchten unverändert lassen. Licht nach Geometrieergänzung rechnen, Tabellen/Isolux/False Colours nativ ausgeben. Elektrisches A/B-Ersatznetz in SIMARIS dimensionieren. Daneben 24 Leitungsabschnitte mit verteilten Lasten als nachvollziehbare Referenz berechnen. Die beiden Methoden und ihre Grenzen getrennt erläutern. Dateistände, Ergebnisquellen und Hashmanifest sichern.

## Software

ReluxDesktop 2026.2; BricsCAD V26; SIMARIS design 27.0.1, Subrevision 2267; Word für PDF-Ausgabe der nativen RTFs; bearbeitbare XLSX für Abschnittsrechnung; PowerShell/Python für Datenabgleich und Ablage; Git/GitHub für Versionierung. Kein neuer kostenpflichtiger Plan aktiviert.

## Leuchtenauswahl

Bestehende Schmidt-Strahl-LDT-Auswahl: acht 18,5-W-Leuchten mit BB-Optik und vier 14-W-Leuchten, 4000 K laut vorhandenen Daten. Produkt-/Treiberfreigabe wird nicht behauptet. Das zusätzlich in der Relux-Bibliothek enthaltene 17-W-Datenblatt gehört nicht zur installierten Liste.

## Lichtberechnung

Exterior 2, Floor (E), Wartungsfaktor 0,8. Native Ergebnisse: Em 18,1 lx, Emin 7,96 lx, Emax 37 lx, U0 0,44. Belege im Relux-Gesamtbericht: Leuchten S.5, Grundriss S.6, Raster S.7-15, Isolux S.16, 3D S.17, False Colours S.18. Die Bild- und Tabellenansichten bleiben zusätzlich einzeln erhalten. Keine neue Lichtrechnung in V1.8, weil keine lichtwirksame Geometrieänderung vorgenommen wurde.

## Elektroplanung

SIMARIS enthält zwei gebündelte 102-W-Endlasten. Zuleitung 10 m Cu/PVC70, L/N/PE 4 mm²; Abgänge 109,7 / 119,7 m mit L/N/PE 1,5 mm², Verlegeart C, Gesamtfaktor 1. Tatsächliche Einstellungen: Standard IEC, Gerätetemperatur 45 °C, Leitertemperatur Spannungsfall 55 °C, Software-Netzgrenze 8 %, balanced-Lastfluss. Keine pauschale DIN/VDE-/Bahn-Konformität.

Autoauswahl: gG25 3NA3810 / Sockel 3NH4030; je B1 A, Icn 10 kA, 5SY41016 und RCD Typ A, 25 A / 30 mA, 5SV33126. Modell-Plausibilität 0,465 A <= 1 A <= 19,5 A. Quellenbemessung 20 A versus gG25 ist als fachlicher Prüffund dokumentiert. LED-Inrush, RCD-Eignung und vollständige Selektivität bleiben offen. Die nativen Kennlinien enthalten keine ausgefüllte Gesamtselektivitätsbewertung.

Der neue CAD-Detailplan zeigt zwölf Leuchten und 24 Stamm-/Stich-IDs. Die XLSX berechnet den Laststrom je Abschnitt und summiert dessen Spannungsfall entlang des Weges. Betriebsreferenz rho=0,0225 Ohm mm²/m, X=0,00008 Ohm/m, S=1,5 mm²; nativer Zuleitungsanteil fest 0,010 %. Keine neue native 12-Knoten-SIMARIS-Rechnung behaupten.

## Ergebnisse

| Ergebnis | A | B | Herkunft |
|---|---:|---:|---|
| Last | 102 W | 102 W | erhaltene Liste / native Ersatzlasten |
| DeltaU kumuliert | 0,596 % | 0,649 % | SIMARIS |
| Ik1 min L-N/L-PE | 59,029 A | 54,374 A | native Kurzschluss-Tabelle |
| Kabel-Iz | 19,5 A | 19,5 A | nativer Szenariowert |
| DeltaU max verteilt | 0,329376 % | 0,387322 % | eigene Abschnittsreferenz |

UV Ik3 max/min 2,078845 / 1,132441 kA. Unterschiede zwischen Ersatzlast- und Abschnittsrechnung sind wegen verschiedener Lastverteilung und Widerstandsannahmen zu erklären; kein identischer Softwarevergleich. Alle zwölf Referenzwege unabhängig summiert, Längen- und Null-Last-Abhängigkeit geprüft. Vorhandene Ergebnisse wurden beim Zusammenstellen nicht nachträglich erfunden.

## Bewertung

Die Arbeitsprobe verbindet echte Softwareausgaben mit einer erklärbaren Referenzrechnung und bearbeitbaren Zeichnungen. Lernpunkte: Einheiten/Koordinaten, Erhalt vorhandener Geometrie, Lichtauswertung, Laststruktur, Modellgrenzen und kritische Geräteprüfung. Ein erfolgreicher Rechenlauf wird von einer technischen Gerätefreigabe unterschieden.

## Grenzen

Fiktives Lernprojekt. Reale Netz-/Bestandsdaten sind kein Blocker für die Präsentation, wären aber für eine Ausführung erforderlich. Schutzstaffelung, Selektivität/I²t, Treiberdaten, SPD/Bahn-PA, tatsächliche Verlegung, unsymmetrischer Lastfluss/Oberschwingungen sowie Licht-Sollwerte und Sicherheitsbeleuchtung sind nicht abschließend nachgewiesen. Die technische Gesamtplanung ist nicht abgeschlossen.

## Fazit

Für die Vorstellung liegen ein dreiseitiger Überblick, ein aktueller Detailstromlaufplan, native Relux-/SIMARIS-Berichte und eine berechenbare Leuchtentabelle vor. Daraus kann der spätere Bericht entstehen. Die offene Ausführungsprüfung wird als Weiterführung beschrieben; sie wird nicht als bereits erledigt dargestellt.

## Dateien, Bilder und Quellen

Einstieg: `00_Vorstellung`. Neu benannte Originale: `09_SIMARIS/Export_Mohamed_Saida`; aktueller Detailplan: `02_CAD/Bahnsteig_Mohamed_Saida_Detailstromlaufplan`. Bilder: `04_Screenshots/VERZEICHNIS.md`. Quellen und Abrufstand: `QUELLEN.md`. Qualitätsklassifikation: `PRUEFSTATUS.csv`. Kein langer endgültiger Bericht erstellt.
