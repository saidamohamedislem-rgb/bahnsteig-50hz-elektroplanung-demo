import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root='outputs/Bahnsteig_V1.7_Detailplanung';
const {loads,edges}=JSON.parse(await fs.readFile('work/detail17_input.json','utf8'));
const w=Workbook.create(),s=w.worksheets.add('Ergebnisse'),b=w.worksheets.add('Abschnitte');
const put=(sh,at,rows)=>{const n=Math.max(...rows.map(r=>r.length));sh.getRange(at).values=rows.map(r=>[...r,...Array(n-r.length).fill(null)]);};
put(s,'A2',[['Bahnsteig V1.7 - Spannungsfall je Leuchte']]);
put(s,'A3',[['Mohamed Saida | 04.11.2026 | Preliminary']]);
put(s,'A6',[['Leuchte','Kreis','P (W)','X (m)','Y (m)','Z (m)','Ib (A)','Abgang (%)','Gesamt (%)']]);
put(s,'A21',[['Kreis','Leuchten','Last (W)','Max. Gesamt (%)','SIMARIS A/B (%)']]);
for(let j=0;j<2;j++){
 const row=22+j,c=['A','B'][j];put(s,`A${row}`,[[c,null,null,null,[.596,.649][j]/100]]);
 s.getRange(`B${row}`).formulas=[[`=COUNTIFS(B7:B18,A${row})`]];
 s.getRange(`C${row}`).formulas=[[`=SUMIFS(C7:C18,B7:B18,A${row})`]];
 const refs=loads.map((l,k)=>l.Circuit===c?'I'+(7+k):null).filter(Boolean);
 s.getRange(`D${row}`).formulas=[[`=MAX(${refs.join(',')})`]];
}
put(s,'A25',[['Referenzeingaben','Wert','Einheit'],['U0',230,'V'],['cos phi',.95,'induktiv'],['rho Cu',.0225,'Ohm mm2/m'],['X je Leiter',.00008,'Ohm/m'],['L/N Querschnitt',1.5,'mm2'],['Zuleitung DeltaU nativ',.0001,'Anteil'],['Vergleichsmarke',.03,'Anteil, kein vereinbarter Sollwert']]);
put(s,'E26',[['A auf L1-N, B auf L2-N. Getrennte N-Leiter nach den RCDs.'],['Abschnittsrechnung: linearer stationaerer Laststrom, gleiche Spannung 230 V.'],['Zuleitung 0,010 % ist ein festes SIMARIS-Ergebnis, kein dynamischer Quellenlauf.'],['rho ist eine Betriebs-Referenzannahme; kein konkreter Kabelartikel bei 55 Grad C.'],['Kein Nachweis fuer LED-Inrush, Unsymmetrie, Oberschwingungen oder Selektivitaet.'],['SIMARIS-Spalte: gebuendelte Ersatzlast; andere Rechenparameter als Referenz.'],['Gelbe Zellen sind editierbare Eingaben. Ergebnisse sind Preliminary.']]);
put(s,'A36',[['Quellen / Eingabebasis'],['Leuchten_und_Stromkreise.csv: unveraenderte 12 Leuchten / 204 W.'],['Netzmodell_Leitungsabschnitte.csv: 24 schematische Leitungsabschnitte.'],['SIMARIS V1.6: Bericht S.6 und native Lastflussansicht, Zuleitung 0,010 %.'],['Prysmian Electrical Information, 18.12.2024, S.35: rho 0,0225 und X 0,08 mOhm/m.'],['https://asean.prysmian.com/sites/asean.prysmian.com/files/media/documents/241218%20-%20Prysmian%20Electrical%20Information%20for%20Low%20Voltage%20Cables.pdf'],['Schneider Electric: Calculation of voltage drop in steady load conditions, Fig.G29.'],['https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions'],['Abruf 04.11.2026. Reale Netz-, Kabel- und Verlegedaten fehlen.']]);
put(b,'A2',[['Bahnsteig V1.7 - 24 Leitungsabschnitte']]);
put(b,'A3',[['Mohamed Saida | Preliminary | Cu L/N 1,5 mm2 als Referenz']]);
put(b,'A6',[['ID','Von','Nach','Typ','Kreis','L (m)','S (mm2)','P nachg. (W)','Ib (A)','R je L (Ohm)','X je L (Ohm)','DeltaU (V)','Kumuliert (V)']]);
put(b,'A35',[['Leuchte','Kreis','P (W)','X (m)','Y (m)','Z (m)','Phase']]);
put(b,'A36',loads.map(l=>[l.ID,l.Circuit,+l.Power_W,+l.X_m,+l.Y_m,+l.Z_m,l.Circuit==='A'?'L1-N':'L2-N']));
const branchRows={};let cum={A:null,B:null};
for(let i=0;i<edges.length;i++){
 const e=edges[i],r=7+i,k=Number(e.ID.match(/\d+$/)[0])-1;
 const inds=loads.map((l,j)=>[l,j]).filter(([l,j])=>l.Circuit===e.Circuit);
 const loadRow=36+inds[k][1];
 put(b,`A${r}`,[[e.ID,e.From,e.To,e.Type==='Trunk'?'Stamm':'Stich',e.Circuit,+e.Length_m]]);
 b.getRange(`G${r}`).formulas=[[`='Ergebnisse'!$B$30`]];
 b.getRange(`H${r}`).formulas=[[e.Type==='Trunk'?`=SUM(${inds.slice(k).map(([,j])=>'C'+(36+j)).join(',')})`:`=C${loadRow}`]];
 b.getRange(`I${r}:L${r}`).formulas=[[
  `=H${r}/'Ergebnisse'!$B$26/'Ergebnisse'!$B$27`,
  `='Ergebnisse'!$B$28*F${r}/G${r}`,
  `='Ergebnisse'!$B$29*F${r}`,
  `=2*I${r}*(J${r}*'Ergebnisse'!$B$27+K${r}*SQRT(1-'Ergebnisse'!$B$27^2))`
 ]];
 b.getRange(`M${r}`).formulas=[[cum[e.Circuit]===null?`=L${r}`:`=M${cum[e.Circuit]}+L${r}`]];
 if(e.Type==='Trunk')cum[e.Circuit]=r;else branchRows[e.To]=r;
}
for(let i=0;i<loads.length;i++){
 const r=7+i,src=36+i,er=branchRows[loads[i].ID];
 s.getRange(`A${r}:F${r}`).formulas=[[...['A','B','C','D','E','F'].map(c=>`='Abschnitte'!${c}${src}`)]];
 s.getRange(`G${r}:I${r}`).formulas=[[
  `=C${r}/$B$26/$B$27`, `='Abschnitte'!M${er}/$B$26`, `=H${r}+$B$31`
 ]];
}
for(const [sh,range]of[[s,'A1:I44'],[b,'A1:M47']]){
 sh.showGridLines=false;sh.getRange(range).format.font.name='Arial';sh.getRange(range).format.font.size=10;
 sh.getRange(range).format.rowHeight=22;sh.getRange(range).format.columnWidth=14;
 sh.getRange(range).format.verticalAlignment='center';sh.getRange('A2').format.font.size=14;
 sh.getRange('A3').format.font.italic=true;
}
s.tabColor='#233448';b.tabColor='#8193A5';
s.getRange('A1:A44').format.columnWidth=18;s.getRange('B25:B32').format.columnWidth=18;
s.getRange('C25:C32').format.columnWidth=23;
s.getRange('H6:I6').format.wrapText=true;s.getRange('A6:I6').format.rowHeight=34;
s.getRange('D21:E21').format.wrapText=true;s.getRange('A21:E21').format.rowHeight=34;
s.getRange('G7:I18').setNumberFormat('0.000');s.getRange('H7:I18').setNumberFormat('0.000%');
s.getRange('D22:E23').setNumberFormat('0.000%');s.getRange('B31:B32').setNumberFormat('0.000%');
s.getRange('B26:B30').setNumberFormat('0.00000');s.getRange('B26:B30').format.fill='#FFF2CC';s.getRange('B32').format.fill='#FFF2CC';
s.getRange('B31').format.fill='#E8EDF2';s.getRange('E22:E23').format.fill='#E8EDF2';
b.getRange('F7:F30').format.fill='#FFF2CC';b.getRange('C36:F47').format.fill='#FFF2CC';
b.getRange('A1:E47').format.columnWidth=16;b.getRange('H6:M6').format.columnWidth=17;
b.getRange('A6:M6').format.wrapText=true;b.getRange('A6:M6').format.rowHeight=34;
b.getRange('F7:M30').setNumberFormat('0.000');b.getRange('C36:F47').setNumberFormat('0.0');
b.getRange('J7:K30').setNumberFormat('0.00000');
for(const[sh,range]of[[s,'A6:I6'],[s,'A21:E21'],[s,'A25:C25'],[b,'A6:M6'],[b,'A35:G35']]){
 sh.getRange(range).format.fill='#233448';sh.getRange(range).format.font.color='#FFFFFF';sh.getRange(range).format.horizontalAlignment='center';
}
b.freezePanes.freezeRows(6);b.freezePanes.freezeColumns(1);
s.getRange('I7:I18').conditionalFormats.addCustom('I7>$B$32',{fill:'#FCE4D6',font:{color:'#9C0006'}});
w.recalculate();
let actual=loads.map((l,i)=>({ID:l.ID,Circuit:l.Circuit,Power_W:+l.Power_W,deltaU_percent:s.getRange('I'+(7+i)).values[0][0]*100}));
// Independent direct summation of every current-carrying route segment, including a non-final sample.
for(let i=0;i<loads.length;i++){
 const l=loads[i],same=loads.filter(x=>x.Circuit===l.Circuit),idx=same.findIndex(x=>x.ID===l.ID);
 let du=0;
 for(let k=0;k<=idx;k++){
  const e=edges.find(e=>e.ID===`${l.Circuit}_TR${k+1}`),P=same.slice(k).reduce((a,x)=>a+Number(x.Power_W),0);
  const L=+e.Length_m;du+=2*(P/230/.95)*(.0225*L/1.5*.95+.00008*L*Math.sqrt(1-.95**2));
 }
 const L=+edges.find(e=>e.To===l.ID).Length_m;du+=2*(+l.Power_W/230/.95)*(.0225*L/1.5*.95+.00008*L*Math.sqrt(1-.95**2));
 if(Math.abs(actual[i].deltaU_percent-(du/230+.0001)*100)>1e-9)throw Error('Independent route check failed '+l.ID);
}
const before=s.getRange('I17').values[0][0],orig=b.getRange('F7').values[0][0];
b.getRange('F7').values=[[orig+10]];
const after=s.getRange('I17').values[0][0];if(!(after>before))throw Error('Length dependency failed');
b.getRange('F7').values=[[orig]];
const origP=b.getRange('C36').values[0][0];b.getRange('C36').values=[[0]];
if(s.getRange('C22').values[0][0]!==83.5||s.getRange('G7').values[0][0]!==0)throw Error('Zero-load dependency failed');
b.getRange('C36').values=[[origP]];w.recalculate();
const errors=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},summary:'Final formula error scan'});
console.log(errors.ndjson);
console.log((await w.inspect({kind:'table',range:'Ergebnisse!A21:E23',include:'values,formulas',maxChars:1800,tableMaxRows:3,tableMaxCols:5})).ndjson);
await fs.writeFile('work/v17_detail_results.json',JSON.stringify({author:'Mohamed Saida',results:actual,independent_all12:true,length_dependency:true,zero_load_dependency:true},null,2));
await (await SpreadsheetFile.exportXlsx(w)).save(root+'/03_Elektro/Bahnsteig_V17_Leitungsberechnung.xlsx');
for(const[sh,range,file]of[['Ergebnisse','A1:I23','14_V17_Leuchten_Spannungsfall.png'],['Abschnitte','A5:M19','15_V17_Leitungsabschnitte.png']]){
 const blob=await w.render({sheetName:sh,range,scale:1.25});await fs.writeFile(root+'/04_Screenshots/'+file,new Uint8Array(await blob.arrayBuffer()));
}
console.log(JSON.stringify({independent_all12:true,length_dependency:true,zero_load_dependency:true,maxA:actual.filter(x=>x.Circuit==='A').at(-1).deltaU_percent,maxB:actual.filter(x=>x.Circuit==='B').at(-1).deltaU_percent}));
