from pathlib import Path
import json,csv,shutil
O=Path('outputs/Bahnsteig_V1.3_Final'); C=O/'02_CAD'
loads=json.loads(Path('C:/Users/mouha/Downloads/Bahnsteig_V11_Deliverables/SIMARIS_INPUT_PREPARATION.json').read_text(encoding='utf-8-sig'))['Loads']
class D:
 def __init__(self):self.e=[];self.layers={'BORDER':7,'TEXT':7,'PLATFORM':7,'CANOPY':8,'SUPPORT':8,'CIRCUIT_A':1,'CIRCUIT_B':5,'PE_PA':3,'DIM':2,'DEVICES':7,'MISSING':6};self.n=[]
 def line(self,a,b,l='BORDER'):
  self.e+=['0','LINE','8',l,'10',str(a[0]),'20',str(a[1]),'30','0','11',str(b[0]),'21',str(b[1]),'31','0']
 def rect(self,x,y,w,h,l='BORDER'):
  for a,b in [((x,y),(x+w,y)),((x+w,y),(x+w,y+h)),((x+w,y+h),(x,y+h)),((x,y+h),(x,y))]:self.line(a,b,l)
 def text(self,x,y,s,h=3,l='TEXT'):
  self.e+=['0','TEXT','8',l,'10',str(x),'20',str(y),'30','0','40',str(h),'1',s]
 def circle(self,x,y,r,l):self.e+=['0','CIRCLE','8',l,'10',str(x),'20',str(y),'30','0','40',str(r)]
 def save(self,p,units):
  a=['0','SECTION','2','HEADER','9','$ACADVER','1','AC1009','9','$INSUNITS','70',str(units),'0','ENDSEC','0','SECTION','2','TABLES','0','TABLE','2','LAYER','70',str(len(self.layers))]
  for l,col in self.layers.items():a+=['0','LAYER','2',l,'70','0','62',str(col),'6','CONTINUOUS']
  a+=['0','ENDTAB','0','ENDSEC','0','SECTION','2','ENTITIES']+self.e+['0','ENDSEC','0','EOF'];p.write_text('\n'.join(a)+'\n',encoding='ascii')
d=D();d.rect(-5,-35,135,70);d.text(0,30,'BAHNSTEIG 50 Hz | V1.3 | LAGEPLAN',1.6);d.text(0,26.5,'Arbeitsprobe - PRELIMINARY / keine Ausfuehrungsfreigabe | 04.11.2026',.85)
d.rect(0,0,120,4,'PLATFORM');d.rect(45,-.5,30,5,'CANOPY');d.text(45,9,'Ueberdachung X=45...75 m',.9)
for x in (45.5,55,65,74.5):
 for y in (.2,3.8):d.rect(x-.16,y-.16,.32,.32,'SUPPORT')
for c,y,last in [('A',3.1,105),('B',.9,115)]:d.line((2,y),(last,y),'CIRCUIT_'+c)
d.rect(1,1.5,2,1,'DEVICES');d.text(0,7,'UV-01',.8)
for i,r in enumerate(loads):
 x=float(r['X_m']); c=r['Circuit'];l='CIRCUIT_'+c;y=3.1 if c=='A' else .9
 d.circle(x,2,.25,l);d.line((x-.2,1.8),(x+.2,2.2),l);d.line((x-.2,2.2),(x+.2,1.8),l);d.line((x,2),(x,y),l)
 d.text(x-1.8,5.5,r['ID']+'/'+c,.65,l);d.text(x-2,-3,str(float(r['Power_W']))+' W',.6,l)
