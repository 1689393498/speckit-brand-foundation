---
description: "Identify underspecified or contradictory areas in docs/brand/brand.md, ask up to five targeted questions, and apply the answers back into the document."
argument-hint: "Optional: areas to focus on, such as audience, positioning, naming, slogan, or visual direction"
---

# Brand Clarify

Remove ambiguity from `docs/brand/brand.md` by asking the smallest useful set of questions and encoding the answers back into the document. This mirrors `/speckit-clarify`, but for brand direction.

## Language

- Use the language of `brand.md` and `spec.md` for questions, tables, and edits.
- Quote existing document text as written.

## User Input

```text
$ARGUMENTS
```

Optional focus areas. If present, prioritize them; still scan the whole document for contradictions.

## Inputs

1. `docs/brand/brand.md` — required. If missing, tell me to run `speckit-brand-create` first and stop.
2. `spec.md` — for product facts and scope. Locate it via `.specify/feature.json`, then the newest `specs/*/spec.md`.
3. Optional, if they exist:
   - `docs/brand/tokens.css`
   - `docs/brand/assets/logo/`
   - `prototype/index.html`
   Use them only to check whether the brand direction is being followed. Do not edit them.

## Scan

Mark each area **Clear / Partial / Missing**, then pick the highest impact × uncertainty:

1. **Audience specificity** — are profiles concrete enough to make decisions from, or still labels?
2. **Positioning vs spec** — does the one-line positioning contradict `spec.md`, promise something the product does not do, or add scope?
3. **Naming** — is the name settled? Is pronunciation, meaning, or cross-language risk unresolved? Does the name still match the audience and anchor?
4. **Slogan vs core** — does the slogan promise something the brand core refuses, or use tone the language direction bans?
5. **Visual direction traceability** — can each image, color tendency, and type choice be traced to the brand core? Are exclusions explicit?
6. **Language direction** — are tone, taboos, story, and product copy consistent with each other?
7. **Execution principles** — are the bottom lines testable, or vague virtues?
8. **Missing decisions** — markets, bilingual naming, sub-brands, future category expansion, or other decisions left unstated.

Do not pad the list. If an area is already clear, leave it alone.

## Questions

Ask at most five, one at a time. For each:

- State the question in one sentence.
- Say in one line why it matters and which section it will change.
- Offer 2–5 options with a short description.
- Recommend one option first, with a one-line reason.
- Accept an option letter, "recommended", or a short free-text answer.

Do not reveal later questions in advance. If I say it does not matter, record that and move on. If I say stop, stop immediately.

## Applying Answers

After all answers are collected:

1. Edit the relevant sections of `brand.md`. Keep the existing structure and language.
2. Do not soften or rewrite sections that were not part of the answers.
3. Add one row per decision to the decision log: date, area, question, decision.
4. Show a short change table: area, what changed, which section.
5. Do not produce a long report.

## Consistency Check (optional)

If `tokens.css`, logo assets, or `prototype/index.html` exist, check whether they still match `brand.md`:

- Colors and type: do they follow the stated direction?
- Logo: does it use the stated imagery and wordmark direction?
- Prototype: does its visual language match the brand core?

Report mismatches as observations. Do not edit the prototype, tokens, or logo. Recommend the fix path:

- Direction is wrong → edit `brand.md` here, then rerun `speckit-brand-prototype`
- Execution drifted → rerun `speckit-brand-prototype` or fix the prototype in `speckit-brand-prototype-clarify`

## Boundaries

- Never modify `spec.md`.
- Never edit `tokens.css`, logo assets, or `prototype/`; this command only touches `brand.md`.
- At most five questions per run.
- No long report, no invented answers, no self-answered questions.
- If there is no critical ambiguity, say so plainly and stop.

## Completion

Report the decisions recorded, the sections changed, any mismatches found, and whether another round is useful.
