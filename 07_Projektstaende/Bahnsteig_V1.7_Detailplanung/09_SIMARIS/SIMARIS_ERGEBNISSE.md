# SIMARIS V1.6 - Rechenmodell, Ergebnisse und Grenzen

04.11.2026. Primärbelege: aktives natives SDX-Projekt, SIMARIS-Berichte, tabulatorgetrennte native CSV-Dateien und Screenshots 12/13. Software 27.0.1 (2026-11-02), Subrevision 2267. Dimensionierung ausgeführt, Messages [0].

## Modell und tatsächliche Einstellungen

- Bestehende Lichtlast: 204 W nominal. A = L01/03/05/07/09/11, B = L02/04/06/08/10/12, je 102 W. Im Rechenprogramm sind dies ZWEI gebündelte Endlasten am letzten Anschlusspunkt, nicht zwölf einzeln modellierte Abzweige.
- A: L1-N, 109,7 m. B: L2-N, 119,7 m. cos phi 0,95 induktiv, g=1, je eine Ersatzlast. Dreiphasige Quelle mit N; 10-m-Zuleitung zur UV.
- Quelle 400 V, TN-S, 50 Hz. Ik3 max/min = 3/1,5 kA und Ik1 max/min = 3/1,5 kA, Quellen-Kurzschluss-cos-phi 0,7: ausdrückliche DEMO-Annahmen. Kein Netzbetreiberwert.
- Quellenbemessungsstrom 20 A. Automatische gG-Auswahl 25 A: vor realer Freigabe mit tatsächlich verfügbarer Anschlusskapazität und vorgeschaltetem Schutz abstimmen. Ein fehlerfreier Programmlauf löst diesen Planungsbedarf nicht auf.
- Land Deutschland, Rechenstandard im Bericht IEC. Keine pauschale DIN/VDE-/Bahn-Konformität. Nativer Hinweis auf nicht implementierte nationale Abweichungen steht auf Berichtseite 12.
- Gerätetemperatur 45 °C, cmax=1,1, cmin=0,9, zulässiger Netzspannungsfall 8 % sind die tatsächlich exportierten Einstellungen. Nicht als nachträglich bestätigte Projektvorgaben ausgeben. Der Istwert liegt zwar auch unter einer optionalen 3-%-Vergleichsmarke; ein verbindlicher Sollwert wurde nicht vereinbart.
- Cu/PVC70, Verlegeart C, Gesamtfaktor 1. Leitertemperaturen: 55 °C für Spannungsfall, 20 °C für Ikmax, 80 °C für Abschaltbedingung. Reale Häufung, Umgebung, Kabelwege und Artikel fehlen.
- Der Bericht enthält allgemeine Mittelspannungs-Defaults 20 kV / 250...100 MVA. Es wurde keine MV-Einspeisung/kein Transformator modelliert; dies sind keine verwendeten Netzbetreiberdaten. Der MV-Schalteinstellungs-CSV enthält nur Überschriften.
- Lastflussanzeige war balanced. Die Lasttabelle bestätigt A auf L1-N und B auf L2-N; ein vollständiger unsymmetrischer Lastfluss-/Neutralleiter- und Oberwellennachweis ist nicht erbracht. Die native Energieansicht rundet/aggregiert die Quelle auf 0,3 kW; sie wird nicht als Nachweis der exakten 204 W verwendet. Nennleistung ergibt sich aus der erhaltenen Leuchtenliste und den zwei nativen 0,102-kW-Lasten.

## Tatsächlich automatisch ausgewählte Geräte

| Funktion | Referenz | Native Auswahl | Einordnung |
|---|---|---|---|
| FSO 1.1a | Sockel 3NH4030 / Sicherung 3NA3810 | gG 25 A, Sockel 160 A, Icu 120 kA, erforderlich 3 kA | Preliminary; Quelle 20 A abstimmen |
| CB 1.2a / CB 1.3a | 5SY41016 | B1 A, Icn 10 kA, erforderlich 1,548 kA | Preliminary; LED-Einschaltstrom offen |
| RCD je A/B | 5SV33126 | Typ A, 25 A, 30 mA, unverzögert | Preliminary; Treibereignung/Ableitströme offen |

Kein zweiter gleich großer Incomer-Schalter wie im alten ELEK-Modell. Kein SPD automatisch ausgewählt. Katalogbezeichnungen im nativen Dokument sind keine Beschaffungs- oder Freigabeliste. Die tatsächlichen Derating-Werte im Diagramm sind niedriger als die Nennwerte (B1-Gerät Iz 0,93 A; Sicherung Iz 23 A bei der gewählten Umgebung).

## Ergebniswerte aus nativer Ausgabe

