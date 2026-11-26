---
description: "Derive a visual board and initial logo/VI from brand.md, design the product prototype from that visual standard, and assemble one combined page for a single review."
argument-hint: "Optional: screens or flows to include, copy source, canvas size, or whether to include the initial logo/VI"
---

# Brand Prototype

Turn `docs/brand/brand.md` into a visual standard and a working product prototype, delivered as **one page**: project brief and visual board on top, prototype screens below.

Order matters: derive the visual board first, design the prototype from it, then review the whole thing once.

## Language

- Use the language of `brand.md` and `spec.md` for all copy, labels, questions, and the page.
- Use the product's real language for interface copy; do not translate product names.

## User Input

```text
$ARGUMENTS
```

Optional: scope, copy source, canvas, or "no logo/VI". Fold it in and skip the matching setup question.

## Prerequisites

- `docs/brand/brand.md` exists and has sections 2–8. If it is missing or incomplete, tell me to run `speckit-brand-create` first and stop.
- `spec.md` exists. Locate it via `.specify/feature.json`, then the newest `specs/*/spec.md`.
- Read `brand.md` and `spec.md`; never modify either.

## Existing Work

Check:

- `prototype/index.html`, `prototype/styles.css`, `prototype/app.js`
- `docs/brand/tokens.css`
- `docs/brand/assets/logo/`
- `docs/brand/assets/app-icon.svg`

If any exist, ask whether to **extend**, **rebuild**, or **keep** each part. Never overwrite without an answer. If logo assets already exist, reuse them and only add missing variants and rules; do not redesign an existing logo.

## Setup Questions

Ask at most three groups in one screen, then continue:

1. **Scope** — propose the flows and screens derived from `spec.md` (for example: onboarding, core task, result, settings). Ask me to confirm, cut, or add.
2. **Content and canvas** — real copy from `spec.md`, or clearly marked placeholder copy; canvas size (mobile 390×844, web 1440×900, or as the product requires).
3. **Initial logo/VI** — include a first version of the logo and basic VI? Default yes. If an existing logo is found, say so and ask whether to keep it. Accept "no" and skip the logo/VI part of the visual board, while still producing colors, type, spacing, and components.

## Phase A: Visual Standard

### A1. Tokens

Derive from `brand.md` section 6 and write `docs/brand/tokens.css`:

- **Color**: one primary, 2–3 neutrals, one accent. Use hex here, nowhere in `brand.md`. Check text contrast at AA or better.
- **Type**: open-source, embeddable families; heading and body roles; a Latin pairing if needed; a type scale with line heights. Minimum 14px for mobile body text.
- **Spacing and shape**: a 4/8 spacing scale, corner radii, minimal shadow use.
- **Variables**: expose everything as CSS custom properties under `:root`.

Do not scatter hardcoded colors through the prototype; use the tokens.

### A2. Initial logo

Unless the user said no:

- **Wordmark**: horizontal and stacked lockups, Chinese and Latin pairing. Use an open-source font; note that the file depends on that font, or convert to outlines if font tooling is available.
- **Mark**: one simple geometric form derived from a concrete brand image (for example: a single dot, a line, a frame). No complex illustration, no generated raster art.
- **Variants**: full color, mono, inverse.
- **App icon**: the mark on a brand background.
- Save editable SVG files:
  - `docs/brand/assets/logo/logo-horizontal.svg`
  - `docs/brand/assets/logo/logo-stacked.svg`
  - `docs/brand/assets/logo/mark.svg`
  - `docs/brand/assets/logo/logo-mono.svg`
  - `docs/brand/assets/logo/logo-inverse.svg`
  - `docs/brand/assets/app-icon.svg`

Produce one recommended direction, not multiple competing concepts. Revise it from my feedback later.

### A3. Basic VI rules

Render these in the board, not as a separate document:

- Clear space around the logo
- Minimum size
- Allowed and forbidden backgrounds
- Don'ts: stretch, recolor, add effects, low contrast
- 2–3 applications suited to the product type: for example app icon, splash screen, social avatar; for physical products, packaging or card

Add this line visibly on the board: "Initial draft, not trademark-cleared. Run a professional trademark search before use."

### A4. Component basics

Define and render the shared component styles the prototype will use:

- Buttons: primary, secondary, quiet
- Inputs and form controls
- Cards and surfaces
- Toggles, chips, and selection controls
- Navigation and headers
- Empty, loading, and error states

Keep the set small. Every component must be traceable to `brand.md`; do not add a component the product does not use.

## Phase B: Product Prototype

Design the confirmed screens from the visual standard:

- Use `tokens.css` for color, type, spacing, and radii.
- Build with plain HTML/CSS/JS. No build step.
- Make interactions real where they matter: navigation, tabs, toggles, steppers, sheets, state changes. No clickable controls that do nothing.
- Cover meaningful states: loading, empty, error, disabled, complete. If a state is out of scope, mark it as out of scope.
- Use real copy from `spec.md`; mark placeholders clearly.
- Accessibility: visible focus, labels, keyboard operation for interactive controls, sufficient contrast.
- The board should read as one system: consistent spacing, one accent use per screen, no decorative noise.

Files:

- `prototype/index.html`
- `prototype/styles.css` — import `../docs/brand/tokens.css` at the top
- `prototype/app.js`
- `prototype/README.md` — how to open, screen list, interactions, links to `../docs/brand/brand.md` and `tokens.css`

## Composite Page

`prototype/index.html` contains, in order:

1. **Project brief** — one paragraph plus key facts, from `brand.md` section 1
2. **Visual board** — logo and VI, color, type, spacing, component basics, imagery, dos and don'ts
3. **Prototype** — screens grouped by flow, with a simple navigation

This is the single deliverable. Do not split the visual board into a separate file. Reference brand assets with relative paths from `prototype/index.html`, for example `../docs/brand/assets/logo/logo-horizontal.svg`.

## Single Review

When the page is assembled:

1. Tell me where to open it and what changed.
2. Ask for feedback on the **whole page**, prototype and visual board together.
3. Apply the feedback to both. If a token changes, update every usage and the board.
4. Repeat until I accept it.

Do not ask for separate approval of the visual board and the prototype. Do not silently change the brand direction; if the feedback is about direction rather than execution, stop and recommend `speckit-brand-clarify`.

## Quality Bar

- One visual system, traceable to `brand.md`; no section may invent a second style.
- Real content, clear hierarchy, honest empty and error states.
- No generic template look: no default gradient hero, no emoji-as-icon, no decorative cards with no job.
- Every screen should be explainable in one sentence by the audience it serves.

## Boundaries

- Never modify `brand.md` or `spec.md`.
- Write only `docs/brand/tokens.css`, `docs/brand/assets/`, and `prototype/`.
- No raster or AI-generated logo art; no trademark clearance; no print files, CMYK, bleed, or packaging production files.
- No full VI manual; this is an initial board, not a delivered identity system.
- Do not build production application code beyond the static prototype.
- Do not claim the logo is trademark-cleared.

## Completion

Report:

- Files created or changed
- Screen and flow list
- Logo variants and applications included
- What is placeholder or out of scope
- The reminder that the logo is an initial draft, not trademark-cleared
- The next step: `speckit-brand-prototype-clarify` for behavior and states
