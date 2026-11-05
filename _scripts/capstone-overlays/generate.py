#!/usr/bin/env python3
"""Generate the SVG layers drawn on top of the C++ capstone page's screenshots.

Every screenshot gets an info box (top-right, white text on a black box): the
transfer function and PID gains used in that run, or for the IK runs the
robot's dimensions and target(s). Highlights 2-4 and the
robot joint also get a full-resolution response line, drawn
from the simulation CSVs in ./data (exported by the capstone program itself,
one sample every 10 ms), plus a "line added for visibility" note.

Output: _includes/capstone-overlays/overlay-N.svg, inlined by the project
page on top of each screenshot, plus the homepage tile image
assets/img/projects/cpp-robotics-capstone/thumbnail.png (Highlight 4 with
the line baked in). The SVG viewBox is the screenshot's own pixel
grid, so everything scales with the image at any display width.

Plot geometry (measured from the screenshots' `*` glyphs, see --check):
  column c  ->  x = 187.5 + 10 * c          (c = 0..49, 50 columns)
  row k     ->  y = Y0 + 22 * k             (k = 0..25, 26 rows)
  value v   ->  column (v - lo) / (hi - lo) * 49   (unrounded here; the
                ASCII plot rounds it to the nearest column)

So the white line doesn't hide the white `*` marks (Miguel's call):
  - the line is shifted a few px (OFFSET, or a per-plot offset), and
  - wherever a `*` is still within CLEAR px of the shifted line, a small gap
    is cut out of the line around it (an SVG mask), so every `*` stays
    visible.

Usage (from the repo root):
  python3 _scripts/capstone-overlays/generate.py           # write SVGs
  python3 _scripts/capstone-overlays/generate.py --check   # also verify against
      the screenshot pixels that the data curve (before the offset) passes
      within half a column of every `*`, that the gap positions match the
      real `*` marks, and that no box covers any terminal text
      (needs numpy + Pillow)

This folder starts with an underscore, so Jekyll ignores it and it is never
published to the site.
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(REPO, "_includes", "capstone-overlays")
IMG_DIR = os.path.join(REPO, "assets", "img", "projects", "cpp-robotics-capstone")
LATO_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

X0, DX = 187.5, 10.0      # x of column 0, px per column
DY = 22.0                 # px per row
NCOLS, NROWS = 50, 26
OFFSET = (0.0, 8.0)       # default shift of the response line, in screenshot px
CLEAR = 7.0               # gap radius around any `*` still this close

# Boxes: white Lato Bold text on black, same look for the note and info box.
FONT = 28                 # font size, in screenshot px
SUB = 20                  # subscript size (the p in Kp, the 1 in L1, ...)
PAD = (12, 7)             # box padding (x, y)
LINE_GAP = 36             # baseline-to-baseline distance in the info box
INFO_TOP = 62             # info box top edge: just under the window title bar
INFO_RIGHT_MARGIN = 12    # info box right edge = image width - this
NOTE = "line added for visibility"
IK_ROBOT = "h = 0.5, L_1 = 1, L_2 = 0.8"   # the robot used in all three IK shots

# One entry per screenshot shown on the page. info: the info box's lines
# (`_x` makes x a subscript, as in K_p). For the PID runs: the plant's
# transfer function with that run's parameters substituted, then the gains;
# for the IK runs: the robot's dimensions, then the target(s).
# overlay: only some plots (Miguel's picks). lo/hi/t-range come from the
# brief (they are the program's own plot axes); y0 is the measured y-pixel
# centre of the `*` glyphs in the t = 0 row; x0 overrides X0 where a
# screenshot's column 0 sits elsewhere; note_xy overrides the note box's
# default spot (top-left corner, in screenshot px); offset overrides OFFSET.
# Per-plot offsets were picked to need the fewest gaps: shifting down only
# separates the line from the `*` marks where the curve runs sideways, so
# the slowly settling plots (2, 7) are shifted sideways instead.
FIGURES = [
    dict(n=1, name="1_second_order_no_pid", size=(929, 1054),
         info=["G(s) = 16 / (s² + 2.4s + 16)", "K_p = 1, K_i = 0, K_d = 0"]),
    dict(n=2, name="2_second_order_full_pid", size=(929, 1054),
         info=["G(s) = 16 / (s² + 2.4s + 16)", "K_p = 3, K_i = 4, K_d = 0.4"],
         overlay=dict(lo=0.0, hi=1.045, t0=0.0, t1=5.0, y0=235.5, offset=(-7.0, 5.0),
                      label="one small overshoot and a shallow dip, then a smooth climb onto 1.0")),
    dict(n=3, name="3_undamped_sine", size=(929, 1054),
         info=["G(s) = 16 / (s² + 16)", "K_p = 1, K_i = 0, K_d = 0"],
         overlay=dict(lo=0.0, hi=1.0, t0=0.0, t1=5.0, y0=240.5,
                      label="constant-amplitude sine between 0 and 1, period 1.11 s")),
    dict(n=4, name="4_integral_instability", size=(929, 1054),
         info=["G(s) = 16 / (s² + 2.4s + 16)", "K_p = 1, K_i = 8, K_d = 0"],
         overlay=dict(lo=-6.268, hi=9.997, t0=0.0, t1=4.700, y0=365.5, diverge=4.715,
                      label="growing oscillation, diverges at 4.715 s")),
    dict(n=6, name="6_first_order_pi", size=(929, 1054),
         info=["G(s) = 2 / (0.5s + 1)", "K_p = 1, K_i = 4, K_d = 0"]),
    # Screenshot 7 comes from a narrower terminal window: column 0 is 1 px
    # further right, and the info box takes the strip above its axis header,
    # so its note goes just under the plot instead.
    dict(n=7, name="7_robot_joint_pd", size=(789, 1013),
         info=["G(s) = 1 / (0.1s² + 0.1s + 1)", "K_p = 3, K_i = 0, K_d = 0.15"],
         overlay=dict(lo=0.0, hi=1.148, t0=0.0, t1=5.0, y0=194.5, x0=188.5,
                      offset=(9.0, 0.0), note_xy=(466, 781),
                      label="lightly damped oscillation settling at 0.75")),
    # IK calculator runs (no title bar: cropped off, it held a capture-script
    # label). No overlay line: the IK output is exact numbers, not a sampled
    # plot. info_top / info_right override INFO_TOP / INFO_RIGHT_MARGIN; the
    # right margin clears the window's scrollbar.
    dict(n=8, name="8_ik_normal", size=(934, 992), info_top=12, info_right=24,
         info=[IK_ROBOT, "target (1, 0.5, 1)"]),
    dict(n=9, name="9_ik_unreachable", size=(934, 992), info_top=12, info_right=24,
         info=[IK_ROBOT, "target 1: (2, 0, 0.5)", "target 2: (0.1, 0, 0.55)",
               "target 3: (1, 0.5, 1)"]),
    dict(n=10, name="10_ik_singularity", size=(934, 992), info_top=12, info_right=24,
         info=[IK_ROBOT, "target (0, 0, 1.6)"]),
]


# ---------- text measuring (so boxes fit their text) ----------

_fonts = {}


def text_width(s, size):
    """Rendered width in Lato Bold (the site's font). Measured with Pillow from
    the system's Lato when available; otherwise estimated at 0.53 em/char."""
    try:
        from PIL import ImageFont
        if size not in _fonts:
            _fonts[size] = ImageFont.truetype(LATO_BOLD, size)
        return _fonts[size].getlength(s)
    except Exception:
        return 0.53 * size * len(s)


def segments(line):
    """'K_p = 1, L_2 = 0.8' as (text, is_subscript) pieces: `_x` makes the
    single character x a subscript."""
    out, buf, i = [], "", 0
    while i < len(line):
        if line[i] == "_" and i + 1 < len(line):
            if buf:
                out.append((buf, False))
                buf = ""
            out.append((line[i + 1], True))
            i += 2
        else:
            buf += line[i]
            i += 1
    if buf:
        out.append((buf, False))
    return out


def plain(line):
    """The line as plain text (for the SVG's aria-label)."""
    return "".join(t for t, _ in segments(line))


def segments_width(segs):
    return sum(text_width(t, SUB if sub else FONT) for t, sub in segs)


def segments_svg(segs):
    """Subscripts drop 6 px; the next normal segment moves back up. (The
    shift has to ride on a segment with characters: browsers ignore dy on an
    empty <tspan>.)"""
    out, level = [], 0
    for t, sub in segs:
        target = 6 if sub else 0
        dy = f' dy="{target - level}"' if target != level else ""
        cls = ' class="ov-sub"' if sub else ""
        out.append(f"<tspan{cls}{dy}>{t}</tspan>")
        level = target
    return "".join(out)


# ---------- geometry ----------

def fx(o, v):
    return o.get("x0", X0) + (v - o["lo"]) / (o["hi"] - o["lo"]) * (NCOLS - 1) * DX


def fy(o, t):
    return o["y0"] + (t - o["t0"]) / (o["t1"] - o["t0"]) * (NROWS - 1) * DY


def read_csv(name):
    with open(os.path.join(HERE, "data", name + ".csv")) as f:
        rows = list(csv.reader(f))[1:]
    return [[float(v) for v in r] for r in rows]


def interp(data, t, col=1):
    for a, b in zip(data, data[1:]):
        if a[0] <= t <= b[0]:
            f = (t - a[0]) / (b[0] - a[0]) if b[0] > a[0] else 0
            return a[col] + f * (b[col] - a[col])
    return data[-1][col]


def star_positions(o, data):
    """Where the program drew each `*`: same rounding rule as the ASCII plot."""
    out = []
    for k in range(NROWS):
        t = o["t0"] + k * (o["t1"] - o["t0"]) / (NROWS - 1)
        col = round((interp(data, t) - o["lo"]) / (o["hi"] - o["lo"]) * (NCOLS - 1))
        out.append((o.get("x0", X0) + col * DX, o["y0"] + k * DY))
    return out


def seg_dist(px, py, ax, ay, bx, by):
    vx, vy = bx - ax, by - ay
    L2 = vx * vx + vy * vy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((px - ax) * vx + (py - ay) * vy) / L2))
    return math.hypot(px - (ax + t * vx), py - (ay + t * vy))


