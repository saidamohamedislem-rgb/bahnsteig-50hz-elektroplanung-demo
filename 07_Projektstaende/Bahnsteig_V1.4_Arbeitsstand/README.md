# Bahnsteig V1.4 - laufender Arbeitsstand

Diese Version setzt V1.3 fort. Die kopierten Relux-, CAD-, PDF- und XLSX-Dateien dokumentieren unverändert den berechneten V1.3-Stand. Neue Arbeit in `08_Webberechnung`: Auswahl einer Web-Alternative und vorbereitete Netzstruktur. Kein neuer Netz-Rechenlauf und keine elektrische Freigabe.

Zum Fortsetzen: [Web-Alternative und Zugang](08_Webberechnung/WEB_ALTERNATIVE.md), [Netzabschnitte](08_Webberechnung/Netzmodell_Leitungsabschnitte.csv), [strukturierte Eingabebasis](08_Webberechnung/Netzmodell_Eingabebasis.json). V1.3 bleibt vollständig separat erhalten.

---

## Geerbte V1.3-Unterlagen

# Bahnsteig 50 Hz – V1.3 Final / gesicherter Arbeitsstand

Stand: 04.11.2026. Fiktives Portfolio- und Lernprojekt für ein Vorstellungsgespräch.
**„Final“ bezeichnet die abgelegte Version, keine abgeschlossene technische Ausführungsplanung.**

## Einstieg

- [FORTSETZUNG.md](FORTSETZUNG.md): Startpunkt und offene Schritte.
- [BERICHT_GRUNDLAGE.md](BERICHT_GRUNDLAGE.md): Grundlage für den späteren Bericht.
- [Prüfstatus](PRUEFSTATUS.csv): Verified / Preliminary / Missing.
- [Relux-Gesamtbericht](01_Relux/Relux_V13_Final_Gesamtbericht.pdf): 18 Seiten mit nativen Relux-Ausgaben.
- [Lageplan](02_CAD/Bahnsteig_V13_Lageplan.pdf) und [Stromlaufplan](02_CAD/Bahnsteig_V13_Stromlaufplan.pdf).
- [Berechnungen](03_Elektro/Bahnsteig_V13_Berechnungen.xlsx) und [Elektroplanung](03_Elektro/ELEKTROPLANUNG_Stand.md).

## Ablage

| Ordner | Inhalt |
|---|---|
| 01_Relux | gespeicherte V1.3-RDF, Berechnungsprotokoll, OBJ-Stützen, LDT-Dateien, echte Relux-PDFs |
| 02_CAD | native DWG, bearbeitbare DXF, Lageplan- und Stromlaufplan-PDF |
| 03_Elektro | Formel-Arbeitsmappe, Leuchten-/Stromkreisverzeichnis, Annahmen und fehlende Nachweise |
| 04_Screenshots | dokumentierte native Anwendungsansichten |
| 05_Grundlagen | unveränderte V1.2-Sicherungen, CAD-/Lastquellen und Geometrieprüfung |
| 06_Werkzeuge | Bearbeitungs- und Prüfskripte mit Nutzungshinweisen |

## Ergebnisstand

12 unveränderte Leuchten, 8 × 18,5 W + 4 × 14 W = 204 W nominal.
A/B abwechselnd: je 6 Leuchten / 102 W. Relux-Neuberechnung des ergänzten Modells:
Em = 18,1 lx, Emin = 7,96 lx, Emax = 37 lx, U0 = 0,44.
Diese Werte sind Ergebnisse dieses Rechenmodells; eine Normerfüllung ist nicht nachgewiesen.
Kurzschluss, Abschaltbedingungen, Strombelastbarkeit, endgültige Schutzgeräte, Selektivität,
SPD und Bahn-Erdung benötigen weitere Eingangsdaten und Fachprüfung.

Originaldateien wurden erhalten. Die beiden V1.2-RDF-Kopien liegen unter 05_Grundlagen.
Verworfene Zwischenstände mit falsch versetzten Dachstützen gehören nicht zu dieser Lieferung.
