import sys
from pathlib import Path
import ezdxf

out = Path(sys.argv[1])

doc = ezdxf.new("R2010", setup=True)
doc.header["$INSUNITS"] = 4

layers = {
    "FRAME": 7,
    "POWER": 3,
    "PROTECTION": 1,
    "LIGHT_A": 5,
    "LIGHT_B": 4,
    "SPD_PE": 6,
    "TEXT": 7,
}

for name, color in layers.items():
    doc.layers.new(name, dxfattribs={"color": color})

m = doc.modelspace()

def line(x1, y1, x2, y2, layer="POWER"):
    m.add_line(
        (x1, y1),
        (x2, y2),
        dxfattribs={"layer": layer}
    )

def rect(x1, y1, x2, y2, layer="FRAME"):
    m.add_lwpolyline(
        [(x1,y1),(x2,y1),(x2,y2),(x1,y2)],
        close=True,
        dxfattribs={"layer":layer}
    )

def text(x, y, value, height=3, layer="TEXT"):
    m.add_text(
        value,
        dxfattribs={
            "insert":(x,y),
            "height":height,
            "layer":layer
        }
    )

def breaker(x, label):
    rect(x-9,194,x+9,208,"PROTECTION")
    line(x-6,197,x+6,205,"PROTECTION")
    text(x-6,199,label,2.4,"TEXT")

def lamp(x, y, name, layer):
    m.add_circle(
        (x,y),4.5,
        dxfattribs={"layer":layer}
    )
    line(x-3,y-3,x+3,y+3,layer)
    line(x-3,y+3,x+3,y-3,layer)
    text(x-7,y-16,name,2.8)

# A3 landscape border
rect(8,10,412,287)
line(8,265,412,265,"FRAME")

# Header
text(17,275,"BAHNSTEIG 50 Hz - ELEKTROPLANUNG",6)
text(17,268,"UV-01 | EINLINIENSCHALTPLAN | V0.3",3)

# Incoming supply
text(18,253,"X0 - NETZBETREIBER / ANNAHME",3)
text(18,245,"3~ 400/230 V | 50 Hz",3.2)

line(28,229,78,229)

# Main switch
rect(78,222,98,236,"PROTECTION")
line(82,225,94,233,"PROTECTION")
text(83,225,"Q0",3)
text(77,212,"Hauptschalter",2.8)

line(98,229,382,229)

text(111,239,"UV-01  |  L1 / L2 / L3 / N / PE",3.2)

# Circuit A
line(145,229,145,208)
breaker(145,"QF1")
line(145,194,145,169)

text(65,187,"STROMKREIS A - LICHT",3.6)
text(65,181,"6 Leuchten | Phase vorlaeufig",2.8)

line(68,169,313,169,"LIGHT_A")

# Circuit B
line(338,229,338,208)
breaker(338,"QF2")
line(338,194,338,103)

text(65,122,"STROMKREIS B - LICHT",3.6)
text(65,116,"6 Leuchten | Phase vorlaeufig",2.8)

line(68,103,338,103,"LIGHT_B")

positions = [90,132,174,216,258,300]

# Six luminaires A
for i,x in enumerate(positions,1):
    line(x,169,x,155,"LIGHT_A")
    lamp(x,150,f"A{i:02d}","LIGHT_A")

# Six luminaires B
for i,x in enumerate(positions,1):
    line(x,103,x,89,"LIGHT_B")
    lamp(x,84,f"B{i:02d}","LIGHT_B")

# SPD conceptual branch
line(382,229,382,216,"SPD_PE")
rect(368,199,401,216,"PROTECTION")
text(372,209,"SPD",4)
text(372,203,"Auslegung offen",2.2)

line(382,199,382,185,"SPD_PE")
line(374,185,390,185,"SPD_PE")
line(377,182,387,182,"SPD_PE")
line(380,179,384,179,"SPD_PE")
text(366,173,"PE / PA",2.8)

# Notes
line(17,59,403,59,"FRAME")
text(17,52,"TECHNISCHE HINWEISE",3.2)
text(17,46,"Einlinienschema: N- und PE-Leiter nicht vollstaendig dargestellt.",2.7)
text(17,40,"Schutzgeraete, Leitungstypen, Querschnitte und Selektivitaet ungeprueft.",2.7)
text(17,34,"SPD-Konzept und Erdung muessen separat dimensioniert werden.",2.7)

# Title block
line(17,28,403,28,"FRAME")
text(17,21,"PROJEKT: Fiktive Bahnsteigmodernisierung",3)
text(17,15,"STATUS: ENTWURF - NICHT ZUR AUSFUEHRUNG",2.8)
text(292,21,"PLAN: E-003",3)
text(292,15,"VERSION: V0.3",3)

doc.saveas(str(out))

check = ezdxf.readfile(str(out))
auditor = check.audit()

if auditor.has_errors:
    raise RuntimeError("DXF validation failed")

print("DXF OK:", out)
print("Entities:", len(check.modelspace()))
print("Validation: OK")