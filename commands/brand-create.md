---
description: "Build or rebuild docs/brand/brand.md from the project's specs: project brief, audience, positioning and cultural anchors, naming, slogan, visual and verbal direction, and execution principles."
argument-hint: "Optional: brand background, preferences, tones to avoid, an existing name, or mode=continue|rebuild"
---

# Brand Create

Build `docs/brand/brand.md` from the project's specs in six stages. Stop at the anchor, the name, and the slogan; never decide them for me.

## Language

- Write everything I see — questions, stage summaries, and the document — in the language of the `current` spec in the confirmed source set.
- If the source set mixes languages and the current spec is unclear, ask once which language to use; record the answer in Sources.
- If my input asks for a different output language, follow that request and record it in Sources.
- Never default to English when the sources are written in another language.

## User Input

```text
$ARGUMENTS
```

Optional context: brand background, preferences, tones to avoid, an existing name, or a resume mode. Fold it into the relevant stage.

## Prerequisites

- A Spec Kit project (`.specify/` exists).
- At least one spec at `specs/*/spec.md`.

Resolve the source set once, before any stage:

1. List every `specs/*/spec.md` (one level under each feature directory).
2. If `.specify/feature.json` exists and its `feature_directory` contains `spec.md`, mark that spec `current`. Ignore a stale pointer whose directory does not exist.
3. If no spec exists, tell me "No spec.md found. Please run `/speckit-specify` first." and stop.
4. If exactly one spec exists, use it as the only source.
5. If more than one exists, show a table — directory, title from the first H1, last modified, current or not — and ask me to confirm the source set. Default to the whole project with all specs included; I may exclude specs that are internal, maintenance, or not product-facing. Never choose by modification time and never choose silently.
6. Read `.specify/memory/constitution.md` and the root `README.md` if they exist, as project-level background. They are not specs and are never modified.

If `brand.md` already has section 0, treat its recorded set as the current scope. Compare it with the `specs/` tree, report added or removed files, and ask before changing scope.

Record the confirmed set in section 0, "Sources", of `brand.md` before writing any other section. Every later command reads that section and does not resolve specs again.

- Read the confirmed sources and existing project docs only; never modify any `spec.md`.

## Existing Document

If `docs/brand/brand.md` exists:

- If the input says `mode=continue` or `mode=rebuild`, follow it.
- Otherwise ask: "Continue the existing brand.md, or start over?" Never overwrite silently.
- In continue mode, read the document, identify the first incomplete section, and resume there.
- If an existing `brand.md` has no section 0, "Sources", add it from the resolution above before resuming.

## Working Rules

- Update `brand.md` progressively after each confirmed stage so progress survives interruption.
- Keep the document in one language (the language recorded in Sources).
- Use only directional description in the visual and language sections: no hex values, font sizes, or other implementation numbers. Concrete values belong to `tokens.css` later.
- Do not repeat functionality already described in the specs. If one spec contradicts another, surface the conflict instead of averaging it.
- Everything must trace back to the audience and the brand core. If a section cannot be derived, say so and ask.

## Stage 0: Project Brief

1. Read every included source fully, plus the project background documents. Extract:
   - What the product or service does
   - Core features and user-facing flows
   - Who it serves and in what situations
   - Explicit constraints, non-goals, and existing decisions
   - Which source each fact comes from, and which facts only one spec states
2. If two sources disagree on audience, scope, or behavior, state the conflict and ask which one governs. Do not average them or pick silently.
3. Summarize this as a one-screen brief: project, audience, core value, key constraints.
4. Ask me to confirm or correct the brief. Stop and wait.
5. Write it as section 1 of `brand.md`, noting whether it came from the sources or from my corrections.

Do not invent product facts. If the sources are silent on something that matters, ask.

## Stage 1: Audience Profiles

1. Build 1–3 audience profiles from the brief. For each:
   - Who they are, age and life stage
   - The situation in which they meet the product
   - Core pain points
   - Aesthetic and emotional preferences
   - What they explicitly reject
2. Be concrete. Ban labels like "young people" or "urban white-collar workers" unless backed by specific behavior and context.
3. Ask 1–3 clarifying questions where the audience is ambiguous, and wait for answers.
4. Summarize the profiles and ask me to confirm or correct. Stop and wait.
5. Write section 2 of `brand.md`.

## Stage 2: Positioning & Cultural Anchors

1. Derive from the audience:
   - A one-line positioning: for whom, what it solves, what it makes them feel
   - 3–5 brand keywords
2. Propose 2–3 cultural anchors from real, verifiable works or cultural phenomena with clear depth. For each:
   - The work or phenomenon
   - The concrete element to borrow — a specific image, layer of meaning, or structure, not a vague label such as "very healing"
   - Why it matches the audience
   - The brand tone it could produce
   - One draft name based on it: name + pronunciation + core meaning + cultural origin
