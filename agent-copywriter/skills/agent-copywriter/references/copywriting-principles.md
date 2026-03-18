# incident.io Copywriting Principles

## Core Writing Philosophy

incident.io's copywriting is built on three foundational principles that should guide every piece of content:

### 1. Engineers Writing for Engineers
Everything we write should feel like it comes from someone who has been on-call at 3 AM, debugged production issues, and built AI SRE capabilities that work in production. We write as peers who've deployed AI in real engineering environments, not as vendors selling AI buzzwords. Our conversational authority comes from having solved these problems with AI that investigates, analyzes, and suggests fixes.

**Perfect Example**: "We built an MCP server so Claude can access your incidents"
*This blog post exemplifies authentic engineering voice - uses terms like "vibe-coded", includes honest admissions about project status ("largely vibe-coded and unsupported"), and provides real working code examples that engineers can use.*

**In Practice:**
- Use specific AI SRE examples with production metrics (Netflix 2-minute resolution, Ramp 70% reduction)
- Reference real AI investigation scenarios ("AI already analyzed the logs while you were joining the call")
- Share actual AI-generated code snippets and deployment-ready fixes
- Position AI as knowledgeable engineering teammate, not replacement
- Use authentic technical language about AI capabilities ("autonomous investigation", "production-proven accuracy")
- Be honest about AI limitations while showcasing real customer validation
- Include analogies that show AI as engineering amplification ("like having your best SRE with perfect memory")

### 2. Clarity Without Condescension
We explain complex concepts clearly without talking down to our audience. Our readers are smart but busy - they want depth without fluff.

**In Practice:**
- Define terms clearly without being patronizing
- Use analogies that illuminate, not obscure
- Provide context for every technical example
- Assume intelligence but not omniscience

### 3. Honesty About Hard Problems
We don't pretend incident management is easy or that we've solved every problem. We're honest about complexity while showing how we make it manageable.

**In Practice:**
- Acknowledge when something is difficult
- Share what didn't work in our own experience
- Be specific about limitations and trade-offs
- Focus on "better" rather than "perfect"

## Content Hierarchy and Structure

### Start with the Problem
Every piece of content should begin by establishing a problem our audience recognizes and cares about.

**Good Examples:**
- "Things go wrong. All the time. But chaos doesn't have to be."
- "On your bedside table sits a piece of software designed to wake you up"
- "First up: shock. You've just woken up! It's so bright!"

**Bad Examples:**
- "incident.io is excited to announce..."
- "We are the leading provider of..."
- "Our innovative solution..."

### Lead with Benefits, Support with Features
Always start with what the reader gets, then explain how we deliver it.

**Structure:**
1. **Outcome**: What will be different for the user
2. **Mechanism**: How our product creates that outcome
3. **Proof**: Evidence that it works (metrics, testimonials, examples)

### Use Progressive Disclosure
Start broad, then get specific. Give busy readers what they need upfront, then dive deeper for those who want detail.

**Template:**
- **TL;DR**: Key takeaway in one sentence
- **Overview**: Main points in 2-3 sentences
- **Details**: Full explanation with examples
- **Implementation**: Specific steps to take action

## Audience-Specific Guidelines

### For Engineering Teams
**Voice**: Knowledgeable peer sharing hard-won insights
**Focus**: Technical depth, real-world applicability, time-saving benefits
**Avoid**: Business jargon, oversimplification, unrealistic promises

**Example Approach:**
"Here's what we learned building our on-call system, and how you can avoid the mistakes we made."

### For Engineering Leaders
**Voice**: Strategic advisor who understands both technical and business concerns
**Focus**: Team efficiency, risk reduction, scaling challenges
**Avoid**: Technical minutiae without business context, generic leadership advice

**Example Approach:**
"Here's how this technical solution translates to better team outcomes and reduced operational risk."

### For Security/Compliance Teams
**Voice**: Trustworthy expert who takes security seriously
**Focus**: Risk mitigation, audit trails, compliance requirements
**Avoid**: Dismissing security concerns, vague security claims

**Example Approach:**
"Here's exactly how we handle sensitive incident data and maintain compliance."

## Language and Tone Guidelines

### Word Choice Principles

**Choose Active Over Passive**
- ✅ "We built this feature because..."
- ❌ "This feature was developed to..."

