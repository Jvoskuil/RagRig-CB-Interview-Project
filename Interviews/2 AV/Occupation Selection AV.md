## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Aviation Maintenance Planner / Reliability Engineer | Reliability trend threshold breach requiring maintenance program change with conflicting data sources | 100% | 3 | High | Adds data-heavy, office-based forecasting role | APPROVED |
| 2 | 2 | Airline Transport Pilot (ATP) – Scheduled Carrier | In-flight weather deviation with marginal fuel and conflicting forecasts under ATC constraints | 100% | 6 | High | Adds high-reliability, time-pressured flight deck setting | APPROVED |
| 3 | 3 | Load Controller / Loadmaster (Commercial) | Last-minute passenger/baggage change requiring weight and balance recalculation under departure deadline with automated load software | 100% | 9 | High | Adds ramp/operations, human-machine collaboration, safety-critical calculation | APPROVED |
| 4 | 4 | Check Airman / Type Rating Instructor (TRI/TRE) | Trainee performance borderline pass/fail with operational safety implications and regulatory standards | 75% | 10 | Moderate-High | Adds training/evaluation, experiential judgment, educational consequences | APPROVED_WITH_CAVEATS (Bias Blind Spot requires meta-cognitive probes) |
| 5 | 5 | Director of Maintenance (DOM) – Part 135/121 | Grounding decision for fleet-wide recurring defect with conflicting engineering assessments, budget pressure, and regulatory exposure | 100% | 15 | High | Adds strategic, multi-stakeholder, high-consequence managerial decision | APPROVED |
| 6 | 6 | Flight Dispatcher / Flight Operations Officer | Dispatch release with marginal weather at destination, limited alternates, cost pressures, and conflicting information sources | 100% | 17 | High | Adds operations control center, planning under uncertainty, regulatory/financial/safety trade-offs | APPROVED |
| 7 | 7 | Continuing Airworthiness Manager (CAMO) | Airworthiness directive compliance deadline with fleet grounding implications, parts availability, and conflicting reliability data | 86% | 19 | Moderate-High | Adds regulatory compliance, long-horizon planning, documentation-heavy setting | APPROVED_WITH_CAVEATS (Bias Blind Spot and Illusion of validity require careful design) |

***

## 2. Candidate occupation matrix

### Interview 1 (Information bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Aviation Maintenance Planner / Reliability Engineer | 1 (Information bias) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multiple data sources, trend analysis) | High (change data source reliability) | High | High (adds forecasting role) | 0.88 |
| Flight Dispatcher | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.75 |
| Air Traffic Controller | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (less data-overload context) | 0.55 |
| Line Maintenance Technician | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Medium | 0.58 |
| Airport Operations Duty Manager | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Low | 0.42 |

**Selected:** Aviation Maintenance Planner / Reliability Engineer (best coverage, distinctness, diversity fit).

***

### Interview 2 (Omitting subjectivity, Plan Continuation)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Airline Transport Pilot (ATP) | 2 (Omitting subjectivity, Plan Continuation) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (multiple decision phases) | High (change weather forecast accuracy) | High | High (adds flight deck emergency-adjacent) | 0.90 |
| Flight Dispatcher | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Medium (overlaps with Interview 6) | 0.78 |
| Air Traffic Controller | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Medium (less subjective judgment) | 0.72 |
| Line Maintenance Technician | 1 | 1 | 0 | 0 | 75% | Moderate | Moderate | Moderate | High | Medium | 0.68 |
| Load Controller | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low | 0.55 |

**Selected:** ATP (best coverage, distinctness, scenario richness, diversity).

***

### Interview 3 (Substitution bias, Apophenia/Correlation Bias, Automaticity/Automation Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Load Controller / Loadmaster | 3 (Substitution, Apophenia, Automation) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (multiple calculations, software reliance) | High (change software output accuracy) | High | High (adds ramp operations, human-machine) | 0.92 |
| Flight Dispatcher | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 6) | 0.80 |
| Air Traffic Controller | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Medium (less substitution context) | 0.76 |
| Aviation Maintenance Planner | 1 | 2 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| Line Maintenance Technician | 1 | 1 | 1 | 0 | 67% | Moderate | Moderate | Moderate | High | Medium | 0.62 |

**Selected:** Load Controller (best coverage, distinctness, diversity fit).

***

### Interview 4 (Bias Blind Spot, Normalcy Bias, Experience Bias/Trusting expert intuition, Illusion of validity)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Check Airman / TRI/TRE | 2 (Normalcy, Experience Bias) | 2 (Bias Blind Spot, Illusion of validity) | 0 | 0 | 100% | Moderate-High (Bias Blind Spot requires meta-cognition) | High (evaluation phases, judgment calls) | High (change trainee actual performance level) | High | High (adds training/evaluation role) | 0.85 |
| Line Maintenance Technician | 2 | 1 | 1 | 0 | 75% | Moderate | Moderate | Moderate | High | Medium (overlaps with maintenance roles) | 0.68 |
| Aviation Maintenance Planner | 1 | 2 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.65 |
| Director of Maintenance | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Medium (overlaps with Interview 5) | 0.70 |
| Air Traffic Controller | 1 | 2 | 1 | 0 | 75% | Moderate | High | High | High | Medium | 0.68 |

**Selected:** Check Airman / TRI/TRE (best diversity fit, adds training context; Bias Blind Spot is plausible with careful design).

***

### Interview 5 (Optimism, Authority Bias, Sunk Cost Fallacy, Representativeness, Overconfidence)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Director of Maintenance (DOM) | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (multiple stakeholders, phases) | High (change engineering assessment accuracy) | High | High (adds strategic managerial role) | 0.94 |
| Airport Operations Duty Manager | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with operations) | 0.82 |
| Base Maintenance Supervisor | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with maintenance) | 0.80 |
| Flight Dispatcher | 3 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| CAMO | 3 | 2 | 0 | 0 | 80% | Moderate-High | High | High | High | Medium (overlaps with Interview 7) | 0.74 |

