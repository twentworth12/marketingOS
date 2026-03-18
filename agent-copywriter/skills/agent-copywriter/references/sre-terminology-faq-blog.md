# The complete SRE terminology guide: Every term engineers actually need to know

*A practical FAQ covering incident response, on-call, observability, and reliability engineering concepts*

---

**Blog Index Description:** A comprehensive guide to Site Reliability Engineering terminology, from AI SRE and MTTR to runbooks and escalation policies. Written by engineers, for engineers who want clear definitions and practical context.

---

## TL;DR: Key SRE terms you should know

1. **SRE (Site Reliability Engineering):** Engineering discipline focused on building and maintaining reliable systems at scale, using software engineering to solve operations problems
2. **AI SRE:** AI-powered systems that investigate incidents, identify root causes, and suggest fixes alongside human engineers
3. **MTTR (Mean Time to Resolution):** Average time from incident detection to complete resolution - the metric that matters most for measuring incident response effectiveness
4. **On-call:** System for ensuring someone is always available to respond to incidents, typically organized in rotating schedules
5. **SLA/SLO/SLI:** The reliability hierarchy - SLIs measure performance, SLOs set internal targets, SLAs are external commitments with consequences
6. **Runbook:** Step-by-step documentation for handling specific incidents or operational tasks
7. **Post-mortem:** Blameless analysis conducted after incidents to understand what happened and prevent recurrence
8. **Escalation policy:** Rules defining who gets notified when, and in what order, during an incident
9. **Alert fatigue:** Desensitization from too many alerts, leading to missed critical issues
10. **Observability:** The ability to understand system state from external outputs - goes beyond monitoring to include logs, metrics, and traces

---

## What is SRE (Site Reliability Engineering)?

**Site Reliability Engineering (SRE) is an engineering discipline that applies software engineering practices to infrastructure and operations problems.** Originally developed at Google in 2003, SRE teams are responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of production systems.

SRE differs from traditional operations in several key ways:

1. **Software-first approach:** SREs write code to automate operational tasks rather than performing them manually
2. **Error budgets:** Teams accept that 100% reliability is impossible and budget for acceptable failure rates
3. **Blameless culture:** Focus on system improvements rather than individual blame when things go wrong
4. **Shared ownership:** SREs work alongside development teams, not as a separate support function

**In practice:** An SRE team might spend 50% of their time on operational work (incident response, on-call, manual tasks) and 50% on engineering projects that improve reliability, such as building better monitoring, automating toil, or improving deployment pipelines.

**Why it matters:** According to the 2025 State of DevOps report, organizations with mature SRE practices achieve 4x faster deployment frequency and 3x lower change failure rates compared to those without dedicated reliability engineering.

---

## What is AI SRE?

**AI SRE refers to artificial intelligence systems designed to investigate incidents, identify root causes, and suggest fixes alongside human engineers.** Unlike basic automation that follows predefined rules, AI SRE uses machine learning to analyze patterns across logs, metrics, code changes, and historical incidents to accelerate investigation and resolution.

Modern AI SRE systems typically provide five core capabilities:

1. **Automated investigation:** Scans logs, metrics, Slack conversations, and recent deployments the moment an incident is detected
2. **Root cause identification:** Correlates symptoms with potential causes using historical incident data and system knowledge
3. **Fix suggestions:** Generates deployment-ready code changes, configuration updates, or rollback recommendations
4. **Post-mortem drafting:** Creates structured incident documentation from communication trails and system data
5. **Context preservation:** Maintains organizational knowledge about past incidents and resolution patterns

**Real-world performance:** Teams using AI-powered incident investigation report 60-80% reductions in context-gathering time. Instead of spending the first 15-30 minutes of an incident manually searching logs and asking "what changed recently?" in Slack, AI SRE surfaces relevant information within 30 seconds.

**Key distinction:** AI SRE acts as a knowledgeable teammate that investigates alongside you, not a replacement for human judgment. The goal is automating the first 80% of incident response - the repetitive context-gathering and correlation work - so engineers can focus on the complex decision-making that requires human expertise.

---

## What is on-call?

**On-call is a scheduling system that ensures someone is always available to respond to incidents affecting production systems.** Engineers on-call are responsible for acknowledging alerts, triaging issues, and either resolving incidents themselves or escalating to appropriate team members.

A well-designed on-call system includes:

