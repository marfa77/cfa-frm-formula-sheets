"""Regenerate README.md, FORMULAS.md, docs/index.html, docs/sitemap.xml, docs/robots.txt from data/."""
import json, pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(root/"data/formulas.json")); E = d["entries"]; W = json.load(open(root/"data/topic_weights.json"))["entries"]
REPO = "https://github.com/marfa77/cfa-frm-formula-sheets"; PAGES = "https://marfa77.github.io/cfa-frm-formula-sheets/"
exams = ["CFA Level I", "CFA Level II", "FRM Part I"]
def wtable(md=True):
    out = []
    for ex in exams:
        rows = [w for w in W if w["exam"] == ex]
        for sess in dict.fromkeys(w["session"] for w in rows):
            rs = [w for w in rows if w["session"] == sess]
            pct = lambda w: f'{w["weight_min_pct"]}%' if w["weight_min_pct"] == w["weight_max_pct"] else f'{w["weight_min_pct"]}–{w["weight_max_pct"]}%'
            out.append((ex, sess, rs[0]["source_url"], [(w["topic"], pct(w)) for w in rs]))
    return out
md_w = "\n".join(f'**{ex}**{" — " + s if s else ""} ([official source]({u})): ' + "; ".join(f"{t} {p}" for t, p in rows) + "\n" for ex, s, u, rows in wtable())
counts = ", ".join(f"{ex}: {sum(e['exam']==ex for e in E)}" for ex in exams)
(root/"README.md").write_text((root/"README.template.md").read_text().replace("{{N}}", str(len(E))).replace("{{COUNTS}}", counts).replace("{{WEIGHTS}}", md_w))
fm = ["# Formula sheet (CFA Level I, CFA Level II, FRM Part I)\n", f"Generated from `data/formulas.json` (v{d['version']}). Rendered version: {PAGES}\n"]
for ex in exams:
    fm.append(f"\n## {ex}\n")
    for t in dict.fromkeys(e["topic"] for e in E if e["exam"] == ex):
        fm.append(f"\n### {t}\n")
        for e in [e for e in E if e["exam"] == ex and e["topic"] == t]:
            fm.append(f"- **{e['name']}** (`{e['id']}`): $${e['latex']}$$ \n  Variables: {e['variables']}. Used for: {e['when_used']}.")
(root/"FORMULAS.md").write_text("\n".join(fm) + "\n")
link_txt = {"CFA Level I": "CFA Level I formula reference deck", "CFA Level II": "CFA Level II formula reference deck", "FRM Part I": "FRM Part I flashcard deck"}
sections = []
for ex in exams:
    ee = [e for e in E if e["exam"] == ex]; url = ee[0]["uniprep2go_url"]
    body = "".join(f'<h3>{html.escape(t)}</h3>' + "".join(f'<div class="f" id="{e["id"]}"><b>{html.escape(e["name"])}</b><div class="m">\\[{html.escape(e["latex"])}\\]</div><small>{html.escape(e["variables"])} — <i>{html.escape(e["when_used"])}</i></small></div>' for e in ee if e["topic"] == t) for t in dict.fromkeys(e["topic"] for e in ee))
    wt = next((r for r in wtable() if r[0] == ex), None)
    wl = "".join(f"<li>{html.escape(t)}: {p}</li>" for t, p in wt[3]) if wt else ""
    sections.append(f'<section id="{ex.lower().replace(" ","-")}"><h2>{ex} ({len(ee)} formulas)</h2><details><summary>Official topic weights{" (" + wt[1] + ")" if wt and wt[1] else ""}</summary><ul>{wl}</ul><small>Source: <a href="{wt[2]}" rel="noopener">{html.escape(wt[2])}</a></small></details>{body}<p>Practise these with the <a href="{url}">{link_txt[ex]}</a> from UniPrep2Go.</p></section>')
ld = {"@context":"https://schema.org","@type":"Dataset","name":"CFA & FRM Formula Sheets (cfa-frm-formula-sheets)",
 "description":f"Open, machine-readable formula reference for CFA Level I, CFA Level II and FRM Part I: {len(E)} formulas in LaTeX with variable definitions and use cases, organised by official CFA Institute and GARP topic areas, plus official topic weights with sources.",
 "url":PAGES,"license":"https://creativecommons.org/licenses/by/4.0/","isAccessibleForFree":True,"version":d["version"],"dateModified":d["source_checked"],
 "keywords":["CFA","FRM","finance formulas","formula sheet","quantitative finance","open data"],
 "creator":{"@type":"Organization","name":"UniPrep2Go","url":"https://uniprep2go.study"},
 "distribution":[{"@type":"DataDownload","encodingFormat":"application/json","contentUrl":f"https://raw.githubusercontent.com/marfa77/cfa-frm-formula-sheets/main/data/formulas.json"},
                 {"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":f"https://raw.githubusercontent.com/marfa77/cfa-frm-formula-sheets/main/data/formulas.csv"}]}
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CFA & FRM Formula Sheets — open dataset (CFA Level I, Level II, FRM Part I)</title>
<meta name="description" content="{html.escape(ld['description'])}"><link rel="canonical" href="{PAGES}">
<script type="application/ld+json">{json.dumps(ld)}</script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body)"></script>
<style>body{{font:15px/1.5 system-ui,sans-serif;margin:0 auto;max-width:960px;padding:24px;color:#1a1a1a}}h2{{border-bottom:2px solid #eee;padding-bottom:4px;margin-top:2em}}
.f{{padding:10px 0;border-bottom:1px solid #eee}}.m{{overflow-x:auto}}small{{color:#555}}input{{width:100%;padding:10px;font-size:1rem;border:1px solid #bbb;border-radius:6px}}a{{color:#0b5cad}}</style></head>
<body><h1>CFA & FRM Formula Sheets</h1>
<p>{len(E)} core formulas for CFA Level I, CFA Level II and FRM Part I, grouped by the official CFA Institute and GARP topic areas, with variable definitions and when to use each one. Official topic weights are linked to their sources. Last checked {d["source_checked"]}.
Download <a href="{REPO}/blob/main/data/formulas.json">JSON</a> · <a href="{REPO}/blob/main/data/formulas.csv">CSV</a> · <a href="{REPO}">GitHub</a>. Data licence: CC BY 4.0.</p>
<p><a href="#cfa-level-i">CFA Level I</a> · <a href="#cfa-level-ii">CFA Level II</a> · <a href="#frm-part-i">FRM Part I</a></p>
<input id="q" type="search" placeholder="Filter formulas (e.g. duration, VaR, WACC)…" aria-label="Filter">
{"".join(sections)}
<p><small>Independent study aid, not affiliated with or endorsed by CFA Institute or GARP. CFA® and FRM® are trademarks of their respective owners.</small></p>
<script>document.getElementById('q').addEventListener('input',e=>{{const q=e.target.value.toLowerCase();for(const r of document.querySelectorAll('.f'))r.style.display=r.textContent.toLowerCase().includes(q)?'':'none'}});</script>
</body></html>'''
(root/"docs/index.html").write_text(page)
(root/"docs/sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{PAGES}</loc><lastmod>{d["source_checked"]}</lastmod></url></urlset>\n')
(root/"docs/robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {PAGES}sitemap.xml\n")
print("docs ok")