**Selected:** DOM (best coverage, distinctness, diversity fit).

***

### Interview 6 (Anchoring Bias, Confirmation Bias, Information bias, Omitting subjectivity, Plan Continuation, Substitution bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Flight Dispatcher / FOO | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms) | High (multiple decision phases, information sources) | High (change weather forecast accuracy) | High | High (adds operations control center) | 0.95 |
| Airline Transport Pilot | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Medium (overlaps with Interview 2) | 0.85 |
| Air Traffic Controller | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Medium | 0.78 |
| Aviation Maintenance Planner | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.72 |
| Load Controller | 3 | 2 | 1 | 0 | 75% | Moderate-High | Moderate | Moderate | High | Medium | 0.65 |

**Selected:** Flight Dispatcher (best coverage, distinctness, scenario richness).

***

### Interview 7 (Apophenia/Correlation Bias, Automaticity/Automation Bias, Bias Blind Spot, Normalcy Bias, Experience Bias/Trusting expert intuition, Illusion of validity, Optimism)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Continuing Airworthiness Manager (CAMO) | 5 (Apophenia, Automation, Normalcy, Experience Bias, Optimism) | 2 (Bias Blind Spot, Illusion of validity) | 0 | 0 | 100% | Moderate-High (Bias Blind Spot, Illusion require meta-cognition) | High (multiple phases, data sources) | High (change AD compliance data accuracy) | High | High (adds regulatory compliance role) | 0.88 |
| Aviation Maintenance Planner | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.80 |
| Director of Maintenance | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Medium (overlaps with Interview 5) | 0.78 |
| Base Maintenance Supervisor | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Medium | 0.75 |
| Flight Dispatcher | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.76 |