1. **Rotating schedules:** Distributing responsibility across team members to prevent burnout, typically in 1-week or 2-week rotations
2. **Follow-the-sun coverage:** For global teams, rotating on-call duties across time zones so no one works overnight
3. **Shadow rotations:** Pairing newer engineers with experienced responders for training
4. **Escalation policies:** Clear rules for who gets notified if the primary responder doesn't acknowledge an alert
5. **Override capabilities:** Mechanisms for swapping shifts when conflicts arise

**On-call compensation considerations:**
- Many organizations provide additional pay for on-call shifts (typically 10-20% bonus or per-incident payments)
- Some companies offer compensatory time off after heavy on-call periods
- Clear escalation paths and reasonable alert volumes are often more valued than monetary compensation

**Industry benchmark:** According to analysis of 10,000+ engineering teams, healthy on-call rotations see 2-5 pages per week per engineer. Teams experiencing more than 10 pages per week typically suffer from alert fatigue and burnout.

---

## What is the difference between SLA, SLO, and SLI?

**SLA, SLO, and SLI form a hierarchy for measuring and committing to system reliability.** SLIs measure actual performance, SLOs set internal targets, and SLAs are external promises with consequences.

### SLI (Service Level Indicator)

**An SLI is a quantitative measurement of a specific aspect of service performance.** It's the actual data point you measure.

Common SLIs include:
- **Availability:** Percentage of time the service responds successfully (e.g., 99.95%)
- **Latency:** Response time at various percentiles (e.g., p99 latency under 200ms)
- **Error rate:** Percentage of requests that fail (e.g., error rate below 0.1%)
- **Throughput:** Requests processed per second

### SLO (Service Level Objective)

**An SLO is an internal target for an SLI that your team commits to maintaining.** It defines "good enough" reliability for your service.

Example: "Our API should have 99.9% availability measured over a 30-day rolling window."

**Error budgets:** The gap between your SLO and 100% becomes your error budget. If your SLO is 99.9% availability, you have a 0.1% error budget - approximately 43 minutes of downtime per month. Teams use error budgets to balance reliability work against feature development.

### SLA (Service Level Agreement)

**An SLA is a contract with customers that specifies minimum performance levels and consequences for missing them.** SLAs should always be less aggressive than your SLOs to provide buffer.

Example: "We guarantee 99.5% API availability. If we fail to meet this, affected customers receive 10% service credits."

**The relationship in practice:**
```
SLI: We measured 99.94% availability this month
SLO: Our target is 99.9% availability (we're meeting it)
SLA: We promise customers 99.5% availability (comfortable margin)
```

---

## What is incident response?

**Incident response is the process of detecting, investigating, communicating about, and resolving service disruptions.** Effective incident response minimizes customer impact, reduces recovery time, and captures learnings to prevent recurrence.

A mature incident response process includes these phases:

1. **Detection:** Monitoring systems identify anomalies and trigger alerts
2. **Triage:** On-call engineer assesses severity and decides whether to escalate
3. **Response:** Team assembles, investigates root cause, and implements fixes
4. **Communication:** Stakeholders and customers receive status updates
5. **Resolution:** Service returns to normal operation
6. **Learning:** Post-mortem analysis captures insights for improvement

### Incident severity levels

Most organizations use 4-5 severity levels:

| Severity | Description | Response Expectation |
|----------|-------------|---------------------|
| **SEV1/Critical** | Complete service outage, major data loss | All-hands response, executive notification |
| **SEV2/High** | Significant degradation, major feature unavailable | Immediate response, broad team engagement |
| **SEV3/Medium** | Minor impact, workarounds available | Response within 1-2 hours during business hours |
| **SEV4/Low** | Minimal impact, single user affected | Next business day response |

**Best practices for incident response:**
- Declare incidents early - it's better to over-communicate than under-communicate
- Assign clear roles: incident commander, communications lead, technical lead
- Use dedicated incident channels to centralize communication
- Document decisions and actions as they happen, not after
- Time-box investigation before escalating

---

## What is MTTR (Mean Time to Resolution)?

**MTTR (Mean Time to Resolution) is the average time from when an incident is detected to when it's fully resolved.** It's the primary metric for measuring incident response effectiveness and directly correlates with customer impact.

MTTR is one of four key incident metrics:

1. **MTTD (Mean Time to Detect):** Time from failure occurrence to detection
2. **MTTA (Mean Time to Acknowledge):** Time from alert to human acknowledgment
3. **MTTM (Mean Time to Mitigate):** Time to implement temporary fix or workaround
4. **MTTR (Mean Time to Resolve):** Time to complete, permanent resolution