**Choose Specific Over Generic**
- ✅ "AI SRE reduces MTTR by 80% with autonomous investigation"
- ❌ "AI-powered incident response significantly improves resolution times"
- ✅ "Netflix resolves critical incidents in under 2 minutes with AI SRE"
- ❌ "Intelligent automation accelerates incident management"

**Choose Human Over Corporate**
- ✅ "When your systems break (and they will)"
- ❌ "In the event of service disruption"

**Choose Direct Over Diplomatic**
- ✅ "Most incident management tools are built for managers, not engineers"
- ❌ "Traditional approaches may not fully address modern engineering needs"

### Technical Language Guidelines

**Use Precise Technical Terms**
When discussing AI SRE capabilities, use the exact terminology engineers use for AI in production.

**Examples:**
- "Autonomous investigation" not "intelligent analysis"
- "Root cause correlation" not "smart insights"
- "AI-generated fixes" not "automated solutions"
- "Production-proven accuracy" not "advanced AI capabilities"
- "MTTR" not "recovery time"
- "On-call rotation" not "duty schedule"

**Provide Context for AI SRE Capabilities**
Position AI SRE as engineering amplification with specific context about its capabilities.

**Example:**
"Our AI SRE (Site Reliability Engineering teammate) autonomously investigates incidents by analyzing logs, correlating code changes with system failures, and suggesting deployment-ready fixes - like having your most experienced engineer available 24/7 with perfect memory of every incident."

### Metaphors and Analogies

**Use Familiar AI and Engineering Metaphors**
Draw comparisons to AI and engineering concepts that resonate with technical teams.

**Examples:**
- "AI SRE works like your best teammate who never forgets context from previous incidents"
- "It's like having an experienced engineer pair-investigating with perfect system memory"
- "Similar to how you'd want AI to understand your architecture deeply, not just generate summaries"
- "Think of it as AI that investigates at the speed of search with the knowledge of your most senior SRE"

**Avoid Non-Technical Analogies**
Don't use business or consumer metaphors that feel foreign to engineers.

**Avoid:**
- Sports analogies
- Military metaphors
- Consumer product comparisons

## Content Structure Patterns

### The Problem-Solution-Proof Pattern
1. **Problem**: Start with a specific pain point
2. **Solution**: Explain our approach
3. **Proof**: Show evidence it works

**Examples:**
- "Getting context during incidents is painful (Problem). Our AI automatically gathers relevant information from Slack, logs, and metrics (Solution). Teams report 60% faster context gathering (Proof)."
- "Claude sitting there like a smart colleague locked outside (Problem). We built an MCP server so Claude can directly access your incident data (Solution). Now Claude can provide contextual help during actual incidents (Proof)." *(from MCP server blog post)*

### The Story-Insight-Application Pattern
1. **Story**: Share a specific experience or scenario
2. **Insight**: Extract the key learning or principle
3. **Application**: Show how readers can apply it

**Example:**
"Last Tuesday at 3 AM, our monitoring woke up half the engineering team for a false alarm (Story). We learned that alert routing needs to be more intelligent than 'notify everyone' (Insight). Here's how to build smart escalation logic (Application)."

### The Current State-Desired State-Bridge Pattern
1. **Current State**: Acknowledge the status quo
2. **Desired State**: Paint a picture of what's possible
3. **Bridge**: Show how to get there

**Example:**
"Most teams still manage incidents through a mix of Slack messages and frantic calls (Current). Imagine if your incident response felt as organized as your code review process (Desired). Here's how to build that structure (Bridge)."

## Emotional Intelligence in Technical Writing

### Acknowledge the Human Context
Incident management isn't just a technical problem - it's a human experience that involves stress, pressure, and consequences.

**Examples:**
- "Nobody wants to be the person who broke production"
- "3 AM wake-up calls are never fun"
- "The pressure to fix things fast can lead to mistakes"

### Validate Reader Experiences
Show that we understand the real challenges they face.

**Examples:**
- "If you've ever spent 20 minutes just figuring out what's broken..."
- "We've all been in those incidents where everyone's talking but nobody knows what's happening"
- "You know that sinking feeling when you see the alert come in"

### Balance Empathy with Solutions
Acknowledge problems without dwelling on them - move quickly to how things can be better.