3. State uncertainty where it exists. Never fabricate a work or a quotation.
4. Recommend one anchor and explain why.
5. Stop and wait for me to choose an anchor or request another batch.
6. Write section 3 of `brand.md` with the chosen anchor and its derivation.

## Stage 3: Naming

### 3a. Naming brief

Ask only naming-specific questions, skipping what the brief already answers:

- Will the product or category expand beyond what the sources describe?
- Which language markets matter: Chinese only, bilingual Chinese/English, pinyin, or another combination?
- Hard constraints: length, characters that must or must not appear, desired domain or store availability
- Do you already have a name?

If I already have a name, skip generation and go straight to screening in 3d.

### 3b. Naming strategies

Propose 2–3 strategies appropriate to the audience and anchor. Examples:

- Descriptive — says what it does
- Evocative — draws on the cultural anchor or a concrete image
- Coined — invented, easier to own
- Compound or blend
- Loanword or borrowed term

For each strategy, state the trade-off: memorability, registrability, cross-language meaning, room to expand.

Stop and wait for me to choose the strategies, or say "all".

### 3c. Candidates

Generate 8–12 candidates across the chosen strategies, grouped by strategy. Each candidate includes:

- Name, in each needed language or script (Chinese, English, pinyin)
- Pronunciation and tone
- Literal meaning and intended brand meaning
- Origin: which strategy and which element
- Why it fits the audience
- Risks: homophones, negative connotations, difficulty of pronunciation or spelling

Never present a candidate whose origin you cannot explain. Ask me to mark **like / dislike / hold** with a one-line reason.

### 3d. Convergence and screening

1. Narrow to 3 finalists based on my marks and reasons, and show why each survived. If I already have a name, treat it as the single finalist.
2. Write section 4.1 of `brand.md` with the candidates and the finalists: name, pronunciation, meaning, origin, fit, risks.
3. Invoke `speckit-brand-name-check` for the finalists. If the host cannot invoke it, read `.specify/extensions/brand/commands/brand-name-check.md` and follow it directly. It reads section 4.1 and writes the screening into section 4.2.
4. Wait for the screening result and for me to choose the name.
5. Record the chosen name in section 4.3, with the reason and the reasons the others were rejected.

Do not pick a name for me. If I ask for another batch, return to 3c.

## Stage 4: Slogan & Brand Core

1. From the confirmed name, anchor, and audience, propose one primary slogan and two alternatives. For each, explain what it promises and what it refuses to promise.
2. Stop and wait for me to choose a slogan and give revision notes.
3. Write section 5 of `brand.md`:
   - Brand foundation: what was borrowed from the anchor and how it became the tone
   - Brand name: name + pronunciation + core meaning + cultural origin
   - Slogan: the chosen line
   - One-line positioning
   - Brand keywords
4. Remove unselected alternatives once the choice is confirmed.

## Stage 5: Visual Direction, Language Direction, Principles

Derive these strictly from section 5. They may not be written independently.

### Visual direction

- 2–3 concrete images with tone notes, each traced to the brand core
- Color direction: adjectives and color-family tendencies only, no hex values
- Typeface character: personality, plus open-source and embeddable suggestions
- Explicit exclusions: styles that must not appear

### Language direction

- Tone of voice: adjectives
- Expression taboos: phrasings or styles that must not appear
- Brand story: about 150 words in the document language
- Product or store description, if applicable: standard and one-line versions
- Context copy, if applicable: launch modal, share signature, notification tone — one line each

### Execution principles

- 3–5 bottom lines that both design and marketing must follow
- One-line test: what to ask when unsure

Write sections 6–8 of `brand.md`. Then check the derivation chain:

- Can every visual direction be traced to the brand core?
- Is the language direction consistent with the chosen tone?
- Is anything copied from the sources that adds no brand decision?

Fix breaks before reporting completion. Initialize section 9, "Decision log", and record the anchor, name, and slogan decisions made so far.

## Output Structure

Adapt headings to the document language. The required sections are:

0. Sources — confirmed spec set with status, output language, confirmation date
1. Project brief
2. Audience profiles
3. Positioning and cultural anchors
4. Naming — candidates, screening, final choice
5. Slogan and brand core
6. Visual direction
7. Language direction
8. Execution principles
9. Decision log — date, stage, question, decision

Section 0 must list every discovered spec with status `current`, `included`, or `excluded`, and record the output language. Downstream commands read it instead of re-resolving specs.

## Boundaries

- Never modify any `spec.md`.
- Keep section 0 current when I add or exclude a spec in a later run.
- Do not create `docs/brand/name-check.md`; screening is written into `brand.md`.
- Do not write `tokens.css`, logos, or prototypes; those belong to `speckit-brand-prototype`.
- Never fabricate anchors, quotations, or screening results.
- Never decide the anchor, name, or slogan alone.
- Write only `docs/brand/brand.md`.

## Completion

Report the path, the confirmed source set, which sections are settled, which decisions I made, and any open questions. Tell me the next step is `speckit-brand-clarify` (or let the full workflow continue).
