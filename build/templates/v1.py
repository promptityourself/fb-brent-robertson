TITLE = "Run sheet"
BLURB = "Broadcast style. Dark, timecoded, the session as a run sheet with planned chapters."

def render(S, POST, KNOW, OFFER, HOMEWORK, RUNSHEET, STEPS, SHOWNOTES, EXAMPLES, HONEST, AFTER, e, link):
    rows = "".join(
        f'<li><time>{e(t)}</time><div><b>{e(n)}</b><span class="dur">{m} min</span><p>{e(d)}</p></div></li>'
        for t, m, n, d in RUNSHEET)
    steps = "".join(
        f'<article><span class="num">{s["n"]}</span><h3>{e(s["name"])}</h3><p>{e(s["what"])}</p>'
        f'<p class="detail">{e(s["detail"])}</p><p class="links">{link(s["link"])}{" · " + link(s["link2"]) if s["link2"] else ""}</p></article>'
        for s in STEPS)
    notes = "".join(f'<li><time>{e(t)}</time>{e(n)}</li>' for t, n in SHOWNOTES)
    ex = "".join(
        f'<article><h3><a href="{e(x["url"])}" rel="noopener">{e(x["name"])}</a></h3><p class="role">{e(x["role"])}</p><p>{e(x["why"])}</p>'
        + (f'<blockquote>“{e(x["quote"])}”</blockquote>' if x["quote"] else "")
        + (f'<p class="links">Episode: {link(x["episode"])}</p>' if x["episode"] else "")
        + '</article>' for x in EXAMPLES)
    know = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in KNOW)
    offer = "".join(f'<li><b>{e(k)}</b> {e(v)}</li>' for k, v in OFFER)
    hw = "".join(f'<li><b>{e(k)}</b> {e(v)}</li>' for k, v in HOMEWORK)
    wants = "".join(f'<li>{e(w)}</li>' for w in POST["wants"])
    after = "".join(f'<li><b>{e(k)}</b> {e(v)}</li>' for k, v in AFTER)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(S["title"])} · Run sheet</title>
