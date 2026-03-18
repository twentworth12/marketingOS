# incident.io Video Brand Guidelines

Creating professional, on-brand, engaging video content.

## Core Principles

**Creative & Professional:** Videos should feel polished and intentional, never rushed or amateur.

**Always On-Brand:** Every frame reinforces incident.io's visual identity—fonts, colors, logo usage, motion style.

**Readable First:** Text must be large enough to read comfortably on any screen size, from mobile to desktop.

**Fun Through Animation:** Use motion to create energy and delight—spring physics, playful pops, smooth easing.

---

## Typography for Video

### Font Requirements

**ALWAYS use incident.io brand fonts:**
- **STK Bureau Serif Book** (headlines)
- **STK Bureau Sans Book** (body text)
- **STK Bureau Sans Medium** (emphasis, subheads)
- **STK Bureau Sans Bold** (signposting, CTAs)

**Never use:** Generic fonts (Arial, Helvetica, Georgia), Google Font substitutes in final videos

**Font loading:** All fonts available in `brand/fonts/*.woff2`

### Minimum Text Sizes (1920×1080)

**Critical for readability:**

| Element | Min Size | Recommended | Font | Weight |
|---------|----------|-------------|------|--------|
| **Hero Headlines** | 80px | 100-140px | Serif Book | 400 |
| **Secondary Headlines** | 60px | 70-100px | Serif Book | 400 |
| **Body Text** | 36px | 42-56px | Sans Book | 400 |
| **Emphasis Text** | 36px | 42-56px | Sans Medium/Bold | 500-700 |
| **CTAs** | 36px | 40-48px | Sans Bold | 700 |
| **Large Stats/Numbers** | 120px | 160-280px | Serif Book | 400 |

**Responsive sizing:** For smaller formats (1200×628, 800×500), scale proportionally while maintaining readability

### Typography Style Rules

**Letter Spacing:**
- Headlines: -3% (tight, clean)
- Body: 0% (standard)
- Never use positive letter spacing

**Line Height:**
- Headlines: 90-100% (tight)
- Body: 120-140% (breathing room)

**Case:**
- **Always sentence case** (never ALL CAPS or Title Case)
- Example: "Move fast when you break things" ✅
- Not: "Move Fast When You Break Things" ❌

