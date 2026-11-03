import sys
from pathlib import Path
import ezdxf

destination = Path(sys.argv[1])

doc = ezdxf.new("R2010")
doc.header["$INSUNITS"] = 6  # metres

layers = {
    "BAHNSTEIG": 7,
    "UEBERDACHUNG": 8,
    "LEUCHTEN_A": 1,
    "LEUCHTEN_B": 5,
    "VERTEILER": 2,
    "BESCHRIFTUNG": 7,
}

for name, color in layers.items():
    doc.layers.new(name, dxfattribs={"color": color})

m = doc.modelspace()

def rectangle(x1, y1, x2, y2, layer):
    m.add_lwpolyline(
        [(x1,y1),(x2,y1),(x2,y2),(x1,y2)],
        close=True,
        dxfattribs={"layer": layer}
    )

def label(x, y, value, height=0.4):
    m.add_text(
        value,
        dxfattribs={
            "layer": "BESCHRIFTUNG",
            "height": height,
            "insert": (x,y)
        }
    )

# Railway platform: 120 x 4 metres
rectangle(0,0,120,4,"BAHNSTEIG")

# Preliminary canopy: 30 metres
rectangle(45,-0.5,75,4.5,"UEBERDACHUNG")

# Distribution board - conceptual position
rectangle(1,1.5,3,2.5,"VERTEILER")
label(1,5.5,"UV-01")

# 12 proposed luminaire positions
for i in range(12):
    x = 5 + i * 10
    circuit = "LEUCHTEN_A" if i % 2 == 0 else "LEUCHTEN_B"
    number = i // 2 + 1
    prefix = "A" if i % 2 == 0 else "B"

    m.add_circle(
        (x,2),
        radius=0.18,
        dxfattribs={"layer": circuit}
    )

    label(x-0.6,2.6,f"{prefix}{number:02d}",0.3)

label(0,-2,"BAHNSTEIG 120 x 4 m",0.6)
label(45,5.5,"UEBERDACHUNG 30 m")
label(0,-4,"V0.4 - Vorentwurf / keine Lichtberechnung")
label(0,-5,"CAD-Einheit: 1 = 1 m")

doc.saveas(str(destination))

check = ezdxf.readfile(str(destination))
audit = check.audit()

if audit.has_errors:
    raise RuntimeError("DXF audit failed")

print("RELUX DXF CREATED:", destination)
print("DXF AUDIT: OK")
print("UNITS: METRES")
print("LUMINAIRE REFERENCES: 12")