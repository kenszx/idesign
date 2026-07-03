# Idesign

A unified design skill collection for AI coding agents. Build interactive prototypes, presentation slides, animations, brand systems, image generation, and more — all through natural language conversation.

**Compatible with**: Claude Code · Hermes Agent · Cursor · Codex

---

## Skills

| Skill | Description | Load |
|---|---|---|
| **web-design-engineer** | Web page / landing page / UI prototype design | `skills/web-design-engineer/SKILL.md` |
| **web-video-presentation** | Script → interactive 16:9 web video | `skills/web-video-presentation/SKILL.md` |
| **gpt-image-2** | Image generation with 79 prompt templates | `skills/gpt-image-2/SKILL.md` |
| **beautiful-article** | URL/PDF/DOCX → polished articles | `skills/beautiful-article/SKILL.md` |
| **kb-retriever** | Local knowledge-base retrieval | `skills/kb-retriever/SKILL.md` |
| **design-prototyping** | iOS/Android/Desktop interactive prototypes | `skills/design-prototyping/SKILL.md` |
| **design-slides** | Slide decks → PPTX/PDF export | `skills/design-slides/SKILL.md` |
| **design-animation** | Motion design → MP4/GIF export | `skills/design-animation/SKILL.md` |
| **design-critique** | 5-dimension expert design review | `skills/design-critique/SKILL.md` |
| **design-direction-advisor** | Style exploration for ambiguous requests | `skills/design-direction-advisor/SKILL.md` |
| **design-brand-system** | Brand asset extraction and application | `skills/design-brand-system/SKILL.md` |

## Installation

### npx skills (any agent)
```bash
npx skills add kenszx/idesign
```

### Claude Code
```bash
# Clone and symlink
git clone https://github.com/kenszx/idesign.git
ln -s $(pwd)/idesign/SKILL.md .claude/skills/idesign.md
```

### Hermes Agent
```bash
# Clone to hermes skills directory
git clone https://github.com/kenszx/idesign.git ~/.hermes/skills/idesign
```

## Usage

The master dispatcher automatically routes your request to the right sub-skill.

```bash
# Load the master dispatcher
npx skills idesign

# Or load a specific sub-skill directly
npx skills idesign/design-prototyping
```

Then just describe what you want:

> "Build an iOS app prototype for a fitness tracker"
> "Create a slide deck about our Q3 results"
> "Review this landing page design"
> "I need a brand system for a coffee shop"

Each skill guides you through an **interactive workflow**:
- Direction selection (2-3 options, you choose)
- Skeleton preview (feedback before build)
- Step-by-step construction (confirm each module)
- Polish and export

## Design Philosophy

- **Human-in-the-loop**: The user participates at every stage, not just the request
- **Choice over blank slate**: Options, not open-ended questions
- **Early correction**: Confirm direction before spending tokens on build
- **Real assets**: Brand assets from official sources, not approximations

## License

MIT
