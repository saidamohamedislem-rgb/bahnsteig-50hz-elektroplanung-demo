# Ausgefuehrtes ELEK-Free-Modell V1.5

Stand 04.11.2026. Software Cable Pro Web 13.0.0.0 [10/09/26], gewaehlter Kabelstandard IEC 60364-5-52. Rechenlauf ohne Fehlerantwort. Es handelt sich um ein definiertes Demo-Szenario, nicht um Mess- oder Bestandsdaten.

## Aufbau und Eingaben

Quelle -> Quellenabgang B20 -> 10 m Zuleitung -> UV-Incomer B20 -> Abgaenge FA/FB B6 -> jeweils sechs gebuendelte Leuchten.

Die native Ausgabe nennt beide B20-Instanzen identisch `F0 DEMO B20`: eine bei Supply und eine bei UV-Incomer. Im CAD werden sie zur Unterscheidung F0-S und F0-U genannt. Zwei identische B20 in Serie sind keine selektive Staffelung. Die Notwendigkeit der zweiten Stufe ist vor einer realen Geraeteplanung zu pruefen. Es wird keine nachgewiesene Selektivitaet behauptet.

| Eingabe | Wert | Status |
|---|---|---|
| Spannung/Frequenz | 400/230 V, 50 Hz, Spannungs-Toleranz +10 % im Modell | Preliminary |
| Netzform/Quelle | TN, angenommener Quellenfehlerstrom 3 kA | Preliminary |
| Z Quelle laut Software | 0,00843 + j0,08425 Ohm | Verified als abgeleiteter Modellwert |
| Zuleitung | 10 m, Cu/PVC70, D1, L/N/PE 6 mm2 | Preliminary |
| A | L1, 109,7 m, 0,47 A, cos phi 0,95 nacheilend | Preliminary |
| B | L2, 119,7 m, 0,47 A, cos phi 0,95 nacheilend | Preliminary |
| A/B Leiter | L/N 1,5 mm2, separater PE 4 mm2, Cu/PVC70, D1 | Preliminary |
| D1 | im Erdreich in Rohren; Korrekturfaktor 1, Referenzbodentemperatur 20 Grad C | Preliminary |
| Schutz | generische MCB IEC/EN 60898-1: B20/B20/B6/B6 | Preliminary |
| Rechenlimits | gesamt 3 %, Zuleitung 0,5 %, Abgang 1,5 %, TN-Abschaltzeit 0,4 s | frei gewaehlte Szenariowerte |

Die einzelnen Leiterquerschnitte ergeben noch keinen ausgewaehlten Kabelartikel. Insbesondere entspricht L/N 1,5 plus PE 4 nicht einem Kabel 3G1,5. Die tatsaechliche Verlegung, PE-Fuehrung, Hauefung, Temperatur und Produktzulassung fehlen.

## Lastmodell

Die Relux-Lastliste enthaelt weiterhin 8 x 18,5 + 4 x 14 = 204 W, A/B je 102 W. Exakter Szenariostrom 102/(230 x 0,95) = 0,466819 A. Wegen des 0,01-A-Rasters verwendet ELEK je 0,47 A: 102,695 W je Kreis, gesamt 205,39 W bei nominal 230 V, rund 0,681 % Aufschlag. Nominalleistung und gerundete Ersatzlast sind deshalb verschieden.

Alle sechs Lasten eines Kreises liegen elektrisch am jeweiligen letzten Punkt. Das ueberschaetzt den lastbedingten Spannungsfall des gleichartigen verteilten Strangs. Es bildet nicht jeden Abzweig, jede Klemmstelle oder jeden Fehlerort ab. Es ist kein Worst-Case-Nachweis fuer alle Betriebs- und Fehlerbedingungen.