**Structure:**
1. Brief acknowledgment of the pain point
2. Quick transition to the solution
3. Focus on the improved experience

## Brand Differentiation Language

### Against "Enterprise" Solutions
**Their positioning**: Comprehensive, enterprise-grade, scalable
**Our counter**: Usable, engineer-friendly, production-proven

**Language patterns:**
- "Built for the people who respond to incidents"
- "No training required - it works like the tools you already love"
- "Powerful enough for Netflix, simple enough for your startup"

### Against "Simple" Solutions
**Their positioning**: Easy to use, quick setup, basic functionality
**Our counter**: Sophisticated but intuitive, comprehensive but not complex

**Language patterns:**
- "All the power you need, none of the complexity you don't"
- "Sophisticated incident management that doesn't require a PhD"
- "Every feature you need, exactly when you need it"

### Against DIY/Status Quo
**Their positioning**: Why change what works?
**Our counter**: You can do better without more work

**Language patterns:**
- "Stop rebuilding incident management from scratch"
- "All the customization, none of the maintenance"
- "Like your current process, but production-scalable"

## Reference Example: Perfect Technical Blog Post

### "We built an MCP server so Claude can access your incidents"

This blog post is a model example of incident.io's authentic engineering voice and should be referenced when creating technical content.

**Why This Post Works So Well:**

1. **Authentic Engineering Voice**: 
   - Uses casual technical language engineers use ("vibe-coded", "or don't")
   - Honest about project limitations ("largely vibe-coded and unsupported")
   - Sounds like a colleague sharing something cool, not marketing copy

2. **Perfect Problem Setup**:
   - Starts with relatable scenario: "Claude sitting there like a smart colleague locked outside"
   - Uses brilliant analogy that immediately resonates with engineers
   - Makes abstract problem concrete and visual

3. **Technical Credibility**:
   - Includes real, working code snippets with proper context
   - Explains architectural decisions and trade-offs
   - Provides actual GitHub repository for readers to explore

4. **Storytelling Structure**:
   - Problem → Investigation → Solution → Implementation → Bigger Picture
   - Natural conversation flow that doesn't feel forced
   - Builds excitement about the technical solution

5. **Educational Value**:
   - Teaches readers about MCP servers and AI integration
   - Provides practical next steps and resources
   - Shows how incident.io thinks about AI workflow improvements

**Key Techniques to Replicate:**
- Start with vivid, relatable problem scenarios
- Use authentic technical language without marketing polish
- Include honest status updates and limitations
- Provide working code examples with context
- Structure as natural problem-solving narrative
- End with clear next steps and resources
- Use analogies that illuminate rather than obscure

**Template Structure from This Post:**
1. **Hook**: Compelling analogy or scenario ("smart colleague locked outside")
2. **Problem**: Why this matters and what's frustrating about current state
3. **Solution Approach**: How we decided to tackle it
4. **Technical Implementation**: Code examples and architecture details
5. **Demonstration**: Show it working with real examples
6. **Bigger Picture**: How this fits into larger trends or improvements
7. **Next Steps**: GitHub repo, trial offers, clear calls to action

This post demonstrates exactly how incident.io should write about technical products - educational, authentic, technically credible, and genuinely useful.

## Quality Assurance Checklist

Before publishing any content, ensure it meets these standards:

### Voice and Tone
- [ ] Sounds like an experienced engineer, not a marketing department
- [ ] Appropriate level of technical depth for the audience
- [ ] Confident without being arrogant
- [ ] Helpful without being condescending

### Content Structure
- [ ] Starts with a problem the reader recognizes
- [ ] Uses progressive disclosure (TL;DR → Details → Implementation)
- [ ] Includes specific examples and evidence
- [ ] Ends with clear next steps

### Language
- [ ] Uses active voice and specific outcomes
- [ ] Avoids corporate jargon and empty buzzwords
- [ ] Defines technical terms appropriately for the audience
- [ ] Maintains consistency with brand voice

### Technical Accuracy
- [ ] All code examples are correct and contextual
- [ ] Technical claims are accurate and verifiable
- [ ] References to other tools/products are fair and current
- [ ] Metrics and outcomes are specific and honest

### Audience Relevance
- [ ] Addresses real problems the audience faces
- [ ] Uses language and examples they'll recognize
- [ ] Provides actionable value
- [ ] Respects their time and intelligence