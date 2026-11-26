---
description: "Run the full brand workflow from the project's specs end to end: brand.md, name screening, brand clarification, then a combined prototype and visual identity page. Stops at every human decision."
argument-hint: "Optional: brand background, preferences, tones to avoid, or the stage to resume from"
---

# Brand — Full Workflow

Run the complete brand workflow in order. This command orchestrates five stage commands and never skips one:

1. `speckit-brand-create` — build `docs/brand/brand.md`
2. `speckit-brand-name-check` — screen shortlisted names (also called by create)
3. `speckit-brand-clarify` — remove ambiguity in `brand.md`
4. `speckit-brand-prototype` — visual board + initial logo/VI + prototype, combined page
5. `speckit-brand-prototype-clarify` — settle prototype behavior and states

## Language

- `speckit-brand-create` confirms the source set and its language before the first stage. Use that language for questions, stage summaries, and generated documents.
- If my input asks for a different output language, follow that request instead.
- Never default to English when the sources are written in another language.

## User Input

```text
$ARGUMENTS
```

Optional context (brand background, preferences, tones to avoid, or a stage to resume from). Fold it into the relevant stage. It does not override the gates below.

## Prerequisites

- The project is a Spec Kit project (`.specify/` exists).
- At least one spec exists at `specs/*/spec.md`.
- `speckit-brand-create` resolves and confirms the source set once, at the start of stage 1. Do not resolve specs here, and do not follow `.specify/feature.json` independently; after that, every stage reads section 0, "Sources", of `brand.md`.
- Read the confirmed sources and existing project docs only; never modify any `spec.md`.

## State Check (once, before any stage)

Check what already exists:

- `docs/brand/brand.md`
- `docs/brand/tokens.css`
- `docs/brand/assets/logo/`
- `prototype/index.html`

If any exist, ask once whether to **continue**, **rebuild**, or **skip** that part. Pass the decision to each stage command as an argument: `mode=continue` or `mode=rebuild` for `create`, `mode=extend`, `mode=rebuild`, or `mode=keep` for `prototype`. Never overwrite existing files without an explicit answer.

## How to Invoke Each Stage

Invoke the stage skill (`speckit-brand-create`, `speckit-brand-name-check`, `speckit-brand-clarify`, `speckit-brand-prototype`, `speckit-brand-prototype-clarify`). In command mode, use `/speckit-brand-create` and so on.

If the host cannot invoke another skill or command from here, read the matching file under `.specify/extensions/brand/commands/` and follow it directly, preserving the same gates:

| Stage | Command file |
|---|---|
| create | `brand-create.md` |
| name-check | `brand-name-check.md` |
| clarify | `brand-clarify.md` |
| prototype | `brand-prototype.md` |
| prototype-clarify | `brand-prototype-clarify.md` |

Do not paraphrase a stage from memory. Either invoke it or read its file.

## Execution Order

### 1. Create

Invoke `speckit-brand-create`. It first resolves the source set — asking me to confirm it when the project has more than one spec — then stops for my confirmation at the anchor, the name, and the slogan, and writes `docs/brand/brand.md` progressively. At the naming stage it calls `speckit-brand-name-check`.

Wait for it to finish before continuing. If it stopped because I did not answer, wait for me — do not proceed.

### 2. Name Check

`create` normally runs it during naming. Verify that `brand.md` contains a screening section with results or a clear "needs manual verification" marker for each finalist. If the section is missing, invoke `speckit-brand-name-check` now.

If screening was impossible (offline), state that plainly and continue with the chosen name recorded as unverified.

### 3. Clarify

Invoke `speckit-brand-clarify`. When it finishes, ask me whether another round is needed. Repeat until it reports no critical ambiguity or I say stop.

Do not run clarify before `brand.md` exists.

### 4. Prototype

Invoke `speckit-brand-prototype`. It:

1. Derives the visual board and initial logo/VI from `brand.md`
2. Designs the prototype screens from that visual standard
3. Assembles one combined page: project brief and visual board on top, prototype below
4. Asks for **one** review of the whole page
5. Revises the prototype and the visual board together

Do not ask for separate approvals for the visual board and the prototype. Do not skip the logo/VI question; the stage asks it explicitly and may be answered "no".

### 5. Prototype Clarify

Invoke `speckit-brand-prototype-clarify`. It asks up to five behavior/state questions and applies the answers to the prototype. After it finishes, ask whether another round is needed; repeat at my request.

### 6. Handoff

Brand work ends here. Do not create `plan.md`.

Tell me the next step is `/speckit-plan` (native Spec Kit), and that it should treat `docs/brand/brand.md`, `docs/brand/tokens.css`, and `prototype/index.html` as inputs.

## Gates

Stop and wait for me at each of these decisions:

- Source set, when `specs/` contains more than one spec
- Project brief
- Audience profiles
- Cultural anchor
- Brand name
- Slogan
- The single review of the combined prototype + visual board page

Never decide these alone. "Full workflow" means sequential execution, not autonomous decisions.

## Boundaries

- Never modify any `spec.md`.
- Write only under `docs/brand/` and `prototype/`.
- Do not create `docs/brand/name-check.md`; screening results live in `brand.md`.
- Do not create `plan.md`; that is native Spec Kit.
- Never fabricate screening results; mark unverifiable items "needs manual verification".
- If a stage fails or the host cannot reach the network, report it and continue only where the user agrees.

## Completion Report

When the full run ends, report:

- Files created or changed
- Which decisions I made (anchor, name, slogan, visual direction)
- Any unresolved items or manual verification still pending
- The next step: `/speckit-plan`
