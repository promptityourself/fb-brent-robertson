TITLE = "Storyboard"
BLURB = "Poster style. Big type, the session as a horizontal storyboard, an episode card at the top."

def render(S, POST, KNOW, OFFER, HOMEWORK, RUNSHEET, STEPS, SHOWNOTES, EXAMPLES, HONEST, AFTER, e, link):
    frames = "".join(
        f'<li class="frame"><div class="fc"><time>{e(t)}</time><span class="dur">{m} min</span></div><h3>{e(n)}</h3><p>{e(d)}</p></li>'
        for t, m, n, d in RUNSHEET)
    steps = "".join(
        f'<article class="step"><div class="big">{s["n"]}</div><h3>{e(s["name"])}</h3><p>{e(s["what"])}</p>'
        f'<p class="muted">{e(s["detail"])}</p><p class="links">{link(s["link"])}{" · " + link(s["link2"]) if s["link2"] else ""}</p></article>'
        for s in STEPS)
    notes = "".join(f'<li><time>{e(t)}</time><span>{e(n)}</span></li>' for t, n in SHOWNOTES)
    ex = "".join(
        f'<article class="guest"><h3><a href="{e(x["url"])}" rel="noopener">{e(x["name"])}</a></h3><p class="muted">{e(x["role"])}</p><p>{e(x["why"])}</p>'
        + (f'<blockquote>{e(x["quote"])}</blockquote>' if x["quote"] else "")
        + (f'<p class="links">{link(x["episode"])}</p>' if x["episode"] else "") + '</article>' for x in EXAMPLES)
    know = "".join(f'<div class="k"><h3>{e(k)}</h3><p>{e(v)}</p></div>' for k, v in KNOW)
    offer = "".join(f'<div class="o"><h3>{e(k)}</h3><p>{e(v)}</p></div>' for k, v in OFFER)
    hw = "".join(f'<li><b>{e(k)}</b><span>{e(v)}</span></li>' for k, v in HOMEWORK)
    wants = "".join(f'<li>{e(w)}</li>' for w in POST["wants"])
    after = "".join(f'<div class="o"><h3>{e(k)}</h3><p>{e(v)}</p></div>' for k, v in AFTER)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(S["title"])} · Storyboard</title>
