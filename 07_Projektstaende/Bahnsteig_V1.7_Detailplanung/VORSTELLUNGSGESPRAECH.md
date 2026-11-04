# Gesprächsleitfaden - fünf Minuten Arbeitsprobe

Mohamed Saida. 04.11.2026. Kein langer Abschlussbericht; Dateiwegweiser und fachliche Erläuterung.

1. **Ziel und Modell (45 s):** Fiktiver 120 x 4 m Bahnsteig, Überdachung von 45 bis 75 m, zwölf vorhandene Leuchten, 204 W. Lageplan und Relux-Falschfarben zeigen.
2. **Lichtplanung (45 s):** Em 18,1 lx, Emin 7,96 lx, U0 0,44. Das sind echte Relux-Modellergebnisse. Welche Sollwerte und Blendungs-/Sicherheitsanforderungen gelten, muss projektbezogen vereinbart werden.
3. **SIMARIS-Netz (90 s):** Lesefassung Seiten 1-3 öffnen: angenommene TN-S-Quelle, UV, zwei getrennte Abgänge. A/B abwechselnd sechs Leuchten je Kreis, Ersatzlast je 102 W. CAD-Export und SDX zeigen durchgängige bearbeitbare Daten.
4. **Ergebnisse erklären (60 s):** Spannungsfall 0,596 / 0,649 %, minimale Endfehlerströme 59,029 / 54,374 A. Autoauswahl gG25, B1 und je RCD Typ A. Die Gerätekandidaten benötigen LED-Inrush-/Netzdatenprüfung. 20-A-Quellenwert und 25-A-Vorsicherung sind noch abzustimmen.
5. **Eigene Bewertung (60 s):** Kennlinien vorhanden, aber kein ausgefüllter Gesamtselektivitätsnachweis. Reale Quelle, Verlegung, PA/SPD und Sicherheitsbeleuchtung fehlen. Nächster Schritt: reale Daten und verteilte zwölf Lasten, neu rechnen und Zeichnungen synchronisieren.

## Kurze Formulierung

„Ich habe die bestehende Lichtplanung erhalten und um eine nachvollziehbare Netzrechnung in SIMARIS ergänzt. Die Ergebnisse und Geräte lassen sich bis zur nativen Datei zurückverfolgen. Für die Vorplanung nutze ich zwei Ersatzlasten. Ich trenne bestätigte Modellergebnisse von Annahmen und noch fehlenden Nachweisen. Für eine Ausführung würde ich zuerst die Netzdaten und das Schutz-/Erdungskonzept vervollständigen.“

## Typische Rückfragen

- **Warum zwei Stromkreise?** Abwechselnde Zuordnung reduziert bei einem Abgangsausfall die Zahl betroffener Leuchten. Gemeinsame Quelle bleibt gemeinsamer Ausfallpunkt; keine Sicherheitsstromversorgung nachgewiesen.
- **Warum B1 statt B6?** Automatische Auswahl bei kleiner Dauerlast. Das ist ohne Treiber-Einschaltstrom noch keine endgültige Empfehlung.
- **Sind die Kurven ein Selektivitätsnachweis?** Der aktuelle Export zeigt Kennlinien und die vorgelagerte Hüllkurve. Bewertungsfeld und bestätigter Selektivitätsgrenzstrom fehlen.
- **Warum andere Ergebnisse als ELEK?** Quelle, Temperatur, Verlegung, PE und Schutzgeräte unterscheiden sich. Es ist ein anderer dokumentierter Modellstand.
- **Was ist fertig?** Native Lichtsimulation, CAD-Bestand, SIMARIS-Ersatznetz und dokumentierte Ausgabe. Reale technische Gesamtplanung ist nicht abgeschlossen.

V1.7 ergänzt die Abschnittsrechnung für zwölf Einzellasten. Die neue Mappe ist als Referenz und die V16-PDFs als historischer nativer Rechenlauf zu zeigen. Aktualisierte V17-PDF-Schriftfelder stehen noch aus.