**Color:**
- Primary text: Charcoal (#161618)
- Accent text: Alarmalade (#F25533) - use sparingly for emphasis
- Light text on dark: White (#FFFFFF)

---

## Motion & Animation Principles

### Core Motion Language

**Headlines:** Rise cleanly from baseline
- Use exponential easing out
- Start 40-60px below final position
- Animate over 15-25 frames (0.5-0.8s at 30fps)
- Creates sense of elevation and importance

**Supporting Text:** Fade and slide
- Use cubic easing out
- Start 15-25px below/above final position
- Fade in simultaneously with slide
- Feels snappy and purposeful

**UI Elements/Graphics:** Pop with spring physics
- Use spring animations (damping: 8-12, stiffness: 150-200)
- Scale from 0.7-0.9 to 1.0
- Fun and playful energy
- Quick but not jarring

**CTAs/Buttons:** Bounce in
- Spring physics with subtle overshoot
- Scale from 0.9 to 1.0
- Add subtle shadow that animates with scale
- Feels clickable and inviting

### Timing & Pacing

**Each beat has room to read:**
- Text on screen minimum: 1.5-2 seconds
- Complex text minimum: 2.5-3 seconds
- Don't rush transitions - let moments land

**Scene transitions:**
- Clean cuts between scenes (no wipes/dissolves usually)
- 0.2-0.5s overlap max if blending
- Maintain steady rhythm throughout

**Stagger animations:**
- Don't animate everything at once
- 5-10 frame delays between related elements
- Creates visual hierarchy and flow

### Playful Elements (Use Sparingly)

**When to add fun:**
- Key stat reveals (lightning bolts ⚡, sparkles ✨)
- Product moments (celebrate features)
- End frames (playful logo bounce)

**Keep it balanced:**
- 1-2 playful moments per 15-second video
- Should enhance, not distract
- Professional first, fun second

---

## Color Usage in Video

### Background Colors (in priority order)

**Primary Backgrounds:**
1. **White (#FFFFFF)** - Clean, confident, professional
2. **Sand (#F8F5F0)** - Warm, approachable, brand signature
3. **Light Sand (#F1EBE2)** - Subtle differentiation

**Accent Backgrounds:**
4. **Alarmalade (#F25533)** - High-impact moments only (used sparingly)
5. **Charcoal (#161618)** - Contrast moments (dark scenes)

**Never use:**
- Pure black backgrounds (#000000)
- Gradients (unless brand-approved for specific campaign)
- Off-brand colors

### Text Colors

**Primary:**
- Charcoal (#161618) on light backgrounds
- White (#FFFFFF) on dark backgrounds/Alarmalade

**Accent:**
- Alarmalade (#F25533) for emphasis, stats, CTAs
- "If everything is orange, nothing is" - use purposefully

**Accessibility:**
- Maintain WCAG AA minimum (4.5:1 contrast for body text)
- Test readability on actual devices, not just in editor

---

## Logo Usage in Video

### When to Use Logo

**Always include logo:**
- End frames (final 2-3 seconds)
- Branded content for external distribution
- Product announcements

**Logo placement:**
- End frames: centered, prominent (50-60% of frame width)
- Watermark: top-right corner, smaller (10-15% of frame width)

### Logo Variations

**Use correct variation for background:**
- `wordmark-colour-dark.svg` on white/light backgrounds ← Primary choice
- `wordmark-colour-light.svg` on dark backgrounds
- `icon-alarmalade.svg` for watermarks (flame only)

**Clear space:**
- Minimum clear space: height of flame
- Don't crowd the logo with text or elements

### Logo Animation

**End frame logo:**
- Spring animation: scale from 0.9 to 1.0
- Damping: 15, Stiffness: 100-120
- Smooth, confident entrance
- Pair with CTA button below

---

## Video Specs & Quality Standards

### Resolution & Aspect Ratios

**Primary Formats:**
- **Full HD Landscape:** 1920×1080 (YouTube, website, presentations)
- **Social Landscape:** 1200×628 (Twitter/X, LinkedIn posts)
- **Square:** 1080×1080 (Instagram, LinkedIn, multi-platform)
- **Vertical:** 1080×1920 (Stories, Reels, TikTok)

**Always render at native resolution** - don't upscale or stretch

### Duration Guidelines

**By platform:**
- Social media clips: 6-15 seconds
- Product features: 10-20 seconds
- Full intros: 15-30 seconds
- Explainers: 30-60 seconds max

**Keep it tight:**
- Every second should have purpose
- Cut ruthlessly - shorter is better
- If you can say it in 10 seconds, don't use 15

### Technical Specs

**Frame rate:** 30fps (standard for social)

**Codec:** H.264 (MP4) for compatibility

**File size targets:**
- 15-second video: < 2MB ideal
- 30-second video: < 4MB ideal
- Optimize for fast loading and smooth playback

**Output location:**
- All videos save to `outputs/`
- Never commit rendered videos to repository

---

## Composition & Visual Design

### Layout Principles

**10-column grid system:**
- Use consistent margins and padding
- Text should breathe within frame
- 10-15% margins on sides recommended

**Visual hierarchy:**
- Biggest/brightest = most important
- Use scale and color to guide the eye
- One focal point per scene

**Centered vs asymmetric:**
- Headlines: Usually centered
- Stats/numbers: Centered for impact
- Complex layouts: Can break grid for expression

### Scene Design

**Clean backgrounds:**
- Solid colors preferred
- Subtle gradients OK if brand-approved
- No busy patterns or textures

**Consistent style within video:**
- Pick a visual approach and stick with it
- Don't mix radically different styles between scenes
- Maintain coherent visual thread

**Negative space:**
- Don't fill every pixel
- Let elements breathe
- Simplicity = professionalism

---

## Animation Do's and Don'ts

### DO:

✅ Use spring physics for playful elements (icons, emojis, UI cards)
✅ Layer animations with 5-10 frame delays for flow
✅ Add subtle shadows that move with animated elements
✅ Keep motion purposeful - every animation should enhance communication
✅ Test on actual playback (Remotion preview, exported video)
✅ Use easing curves (never linear motion for text)

### DON'T:

❌ Animate everything simultaneously (overwhelming)
❌ Use rapid, jarring transitions (causes eye strain)
❌ Add motion just for motion's sake
❌ Use rotation unless it has clear purpose
❌ Overuse blur or motion blur effects
❌ Create accessibility issues (seizure-inducing flashes, rapid strobing)

---

## Content-Specific Guidelines

### Product Feature Videos

**Structure:**
1. Problem statement (3-4s)
2. Feature demonstration (5-8s)
3. Outcome/benefit (3-4s)
4. Logo + CTA (2-3s)

**Focus:**
- Show the feature clearly
- Use actual UI when possible (screenshots, simplified mockups)
- Emphasize speed, ease, or power

### Product Updates/Changelog

**Structure:**
1. Hook ("3× faster" stat, speedometer visual) (2-3s)
2. What changed (3-5s)
3. Why it matters (2-3s)
4. Logo + CTA (2s)

**Focus:**
- Lead with the benefit
- Be concise and punchy
- Celebrate the improvement

### Brand/Company Videos

**Structure:**
1. Tagline/mission (3-4s)
2. Problem recognition (2-3s)
3. Solution (3-5s)
4. Social proof or results (2-3s)
5. Logo + CTA (2-3s)

**Focus:**
- Emotional connection through recognized problems
- Position as peer sharing solution
- End with low-pressure invitation

---

## Quality Checklist

Before finalizing any video, verify:

### Brand Compliance
- [ ] Uses STK Bureau Serif/Sans fonts (not substitutes)
- [ ] Text minimum 36px for body, 80px for headlines
- [ ] All text in sentence case
- [ ] Colors match brand palette (no off-brand colors)
- [ ] Logo appears on end frame with proper clear space
- [ ] Background colors: White, Sand, or approved brand colors

### Motion & Animation
- [ ] Headlines rise from baseline (exponential easing)
- [ ] Supporting text fades/slides (cubic easing)
- [ ] UI elements pop (spring physics)
- [ ] Timing allows each beat to be read
- [ ] No jarring or uncomfortable motion
- [ ] Animations enhance communication, not distract

### Readability & Accessibility
- [ ] Text large enough to read on mobile devices
- [ ] Sufficient contrast (WCAG AA minimum)
- [ ] Text on screen long enough to read (1.5s minimum)
- [ ] No rapid flashing or strobing effects
- [ ] Clear visual hierarchy

### Technical Quality
- [ ] Renders at correct resolution (no scaling artifacts)
- [ ] Smooth playback at 30fps
- [ ] File size appropriate for platform
- [ ] Fonts load correctly (no fallback to system fonts)
- [ ] All assets render properly (logos, icons, images)

### Professional Polish
- [ ] Consistent visual style throughout
- [ ] Clean composition with proper negative space
- [ ] Purposeful design choices (every element has a reason)
- [ ] Feels cohesive as a complete piece
- [ ] Represents incident.io brand well

---

## Tools & Workflow

**Video Generation Stack:**
- **Remotion** for programmatic video creation
- **Brand fonts:** Load from `brand/fonts/*.woff2`
- **Logo assets:** Use from `incident-logo-video/public/SVGs/`
- **Output:** Always to `outputs/`

**Preview workflow:**
1. `npm start` - Preview in Remotion Studio
2. Scrub timeline to check timing
3. Test on actual size (don't just view zoomed in)
4. Export and watch final video

**Iteration:**
- Preview early and often
- Test on multiple devices/screens
- Get feedback before finalizing
- Iterate based on readability and impact

---

## Examples of Good Execution

**From our videos:**

✅ **"30-50% faster resolution"** (incident-response-product.mp4)
- 280px stat in Alarmalade dominates screen
- Lightning bolts ⚡ add energy without distraction
- Subtle pulse keeps it dynamic
- Clear, immediate impact

✅ **"Move fast when you break things"** (homepage-hero.mp4)
- Headlines rise with confident motion
- Speed lines on "fast" reinforce meaning
- Staggered word reveals create rhythm
- Brand fonts at 140px perfectly readable

✅ **"/incident command"** (incident-response-product.mp4)
- Terminal box pops with spring physics
- Charcoal background with Alarmalade text (high contrast)
- Large enough to read command clearly
- Professional tech aesthetic

**What makes these work:**
- Large, readable text
- On-brand fonts and colors
- Purposeful animation
- Clean composition
- Professional polish with playful energy

---

## Red Flags (What to Avoid)

❌ **Text too small** - Can't read on mobile (< 36px body, < 80px headlines)
❌ **Wrong fonts** - Using system fonts or Google Font substitutes in final output
❌ **Off-brand colors** - Random colors not in brand palette
❌ **Too busy** - Animating everything at once, cluttered composition
❌ **Generic motion** - Linear transitions, no easing, boring fades
❌ **Poor readability** - Low contrast text, text too fast, insufficient time to read
❌ **Inconsistent style** - Mixing different visual approaches within one video
❌ **No personality** - Sterile, corporate, no energy or human touch

---

## Platform-Specific Considerations

### LinkedIn
- **Aspect:** 1920×1080 or 1200×628
- **Duration:** 15-30 seconds ideal
- **Tone:** Professional but approachable
- **Hook:** First 3 seconds critical (auto-play without sound)
- **Captions:** Consider adding for sound-off viewing

### Twitter/X
- **Aspect:** 1200×628 (landscape) or 1080×1080 (square)
- **Duration:** 6-20 seconds
- **File size:** < 512MB, but aim for < 5MB for fast loading
- **Hook:** Immediate visual impact in first second

### Website/Landing Pages
- **Aspect:** 1920×1080 (16:9 standard)
- **Duration:** 15-45 seconds
- **Quality:** Higher bitrate OK (users expect higher quality)
- **Loop:** Consider if video should loop seamlessly

### Stories/Reels
- **Aspect:** 1080×1920 (9:16 vertical)
- **Duration:** 6-15 seconds
- **Style:** More dynamic, faster pacing
- **Text position:** Safe zones (avoid top/bottom 250px)

---

## Version Control & File Management

### Naming Convention

Use descriptive names with context:
- `incident-response-product.mp4` (what it's about)
- `homepage-hero-2026-01.mp4` (versioned)
- `3x-faster-product-update.mp4` (specific update)

### Storage

**Source files (commit to repo):**
- `.tsx` components in `incident-logo-video/src/`
- Configuration in `package.json`, `tsconfig.json`
- Brand assets in `public/SVGs/`, `public/fonts/`

**Output files (Desktop only):**
- All rendered videos: `outputs/`
- Never commit `.mp4`, `.mov`, `.gif` files to repository
- Keep source code, not rendered outputs

### Iteration & Versioning

**When updating videos:**
1. Modify source `.tsx` file
2. Re-render to Desktop
3. Review improved version
4. Keep or iterate further
5. Commit source changes to repository (not rendered video)

---

## Creative Process

### Planning a New Video

**1. Define objective:**
- What's the one thing viewers should remember?
- What action should they take?
- Who's the audience?

**2. Script the content:**
- Write text for each scene
- Aim for 2-4 words per second speaking pace
- Less text = more impact

**3. Sketch timing:**
- Map out scenes and duration
- Plan animation sequence
- Identify hero moment (biggest impact)

**4. Design visual style:**
- Which backgrounds? (White vs Sand)
- Text hierarchy (what's biggest?)
- Fun elements (where to add playfulness?)

**5. Build and iterate:**
- Create Remotion component
- Preview in studio
- Adjust timing, sizes, colors
- Test on actual devices

### Getting Feedback

**Internal review:**
- Does it match brand guidelines?
- Is text readable on mobile?
- Does animation feel smooth?
- Is the message clear?

**Quality gates:**
- Run through checklist above
- Test on phone, tablet, desktop
- Watch without sound (check if message lands)
- Get fresh eyes on it

---

## Advanced Techniques

### Creating Impact Moments

**Scale + Color + Motion:**
- Use large scale for important stats (200-280px)
- Add accent color (Alarmalade)
- Spring animation for pop
- Optional: Add particles/effects (sparingly)

**Example:** "30-50%" stat with lightning bolts

### Smooth Scene Transitions

**Clean cuts:**
- Most transitions should be instant cuts
- Maintains energy and professionalism

**Overlapping sequences:**
- 5-15 frame overlap for flow
- Use when connecting related ideas
- Keep it subtle

### Layered Animation

**Create depth:**
- Background elements animate first
- Text rises/slides in after
- Foreground elements pop last
- Creates visual layers and interest

### Looping Videos

**For continuous playback:**
- End state matches start state
- Smooth transition from last frame to first
- No jarring reset
- Good for website hero sections

---

## Troubleshooting Common Issues

**Problem:** Text too small to read on mobile
**Solution:** Use minimum sizes from Typography table, test on actual phone

**Problem:** Animation feels jarring or too fast
**Solution:** Increase duration (20-30 frames instead of 10-15), use easing curves

**Problem:** Colors look wrong after export
**Solution:** Verify hex codes match brand palette exactly, check color space settings

**Problem:** Fonts not loading correctly
**Solution:** Verify font files in `public/fonts/`, check font-face CSS in component

**Problem:** Video too large for platform
**Solution:** Adjust codec settings (--crf flag), reduce duration, optimize assets

**Problem:** Composition feels cluttered
**Solution:** Remove elements, increase negative space, simplify visual hierarchy

---

## Reference Materials

**Brand System:**
- [Brand Assets Reference](brand-assets-reference.md) - Full visual identity system
- [Brand Fonts](../brand/fonts/) - Official typeface files
- [incident.io/brand](https://incident.io/brand) - Logo downloads

**Video Tools:**
- [VIDEO-GENERATION-GUIDE.md](../incident-logo-video/VIDEO-GENERATION-GUIDE.md) - Remotion technical guide
- [Remotion Best Practices](../.agents/skills/remotion-best-practices/) - Animation patterns
- [Remotion Documentation](https://remotion.dev) - Official docs

**Examples:**
- `incident-intro-branded.mp4` - Full intro following all guidelines
- `incident-response-product.mp4` - Product feature showcase
- `homepage-hero.mp4` - Homepage messaging animation
- `3x-faster-incident.mp4` - Product update announcement

---

*These guidelines ensure every video we create is professional, on-brand, readable, and engaging. When in doubt, prioritize clarity and brand consistency over visual complexity.*
