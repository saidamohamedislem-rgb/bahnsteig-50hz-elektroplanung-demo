from pathlib import Path
import hashlib, json, html, shutil, urllib.parse
import pypdfium2 as pdfium
from PIL import Image

root=Path('outputs/Bahnsteig_V1.8_Arbeitsprobe')
out=Path('outputs/Bericht_Abbildungen_HD')
(out/'Original_PDF').mkdir(exist_ok=True,parents=True)
records=[]
def render(src,page,name,crop=None):
    doc=pdfium.PdfDocument(root/src)
    im=doc[page-1].render(scale=400/72).to_pil().convert('RGB')
    if crop:
        w,h=im.size
        im=im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(crop)))
    im.save(out/name,dpi=(400,400))
    records.append(dict(file=name,type='PDF-Rendering / Ausschnitt' if crop else 'PDF-Rendering / vollstaendige Seite',source=src,page=page,crop_normalized=crop,width=im.width,height=im.height,source_sha256=hashlib.sha256((root/src).read_bytes()).hexdigest()))

cad='02_CAD/Bahnsteig_Mohamed_Saida_Detailstromlaufplan.pdf'
lage='02_CAD/Bahnsteig_V13_Lageplan.pdf'
iso='01_Relux/Relux_V13_Final_Tabellen_Isolux.pdf'
false='01_Relux/Relux_V13_Final_FalseColours.pdf'
render(cad,1,'10_Stromlaufplan_Druckqualitaet_400dpi.png')
render(cad,1,'11_Stromlaufplan_Einspeisung_Detail.png',(.01,.01,.99,.25))
render(cad,1,'12_Stromlaufplan_Kreis_A_Detail.png',(.01,.235,.99,.515))
render(cad,1,'13_Stromlaufplan_Kreis_B_Detail.png',(.01,.52,.99,.795))
render(lage,1,'14_Lageplan_Druckqualitaet_400dpi.png')
render(iso,16,'15_Relux_Isolux_Originalseite_400dpi.png')
render(false,1,'16_Relux_FalseColours_Originalseite_400dpi.png')
render(iso,16,'17_Relux_Isolux_Planstreifen.png',(.065,.335,.87,.400))
render(false,1,'18_Relux_FalseColours_Planstreifen.png',(.065,.335,.87,.400))
render(false,1,'19_Relux_FalseColours_Dachdetail.png',(.373,.34,.575,.400))
render(false,1,'20_Relux_Farbskala_und_Ergebnisse.png',(.07,.59,.93,.78))
render(iso,5,'21_Relux_Leuchtenliste_400dpi.png')
render(iso,7,'22_Relux_Ergebnistabelle_400dpi.png')
for src in (cad,lage,iso,false):
    shutil.copy2(root/src,out/'Original_PDF'/Path(src).name)
native=[]
repo=Path('C:/Users/mouha/OneDrive/Documents/bahnsteig-50hz-elektroplanung-demo/07_Projektstaende')
for p in sorted(out.glob('0*.png')):
    with Image.open(p) as im: fmt=im.format
    if fmt=='JPEG':
        corrected=p.with_suffix('.jpg')
        p.rename(corrected)
        duplicate=repo/out.name/p.name
        if duplicate.exists(): duplicate.unlink()
for p in sorted(out.glob('0*.jpg')):
    with Image.open(p) as im:
        native.append(dict(file=p.name,type='Native Bildschirmaufnahme, 05.11.2026',width=im.width,height=im.height))
