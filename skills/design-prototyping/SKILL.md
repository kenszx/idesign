---
name: design-prototyping
description: >
  Build interactive high-fidelity prototypes using HTML device frames.
  Supports iOS, Android, Mac, and browser form factors with clickable
  multi-screen navigation.
version: 1.0.0
platforms: [macos, linux, windows]
tags: [prototyping, iOS, Android, UI, mobile]
category: Design / Prototyping
---

# Design Prototyping — Interactive Prototypes

## When to Use

- "Build an app prototype / mockup"
- "iOS/Android app design"
- "Interactive demo"
- "Hi-fi prototype"

## Device Frames Available

| Device | Frame | File |
|---|---|---|
| iPhone 15 Pro | Dynamic Island + Home Indicator | `assets/ios_frame.jsx` |
| Android | Standard bezel | `assets/android_frame.jsx` |
| Mac window | Title bar + traffic lights | `assets/macos_window.jsx` |
| Browser | Tab bar + URL bar | `assets/browser_window.jsx` |

## 5-Phase Workflow

### Phase 0: Clarify
Ask ONE question:
- "Target platform? (iOS/Android/Desktop Web) Core features?"

### Phase 1: Style Direction
Show 2-3 style options with:
- Color palette swatches
- Typography pairing
- 1-2 sentence vibe description

Let user choose or adjust.

### Phase 2: Screen Map
Show screen flow diagram:
```
[Home] → [Detail] → [Settings]
  ↓
[Search]
```
Confirm with user before building.

### Phase 3: Build Screen by Screen
For each screen:
1. Build HTML/CSS inside device frame
2. Show result
3. Wait for confirmation before next screen

### Phase 4: Connect & Export
Wire up navigation between screens.
Offer to add: transitions, dark mode, gesture hints.

## Build Rules

- **React via CDN**: Use pinned CDN + integrity hashes (see `references/react-setup.md`)
- **State-driven screens**: All screens in one HTML file, switch via state
- **Real content**: No lorem ipsum. Use relevant placeholder text.
- **Device-accurate**: Respect safe areas, status bar, home indicator
- **Clickable**: Every tappable element must work

## References

- Device frame assets: `assets/`
- React + Vite setup: `references/react-setup.md`
- Pre-delivery checklist: `references/verification.md`
- Anti-slop rules: `../../shared/anti-slop-rules.md`
