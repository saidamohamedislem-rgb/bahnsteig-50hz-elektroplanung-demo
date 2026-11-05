from pathlib import Path
import html,json,urllib.parse,shutil

base=Path('outputs/Bahnsteig_V1.8_Arbeitsprobe')
out=Path('outputs/Bericht_Material_Start.html')
def url(p):return urllib.parse.quote(base.name+'/'+p, safe='/')
def link(p,label):
 assert (base/p).is_file(),p
 return '<a target="_blank" href="'+url(p)+'">'+html.escape(label)+'</a>'
primary=[
 ('00_Vorstellung/00_Nachweismappe_Mohamed_Saida.pdf','الملف الكامل — 44 صفحة مع الفهرس'),
 ('00_Vorstellung/01_Arbeitsprobe_Mohamed_Saida_Kurzueberblick.pdf','الملخّص — 3 صفحات'),
 ('00_Vorstellung/02_Detailstromlaufplan.pdf','Stromlaufplan — الرسم الحالي A/B'),
 ('00_Vorstellung/03_SIMARIS_Berechnung.pdf','SIMARIS — الحساب الأصلي'),
 ('00_Vorstellung/04_SIMARIS_Schutzkennlinien.pdf','SIMARIS — منحنيات الحماية'),
 ('00_Vorstellung/06_Relux_Originalbericht.pdf','Relux — التقرير الأصلي'),
 ('01_Relux/Relux_V13_Final_Tabellen_Isolux.pdf','Relux — Tabellen und Isolux'),
 ('01_Relux/Relux_V13_Final_FalseColours.pdf','Relux — False Colours'),
 ('03_Elektro/Bahnsteig_V17_Leitungsberechnung.xlsx','Excel — حسابات الـ12 مصباح'),
 ('BERICHT_GRUNDLAGE.md','BERICHT_GRUNDLAGE — معلومات البداية'),
 ('QUELLEN.md','Quellen — المراجع'),
 ('PRUEFSTATUS.csv','Verified / Preliminary / Missing')]
files=[p for p in sorted(base.rglob('*')) if p.is_file() and p.suffix.lower()not in ['.dwl','.dwl2'] and not p.name.startswith('~$') and not p.name.endswith('.inspect.ndjson')]
images=[p for p in files if p.suffix.lower()in ['.png','.jpg','.jpeg']]
cards=[]
for p in images:
 rel=p.relative_to(base).as_posix()
 if 'sel_node_'in p.name:group='SIMARIS — original curves'
 elif any(x in p.name for x in ['ELEK','V15','V16']):group='Historisch / صورة مرحلة سابقة'
 elif p.name.startswith(('16_','17_')):group='V1.8 — الوثائق الحالية'
 else:group='الموديل والصور المحفوظة'
 cards.append('<article class="imagecard" data-search="'+html.escape(rel.lower())+'"><a href="'+url(rel)+'" target="_blank"><img loading="lazy" src="'+url(rel)+'" alt="'+html.escape(p.stem)+'"></a><p>'+html.escape(group)+'</p><b dir="ltr">'+html.escape(p.name)+'</b></article>')
rows=[]
for p in files:
 rel=p.relative_to(base).as_posix()
 rows.append('<li data-search="'+html.escape(rel.lower())+'">'+link(rel,rel)+' <small>'+str(round(p.stat().st_size/1024,1))+' KB</small></li>')
page='''<!doctype html><html lang="ar" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bericht-Material — Mohamed Saida</title>
<style>*{box-sizing:border-box}body{margin:0;background:#f2f5f8;color:#203247;font:17px/1.6 Arial,sans-serif}main{max-width:1400px;margin:auto;padding:30px}header{background:white;border-radius:16px;padding:26px;border:1px solid #dce3eb}h1{margin:0 0 5px;font-size:30px}h2{margin-top:32px}p{margin:7px 0}a{color:#135bb5;text-decoration:none}a:hover{text-decoration:underline}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:15px}.doc{display:flex;background:#fff;border:1px solid #dce3eb;border-radius:10px;padding:16px;min-height:80px;align-items:center}.imagecard{background:white;border:1px solid #dce3eb;border-radius:12px;overflow:hidden;padding-bottom:16px}.imagecard img{width:100%;height:235px;object-fit:contain;background:#e7edf3}.imagecard p,.imagecard b{display:block;margin:10px 15px;font-size:13px;overflow-wrap:anywhere}.imagecard p{color:#617084}input{width:100%;padding:14px;font:inherit;border:1px solid #c5d0dc;border-radius:10px;margin:18px 0}details{background:white;padding:20px;border-radius:12px;margin-top:25px}li{padding:6px;overflow-wrap:anywhere}small{color:#617084}footer{padding:25px 0;color:#617084}button{padding:10px 18px;border:0;border-radius:8px;background:#203247;color:white;font:inherit;cursor:pointer}[hidden]{display:none!important}</style>
<main><header><h1>وثائق وصور الـBericht</h1><p><b>Mohamed Saida — Bahnsteig 50 Hz — V1.8</b></p><p>الملفات الأصلية الكل في مجلّد <b dir="ltr">Bahnsteig_V1.8_Arbeitsprobe</b>. ابدأ بالملخّص والرسم الحالي، وبعد افتح التقارير والصور اللي تحتاجهم.</p><p>الصور تفتح بالحجم الكامل بالنقر عليها. الصور والنتائج الأقدم تبقى مرجع، وما تتخلطش مع الاختيارات الحالية.</p></header>
<h2>الوثائق الأساسية</h2><div class="grid">'''
page+='<div class="doc"><a href="Bericht_Abbildungen_HD/START.html" target="_blank">الصور الجديدة الواضحة — BricsCAD وRelux بدقّة عالية</a></div>'
page+=''.join('<div class="doc">'+link(p,label)+'</div>'for p,label in primary)
page+='</div><h2>الصور الكل — '+str(len(images))+' صورة</h2><label for="search">بحث باسم الملف أو البرنامج</label><input id="search" placeholder="Relux, SIMARIS, V18, Lageplan …"><div class="grid">'+''.join(cards)+'</div>'
page+='<details><summary>قائمة كاملة بكل الملفات ('+str(len(files))+')</summary><ul dir="ltr">'+''.join(rows)+'</ul></details><footer>الملفات القابلة للتعديل: Relux / DWG / SIMARIS / Excel. المراجع والحدود الهندسية موثّقة داخل الحزمة.</footer></main>'
page+='''<script>document.getElementById('search').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();document.querySelectorAll('[data-search]').forEach(el=>el.hidden=!el.dataset.search.includes(q));});</script></html>'''
out.write_text(page,encoding='utf-8')
repo=Path('C:/Users/mouha/OneDrive/Documents/bahnsteig-50hz-elektroplanung-demo')
target=repo/'07_Projektstaende/Bericht_Material_Start.html';shutil.copy2(out,target)
for p in files:assert (repo/'07_Projektstaende'/base.name/p.relative_to(base)).is_file()
print(json.dumps({'gallery':str(out.resolve()),'images':len(images),'files':len(files),'all_local_and_repo_links_exist':True},ensure_ascii=False))
