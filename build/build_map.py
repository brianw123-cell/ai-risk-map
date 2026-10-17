#!/usr/bin/env python3
"""Build the AI Risk Map page from the scenario cards.

Usage:  python3 build/build_map.py
Reads   cards/*.md (skips files starting with _)
Writes  ai-risk-map.html
"""
import re, html, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
OUT = ROOT / "ai-risk-map.html"
ARGMAP = ROOT.parent / "AI Ethics" / "ai-argument-map.html"

DOMAINS = ["Health and biology", "Work and income", "Science, energy and environment",
           "Information and democracy", "Security and infrastructure", "Power and governance",
           "Daily life, mind and meaning", "Control of advanced AI", "none"]
TRIAGE = {
    "act-now": ("Policy: act now", "t-act"),
    "prepare-and-watch": ("Policy: prepare and watch", "t-prep"),
    "enforcement-problem": ("Enforcement problem", "t-enf"),
    "covered-communicate": ("Covered: communicate", "t-cov"),
    "communicate": ("Communicate", "t-com"),
}
CONF = ["very-low", "low", "medium", "high", "very-high"]
QUADS = {
    "gradual-shared": ("Steady tool", "Gradual change, benefits widely shared"),
    "fast-shared": ("Broad abundance", "Fast change, benefits widely shared"),
    "gradual-concentrated": ("Slow squeeze", "Gradual change, control concentrating"),
    "fast-concentrated": ("Runaway", "Fast change, control concentrated or lost"),
}