<meta name="description" content="{e(S["tagline"])}">
<style>
:root{{--bg:#f3efe6;--fg:#141414;--muted:#6a675f;--line:#d6d0c2;--card:#fffdf8;--ink:#141414;--pop:#2b4cff;--pop2:#ffd23f}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#121214;--fg:#efece4;--muted:#a09c92;--line:#2d2d33;--card:#1a1a1f;--ink:#fff;--pop:#7a8dff;--pop2:#ffd23f}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:0 16px 80px}}a{{color:var(--pop)}}h1,h2,h3{{line-height:1.05;margin:0 0 .4em;color:var(--ink);letter-spacing:-.02em}}
.ep{{margin:24px 0 0;background:var(--ink);color:#fff;border-radius:16px;padding:28px;display:grid;grid-template-columns:1fr auto;gap:16px;align-items:end}}
.ep .l{{font:600 12px/1 system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--pop2)}}.ep h1{{color:#fff;font-size:clamp(2rem,7vw,4.2rem);margin:.2em 0}}
.ep p{{margin:0;color:#d9d6cd;max-width:60ch}}.ep .meta{{font:600 14px system-ui,sans-serif;color:var(--pop2);text-align:right;white-space:nowrap}}
@media(max-width:720px){{.ep{{grid-template-columns:1fr}}.ep .meta{{text-align:left}}}}
.cta{{display:inline-block;background:var(--pop);color:#fff;text-decoration:none;font-weight:800;padding:14px 22px;border-radius:999px;margin:16px 10px 0 0}}.cta.alt{{background:var(--pop2);color:#141414}}
section{{padding:48px 0 8px}}section h2{{font-size:clamp(1.6rem,4vw,2.4rem)}}section h2 small{{display:block;font:700 12px system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--pop);margin-bottom:8px}}
.muted{{color:var(--muted);font-size:.95rem}}.links{{font-size:.92rem}}
.ask{{display:grid;gap:16px;grid-template-columns:1.2fr 1fr}}@media(max-width:720px){{.ask{{grid-template-columns:1fr}}}}
.pane{{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:20px}}.pane ul{{margin:0;padding-left:20px}}.pane li{{margin:4px 0}}
.grid3{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}.k,.o{{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:18px}}.k h3,.o h3{{font-size:1.05rem;color:var(--pop)}}.k p,.o p{{margin:0}}
.hw{{list-style:none;margin:0;padding:0;display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}.hw li{{background:var(--pop2);color:#141414;border-radius:12px;padding:14px 16px;display:grid;gap:4px}}.hw b{{font-size:1.02rem}}.hw span{{font-size:.92rem;color:#3a3a2a}}
.board{{list-style:none;margin:0;padding:8px 0 20px;display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;counter-reset:f}}
.frame{{flex:0 0 272px;scroll-snap-align:start;background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:16px;box-shadow:6px 6px 0 var(--pop)}}.frame h3{{font-size:1.15rem}}.frame p{{margin:0;font-size:.95rem}}
.fc{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}}.fc time{{font-weight:800;font-size:1.5rem;color:var(--pop)}}.dur{{font:700 12px system-ui,sans-serif;background:var(--pop2);color:#141414;padding:2px 8px;border-radius:999px}}
.hint{{font-size:.9rem;color:var(--muted);margin:0 0 8px}}
.steps{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.step{{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:20px;position:relative;overflow:hidden}}.big{{position:absolute;right:-6px;top:-18px;font-size:7rem;font-weight:900;color:var(--pop2);line-height:1;opacity:.9;z-index:0}}.step h3,.step p{{position:relative;z-index:1}}.step h3{{font-size:1.2rem;padding-right:70px}}.step p{{margin:.3em 0}}
.notes{{list-style:none;margin:0;padding:0;display:grid;gap:8px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}.notes li{{display:grid;grid-template-columns:56px 1fr;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.95rem}}.notes time{{font-weight:800;color:var(--pop)}}
.guests{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}.guest{{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:18px}}.guest h3{{font-size:1.1rem}}.guest h3 a{{color:var(--ink);text-decoration:none}}.guest p{{margin:.3em 0}}
blockquote{{margin:10px 0 0;font-style:italic;font-size:1.05rem;color:var(--ink)}}blockquote::before{{content:"“";color:var(--pop);font-size:1.6rem;line-height:0;margin-right:4px}}
.honest{{background:var(--pop2);color:#141414;border-radius:14px;padding:16px 20px;font-weight:600;margin-top:16px}}
footer{{color:var(--muted);font-size:.9rem;padding-top:32px;margin-top:40px;border-top:1px solid var(--line)}}
</style></head><body><main>
<header class="ep"><div><div class="l">Prompt It Yourself · a session proposed for</div><h1>Brent's shop. Live. His hands.</h1><p>{e(S["tagline"])}</p>
<a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["guests"])}">Who has done it</a></div><div class="meta">with Brent · North Lakes<br>up to 4h, live + uncut<br>free</div></header>

<section><h2><small>The ask</small>Your post, answered</h2><div class="ask">
<div class="pane"><p class="muted">{e(POST["where"])}. You wrote that you want:</p><ul>{wants}</ul></div>
<div class="pane"><p class="muted">You already have:</p><ul>{"".join(f"<li>{e(h)}</li>" for h in POST["has"])}</ul><p class="muted" style="margin-bottom:0">{e(POST["unknown"])}</p></div></div>
<div class="grid3" style="margin-top:14px">{know}</div></section>

<section><h2><small>The offer</small>What a session is</h2><div class="grid3">{offer}</div></section>

<section><h2><small>Before</small>Bring these</h2><ul class="hw">{hw}</ul></section>

<section><h2><small>The storyboard</small>Four hours, frame by frame</h2><p class="hint">Scroll sideways.</p><ol class="board">{frames}</ol></section>

<section><h2><small>The method</small>Five steps. All of them Shopify's own.</h2><div class="steps">{steps}</div><p class="honest">{e(HONEST)}</p></section>

<section><h2><small>Show notes</small>Chapters, written before we start</h2><ol class="notes">{notes}</ol></section>

<section><h2><small>Examples</small>Guests who came with a real problem</h2><div class="guests">{ex}</div></section>

<section><h2><small>After</small>Then what</h2><div class="grid3">{after}</div><p><a class="cta" href="{e(S["show"])}">Apply to be a guest</a><a class="cta alt" href="{e(S["piy"])}">promptityourself.com</a></p></section>
<footer>Proposal page, 17 October 2026. Shopify prices and limits are from Shopify's Australian pricing page and help centre on that date. <a href="../">Other versions of this page</a>.</footer>
</main></body></html>'''
