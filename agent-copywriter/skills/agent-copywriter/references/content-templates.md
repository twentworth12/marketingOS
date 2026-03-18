# incident.io Content Templates and Examples

## Blog Post Templates

### Technical Deep Dive Template

**Purpose**: Share detailed technical insights and lessons learned
**Audience**: Engineering teams looking for implementation guidance
**Tone**: Knowledgeable peer sharing hard-won experience

**Perfect Example**: "We built an MCP server so Claude can access your incidents"
*This blog post demonstrates ideal incident.io technical writing - authentic engineering voice, honest about limitations, includes real code, and provides clear next steps.*

#### Structure:
```
1. Hook: Relatable problem or surprising finding
2. Context: Why this matters and when we discovered it
3. Investigation: How we dug into the problem
4. Solution: What we built and why
5. Implementation: Code examples and technical details
6. Results: What we learned and measured outcomes
7. Takeaways: What readers should do next
```

#### Key Elements from MCP Server Blog Post:
```
1. Relatable Problem Setup: "Claude sitting there like a smart colleague locked outside"
2. Honest Status: "largely vibe-coded and unsupported" (transparency builds trust)
3. Authentic Language: Uses terms engineers actually use ("vibe-coded", "or don't")
4. Real Code Examples: Working code snippets with proper context
5. Practical Analogies: "like having a smart colleague locked outside"
6. Clear Implementation: Step-by-step technical details
7. Bigger Picture: How this fits into AI workflow improvements
8. Next Steps: GitHub repo, trial offer, clear calls to action
```

#### Example Opening (Inspired by MCP Server Post):
```
"Picture this: Claude is sitting there, ready to help with your incident response, but it's like having a smart colleague locked outside your office while everything's on fire inside.

That's exactly how we felt when we realized Claude couldn't directly access our incident data to provide meaningful help during outages. So we built something to fix it.

Here's how we created an MCP server that lets Claude access your incidents, what we learned about AI integration challenges, and why this might change how you think about AI-powered incident response."
```

#### Alternative Opening (Original Template):
```
"At 3:47 AM last Tuesday, our monitoring system decided to wake up exactly zero people about a critical database issue. The irony? We're the company that builds incident management software.

Here's the story of how we debugged our own alerting system, what we learned about notification reliability, and the changes we made to ensure it never happens again."
```

#### Technical Section Example:
```
The root cause turned out to be a race condition in our alert routing logic:

```python
def route_alert(alert, escalation_policy):
    # This looked fine, but had a subtle timing issue
    on_call_user = get_current_on_call(escalation_policy)
    if on_call_user.is_available():
        send_notification(on_call_user, alert)
```

The problem: between checking availability and sending the notification, 
the user's status could change. Here's how we fixed it...
```

### Product Announcement Template

**Purpose**: Introduce new features or capabilities
**Audience**: Current users and prospects
**Tone**: Excited engineer sharing something they built

#### Structure:
```
1. Problem: What users currently struggle with
2. Announcement: What we built and why it matters
3. How it Works: Core functionality with examples
4. Customer Impact: Early feedback and use cases
5. Getting Started: How to try it
6. What's Next: Future development plans
```

#### Example Opening:
```
"We've shipped hundreds of features since launching incident.io, but this one feels different. 

AI SRE doesn't just make incident response faster—it changes who can participate in fixing complex issues. Instead of waking up your most senior engineer every time something breaks, your AI teammate can handle the first 80% of investigation and remediation.

Here's how it works, why we built it, and what early customers are saying..."
```

### Process/Culture Post Template

**Purpose**: Share internal practices and cultural insights
**Audience**: Engineering leaders and team builders
**Tone**: Transparent thought leader sharing lessons

#### Structure:
```
1. Context: The challenge or decision we faced
2. Our Approach: How we tackled it and why
3. Implementation: Specific practices and tools
4. Results: What worked, what didn't, metrics
5. Evolution: How our thinking has changed
6. Advice: What others should consider
```

