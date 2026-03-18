# incident.io LinkedIn Posting Guidelines

*Guidelines for creating LinkedIn content that sounds authentically incident.io*

## Overview

LinkedIn is our primary platform for reaching engineering leaders, SREs, and technical decision-makers. Every post should feel like it comes from an experienced engineer sharing insights with peers - never like corporate marketing broadcasting at an audience.

**Posting Cadence**: ~1 post per day

**Primary Audience**: Engineering leaders, SREs, VPs of Engineering, CTOs, and technical practitioners who make or influence incident management decisions.

---

## The incident.io LinkedIn Voice

### Core Principle: Conversational Authority on a Professional Platform

On LinkedIn, we maintain our engineer-to-engineer credibility while acknowledging the platform's professional context. We're still the experienced engineer who's been on-call at 3 AM, but we're sharing those insights in a way that resonates with both individual contributors and engineering leadership.

### Voice Characteristics

**Empathetic First**
Start from understanding, not selling. Acknowledge the human reality of engineering work - the 3 AM pages, the stress of production issues, the pressure of high-stakes decisions.

**Technically Credible**
Include specific details that only someone who's lived through incident response would know. Reference real metrics, actual scenarios, genuine challenges.

**Professionally Casual**
More polished than a Slack message, less formal than a press release. Think "presenting at a conference" not "writing a legal document."

**Confidently Helpful**
Share insights because they're genuinely useful, not because you're trying to close a deal. The best LinkedIn posts feel like advice from a trusted colleague.

---

## Opening Hooks

The first line determines whether anyone reads the rest. Strong hooks create immediate recognition or curiosity.

### Hook Patterns That Work

**The Relatable Scenario**
Drop readers into a moment they've experienced. Make them think "yes, I know exactly what that feels like."

Examples:
- "You get paged at 3 AM. Slack is already chaos."
- "The dashboard is red. Everyone's talking. Nobody knows what's broken."
- "You're two hours into an incident and still don't know the root cause."

**The Provocative Statement**
Challenge assumptions or reveal uncomfortable truths. Create tension that the post resolves.

Examples:
- "An incident broke data emission for days. Quietly."
- "Most incident retrospectives are a waste of time."
- "Your on-call rotation is burning out your best engineers."

**The Empathy-First Opening**
Acknowledge the emotional reality before diving into solutions.

Examples:
- "Stress in incidents doesn't always come from the tech."
- "Nobody wants to be the person who broke production."
- "The worst part of being on-call isn't the pages. It's the anxiety between them."

**The Counter-Intuitive Insight**
Present a perspective that challenges conventional wisdom.

Examples:
- "The best incident response teams actually have more incidents."
- "Moving faster sometimes means slowing down your deployments."
- "Your monitoring is probably too noisy to be useful."

### Hooks to Avoid

- "We're excited to announce..." (corporate, not conversational)
- "incident.io is proud to..." (self-focused, not reader-focused)
- Generic statistics without context
- Questions that feel rhetorical rather than genuine

---

## Post Structure Patterns

### Pattern 1: Problem-First (Most Common)

**Structure:**
1. Hook with relatable problem (1-2 lines)
2. Expand on the pain point (2-3 lines)
3. Pivot to insight or solution (2-3 lines)
4. Social proof or specifics (1-2 lines)
5. Call to action

**Example:**
```
You get paged at 3 AM. Slack is already chaos.

Three different people are debugging the same thing. Nobody knows who's leading. The customer impact is growing every minute.

This is exactly why we built incident.io to work inside Slack - so everyone can see who's doing what, right where they're already talking.

Teams like Netflix and Etsy resolve incidents 60% faster because they stopped switching between tools.

Link in comments.
```

### Pattern 2: Story Arc (For Case Studies)

**Structure:**
1. Set the scene (company/situation)
2. The challenge they faced
3. What changed
4. Specific results
5. Takeaway or CTA

**Example:**
```
Running incidents at fintech scale without burning out the team feels... interest-ing.

Rho manages billions in business banking. When they grew from 100 to 400+ employees, their incident process couldn't keep up.

The fix wasn't more process - it was better tooling. They moved to incident.io and reduced senior engineer escalations by 70%.

Now their team handles 2x the incidents with half the stress.

Full story in comments.
```

### Pattern 3: Quick Hit (For Announcements)

**Structure:**
1. Punchy announcement (1 line)
2. Why it matters (1-2 lines)
3. Social proof or context (optional)
4. CTA

**Example:**
```
Thrilled that Tinder swiped right on incident.io

When your platform connects millions of people, downtime means missed connections. We're honored to help their team respond faster.

Welcome to the family.
```

### Pattern 4: Educational (For Thought Leadership)

**Structure:**
1. Insight or principle
2. Why this matters
3. Practical application
4. Additional context or resources

**Example:**
```
The best incident commanders aren't the best debuggers.

They're the best communicators.

Technical skill gets you into the room. But keeping everyone aligned, making decisions under pressure, knowing when to escalate - that's what separates good incident response from chaos.

We've been studying what makes incident commanders effective. Our findings in the latest SEV0 session.

Link in comments.
```

