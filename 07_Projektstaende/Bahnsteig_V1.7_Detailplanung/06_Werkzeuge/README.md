# Bearbeitungswerkzeuge – archivierter Entstehungsstand

Die Skripte dokumentieren die Erstellung der V1.3-Artefakte. Sie enthalten lokale Quell-/Zielpfade des Bearbeitungsrechners und sind **kein automatisch auszuführendes Fortsetzungsskript**. Vor Wiederverwendung Pfade prüfen und in einer neuen Arbeitsversion testen. Bestehende Dateien werden teilweise neu erzeugt.

Für die normale Weiterarbeit direkt die RDF-, DWG- und XLSX-Dateien öffnen. `prepare_v13.py` extrahiert nur CANOPY_SUPPORT aus vorhandenem CAD; `draw_v13.py` erzeugt Entwurfs-DXF; `build_calcs.mjs` erzeugt die Formelmappe mit @oai/artifact-tool. BricsCAD-LISP dient nativem Export/SaveAs und Geometrieprüfung. Python-PDF-Verarbeitung benötigt pypdf, Rendering optional pypdfium2/Pillow. Keine Zugangsdaten oder Laufzeit-Abhängigkeiten werden mitgeliefert.

V1.5: draw_v15.py, finalize_v15.lsp und build_v15.mjs dokumentieren die neue separate Schaltung und Formelmappe. Die Skripte koennen Ausgabedateien ueberschreiben; nicht blind ausfuehren. Neue Version mit passenden Pfaden verwenden.

V1.7: build_v17.mjs und detail17_input.json dokumentieren die Abschnittsrechnung. Der Builder erwartet die Eingabe unter work/detail17_input.json und schreibt den fest angegebenen V1.7-Ausgabepfad; vor erneutem Start Pfade auf eine neue Version anpassen.
