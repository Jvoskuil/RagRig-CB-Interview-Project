## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Shift Supervisor / Control Room Supervisor (Nuclear) | Evaluating whether to proceed with planned maintenance during minor instrument fluctuation; imperfect rationality in balancing procedural compliance with operational judgment | 100% | 3 | High | Adds supervisory, team coordination, regulatory accountability context | APPROVED |
| 2 | 2 | Chemistry Technician / Radiochemistry Laboratory Technician | Analyzing coolant sample showing anomalous readings; salience of striking values, similarity bias comparing to past samples | 100% | 6 | High | Adds laboratory, analytical, individual work with technical data context | APPROVED |
| 3 | 3 | Maintenance Planner / Outage Coordinator | Planning refueling outage scope with competing priorities; availability of recent issues, bounded rationality in scope optimization, confirmation in vendor recommendations | 100% | 9 | High | Adds planning, office-field interface, resource allocation, long-horizon context | APPROVED |
| 4 | 4 | Field Operator / Equipment Operator (Nuclear) | Responding to pump vibration alarm during routine rounds; experience/habit in prior responses, recency of similar alarms, imperfect rationality in stress, salience of alarm | 100% | 12 | High | Adds field-based, hands-on, time-pressured, individual decision-making context | APPROVED |
| 5 | 5 | Procedure Engineer / Technical Procedure Writer | Revising emergency operating procedure after near-miss; similarity to past procedures, bounded rationality in revision scope, experience bias in prior revisions, recency of event, imperfect rationality in balancing competing demands | 100% | 15 | High | Adds engineering, documentation, regulatory interface, office-based context | APPROVED |
| 6 | 6 | Reactor Operator (NRC-licensed) | Managing reactor power maneuver with conflicting instrument indications; confirmation in initial assessment, imperfect rationality under time pressure, salience of alarms, similarity to past maneuvers, bounded rationality in information processing, confirmation in seeking supporting data | 100% | 18 | High | Adds control room, licensed operator, high-consequence, human-machine collaboration context | APPROVED |
| 7 | 7 | Process Control Operator (Chemical/Petrochemical Refinery) | Responding to distillation column pressure excursion with multiple alarms; recency of similar upsets, availability of recent incidents, experience/habit in prior responses, availability of vivid scenarios, salience of alarms, similarity to past upsets, bounded rationality in information overload | 86% | 19 | Moderate-High | Adds chemical/process industry, control room, mixed information sources, operational continuity context | APPROVED_WITH_CAVEATS (One Availability Bias is duplicate in list; requires careful design) |

***

## 2. Candidate occupation matrix

### Interview 1 (Imperfect Rationality)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Shift Supervisor / Control Room Supervisor | 1 (Imperfect Rationality) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multiple decision phases) | High (change instrument data accuracy) | High | High (adds supervisory, team context) | 0.88 |
| Reactor Operator | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.78 |
| Field Operator | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Medium | 0.58 |
| Maintenance Planner | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.62 |
| Chemistry Technician | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Low | 0.42 |

**Selected:** Shift Supervisor / Control Room Supervisor (best coverage, distinctness, diversity fit).

***

### Interview 2 (Salience Bias, Similarity Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Chemistry Technician / Radiochemistry Laboratory Technician | 2 (Salience, Similarity) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (laboratory analysis phases) | High (change sample data accuracy) | High | High (adds laboratory, analytical role) | 0.90 |
| Reactor Operator | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Medium (overlaps with Interview 6) | 0.75 |
| Process Control Operator | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Medium | 0.70 |
| Field Operator | 1 | 0 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low | 0.55 |
| Procedure Engineer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low | 0.52 |

**Selected:** Chemistry Technician / Radiochemistry Laboratory Technician (best coverage, distinctness, diversity fit).

***

### Interview 3 (Availability Bias, Bounded Rationality, Confirmation Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Maintenance Planner / Outage Coordinator | 3 (Availability, Bounded Rationality, Confirmation) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (planning phases, multiple stakeholders) | High (change vendor recommendation accuracy) | High | High (adds planning, resource allocation role) | 0.92 |
| Shift Supervisor | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 1) | 0.80 |
| Process Control Operator | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Medium | 0.76 |
| Reactor Operator | 2 | 1 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.68 |
| Field Operator | 1 | 2 | 0 | 0 | 83% | Moderate | Moderate | Moderate | High | Medium | 0.62 |

**Selected:** Maintenance Planner / Outage Coordinator (best coverage, distinctness, diversity fit).

***

### Interview 4 (Experience/Frequency/Habit Bias, Recency Bias, Imperfect Rationality, Salience Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Field Operator / Equipment Operator (Nuclear) | 4 (Experience/Habit, Recency, Imperfect Rationality, Salience) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (field response phases, time pressure) | High (change alarm cause accuracy) | High | High (adds field-based, hands-on role) | 0.94 |
| Reactor Operator | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 6) | 0.82 |
| Process Control Operator | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.80 |
| Shift Supervisor | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 1) | 0.72 |
| Chemistry Technician | 2 | 1 | 1 | 0 | 75% | Moderate-High | Moderate | Moderate | High | Low | 0.65 |

**Selected:** Field Operator / Equipment Operator (best coverage, distinctness, diversity fit).

***

### Interview 5 (Similarity Bias, Bounded Rationality, Experience/Frequency/Habit Bias, Recency Bias, Imperfect Rationality)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Procedure Engineer / Technical Procedure Writer | 5 (Similarity, Bounded Rationality, Experience/Habit, Recency, Imperfect Rationality) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (procedure revision phases, regulatory interface) | High (change near-miss data accuracy) | High | High (adds engineering, documentation role) | 0.95 |
| Shift Supervisor | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 1) | 0.82 |
| Reactor Operator | 3 | 2 | 0 | 0 | 80% | High | High | High | High | Medium | 0.76 |
| Maintenance Planner | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Process Control Operator | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Medium | 0.74 |

**Selected:** Procedure Engineer / Technical Procedure Writer (best coverage, distinctness, scenario richness).

***