### MTTR calculation

```
MTTR = Total resolution time for all incidents / Number of incidents

Example:
- Incident 1: 45 minutes
- Incident 2: 120 minutes
- Incident 3: 30 minutes
- Incident 4: 90 minutes

MTTR = (45 + 120 + 30 + 90) / 4 = 71.25 minutes
```

**Industry benchmarks for MTTR:**

| Team Maturity | Typical MTTR (SEV1) | Typical MTTR (SEV2) |
|--------------|---------------------|---------------------|
| Early-stage | 2-4 hours | 4-8 hours |
| Maturing | 30-60 minutes | 1-2 hours |
| Advanced | Under 15 minutes | Under 30 minutes |

**Strategies to reduce MTTR:**
1. Improve detection speed with better monitoring and alerting
2. Automate context gathering to reduce investigation time
3. Pre-build runbooks for common failure modes
4. Practice incident response through game days and drills
5. Use AI-powered investigation to surface relevant information faster

**Critical insight:** Teams that invest in reducing MTTD and MTTA often see the biggest MTTR improvements. Many incidents could be resolved in minutes if detected and acknowledged faster.

---

## What is a runbook?

**A runbook is a documented set of step-by-step procedures for handling specific incidents, operational tasks, or maintenance activities.** Good runbooks transform tribal knowledge into repeatable processes that any trained team member can execute.

### Effective runbook structure

1. **Overview:** What this runbook addresses and when to use it
2. **Prerequisites:** Required access, tools, or knowledge
3. **Steps:** Numbered actions with expected outcomes
4. **Verification:** How to confirm the procedure worked
5. **Escalation:** When and who to contact if steps don't resolve the issue
6. **Related documentation:** Links to architecture diagrams, monitoring dashboards, or related runbooks

### Runbook example format

```markdown
# Database Connection Pool Exhaustion

## Symptoms
- Spike in "connection timeout" errors
- Application logs showing "unable to acquire connection"
- Database connections at max_pool_size limit

## Resolution Steps

1. Verify the issue
   - Check Grafana dashboard: [link]
   - Expected: connection_pool_active > 95%

2. Identify the cause
   - Check for long-running queries: SELECT * FROM pg_stat_activity WHERE state != 'idle';
   - Check for connection leaks in recent deployments

3. Immediate mitigation
   - Kill long-running queries if safe: SELECT pg_terminate_backend(pid);
   - Restart affected application pods: kubectl rollout restart deployment/api

4. Verify resolution
   - Confirm connection pool utilization drops below 80%
   - Confirm error rate returns to baseline

## Escalation
If issue persists after step 3, escalate to database team via #db-oncall
```

**Runbook maintenance tips:**
- Review and update runbooks after every incident where they're used
- Delete outdated runbooks that no longer apply
- Link runbooks directly to alerts so responders find them immediately
- Test runbooks during incident drills to identify gaps

---

## What is a post-mortem (or postmortem)?

**A post-mortem is a structured analysis conducted after an incident to understand what happened, why it happened, and how to prevent similar incidents in the future.** Also called incident reviews, retrospectives, or learning reviews, effective post-mortems focus on system improvements rather than individual blame.

### Key principles of blameless post-mortems

1. **Assume good intent:** Everyone involved was trying to do the right thing with the information they had
2. **Focus on systems, not people:** Ask "what allowed this to happen?" not "who made the mistake?"
3. **Seek multiple causes:** Incidents rarely have a single root cause - look for contributing factors
4. **Prioritize learning over punishment:** The goal is preventing recurrence, not assigning blame

### Post-mortem template structure

```markdown
# Incident Post-Mortem: [Incident Title]

## Summary
[2-3 sentence description of what happened and impact]

## Timeline
- 14:32 - Alert fired for elevated error rates
- 14:35 - On-call engineer acknowledged
- 14:42 - Root cause identified (bad config deployed)
- 14:48 - Config rolled back
- 14:52 - Service recovered

## Root Cause Analysis
[Detailed explanation of what went wrong and why]

## Impact
- Duration: 20 minutes
- Users affected: ~5,000
- Revenue impact: Estimated $2,000 in failed transactions

## What Went Well
- Alert fired within 3 minutes of issue start
- Clear runbook for config rollback

## What Could Be Improved
- Config change lacked automated testing
- No canary deployment for config changes

## Action Items
1. [Owner: Alice] Add automated config validation - Due: Jan 15
2. [Owner: Bob] Implement config canary deployments - Due: Jan 30
3. [Owner: Carol] Update runbook with new validation steps - Due: Jan 10
```

