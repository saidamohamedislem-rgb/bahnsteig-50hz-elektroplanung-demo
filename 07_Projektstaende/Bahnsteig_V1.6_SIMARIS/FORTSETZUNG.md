# Fortsetzung ab V1.6 SIMARIS

Stand 04.11.2026. SDX-Projekt: `09_SIMARIS/Bahnsteig_V16_SIMARIS.sdx`, SIMARIS design 27.0.1. Berechnung bereits ausgeführt, Messages [0]. Keine zwölf Relux-Leuchten neu anlegen und keinen alten V1.5-Schutzplan als aktuelle Auswahl verwenden.

1. Vor Änderungen nächste Arbeitsversion kopieren; V1.2 bis V1.6 erhalten. Aktuelle Annahmen und echte Geräte unter `09_SIMARIS/SIMARIS_ERGEBNISSE.md` lesen.
2. Reale Netzform, Ik1/Ik3 min/max, Vorsicherung und Anschlusskapazität beschaffen. 20-A-Quellenbemessung versus gG25 abstimmen. IEC-/länderspezifische Einstellungen fachlich festlegen.
3. Gewünschten Detailgrad umsetzen: zwei gebündelte Lasten durch zwölf verteilte Lasten mit den bestehenden 24 Stamm-/Abzweigabschnitten ersetzen, ohne Lasten doppelt zu zählen. CSV unter `08_Webberechnung/Netzmodell_Leitungsabschnitte.csv` ist eine Entwurfsgrundlage, keine zugesicherte SIMARIS-Importvorlage.
4. Reale Verlegung, Häufung, Kabelartikel, Temperaturen, PE und Spannungsfallbudget eintragen. Unsymmetrischen Lastfluss und Neutralleiter-/Oberschwingungsbelastung gesondert prüfen.
5. LED-Treiber-Inrush und Ableitströme beschaffen; B1-Kandidaten und RCD-Typ prüfen. Selektivität einschließlich gG-Vorsicherung, Hersteller-Grenzstrom/I²t, Ausschaltvermögen und Kurzschlussenergie nachweisen. SPD und Bahn-PA/Erdung vollständig planen.
6. Danach neu dimensionieren, native Berichte/DWG und den CAD-Detailstromlaufplan synchronisieren. Historische B20/B6-Pläne behalten und eindeutig als überholt markieren. Lichtmodell nur bei lichttechnisch wirksamer Änderung erneut rechnen.
7. Anforderungen an Licht, Blendung, Sicherheitsbeleuchtung und weitere Verbraucher ergänzen. Verified / Preliminary / Missing aktualisieren; erst danach technische Gesamtplanung bewerten.

Die aktuelle Gesprächsvorbereitung benötigt keinen ELEK-Professional-Kauf. Erweiterte SIMARIS-Funktionen nur bei tatsächlicher Funktionssperre und klarem Bedarf besprechen. Professionelle Lizenzen ersetzen keine fehlenden Eingangsdaten.
