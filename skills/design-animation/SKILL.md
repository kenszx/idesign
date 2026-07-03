---
name: design-animation
description: >
  Create timeline-driven motion design animations using Stage + Sprite model.
  Export to MP4, GIF, or video with BGM and voiceover overlay.
version: 1.0.0
platforms: [macos, linux, windows]
tags: [animation, motion, video, MP4, GIF]
category: Design / Animation
---

# Design Animation — Motion Design & Video Export

## When to Use

- "Animate this / make a motion design"
- "Export to MP4 / GIF"
- "60fps video"
- "Animation with voiceover / narration"
- "Social media video"

## 5-Phase Workflow

### Phase 0: Clarify
Ask ONE question:
- "Use case? (social media/product showcase/brand video) Target duration?"

### Phase 1: Storyboard
Present a timeline storyboard:
```
[0:00-0:05] Intro — brand reveal
[0:05-0:15] Problem visualization
[0:15-0:30] Solution animation
[0:30-0:40] Key feature callouts
[0:40-0:45] CTA / Outro
```
Let user adjust timing and sequence.

### Phase 2: Style Direction
Show 2-3 animation style options:
- Motion language (bouncy/smooth/mechanical)
- Color palette
- Typography treatment
Let user choose.

### Phase 3: Build Scene by Scene
For each scene:
1. Build HTML/CSS animation using Stage + Sprite model
2. Show result
3. Wait for confirmation before next scene

### Phase 4: Export
Offer export options:
- **Screen recording** — MP4 at 25fps or 60fps
- **GIF** — Palette-optimized animated GIF
- **With BGM** — Layered background music
- **With voiceover** — Narration overlay

## References

- Rendering scripts: `scripts/`
- Animation engine: `../../shared/assets/animations.jsx`
- Audio assets: `../../shared/assets/audio/`
- Anti-slop rules: `../../shared/anti-slop-rules.md`