<meta name="description" content="{e(S["tagline"])}">
<style>
:root{{--bg:#0e0f12;--fg:#f2efe8;--muted:#9a978f;--line:#2a2c33;--card:#16181d;--red:#ff4b3e;--amber:#f5b942;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1040px;margin:0 auto;padding:0 16px 80px}}
a{{color:var(--amber)}}h1,h2,h3{{line-height:1.15;margin:0 0 .4em}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-bottom:1px solid var(--line);font-family:var(--mono);font-size:13px;color:var(--muted)}}
.top .live{{color:var(--red)}}.top .live::before{{content:"●";margin-right:6px;animation:blink 1.4s infinite}}
@keyframes blink{{50%{{opacity:.2}}}}
.hero{{padding:56px 0 32px}}.hero .kicker{{font-family:var(--mono);color:var(--amber);font-size:13px;letter-spacing:.12em;text-transform:uppercase}}
.hero h1{{font-size:clamp(2rem,6vw,3.6rem);letter-spacing:-.02em}}.hero p{{font-size:1.15rem;max-width:62ch;color:#d8d5cd}}
.cta{{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:6px;margin:12px 12px 0 0}}
.cta.alt{{background:transparent;border:1px solid var(--line);color:var(--fg)}}
section{{padding:40px 0;border-top:1px solid var(--line)}}section h2{{font-size:1.6rem}}section h2 small{{display:block;font-family:var(--mono);font-size:12px;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;margin-bottom:6px}}
.two{{display:grid;gap:24px;grid-template-columns:1fr 1fr}}@media(max-width:720px){{.two{{grid-template-columns:1fr}}}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:20px}}.card ul{{padding-left:18px;margin:0}}.card li{{margin:6px 0}}
dl{{display:grid;gap:16px;grid-template-columns:repeat(3,1fr);margin:0}}@media(max-width:720px){{dl{{grid-template-columns:1fr}}}}
dl div{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px}}dt{{font-family:var(--mono);font-size:12px;color:var(--amber);text-transform:uppercase;letter-spacing:.1em}}dd{{margin:8px 0 0}}
.sheet{{list-style:none;padding:0;margin:0;border-left:2px solid var(--line)}}.sheet li{{display:grid;grid-template-columns:72px 1fr;gap:12px;padding:14px 0 14px 18px;position:relative}}
.sheet li::before{{content:"";position:absolute;left:-7px;top:22px;width:12px;height:12px;border-radius:50%;background:var(--amber);border:2px solid var(--bg)}}
.sheet time{{font-family:var(--mono);color:var(--amber);font-size:15px;padding-top:2px}}.sheet b{{font-size:1.05rem}}.sheet .dur{{font-family:var(--mono);font-size:12px;color:var(--muted);margin-left:10px}}.sheet p{{margin:4px 0 0;color:#cfccc4}}
.steps{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}.steps article{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:20px;position:relative}}
.num{{font-family:var(--mono);font-size:2.4rem;color:var(--line);position:absolute;right:16px;top:8px;font-weight:700}}.steps h3{{font-size:1.1rem;padding-right:40px}}.detail{{color:var(--muted);font-size:.95rem}}.links{{font-size:.9rem}}
.notes{{list-style:none;padding:0;margin:0;columns:2;column-gap:32px}}@media(max-width:720px){{.notes{{columns:1}}}}.notes li{{break-inside:avoid;padding:8px 0;border-bottom:1px dashed var(--line);font-size:.98rem}}.notes time{{font-family:var(--mono);color:var(--amber);margin-right:12px;font-size:14px}}
.ex{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}.ex article{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:20px}}.ex h3{{font-size:1.05rem}}.ex h3 a{{color:var(--fg);text-decoration:none}}.role{{color:var(--muted);font-size:.9rem;margin-top:-6px}}
blockquote{{margin:12px 0 0;padding-left:12px;border-left:3px solid var(--amber);color:#e6e2d8;font-style:italic}}
.honest{{background:#1f1a12;border:1px solid #5a4a1f;border-radius:10px;padding:16px 20px;color:#f1e3b5}}
footer{{color:var(--muted);font-size:.9rem;padding-top:24px;border-top:1px solid var(--line)}}
</style></head><body><main>
<div class="top"><span>PROMPT IT YOURSELF · PROPOSAL</span><span class="live">PLANNED SESSION · 4H</span></div>
<header class="hero"><div class="kicker">For Brent, North Lakes</div><h1>Your Shopify store. Built live. By you.</h1>
<p>{e(S["tagline"])} You asked on Facebook for someone local to build it. This is a different offer: we build it together, in one session, and you leave able to run it.</p>
<a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["guests"])}">See who has done it</a></header>

<section><h2><small>00 · The brief</small>What you asked for</h2><div class="two">
<div class="card"><p><b>From your post.</b> {e(POST["where"])}.</p><ul>{wants}</ul></div>
<div class="card"><p><b>What you already have.</b></p><ul>{"".join(f"<li>{e(h)}</li>" for h in POST["has"])}</ul><p style="color:var(--muted)">{e(POST["unknown"])}</p></div></div>
<dl style="margin-top:24px">{know}</dl></section>

<section><h2><small>01 · The offer</small>What a session is</h2><div class="card"><ul>{offer}</ul></div></section>

<section><h2><small>02 · Before the show</small>What you bring</h2><div class="card"><ul>{hw}</ul></div></section>

<section><h2><small>03 · Run sheet</small>Four hours, minute by minute</h2><ol class="sheet">{rows}</ol></section>

<section><h2><small>04 · The method</small>Five steps, each one Shopify's own</h2><div class="steps">{steps}</div>
<p class="honest" style="margin-top:20px">{e(HONEST)}</p></section>

<section><h2><small>05 · Planned show notes</small>The chapters the episode page will carry</h2><ol class="notes">{notes}</ol></section>

<section><h2><small>06 · Examples</small>People who came on with a real problem</h2><div class="ex">{ex}</div></section>

<section><h2><small>07 · After</small>What happens next</h2><div class="card"><ul>{after}</ul></div>
<p><a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["piy"])}">promptityourself.com</a></p></section>
<footer>Proposal page, 17 October 2026. Shopify prices and limits are from Shopify's Australian pricing page and help centre on that date. <a href="../">Other versions of this page</a>.</footer>
</main></body></html>'''