def info_box(fig):
    """(x, y, w, h) of the info box, top-right."""
    W, _ = fig["size"]
    w = max(segments_width(segments(line)) for line in fig["info"]) + 2 * PAD[0]
    h = FONT + (len(fig["info"]) - 1) * LINE_GAP + 2 * PAD[1] + 2
    x = W - fig.get("info_right", INFO_RIGHT_MARGIN) - w
    return (x, fig.get("info_top", INFO_TOP), w, h)


def note_box(o, W):
    """(x, y, w, h) of the note box: by default right-aligned just above the
    axis header, a strip that is empty in the 929 px screenshots."""
    w = text_width(NOTE, FONT) + 2 * PAD[0]
    h = FONT + 2 * PAD[1]
    if "note_xy" in o:
        return (*o["note_xy"], w, h)
    bottom = o["y0"] - 30
    return (W - 14 - w, bottom - h, w, h)


def line_geometry(fig):
    """The response line's points (shifted) and the `*` positions that need a
    gap cut around them. Shared by the SVG overlay and the homepage thumbnail."""
    o = fig["overlay"]
    data = read_csv(fig["name"])
    ox, oy = o.get("offset", OFFSET)
    pts = [(fx(o, r[1]) + ox, fy(o, r[0]) + oy) for r in data]
    gaps = [(sx, sy) for sx, sy in star_positions(o, data)
            if min(seg_dist(sx, sy, *a, *b) for a, b in zip(pts, pts[1:])) < CLEAR]
    return pts, gaps


