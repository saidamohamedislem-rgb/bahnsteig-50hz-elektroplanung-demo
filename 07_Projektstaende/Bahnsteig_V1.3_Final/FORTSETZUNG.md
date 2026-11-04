# Fortsetzung – exakt an diesem Stand beginnen

Gesichert am 04.11.2026. Benutzerwunsch: gesamten aktuellen Arbeitsstand im bestehenden GitHub-Projekt sichern, um später weiterzuarbeiten.

## Zuerst öffnen

1. ReluxDesktop 2026.2: `01_Relux/Bahnsteig_Beleuchtung_V1.3_Final.rdf`.
2. Aktuelle Szene: **Exterior 2**. Berechnung nach Ergänzung der Stützen ist erfolgt; zuletzt Strg+S im Programm ausgeführt.
3. BricsCAD V26: `02_CAD/Bahnsteig_V13_Lageplan.dwg`, `Bahnsteig_V13_Stromlaufplan.dwg`, `Bahnsteig_V13_Modell3D.dwg`.
4. `03_Elektro/Bahnsteig_V13_Berechnungen.xlsx` und `PRUEFSTATUS.csv` lesen.

## Bestehendes bewahren

- Nicht neu starten und die zwölf Leuchten L01–L12 nicht löschen, verschieben oder neu erzeugen.
- Koordinaten: X = 5, 15, …, 115 m; Y = 2 m; Z = 4,3 m für L05–L08, sonst 4,5 m. Rotation im nativen Plan unverändert.
- Rapportraster und Darstellungshöhen nicht als Leuchtenpositionen missverstehen. Maßgebend ist die Leuchtenliste, PDF Seite 5.
- Plattform: X=0…120, Y=0…4 m. Bestehendes Dach: X=45…75, Y=−0,5…4,5, Z=4,75…5 m.
- `Canopy_Supports_V13.obj` enthält bereits **globale Meterkoordinaten**. Instanzposition **X=Y=Z=0**, Rotation 0, Faktor 1. NICHT um (60;2;0,08) versetzen!
- Die 96 importierten Stützen-/Trägerflächen ergänzen das vorhandene Dach; weder Plattform noch Dach wurden ein zweites Mal importiert.
- Originaler Lageplan ist eine gesperrte Konstruktionshilfe; 1000 Zeichnungseinheiten/m, Translation/Rotation 0. Alte LIGHT_A/B- und CABLE_A/B-Referenzlayer ausgeblendet.
- Stromlaufplan bleibt separate elektrische Dokumentation.
- Vor neuer Bearbeitung nächste Version sichern. V1.2 liegt unverändert unter 05_Grundlagen.

## Als Nächstes ingenieurtechnisch bearbeiten

1. Projektanforderungen festlegen: Bahnsteig-/Beleuchtungsklasse, Sollwerte, Blendung, Randzonen, Wartung und Sicherheitsbeleuchtung. Erst danach Lichtbewertung abschließen.
2. Einspeisung beschaffen: Netzform, realer Übergabepunkt, Quellimpedanz bzw. Ik min/max, Vorsicherung und deren Herstellerdaten, vorgelagerte Leitungen.
3. Reale Kabelwege, Verlegearten, Häufung, Umgebungstemperatur, Kabeltyp und LED-Treiberdaten einschließlich Einschaltstrom/Fehlerstrom festlegen.
4. Netzmodell in geeignetem Werkzeug, z.B. SIMARIS design, aufbauen. Es existiert hier **kein ausgeführter nativer SIMARIS-Netznachweis**.
5. Ib/Iz/In, Spannungsfall mit allen Abschnitten, Kurzschluss, Ausschaltvermögen und Abschaltung berechnen. Danach Selektivität mit konkreten Gerätepaaren prüfen.
6. RCD-/SPD-Konzept, PE/PA, Bahn-Erdung und Schnittstellen fachlich koordinieren. Keine ungeprüfte Verbindung zu Schienen herstellen.
7. Geräte und Kabel erst nach diesen Prüfungen im Stromlaufplan konkretisieren. Schematische Trassen mit realer Leitungsführung abgleichen.
8. Relux nur bei Änderungen am lichttechnischen Modell neu rechnen. Bei F12 explizit künstliche Beleuchtung wählen; den optionalen Raytracing-Zweig nicht mit dem eigentlichen Nachweis verwechseln.
9. Neue PDF-Ausgaben exportieren, Prüfstatus aktualisieren und danach den ausführlichen Bericht schreiben.

## Nachweise zur aktuellen Version

Gültige native Lichtwerte: **18,1 / 7,96 / 37 lx, U0 0,44**. Veraltete Zwischenwerte 17,6 lx oder Emax 35 lx nicht verwenden.
Die nativen PDFs behalten das ursprüngliche Projektdatum 03.11.2026 und einen Adressplatzhalter; Bearbeitungsstand dieser Ablage ist 04.11.2026.
Seite 2 der Relux-Gesamtausgabe enthält zusätzlich einen unbenutzten 17-W-Bibliothekstyp; die installierte Liste umfasst ausschließlich die bestehenden 18,5-/14-W-Leuchten.
Die CAD-PDFs stammen aus BricsCAD EXPORTPDF; nur ungenutzte Seitenränder wurden zugeschnitten. Der Gesamtbericht fügt die unveränderten nativen PDF-Seiten zusammen.
