---
name: design-slides
description: >
  Create presentation slide decks as HTML with export to editable PPTX,
  PDF, and video. Supports cinematic patterns, speaker notes, and
  multi-format delivery.
version: 1.0.0
platforms: [macos, linux, windows]
tags: [slides, presentation, PPTX, deck]
category: Design / Slides
---

# Design Slides — Presentation Deck Creator

## When to Use

- "Create a slide deck / presentation"
- "Export to PPTX / PowerPoint"
- "Make a keynote"
- "Presentation slides for client/internal"

## 5-Phase Workflow

### Phase 0: Clarify
Ask ONE question:
- "Presentation scenario? (internal share/client pitch/conference talk) Slide count estimate?"

### Phase 1: Deck Structure
Present a slide outline:
```
1. Cover — title + subtitle
2. Problem — the gap / opportunity
3. Solution — what we built
4. Demo / Screenshots
5. Results / Data
6. Next Steps
```
Let user reorder/add/remove sections.

### Phase 2: Style Direction
Show 2-3 visual style options for the deck.
Each option: color palette + typography + sample slide visual.
Let user choose or mix.

### Phase 3: Build Slide by Slide
For each slide:
1. Build as 1920×1080 HTML section
2. Show result
3. Wait for confirmation

### Phase 4: Export
Offer export options:
- **HTML deck** — All slides in one HTML file, navigation controls
- **PPTX** — Editable PowerPoint via `html2pptx.js`
- **PDF** — Print-ready PDF

## Build Rules

- **1920×1080** — Fixed aspect ratio, each slide is a full viewport
- **Speaker notes** — Include `data-notes` attribute on each slide
- **Print-friendly** — `@media print` rules for slide breaks
- **No page-like scrolling** — Slides are discrete views, not a page
- **Cinematic patterns** — Consider: reveal, wipe, fade transitions

## References

- PPTX export scripts: `scripts/html2pptx.js`, `scripts/export_deck_pptx.mjs`
- PDF export: `scripts/export_deck_pdf.mjs`
- Deck template: `scripts/deck_stage.js`, `scripts/deck_index.html`
- Anti-slop rules: `../../shared/anti-slop-rules.md`
