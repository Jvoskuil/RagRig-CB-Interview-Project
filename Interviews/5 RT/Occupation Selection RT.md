## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Rail Traffic Controller / Train Dispatcher | Managing train movements during signal system degradation with incomplete information; uncertainty bias in decision-making under ambiguous conditions | 100% | 3 | High | Adds control center, high-reliability, individual decision-making, safety-critical context | APPROVED |
| 2 | 2 | Signal Maintainer / Signal Technician | Deciding whether to replace marginal signal component vs. continue monitoring; zero-risk bias favoring elimination of small risk, ambiguity effect avoiding uncertain options | 100% | 6 | High | Adds field-based, technical maintenance, hands-on, individual work with equipment context | APPROVED |
| 3 | 3 | Yardmaster / Rail Yard Supervisor | Planning yard track allocation with competing train priorities; anchoring on initial plan, availability of recent conflicts, confirmation in crew recommendations | 100% | 9 | High | Adds yard operations, team coordination, resource allocation, moderate time pressure context | APPROVED |
| 4 | 4 | Division Superintendent / Operations Manager | Leading safety review meeting after near-miss incident; conservatism in changing procedures, experience bias in prior incidents, group polarization in team discussion, groupthink in consensus | 100% | 12 | High | Adds management, office-based, team decision-making, multi-stakeholder, regulatory interface context | APPROVED |
| 5 | 5 | Project Manager / Capital Projects Manager (Rail Infrastructure) | Planning track renewal project timeline; hindsight in past project reviews, illusion of control in schedule management, loss aversion in budget decisions, ostrich effect in risk monitoring, planning fallacy in timeline estimation | 100% | 15 | High | Adds project management, office-field interface, long-horizon planning, budget accountability context | APPROVED |
| 6 | 6 | Locomotive Engineer / Train Driver | Operating freight train through territory with temporary speed restrictions; recency of prior restrictions, self-serving in performance attribution, status quo in operating habits, uncertainty in conditions, zero-risk in speed selection, conservatism in procedure adherence | 100% | 18 | High | Adds train crew, cab-based, individual work with technology, high-consequence, operational continuity context | APPROVED |
| 7 | 7 | Maintenance-of-Way Supervisor / Track Maintenance Supervisor | Planning track maintenance crew assignments with competing priorities; group polarization in crew discussion, ostrich effect in risk avoidance, self-serving in performance attribution, planning fallacy in timeline, loss aversion in resource decisions, experience bias in prior assignments, illusion of control in schedule management | 86% | 19 | Moderate-High | Adds field supervision, team coordination, resource allocation, safety-operational trade-off context | APPROVED_WITH_CAVEATS (Group Polarization requires careful design in supervision context) |

***

## 2. Candidate occupation matrix

### Interview 1 (Uncertainty Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Rail Traffic Controller / Train Dispatcher | 1 (Uncertainty Bias) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multiple decision phases) | High (change signal system data accuracy) | High | High (adds control center, high-reliability context) | 0.88 |
| Locomotive Engineer | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.78 |
| Yardmaster | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Medium | 0.62 |
| Signal Maintainer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.58 |
| Division Superintendent | 0 | 0 | 1 | 0 | 25% | Low | High | High | High | Low | 0.45 |

**Selected:** Rail Traffic Controller / Train Dispatcher (best coverage, distinctness, diversity fit).

***

### Interview 2 (Zero-Risk Bias, Ambiguity Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Signal Maintainer / Signal Technician | 2 (Zero-Risk, Ambiguity) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (maintenance decision phases) | High (change component reliability data) | High | High (adds field-based, technical maintenance context) | 0.90 |
| Rail Traffic Controller | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Medium (overlaps with Interview 1) | 0.75 |
| Track Maintenance Worker | 1 | 1 | 0 | 0 | 75% | Moderate-High | Moderate | Moderate | High | Medium | 0.68 |
| Locomotive Engineer | 0 | 1 | 1 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.55 |
| Yardmaster | 0 | 1 | 1 | 0 | 50% | Moderate | High | High | High | Low | 0.52 |

