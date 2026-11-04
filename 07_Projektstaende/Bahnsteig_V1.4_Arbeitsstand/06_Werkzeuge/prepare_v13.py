from pathlib import Path
import shutil,json,hashlib
out=Path('outputs/Bahnsteig_V1.3_Final')
src=Path('C:/Users/mouha/Downloads/Bahnsteig_Real3D_V07/Bahnsteig_50Hz_Real3D_V0.7.dxf')
lines=src.read_text().splitlines(); pairs=list(zip(lines[::2],lines[1::2])); ents=[]; e=[]
for c,v in pairs:
    if c.strip()=='0':
        if e: ents.append(e)
        e=[]
    e.append((c.strip(),v.strip()))
if e:ents.append(e)
faces=[]
for e in ents:
    d=dict(e)
    if d.get('0')=='3DFACE' and d.get('8')=='CANOPY_SUPPORT':
        faces.append([tuple(float(d[str(k+i)]) for k in (10,20,30)) for i in range(4)])
assert len(faces)>0
obj=['# Canopy supports from existing V0.7 CAD, metres, global coordinates. No platform or roof.','o Canopy_Supports_V13']
for i,f in enumerate(faces):
    obj.extend('v '+' '.join(map(str,p)) for p in f)
    obj.append('f '+' '.join(str(i*4+j+1) for j in range(4)))
(out/'01_Relux/Canopy_Supports_V13.obj').write_text('\n'.join(obj)+'\n')
shutil.copy2(src,out/'05_Grundlagen/Existing_3D_V07.dxf')
for p in Path('C:/Users/mouha/Downloads/Bahnsteig_V11_Deliverables').glob('*.LDT'):shutil.copy2(p,out/'01_Relux'/p.name)
print('Support faces',len(faces),'bounds',[(min(p[k] for f in faces for p in f),max(p[k] for f in faces for p in f)) for k in range(3)])
