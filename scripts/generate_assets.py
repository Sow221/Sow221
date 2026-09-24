"""Generate the animated SVG assets for the Sow221 profile README.

Animations use CSS keyframes only (no SMIL) so a single
`prefers-reduced-motion` rule can switch them all off.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

TEAL, INDIGO = "#14B8A6", "#6366F1"
SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
REDUCED = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; opacity: 1 !important; } }"

THEMES = {
    "dark": dict(bg="#0D1117", fg="#F0F6FC", muted="#8B949E", grid="#FFFFFF", grid_op=0.05, node="#161B22"),
    "light": dict(bg="#FFFFFF", fg="#0D1117", muted="#57606A", grid="#0D1117", grid_op=0.06, node="#F6F8FA"),
}


def banner(theme: str) -> str:
    t = THEMES[theme]
    # Small neural/data graph on the right-hand side.
    nodes = [(900, 100), (900, 175), (900, 250), (1015, 70), (1015, 145), (1015, 215), (1015, 285),
             (1130, 130), (1130, 220)]
    edges = [(0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6), (0, 5), (1, 3), (2, 4),
             (3, 7), (4, 7), (4, 8), (5, 8), (6, 8), (5, 7)]
    edge_svg = []
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        edge_svg.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="edge"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="pulse" '
            f'style="animation-delay:{(i * 0.37) % 4:.2f}s"/>'
        )
    node_svg = []
    for i, (x, y) in enumerate(nodes):
        color = TEAL if x < 950 else (INDIGO if x > 1100 else "url(#g)")
        node_svg.append(
            f'<circle cx="{x}" cy="{y}" r="11" fill="{t["node"]}" stroke="{color}" stroke-width="2.5"/>'
            f'<circle cx="{x}" cy="{y}" r="4" fill="{color}" class="core" style="animation-delay:{i * 0.3:.1f}s"/>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" role="img" aria-labelledby="title desc">
<title id="title">Moussa Sow</title>
<desc id="desc">Software Engineering, Information Systems, Data and AI</desc>
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{INDIGO}"/>
  </linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}"/>
  </pattern>
  <radialGradient id="glowT"><stop offset="0" stop-color="{TEAL}" stop-opacity=".35"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glowI"><stop offset="0" stop-color="{INDIGO}" stop-opacity=".35"/><stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/></radialGradient>
</defs>
<style>
  .edge {{ stroke: {t["muted"]}; stroke-opacity: .25; stroke-width: 1.5; }}
  .pulse {{ stroke: url(#g); stroke-width: 2.5; stroke-linecap: round; stroke-dasharray: 18 1000;
           stroke-dashoffset: 18; animation: flow 4s linear infinite; }}
  @keyframes flow {{ from {{ stroke-dashoffset: 18; }} to {{ stroke-dashoffset: -260; }} }}
  .core {{ animation: beat 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
  @keyframes beat {{ 0%,100% {{ opacity: .45; }} 50% {{ opacity: 1; }} }}
  .glow {{ animation: drift 12s ease-in-out infinite alternate; }}
  @keyframes drift {{ to {{ transform: translate(60px, 20px); }} }}
  .prompt {{ font: 500 20px {MONO}; fill: {TEAL}; }}
  .caret {{ fill: {TEAL}; animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  .name {{ font: 800 76px {SANS}; fill: {t["fg"]}; letter-spacing: -1.5px; }}
  .dom {{ font: 700 27px {SANS}; fill: url(#g); animation: rise 1.2s ease-out .3s backwards; }}
  .sep {{ fill: {t["muted"]}; }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(10px); }} }}
  .tag {{ font: 400 19px {SANS}; fill: {t["muted"]}; }}
  {REDUCED}
</style>
<rect width="1200" height="340" rx="20" fill="{t["bg"]}"/>
<rect width="1200" height="340" rx="20" fill="url(#grid)"/>
<circle class="glow" cx="980" cy="120" r="260" fill="url(#glowI)"/>
<circle class="glow" cx="760" cy="300" r="220" fill="url(#glowT)" style="animation-delay:-6s"/>
<text x="64" y="92" class="prompt">~/sow221 $ whoami</text>
<rect x="276" y="75" width="11" height="21" class="caret"/>
<text x="60" y="176" class="name">Moussa Sow</text>
<text x="64" y="226" class="dom">Software Engineering<tspan class="sep"> · </tspan>Information Systems<tspan class="sep"> · </tspan>Data &amp; AI</text>
<text x="64" y="274" class="tag">Maintainable, testable, deployable systems — extended with ML where it creates value.</text>
<rect x="64" y="300" width="120" height="4" rx="2" fill="url(#g)"/>
{"".join(edge_svg)}
{"".join(node_svg)}
</svg>
'''


def card_frame(inner: str, label: str, desc: str, extra_style: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" role="img" aria-labelledby="t d">
<title id="t">{label}</title><desc id="d">{desc}</desc>
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{INDIGO}"/>
  </linearGradient>
  <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
    <path d="M24 0H0V24" fill="none" stroke="#FFFFFF" stroke-opacity=".04"/>
  </pattern>
</defs>
<style>
  .lbl {{ font: 600 13px {MONO}; fill: #8B949E; }}
  .txt {{ font: 600 14px {SANS}; fill: #F0F6FC; }}
  .sm {{ font: 500 12px {SANS}; fill: #8B949E; }}
  {extra_style}
  {REDUCED}
</style>
<rect width="480" height="300" rx="16" fill="#0D1117"/>
<rect width="480" height="300" rx="16" fill="url(#grid)"/>
<rect x=".75" y=".75" width="478.5" height="298.5" rx="15.5" fill="none" stroke="#30363D" stroke-width="1.5"/>
<circle cx="24" cy="24" r="5" fill="#FF5F57"/><circle cx="42" cy="24" r="5" fill="#FEBC2E"/><circle cx="60" cy="24" r="5" fill="#28C840"/>
<text x="80" y="28" class="lbl">{label}</text>
{inner}
</svg>
'''


def engine_card() -> str:
    stages = [("Credit data", "raw · versioned"), ("Pipelines", "DVC · Dagster"),
              ("Model", "XGBoost · MLflow"), ("Serving", "FastAPI")]
    parts = []
    for i, (title, sub) in enumerate(stages):
        x = 22 + i * 112
        parts.append(
            f'<rect x="{x}" y="72" width="102" height="70" rx="10" fill="#161B22" stroke="{TEAL if i < 2 else INDIGO}" stroke-width="1.5"/>'
            f'<text x="{x + 51}" y="102" text-anchor="middle" class="txt">{title}</text>'
            f'<text x="{x + 51}" y="122" text-anchor="middle" class="sm" style="font-size:11px">{sub}</text>'
        )
        if i < 3:
            parts.append(f'<line x1="{x + 102}" y1="107" x2="{x + 112}" y2="107" stroke="url(#g)" stroke-width="2" class="flow"/>')
    # Drift monitor sparkline
    pts = "40,250 80,244 120,247 160,238 200,241 240,229 280,233 320,220 360,226 400,212 440,216"
    parts.append('<text x="28" y="180" class="lbl">drift monitor · PSI</text>')
    parts.append('<line x1="28" y1="205" x2="452" y2="205" stroke="#F85149" stroke-opacity=".5" stroke-dasharray="4 4"/>')
    parts.append('<text x="452" y="198" text-anchor="end" class="sm">alert threshold</text>')
    parts.append(f'<polyline points="{pts}" fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="spark"/>')
    style = (".flow { stroke-dasharray: 4 4; animation: dash 1s linear infinite; }"
             "@keyframes dash { to { stroke-dashoffset: -8; } }"
             ".spark { stroke-dasharray: 520; animation: draw 3s ease-out backwards; }"
             "@keyframes draw { from { stroke-dashoffset: 520; } }")
    return card_frame("".join(parts), "cif-credit-engine",
                      "Illustration: data flows through versioned pipelines to an XGBoost model served by FastAPI, with drift monitoring.",
                      style)


def platform_card() -> str:
    feats = [("repayment_history", 0.78, -1), ("savings_balance", 0.55, -1), ("loan_amount", 0.46, 1),
             ("thin_file", 0.34, 1), ("tenure_months", 0.22, -1)]
    parts = ['<text x="28" y="66" class="lbl">SHAP · feature contributions</text>',
             '<line x1="250" y1="80" x2="250" y2="210" stroke="#30363D"/>']
    for i, (name, w, sign) in enumerate(feats):
        y = 84 + i * 26
        width = w * 150
        x = 250 if sign > 0 else 250 - width
        color = "#F85149" if sign > 0 else TEAL
        parts.append(f'<text x="28" y="{y + 13}" class="sm">{name}</text>')
        parts.append(f'<rect x="{x:.0f}" y="{y}" width="{width:.0f}" height="16" rx="4" fill="{color}" class="bar" '
                     f'style="transform-origin:250px {y + 8}px;animation-delay:{i * .15:.2f}s"/>')
    chips = [("Approve", False), ("Human review", True), ("Adjust", False), ("Reject", False)]
    x = 28
    for label, active in chips:
        w = 16 + len(label) * 7.6
        stroke = INDIGO if active else "#30363D"
        fill = "#1F2150" if active else "#161B22"
        pick = ' class="pick"' if active else ""
        parts.append(f'<rect x="{x:.0f}" y="238" width="{w:.0f}" height="32" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="1.5"'
                     f'{pick}/>')
        parts.append(f'<text x="{x + w / 2:.0f}" y="259" text-anchor="middle" class="txt" style="font-size:13px">{label}</text>')
        x += w + 10
    style = (".bar { animation: grow .9s cubic-bezier(.2,.8,.2,1) backwards; }"
             "@keyframes grow { from { transform: scaleX(0); } }"
             ".pick { animation: ring 2s ease-in-out infinite; }"
             "@keyframes ring { 50% { stroke: #14B8A6; } }")
    return card_frame("".join(parts), "cif-credit-platform",
                      "Illustration: SHAP contributions explaining a credit score and the four decision outcomes.",
                      style)


def tontine_card() -> str:
    import math
    cx, cy, r = 240, 165, 92
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#30363D" stroke-width="2" stroke-dasharray="6 6"/>']
    n = 8
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="#161B22" stroke="{TEAL}" stroke-width="2"/>'
                     f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" class="sm" style="fill:#F0F6FC">{i + 1}</text>')
    parts.append(f'<g class="spin" style="transform-origin:{cx}px {cy}px">'
                 f'<circle cx="{cx}" cy="{cy - r}" r="21" fill="none" stroke="{INDIGO}" stroke-width="3"/></g>')
    parts.append(f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" class="txt" style="font-size:16px">Cycle</text>')
    parts.append(f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" class="sm">draw · payout</text>')
    style = (".spin { animation: turn 8s steps(8) infinite; }"
             "@keyframes turn { to { transform: rotate(360deg); } }")
    return card_frame("".join(parts), "tontinesn",
                      "Illustration: members of a tontine in a contribution cycle, with the payout rotating between them.",
                      style)


def footer() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 110" preserveAspectRatio="none" role="img" aria-label="Decorative wave">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{INDIGO}"/></linearGradient></defs>
<style>
  .w1 {{ animation: sway 9s ease-in-out infinite alternate; }}
  .w2 {{ animation: sway 13s ease-in-out infinite alternate-reverse; }}
  @keyframes sway {{ to {{ transform: translateX(-120px); }} }}
  {REDUCED}
</style>
<path class="w2" d="M0 60 C200 20 400 100 600 60 S1000 20 1200 60 S1600 100 1800 60 V110 H0Z" fill="url(#g)" opacity=".35"/>
<path class="w1" d="M0 75 C200 45 400 105 600 75 S1000 45 1200 75 S1600 105 1800 75 V110 H0Z" fill="url(#g)" opacity=".8"/>
</svg>
'''


def divider() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 12" preserveAspectRatio="none" role="img" aria-label="divider">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset=".3" stop-color="{TEAL}"/>
  <stop offset=".7" stop-color="{INDIGO}"/><stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/></linearGradient></defs>
<rect y="5" width="1200" height="2" rx="1" fill="url(#g)"/>
</svg>
'''


files = {
    "banner-dark.svg": banner("dark"),
    "banner-light.svg": banner("light"),
    "card-engine.svg": engine_card(),
    "card-platform.svg": platform_card(),
    "card-tontine.svg": tontine_card(),
    "footer-wave.svg": footer(),
    "divider.svg": divider(),
}
for name, content in files.items():
    (OUT / name).write_text(content, encoding="utf-8")
    print(f"{name}: {len(content)} bytes")
