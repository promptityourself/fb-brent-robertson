TITLE = "Checklist"
BLURB = "Light and plain. Five numbered cards, a time bar, and a checklist Brent can print."

def render(S, POST, KNOW, OFFER, HOMEWORK, RUNSHEET, STEPS, SHOWNOTES, EXAMPLES, HONEST, AFTER, e, link):
    total = sum(m for _, m, _, _ in RUNSHEET) or 1
    bar = "".join(
        f'<div class="seg{" short" if m < 20 else ""}" style="flex:{m}" title="{e(t)} {e(n)} ({m} min)"><span>{e(n)}</span></div>'
        for t, m, n, _ in RUNSHEET if m)
    rows = "".join(
        f'<tr><td class="t">{e(t)}</td><td class="m">{m or "—"}</td><td><b>{e(n)}</b><br><span class="muted">{e(d)}</span></td></tr>'
        for t, m, n, d in RUNSHEET)
    steps = "".join(
        f'<li class="step"><div class="badge">{s["n"]}</div><div><h3>{e(s["name"])}</h3><p>{e(s["what"])}</p>'
        f'<p class="muted">{e(s["detail"])}</p><p class="links">{link(s["link"])}{" · " + link(s["link2"]) if s["link2"] else ""}</p></div></li>'
        for s in STEPS)
    notes = "".join(f'<li><span class="t">{e(t)}</span>{e(n)}</li>' for t, n in SHOWNOTES)
    ex = "".join(
        f'<div class="person"><h3><a href="{e(x["url"])}" rel="noopener">{e(x["name"])}</a></h3><p class="muted">{e(x["role"])}</p><p>{e(x["why"])}</p>'
        + (f'<p class="q">“{e(x["quote"])}”</p>' if x["quote"] else "")
        + (f'<p class="links">{link(x["episode"])}</p>' if x["episode"] else "") + '</div>' for x in EXAMPLES)
    know = "".join(f'<div class="k"><h3>{e(k)}</h3><p>{e(v)}</p></div>' for k, v in KNOW)
    offer = "".join(f'<li><b>{e(k)}.</b> {e(v)}</li>' for k, v in OFFER)
    hw = "".join(f'<li><span class="box"></span><div><b>{e(k)}</b><br><span class="muted">{e(v)}</span></div></li>' for k, v in HOMEWORK)
    wants = "".join(f'<li><span class="box"></span>{e(w)}</li>' for w in POST["wants"])
    after = "".join(f'<li><b>{e(k)}.</b> {e(v)}</li>' for k, v in AFTER)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(S["title"])} · Checklist</title>