**Post-mortem best practices:**
- Conduct post-mortems within 24-72 hours while details are fresh
- Include everyone involved in the incident, plus relevant stakeholders
- Track action items to completion - the post-mortem isn't done until fixes are implemented
- Share learnings broadly so other teams can benefit

---

## What is an escalation policy?

**An escalation policy defines who gets notified about an incident, in what order, and through what channels.** Well-designed escalation policies ensure the right people are engaged quickly without overwhelming teams with unnecessary alerts.

### Escalation policy components

1. **Primary responder:** First person notified, typically current on-call
2. **Escalation layers:** Who to notify if primary doesn't acknowledge
3. **Time delays:** How long to wait before escalating (typically 5-15 minutes)
4. **Notification methods:** How to reach each responder (push notification, SMS, phone call)
5. **Severity-based routing:** Different policies for different incident severities

### Example escalation policy

```
Alert triggers →

Layer 1 (0 min): Primary on-call
  - Push notification + SMS
  - If no acknowledgment in 5 minutes...

Layer 2 (5 min): Secondary on-call
  - Push notification + SMS + Phone call
  - If no acknowledgment in 10 minutes...

Layer 3 (15 min): Engineering manager + Primary on-call (again)
  - Phone call to manager
  - Escalate to #engineering-urgent Slack channel

Layer 4 (30 min): VP Engineering + Incident commander on-call
  - Phone call
  - Page entire team
```

### Escalation policy best practices

1. **Match urgency to severity:** SEV1 incidents should escalate faster and more aggressively
2. **Use multiple notification channels:** Don't rely solely on push notifications - they get missed
3. **Include override contacts:** Have a way to reach specific subject matter experts for complex issues
4. **Test regularly:** Run escalation drills to verify policies work as expected
5. **Review after incidents:** Update policies based on real-world performance

**Common mistake:** Making escalation too slow. If your primary on-call doesn't respond to a SEV1 incident, waiting 15 minutes to escalate can mean significant additional customer impact.

---

## What is alert fatigue?

**Alert fatigue is the desensitization that occurs when on-call engineers receive too many alerts, leading to slower response times, missed critical issues, and eventual burnout.** It's one of the most common causes of incident response failures.

### Symptoms of alert fatigue

1. **High alert volume:** More than 5-10 alerts per on-call shift
2. **Low acknowledgment rates:** Alerts being auto-closed or ignored
3. **Delayed response times:** Growing gap between alert and acknowledgment
4. **Alert suppression:** Engineers muting or disabling alerts
5. **Burnout indicators:** On-call avoidance, reduced morale, increased turnover

### Causes of alert fatigue

| Cause | Example | Solution |
|-------|---------|----------|
| **False positives** | Alert fires but no actual issue | Tune thresholds, add correlation |
| **Duplicate alerts** | Same issue triggers 10 alerts | Implement alert deduplication |
| **Low-urgency alerts** | Non-actionable notifications during on-call | Route to async channels |
| **Missing context** | Alert provides no investigation path | Include runbook links, context |
| **Alert sprawl** | Alerts never cleaned up | Regular alert hygiene reviews |

### Strategies to reduce alert fatigue

1. **Apply the "3 AM test":** Would you want to be woken up for this alert? If not, it shouldn't page
2. **Require runbooks:** Every paging alert must link to actionable documentation
3. **Track signal-to-noise ratio:** Monitor what percentage of alerts lead to real incidents
4. **Implement intelligent grouping:** Correlate related alerts into single incidents
5. **Regular alert reviews:** Quarterly audits to remove or tune low-value alerts
6. **Use AI-powered filtering:** Machine learning can identify and suppress likely false positives

**Industry benchmark:** Elite teams maintain less than 5 pages per on-call engineer per week, with over 80% of alerts being actionable.

---

## What is the difference between monitoring and observability?

**Monitoring tracks known failure modes through predefined metrics and thresholds, while observability provides the ability to understand any system state - including novel failures - by examining outputs like logs, metrics, and traces.**

### Monitoring

**Monitoring answers the question: "Is the system working?"**

- Uses predefined metrics and alert thresholds
- Effective for known failure modes
- Dashboard-driven approach
- Example: "Alert when CPU exceeds 90%"

**Limitations:** Monitoring only catches issues you've anticipated. If a new failure mode occurs that doesn't trip existing alerts, you won't know until customers report problems.