| Größe | Zuleitung / UV | A | B |
|---|---:|---:|---:|
| Länge m | 10 | 109,7 | 119,7 |
| L/N/PE mm² | 4/4/4 (3 L) | 1,5/1,5/1,5 | 1,5/1,5/1,5 |
| Ib A, Bericht | 0,465 | 0,465 | 0,465 |
| Iz Kabel A | 32 | 19,5 | 19,5 |
| Spannungsfall Abschnitt % | 0,010 | 0,586 | 0,639 |
| Spannungsfall kumuliert % | 0,010 | 0,596 | 0,649 |
| Ik1 min L-N / L-PE A | 889,774 | 59,029 | 54,374 |
| Ik1 max L-N / L-PE A | 1547,839 | 89,230 | 82,146 |
| Ik3 max A | 2078,845 | nicht anwendbar | nicht anwendbar |
| Ik3 min A | 1132,441 | nicht anwendbar | nicht anwendbar |

Der Quell-/Zuleitungsstrom ist ein nativer Phasen-/Bemessungswert; zwei Abgangsströme auf unterschiedlichen Phasen werden nicht einfach addiert. Native CSV runden Ib auf 0,47 A und Spannungsfall auf zwei Stellen. Präzisere Spannungsfallwerte stammen aus Berichtseite 6 und der Netzansicht. Zs ist in der Kurzschluss-CSV mit '-' belegt; es wird kein vermeintlich gemessener Schleifenwiderstand ergänzt.

Die einfache Plausibilitätsbeziehung gilt im Modell: 0,465 A <= 1 A <= 19,5 A für beide Abgänge. Der konservative magnetische B-Vergleich mit 5 x In = 5 A wird von 59,029 / 54,374 A überschritten. Der native Einstellwert Ii=3 A ist die untere Kennliniengrenze und wurde nicht als garantierter oberer Auslösestrom verwendet. Dies ersetzt keine vollständige Zeit-/Energie-/RCD-Prüfung. Berichtseite 9 bestätigt die Abschaltbedingung innerhalb des Softwaremodells.

## Selektivität

Fünfseitiger nativer Export vorhanden, einschließlich gG- und B1-Kennlinien sowie vorgelagerter Hüllkurve. Die Felder 'Selectivity evaluation' enthalten keinen Ergebnistext. Die zeitliche Trennung in den gezeigten Kennlinien ist sichtbar, liefert aber keinen dokumentierten Grenzstrom für Gesamtselektivität. Hersteller-Selektivitätstabellen, Strombegrenzung/I²t, RCD-Koordination und reale Vorsicherung bleiben Missing. Keine positive Herstellerfreigabe erfinden. 'Messages [0]' bedeutet hier erfolgreicher Modelllauf, nicht vollständige technische Freigabe.

## Vergleich mit V1.5 ELEK

| Merkmal | V1.5 ELEK, historisch | V1.6 SIMARIS, aktuelles Szenario |
|---|---|---|
| Quelle | 3 kA mit eigenem R/X-Modell | Ik1/Ik3 1,5...3 kA, Kurzschluss-cos-phi 0,7 |
| Zuleitung | 6 mm², 10 m | 4 mm², 10 m |
| Abgang PE | separat 4 mm² | 1,5 mm² im Modell |
| Verlegung / Temperatur | D1 / 20 °C | C / 55 °C Spannungsfall |
| Schutz | B20 + B20 + B6 | gG25 + B1 + RCD Typ A |
| ΔU kumuliert A/B % | 0,652 / 0,710 | 0,596 / 0,649 |
| Endfehlerstrom min A/B A | 98,03 / 90,12 (andere Definition/Randbedingungen) | 59,029 / 54,374 |

Diese Modelle sind keine identischen Eingaben in zwei Rechenkernen. Differenzen nicht als Softwarefehler oder gegenseitige Validierung verkaufen. Die SIMARIS-Ersatzlasten sind exakt 0,102 kW; ELEK war wegen Eingaberaster 0,47 A je Last. Die älteren Referenz-XLSX bleiben historisch und werden nicht auf die neue Gerätestaffelung umetikettiert.

## Noch erforderlich

Reale Quelle/Vorsicherung und Netzdaten; tatsächliche Kabelartikel/Verlegung; zwölf verteilte native Lasten mit allen Abzweigen; unsymmetrischer Lastfluss/Neutralleiter und LED-Oberschwingungen; Treiber-Inrush; vollständige Schutzkoordination und Kurzschlussenergie; SPD-Konzept; Erdung/Bahn-PA-Schnittstellen; RCD-Eignung und Ableitströme; Licht-Sollwerte, Blendung und Sicherheitsbeleuchtung; zusätzliche Bahnhofslasten. Die Arbeitsprobe ist vorzeigbar, die technische Gesamtplanung bleibt offen.
