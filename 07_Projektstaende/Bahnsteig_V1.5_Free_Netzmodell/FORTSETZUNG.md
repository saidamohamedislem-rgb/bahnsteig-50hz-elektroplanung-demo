# Fortsetzung ab V1.5

Aktueller Stand: kostenloses ELEK-Netz 23427, natives A/B-Ersatzmodell berechnet, BricsCAD-Schema und Referenz-XLSX abgelegt. Kein bezahlter Plan aktiv. Relux V1.3 unveraendert; keine Wiederholung des Lichtlaufs erforderlich.

1. In ELEK das Netz `Bahnsteig V1.5 - A-B Ersatzmodell DEMO` oeffnen: https://cablepro.elek.com/app/main/projects/143977/networkcalc/23427 . Teilentwurf 23426 nicht mit aktuellem Modell verwechseln.
2. Zuerst `08_Webberechnung/FREE_MODELL_V15.md` und `PRUEFSTATUS.csv` lesen. Keine neue Leuchte in Relux anlegen und die zwoelf Positionen nicht aendern.
3. Fuer das Vorstellungsgespraech `PROFESSIONAL_NUTZEN.md`, V15-Schaltplan, Relux-Gesamtbericht und Modellvergleich verwenden. Free-PDF-Wasserzeichen bleiben erhalten.
4. Vor weiterer Bemessung: Netzform / bestaetigte Ik min-max und Z Quelle, reale Kabelwege und Verlegung, Temperatur/Hauefung, Leuchten-/Treiber-Einschaltstrom und Herstellergeraete beschaffen.
5. Zwei gleich bezeichnete B20-Instanzen sind im nativen Modell in Serie. Ihre Notwendigkeit pruefen; anschliessend eindeutige Geraetekennzeichen und passende Staffelung festlegen. Kein positiver Selektivitaetsnachweis vorhanden.
6. Bei freigeschaltetem groesserem Netz die vorbereiteten 12 Lasten / 24 Abschnitte einzeln uebernehmen. Die CSV ist eine Eingabehilfe, kein nachgewiesenes ELEK-Importformat. Erst nach diesen Aenderungen neu rechnen und aktuelle Berichte exportieren.
7. Icn, Abschaltzeiten, Durchlassenergie, Selektivitaet, RCD/SPD, Erdung/Bahn-PA sowie Sicherheitsbeleuchtung und Lichtanforderungen abschliessen. Erst dann technische Gesamtbewertung.

V1.3-XLSX: historisches verteiltes 2,5-mm2-Szenario. V1.5-XLSX: aktuelles gebuendeltes 1,5-mm2-Szenario mit separatem 4-mm2-PE. Unterschiedliche Ergebnisse sind kein Versionsfehler. Eingabeprotokolle enthalten inaktive Software-Defaults; nur dokumentierte aktive Werte verwenden. Cloud-Sicherung ist von Anbieterzugang abhaengig; lokale Tabellen sind kein zugesicherter Cloud-Reimport.
