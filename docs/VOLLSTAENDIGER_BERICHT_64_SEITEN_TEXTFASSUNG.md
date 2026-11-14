# Vollständiger Bericht – 64 Seiten (Textfassung)

**Elektroplanung eines Bahnsteigs bei 50 Hz** · Mohamed Saida · Technischer Projektbericht V1.8

> Diese Datei überträgt den **vollständigen auslesbaren Text** des vorhandenen 64-seitigen PDF-Berichts *Bahnsteig_Overleaf_Ueberarbeitet.pdf* in die GitHub-Ansicht, mit Seitenzuordnung. **Sie ist nicht das Original-PDF:** PDF-Seitengestaltung, mathematischer Formelsatz, eingebettete Abbildungen und grafische Originalausgaben können in dieser Textfassung anders erscheinen oder fehlen. Für den visuellen Nachweis die unveränderten originalen CAD-, Relux- und SIMARIS-PDFs und die HD-Abbildungen verwenden.

**Visualisierungen / Originalausgaben:**
- [Berichtsbilder in hoher Auflösung](../07_Projektstaende/Bericht_Abbildungen_HD/README.md)
- [44-seitige Nachweismappe mit den Programmausgaben](../07_Projektstaende/Bahnsteig_V1.8_Arbeitsprobe/00_Vorstellung/00_Nachweismappe_Mohamed_Saida.pdf)
- [Detaillierte GitHub-Lesefassung mit Bildbeispielen](TECHNISCHER_PROJEKTBERICHT_LESFASSUNG.md)

**Wichtig:** Die technische Gesamtplanung ist nicht abgeschlossen; die Projektdateien dienen als Arbeitsprobe, nicht als Ausführungsfreigabe.

---

## PDF-Seite 1 von 64

Technischer Projektbericht

                  Arbeitsprobe zur Elektroplanung




Elektroplanung eines Bahnsteigs
           bei 50 Hz
         Electrical Design of a 50 Hz Railway Platform


      Lichtplanung, CAD-Koordination und elektrische Vorplanung


 Verfasser              Mohamed Saida

 Fachgebiet             Elektrotechnik

 Projektstand           V1.8

 Datengrundlage         Projektunterlagen vom 5. November 2026

---

## PDF-Seite 2 von 64

Kurzfassung

Die Arbeitsprobe untersucht die Allgemeinbeleuchtung eines fiktiven Bahnsteigs
mit einer Grundfläche von 120 m mal 4 m. Ein gemeinsames Koordinatensystem
verbindet das BricsCAD-Modell, die Relux-Lichtberechnung und die elektrische
Zuordnung der Leuchten. Die zwölf Leuchten mit insgesamt 204 W sind abwech-
selnd den Stromkreisen A und B zugeordnet.

Auf der Bodenfläche berechnet Relux im Mittel 18,1 lx, im Minimum 7,96 lx und
eine Gleichmäßigkeit von 0,44. Das SIMARIS-Ersatzlastmodell ergibt kumulierte
Spannungsfälle von 0,596 % und 0,649 %. Die separate Abschnittsrechnung bildet
die Leuchten einzeln ab und ergibt maximal 0,3294 % und 0,3873 %. Der Bericht legt
die Eingaben offen, rechnet einen Leuchtenweg vor und beschreibt den Prüfbedarf
für die spätere Ausführung.



Abstract


This project documents the preliminary design of the general lighting for a fictional
120 m railway platform with a central canopy. The CAD model, lighting simulation
and circuit schedule share twelve luminaire identifiers. The luminaires have a total
rated load of 204 W and are assigned alternately to two circuits.

The Relux floor grid yields an average illuminance of 18.1 lx and an overall
uniformity of 0.44. The report compares voltage drop from a SIMARIS model
with two equivalent end loads against a calculation based on individual cable
sections and distributed loads. It documents the calculation steps and identifies
the lighting requirements, supply data and protection studies needed for detailed
design.




ii

---

## PDF-Seite 3 von 64

Inhaltsverzeichnis
Kurzfassung und Abstract                                                                 ii

Abbildungs-, Tabellen- und Abkürzungsverzeichnis                                        iv

1. Aufgabe und Vorgehensweise                                                            1
   1.1. Zielsetzung und Umfang . . . . . . . . . . . . . . . . . . . . . . . . . .       1
   1.2. Ausgangslage und Arbeitsablauf . . . . . . . . . . . . . . . . . . . . . .       1

2. BricsCAD: Geometrie und Planableitung                                                 2
   2.1. Geometrie und Leuchtenanordnung . . . . . . . . . . . . . . . . . . . .          2
   2.2. Koordination der 2D- und 3D-Daten . . . . . . . . . . . . . . . . . . . .        3
   2.3. Zeichnungen und Stromlaufplan . . . . . . . . . . . . . . . . . . . . . .        4

3. Relux: Modell und Lichtberechnung                                                     5
   3.1. Szenenaufbau und Geometrieübernahme . . . . . . . . . . . . . . . . . .          5
   3.2. Leuchtentypen und Leistung . . . . . . . . . . . . . . . . . . . . . . . .       5
   3.3. Berechnung und Auswertung der Bodenfläche . . . . . . . . . . . . . . .          6
        3.3.1. Isolux und Falschfarben . . . . . . . . . . . . . . . . . . . . . . .     6

4. SIMARIS: Elektrische Vorplanung und Netzmodell                                        8
   4.1. Versorgung und Stromkreisaufteilung . . . . . . . . . . . . . . . . . . .        8
   4.2. Netzmodell in SIMARIS . . . . . . . . . . . . . . . . . . . . . . . . . . .      9
   4.3. Parametrierung und Programmausgaben . . . . . . . . . . . . . . . . . .         10

5. Leitungsberechnung und Schutzbewertung                                               11
   5.1. Spannungsfall mit verteilten Lasten . . . . . . . . . . . . . . . . . . . . .   11
        5.1.1. Rechenbeispiel für Leuchte L11 . . . . . . . . . . . . . . . . . . .     11
   5.2. Ergebnisse und Vergleich der Modelle . . . . . . . . . . . . . . . . . . .      12
   5.3. Schutzkonzept und offene Nachweise . . . . . . . . . . . . . . . . . . . .      13
        5.3.1. Einordnung der Kurzschlusswerte . . . . . . . . . . . . . . . . . .      13

6. Bewertung und Fazit                                                                  14
   6.1. Ergebnisse und Belegstatus . . . . . . . . . . . . . . . . . . . . . . . . .    14
   6.2. Nächste Planungsschritte . . . . . . . . . . . . . . . . . . . . . . . . . .    14

A. Leuchten und Berechnungsbelege                                                       15
   A.1. Zuordnung der zwölf Leuchten . . . . . . . . . . . . . . . . . . . . . . .      15
   A.2. Detailansichten der Stromkreise . . . . . . . . . . . . . . . . . . . . . . .   16

Quellen und Projektunterlagen                                                           17

B. Originalausgaben der Programme                                                       18
   B.1. BricsCAD-Lageplan . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     19
   B.2. BricsCAD-Detailstromlaufplan A/B . . . . . . . . . . . . . . . . . . . . .      20
   B.3. Relux-Gesamtbericht . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   21
   B.4. SIMARIS-Berechnungsbericht . . . . . . . . . . . . . . . . . . . . . . . .      39
   B.5. SIMARIS-Netzansichten . . . . . . . . . . . . . . . . . . . . . . . . . . .     51
   B.6. SIMARIS-Schutzkennlinien . . . . . . . . . . . . . . . . . . . . . . . . .      56



                                                                                        iii

---

## PDF-Seite 4 von 64

Verzeichnisse

Abbildungsverzeichnis
     2.1. BricsCAD-Lageplan mit Leuchtenpositionen und mittiger Überdachung [4].              2
     2.2. Dachzone mit Stützen und Trägern in einer Bildschirmaufnahme aus Brics-
          CAD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       3
     2.3. Schattierte BricsCAD-Gesamtansicht zur räumlichen Kontrolle von Bahn-
          steig und Überdachung. . . . . . . . . . . . . . . . . . . . . . . . . . . .        3
     3.1. Isolux-Linien auf der Bodenfläche. Ausschnitt aus der Relux-Ausgabe [2,
          S. 16]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    6
     3.2. Falschfarben mit Skala und Dachdetail . . . . . . . . . . . . . . . . . . .          7
     4.1. Detailstromlaufplan aus BricsCAD mit gemeinsamer Einspeisung und den
          Beleuchtungsstromkreisen A und B [3]. . . . . . . . . . . . . . . . . . . .          8
     4.2. Aufbau des SIMARIS-Ersatzlastmodells . . . . . . . . . . . . . . . . . .             9
     4.3. Spannungsfallansicht aus dem SIMARIS-Rechenlauf mit den Abgängen A
          und B. Die dokumentierten Werte stammen aus der Projektausgabe [5]. . .             10
     A.1. Kreis A mit den ungeraden Leuchtenkennzeichen. Ausschnitt aus dem
          Detailstromlaufplan [3]. . . . . . . . . . . . . . . . . . . . . . . . . . . .      16
     A.2. Kreis B mit den geraden Leuchtenkennzeichen. Ausschnitt aus dem Detail-
          stromlaufplan [3]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      16


Tabellenverzeichnis
     1.1. Werkzeuge und ihre Aufgaben im Projekt . . . . . . . . . . . . . . . . . .           1
     3.1. Relux-Ergebnisse der Bodenfläche Floor (E) [2] . . . . . . . . . . . . . . .        6
     5.1. Rechenweg vom Abgang A bis zur Leuchte L11 . . . . . . . . . . . . . .              12
     5.2. Elektrische Ergebnisse für die beiden Abgänge [5, 6] . . . . . . . . . . . .        12
     5.3. Schutzgeräte aus der SIMARIS-Auswahl und zugehörige Prüfpunkte . . .                13
     6.1. Belegstatus und Grenzen der Vorplanung [1] . . . . . . . . . . . . . . . .          14
     A.1. Leuchtenliste und kumulierter Spannungsfall je Leuchtenweg . . . . . . .            15


Abkürzungen
CAD      Rechnergestütztes Konstruieren
LDT      EULUMDAT-Datei mit photometrischen Leuchtendaten
LS       Leitungsschutzschalter
PE       Schutzleiter
RCD      Fehlerstrom-Schutzeinrichtung
SPD      Überspannungs-Schutzeinrichtung
UV       Unterverteilung




iv

---

## PDF-Seite 5 von 64

1. Aufgabe und Vorgehensweise


1.1. Zielsetzung und Umfang


Ziel war eine nachvollziehbare Vorplanung für die Allgemeinbeleuchtung eines
kleinen Bahnsteigs. Die Arbeitsprobe sollte zeigen, wie aus einem Lageplan ein
Lichtmodell entsteht und wie sich die Leuchten desselben Modells in Stromkreise
und Leitungsabschnitte übersetzen lassen. Die Leuchtenkennzeichen L01 bis L12
verbinden den Lageplan, den Stromlaufplan und die elektrische Berechnung.

Der Bahnsteig ist ein fiktives Szenario. Die Geometrie, die angenommene Netze-
inspeisung und die dokumentierten Kabelwege bilden die Grundlage für die
Rechenmodelle. Fahrstromversorgung, weitere Bahnhofslasten und eine eigenstän-
dige Sicherheitsbeleuchtung liegen außerhalb des untersuchten Umfangs.



1.2. Ausgangslage und Arbeitsablauf


Ausgangspunkt waren eine Relux-Datei V1.2 mit zwölf Leuchten und vorhandene
CAD-Unterlagen. In BricsCAD wurden die Abmessungen und Leuchtenbezüge
für Lageplan und 3D-Modell übernommen. Für die Lichtberechnung wurden im
Relux-Arbeitsstand V1.3 ergänzende Stützen und Träger berücksichtigt. Boden und
Dach blieben jeweils als vorhandenes Element erhalten. Die Leuchtenpositionen
wurden aus der Ausgangsdatei übernommen. Der Projektstand V1.8 führt die
Lichtausgabe, den CAD-Detailstromlaufplan und die SIMARIS-Ausgaben mit der
Abschnittsrechnung zusammen. [1, 2, 3]


Tabelle 1.1.: Werkzeuge und ihre Aufgaben im Projekt
Werkzeug                   Aufgabe
BricsCAD V26               Lageplan, 3D-Geometrie und Detailstromlaufplan
ReluxDesktop 2026.2        Leuchtenmodell, Bodenraster, Isolux und Falschfarben
SIMARIS design 27.0.1      Netzmodell mit zwei Ersatzlasten, Spannungsfall und
                           Fehlerströme
Excel-Rechenmappe          Laststrom und Spannungsfall je Leitungsabschnitt und
V1.7                       Leuchtenweg




                                                                             1

---

## PDF-Seite 6 von 64

2. BricsCAD: Geometrie und Planableitung


2.1. Geometrie und Leuchtenanordnung


Die Bahnsteigfläche misst 120 m in Längsrichtung und 4 m in Querrichtung.
Der überdachte Abschnitt liegt zwischen 𝑥 = 45 m und 𝑥 = 75 m. Das Dach
ist damit 30 m lang. Die Leuchten liegen auf der Mittellinie bei 𝑦 = 2 m. Ihre
Längskoordinaten reichen von 5 m bis 115 m in Schritten von 10 m. Abbildung 2.1
zeigt die Anordnung im Lageplan. Abbildung 2.2 zeigt die Dachzone im 3D-Modell.
[4, 1]




Abbildung 2.1.: BricsCAD-Lageplan mit Leuchtenpositionen und mittiger Überdachung
                [4].




2

---

## PDF-Seite 7 von 64

2. BricsCAD: Geometrie und Planableitung




Abbildung 2.2.: Dachzone mit Stützen und Trägern in einer Bildschirmaufnahme aus
                BricsCAD.


2.2. Koordination der 2D- und 3D-Daten


Der Original-Lageplan und das 3D-Ausgangsmodell dienten als Geometriegrund-
lage. Für die Koordination war ein gemeinsamer Ursprung entscheidend. Die
𝑥-Achse folgt der Bahnsteiglänge, 𝑦 beschreibt die Querrichtung und 𝑧 die Höhe.
Der CAD-Geometrieabgleich prüfte den Boden von (0, 0, 0) bis (120, 4, 0) und die
Dachplatte mit einer Längsausdehnung von 𝑥 = 45 bis 𝑥 = 75, einem Querbereich
von 𝑦 = −0,5 bis 𝑦 = 4,5 und Höhen von 𝑧 = 4,75 bis 𝑧 = 5,00, jeweils in Metern.
Die Querabmessung der Dachplatte beträgt somit 5 m. Der Abgleich erfasste auch
die Einfügepositionen und Typattribute der zwölf Leuchtenblöcke. [1, 4, 2]




Abbildung 2.3.: Schattierte BricsCAD-Gesamtansicht zur räumlichen Kontrolle von Bahn-
                steig und Überdachung.



                                                                                   3

---

## PDF-Seite 8 von 64

2. BricsCAD: Geometrie und Planableitung


2.3. Zeichnungen und Stromlaufplan


Der Lageplan zeigt die Positionen der Leuchten und die Grenzen der Überdachung.
Das 3D-Modell ergänzt die Höhen und den räumlichen Bezug von Stützen, Trägern
und Dach. Für den Lichtabgleich gibt es eine eigene CAD-Koordinationsdatei. Im
Detailstromlaufplan wurden die Leuchtenkennzeichen aus dem Lageplan mit der
Stromkreisbelegung verknüpft. Der Plan enthält eine gemeinsame Einspeisung,
die beiden Abgänge A und B sowie 24 bezeichnete Stamm- und Stichabschnitte.
Diese IDs wurden gegen die Rechentabelle abgeglichen.

Der Lageplan und der Detailstromlaufplan liegen als DWG und DXF sowie als
PDF-Ausgabe vor. Das 3D-Modell und der Koordinationsplan sind als DWG
verfügbar. Die Plan-PDFs folgen im Anhang der Originalausgaben. [3, 4, 1]




4

---

## PDF-Seite 9 von 64

3. Relux: Modell und Lichtberechnung


3.1. Szenenaufbau und Geometrieübernahme


Die Arbeitsdatei V1.3 baut auf dem gesicherten Relux-Stand V1.2 auf. Aus der
koordinierten 3D-Geometrie wurden die ergänzenden Stützen und Träger als
separates OBJ-Modell übernommen. Die Relux-Szene behielt die vorhandene
Bodenfläche und Dachplatte. Die bestehenden zwölf Leuchten wurden in ihrer
Lage und Zuordnung übernommen. Dadurch lassen sich CAD-Plan, Relux-Liste
und Stromkreiszuordnung über dieselben Kennzeichen vergleichen. Nach der
Übernahme der zusätzlichen Geometrie wurde die Kunstlichtberechnung erneut
ausgeführt. [1, 2]

Die RDF-Datei, beide LDT-Dateien und der OBJ-Export bilden die bearbeitbare
Grundlage. Der Originalbericht enthält die Leuchtenliste, den Grundriss, das
vollständige Bodenraster und die 3D-Ergebnisansicht. [2, 1]



3.2. Leuchtentypen und Leistung


Die Lichtverteilungen stammen aus den im Relux-Modell hinterlegten Schmidt-
Strahl-LDT-Dateien mit einer angegebenen Farbtemperatur von 4000 K. In den
offenen Bereichen sind acht Leuchten mit 18,5 W und BB-Optik bei 4,5 m modelliert.
Die vier Leuchten L05 bis L08 in der Dachzone haben je 14 W und liegen bei 4,3 m.
Damit beträgt die Nennleistung

                       𝑃ges = 8 · 18,5 W + 4 · 14 W = 204 W.

Die vollständige Zuordnung von Leuchtentyp, Position, Stromkreis und Span-
nungsfall steht in Tabelle A.1. Die Nennleistung dient als Lastansatz für die
elektrische Vorplanung. [2, S. 5]




                                                                                5

---

## PDF-Seite 10 von 64

3. Relux: Modell und Lichtberechnung


3.3. Berechnung und Auswertung der Bodenfläche


Die Auswertung bezieht sich auf das horizontale Bodenraster Floor (E) der Relux-
Szene Exterior 2. Der im Projekt eingestellte Wartungsfaktor beträgt 0,8. Relux gibt
für das Raster die Beleuchtungsstärken aus Tabelle 3.1 aus. Die Gleichmäßigkeit
ergibt sich aus dem Verhältnis von minimaler zu mittlerer Beleuchtungsstärke. Mit
den gerundeten Berichtswerten gilt 𝑈0 = 𝐸min /𝐸m ≈ 0,44. [2, S. 7–18]


Tabelle 3.1.: Relux-Ergebnisse der Bodenfläche Floor (E) [2]
Kenngröße                                                Zeichen    Berechneter Wert
Mittlere Beleuchtungsstärke                              𝐸m               18,1 lx
Minimale Beleuchtungsstärke                              𝐸min             7,96 lx
Maximale Beleuchtungsstärke                              𝐸max              37 lx
Gleichmäßigkeit                                          𝑈0                0,44



3.3.1. Isolux und Falschfarben


Die Rastertabelle enthält die Einzelwerte. Isolux-Linien verbinden Punkte gleicher
Beleuchtungsstärke und zeigen den räumlichen Verlauf. Die Falschfarbenansicht
ordnet jedem Wertebereich eine Farbe zu. Abbildungen 3.1 und 3.2 zeigen die
Verteilung. Das Minimum beträgt rund 44 % des Mittelwerts. Für eine Sollbe-
wertung sind die konkreten Lichtanforderungen einschließlich Mindestwert und
Gleichmäßigkeit festzulegen.




Abbildung 3.1.: Isolux-Linien auf der Bodenfläche. Ausschnitt aus der Relux-Ausgabe [2,
                S. 16].




6

---

## PDF-Seite 11 von 64

3. Relux: Modell und Lichtberechnung




Abbildung 3.2.: Falschfarben der Bodenfläche, Skala und Ergebnisübersicht sowie ver-
                größerter Dachausschnitt. Ausschnitte aus der Relux-Ausgabe [2, S. 18].




                                                                                     7

---

## PDF-Seite 12 von 64

4. SIMARIS: Elektrische Vorplanung und Netzmodell


4.1. Versorgung und Stromkreisaufteilung


Das Modell geht von einer TN-S-Niederspannungsversorgung mit 400 V zwischen
den Außenleitern, 230 V gegen Neutralleiter und 50 Hz aus. Die angesetzten
minimalen und maximalen Kurzschlussströme an der Quelle betragen für die
ein- und dreipolige Betrachtung 1,5 kA und 3 kA. Für die Leuchtenlasten gilt
cos 𝜑 = 0,95. Diese Werte sind Eingaben des fiktiven Szenarios. [5]

Stromkreis A versorgt an L1–N die Leuchten mit ungeradem Kennzeichen. Strom-
kreis B versorgt an L2–N die geraden Kennzeichen. Beide Kreise enthalten vier
Leuchten mit 18,5 W und zwei mit 14 W. Pro Kreis ergeben sich damit 102 W und
ein rechnerischer Betriebsstrom von rund 0,467 A bei Nennspannung. Die abwech-
selnde Belegung verteilt die verbleibenden Leuchten über die Bahnsteiglänge,
wenn ein einzelner Endstromkreis ausfällt. Die Zuleitung und die Untervertei-
lung bilden gemeinsame Ausfallpunkte. Die Beleuchtungsstärke bei Ausfall eines
Kreises bleibt ein eigener Prüfpunkt. [3, 6]




Abbildung 4.1.: Detailstromlaufplan aus BricsCAD mit gemeinsamer Einspeisung und
                den Beleuchtungsstromkreisen A und B [3].


8

---

## PDF-Seite 13 von 64

4. SIMARIS: Elektrische Vorplanung und Netzmodell


4.2. Netzmodell in SIMARIS


Die Unterverteilung wird im Modell über eine 10 m lange Cu/PVC-Zuleitung mit
4 mm2 je Leiter versorgt. Die einphasigen Abgänge A und B sind mit 109,7 m bzw.
119,7 m und jeweils 1,5 mm2 für L, N und PE angesetzt. SIMARIS setzt je Abgang
die gesamte Nennleistung von 102 W als Ersatzlast am Leitungsende an. In diesem
Modell fließt der Laststrom des jeweiligen Kreises über die gesamte Abgangslänge.
[5, S. 6]

Die native Ausgabe dokumentiert Verlegeart C, Gesamtfaktor 1 und eine Leiter-
temperatur von 55 °C für die Spannungsfallrechnung. Der Lastfluss wurde in der
Einstellung balanced ausgewertet. Der ausgewiesene Abgangsstrom beträgt jeweils
0,465 A. Die Auswertung übernimmt diesen nativen Wert für die Modellprüfung.
Die Abschnittsrechnung verwendet dagegen den aus Leistung, Nennspannung
und Leistungsfaktor ermittelten Strom. [5, 6]

                                TN-S-Einspeisung
                                400 V/230 V, 50 Hz

                                          Zuleitung 10 m

                               Unterverteilung UV01




            Kreis A auf L1–N                               Kreis B auf L2–N
             109,7 m, 102 W                                 119,7 m, 102 W

Abbildung 4.2.: Aufbau des SIMARIS-Ersatzlastmodells mit je einer gebündelten Leuch-
                tenlast pro Abgang. Schematische Darstellung nach der Projektdoku-
                mentation [5].

Abbildung 4.2 zeigt die Modellgrenze. Das SIMARIS-Projekt ermittelt Werte
an der Unterverteilung und den Endpunkten A und B. Der CAD-Detailplan
in Abbildung 4.1 enthält die einzelnen Abzweige und liefert die Wege für die
Abschnittsrechnung.




                                                                                  9

---

## PDF-Seite 14 von 64

4. SIMARIS: Elektrische Vorplanung und Netzmodell


4.3. Parametrierung und Programmausgaben


Der Rechenlauf verwendet in SIMARIS design den IEC-Rechenstandard mit dem in
der Projektdokumentation ausgewiesenen Quellenmodell. Die Gerätetemperatur
ist mit 45 °C angesetzt. Für den maximalen Kurzschlussstrom verwendet das
Modell eine Leitertemperatur von 20 °C, für die Abschaltbedingung 80 °C. Die im
Programm hinterlegte Netzspannungsfallgrenze von 8 % ist ein Modellparameter.
Ein verbindlicher Grenzwert für die fiktive Anlage wurde nicht festgelegt. [5, 1]

Der Rechenlauf lieferte eine Projektdokumentation mit Lasten, Leitungsdaten,
Spannungsfall, Kurzschlusswerten und Schutzgeräten. Die gesonderten Netzan-
sichten und Kennlinien dokumentieren den gleichen Modellstand. Das Netzprojekt
liegt als SDX und der exportierte Stand als SX vor. Der Netzplan wurde zusätzlich
als DWG exportiert. [5, 7, 1]




Abbildung 4.3.: Spannungsfallansicht aus dem SIMARIS-Rechenlauf mit den Abgängen
                A und B. Die dokumentierten Werte stammen aus der Projektausgabe
                [5].




10

---

## PDF-Seite 15 von 64

5. Leitungsberechnung und Schutzbewertung


5.1. Spannungsfall mit verteilten Lasten


Im CAD-Detailplan bestehen beide Kreise aus jeweils sechs Stammstücken und
sechs Stichen. Auf jedem Stammstück zählt nur die Summe der nachgelagerten
Leuchtenleistungen. Ein Stich führt den Strom seiner einzelnen Leuchte. Für
einen Abschnitt 𝑗 mit der Länge 𝑙 𝑗 und dem Leiterquerschnitt 𝑆 berechnet die
Excel-Mappe

                                       𝑘 hinter 𝑗 𝑃 𝑘
                                  ∑︁
                           𝐼𝑗 =               ,                              (5.1)
                                  𝑈0 cos 𝜑
                                  𝑙𝑗
                          𝑅𝑗 = 𝜌 ,         𝑋𝑗 = 𝑥′ 𝑙𝑗 ,                      (5.2)
                                   𝑆
                         Δ𝑈 𝑗 = 2𝐼 𝑗 𝑅 𝑗 cos 𝜑 + 𝑋 𝑗 sin 𝜑 .
                                     (︁                   )︁
                                                                             (5.3)

Hier bezeichnet 𝑈0 = 230 V die Nennspannung gegen Neutralleiter. Der Faktor zwei
berücksichtigt Hin- und Rückleiter gleichen Querschnitts. Die Referenzrechnung
setzt 𝜌 = 0,0225 Ω mm2/m und 𝑥 ′ = 0,000 08 Ω/m an. Für jede Leuchte werden
die Spannungsfälle der Stammstücke ihres Wegs und ihres eigenen Stichs addiert.
Hinzu kommt der aus SIMARIS übernommene Zuleitungsanteil von 0,010 %. Die
Mappe verwendet die Nennspannung für alle Lastströme und führt keine iterative
Lastflussrechnung aus. [6, 8]



5.1.1. Rechenbeispiel für Leuchte L11


L11 liegt am Ende von Kreis A. Im ersten Stammstück A_TR1 fließt der Strom
aller sechs Leuchten. Hinter dem ersten Abzweig verbleiben 83,5 W. Auf dem
letzten Stammstück und dem Stich zu L11 verbleiben jeweils 18,5 W. Für A_TR1
ergeben sich mit 4,1 m Länge ein Strom von 0,4668 A, ein Leiterwiderstand von
0,0615 Ω und ein Spannungsfall von 0,054 64 V. Tabelle 5.1 zeigt den Beitrag jedes
Abschnitts zum Spannungsfall an L11. [6, 3]




                                                                               11

---

## PDF-Seite 16 von 64

5. Leitungsberechnung und Schutzbewertung


Tabelle 5.1.: Rechenweg vom Abgang A bis zur Leuchte L11
               Abschnitt    Länge (m)     Last dahinter (W)     Δ𝑈 𝑗 (V)
               A_TR1             4,1             102,0          0,054 64
               A_TR2            20,0              83,5          0,218 21
               A_TR3            20,0              65,0          0,169 86
               A_TR4            20,0              51,0          0,133 28
               A_TR5            20,0              37,0          0,096 69
               A_TR6            20,0              18,5          0,048 35
               A_AB6             5,6              18,5          0,013 54


Die ungerundete Summe für diesen Weg beträgt rund 0,734 56 V. Mit dem Zulei-
tungsanteil ergibt sich

                           0,734 56 V
                 Δ𝑢L11 =              · 100 % + 0,010 % ≈ 0,3294 %.
                             230 V

Kreis B hat dieselbe Lastabfolge. Sein erstes Stammstück ist 10 m länger, während
dort noch die volle Last fließt. Das erklärt die zusätzliche Differenz von rund 0,058
Prozentpunkten zwischen L11 und L12 innerhalb der Abschnittsrechnung. [6]



5.2. Ergebnisse und Vergleich der Modelle


Tabelle 5.2 stellt die kumulierten Werte gegenüber. Im Abschnittsmodell liegen die
höchsten Spannungsfälle an L11 und L12. Die Werte sind kleiner als im SIMARIS-
Ersatzlastmodell, weil nach jedem Abzweig weniger Last auf den folgenden
Stammstücken liegt. Die Widerstands- und Lastflussannahmen unterscheiden sich
ebenfalls. Die Differenz lässt sich daher nicht allein der Lastverteilung zuordnen.


Tabelle 5.2.: Elektrische Ergebnisse für die beiden Abgänge [5, 6]
Kenngröße                                                            Kreis A    Kreis B
Leuchtennennleistung                                                  102 W      102 W
Kumulierter Spannungsfall in SIMARIS                                 0,596 %    0,649 %
Maximaler Spannungsfall der Abschnittsrechnung                       0,3294 %   0,3873 %
Minimaler einpoliger Fehlerstrom am Ende (SIMARIS)                   59,029 A   54,374 A
Modell-Strombelastbarkeit der Abgangsleitung                          19,5 A     19,5 A




12

---

## PDF-Seite 17 von 64

5. Leitungsberechnung und Schutzbewertung


5.3. Schutzkonzept und offene Nachweise


SIMARIS wählt in diesem Szenario eine gG-Sicherung mit 25 A für die Einspeisung
sowie je Abgang einen Leitungsschutzschalter B1 mit 10 kA Bemessungsschaltver-
mögen und einen RCD Typ A mit 25 A Bemessungsstrom und 30 mA Bemessungs-
differenzstrom. Für die Abgänge lässt sich im Modell die Beziehung 𝐼B ≤ 𝐼n ≤ 𝐼Z
anhand von 0,465 A, 1 A und 19,5 A nachvollziehen. An der Unterverteilung liegen
die modellierten dreipoligen Kurzschlussströme zwischen 1,132 kA und 2,079 kA.
Die Auswertung der Abschaltbedingung im SIMARIS-Bericht gilt für die dort
hinterlegten Quellen- und Leitungsdaten. [5]


Tabelle 5.3.: Schutzgeräte aus der SIMARIS-Auswahl und zugehörige Prüfpunkte
Position              Kandidat              Offener Prüfpunkt
Einspeisung           gG 25 A               Abstimmung mit Anschlusskapazität
                                            und Vorsicherung
Abgang A/B            LS B1, 10 kA          Einschaltstrom der Treiber, Abschal-
                                            tung und thermische Beanspruchung
Je Endstromkreis      RCD Typ A, 30 mA      Verträglichkeit mit Treibern und be-
                                            triebliche Ableitströme


Die Quelle ist im Modell mit 20 A bemessen. Die vorgeschlagene 25 A-Sicherung
muss deshalb mit der verfügbaren Anschlusskapazität und der vorgelagerten Ab-
sicherung abgestimmt werden. Der Kennlinienexport zeigt die Gerätekennlinien,
enthält jedoch kein ausgefülltes Gesamturteil zur Selektivität. Für die Geräteaus-
wahl fehlen insbesondere die Einschalt- und Ableitströme der LED-Treiber sowie
der Nachweis der Schutzkoordination und der thermischen Kurzschlussfestigkeit.
Erdung, bahnspezifischer Potenzialausgleich und Überspannungsschutz sind als
eigene Planungspunkte weiterzuführen. [5, 7, 1]



5.3.1. Einordnung der Kurzschlusswerte


Die Auswertung unterscheidet die Unterverteilung vom Ende des jeweiligen
Abgangs. Dort begrenzt die zusätzliche Leitungsimpedanz den Fehlerstrom. Für
L–N bzw. L–PE weist die native Tabelle an A maximal 89,230 A und an B maximal
82,146 A aus. Den kleineren Endwert von B begleitet im Modell der längere
Abgang. Die Kennlinienausgabe enthält je eine Ansicht für die Abgänge A und B.
Zur Bewertung der Selektivität fehlen ein dokumentierter Grenzstrom und die
Gerätekoordination mit der tatsächlichen Vorsicherung. [5, 7]



                                                                               13

---

## PDF-Seite 18 von 64

6. Bewertung und Fazit


6.1. Ergebnisse und Belegstatus


Der Lageplan, die Lichtberechnung und der Detailstromlaufplan verwenden die-
selbe Zuordnung der zwölf Leuchten. Dadurch lässt sich beispielsweise L11 im
Lageplan bei 𝑥 = 105 m, im Stromkreis A und am Ende des längsten Leuchten-
wegs dieses Kreises wiederfinden. Die Relux-Ausgabe belegt die Verteilung der
Beleuchtungsstärke im untersuchten Modell. Der Vergleich der beiden elektri-
schen Rechnungen zeigt, wie stark die Abbildung der Lasten den ermittelten
Spannungsfall beeinflusst.


Tabelle 6.1.: Belegstatus und Grenzen der Vorplanung [1]
Status                 Gegenstand
Belegt                 Übereinstimmung der Leuchtenzuordnung, native Relux-
                       und SIMARIS-Ausgaben, CAD-Detailplan und reproduzier-
                       bare Abschnittsrechnung
Vorläufig              Einspeise- und Verlegeannahmen, Schutzgeräte aus der
                       Modellauswahl
Offen                  Licht-Sollwerte, Sicherheitsbeleuchtung, tatsächliche Kabel-
                       wege, Selektivität, Erdung, bahnspezifischer Potenzialaus-
                       gleich und Überspannungsschutz




6.2. Nächste Planungsschritte


Für die Fortführung sind zuerst die Licht-Sollwerte und der Umfang der Si-
cherheitsbeleuchtung festzulegen. Für die elektrische Ausführung werden die
tatsächlichen Einspeisedaten, Kabelwege, Verlegebedingungen und Gerätedaten
benötigt. Darauf aufbauend können die Schutzorgane, Selektivität, Erdung und
der Überspannungsschutz projektbezogen bewertet werden. Der vorliegende
Stand dokumentiert die Vorplanung und hält Berechnung, Annahmen und offene
Nachweise für diese Schritte getrennt.




14

---

## PDF-Seite 19 von 64

A. Leuchten und Berechnungsbelege


A.1. Zuordnung der zwölf Leuchten


In Tabelle A.1 ist 𝑥 die Längskoordinate und 𝑧 die Montagehöhe im Modell. Alle
Leuchten liegen bei 𝑦 = 2 m. Der Spannungsfall ist der kumulierte Wert aus der
Abschnittsrechnung einschließlich des angesetzten Zuleitungsanteils. [3, 6]


Tabelle A.1.: Leuchtenliste und kumulierter Spannungsfall je Leuchtenweg
                Leuchte    Kreis   𝑥 (m)   𝑧 (m)   𝑃 (W)    Δ𝑈 (%)
                L01          A        5      4,5    18,5    0,0396
                L02          B       15      4,5    18,5    0,0976
                L03          A       25      4,5    18,5    0,1345
                L04          B       35      4,5    18,5    0,1925
                L05          A       45      4,3    14,0    0,2068
                L06          B       55      4,3    14,0    0,2647
                L07          A       65      4,3    14,0    0,2647
                L08          B       75      4,3    14,0    0,3227
                L09          A       85      4,5    18,5    0,3084
                L10          B       95      4,5    18,5    0,3663
                L11          A      105      4,5    18,5    0,3294
                L12          B      115      4,5    18,5    0,3873




                                                                              15

---

## PDF-Seite 20 von 64

A. Leuchten und Berechnungsbelege


A.2. Detailansichten der Stromkreise


Die Ausschnitte zeigen die Stamm- und Stichabschnitte für die Zuordnung zur
Berechnungstabelle. Die vollständige Zeichnung steht in Abbildung 4.1. Beide
Kreise haben sechs Stammstücke und sechs Stiche. Das erste Stammstück misst in
A 4,1 m und in B 14,1 m. Die nachfolgenden Stammstücke sind jeweils 20 m lang.
Die Stichlängen betragen 5,4 m in der Dachzone und 5,6 m im offenen Bereich.
Diese Längen stammen aus dem schematischen Abschnittsmodell. [3, 6]




Abbildung A.1.: Kreis A mit den ungeraden Leuchtenkennzeichen. Ausschnitt aus dem
                Detailstromlaufplan [3].




Abbildung A.2.: Kreis B mit den geraden Leuchtenkennzeichen. Ausschnitt aus dem
                Detailstromlaufplan [3].




16

---

## PDF-Seite 21 von 64

Quellen und Projektunterlagen

[1] Mohamed Saida. Bahnsteig 50 Hz – Bericht-Grundlage und Prüfstatus. Projekt-
     stand V1.8. Projektinterne Dokumentation. 5. Nov. 2026.
[2] ReluxDesktop. Bahnsteigbeleuchtung: Relux-Originalbericht. Modell V1.3, Szene
     Exterior 2, Bodenraster Floor (E). Projektdatei und Originalausgabe in der
     Nachweismappe V1.8.
[3] Mohamed Saida. Bahnsteig 50 Hz: Detailstromlaufplan A/B. BricsCAD V26, PDF-
     und DWG-Ausgabe im Projektstand V1.8. 5. Nov. 2026.
[4] Mohamed Saida. Bahnsteig 50 Hz: Lageplan und 3D-Modell. BricsCAD-
     Unterlagen V1.3 im Projektstand V1.8.
[5] Siemens SIMARIS design. Bahnsteig V1.7: Projektdokumentation der Netzberech-
     nung. Projektbearbeiter Mohamed Saida. Nativer Bericht mit 12 Seiten in der
     Nachweismappe V1.8. 5. Nov. 2026.
[6] Mohamed Saida. Abschnittsrechnung V1.7: Spannungsfall an zwölf Leuchten.
     Excel-Arbeitsmappe und dokumentierte Referenzrechnung im Projektstand
     V1.8. 4. Nov. 2026.
[7] Siemens SIMARIS design. Bahnsteig V1.7: Schutzkennlinien. Projektbearbeiter
     Mohamed Saida. Nativer Export mit fünf Seiten in der Nachweismappe V1.8.
     5. Nov. 2026.
[8] Schneider Electric. Calculation of voltage drop in steady load conditions. Abbildung
     G29, Ansatz für Außenleiter gegen Neutralleiter. Electrical Installation Guide.
     url: https://www.electrical-installation.org/enwiki/Calculation_
     of_voltage_drop_in_steady_load_conditions (besucht am 04. 11. 2026).




                                                                                     17

---

## PDF-Seite 22 von 64

B. Originalausgaben der Programme

Die folgenden Ausgaben ergänzen den Bericht um vollständige Zeichnungen,
Berechnungstabellen und Kennlinien. Die Herkunft und der jeweilige Projektstand
sind in den Ausgaben angegeben.

Programm             Anlagen

BricsCAD             Lageplan und Detailstromlaufplan A/B
Relux                Gesamtbericht mit Leuchtenliste, Raster, Isolux, 3D-Ansicht
                     und Falschfarben
SIMARIS              Berechnungsbericht, Netzansichten und Schutzkennlinien




18

---

## PDF-Seite 23 von 64

BAHNSTEIG 50 Hz | V1.3 | LAGEPLAN
     Arbeitsprobe - PRELIMINARY / keine Ausfuehrungsfreigabe | 04.11.2026



     12 Leuchten | 8 x 18.5 W + 4 x 14 W = 204 W

     A: L01/03/05/07/09/11 = 102 W | B: L02/04/06/08/10/12 = 102 W
     Trassen schematisch: A y=3.1 / B y=0.9; reale Kabelwege und Verlegeart fehlen.

                                                                     Ueberdachung X=45...75 m
     UV-01                                                                                30.00 m
         L01/A         L02/B          L03/A         L04/B          L05/A         L06/B              L07/A      L08/B          L09/A           L10/B        L11/A    L12/B


                                                                                                                                                                             4.00 m


         18.5 W        18.5 W         18.5 W        18.5 W        14.0 W         14.0 W             14.0 W     14.0 W         18.5 W         18.5 W        18.5 W   18.5 W


                                                                                 120.00 m

     QUERSCHNITT UNTER DACH - schematisch, geometrische Hoehen in m
                                                                                    PLANUNGSSTATUS
                                                                                    Verified: native Relux-Positionen L01-L12 / Boden 120 x 4 m
                    Dach UK 4.75 / OK 5.00                                          Preliminary: Hoehen, Stuetzen, Trassen, Materialreflexion
                    Leuchte unter Dach z=4.30                                       Missing: Netzform, Netzimpedanz, Kabel- und Schutzbemessung
                    Freie Abschnitte z=4.50
                                                                                    A/B verbessert Verfuegbarkeit; ersetzt keine Sicherheitsbeleuchtung.
                                                                                    Kein automatischer Anschluss von PE/PA an die Fahrschiene.


     Einheit: 1 ZE = 1 m | Geometrie 1:1; PDF-Darstellung skaliert | B13-LP-01
19

---

## PDF-Seite 24 von 64

BAHNSTEIG 50 Hz - STROMLAUFPLAN A/B
     Mohamed Saida - V1.8 - 05.11.2026 - Fiktive Arbeitsprobe / Vorplanung

       NETZANNAHME TN-S                         FSO 1.1a: gG25         10 m Cu/PVC70, 3L+N+PE
                                                                                                                       UV-01 / gemeinsame Einspeisung
20




       400/230 V, 50 Hz                         3NA3810                                                                Quellenbemessung 20 A vs. gG25: Abstimmung offen
       Ik1 / Ik3: 1.5...3 kA                    Sockel 3NH4030         L/N/PE 4 mm2 - Verlegeart C                     Getrennte A/B-Abgaenge; kein Sicherheitsnetz




               KREIS A / L1-N - 6 LEUCHTEN / 102 W

                FA    B1 A       RCD Typ A         A_TR1   4.1 m           A_TR2   20 m          A_TR3   20 m          A_TR4   20 m          A_TR5   20 m          A_TR6   20 m
                5SY41016         25 A / 30 mA
                Icn 10 kA        5SV33126
                                                                        A_AB1                 A_AB2                 A_AB3                 A_AB4                 A_AB5                    A_AB6
                                                                        5.6 m                 5.6 m                 5.4 m                 5.4 m                 5.6 m                    5.6 m



                                                                     L01                   L03                   L05                   L07                   L09                   L11
                                                                    18.5 W                18.5 W                14 W                  14 W                  18.5 W                18.5 W
                                                                    z=4.5 m               z=4.5 m               z=4.3 m               z=4.3 m               z=4.5 m               z=4.5 m

               KREIS B / L2-N - 6 LEUCHTEN / 102 W

                FB    B1 A       RCD Typ A         B_TR1   14.1 m          B_TR2   20 m          B_TR3   20 m          B_TR4   20 m          B_TR5   20 m          B_TR6   20 m
                5SY41016         25 A / 30 mA
                Icn 10 kA        5SV33126
                                                                        B_AB1                 B_AB2                 B_AB3                 B_AB4                 B_AB5                    B_AB6
                                                                        5.6 m                 5.6 m                 5.4 m                 5.4 m                 5.6 m                    5.6 m



                                                                     L02                   L04                   L06                   L08                   L10                   L12
                                                                    18.5 W                18.5 W                14 W                  14 W                  18.5 W                18.5 W
                                                                    z=4.5 m               z=4.5 m               z=4.3 m               z=4.3 m               z=4.5 m               z=4.5 m


      LEITUNGEN / FUNKTION
      Stamm und Stich: Cu/PVC70, L/N/PE 1.5 mm2 als Modellkandidat. Reale Verlegung nicht festgelegt.

      Einpoliges Funktionsschema, nicht massstaeblich. N_A und N_B nach den RCDs getrennt; PE durchgaengig.

      Schutzgeraete nach SIMARIS-Autoauswahl; LED-Inrush / Selektivitaet / SPD und Bahn-PA noch offen.

      12 Leuchten / 24 Abschnitte: IDs und Laengen entsprechen der V1.7-Formelmappe. Gesamtleistung 204 W.

      B18-SLP-01 - Bearbeiter: Mohamed Saida - Planungsstand: Preliminary

---

## PDF-Seite 25 von 64

B50HZ-DEMO-V04

Installation : Bahnsteigmodernisierung 120 m

Project number         :
Customer               : Bahnsteigbeleuchtung 50 Hz
Processed by           : Portfolio-Demoprojekt
Date                   : 03.11.2026




The following values are based on precise calculations performed on calibrated lamps and luminaires, and their configurations, whereby
gradual, unavoidable deviations can occur in practice. All guarantee claims are excluded for the specified data.

This exclusion of liability applies irrespective of the legal grounds for both damages and consequential damages suffered by users and third
parties.



                                                  -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                    Page 1/17




                                                                                                                                    21

---

## PDF-Seite 26 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026

1       Luminaire data
1.1     Schmidt-Strahl, Basic-Bahnsteigleuchte... (PSH-395381-G2-S...)
1.1.1 Data sheet


Manufacturer: Schmidt-Strahl



PSH-395381-G2-SKII-4000K-6-Ø60-76-Auf-0°-17W-DB703 #100575                        Basic-Bahnsteigleuchte 17W 4000K


Luminaire data                                                             Equipped with
Luminaire efficiency               :   78.19%                              Quantity               :   1
Luminaire efficacy                 :   146.71 lm/W                         Designation            :   395381-4000-17
Classification                     :   A40 ¯ 100% ­ 0%                     Colour                 :   4000
CIE Flux Codes                     :   52 86 99 100 78                     Luminous flux          :   3190 lm
Glare                              :   G*5 / D6                            Colour reproduction    :   80
Power                              :   17 W
Luminous flux                      :   2494 lm

Dimensions                         :   590 mm x 305 mm x 135 mm




                                             -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                           Page 2/17




         22

---

## PDF-Seite 27 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026

1       Luminaire data
1.2     Schmidt-Strahl, Basic-Bahnsteigleuchte... (PSH-395381-G2-B...)
1.2.1 Data sheet


Manufacturer: Schmidt-Strahl



PSH-395381-G2-BB-SKII-4000K-6-Ø76-Auf-0°-DB703 #100325                     Basic-Bahnsteigleuchte 18,5W Optik BB
4000K


Luminaire data                                                             Equipped with
Luminaire efficiency               :   73.17%                              Quantity              :   1
Luminaire efficacy                 :   137.95 lm/W                         Designation           :   395381-4000K-BB
Classification                     :   A30 ¯ 100% ­ 0%
CIE Flux Codes                     :   28 70 97 100 73                     Colour                :   4000
UGR 4H 8H                          :   30.2 / 30.1                         Luminous flux         :   3488 lm
Power                              :   18.5 W                              Colour reproduction   :   80
Luminous flux                      :   2552 lm

Dimensions                         :   590 mm x 305 mm x 135 mm




                                             -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                          Page 3/17




                                                                                                          23

---

## PDF-Seite 28 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026

1       Luminaire data
1.3     Schmidt-Strahl, Basic-Bahnsteigleuchte... (PSH-395381-G2-S...)
1.3.1 Data sheet


Manufacturer: Schmidt-Strahl



PSH-395381-G2-SKII-4000K-6-Ø60-76-Auf-0°-14W-DB703 #100116                        Basic-Bahnsteigleuchte 14W 4000K


Luminaire data                                                             Equipped with
Luminaire efficiency               :   78.19%                              Quantity               :   1
Luminaire efficacy                 :   146.6 lm/W                          Designation            :   395381-4000-14
Classification                     :   A40 ¯ 100% ­ 0%                     Colour                 :   4000
CIE Flux Codes                     :   52 86 99 100 78                     Luminous flux          :   2625 lm
Glare                              :   G*5 / D6                            Colour reproduction    :   80
Power                              :   14 W
Luminous flux                      :   2052 lm

Dimensions                         :   590 mm x 305 mm x 135 mm




                                             -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                           Page 4/17




         24

---

## PDF-Seite 29 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026

2       Exterior 2
2.1     Calculation results, Exterior 2
2.1.1 Luminaire list


-----                                  1
    Luminaire                                      Position (x/y/z)           Aiming point (x/y) Rotation Tilt
Basic-Bahnsteigleuch...                1      5.00 m 2.00 m       4.50 m     5.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...                2     15.00 m 2.00 m       4.50 m    15.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...                3     25.00 m 2.00 m       4.50 m    25.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...                4     35.00 m 2.00 m       4.50 m    35.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...                5     45.00 m 2.00 m       4.30 m    45.00 m    3.63 m     0.0°    0.0°
Basic-Bahnsteigleuch...                6     55.00 m 2.00 m       4.30 m    55.00 m    3.63 m     0.0°    0.0°
Basic-Bahnsteigleuch...                7     65.00 m 2.00 m       4.30 m    65.00 m    3.63 m     0.0°    0.0°
Basic-Bahnsteigleuch...                8     75.00 m 2.00 m       4.30 m    75.00 m    3.63 m     0.0°    0.0°
Basic-Bahnsteigleuch...                9     85.00 m 2.00 m       4.50 m    85.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...               10     95.00 m 2.00 m       4.50 m    95.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...               11    105.00 m 2.00 m       4.50 m   105.00 m    2.00 m     0.0°    0.0°
Basic-Bahnsteigleuch...               12    115.00 m 2.00 m       4.50 m   115.00 m    2.00 m     0.0°    0.0°




                                           -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                           Page 5/17




                                                                                                           25

---

## PDF-Seite 30 von 64

Object                    : B50HZ-DEMO-V04
Installation              : Bahnsteigmodernisierung 120 m
Project number            :
Date                      : 03.11.2026



2.1     Description, Exterior 2
2.1.2 Floor plan




y [m]

  2.5
 -0.5




           0         10            20   30    40      50      60       70         80   90   100   110     120 x [m]




                                             -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                        Page 6/17




         26

---

## PDF-Seite 31 von 64

Object                       : B50HZ-DEMO-V04
Installation                 : Bahnsteigmodernisierung 120 m
Project number               :
Date                         : 03.11.2026

2        Exterior 2
2.2      Calculation results, Exterior 2
2.2.1 Table, Floor (E)


  [m]
        7.98 8.49 9.44 10.4 11.5 12.3 12.8 13.1 13.1 13.1 13.1 13.4 13.5 13.9 14.5 14.8 15.2 15.5 15.5 15.3 15.0 14.8 14.8 14.8 14.9 15.0 15.2 15.7 15.8
  4.0

  3.5   (7.96) 8.47 9.48 10.5 11.6 12.4 12.9 13.1 13.1 13.0 13.0 13.2 13.4 13.8 14.4 14.8 15.1 15.4 15.6 15.5 15.1 14.9 14.8 14.8 14.9 15.1 15.4 15.8 15.9

  3.0   7.97 8.50 9.59 10.7 11.8 12.4 12.8 13.0 13.0 12.8 12.8 12.9 13.2 13.5 14.1 14.6 15.0 15.4 15.7 15.7 15.4 15.1 14.9 14.9 15.0 15.3 15.6 16.0 15.9

  2.5   8.06 8.61 9.73 10.9 11.8 12.5 12.8 13.0 12.9 12.7 12.6 12.7 13.0 13.3 13.9 14.5 15.1 15.5 15.8 15.8 15.5 15.2 15.0 15.0 15.2 15.4 15.8 16.0 16.0
  2.0
        8.06 8.61 9.73 10.9 11.8 12.5 12.8 13.0 12.9 12.7 12.6 12.7 13.0 13.3 13.9 14.5 15.1 15.5 15.8 15.8 15.5 15.2 15.0 15.0 15.2 15.4 15.8 16.0 16.0
  1.5
        7.97 8.50 9.59 10.7 11.8 12.4 12.8 13.0 13.0 12.8 12.8 12.9 13.2 13.5 14.1 14.6 15.0 15.4 15.7 15.7 15.4 15.1 14.9 14.9 15.0 15.3 15.6 16.0 15.9
  1.0
        (7.96) 8.47 9.48 10.5 11.6 12.4 12.9 13.1 13.1 13.0 13.0 13.2 13.4 13.8 14.4 14.8 15.1 15.4 15.6 15.5 15.1 14.9 14.8 14.8 14.9 15.1 15.4 15.8 15.9
  0.5
        7.98 8.49 9.44 10.4 11.5 12.3 12.8 13.1 13.1 13.1 13.1 13.4 13.5 13.9 14.5 14.8 15.2 15.5 15.5 15.3 15.0 14.8 14.8 14.8 14.9 15.0 15.2 15.7 15.8
  0.0

         0                                                                                                                   10
          Illuminance [lx]




                                                                                                                                                     Part1

Average illuminance                                         E̅m                 : 18.1 lx
Minimum illuminance                                         Emin                : 7.96 lx
Maximum illuminance                                         Emax                : 37 lx
Uniformity Uo                                               Emin/E̅m            : 1 : 2.27 (0.44)




                                                      -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                              Page 7/17




                                                                                                                                              27

---

## PDF-Seite 32 von 64

Object                     : B50HZ-DEMO-V04
Installation               : Bahnsteigmodernisierung 120 m
Project number             :
Date                       : 03.11.2026

2        Exterior 2
2.2      Calculation results, Exterior 2
2.2.1 Table, Floor (E)


15.8 15.6 15.1 14.7 14.6 14.5 14.6 14.8 15.2 15.5 15.6 15.8 15.9 15.6 15.2 15.0 15.0 15.0 15.0 15.2 15.4 15.8 15.9 15.8 15.7 15.2 14.8 14.7 14.5 14.6 14.9

15.8 15.5 15.0 14.7 14.5 14.4 14.4 14.7 15.1 15.5 15.6 15.8 15.9 15.7 15.3 15.1 15.0 15.0 15.1 15.2 15.5 15.9 15.9 15.8 15.6 15.1 14.7 14.6 14.4 14.5 14.7

15.7 15.4 15.0 14.5 14.2 14.2 14.2 14.4 14.9 15.3 15.6 15.8 16.0 15.9 15.5 15.2 15.0 15.0 15.1 15.4 15.8 16.1 15.9 15.7 15.4 14.9 14.5 14.3 14.2 14.3 14.5

15.7 15.4 14.9 14.3 14.0 13.9 14.0 14.2 14.7 15.2 15.6 15.9 16.1 16.0 15.7 15.4 15.2 15.1 15.3 15.6 15.9 16.1 16.0 15.7 15.4 14.8 14.3 14.0 13.9 14.0 14.3

15.7 15.4 14.9 14.3 14.0 13.9 14.0 14.2 14.7 15.2 15.6 15.9 16.1 16.0 15.7 15.4 15.2 15.1 15.3 15.6 15.9 16.1 16.0 15.7 15.4 14.8 14.3 14.0 13.9 14.0 14.3

15.7 15.4 15.0 14.5 14.2 14.2 14.2 14.4 14.9 15.3 15.6 15.8 16.0 15.9 15.5 15.2 15.0 15.0 15.1 15.4 15.8 16.1 15.9 15.7 15.4 14.9 14.5 14.3 14.2 14.3 14.5

15.8 15.5 15.0 14.7 14.5 14.4 14.4 14.7 15.1 15.5 15.6 15.8 15.9 15.7 15.3 15.1 15.0 15.0 15.1 15.2 15.5 15.9 15.9 15.8 15.6 15.1 14.7 14.6 14.4 14.5 14.8

15.8 15.6 15.1 14.7 14.6 14.5 14.6 14.8 15.2 15.5 15.6 15.8 15.9 15.6 15.2 15.0 15.0 15.0 15.0 15.2 15.4 15.8 15.9 15.8 15.7 15.2 14.8 14.7 14.5 14.6 14.9

                                                                                    20




                                                                                                                                                    Part2




                                                      -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                             Page 8/17




          28

---

## PDF-Seite 33 von 64

Object                    : B50HZ-DEMO-V04
Installation              : Bahnsteigmodernisierung 120 m
Project number            :
Date                      : 03.11.2026

2       Exterior 2
2.2     Calculation results, Exterior 2
2.2.1 Table, Floor (E)


15.3 15.6 15.7 15.8 15.8 15.5 15.1 14.9 14.9 14.9 14.9 15.1 15.5 15.9 15.9 15.8 15.7 15.4 15.1 14.9 14.9 15.2 15.5 16.0 16.8 17.2 17.6 17.8 17.7 17.8 18.0

15.1 15.5 15.7 15.9 15.9 15.6 15.2 15.0 14.9 14.9 15.0 15.2 15.6 16.0 15.9 15.8 15.7 15.3 15.0 14.9 14.9 15.2 15.5 16.0 16.8 17.3 17.8 18.1 18.1 18.1 18.3

14.9 15.3 15.6 15.9 16.0 15.8 15.4 15.1 15.0 15.0 15.1 15.4 15.8 16.1 16.0 15.8 15.5 15.2 14.8 14.7 14.8 15.0 15.5 16.1 16.8 17.4 18.0 18.5 18.6 18.6 18.9

14.8 15.3 15.6 16.0 16.1 15.9 15.6 15.3 15.1 15.1 15.3 15.6 15.9 16.1 16.0 15.7 15.4 15.0 14.6 14.4 14.5 14.7 15.2 16.0 16.8 17.4 18.0 18.5 18.6 18.6 18.7

14.8 15.3 15.6 16.0 16.1 15.9 15.6 15.3 15.1 15.1 15.3 15.6 15.9 16.1 16.0 15.7 15.4 15.0 14.5 14.3 14.4 14.6 15.1 15.8 16.5 17.0 17.6 17.8 17.8 17.6 17.6

14.9 15.3 15.6 15.9 16.0 15.8 15.4 15.1 15.0 15.0 15.2 15.5 15.8 16.1 16.0 15.7 15.4 15.0 14.7 14.5 14.5 14.7 15.0 15.5 16.0 16.4 16.7 16.8 16.6 16.2 16.0

15.1 15.5 15.7 15.9 15.9 15.6 15.2 15.0 14.9 14.9 15.0 15.2 15.6 16.0 15.9 15.8 15.6 15.2 14.8 14.6 14.5 14.7 14.9 15.2 15.7 15.9 15.9 15.8 15.4 15.0 14.7

15.3 15.6 15.7 15.8 15.9 15.5 15.1 15.0 14.9 14.9 15.0 15.1 15.5 15.9 15.9 15.7 15.6 15.3 14.9 14.6 14.5 14.7 14.7 15.1 15.5 15.6 15.6 15.4 14.9 14.5 14.2

                                           30




                                                                                                                                                  Part3




                                                     -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                            Page 9/17




                                                                                                                                            29

---

## PDF-Seite 34 von 64

Object                        : B50HZ-DEMO-V04
Installation                  : Bahnsteigmodernisierung 120 m
Project number                :
Date                          : 03.11.2026

2         Exterior 2
2.2       Calculation results, Exterior 2
2.2.1 Table, Floor (E)


 18.3 18.8 19.5     20   22   23   25   26   28   30   31   32   31   31   31   30   28   27   26   25   24    23   22   22   22   23   23    24   26   27   28

 18.8 19.4     20   21   23   25   26   28   30   31   33   34   34   34   33   32   30   29   27   26   25    24   23   23   23   24   25    26   27   28   30

 19.4    20    21   23   24   26   28   29   31   33   34   35   36   36   35   33   32   30   29   28   26    25   25   24   25   25   26    27   29   30   31

 19.0 19.6     21   22   23   25   27   28   30   32   34   35   35   35   34   32   31   30   29   27   25    24   24   23   24   24   25    26   28   29   31

 17.7 18.1 18.8 19.9     21   23   25   26   28   30   32   33   33   33   32   30   29   27   26   24   23    22   21   21   21   21   22    24   26   27   28

 16.1 16.4 16.9 17.8 19.0     21   22   23   25   27   28   29   30   29   28   27   25   24   22   21   19.3 18.3 17.8 17.6 17.7 18.1 19.0   20   22   23   25

 14.6 14.7 15.0 15.6 16.3 17.3 18.5 19.6     21   22   23   24   24   23   23   22   20   19.3 18.1 16.9 15.9 15.2 14.7 14.6 14.7 15.0 15.7 16.6 17.8 19.0   20

 13.9 13.8 14.0 14.4 14.9 15.6 16.7 17.7 18.5 19.3     20   21   20   19.7 19.7 19.2 18.0 17.0 16.0 15.0 14.3 13.7 13.2 13.0 13.1 13.5 14.1 14.8 15.8 16.8 17.8

    40                                                                                                                   50




                                                                                                                                                        Part4




                                                        -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                               Page 10/17




              30

---

## PDF-Seite 35 von 64

Object                             : B50HZ-DEMO-V04
Installation                       : Bahnsteigmodernisierung 120 m
Project number                     :
Date                               : 03.11.2026

2         Exterior 2
2.2       Calculation results, Exterior 2
2.2.1 Table, Floor (E)


    30    31    32   16.6 16.6      32   31   30   28   27   26   24   23   23    22   22   22   23   23    24   26   27   28   30   31   32   16.6 16.6     32    31

    31    33    34   27     27      34   33   31   30   29   27   26   25   24    23   23   23   24   25    26   27   29   30   31   33   34   27     27     34    33

    33    34    36   [37]   [37]    36   35   33   32   30   29   28   26   25    25   24   25   25   26    28   29   30   32   33   35   36   [37]   [37]   36    34

    32    34    35   36     36      35   34   32   31   30   28   27   25   24    24   23   24   24   25    27   28   30   31   32   34   35   36     36     35    34

    30    31    33   34     34      33   32   30   28   27   26   24   22   21    21   21   21   21   22    24   26   27   28   30   32   33   34     34     33    31

    26    28    29   30     30      29   28   26   25   23   22   21   19.1 18.2 17.7 17.5 17.7 18.2 19.1   21   22   23   25   26   28   29   30     30     29    28

    21    22    23   19.3 19.3      24   23   22   20   19.1 18.0 16.7 15.8 15.1 14.7 14.5 14.7 15.1 15.8 16.7 18.0 19.1   20   22   23   24   19.3 19.3     23    22

    18.8 19.6   20   10.8 10.8      20   20   19.1 17.9 16.9 15.9 14.9 14.2 13.6 13.1 13.0 13.1 13.6 14.2 14.9 15.9 16.9 17.9 19.1   20   20   10.8 10.8     20   19.6

                                                                                       60




                                                                                                                                                                  Part5




                                                             -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                                      Page 11/17




                                                                                                                                                        31

---

## PDF-Seite 36 von 64

Object                     : B50HZ-DEMO-V04
Installation               : Bahnsteigmodernisierung 120 m
Project number             :
Date                       : 03.11.2026

2         Exterior 2
2.2       Calculation results, Exterior 2
2.2.1 Table, Floor (E)


30   28   27   26   24   23   23   22    22   22   23   24    25   26   27   28   30   31   31   31   32   31   30   28   26   25    23   22   20   19.5 18.8

31   30   28   27   26   25   24   23    23   23   24   25    26   27   29   30   32   33   34   34   34   33   31   30   28   26    25   23   21    20   19.4

33   31   30   29   27   26   25   25    24   25   25   26    28   29   30   32   33   35   36   36   35   34   33   31   29   28    26   24   23    21   20

32   31   29   28   26   25   24   24    23   24   24   25    27   29   30   31   32   34   35   35   35   34   32   30   28   27    25   23   22    21   19.6

30   28   27   26   24   22   21   21    21   21   22   23    24   26   27   29   30   32   33   33   33   32   30   28   26   25    23   21   19.9 18.8 18.1

26   25   23   22   20   19.0 18.1 17.7 17.6 17.8 18.3 19.3   21   22   24   25   27   28   29   30   29   28   27   25   23   22    21   19.0 17.8 16.9 16.4

21   20   19.0 17.8 16.6 15.7 15.0 14.7 14.6 14.7 15.2 15.9 16.9 18.1 19.3   20   22   23   23   24   24   23   22   21   19.6 18.5 17.3 16.3 15.6 15.0 14.7

18.8 17.8 16.8 15.8 14.8 14.1 13.5 13.1 13.0 13.2 13.7 14.3 15.0 16.0 17.0 18.0 19.2 19.7 19.7   20   21   20   19.3 18.5 17.7 16.7 15.6 14.9 14.4 14.0 13.8

                                        70                                                                                                                       80




                                                                                                                                                      Part6




                                                        -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                               Page 12/17




          32

---

## PDF-Seite 37 von 64

Object                    : B50HZ-DEMO-V04
Installation              : Bahnsteigmodernisierung 120 m
Project number            :
Date                      : 03.11.2026

2       Exterior 2
2.2     Calculation results, Exterior 2
2.2.1 Table, Floor (E)


18.3 18.0 17.8 17.7 17.8 17.6 17.2 16.8 16.0 15.5 15.2 14.9 14.9 15.1 15.4 15.7 15.8 15.9 15.9 15.5 15.1 14.9 14.9 14.9 14.9 15.1 15.5 15.8 15.8 15.7 15.6

18.8 18.3 18.1 18.1 18.1 17.8 17.3 16.8 16.0 15.5 15.2 14.9 14.9 15.0 15.3 15.7 15.8 15.9 16.0 15.6 15.2 15.0 14.9 14.9 15.0 15.2 15.6 15.9 15.9 15.7 15.5

19.4 18.9 18.6 18.6 18.5 18.0 17.4 16.8 16.1 15.5 15.0 14.8 14.7 14.8 15.2 15.5 15.8 16.0 16.1 15.8 15.4 15.1 15.0 15.0 15.1 15.4 15.8 16.0 15.9 15.6 15.3

19.0 18.7 18.6 18.6 18.5 18.0 17.4 16.8 16.0 15.2 14.7 14.5 14.4 14.6 15.0 15.4 15.7 16.0 16.1 15.9 15.6 15.3 15.1 15.1 15.3 15.6 15.9 16.1 16.0 15.6 15.3

17.7 17.6 17.6 17.8 17.8 17.6 17.0 16.5 15.8 15.1 14.6 14.4 14.3 14.5 15.0 15.4 15.7 16.0 16.1 15.9 15.6 15.3 15.1 15.1 15.3 15.6 15.9 16.1 16.0 15.6 15.3

16.1 16.0 16.2 16.6 16.8 16.7 16.4 16.0 15.5 15.0 14.7 14.5 14.5 14.7 15.0 15.4 15.7 16.0 16.1 15.8 15.5 15.2 15.0 15.0 15.1 15.4 15.8 16.0 15.9 15.6 15.3

14.6 14.7 15.0 15.4 15.8 15.9 15.9 15.7 15.2 14.9 14.7 14.5 14.6 14.8 15.2 15.6 15.8 15.9 16.0 15.6 15.2 15.0 14.9 14.9 15.0 15.2 15.6 15.9 15.9 15.7 15.5

13.9 14.2 14.5 14.9 15.4 15.6 15.6 15.5 15.1 14.7 14.7 14.5 14.6 14.9 15.3 15.6 15.7 15.9 15.9 15.5 15.1 15.0 14.9 14.9 15.0 15.1 15.5 15.9 15.8 15.7 15.6

80                                                                                                               90




                                                                                                                                                  Part7




                                                     -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                          Page 13/17




                                                                                                                                            33

---

## PDF-Seite 38 von 64

Object                    : B50HZ-DEMO-V04
Installation              : Bahnsteigmodernisierung 120 m
Project number            :
Date                      : 03.11.2026

2       Exterior 2
2.2     Calculation results, Exterior 2
2.2.1 Table, Floor (E)


 15.3 14.9 14.6 14.5 14.7 14.8 15.2 15.7 15.8 15.9 15.8 15.4 15.2 15.0 15.0 15.0 15.0 15.2 15.6 15.9 15.8 15.6 15.5 15.2 14.8 14.6 14.5 14.6 14.7 15.1 15.6

 15.1 14.7 14.5 14.4 14.6 14.7 15.1 15.6 15.8 15.9 15.9 15.5 15.2 15.1 15.0 15.0 15.1 15.3 15.7 15.9 15.8 15.6 15.5 15.1 14.7 14.4 14.4 14.5 14.7 15.0 15.5

 14.9 14.5 14.3 14.2 14.3 14.5 14.9 15.4 15.7 15.9 16.1 15.8 15.4 15.1 15.0 15.0 15.2 15.5 15.9 16.0 15.8 15.6 15.3 14.9 14.4 14.2 14.2 14.2 14.5 15.0 15.4

 14.8 14.3 14.0 13.9 14.0 14.3 14.8 15.4 15.7 16.0 16.1 15.9 15.6 15.3 15.1 15.2 15.4 15.7 16.0 16.1 15.9 15.6 15.2 14.7 14.2 14.0 13.9 14.0 14.3 14.9 15.4

 14.8 14.3 14.0 13.9 14.0 14.3 14.8 15.4 15.7 16.0 16.1 15.9 15.6 15.3 15.1 15.2 15.4 15.7 16.0 16.1 15.9 15.6 15.2 14.7 14.2 14.0 13.9 14.0 14.3 14.9 15.4

 14.9 14.5 14.3 14.2 14.3 14.5 14.9 15.4 15.7 15.9 16.1 15.8 15.4 15.1 15.0 15.0 15.2 15.5 15.9 16.0 15.8 15.6 15.3 14.9 14.4 14.2 14.2 14.2 14.5 15.0 15.4

 15.1 14.8 14.5 14.4 14.6 14.7 15.1 15.6 15.8 15.9 15.9 15.5 15.2 15.1 15.0 15.0 15.1 15.3 15.7 15.9 15.8 15.6 15.5 15.1 14.7 14.4 14.4 14.5 14.7 15.0 15.5

 15.3 14.9 14.6 14.5 14.7 14.8 15.2 15.7 15.8 15.9 15.8 15.4 15.2 15.0 15.0 15.0 15.0 15.2 15.6 15.9 15.8 15.6 15.5 15.2 14.8 14.6 14.5 14.6 14.7 15.1 15.6

                                                                         100




                                                                                                                                                  Part8




                                                     -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                          Page 14/17




         34

