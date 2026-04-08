# Piki Use Cases Section Spec

## Objective
Create a dedicated `Cas d'usages` page linked from the main navigation, so Piki can explain concrete restaurant situations without overloading the homepage.

The goal is no longer just to improve the current homepage `use_cases` block. The new direction is:
- add a navigation link: `Cas d'usages`
- create a dedicated page focused on real restaurant patterns
- optionally keep a lighter teaser on the homepage later if useful

This page should explain when Piki is useful, for whom, and in which service situations it creates value.

## Why This Change Matters
On the current homepage, the section is understandable but still feature-led. A visitor sees three capabilities, but does not immediately recognize their own business model or workflow.

This new section should help restaurant owners self-identify quickly:
- "This is for my lunch rush"
- "This is for my counter service"
- "This is for my direct delivery strategy"
- "This is for my hybrid setup"

That makes the content more commercial, more concrete, and more useful than a short homepage card row.

## Current State
Current source:
- `content/french/_index.md`
- `layouts/index.html`

Current rendering behavior:
- the template displays one icon, one title, and one paragraph per card
- cards are shown in a simple grid
- current layout is optimized for 3 concise cards

Current content pattern:
- capability name
- short description

Current limitation:
- the cards explain features, not user patterns
- there is no self-qualification signal for different restaurant profiles
- the section overlaps with later homepage blocks like features and how-it-works
- the current homepage format is too short to handle nuanced use-case messaging well

## New Strategic Direction
Move from:
- `what Piki offers`

To:
- `when restaurants use Piki`
- `what service problem it solves`
- `what operational gain they get`

The dedicated page should answer:
- Which restaurant patterns does Piki fit?
- What kind of daily problems does it solve?
- In which situations is Piki relevant?
- What does Piki improve realistically, without overpromising behavior change?

## Key Messaging Correction
The previous framing around pre-order and lunch rush needs to be softened.

Important clarification:
- Piki does not automatically make customers order before the rush
- Piki creates the conditions for earlier or smoother ordering when that behavior already fits the restaurant model
- the message should stay realistic and credible

So instead of saying:
- `Vos clients commandent avant le rush grace a Piki`

Use wording closer to:
- `Piki facilite les commandes en avance quand ce mode est pertinent pour votre clientele`
- `Si une partie de vos clients commande en amont, vous gagnez en visibilite`
- `Piki aide a structurer les flux, sans promettre de changer a lui seul le comportement client`

## Recommended Use Case Families
### 1. Commandes en avance quand cela correspond a votre clientele
Best for:
- lunch-driven restaurants
- office-area restaurants
- fast casual operators
- takeaway-heavy businesses

User pattern:
- some customers know what they want before arriving
- the team benefits from having a bit more visibility before service
- timing and preparation matter more than upsell detail

Business problem:
- the team gets overloaded at peak time
- phone orders and last-minute preparation create stress
- queueing slows down service

Piki value:
- the restaurant can accept pre-orders in a clean and structured way
- if customers use that flow, the team gains earlier visibility
- production can become easier to anticipate for part of the service

### 2. Salle ou comptoir avec attente
Best for:
- coffee shops
- counters
- quick-service restaurants
- dine-in restaurants with recurring queue friction

User pattern:
- customers arrive on site but should not wait to discover the menu or place a basic order
- the staff should spend less time repeating the same ordering flow

Business problem:
- the queue builds up fast
- staff time is consumed by repetitive order taking
- service feels slower than it should

Piki value:
- QR ordering reduces friction
- customers browse, order, and pay faster
- staff can focus more on preparation and service

### 3. Vente directe en livraison
Best for:
- restaurants already using marketplaces
- operators trying to improve margins
- brands wanting direct repeat business
- restaurants with Uber Direct or their own drivers

User pattern:
- delivery already exists or is desired
- the business wants to stop depending entirely on external platforms

Business problem:
- commissions reduce margin
- customer ownership stays with the marketplace
- the brand experience is diluted

Piki value:
- direct delivery orders happen under the restaurant's brand
- the business keeps more control over margins
- customer relationship stays closer to the restaurant

### 4. Etablissements hybrides
Best for:
- businesses mixing takeaway, dine-in, and delivery
- brands with different traffic peaks across the day
- restaurants that do not want separate tools for each flow

User pattern:
- one establishment serves several customer behaviors
- the same team handles more than one service model

Business problem:
- disconnected tools create friction
- the customer experience becomes inconsistent
- staff has to adapt to fragmented workflows

Piki value:
- one storefront supports several order journeys
- the restaurant can activate only the flows it needs
- operations stay simpler and more unified

## Recommended Page Structure
### Navigation
Add a new top-level navigation item:
- `Cas d'usages`

### Page role
This page should work as a self-qualification and conversion-support page.

It should help a restaurant owner think:
- `Piki correspond a mon mode de service`
- `Piki repond a une situation concrete de mon etablissement`

### Recommended page sections
1. Hero
2. Intro explaining the role of the page
3. Use-case blocks grouped by restaurant pattern
4. Optional segment filters or labels
5. Closing CTA

### Recommended block structure per use case
Each use case block should include:
- a recognizable situation title
- a short explanation of the current pain point
- a short explanation of the realistic Piki outcome
- optionally a qualifier such as `ideal pour restauration rapide, coffee shops, restaurants de quartier, dark kitchens`

### Best content formula
For each block:
- `Situation`
- `Probleme`
- `Avec Piki`

### Scanability rules
- keep headings short
- avoid feature jargon
- keep descriptions under 2 to 3 short paragraphs or bullet-sized lines
- make each block self-contained
- use direct restaurant language

## Implementation Options
## Option A: Dedicated content page using an existing layout pattern
Create a new content file such as:
- `content/french/use-cases.md`

And connect it to:
- an existing flexible page layout if one fits
- or a new dedicated layout if needed

### Pros
- clearer editorial space
- no need to compress all use cases into the homepage
- better support for richer descriptions

### Cons
- requires deciding which layout to use
- may still need some template work

## Option B: Dedicated custom page + nav integration
Create:
- `content/french/use-cases.md`
- a dedicated template for use cases if existing layouts are too generic
- a new navigation link in the header

### Pros
- strongest clarity
- best long-term structure
- lets Piki explain use cases without compromise

### Cons
- more implementation work
- requires navigation update and likely template adjustments

## Recommended Direction
For your stated goal, the best direction is Option B:
- a dedicated `Cas d'usages` page
- a link in the main navigation
- realistic situation-based copy

The strongest business direction is:
- keep the content diagnostic
- keep the wording concrete
- map it to restaurant realities, not abstract feature names
- avoid exaggerated causal claims about customer behavior

## Proposed Page Copy Direction
The page should shift from product naming to situation-based wording.

### Recommended use-case titles
1. `Vous acceptez des commandes en avance quand cela a du sens`
2. `Vous servez sur place sans ralentir la file`
3. `Vous developpez votre livraison en direct`
4. `Vous combinez plusieurs modes de commande`

### Example copy style
#### 1. Vous acceptez des commandes en avance quand cela a du sens
Pour les restaurants dont une partie de la clientele aime commander en amont, surtout sur le dejeuner ou la vente a emporter.  
Piki permet de structurer ce flux proprement et de gagner en visibilite lorsque ce comportement existe deja.

#### 2. Vous servez sur place sans ralentir la file
Pour les comptoirs, coffee shops et restaurants avec attente recurrente.  
Le QR code permet a vos clients de consulter, commander et payer plus vite, sans bloquer le service.

#### 3. Vous developpez votre livraison en direct
Pour les restaurants qui veulent vendre en livraison sans laisser leur marge a une marketplace.  
Piki vous aide a garder votre marque, votre relation client et un modele plus previsible.

#### 4. Vous combinez plusieurs modes de commande
Pour les etablissements qui font a la fois vente a emporter, sur place et livraison.  
Une seule boutique vous permet d'activer les parcours adaptes a votre organisation.

## Relationship To The Homepage
The homepage does not need to carry the full use-case story anymore.

Recommended homepage role:
- keep a short summary block if useful
- add a CTA toward the dedicated `Cas d'usages` page
- let the detailed qualification happen on the dedicated page

This keeps the homepage lighter and more credible.

## Relationship To Other Homepage Sections
### Hero
The hero explains the broad promise:
- direct selling
- one storefront
- zero commission

### Cas d'usages
The dedicated page explains:
- where the promise applies in the real world
- which restaurant patterns fit Piki
- which situations benefit most from each flow

### Features
The features section explains:
- what the product enables in detail

### Comparison
The comparison section explains:
- why Piki is economically better than a marketplace

This sequencing makes the site structure clearer.

## Acceptance Criteria
- A restaurant owner can identify at least one use case that matches their business within a few seconds.
- The `Cas d'usages` page feels different from the features page.
- The wording is concrete enough for restaurant operators, not generic SaaS language.
- The page remains easy to scan on mobile.
- The content supports the current site positioning around direct selling and zero commission.
- The copy avoids overstating Piki's impact on customer ordering habits.

## Files Likely Affected
### Minimum scope
- `content/french/use-cases.md`
- navigation configuration or header data source

### Likely scope
- `content/french/use-cases.md`
- navigation configuration or header source
- `layouts/partials/header.html`
- possibly a dedicated layout file if no current template fits

## Suggested Delivery Sequence
1. Decide the content model for the dedicated `Cas d'usages` page.
2. Add the navigation link.
3. Draft final French copy for each use case.
4. Choose whether to reuse an existing layout or create a dedicated one.
5. Validate mobile readability and navigation clarity.

## Recommendation
The best next move is to implement a dedicated `Cas d'usages` page first.

That will:
- remove the pressure to compress nuanced messaging into the homepage
- give room for realistic explanations
- make the navigation clearer for visitors evaluating fit

## Summary
This change is not only a copy refresh.

It changes the role of use-case content from:
- a small homepage feature summary

to:
- a dedicated self-qualification page linked from navigation

That makes the content more useful for conversion, more aligned with restaurant buying behavior, and more credible for Piki's actual value proposition.
