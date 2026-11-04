# Abschnittsrechnung V1.7

Bearbeiter: Mohamed Saida. 04.11.2026. Status Preliminary bezogen auf die reale Anlage.

## Rechenweg

24 vorhandene schematische Leitungsabschnitte: A/B je sechs Stammstücke und sechs Stiche. Die Länge des ersten Stammstücks beträgt 4,1 m in A und 14,1 m in B. Weitere Stammstücke sind je 20 m lang. Stiche betragen 5,4 m unter dem Dach und 5,6 m im freien Bereich. Keine geometrische Änderung an den Relux-Leuchten.

Jedes Stammstück trägt nur die Summe der tatsächlich dahinter liegenden Leuchtenleistungen; ein Stich trägt nur seine einzelne Leuchte. Je Kreis sechs Lasten, 102 W; Gesamt 204 W. Mit U0=230 V und cos phi=0,95 gilt I=P/(U0 cos phi).

Für Phase und eigenen Neutralleiter gleichen Querschnitts:

DeltaU = 2 I (R cos phi + X sin phi).

R = rho L/S, X = x L. Referenzeingaben: Cu rho=0,0225 Ohm mm²/m, x=0,00008 Ohm/m, S=1,5 mm². Diese Betriebsreferenz ist kein genauer Nachbau der 55-Grad-SIMARIS-Leitungsparameter. Der gemeinsame Zuleitungsanteil 0,010 % stammt fest aus der nativen SIMARIS-Rechnung. Er wird bei Änderungen der Referenzeingaben nicht neu gerechnet.

Die Spannungsfälle der Stammstücke werden entlang des Weges kumuliert. Am jeweiligen Leuchtenpunkt kommt nur dessen eigener Stich dazu. Die Werte benutzen konstante Nennspannung zur Laststromermittlung; keine iterative Leistungsflussrechnung, keine Neutralleiterkopplung zwischen A/B und keine Oberwellenberechnung.

## Ergebnisse

| Kreis | Last | Letzte Leuchte | Max. DeltaU gesamt Referenz | Nativer SIMARIS-Ersatzlastwert |
|---|---:|---|---:|---:|
| A | 102 W | L11 | 0,329376 % | 0,596 % |
| B | 102 W | L12 | 0,387322 % | 0,649 % |

Die geringere Belastung der hinteren Stammstücke erklärt einen großen Teil der niedrigeren Abschnitts-Spannungsfälle. Wegen unterschiedlicher Widerstands- und Lastflussannahmen ist der Vergleich kein isolierter Softwarevalidierungstest. Die 3-%-Marke in der XLSX ist ein editierbarer Vergleich, kein vereinbarter Projektsollwert.

## Ausgeführte Prüfungen

Alle zwölf Wege unabhängig durch direkte Summation nachgerechnet; Übereinstimmung innerhalb 1e-9 Prozentpunkten. Änderung einer Stammlänge erhöhte das abhängige Endergebnis. Eine einzelne Null-Last senkte die Kreisleistung auf 83,5 W und setzte den zugehörigen Laststrom auf null. Temporäre Änderungen wurden zurückgesetzt. Formel-Fehlersuche ohne Treffer. Beide Tabellenblätter gerendert und visuell geprüft. Keine native Microsoft-Excel-Neuberechnung behauptet.

Kein neuer Kurzschluss- oder Selektivitätsnachweis aus dieser Mappe. Native SIMARIS-Fehlerströme bleiben unter den dort dokumentierten Quellenannahmen gültig; reale Messdaten fehlen.

## Quellen

Vorhandene Leuchtenliste und `Netzmodell_Leitungsabschnitte.csv`; nativer SIMARIS-Bericht S.6. Abgerufen 04.11.2026:

- Prysmian, Electrical Information for Low Voltage Cables, Dokument 18.12.2024, gedruckte S.35: https://asean.prysmian.com/sites/asean.prysmian.com/files/media/documents/241218%20-%20Prysmian%20Electrical%20Information%20for%20Low%20Voltage%20Cables.pdf
- Schneider Electric, Fig.G29: https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions
