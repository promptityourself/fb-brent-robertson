# fb-brent-robertson

One page for one [Prompt It Yourself](https://promptityourself.com/) session: a small-business
Shopify store for a guest in North Lakes, Brisbane, built live on his own laptop by an AI agent.

Live: https://fb-brent-robertson.promptityourself.com/

## What is in it

- `site/index.html` — the page. Plain HTML and CSS, no build step.
- `site/media/` — three images made with the agent through Replicate (`google/nano-banana-2`,
  16:9, prompted for the show's look: near-black, one red, no text). The prompts are in `media/PROMPTS.md`.
- `site/fonts/` — Bebas Neue, the show's title face, self-hosted as the site does.
- Logo, lockup and colours are the show's own, used from
  [promptityourself.com/media](https://promptityourself.com/media/).

## Deploy

Static assets on a Cloudflare Worker, custom domain in `wrangler.jsonc`:

```sh
CLOUDFLARE_ACCOUNT_ID=ef7d622089ca4480c9f6fbf368f66787 npx wrangler deploy   # token: CLOUDFLARE_API_TOKEN in the env
```

## What is and is not claimed

The chapters under "What usually happens" are patterns from past episodes, not a plan. Nobody on the
show has built a Shopify store yet; the page says so. Guest quotes are verbatim from their pages on
promptityourself.com.