**Selected:** Signal Maintainer / Signal Technician (best coverage, distinctness, diversity fit).

***

### Interview 3 (Anchoring Effect, Availability Bias, Confirmation Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Yardmaster / Rail Yard Supervisor | 3 (Anchoring, Availability, Confirmation) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (yard planning phases, multiple stakeholders) | High (change crew recommendation accuracy) | High | High (adds yard operations, resource allocation context) | 0.92 |
| Rail Traffic Controller | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 1) | 0.80 |
| Division Superintendent | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Medium | 0.76 |
| Locomotive Engineer | 2 | 1 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.68 |
| Project Manager | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.72 |

**Selected:** Yardmaster / Rail Yard Supervisor (best coverage, distinctness, diversity fit).

***

### Interview 4 (Conservatism Bias, Experience Bias, Group Polarization, Groupthink)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Division Superintendent / Operations Manager | 4 (Conservatism, Experience, Group Polarization, Groupthink) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (safety review meeting phases, team dynamics) | High (change incident data accuracy) | High | High (adds management, team decision-making context) | 0.94 |
| Yardmaster | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 3) | 0.82 |
| Project Manager | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.80 |
| Rail Traffic Controller | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 1) | 0.72 |
| Maintenance-of-Way Supervisor | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Medium | 0.68 |

**Selected:** Division Superintendent / Operations Manager (best coverage, distinctness, scenario richness).

***

### Interview 5 (Hindsight Bias, Illusion of Control, Loss Aversion, Ostrich Effect, Planning Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Project Manager / Capital Projects Manager (Rail Infrastructure) | 5 (Hindsight, Illusion of Control, Loss Aversion, Ostrich Effect, Planning Fallacy) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (project planning phases, budget accountability) | High (change project timeline data accuracy) | High | High (adds project management, long-horizon planning context) | 0.95 |
| Division Superintendent | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 4) | 0.82 |
| Maintenance-of-Way Supervisor | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.80 |
| Yardmaster | 3 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 3) | 0.74 |
| Rail Traffic Controller | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low | 0.70 |

**Selected:** Project Manager / Capital Projects Manager (best coverage, distinctness, diversity fit).

***

### Interview 6 (Recency Effect, Self-serving Bias, Status Quo Bias, Uncertainty Bias, Zero-Risk Bias, Conservatism Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Locomotive Engineer / Train Driver | 6 (Recency, Self-serving, Status Quo, Uncertainty, Zero-Risk, Conservatism) | 0 | 0 | 0 | 100% | High (six distinct mechanisms) | High (train operation phases, multiple decision points) | High (change speed restriction data accuracy) | High | High (adds train crew, cab-based, operational context) | 0.96 |
| Rail Traffic Controller | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Medium (overlaps with Interview 1) | 0.86 |
| Maintenance-of-Way Supervisor | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Medium | 0.78 |
| Yardmaster | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Medium | 0.72 |
| Signal Maintainer | 3 | 2 | 1 | 0 | 75% | Moderate-High | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.65 |

**Selected:** Locomotive Engineer / Train Driver (best coverage, distinctness, diversity fit).

***

### Interview 7 (Group Polarization, Ostrich Effect, Self-serving Bias, Planning Fallacy, Loss Aversion, Experience Bias, Illusion of Control)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Maintenance-of-Way Supervisor / Track Maintenance Supervisor | 5 (Ostrich Effect, Self-serving, Planning Fallacy, Loss Aversion, Experience Bias, Illusion of Control) | 2 (Group Polarization) | 0 | 0 | 100% | Moderate-High (Group Polarization requires careful design in supervision context) | High (crew assignment phases, team dynamics) | High (change maintenance priority data accuracy) | High | High (adds field supervision, team coordination context) | 0.88 |
| Division Superintendent | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.80 |
| Project Manager | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| Yardmaster | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Medium | 0.75 |
| Locomotive Engineer | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.72 |

