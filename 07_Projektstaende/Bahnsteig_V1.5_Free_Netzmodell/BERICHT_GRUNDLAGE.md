# Bericht-Grundlage – Bahnsteig 50 Hz Elektroplanung, V1.5

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

ReluxDesktop 2026.2 für Lichtberechnung und Originalausgabe; BricsCAD V26 für native DWG und PDF; PowerShell/Python für Ablage, Datenabgleich und PDF-Verarbeitung; Tabellenwerkzeug für eine bearbeitbare XLSX mit Formeln; Git/GitHub zur Sicherung. SIMARIS Suite ist vorhanden, wurde aber nicht fuer einen nativen Netzlauf verwendet. V1.5 nutzt stattdessen den nativen ELEK Cable Pro Web Calculator (IEC 60364-5-52) mit einem kostenlosen A/B-Ersatzmodell.

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

V1.5 ergaenzt den echten ELEK-Netzlauf und das passende separate BricsCAD-Schema. Quelle 400/230 V, 50 Hz, TN und 3 kA sind ausdrueckliche Demoannahmen. UV-Zuleitung 10 m Cu/PVC70 L/N/PE 6 mm2; A/B 109,7/119,7 m, L/N 1,5 mm2, PE 4 mm2 separat, D1 mit Korrekturfaktor 1. A liegt auf L1, B auf L2. Je Kreis sind sechs nominale 102-W-Leuchten am letzten Punkt als Ersatzlast zusammengefasst. 0,47 A Eingaberaster entspricht je 102,695 W statt exakt 102 W bei nominal 230 V.

Generische B20 an Quelle und UV-Incomer sowie B6 je Abgang. Beide B20 heissen nativ F0 DEMO B20, im CAD zur Unterscheidung F0-S/F0-U. Diese doppelte B20-Stufe ist nicht selektiv freigegeben und bedarf einer spaeteren Entwurfsentscheidung. Das vorhandene V1.3-Funktionsschema bleibt Historie. Der aktuelle V15-Stromlaufplan zeigt die tatsaechlichen Szenariogeraete und die offenen RCD-/SPD-/PE/PA-Funktionen.

Die V1.3-Rechenmappe bleibt ein separater historischer 2,5-mm2-Vergleich mit verteilten Lasten. Die V1.5-Mappe vergleicht das aktuelle 1,5-mm2-Ersatzmodell mit Referenzformeln. Keine der beiden Mappen ist eine reale Produktauswahl.

## Ergebnisse

| Ergebnis | A | B | Einordnung |
|---|---:|---:|---|
| Kumulierter Spannungsfall | 0,652 % | 0,710 % | Verified als natives Szenarioergebnis |
| Fehlerstrom Ief am Endpunkt | 98,03 A | 90,12 A | Verified als natives Szenarioergebnis |
| Strombelastbarkeit Iz | 22 A | 22 A | Preliminary bezogen auf reale Verlegung |
| Zs real / imaginaer | 2,3445 / 0,0881 Ohm | 2,5507 / 0,0897 Ohm | native TN-Annahme |
| Beruehrungsspannung vor Abschaltung | 60,50 V | 60,68 V | kein zulaessiger Dauerwertnachweis |

UV-Ik3 laut Szenario 2,617 kA max / 2,504 kA min. Ief=230/abs(Zs) unabhaengig nachgerechnet. B6 mit generischem Ia=30 A wird im angenommenen TN-Modell rechnerisch erreicht; reale Netz-/Geraeteparameter fehlen weiterhin. B20/B6-Kennlinienbericht ist erzeugt, Gesamtselektivitaet ist nicht nachgewiesen. Die Fehlerstroeme liegen im magnetischen Toleranzbereich des vorgelagerten B20. Icn, LED-Einschaltstrom und Hersteller-I2t-Koordination sind offen.

Verified: native Relux- und ELEK-Ausgaben, erhaltene Leuchtenliste, bearbeitbare CAD-/Tabellendateien. Preliminary: Netz-/Kabel-/Schutz-Szenario und geometrische Demoannahmen. Missing: reale vollstaendige Schutzauslegung, Selektivitaet, Bahn-Erdungs-/SPD-/RCD-Konzept, Sicherheitsbeleuchtung und Licht-Sollwertbewertung. Details in `PRUEFSTATUS.csv` und `08_Webberechnung/FREE_MODELL_V15.md`.

## Bewertung

Der Stand bietet eine vorzeigbare digitale Planungsgrundlage mit echten Softwareausgaben und nachvollziehbaren Annahmen. Die Trennung zwischen berechnetem Modellergebnis und offenem Auslegungsnachweis ist Bestandteil der Arbeitsprobe. Die A/B-Aufteilung begrenzt die Zahl der Leuchten je Abgang; sie beseitigt nicht den gemeinsamen Ausfallpunkt der Einspeisung.

## Grenzen

Fiktives Lernprojekt ohne reale Netz- und Bestandsdaten. Keine Ausführungsfreigabe. Rechenwerte sind nicht gemessen. Volltexte der relevanten Normen und projektspezifische Bahnregelwerke wurden nicht vollständig geprüft. Die native Relux-Ausgabe enthält ein geerbtes Datum und einen Adressplatzhalter. Material-/Reflexionsannahmen und die Anforderungen an Blendung und Sicherheitsbeleuchtung sind vor Abschluss zu bestätigen.

## Fazit

V1.5 enthaelt eine ausgefuehrte Lichtsimulation und eine native elektrische Szenariorechnung mit offengelegten Grenzen. Die Arbeitsprobe ist fuer die Erlaeuterung des Vorgehens vorbereitet. Wesentliche reale Schutz-, Erdungs- und Anforderungsnachweise bleiben offen; die technische Gesamtplanung ist nicht abgeschlossen.

## Bild- und Tabellenmaterial für den späteren Bericht

Lageplan-PDF; Stromlaufplan-PDF; nativer Relux-Bericht Seite 5 (Leuchten), 6 (Grundriss), 7–15 (Raster), 16 (Isolux), 17 (3D), 18 (False Colours). Screenshots mit Verzeichnis unter `04_Screenshots`; Last-/Leuchtenliste als CSV und XLSX. Quellen und Abrufdatum in `QUELLEN.md`. Technischer Fortsetzungsplan in `FORTSETZUNG.md`.

V1.5 ergaenzt native ELEK-PDFs (7 + 3 Seiten), V15-Stromlaufplan und Modellvergleich-XLSX. Free-Wasserzeichen und Lizenzhinweise wurden unveraendert beibehalten. Kein kostenpflichtiger Plan wurde aktiviert.
