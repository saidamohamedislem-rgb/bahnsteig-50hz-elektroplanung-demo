import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root='C:/Users/mouha/Documents/Codex/2026-11-04/remote-desktop-commander-https-files-openai-4/outputs/Bahnsteig_V1.3_Final';
const source=JSON.parse(await fs.readFile('C:/Users/mouha/Downloads/Bahnsteig_V11_Deliverables/SIMARIS_INPUT_PREPARATION.json','utf8'));
const w=Workbook.create();const c=w.worksheets.add('Vorberechnung'),l=w.worksheets.add('Leuchten'),n=w.worksheets.add('Nachweise');
function rows(s,a,v){const m=Math.max(...v.map(r=>r.length));s.getRange(a).values=v.map(r=>[...r,...Array(m-r.length).fill(null)]);}
rows(c,'A2',[['Bahnsteig 50 Hz - V1.3 | Rechenstand']]);
rows(c,'A4',[['Status','Preliminary - keine Kabel- oder Schutzfreigabe']]);
rows(c,'A6',[['Eingabe','Wert','Einheit','Herkunft / Bedeutung'],['U0',230,'V','Projektauftrag: Annahme 400/230 V'],['cos phi',.95,'-','Szenario, Treiberdaten fehlen'],['rho Cu',.0225,'Ohm mm2/m','Betriebstemperatur-Szenario; Prysmian Quelle unten'],['Leiterquerschnitt',2.5,'mm2','Vergleichswert, nicht ausgewaehlt'],['UV x',2,'m','Schematischer UV-01-Standort'],['Gemeinsamer Querweg',1.1,'m','UV y=2 bis Trasse y=0.9/3.1'],['Letzte Abzweiglaenge',5.6,'m','1.1 m quer + 4.5 m vertikal'],['Letzte Leuchtenleistung',18.5,'W','L11 und L12 nominal']]);
rows(l,'A2',[['Leuchtenpositionen und nominale Lasten - identisch zum Relux-Ansatz']]);
rows(l,'A4',[['ID','Kreis','X [m]','Y [m]','Z [m]','P [W]','Ib [A]','P x Trassenweg [Wm]']]);
rows(l,'A5:H16',source.Loads.map(x=>[x.ID,x.Circuit,+x.X_m,+x.Y_m,+x.Z_m,+x.Power_W,null,null]));
for(let r=5;r<=16;r++){l.getRange(`G${r}`).formulas=[[`=F${r}/Vorberechnung!$B$7/Vorberechnung!$B$8`]];l.getRange(`H${r}`).formulas=[[`=F${r}*(C${r}-Vorberechnung!$B$11+Vorberechnung!$B$12)`]];}
rows(l,'A19',[['Datenquelle: vorhandene Relux-/CAD-Leuchtenliste V1.1, in V1.3 unveraendert.']]);
rows(c,'A17',[['Kreis','Anzahl','P nominal [W]','Ib Szenario [A]','Summe P L [Wm]','Delta U_R [V]','Delta U_R [%]'],['A'],['B'],['Gesamt']]);
for(let r=18;r<=19;r++){
 c.getRange(`B${r}`).formulas=[[`=COUNTIFS(Leuchten!B5:B16,A${r})`]];
 c.getRange(`C${r}`).formulas=[[`=SUMIFS(Leuchten!F5:F16,Leuchten!B5:B16,A${r})`]];
 c.getRange(`D${r}`).formulas=[[`=C${r}/$B$7/$B$8`]];
 c.getRange(`E${r}`).formulas=[[`=SUMIFS(Leuchten!H5:H16,Leuchten!B5:B16,A${r})+$B$13*$B$14`]];
 c.getRange(`F${r}`).formulas=[[`=2*$B$9*E${r}/$B$10/$B$7`]];
 c.getRange(`G${r}`).formulas=[[`=F${r}/$B$7*100`]];
}
c.getRange('B20:D20').formulas=[['=SUM(B18:B19)','=SUM(C18:C19)','=SUM(D18:D19)']];
rows(c,'A23',[['Methode: radialer A/B-Trunk, aktive Lasten; Delta U_R = 2 rho/(S U0) x [Summe(Pi Li) + Plast LAbzweig].'],['Li = Xi - XUV + gemeinsamer Querweg. Weitere Abzweige sind nicht Teil des letzten Leitungsweges.'],['Nur resistiver Anteil: Reaktanz, Einspeisung und reale Temperatur/Kabeldaten fehlen. Kein Grenzwertnachweis.'],['Ib = P/(U0 cos phi). Einschaltstroeme, C/D-Zusatzlasten, Neutralleiter und Phasenaufteilung fehlen.']]);
rows(c,'A29',[['Kurzschluss / Abschaltung','Missing - Z Quelle, Netzform und Schutzorgan fehlen'],['Ueberlast / Iz','Missing - Verlegeart, Kabeltyp, Haeufung und Temperatur fehlen'],['Selektivitaet','Missing - Vorsicherung, Abgangsgeraete und Herstellerkennlinien fehlen'],['SPD / Bahnerdung','Preliminary - Konzept, keine Typ- oder Anschlussfreigabe']]);
rows(c,'A35',[['Quellen (geprueft 04.11.2026)'],['https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions'],['https://asean.prysmian.com/sites/asean.prysmian.com/files/media/documents/241218%20-%20Prysmian%20Electrical%20Information%20for%20Low%20Voltage%20Cables.pdf']]);
rows(n,'A2',[['Nachweisregister V1.3']]);
rows(n,'A4:D15',[['Nachweis','Status','Beleg','Naechster Schritt'],['Leuchtenanzahl / Positionen','Verified','Native Relux-Liste / CAD-Koordination','Keine Verschiebung'],['Nominale Beleuchtungsleistung','Verified','8 x 18.5 + 4 x 14 = 204 W','Treiberdaten bestaetigen'],['A/B-Aufteilung','Verified','je 6 Leuchten / 102 W','Phasen und Vorsicherung klaeren'],['Massen/Hoehen/Dachstuetzen','Preliminary','bestehendes Demo-CAD','Bestandsaufnahme'],['Native Lichtberechnung','Verified','Relux PDF / .rdf.log','Ergebnisbewertung separat'],['Lichtklasse / Normerfuellung','Missing','keine Zielwerte / Freigabe','Projektvorgaben einholen'],['Spannungsfall','Preliminary','Szenariorechnung','reale Kabelwege/Kabeldaten'],['Kurzschluss / Abschaltung','Missing','keine Netzimpedanz','Ik min/max beschaffen'],['Kabel / Schutzgeraete','Missing','keine Iz-/In-/Icn-Pruefung','vollstaendige Bemessung'],['Selektivitaet','Missing','keine Geraetekombination','Herstellertabellen pruefen'],['SPD / Erdung / Notbeleuchtung','Missing','nur Funktionskonzept','fachliche Schnittstellenfreigabe']]);
for(const s of [c,l,n]){const ar=s===c?'A1:G38':s===l?'A1:H20':'A1:D16';s.getRange(ar).format.font.name='Arial';s.getRange(ar).format.font.size=10;s.getRange(ar).format.rowHeight=23;s.getRange(ar).format.columnWidth=20;}
c.getRange('D6:D14').format.columnWidth=53;c.getRange('A6:A14').format.columnWidth=29;c.getRange('B7:B14').format.fill='#FFF2CC';c.getRange('A17:G17').format.fill='#233448';c.getRange('A17:G17').format.font.color='#FFFFFF';c.getRange('A17:G17').format.rowHeight=32;c.getRange('A17:G17').format.wrapText=true;c.getRange('D18:G20').setNumberFormat('0.000');
l.getRange('A4:H4').format.fill='#233448';l.getRange('A4:H4').format.font.color='#FFFFFF';l.getRange('G5:H16').setNumberFormat('0.000');n.getRange('A4:D4').format.fill='#233448';n.getRange('A4:D4').format.font.color='#FFFFFF';n.getRange('A4:A15').format.columnWidth=30;n.getRange('C4:D15').format.columnWidth=48;
w.recalculate();console.log((await w.inspect({kind:'table',range:'Vorberechnung!A17:G20',include:'values,formulas',tableMaxRows:4,tableMaxCols:7})).ndjson);
await (await SpreadsheetFile.exportXlsx(w)).save(root+'/03_Elektro/Bahnsteig_V13_Berechnungen.xlsx');
for(const [sheet,range,name] of [['Vorberechnung','A6:G20','calc'],['Leuchten','A4:H16','loads'],['Nachweise','A4:D15','status']]){const b=await w.render({sheetName:sheet,range,scale:1.3});await fs.writeFile(`work/${name}.png`,new Uint8Array(await b.arrayBuffer()));}