**Selected:** CAMO (best diversity fit, adds regulatory compliance context; Bias Blind Spot and Illusion of validity are plausible with careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Information bias
- **Selected occupation:** Aviation Maintenance Planner / Reliability Engineer
- **Role and setting:** Office-based analytical role within airline/MRO reliability department; interfaces with maintenance operations, engineering, and regulatory compliance.
- **Why this occupation fits the bias list:** This role routinely synthesizes large volumes of maintenance data (fault reports, reliability trends, engine health monitoring, component removal rates) from multiple software systems. Information bias (over-reliance on abundant but low-quality or redundant data) can naturally arise when deciding whether to change maintenance intervals or programs based on conflicting data sources.
- **Primary CTA scenario:** Reliability trend threshold breach requiring maintenance program change with conflicting data sources.
- **Triggering event:** Reliability software flags a component type exceeding removal rate threshold, triggering potential maintenance program change.
- **Decision episodes:**
  1. Initial data review across multiple sources (reliability database, engine health monitoring, maintenance records).
  2. Consultation with engineering and maintenance control on root cause hypotheses.
  3. Recommendation on maintenance program change (interval reduction, task modification, or no change).
  4. Documentation and regulatory submission preparation.
- **Available cues and evidence:** Reliability trend graphs, component removal logs, engine health monitoring data, maintenance defect reports, OEM service bulletins, regulatory guidance.
- **Competing interpretations:** Data reflects genuine reliability degradation vs. data artifact (reporting changes, sensor drift, operational changes); proactive program change vs. wait for more data.
- **Plausible actions:** Recommend immediate program change; recommend monitoring with enhanced data collection; recommend no change pending further investigation.
- **Constraints and pressures:** Regulatory compliance deadlines, cost implications of program change, operational impact of increased maintenance, conflicting expert opinions.
- **Consequences of error:** Unnecessary maintenance cost and downtime vs. undetected reliability risk leading to in-service failures.
- **Counterfactual causal variable:** Accuracy/reliability of one data source (e.g., engine health monitoring data is later found to have sensor calibration drift).
- **Expected interview structure:** Opening (role context), Episode 1 (initial data review), Episode 2 (consultation and hypothesis formation), Episode 3 (recommendation decision), Closing (reflection on information sources).
- **Natural biases:** Information bias (over-weighting abundant data sources).
- **Plausible but difficult biases:** None for this single-bias list.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Flight Dispatcher (would overlap with Interview 6; less distinct data-overload context).
- **Rejected alternative occupation 2:** Air Traffic Controller (less natural fit for Information bias; more time-pressured, less data-heavy).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Omitting subjectivity, Plan Continuation
- **Selected occupation:** Airline Transport Pilot (ATP) – Scheduled Carrier
- **Role and setting:** Flight deck of commercial airliner; high-reliability, safety-critical, time-pressured environment.
- **Why this occupation fits the bias list:** Pilots must integrate objective data (weather radar, fuel calculations, ATC constraints) with subjective judgment (risk tolerance, situational awareness). Omitting subjectivity (downplaying gut feeling or experiential cues in favor of "objective" data) and Plan Continuation (sticking with original flight plan despite changing conditions) are well-documented in aviation decision-making.
- **Primary CTA scenario:** In-flight weather deviation with marginal fuel and conflicting forecasts under ATC constraints.
- **Triggering event:** En-route weather radar shows building convective activity ahead; original flight plan becomes questionable.
- **Decision episodes:**
  1. Initial weather assessment and comparison with dispatch forecast.
  2. Fuel calculation for deviation options vs. destination alternate.
  3. ATC coordination for deviation clearance.
  4. Final go/no-go decision for deviation vs. continuation.
- **Available cues and evidence:** Weather radar, ACARS updates, dispatch weather forecasts, fuel state, ATC traffic constraints, company fuel policy, prior experience with similar weather patterns.
- **Competing interpretations:** Weather is passable with minor deviation vs. weather requires significant reroute; subjective concern about fuel margin vs. objective fuel calculations showing compliance.
- **Plausible actions:** Request deviation clearance; continue on plan with monitoring; divert to alternate pre-emptively.
- **Constraints and pressures:** Fuel margins, ATC traffic flow, company policy, passenger schedule, regulatory fuel requirements.
- **Consequences of error:** Fuel emergency, weather encounter, schedule disruption, regulatory violation.
- **Counterfactual causal variable:** Accuracy of dispatch weather forecast (later found to be outdated).
- **Expected interview structure:** Opening (flight context), Episode 1 (weather assessment), Episode 2 (fuel and options analysis), Episode 3 (ATC coordination and decision), Closing (reflection on subjective vs. objective factors).
- **Natural biases:** Omitting subjectivity (discounting gut feeling), Plan Continuation (sticking with original plan).
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Flight Dispatcher (overlaps with Interview 6; less time-pressured).
- **Rejected alternative occupation 2:** Air Traffic Controller (less natural for Omitting subjectivity; more system-focused).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Substitution bias, Apophenia/Correlation Bias, Automaticity/Automation Bias
- **Selected occupation:** Load Controller / Loadmaster (Commercial)
- **Role and setting:** Ramp/operations control; calculates aircraft weight and balance, ULD build-up, load sheet preparation; uses automated load planning software.
- **Why this occupation fits the bias list:** Load controllers routinely use automated software for weight and balance calculations. Substitution bias (using a simpler heuristic instead of complex calculation), Apophenia (seeing patterns in ULD weights or passenger distributions that aren't meaningful), and Automation Bias (over-relying on software output) are all plausible in this context.
- **Primary CTA scenario:** Last-minute passenger/baggage change requiring weight and balance recalculation under departure deadline with automated load software.
- **Triggering event:** Gate agent reports last-minute passenger no-shows and additional baggage additions 20 minutes before departure.
- **Decision episodes:**
  1. Initial load sheet review and software update.
  2. Manual verification of weight and balance calculations.
  3. ULD reconfiguration decision if needed.
  4. Final load sheet approval and transmission to flight crew.
- **Available cues and evidence:** Passenger manifest, baggage tags, ULD weights, aircraft weight and balance limits, software output, prior load sheets for similar flights.
- **Competing interpretations:** Software output is accurate vs. manual verification needed; pattern in baggage distribution is meaningful vs. random variation.
- **Plausible actions:** Accept software output; perform manual recalculation; reconfigure ULDs; delay departure for verification.
- **Constraints and pressures:** Departure deadline, crew duty time limits, gate constraints, regulatory weight and balance requirements.
- **Consequences of error:** Aircraft out of balance, performance limitations, regulatory violation, departure delay.
- **Counterfactual causal variable:** Software output accuracy (later found to have used outdated aircraft configuration data).
- **Expected interview structure:** Opening (role context), Episode 1 (initial load update), Episode 2 (verification decision), Episode 3 (ULD configuration and approval), Closing (reflection on software reliance).
- **Natural biases:** Substitution bias (using heuristic instead of full calculation), Apophenia (seeing patterns in baggage/passenger data), Automation Bias (trusting software output).
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Flight Dispatcher (overlaps with Interview 6; less natural for Apophenia).
- **Rejected alternative occupation 2:** Air Traffic Controller (less natural for Substitution and Apophenia).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Bias Blind Spot, Normalcy Bias, Experience Bias/Trusting expert intuition, Illusion of validity
- **Selected occupation:** Check Airman / Type Rating Instructor (TRI/TRE)
- **Role and setting:** Training organization/simulator center; evaluates trainee pilots during type rating or recurrent training; regulatory authority for pass/fail decisions.
- **Why this occupation fits the bias list:** Instructors rely heavily on experiential judgment and pattern recognition. Normalcy Bias (assuming trainee will perform normally based on prior performance), Experience Bias (trusting expert intuition over objective metrics), Illusion of validity (confidence in judgment based on past success), and Bias Blind Spot (failure to recognize own biases in evaluation) are all plausible, though Bias Blind Spot requires meta-cognitive probes.
- **Primary CTA scenario:** Trainee performance borderline pass/fail with operational safety implications and regulatory standards.
- **Triggering event:** Trainee exhibits inconsistent performance during simulator evaluation, with some maneuvers excellent and others marginal.
- **Decision episodes:**
  1. Initial performance assessment against regulatory standards.
  2. Comparison with prior training records and subjective impression.
  3. Consultation with other instructors (if available) or review of objective metrics.
  4. Final pass/fail decision and documentation.
- **Available cues and evidence:** Simulator performance metrics, regulatory evaluation criteria, prior training records, subjective impression of trainee's airmanship, peer input.
- **Competing interpretations:** Trainee is safe but inconsistent vs. trainee poses operational risk; objective metrics support pass vs. subjective concern about specific maneuvers.
- **Plausible actions:** Pass with recommendations; fail with remediation plan; extend evaluation for additional data.
- **Constraints and pressures:** Regulatory standards, training schedule, trainee career implications, organizational pressure to maintain throughput.
- **Consequences of error:** Unsafe pilot certified vs. qualified pilot unnecessarily delayed.
- **Counterfactual causal variable:** Trainee's actual performance level (later found that simulator had minor calibration issue affecting one maneuver).
- **Expected interview structure:** Opening (instructor role context), Episode 1 (initial assessment), Episode 2 (comparison with prior records), Episode 3 (decision and documentation), Closing (reflection on evaluation process).
- **Natural biases:** Normalcy Bias, Experience Bias/Trusting expert intuition.
- **Plausible but difficult biases:** Bias Blind Spot (requires meta-cognitive probes), Illusion of validity (requires careful design to separate from legitimate expertise).
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Line Maintenance Technician (less natural for Illusion of validity and Bias Blind Spot).
- **Rejected alternative occupation 2:** Air Traffic Controller (less natural for Experience Bias in evaluation context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Bias Blind Spot and Illusion of validity require careful meta-cognitive probe design)

***

### Interview 5

- **Requested biases:** Optimism, Authority Bias, Sunk Cost Fallacy, Representativeness, Overconfidence
- **Selected occupation:** Director of Maintenance (DOM) – Part 135/121
- **Role and setting:** Senior managerial role within airline/MRO; overall authority for maintenance operations, regulatory compliance, budget, and safety.
- **Why this occupation fits the bias list:** DOMs make high-stakes decisions with conflicting engineering assessments, budget pressures, and regulatory exposure. Optimism (believing issues will resolve favorably), Authority Bias (deferring to senior engineer or regulatory interpretation), Sunk Cost (continuing with maintenance approach due to already-invested resources), Representativeness (judging current defect based on similarity to past cases), and Overconfidence (confidence in maintenance program's ability to manage risk) are all naturally embedded.
- **Primary CTA scenario:** Grounding decision for fleet-wide recurring defect with conflicting engineering assessments, budget pressure, and regulatory exposure.
- **Triggering event:** Multiple aircraft report similar defect; engineering assessments conflict on root cause and corrective action.
- **Decision episodes:**
  1. Initial defect review and engineering consultation.
  2. Risk assessment and regulatory compliance evaluation.
  3. Budget and operational impact analysis.
  4. Final grounding vs. continued operation decision.
- **Available cues and evidence:** Defect reports, engineering assessments, regulatory guidance, maintenance history, budget constraints, operational schedule.
- **Competing interpretations:** Defect is systemic and requires grounding vs. defect is manageable with monitoring; engineering assessment A is correct vs. assessment B.
- **Plausible actions:** Ground fleet immediately; continue operation with enhanced monitoring; partial grounding with targeted inspections.
- **Constraints and pressures:** Regulatory compliance, budget limitations, operational schedule, customer commitments, safety reputation.
- **Consequences of error:** Unnecessary grounding cost vs. in-service failure with safety and regulatory implications.
- **Counterfactual causal variable:** Accuracy of one engineering assessment (later found that one assessment was based on incomplete data).
- **Expected interview structure:** Opening (DOM role context), Episode 1 (defect review), Episode 2 (risk and compliance evaluation), Episode 3 (decision and communication), Closing (reflection on decision factors).
- **Natural biases:** Optimism, Authority Bias, Sunk Cost Fallacy, Representativeness, Overconfidence.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Airport Operations Duty Manager (less natural for Representativeness and Sunk Cost in maintenance context).
- **Rejected alternative occupation 2:** Base Maintenance Supervisor (overlaps with maintenance but less strategic authority).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Anchoring Bias, Confirmation Bias, Information bias, Omitting subjectivity, Plan Continuation, Substitution bias
- **Selected occupation:** Flight Dispatcher / Flight Operations Officer
- **Role and setting:** Operations control center; plans and releases flights, monitors en-route conditions, coordinates with flight crews and ATC.
- **Why this occupation fits the bias list:** Dispatchers synthesize multiple information sources (weather forecasts, NOTAMs, aircraft status, crew constraints) under time pressure. Anchoring (initial flight plan), Confirmation (seeking data supporting plan), Information bias (over-reliance on abundant data), Omitting subjectivity (discounting gut feeling), Plan Continuation (sticking with plan), and Substitution (using heuristic instead of complex analysis) are all well-documented in dispatch decision-making.
- **Primary CTA scenario:** Dispatch release with marginal weather at destination, limited alternates, cost pressures, and conflicting information sources.
- **Triggering event:** Weather forecasts for destination airport show marginal conditions near minimums; alternate airports have limitations.
- **Decision episodes:**
  1. Initial flight plan development and weather review.
  2. Alternate airport evaluation and fuel calculation.
  3. Coordination with flight crew and operations control.
  4. Final dispatch release decision.
- **Available cues and evidence:** Weather forecasts (multiple sources), NOTAMs, aircraft status, crew duty time, company fuel policy, cost constraints, alternate airport availability.
- **Competing interpretations:** Weather will be at or above minimums vs. weather will deteriorate; initial plan is sound vs. alternative plan needed.
- **Plausible actions:** Release flight as planned; release with additional fuel; delay release pending updated forecasts; cancel flight.
- **Constraints and pressures:** Regulatory requirements, cost pressures, crew duty time, passenger schedule, aircraft availability.
- **Consequences of error:** Unnecessary delay/cancellation cost vs. fuel emergency or diversion with safety implications.
- **Counterfactual causal variable:** Accuracy of one weather forecast source (later found to be outdated).
- **Expected interview structure:** Opening (dispatcher role context), Episode 1 (initial plan and weather review), Episode 2 (alternate evaluation), Episode 3 (coordination and decision), Closing (reflection on information sources).
- **Natural biases:** Anchoring Bias, Confirmation Bias, Information bias, Omitting subjectivity, Plan Continuation, Substitution bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Airline Transport Pilot (overlaps with Interview 2; less natural for Information bias with multiple data sources).
- **Rejected alternative occupation 2:** Air Traffic Controller (less natural for Substitution and Omitting subjectivity).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Apophenia/Correlation Bias, Automaticity/Automation Bias, Bias Blind Spot, Normalcy Bias, Experience Bias/Trusting expert intuition, Illusion of validity, Optimism
- **Selected occupation:** Continuing Airworthiness Manager (CAMO)
- **Role and setting:** Office-based regulatory compliance role; manages airworthiness directives, reliability programs, maintenance program changes, and regulatory submissions.
- **Why this occupation fits the bias list:** CAMOs synthesize large volumes of data (AD compliance, reliability trends, maintenance records) and make judgment calls on compliance deadlines and program changes. Apophenia (seeing patterns in reliability data), Automation Bias (relying on compliance software), Bias Blind Spot (failure to recognize own biases), Normalcy Bias (assuming normal compliance patterns), Experience Bias (trusting expert intuition), Illusion of validity (confidence in judgment based on past success), and Optimism (believing issues will resolve favorably) are all plausible, though Bias Blind Spot and Illusion of validity require careful design.
- **Primary CTA scenario:** Airworthiness directive compliance deadline with fleet grounding implications, parts availability, and conflicting reliability data.
- **Triggering event:** AD compliance deadline approaching; parts availability is limited; reliability data shows conflicting trends on defect severity.
- **Decision episodes:**
  1. Initial AD review and compliance status assessment.
  2. Parts availability and maintenance capacity evaluation.
  3. Reliability data analysis and risk assessment.
  4. Final compliance decision (full compliance, partial compliance with exemption, or fleet grounding).
- **Available cues and evidence:** AD text, compliance records, parts availability, maintenance capacity, reliability trends, regulatory guidance, OEM input.
- **Competing interpretations:** AD requires immediate full compliance vs. partial compliance with exemption is acceptable; reliability data shows significant risk vs. risk is manageable.
- **Plausible actions:** Full compliance by deadline; partial compliance with regulatory exemption request; fleet grounding until parts available.
- **Constraints and pressures:** Regulatory deadlines, parts availability, maintenance capacity, operational schedule, safety reputation.
- **Consequences of error:** Unnecessary grounding cost vs. regulatory violation with safety implications.
- **Counterfactual causal variable:** Accuracy of reliability data (later found that one data source had reporting errors).
- **Expected interview structure:** Opening (CAMO role context), Episode 1 (AD review), Episode 2 (parts and capacity evaluation), Episode 3 (risk assessment and decision), Closing (reflection on decision factors).
- **Natural biases:** Apophenia/Correlation Bias, Automaticity/Automation Bias, Normalcy Bias, Experience Bias/Trusting expert intuition, Optimism.
- **Plausible but difficult biases:** Bias Blind Spot, Illusion of validity.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Aviation Maintenance Planner (overlaps with Interview 1; less regulatory authority).
- **Rejected alternative occupation 2:** Director of Maintenance (overlaps with Interview 5; less focus on AD compliance).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Bias Blind Spot and Illusion of validity require careful meta-cognitive probe design)

***

## 4. Bias-by-occupation compatibility matrix

| Occupation | Information bias | Omitting subjectivity | Plan Continuation | Substitution bias | Apophenia/Correlation Bias | Automaticity/Automation Bias | Bias Blind Spot | Normalcy Bias | Experience Bias/Trusting expert intuition | Illusion of validity | Optimism | Authority Bias | Sunk Cost Fallacy | Representativeness | Overconfidence | Anchoring Bias | Confirmation Bias |
|------------|------------------|-----------------------|-------------------|-------------------|---------------------------|-----------------------------|-----------------|---------------|------------------------------------------|----------------------|----------|----------------|-------------------|--------------------|----------------|----------------|-------------------|
| Aviation Maintenance Planner / Reliability Engineer | NATURAL | PLAUSIBLE | PLAUSIBLE | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | WEAK | PLAUSIBLE | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE |
| Airline Transport Pilot (ATP) | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | PLAUSIBLE | WEAK | NATURAL | NATURAL | NATURAL |
| Load Controller / Loadmaster | PLAUSIBLE | WEAK | PLAUSIBLE | NATURAL | NATURAL | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | WEAK | PLAUSIBLE | WEAK | WEAK | WEAK | PLAUSIBLE | NATURAL | PLAUSIBLE |
| Check Airman / TRI/TRE | WEAK | NATURAL | PLAUSIBLE | WEAK | WEAK | WEAK | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | WEAK | PLAUSIBLE | NATURAL | PLAUSIBLE | PLAUSIBLE |
| Director of Maintenance (DOM) | PLAUSIBLE | PLAUSIBLE | NATURAL | WEAK | PLAUSIBLE | WEAK | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE |
| Flight Dispatcher / FOO | NATURAL | NATURAL | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE | NATURAL | NATURAL | NATURAL |
| Continuing Airworthiness Manager (CAMO) | PLAUSIBLE | PLAUSIBLE | NATURAL | WEAK | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE |

**Explanations for non-NATURAL cells:**
- **WEAK:** Bias mechanism is possible but would require careful scenario design to avoid feeling artificial (e.g., Substitution bias in DOM role is less natural as decisions are typically data-driven).
- **PLAUSIBLE:** Bias can be embedded with moderate scenario design effort (e.g., Bias Blind Spot in most roles requires meta-cognitive probes).

***

## 5. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations | None | None | None | None needed |
| Work setting | Office (1, 5, 6, 7), Flight deck (2), Ramp/operations (3), Simulator/training (4) | Office-based (4/7) | Office/administrative | Field/outdoor, Industrial/technical | None critical; office overrepresentation reflects aviation decision-making nature |
| Decision type | Forecasting (1), Risk assessment (2, 5, 7), Resource allocation (3, 6), Evaluation (4) | Risk assessment (3/7) | Risk assessment | Troubleshooting, Emergency response | None critical; risk assessment is natural for aviation |
| Information environment | Data-heavy (1, 3, 6, 7), Rapidly changing (2, 6), Conflicting sources (1, 2, 5, 6, 7), Regulated (4, 5, 7) | Conflicting sources (5/7), Data-heavy (4/7) | Conflicting sources, Data-heavy | Primarily experiential, Socially mediated | None critical; reflects aviation information complexity |
| Time pressure | Moderate (1, 4, 5, 7), High (2, 3, 6) | Moderate (4/7) | Moderate | Low | None needed |
| Consequence of error | Safety (2, 3, 4, 5, 7), Financial (1, 5, 6, 7), Regulatory (1, 4, 5, 6, 7), Operational (1, 2, 3, 5, 6, 7) | Safety (5/7), Regulatory (5/7), Operational (6/7) | Safety, Regulatory, Operational | Environmental, Educational | None critical; reflects aviation consequence profile |
| Expertise level | Specialist (1, 3, 4, 7), Senior practitioner (2, 6), Manager/Strategist (5) | Specialist (4/7) | Specialist | Developing practitioner, Independent professional | None needed |
| Stakeholder pattern | Individual (1, 3), Team (2, 4, 6), Multi-party (5, 7) | Team (3/7) | Team | One-to-one, Public interaction | None critical |
| Scenario archetype | Data analysis (1, 7), In-flight decision (2), Load calculation (3), Evaluation (4), Strategic decision (5), Planning (6) | Data analysis (2/7) | Data analysis | Emergency response, Negotiation | None critical |
| Causal-counterfactual structure | Data accuracy (1, 7), Forecast accuracy (2, 6), Software accuracy (3), Performance level (4), Engineering assessment (5) | Data/forecast accuracy (4/7) | Data/forecast accuracy | Equipment failure, Human performance | None critical; reflects aviation causal structure |

**Overall assessment:** Good diversity across occupations, settings, decision types, and consequence profiles. Office-based and data-heavy roles are slightly overrepresented (4/7 each), but this reflects the nature of aviation decision-making where analytical roles are prominent. No critical substitutions needed.

***

## 6. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Information bias (clear mechanism: over-reliance on abundant data) | None | None | None | None | None | Ensure multiple data sources with varying quality; probe information weighting explicitly |
| 2 | Omitting subjectivity (discounting gut feeling), Plan Continuation (sticking with plan) | None | None | None | None | None | Separate subjective cues from objective data; probe plan revision triggers |
| 3 | Substitution (heuristic vs. calculation), Apophenia (pattern detection), Automation (software reliance) | Apophenia and Automation (both involve pattern/software) | None | None | Apophenia (pattern cues may be subtle) | Apophenia (needs clear pattern cues) | Provide explicit pattern cues in data; separate software output from manual calculation |
| 4 | Normalcy (assuming normal performance), Experience Bias (trusting intuition) | Bias Blind Spot and Illusion of validity (both meta-cognitive) | None | None | Bias Blind Spot (requires meta-cognitive probes), Illusion of validity (requires confidence calibration) | Bias Blind Spot, Illusion of validity | Include explicit meta-cognitive probes; separate confidence from accuracy |
| 5 | Optimism, Authority Bias, Sunk Cost, Representativeness, Overconfidence (all distinct mechanisms) | Authority Bias and Overconfidence (both involve confidence in others/self) | None | None | None | None | Separate authority input from personal confidence; probe sunk cost explicitly |
| 6 | Anchoring, Confirmation, Information, Omitting subjectivity, Plan Continuation, Substitution (all distinct) | Anchoring and Confirmation (both involve initial information), Information and Omitting subjectivity (both involve information weighting) | None | None | Omitting subjectivity (subjective cues may be subtle) | Omitting subjectivity | Provide clear subjective cues; separate initial anchor from subsequent information |
| 7 | Apophenia, Automation, Normalcy, Experience Bias, Optimism (distinct); Bias Blind Spot, Illusion of validity (meta-cognitive) | Bias Blind Spot and Illusion of validity (both meta-cognitive), Apophenia and Automation (both involve pattern/software) | None | None | Bias Blind Spot, Illusion of validity | Bias Blind Spot, Illusion of validity | Include explicit meta-cognitive probes; separate pattern cues from software output |

**Overall safeguards:**
- **Prompt 1 (interview generation):** Ensure each bias has distinct cues and decision episodes; avoid conflating meta-cognitive biases (Bias Blind Spot, Illusion of validity) with substantive biases.
- **Prompt 2 (annotation):** Provide clear bias definitions and decision episode boundaries; require annotators to identify specific cues for each bias.

***

## 7. Final generation handoff blocks

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
1

SELECTED OCCUPATION:
Aviation Maintenance Planner / Reliability Engineer

ROLE AND SETTING:
Office-based analytical role within airline/MRO reliability department; interfaces with maintenance operations, engineering, and regulatory compliance.

REQUESTED BIASES:
Information bias

PRIMARY SCENARIO:
Reliability trend threshold breach requiring maintenance program change with conflicting data sources.

DECISION EPISODES:
1. Initial data review across multiple sources (reliability database, engine health monitoring, maintenance records).
2. Consultation with engineering and maintenance control on root cause hypotheses.
3. Recommendation on maintenance program change (interval reduction, task modification, or no change).
4. Documentation and regulatory submission preparation.

AVAILABLE INFORMATION AND CUES:
Reliability trend graphs, component removal logs, engine health monitoring data, maintenance defect reports, OEM service bulletins, regulatory guidance.

COMPETING INTERPRETATIONS:
Data reflects genuine reliability degradation vs. data artifact (reporting changes, sensor drift, operational changes); proactive program change vs. wait for more data.

CONSTRAINTS AND PRESSURES:
Regulatory compliance deadlines, cost implications of program change, operational impact of increased maintenance, conflicting expert opinions.

CONSEQUENCES:
Unnecessary maintenance cost and downtime vs. undetected reliability risk leading to in-service failures.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy/reliability of one data source (e.g., engine health monitoring data is later found to have sensor calibration drift).

BIAS-SPECIFIC DESIGN NOTES:
Information bias should manifest as over-weighting abundant but low-quality data sources (e.g., engine health monitoring data with sensor drift) while under-weighting higher-quality but less abundant data (e.g., maintenance defect reports).

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
Aviation

INTERVIEW ID:
2

SELECTED OCCUPATION:
Airline Transport Pilot (ATP) – Scheduled Carrier

ROLE AND SETTING:
Flight deck of commercial airliner; high-reliability, safety-critical, time-pressured environment.

REQUESTED BIASES:
Omitting subjectivity, Plan Continuation

PRIMARY SCENARIO:
In-flight weather deviation with marginal fuel and conflicting forecasts under ATC constraints.

DECISION EPISODES:
1. Initial weather assessment and comparison with dispatch forecast.
2. Fuel calculation for deviation options vs. destination alternate.
3. ATC coordination for deviation clearance.
4. Final go/no-go decision for deviation vs. continuation.

AVAILABLE INFORMATION AND CUES:
Weather radar, ACARS updates, dispatch weather forecasts, fuel state, ATC traffic constraints, company fuel policy, prior experience with similar weather patterns.

COMPETING INTERPRETATIONS:
Weather is passable with minor deviation vs. weather requires significant reroute; subjective concern about fuel margin vs. objective fuel calculations showing compliance.

CONSTRAINTS AND PRESSURES:
Fuel margins, ATC traffic flow, company policy, passenger schedule, regulatory fuel requirements.

CONSEQUENCES:
Fuel emergency, weather encounter, schedule disruption, regulatory violation.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of dispatch weather forecast (later found to be outdated).

BIAS-SPECIFIC DESIGN NOTES:
Omitting subjectivity should manifest as discounting gut feeling or experiential cues in favor of "objective" data (e.g., fuel calculations). Plan Continuation should manifest as sticking with original flight plan despite changing weather conditions.

BIAS PAIRS TO KEEP SEPARATE:
Omitting subjectivity and Plan Continuation (distinct mechanisms: one involves information weighting, the other involves plan revision).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
3

SELECTED OCCUPATION:
Load Controller / Loadmaster (Commercial)

ROLE AND SETTING:
Ramp/operations control; calculates aircraft weight and balance, ULD build-up, load sheet preparation; uses automated load planning software.

REQUESTED BIASES:
Substitution bias, Apophenia or Correlation Bias, Automaticity or Automation Bias

PRIMARY SCENARIO:
Last-minute passenger/baggage change requiring weight and balance recalculation under departure deadline with automated load software.

DECISION EPISODES:
1. Initial load sheet review and software update.
2. Manual verification of weight and balance calculations.
3. ULD reconfiguration decision if needed.
4. Final load sheet approval and transmission to flight crew.

AVAILABLE INFORMATION AND CUES:
Passenger manifest, baggage tags, ULD weights, aircraft weight and balance limits, software output, prior load sheets for similar flights.

COMPETING INTERPRETATIONS:
Software output is accurate vs. manual verification needed; pattern in baggage distribution is meaningful vs. random variation.

CONSTRAINTS AND PRESSURES:
Departure deadline, crew duty time limits, gate constraints, regulatory weight and balance requirements.

CONSEQUENCES:
Aircraft out of balance, performance limitations, regulatory violation, departure delay.

COUNTERFACTUAL CAUSAL VARIABLE:
Software output accuracy (later found to have used outdated aircraft configuration data).

BIAS-SPECIFIC DESIGN NOTES:
Substitution bias should manifest as using a simpler heuristic (e.g., "similar flights had no issues") instead of full calculation. Apophenia should manifest as seeing patterns in baggage/passenger data that aren't meaningful. Automation Bias should manifest as over-relying on software output without manual verification.

BIAS PAIRS TO KEEP SEPARATE:
Apophenia and Automation Bias (distinct mechanisms: one involves pattern detection, the other involves software reliance).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
4

SELECTED OCCUPATION:
Check Airman / Type Rating Instructor (TRI/TRE)

ROLE AND SETTING:
Training organization/simulator center; evaluates trainee pilots during type rating or recurrent training; regulatory authority for pass/fail decisions.

REQUESTED BIASES:
Bias Blind Spot, Normalcy Bias, Experience Bias or Trusting expert intuition, Illusion of validity

PRIMARY SCENARIO:
Trainee performance borderline pass/fail with operational safety implications and regulatory standards.

DECISION EPISODES:
1. Initial performance assessment against regulatory standards.
2. Comparison with prior training records and subjective impression.
3. Consultation with other instructors (if available) or review of objective metrics.
4. Final pass/fail decision and documentation.

AVAILABLE INFORMATION AND CUES:
Simulator performance metrics, regulatory evaluation criteria, prior training records, subjective impression of trainee's airmanship, peer input.

COMPETING INTERPRETATIONS:
Trainee is safe but inconsistent vs. trainee poses operational risk; objective metrics support pass vs. subjective concern about specific maneuvers.

CONSTRAINTS AND PRESSURES:
Regulatory standards, training schedule, trainee career implications, organizational pressure to maintain throughput.

CONSEQUENCES:
Unsafe pilot certified vs. qualified pilot unnecessarily delayed.

COUNTERFACTUAL CAUSAL VARIABLE:
Trainee's actual performance level (later found that simulator had minor calibration issue affecting one maneuver).

BIAS-SPECIFIC DESIGN NOTES:
Bias Blind Spot should manifest as failure to recognize own biases in evaluation (requires meta-cognitive probes). Normalcy Bias should manifest as assuming trainee will perform normally based on prior performance. Experience Bias should manifest as trusting expert intuition over objective metrics. Illusion of validity should manifest as confidence in judgment based on past success.

BIAS PAIRS TO KEEP SEPARATE:
Bias Blind Spot and Illusion of validity (both meta-cognitive but distinct: one involves bias recognition, the other involves confidence calibration).

BIAS MECHANISMS NOT TO FORCE:
Bias Blind Spot and Illusion of validity (require careful meta-cognitive probe design).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
5

SELECTED OCCUPATION:
Director of Maintenance (DOM) – Part 135/121

ROLE AND SETTING:
Senior managerial role within airline/MRO; overall authority for maintenance operations, regulatory compliance, budget, and safety.

REQUESTED BIASES:
Optimism, Authority Bias, Sunk Cost Fallacy, Representativeness, Overconfidence

PRIMARY SCENARIO:
Grounding decision for fleet-wide recurring defect with conflicting engineering assessments, budget pressure, and regulatory exposure.

DECISION EPISODES:
1. Initial defect review and engineering consultation.
2. Risk assessment and regulatory compliance evaluation.
3. Budget and operational impact analysis.
4. Final grounding vs. continued operation decision.

AVAILABLE INFORMATION AND CUES:
Defect reports, engineering assessments, regulatory guidance, maintenance history, budget constraints, operational schedule.

COMPETING INTERPRETATIONS:
Defect is systemic and requires grounding vs. defect is manageable with monitoring; engineering assessment A is correct vs. assessment B.

CONSTRAINTS AND PRESSURES:
Regulatory compliance, budget limitations, operational schedule, customer commitments, safety reputation.

CONSEQUENCES:
Unnecessary grounding cost vs. in-service failure with safety and regulatory implications.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of one engineering assessment (later found that one assessment was based on incomplete data).

BIAS-SPECIFIC DESIGN NOTES:
Optimism should manifest as believing issues will resolve favorably. Authority Bias should manifest as deferring to senior engineer or regulatory interpretation. Sunk Cost should manifest as continuing with maintenance approach due to already-invested resources. Representativeness should manifest as judging current defect based on similarity to past cases. Overconfidence should manifest as confidence in maintenance program's ability to manage risk.

BIAS PAIRS TO KEEP SEPARATE:
Authority Bias and Overconfidence (distinct mechanisms: one involves deference to others, the other involves self-confidence).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
6

SELECTED OCCUPATION:
Flight Dispatcher / Flight Operations Officer

ROLE AND SETTING:
Operations control center; plans and releases flights, monitors en-route conditions, coordinates with flight crews and ATC.

REQUESTED BIASES:
Anchoring Bias, Confirmation Bias, Information bias, Omitting subjectivity, Plan Continuation, Substitution bias

PRIMARY SCENARIO:
Dispatch release with marginal weather at destination, limited alternates, cost pressures, and conflicting information sources.

DECISION EPISODES:
1. Initial flight plan development and weather review.
2. Alternate airport evaluation and fuel calculation.
3. Coordination with flight crew and operations control.
4. Final dispatch release decision.

AVAILABLE INFORMATION AND CUES:
Weather forecasts (multiple sources), NOTAMs, aircraft status, crew duty time, company fuel policy, cost constraints, alternate airport availability.

COMPETING INTERPRETATIONS:
Weather will be at or above minimums vs. weather will deteriorate; initial plan is sound vs. alternative plan needed.

CONSTRAINTS AND PRESSURES:
Regulatory requirements, cost pressures, crew duty time, passenger schedule, aircraft availability.

CONSEQUENCES:
Unnecessary delay/cancellation cost vs. fuel emergency or diversion with safety implications.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of one weather forecast source (later found to be outdated).

BIAS-SPECIFIC DESIGN NOTES:
Anchoring Bias should manifest as reliance on initial flight plan. Confirmation Bias should manifest as seeking data supporting plan. Information bias should manifest as over-reliance on abundant data. Omitting subjectivity should manifest as discounting gut feeling. Plan Continuation should manifest as sticking with plan. Substitution bias should manifest as using heuristic instead of complex analysis.

BIAS PAIRS TO KEEP SEPARATE:
Anchoring and Confirmation (distinct mechanisms: one involves initial information, the other involves selective search); Information and Omitting subjectivity (distinct mechanisms: one involves data volume, the other involves subjective cues).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Aviation

INTERVIEW ID:
7

SELECTED OCCUPATION:
Continuing Airworthiness Manager (CAMO)

ROLE AND SETTING:
Office-based regulatory compliance role; manages airworthiness directives, reliability programs, maintenance program changes, and regulatory submissions.

REQUESTED BIASES:
Apophenia or Correlation Bias, Automaticity or Automation Bias, Bias Blind Spot, Normalcy Bias, Experience Bias or Trusting expert intuition, Illusion of validity, Optimism

PRIMARY SCENARIO:
Airworthiness directive compliance deadline with fleet grounding implications, parts availability, and conflicting reliability data.

DECISION EPISODES:
1. Initial AD review and compliance status assessment.
2. Parts availability and maintenance capacity evaluation.
3. Reliability data analysis and risk assessment.
4. Final compliance decision (full compliance, partial compliance with exemption, or fleet grounding).

AVAILABLE INFORMATION AND CUES:
AD text, compliance records, parts availability, maintenance capacity, reliability trends, regulatory guidance, OEM input.

COMPETING INTERPRETATIONS:
AD requires immediate full compliance vs. partial compliance with exemption is acceptable; reliability data shows significant risk vs. risk is manageable.

CONSTRAINTS AND PRESSURES:
Regulatory deadlines, parts availability, maintenance capacity, operational schedule, safety reputation.

CONSEQUENCES:
Unnecessary grounding cost vs. regulatory violation with safety implications.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of reliability data (later found that one data source had reporting errors).

BIAS-SPECIFIC DESIGN NOTES:
Apophenia should manifest as seeing patterns in reliability data that aren't meaningful. Automation Bias should manifest as relying on compliance software. Bias Blind Spot should manifest as failure to recognize own biases (requires meta-cognitive probes). Normalcy Bias should manifest as assuming normal compliance patterns. Experience Bias should manifest as trusting expert intuition. Illusion of validity should manifest as confidence in judgment based on past success. Optimism should manifest as believing issues will resolve favorably.

BIAS PAIRS TO KEEP SEPARATE:
Bias Blind Spot and Illusion of validity (both meta-cognitive but distinct); Apophenia and Automation Bias (distinct mechanisms: pattern detection vs. software reliance).

BIAS MECHANISMS NOT TO FORCE:
Bias Blind Spot and Illusion of validity (require careful meta-cognitive probe design).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

***

## 8. Machine-readable JSON

Removed to .json file
