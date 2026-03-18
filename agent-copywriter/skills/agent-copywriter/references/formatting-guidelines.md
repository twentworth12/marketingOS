# incident.io Formatting and Structure Guidelines

## Document Structure Standards

### Header Hierarchy
Use consistent header levels to create scannable content:

```markdown
# Main Title (H1) - One per document
## Section Headers (H2) - Main content sections  
### Subsection Headers (H3) - Detailed breakdowns
#### Detail Headers (H4) - Specific points or examples
```

**Header Capitalization Rule: Use sentence case, not title case**

**Example Structure:**
```markdown
# How to set up smart alert routing

## The problem with basic alerting
### Why "notify everyone" doesn't scale
### The cost of alert fatigue

## Building intelligent escalation
### Defining priority levels
### Setting up escalation paths
### Testing your configuration

## Advanced routing strategies
### Time-based routing
### Service-specific escalation
### Geographic distribution
```

**Header Capitalization Guidelines:**
- Only capitalize the first word of headers
- Capitalize proper nouns (incident.io, Slack, AI SRE)
- Keep all other words lowercase
- Exception: Quoted phrases maintain their original capitalization

### Content Flow Pattern
Follow this consistent flow for maximum readability:

1. **Hook/Problem Statement** (1-2 sentences)
2. **Context/Why It Matters** (1 paragraph)
3. **Main Content** (structured sections)
4. **Implementation/Next Steps** (actionable conclusion)
5. **Additional Resources** (links, references)

## Code and Technical Content

### Code Block Formatting
Always include language specification and context:

```python
# Good: Includes language and descriptive comment
def handle_incident_alert(alert_data):
    """
    Process incoming alert and route to appropriate team
    """
    severity = calculate_severity(alert_data)
    on_call_engineer = get_current_oncall(alert_data.service)
    
    if severity == 'critical':
        escalate_immediately(on_call_engineer, alert_data)
    else:
        queue_for_business_hours(alert_data)
```

### Inline Code
Use backticks for:
- Function names: `handle_incident_alert()`
- File paths: `config/alert_routing.yaml`
- Commands: `incident.io create --severity high`
- Technical terms: `MTTR`, `SLA`, `webhook`

### Configuration Examples
Always provide complete, working examples:

```yaml
# incident.io escalation policy configuration
escalation_policies:
  - name: "Production API"
    steps:
      - level: 1
        timeout: "5m"
        targets:
          - type: "user"
            id: "primary-oncall"
      - level: 2  
        timeout: "10m"
        targets:
          - type: "user"
            id: "secondary-oncall"
          - type: "slack"
            channel: "#incidents"
```

## Lists and Bullets

### When to Use Each List Type

**Numbered Lists**: For sequential steps or ranked items
```markdown
1. Connect your monitoring tools
2. Set up escalation policies  
3. Create your first test incident
4. Configure status page
```

**Bullet Points**: For parallel items or features
```markdown
- Real-time Slack integration
- AI-powered context gathering
- Automated customer communication
- Comprehensive incident timeline
```

**Checkbox Lists**: For actionable items or requirements
```markdown
- [ ] Slack workspace connected
- [ ] Primary on-call engineer assigned
- [ ] Escalation policy configured
- [ ] Status page customized
```

### List Formatting Rules
- Use parallel structure (all items start with verb, noun, etc.)
- Keep items roughly equal in length and complexity
- Use sub-bullets sparingly (max 2 levels deep)
- Start each item with a capital letter
- Don't end list items with periods unless they're complete sentences

## Visual Elements

### Callout Boxes
Use consistent formatting for different types of callouts:

**Important Information:**
```markdown
> **💡 Pro Tip**: You can test your escalation policy without triggering real alerts by using our test incident feature.
```

**Warnings:**
```markdown
> **⚠️ Warning**: Changing this setting will affect all active incidents. Make sure your team is aware before proceeding.
```

**Technical Notes:**
```markdown
> **🔧 Technical Note**: This integration requires admin permissions in both Slack and your monitoring tool.
```

### Tables
Use tables for structured comparisons or reference information:

```markdown
| Plan | Monthly Price | Key Features |
|------|---------------|-------------|
| Basic | Free | Single team, basic workflows |
| Team | $19/user | Multi-team, AI features |
| Pro | $25/user | Teams integration, advanced insights |
| Enterprise | Custom | SSO, dedicated support |
```

**Table Guidelines:**
- Keep column headers short and descriptive
- Align text consistently (left for text, right for numbers)
- Use "—" for unavailable features rather than leaving blank
- Include units for numerical values ($, %, etc.)

### Images and Screenshots
When including visuals:

```markdown
![Alt text describing the image](image-url)
*Caption explaining what the user should notice*
```

**Image Guidelines:**
- Always include descriptive alt text
- Add captions for complex screenshots
- Use consistent sizing and style
- Highlight relevant UI elements with arrows or boxes

## Punctuation Rules

### CRITICAL: No Em Dashes

**NEVER use em dashes (—) in any incident.io content.**

**Forbidden:**
```markdown
❌ Teams need AI that investigates—not just correlates alerts.
❌ The platform was built in 2021—by engineers who lived the problem.
❌ You have two choices: migrate to another pager—or choose the endpoint.
```

**Instead, use these alternatives:**

**1. Two sentences (preferred for clarity):**
```markdown
✅ Teams need AI that investigates. Not just correlates alerts.
✅ The platform was built in 2021. By engineers who lived the problem.
```

**2. Comma + conjunction:**
```markdown
✅ Teams need AI that investigates, not just correlates alerts.
✅ The platform was built in 2021 by engineers who lived the problem.
```

