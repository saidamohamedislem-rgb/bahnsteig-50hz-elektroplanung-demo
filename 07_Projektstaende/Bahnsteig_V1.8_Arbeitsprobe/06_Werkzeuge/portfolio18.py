from pathlib import Path
import shutil,csv
from pypdf import PdfReader,PdfWriter
from pypdf.generic import RectangleObject
import pypdfium2 as pdfium
from PIL import Image,ImageChops
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing,Rect,Line,Circle,String

R=Path('outputs/Bahnsteig_V1.8_Arbeitsprobe');V=R/'00_Vorstellung';V.mkdir(exist_ok=True)
work=Path('work/review18');work.mkdir(exist_ok=True)
# Preserve the exact native full-page plot, then create a readable landscape crop.
p=R/'02_CAD/Bahnsteig_Mohamed_Saida_Detailstromlaufplan.pdf'
native=R/'02_CAD/Native_Ausgabe';native.mkdir(exist_ok=True)
original=native/'Detailstromlaufplan_Originalseite.pdf'
if not original.exists():shutil.copy2(p,original)
d=pdfium.PdfDocument(original);im=d[0].render(scale=2).to_pil().convert('RGB')
box=ImageChops.difference(im,Image.new('RGB',im.size,'white')).getbbox()
rd=PdfReader(original);pg=rd.pages[0];h=float(pg.mediabox.height)
rect=[max(0,box[0]/2-6),max(0,h-box[3]/2-6),min(float(pg.mediabox.width),box[2]/2+6),min(h,h-box[1]/2+6)]
pg.cropbox=RectangleObject(rect);pg.mediabox=RectangleObject(rect);w=PdfWriter();w.add_page(pg)
with p.open('wb')as f:w.write(f)
pdfium.PdfDocument(p)[0].render(scale=1.7).to_pil().save(work/'Detailplan_Lesefassung.png')

pdfmetrics.registerFont(TTFont('ProjectArial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ProjectArialBold','C:/Windows/Fonts/arialbd.ttf'))
sty=getSampleStyleSheet()
for name in ['Normal','BodyText','Heading1','Heading2','Title']:
 sty[name].fontName='ProjectArial';sty[name].textColor=colors.HexColor('#203247')