### Observability

**Observability answers the question: "Why is the system behaving this way?"**

Built on three pillars:

1. **Metrics:** Numerical measurements over time (CPU usage, request rate, error count)
2. **Logs:** Discrete events with contextual information (error messages, request details)
3. **Traces:** End-to-end request paths showing how services interact

**Key capability:** With proper observability, you can investigate issues you've never seen before by asking arbitrary questions of your telemetry data.

### Comparison

| Aspect | Monitoring | Observability |
|--------|-----------|---------------|
| **Approach** | Predefined checks | Exploratory investigation |
| **Question** | "Is it broken?" | "Why is it broken?" |
| **Coverage** | Known failure modes | Unknown failure modes |
| **Data** | Aggregated metrics | High-cardinality data |
| **Tools** | Dashboards, alerts | Log analysis, distributed tracing |

**Practical insight:** You need both. Monitoring tells you something is wrong; observability helps you figure out what. Teams often start with monitoring and add observability capabilities as their systems grow more complex.

---

## What is an error budget?

**An error budget is the maximum amount of unreliability your service can have while still meeting its Service Level Objective (SLO).** It's calculated as 100% minus your SLO target, and it creates a shared framework for balancing reliability work against feature development.

### Error budget calculation

```
If your SLO is 99.9% availability:
Error budget = 100% - 99.9% = 0.1%

In a 30-day month:
0.1% of 30 days = 43.2 minutes of allowed downtime
```

### How error budgets work in practice

**When error budget is healthy (plenty remaining):**
- Teams can move faster on feature development
- Lower-risk deployments can proceed without extensive review
- Engineering focus shifts toward new capabilities

**When error budget is depleted:**
- Feature work pauses until reliability improves
- All engineering effort focuses on stability
- Deployment freeze may be implemented
- Post-mortems prioritized for recent incidents

### Error budget policies

| Error Budget Status | Development Velocity | Risk Tolerance |
|--------------------|---------------------|----------------|
| >50% remaining | Full speed | Normal deployment process |
| 25-50% remaining | Moderate caution | Additional review for risky changes |
| 10-25% remaining | Slow down | Only low-risk changes allowed |
| <10% remaining | Freeze | Reliability work only |

**Why error budgets matter:** They eliminate the traditional tension between "ship faster" and "be more reliable" by creating objective criteria. Instead of arguing about whether to delay a feature for reliability work, the error budget provides a clear answer.

---

## What is toil?

**Toil is manual, repetitive, automatable work that scales linearly with system size and provides no enduring value.** In SRE, eliminating toil is a primary objective because it frees engineers to focus on work that improves systems rather than just maintaining them.

### Characteristics of toil

Work qualifies as toil if it has these attributes:

1. **Manual:** Requires human intervention rather than running automatically
2. **Repetitive:** Done over and over again (not a one-time project)
3. **Automatable:** Could theoretically be handled by software
4. **Reactive:** Triggered by external events rather than planned
5. **No enduring value:** Doesn't improve the system's long-term state
6. **Scales linearly:** More users/traffic means more of this work

### Examples of toil

| Toil | Not Toil |
|------|----------|
| Manually restarting crashed services | Building auto-restart capability |
| Provisioning accounts by hand | Creating self-service provisioning |
| Running manual deployments | Implementing CI/CD pipelines |
| Responding to capacity alerts by adding resources | Building auto-scaling |
| Manually rotating credentials | Automating credential rotation |

### The 50% rule

**Google SRE recommends that SRE teams spend no more than 50% of their time on toil.** The other 50% should go toward engineering projects that reduce future toil or improve reliability.

**Tracking toil:** Many teams categorize their work weekly to ensure toil doesn't exceed healthy levels. If toil consistently exceeds 50%, it signals a need for more automation investment.

---

## What is incident severity?

**Incident severity is a classification system that indicates the urgency and impact of an incident, determining response speed, communication requirements, and resource allocation.** Consistent severity classification ensures appropriate response effort and helps prioritize when multiple incidents occur simultaneously.

### Common severity levels

| Level | Name | Definition | Typical Response |
|-------|------|------------|------------------|
| **SEV1** | Critical | Complete outage or data loss affecting all users | Immediate all-hands response, executive notification, status page update |
| **SEV2** | High | Major feature unavailable or significant performance degradation | Immediate response, team-wide notification |
| **SEV3** | Medium | Minor impact with workarounds available | Response within 1-2 hours, standard on-call handling |
| **SEV4** | Low | Minimal impact, single user or cosmetic issue | Next business day, may be handled as bug ticket |

