# Bahnsteig 50Hz - independent editable 3D CAD generator
# Python 3.8+ standard library only. No Relux RDF files are modified.
from pathlib import Path
import math, sys, csv

output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd() / "Bahnsteig_50Hz_Real3D_V0.7.dxf"
output.parent.mkdir(parents=True, exist_ok=True)
lines = []
def emit(code, value):
    lines.extend((str(code), str(value)))
def section(name):
    emit(0,"SECTION");emit(2,name)
def endsection():
    emit(0,"ENDSEC")
layers = {
    "PLATFORM":8,"SURFACE":9,"TACTILE":2,"RAILS":7,
    "SLEEPERS":8,"ROOF":5,"CANOPY_SUPPORT":4,
    "CIRCUIT_A":1,"CIRCUIT_B":6,
    "UV01":3,"TEXT":7,
}
section("HEADER")
emit(9,"$ACADVER");emit(1,"AC1009")
emit(9,"$INSUNITS");emit(70,6)
endsection()
section("TABLES")
emit(0,"TABLE");emit(2,"LAYER");emit(70,len(layers))
for name,color in layers.items():
    emit(0,"LAYER");emit(2,name);emit(70,0);emit(62,color);emit(6,"CONTINUOUS")
emit(0,"ENDTAB")
endsection()
section("BLOCKS");endsection()
section("ENTITIES")
def vertex(base, point, i=0):
    emit(base+i,round(point[0],6))
    emit(base+10+i,round(point[1],6))
    emit(base+20+i,round(point[2],6))
def quad(points,layer):
    emit(0,"3DFACE");emit(8,layer)
    for i,p in enumerate(points): vertex(10,p,i)
def box(x1,y1,z1,x2,y2,z2,layer):
    corners=[(x1,y1,z1),(x2,y1,z1),(x2,y2,z1),(x1,y2,z1),
             (x1,y1,z2),(x2,y1,z2),(x2,y2,z2),(x1,y2,z2)]
    for ids in ((0,1,2,3),(4,5,6,7),(0,1,5,4),
                (1,2,6,5),(2,3,7,6),(3,0,4,7)):
        quad([corners[j] for j in ids],layer)
def line(a,b,layer):
    emit(0,"LINE");emit(8,layer);vertex(10,a);vertex(11,b)
def circle(x,y,z,r,layer):
    emit(0,"CIRCLE");emit(8,layer);vertex(10,(x,y,z));emit(40,r)
def text(x,y,z,title,height=0.4):
    emit(0,"TEXT");emit(8,"TEXT");vertex(10,(x,y,z));emit(40,height);emit(1,title)
def pylon(x,y,z1,z2,r,layer):
    for i in range(12):
        a=2*math.pi*i/12
        b=2*math.pi*(i+1)/12
        v1=(x+r*math.cos(a),y+r*math.sin(a))
        v2=(x+r*math.cos(b),y+r*math.sin(b))
        quad([(v1[0],v1[1],z1),(v2[0],v2[1],z1),
              (v2[0],v2[1],z2),(v1[0],v1[1],z2)],layer)

box(0,0,-.4,120,4,0,"PLATFORM")
box(0,.03,0,120,3.97,.08,"SURFACE")
box(0,.25,.08,120,.6,.095,"TACTILE")
for x in range(0,121,2):
    line((x,.6,.085),(x,3.97,.085),"SURFACE")
for y in (1,2,3):
    line((0,y,.086),(120,y,.086),"SURFACE")
for y in (-1.1,-2.54):
    box(0,y-.055,-.24,120,y+.055,-.08,"RAILS")
for x in range(1,120,2):
    box(x-.09,-2.95,-.40,x+.09,-.70,-.25,"SLEEPERS")
for x in (45.5,55,65,74.5):
    for y in (.20,3.80):
        box(x-.16,y-.16,.08,x+.16,y+.16,4.65,"CANOPY_SUPPORT")
    box(x-.25,-.5,4.50,x+.25,4.5,4.70,"CANOPY_SUPPORT")
box(45,-.5,4.75,75,4.5,5.00,"ROOF")
box(44.85,-.62,4.73,75.15,-.45,5.10,"ROOF")
box(44.85,4.45,4.73,75.15,4.62,5.10,"ROOF")
box(1,3.30,.08,2.2,3.90,2.20,"UV01")
records=[]
for i in range(12):
    x=5+i*10
    circuit="A" if i%2==0 else "B"
    tag=f"{circuit}{i//2+1:02d}"
    canopy=45<=x<=75
    layer=f"CIRCUIT_{circuit}"
    if canopy:
        z=4.30
        box(x-.25,1.82,4.30,x+.25,2.18,4.44,layer)
        box(x-.08,1.93,4.44,x+.08,2.07,4.78,"CANOPY_SUPPORT")
        watt=14
    else:
        z=4.50
        pylon(x,2,.08,4.45,.0675,layer)
        box(x-.28,1.79,4.45,x+.28,2.21,4.58,layer)
        watt=18.5
    circle(x,2,z,.26,layer)
    text(x-.65,2.55,5.2,tag,.35)
    records.append((tag,circuit,x,2,z,"Canopy" if canopy else "Open",watt,"PROVISIONAL_NOT_RELUX_CALCULATED"))
text(0,5.75,0,"BAHNSTEIG 50 Hz - REAL 3D CAD MODEL V0.7",.7)
text(0,5.00,0,"120 x 4 m platform / 30 m canopy / 12 reference luminaires",.42)
text(0,-5.5,0,"PRELIMINARY CAD - NO RELUX LUX CALCULATION / NO COMPLIANCE VALIDATION",.40)
text(0,-6.3,0,"Illustrative heights: open 4.50m; canopy 4.30m - NOT ENGINEERED",.32)
endsection()
emit(0,"EOF")
output.write_text("\n".join(lines)+"\n",encoding="ascii")
csvpath=output.with_suffix(".csv")
with csvpath.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f,delimiter=";")
    w.writerow(("Tag","Circuit","X_m","Y_m","Illustrative_Z_m","Zone","Nominal_W","Status"))
    w.writerows(records)
print("CAD_CREATED:",output)
print("CAD_BYTES:",output.stat().st_size)
print("PLACEMENT_CSV:",csvpath)
print("LUMINAIRES: 12 | AREA: 120 x 4 m | CANOPY: 30 m")
print("NOTE: Real 3D CAD objects; NOT a Relux lighting calculation.")