**Selected:** Maintenance-of-Way Supervisor / Track Maintenance Supervisor (best diversity fit, adds field supervision context; Group Polarization requires careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Uncertainty Bias
- **Selected occupation:** Rail Traffic Controller / Train Dispatcher
- **Role and setting:** Control center-based role; monitors and coordinates train movements across designated territory, issues clearances and instructions to train crews, manages track usage conflicts, responds to operational issues and emergencies.
- **Why this occupation fits the bias list:** Rail traffic controllers routinely make decisions under uncertainty with incomplete information about train positions, signal system status, and track conditions. Uncertainty bias (decision-making patterns under ambiguous conditions) is well-documented in high-reliability control center operations where operators must balance safety with operational efficiency.
- **Primary CTA scenario:** Managing train movements during signal system degradation with incomplete information; uncertainty bias in decision-making under ambiguous conditions.
- **Triggering event:** Rail traffic controller receives reports of signal system degradation in busy territory; multiple trains approaching with conflicting movements.
- **Decision episodes:**
  1. Initial situation assessment and information gathering on signal system status.
  2. Train movement coordination and conflict resolution planning.
  3. Communication with train crews and maintenance personnel on restrictions.
  4. Final decision on movement authorities and track allocation.
- **Available cues and evidence:** Signal system indications, train position reports, track occupancy data, maintenance crew input, weather conditions, historical signal performance data.
- **Competing interpretations:** Signal degradation is temporary and can be managed with restrictions vs. degradation requires stopping movements; incomplete information supports caution vs. operational pressure supports continuing.
- **Plausible actions:** Issue restrictive movement authorities; stop movements pending signal repair; coordinate with maintenance for expedited repair; reroute trains through alternate territory.
- **Constraints and pressures:** Safety requirements, operational schedule pressure, train crew duty time limits, maintenance resource availability, passenger/cargo delivery commitments.
- **Consequences of error:** Unnecessary delays affecting schedule and crew duty time vs. continuing movements that could lead to safety incident or signal violation.
- **Counterfactual causal variable:** Actual signal system status (later found that signal degradation was more severe than initially reported; restrictions should have been more conservative).
- **Expected interview structure:** Opening (controller role context), Episode 1 (initial assessment), Episode 2 (coordination planning), Episode 3 (communication and decision), Closing (reflection on decision process).
- **Natural biases:** Uncertainty Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Locomotive Engineer (would overlap with Interview 6; less natural for uncertainty in control center context).
- **Rejected alternative occupation 2:** Yardmaster (overlaps with Interview 3; less natural for uncertainty in signal system context).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Zero-Risk Bias, Ambiguity Effect
- **Selected occupation:** Signal Maintainer / Signal Technician
- **Role and setting:** Field-based technical role; installs, inspects, tests, and repairs railway signaling systems including wayside signals, crossing signals, and communication systems; works on track and in signal bungalows.
- **Why this occupation fits the bias list:** Signal maintainers routinely make maintenance decisions on signal components with marginal readings. Zero-risk bias (favoring elimination of small risks even when costs outweigh benefits) and ambiguity effect (avoiding options with uncertain outcomes) are natural in this context where safety-critical equipment must be maintained with limited information.
- **Primary CTA scenario:** Deciding whether to replace marginal signal component vs. continue monitoring; zero-risk bias favoring elimination of small risk, ambiguity effect avoiding uncertain options.
- **Triggering event:** Signal maintainer receives test readings on signal component showing marginal performance; component is within technical specifications but showing degradation trend.
- **Decision episodes:**
  1. Initial component assessment and test data review.
  2. Comparison to historical performance data and replacement criteria.
  3. Consultation with supervisor and operations on replacement urgency.
  4. Final decision on component replacement vs. continued monitoring.
- **Available cues and evidence:** Test instrument readings, technical specifications, historical performance data, component age and condition, operations input on traffic density, supervisor guidance.
- **Competing interpretations:** Component degradation requires immediate replacement vs. component is acceptable for continued monitoring; zero-risk approach supports replacement vs. cost-benefit supports monitoring.
- **Plausible actions:** Replace component immediately; continue monitoring with enhanced testing; schedule replacement at next maintenance window; consult with vendor on component reliability.
- **Constraints and pressures:** Technical specification compliance, traffic density and operational impact, maintenance resource availability, budget constraints, safety requirements.
- **Consequences of error:** Unnecessary component replacement wasting resources vs. delayed replacement leading to signal failure and operational disruption.
- **Counterfactual causal variable:** Actual component reliability (later found that component was more reliable than test readings suggested; replacement was not actually required).
- **Expected interview structure:** Opening (maintainer role context), Episode 1 (initial assessment), Episode 2 (historical comparison), Episode 3 (consultation and decision), Closing (reflection on decision process).
- **Natural biases:** Zero-Risk Bias, Ambiguity Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Rail Traffic Controller (overlaps with Interview 1; less natural for zero-risk in maintenance context).
- **Rejected alternative occupation 2:** Track Maintenance Worker (overlaps with Interview 7; less natural for ambiguity in signal component context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Anchoring Effect, Availability Bias, Confirmation Bias
- **Selected occupation:** Yardmaster / Rail Yard Supervisor
- **Role and setting:** Yard-based supervisory role; manages rail yard operations, coordinates train arrivals and departures, allocates track space, supervises yard crew, manages resources and priorities.
- **Why this occupation fits the bias list:** Yardmasters routinely plan yard track allocation with competing train priorities and limited information. Anchoring effect (relying on initial plan), availability bias (recent conflicts), and confirmation bias (seeking data supporting preferred allocation) are all well-documented in yard planning contexts.
- **Primary CTA scenario:** Planning yard track allocation with competing train priorities; anchoring on initial plan, availability of recent conflicts, confirmation in crew recommendations.
- **Triggering event:** Yardmaster tasked to allocate yard tracks for multiple arriving trains with conflicting priorities; limited track space and crew resources.
- **Decision episodes:**
  1. Initial track allocation plan development.
  2. Resource allocation and crew assignment optimization.
  3. Crew recommendation evaluation and confirmation.
  4. Final track allocation approval and communication.
- **Available cues and evidence:** Train arrival schedules, track availability, crew availability, recent conflict history, operations priorities, customer requirements, historical yard performance data.
- **Competing interpretations:** Initial plan is optimal vs. requires modification; recent conflicts should be prioritized vs. long-term efficiency should be prioritized; crew recommendations are optimal vs. require modification.
- **Plausible actions:** Approve track allocation as developed; modify allocation to reduce conflicts; defer certain train movements; request additional resources or track space.
- **Constraints and pressures:** Track space limitations, crew availability, train schedule adherence, customer delivery commitments, safety requirements, operational efficiency targets.
- **Consequences of error:** Unnecessary track allocation modifications affecting efficiency vs. over-allocation leading to conflicts and delays.
- **Counterfactual causal variable:** Accuracy of crew recommendations (later found that one crew recommendation was based on incomplete information; track allocation could have been more efficient).
- **Expected interview structure:** Opening (yardmaster role context), Episode 1 (initial plan development), Episode 2 (resource optimization), Episode 3 (crew evaluation and approval), Closing (reflection on planning process).
- **Natural biases:** Anchoring Effect, Availability Bias, Confirmation Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Rail Traffic Controller (overlaps with Interview 1; less natural for anchoring in yard planning context).
- **Rejected alternative occupation 2:** Division Superintendent (overlaps with Interview 4; less natural for availability in yard track context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Conservatism Bias, Experience Bias, Group Polarization, Groupthink
- **Selected occupation:** Division Superintendent / Operations Manager
- **Role and setting:** Management role within rail operations; oversees operations for geographic division, manages safety programs, leads incident reviews, interfaces with regulatory bodies and union representatives.
- **Why this occupation fits the bias list:** Division superintendents routinely lead safety review meetings with multiple stakeholders. Conservatism bias (resistance to changing procedures), experience bias (relying on prior incidents), group polarization (team discussion amplifying initial positions), and groupthink (consensus without critical evaluation) are all natural in this context where team dynamics and organizational pressure influence decisions.
- **Primary CTA scenario:** Leading safety review meeting after near-miss incident; conservatism in changing procedures, experience bias in prior incidents, group polarization in team discussion, groupthink in consensus.
- **Triggering event:** Division superintendent tasked to lead safety review meeting after near-miss incident; multiple stakeholders with competing perspectives on root cause and corrective actions.
- **Decision episodes:**
  1. Initial incident review and root cause analysis.
  2. Stakeholder input and discussion on corrective actions.
  3. Group discussion dynamics and position amplification.
  4. Final consensus on corrective actions and procedure changes.
- **Available cues and evidence:** Incident reports, historical incident data, stakeholder input, regulatory requirements, operational feedback, prior corrective action effectiveness.
- **Competing interpretations:** Incident requires significant procedure change vs. minor revision is sufficient; prior experience supports conservative approach vs. new approach is needed; group consensus reflects best analysis vs. groupthink.
- **Plausible actions:** Approve corrective actions as developed; modify actions to reduce changes; defer certain actions to future review; request additional stakeholder input.
- **Constraints and pressures:** Regulatory compliance deadlines, operational continuity, stakeholder consensus, management expectations, union agreements, budget constraints.
- **Consequences of error:** Unnecessary procedure complexity affecting operations vs. insufficient corrective actions leaving operational vulnerabilities.
- **Counterfactual causal variable:** Accuracy of incident root cause analysis (later found that root cause was mischaracterized; corrective actions were not actually required).
- **Expected interview structure:** Opening (superintendent role context), Episode 1 (initial review), Episode 2 (stakeholder discussion), Episode 3 (consensus and approval), Closing (reflection on decision process).
- **Natural biases:** Conservatism Bias, Experience Bias, Group Polarization, Groupthink.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Yardmaster (overlaps with Interview 3; less natural for conservatism in safety review context).
- **Rejected alternative occupation 2:** Project Manager (overlaps with Interview 5; less natural for group polarization in management context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Hindsight Bias, Illusion of Control, Loss Aversion or Loss Framing Effect, Ostrich Effect, Planning Fallacy
- **Selected occupation:** Project Manager / Capital Projects Manager (Rail Infrastructure)
- **Role and setting:** Project management role; plans and executes rail infrastructure capital projects (track renewal, signal upgrades, bridge repairs), manages budgets and timelines, interfaces with operations and regulatory bodies.
- **Why this occupation fits the bias list:** Project managers routinely plan infrastructure projects with competing priorities and limited information. Hindsight bias (in past project reviews), illusion of control (in schedule management), loss aversion (in budget decisions), ostrich effect (in risk monitoring), and planning fallacy (in timeline estimation) are all well-documented in project management contexts.
- **Primary CTA scenario:** Planning track renewal project timeline; hindsight in past project reviews, illusion of control in schedule management, loss aversion in budget decisions, ostrich effect in risk monitoring, planning fallacy in timeline estimation.
- **Triggering event:** Project manager tasked to develop track renewal project timeline and budget; multiple stakeholders with competing priorities and limited historical data.
- **Decision episodes:**
  1. Initial project scope and timeline development.
  2. Budget estimation and resource allocation.
  3. Risk assessment and mitigation planning.
  4. Final project plan approval and stakeholder communication.
- **Available cues and evidence:** Historical project data, stakeholder input, regulatory requirements, operational constraints, resource availability, weather and environmental factors.
- **Competing interpretations:** Past project performance is predictive vs. current project is unique; timeline is achievable vs. requires extension; budget is sufficient vs. requires contingency.
- **Plausible actions:** Approve project plan as developed; modify timeline to reduce risk; increase budget contingency; defer certain project elements to future phases.
- **Constraints and pressures:** Budget limitations, operational continuity, regulatory compliance, stakeholder expectations, resource availability, weather constraints.
- **Consequences of error:** Unnecessary timeline extension affecting operational benefits vs. over-optimistic timeline leading to delays and cost overruns.
- **Counterfactual causal variable:** Accuracy of historical project data (later found that historical data was incomplete; timeline should have been more conservative).
- **Expected interview structure:** Opening (project manager role context), Episode 1 (initial scope development), Episode 2 (budget estimation), Episode 3 (risk assessment and approval), Closing (reflection on planning process).
- **Natural biases:** Hindsight Bias, Illusion of Control, Loss Aversion or Loss Framing Effect, Ostrich Effect, Planning Fallacy.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Division Superintendent (overlaps with Interview 4; less natural for hindsight in project planning context).
- **Rejected alternative occupation 2:** Maintenance-of-Way Supervisor (overlaps with Interview 7; less natural for illusion of control in capital project context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Recency Effect, Self-serving Bias, Status Quo Bias, Uncertainty Bias, Zero-Risk Bias, Conservatism Bias
- **Selected occupation:** Locomotive Engineer / Train Driver
- **Role and setting:** Train crew role; operates locomotive and controls train movement, monitors signals and track conditions, communicates with dispatchers and crew, maintains regulatory compliance.
- **Why this occupation fits the bias list:** Locomotive engineers routinely operate trains through territory with varying conditions and restrictions. Recency effect (prior restrictions), self-serving bias (performance attribution), status quo bias (operating habits), uncertainty bias (in conditions), zero-risk bias (in speed selection), and conservatism bias (in procedure adherence) are all natural in this context where safety and operational efficiency must be balanced.
- **Primary CTA scenario:** Operating freight train through territory with temporary speed restrictions; recency of prior restrictions, self-serving in performance attribution, status quo in operating habits, uncertainty in conditions, zero-risk in speed selection, conservatism in procedure adherence.
- **Triggering event:** Locomotive engineer receives temporary speed restriction notices for territory; multiple restrictions with varying conditions and enforcement.
- **Decision episodes:**
  1. Initial restriction review and operating plan development.
  2. Speed selection and restriction compliance monitoring.
  3. Communication with dispatcher on restriction status.
  4. Final operating decision and documentation.
- **Available cues and evidence:** Speed restriction notices, signal indications, track conditions, weather conditions, dispatcher communications, prior restriction experience, train handling characteristics.
- **Competing interpretations:** Restrictions are necessary for safety vs. restrictions are overly conservative; prior experience supports current speed vs. conditions require slower speed; self-serving attribution supports performance vs. external factors affected performance.
- **Plausible actions:** Operate at restricted speed as planned; operate at slower speed for additional safety; contact dispatcher for restriction clarification; document restriction concerns for future review.
- **Constraints and pressures:** Schedule adherence, safety requirements, regulatory compliance, train handling limitations, weather conditions, dispatcher coordination.
- **Consequences of error:** Unnecessary speed reduction affecting schedule vs. excessive speed leading to safety incident or regulatory violation.
- **Counterfactual causal variable:** Accuracy of speed restriction data (later found that one restriction was based on outdated information; speed could have been higher).
- **Expected interview structure:** Opening (engineer role context), Episode 1 (initial review), Episode 2 (speed selection), Episode 3 (communication and decision), Closing (reflection on operating process).
- **Natural biases:** Recency Effect, Self-serving Bias, Status Quo Bias, Uncertainty Bias, Zero-Risk Bias, Conservatism Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Rail Traffic Controller (overlaps with Interview 1; less natural for recency in train operation context).
- **Rejected alternative occupation 2:** Maintenance-of-Way Supervisor (overlaps with Interview 7; less natural for self-serving in operating context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Group Polarization, Ostrich Effect, Self-serving Bias, Planning Fallacy, Loss Aversion or Loss Framing Effect, Experience Bias, Illusion of Control
- **Selected occupation:** Maintenance-of-Way Supervisor / Track Maintenance Supervisor
- **Role and setting:** Field-based supervisory role; manages track maintenance crews, plans maintenance assignments, allocates resources, ensures safety compliance, interfaces with operations on track availability.
- **Why this occupation fits the bias list:** Maintenance-of-way supervisors routinely plan crew assignments with competing priorities and limited information. Group polarization (in crew discussion), ostrich effect (in risk avoidance), self-serving bias (in performance attribution), planning fallacy (in timeline), loss aversion (in resource decisions), experience bias (in prior assignments), and illusion of control (in schedule management) are all plausible, though group polarization requires careful design in supervision context.
- **Primary CTA scenario:** Planning track maintenance crew assignments with competing priorities; group polarization in crew discussion, ostrich effect in risk avoidance, self-serving in performance attribution, planning fallacy in timeline, loss aversion in resource decisions, experience bias in prior assignments, illusion of control in schedule management.
- **Triggering event:** Maintenance-of-way supervisor tasked to assign track maintenance crews to multiple work locations; competing priorities from operations and safety requirements.
- **Decision episodes:**
  1. Initial crew assignment plan development.
  2. Crew discussion and position amplification on priorities.
  3. Resource allocation and timeline estimation.
  4. Final assignment approval and communication to operations.
- **Available cues and evidence:** Work location priorities, crew availability, equipment availability, historical performance data, operations input, safety requirements, weather conditions.
- **Competing interpretations:** Crew discussion supports aggressive timeline vs. conservative approach; prior experience supports current assignments vs. new approach is needed; self-serving attribution supports performance vs. external factors affected performance.
- **Plausible actions:** Approve crew assignments as developed; modify assignments to reduce risk; defer certain work to future windows; request additional resources or crew support.
- **Constraints and pressures:** Track availability windows, crew duty time limits, equipment availability, operational schedule, safety requirements, budget constraints.
- **Consequences of error:** Unnecessary assignment modifications affecting efficiency vs. over-optimistic assignments leading to incomplete work and safety risks.
- **Counterfactual causal variable:** Accuracy of work location priorities (later found that one priority was mischaracterized; assignments could have been more efficient).
- **Expected interview structure:** Opening (supervisor role context), Episode 1 (initial plan development), Episode 2 (crew discussion), Episode 3 (resource allocation and approval), Closing (reflection on assignment process).
- **Natural biases:** Ostrich Effect, Self-serving Bias, Planning Fallacy, Loss Aversion or Loss Framing Effect, Experience Bias, Illusion of Control.
- **Plausible but difficult biases:** Group Polarization (requires careful design in supervision context).
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Division Superintendent (overlaps with Interview 4; less natural for ostrich effect in field supervision context).
- **Rejected alternative occupation 2:** Project Manager (overlaps with Interview 5; less natural for group polarization in maintenance context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Group Polarization requires careful design in supervision context)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations | None | None | None | None needed |
| Work setting | Control center (1), Field-based (2, 7), Yard-based (3), Office-based (4, 5), Train cab (6) | Field-based (2/7), Office-based (2/7) | Balanced | Office-based analytical, Industrial/technical | None critical; reflects rail operations nature |
| Decision type | Coordination (1, 3, 6), Maintenance (2, 7), Management (4, 5) | Coordination (3/7), Maintenance (2/7) | Coordination | Diagnosis, Emergency response | None critical; coordination is natural for rail |
| Information environment | Data-heavy (1, 3, 6), Conflicting sources (1, 4, 7), Incomplete (2, 7), Regulated (1, 4, 5, 6) | Data-heavy (3/7), Regulated (4/7) | Regulated | Rich/structured, Socially mediated | None critical; reflects rail information complexity |
| Time pressure | Moderate (2, 3, 4, 5, 7), High (1, 6) | Moderate (5/7) | Moderate | Low | None needed |
| Consequence of error | Safety (1, 2, 6, 7), Operational (1, 3, 4, 6, 7), Regulatory (1, 4, 5, 6), Financial (3, 4, 5, 7) | Operational (5/7), Safety (4/7) | Operational, Safety | Environmental, Educational | None critical; reflects rail consequence profile |
| Expertise level | Independent professional (1, 2, 6), Senior practitioner (3, 7), Supervisor/manager (4, 5) | Independent professional (3/7), Supervisor/manager (2/7) | Balanced | Developing practitioner | None needed |
| Stakeholder pattern | Individual (1, 2, 6), Team (3, 7), Multi-party (4, 5) | Individual (3/7), Team (2/7) | Balanced | One-to-one, Public interaction | None critical |
| Scenario archetype | Coordination (1, 3, 6), Maintenance (2, 7), Management (4, 5) | Coordination (3/7), Maintenance (2/7), Management (2/7) | Balanced | Emergency response, Negotiation | None critical |
| Causal-counterfactual structure | Data accuracy (1, 3, 6), Equipment/process cause (2, 7), Recommendation accuracy (3), Event analysis (4, 5) | Data accuracy (3/7) | Data accuracy | Equipment failure, Human performance | None critical; reflects rail causal structure |

**Overall assessment:** Good diversity across occupations, settings, decision types, and consequence profiles. Coordination scenarios are slightly overrepresented (3/7), but this reflects the nature of rail operations where train movement coordination is prominent. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Uncertainty Bias (clear mechanism: decision-making under ambiguity) | None | None | None | None | None | Ensure clear ambiguous conditions; probe decision reasoning explicitly |
| 2 | Zero-Risk Bias (risk elimination), Ambiguity Effect (uncertain outcomes) | None | None | None | None | None | Provide clear risk trade-offs; separate zero-risk from ambiguity |
| 3 | Anchoring Effect (initial plan), Availability Bias (recent conflicts), Confirmation Bias (supporting data) | Availability and Confirmation (both involve information selection) | None | None | None | None | Separate recent conflicts from confirmation seeking; probe anchoring explicitly |
| 4 | Conservatism Bias (procedure resistance), Experience Bias (prior incidents), Group Polarization (position amplification), Groupthink (consensus) | Group Polarization and Groupthink (both involve group dynamics), Conservatism and Experience (both involve prior state) | None | None | Group Polarization (group dynamics cues may be subtle), Groupthink (consensus cues may be subtle) | Group Polarization, Groupthink | Provide clear group dynamics; separate polarization from groupthink |
| 5 | Hindsight Bias (outcome knowledge), Illusion of Control (schedule management), Loss Aversion (budget decisions), Ostrich Effect (risk avoidance), Planning Fallacy (timeline estimation) | Hindsight Bias and outcome bias (both involve outcome knowledge), Illusion of Control and Planning Fallacy (both involve timeline/schedule) | Hindsight Bias | Hindsight Bias | Ostrich Effect (risk avoidance cues may be subtle) | Ostrich Effect, Hindsight Bias | Separate outcome knowledge from decision process; probe risk avoidance explicitly |
| 6 | Recency Effect (prior restrictions), Self-serving Bias (performance attribution), Status Quo Bias (operating habits), Uncertainty Bias (conditions), Zero-Risk Bias (speed selection), Conservatism Bias (procedure adherence) | Recency and Status Quo (both involve prior state), Uncertainty and Zero-Risk (both involve risk conditions) | None | None | Uncertainty Bias (ambiguous conditions cues may be subtle) | Uncertainty Bias | Provide clear ambiguous conditions; separate recency from status quo |
| 7 | Group Polarization (position amplification), Ostrich Effect (risk avoidance), Self-serving Bias (performance attribution), Planning Fallacy (timeline), Loss Aversion (resource decisions), Experience Bias (prior assignments), Illusion of Control (schedule management) | Group Polarization and Experience (both involve prior state), Planning Fallacy and Illusion of Control (both involve timeline/schedule) | None | None | Group Polarization (group dynamics cues may be subtle), Ostrich Effect (risk avoidance cues may be subtle) | Group Polarization, Ostrich Effect | Provide clear group dynamics; separate polarization from experience |

**Overall safeguards:**
- **Prompt 1 (interview generation):** Ensure each bias has distinct cues and decision episodes; avoid conflating group dynamics biases (Group Polarization, Groupthink) with individual biases.
- **Prompt 2 (annotation):** Provide clear bias definitions and decision episode boundaries; require annotators to identify specific cues for each bias.