---

## PDF-Seite 39 von 64

Object                      : B50HZ-DEMO-V04
Installation                : Bahnsteigmodernisierung 120 m
Project number              :
Date                        : 03.11.2026

2         Exterior 2
2.2       Calculation results, Exterior 2
2.2.1 Table, Floor (E)


    15.8 15.8 15.7 15.2 15.0 14.9 14.8 14.8 14.8 15.0 15.3 15.5 15.5 15.2 14.8 14.5 13.9 13.5 13.4 13.1 13.1 13.1 13.1 12.8 12.3 11.5 10.4 9.44 8.49 7.98

    15.8 15.9 15.8 15.4 15.1 14.9 14.8 14.8 14.9 15.1 15.5 15.6 15.4 15.1 14.8 14.4 13.8 13.4 13.2 13.0 13.0 13.1 13.1 12.9 12.4 11.6 10.5 9.48 8.47 (7.96)

    15.7 15.9 16.0 15.6 15.3 15.0 14.9 14.9 15.1 15.4 15.7 15.7 15.4 15.0 14.6 14.1 13.5 13.2 12.9 12.8 12.8 13.0 13.0 12.8 12.4 11.8 10.7 9.59 8.50 7.97

    15.7 16.0 16.0 15.8 15.4 15.2 15.0 15.0 15.2 15.5 15.8 15.8 15.5 15.1 14.5 13.9 13.3 13.0 12.7 12.6 12.7 12.9 13.0 12.8 12.5 11.8 10.9 9.73 8.61 8.06

    15.7 16.0 16.0 15.8 15.4 15.2 15.0 15.0 15.2 15.5 15.8 15.8 15.5 15.1 14.5 13.9 13.3 13.0 12.7 12.6 12.7 12.9 13.0 12.8 12.5 11.8 10.9 9.73 8.61 8.06

    15.7 15.9 16.0 15.6 15.3 15.0 14.9 14.9 15.1 15.4 15.7 15.7 15.4 15.0 14.6 14.1 13.5 13.2 12.9 12.8 12.8 13.0 13.0 12.8 12.4 11.8 10.7 9.59 8.50 7.97

    15.8 15.9 15.8 15.4 15.1 14.9 14.8 14.8 14.9 15.1 15.5 15.6 15.4 15.1 14.8 14.4 13.8 13.4 13.2 13.0 13.0 13.1 13.1 12.9 12.4 11.6 10.5 9.48 8.47 (7.96)

    15.8 15.8 15.7 15.2 15.0 14.9 14.8 14.8 14.8 15.0 15.3 15.5 15.5 15.2 14.8 14.5 13.9 13.5 13.4 13.1 13.1 13.1 13.1 12.8 12.3 11.5 10.4 9.44 8.49 7.98

                                   110                                                                                                                 120
                                                                                                                                                              [m]




                                                                                                                                                     Part9




                                                       -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                                                             Page 15/17




                                                                                                                                              35

---

## PDF-Seite 40 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026



2.2     Calculation results, Exterior 2
2.2.2 Pseudo colours, Floor (E)




y [m]

 3.0
 0.0




          0        10        20    30    40        50     60     70      80        90   100   110       120 x [m]




Average illuminance                                                        E̅m                      : 18.1 lx
Minimum illuminance                                                        Emin                     : 7.96 lx
Maximum illuminance                                                        Emax                     : 37 lx
Uniformity Uo                                                              Emin/E̅m                 : 1 : 2.27 (0.44)




                                              -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                               Page 16/17




         36

---

## PDF-Seite 41 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026



2.2     Calculation results, Exterior 2
2.2.3 3D pseudo colours, View 1 (E)




0 0.10.150.2 0.3 0.50.75 1 1.5 2       3   5 7.5 10 15 20 30 50 75 1001502003005007501000
                                                                                        1500
                                                                                           2000
                                                                                              3000
                                                                                                 5000
                                                                                                    7500
Illuminance [lx]




                                           -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final                                                                Page 17/17




                                                                                                 37

---

## PDF-Seite 42 von 64

Object                   : B50HZ-DEMO-V04
Installation             : Bahnsteigmodernisierung 120 m
Project number           :
Date                     : 03.11.2026

Exterior 2
Calculation results, Exterior 2
Pseudo colours, Floor (E)




y [m]

 3.0
 0.0




          0        10        20    30       40        50     60     70      80        90   100   110       120 x [m]



0 0.10.150.2 0.3 0.50.75 1 1.5 2        3    5 7.5 10 15 20 30 50 75 1001502003005007501000
                                                                                          1500
                                                                                             2000
                                                                                                3000
                                                                                                   5000
                                                                                                      7500
Illuminance [lx]




Average illuminance                                                           E̅m                      : 18.1 lx
Minimum illuminance                                                           Emin                     : 7.96 lx
Maximum illuminance                                                           Emax                     : 37 lx
Uniformity Uo                                                                 Emin/E̅m                 : 1 : 2.27 (0.44)




                                                 -please put your own address here-
Bahnsteig_Beleuchtung_V1.3_Final




         38

---

## PDF-Seite 43 von 64

Bahnsteig V1.7 - Mohamed Saida                                                        Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                             5 Nov 2026 / Mohamed Saida



                                  Project documentation
                                                   created with

                                               SIMARIS design
                                           Version: 27.0.1 (2026-11-02)
                                               Subrevision: 2267

                                     © SIEMENS AG 2026. All rights reserved.

                                         http://www.siemens.com/simaris




Master data

Project name:                    Bahnsteig V1.7 - Mohamed Saida
Project description:             DEMO A-B Beleuchtung 204 W - Vorplanung
Editor:                          Mohamed Saida
Planning office:
Created at:                      Wednesday, 4 November 2026
Changed at:                      Wednesday, 4 November 2026



Customer data

City:
Customer:



Comment:




Fiktive Arbeitsprobe - Vorplanung. 12 Leuchten, nominal 204 W; A/B je 102 W als Ersatzlasten. TN-S und Ik 1,5..3 kA
sind Annahmen. Keine Ausfuehrungsfreigabe; LED-Inrush, reale Netz-/Verlegedaten, Selektivitaet, SPD und Bahn-
PA offen.




                                                                                                             Page 1/12



                                                                                                        39

---

## PDF-Seite 44 von 64

Bahnsteig V1.7 - Mohamed Saida                                                   Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                        5 Nov 2026 / Mohamed Saida


                                              Network parameters:

                            General
Standard                                                  IEC
Attitude of Site                                          < 1000 m


                       Medium Voltage
Rated voltage                                             20 kV
Relative operating voltage at feeding point               100 %
Voltage factor c max                                      1,1
Voltage factor c min                                      1
Max./Min short-circuit power                              250 / 100 MVA
Max./Min. short-circuit current                           7,217 / 2,887 kA
Neutral System                                            Low-resistance
Relation R1/X1                                            0,2


                          Low Voltage
Rated voltage                                             400 V
System configuration                                      TN-S
Frequency                                                 50 Hz
Tolerable touch voltage                                   50 V
Ambient temperature of devices                            45 °C
Voltage factor c max                                      1,1
Voltage factor c min                                      0,9
Base point of voltage drop calculation                    Transformer-secondary terminals
Max. permissible voltage drop in network                  8%




                                                                                                        Page 2/12



           40

---

## PDF-Seite 45 von 64

Bahnsteig V1.7 - Mohamed Saida                                          Bahnsteig_V17_Mohamed_Saida.sdx
                                                                               5 Nov 2026 / Mohamed Saida


                        Defined network modes for calculation and dimensioning:

Operating mode: Operating mode 1


Starting point                   Target point             Connection                     Status

Network infeed 1.1               LVMD 1                   LVMD 1.1                                On




                                                                                                  Page 3/12



                                                                                          41

---

## PDF-Seite 46 von 64

Bahnsteig V1.7 - Mohamed Saida                                                             Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                   5 Nov 2026 / Mohamed Saida


                                                     List of devices:

 Sources of feeding:

 Neutral Infeed:

Designation               Un [V]   In [A]   Imp. in positive phase   Loop Impedance   Short circuit current   Phase connection
                                            system                   Zs               [kA]
                                            [mΩ]                     [mΩ]             Ik3max
                                            Z1 max                   φ [°]            Ik3min
                                            Z1 min                   R0/R1            Ik1max
                                            Zs max                   X0/X1            Ik1min
                                            Zs min                   Ikmax/Ikmin

Network infeed 1.1        400      20                                                 3                       L1-L2-L3-N
                                                                                      1,5
                                                                                      3
                                                                                      1,5




                                                                                                                    Page 4/12



              42

---

## PDF-Seite 47 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                                        Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                             5 Nov 2026 / Mohamed Saida


Switches/Fuses:

Circuit Breaker/Miniature circuit-breaker:

Place                     Designation                   Catalog Reference               In [A]    Icu/Icn [kA]       Icu/Icn [kA]        Release              Quantit
                                                                                                                     required            type /               y
                                                                                                                                         characteristi
                                                                                                                                         cs

A - 6 Leuchten - 102W     CB 1.2a                       5SY41016                        1         10                 1,548               B                    1

B - 6 Leuchten - 102W     CB 1.3a                       5SY41016                        1         10                 1,548               B                    1



Residual current device (RCD):

Place                     Designation                   Catalog               In [A]             IΔn [mA]        Release type /                         Quantity
                                                        Reference                                                characteristics

A - 6 Leuchten - 102W     CB 1.2a                       5SV33126              25                 30              A                                      1

B - 6 Leuchten - 102W     CB 1.3a                       5SV33126              25                 30              A                                      1



Fuse with base:

Place                Designation             Catalog Reference      In fuse        Utilizatio    Frame      In base          Icu(fuse)       Icu/Icn        Quantity
                                             Socket/ Fuse           [A]            n             size       [A]              [kA]            [kA]           Socket/
                                                                                   category      Socket/                                     required       Fuse
                                                                                                 Fuse

LVMD 1.1             FSO 1.1a                3NH4030/               25             gG            00/ 000    160              120             3              1/3
                                             3NA3810




                                                                                                                                                            Page 5/12



                                                                                                                                                 43

---

## PDF-Seite 48 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                               Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                    5 Nov 2026 / Mohamed Saida


Connections and line distribution:

Cable/Conductor Low voltage:

Designation    Type/          Starting       Ib [A] Iz [A]   Material   Length   Isolation   Installation   u [%] / Δu   θΔu [°C] /      Number
               Profile        point /                                   [m]                  type / ftot    [%] / ∑ Δu   θIkmax [°C] /   of runs
               [mm²]          Target point                                                                  [%]          θIkmin [°C]


C/L 1.1        e.g. NYY,      LVMD 1.1       0,465           Cu         10       PVC70       C              99,99        55              1
               NYCWY,         LVMD 1         32                                              1              0,01         20
               NYCY,                                                                                        0,01         80
               NYKY
               3x4/4/4

C/L 1.2        e.g. NYY,      LVMD 1         0,465           Cu         109,7    PVC70       C              99,4         55              1
               NYCWY,         A-6            19,5                                            1              0,586        20
               NYCY,          Leuchten -                                                                    0,596        80
               NYKY           102W
               1x1,5/1,5/1,
               5

C/L 1.3        e.g. NYY,      LVMD 1         0,465           Cu         119,7    PVC70       C              99,35        55              1
               NYCWY,         B-6            19,5                                            1              0,639        20
               NYCY,          Leuchten -                                                                    0,649        80
               NYKY           102W
               1x1,5/1,5/1,
               5




                                                                                                                                         Page 6/12



              44

