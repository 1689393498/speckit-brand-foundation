# Brand Foundation Extension

[中文](README.md) | English

**Brand Foundation** is a Spec Kit extension for projects that already have a `spec.md` but haven't established a brand yet.

It breaks brand planning into four confirmable stages: positioning & anchors, naming & screening, slogan & full plan, and finalization & delivery. It doesn't generate a logo or visual identity — it produces brand foundation documents: who the brand serves, why this name, how to say it, and the direction and boundaries for visual and verbal identity.

Names and slogans are always decided by a human. When name checks can't reach the internet, items are marked "needs manual verification" instead of fabricating results.

## Prerequisites

- An initialized Spec Kit project (`.specify/` exists)
- `/speckit-specify` completed, with `spec.md` in the project
- Spec Kit `>= 1.4.0`

## Installation

### Option 1: Release archive (recommended)

```bash
specify extension add --from https://github.com/1689393498/spec-brand-foundation/raw/main/release/brand-foundation-1.0.0.zip
```

- The project is mirrored on Gitee; if the repository moves, replace the URL with the new HTTPS address.
- The first install prompts **Untrusted Source** — verify the source, then type `y` to continue.
- HTTPS is required (HTTP is allowed only for `localhost` debugging).

### Option 2: Self-hosted catalog (optional, for teams)

```bash
specify extension catalog add https://your-host/catalog.json --name my-brand-catalog --install-allowed
specify extension add brand
```

Only enable `--install-allowed` for a catalog you own and have reviewed. Once added, use `specify extension search` to search within that catalog.

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

In Claude Code (skills mode):

```text
/speckit-brand-foundation
```

Optional extra guidance can be appended:

```text
/speckit-brand-foundation professional tone, not playful, may also serve B2B
```

Other integrations use their own invocation syntax.

## The Four Stages

| Stage | What happens | Human decision |
|---|---|---|
| 1. Positioning & Anchors | Build audience profiles, ask clarifying questions; propose 2–3 cultural anchor candidates and draft names | Pick an anchor |
| 2. Naming & Screening | Generate 3–5 name candidates; check each against the App Store, domains, public search, and brand-conflict risk | Pick a name |
| 3. Slogan & Full Plan | Propose one primary slogan + two alternatives; derive a `brand.md` draft along audience → core → visual → language → execution principles | Pick a slogan, request revisions |
| 4. Finalization & Delivery | Apply revisions, remove unused options, verify the reasoning chain, write the final document | Approve delivery |

## Outputs

```text
docs/brand/
├── name-check.md   # Stage 2: name screening report (with evidence, risk levels, disclaimers)
└── brand.md        # Stage 4: the single settled brand plan
```

## Boundaries

- Reads `spec.md` and existing project docs; never modifies `spec.md`
- Does no visual execution (logo, VI, collateral, media placement) — only brand direction and principles
- When screening can't reach the internet, each item is marked "needs manual verification"; results are never fabricated
- Screening results are not legal advice; consult a professional before formal registration
- Outputs are always written under `docs/brand/`

## Release & Versioning

### Packaging

```bash
python scripts/package.py
```

Produces:

```text
dist/brand-foundation-1.0.0.zip
dist/brand-foundation-1.0.0.zip.sha256
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
│   └── brand.md
├── scripts/
│   └── package.py
├── README.md        # Chinese
├── README.en.md     # English
├── CHANGELOG.md
├── LICENSE
├── release/         # Committed release archives, served via --from
└── dist/            # Local build output, not committed
```

## Uninstall

```bash
specify extension remove brand
```

## License

MIT