records=native+records
(out/'ABBILDUNGSNACHWEIS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# Abbildungen fuer den Bericht','', 'Mohamed Saida | 05.11.2026','',
'## Verwendung','',
'Fuer den Bericht die Dateien 10-22 verwenden: verlustfreie PNG-Ansichten aus den unveraenderten nativen PDF-Ausgaben mit 400 dpi. Die Original-PDFs liegen im Unterordner Original_PDF. Die vollstaendigen Seiten erhalten Kopfzeilen, Skalen und Ergebnisangaben. Detailausschnitte immer gemeinsam mit ihrer Uebersichtsseite bzw. Farbskala verwenden. Ein Ausschnitt ist keine vollstaendige Ergebnisdarstellung.','',
'01-07 sind neue native Bildschirmaufnahmen aus maximierten Programmfenstern. 04 zeigt die Ueberdachung in einer vergroesserten schattierten BricsCAD-Ansicht. Dunkelblaue CAD-Layer sind auf dunklem Bildschirm schlechter lesbar; fuer diese Beschriftungen die PDF-Renderings 10-14 bevorzugen.','',
'Die schmale Geometrie von 120 x 4 m erfordert eine Uebersicht und zusaetzliche Details. Kein nachtraegliches Hochskalieren alter Screenshots. Es wurden nur Ansichten, Zoom und Darstellungsmodi angepasst; keine Leuchten oder Berechnungsergebnisse geaendert. Alte Aufnahmen bleiben im V1.8-Ordner erhalten.','',
'Die PDF-Kopfzeilen enthalten historische Projektmetadaten. Das ist unveraenderte Softwareausgabe. Der Planungsstatus bleibt Vorplanung; die Abbildungen sind keine Ausfuehrungsfreigabe.','',
'## Quellen und Bildgroessen','', '| Datei | Herkunft | Pixel |','|---|---|---|']
for r in records:
    src=(r.get('source','BricsCAD V26 / ReluxDesktop 2026.2')+(' | Seite '+str(r['page']) if 'page'in r else '')).replace('|',';')
    lines.append(f"| {r['file']} | {r['type']}; {src} | {r['width']} x {r['height']} |")
(out/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
cards=[]
for r in sorted(records,key=lambda r:(r['file']<'10',r['file'])):
    u=urllib.parse.quote(r['file'])
    cards.append(f'<article><a href="{u}" target="_blank"><img loading="lazy" src="{u}" alt="{html.escape(r["file"])}"></a><b>{html.escape(r["file"])}</b><p>{html.escape(r["type"])} · {r["width"]} × {r["height"]} px</p></article>')
page='''<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bericht-Abbildungen HD | Mohamed Saida</title><style>body{margin:0;background:#edf1f5;color:#203247;font:17px/1.55 Arial}main{max-width:1450px;margin:auto;padding:28px}header,article{background:white;border:1px solid #d2dce6;border-radius:12px;padding:22px}h1{margin:0}a{color:#125eb0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(400px,1fr));gap:18px;margin-top:24px}article{padding:12px;overflow-wrap:anywhere}img{width:100%;height:300px;object-fit:contain;background:#f7f9fb}b{display:block;margin:10px 0}p{margin:6px 0}article p{font-size:14px;color:#5c6877}</style><main><header><h1>Bericht-Abbildungen in hoher Aufloesung</h1><p>Mohamed Saida · Bahnsteig 50 Hz · 05.11.2026</p><p dir="rtl">انقر على الصورة باش تشوفها بالحجم الكامل. للـBericht استعمل خاصة الصور 10-22؛ التفاصيل عندها صور مستقلّة ومعاها الصفحة الأصلية.</p><p>10-22: PNG aus Original-PDF, 400 dpi. 01-07: neue native Bildschirmaufnahmen. Ausschnitte zusammen mit Uebersicht und Farbskala verwenden.</p><a href="README.md">Bildnachweise und Verwendung</a> · <a href="Original_PDF/">Original-PDFs</a></header><div class="grid">'''+''.join(cards)+'</div></main></html>'
(out/'START.html').write_text(page,encoding='utf-8')
for r in records:
    p=out/r['file']
    with Image.open(p) as im: im.verify()
shutil.copytree(out,repo/out.name,dirs_exist_ok=True)
print(json.dumps({'images':len(records),'output':str(out.resolve()),'png_decode_check':'PASS'},ensure_ascii=False))
