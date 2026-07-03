# Design Brand System — Brand Asset Protocol

## When to Use

- User mentions a specific brand for design work
- Design will include recognizable product/brand names/logos
- User asks for brand guidelines or design system setup

## 5-Phase Workflow

### Phase 0: Fact Verify
Before anything else: `WebSearch` the brand/product to confirm:
- Latest version/release status
- Official name spelling and capitalization
- Product category and positioning

Write findings to `product-facts.md`.

### Phase 1: Asset Inventory
Ask user ONE question covering all:
- Do you have logo files / brand guidelines / screenshots?
- (If no) I'll source from official channels

### Phase 2: Official Source Search
Search in order:
1. `{brand}.com/brand` or `{brand}.com/press`
2. Wikimedia Commons, brand directories
3. Official social media profiles

### Phase 3: Download Assets
For each identified asset:
- **Logo**: SVG → extract inline → capture viewBox
- **Colors**: Grep `#xxxxxx` from assets → frequency-sort → filter grays
- **Typography**: Check brand site CSS for font-family declarations
- **Product images**: Download high-res from official press kits

### Phase 4: Solidify
Create `brand-spec.md` with:
- Brand name + official URL
- Color palette (primary + secondary + neutral)
- Typography stack
- Logo usage guidelines
- CSS variables: `--brand-*`

### Phase 5: Apply
Present the brand spec to user for approval.
Once approved, all generated designs use `var(--brand-*)` CSS variables.

## Interaction Rules

- **Show, don't describe**: Show found assets (SVG, screenshots) not just URLs
- **Fallback transparently**: If an asset can't be found, say so honestly
- **One question per phase**: Don't dump all questions at once