# ---------- SVG ----------

def build_svg(fig):
    W, H = fig["size"]
    aria = "Added for this page: " + "; ".join(plain(line) for line in fig["info"])
    o = fig.get("overlay")
    if o:
        aria += f". Overlay: full resolution response, {o['label']}"
    parts = [f'<svg class="term-overlay" viewBox="0 0 {W} {H}" role="img" '
             f'aria-label="{aria}" preserveAspectRatio="xMidYMid meet">']
    ngaps = 0

    if o:
        pts, gaps = line_geometry(fig)
        oy = o.get("offset", OFFSET)[1]
        ngaps = len(gaps)
        mid = f"ov-gaps-{fig['n']}"
        # .ov-data is what the page's "Hide overlay" button hides.
        parts += [
            '<g class="ov-data">',
            f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">'
            f'<rect width="{W}" height="{H}" fill="#fff"/>'
            + "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{CLEAR}" fill="#000"/>' for x, y in gaps)
            + "</mask></defs>",
            f'<g mask="url(#{mid})">',
            '<polyline class="ov-line" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '"/>',
        ]
        if "diverge" in o:
            y = fy(o, o["diverge"]) + oy
            x0 = o.get("x0", X0)
            parts.append(f'<line class="ov-diverge" x1="{x0 - 10}" y1="{y:.1f}" '
                         f'x2="{x0 + (NCOLS - 1) * DX + 10}" y2="{y:.1f}"/>')
        parts.append("</g>")
        x, y, w, h = note_box(o, W)
        parts.append(f'<rect class="ov-box" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="4"/>')
        parts.append(f'<text class="ov-text" x="{x + PAD[0]:.1f}" y="{y + h / 2 + 0.36 * FONT:.1f}">{NOTE}</text>')
        parts.append("</g>")

    x, y, w, h = info_box(fig)
    base1 = y + PAD[1] + 0.86 * FONT
    parts += ['<g class="ov-info">',
              f'<rect class="ov-box" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h:.0f}" rx="4"/>']
    for i, line in enumerate(fig["info"]):
        parts.append(f'<text class="ov-text" x="{x + PAD[0]:.1f}" y="{base1 + i * LINE_GAP:.1f}">'
                     + segments_svg(segments(line)) + "</text>")
    parts += ["</g>", "</svg>"]
    return "\n".join(parts) + "\n", ngaps