### Severity determination factors

1. **Customer impact:** How many users are affected?
2. **Business impact:** What's the revenue or reputation cost?
3. **Scope:** Is it total outage or partial degradation?
4. **Duration:** How long will it take to resolve?
5. **Workarounds:** Can users accomplish their goals another way?

### Severity escalation and de-escalation

**Escalate severity when:**
- Impact is worse than initially assessed
- Resolution is taking longer than expected
- Additional customers or services are affected

**De-escalate severity when:**
- Workaround is implemented
- Impact is contained
- Partial resolution reduces urgency

**Best practice:** When uncertain, err toward higher severity. It's easier to de-escalate a well-managed incident than to recover from an under-resourced response.

---

## What is a service catalog?

**A service catalog is a structured inventory of all services in your organization, including their owners, dependencies, runbooks, and metadata.** It serves as the single source of truth for understanding what you're running and who's responsible for it.

### Service catalog contents

A comprehensive service catalog entry includes:

1. **Service identity:** Name, description, tier/criticality
2. **Ownership:** Team responsible, primary contacts, escalation paths
3. **Dependencies:** What this service depends on and what depends on it
4. **Runbooks:** Links to operational documentation
5. **Monitoring:** Dashboard links, key metrics, alert configurations
6. **Documentation:** Architecture diagrams, API docs, deployment guides
7. **Metadata:** Language, repository, deployment environment

### Service catalog benefits

| Benefit | Description |
|---------|-------------|
| **Faster incident response** | Instantly find the right team to contact |
| **Dependency awareness** | Understand blast radius of failures |
| **Onboarding acceleration** | New team members quickly understand the system |
| **Audit compliance** | Track ownership and changes for compliance |
| **Automation foundation** | Power workflows with accurate service data |

**Integration with incident response:** When an incident occurs, the service catalog can automatically identify the owning team, surface relevant runbooks, and map potential impact to dependent services.

---

## What is chaos engineering?

**Chaos engineering is the practice of intentionally introducing failures into production systems to test resilience and uncover weaknesses before they cause real incidents.** Rather than waiting for systems to fail unexpectedly, chaos engineering proactively validates that systems can handle adverse conditions.

### Chaos engineering principles

1. **Start with a hypothesis:** Define expected behavior under failure conditions
2. **Minimize blast radius:** Begin with small, contained experiments
3. **Run in production:** Test real systems, not just staging environments
4. **Automate experiments:** Make chaos testing repeatable and continuous
5. **Build confidence gradually:** Start simple and increase complexity over time

### Common chaos experiments

| Experiment | Tests For | Example |
|-----------|-----------|---------|
| **Server termination** | Auto-scaling, failover | Randomly kill EC2 instances |
| **Network latency** | Timeout handling | Add 500ms delay to service calls |
| **Dependency failure** | Graceful degradation | Block traffic to database |
| **Resource exhaustion** | Capacity limits | Fill disk, exhaust memory |
| **Zone outage** | Multi-AZ resilience | Disable entire availability zone |

### Chaos engineering process

```
1. Define steady state (normal system behavior)
2. Hypothesize that steady state will continue during experiment
3. Introduce failure (server crash, network partition, etc.)
4. Observe system behavior
5. Either confirm hypothesis or discover weakness
6. Fix weaknesses and repeat
```

**Key insight:** Chaos engineering isn't about breaking things for fun - it's about building confidence in your system's ability to handle real-world failures. The goal is finding weaknesses in controlled conditions rather than during actual incidents.

---

## What is an incident commander?

**An incident commander (IC) is the designated leader responsible for coordinating an incident response, making decisions, and ensuring effective communication.** The IC doesn't need to be the most technical person - their role is coordination and decision-making, not debugging.

### Incident commander responsibilities

1. **Coordinate response:** Ensure the right people are working on the right problems
2. **Make decisions:** Break deadlocks and choose between competing priorities
3. **Manage communication:** Ensure stakeholders receive timely updates
4. **Track progress:** Maintain incident timeline and current status
5. **Escalate when needed:** Bring in additional resources or expertise
6. **Call resolution:** Declare when the incident is over

### IC best practices

**Do:**
- Delegate technical investigation to subject matter experts
- Maintain a single source of truth for incident status
- Set clear expectations for update frequency
- Document key decisions and rationale
- Protect responders from external interruptions

