# fb-brent-robertson

A proposal page for one [Prompt It Yourself](https://promptityourself.com/) session: a small-business
Shopify store for a guest in North Lakes, Brisbane, built live on his own laptop.

Live: https://fb-brent-robertson.promptityourself.com/

Three versions of the same proposal, same facts and plan, three designs:

- `/v1/` Run sheet. Dark, timecoded, the session as a broadcast run sheet.
- `/v2/` Checklist. Light, printable, five numbered cards and a time bar.
- `/v3/` Storyboard. Poster style, the session as a horizontal storyboard.

## How it is built

- `build/content.py` holds every word on the pages: the brief, the offer, the run sheet, the five
  Shopify steps with the official help-centre link each rests on, the planned show notes, and the
  guest examples (quotes verbatim from promptityourself.com).
- `build/templates/v1.py`, `v2.py`, `v3.py` are the three designs; `index.py` is the chooser.
- `python3 build/render.py` writes `site/`. No dependencies beyond Python 3.

## Deploy

Static assets on a Cloudflare Worker, custom domain in `wrangler.jsonc`:

```sh
python3 build/render.py
CLOUDFLARE_ACCOUNT_ID=ef7d622089ca4480c9f6fbf368f66787 npx wrangler deploy   # token: CLOUDFLARE_API_TOKEN in the env
```

## What is and is not claimed

Shopify prices and limits were read from Shopify's Australian pricing page and help centre on
17 October 2026 and are linked from each step. Nobody on the show has built a Shopify store yet;
the pages say so.