#### Example Opening:
```
"How do you hire engineers when you're competing with companies that pay 40% more?

After losing our third top candidate to a higher offer last quarter, we realized we were asking the wrong question. Instead of 'How do we compete on salary?' we started asking 'What do great engineers actually want?'

Here's what we learned, how we changed our approach, and why our offer acceptance rate jumped from 40% to 85%."
```

## Product Marketing Templates

### Feature Description Template

**Purpose**: Explain product capabilities clearly and compellingly
**Audience**: Prospects evaluating solutions
**Tone**: Confident problem-solver

#### Structure:
```
1. Problem Recognition: Pain point they experience
2. Solution Overview: How we solve it differently
3. Key Benefits: Specific outcomes and metrics
4. How It Works: Brief technical explanation
5. Social Proof: Customer quotes or case studies
6. Call to Action: Next step to take
```

#### Example:
```
**Problem**: "Gathering context during incidents feels like archaeology. By the time you've found the relevant logs, metrics, and recent deployments, 20 minutes have passed and your customers are getting angry."

**Solution**: "Our AI SRE automatically correlates alerts with recent code changes, gathers relevant context from your monitoring tools, and presents everything in a single view—usually before you've even joined the incident channel."

**Benefits**: 
- 75% faster context gathering
- 60% reduction in mean time to resolution
- Junior engineers can effectively handle complex incidents

**How It Works**: "When an alert fires, AI SRE immediately scans your recent deployments, related metrics, similar past incidents, and team Slack conversations. It builds a comprehensive incident briefing and updates it in real-time as new information becomes available."

**Social Proof**: "Before AI SRE, I'd spend the first 15 minutes of every incident just figuring out what was broken. Now I get that context instantly and can focus on actually fixing the problem." - Senior Engineer, Etsy
```

### Competitive Positioning Template

**Purpose**: Differentiate from alternatives without being negative
**Audience**: Prospects comparing solutions
**Tone**: Confident and direct

#### Structure:
```
1. Status Quo Problem: What's wrong with current approaches
2. Our Different Approach: How we think about the problem
3. Specific Differences: Concrete comparisons
4. Customer Validation: Quotes supporting our approach
5. Why It Matters: Business impact of the difference
```

#### Example:
```
**The Problem with Traditional Tools**: "Most incident management platforms were built for IT managers, not the engineers who actually respond to incidents. They focus on ticket tracking and SLA compliance instead of helping you fix things fast."

**Our Approach**: "We built incident.io for the people who get woken up at 3 AM. Every feature starts with the question: 'Does this help engineers resolve incidents faster?'"

**Key Differences**:
- Native Slack integration vs. separate dashboard
- AI-powered context gathering vs. manual information collection  
- Engineer-friendly interface vs. management-focused reporting
- Modern API-first architecture vs. legacy monolithic systems

**Customer Validation**: "We switched from [competitor] because incident.io actually makes our engineers more effective during incidents, not just our managers more informed about them." - Engineering Director, SumUp

**Business Impact**: Teams using incident.io see 40% faster resolution times because engineers spend less time fighting their tools and more time fixing problems.
```

## Email Templates

### Welcome Email Template

**Purpose**: Onboard new users effectively
**Audience**: New trial users or customers
**Tone**: Helpful guide

```
Subject: Ready to move fast when things break?

Hi [Name],

Welcome to incident.io! You're now part of a community of 500+ engineering teams who've decided that incident management doesn't have to be painful.

Here's what happens next:

**This week**: Get your first incident set up
→ Connect your monitoring tools (5 minutes)
→ Set up your first escalation policy (5 minutes)  
→ Create a test incident to see how it works (2 minutes)

**Next week**: Add your team
→ Invite your teammates
→ Set up on-call rotations
→ Configure your status page

**Questions?** Reply to this email or check out our docs at docs.incident.io. Real humans answer support questions, usually within an hour.

One more thing: we built incident.io because we were frustrated with existing tools. If something doesn't work the way you expect, please tell us. We ship fixes fast.

Welcome aboard,
[Name]
incident.io team

P.S. If you want to see how teams like Netflix and Airbnb use incident.io, check out our case studies: [link]
```

### Feature Announcement Email

**Purpose**: Announce new features to existing users
**Audience**: Current customers
**Tone**: Excited teammate sharing news