**Don't:**
- Get pulled into deep technical debugging
- Make major architectural decisions during the incident
- Forget to communicate with stakeholders
- Assume everyone knows what's happening
- Skip handoffs when rotating IC responsibilities

**Rotating the IC role:** During long incidents, IC responsibilities should transfer between engineers to prevent fatigue. Clear handoffs with status summaries ensure continuity.

---

## What is mean time to detect (MTTD)?

**Mean Time to Detect (MTTD) is the average time between when a failure occurs and when it's detected by monitoring systems or users.** MTTD is often the largest hidden contributor to overall incident duration - you can't fix what you don't know is broken.

### MTTD calculation

```
MTTD = Time of detection - Time of failure

Example:
- Failure occurred: 14:00:00
- Alert fired: 14:03:30
- MTTD: 3 minutes 30 seconds
```

### Factors affecting MTTD

| Factor | Impact on MTTD |
|--------|---------------|
| **Alert sensitivity** | Tighter thresholds detect faster but increase false positives |
| **Monitoring coverage** | Blind spots create detection gaps |
| **Alert routing** | Misconfigured routing delays notification |
| **Health check frequency** | Longer intervals mean longer detection time |
| **Synthetic monitoring** | User-journey tests catch issues before real users |

### Strategies to reduce MTTD

1. **Implement synthetic monitoring:** Continuously test critical user journeys
2. **Use anomaly detection:** ML-based systems can identify unusual patterns faster than static thresholds
3. **Monitor SLIs directly:** Alert on customer-facing metrics, not just infrastructure
4. **Reduce check intervals:** More frequent health checks mean faster detection
5. **Add redundant detection:** Multiple independent systems watching for the same issues

**Industry benchmark:** Elite teams achieve MTTD under 5 minutes for critical issues. Most organizations operate in the 10-30 minute range.

---

## What is a game day?

**A game day is a planned exercise where teams practice incident response by responding to simulated or real failures in a controlled environment.** Game days build muscle memory, identify process gaps, and ensure teams can respond effectively under pressure.

### Game day types

| Type | Description | Best For |
|------|-------------|----------|
| **Tabletop exercise** | Discussion-based scenario walkthrough | Process validation, new team training |
| **Simulation** | Realistic scenario with mocked failures | Testing runbooks and coordination |
| **Live fire** | Real failures in production | Validating actual system resilience |

### Game day structure

```
1. Preparation (1-2 weeks before)
   - Define scenario and objectives
   - Identify participants
   - Prepare monitoring and communication channels

2. Execution (2-4 hours)
   - Brief participants on rules and objectives
   - Inject failure scenario
   - Observe response without intervention
   - Call exercise when objectives are met

3. Debrief (1 hour)
   - Review timeline and decisions
   - Identify gaps and improvements
   - Document findings
   - Assign follow-up actions
```

### Game day best practices

1. **Start with tabletop exercises** before attempting live fire drills
2. **Include realistic pressure** but maintain psychological safety
3. **Rotate participants** so everyone gets practice
4. **Document everything** for learning and improvement
5. **Celebrate success** while addressing gaps constructively

**Frequency:** Most mature organizations run game days quarterly, with tabletop exercises monthly.

---

## What is an SRE team structure?

**SRE teams can be organized in several models depending on company size, technical complexity, and organizational culture.** There's no single correct structure - the best approach depends on your specific context.

### Common SRE team models

**1. Centralized SRE**
- Single SRE team serves all product teams
- Best for: Small-to-medium organizations
- Pros: Consistent practices, efficient resource use
- Cons: Can become bottleneck, less product context

**2. Embedded SRE**
- SREs embedded within product teams
- Best for: Organizations with diverse, complex products
- Pros: Deep product knowledge, close collaboration
- Cons: Inconsistent practices, harder to share learnings

**3. Platform SRE**
- SRE team builds platform used by all product teams
- Best for: Large organizations with many similar services
- Pros: Scalable, self-service capabilities
- Cons: Less direct support, platform may not fit all needs

**4. Hybrid Model**
- Combines centralized platform with embedded support
- Best for: Growing organizations transitioning from centralized
- Pros: Balances consistency with product focus
- Cons: Complex coordination, unclear boundaries

### SRE-to-developer ratios

| Company Stage | Typical Ratio | Context |
|--------------|---------------|---------|
| Early startup | 0 SREs | Developers handle operations |
| Growth stage | 1:10-15 | Building SRE foundation |
| Scale-up | 1:8-12 | Mature practices, automation focus |
| Enterprise | 1:6-10 | Complex systems, compliance requirements |

