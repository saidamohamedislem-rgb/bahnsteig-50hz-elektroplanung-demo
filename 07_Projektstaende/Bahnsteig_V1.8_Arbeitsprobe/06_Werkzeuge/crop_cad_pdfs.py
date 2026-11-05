from pathlib import Path
from pypdf import PdfReader,PdfWriter
from pypdf.generic import RectangleObject
import pypdfium2 as pdfium
from PIL import Image,ImageChops
for name in ['Bahnsteig_V13_Lageplan','Bahnsteig_V13_Stromlaufplan']:
 p=Path('outputs/Bahnsteig_V1.3_Final/02_CAD')/(name+'.pdf')
 raw=p.read_bytes();Path('work/'+name+'_native_fullpage.pdf').write_bytes(raw)
 doc=pdfium.PdfDocument(raw);im=doc[0].render(scale=2).to_pil().convert('RGB');bbox=ImageChops.difference(im,Image.new('RGB',im.size,'white')).getbbox()
 r=PdfReader(p);pg=r.pages[0];height=float(pg.mediabox.height);b=[max(0,bbox[0]/2-8),max(0,height-bbox[3]/2-8),min(float(pg.mediabox.width),bbox[2]/2+8),min(height,height-bbox[1]/2+8)]
 pg.mediabox=RectangleObject(b);pg.cropbox=RectangleObject(b);w=PdfWriter();w.add_page(pg)
 with p.open('wb') as f:w.write(f)
 d=pdfium.PdfDocument(p);image=d[0].render(scale=2).to_pil();image.save('work/'+name+'_review.png')
 print(name,'PDF cropped to native drawing border',b)