```
Subject: AI SRE is here (and it's pretty incredible)

Hi [Name],

Remember when we said AI would change incident management? Well, that future just arrived.

AI SRE is now live in your account, and it's already helping teams resolve incidents 5x faster. Here's what it does:

**Automatic Investigation**: The moment an alert fires, AI SRE starts gathering context—recent deployments, related metrics, similar past incidents, and relevant Slack conversations.

**Root Cause Identification**: Instead of spending 20 minutes figuring out what's broken, you get a detailed analysis of what likely went wrong and why.

**Fix Suggestions**: For common issues, AI SRE can draft pull requests with potential fixes or suggest specific remediation steps.

**Getting Started**: 
AI SRE is automatically enabled for all Pro and Enterprise accounts. Just create an incident like you normally would—you'll see the AI analysis appear within seconds.

**Early Results**:
"AI SRE correctly identified the root cause of our last three production issues before our senior engineer even looked at them. It's like having a really smart intern who never sleeps." - Engineering Lead, Intercom

Questions? Our team is standing by at support@incident.io.

Happy debugging,
[Name]
incident.io team

P.S. We're just getting started with AI. Reply and tell us what you'd like to see next.
```

## Social Media Templates

### Feature Announcement Tweet Template

```
🚨 New feature alert: [Feature Name] is live!

[One-sentence problem statement]

Now: [One-sentence solution]

Early users are seeing [specific metric/outcome].

Who wants to try it? 👇

[Link to blog post or docs]

#IncidentManagement #DevOps #SRE
```

### Customer Success Tweet Template

```
"[Customer quote about specific outcome]" 

- [Title], [Company]

This is why we build what we build. 

Faster incident response = better customer experience = happier engineering teams.

[Link to case study]

#CustomerSuccess #IncidentManagement
```

### Behind-the-Scenes Tweet Template

```
Behind the scenes: How we [specific technical achievement]

🧵 Thread with the technical details our engineering team loved sharing:

1/ [Problem we faced]
2/ [Initial approach that didn't work]  
3/ [What we learned]
4/ [Solution that worked]
5/ [Code snippet or technical detail]

Full writeup: [link to blog post]
```

### Technical Innovation Blog Post Template (Based on MCP Server Post)

**Purpose**: Share a specific technical solution or innovation
**Audience**: Engineers interested in implementation details and technical approaches
**Tone**: Excited colleague sharing something they built

**Perfect Example**: "We built an MCP server so Claude can access your incidents"

#### Structure Pattern:
```
1. Compelling Analogy/Hook: Paint a vivid picture of the problem
2. Problem Context: Why this matters and what's frustrating about current state
3. Solution Approach: How we decided to tackle it (honest about status/limitations)
4. Technical Implementation: Architecture details and code examples
5. Demonstration: Show it working with real, memorable examples
6. Bigger Picture: How this fits into larger trends or improvements
7. Next Steps: Clear resources and calls to action
```

#### Template Example:
```
**Hook**: "Picture this: [Vivid analogy that makes abstract problem concrete]"

**Problem Context**: "That's exactly how we felt when [specific frustration]. [Why this matters to engineers]."

**Solution Approach**: "So we built [solution]. Here's how [brief overview], and fair warning - this is [honest status assessment like 'largely experimental' or 'production-ready']."

**Technical Implementation**:
```code
// Real working code example with context
function solutionExample() {
  // Explain why this approach
  return implementation;
}
```

**Demonstration**: "Here's what this looks like in practice: [Real examples, maybe with screenshots or memorable scenarios like 'The Office incidents']"

**Bigger Picture**: "This is part of a larger trend toward [broader implication]. We think [vision for where this is heading]."

**Next Steps**: "Want to try it? [GitHub repo link]. Questions? [Contact]. Ready to see it in action? [Trial offer]."
```