# ---------- homepage thumbnail ----------

# The homepage tile shows its image as a CSS background, so an SVG can't sit
# on top of it; instead this bakes the response line into a PNG. Highlight 4,
# cropped (left, top, right, bottom) to just the plot rows (Miguel's call: no
# axis header above, no program text below), minus the window's border
# (x 0-1) and scrollbar (right edge). The plot is too tall for a 5:3 crop at
# the screenshot's width, so the sides are padded out to the tile's 5:3 shape
# with the terminal's own (flat) background color.
THUMB = dict(n=4, crop=(2, 354, 900, 930), aspect=5 / 3, bg=(48, 10, 36),
             out="thumbnail.png")
LINE_RGBA = (244, 244, 244, 153)   # matches .ov-line: #f4f4f4 at 0.6 opacity
LINE_W = 4                         # matches .ov-line stroke-width
SS = 4                             # supersampling factor, for smooth edges


def build_thumbnail():
    from PIL import Image, ImageDraw
    fig = next(f for f in FIGURES if f["n"] == THUMB["n"])
    cx0, cy0, cx1, cy1 = THUMB["crop"]
    base = Image.open(os.path.join(IMG_DIR, fig["name"] + ".png")).convert("RGBA")
    base = base.crop(THUMB["crop"])

    # Draw the line SS times larger on a transparent layer, punch the gaps out
    # (drawing transparent pixels replaces rather than blends), then shrink it
    # back down so the edges come out antialiased.
    pts, gaps = line_geometry(fig)
    layer = Image.new("RGBA", ((cx1 - cx0) * SS, (cy1 - cy0) * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.line([((x - cx0) * SS, (y - cy0) * SS) for x, y in pts],
           fill=LINE_RGBA, width=LINE_W * SS, joint="curve")
    r = CLEAR * SS
    for x, y in gaps:
        X, Y = (x - cx0) * SS, (y - cy0) * SS
        d.ellipse((X - r, Y - r, X + r, Y + r), fill=(0, 0, 0, 0))
    layer = layer.resize(base.size, Image.LANCZOS)

    img = Image.alpha_composite(base, layer).convert("RGB")
    w, h = img.size
    W = max(w, round(h * THUMB["aspect"]))
    canvas = Image.new("RGB", (W, h), THUMB["bg"])
    canvas.paste(img, ((W - w) // 2, 0))
    out = os.path.join(IMG_DIR, THUMB["out"])
    canvas.save(out, optimize=True)
    return out


# ---------- verification against the screenshot pixels (--check) ----------

def asterisks(white):
    """(y_centre, x_centre) of every 4-px-tall `*` glyph in the plot area."""
    import numpy as np
    sub = white[:, 178:700]
    rows = np.where(sub.sum(1) > 0)[0]
    groups, start, prev = [], rows[0], rows[0]
    for r in rows[1:]:
        if r != prev + 1:
            groups.append((start, prev))
            start = r
        prev = r
    groups.append((start, prev))
    out = []
    for g0, g1 in groups:
        if g1 - g0 != 3:          # `*` is exactly 4 px tall; text lines are taller
            continue
        ys, xs = np.nonzero(sub[g0:g1 + 1])
        out.append(((g0 + g1) / 2, xs.mean() + 178))
    return out


def check(fig):
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(os.path.join(IMG_DIR, fig["name"] + ".png")).convert("RGB")).astype(int)
    ok = True

    # Boxes must sit on plain terminal background (no text under them).
    terminal_bg = np.abs(a - np.array([48, 10, 36])).max(2) <= 25
    boxes = [("info box", info_box(fig))]
    if fig.get("overlay"):
        boxes.append(("note box", note_box(fig["overlay"], fig["size"][0])))
    for label, (x, y, w, h) in boxes:
        m = 4
        region = terminal_bg[int(y) - m:int(y + h) + m, int(x) - m:int(x + w) + m]
        covered = int((~region).sum())
        if covered:
            ok = False
        print(f"  {fig['name']}: {label} covers {covered} non-background px "
              f"-> {'OK' if not covered else 'FAIL'}")

    o = fig.get("overlay")
    if o:
        data = read_csv(fig["name"])
        white = (a[:, :, 0] > 180) & (a[:, :, 1] > 180) & (a[:, :, 2] > 180)
        stars = [s for s in asterisks(white) if o["y0"] - 1 <= s[0] <= o["y0"] + 25 * DY + 1]
        computed = star_positions(o, data)
        worst_curve = worst_pos = 0.0
        for k in range(NROWS):
            t = o["t0"] + k * (o["t1"] - o["t0"]) / (NROWS - 1)
            hit = [s for s in stars if abs(s[0] - (o["y0"] + k * DY)) < 2]
            if len(hit) != 1:
                print(f"  row {k}: expected one `*`, found {len(hit)}")
                worst_curve = 99.0
                continue
            sy, sx = hit[0]
            worst_curve = max(worst_curve, abs(sx - fx(o, interp(data, t))))
            worst_pos = max(worst_pos, math.hypot(sx - computed[k][0], sy - computed[k][1]))
        good = worst_curve <= DX / 2 + 0.01 and worst_pos <= 1.0
        ok = ok and good
        print(f"  {fig['name']}: data curve within {worst_curve:.2f} px of every `*` "
              f"(limit {DX / 2:.1f}); computed `*` positions off by <= {worst_pos:.2f} px "
              f"-> {'OK' if good else 'FAIL'}")
    return ok


def main():
    do_check = "--check" in sys.argv
    os.makedirs(OUT_DIR, exist_ok=True)
    ok = True
    for fig in FIGURES:
        svg, ngaps = build_svg(fig)
        out = os.path.join(OUT_DIR, f"overlay-{fig['n']}.svg")
        with open(out, "w") as f:
            f.write(svg)
        extra = f", {ngaps} of {NROWS} `*` needed a gap" if fig.get("overlay") else ""
        print(f"wrote {os.path.relpath(out, REPO)}{extra}")
        if do_check:
            ok = check(fig) and ok
    try:
        out = build_thumbnail()
        print(f"wrote {os.path.relpath(out, REPO)}  (homepage tile)")
    except ImportError:
        print("skipped the homepage thumbnail: needs Pillow")
    if do_check and not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
