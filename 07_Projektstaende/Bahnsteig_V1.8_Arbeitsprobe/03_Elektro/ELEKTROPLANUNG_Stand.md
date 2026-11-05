# Historischer Elektrostand V1.3

Ueberholt durch V1.5: natives Free-A/B-Modell jetzt ausgefuehrt. Aktuelle Werte und Grenzen in `08_Webberechnung/FREE_MODELL_V15.md` (vom Projektstamm aus), aktuelles Schema V15, aktuelle XLSX V15. Nachfolgender Text bleibt als Historie erhalten.

---

# Elektroplanung – Rechen- und Bearbeitungsstand

04.11.2026. Status Preliminary; keine Geräte- oder Kabelfreigabe.

## Lasten und Stromkreise

A: L01/L03/L05/L07/L09/L11. B: L02/L04/L06/L08/L10/L12. Je sechs Leuchten, 102 W nominal. Gesamt 204 W. Keine sonstigen Anlagenlasten enthalten. LED-Einschaltströme, Ableitströme und Leistungsfaktor müssen aus den tatsächlichen Treiberdaten folgen. A/B sind alternierend, keine nachgewiesene Notbeleuchtung.

## Offen gelegte Vorberechnung

In der XLSX gelb markierte Eingaben: U0=230 V, cos φ=0,95 (Szenario), ρCu=0,0225 Ωmm²/m, S=2,5 mm² (Vergleichswert). UV-01 schematisch bei (2;2), Trassen bei Y=3,1 und 0,9 m. Gemeinsamer Querweg 1,1 m; letzter Stichweg 1,1 + 4,5 = 5,6 m. Trassen und Querschnitt sind nicht bestätigt.

Ib=P/(U0·cos φ). Für verteilte Lasten: ΣPiLi=Σ[Pi·(Xi−2+1,1)]+Pletzte·5,6. Der ohmsche Spannungsfallanteil lautet ΔUR=2ρ·ΣPiLi/(S·U0); ΔUR%=100·ΔUR/U0. Dies ist nur der R-Anteil des Einphasen-Szenarios, kein vollständiger Grenzwertnachweis.

| Kreis | P | Ib Szenario | ΣPiLi | ΔUR | ΔUR/U0 |
|---|---:|---:|---:|---:|---:|
| A | 102 W | 0,4668 A | 5621,8 Wm | 0,4400 V | 0,1913 % |
| B | 102 W | 0,4668 A | 6641,8 Wm | 0,5198 V | 0,2260 % |

Nicht enthalten: vorgelagerte Leitungen, vollständige Reaktanz-/Phasenbetrachtung, reale Leiter-/Schleifentemperaturen, harmonische Ströme und Abzweigvarianten. Kein Schluss auf zulässige Kabellänge oder zulässiges Schutzgerät.

## Kabel, Überstromschutz und Abschaltung – Missing

Vor Auswahl Verlegeart, Kabelbauart, Temperatur, Häufung, Iz, Kurzschlussbeanspruchung und realen Spannungsfall ermitteln. Ib/Iz/In sowie I2-Beziehung und herstellerbezogene Randbedingungen prüfen. Ik min/max und Netzform fehlen; daher sind Abschaltzeiten, Ausschaltvermögen und thermischer Kurzschlussschutz nicht nachgewiesen. Keine B-/C-Charakteristik oder Nennströme sind als endgültige Auswahl freigegeben.

## Selektivität und RCD – Missing

Vorgeschaltete Geräte, konkrete Fabrikate, Kennlinien und Fehlerstromkonzept fehlen. Selektivität kann erst mit realer Gerätekombination und Herstellerunterlagen bewertet werden. RCD-Typ und Aufteilung mit LED-Treiberdaten, Netzform und Projektanforderungen abstimmen.

## SPD, Erdung und Potentialausgleich – Missing

SPD im Stromlaufplan ist eine Funktionsposition. Auswahl nach Netzform, äußerem Blitzschutz, Einspeisung, Installationsbedingungen, Schutzpegel, Koordination und Anschlusslängen; keine Typ-/Gerätefreigabe vorhanden. PE-Kontinuität und Potentialausgleich von leitfähigen Teilen fachlich planen. Bahnspezifische Schnittstellen, Berührungsspannungen, Rückstromführung und Erdung nach verbindlichem Projektregelwerk abstimmen; kein ungeprüfter Anschluss an Schienen. DIN-EN-50122-1-Katalogangaben allein ersetzen keinen Nachweis.

## Fehlende Eingänge

Netzform; Spannungstoleranz; Trafo-/Netzdaten; Ik min/max; Einspeise- und Vorsicherungsdaten; reale Kabelwege und Kabeltypen; Verlege-/Umgebungsbedingungen; Treiberdaten; externe Verbraucher; Blitzschutz-/Erdungskonzept; Sicherheitsbeleuchtungsanforderungen; maßgebende Projekt- und Bahnregelwerke. Ohne diese Daten keine vollständige native SIMARIS-Berechnung behaupten.