### Interview 6 (Confirmation Bias, Imperfect Rationality, Salience Bias, Similarity Bias, Bounded Rationality, Confirmation Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Reactor Operator (NRC-licensed) | 6 (Confirmation x2, Imperfect Rationality, Salience, Similarity, Bounded Rationality) | 0 | 0 | 0 | 100% | High (six distinct mechanisms; Confirmation Bias appears twice but can be embedded in separate episodes) | High (power maneuver phases, multiple decision points) | High (change instrument indication accuracy) | High | High (adds control room, licensed operator role) | 0.96 |
| Process Control Operator | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Medium (overlaps with Interview 7) | 0.86 |
| Shift Supervisor | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Medium | 0.78 |
| Field Operator | 4 | 1 | 1 | 0 | 83% | Moderate-High | Moderate | Moderate | High | Medium | 0.72 |
| Maintenance Planner | 3 | 2 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.68 |

**Selected:** Reactor Operator (best coverage, distinctness, diversity fit).

***

### Interview 7 (Recency Bias, Availability Bias x2, Experience/Frequency/Habit Bias, Salience Bias, Similarity Bias, Bounded Rationality)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Process Control Operator (Chemical/Petrochemical Refinery) | 5 (Recency, Availability x2, Experience/Habit, Salience, Similarity, Bounded Rationality) | 2 (one Availability Bias is duplicate in list) | 0 | 0 | 100% | Moderate-High (Availability Bias appears twice; requires careful design to separate) | High (process upset response phases, multiple alarms) | High (change upset cause accuracy) | High | High (adds chemical/process industry, control room role) | 0.88 |
| Reactor Operator | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.80 |
| Field Operator | 4 | 2 | 1 | 0 | 86% | Moderate-High | Moderate | Moderate | High | Medium | 0.75 |
| Shift Supervisor | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.76 |
| Maintenance Planner | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.72 |

