# Bericht-Grundlage – Bahnsteig 50 Hz Elektroplanung, V1.3

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

ReluxDesktop 2026.2 für Lichtberechnung und Originalausgabe; BricsCAD V26 für native DWG und PDF; PowerShell/Python für Ablage, Datenabgleich und PDF-Verarbeitung; Tabellenwerkzeug für eine bearbeitbare XLSX mit Formeln; Git/GitHub zur Sicherung. SIMARIS Suite ist vorhanden, ein nativer Netzberechnungslauf ist nicht durchgeführt und wird nicht behauptet.

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

Funktionsschema UV-01 mit Einspeisung, A/B-Abgängen, Platzhaltern für Schutz-/Schaltfunktionen, SPD und PE/PA-Schnittstelle. Reale Gerätewerte wurden nicht erfunden. Die Rechenmappe enthält ein offen gelegtes 230-V-Szenario mit cos φ=0,95, Cu-Rechenwert ρ=0,0225 Ωmm²/m und Vergleichsquerschnitt 2,5 mm². Die letztgenannten Größen sind Annahmen, keine freigegebene Auslegung.

Nominaler Szenariostrom je Kreis 0,467 A. Der rein ohmsche Anteil des Spannungsfalls bis zur letzten Leuchte beträgt A etwa 0,440 V / 0,191 %, B etwa 0,520 V / 0,226 %. Vorgelagerte Leitungen, Reaktanz, reale Routen, Erwärmung und Treiberverhalten sind nicht vollständig erfasst. Weitere Erläuterung in `03_Elektro/ELEKTROPLANUNG_Stand.md`.

## Ergebnisse

- Verified: native Berechnung und PDF-Ausgaben, zwölf unveränderte Leuchtenkoordinaten, nominale 204 W, abwechselnde A/B-Zuordnung, native DWG-Dateien und koordinierte 3D-Geometrie.
- Preliminary: Abmessungen/Materialien als Demo-Ansatz, schematische Trassen, Funktionsstromlaufplan und ohmsche Spannungsfall-Vorberechnung.
- Missing: Sollwertbewertung, vollständige Kabelbemessung, Kurzschluss-/Abschaltnachweis, Schutzgeräte-/RCD-Auswahl, Selektivität, abgestimmte Erdungs-/SPD- und Sicherheitsbeleuchtungsplanung.

## Bewertung

Der Stand bietet eine vorzeigbare digitale Planungsgrundlage mit echten Softwareausgaben und nachvollziehbaren Annahmen. Die Trennung zwischen berechnetem Modellergebnis und offenem Auslegungsnachweis ist Bestandteil der Arbeitsprobe. Die A/B-Aufteilung begrenzt die Zahl der Leuchten je Abgang; sie beseitigt nicht den gemeinsamen Ausfallpunkt der Einspeisung.

## Grenzen

Fiktives Lernprojekt ohne reale Netz- und Bestandsdaten. Keine Ausführungsfreigabe. Rechenwerte sind nicht gemessen. Volltexte der relevanten Normen und projektspezifische Bahnregelwerke wurden nicht vollständig geprüft. Die native Relux-Ausgabe enthält ein geerbtes Datum und einen Adressplatzhalter. Material-/Reflexionsannahmen und die Anforderungen an Blendung und Sicherheitsbeleuchtung sind vor Abschluss zu bestätigen.

## Fazit

V1.3 ist ein gesicherter Zwischenstand für Präsentation und Weiterbearbeitung. Die Lichtsimulation wurde ausgeführt, die wesentlichen elektrischen Nachweise stehen weiterhin aus. Erst nach deren Bearbeitung kann eine technische Abschlussbewertung erfolgen.

## Bild- und Tabellenmaterial für den späteren Bericht

Lageplan-PDF; Stromlaufplan-PDF; nativer Relux-Bericht Seite 5 (Leuchten), 6 (Grundriss), 7–15 (Raster), 16 (Isolux), 17 (3D), 18 (False Colours). Screenshots mit Verzeichnis unter `04_Screenshots`; Last-/Leuchtenliste als CSV und XLSX. Quellen und Abrufdatum in `QUELLEN.md`. Technischer Fortsetzungsplan in `FORTSETZUNG.md`.
