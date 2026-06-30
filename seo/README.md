# Piki — SEO Workspace

Durable workspace for SEO work on **Piki**. Agents and humans save notes, exports, keyword
lists, briefs, and reports here so context builds over time instead of starting from a blank
conversation each session.

_Last updated: 2026-06-29_

## Site scope

- **Primary domain:** https://www.piki-app.fr/
- **Language / market:** French only (`fr-fr`, France). English content exists in the repo but is
  disabled in Hugo config (`disableLanguages = ["en"]`).
- **Platform:** Hugo static site (`saasis-hugo` theme), deployed via Netlify.
- **App / signup URL:** https://piki-app.com/admin/register
- **Contact:** contact@piki-app.fr

### Key pages (French money pages)

- `/features/` — Fonctionnalités
- `/how-it-works/` — Comment ça marche
- `/use-cases/` — Cas d'usages
- `/pricing/` — Tarif
- `/faq/` — FAQ
- `/contact/` — Contact
- `/blog/` — 11 published posts (see Content inventory)

## What Piki is

Piki is an **online-ordering platform for restaurants with 0% commission**. Core offering:

- **Click & Collect** / pre-order (pré-commande), especially to boost the lunch service
- **On-site ordering via QR code** (menu digital)
- **Delivery** (livraison)
- 14-day free trial, no commission on sales

### Positioning angle

The differentiator is **0% commission** vs. marketplace aggregators (Uber Eats, Deliveroo, etc.)
that charge high commissions. Messaging targets independent restaurant owners who want to own
their customer relationship and margins.

## Goals

- **Primary goal:** Drive **free-trial signups** from restaurant owners.
- **Focus:** Non-branded, buying-intent ("bottom of funnel") French terms — e.g.
  _logiciel de commande en ligne restaurant_, _solution click & collect restaurant_,
  _menu QR code restaurant_, _commande en ligne sans commission_.
- **Secondary:** Top-of-funnel educational blog traffic that can be funneled toward trial.

## Positioning & audience notes

- **Audience:** Independent restaurant owners / small chains in France.
- **Pain solved:** High commissions from delivery marketplaces; lack of a direct ordering channel;
  inefficient lunch service.
- **Why choose Piki:** 0% commission, owns the customer relationship, all-in-one (collect + on-site
  QR + delivery).
- _Competitors / substitutes: TBD — run `competitive-landscape` or `competitor-analysis`._
- _Topics to avoid / strong claims: TBD with owner._

## Data & integrations status

- **OpenSEO MCP:** Connected (self-hosted mode). Only one project ("Default") exists and it has
  **no domain mapped** — live tools (rank tracker, ranked keywords, Search Console) are not yet
  pointed at piki-app.fr.
  - **Action needed:** In the OpenSEO UI (http://localhost:3001/), map `piki-app.fr` to a project
    and connect Google Search Console.
- **Google Search Console:** Not connected via OpenSEO yet. A `gsc_auth.py` script exists in the
  repo root (OAuth + data fetch, `webmasters.readonly` scope) as a fallback export path.
  - Drop CSV exports into `gsc/` using names like `queries-last-3-months.csv`,
    `pages-last-3-months.csv`, `queries-last-16-months.csv`, `pages-last-16-months.csv`.

## Content inventory (French blog, 11 posts)

| File | Topic | Slug |
| --- | --- | --- |
| blog-1 | Commande en ligne transforme la restauration en 2026 | commande-en-ligne-restaurant-2026 |
| blog-2 | 0% de commission — pourquoi c'est important | commission-zero-livraison-restaurant |
| blog-3 | QR code au restaurant / menu digital | qr-code-restaurant-menu-digital |
| blog-4 | Pré-commande — boostez le service du midi | pre-commande-restaurant-service-midi |
| blog-5 | 5 erreurs à éviter (lancer la commande en ligne) | erreurs-commande-en-ligne-restaurant |
| blog-6 | Fidéliser vos clients grâce au digital | fideliser-clients-restaurant-digital |
| blog-7 | Livraison vs click & collect | livraison-vs-click-and-collect-restaurant |
| blog-8 | Créer un menu digital attractif | creer-menu-digital-restaurant-attractif |
| blog-9 | Rappel listeria plats préparés (actualité) | rappel-listeria-plats-prepares-restaurateurs |
| blog-10 | Titres-restaurant le dimanche | titres-restaurant-dimanche-restaurateurs |
| blog-11 | Fidélité client restaurant — le guide | fidelite-client-restaurant-guide |

## How the agent should work on this project

- Output and target keywords are **in French**, for the **France** market.
- Prioritize buying-intent terms that map to trial signups; keep blog topics funnel-aware.
- Distinguish source evidence from inference; don't claim GSC is connected unless a live tool
  confirms it.
- Save keyword lists to `keywords/`, competitor findings to `competitors/`, content briefs to
  `content/`, and reports to `reports/`.

## Recommended next workflow

`keyword-research` — seed from the buying-intent themes above to find trial-driving terms, then
`keyword-clustering` to map them onto the existing money pages and blog posts.