d.line((0,-6),(120,-6),'DIM')
for x in(0,45,75,120):d.line((x,-5.4),(x,-6.6),'DIM')
d.text(53,-5.6,'120.00 m',.8,'DIM');d.text(57,7.2,'30.00 m',.8,'DIM');d.text(121,1,'4.00 m',.65,'DIM')
d.text(0,19,'12 Leuchten | 8 x 18.5 W + 4 x 14 W = 204 W',1.1)
d.text(0,15.8,'A: L01/03/05/07/09/11 = 102 W | B: L02/04/06/08/10/12 = 102 W',.85)
d.text(0,12.8,'Trassen schematisch: A y=3.1 / B y=0.9; reale Kabelwege und Verlegeart fehlen.',.8)
d.text(0,-10,'QUERSCHNITT UNTER DACH - schematisch, geometrische Hoehen in m',.85)
d.line((0,-24),(10,-24),'PLATFORM');d.rect(2.5,-19.25,5,.25,'CANOPY')
for x in(3.2,6.8):d.rect(x-.16,-23.92,.32,4.57,'SUPPORT')
d.circle(5,-19.7,.14,'DEVICES');d.text(11,-19,'Dach UK 4.75 / OK 5.00',.8);d.text(11,-21,'Leuchte unter Dach z=4.30',.8);d.text(11,-23,'Freie Abschnitte z=4.50',.8)
d.text(55,-13,'PLANUNGSSTATUS',1)
for j,s in enumerate(['Verified: native Relux-Positionen L01-L12 / Boden 120 x 4 m','Preliminary: Hoehen, Stuetzen, Trassen, Materialreflexion','Missing: Netzform, Netzimpedanz, Kabel- und Schutzbemessung','A/B verbessert Verfuegbarkeit; ersetzt keine Sicherheitsbeleuchtung.','Kein automatischer Anschluss von PE/PA an die Fahrschiene.']):d.text(55,-16-j*2.6,s,.7)
d.text(0,-32,'Einheit: 1 ZE = 1 m | Geometrie 1:1; PDF-Darstellung skaliert | B13-LP-01',.8)
d.save(C/'Bahnsteig_V13_Lageplan.dxf',6)
s=D();s.rect(8,8,404,281);s.text(15,276,'BAHNSTEIG 50 Hz | V1.3 | STROMLAUFPLAN UV-01',5)
s.text(15,267,'PRELIMINARY - Funktionsschema, keine Schutzgeraete oder Kabel freigegeben.',3.2,'MISSING')
s.rect(20,225,66,25,'DEVICES');s.text(24,242,'EINSPEISUNG',3.5);s.text(24,234,'400/230 V, 50 Hz',3);s.text(24,228,'Annahme / Netzform offen',2.5)
s.line((86,237),(115,237));s.rect(115,228,48,18,'DEVICES');s.text(119,239,'Q0 Trennfunktion',3);s.text(119,232,'Polzahl/Bemessung offen',2.5)
s.line((163,237),(375,237));s.text(178,243,'UV-01: Sammelschiene / N- und PE-Konzept netzabhaengig',3)
s.line((185,237),(185,217));s.rect(167,195,37,22,'MISSING');s.text(171,209,'SPD-Konzept',3);s.text(171,201,'Typ/Up/Uc offen',2.5);s.line((185,195),(185,185),'PE_PA')
for c,x,ids in [('A',250,'L01/03/05/07/09/11'),('B',345,'L02/04/06/08/10/12')]:
 l='CIRCUIT_'+c;s.line((x,237),(x,218),l);s.rect(x-25,192,50,26,'DEVICES');s.text(x-21,208,'F'+c+' Schutzfunktion',3,l);s.text(x-21,200,'LS / RCD-Konzept offen',2.5);s.text(x-21,194,'In, Icn, Kennlinie: offen',2.3)
 s.line((x,192),(x,170),l);s.rect(x-25,148,50,22,l);s.text(x-21,160,'K'+c+' Schaltfunktion',3,l);s.text(x-21,152,'Steuerung / Hand-Auto offen',2.4)
 s.line((x,148),(x,126),l);s.circle(x,120,6,l);s.line((x-4,116),(x+4,124),l);s.line((x-4,124),(x+4,116),l)
 s.text(x-30,105,'6 Leuchten / 102 W',3,l);s.text(x-30,98,ids,2.7,l);s.text(x-30,90,'Leitung: Typ / S / Laenge offen',2.4)
s.line((20,185),(385,185),'PE_PA');s.text(23,189,'PE / Potentialausgleich - System und Anschlussstellen projektbezogen nachweisen',2.8,'PE_PA')
s.line((60,185),(60,170),'PE_PA');s.line((49,170),(71,170),'PE_PA');s.line((52,166),(68,166),'PE_PA');s.line((56,162),(64,162),'PE_PA')
s.text(20,145,'ZUSAETZLICHE ABGAENGE',3.4);s.text(20,137,'C Informationsanzeige: Last und Anschluss fehlen',2.8);s.text(20,130,'D Beschallung: Last und Schnittstelle fehlen',2.8)
s.text(20,116,'NACHWEISE OFFEN',3.4,'MISSING')
for j,t in enumerate(['Netzimpedanz / Ik min-max / Abschaltbedingungen','Verlegeart / Haeufung / Temperatur / Iz','Treiber-cos phi / Einschaltstrom / RCD-Vertraeglichkeit','Selektivitaet zur Vorsicherung und SPD-Vorsicherung','Bahnerdung / PA / Rueckstrom- und Oberleitungsbereich']):s.text(20,108-7*j,t,2.6)
s.line((15,69),(405,69));s.text(20,58,'LASTBILANZ: 12 Leuchten / 204 W nominal; weitere Verbraucher sind nicht enthalten.',3.2)
s.text(20,49,'230-V-Szenario bei cos phi=0.95: Ib,A = Ib,B = 0.467 A. Vorberechnung, keine Auslegung.',2.8)
s.text(20,40,'A und B abwechselnd. Gemeinsame Einspeisung bleibt gemeinsamer Ausfallpunkt.',2.8)
s.text(20,31,'Funktionen F/KA/KB sind Platzhalter ohne Fabrikat, Nennstrom oder Freigabe.',2.8)
s.text(20,19,'04.11.2026 | B13-SLP-01 | Nicht massstaebliches Funktionsschema | Status: Preliminary',3)
s.save(C/'Bahnsteig_V13_Stromlaufplan.dxf',4)
with (O/'03_Elektro/Leuchten_und_Stromkreise.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(loads[0]),delimiter=';');w.writeheader();w.writerows(loads)
print('CAD source drawings and luminaire schedule prepared')
