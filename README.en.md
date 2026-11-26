# Brand Extension

[中文](README.md) | English

**Brand** is a Spec Kit extension. It starts from the project's `specs/` and runs the brand work as one chain: brand manual, name screening, brand clarification, and finally a single page that combines the visual board, initial logo/VI, and product prototype. Brand is a project-level asset, so a project gets one `brand.md`.

Brand direction lives in the document; concrete colors, type, logo assets, and the prototype are produced by the prototype stage. Names, slogans, cultural anchors, and visual direction are always decided by a human. When name checks cannot reach the internet, items are marked "needs manual verification" instead of fabricating results.

## Prerequisites

- An initialized Spec Kit project (`.specify/` exists)
- `/speckit-specify` completed, with at least one `spec.md` under `specs/`
- Spec Kit `>= 1.4.0`

## Installation

### Option 1: Release archive (recommended)

```bash
# GitHub (primary)
specify extension add --from https://github.com/1689393498/speckit-brand-foundation/raw/main/release/brand-foundation-2.1.0.zip

# Gitee (mirror)
specify extension add --from https://gitee.com/LeisDevelopment/speckit-brand-foundation/raw/main/release/brand-foundation-2.1.0.zip
```

- Both URLs serve identical archives; pick either one.
- The first install prompts **Untrusted Source** — verify the source, then type `y` to continue.
- HTTPS is required (HTTP is allowed only for `localhost` debugging).

### Option 2: Self-hosted catalog (optional, for teams)

```bash
specify extension catalog add https://your-host/catalog.json --name my-brand-catalog --install-allowed
specify extension add brand
```

Only enable `--install-allowed` for a catalog you own and have reviewed.

### Option 3: Local development

```bash
specify extension add --dev /path/to/brand-foundation
```

After installation, verify with:

```bash
specify extension list
specify extension info brand --json
```

## Usage

In Claude Code (skills mode), run the full workflow:

```text
/speckit-brand-run
```

Or run one stage:

| Command | What it does |
|---|---|
| `/speckit-brand-run` | Full workflow, in order, stopping at every decision |
| `/speckit-brand-create` | Build or rebuild `docs/brand/brand.md` only |
| `/speckit-brand-name-check` | Screen names only; results go into `brand.md` |
| `/speckit-brand-clarify` | Clarify brand direction only |
| `/speckit-brand-prototype` | Visual board, initial logo/VI, and prototype page only |
| `/speckit-brand-prototype-clarify` | Settle prototype behavior and states only |

> Spec Kit requires command names to follow `speckit.{extension}.{command}`, so the default entry is `/speckit-brand-run`; there is no standalone `/speckit-brand`.

Optional guidance can be appended:

```text
/speckit-brand-run professional tone, not playful, may also serve B2B
```

### Language

All questions, stage summaries, and generated documents follow the language of the source specs automatically; if they mix languages, you confirm once. You can also request a language explicitly:

```text
/speckit-brand-run please write everything in English
```

The command prompts are written in English so international users and contributors can read and extend them.

### Multiple specs and source confirmation

A project usually has several `specs/<feature>/spec.md` files. Brand is a project-level asset, so `brand.md` stays a single document:

- On the first `/speckit-brand-create` or `/speckit-brand-run`, the extension lists every spec (directory, title, last modified, whether it is the current feature) and asks which ones the brand should derive from.
- The whole project is included by default; you can exclude specs for internal refactors or pure maintenance.
- The confirmed set is written to section 0, "Sources", of `brand.md`. Clarify, name-check, and prototype read that list only, so they do not drift when `feature.json` changes.
- When specs are added or removed later, commands flag it but never change the source scope on their own.

## Flow

```text
specs/*/spec.md (confirmed source set)
  │  /speckit-brand-create
  ▼
docs/brand/brand.md                sources, brief, audience, positioning and anchors, naming, slogan, direction
  │  /speckit-brand-name-check
  ▼
final name (screening written back into brand.md)
  │  /speckit-brand-clarify
  ▼
settled brand.md
  │  /speckit-brand-prototype
  ▼
A: visual board + initial logo/VI
  │
  ▼
B: prototype screens designed from A
  │
  ▼
prototype/index.html               top: brief + A; bottom: B
  │  one human review; revise B and A together
  ▼
/speckit-brand-prototype-clarify   behavior and states; revise B
  │
  ▼
/speckit-plan (native)             specs/<feature>/plan.md
```

### Where it stops for you

| Stage | Your decision |
|---|---|
| create | Source scope (when there are multiple specs), project brief, audience, cultural anchor, name, slogan |
| name-check | Screening result and final name |
| clarify | Up to 5 questions per round |
| prototype | One review of the combined page: visual board, logo/VI, and prototype together |
| prototype-clarify | Up to 5 questions per round |