Die UV wurde auf Connected Load gestellt. Maximaler Aussenleiterstrom 0,47 A (L1 und L2 je 0,47, L3 unbelastet). Neutralleiterstrom bei den angenommenen linearen sinusfoermigen Lasten ebenfalls ca. 0,47 A. Die skalare Summe 0,94 A ist kein maximaler UV-Phasenstrom. Treiberoberwellen wurden nicht modelliert.

## Native Ergebnisse

| Groesse | A | B |
|---|---:|---:|
| Abgang Delta U | 1,472 V / 0,640 % | 1,606 V / 0,698 % |
| Kumulierter Delta U | 0,652 % | 0,710 % |
| Iz korrigiert | 22 A | 22 A |
| Zs | 2,3445 + j0,0881 Ohm | 2,5507 + j0,0897 Ohm |
| Ief | 98,03 A | 90,12 A |
| Beruehrungsspannung vor Abschaltung | 60,50 V | 60,68 V |

Zuleitung: Delta U 0,046 V / 0,012 %, Iz 38 A. UV: Ik3 2617,38 A max / 2504,02 A min nach Software-Szenario. Diese Min-/Maxwerte ersetzen keine vom Netzbetreiber bestaetigten Netzdaten.

Referenzpruefung: Ief=230/abs(Zs) ergibt 98,033 bzw. 90,116 A. Generische B6-Obergrenze fuer magnetische Ausloesung Ia=5 x 6=30 A, Zs,max=230/30=7,6667 Ohm. Beide Ief sind im angenommenen TN-Modell groesser. Das bestaetigt die Rechenbeziehung, aber keine reale Abschalt-/Geraetefreigabe. Beruehrungsspannungen ueber 50 V sind nicht als dauerhaft zulaessig zu bewerten; Abschaltung, PE/PA und Netzbedingungen muessen tatsaechlich nachgewiesen werden.

## Schutzkoordination und Grenzen

Der native Kennlinienbericht stellt UV-B20 und FA-B6 mit Kabelgrenze und Fehlerstrommarkierungen dar. FB verwendet denselben generischen B6-Typ, hat aber einen anderen Fehlerstrom. Es wurde ein Kennlinienpaar exportiert, keine Hersteller-Selektivitaetsmatrix.

B20 hat einen magnetischen Toleranzbereich von 60 bis 100 A. Die Endfehlerstroeme 90/98 A liegen darin. Zudem liegen zwei gleiche B20 in Serie. Eine ausschliessliche Abschaltung nur des betroffenen B6 ist nicht garantiert. Hoehere Fehlerstroeme nahe UV sowie Durchlassenergie, reale Icn-Werte und Herstellerkombinationen brauchen eine eigene Bewertung.

Die Softwaretabellen lassen Nennspannung des generischen Geraets offen. Ein konkretes Ausschaltvermoegen ist nicht belegt. Keine automatische Freigabe aus Ib < In < Iz ableiten. LED-Einschaltstrom, Anzahl Treiber pro LS, RCD-Vertraeglichkeit, SPD-Koordination und Bahn-Erdung bleiben offen.

## Bearbeitbare Ablage

Cloud-Netz: https://cablepro.elek.com/app/main/projects/143977/networkcalc/23427

Name: `Bahnsteig V1.5 - A-B Ersatzmodell DEMO`, Projekt `Misc. calculations`. Angemeldetes Benutzerkonto erforderlich. Der aeltere Teilentwurf 23426 ist unvollstaendig und nicht der aktuelle Ergebnisstand.

`ELEK_V15_Eingabeprotokoll.json` archiviert die beobachteten Eingaben ohne Anmeldeinformationen. Es enthaelt auch inaktive Standardfelder; nur die oben aufgefuehrten aktiven Einstellungen gelten als Szenarioannahmen. Kein zugesichertes natives Reimportformat. JSON/CSV-Ergebnistabellen stammen aus demselben erfolgreichen nativen Rechenlauf. PDF-Ausgaben behalten die Free-Preview-Wasserzeichen unveraendert.