#### Key Writing Techniques:
- **Authentic Language**: Use terms engineers actually use ("vibe-coded", "or don't")
- **Honest Status**: Be transparent about limitations or experimental nature
- **Brilliant Analogies**: "like having a smart colleague locked outside"
- **Working Code**: Provide real examples that readers can actually use
- **Memorable Examples**: Use fun, relatable scenarios (The Office references)
- **Clear Next Steps**: Multiple ways for readers to engage (code, trial, contact)
```

## Sales/Marketing Copy Templates

### Homepage Hero Template

```
**Headline**: [Action-oriented statement about moving fast during incidents]

**Subheadline**: [Specific outcome teams achieve - faster resolution, better communication, reduced stress]

**Body**: 
[Current state problem] → [Desired state outcome] → [How we make it possible]

**Social Proof**: 
"[Specific customer quote with metric]" - [Title], [Well-known company]

**CTA**: [Action-oriented button like "Start free trial" or "See how it works"]
```

#### Example:
```
**Headline**: Move fast when you break things

**Subheadline**: Give your team everything they need to respond quickly, reduce downtime, and keep customers in the loop.

**Body**: 
Things go wrong. All the time. But chaos doesn't have to be. incident.io turns incident response from a frantic scramble into an organized process that actually works.

From alert to resolution, your team gets AI-powered insights, automated workflows, and seamless communication tools—all integrated with Slack and the tools you already use.

**Social Proof**: 
"incident.io reduced our mean time to resolution by 60% and completely eliminated the confusion we used to have during major incidents." - Senior Engineering Manager, Netflix

**CTA**: Start your free trial
```

### Product Page Template

```
**Problem Section**:
[Specific pain point with emotional resonance]
[Why current solutions don't work]

**Solution Section**:
[How our approach is different]
[Key capabilities with specific benefits]

**How It Works**:
[3-4 step process with visuals]
[Technical details for credibility]

**Customer Stories**:
[2-3 customer quotes with specific outcomes]
[Company logos for credibility]

**Implementation**:
[How easy it is to get started]
[Integration details]
[Support available]

**Pricing**:
[Clear pricing with value justification]
[Free trial or demo option]
```

## Support/Help Content Templates

### Troubleshooting Guide Template

```
# [Specific Problem] - Troubleshooting Guide

## TL;DR
[One-sentence summary of the solution]

## Symptoms
You'll know you're experiencing this issue if:
- [Specific symptom 1]
- [Specific symptom 2]  
- [Specific symptom 3]

## Root Causes
This usually happens because:
1. [Most common cause with percentage]
2. [Second most common cause]
3. [Less common but possible cause]

## Solutions

### Quick Fix (5 minutes)
[Step-by-step instructions for immediate resolution]

### Permanent Fix (15 minutes)  
[Step-by-step instructions for preventing recurrence]

### Advanced Troubleshooting
If the above doesn't work:
[More complex diagnostic steps]

## Prevention
To avoid this in the future:
- [Specific preventive measure]
- [Configuration recommendation]
- [Monitoring suggestion]

## Still Stuck?
Contact us at support@incident.io with:
- Your account details
- Screenshots of the issue
- What you were trying to do when it happened

We typically respond within 2 hours.
```

### FAQ Template

```
## [Common Question]

**Short Answer**: [One-sentence response]

**Detailed Answer**: [Comprehensive explanation with examples]

**Related**: 
- [Link to related documentation]
- [Link to tutorial or guide]
- [Link to API reference if applicable]

**Still have questions?** Contact support@incident.io or check out our community forum.
```

## Content Quality Checklist

Before publishing any content, verify:

### Voice and Tone
- [ ] Sounds like an experienced engineer, not marketing
- [ ] Appropriate technical depth for audience
- [ ] Confident but not arrogant tone
- [ ] Specific and actionable advice

### Structure and Flow
- [ ] Starts with a problem readers recognize
- [ ] Uses progressive disclosure (TL;DR → details)
- [ ] Includes concrete examples and evidence
- [ ] Ends with clear next steps

### Technical Accuracy
- [ ] All code examples work as written
- [ ] Technical claims are verifiable
- [ ] Metrics and outcomes are specific
- [ ] References to other tools are current

### Brand Consistency  
- [ ] Uses incident.io voice and language patterns
- [ ] Differentiates appropriately from competitors
- [ ] Includes social proof when relevant
- [ ] Clear call to action where appropriate