"Full workflow" means sequential execution, not autonomous decisions. Every gate stops.

## Outputs

```text
docs/brand/
├── brand.md                  # Single source of brand text; sources, screening, and decision log included
├── tokens.css                # Colors, type, scale, spacing, radii; used by development
└── assets/
    ├── logo/
    │   ├── logo-horizontal.svg
    │   ├── logo-stacked.svg
    │   ├── mark.svg
    │   ├── logo-mono.svg
    │   └── logo-inverse.svg
    └── app-icon.svg

prototype/
├── index.html                # Top: project brief + visual board; bottom: prototype
├── styles.css                # Imports ../docs/brand/tokens.css
├── app.js
└── README.md
```

- No separate `name-check.md`; screening, evidence, and risk levels are merged into the "Naming" section of `brand.md`.
- No `plan.md`; the next step is native `/speckit-plan`.

## Initial logo and VI

The prototype stage derives the visual board from `brand.md` and, by default, adds a first version of the logo and basic VI:

- Wordmark (horizontal and stacked), one simple mark, mono and inverse variants, app icon
- Clear space, minimum size, background rules, don'ts
- 2–3 applications suited to the product type
- All editable SVG; open-source, embeddable fonts only

Boundaries:

- One recommended direction, not multiple competing concepts
- No trademark similarity search; the draft is not legal advice — run a professional search before use
- No AI-generated raster logos
- No print delivery (CMYK, bleed, die lines), no full brand guidelines PDF
- No standalone VI manual; the board is an initial draft, not a delivered identity system

If the project already has a logo, the command checks `docs/brand/assets/logo/`, reuses it, and adds missing rules instead of redesigning it.

## Boundaries

- Reads the confirmed specs and existing project docs; never modifies any `spec.md`
- Names, slogans, anchors, and visual direction are decided by a human
- When screening cannot reach the internet, each item is marked "needs manual verification"; results are never fabricated
- `brand.md` stays directional; concrete values live in `tokens.css`
- Outputs are written only under `docs/brand/` and `prototype/`
- Brand work ends at the prototype and visual board; engineering planning is left to native `/speckit-plan`

## Release & Versioning

### Packaging

```bash
python scripts/package.py
```

Produces:

```text
dist/brand-foundation-2.1.0.zip
dist/brand-foundation-2.1.0.zip.sha256
```

Upload the zip to any HTTPS host to distribute it; the SHA-256 can be used for self-hosted catalogs or user verification.

### Version bumps

1. Update `extension.version` in `extension.yml`
2. Record the change in `CHANGELOG.md`
3. Re-run `python scripts/package.py`

## Directory Structure

```text
brand-foundation/
├── extension.yml
├── commands/
│   ├── brand-run.md                  # speckit.brand.run
│   ├── brand-create.md               # speckit.brand.create
│   ├── brand-name-check.md           # speckit.brand.name-check
│   ├── brand-clarify.md              # speckit.brand.clarify
│   ├── brand-prototype.md            # speckit.brand.prototype
│   └── brand-prototype-clarify.md    # speckit.brand.prototype-clarify
├── scripts/
│   └── package.py
├── README.md        # Chinese
├── README.en.md     # English
├── CHANGELOG.md
├── LICENSE
├── release/         # Committed release archives, served via --from
└── dist/            # Local build output, not committed
```

## Upgrading from 1.x

2.0.0 is a breaking redesign:

- `speckit.brand.foundation` is removed; use `/speckit-brand-run` and its subcommands
- `docs/brand/name-check.md` merges into `brand.md` and can be deleted
- A separately installed `speckit-prototype-clarify` is replaced by `/speckit-brand-prototype-clarify`
- Existing `prototype/` is detected; the command asks whether to extend or rebuild and never overwrites silently

### Upgrading from 2.0.0

2.1.0 is non-breaking; an existing `brand.md` keeps working. On the next run of any command, if section 0, "Sources", is missing, it falls back once to the old spec resolution, then offers to write the source list.

## Repositories & Sync

| Repository | SSH URL | Remote |
|---|---|---|
| GitHub (primary) | `git@github.com:1689393498/speckit-brand-foundation.git` | `github` |
| Gitee (mirror) | `git@gitee.com:LeisDevelopment/speckit-brand-foundation.git` | `origin` |

```bash
git push origin main   # Gitee
git push github main   # GitHub
```

GitHub is connected over SSH; add your local public key to your GitHub account before the first push.

## Uninstall

```bash
specify extension remove brand
```

## License

MIT
