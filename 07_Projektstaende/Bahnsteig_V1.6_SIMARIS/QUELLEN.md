# Quellen und Werkzeuge

Geprüft am 04.11.2026. Hersteller-/Anbieterinformationen stützen Methoden und Funktionen; sie ersetzen keine projektbezogene Freigabe. Normkataloge wurden nur für Metadaten, nicht als gelesene Vollnorm verwendet.

- Relux CAD-Plan-Workflow: https://relux.com/knowledge-hub/knowledge-db/relux-desktop/import-and-export/construct-scene-from-cad-plan
- ReluxDesktop: https://relux.com/lighting-planning/reluxdesktop
- Siemens SIMARIS: https://www.siemens.com/en-us/products/simaris/
- Schneider Electric, Spannungsfall: https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions
- Prysmian, Electrical Information for Low Voltage Cables (Dokument 18.12.2024; Rechenwert Cu): https://asean.prysmian.com/sites/asean.prysmian.com/files/media/documents/241218%20-%20Prysmian%20Electrical%20Information%20for%20Low%20Voltage%20Cables.pdf
- Schneider Electric, Kurzschluss: https://www.electrical-installation.org/enwiki/Short-circuit_current
- Schneider Electric, Schutzkoordination: https://www.electrical-installation.org/enwiki/Coordination_between_circuit-breakers
- Schneider Electric, Gerätauswahl: https://www.electrical-installation.org/enwiki/Selection_of_a_circuit-breaker
- DEHN, Bahn/Normen: https://www.dehn.de/de/loesungen/bahn/normen
- DIN Media, DIN EN 50122-1, Katalogausgabe 2026-08: https://www.dinmedia.de/de/norm/din-en-50122-1/399708859
- Bricsys, native PDF-Ausgabe (ältere Befehlsreferenz; tatsächlicher V26-Export im Programm geprüft): https://developer.bricsys.com/bricscad/help/en_US/V17/CmdRef/source/E/ExportPdf.htm

Primäre lokale Belege: native V1.3-Relux-Berichte und RDF-Protokoll, unveränderte V1.2-Sicherungen, vorhandene LDT-Dateien, ursprünglicher CAD-Stromlaufplan, Lastquelle und nativer Geometrieexport. Vorhandene LDT-Daten wurden nicht als aktuelle Herstellerfreigabe neu zertifiziert.

Verwendete Skills: computer-use, verified-improvement, pdf, spreadsheets, write-like-me (neutrales technisches Deutsch; keine verbundene persönliche Stilprobe verfügbar).
Keine kostenpflichtigen Dienste oder neuen Lizenzen erworben. Vorhandene installierte Software wurde genutzt.


## Ergänzung V1.4 - Web-Alternativen (04.11.2026)

- ELEK IEC-Produktseite: https://elek.com/electrical-software/cable-pro-web-iec60364/
- ELEK interaktiver Netzschaltplan / Professional-Test: https://elek.com/tutorials/cable-pro-web/new-feature-interactive-single-line-diagram/
- ELEK offizielle Registrierung: https://cablepro.elek.com/create-free-account
- Nexans tatsächlich getestete Webmaske: https://www.nexans.ch/de/Tools-and-downloads/easycalc/easycalc.html
- Siemens SIMARIS-Funktionen / Registrierung: https://www.siemens.com/de-de/products/simaris/

Kosten: keine Buchung vorgenommen. ELEK-Professional-Test laut Anbieter 14 Tage; native Netzrechnung noch nicht ausgeführt. Herstellerbeschreibungen sind keine unabhängige Validierung des Rechenkerns. Auswahlrecherche mit ai-research-analyst und verified-improvement; native Zustandsprüfung mit computer-use. Browserprüfung: Nexans erreichbar, Stromeingabe unter 1 A abgelehnt; ELEK-Registrierungsnavigation im lokalen Browser Timeout. Schema-/Lastdaten wurden lokal aus dem vorhandenen Modell aufgebaut und die Abschnittssummen mit der V1.3-Rechnung abgeglichen.


## V1.5 Web-Netzrechnung, Stand 04.11.2026

- Primaerbeleg: nativer ELEK-Netzbericht S. 1-7 und Kennlinienbericht S. 1-3, im angemeldeten Free-Konto erzeugt. Eingaben/Tabellen ohne Zugangsdaten archiviert.
- https://elek.com/electrical-software/cable-pro-web-iec60364/ - offizieller IEC-Produktumfang.
- https://elek.com/tutorials/cable-pro-web/new-feature-interactive-single-line-diagram/ - offizieller SLD-Workflow. Beide Seiten im Verlauf gelesen; erneuter Abschlussabruf Timeout. Free-Limits und Berichte direkt in der App beobachtet.
- https://cache.industry.siemens.com/dl/files/792/45302792/att_1328163/v1/MAN_L1V30914799-04_en_en-US.pdf - Siemens SENTRON, Ausgabe 03/2025, Abschnitt 9.2.2.1, B-Magnetausloesung 3-5 In. Kein Nachweis eines konkret ausgewaehlten Siemens-Geraets.
- https://de.electrical-installation.org/dewiki/TN-_Bestimmung_der_Kurzschlussstromwerte_zur_Einhaltung_der_Abschaltbedingung - Schneider, TN-/Abschaltmethodik. Die vereinfachte konventionelle 0,8-U-Methode wurde nicht zusaetzlich mit dem nativen Quellmodell vermischt.

Volltexte der projektrelevanten Normen wurden nicht vollstaendig geprueft. IEC-Softwareeinstellung ist keine pauschale DIN/VDE-/Bahnkonformitaet. Keine reale Messung, kein Hersteller-Selektivitaetsnachweis.


## V1.6 SIMARIS, geprüft am 04.11.2026

- Primärbelege: tatsächlich ausgeführtes SIMARIS design 27.0.1, Subrevision 2267; SDX/SX, native RTF/CSV/PDF/DWG unter `09_SIMARIS`. Benutzerfreigabe zur Installation lag ausdrücklich vor. Die Native-Exportdateien sind unverändert archiviert; Word erzeugte PDF aus den beiden RTFs.
- Siemens Produktkatalog: https://sieportal.siemens.com/en-ie/products-services/10374072 - Netzaufbau, Dimensionierung, Dokumentation und Professional-Funktionen. Suchinhalt zugänglich; späterer Direktaufruf JavaScript-beschränkt. Tatsächliche Funktionen wurden in der installierten Anwendung beobachtet.
- Siemens Schulung, veröffentlicht 22.04.2026: https://resources.sw.siemens.com/en-US/simaris-design-basic-handling-sources-operating-modes-webinar/ - Quellen und Betriebsarten.
- Siemens SENTRON 03/2025, Abschnitt 9.2.2.1: https://cache.industry.siemens.com/dl/files/792/45302792/att_1328163/v1/MAN_L1V30914799-04_en_en-US.pdf - B-Kennlinie 3 bis 5 In. Einfache 5-In-Plausibilität ist kein vollständiger Selektivitätsnachweis.

Native Gerätereferenzen wurden aus dem tatsächlich erzeugten Bericht übernommen; keine Behauptung einer aktuellen individuellen Beschaffungsfreigabe. Kein vollständiger Normtextvergleich oder Messnachweis. Skills für V1.6: computer-use, verified-improvement, ai-research-analyst und pdf. Keine zusätzliche Servicezahlung; kein Professional-Plan aktiviert.
