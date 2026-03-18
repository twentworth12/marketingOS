# Netflix Case Study: Incident Management at Scale

## Customer
**Netflix**

## Industry
Media & Entertainment / Streaming Technology

## Problem/Challenge

Netflix's incident management process wasn't scaling effectively with organizational growth. Key challenges included:

- Operating incidents through a single Slack channel and Jira, which lacked proper incident management UX
- Difficulty achieving a "paved road to incident management" that would be accessible to all engineers
- Inconsistent processes across thousands of engineers with varying experience levels
- Lack of contextual information during critical incident response situations
- CORE team handling ~90% of declared incidents across the organization

As Hank Jacobs noted: *"The ergonomics of Jira for declaring and managing an incident just weren't there."*

## Solution

Netflix adopted **incident.io** as their unified incident management platform, motivated by:

- Superior user experience and intuitive design
- Ability to democratize incident response across engineering teams
- **Catalog** feature for embedding Netflix-specific context directly into the tool
- Partnership approach with incident.io team committed to collaborative growth

## Results & Outcomes

### Cultural Impact
- Increased cross-organizational visibility of incidents at all severity levels
- Shifted from siloed incident discussions to company-wide learning culture
- Organic adoption well beyond initial CORE team rollout

### Operational Improvements
- Teams now own their own incident management processes
- Automated incident creation and team routing through Catalog integration
- Reduced incident duration through faster context and team activation

### Catalog Adoption
- **25 internal status pages** created for team-to-team communication
- Tens of thousands of entities in Catalog (largest user of the feature)
- Integration with internal systems for automated developer-impacting incident flagging
- Catalog Importer syncing all Netflix services automatically

## Key Quotes

*"What stood out about incident.io was that you hardly had to explain it. The tool's seamless UI let you discover features you needed."* — Molly Struve, Staff SRE

*"The ability to bring Netflix-specific context into the tool and have it appear in the product was a pivotal moment."* — Hank Jacobs, Staff SRE

*"I'll wake up the next day, and in some cases, it'll be implemented in the product. That's amazing."* — Hank Jacobs

## Additional Details

- **Team Size**: CORE (Critical Operations and Reliability Engineering) - small team supporting 300 million Netflix users
- **Build vs. Buy Decision**: Netflix evaluated building in-house but determined that investment and ongoing ownership costs made purchasing the better choice
- **Partnership Model**: Daily collaboration between Netflix and incident.io teams with rapid iteration and shared vision for incident management excellence

**Source:** https://incident.io/customers/netflix