---

## PDF-Seite 49 von 64

Bahnsteig V1.7 - Mohamed Saida                 Bahnsteig_V17_Mohamed_Saida.sdx
                                                      5 Nov 2026 / Mohamed Saida


Distribution:

Low voltage distribution:

Designation                      gi   Phase connection

LVMD 1                           1    L1-L2-L3-N




                                                                      Page 7/12



                                                                 45

---

## PDF-Seite 50 von 64

Bahnsteig V1.7 - Mohamed Saida                                                  Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                       5 Nov 2026 / Mohamed Saida


Loads:

Stationary loads:

Designation               Place        Pn [kW]   In [A]   Un [V]   cos φ   ai   Phase      Type of load     Quantit
                                                                                connecti                    y
                                                                                on

A - 6 Leuchten - 102W     Outer zone   0,102     0,465    230      0,95    1    L1-N       inductive        1

B - 6 Leuchten - 102W     Outer zone   0,102     0,465    230      0,95    1    L2-N       inductive        1




                                                                                                          Page 8/12



              46

---

## PDF-Seite 51 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                                     Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                          5 Nov 2026 / Mohamed Saida


                                         Personal protection against electric shock

All circuits of the project have a permissable break time ta-req > ta-cur and therefor fulfill the requirements for Personal protection against electric
shock.


                                                                    Disclaimer:

Dimensioned protection devices inside tap-off units of busbar trunking systems may not correspond to the actual available devices for
those components. Please verify the dimensioning results in the device lists and correct them accordingly.




                                                                                                                                                Page 9/12



                                                                                                                                          47

---

## PDF-Seite 52 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                              Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                   5 Nov 2026 / Mohamed Saida


                                                           Symbols legend:

Symbol [Unit]                    Description

ai                               Load factor

cos φ                            Power factor

ftot                             Derating factor

gi                               Simultaneity factor

Ia/In                            Inrush current relation

Ib [A] Iz [A]                    Operating current / allowed load capacity

Icu(fuse) [kA]                   Rated ultimate short-circuit breaking capacity - fuse

Icu [kA]                         Rated ultimate short-circuit breaking capacity according to IEC 60947-2
Icn [kA]                         Rated short-circuit breaking capacity according to IEC 60898-1

Icu/Icn [kA] required            the required breaking capacity of the protection device at installation location

Icw 1s [kA]                      Rated short-time withstand current 1s

IΔn [mA]                         Residual current - RCD

Ik1max                           Maximum single phase short-circuit current

Ik1min                           Minimum single phase short-circuit current

Ik3max                           Maximum three phase short-circuit current

Ik3min                           Minimum three phase short-circuit current

Ik1D [kA]                        single pole uninterrupted short-circuit current

Ik3D [kA]                        three pole uninterrupted short-circuit current

Ikmax/Ikmin                      Relation of maximum and minimum short-circuit current

Ikre                             Short-circuit current recovery factor

In [A]                           Nominal current

P0 [kW]                          No-load losses

Pk [kW]                          Short-circuit losses

Pmech [kW]                       mechan. Power

Pn [kW]                          Active power

R0 N [mΩ]                        Zero phase-sequence resistance phase-neutral conductor

R0 PE(N) [mΩ]                    Zero phase-sequence resistance phase-PE(N) conductor

R0/R1                            Resistance relation positive / zero phase-sequence system

r1 [%]                           Relative value of positive phase-sequence resistance

R1 [mΩ]                          Positive phase-sequence resistance




                                                                                                                                  Page 10/12



                48

---

## PDF-Seite 53 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                               Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                    5 Nov 2026 / Mohamed Saida

Sn [kVA]                               Nominal apparent power

ukr [%]                                Short-circuit voltage

Un [V]                                 Nominal voltage

Uprim [kV]                             Primary voltage

Usec [V]                               Secondary voltage

X0 N [mΩ]                              Zero phase-sequence reactance phase-neutral conductor

X0 PE(N) [mΩ]                          Zero phase-sequence reactance phase-PE(N) conductor

X0/X1                                  Reactance relation positive / zero phase-sequence system

X1 [mΩ]                                Positive phase-sequence reactance

xd'' [%]                               Subtransient reactance

Z1 max                                 Maximum impedance in positive phase-sequence system

Z1 min                                 Minimum impedance in positive phase-sequence system

Zs                                     Faulted circuit impedance

Zs max                                 Maximum faulted circuit impedance

Zs min                                 Minimum faulted circuit impedance

                                       Relative nominal voltage / voltage drop between beginning and end of a section / cumulated voltage drop
u [%] / Δu [%] / ∑ Δu [%]
                                       from the transformer primary/ secondary clamps to the specified point

                                       Conductor temperature of MV cable / Conductor temperature of LV cable
θΔu [°C] / θIkmax [°C] / θIkmin [°C]
                                       for voltage drop / on beginning of short circuit / for disconnection

η                                      Efficiency

φ [°]                                  Phase angle

φ1 min/max [°]                         Phase angle at Ik1 min/max

φ3 min/max [°]                         Phase angle at Ik3 min/max




                                                                                                                                        Page 11/12



                                                                                                                                   49

---

## PDF-Seite 54 von 64

Bahnsteig V1.7 - Mohamed Saida                                                                             Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                                                  5 Nov 2026 / Mohamed Saida


                                                       Standards for computation:

Title                                                                               IEC          HD            EN         DIN VDE

Low-voltage electrical installations *                                              60364-1…6    384                      0100 – 100...710

Short-circuit currents in three-phase a.c. systems – Calculation of currents        60909                      60909      0102

Short-circuit currents – calculation of effects
                                                                                    60865                      60865      0103
Definitions and calculation methods

Low-voltage switchgear and controlgear – Circuit-breakers                           60947-2                    60947-2    0660 – 101

Low-voltage switchgear and controlgear assemblies                                   61439                      61439      0660 – 600

A method of temperature-rise assessment by extrapolation for partially type-
                                                                                    60890+C      528 S2                   0660 – 507
tested assemblies (PTTA) of low-voltage switchgear and controlgear

Electrical installations of buildings – Part 5-52: Selection and erection of
                                                                                    60364-5-52   384                      0298 – 4
electrical equipment – Wiring systems

Low-voltage electrical installations – Selection and erection of electrical
equipment – Part 520: Wiring systems – Supplement 3: Current-carrying                                                     0100-520
capacity of cables in three-phase distribution circuits at load currents with                                             Supplement 3
harmonic content

Electrical accessories – Circuit-breakers for overcurrent protection for
                                                                                    60898-1                    60898-1    0641 – 11
household and similar installations – Circuit-breakers for a.c. operation

Power cables – Part 1000: Current-carrying capacity, general, conversion
                                                                                                                          0276-1000
factors

High-voltage switchgear and controlgear – Alternating Current switch-fuse
                                                                                    62271                      62271      0671 – 105
combinations

Electrical installations of buildings – Selection and erection of electrical
                                                                                    60364-5-53   60364-5-534              0100-534
equipment – Isolation, switching and control

Low-voltage electrical installations – Protection for safety – Protection against
                                                                                    60364-4-44   60364-4-443              0100-443
voltage disturbances and electromagnetic disturbances

Protection against lightning – Part 1…4                                             62305-1…4                             0185 – 1…4

Low-voltage surge protective devices - Surge protective devices connected to
                                                                                    61643-11                              0675-6-11
low-voltage power systems; Requirements and tests

Tests for electric cables under fire conditions – Circuit integrity                 60331-11,                  50200      0472-814
                                                                                    21                                    0482-200

Fire behaviour of building materials and building components — Part 12: Circuit                                           4102-12 : 1998-11
integrity maintenance of electric cable systems, requirements and testing

Electrical equipment of electric road vehicles - Electric vehicles conductive       61851                      61851
charging system

*) Special national conditions and deviations from IEC 60364-4-41: 2005 are not implemented and need to be considered!




                                                                                                                                  Page 12/12



             50

---

## PDF-Seite 55 von 64

51

---

## PDF-Seite 56 von 64

52

---

## PDF-Seite 57 von 64

53

---

## PDF-Seite 58 von 64

54

---

## PDF-Seite 59 von 64

55

---

## PDF-Seite 60 von 64

Bahnsteig V1.7 - Mohamed Saida                                                        Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                             5 Nov 2026 / Mohamed Saida



                                    Selectivity evaluation
                                                   created with

                                               SIMARIS design
                                           Version: 27.0.1 (2026-11-02)
                                               Subrevision: 2267

                                     © SIEMENS AG 2026. All rights reserved.

                                         http://www.siemens.com/simaris




Master data

Project name:                    Bahnsteig V1.7 - Mohamed Saida
Project description:             DEMO A-B Beleuchtung 204 W - Vorplanung
Editor:                          Mohamed Saida
Planning office:
Created at:                      Wednesday, 4 November 2026
Changed at:                      Wednesday, 4 November 2026



Customer data

City:
Customer:



Comment:




Fiktive Arbeitsprobe - Vorplanung. 12 Leuchten, nominal 204 W; A/B je 102 W als Ersatzlasten. TN-S und Ik 1,5..3 kA
sind Annahmen. Keine Ausfuehrungsfreigabe; LED-Inrush, reale Netz-/Verlegedaten, Selektivitaet, SPD und Bahn-
PA offen.




                                                                                                               Page 1/5



           56

---

## PDF-Seite 61 von 64

Bahnsteig V1.7 - Mohamed Saida                                         Bahnsteig_V17_Mohamed_Saida.sdx
                                                                              5 Nov 2026 / Mohamed Saida
Circuit name:                    LVMD 1.1
Designation:                     FSO 1.1a
Main operating mode:             Operating mode 1
Short cut current:               Ik3 / Ik2
Selectivity evaluation:


                                                    Switch settings:
                                                    Designation:     FSO 1.1a

                                                    3NA3810

                                                    In        25 A




Short cut current:               Ik1-PE
Selectivity evaluation:




                                                                                                Page 2/5



                                                                                         57

---

## PDF-Seite 62 von 64

Bahnsteig V1.7 - Mohamed Saida           Bahnsteig_V17_Mohamed_Saida.sdx
                                                5 Nov 2026 / Mohamed Saida
Short cut current:               Ik1-N
Selectivity evaluation:




                                                                  Page 3/5



           58

---

## PDF-Seite 63 von 64

Bahnsteig V1.7 - Mohamed Saida                                              Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                   5 Nov 2026 / Mohamed Saida
Circuit name:                    A - 6 Leuchten - 102W
Designation:                     CB 1.2a
Main operating mode:             Operating mode 1
Short cut current:               Ik1-PE
Selectivity evaluation:


                                                         Switch settings:
                                                         Designation:    CB 1.2a

                                                         5SY41016

                                                         In        1A

                                                         L Protection:   On
                                                         Ir        -               corresp. 1 A

                                                         I Protection:   On
                                                         Ii         -              corresp. 3 A




Short cut current:               Ik1-N
Selectivity evaluation:




                                                                                                       Page 4/5



                                                                                                  59

---

## PDF-Seite 64 von 64

Bahnsteig V1.7 - Mohamed Saida                                              Bahnsteig_V17_Mohamed_Saida.sdx
                                                                                   5 Nov 2026 / Mohamed Saida
Circuit name:                    B - 6 Leuchten - 102W
Designation:                     CB 1.3a
Main operating mode:             Operating mode 1
Short cut current:               Ik1-PE
Selectivity evaluation:


                                                         Switch settings:
                                                         Designation:    CB 1.3a

                                                         5SY41016

                                                         In        1A

                                                         L Protection:   On
                                                         Ir        -               corresp. 1 A

                                                         I Protection:   On
                                                         Ii         -              corresp. 3 A




Short cut current:               Ik1-N
Selectivity evaluation:




                                                                                                     Page 5/5



           60

---
