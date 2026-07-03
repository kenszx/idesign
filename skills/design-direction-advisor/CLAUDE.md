# Design Direction Advisor

## When to Use

- User says "not sure about style" / "just make it look good"
- Request is ambiguous with no reference
- No sub-skill clearly matches the request

## 5-Phase Workflow

### Phase 0: Gather Context
Ask ONE question:
- "What's the project/product about? Who's the audience?"
- If still vague, proceed — that's what this skill is for.

### Phase 1: Parallel Exploration (Run 3 Sub-Agents)

Launch 3 independent reasoning paths. Each produces a REAL HTML visual, not a description.

**Path A — Situation Roulette**
Use a deterministic seed from the context to pick 1 of 20 style directions.
Output: HTML page with that style applied to the user's content.

**Path B — Real-World Reference**
Think of 1-2 award-winning real products/sites that match the context.
Extract their design language (layout, color, typography).
Output: HTML page adapting that language to the user's content.

**Path C — Design Philosophy**
Apply a known design philosophy (e.g., Swiss/Japanese/Minimalist/Brutalist).
Output: HTML page demonstrating that philosophy.

### Phase 2: Present Options
Show all 3 HTML outputs side by side with:
- 1-sentence summary of each approach
- What makes it different from the others
- Ask: "Which direction resonates with you?"

### Phase 3: Refine Based on Choice
Take the chosen direction and:
- Identify what the user liked
- Adjust based on any feedback
- Ask: "Any specific changes before I proceed?"

### Phase 4: Handoff to Sub-Skill
Once direction is clear, switch to the appropriate sub-skill:
- Prototyping → `design-prototyping`
- Web design → `web-design-engineer`
- Slides → `design-slides`
- Animation → `design-animation`
- Brand system → `design-brand-system`

### Phase 5: Build with Interaction
Follow the target sub-skill's full workflow (Phases 2-4 with checkpoints).

## Key Rules

- **Real visuals, not descriptions**: All three paths output real HTML
- **No style blending in Phase 1**: Each path is pure. User picks one.
- **Deterministic randomization**: Same context → same roulette result
- **Fallback to minimalist**: If all else fails, Swiss design is the safe default