---

## Emoji Usage Guidelines

### Philosophy

Emojis should reinforce personality and improve readability - never replace words or feel excessive. Think of them as punctuation that adds warmth, not decoration that clutters.

### Appropriate Uses

**Signature Brand Moments**
- Fire for incidents/urgency/energy (but not overused)
- Handshake for partnerships
- Pager imagery for on-call content

**Playful Punctuation**
- One emoji at the end of a lighthearted post
- Wordplay reinforcement (like the Tinder "swipe right" example)
- Celebratory moments (customer wins, milestones)

**Functional Markers**
- Pointing hand for "link in comments" CTAs
- Checkmarks for list items (sparingly)

### Emoji Rules

1. **Maximum 2-3 emojis per post** - more feels like consumer brand, not B2B
2. **Never in the first line** - let words do the work first
3. **Never multiple emojis in a row** - no emoji strings
4. **Match the tone** - serious posts about outages shouldn't have party emojis
5. **Skip emojis entirely for heavy topics** - burnout, major incidents, sensitive subjects

### Examples

**Good:**
- "Thrilled that Tinder swiped right on incident.io" (one emoji, wordplay reinforcement)
- "Link in comments" (functional marker)
- "Running incidents at fintech scale without burning out the team feels... interest-ing." (pun without emoji overkill)

**Avoid:**
- Multiple fire emojis
- Emoji in every sentence
- Emojis that feel like filler

---

## Post Categories and Templates

### 1. Product Launches and Features

**Tone:** Excited but grounded in user benefit
**Focus:** What problem this solves, not just what we built

**Template:**
```
[Problem this feature solves]

[What we built to address it]

[Specific benefit or outcome]

[Link to learn more]
```

**Example:**
```
Figuring out who can do what during an incident shouldn't require a spreadsheet.

We just shipped team permissions - so you can control exactly who can acknowledge pages, lead incidents, or update status pages.

Set it once, never think about it again.

Details in comments.
```

### 2. Event Promotion (SEV0 Sessions, Webinars)

**Tone:** Educational invitation, not sales pitch
**Focus:** What attendees will learn, not what we'll present

**Template:**
```
[Compelling question or insight teaser]

[What we'll cover and why it matters]

[Who should attend]

[Registration CTA]
```

**Example:**
```
What makes some incident commanders calm under pressure while others panic?

We've interviewed dozens of engineering leaders about crisis leadership. In our next SEV0 session, we're sharing what we learned.

If you've ever wondered how to stay effective when everything's on fire, this one's for you.

Register: [link in comments]
```

### 3. Case Studies and Customer Wins

**Tone:** Proud but focused on the customer's achievement
**Focus:** Their transformation, not our product

**Template:**
```
[Customer's challenge or context]

[What changed for them]

[Specific, measurable result]

[Link to full story]
```

**Example:**
```
Skyscanner's incident response used to involve 30+ Slack channels.

Now? One channel, one source of truth, 70% of the company participating in incidents.

When your platform helps millions of travelers, you can't afford chaos.

Full story in comments.
```

### 4. Partnership Announcements

**Tone:** Genuine enthusiasm, focused on customer benefit
**Focus:** What this unlocks for users

**Template:**
```
[Partnership announcement]

[Why this matters for our customers]

[Specific capability or access this enables]

[Welcome/celebration]
```

**Example:**
```
Big news: incident.io is now a Datadog partner.

This means faster setup, deeper integration, and better incident context for teams using both platforms.

Because when your monitoring fires an alert, you shouldn't have to copy-paste into another tool.

Excited to build together.
```

### 5. Thought Leadership

**Tone:** Insightful peer sharing hard-won wisdom
**Focus:** Actionable principles, not abstract philosophy

**Template:**
```
[Core insight or principle]

[Why this matters / context]

[Practical application]

[Invitation to engage or learn more]
```

**Example:**
```
Incident ownership isn't about blame. It's about learning.

The teams that improve fastest after incidents are the ones that ask "what can we learn?" instead of "who did this?"

Blameless doesn't mean accountability-free. It means focusing accountability on systems, not individuals.

What's the best post-incident insight you've ever uncovered?
```

---

## Social Proof Integration

### Customer Names to Reference

These customers have approved public references and represent our market credibility:

**Enterprise/Scale:** Netflix, Etsy, Intercom, Skyscanner, monday.com
**Fast-Growing:** Ramp, Vanta, Airbnb, Buffer
**Specific Verticals:** Tinder (consumer), Rho (fintech), Trainline (travel)

### Using Social Proof Effectively

**Do:**
- Mention specific customer outcomes with numbers when available
- Use customer names to establish credibility for claims
- Reference customers whose audience matches the post topic

**Don't:**
- Name-drop without context
- Overuse the same customer references
- Claim results without specifics

**Examples:**