# ---------------- parsing ----------------
def parse_front(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise ValueError("missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"') for x in v[1:-1].split(",") if x.strip()]
        elif len(v) >= 2 and v[0] == v[-1] == '"':
            v = v[1:-1]
        meta[k.strip()] = v
    return meta, m.group(2)

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img alt="\1" src="\2">', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r'(?<!href=")(?<!src=")(?<![">])(https?://[^\s<)]+[^\s<).,;])', r'<a href="\1">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t

def md_to_html(body):
    lines = body.splitlines()
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        if s.startswith("# "):
            i += 1; continue  # title shown in summary
        if s.startswith("## "):
            out.append(f'<h4>{inline(s[3:])}</h4>'); i += 1; continue
        if s.startswith("### "):
            out.append(f'<h5>{inline(s[4:])}</h5>'); i += 1; continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            body_rows = [c for c in cells[1:] if not all(re.fullmatch(r":?-{2,}:?", x) for x in c)]
            h = "".join(f"<th>{inline(c)}</th>" for c in cells[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body_rows)
            out.append(f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            continue
        if re.match(r"^[-*] ", s):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append(re.sub(r"^\s*[-*] ", "", lines[i])); i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() and not re.match(r"^\s*[-*] |\s*\d+\. ", lines[i]):
                    items[-1] += " " + lines[i].strip(); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"^\d+\. ", s):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append(re.sub(r"^\s*\d+\. ", "", lines[i])); i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip() and not re.match(r"^\s*[-*] |\s*\d+\. ", lines[i]):
                    items[-1] += " " + lines[i].strip(); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||[-*] |\d+\. )", lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)

def load_cards():
    cards = []
    for p in sorted(CARDS.glob("*.md")):
        if p.name.startswith("_"):
            continue
        meta, body = parse_front(p.read_text())
        meta["body"] = body
        meta["file"] = p.name
        cards.append(meta)
    return cards

# ---------------- rendering helpers ----------------
def esc(t): return html.escape(str(t), quote=True)

def conf_dots(level):
    n = CONF.index(level) + 1 if level in CONF else 0
    label = level.replace("-", " ") if level in CONF else "not rated"
    return f'<span class="conf" title="Evidence confidence: {label}" aria-label="Evidence confidence: {label}">' + "".join(
        f'<i class="{"on" if k < n else ""}"></i>' for k in range(5)) + f'<span class="conf-l">{label}</span></span>'

def triage_chip(t):
    label, cls = TRIAGE.get(t, ("Not triaged", "t-none"))
    return f'<span class="chip {cls}">{label}</span>'

def dir_tag(d):
    return {"good": '<span class="dir d-good">Good direction</span>',
            "bad": '<span class="dir d-bad">Bad direction</span>',
            "neutral": '<span class="dir d-neu">Neutral</span>'}.get(d, "")

def prob_chart_html():
    """Reuse the themed probability chart from the AI Argument Map."""
    if not ARGMAP.exists():
        return None
    s = ARGMAP.read_text()
    m = re.search(r'(<figure class="chart">\s*<figcaption>\s*<span class="ctitle">How far apart the published estimates are</span>.*?</figure>)', s, re.S)
    if not m:
        return None
    fig = re.sub(r'<sup class="cite">.*?</sup>', "", m.group(1), flags=re.S)
    return fig

def render_card(c, names):
    body = md_to_html(c["body"])
    # swap the static estimates image for the themed chart
    if "loss-of-control-estimates.svg" in body:
        chart = prob_chart_html()
        if chart:
            body = re.sub(r'<p><img alt="[^"]*" src="img/loss-of-control-estimates.svg"></p>', chart, body)
    # link scenario names inside Related scenarios
    m = re.search(r"(<h4>Related scenarios</h4>)(.*?)(?=<h4>|$)", body, re.S)
    if m:
        seg = m.group(2)
        for nm, cid in sorted(names.items(), key=lambda x: -len(x[0])):
            if cid == c["id"]:
                continue
            seg = re.sub(r'(?<![\w>"])(' + re.escape(html.escape(nm, quote=False)) + r')(?![\w<])',
                         rf'<a href="#{cid}">\1</a>', seg, count=1, flags=re.I)
        body = body[:m.start(2)] + seg + body[m.end(2):]
    quads = " ".join(f'<span class="qtag">{QUADS[q][0]}</span>' for q in c.get("quadrants", []) if q in QUADS)
    status = "Draft. Not yet reviewed by either side" if c.get("status") == "draft" else esc(c.get("status", ""))
    return f'''
<details class="card" id="{esc(c["id"])}" data-triage="{esc(c.get("triage",""))}" data-dir="{esc(c.get("direction",""))}">
  <summary>
    <span class="c-name">{esc(c["name"])}</span>
    <span class="c-meta">{dir_tag(c.get("direction"))}{triage_chip(c.get("triage"))}{conf_dots(c.get("confidence"))}</span>
    <span class="c-sum">{esc(c.get("summary",""))}</span>
  </summary>
  <div class="c-body">
    <div class="c-facts"><span>Domain: {esc(c.get("domain") if c.get("domain")!="none" else "Outside any domain")}</span><span>Mechanism: {esc(", ".join(c.get("mechanism", [])) if isinstance(c.get("mechanism"), list) else c.get("mechanism",""))}</span><span>Big picture: {quads or "not set"}</span><span>Status: {status}</span></div>
    {body}
  </div>
</details>'''

def tile(c):
    return f'''<a class="tile" href="#{esc(c["id"])}" data-triage="{esc(c.get("triage",""))}" data-dir="{esc(c.get("direction",""))}">
      <span class="tile-n">{esc(c["name"])}</span>
      <span class="tile-m">{triage_chip(c.get("triage"))}{conf_dots(c.get("confidence"))}</span>
    </a>'''

def empty_tile(label):
    return f'<div class="tile empty"><span class="tile-n">{esc(label)}</span><span class="tile-m"><span class="chip t-none">Not yet drafted</span></span></div>'

# ---------------- page ----------------
PLANNED = {
    ("Health and biology", "good"): "Medical progress compressed into years",
    ("Health and biology", "bad"): "AI-assisted biological or chemical attack",
    ("Work and income", "good"): "Broad productivity gains and cheaper goods",
    ("Work and income", "bad"): "Mass job loss and widening inequality",
    ("Science, energy and environment", "good"): "Faster discovery and cheaper clean energy",
    ("Science, energy and environment", "bad"): "AI's energy and resource demand outpaces its gains",
    ("Information and democracy", "good"): "Better shared understanding and forecasting",
    ("Information and democracy", "bad"): "Manipulation, fraud and collapse of trust",
    ("Security and infrastructure", "good"): "Defenders gain the advantage",
    ("Security and infrastructure", "bad"): "Cheap large-scale cyberattacks and critical-system failures",
    ("Power and governance", "good"): "Wider access and more accountable institutions",
    ("Power and governance", "bad"): "Concentrated power or AI-enabled surveillance",
    ("Daily life, mind and meaning", "good"): "Personal tutors, care and freed time",
    ("Daily life, mind and meaning", "bad"): "Over-reliance, lost skills and unhealthy AI companions",
    ("Control of advanced AI", "good"): "Powerful AI that stays aligned and overseeable",
    ("Control of advanced AI", "bad"): "Loss of control over advanced AI",
    ("none", "good"): "AI disappoints: modest progress, investment falls",
    ("none", "bad"): "Unknown, combined and slow-building risks",
}

def borrowed_css():
    if not ARGMAP.exists():
        return ""
    st = re.search(r"<style>(.*?)</style>", ARGMAP.read_text(), re.S).group(1)
    parts = re.split(r"(?=/\* ---------- )", st)
    keep = [p for p in parts if re.match(r"/\* ---------- (charts|four questions diagram|probability spread)", p)]
    return "\n".join(keep).replace("@media (max-width:900px){", "").strip()

def borrowed_fq():
    if not ARGMAP.exists():
        return ""
    m = re.search(r'(<figure class="fq".*?</figure>)', ARGMAP.read_text(), re.S)
    return m.group(1).replace("The short answers come from section 05.", "The short answers come from the job-loss card.") if m else ""

TRIAGE_SVG = '''<figure class="fq tri">
  <svg viewBox="0 0 680 372" role="img" aria-labelledby="tri-t tri-d">
    <title id="tri-t">The four-step sorting test</title>
    <desc id="tri-d">Each scenario goes through four questions in order. Already illegal leads to covered or an enforcement problem. An action both sides accept leads to policy now. Severe, hard to reverse and plausible within ten years leads to prepare and watch. Otherwise communicate.</desc>
    <defs><marker id="tri-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
    <g>
      <rect class="claim" x="40" y="20" width="340" height="62" rx="6" stroke-width="1"/>
      <text class="num" x="54" y="38">STEP 1</text><text class="t" x="210" y="52" text-anchor="middle" dominant-baseline="central">Already illegal or regulated?</text><text class="sub" x="210" y="70" text-anchor="middle" dominant-baseline="central">Checks the "already covered" claim</text>
      <rect class="claim" x="40" y="112" width="340" height="62" rx="6" stroke-width="1"/>
      <text class="num" x="54" y="130">STEP 2</text><text class="t" x="210" y="144" text-anchor="middle" dominant-baseline="central">An action both sides accept?</text><text class="sub" x="210" y="162" text-anchor="middle" dominant-baseline="central">No need to settle the odds first</text>
      <rect class="claim" x="40" y="204" width="340" height="62" rx="6" stroke-width="1"/>
      <text class="num" x="54" y="222">STEP 3</text><text class="t" x="210" y="236" text-anchor="middle" dominant-baseline="central">Severe, hard to undo, within ~10 years?</text><text class="sub" x="210" y="254" text-anchor="middle" dominant-baseline="central">The only place worst-case thinking leads</text>
      <rect class="claim" x="40" y="296" width="340" height="62" rx="6" stroke-width="1"/>
      <text class="num" x="54" y="314">STEP 4</text><text class="t" x="210" y="328" text-anchor="middle" dominant-baseline="central">Everything else</text><text class="sub" x="210" y="346" text-anchor="middle" dominant-baseline="central">Name the purpose of the message</text>
    </g>
    <line class="ln" x1="210" y1="84" x2="210" y2="108" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="218" y="100">NO</text>
    <line class="ln" x1="210" y1="176" x2="210" y2="200" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="218" y="192">NO</text>
    <line class="ln" x1="210" y1="268" x2="210" y2="292" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="218" y="284">NO</text>
    <line class="ln" x1="382" y1="51" x2="426" y2="51" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="388" y="44">YES</text>
    <line class="ln" x1="382" y1="143" x2="426" y2="143" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="388" y="136">YES</text>
    <line class="ln" x1="382" y1="235" x2="426" y2="235" stroke-width="1" marker-end="url(#tri-arrow)"/><text class="num" x="388" y="228">YES</text>
    <line class="ln" x1="382" y1="327" x2="426" y2="327" stroke-width="1" marker-end="url(#tri-arrow)"/>
    <rect class="o-cov" x="430" y="20" width="210" height="62" rx="6" stroke-width="1"/>
    <text class="t" x="535" y="42" text-anchor="middle" dominant-baseline="central">Covered: communicate</text><text class="sub" x="535" y="64" text-anchor="middle" dominant-baseline="central">or Enforcement problem</text>
    <rect class="o-act" x="430" y="112" width="210" height="62" rx="6" stroke-width="1"/>
    <text class="t" x="535" y="143" text-anchor="middle" dominant-baseline="central">Policy: act now</text>
    <rect class="o-prep" x="430" y="204" width="210" height="62" rx="6" stroke-width="1"/>
    <text class="t" x="535" y="235" text-anchor="middle" dominant-baseline="central">Policy: prepare and watch</text>
    <rect class="o-com" x="430" y="296" width="210" height="62" rx="6" stroke-width="1"/>
    <text class="t" x="535" y="327" text-anchor="middle" dominant-baseline="central">Communicate</text>
  </svg>
  <figcaption>Every card shows its reasoning at each step, so anyone can disagree with a specific step rather than with the result as a whole. Good-direction scenarios run the same test with the question flipped: what is blocking this, and does removing the block need policy?</figcaption>
</figure>'''

CSS = r'''
:root{
  --ground:#eef0f3; --surface:#f8f9fb; --surface-2:#e2e7ed; --sunk:#e8ebef;
  --ink:#131a22; --ink-2:#3c4653; --ink-3:#6a7583; --rule:#c9d0d9; --rule-soft:#dde2e9;
  --accent:#8f6410; --accent-soft:#f2e7cd; --deep:#134a5b; --deep-soft:#dbe8ec;
  --s1:#2a78d6; --s2:#eb6834;
  --act:#134a5b; --act-ink:#ffffff; --prep:#8f6410; --prep-ink:#ffffff;
  --enf:#a3402a; --enf-soft:#f6e1da; --cov:#5b6673;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0d1218; --surface:#141b23; --surface-2:#1c242e; --sunk:#0a0e13;
    --ink:#e7ebf0; --ink-2:#b2bcc8; --ink-3:#7c8794; --rule:#2a333e; --rule-soft:#1f262f;
    --accent:#dda647; --accent-soft:#2c2415; --deep:#74b6c7; --deep-soft:#152932;
    --s1:#3987e5; --s2:#d95926;
    --act:#74b6c7; --act-ink:#0d1218; --prep:#dda647; --prep-ink:#0d1218;
    --enf:#e58a72; --enf-soft:#33201a; --cov:#9aa5b2;
  }
}
:root[data-theme="dark"]{
  --ground:#0d1218; --surface:#141b23; --surface-2:#1c242e; --sunk:#0a0e13;
  --ink:#e7ebf0; --ink-2:#b2bcc8; --ink-3:#7c8794; --rule:#2a333e; --rule-soft:#1f262f;
  --accent:#dda647; --accent-soft:#2c2415; --deep:#74b6c7; --deep-soft:#152932;
  --s1:#3987e5; --s2:#d95926;
  --act:#74b6c7; --act-ink:#0d1218; --prep:#dda647; --prep-ink:#0d1218;
  --enf:#e58a72; --enf-soft:#33201a; --cov:#9aa5b2;
}
*{box-sizing:border-box}
body{margin:0; background:var(--ground); color:var(--ink); font-family:"Source Serif 4",Georgia,serif; font-size:17px; line-height:1.6; -webkit-font-smoothing:antialiased}
.wrap{max-width:1180px; margin:0 auto; padding:0 clamp(1rem,4vw,3rem) 6rem}
h1,h2,h3,h4,h5{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; text-wrap:balance}
h1{font-size:clamp(2.6rem,7vw,4.8rem); line-height:1; font-weight:700; letter-spacing:-.03em; margin:0}
h2{font-size:clamp(1.5rem,3vw,2.05rem); line-height:1.12; font-weight:700; letter-spacing:-.02em; margin:0 0 .5rem}
p{margin:0 0 1em; max-width:68ch}
a{color:inherit; text-decoration:none; border-bottom:1px solid var(--accent)}
a:hover{color:var(--accent)}
a:focus-visible,summary:focus-visible,button:focus-visible{outline:2px solid var(--accent); outline-offset:3px; border-radius:2px}
.eyebrow{font-family:"IBM Plex Mono",monospace; font-size:.7rem; font-weight:600; letter-spacing:.16em; text-transform:uppercase; color:var(--ink-3)}
header.mast{padding:clamp(2.6rem,7vw,5rem) 0 2rem; border-bottom:2px solid var(--ink)}
.kicker{display:flex; gap:.6rem 1.4rem; flex-wrap:wrap; margin-bottom:1.8rem}
.kicker .eyebrow:first-child{color:var(--accent)}
.lede{font-size:clamp(1.08rem,2vw,1.3rem); line-height:1.5; color:var(--ink-2); max-width:60ch; margin:1.4rem 0 0}
.credit{font-size:.95rem; color:var(--ink-3); margin-top:1rem; max-width:64ch}
.stats{display:flex; flex-wrap:wrap; gap:1rem 2.4rem; margin-top:2rem; font-family:"IBM Plex Mono",monospace; font-size:.7rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-3)}
.stats b{display:block; font-family:Archivo,sans-serif; font-size:1.7rem; letter-spacing:-.02em; color:var(--ink); text-transform:none; line-height:1.1}
section{padding-top:3.6rem}
.sechead{border-top:1px solid var(--rule); padding-top:1rem; margin-bottom:1.6rem; display:grid; grid-template-columns:8rem minmax(0,1fr); gap:1.6rem}
.sechead .num{font-family:"IBM Plex Mono",monospace; font-size:.72rem; letter-spacing:.14em; color:var(--accent); font-weight:600; padding-top:.4rem}
.sechead p{color:var(--ink-2); margin:.4rem 0 0}
/* chips */
.chip{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:.62rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; padding:.22rem .45rem; border-radius:2px; border:1px solid transparent; white-space:nowrap; line-height:1.3}
.t-act{background:var(--act); color:var(--act-ink)}
.t-prep{background:var(--prep); color:var(--prep-ink)}
.t-enf{background:var(--enf-soft); color:var(--enf); border-color:var(--enf)}
.t-cov{background:transparent; color:var(--cov); border-color:var(--cov)}
.t-com{background:transparent; color:var(--ink-2); border-color:var(--rule); border-style:dashed}
.t-none{background:transparent; color:var(--ink-3); border-color:var(--rule); border-style:dotted}
.dir{font-family:"IBM Plex Mono",monospace; font-size:.62rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-3)}
.d-good{color:var(--deep)} .d-bad{color:var(--accent)}
.conf{display:inline-flex; align-items:center; gap:2px}
.conf i{width:7px; height:7px; border-radius:50%; border:1.5px solid var(--ink-3); display:inline-block}
.conf i.on{background:var(--ink-2); border-color:var(--ink-2)}
.conf-l{font-family:"IBM Plex Mono",monospace; font-size:.6rem; color:var(--ink-3); margin-left:.35rem; text-transform:uppercase; letter-spacing:.05em}
/* filters */
.filters{display:flex; flex-wrap:wrap; gap:.5rem; align-items:center; margin:0 0 1.2rem}
.filters .eyebrow{margin-right:.4rem}
.filters button{font-family:"IBM Plex Mono",monospace; font-size:.68rem; letter-spacing:.04em; padding:.4rem .7rem; border-radius:3px; border:1px solid var(--rule); background:var(--surface); color:var(--ink-2); cursor:pointer}
.filters button[aria-pressed="true"]{background:var(--ink); color:var(--ground); border-color:var(--ink)}
/* the map grid */
.mapwrap{overflow-x:auto}
.mapgrid{display:grid; grid-template-columns:11rem minmax(0,1fr) minmax(0,1fr); min-width:720px; border:1px solid var(--rule); border-radius:3px; background:var(--surface)}
.mapgrid > div,.mapgrid > a{border-top:1px solid var(--rule-soft)}
.mh{font-family:"IBM Plex Mono",monospace; font-size:.66rem; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-2); padding:.75rem .9rem; background:var(--surface-2); border-top:none !important}
.mh.good{color:var(--deep)} .mh.bad{color:var(--accent)}
.dl{padding:.9rem; font-family:Archivo,sans-serif; font-weight:600; font-size:.88rem; color:var(--ink-2); display:flex; align-items:center; border-right:1px solid var(--rule-soft)}
a.tile,div.tile{display:flex; flex-direction:column; gap:.55rem; padding:.85rem .95rem; border-bottom:none; border-left:3px solid transparent; transition:background .12s, opacity .15s}
a.tile:hover{background:var(--sunk); color:var(--ink)}
a.tile[data-dir="good"],a.tile[data-dir="neutral"]{border-left-color:var(--deep)}
a.tile[data-dir="bad"]{border-left-color:var(--accent)}
a.tile[data-dir="neutral"]{border-left-style:dashed}
.tile-n{font-family:Archivo,sans-serif; font-weight:600; font-size:.98rem; line-height:1.25; color:var(--ink)}
.tile-m{display:flex; flex-wrap:wrap; gap:.4rem .7rem; align-items:center}
.tile.empty .tile-n{color:var(--ink-3); font-weight:500}
.dim{opacity:.22}
/* quadrant */
.quad{display:grid; grid-template-columns:2rem 1fr 1fr; grid-template-rows:1fr 1fr 2rem; gap:.6rem; min-width:640px}
.quadwrap{overflow-x:auto}
.qcell{background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:1rem 1.1rem}
.qcell h3{font-size:1.05rem; margin:0} .qcell p{font-size:.86rem; color:var(--ink-3); margin:.15rem 0 .8rem}
.qchips{display:flex; flex-wrap:wrap; gap:.4rem}
.qchips a{font-size:.8rem; line-height:1.25; padding:.3rem .5rem; border-radius:3px; border:1.5px solid var(--rule); color:var(--ink); border-bottom-width:1.5px}
.qchips a.g{border-color:var(--deep); background:var(--deep-soft)}
.qchips a.b{border-color:var(--accent); background:var(--accent-soft)}
.qchips a.n{border-style:dashed; border-color:var(--deep)}
.yaxis{writing-mode:vertical-rl; transform:rotate(180deg); display:flex; justify-content:space-between; font-family:"IBM Plex Mono",monospace; font-size:.62rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3); grid-row:1 / span 2}
.xaxis{grid-column:2 / span 2; display:flex; justify-content:space-between; font-family:"IBM Plex Mono",monospace; font-size:.62rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3); align-items:center}
/* how to read */
.readgrid{display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:1.4rem; align-items:start}
.rules{background:var(--surface); border:1px solid var(--rule); border-radius:3px; padding:1.2rem 1.4rem}
.rules h3{font-size:1rem; margin:0 0 .6rem}
.rules ol,.rules ul{margin:0; padding-left:1.2rem; font-size:.94rem} .rules li{margin-bottom:.45rem}
figure.tri .o-act{fill:var(--act); stroke:var(--act)} figure.tri .o-prep{fill:var(--prep); stroke:var(--prep)}
figure.tri .o-cov{fill:var(--surface); stroke:var(--cov)} figure.tri .o-com{fill:var(--surface); stroke:var(--rule); stroke-dasharray:4 3}
figure.tri .o-act + text, figure.tri .o-prep + text{fill:var(--act-ink)}
/* cards */
.domain{margin-top:2.2rem}
.domain h3{font-size:.78rem; font-family:"IBM Plex Mono",monospace; letter-spacing:.14em; text-transform:uppercase; color:var(--ink-3); margin:0 0 .7rem; font-weight:600}
details.card{background:var(--surface); border:1px solid var(--rule); border-radius:3px; margin-bottom:.8rem; transition:opacity .15s}
details.card[data-dir="good"],details.card[data-dir="neutral"]{border-left:3px solid var(--deep)}
details.card[data-dir="bad"]{border-left:3px solid var(--accent)}
details.card > summary{cursor:pointer; list-style:none; padding:1rem 1.2rem; display:grid; gap:.45rem}
details.card > summary::-webkit-details-marker{display:none}
.c-name{font-family:Archivo,sans-serif; font-weight:700; font-size:1.15rem; letter-spacing:-.01em}
.c-name::after{content:" +"; color:var(--accent); font-family:"IBM Plex Mono",monospace; font-weight:600}
details[open] .c-name::after{content:" –"}
.c-meta{display:flex; flex-wrap:wrap; gap:.4rem .9rem; align-items:center}
.c-sum{color:var(--ink-2); font-size:.96rem; max-width:80ch}
.c-body{padding:.2rem 1.2rem 1.4rem; border-top:1px solid var(--rule-soft)}
.c-facts{display:flex; flex-wrap:wrap; gap:.4rem 1.4rem; font-family:"IBM Plex Mono",monospace; font-size:.66rem; color:var(--ink-3); margin:1rem 0 .4rem; text-transform:uppercase; letter-spacing:.05em}
.qtag{background:var(--surface-2); padding:.05rem .35rem; border-radius:2px; margin-right:.25rem; text-transform:none}
.c-body h4{font-size:.98rem; margin:1.6rem 0 .5rem; padding-top:.8rem; border-top:1px solid var(--rule-soft)}
.c-body h5{font-size:.9rem; margin:1rem 0 .4rem}
.c-body p,.c-body li{font-size:.95rem; max-width:76ch}
.c-body ul,.c-body ol{padding-left:1.25rem; margin:0 0 1em} .c-body li{margin-bottom:.35rem}
.c-body code{font-family:"IBM Plex Mono",monospace; font-size:.82em; background:var(--surface-2); padding:.05rem .25rem; border-radius:2px}
.c-body img{max-width:100%; height:auto}
.tw{overflow-x:auto; margin:.6rem 0 1.2rem; border:1px solid var(--rule-soft); border-radius:3px}
.tw table{border-collapse:collapse; width:100%; font-size:.85rem; min-width:560px}
.tw th{font-family:"IBM Plex Mono",monospace; font-size:.62rem; letter-spacing:.08em; text-transform:uppercase; text-align:left; color:var(--ink-3); background:var(--surface-2); padding:.55rem .7rem}
.tw td{padding:.55rem .7rem; border-top:1px solid var(--rule-soft); vertical-align:top; font-variant-numeric:tabular-nums}
.c-body a{word-break:break-word}
.method{display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1.2rem}
footer{margin-top:4rem; padding-top:1.4rem; border-top:2px solid var(--ink); font-family:"IBM Plex Mono",monospace; font-size:.7rem; color:var(--ink-3); line-height:1.8}
@media (max-width:760px){ .sechead{grid-template-columns:1fr; gap:.4rem} }
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''

JS = r'''
(function(){
  const btns=[...document.querySelectorAll('.filters button')];
  function apply(f){
    btns.forEach(b=>b.setAttribute('aria-pressed', String(b.dataset.f===f)));
    document.querySelectorAll('a.tile, details.card').forEach(el=>{
      const ok = f==='all' || el.dataset.triage===f || el.dataset.dir===f;
      el.classList.toggle('dim', !ok);
    });
  }
  btns.forEach(b=>b.addEventListener('click',()=>apply(b.dataset.f)));
  function openHash(){
    const id=decodeURIComponent(location.hash.slice(1));
    if(!id) return;
    const el=document.getElementById(id);
    if(el && el.tagName==='DETAILS'){ el.open=true; el.scrollIntoView({block:'start'}); }
  }
  window.addEventListener('hashchange', openHash);
  openHash();
  document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{
    const el=document.getElementById(a.getAttribute('href').slice(1));
    if(el && el.tagName==='DETAILS') el.open=true;
  }));
})();
'''

def build():
    cards = load_cards()
    by = {(c.get("domain"), c.get("direction") if c.get("direction") != "neutral" else "good"): c for c in cards}
    names = {c["name"]: c["id"] for c in cards}
    # short names for related-scenario linking
    for c in cards:
        short = re.split(r":", c["name"])[0].strip()
        names.setdefault(short, c["id"])

    n = len(cards)
    counts = {k: sum(1 for c in cards if c.get("triage") == k) for k in TRIAGE}
    signed = sum(1 for c in cards if c.get("status") == "signed-off")

    # grid
    g = ['<div class="mh">Domain</div><div class="mh good">Good direction</div><div class="mh bad">Bad direction</div>']
    for d in DOMAINS:
        label = d if d != "none" else "Outside any domain"
        g.append(f'<div class="dl">{esc(label)}</div>')
        for side in ("good", "bad"):
            c = by.get((d, side))
            g.append(tile(c) if c else empty_tile(PLANNED[(d, side)]))

    # quadrant
    def qchips(q):
        out = []
        for c in cards:
            if q in (c.get("quadrants") or []):
                cls = {"good": "g", "bad": "b"}.get(c.get("direction"), "n")
                out.append(f'<a class="{cls}" href="#{esc(c["id"])}">{esc(c["name"])}</a>')
        return "".join(out) or '<span class="dir">None yet</span>'
    def qcell(q):
        t, sub = QUADS[q]
        return f'<div class="qcell"><h3>{t}</h3><p>{sub}</p><div class="qchips">{qchips(q)}</div></div>'
    quad = f'''<div class="quad">
      <div class="yaxis"><span>Concentrated or lost</span><span>Shared</span></div>
      {qcell("gradual-shared")}{qcell("fast-shared")}{qcell("gradual-concentrated")}{qcell("fast-concentrated")}
      <div></div><div class="xaxis"><span>Gradual: AI as a normal technology</span><span>Fast transformation</span></div>
    </div>'''

    # cards by domain
    blocks = []
    for d in DOMAINS:
        cs = [c for c in cards if c.get("domain") == d]
        if not cs: continue
        cs.sort(key=lambda c: {"good": 0, "neutral": 0, "bad": 1}.get(c.get("direction"), 2))
        label = d if d != "none" else "Outside any domain"
        blocks.append(f'<div class="domain"><h3>{esc(label)}</h3>' + "".join(render_card(c, names) for c in cs) + "</div>")

    filt = ['<span class="eyebrow">Show</span>', '<button type="button" data-f="all" aria-pressed="true">All</button>']
    for k, (lab, _) in TRIAGE.items():
        if counts[k]:
            filt.append(f'<button type="button" data-f="{k}" aria-pressed="false">{lab} ({counts[k]})</button>')
    filt += ['<button type="button" data-f="good" aria-pressed="false">Good direction</button>',
             '<button type="button" data-f="bad" aria-pressed="false">Bad direction</button>']

    today = datetime.date(2026, 10, 9).strftime("%-d %B %Y")
    page = f'''<title>The AI Risk Map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>{CSS}
{borrowed_css()}
</style>
<div class="wrap">
<header class="mast">
  <div class="kicker"><span class="eyebrow">Working draft</span><span class="eyebrow">Not yet reviewed by either side</span><span class="eyebrow">Updated {today}</span></div>
  <h1>The AI<br>Risk Map</h1>
  <p class="lede">The major ways AI could go, good and bad, on one map. For each one, the worried side and the hopeful side make their case in their own words, every published probability is shown with its source, and a simple four-step test sorts out what needs new rules and what mainly needs explaining.</p>
  <p class="credit">The idea comes from Emad Mostaque, who said on the <a href="https://www.youtube.com/watch?v=LRdb8UmPnh0&amp;t=2954s">Moonshots podcast</a> in October 2026 that nobody had built a proper map of what both camps say about each scenario. He is hopeful about what AI can do and worried about who will own it, and every card here is built to be signed off by someone from each side before it counts.</p>
  <div class="stats">
    <div><b>{n}</b>scenarios</div>
    <div><b>{counts["act-now"]}</b>policy: act now</div>
    <div><b>{counts["prepare-and-watch"]}</b>prepare and watch</div>
    <div><b>{counts["enforcement-problem"] + counts["covered-communicate"]}</b>covered or enforcement</div>
    <div><b>{counts["communicate"]}</b>communicate</div>
    <div><b>{signed} of {n}</b>signed off by both sides</div>
  </div>
</header>

<section id="map" style="padding-top:2.6rem">
  <div class="sechead"><div class="num">01</div><div><h2>The map</h2><p>Eight areas of life, each with a good and a bad way things could go, plus two that fit nowhere. Click any scenario to open its card. The colored tag is the result of the sorting test; the dots show how solid the evidence is.</p></div></div>
  <div class="filters" role="group" aria-label="Filter scenarios">{"".join(filt)}</div>
  <div class="mapwrap"><div class="mapgrid">{"".join(g)}</div></div>
</section>

<section id="big-picture">
  <div class="sechead"><div class="num">02</div><div><h2>The big picture</h2><p>Underneath the disagreements sit two questions: how fast AI arrives, and whether control and benefits stay broadly shared. Each scenario sits in the futures where it is most likely. Some sit in more than one.</p></div></div>
  <div class="quadwrap">{quad}</div>
</section>

<section id="how-to-read">
  <div class="sechead"><div class="num">03</div><div><h2>How to read a card</h2><p>Every card follows the same structure, and the same rules apply to all of them, so a reader can compare scenarios without trusting anyone's overall judgment.</p></div></div>
  {borrowed_fq()}
  {TRIAGE_SVG}
  <div class="readgrid">
    <div class="rules"><h3>Probability rules</h3><ul>
      <li>The map never publishes a probability of its own.</li>
      <li>Every number shows who gave it, the exact question, the date, and how widely people disagreed.</li>
      <li>Numbers from differently worded questions are never averaged. Changing one word in a survey has doubled the answer.</li>
      <li>Where nobody has published an estimate, the card says so.</li>
    </ul></div>
    <div class="rules"><h3>Evidence confidence</h3><ul>
      <li>Separate from how likely something is. It rates how solid the evidence base is.</li>
      <li>Five levels, from very low (mostly argument, cannot be checked) to very high (many independent measurements agree).</li>
      <li>Most catastrophe estimates honestly rate low, because they cannot be scored until the outcome arrives.</li>
    </ul></div>
    <div class="rules"><h3>Fair statement</h3><ul>
      <li>Each side's case is written to be recognizable to that side's own proponents.</li>
      <li>Before a card counts as final, at least two people from each side sign off that their case is fairly stated, and may swap in quotes they prefer.</li>
      <li>"Worried" and "hopeful" are defined per scenario. Most people are worried about some and hopeful about others.</li>
    </ul></div>
  </div>
</section>

<section id="scenarios">
  <div class="sechead"><div class="num">04</div><div><h2>The scenarios</h2><p>Every card in full: both sides' cases, common ground, the questions that would change minds, published probabilities, early warning signs, existing law, and the sorting result with its reasoning. Sources are listed at the bottom of each card.</p></div></div>
  {"".join(blocks)}
</section>

<section id="method">
  <div class="sechead"><div class="num">05</div><div><h2>How the map is kept honest</h2><p>The hard part of a project like this is not the website. It is keeping it fair to both sides over time and paying for the upkeep without letting any one funder steer it.</p></div></div>
  <div class="method">
    <div class="rules"><h3>Getting on the map</h3><ul>
      <li>A named, credible person has written the scenario up publicly.</li>
      <li>It is meaningfully different from existing scenarios. Variants sit inside an existing card.</li>
      <li>A balanced panel agrees it deserves a place. New ideas wait in "Unknown, combined and slow-building risks" first.</li>
    </ul></div>
    <div class="rules"><h3>Staying fair</h3><ul>
      <li>Editors work in pairs, one from each side, with a neutral chair who rules on process only.</li>
      <li>Each release has a public review window. Every comment gets a written answer, and all are published.</li>
      <li>The whole map is plain text files with a public change history, under an open license so anyone can copy it.</li>
    </ul></div>
    <div class="rules"><h3>Money</h3><ul>
      <li>Every funder above a set amount is listed publicly.</li>
      <li>No single funder may provide more than a third of the budget.</li>
      <li>No money from AI companies, since the map covers them. This draft is self-funded.</li>
    </ul></div>
  </div>
  <p style="margin-top:1.6rem; color:var(--ink-2)">For the wider background on each issue, with charts and numbered sources, see the companion piece, <b>The AI Argument Map</b>.</p>
</section>

<footer>
  The AI Risk Map · Working draft, updated {today} · {n} scenarios, {signed} signed off by both sides<br>
  Generated from one file per scenario. Every figure links to its source on the card where it appears.
</footer>
</div>
<script>{JS}</script>
'''
    OUT.write_text(page)
    return n, counts

if __name__ == "__main__":
    n, counts = build()
    print(f"built {OUT.name}: {n} cards", counts)
