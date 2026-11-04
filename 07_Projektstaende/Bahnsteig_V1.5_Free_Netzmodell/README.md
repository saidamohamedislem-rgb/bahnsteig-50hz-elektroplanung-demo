# Bahnsteig V1.5 - berechnetes Free-Netzmodell

Stand 04.11.2026. Fiktive Arbeitsprobe zur Bahnsteigbeleuchtung und Elektroplanung. V1.2, V1.3 und V1.4 bleiben erhalten. Kein Bau- oder Ausfuehrungsstand.

## Was neu ist

ELEK Cable Pro Web hat ein natives A/B-Ersatznetz berechnet. Der kostenlose Zugang erlaubte drei Netzobjekte: eine UV und zwei gebuendelte Lasten. Die Quelle kommt hinzu. Die zwoelf echten Leuchten bleiben im Relux- und CAD-Lageplan unveraendert. Das kostenpflichtige Abonnement wurde nicht aktiviert.

- [Nativer Netzbericht](08_Webberechnung/ELEK_V15_Nativer_Netzbericht.pdf): 7 Seiten, inklusive Single-Line Diagram, Kabel-, Last-, Fehlerstrom- und Spannungsfalltabellen.
- [Nativer Kennlinienvergleich](08_Webberechnung/ELEK_V15_Nativer_Kennlinienvergleich.pdf): 3 Seiten, generisch B20/B6. Keine nachgewiesene Gesamtselektivitaet.
- [Aktueller Stromlaufplan PDF](02_CAD/Bahnsteig_V15_Stromlaufplan.pdf), [DWG](02_CAD/Bahnsteig_V15_Stromlaufplan.dwg) und [DXF](02_CAD/Bahnsteig_V15_Stromlaufplan.dxf): eigenstaendige BricsCAD-Zeichnung auf Basis der dokumentierten Ergebnisse, kein ELEK-CAD-Export.
- [Aktueller Modellvergleich XLSX](03_Elektro/Bahnsteig_V15_Modellvergleich.xlsx): Eingaben, transparente Referenzformeln und archivierte native Ergebnistabellen.
- [Modell und Grenzen](08_Webberechnung/FREE_MODELL_V15.md), [Professional und Vorstellungsgespraech](PROFESSIONAL_NUTZEN.md), [Pruefstatus](PRUEFSTATUS.csv).
- [Bericht-Grundlage](BERICHT_GRUNDLAGE.md) und [Fortsetzung](FORTSETZUNG.md).

## Unveraenderte Lichtplanung

Die V1.3-RDF und der echte 18-seitige Relux-Bericht unter `01_Relux` bleiben massgebend: 12 Leuchten, 204 W nominal, Em 18,1 lx, Emin 7,96 lx, Emax 37 lx, U0 0,44. Kein neuer Lichtlauf, weil V1.5 keine optisch wirksame Geometrie oder Leuchte aendert. Der 120 x 4 m grosse Bahnsteig und das Dach X=45...75 m sind weiterhin in den vorhandenen CAD-Dateien enthalten.

## Einordnung

Verified bedeutet hier: Datei, Eingabe oder ausgefuehrtes Softwareergebnis belegt. Preliminary bedeutet: Demoannahme oder fachlich noch zu bestaetigender Entwurf. Missing bedeutet: erforderlicher Nachweis fehlt. Native Ausfuehrung ist kein Nachweis realer Netzparameter.

Alle ELEK-PDFs sind unveraenderte kostenlose Vorschauausgaben mit Anbieter-Wasserzeichen und Lizenzhinweis. Diese Hinweise bleiben erhalten. Der Cloud-Stand ist im angemeldeten Benutzerkonto bearbeitbar; das Eingabeprotokoll ist kein zugesichertes Reimportformat.

Wesentliche offene Punkte: reales Netz / Ik min-max, Icn und konkrete Schutzgeraete, LED-Einschaltstroeme, Verlegebedingungen und Produktwahl, Selektivitaet, RCD-/SPD-Konzept, Bahn-Erdung/PA, Sicherheitsbeleuchtung und Licht-Sollwertbewertung. Die technische Gesamtplanung ist noch nicht abgeschlossen.
