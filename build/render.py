#!/usr/bin/env python3
"""Render site/ from content.py and the three templates. Run: python3 build/render.py"""
import html, importlib.util, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT.parent / "site"
spec = importlib.util.spec_from_file_location("content", ROOT / "content.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

e = html.escape

def link(t):  # ("label", "url") -> <a>
    return f'<a href="{e(t[1])}" rel="noopener">{e(t[0])}</a>' if t else ""

def ctx():
    """Pre-rendered HTML fragments every template can drop in."""
    return {
        "S": C.SITE, "POST": C.POST, "KNOW": C.KNOW, "OFFER": C.OFFER, "HOMEWORK": C.HOMEWORK,
        "RUNSHEET": C.RUNSHEET, "STEPS": C.STEPS, "SHOWNOTES": C.SHOWNOTES, "EXAMPLES": C.EXAMPLES,
        "HONEST": C.HONEST, "AFTER": C.AFTER, "e": e, "link": link,
    }

def main():
    OUT.mkdir(exist_ok=True)
    versions = sorted(p for p in (ROOT / "templates").glob("v*.py"))
    index_cards = []
    for tpl in versions:
        name = tpl.stem
        spec = importlib.util.spec_from_file_location(name, tpl)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        d = OUT / name; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(m.render(**ctx()), encoding="utf-8")
        index_cards.append((name, m.TITLE, m.BLURB))
        print("wrote", d / "index.html")
    spec = importlib.util.spec_from_file_location("index", ROOT / "templates" / "index.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    (OUT / "index.html").write_text(m.render(index_cards, **ctx()), encoding="utf-8")
    print("wrote", OUT / "index.html")

if __name__ == "__main__":
    sys.exit(main())