**Selected:** Process Control Operator (best diversity fit, adds chemical/process industry context; one Availability Bias is duplicate in list, requires careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Imperfect Rationality
- **Selected occupation:** Shift Supervisor / Control Room Supervisor (Nuclear)
- **Role and setting:** Supervisory role in nuclear power plant control room; oversees reactor operators, field operators, and control room activities; responsible for shift performance, regulatory compliance, and emergency response coordination.
- **Why this occupation fits the bias list:** Shift supervisors routinely make judgment calls balancing procedural compliance with operational realities. Imperfect rationality (deviation from purely rational decision-making due to cognitive limitations, stress, or competing demands) is well-documented in supervisory decision-making where multiple constraints must be balanced. [nrc](https://www.nrc.gov/docs/ML1025/ML102520363.pdf)
- **Primary CTA scenario:** Evaluating whether to proceed with planned maintenance during minor instrument fluctuation; imperfect rationality in balancing procedural compliance with operational judgment.
- **Triggering event:** Shift supervisor receives report of minor instrument fluctuation in reactor coolant system during planned maintenance window; maintenance team is ready to proceed.
- **Decision episodes:**
  1. Initial assessment of instrument fluctuation and maintenance readiness.
  2. Consultation with reactor operators and engineering support.
  3. Risk-benefit analysis of proceeding vs. delaying maintenance.
  4. Final decision on maintenance authorization and documentation.
- **Available cues and evidence:** Instrument readings, maintenance work orders, procedural requirements, operator assessments, engineering input, historical data on similar fluctuations.
- **Competing interpretations:** Fluctuation is benign and maintenance can proceed vs. fluctuation indicates underlying issue requiring investigation; procedural compliance requires delay vs. operational judgment supports proceeding.
- **Plausible actions:** Authorize maintenance to proceed; delay maintenance pending further investigation; authorize maintenance with enhanced monitoring; cancel maintenance and reschedule.
- **Constraints and pressures:** Maintenance schedule and resource availability, regulatory compliance requirements, operational continuity, shift staffing limitations, management expectations.
- **Consequences of error:** Unnecessary maintenance delay costing resources and schedule vs. proceeding with maintenance that could exacerbate underlying issue leading to operational upset.
- **Counterfactual causal variable:** Actual cause of instrument fluctuation (later found that fluctuation was sensor drift; no underlying issue existed).
- **Expected interview structure:** Opening (supervisor role context), Episode 1 (initial assessment), Episode 2 (consultation), Episode 3 (risk-benefit analysis and decision), Closing (reflection on decision process).
- **Natural biases:** Imperfect Rationality.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Reactor Operator (would overlap with Interview 6; less natural for supervisory judgment context).
- **Rejected alternative occupation 2:** Field Operator (less natural for imperfect rationality in maintenance authorization context).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Salience Bias, Similarity Bias
- **Selected occupation:** Chemistry Technician / Radiochemistry Laboratory Technician
- **Role and setting:** Laboratory-based analytical role within nuclear power plant; analyzes coolant, water chemistry, and radiochemistry samples to support plant operations and regulatory compliance.
- **Why this occupation fits the bias list:** Chemistry technicians routinely interpret analytical data and compare results to historical baselines. Salience bias (overweighting striking or prominent values) and similarity bias (comparing to similar past samples) are natural in this context where pattern recognition and data interpretation are critical. [tandfonline](https://www.tandfonline.com/doi/full/10.1080/18811248.1999.9726296)
- **Primary CTA scenario:** Analyzing coolant sample showing anomalous readings; salience of striking values, similarity bias comparing to past samples.
- **Triggering event:** Chemistry technician receives reactor coolant sample showing anomalous readings for specific chemical parameters; values are outside normal range but within technical specifications.
- **Decision episodes:**
  1. Initial data review and comparison to technical specifications.
  2. Comparison to historical samples and baseline trends.
  3. Consultation with chemistry supervisor and operations on sample validity.
  4. Final determination on sample acceptance and recommendation on plant chemistry adjustments.
- **Available cues and evidence:** Analytical instrument readings, technical specifications, historical sample data, sample collection records, plant operating conditions, supervisor input.
- **Competing interpretations:** Anomalous readings reflect genuine chemistry change vs. sampling or analytical error; historical similarity supports acceptance vs. deviation requires rejection.
- **Plausible actions:** Accept sample and recommend chemistry adjustments; reject sample and request resampling; accept sample with enhanced monitoring; consult with vendor laboratory for confirmation.
- **Constraints and pressures:** Technical specification compliance, sample stability time limits, operational chemistry requirements, laboratory workload, regulatory reporting deadlines.
- **Consequences of error:** Unnecessary chemistry adjustments wasting resources vs. accepting bad sample leading to undetected chemistry degradation.
- **Counterfactual causal variable:** Actual sample validity (later found that sample was contaminated during collection; analytical readings were accurate but sample was not representative).
- **Expected interview structure:** Opening (technician role context), Episode 1 (initial data review), Episode 2 (historical comparison), Episode 3 (consultation and determination), Closing (reflection on decision process).
- **Natural biases:** Salience Bias, Similarity Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Reactor Operator (overlaps with Interview 6; less natural for salience in analytical context).
- **Rejected alternative occupation 2:** Process Control Operator (overlaps with Interview 7; less natural for similarity in laboratory context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Availability Bias, Bounded Rationality, Confirmation Bias
- **Selected occupation:** Maintenance Planner / Outage Coordinator
- **Role and setting:** Planning role within nuclear power plant; coordinates refueling outages, maintenance activities, and resource allocation; interfaces with operations, engineering, and contractors.
- **Why this occupation fits the bias list:** Maintenance planners routinely optimize outage scope with competing priorities and limited information. Availability bias (relying on recent or memorable issues), bounded rationality (optimizing within cognitive and information constraints), and confirmation bias (seeking data supporting preferred scope) are all well-documented in planning contexts. [nrc](https://www.nrc.gov/docs/ML1025/ML102520363.pdf)
- **Primary CTA scenario:** Planning refueling outage scope with competing priorities; availability of recent issues, bounded rationality in scope optimization, confirmation in vendor recommendations.
- **Triggering event:** Maintenance planner tasked to finalize refueling outage scope; multiple competing priorities from operations, engineering, and regulatory requirements.
- **Decision episodes:**
  1. Initial scope review and prioritization of maintenance activities.
  2. Resource allocation and scheduling optimization.
  3. Vendor recommendation evaluation and confirmation.
  4. Final scope approval and communication to stakeholders.
- **Available cues and evidence:** Maintenance work orders, resource availability, vendor recommendations, regulatory requirements, historical outage data, operations input, engineering assessments.
- **Competing interpretations:** Recent issues should be prioritized vs. long-term reliability should be prioritized; vendor recommendations are optimal vs. require modification; scope is achievable vs. requires reduction.
- **Plausible actions:** Approve scope as developed; modify scope to reduce activities; defer certain activities to next outage; request additional resources or time.
- **Constraints and pressures:** Outage schedule and critical path, resource limitations, regulatory requirements, operations priorities, budget constraints, contractor availability.
- **Consequences of error:** Unnecessary scope reduction affecting long-term reliability vs. over-scoping leading to schedule delays and cost overruns.
- **Counterfactual causal variable:** Accuracy of vendor recommendations (later found that one vendor recommendation was based on incomplete data; activity was not actually required).
- **Expected interview structure:** Opening (planner role context), Episode 1 (scope review), Episode 2 (resource optimization), Episode 3 (vendor evaluation and approval), Closing (reflection on planning process).
- **Natural biases:** Availability Bias, Bounded Rationality, Confirmation Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Shift Supervisor (overlaps with Interview 1; less natural for availability in planning context).
- **Rejected alternative occupation 2:** Process Control Operator (overlaps with Interview 7; less natural for bounded rationality in outage scope context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality, Salience Bias
- **Selected occupation:** Field Operator / Equipment Operator (Nuclear)
- **Role and setting:** Field-based operational role within nuclear power plant; conducts equipment rounds, responds to alarms, performs field operations and troubleshooting; works in plant areas with direct equipment access.
- **Why this occupation fits the bias list:** Field operators routinely respond to alarms and equipment issues with time pressure and incomplete information. Experience/habit bias (relying on prior responses), recency bias (recent similar alarms), imperfect rationality (under stress), and salience bias (prominent alarms) are all natural in this context. [nrc](https://www.nrc.gov/docs/ML1025/ML102520363.pdf)
- **Primary CTA scenario:** Responding to pump vibration alarm during routine rounds; experience/habit in prior responses, recency of similar alarms, imperfect rationality in stress, salience of alarm.
- **Triggering event:** Field operator receives pump vibration alarm during routine equipment rounds; alarm is prominent and requires immediate response.
- **Decision episodes:**
  1. Initial alarm assessment and equipment inspection.
  2. Comparison to recent similar alarms and prior experience.
  3. Decision on immediate action vs. further investigation.
  4. Final action and communication to control room.
- **Available cues and evidence:** Alarm indications, equipment vibration readings, recent alarm history, prior experience with similar alarms, equipment condition indicators, control room communications.
- **Competing interpretations:** Alarm reflects genuine equipment issue requiring immediate action vs. alarm is transient or false; prior experience supports immediate action vs. further investigation needed.
- **Plausible actions:** Take immediate corrective action; investigate further before action; notify control room and await instructions; tag equipment out of service.
- **Constraints and pressures:** Time pressure for response, equipment criticality, procedural requirements, control room coordination, personal safety, shift staffing.
- **Consequences of error:** Unnecessary equipment shutdown affecting operations vs. delayed action leading to equipment damage or operational upset.
- **Counterfactual causal variable:** Actual cause of vibration alarm (later found that alarm was caused by temporary process condition; no equipment issue existed).
- **Expected interview structure:** Opening (field operator role context), Episode 1 (initial alarm assessment), Episode 2 (comparison to recent/prior), Episode 3 (action decision and communication), Closing (reflection on response process).
- **Natural biases:** Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality, Salience Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Reactor Operator (overlaps with Interview 6; less natural for experience/habit in field response context).
- **Rejected alternative occupation 2:** Chemistry Technician (overlaps with Interview 2; less natural for recency in alarm response context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Similarity Bias, Bounded Rationality, Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality
- **Selected occupation:** Procedure Engineer / Technical Procedure Writer
- **Role and setting:** Engineering role within nuclear power plant; writes and revises operating procedures, emergency procedures, and technical documentation; interfaces with operations, engineering, and regulatory compliance.
- **Why this occupation fits the bias list:** Procedure engineers routinely revise procedures based on operational experience and regulatory requirements. Similarity bias (comparing to past procedures), bounded rationality (optimizing within constraints), experience/habit bias (relying on prior revisions), recency bias (recent events), and imperfect rationality (balancing competing demands) are all natural in this context. [nrc](https://www.nrc.gov/docs/ML1025/ML102520363.pdf)
- **Primary CTA scenario:** Revising emergency operating procedure after near-miss; similarity to past procedures, bounded rationality in revision scope, experience bias in prior revisions, recency of event, imperfect rationality in balancing competing demands.
- **Triggering event:** Procedure engineer tasked to revise emergency operating procedure after near-miss event; multiple stakeholder inputs and regulatory requirements.
- **Decision episodes:**
  1. Initial procedure review and near-miss event analysis.
  2. Comparison to past procedures and prior revisions.
  3. Stakeholder consultation and revision scope optimization.
  4. Final procedure approval and regulatory submission.
- **Available cues and evidence:** Near-miss event reports, existing procedures, historical revision data, stakeholder input, regulatory requirements, operational feedback.
- **Competing interpretations:** Near-miss requires significant procedure change vs. minor revision is sufficient; past procedures are appropriate baseline vs. require major modification; stakeholder inputs are consistent vs. conflicting.
- **Plausible actions:** Approve procedure revision as developed; modify revision scope to reduce changes; defer certain changes to future revision; request additional stakeholder input.
- **Constraints and pressures:** Regulatory compliance deadlines, operational continuity, stakeholder consensus, documentation workload, management expectations.
- **Consequences of error:** Unnecessary procedure complexity affecting operator performance vs. insufficient revision leaving operational vulnerabilities.
- **Counterfactual causal variable:** Accuracy of near-miss event analysis (later found that near-miss was mischaracterized; procedure revision was not actually required).
- **Expected interview structure:** Opening (procedure engineer role context), Episode 1 (initial review), Episode 2 (historical comparison), Episode 3 (stakeholder consultation and approval), Closing (reflection on revision process).
- **Natural biases:** Similarity Bias, Bounded Rationality, Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Shift Supervisor (overlaps with Interview 1; less natural for similarity in procedure context).
- **Rejected alternative occupation 2:** Maintenance Planner (overlaps with Interview 3; less natural for experience/habit in procedure revision context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Confirmation Bias, Imperfect Rationality, Salience Bias, Similarity Bias, Bounded Rationality, Confirmation Bias
- **Selected occupation:** Reactor Operator (NRC-licensed)
- **Role and setting:** Licensed control room role within nuclear power plant; directly operates reactor and primary plant systems, executes emergency procedures, maintains regulatory compliance; works in control room with human-machine collaboration.
- **Why this occupation fits the bias list:** Reactor operators routinely manage reactor power maneuvers with conflicting instrument indications and time pressure. Confirmation bias (seeking supporting data), imperfect rationality (under stress), salience bias (prominent alarms), similarity bias (comparing to past maneuvers), and bounded rationality (information processing limits) are all well-documented in control room decision-making. [nrc](https://www.nrc.gov/docs/ML1025/ML102520363.pdf)
- **Primary CTA scenario:** Managing reactor power maneuver with conflicting instrument indications; confirmation in initial assessment, imperfect rationality under time pressure, salience of alarms, similarity to past maneuvers, bounded rationality in information processing, confirmation in seeking supporting data.
- **Triggering event:** Reactor operator tasked to execute reactor power maneuver; instrument indications show conflicting data on reactor state.
- **Decision episodes:**
  1. Initial reactor state assessment and maneuver planning.
  2. Instrument indication evaluation and conflict resolution.
  3. Maneuver execution with ongoing monitoring.
  4. Final reactor state confirmation and documentation.
- **Available cues and evidence:** Instrument readings, alarm indications, procedural requirements, prior maneuver experience, control room communications, engineering support.
- **Competing interpretations:** Instrument conflict reflects sensor error vs. genuine reactor state change; initial assessment is accurate vs. requires revision; maneuver can proceed vs. requires modification.
- **Plausible actions:** Proceed with maneuver as planned; modify maneuver based on instrument conflict; suspend maneuver pending further investigation; notify shift supervisor and engineering.
- **Constraints and pressures:** Time pressure for maneuver, procedural compliance, regulatory requirements, control room coordination, operational continuity, personal regulatory accountability.
- **Consequences of error:** Unnecessary maneuver suspension affecting operations vs. proceeding with maneuver that could lead to operational upset or regulatory violation.
- **Counterfactual causal variable:** Accuracy of instrument indications (later found that one instrument was calibrated incorrectly; indications were misleading).
- **Expected interview structure:** Opening (reactor operator role context), Episode 1 (initial assessment), Episode 2 (instrument evaluation), Episode 3 (maneuver execution and confirmation), Closing (reflection on decision process).
- **Natural biases:** Confirmation Bias (x2, can be embedded in separate episodes), Imperfect Rationality, Salience Bias, Similarity Bias, Bounded Rationality.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Process Control Operator (overlaps with Interview 7; less natural for confirmation in nuclear control room context).
- **Rejected alternative occupation 2:** Shift Supervisor (overlaps with Interview 1; less natural for similarity in power maneuver context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Recency Bias, Availability Bias, Experience Bias or Frequency Bias or Habit, Availability Bias, Salience Bias, Similarity Bias, Bounded Rationality
- **Selected occupation:** Process Control Operator (Chemical/Petrochemical Refinery)
- **Role and setting:** Control room role within chemical/petrochemical refinery; monitors and controls distillation columns, reactors, and other process units; interfaces with field operators and maintenance.
- **Why this occupation fits the bias list:** Process control operators routinely respond to process upsets with multiple alarms and incomplete information. Recency bias (recent similar upsets), availability bias (recent incidents and vivid scenarios), experience/habit bias (prior responses), salience bias (prominent alarms), similarity bias (comparing to past upsets), and bounded rationality (information overload) are all natural in this context. [jobbank.gc](https://www.jobbank.gc.ca/marketreport/occupation/20478/geo29315;jsessionid=AE441A634A126432DE5E0C1B5C101514.jobsearch77)
- **Primary CTA scenario:** Responding to distillation column pressure excursion with multiple alarms; recency of similar upsets, availability of recent incidents, experience/habit in prior responses, availability of vivid scenarios, salience of alarms, similarity to past upsets, bounded rationality in information overload.
- **Triggering event:** Process control operator receives multiple alarms indicating distillation column pressure excursion; situation developing rapidly with incomplete information.
- **Decision episodes:**
  1. Initial upset assessment and alarm evaluation.
  2. Comparison to recent upsets and prior experience.
  3. Response action selection and implementation.
  4. Final upset resolution and documentation.
- **Available cues and evidence:** Alarm indications, process trends, recent upset history, prior experience, field operator input, procedural requirements, engineering support.
- **Competing interpretations:** Upset reflects genuine process issue requiring immediate action vs. upset is transient or instrument error; recent upset history supports immediate action vs. further investigation needed.
- **Plausible actions:** Take immediate corrective action; investigate further before action; notify field operators and await input; initiate emergency shutdown.
- **Constraints and pressures:** Time pressure for response, process criticality, procedural requirements, field operator coordination, personal safety, production targets.
- **Consequences of error:** Unnecessary process shutdown affecting production vs. delayed action leading to equipment damage or safety incident.
- **Counterfactual causal variable:** Actual cause of pressure excursion (later found that excursion was caused by instrument malfunction; no process issue existed).
- **Expected interview structure:** Opening (process control operator role context), Episode 1 (initial upset assessment), Episode 2 (comparison to recent/prior), Episode 3 (response action and resolution), Closing (reflection on response process).
- **Natural biases:** Recency Bias, Availability Bias (x2, one is duplicate in list), Experience Bias or Frequency Bias or Habit, Salience Bias, Similarity Bias, Bounded Rationality.
- **Plausible but difficult biases:** One Availability Bias is duplicate in list (requires careful design to separate or treat as secondary).
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Reactor Operator (overlaps with Interview 6; less natural for recency in chemical process context).
- **Rejected alternative occupation 2:** Field Operator (overlaps with Interview 4; less natural for bounded rationality in control room context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (One Availability Bias is duplicate in list; requires careful design to separate or treat as secondary label)

***

## 4. Bias-by-occupation compatibility matrix

| Occupation | Imperfect Rationality | Salience Bias | Similarity Bias | Availability Bias | Bounded Rationality | Confirmation Bias | Experience/Frequency/Habit Bias | Recency Bias |
|------------|----------------------|---------------|-----------------|-------------------|---------------------|-------------------|--------------------------------|--------------|
| Shift Supervisor / Control Room Supervisor | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE |
| Chemistry Technician / Radiochemistry Laboratory Technician | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE |
| Maintenance Planner / Outage Coordinator | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL |
| Field Operator / Equipment Operator (Nuclear) | NATURAL | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL |
| Procedure Engineer / Technical Procedure Writer | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | NATURAL | NATURAL |
| Reactor Operator (NRC-licensed) | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL |
| Process Control Operator (Chemical/Petrochemical) | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL |

**Explanations for non-NATURAL cells:**
- **PLAUSIBLE:** Bias can be embedded with moderate scenario design effort (e.g., Salience Bias in Shift Supervisor role requires prominent alarm or indication design).

***

## 5. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations | None | None | None | None needed |
| Work setting | Control room (1, 6, 7), Laboratory (2), Office/field interface (3, 5), Field-based (4) | Control room (3/7) | Control room | Office-based analytical, Industrial/technical | None critical; reflects nuclear/process operations nature |
| Decision type | Assessment (1, 2, 6), Planning (3, 5), Response (4, 7) | Assessment (3/7), Response (2/7) | Assessment | Diagnosis, Emergency response | None critical; assessment is natural for nuclear |
| Information environment | Data-heavy (1, 2, 6, 7), Conflicting sources (1, 6, 7), Incomplete (4, 7), Regulated (1, 3, 5, 6) | Data-heavy (4/7), Regulated (4/7) | Data-heavy, Regulated | Rich/structured, Socially mediated | None critical; reflects nuclear information complexity |
| Time pressure | Moderate (1, 2, 3, 5), High (4, 6, 7) | Moderate (4/7), High (3/7) | Balanced | Low | None needed |
| Consequence of error | Safety (4, 6, 7), Operational (1, 3, 4, 6, 7), Regulatory (1, 2, 5, 6), Financial (3, 5, 7) | Operational (5/7), Safety (3/7) | Operational, Safety | Environmental, Educational | None critical; reflects nuclear consequence profile |
| Expertise level | Independent professional (2, 4, 7), Senior practitioner (1, 6), Specialist (3, 5) | Independent professional (3/7), Senior practitioner (2/7) | Balanced | Developing practitioner, Supervisor/manager | None needed |
| Stakeholder pattern | Individual (2, 4), Team (1, 6, 7), Multi-party (3, 5) | Team (3/7) | Team | One-to-one, Public interaction | None critical |
| Scenario archetype | Assessment (1, 2, 6), Planning (3, 5), Response (4, 7) | Assessment (3/7), Planning (2/7), Response (2/7) | Balanced | Emergency response, Negotiation | None critical |
| Causal-counterfactual structure | Data accuracy (1, 2, 6), Equipment/process cause (4, 7), Recommendation accuracy (3), Event analysis (5) | Data accuracy (3/7) | Data accuracy | Equipment failure, Human performance | None critical; reflects nuclear causal structure |

**Overall assessment:** Good diversity across occupations, settings, decision types, and consequence profiles. Control room roles are slightly overrepresented (3/7), but this reflects the nature of nuclear/process operations where control room decision-making is prominent. No critical substitutions needed.

***

## 6. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Imperfect Rationality (clear mechanism: deviation from rational decision-making) | None | None | None | None | None | Ensure clear competing demands; probe decision reasoning explicitly |
| 2 | Salience Bias (prominent values), Similarity Bias (historical comparison) | None | None | None | None | None | Provide clear prominent cues; separate salience from similarity |
| 3 | Availability Bias (recent issues), Bounded Rationality (optimization limits), Confirmation Bias (seeking supporting data) | Availability and Confirmation (both involve information selection) | None | None | None | None | Separate recent issues from confirmation seeking; probe optimization constraints |
| 4 | Experience/Habit Bias (prior responses), Recency Bias (recent alarms), Imperfect Rationality (stress), Salience Bias (prominent alarms) | Recency and Experience/Habit (both involve prior events), Imperfect Rationality and Salience (both involve stress/prominence) | None | None | Imperfect Rationality (stress cues may be subtle) | Imperfect Rationality | Provide clear stress indicators; separate recency from experience |
| 5 | Similarity Bias (past procedures), Bounded Rationality (optimization limits), Experience/Habit Bias (prior revisions), Recency Bias (recent event), Imperfect Rationality (competing demands) | Similarity and Experience/Habit (both involve past), Recency and Experience/Habit (both involve prior events) | None | None | Imperfect Rationality (competing demands cues may be subtle) | Imperfect Rationality | Provide clear competing demands; separate similarity from experience |
| 6 | Confirmation Bias (x2, separate episodes), Imperfect Rationality, Salience Bias, Similarity Bias, Bounded Rationality | Confirmation Bias (x2, must be in separate episodes), Salience and Confirmation (both involve information selection) | None | None | Imperfect Rationality (stress cues may be subtle) | Imperfect Rationality | Provide clear stress indicators; separate confirmation episodes |
| 7 | Recency Bias, Availability Bias (x2, one duplicate), Experience/Habit Bias, Salience Bias, Similarity Bias, Bounded Rationality | Availability Bias (x2, one is duplicate), Recency and Availability (both involve memory), Similarity and Experience/Habit (both involve past) | None | None | Availability Bias (duplicate in list), Bounded Rationality (information overload cues may be subtle) | Availability Bias (duplicate), Bounded Rationality | Provide clear information overload; separate recency from availability |

**Overall safeguards:**
- **Prompt 1 (interview generation):** Ensure each bias has distinct cues and decision episodes; avoid conflating memory-based biases (Recency, Availability, Experience/Habit) with information-selection biases (Confirmation, Salience).
- **Prompt 2 (annotation):** Provide clear bias definitions and decision episode boundaries; require annotators to identify specific cues for each bias.

***

## 7. Final generation handoff blocks

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
1

SELECTED OCCUPATION:
Shift Supervisor / Control Room Supervisor (Nuclear)

ROLE AND SETTING:
Supervisory role in nuclear power plant control room; oversees reactor operators, field operators, and control room activities; responsible for shift performance, regulatory compliance, and emergency response coordination.

REQUESTED BIASES:
Imperfect Rationality

PRIMARY SCENARIO:
Evaluating whether to proceed with planned maintenance during minor instrument fluctuation; imperfect rationality in balancing procedural compliance with operational judgment.

DECISION EPISODES:
1. Initial assessment of instrument fluctuation and maintenance readiness.
2. Consultation with reactor operators and engineering support.
3. Risk-benefit analysis of proceeding vs. delaying maintenance.
4. Final decision on maintenance authorization and documentation.

AVAILABLE INFORMATION AND CUES:
Instrument readings, maintenance work orders, procedural requirements, operator assessments, engineering input, historical data on similar fluctuations.

COMPETING INTERPRETATIONS:
Fluctuation is benign and maintenance can proceed vs. fluctuation indicates underlying issue requiring investigation; procedural compliance requires delay vs. operational judgment supports proceeding.

CONSTRAINTS AND PRESSURES:
Maintenance schedule and resource availability, regulatory compliance requirements, operational continuity, shift staffing limitations, management expectations.

CONSEQUENCES:
Unnecessary maintenance delay costing resources and schedule vs. proceeding with maintenance that could exacerbate underlying issue leading to operational upset.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual cause of instrument fluctuation (later found that fluctuation was sensor drift; no underlying issue existed).

BIAS-SPECIFIC DESIGN NOTES:
Imperfect Rationality should manifest as deviation from purely rational decision-making due to cognitive limitations, stress, or competing demands. Supervisor should balance procedural compliance with operational judgment, showing deviation from optimal rational choice.

BIAS PAIRS TO KEEP SEPARATE:
None (single bias).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
2

SELECTED OCCUPATION:
Chemistry Technician / Radiochemistry Laboratory Technician

ROLE AND SETTING:
Laboratory-based analytical role within nuclear power plant; analyzes coolant, water chemistry, and radiochemistry samples to support plant operations and regulatory compliance.

REQUESTED BIASES:
Salience Bias, Similarity Bias

PRIMARY SCENARIO:
Analyzing coolant sample showing anomalous readings; salience of striking values, similarity bias comparing to past samples.

DECISION EPISODES:
1. Initial data review and comparison to technical specifications.
2. Comparison to historical samples and baseline trends.
3. Consultation with chemistry supervisor and operations on sample validity.
4. Final determination on sample acceptance and recommendation on plant chemistry adjustments.

AVAILABLE INFORMATION AND CUES:
Analytical instrument readings, technical specifications, historical sample data, sample collection records, plant operating conditions, supervisor input.

COMPETING INTERPRETATIONS:
Anomalous readings reflect genuine chemistry change vs. sampling or analytical error; historical similarity supports acceptance vs. deviation requires rejection.

CONSTRAINTS AND PRESSURES:
Technical specification compliance, sample stability time limits, operational chemistry requirements, laboratory workload, regulatory reporting deadlines.

CONSEQUENCES:
Unnecessary chemistry adjustments wasting resources vs. accepting bad sample leading to undetected chemistry degradation.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual sample validity (later found that sample was contaminated during collection; analytical readings were accurate but sample was not representative).

BIAS-SPECIFIC DESIGN NOTES:
Salience Bias should manifest as overweighting striking or prominent values in analytical readings. Similarity Bias should manifest as comparing to similar past samples and assuming similar validity.

BIAS PAIRS TO KEEP SEPARATE:
Salience Bias and Similarity Bias (distinct mechanisms: one involves prominence, the other involves historical comparison).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
3

SELECTED OCCUPATION:
Maintenance Planner / Outage Coordinator

ROLE AND SETTING:
Planning role within nuclear power plant; coordinates refueling outages, maintenance activities, and resource allocation; interfaces with operations, engineering, and contractors.

REQUESTED BIASES:
Availability Bias, Bounded Rationality, Confirmation Bias

PRIMARY SCENARIO:
Planning refueling outage scope with competing priorities; availability of recent issues, bounded rationality in scope optimization, confirmation in vendor recommendations.

DECISION EPISODES:
1. Initial scope review and prioritization of maintenance activities.
2. Resource allocation and scheduling optimization.
3. Vendor recommendation evaluation and confirmation.
4. Final scope approval and communication to stakeholders.

AVAILABLE INFORMATION AND CUES:
Maintenance work orders, resource availability, vendor recommendations, regulatory requirements, historical outage data, operations input, engineering assessments.

COMPETING INTERPRETATIONS:
Recent issues should be prioritized vs. long-term reliability should be prioritized; vendor recommendations are optimal vs. require modification; scope is achievable vs. requires reduction.

CONSTRAINTS AND PRESSURES:
Outage schedule and critical path, resource limitations, regulatory requirements, operations priorities, budget constraints, contractor availability.

CONSEQUENCES:
Unnecessary scope reduction affecting long-term reliability vs. over-scoping leading to schedule delays and cost overruns.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of vendor recommendations (later found that one vendor recommendation was based on incomplete data; activity was not actually required).

BIAS-SPECIFIC DESIGN NOTES:
Availability Bias should manifest as relying on recent or memorable issues in prioritization. Bounded Rationality should manifest as optimizing within cognitive and information constraints. Confirmation Bias should manifest as seeking data supporting preferred scope.

BIAS PAIRS TO KEEP SEPARATE:
Availability and Confirmation (distinct mechanisms: one involves memory, the other involves information selection).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
4

SELECTED OCCUPATION:
Field Operator / Equipment Operator (Nuclear)

ROLE AND SETTING:
Field-based operational role within nuclear power plant; conducts equipment rounds, responds to alarms, performs field operations and troubleshooting; works in plant areas with direct equipment access.

REQUESTED BIASES:
Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality, Salience Bias

PRIMARY SCENARIO:
Responding to pump vibration alarm during routine rounds; experience/habit in prior responses, recency of similar alarms, imperfect rationality in stress, salience of alarm.

DECISION EPISODES:
1. Initial alarm assessment and equipment inspection.
2. Comparison to recent similar alarms and prior experience.
3. Decision on immediate action vs. further investigation.
4. Final action and communication to control room.

AVAILABLE INFORMATION AND CUES:
Alarm indications, equipment vibration readings, recent alarm history, prior experience with similar alarms, equipment condition indicators, control room communications.

COMPETING INTERPRETATIONS:
Alarm reflects genuine equipment issue requiring immediate action vs. alarm is transient or false; prior experience supports immediate action vs. further investigation needed.

CONSTRAINTS AND PRESSURES:
Time pressure for response, equipment criticality, procedural requirements, control room coordination, personal safety, shift staffing.

CONSEQUENCES:
Unnecessary equipment shutdown affecting operations vs. delayed action leading to equipment damage or operational upset.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual cause of vibration alarm (later found that alarm was caused by temporary process condition; no equipment issue existed).

BIAS-SPECIFIC DESIGN NOTES:
Experience/Habit Bias should manifest as relying on prior responses. Recency Bias should manifest as overweighting recent similar alarms. Imperfect Rationality should manifest as deviation from rational decision-making under stress. Salience Bias should manifest as overweighting prominent alarm.

BIAS PAIRS TO KEEP SEPARATE:
Recency and Experience/Habit (distinct mechanisms: one involves recent events, the other involves accumulated experience); Imperfect Rationality and Salience (distinct mechanisms: one involves stress, the other involves prominence).

BIAS MECHANISMS NOT TO FORCE:
Imperfect Rationality (requires clear stress indicators).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
5

SELECTED OCCUPATION:
Procedure Engineer / Technical Procedure Writer

ROLE AND SETTING:
Engineering role within nuclear power plant; writes and revises operating procedures, emergency procedures, and technical documentation; interfaces with operations, engineering, and regulatory compliance.

REQUESTED BIASES:
Similarity Bias, Bounded Rationality, Experience Bias or Frequency Bias or Habit, Recency Bias, Imperfect Rationality

PRIMARY SCENARIO:
Revising emergency operating procedure after near-miss; similarity to past procedures, bounded rationality in revision scope, experience bias in prior revisions, recency of event, imperfect rationality in balancing competing demands.

DECISION EPISODES:
1. Initial procedure review and near-miss event analysis.
2. Comparison to past procedures and prior revisions.
3. Stakeholder consultation and revision scope optimization.
4. Final procedure approval and regulatory submission.

AVAILABLE INFORMATION AND CUES:
Near-miss event reports, existing procedures, historical revision data, stakeholder input, regulatory requirements, operational feedback.

COMPETING INTERPRETATIONS:
Near-miss requires significant procedure change vs. minor revision is sufficient; past procedures are appropriate baseline vs. require major modification; stakeholder inputs are consistent vs. conflicting.

CONSTRAINTS AND PRESSURES:
Regulatory compliance deadlines, operational continuity, stakeholder consensus, documentation workload, management expectations.

CONSEQUENCES:
Unnecessary procedure complexity affecting operator performance vs. insufficient revision leaving operational vulnerabilities.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of near-miss event analysis (later found that near-miss was mischaracterized; procedure revision was not actually required).

BIAS-SPECIFIC DESIGN NOTES:
Similarity Bias should manifest as comparing to past procedures. Bounded Rationality should manifest as optimizing within constraints. Experience/Habit Bias should manifest as relying on prior revisions. Recency Bias should manifest as overweighting recent event. Imperfect Rationality should manifest as deviation from rational decision-making due to competing demands.

BIAS PAIRS TO KEEP SEPARATE:
Similarity and Experience/Habit (distinct mechanisms: one involves comparison, the other involves accumulated experience); Recency and Experience/Habit (distinct mechanisms: one involves recent events, the other involves accumulated experience).

BIAS MECHANISMS NOT TO FORCE:
Imperfect Rationality (requires clear competing demands).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
6

SELECTED OCCUPATION:
Reactor Operator (NRC-licensed)

ROLE AND SETTING:
Licensed control room role within nuclear power plant; directly operates reactor and primary plant systems, executes emergency procedures, maintains regulatory compliance; works in control room with human-machine collaboration.

REQUESTED BIASES:
Confirmation Bias, Imperfect Rationality, Salience Bias, Similarity Bias, Bounded Rationality, Confirmation Bias

PRIMARY SCENARIO:
Managing reactor power maneuver with conflicting instrument indications; confirmation in initial assessment, imperfect rationality under time pressure, salience of alarms, similarity to past maneuvers, bounded rationality in information processing, confirmation in seeking supporting data.

DECISION EPISODES:
1. Initial reactor state assessment and maneuver planning.
2. Instrument indication evaluation and conflict resolution.
3. Maneuver execution with ongoing monitoring.
4. Final reactor state confirmation and documentation.

AVAILABLE INFORMATION AND CUES:
Instrument readings, alarm indications, procedural requirements, prior maneuver experience, control room communications, engineering support.

COMPETING INTERPRETATIONS:
Instrument conflict reflects sensor error vs. genuine reactor state change; initial assessment is accurate vs. requires revision; maneuver can proceed vs. requires modification.

CONSTRAINTS AND PRESSURES:
Time pressure for maneuver, procedural compliance, regulatory requirements, control room coordination, operational continuity, personal regulatory accountability.

CONSEQUENCES:
Unnecessary maneuver suspension affecting operations vs. proceeding with maneuver that could lead to operational upset or regulatory violation.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of instrument indications (later found that one instrument was calibrated incorrectly; indications were misleading).

BIAS-SPECIFIC DESIGN NOTES:
Confirmation Bias should manifest in two separate episodes (initial assessment and seeking supporting data). Imperfect Rationality should manifest as deviation from rational decision-making under time pressure. Salience Bias should manifest as overweighting prominent alarms. Similarity Bias should manifest as comparing to past maneuvers. Bounded Rationality should manifest as information processing limits.

BIAS PAIRS TO KEEP SEPARATE:
Confirmation Bias (x2, must be in separate episodes); Salience and Confirmation (distinct mechanisms: one involves prominence, the other involves information selection).

BIAS MECHANISMS NOT TO FORCE:
Imperfect Rationality (requires clear time pressure indicators).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Nuclear Power and Process-control operations

INTERVIEW ID:
7

SELECTED OCCUPATION:
Process Control Operator (Chemical/Petrochemical Refinery)

ROLE AND SETTING:
Control room role within chemical/petrochemical refinery; monitors and controls distillation columns, reactors, and other process units; interfaces with field operators and maintenance.

REQUESTED BIASES:
Recency Bias, Availability Bias, Experience Bias or Frequency Bias or Habit, Availability Bias, Salience Bias, Similarity Bias, Bounded Rationality

PRIMARY SCENARIO:
Responding to distillation column pressure excursion with multiple alarms; recency of similar upsets, availability of recent incidents, experience/habit in prior responses, availability of vivid scenarios, salience of alarms, similarity to past upsets, bounded rationality in information overload.

DECISION EPISODES:
1. Initial upset assessment and alarm evaluation.
2. Comparison to recent upsets and prior experience.
3. Response action selection and implementation.
4. Final upset resolution and documentation.

AVAILABLE INFORMATION AND CUES:
Alarm indications, process trends, recent upset history, prior experience, field operator input, procedural requirements, engineering support.

COMPETING INTERPRETATIONS:
Upset reflects genuine process issue requiring immediate action vs. upset is transient or instrument error; recent upset history supports immediate action vs. further investigation needed.

CONSTRAINTS AND PRESSURES:
Time pressure for response, process criticality, procedural requirements, field operator coordination, personal safety, production targets.

CONSEQUENCES:
Unnecessary process shutdown affecting production vs. delayed action leading to equipment damage or safety incident.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual cause of pressure excursion (later found that excursion was caused by instrument malfunction; no process issue existed).

BIAS-SPECIFIC DESIGN NOTES:
Recency Bias should manifest as overweighting recent similar upsets. Availability Bias should manifest in two forms (recent incidents and vivid scenarios); one is duplicate in list and requires careful design to separate or treat as secondary. Experience/Habit Bias should manifest as relying on prior responses. Salience Bias should manifest as overweighting prominent alarms. Similarity Bias should manifest as comparing to past upsets. Bounded Rationality should manifest as information processing limits under overload.

BIAS PAIRS TO KEEP SEPARATE:
Recency and Availability (distinct mechanisms: one involves recent events, the other involves memory); Availability Bias (x2, one is duplicate in list); Similarity and Experience/Habit (distinct mechanisms: one involves comparison, the other involves accumulated experience).

BIAS MECHANISMS NOT TO FORCE:
Availability Bias (duplicate in list; requires careful design to separate or treat as secondary label).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

***

## 8. Machine-readable JSON

Removed to .json file