sty['BodyText'].fontSize=10;sty['BodyText'].leading=14;sty['BodyText'].spaceAfter=9
sty['Title'].fontName='ProjectArialBold';sty['Title'].fontSize=25;sty['Title'].leading=29;sty['Title'].alignment=TA_LEFT;sty['Title'].spaceAfter=14
sty['Heading1'].fontName='ProjectArialBold';sty['Heading1'].fontSize=18;sty['Heading1'].leading=23;sty['Heading1'].spaceAfter=13
sty['Heading2'].fontName='ProjectArialBold';sty['Heading2'].fontSize=12;sty['Heading2'].leading=16;sty['Heading2'].spaceBefore=11;sty['Heading2'].spaceAfter=7
sty.add(ParagraphStyle(name='SmallProject',parent=sty['BodyText'],fontSize=8,leading=11,spaceAfter=7))
P=lambda t,style='BodyText':Paragraph(t,sty[style])
def table(rows,widths):
 header=ParagraphStyle(name='TableHeader',parent=sty['SmallProject'],textColor=colors.white,fontName='ProjectArialBold')
 t=Table([[Paragraph(str(c),header) if i==0 else P(str(c),'SmallProject')for c in row]for i,row in enumerate(rows)],colWidths=widths,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#203247')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#203247')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F1F4F7')])]))
 return t
def footer(c,doc):
 c.setStrokeColor(colors.HexColor('#CED6DF'));c.line(43,39,552,39)
 c.setFont('ProjectArial',8);c.setFillColor(colors.HexColor('#617084'));c.drawString(43,26,'Mohamed Saida | Bahnsteig 50 Hz | Arbeitsprobe V1.8 | 05.11.2026');c.drawRightString(552,26,str(doc.page))
loads=list(csv.DictReader((R/'03_Elektro/Leuchten_und_Stromkreise.csv').open(encoding='utf-8-sig'),delimiter=';'))
plan=Drawing(500,112);scale=3.9;x0=12;y0=40
plan.add(Rect(x0,y0,120*scale,4*scale,fillColor=colors.HexColor('#EDF1F5'),strokeColor=colors.HexColor('#526477'),strokeWidth=.8))
plan.add(Rect(x0+45*scale,y0-.5*scale,30*scale,5*scale,fillColor=colors.HexColor('#D3DDE8'),strokeColor=colors.HexColor('#526477'),strokeWidth=.8))
plan.add(String(x0+45*scale,87,'Überdachung X = 45 bis 75 m',fontName='ProjectArial',fontSize=9,fillColor=colors.HexColor('#203247')))
for l in loads:
 x=x0+float(l['X_m'])*scale;col=colors.HexColor('#BF3141'if l['Circuit']=='A'else'#225CAE')
 plan.add(Circle(x,y0+2*scale,2.7,fillColor=col,strokeColor=col));plan.add(String(x-8,66,l['ID'],fontName='ProjectArial',fontSize=8,fillColor=col))
plan.add(Line(x0,22,x0+120*scale,22,strokeColor=colors.HexColor('#526477'),strokeWidth=.5))
for x in [x0,x0+120*scale]:plan.add(Line(x,18,x,26,strokeColor=colors.HexColor('#526477')))
plan.add(String(218,8,'120 m Länge / 4 m Breite',fontName='ProjectArial',fontSize=9,fillColor=colors.HexColor('#203247')))

story=[P('Bahnsteig 50 Hz<br/>Elektroplanung','Title'),P('Mohamed Saida - Arbeitsprobe für das Vorstellungsgespräch','Heading2'),P('Lichtplanung, CAD-Koordination und elektrische Vorplanung an einem fiktiven 120-m-Bahnsteig. Die Unterlagen verbinden ein bearbeitbares Modell mit echten Programmausgaben und einer nachvollziehbaren Abschnittsrechnung.'),P('1. Aufgabe und Planungsmodell','Heading2'),plan,P('Zwölf vorhandene Leuchten bleiben in ihren Positionen erhalten. Die Kreise A und B versorgen abwechselnd je sechs Leuchten. Die Überdachung liegt zwischen X = 45 und X = 75 m. Unter dem Dach beträgt die Leuchtenhöhe 4,3 m, außerhalb 4,5 m.'),table([['Kenngröße','Modell'],['Bahnsteig / Überdachung','120 × 4 m / 30 m Länge, 5 m Dachbreite'],['Leuchten / Anschlussleistung','8 × 18,5 W + 4 × 14 W = 204 W; A/B je 102 W'],['Software','ReluxDesktop 2026.2, BricsCAD V26, SIMARIS design 27.0.1']], [180,329]),P('2. Ergebnis der Lichtberechnung','Heading2'),table([['Auswertung Floor (E)','Relux-Modellergebnis'],['Em / Emin / Emax','18,1 lx / 7,96 lx / 37 lx'],['Gleichmäßigkeit Emin/Em','0,44'],['Wartungsfaktor','0,8']], [230,279]),P('Isolux, False Colours und Rasterwerte liegen als native Relux-Ausgabe vor. Eine Bewertung gegen verbindliche Licht-Sollwerte ist nicht Gegenstand dieses Modellvergleichs.','SmallProject'),PageBreak()]
story += [P('Elektrische Planung','Heading1'),P('3. Zwei Modelle mit unterschiedlichem Detailgrad','Heading2'),P('<b>SIMARIS:</b> zwei Ersatzlasten zu je 102 W am letzten Punkt des jeweiligen Kreises. A liegt auf L1-N, B auf L2-N. Das vorhandene Projekt wurde dimensioniert; die Meldungsliste zeigte Messages [0].'),P('<b>Abschnittsrechnung:</b> zwölf Einzellasten und 24 Stamm-/Stichabschnitte. In jedem Stammstück wird nur die dahinter liegende Last berücksichtigt. Die bearbeitbare Formelmappe zeigt den Spannungsfall je Leuchte.'),table([['Ergebnis','Kreis A','Kreis B'],['Spannungsfall kumuliert, nativ SIMARIS','0,596 %','0,649 %'],['Spannungsfall verteilt, Referenz','0,329376 %','0,387322 %'],['Minimaler Endfehlerstrom L-N / L-PE, nativ','59,029 A','54,374 A'],['Kabel-Iz im nativen Szenario','19,5 A','19,5 A']], [265,122,122]),P('Die geringeren Referenzwerte ergeben sich aus verteilter Last und abweichenden Widerstandsannahmen. Die Gegenüberstellung ist kein identischer Zweitlauf des SIMARIS-Rechenkerns.','SmallProject'),P('4. Eingaben und automatische Geräteauswahl','Heading2'),P('Quellenannahme: 400/230 V, TN-S, 50 Hz, Ik1/Ik3 min. 1,5 kA und max. 3 kA. Zuleitung: 10 m Cu/PVC70, L/N/PE 4 mm². Abgänge: 109,7 / 119,7 m, L/N/PE 1,5 mm², Verlegeart C, Faktor 1. Die Referenzmappe verwendet eigene Betriebswiderstandsannahmen.'),table([['Funktion','Native Kandidaten'],['Einspeisung','gG 25 A, 3NA3810, Sockel 3NH4030'],['LS je Abgang','B1 A, Icn 10 kA, 5SY41016'],['RCD je Abgang','Typ A, 25 A / 30 mA, 5SV33126']], [180,329]),P('<b>Fachlicher Prüffund:</b> Die Quelle ist mit 20 A bemessen, die automatische Auswahl liefert gG25. Das muss vor einer Gerätefreigabe abgestimmt werden. B1 A benötigt außerdem die Prüfung des LED-Einschaltstroms. Die vorhandenen Kennlinien enthalten keine ausgefüllte Gesamtselektivitätsbewertung.'),P('Der neue CAD-Stromlaufplan zeigt alle zwölf Leuchten mit 24 Abschnitts-IDs, getrennten Neutralleitern nach den RCDs und den aktuellen Gerätekandidaten.','SmallProject'),PageBreak()]
story += [P('Vorgehen und Lerninhalte','Heading1'),table([['Arbeitsschritt','Im Projekt nachvollziehbar'],['Geometrie koordinieren','Einheiten und globale Koordinaten abgleichen; Plattform und Dach nicht doppelt importieren; bestehende Leuchten erhalten.'],['Licht auswerten','Wartungsfaktor, Em/Emin/Emax und Gleichmäßigkeit gemeinsam betrachten; Ergebnisse mit Isolux und False Colours erläutern.'],['Stromkreise strukturieren','A/B-Zuordnung, gemeinsame Einspeisung und verbleibenden gemeinsamen Ausfallpunkt erkennen.'],['Lastverteilung berechnen','Ersatzlast und verteilte Last unterscheiden; nachgelagerte Leistung und Spannungsfall abschnittsweise summieren.'],['Schutz kritisch prüfen','Ib, In und Iz vergleichen; Kurzschlussströme und Ausschaltvermögen lesen; automatische Auswahl und Selektivitätsnachweis auseinanderhalten.'],['Planungsstand dokumentieren','DWG, native Rechenprojekte, Tabellen, PDF-Ausgaben und Originalstände getrennt und nachvollziehbar ablegen.']], [155,354]),P('Vorschlag für die Vorstellung','Heading2'),P('Mit dem Lageplan beginnen, anschließend das Lichtresultat zeigen. Danach am A/B-Stromlaufplan die Lastverteilung erklären. Einen Spannungsfallwert bis zur Formelmappe zurückverfolgen. Zum Schluss den Unterschied zwischen einem berechneten Modellergebnis und einer freigegebenen Geräteauswahl am Beispiel gG25/B1 erläutern.'),P('Rahmen der Arbeitsprobe','Heading2'),P('Fiktives Lern- und Portfolio-Projekt. Netz-, Verlege- und Treiberdaten sind Modellannahmen, keine Messwerte. Die Unterlagen zeigen den Planungsablauf; sie sind keine Ausführungsfreigabe. Für ein reales Projekt wären insbesondere Quelle/Vorsicherung, LED-Inrush, Selektivität, SPD, Erdung/Bahn-PA und Lichtanforderungen zu vervollständigen.'),P('Material für den späteren Bericht','Heading2'),P('Bearbeitbare Relux-/SIMARIS-Projekte und DWG/DXF; native Licht- und Elektroberichte; Formelmappe für zwölf Leuchten; Screenshots; deutsche Bericht-Grundlage. Der lange Abschlussbericht wird daraus erst später erstellt.'),P('Belege und Quellen','Heading2'),P('Primärbelege: Relux-Gesamtbericht, S.5-18; SIMARIS-Projektdokumentation, S.2-9; native Schutzkennlinien; V1.7-Leitungsberechnung. Formeln: Schneider Electric, Fig.G29, <link href="https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions" color="#225CAE">Electrical Installation Guide</link>. Referenzwerte: Prysmian, Electrical Information for Low Voltage Cables, 18.12.2024, S.35. Vollständige Quellen- und Dateiliste im Projektordner.','SmallProject')]
out=V/'01_Arbeitsprobe_Mohamed_Saida_Kurzueberblick.pdf'
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=42,bottomMargin=53,title='Bahnsteig 50 Hz - Arbeitsprobe Mohamed Saida',author='Mohamed Saida')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
assert len(PdfReader(out).pages)==3,'Summary layout must stay at three pages'
selected=[(p,'02_Detailstromlaufplan.pdf'),(R/'09_SIMARIS/SIMARIS_Mohamed_Saida_Berechnungsbericht.pdf','03_SIMARIS_Berechnung.pdf'),(R/'09_SIMARIS/SIMARIS_Mohamed_Saida_Schutzkennlinien.pdf','04_SIMARIS_Schutzkennlinien.pdf'),(R/'09_SIMARIS/Export_Mohamed_Saida/Bahnsteig_V17_Mohamed_Saida.pdf','05_SIMARIS_Netzansichten.pdf'),(R/'01_Relux/Relux_V13_Final_Gesamtbericht.pdf','06_Relux_Originalbericht.pdf')]
for src,name in selected:shutil.copy2(src,V/name)
writer=PdfWriter();pos=0
for file,label in [(out,'Kurzüberblick - Mohamed Saida'),*[(V/name,name[3:-4].replace('_',' '))for _,name in selected]]:
 reader=PdfReader(file)
 for page in reader.pages:writer.add_page(page)
 writer.add_outline_item(label,pos)
 pos+=len(reader.pages)
writer.add_metadata({'/Title':'Bahnsteig 50 Hz - Nachweismappe','/Author':'Mohamed Saida','/Subject':'Fiktive Arbeitsprobe: Kurzueberblick und unveraenderte Originalausgaben'})
with (V/'00_Nachweismappe_Mohamed_Saida.pdf').open('wb')as f:writer.write(f)
d=pdfium.PdfDocument(out)
for i in range(len(d)):d[i].render(scale=1.3).to_pil().save(work/f'Kurzueberblick_{i+1}.png')
print('Three-page overview; named original outputs; bookmarked evidence packet:',pos,'pages')
