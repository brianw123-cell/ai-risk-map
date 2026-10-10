#!/usr/bin/env python3
"""Build the public site for Vercel: the risk map plus three infographics.

Usage:  python3 build/build_site.py [site_url]
Writes  site/index.html, site/poster.html, site/landscape.html, site/anatomy.html, site/vercel.json
"""
import sys, math, html, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_map as B

ROOT = B.ROOT
SITE = ROOT / "site"
URL = (sys.argv[1] if len(sys.argv) > 1 else "ai-risk-map.vercel.app").replace("https://", "").rstrip("/")
EPISODE = "Moonshots with Peter Diamandis, 7 October 2026, at 49:14"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">'

def doc(title, desc, head_extra, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="description" content="{html.escape(desc)}">
<title>{html.escape(title)}</title>
{head_extra}
</head>
<body>
{body}
</body>
</html>
'''

# ---------- shared infographic styling (deliberately single light theme, made for sharing) ----------
IG_CSS = '''
:root{--bg:#e9ecf0;--paper:#f8f9fb;--ink:#131a22;--ink2:#3c4653;--ink3:#6a7583;--rule:#c9d0d9;--soft:#dde2e9;
--deep:#134a5b;--deepsoft:#dbe8ec;--accent:#8f6410;--accentsoft:#f2e7cd;--act:#134a5b;--prep:#8f6410;--enf:#a3402a;--dot:#2a78d6;color-scheme:light}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink)}
body{font-family:"Source Serif 4",Georgia,serif;padding:24px 16px}
.sheet{max-width:1200px;margin:0 auto;background:var(--paper);border:1px solid var(--rule);padding:clamp(24px,5vw,60px)}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
h1{font-family:Archivo,"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:-.03em;line-height:1;font-size:clamp(40px,7vw,76px);margin:12px 0 0;text-wrap:balance}
.sub{font-size:clamp(17px,2vw,22px);line-height:1.45;color:var(--ink2);max-width:62ch;margin:16px 0 0}
.mono{font-family:"IBM Plex Mono",monospace}
.foot{margin-top:36px;padding-top:18px;border-top:2px solid var(--ink);display:flex;flex-wrap:wrap;gap:8px 28px;justify-content:space-between;font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink3);line-height:1.6}
.foot b{color:var(--ink);font-weight:600}
.legend{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:22px;font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink2)}
.legend span{display:inline-flex;align-items:center;gap:8px}
.sw{width:18px;height:14px;border-radius:2px;display:inline-block}
.sw.act{background:var(--act)}.sw.prep{background:var(--prep)}.sw.enf{background:var(--enf)}.sw.com{background:#fff;border:1.5px dashed var(--ink3)}
a{color:inherit}
'''

TRI = {"act-now": ("act", "Policy: act now"), "prepare-and-watch": ("prep", "Prepare and watch"),
       "enforcement-problem": ("enf", "Enforcement problem"), "covered-communicate": ("com", "Covered"),
       "communicate": ("com", "Communicate")}

def stats(cards):
    c = {k: sum(1 for x in cards if x["triage"] == k) for k in TRI}
    signed = sum(1 for x in cards if x.get("status") == "signed-off")
    return c, signed

def footer(cards):
    return f'''<div class="foot"><span>Idea: Emad Mostaque, {EPISODE}.</span><span>Full map with every source: <b>{URL}</b></span><span>Working draft, October 2026. {stats(cards)[1]} of {len(cards)} scenarios signed off by both sides so far.</span></div>'''

# ---------- option 1: poster grid ----------
def poster(cards):
    by = {(c["domain"], "good" if c["direction"] in ("good", "neutral") else "bad"): c for c in cards}
    rows = []
    for d in B.DOMAINS:
        lab = d if d != "none" else "Outside any domain"
        cells = []
        for side in ("good", "bad"):
            c = by[(d, side)]
            cls, tl = TRI[c["triage"]]
            neu = ' <span class="neu">neutral</span>' if c["direction"] == "neutral" else ""
            cells.append(f'<div class="cell {cls}"><span class="nm">{html.escape(c["name"])}</span><span class="tl">{tl}{neu}</span></div>')
        rows.append(f'<div class="dom">{html.escape(lab)}</div>' + "".join(cells))
    s, signed = stats(cards)
    css = IG_CSS + '''
.grid{display:grid;grid-template-columns:minmax(120px,210px) 1fr 1fr;gap:6px;margin-top:34px}
.gh{font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;padding:0 4px 6px}
.gh.g{color:var(--deep)}.gh.b{color:var(--accent)}
.dom{font-family:Archivo,sans-serif;font-weight:600;font-size:15px;color:var(--ink2);display:flex;align-items:center;padding:10px 4px;border-top:1px solid var(--soft)}
.cell{border-radius:3px;padding:14px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px;min-height:76px;min-width:0}
.cell .nm{font-family:Archivo,sans-serif;font-weight:600;font-size:clamp(14px,1.6vw,17px);line-height:1.22}
.cell .tl{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;opacity:.85}
.cell.act{background:var(--act);color:#fff}.cell.prep{background:var(--prep);color:#fff}.cell.enf{background:var(--enf);color:#fff}
.cell.com{background:#fff;color:var(--ink);border:1.5px dashed var(--ink3)}
.neu{margin-left:6px;padding:1px 5px;border:1px solid currentColor;border-radius:2px}
.stats{display:flex;flex-wrap:wrap;gap:14px 40px;margin-top:30px}
.stats div{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3)}
.stats b{display:block;font-family:Archivo,sans-serif;font-size:40px;letter-spacing:-.02em;color:var(--ink);text-transform:none;line-height:1.05}
@media (max-width:640px){.grid{grid-template-columns:1fr 1fr}.dom{grid-column:1 / -1;padding-bottom:2px}.gh:first-child{display:none}}
'''
    body = f'''<div class="sheet">
<div class="eyebrow">The AI Risk Map · working draft</div>
<h1>Eighteen ways AI could go</h1>
<p class="sub">Eight areas of life, each with a hopeful and a worrying direction, plus two that fit nowhere. Every scenario gets both sides' case in their own words, every published probability, and one test: does it need new rules, or mainly explaining?</p>
<div class="grid"><div class="gh">Area</div><div class="gh g">Hopeful direction</div><div class="gh b">Worrying direction</div>{"".join(rows)}</div>
<div class="legend"><span><i class="sw act"></i>Policy: act now. An action both sides accept</span><span><i class="sw enf"></i>Enforcement problem. The law exists, enforcement lags</span><span><i class="sw prep"></i>Prepare and watch</span><span><i class="sw com"></i>Communicate</span></div>
<div class="stats"><div><b>{len(cards)}</b>scenarios</div><div><b>{s["act-now"]}</b>policy now</div><div><b>{s["enforcement-problem"]}</b>enforcement gaps</div><div><b>{s["prepare-and-watch"]}</b>prepare and watch</div><div><b>{s["communicate"]}</b>communicate</div><div><b>{signed}</b>signed off by both sides</div></div>
{footer(cards)}
</div>'''
    return doc("The AI Risk Map poster", "Eighteen ways AI could go, sorted by what needs new rules.", FONTS + f"<style>{css}</style>", body)

# ---------- option 2: landscape (3x3) ----------
def landscape(cards):
    def pos(c):
        q = c["quadrants"]
        sp = {x.split("-")[0] for x in q}; sh = {x.split("-")[1] for x in q}
        col = 0 if sp == {"gradual"} else 2 if sp == {"fast"} else 1
        row = 0 if sh == {"shared"} else 2 if sh == {"concentrated"} else 1
        return row, col
    cells = {(r, k): [] for r in range(3) for k in range(3)}
    for c in cards:
        cells[pos(c)].append(c)
    rowlab = ["Benefits and control widely shared", "Could go either way", "Control concentrated or lost"]
    collab = ["Gradual change", "Either pace", "Fast change"]
    g = ['<div></div>'] + [f'<div class="ch">{x}</div>' for x in collab]
    for r in range(3):
        g.append(f'<div class="rh">{rowlab[r]}</div>')
        for k in range(3):
            items = "".join(f'<span class="chip {"g" if c["direction"]=="good" else "b" if c["direction"]=="bad" else "n"}">{html.escape(c["name"])}</span>' for c in sorted(cells[(r, k)], key=lambda c: c["direction"]))
            g.append(f'<div class="cell{" empty" if not items else ""}">{items or "<span class=none>none</span>"}</div>')
    shared = len(cells[(0, 1)]) + len(cells[(0, 0)]) + len(cells[(0, 2)])
    css = IG_CSS + '''
.wrapg{overflow-x:auto;margin-top:34px}
.lg{display:grid;grid-template-columns:150px repeat(3,minmax(0,1fr));gap:8px;min-width:760px}
.ch{font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);text-align:center;padding-bottom:4px}
.rh{font-family:Archivo,sans-serif;font-weight:600;font-size:14px;color:var(--ink2);display:flex;align-items:center;line-height:1.25}
.cell{background:#fff;border:1px solid var(--rule);border-radius:4px;padding:12px;display:flex;flex-wrap:wrap;align-content:center;justify-content:center;gap:7px;min-height:130px}
.cell.empty{background:repeating-linear-gradient(45deg,transparent 0 8px,#eef0f3 8px 9px);}
.none{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink3);text-transform:uppercase;letter-spacing:.08em}
.chip{font-family:Archivo,sans-serif;font-weight:500;font-size:13.5px;line-height:1.25;padding:6px 9px;border-radius:3px;border:1.5px solid}
.chip.g{border-color:var(--deep);background:var(--deepsoft);color:#0d3441}
.chip.b{border-color:var(--accent);background:var(--accentsoft);color:#5c400a}
.chip.n{border-color:var(--deep);border-style:dashed;background:#fff}
.axisx{display:flex;justify-content:space-between;margin:10px 0 0 158px;min-width:600px;font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink3)}
.take{margin-top:26px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.take div{border-left:3px solid var(--accent);padding:4px 0 4px 14px;font-size:16px;line-height:1.45;color:var(--ink2)}
.take b{color:var(--ink)}
'''
    body = f'''<div class="sheet">
<div class="eyebrow">The AI Risk Map · the big picture</div>
<h1>Where AI's futures sit</h1>
<p class="sub">Most arguments about AI come down to two questions: how fast it arrives, and whether control and benefits stay widely shared. Each of the eighteen scenarios is placed in the futures where it is most likely.</p>
<div class="wrapg"><div class="lg">{"".join(g)}</div><div class="axisx"><span>← slower, AI as a normal technology</span><span>faster, transformative AI →</span></div></div>
<div class="legend"><span><i class="sw" style="background:var(--deepsoft);border:1.5px solid var(--deep)"></i>Hopeful scenario</span><span><i class="sw" style="background:var(--accentsoft);border:1.5px solid var(--accent)"></i>Worrying scenario</span><span><i class="sw" style="background:#fff;border:1.5px dashed var(--deep)"></i>Neutral</span></div>
<div class="take">
<div><b>{shared} of {len(cards)}</b> scenarios belong to futures where AI is widely shared. That includes the two misuse risks, because wide access is what makes misuse possible.</div>
<div><b>The concentration risks sit together at the bottom:</b> job loss, energy demand, concentrated power. They don't depend on how fast AI arrives.</div>
<div><b>Only loss of control needs both fast change and lost control.</b> It is the most debated scenario, and the narrowest.</div>
</div>
{footer(cards)}
</div>'''
    return doc("Where AI's futures sit", "The eighteen AI Risk Map scenarios placed by speed and by who controls the technology.", FONTS + f"<style>{css}</style>", body)

# ---------- option 3: anatomy of one scenario ----------
def prob_svg():
    X0, X1 = 330, 1040
    def x(v): return X0 + (math.log10(v) + 1) / (math.log10(30) + 1) * (X1 - X0)
    rows = [("Expert forecasters", "Tournament, 2022. Extinction by 2100", 0.38, None),
            ("AI domain experts", "Same tournament and question", 3, None),
            ("Skeptical panel", "Collaboration, 2023. Catastrophe by 2100", 0.12, None),
            ("Concerned panel", "Same collaboration and question", 20, None),
            ("AI researchers", "Survey of 2,778, 2023. Extremely bad outcome", 5, None),
            ("Geoffrey Hinton", "Personal estimate, 2024. Within ~30 years", 10, 20)]
    top, rh = 20, 44; H = top + len(rows) * rh + 40
    o = [f'<svg viewBox="0 0 1080 {H}" role="img" aria-label="Published estimates of the chance AI causes extinction or catastrophe range from 0.12% to 20%" style="width:100%;height:auto;display:block">']
    for v, l in [(0.1, "0.1%"), (0.3, "0.3%"), (1, "1%"), (3, "3%"), (10, "10%"), (30, "30%")]:
        xx = x(v); o.append(f'<line x1="{xx:.0f}" y1="{top}" x2="{xx:.0f}" y2="{top+len(rows)*rh}" stroke="#dde2e9"/>')
        o.append(f'<text x="{xx:.0f}" y="{top+len(rows)*rh+20}" font-family="IBM Plex Mono,monospace" font-size="13" fill="#6a7583" text-anchor="middle">{l}</text>')
    for i, (n, sub, v, hi) in enumerate(rows):
        cy = top + i * rh + 24
        o.append(f'<text x="0" y="{cy-3}" font-family="Archivo,sans-serif" font-weight="600" font-size="16" fill="#131a22">{n}</text>')
        o.append(f'<text x="0" y="{cy+14}" font-family="Source Serif 4,Georgia,serif" font-size="13" fill="#3c4653">{sub}</text>')
        o.append(f'<line x1="{X0}" y1="{cy}" x2="{X1}" y2="{cy}" stroke="#c9d0d9"/>')
        if hi:
            a, b = x(v), x(hi)
            o.append(f'<rect x="{a:.0f}" y="{cy-6}" width="{b-a:.0f}" height="12" rx="6" fill="#2a78d6"/>')
            o.append(f'<text x="{(a+b)/2:.0f}" y="{cy-12}" font-family="IBM Plex Mono,monospace" font-size="13" fill="#3c4653" text-anchor="middle">10–20%</text>')
        else:
            xx = x(v)
            o.append(f'<circle cx="{xx:.0f}" cy="{cy}" r="8" fill="#2a78d6" stroke="#f8f9fb" stroke-width="2.5"/>')
            o.append(f'<text x="{xx:.0f}" y="{cy-13}" font-family="IBM Plex Mono,monospace" font-size="13" fill="#3c4653" text-anchor="middle">{v:g}%</text>')
    o.append("</svg>")
    return "".join(o)

def anatomy(cards):
    css = IG_CSS + '''
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin-top:34px}
.side{border-radius:4px;padding:22px 24px}
.side.w{background:var(--accentsoft);border-top:5px solid var(--accent)}
.side.s{background:var(--deepsoft);border-top:5px solid var(--deep)}
.side h3,.blk h3{font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin:0 0 12px;color:var(--ink2)}
.side p{margin:0 0 10px;font-size:17px;line-height:1.45}
.side .who{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink3)}
.blk{margin-top:34px}
.blk .lead{font-size:17px;color:var(--ink2);margin:0 0 14px;max-width:70ch;line-height:1.45}
.agree{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.agree div{background:#fff;border:1px solid var(--rule);border-radius:4px;padding:14px 16px;font-size:16px;line-height:1.4}
.path{display:flex;flex-wrap:wrap;align-items:stretch;gap:10px}
.step{flex:1 1 170px;border:1.5px solid var(--rule);border-radius:4px;padding:12px 14px;background:#fff;font-size:15px;line-height:1.35}
.step .n{display:block;font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.12em;color:var(--ink3);margin-bottom:4px}
.step .a{display:block;font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;margin-top:8px}
.step.no .a{color:var(--ink3)} .step.yes{border-color:var(--act)} .step.yes .a{color:var(--act)}
.step.res{background:var(--act);color:#fff;border-color:var(--act);font-family:Archivo,sans-serif;font-weight:700;font-size:20px;display:flex;align-items:center}
.step.skip{opacity:.4;border-style:dashed}
.arrow{align-self:center;font-family:"IBM Plex Mono",monospace;color:var(--ink3)}
'''
    body = f'''<div class="sheet">
<div class="eyebrow">The AI Risk Map · anatomy of one scenario</div>
<h1>Loss of control over advanced AI</h1>
<p class="sub">The most argued-over scenario on the map, broken down the way all eighteen are: both sides' case, every published number, what they already agree on, and the sorting test.</p>
<div class="two">
<div class="side w"><h3>The worried case</h3>
<p>Nobody can yet reliably give an AI the goals we intend, or fully read the goals it ends up with.</p>
<p>Once systems out-plan us, a mismatch could become impossible to correct, and the downside cannot be undone.</p>
<p class="who">Eliezer Yudkowsky and Nate Soares (2025). Geoffrey Hinton (2024).</p></div>
<div class="side s"><h3>The skeptical case</h3>
<p>Being intelligent does not imply wanting to dominate. Safety is an engineering problem, like early jet engines.</p>
<p>Deployment stays gradual, which gives societies time to notice and fix problems, as with every past technology.</p>
<p class="who">Yann LeCun (2023). Arvind Narayanan and Sayash Kapoor (2025).</p></div>
</div>
<div class="blk"><h3>How far apart the published estimates are</h3>
<p class="lead">Each dot is a published median. The scale is logarithmic because the estimates span more than a hundredfold, and months of structured debate barely moved anyone. The map never adds a number of its own.</p>
{prob_svg()}</div>
<div class="blk"><h3>What both camps already agree on</h3>
<p class="lead">From a November 2025 joint essay by the authors of the two best-known opposing forecasts, "AI 2027" and "AI as Normal Technology."</p>
<div class="agree"><div>AI should not autonomously control critical systems.</div><div>Developers should be transparent and independently audited.</div><div>Governments need real technical capacity to track AI.</div><div>No unmonitored AI rebuilding itself.</div></div></div>
<div class="blk"><h3>The sorting test</h3>
<div class="path">
<div class="step no"><span class="n">STEP 1</span>Already covered by law?<span class="a">NO</span></div><span class="arrow">→</span>
<div class="step yes"><span class="n">STEP 2</span>An action both sides accept?<span class="a">YES, THE LIST ABOVE</span></div><span class="arrow">→</span>
<div class="step res">Policy: act now</div>
</div>
<p class="lead" style="margin-top:14px">The safeguards don't depend on settling who is right about the odds. That is the point of the map: find the actions both sides can live with.</p></div>
{footer(cards)}
</div>'''
    return doc("Anatomy of an AI scenario", "How the AI Risk Map breaks down one scenario: loss of control over advanced AI.", FONTS + f"<style>{css}</style>", body)


# ---------- download bar (site only; downloads don't work inside the claude.ai artifact) ----------
DL_JS = """<script>(function(){var q=new URLSearchParams(location.search);var b=document.querySelector('.dlbar');
if(q.has('print')){document.querySelectorAll('details').forEach(function(d){d.open=true});}
if((q.has('bare')||q.has('print'))&&b){b.remove();}})();</script>"""
DL_CSS_PAGE = """<style>
.dlbar{display:flex;justify-content:flex-end;align-items:center;gap:.6rem;flex-wrap:wrap;padding:1rem 0 0}
.dlbtn{font-family:"IBM Plex Mono",monospace;font-size:.72rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:.6rem .95rem;border:1px solid var(--ink);border-radius:3px;color:var(--ink);background:var(--surface);text-decoration:none}
.dlbtn:hover{color:var(--ink);background:var(--surface-2)}
.dlbtn.primary{background:var(--ink);color:var(--ground)}
.dlbtn.primary:hover{background:var(--ink-2);color:var(--ground)}
@media print{.dlbar,.filters{display:none!important} body{-webkit-print-color-adjust:exact;print-color-adjust:exact} details.card{break-inside:avoid-page} .mapgrid,.quad{min-width:0} @page{margin:12mm}}
</style>"""
DL_CSS_IG = """<style>
.dlbar{max-width:1200px;margin:0 auto 12px;display:flex;justify-content:flex-end;align-items:center;gap:10px;flex-wrap:wrap}
.dlbtn{font-family:"IBM Plex Mono",monospace;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:10px 14px;border:1px solid var(--ink);border-radius:3px;color:var(--ink);background:var(--paper);text-decoration:none}
.dlbtn.primary{background:var(--ink);color:#fff}
@media print{.dlbar{display:none!important}}
</style>"""

def dl_bar(links):
    return '<div class="dlbar">' + "".join(
        f'<a class="dlbtn{" primary" if i == 0 else ""}" href="{href}"' + (f' download="{dl}"' if dl else "") + f'>{label}</a>'
        for i, (label, href, dl) in enumerate(links)) + '</div>'

def with_bar(page, links, css):
    page = page.replace("</head>", css + "\n</head>", 1)
    if '<div class="wrap">' in page:
        page = page.replace('<div class="wrap">', '<div class="wrap">' + dl_bar(links), 1)
    else:
        page = page.replace("<body>\n", "<body>\n" + dl_bar(links) + "\n", 1)
    return page.replace("</body>", DL_JS + "\n</body>", 1)

def main():
    SITE.mkdir(exist_ok=True)
    B.build()
    page = B.OUT.read_text()
    head, body = page.split('<div class="wrap">', 1)
    index = doc("The AI Risk Map", "Eighteen AI futures, good and bad, each with both sides' case, sourced probabilities and a test for what needs policy.", head, '<div class="wrap">' + body)
    (SITE / "index.html").write_text(with_bar(index, [("Download PDF summary", "/downloads/ai-risk-map-summary.pdf", "ai-risk-map-summary.pdf"), ("Full PDF, every card", "/downloads/ai-risk-map.pdf", "ai-risk-map.pdf"), ("One-page overview", "/poster", None)], DL_CSS_PAGE))
    cards = B.load_cards()
    for name, fn in (("poster", poster), ("landscape", landscape), ("anatomy", anatomy)):
        links = [("Download PDF", f"/downloads/ai-risk-map-{name}.pdf", f"ai-risk-map-{name}.pdf"),
                 ("Download image", f"/img/{name}.png", f"ai-risk-map-{name}.png"), ("Full map", "/", None)]
        (SITE / f"{name}.html").write_text(with_bar(fn(cards), links, DL_CSS_IG))
    (SITE / "vercel.json").write_text(json.dumps({"cleanUrls": True, "ignoreCommand": "git diff --quiet HEAD^ HEAD -- ."}, indent=2))
    print("site built for", URL)

if __name__ == "__main__":
    main()
