# Bericht-Grundlage – Bahnsteig 50 Hz Elektroplanung, V1.6

Stand 04.11.2026. Materialsammlung und Gliederungsgrundlage; kein fertig ausformulierter Abschlussbericht.

## Zielsetzung

Eine nachvollziehbare Arbeitsprobe für die elektrische Versorgung und Beleuchtung eines fiktiven Bahnsteigs erstellen. Geometrie, Leuchten, Stromkreisaufteilung, Berechnungen und Zeichnungen sollen zusammenpassen und später im Vorstellungsgespräch erläutert werden können.

## Ausgangssituation

Vorhanden waren die Relux-Version V1.2 mit zwölf Leuchten, BricsCAD-Lageplan und Stromlaufplan sowie ein älteres 3D-Modell. V1.2 und Originaldateien bleiben erhalten. V1.3 ergänzt die vorhandene Überdachung und dokumentiert den tatsächlichen Bearbeitungsstand.

## Planungsgrundlagen

- Bahnsteig 120 × 4 m, globales Koordinatensystem in Metern.
- Überdachung zwischen X=45 und X=75 m, Dachbreite 5 m einschließlich Überstand, Z=4,75…5 m.
- Versorgung 400/230 V, 50 Hz als Projektannahme; reale Netzform und Einspeiseparameter fehlen.
- Zwei abwechselnd zugeordnete Beleuchtungsstromkreise A/B; kein Nachweis unabhängiger oder sicherheitsgerichteter Versorgung.
- Reale Bestandsaufnahme, Beleuchtungsanforderungen, Netzimpedanzen, Kabelwege und Freigaben liegen nicht vollständig vor.

## Vorgehensweise

V1.2 sichern, V1.3 separat speichern, bestehende Lageplanreferenz behalten. Aus dem vorhandenen 3D-CAD ausschließlich 96 Flächen der Stützen-/Trägergeometrie übernehmen, ohne Plattform und Dach zu duplizieren. Globale Koordinaten der importierten Geometrie durch nativen CAD-Export kontrollieren. Zwölf Leuchten unverändert belassen, künstliche Beleuchtung neu berechnen, native Tabellen sowie Isolux und False Colours exportieren. Lageplan, Funktionsstromlaufplan und vorläufige elektrische Rechenmappe erstellen. Ergebnisse und Lücken getrennt kennzeichnen.

## Software

ReluxDesktop 2026.2 für Lichtberechnung; BricsCAD V26 für DWG/PDF; SIMARIS design 27.0.1, Subrevision 2267, für das aktuelle native A/B-Netz und dessen Dimensionierung. Word wurde ausschließlich zum PDF-Export der nativen SIMARIS-RTFs verwendet. PowerShell/Python dienen Ablage, Datenabgleich und PDF-Verarbeitung; Git/GitHub sichern die Versionen. Historisch bleiben ELEK-Free V1.5 und dessen Formel-XLSX erhalten.

## Leuchtenauswahl

Die bestehende Auswahl wurde übernommen: acht Schmidt-Strahl 18,5-W-Leuchten mit BB-Optik und vier 14-W-Leuchten, jeweils 4000 K nach den vorhandenen LDT-Daten. L05–L08 unter der Überdachung auf 4,3 m; übrige Leuchten auf 4,5 m. X-Abstand 10 m, Y=2 m. Gesamtleistung nominal 204 W, A/B je 102 W. Produkt-/Treiberfreigabe und Betriebsbedingungen bleiben zu prüfen. Ein zusätzliches 17-W-Bibliotheksdatenblatt im Relux-PDF gehört nicht zur installierten Leuchtenliste.

## Lichtberechnung

Native Neuberechnung der Szene Exterior 2 nach Ergänzung der Dachstützen. Auswertung Floor (E), Wartungsfaktor im Modell 0,8:

| Größe | Ergebnis | Status |
|---|---:|---|
| Mittlere Beleuchtungsstärke Em | 18,1 lx | Verified als Modellergebnis |
| Minimale Beleuchtungsstärke Emin | 7,96 lx | Verified als Modellergebnis |
| Maximale Beleuchtungsstärke Emax | 37 lx | Verified als Modellergebnis |
| Gleichmäßigkeit U0 = Emin/Em | 0,44 | Verified als Modellergebnis |

Belege: `01_Relux/Relux_V13_Final_Gesamtbericht.pdf`, Seiten 5–18, RDF und Berechnungsprotokoll. Keine Konformitätsbewertung ohne vereinbarte Sollwerte, Randbedingungen und fachliche Prüfung. Ein berechnetes Bild stellt keine Messung vor Ort dar.

## Elektroplanung

V1.6 enthält den ausgeführten nativen SIMARIS-Netzlauf. Zwei Ersatzlasten zu je 102 W repräsentieren die vorhandenen zwölf Leuchten; A auf L1-N, B auf L2-N. 400-V-TN-S-Quelle, 50 Hz, Ik1/Ik3 min 1,5 kA / max 3 kA sind Demoannahmen. Einspeisung 10 m Cu L/N/PE 4 mm², Abgänge 109,7 / 119,7 m Cu L/N/PE 1,5 mm², PVC70, Verlegeart C, Faktor 1. Leitertemperatur Spannungsfall 55 °C, Gerätetemperatur 45 °C, zulässiger Netzspannungsfall in der Software 8 %. Tatsächlicher Rechenstandard IEC.

