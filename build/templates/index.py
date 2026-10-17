def render(cards, S, e, **_):
    items = "".join(
        f'<li><a href="{e(n)}/"><span class="n">{e(n).upper()}</span><b>{e(t)}</b><p>{e(b)}</p></a></li>' for n, t, b in cards)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(S["title"])}</title><meta name="description" content="{e(S["tagline"])}">
<style>
:root{{--bg:#f6f4ef;--fg:#1d1d1b;--muted:#5b5a55;--card:#fff;--line:#d9d5cc;--accent:#0a6b4f}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#15161a;--fg:#ebe9e3;--muted:#a4a29a;--card:#1f2127;--line:#33363e;--accent:#3fbf93}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:860px;margin:0 auto;padding:48px 16px 64px}}h1{{font-size:clamp(1.8rem,5vw,2.6rem);line-height:1.1;margin:0 0 8px}}.sub{{color:var(--muted);margin:0 0 28px;max-width:60ch}}
ul{{list-style:none;padding:0;margin:0;display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}}
li a{{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px;color:inherit;text-decoration:none;height:100%}}li a:hover{{border-color:var(--accent)}}
.n{{display:block;font:700 12px/1 system-ui,sans-serif;letter-spacing:.14em;color:var(--accent);margin-bottom:10px}}li b{{font-size:1.15rem}}li p{{color:var(--muted);margin:6px 0 0;font-size:.95rem}}
footer{{margin-top:36px;color:var(--muted);font-size:.9rem}}a{{color:var(--accent)}}
</style></head><body><main>
<h1>{e(S["title"])}</h1><p class="sub">{e(S["tagline"])} Three versions of the same proposal. Same facts, same plan, three designs.</p>
<ul>{items}</ul>
<footer>A <a href="{e(S["piy"])}">Prompt It Yourself</a> proposal page. Source: <a href="https://github.com/promptityourself/fb-brent-robertson">github.com/promptityourself/fb-brent-robertson</a>.</footer>
</main></body></html>'''
