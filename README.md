# fb-brent-robertson

One page for one [Prompt It Yourself](https://promptityourself.com/) session: a small-business
Shopify store for a guest in North Lakes, Brisbane, built live on his own laptop by an AI agent.

Live: https://fb-brent-robertson.promptityourself.com/

## What is in it

- `site/index.html` — the page. Plain HTML and CSS, no build step.
- `site/designs/{market,studio,bold}/` — three clickable storefront directions for a store whose product
  we do not know yet. Placeholder blocks where photos go, no fake products.
- `site/media/` — screenshots of three live sites our guests own (deoblock.com, vipaccountingau.com,
  dokabernadett.com) and of the three directions, taken with headless Chromium on 17 October 2026.
  Nothing on the page is AI-generated imagery.
- `og/card.html` — the source of the OG image. Rendered by headless Chromium at 1200×630 into
  `site/media/og.png`; the show's fonts, logo and colours, drawn by code.
- `site/fonts/` — Bebas Neue, the show's title face, self-hosted as the site does.
- Logo, lockup, colours and the episode cards are the show's own, loaded from
  [promptityourself.com/media](https://promptityourself.com/media/).

## Deploy

Static assets on a Cloudflare Worker, custom domain in `wrangler.jsonc`:

```sh
CLOUDFLARE_ACCOUNT_ID=ef7d622089ca4480c9f6fbf368f66787 npx wrangler deploy   # token: CLOUDFLARE_API_TOKEN in the env
```

## What is and is not claimed

Every episode moment on the page comes from that episode's page on promptityourself.com, and links to
it. Nobody on the show has built a Shopify store yet; the page says so. deoblock.com is the one Shopify
store among the three sites, and the page says which.
