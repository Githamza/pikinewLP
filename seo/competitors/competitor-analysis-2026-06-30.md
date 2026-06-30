# Competitor Analysis — Piki

_Date: 2026-06-30 · Market: France (loc 2250) / French_
_Source: OpenSEO `get_domain_overview`, `get_ranked_keywords` (US-locale sample), France SERP data._
_Caveats: `get_ranked_keywords`/`find_serp_competitors` are US-market-only in this deployment; Backlinks API disabled (ref-domain counts read from SERP elements). `piki-app.fr` has no organic data yet (hasData:false)._

## Footprint comparison

| Domain | Organic traffic/mo | Organic keywords | Ref. domains (homepage) | Model |
| --- | ---: | ---: | ---: | --- |
| tastycloud.fr | ~41,535 | 3,265 | ~3 | Platform SEO — hosted client menu pages |
| click-eat.fr | ~1,270 | 77 | ~44 | Product pages + brand, demo-led |
| piki-app.fr | — (no data) | — | — | New, starting from zero |

---

## click-eat.fr

- **Snapshot:** small, focused footprint (1,270 visits / 77 kw). ~44 referring domains, 333 backlinks. Domain rank 255.
- **Positioning:** "La meilleure solution de commande en ligne… click and collect, livraison ou borne, 2000+ restaurants, tout-en-un." **Demo-led** ("Demander une démo").
- **SERP wins (FR):** #1 `commande en ligne restaurant`, #1 `click and collect restaurant` — both on product pages (`/commande-en-ligne`, `/click-and-collect`).
- **Lesson:** ranks #1 on age/brand trust + tight product pages, not scale or links — beatable.
- **Vulnerabilities:** almost no informational/blog footprint; demo-gated funnel (vs Piki free trial); modest authority.

## tastycloud.fr — the important one

- **Snapshot:** ~41,535 visits / 3,265 kw but only ~3 referring domains. **Huge traffic, tiny authority.**
- **Positioning:** "Click and collect **sans commission**" + "Essayez gratuitement" — nearly identical to Piki.
- **The moat:** footprint is driven by **hosted client menu pages** indexed by Google. Ranked URLs are per-restaurant pages (`/{hash}/menu/0`, `/ozzy-pizzeria-/59/menu`) ranking for branded queries ("o'tacos menu", "nonno and nonna", "menu hotel ibis"). Every onboarded restaurant = new indexed pages → SEO compounds with client growth.
- **Lesson:** the scale comes from **platform-generated pages, not content or links**.
- **Vulnerabilities:** negligible backlink profile; thin marketing content; "sans commission" slogan is not differentiated (Piki, Collectly, Delicity all use it).

## Strategic takeaways for Piki

1. **Build the indexed-client-page mechanism (highest leverage).** Make each restaurant's Piki ordering/menu page publicly indexable, clean URL, restaurant name in title/H1, Menu/Restaurant schema, internally linked. This is how tastycloud reached 41k visits — it compounds with every signup and directly serves the trial-signup goal.
2. **Contest the B2B SERP** with a dedicated Click & Collect landing page — both rivals rank with beatable pages and the same slogan.
3. **Press the content advantage** — commission-pain (blog-2) and "logiciels restaurant" guide (Cluster 6) are uncontested by both.
4. **Invest in links early** — neither rival defends authority (3–44 ref. domains); modest PR/roundup placements would leapfrog them.

### What NOT to copy
- Don't rely on "sans commission" as differentiation — table stakes now. Differentiate on execution + free trial + content + indexed client pages.
- Don't manually chase branded-restaurant long-tail — it only works as a byproduct of hosting client pages.

### Suggested next OpenSEO work
- `competitive-landscape` to confirm the full leader set (Collectly, Delicity, Sunday, Innovorder, Zelty).
- `link-prospecting` for restaurant-tech roundups + local press (closes the authority gap).
- Re-run with `piki-app.fr` mapped + GSC connected for a true keyword-gap diff.
