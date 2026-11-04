# Historische Recherche V1.4

Ueberholt durch V1.5: natives Free-A/B-Modell jetzt ausgefuehrt. Aktuelle Werte und Grenzen in `08_Webberechnung/FREE_MODELL_V15.md` (vom Projektstamm aus), aktuelles Schema V15, aktuelle XLSX V15. Nachfolgender Text bleibt als Historie erhalten.

---

# Web-Alternative für Netzschaltplan und Berechnung

Stand 04.11.2026. SIMARIS Suite zeigte bei der Prüfung „Your account is deactivated / registration under review“. Es wurde keine Kontoeinstellung geändert und kein nativer SIMARIS-Rechenlauf ausgeführt.

## Gewählte nächste Option: ELEK Cable Pro Web

Offizielle Produktseite (IEC 60364): https://elek.com/electrical-software/cable-pro-web-iec60364/
Offizielle Registrierung: https://cablepro.elek.com/create-free-account
Interaktiver Netzschaltplan: https://elek.com/tutorials/cable-pro-web/new-feature-interactive-single-line-diagram/

Laut Anbieter bietet der Professional-Plan den LV Network Calculator mit interaktivem Single-Line Diagram, Kabel-/Netzberechnung, Fehlerstromberechnung und Schutzkoordination. Der vollständige Funktionsumfang kann 14 Tage getestet werden. Der dauerhaft kostenlose Basiszugang umfasst nicht automatisch diese Netzfunktionen. Es wurde kein kostenpflichtiger Plan gebucht und noch kein Nutzerkonto erstellt. Der Benutzer übernimmt Registrierung/Anmeldung selbst. Die lokale Browsernavigation zur Registrierungsseite lief in einen Timeout; der offizielle Registrierungslink konnte über die Webquelle gelesen werden. Zugriff nach Anmeldung ist noch zu prüfen.

## Vorbereiteter Projektumfang

Einspeisung -> UV-01 -> getrennte Abgänge A und B -> jeweils sechs Leuchten. Die 12 bestehenden Relux-Leuchten bleiben unverändert. In der Netzrechnung werden die Leuchten als elektrische Lasten verknüpft, nicht in Relux neu erzeugt.

`Netzmodell_Leitungsabschnitte.csv` enthält 24 vorläufige Abschnitte: je sechs Stammabschnitte und sechs Leuchtenabzweige pro Kreis. `Netzmodell_Eingabebasis.json` enthält Lasten, Topologie und fehlende Eingänge. Diese Dateien sind eine manuelle Eingabebasis, KEIN behauptetes natives ELEK-Importformat.

Die Abschnittslängen stammen aus den schematischen V1.3-Kabelwegen: UV bei (2;2), Trassen y=3,1 bzw. 0,9 m; 1,1 m Querweg und senkrechter Weg bis zur jeweiligen Leuchtenhöhe. Letzter Leitungsweg: A 109,7 m, B 119,7 m. Gesamte modellierte Kabelwege mit allen Abzweigen: A 137,3 m, B 147,3 m. Nicht vermessen, keine Längenreserve und keine Einspeiseleitung enthalten.

Nach Registrierung: Standard IEC 60364 wählen, Projekt als fiktive Arbeitsprobe kennzeichnen, Quelle/UV/A/B aufbauen, Abschnitts- und Lastdaten übernehmen. Netzform, Quellimpedanz und Schutzgeräte nicht durch stillschweigende Softwarevorgaben als „Bestand“ ausgeben. Nur ausdrücklich definierte Demoannahmen verwenden und im Bericht aufführen. Zuerst ein einfaches Rechenbeispiel mit der lokalen Rechnung vergleichen, dann vollständige Netz-/Schutzrechnung und Exporte erstellen. Schutz-, Kabel- und Normnachweise bleiben bis dahin Missing/Preliminary.

## Bereits geprüfte Alternative: Nexans EASYCALC

https://www.nexans.ch/de/Tools-and-downloads/easycalc/easycalc.html
Der Kabelrechner war ohne Konto erreichbar. Das Stromfeld verlangt jedoch mindestens 1 A; unser Vergleichsstrom pro A/B-Kreis beträgt nur rund 0,467 A. Mit diesem Eingabemodus wurde deshalb kein gültiges Projektergebnis erzeugt. Ein Strom von 1 A wurde nicht als tatsächlicher Laststrom eingesetzt. Das Werkzeug ersetzt außerdem keinen vollständigen Netzschaltplan mit Selektivitätsnachweis.

## Noch offen

ELEK-Konto / Professional-Testzugang; tatsächliche Verfügbarkeit der IEC-Netzfunktionen; eindeutige Demo-Netzgrundlage oder reale Einspeisedaten; nativer Projektaufbau und Rechenlauf; Export von Schaltplan und Bericht. Keine neuen bestätigten elektrischen Auslegungsergebnisse in V1.4.
