"""Render the original field-report poster using existing Pillow/system fonts.

Run: python3 docs/assets/works/wan-animate2-apple-silicon-lab/poster.py
Source palette/design: public site at commit
99aa65d459ab43c8b21d0f9eafabf5e237212e7f (site/index.html, site/assets/css/site.css).
Execution diagram is schematic, not measured telemetry. No private media inputs.
"""

from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont, ImageFilter


SCALE = 2
WIDTH, HEIGHT = 1280, 720
BG = "#080f13"
WHITE = "#edfff4"
MUTED = "#afc2bf"
GREEN = "#79ffba"
CYAN = "#69dfeb"
LINE = "#2b4249"
FONT_DIR = Path("/System/Library/Fonts")
image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), BG)
draw = ImageDraw.Draw(image)


def font(size, family="display", bold=True):
    filename = {"display": "Avenir Next Condensed.ttc", "body": "Avenir Next.ttc", "mono": "Menlo.ttc"}[family]
    index = (1 if bold else 0) if family == "mono" else (0 if bold else 7)
    return ImageFont.truetype(str(FONT_DIR / filename), round(size * SCALE), index=index)


def text(x, y, value, size, color=WHITE, family="mono", bold=False):
    draw.text((round(x * SCALE), round(y * SCALE)), value,
              font=font(size, family, bold), fill=color, anchor="lt")


def line(points, color=LINE, width=1):
    draw.line([(round(x * SCALE), round(y * SCALE)) for x, y in points],
              fill=color, width=round(width * SCALE))


def box(bounds, outline=LINE, fill=None, width=1):
    draw.rectangle(tuple(round(v * SCALE) for v in bounds), outline=outline,
                   fill=fill, width=round(width * SCALE))


# Restrained diffuse glow; fine grid belongs to the abstract execution panel.
glow = Image.new("RGB", image.size, "#000000")
gd = ImageDraw.Draw(glow)
gd.ellipse((790 * SCALE, 110 * SCALE, 1200 * SCALE, 480 * SCALE), fill="#08252a")
glow = glow.filter(ImageFilter.GaussianBlur(80 * SCALE))
from PIL import ImageChops
image = ImageChops.add(image, glow)
draw = ImageDraw.Draw(image)

# Reserve the upper-left area for the HTML kind badge at narrow card widths.
box((538, 58, 546, 66), GREEN, GREEN)
text(560, 56, "LOCAL AI / FIELD REPORT", 15, GREEN, bold=True)
text(951, 56, "GREENWAKAME LAB", 14, MUTED)
line([(56, 88), (1224, 88)])

# At a 267px card width, title y=212 clears the 40px-high badge region.
# Keep WAN oversized; compact the supporting lines without changing content.
text(51, 212, "WAN", 164, WHITE, "display", True)
text(51, 376, "ANIMATE 2", 110, GREEN, "display", True)
text(58, 490, "ON APPLE SILICON", 24, CYAN, "mono", True)
text(58, 521, "APPLE M5 / 32GB", 12, WHITE, bold=True)
text(300, 521, "COMFYUI / MPS", 12, MUTED)

# Abstract execution record: topology only; no invented time series or scores.
box((828, 114, 1224, 510), LINE, "#0b141b")
text(850, 135, "EXECUTION RECORD", 13, MUTED)
box((1193, 136, 1201, 144), GREEN, GREEN)
line([(850, 164), (1202, 164)])
for x in range(873, 1187, 26):
    line([(x, 180), (x, 372)], "#142930")
for y in range(190, 373, 26):
    line([(850, y), (1202, y)], "#142930")

# Stacked processing planes, with reference coordinates and a central cross.
for offset, color in [(-22, "#24464c"), (-11, "#3c6b6d"), (0, CYAN)]:
    points = [(940 + offset, 215 + offset), (1110 + offset, 215 + offset),
              (1110 + offset, 357 + offset), (940 + offset, 357 + offset),
              (940 + offset, 215 + offset)]
    line(points, color)
cx, cy = 1025, 286
draw.ellipse(((cx-42)*SCALE, (cy-42)*SCALE, (cx+42)*SCALE, (cy+42)*SCALE),
             outline=GREEN, width=SCALE)
line([(cx-58, cy), (cx+58, cy)], "#4b8d87")
line([(cx, cy-58), (cx, cy+58)], "#4b8d87")
box((cx-3, cy-3, cx+3, cy+3), GREEN, GREEN)
text(952, 228, "MPS", 12, CYAN, bold=True)
text(856, 382, "512 × 512 / 17F / 8 FPS", 15, WHITE)
line([(850, 418), (1202, 418)])
stages = [(864, "LOAD"), (954, "SAMPLE"), (1044, "DECODE"), (1134, "SAVE")]
for index, (x, label) in enumerate(stages):
    draw.ellipse(((x-4)*SCALE, 435*SCALE, (x+4)*SCALE, 443*SCALE), fill=GREEN)
    if index < 3:
        line([(x+8, 439), (x+80, 439)], "#417865")
    text(x-12, 455, label, 11, MUTED)
text(850, 487, "COMPLETED PATH / SCHEMATIC", 11, GREEN)

# The primary conclusion is visually separate from technical completion.
line([(56, 542), (1224, 542)], "#417865")
text(58, 560, "THE CENTRAL FINDING", 12, MUTED)
text(54, 586, "TECHNICAL PASS", 46, GREEN, "body", True)
text(489, 578, "≠", 60, CYAN, "body", True)
text(560, 586, "VISUAL SUCCESS", 46, WHITE, "body", True)
line([(56, 653), (1224, 653)])
text(58, 674, "TWO OBSERVED RUNS. IDENTITY NOT SOLVED.", 13, MUTED)
text(999, 674, "V4 / UNRUN", 14, CYAN, bold=True)

output = Path(__file__).with_name("poster.webp")
image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
image.save(output, "WEBP", quality=92, method=6)
print(f"{output}: {WIDTH} × {HEIGHT}, {output.stat().st_size} bytes")