Autoauswahl gG25 (3NA3810 / Sockel 3NH4030), B1 A 10 kA (5SY41016) und je RCD Typ A 25 A / 30 mA (5SV33126). Quellenbemessung 20 A versus gG25, LED-Einschaltstrom, RCD-Eignung und reale Installation sind noch zu prüfen. Keine zweite B20-Stufe aus dem alten ELEK-Entwurf übernommen. SPD und Bahn-Erdung/PA bleiben offen.

Die gebündelten Lasten sind ein Ersatzmodell. Zwölf verteilte native Lasten, unsymmetrischer Lastfluss, Neutralleiter/Oberschwingungen und vollständige Schutzkoordination sind noch nicht nachgewiesen. Die alten V1.3-/V1.5-Pläne und XLSX sind historische Vergleichsstände. Aktueller nativer elektrischer Netzplan: `09_SIMARIS/SIMARIS_V16_Netzplan.dwg`.

## Ergebnisse

| Ergebnis | A | B | Einordnung |
|---|---:|---:|---|
| Last nominal | 102 W | 102 W | aus unveränderter Leuchtenliste und nativen Lasten |
| Kumulativer Spannungsfall | 0,596 % | 0,649 % | Verified als Modellergebnis |
| Ik1 min L-PE / L-N | 59,029 A | 54,374 A | Verified als Modellergebnis |
| Ik1 max L-PE / L-N | 89,230 A | 82,146 A | Verified als Modellergebnis |
| Kabel-Iz | 19,5 A | 19,5 A | nativ; reale Verlegung Preliminary |

UV Ik3 max/min 2,078845 / 1,132441 kA. SIMARIS meldete Messages [0]. Berichtseite 9 bestätigt die Abschaltbedingung im Modell. Einfache Plausibilität Ib 0,465 A <= In 1 A <= Iz 19,5 A. Endfehlerstrom größer als 5 x In des B1-Kandidaten. Dies ist keine Feldmessung oder vollständige Schutzfreigabe.

Native Kennlinien liegen vor, die Felder 'Selectivity evaluation' sind leer. Gesamtselektivität und Hersteller-I²t-/Grenzstromkoordination bleiben Missing. Kein vermeintliches positives Ergebnis ergänzen. Die native Energieansicht mit 0,3 kW ist wegen balanced-Darstellung/geringer Anzeigeauflösung nicht Grundlage der 204-W-Lastbilanz.

Verified: echte SIMARIS-, Relux- und erhaltene CAD-Dateien sowie exportierte Modellwerte. Preliminary: reale Anwendbarkeit der Netz-, Kabel- und Gerätauswahl. Missing: Eingangsdaten, verteiltes Detailnetz und abschließende Schutz-, Erdungs-/SPD-, Lichtanforderungs- und Sicherheitsbeleuchtungsnachweise. Einzelheiten: `09_SIMARIS/SIMARIS_ERGEBNISSE.md`, `PRUEFSTATUS.csv`.

## Bewertung

Der Stand bietet eine vorzeigbare digitale Planungsgrundlage mit echten Softwareausgaben und nachvollziehbaren Annahmen. Die Trennung zwischen berechnetem Modellergebnis und offenem Auslegungsnachweis ist Bestandteil der Arbeitsprobe. Die A/B-Aufteilung begrenzt die Zahl der Leuchten je Abgang; sie beseitigt nicht den gemeinsamen Ausfallpunkt der Einspeisung.

## Grenzen

Fiktives Lernprojekt ohne reale Netz- und Bestandsdaten. Keine Ausführungsfreigabe. Rechenwerte sind nicht gemessen. Volltexte der relevanten Normen und projektspezifische Bahnregelwerke wurden nicht vollständig geprüft. Die native Relux-Ausgabe enthält ein geerbtes Datum und einen Adressplatzhalter. Material-/Reflexionsannahmen und die Anforderungen an Blendung und Sicherheitsbeleuchtung sind vor Abschluss zu bestätigen.

## Fazit

V1.6 ergänzt die erhaltene Lichtplanung um einen tatsächlich gerechneten SIMARIS-Entwurf und native Geräte-/Kabel-/Kurzschlussausgaben. Die Arbeitsprobe zeigt den Planungsablauf und seine Grenzen. Wesentliche reale Schutz-, Erdungs- und Anforderungsnachweise bleiben offen; die technische Gesamtplanung ist nicht abgeschlossen.

## Bild- und Tabellenmaterial für den späteren Bericht

- Relux-Gesamtbericht: Leuchten S.5, Grundriss S.6, Raster S.7-15, Isolux S.16, 3D S.17, False Colours S.18. Die ursprünglichen V1.2-Sicherungen bleiben erhalten.
- SIMARIS-Projektdokumentation: Parameter S.2, Betrieb S.3, Quelle S.4, Geräte S.5, Kabel/Spannungsfall S.6, Lasten S.8, Abschaltbedingung S.9, Normhinweise S.12.
- SIMARIS-Kennlinien: Quelle S.2-3, A S.4, B S.5. Keine ausgefüllte Selektivitätsbewertung.
- Netzansichten-Lesefassung: Geräte S.1, Lastfluss S.2, Kurzschluss S.3. Unverändertes fünfseitiges Original separat.
- Screenshots 11-13 dokumentieren den tatsächlich geöffneten DWG-Export und den SIMARIS-Lauf mit Messages [0]. Tabelle `09_SIMARIS/SIMARIS_Ergebnisvergleich.csv`; native Roh-CSV sind tabulatorgetrennt trotz Endung .csv.
- Quellen/Abrufdaten in `QUELLEN.md`; kurzer Gesprächsleitfaden in `VORSTELLUNGSGESPRAECH.md`. Kein langer endgültiger Bericht erstellt.