---

## What is a blameless culture?

**A blameless culture is an organizational approach where the focus after incidents is on understanding system failures and preventing recurrence, rather than punishing individuals who made mistakes.** This approach recognizes that human error is inevitable and that blame-focused responses discourage transparency and learning.

### Principles of blameless culture

1. **Human error is a symptom, not a cause:** People make mistakes because systems allow them to
2. **Transparency enables improvement:** People must feel safe reporting errors to fix systemic issues
3. **Hindsight is unfair:** Decisions that seem obviously wrong afterward often seemed reasonable at the time
4. **Systems can be improved; human nature cannot:** Focus energy on building better systems

### Implementing blamelessness

**Language matters:**
- Instead of: "Who deployed the bad config?"
- Use: "What allowed the bad config to be deployed?"

**Process changes:**
- Remove names from incident timelines during initial review
- Focus post-mortems on system improvements, not individual mistakes
- Celebrate people who surface issues, not punish them
- Make near-misses as valuable as actual incidents for learning

### Common misconceptions

| Misconception | Reality |
|--------------|---------|
| "Blameless means no accountability" | Accountability for learning exists; punishment for honest mistakes doesn't |
| "Everyone is equally responsible" | Clear ownership still matters; blame assignment doesn't |
| "We can't address repeat issues" | Patterns can be addressed through systems, not blame |

**Key insight:** Blameless culture isn't about being soft on mistakes - it's about being smart about how you prevent future mistakes. Research consistently shows that blameless environments surface more issues and improve faster than punitive ones.

---

## How do I get started with SRE practices?

**Starting with SRE doesn't require hiring a dedicated team or implementing every practice at once.** Begin with the fundamentals that provide the most value for your current stage, and add sophistication as you grow.

### Recommended starting sequence

**Phase 1: Foundation (Week 1-4)**
1. Define your most critical services
2. Implement basic monitoring and alerting
3. Set up on-call rotation with clear escalation
4. Create incident communication channels

**Phase 2: Process (Month 2-3)**
1. Define severity levels and response expectations
2. Start writing runbooks for common issues
3. Conduct basic post-mortems after incidents
4. Track MTTR and incident frequency

**Phase 3: Improvement (Month 4-6)**
1. Define SLOs for critical services
2. Implement error budgets
3. Identify and automate major toil sources
4. Run first game day exercise

**Phase 4: Maturity (Month 6+)**
1. Expand observability (logs, traces, metrics)
2. Implement chaos engineering
3. Build service catalog
4. Develop reliability roadmap

### Key principles for success

1. **Start small and iterate:** Perfect is the enemy of good in SRE adoption
2. **Measure before optimizing:** Understand your current state before making changes
3. **Focus on customer impact:** Prioritize work that improves user experience
4. **Build habits, not just tools:** Process adoption matters more than tool selection
5. **Celebrate progress:** SRE transformation takes time; acknowledge wins along the way

---

## Conclusion: Building reliability is a journey

Site Reliability Engineering isn't a destination you arrive at - it's a continuous process of improving how your team builds, operates, and learns from production systems. The terminology in this guide represents decades of hard-won lessons from engineering teams at organizations of all sizes.

**Key takeaways:**

1. **Start with the basics:** On-call rotations, incident response processes, and post-mortems provide the foundation for everything else
2. **Measure what matters:** MTTR, error budgets, and SLOs give you objective data to drive decisions
3. **Automate toil relentlessly:** Every hour spent on repetitive work is an hour not spent improving your systems
4. **Build a learning culture:** Blameless post-mortems and game days turn incidents into opportunities for improvement
5. **Use AI as a teammate:** Modern AI SRE tools can handle the first 80% of investigation work, letting humans focus on complex problem-solving

Whether you're building your first on-call rotation or implementing chaos engineering at scale, the goal remains the same: reliable systems that let you move fast when things inevitably break.

---

*Last updated: January 2026*

---

## Related resources

For teams looking to implement these practices:

- **On-call setup:** incident.io's on-call product provides flexible scheduling with 99.99% alert delivery reliability
- **Incident response:** Slack-native incident management that works where your team already collaborates
- **AI-powered investigation:** AI SRE automates context gathering and root cause analysis
- **Post-mortem automation:** Generate structured incident reviews from communication trails and system data

Start with a free trial at incident.io to see how these concepts work in practice.