<meta name="description" content="{e(S["tagline"])}">
<style>
:root{{--bg:#fbfaf7;--fg:#1b1f1d;--muted:#5f6662;--line:#dfe3df;--card:#fff;--green:#008060;--green2:#e3f1ea;--ink:#111}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#111513;--fg:#e9ede9;--muted:#9aa49e;--line:#2a322d;--card:#171c19;--green:#3fbf93;--green2:#16281f;--ink:#fff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,"Times New Roman",serif}}
main{{max-width:900px;margin:0 auto;padding:0 16px 80px}}a{{color:var(--green)}}
h1,h2,h3{{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.15;margin:0 0 .4em;color:var(--ink)}}
.hero{{padding:56px 0 24px;border-bottom:3px solid var(--green)}}.hero h1{{font-size:clamp(2rem,6vw,3.2rem)}}.hero p{{font-size:1.15rem;max-width:60ch}}
.tag{{display:inline-block;background:var(--green2);color:var(--green);font:600 13px system-ui,sans-serif;padding:4px 10px;border-radius:999px;margin-bottom:12px}}
.cta{{display:inline-block;background:var(--green);color:#fff;text-decoration:none;font:700 16px system-ui,sans-serif;padding:12px 20px;border-radius:8px;margin:8px 8px 0 0}}.cta.alt{{background:var(--card);color:var(--green);border:1px solid var(--green)}}
section{{padding:36px 0}}section+section{{border-top:1px solid var(--line)}}section h2{{font-size:1.5rem}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 24px}}.muted{{color:var(--muted);font-size:.95rem}}
.grid{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}}.k{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}}.k h3{{font-size:1rem;color:var(--green)}}.k p{{margin:0}}
ul.check{{list-style:none;padding:0;margin:0}}ul.check li{{display:flex;gap:12px;padding:8px 0;border-bottom:1px dashed var(--line);align-items:flex-start}}
.box{{flex:0 0 18px;height:18px;border:2px solid var(--green);border-radius:4px;margin-top:5px}}
.bar{{display:flex;gap:3px;height:54px;margin:12px 0 6px}}.seg{{background:var(--green2);border:1px solid var(--green);border-radius:6px;overflow:hidden;position:relative;min-width:6px}}.seg.short span{{display:none}}.seg span{{position:absolute;left:6px;top:4px;font:600 11px/1.2 system-ui,sans-serif;color:var(--green);white-space:nowrap}}
.scale{{display:flex;justify-content:space-between;font:12px system-ui,sans-serif;color:var(--muted)}}
table{{width:100%;border-collapse:collapse;margin-top:16px;font-size:.98rem}}td{{padding:10px 8px;border-top:1px solid var(--line);vertical-align:top}}td.t{{font:600 14px system-ui,sans-serif;color:var(--green);white-space:nowrap}}td.m{{font:13px system-ui,sans-serif;color:var(--muted);white-space:nowrap}}
ol.steps{{list-style:none;padding:0;margin:0;display:grid;gap:14px}}.step{{display:grid;grid-template-columns:48px 1fr;gap:16px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px}}
.badge{{width:44px;height:44px;border-radius:50%;background:var(--green);color:#fff;display:grid;place-items:center;font:700 20px system-ui,sans-serif}}.step h3{{font-size:1.15rem}}.step p{{margin:.3em 0}}.links{{font:14px system-ui,sans-serif}}
.notes{{list-style:none;padding:0;margin:0;columns:2;column-gap:32px;font-size:.98rem}}@media(max-width:720px){{.notes{{columns:1}}}}.notes li{{break-inside:avoid;padding:6px 0;border-bottom:1px dotted var(--line)}}.notes .t{{display:inline-block;width:52px;font:600 13px system-ui,sans-serif;color:var(--green)}}
.people{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}}.person{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}}.person h3{{font-size:1.05rem}}.person h3 a{{color:var(--ink);text-decoration:none}}.person p{{margin:.3em 0}}.q{{font-style:italic;border-left:3px solid var(--green);padding-left:10px}}
.honest{{background:#fff7df;border:1px solid #e8cf7a;border-radius:12px;padding:14px 18px;color:#5a4300}}@media(prefers-color-scheme:dark){{:root:not([data-theme=light]) .honest{{background:#2a2410;border-color:#6b5a1f;color:#f1e3b5}}}}
footer{{color:var(--muted);font:14px system-ui,sans-serif;padding-top:24px;border-top:1px solid var(--line)}}
@media print{{.cta{{display:none}}body{{font-size:13px}}}}
</style></head><body><main>
<header class="hero"><span class="tag">Prompt It Yourself · proposal for Brent, North Lakes</span><h1>Your Shopify store, in one sitting. You keep the keyboard.</h1>
<p>{e(S["tagline"])}</p><a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["guests"])}">Past guests</a></header>

<section><h2>Your list, ticked</h2><div class="card"><p class="muted">From your post. {e(POST["where"])}.</p><ul class="check">{wants}</ul><p class="muted" style="margin-top:12px">{e(POST["unknown"])}</p></div>
<div class="grid" style="margin-top:16px">{know}</div></section>

<section><h2>The offer</h2><div class="card"><ul>{offer}</ul></div></section>

<section><h2>Bring on the day</h2><div class="card"><ul class="check">{hw}</ul></div></section>

<section><h2>How the four hours go</h2><div class="card"><div class="bar">{bar}</div><div class="scale"><span>0:00</span><span>1:00</span><span>2:00</span><span>3:00</span><span>4:00</span></div>
<table>{rows}</table></div></section>

<section><h2>The five steps</h2><ol class="steps">{steps}</ol><p class="honest" style="margin-top:16px">{e(HONEST)}</p></section>

<section><h2>Show notes, written before the show</h2><div class="card"><ol class="notes">{notes}</ol></div></section>

<section><h2>Examples from the show</h2><div class="people">{ex}</div></section>

<section><h2>After the show</h2><div class="card"><ul>{after}</ul></div><p><a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["piy"])}">promptityourself.com</a></p></section>
<footer>Proposal page, 17 October 2026. Shopify prices and limits are from Shopify's Australian pricing page and help centre on that date. <a href="../">Other versions of this page</a>.</footer>
</main></body></html>'''
