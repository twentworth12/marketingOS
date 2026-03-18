# Favor Customer Case Study

## Company Overview

**Company**: Favor Delivery
**Industry**: Food & Grocery Delivery
**Region**: Texas (H-E-B subsidiary)
**Use Case**: Complex logistics coordination for drivers, merchants, and customers

## Executive Summary

Favor, a food delivery subsidiary of H-E-B operating across Texas, transformed their incident management by implementing incident.io. They achieved a **37% MTTR reduction** while increasing incident detection by 214%, demonstrating how proper tooling improves both speed and visibility.

## The Challenge

### Incident Coordination Breakdown

Favor's incident response required 20-30 minutes of manual setup before troubleshooting could begin. Director of Engineering Ross McKelvie described the chaos: managing incidents across "two different Zoom calls running and two laptops open," manually routing communications between teams.

### Tooling Fragmentation

Favor's fragmented tooling stack created operational inefficiencies:
- **OpsGenie** handled alerting
- **Status Page** required separate logins and licenses
- No integration between tools despite both being Atlassian products

Principal SRE Abbas Bandali noted: "These are both Atlassian products, and they didn't play well together."

The lack of integration meant:
- Manual coordination between alerting and status updates
- No automated routing to appropriate teams
- Constant manual updates when team structures changed
- Engineers spending time on tool management instead of incident resolution

## The Solution

### incident.io Implementation

Favor discovered incident.io addressed their operational gaps with automation they "didn't even think to automate" according to McKelvie.

**Implementation Scope:**
- Engineering teams (primary use case)
- Operations teams (POS outages)
- Trust & Safety teams (security issues)

**Key Integration: Service Catalog**

The service catalog integration automatically routes alerts to appropriate teams, eliminating manual configuration updates when teams reorganize. This single feature removed a recurring operational burden.

## Measurable Results

### Performance Metrics

- **37% MTTR reduction** - Nearly 40% improvement in mean time to resolution
- **214% increase in incident detection** - Better visibility into system issues
- **2-to-1 ratio flip** - Automatic incident creation now outpaces user-reported incidents
- **Fewer critical incidents** - Despite higher overall detection, critical incidents decreased

### What the Metrics Mean

The dramatic increase in incident detection combined with fewer critical incidents reveals a crucial insight: Favor now catches problems earlier before they escalate. The automation doesn't just speed up response—it prevents customer impact entirely.

## Organizational Impact

### Improved Transparency

**Customer-Facing Teams:**
- Monitor incident progress directly in Slack
- No longer need to interrupt engineers for status updates
- Self-service visibility into resolution progress

**Leadership:**
- Gained visibility into incident patterns and resolution metrics
- No additional communication overhead required
- Data-driven insights into system reliability

### Cross-Functional Adoption

The platform expanded beyond engineering:
- **Operations**: POS system outages
- **Trust & Safety**: Security incident response
- **Customer Support**: Real-time incident status for customer inquiries

## Key Success Factors

1. **Automation Beyond Expectations** - McKelvie's comment about "automating things we didn't even think to automate" reveals how comprehensive the platform's capabilities are

2. **Service Catalog Intelligence** - Automatic routing eliminated manual team configuration, a recurring pain point

3. **Slack-Native Architecture** - Incident response happens where teams already work, eliminating tool switching

4. **Cross-Functional Scalability** - Platform proved valuable beyond engineering to operations and security teams

## Customer Quotes

> "We were managing incidents across two different Zoom calls running and two laptops open, manually routing communications."
> — **Ross McKelvie**, Director of Engineering

> "These are both Atlassian products, and they didn't play well together."
> — **Abbas Bandali**, Principal SRE (referring to OpsGenie and Status Page)

> "incident.io was automating things we didn't even think to automate."
> — **Ross McKelvie**, Director of Engineering

## Use This Case Study For

- **MTTR reduction proof points** - 37% improvement is substantial and verified
- **Tool consolidation arguments** - Favor replaced OpsGenie + Status Page fragmentation
- **Proactive detection positioning** - 214% increase in incidents but fewer critical ones
- **Cross-functional adoption** - Operations and Trust & Safety teams adopted beyond engineering
- **Service catalog value** - Automatic routing eliminated manual configuration burden

## Related Case Studies

- Intercom (PagerDuty migration)
- Netflix (AI SRE proof of concept)
- AudioStack (workflow automation)

## Source

https://incident.io/customers/favor

**Last Updated**: November 2025