**3. Colon (for lists or explanations):**
```markdown
✅ You have two choices: migrate to another pager, or choose the endpoint.
✅ The pricing model is simple: $25/user/month with everything included.
```

**4. Parentheses (for asides):**
```markdown
✅ The platform was built in 2021 (by engineers who lived the problem).
✅ AI SRE launched in April 2025 (now in production with 150+ customers).
```

**Why this matters:** Em dashes create visual clutter and break reading flow. Our conversational authority voice works better with simple punctuation—periods, commas, and occasional colons.

---

## Links and References

### Internal Links
Link to related content to help readers go deeper:

```markdown
For more details, see our [Integration Guide](integrations-guide.md) or 
check out the [API Reference](api-reference.md).
```

### External Links
Open external links appropriately and provide context:

```markdown
You can learn more about webhooks in the 
[Slack API documentation](https://api.slack.com/messaging/webhooks).
```

### Link Text Guidelines
- Use descriptive link text, not "click here" or "read more"
- Make link purpose clear from the text itself
- Keep link text concise but informative

## Responsive Writing Structure

### TL;DR Sections
For complex topics, start with a summary:

```markdown
## Setting Up Advanced Escalation

**TL;DR**: Create multi-level escalation policies by defining timeout periods, 
backup engineers, and automatic escalation triggers. Most teams need 2-3 
escalation levels with 5-15 minute timeouts.

[Detailed explanation follows...]
```

### Progressive Disclosure
Structure content for different reader needs:

```markdown
## Quick Setup (5 minutes)
[Essential steps only]

## Complete Configuration (15 minutes)  
[All options and customization]

## Advanced Features (30 minutes)
[Power user features and automation]
```

### Scannable Formatting
Make content easy to scan:

- **Bold key terms** on first mention
- Use *italics* for emphasis, not bold
- Break up long paragraphs (max 3-4 sentences)
- Use white space generously
- Include descriptive subheaders every 2-3 paragraphs

## Content Type Specific Guidelines

### Blog Posts
```markdown  
# Engaging Title That Promises Value

*Published on [Date] by [Author]*

**TL;DR**: [One sentence summary]

[Hook paragraph - problem or interesting insight]

## Context Section
[Why this matters, background]

## Main Content
[Detailed sections with examples]

## Key Takeaways
- [Main point 1]
- [Main point 2] 
- [Main point 3]

## What's Next
[Clear call to action or next steps]

---
*Questions? Reach out to us at support@incident.io or on Twitter [@incident_io](https://twitter.com/incident_io).*
```

### Technical Documentation
```markdown
# Feature name

## Overview
[What this feature does and why you'd use it]

## Prerequisites  
- [Required permissions]
- [Required integrations]
- [Technical requirements]

## Setup instructions
### Step 1: [Action]
[Detailed instructions with screenshots]

### Step 2: [Action] 
[Detailed instructions with screenshots]

## Configuration options
| Setting | Description | Default |
|---------|-------------|---------|
| [Option] | [What it does] | [Default value] |

## Troubleshooting
### [Common problem]
**Symptoms**: [What you'll see]
**Solution**: [How to fix it]

## API reference
[If applicable - endpoints, parameters, examples]
```

### Product Announcements
```markdown
# [Feature name] is here

[Problem statement - what users struggle with today]

Today, we're launching [Feature name] to solve exactly this problem.

## What it does
[Clear explanation with benefits]

## How it works
[Technical overview with examples]

## Early results
"[Customer quote with specific outcome]" - [Title], [Company]

## Getting started
[Step-by-step instructions]

## What's next
[Future roadmap or related features]

---
*Ready to try [Feature name]? [Link to get started]*
```

## Quality Assurance Checklist

### Before Publishing
- [ ] Headers follow hierarchy (H1 → H2 → H3 → H4)
- [ ] Code blocks include language specification
- [ ] All links work and open appropriately  
- [ ] Images have descriptive alt text
- [ ] Lists use parallel structure
- [ ] Callouts use consistent formatting
- [ ] Content follows TL;DR → Details → Action structure
- [ ] Technical terms are defined or linked
- [ ] Examples are complete and accurate
- [ ] Voice matches incident.io brand guidelines

### Accessibility Standards
- [ ] Color is not the only way to convey information
- [ ] Images have meaningful alt text
- [ ] Headers create logical document outline
- [ ] Link text describes destination
- [ ] Contrast ratios meet WCAG guidelines
- [ ] Content is readable without formatting

### Mobile Optimization
- [ ] Tables don't require horizontal scrolling
- [ ] Code blocks wrap appropriately
- [ ] Images scale correctly
- [ ] Touch targets are adequately sized
- [ ] Content hierarchy works on small screens

## File Organization

### Naming Conventions
```
blog-posts/
├── 2025-01-15-ai-sre-launch.md
├── 2025-01-20-incident-response-best-practices.md
└── 2025-02-01-monitoring-integration-guide.md

documentation/
├── getting-started.md
├── api-reference.md
├── integrations/
│   ├── slack-integration.md
│   ├── datadog-integration.md
│   └── webhook-setup.md
└── troubleshooting/
    ├── common-issues.md
    └── api-errors.md
```

### Metadata Standards
Include consistent frontmatter:

```yaml
---
title: "How to Set Up Smart Alert Routing"
author: "Engineering Team"
date: "2025-01-15"
category: "Technical Guide"
tags: ["alerts", "configuration", "best-practices"]
audience: ["engineers", "sre"]
difficulty: "intermediate"
estimated_time: "15 minutes"
---
```

This formatting guide ensures all incident.io content maintains consistency, readability, and professional quality while supporting our brand voice and user experience goals.