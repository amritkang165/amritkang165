"""
flower_garden.py  —  amritkang165
Fetches 52 weeks of GitHub contributions and renders them as an actual
SVG flower garden: dark sky, glowing soil, real SVG flowers per cell.

Flower type by commit count:
  0        →  bare soil dot
  1–2      →  tiny sprout  (2-petal bud)
  3–5      →  daisy        (6 petals)
  6–9      →  blossom      (5 petals, wider)
  10+      →  lotus        (layered petals, glow)
"""

import os, math, datetime, requests, random

USER  = os.environ.get("GH_USER", "amritkang165")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        weeks{
          contributionDays{
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

def fetch():
    headers = {"Authorization": f"bearer {TOKEN}"}
    r = requests.post(
        "https://api.github.com/graphql",
        json={"query": QUERY, "variables": {"login": USER}},
        headers=headers, timeout=20,
    )
    r.raise_for_status()
    weeks = r.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    grid = []
    for week in weeks:
        col = []
        for d in week["contributionDays"]:
            col.append((d["date"], d["contributionCount"]))
        while len(col) < 7:
            col.insert(0, ("", -1))
        grid.append(col)
    return grid

# ── SVG flower primitives ─────────────────────────────────────────────────────

def sprout(x, y, color, seed):
    r = random.Random(seed)
    angle = r.uniform(-15, 15)
    return f"""
  <g transform="translate({x},{y}) rotate({angle})">
    <line x1="0" y1="2" x2="0" y2="-7" stroke="#2fc4a5" stroke-width="1.4" stroke-linecap="round"/>
    <ellipse cx="-2.5" cy="-5" rx="2.8" ry="4.5" fill="{color}" opacity="0.9" transform="rotate(-25,-2.5,-5)"/>
    <ellipse cx="2.5" cy="-5" rx="2.8" ry="4.5" fill="{color}" opacity="0.9" transform="rotate(25,2.5,-5)"/>
  </g>"""

def daisy(x, y, color, seed):
    r = random.Random(seed)
    angle = r.uniform(0, 60)
    petals = ""
    n = 6
    for i in range(n):
        a = math.radians(angle + i * 360 / n)
        px, py = math.cos(a) * 5.5, math.sin(a) * 5.5
        petals += f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="2.2" ry="4.8" fill="{color}" opacity="0.88" transform="rotate({angle + i*60:.1f},{px:.2f},{py:.2f})"/>'
    return f"""
  <g transform="translate({x},{y})">
    <line x1="0" y1="6" x2="0" y2="-2" stroke="#2fc4a5" stroke-width="1.2" stroke-linecap="round"/>
    {petals}
    <circle r="2.4" fill="#fff3b0"/>
  </g>"""

def blossom(x, y, color, seed):
    r = random.Random(seed)
    angle = r.uniform(0, 72)
    petals = ""
    n = 5
    for i in range(n):
        a = math.radians(angle + i * 360 / n)
        px, py = math.cos(a) * 6, math.sin(a) * 6
        petals += f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="3.5" ry="5.5" fill="{color}" opacity="0.85" transform="rotate({angle + i*72:.1f},{px:.2f},{py:.2f})"/>'
    dur = r.uniform(3, 6)
    begin = r.uniform(-6, 0)
    return f"""
  <g transform="translate({x},{y})">
    <line x1="0" y1="7" x2="0" y2="-1" stroke="#2fc4a5" stroke-width="1.4" stroke-linecap="round"/>
    {petals}
    <circle r="3" fill="#fff3b0"/>
    <circle r="3" fill="{color}" opacity="0.25">
      <animate attributeName="r" values="3;5;3" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.25;0;0.25" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>
    </circle>
  </g>"""

def lotus(x, y, color, seed):
    r = random.Random(seed)
    # outer ring
    outer = ""
    for i in range(5):
        a = math.radians(i * 72 - 90)
        px, py = math.cos(a) * 6.5, math.sin(a) * 6.5
        outer += f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="4" ry="7" fill="{color}" opacity="0.7" transform="rotate({i*72-90:.1f},{px:.2f},{py:.2f})"/>'
    # inner ring
    inner = ""
    for i in range(5):
        a = math.radians(i * 72 - 54)
        px, py = math.cos(a) * 3.5, math.sin(a) * 3.5
        inner += f'<ellipse cx="{px:.2f}" cy="{py:.2f}" rx="2.5" ry="4.5" fill="{color}" opacity="0.9" transform="rotate({i*72-54:.1f},{px:.2f},{py:.2f})"/>'
    dur  = r.uniform(2.5, 5)
    begin = r.uniform(-5, 0)
    glow_r = r.uniform(8, 11)
    return f"""
  <g transform="translate({x},{y})">
    <circle r="{glow_r:.1f}" fill="{color}" opacity="0.08">
      <animate attributeName="opacity" values="0.08;0.18;0.08" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>
    </circle>
    <line x1="0" y1="8" x2="0" y2="0" stroke="#2fc4a5" stroke-width="1.5" stroke-linecap="round"/>
    {outer}
    {inner}
    <circle r="2.8" fill="#fff3b0"/>
    <circle r="1.4" fill="#fffde7"/>
  </g>"""

def soil_dot(x, y, seed):
    r = random.Random(seed)
    opacity = r.uniform(0.12, 0.22)
    return f'<circle cx="{x}" cy="{y}" r="0.8" fill="#2fc4a5" opacity="{opacity:.2f}"/>'

# ── palette ───────────────────────────────────────────────────────────────────

PALETTES = [
    ["#ff7ac6", "#b28dff", "#6be3ff", "#ff9bd8", "#c9a7ff"],  # pink/purple/cyan
    ["#8ff0d8", "#ff7ac6", "#ffd6e0", "#b28dff", "#6be3ff"],  # mint/pink
    ["#c9a7ff", "#ff9bd8", "#8ff0d8", "#ffeaa7", "#6be3ff"],  # lavender/peach
]

def pick_color(count, seed):
    r = random.Random(seed)
    pal = PALETTES[seed % len(PALETTES)]
    if count <= 2:   return pal[0]
    if count <= 5:   return pal[1 + (seed % 2)]
    if count <= 9:   return pal[2 + (seed % 2)]
    return pal[r.randint(0, len(pal)-1)]

# ── main renderer ─────────────────────────────────────────────────────────────

def render(grid):
    CELL   = 22
    GAP    = 4
    STEP   = CELL + GAP
    COLS   = len(grid)
    ROWS   = 7
    PAD_L  = 36
    PAD_T  = 32
    PAD_R  = 20
    PAD_B  = 40

    W = PAD_L + COLS * STEP + PAD_R
    H = PAD_T + ROWS * STEP + PAD_B

    today = datetime.date.today()
    start = today - datetime.timedelta(weeks=COLS - 1)
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')

    # ── defs ──────────────────────────────────────────────────────────────────
    parts.append("""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#070417"/>
    <stop offset="60%" stop-color="#1b1046"/>
    <stop offset="100%" stop-color="#2a1155"/>
  </linearGradient>
  <radialGradient id="glow_pink" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff7ac6" stop-opacity="0.35"/>
    <stop offset="100%" stop-color="#ff7ac6" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glow_purple" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#b28dff" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#b28dff" stop-opacity="0"/>
  </radialGradient>
  <filter id="blur4"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
</defs>""")

    # ── background ────────────────────────────────────────────────────────────
    parts.append(f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>')

    # subtle nebula blobs
    parts.append(f'<ellipse cx="{W*0.25:.0f}" cy="{H*0.3:.0f}" rx="{W*0.2:.0f}" ry="{H*0.2:.0f}" fill="url(#glow_purple)" filter="url(#blur4)"/>')
    parts.append(f'<ellipse cx="{W*0.75:.0f}" cy="{H*0.6:.0f}" rx="{W*0.18:.0f}" ry="{H*0.18:.0f}" fill="url(#glow_pink)" filter="url(#blur4)"/>')

    # stars
    rng = random.Random(42)
    for _ in range(60):
        sx = rng.uniform(0, W)
        sy = rng.uniform(0, PAD_T + ROWS * STEP * 0.4)
        sr = rng.uniform(0.4, 1.2)
        dur = rng.uniform(2, 6)
        begin = rng.uniform(-6, 0)
        parts.append(
            f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" fill="#fff">'
            f'<animate attributeName="opacity" values="0.1;0.9;0.1" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>'
            f'</circle>'
        )

    # soil strip at bottom of each row
    for ri in range(ROWS):
        sy = PAD_T + ri * STEP + CELL - 2
        parts.append(
            f'<rect x="{PAD_L - 4}" y="{sy}" width="{COLS * STEP + 4}" height="4" '
            f'rx="2" fill="#0d0830" opacity="0.6"/>'
        )

    # ── month labels ──────────────────────────────────────────────────────────
    seen = set()
    for ci in range(COLS):
        col_date = start + datetime.timedelta(weeks=ci)
        m = col_date.month
        if m not in seen:
            seen.add(m)
            lx = PAD_L + ci * STEP
            parts.append(
                f'<text x="{lx}" y="{PAD_T - 10}" '
                f'font-family="\'SF Mono\',\'Fira Code\',monospace" font-size="9" '
                f'fill="#4a3a7a" letter-spacing="0.5">{month_names[m-1]}</text>'
            )

    # ── day labels ────────────────────────────────────────────────────────────
    day_labels = ["Sun","","Tue","","Thu","","Sat"]
    for ri, label in enumerate(day_labels):
        if label:
            ly = PAD_T + ri * STEP + CELL // 2 + 4
            parts.append(
                f'<text x="{PAD_L - 8}" y="{ly}" '
                f'font-family="\'SF Mono\',\'Fira Code\',monospace" font-size="8" '
                f'fill="#4a3a7a" text-anchor="end">{label}</text>'
            )

    # ── flowers ───────────────────────────────────────────────────────────────
    for ci, col in enumerate(grid):
        for ri, (date, count) in enumerate(col):
            if count < 0:
                continue
            cx = PAD_L + ci * STEP + CELL // 2
            cy = PAD_T + ri * STEP + CELL // 2
            seed = ci * 7 + ri

            # cell background — faint glow pill
            if count > 0:
                intensity = min(count / 12, 1.0)
                col_hex = pick_color(count, seed)
                parts.append(
                    f'<rect x="{PAD_L + ci * STEP}" y="{PAD_T + ri * STEP}" '
                    f'width="{CELL}" height="{CELL}" rx="4" '
                    f'fill="{col_hex}" opacity="{0.04 + intensity * 0.10:.2f}"/>'
                )

            if count == 0:
                parts.append(soil_dot(cx, cy, seed))
            elif count <= 2:
                c = pick_color(count, seed)
                parts.append(sprout(cx, cy + 3, c, seed))
            elif count <= 5:
                c = pick_color(count, seed)
                parts.append(daisy(cx, cy + 3, c, seed))
            elif count <= 9:
                c = pick_color(count, seed)
                parts.append(blossom(cx, cy + 2, c, seed))
            else:
                c = pick_color(count, seed)
                parts.append(lotus(cx, cy + 1, c, seed))

    # ── legend ────────────────────────────────────────────────────────────────
    lx = PAD_L
    ly = H - 16
    legend = [
        (soil_dot, "no commits",  "#888"),
        (None,     "1–2",         "#ff7ac6"),
        (None,     "3–5",         "#b28dff"),
        (None,     "6–9",         "#6be3ff"),
        (None,     "10+",         "#ffd6e0"),
    ]
    parts.append(
        f'<text x="{lx}" y="{ly + 4}" font-family="\'SF Mono\',monospace" '
        f'font-size="8" fill="#4a3a7a">less</text>'
    )
    lx += 28
    icons = ["·", "🌱", "🌷", "🌸", "🌺"]
    colors = ["#4a3a7a", "#ff7ac6", "#b28dff", "#6be3ff", "#ffd6e0"]
    for icon, color in zip(icons, colors):
        parts.append(
            f'<rect x="{lx}" y="{ly - 8}" width="13" height="13" rx="3" '
            f'fill="{color}" opacity="0.25"/>'
        )
        parts.append(
            f'<text x="{lx + 6}" y="{ly + 3}" font-family="serif" font-size="10" '
            f'fill="{color}" text-anchor="middle">{icon}</text>'
        )
        lx += 17
    parts.append(
        f'<text x="{lx + 4}" y="{ly + 4}" font-family="\'SF Mono\',monospace" '
        f'font-size="8" fill="#4a3a7a">more</text>'
    )

    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    os.makedirs("dist", exist_ok=True)
    grid = fetch()
    svg  = render(grid)
    with open("dist/flower-garden.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"🌸 done — {len(grid)} weeks rendered")