Good: "Netflix resolves critical incidents in under 2 minutes."
Good: "Teams like Etsy and Intercom have reduced MTTR by 60%."
Good: "Rho reduced senior engineer escalations by 70% after switching."

Avoid: "Companies like Netflix use incident.io." (vague, no outcome)
Avoid: "Join Netflix, Etsy, Intercom, Skyscanner, Airbnb, Ramp, and Buffer..." (list overload)

---

## Call-to-Action Best Practices

### "Link in Comments" Pattern

LinkedIn's algorithm reportedly favors posts without links in the main body. Our standard practice:

1. End post with "Link in comments" (with pointing emoji optional)
2. Immediately add first comment with the actual link
3. Keep the comment simple - just the link or minimal context

### CTA Variations

**For content (blogs, case studies):**
- "Full story in comments"
- "Link in comments"
- "Read more in comments"

**For events:**
- "Register in comments"
- "Save your spot - link in comments"

**For engagement:**
- "What's your experience?"
- "Curious what others think"
- Direct question related to the post topic

**For product:**
- "Try it free - link in comments"
- "Details in comments"

---

## Formatting Guidelines

### Length

**Optimal:** 150-300 words (enough for substance, short enough for mobile)
**Minimum:** 50 words (quick hits, announcements)
**Maximum:** 500 words (deep thought leadership, exceptional stories)

### Line Breaks

Use line breaks liberally. LinkedIn's display makes dense paragraphs hard to read on mobile.

**Good:**
```
This is a hook.

This expands on it.

This provides the insight.
```

**Avoid:**
```
This is a hook. This expands on it. This provides the insight. This adds more context. This continues further.
```

### Capitalization

Follow our standard brand guidelines:
- Sentence case for all copy (not Title Case)
- "incident.io" always lowercase (unless starting a sentence)
- Proper nouns capitalized normally

### Lists

Keep lists short (3-5 items max). Use line breaks between items rather than bullet points when possible - they read more naturally on LinkedIn.

---

## Do's and Don'ts

### Do

- Start with problems your audience actually has
- Include specific numbers and outcomes when available
- Sound like you're talking to a colleague, not presenting to a board
- Use the platform's native features (comments for links, engaging with replies)
- Mix content types - not every post should be a product push
- Acknowledge the human side of engineering work
- Test different hook styles to see what resonates

### Don't

- Start posts with "We're excited to announce"
- Use corporate buzzwords (synergy, leverage, robust, seamless)
- Post links in the main body (use "link in comments")
- Make every post about incident.io - share industry insights too
- Use excessive emojis or hashtags
- Be negative about competitors by name
- Post without a clear point or value for the reader

---

## Quality Checklist

Before posting, verify:

- [ ] First line creates immediate recognition or curiosity
- [ ] Post sounds like an experienced engineer, not a marketing department
- [ ] There's a clear "so what" - why should the reader care?
- [ ] Specific details or outcomes rather than vague claims
- [ ] Emoji usage is strategic, not decorative (max 2-3)
- [ ] CTA is clear and appropriate for the content type
- [ ] Link is in comments, not main post body
- [ ] Length is appropriate for the content (usually under 300 words)
- [ ] Follows sentence case capitalization
- [ ] Brand name is lowercase (incident.io, not Incident.io)

---

## Examples: Before and After

### Example 1: Product Launch

**Before (too corporate):**
```
We're excited to announce the launch of our new Team Permissions feature! This robust solution enables enterprise-grade access control for your incident management workflow. Contact us to learn more about how incident.io can transform your organization's incident response capabilities.
```

**After (incident.io voice):**
```
Figuring out who can do what during an incident shouldn't require a spreadsheet.

We just shipped team permissions - so you can control exactly who can acknowledge pages, lead incidents, or update status pages.

Set it once, never think about it again.

Details in comments.
```

### Example 2: Case Study

**Before (feature-focused):**
```
Rho Financial leverages incident.io's AI-powered platform to achieve significant improvements in their incident management metrics. Our solution helped them reduce escalations and improve team efficiency. Read the full case study to learn more.
```

**After (customer story):**
```
Running incidents at fintech scale without burning out the team feels... interest-ing.

Rho manages billions in business banking. When they grew from 100 to 400+ employees, their incident process couldn't keep up.

The fix wasn't more process - it was better tooling. They moved to incident.io and reduced senior engineer escalations by 70%.

Now their team handles 2x the incidents with half the stress.

Full story in comments.
```

### Example 3: Thought Leadership

**Before (vague and preachy):**
```
Effective incident management is critical for modern engineering organizations. Teams must embrace a culture of continuous improvement and invest in the right tools and processes to succeed in today's fast-paced environment.
```

**After (specific and insightful):**
```
The best incident commanders aren't the best debuggers.

They're the best communicators.

Technical skill gets you into the room. But keeping everyone aligned, making decisions under pressure, knowing when to escalate - that's what separates good incident response from chaos.

We've been studying what makes incident commanders effective. Our findings in the latest SEV0 session.

Link in comments.
```

---

*Last Updated: January 2026*
*Owner: @agent-copywriter*
