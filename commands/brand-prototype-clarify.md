---
description: "Ask up to five targeted questions about prototype behavior, states, flows, and boundaries, then apply the answers directly to the prototype. Does not review fonts, colors, or brand direction."
argument-hint: "Optional: a focused prototype area, such as onboarding, input, or settings"
---

# Brand Prototype Clarify

Settle what the prototype actually does. Ask at most five questions, one at a time, and apply the answers to the prototype.

Do not review typography, color, contrast, copy tone, or brand derivation. Those belong to `speckit-brand-clarify`.

## Language

- Use the language recorded in `brand.md` section 0, "Sources".
- Quote prototype text as written.

## User Input

```text
$ARGUMENTS
```

Optional focus area. If present, scan there first but still check the flows it touches.

## Inputs

1. `prototype/` — read `index.html`, `styles.css`, `app.js`, `README.md`, and `screens/manifest.json` if present.
2. The spec set recorded in `brand.md` section 0, "Sources" — product facts. Read exactly those files; do not resolve specs independently.
   - If `brand.md` or its Sources section is missing, resolve once via `.specify/feature.json` then `specs/*/spec.md`, and report which files were used.
3. `docs/brand/brand.md` — optional. Use it only to check whether product-facing claims match; do not audit brand direction.
4. `docs/brand/tokens.css` — read-only reference for what the prototype should be using.
5. Read-only: never modify any `spec.md`, `brand.md`, `tokens.css`, or logo assets.

## Scan

Look for issues in these categories, ranked by impact × uncertainty:

1. **Dead controls** — clickable, but no handler, no navigation target, no state change.
2. **Same label, different behavior** — or different labels doing the same thing.
3. **Hardcoded demo state** — the selected item does not match what the next screen shows.
4. **Missing states** — loading, empty, error, permission denied, complete, disabled.
5. **Product fact conflicts** — defaults, online/offline behavior, parallelism, persistence, limits that contradict the recorded sources.
6. **Static vs operable boundary** — which screens are illustrations and which controls must actually work.
7. **Navigation, back, interruption** — where back goes, what happens mid-flow, what survives a cancel.
8. **Data and privacy behavior** — what is saved, sent, exported, or cleared.

Skip anything that is purely visual or editorial.

## Questions

Ask at most five, one at a time:

```markdown
**Question:** <one complete question>
Why it matters: <which prototype behavior or review decision it changes>
**Recommended:** Option X — <one-line reason>

| Option | Description |
|---|---|
| A | ... |
| B | ... |
| C | ... |
```

Accept an option letter, "recommended", or a short answer. Do not reveal later questions. If I say "none of these", ask for the constraint and re-ask only that question. If I say stop, stop.

## Applying Answers

After the question loop:

1. Apply each accepted answer to the prototype files with targeted edits.
2. Keep the existing structure and visual system; do not restyle anything.
3. If a fix needs a new visual pattern, use existing tokens and components; if it needs a new token or a brand-level change, stop and recommend `speckit-brand-clarify`.
4. If a fix needs a structural rebuild rather than a local edit, recommend rerunning `speckit-brand-prototype`.
5. Report the files changed and a short table: ID, question, decision, effect.
6. List any unresolved items.

Do not produce a long report. Do not modify `brand.md`, any `spec.md`, `tokens.css`, or logo assets.

## Boundaries

- Behavior, states, flows, and boundaries only.
- No font, color, contrast, copy-tone, or brand-direction review.
- At most five questions per run.
- Never change the brand direction; send those issues to `speckit-brand-clarify`.
- Never fabricate prototype behavior that conflicts with the recorded sources.

## Completion

Report the decisions applied, files changed, unresolved items, and whether another round is useful.
