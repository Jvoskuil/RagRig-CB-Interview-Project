This confirms strong grounding for production planning and control (PPC) bias research, reliability engineering, and process/manufacturing selection biases directly relevant to this domain. Now building the full allocation.

## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Production Planner / Scheduler | Finalizing a weekly production schedule under multiple competing constraints with limited time to evaluate all options; bounded rationality in settling on a workable rather than optimal schedule | 100% | 3 | High | Adds planning/scheduling, office-floor interface, moderate procedural structure context | APPROVED |
| 2 | 2 | Quality Assurance Analyst (Statistical Process Control) | Interpreting a control chart showing two variables trending together and deciding whether to revise a long-standing process specification; correlation bias in inferring causation from co-occurring trends, conservatism bias in underweighting the new data relative to established specification limits | 100% | 6 | High | Adds data-heavy/quantified analytical work, individual-with-instruments context | APPROVED |
| 3 | 3 | Environmental/Safety Compliance Officer (Manufacturing Plant) | Reviewing a new chemical process's risk profile after a near-miss elsewhere in the industry, deciding how much attention to give an uncomfortable emerging hazard indicator; imaginability bias in scenario generation, ostrich effect in avoiding the uncomfortable data, primacy effect in the first risk report shaping the ongoing assessment | 100% | 9 | High | Adds regulatory/safety, documentation-heavy, individual-with-organizational-stakes context | APPROVED |
| 4 | 4 | Maintenance Reliability Engineer | Investigating repeated equipment failures and deciding whether a maintenance technician's error pattern reflects individual competence or a systemic issue, while estimating the probability the next failure is due; fundamental attribution bias in explaining the technician's errors, gambler's fallacy in failure-timing expectations, illusion of control in the maintenance schedule's predictive power, ambiguity effect in an unclear failure-mode classification | 100% | 12 | High | Adds technical/data-heavy troubleshooting, individual-with-team-interface, root-cause-analysis context | APPROVED |
| 5 | 5 | Plant/Industrial Production Manager | Deciding whether to approve a shift-change proposal championed by two department heads, informed by the most recent quarter's output data; bandwagon effect from department heads' early support, recency effect in weighting the most recent quarter, overconfidence bias in the manager's own production forecasts, availability heuristic from a vivid recent success story, anchoring bias on the initial proposal figures | 100% | 15 | High | Adds senior decision authority, cross-departmental stakeholder, resource allocation context | APPROVED |
| 6 | 6 | Production Planning and Control (PPC) Analyst | Revising the production programme after a supplier delay, drawing on incomplete data and established planning heuristics; confirmation bias in evaluating the revised schedule, bounded rationality in the time-constrained revision, correlation bias in linking the delay to an unrelated metric, conservatism bias in underweighting the delay's severity, imaginability bias in scenario planning, ostrich effect in avoiding a costly full replan | 100% | 18 | High | Adds data-heavy/software-mediated planning, individual analytical work, operational-continuity context | APPROVED |
| 7 | 7 | Process/Manufacturing Engineer (Process Selection) | Selecting a manufacturing process for a new product line after an initial vendor demonstration and a string of recent minor process failures; primacy effect from the first vendor demonstration, fundamental attribution bias in explaining a colleague's process failure, gambler's fallacy in expecting the next trial to succeed, illusion of control in the selected process's predictability, ambiguity effect in avoiding an unfamiliar but potentially superior process, bandwagon effect from peer engineers' process preference, recency effect in weighting the most recent trial run | 86% | 19 | Moderate-High | Adds technical/creative design, cross-functional coordination, resource-allocation context | APPROVED_WITH_CAVEATS (Bandwagon Effect requires an explicit peer-preference cue distinct from Primacy Effect) |

***

## 2. Candidate occupation matrix

### Interview 1 (Bounded Rationality)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Production Planner / Scheduler | 1 (Bounded Rationality) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multi-constraint scheduling phases) | High (change one constraint's actual severity) | High | High (adds planning/scheduling, moderate structure context) | 0.88 |
| PPC Analyst | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.76 |
| Quality Assurance Analyst | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.58 |
| Maintenance Reliability Engineer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 4) | 0.55 |
| Plant Manager | 0 | 0 | 1 | 0 | 25% | Low | High | High | High | Low (overlaps with Interview 5) | 0.42 |

**Selected:** Production Planner / Scheduler (best coverage, distinctness, diversity fit; bounded rationality is the natural core mechanism of production scheduling literature). [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)

***

### Interview 2 (Correlation Bias, Conservatism Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Quality Assurance Analyst (Statistical Process Control) | 2 (Correlation, Conservatism) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (control-chart interpretation, specification-review phases) | High (change the two variables' actual causal relationship) | High | High (adds data-heavy/quantified analytical context) | 0.90 |
| PPC Analyst | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| Maintenance Reliability Engineer | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.65 |
| Production Planner | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.50 |
| Process Engineer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 7) | 0.48 |

**Selected:** Quality Assurance Analyst (Statistical Process Control) (best coverage, distinctness, diversity fit; grounded directly in statistical-process-control interpretation, a well-recognized quality-assurance function). [ucas](https://www.ucas.com/explore/career-path/4.1?assessmentId=false)

***

### Interview 3 (Imaginability Bias, Ostrich Effect, Primacy Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Environmental/Safety Compliance Officer (Manufacturing Plant) | 3 (Imaginability, Ostrich, Primacy) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (risk assessment, ongoing monitoring phases) | High (change hazard indicator's actual severity) | High | High (adds regulatory/safety, documentation-heavy context) | 0.92 |
| Quality Assurance Analyst | 1 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.76 |
| Maintenance Reliability Engineer | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.62 |
| Plant Manager | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.60 |
| Process Engineer | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.58 |

**Selected:** Environmental/Safety Compliance Officer (best coverage, distinctness, diversity fit).

***

### Interview 4 (Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Maintenance Reliability Engineer | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (failure investigation, root-cause phases) | High (change actual failure-mode classification) | High | High (adds technical/data-heavy troubleshooting context) | 0.94 |
| Process Engineer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Quality Assurance Analyst | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 2) | 0.70 |
| Plant Manager | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.65 |
| PPC Analyst | 1 | 2 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.60 |

**Selected:** Maintenance Reliability Engineer (best coverage, distinctness, scenario richness; grounded directly in the domain's root-cause-analysis and failure-mode-classification workflow). [search-careers.gm](https://search-careers.gm.com/en/jobs/jr-202618292/maintenance-reliability-engineer/)

***

### Interview 5 (Bandwagon Effect, Recency Effect, Overconfidence Bias, Availability Heuristic, Anchoring Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Plant/Industrial Production Manager | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (proposal review, cross-departmental phases) | High (change actual output-data validity) | High | High (adds senior decision authority, cross-departmental context) | 0.95 |
| Process Engineer | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| PPC Analyst | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 6) | 0.74 |
| Maintenance Reliability Engineer | 2 | 2 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.66 |
| Production Planner | 2 | 1 | 2 | 0 | 60% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.52 |

**Selected:** Plant/Industrial Production Manager (best coverage, distinctness, scenario richness; grounded directly in the O*NET industrial-production-manager occupation). [onetonline](https://www.onetonline.org/link/summary/11-3051.00)

***

### Interview 6 (Confirmation Bias, Bounded Rationality, Correlation Bias, Conservatism Bias, Imaginability Bias, Ostrich Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Production Planning and Control (PPC) Analyst | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across planning phases) | High (schedule revision, data-review phases) | High (change supplier-delay severity data) | High | High (adds data-heavy/software-mediated planning context) | 0.96 |
| Production Planner | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 1) | 0.82 |
| Quality Assurance Analyst | 3 | 2 | 1 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 2) | 0.72 |
| Environmental/Safety Officer | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.70 |
| Maintenance Reliability Engineer | 2 | 2 | 2 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.60 |

**Selected:** Production Planning and Control (PPC) Analyst (best coverage, distinctness, diversity fit; grounded directly in the PPC bias literature covering exactly this bias cluster across planning phases). [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)

***

### Interview 7 (Primacy Effect, Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect, Bandwagon Effect, Recency Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Process/Manufacturing Engineer (Process Selection) | 5 (Primacy, Fundamental Attribution, Gambler's Fallacy, Illusion of Control, Ambiguity Effect) | 2 (Bandwagon Effect, Recency Effect) | 0 | 0 | 100% | Moderate-High (Bandwagon Effect requires an explicit peer-preference cue distinct from Primacy Effect) | High (process-selection phases, multiple trial runs) | High (change the selected process's actual reliability) | High | High (adds technical/creative design, resource-allocation context) | 0.88 |
| Maintenance Reliability Engineer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.78 |
| Plant Manager | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.76 |
| PPC Analyst | 3 | 2 | 1 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.68 |
| Quality Assurance Analyst | 3 | 2 | 1 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.66 |

**Selected:** Process/Manufacturing Engineer (Process Selection) (best diversity fit, adds technical/creative design context; Bandwagon Effect requires careful separation from Primacy Effect). [fem.put.poznan](https://fem.put.poznan.pl/sites/default/files/inline-files/Obrony_doktoratow/Fredrick_Mumali/doktorat_Fredrick_Mumali.pdf)

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Bounded Rationality
- **Selected occupation:** Production Planner / Scheduler
- **Role and setting:** Manufacturing planning role responsible for developing weekly and daily production schedules; balances machine availability, labor, material supply, and order deadlines, works under time-constrained planning cycles with imperfect information about all constraints. [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)
- **Why this occupation fits the bias list:** Production planners must finalize schedules within limited time and cognitive capacity, unable to fully evaluate every possible sequencing combination against every constraint. Bounded rationality — settling on a workable, "satisfactory" schedule rather than exhaustively searching for the mathematically optimal one — is a well-documented mechanism in production-planning-and-control (PPC) decision-making research. [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)
- **Primary CTA scenario:** Finalizing a weekly production schedule under multiple competing constraints with limited time to evaluate all options; bounded rationality in settling on a workable rather than optimal schedule.
- **Triggering event:** A production planner has two hours before the schedule must be released to finalize next week's sequencing across three production lines, with constraints including a partial material shortage, one machine's planned maintenance window, and two rush orders with tight deadlines.
- **Decision episodes:**
  1. Initial review of the constraints and generation of a first workable schedule sequence.
  2. Quick check of the first sequence against the most obvious conflicts (material shortage, maintenance window).
  3. Consideration of whether to continue searching for a better sequence or finalize the current one given the time remaining.
  4. Final schedule release and communication to production supervisors.
- **Available cues and evidence:** Machine availability calendar, material inventory levels, order deadlines and priorities, the planner's own experience with similar past scheduling conflicts, remaining time before the schedule release deadline.
- **Competing interpretations:** The first workable sequence adequately balances all constraints vs. a more thorough search would reveal a sequence with fewer downstream conflicts; the time pressure justifies settling on the current sequence vs. the stakes warrant extending the search despite the deadline.
- **Plausible actions:** Release the current workable sequence; spend additional time searching for a better sequence, delaying the release; consult a colleague for a quick second opinion before finalizing; use a scheduling tool to generate additional alternative sequences.
- **Constraints and pressures:** The release deadline, the planner's own time and cognitive capacity to evaluate sequencing options, the complexity of interacting constraints, production supervisors' need for advance notice.
- **Consequences of error:** A schedule with an overlooked conflict causing downstream production delays or missed deadlines, or unnecessary time spent searching for marginal improvements when the first workable sequence would have been adequate.
- **Counterfactual causal variable:** Actual severity of the material shortage relative to the planner's initial assessment (later found to be more constraining than accounted for in the released schedule).
- **Expected interview structure:** Opening (planner role context), Episode 1 (initial sequence generation), Episode 2 (conflict check), Episode 3 (continue-searching decision), Closing (reflection on the basis for finalizing the schedule).
- **Natural biases:** Bounded Rationality.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Production Planning and Control (PPC) Analyst (would overlap with Interview 6; bounded rationality is plausible there but reserved for the more complex six-bias planning scenario).
- **Rejected alternative occupation 2:** Plant Manager (overlaps with Interview 5; bounded rationality is less naturally isolated from the five other mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Correlation Bias, Conservatism Bias
- **Selected occupation:** Quality Assurance Analyst (Statistical Process Control)
- **Role and setting:** Quality assurance role responsible for monitoring process control charts and statistical variation data across a manufacturing line; interprets trends to identify when a process requires adjustment, works individually with instrumentation and historical specification data. [ucas](https://www.ucas.com/explore/career-path/4.1?assessmentId=false)
- **Why this occupation fits the bias list:** QA analysts interpret control-chart data where two variables may trend together, making correlation bias (inferring a causal relationship between two co-occurring trending variables without established mechanism) and conservatism bias (underweighting new data relative to established, long-standing specification limits) both natural, distinct mechanisms in this quantified analytical context.
- **Primary CTA scenario:** Interpreting a control chart showing two variables trending together and deciding whether to revise a long-standing process specification; correlation bias in inferring causation from co-occurring trends, conservatism bias in underweighting the new data relative to established specification limits.
- **Triggering event:** A QA analyst notices that a temperature reading and a defect rate metric have been trending upward together over the past several weeks, while the process specification limits (unchanged for several years) suggest the process remains within acceptable bounds.
- **Decision episodes:**
  1. Initial observation of the two co-trending variables on the control chart.
  2. Formation of a working hypothesis about the relationship between temperature and defect rate.
  3. Comparison of the new trend data against the long-standing specification limits.
  4. Final decision on whether to recommend a specification revision or attribute the trend to normal variation.
- **Available cues and evidence:** The control chart data for both variables, the specification limits and their original basis, alternative explanations for the co-trending pattern (a third, unmeasured factor affecting both), historical process performance data.
- **Competing interpretations:** The temperature increase is causing the rising defect rate vs. both are being driven by an unmeasured third factor (e.g., ambient conditions); the long-standing specification limits remain appropriate vs. the new trend data warrants revision despite the limits' established history.
- **Plausible actions:** Recommend a specification revision based on the observed correlation; investigate the possible third factor before concluding causation; retain the current specification limits, attributing the trend to normal variation; commission a controlled test isolating temperature's effect on defect rate.
- **Constraints and pressures:** Reporting deadlines, the specification limits' long-established status and the organizational effort required to revise them, limited time for a controlled investigation, production continuity concerns.
- **Consequences of error:** A specification revision based on a spurious correlation, or a missed genuine process issue due to over-reliance on outdated specification limits.
- **Counterfactual causal variable:** Actual causal relationship between temperature and defect rate (later found, through controlled testing, to be driven by an unmeasured humidity factor rather than a direct temperature effect).
- **Expected interview structure:** Opening (QA analyst role context), Episode 1 (trend observation), Episode 2 (hypothesis formation), Episode 3 (specification comparison), Closing (reflection on the basis for the final decision).
- **Natural biases:** Correlation Bias, Conservatism Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** PPC Analyst (overlaps with Interview 6; both mechanisms already assigned there in a scheduling rather than statistical-quality context).
- **Rejected alternative occupation 2:** Maintenance Reliability Engineer (overlaps with Interview 4; correlation bias is plausible in failure analysis but less naturally tied to a specification-revision decision).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Imaginability Bias, Ostrich Effect, Primacy Effect
- **Selected occupation:** Environmental/Safety Compliance Officer (Manufacturing Plant)
- **Role and setting:** Regulatory compliance and safety role within a manufacturing facility; assesses process safety risks, monitors emerging hazard indicators, prepares risk reports for management, maintains ongoing safety documentation across a facility's operational lifetime.
- **Why this occupation fits the bias list:** Safety compliance officers form early risk assessments that can persist in influencing later judgment (primacy effect — the first risk report shaping the ongoing assessment), generate scenarios for potential hazards partly based on how easily they can imagine them occurring (imaginability bias), and sometimes avoid engaging with uncomfortable, ambiguous hazard information (ostrich effect — deliberately not seeking out or attending to an unsettling emerging indicator). All three are well-documented, distinct mechanisms in safety risk-assessment literature.
- **Primary CTA scenario:** Reviewing a new chemical process's risk profile after a near-miss elsewhere in the industry, deciding how much attention to give an uncomfortable emerging hazard indicator; imaginability bias in scenario generation, ostrich effect in avoiding the uncomfortable data, primacy effect in the first risk report shaping the ongoing assessment.
- **Triggering event:** A safety compliance officer's initial risk report for a new chemical process, filed a year ago, characterized the process as low-risk; an industry near-miss elsewhere raises an uncomfortable question about a specific hazard pathway the officer had not previously imagined, and new monitoring data hints at (but does not confirm) a similar indicator at this facility.
- **Decision episodes:**
  1. Initial recall of the year-old risk report's low-risk characterization as a starting reference point.
  2. Attempt to generate plausible hazard scenarios for the new information, constrained by which scenarios come easily to mind.
  3. Encounter with the uncomfortable, ambiguous new monitoring data and a choice about how thoroughly to investigate it.
  4. Final updated risk assessment and recommendation.
- **Available cues and evidence:** The original risk report and its stated basis, the industry near-miss's specific hazard pathway, the new, ambiguous monitoring data at this facility, the officer's own experience with similar past hazard scenarios, available time and resources for further investigation.
- **Competing interpretations:** The original low-risk characterization remains valid vs. the industry near-miss reveals a hazard pathway that was never adequately considered; the new monitoring data is a genuine early warning vs. an ambiguous signal not worth escalating; the officer's imagined hazard scenarios are comprehensive vs. limited by what comes easily to mind rather than a systematic hazard analysis.
- **Plausible actions:** Update the risk assessment to reflect the new hazard pathway; retain the original low-risk characterization pending further data; commission a systematic hazard analysis rather than relying on imagined scenarios; actively investigate the uncomfortable monitoring data rather than deferring it.
- **Constraints and pressures:** The original report's established status and the officer's professional investment in it, discomfort with the ambiguous new data, limited time and resources for a full re-analysis, management's expectation for a clear, actionable risk characterization.
- **Consequences of error:** A genuine, previously unimagined hazard pathway going unaddressed, or unnecessary alarm and resource diversion based on an ultimately unrelated ambiguous indicator.
- **Counterfactual causal variable:** Actual relevance of the industry near-miss's hazard pathway to this facility's process (later found, through systematic analysis, to be directly applicable rather than a superficially similar but distinct scenario).
- **Expected interview structure:** Opening (compliance officer role context), Episode 1 (recall of original report), Episode 2 (scenario generation), Episode 3 (encounter with uncomfortable data), Closing (reflection on the basis for the updated assessment).
- **Natural biases:** Imaginability Bias, Ostrich Effect, Primacy Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Quality Assurance Analyst (overlaps with Interview 2; primacy effect is plausible there but less naturally isolated from the correlation/conservatism mechanisms already assigned).
- **Rejected alternative occupation 2:** PPC Analyst (overlaps with Interview 6; ostrich effect and imaginability bias already assigned there in a scheduling rather than safety-risk context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect
- **Selected occupation:** Maintenance Reliability Engineer
- **Role and setting:** Technical role responsible for equipment reliability, root-cause failure analysis, and maintenance program design in a manufacturing plant; investigates recurring equipment failures, evaluates maintenance technician performance data, and classifies failure modes to inform preventive maintenance scheduling. [search-careers.gm](https://search-careers.gm.com/en/jobs/jr-202618292/maintenance-reliability-engineer/)
- **Why this occupation fits the bias list:** Reliability engineers investigate repeated equipment failures involving both human performance and technical factors, making fundamental attribution bias (attributing a maintenance technician's errors to individual competence rather than situational or systemic factors), gambler's fallacy (expecting a failure to be "due" based on time elapsed since the last one, independent of the actual failure-rate distribution), illusion of control (overestimating the predictive power of the maintenance schedule over inherently variable equipment behavior), and ambiguity effect (avoiding a clear classification decision for an ambiguous failure mode in favor of a safer default category) all well-documented and distinct mechanisms in reliability-engineering root-cause analysis.
- **Primary CTA scenario:** Investigating repeated equipment failures and deciding whether a maintenance technician's error pattern reflects individual competence or a systemic issue, while estimating the probability the next failure is due; fundamental attribution bias in explaining the technician's errors, gambler's fallacy in failure-timing expectations, illusion of control in the maintenance schedule's predictive power, ambiguity effect in an unclear failure-mode classification.
- **Triggering event:** A reliability engineer investigates a third equipment failure in six months involving the same maintenance technician's inspection route; the failure mode is ambiguous, potentially fitting two different classification categories, and the engineer must also decide how confident to be that the current preventive maintenance schedule will prevent the next failure.
- **Decision episodes:**
  1. Initial review of the technician's inspection records for the failure pattern.
  2. Explanation of the error pattern's likely cause (technician competence vs. systemic factors such as workload or procedure design).
  3. Estimation of the likelihood and timing of the next similar failure, given the time elapsed since the last one.
  4. Failure-mode classification decision and final maintenance-schedule confidence assessment.
- **Available cues and evidence:** The technician's inspection records and workload data, procedure documentation for the inspection route, the failure mode's specific characteristics relative to the two possible classification categories, the maintenance schedule's historical prevention rate, the time elapsed since the last failure.
- **Competing interpretations:** The technician's errors reflect individual competence issues vs. systemic factors like excessive workload or unclear procedures; the next failure is now more or less likely simply because time has elapsed vs. failure timing is independent of elapsed time; the maintenance schedule reliably prevents failures vs. equipment behavior remains inherently variable despite the schedule; the failure mode belongs in one classification category vs. the other, or genuinely straddles both.
- **Plausible actions:** Recommend additional training for the technician; investigate systemic factors (workload, procedure clarity) before attributing cause; adjust the maintenance schedule's timing based on the elapsed-time reasoning; classify the failure mode into a default category without resolving the ambiguity; commission a broader review of the inspection route's design.
- **Constraints and pressures:** Reporting deadlines, the engineer's own confidence in the maintenance program's design, limited time to investigate systemic factors in depth, the ambiguous failure mode's classification requirements for documentation.
- **Consequences of error:** Unwarranted disciplinary action against the technician for a systemic issue, a misclassified failure mode obscuring the true cause, or an overconfident maintenance schedule that fails to prevent a genuinely due failure.
- **Counterfactual causal variable:** Actual cause of the technician's error pattern (later found, through a systemic review, to result from an ambiguous procedure rather than individual competence).
- **Expected interview structure:** Opening (reliability engineer role context), Episode 1 (record review), Episode 2 (error-pattern explanation), Episode 3 (failure-timing estimation), Episode 4 (classification decision), Closing (reflection on the four-mechanism reasoning process).
- **Natural biases:** Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Process Engineer (overlaps with Interview 7; fundamental attribution bias and gambler's fallacy already assigned there in a process-selection rather than failure-investigation context).
- **Rejected alternative occupation 2:** Quality Assurance Analyst (overlaps with Interview 2; ambiguity effect is plausible in specification decisions but less naturally tied to a human-performance attribution context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Bandwagon Effect, Recency Effect, Overconfidence Bias, Availability Heuristic, Anchoring Bias
- **Selected occupation:** Plant/Industrial Production Manager
- **Role and setting:** Senior management role overseeing overall plant operations; approves major operational changes (shift structures, staffing, production targets), coordinates across departments, makes forecasting and resource-allocation decisions informed by production data and departmental input. [onetonline](https://www.onetonline.org/link/summary/11-3051.00)
- **Why this occupation fits the bias list:** Plant managers approve major cross-departmental proposals informed by recent data and departmental advocacy, making bandwagon effect (department heads' early support shaping the manager's own view), recency effect (the most recent quarter's data being weighted more heavily than the fuller historical record), overconfidence bias (in the manager's own production forecasts), availability heuristic (a vivid, memorable recent success story disproportionately shaping judgment), and anchoring bias (the initial proposal figures setting a reference point for evaluation) all well-documented, distinct mechanisms in senior operational decision-making.
- **Primary CTA scenario:** Deciding whether to approve a shift-change proposal championed by two department heads, informed by the most recent quarter's output data; bandwagon effect from department heads' early support, recency effect in weighting the most recent quarter, overconfidence bias in the manager's own production forecasts, availability heuristic from a vivid recent success story, anchoring bias on the initial proposal figures.
- **Triggering event:** Two department heads jointly propose a shift-structure change, presenting figures showing improved output in the most recent quarter and citing a vivid recent success story from a similar change at a sister facility; the manager must decide whether to approve the change plant-wide.
- **Decision episodes:**
  1. Initial review of the proposal's figures, anchored to the department heads' presented numbers.
  2. Consideration of the department heads' early, visible support for the change.
  3. Comparison of the most recent quarter's output data against the fuller historical production record.
  4. Final approval decision, including the manager's own confidence in the resulting production forecast.
- **Available cues and evidence:** The proposal's initial figures, the department heads' stated support and rationale, the most recent quarter's output data, the fuller historical production record across multiple quarters, the vivid sister-facility success story and its actual comparability, the manager's own forecasting track record.
- **Competing interpretations:** The initial proposal figures accurately represent the expected outcome vs. were selectively framed to support the proposal; the department heads' support reflects sound operational judgment vs. shapes the manager's own view independent of the proposal's actual merits; the most recent quarter's improvement is representative vs. reflects a temporary or coincidental factor; the sister-facility success story is a valid comparison vs. differs materially in conditions; the manager's production forecast is well-calibrated vs. overconfident given the limited data basis.
- **Plausible actions:** Approve the shift-change proposal plant-wide; approve a limited pilot before full implementation; request the fuller historical record and an independent comparability assessment of the sister-facility case; decline the proposal pending further data.
- **Constraints and pressures:** Departmental advocacy and relationship dynamics, budget cycle timing for implementation, the manager's own accountability for the production forecast, the vividness of the cited success story.
- **Consequences of error:** A plant-wide change based on an unrepresentative recent quarter and a non-comparable success story, leading to underperformance relative to the overconfident forecast, or an unnecessarily rejected proposal that would have genuinely improved output.
- **Counterfactual causal variable:** Actual comparability of the sister-facility case to this plant's operating conditions (later found to differ in a material respect that undermined the success story's relevance).
- **Expected interview structure:** Opening (production manager role context), Episode 1 (initial figure review and anchor), Episode 2 (department-head support consideration), Episode 3 (recent-vs-historical data comparison), Episode 4 (approval and forecast confidence), Closing (reflection on the five-mechanism decision process).
- **Natural biases:** Bandwagon Effect, Recency Effect, Overconfidence Bias, Availability Heuristic, Anchoring Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Process Engineer (overlaps with Interview 7; bandwagon effect and recency effect already assigned there in a process-selection rather than management-approval context).
- **Rejected alternative occupation 2:** PPC Analyst (overlaps with Interview 6; anchoring bias is plausible in planning revision but less naturally tied to a senior-approval decision structure).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Confirmation Bias, Bounded Rationality, Correlation Bias, Conservatism Bias, Imaginability Bias, Ostrich Effect
- **Selected occupation:** Production Planning and Control (PPC) Analyst
- **Role and setting:** Specialized planning role responsible for production programme planning, production data management, and performance measurement across the full PPC workflow; revises schedules in response to supply-chain disruptions, works with planning software and incomplete real-time data. [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)
- **Why this occupation fits the bias list:** PPC analysts revise production programmes under time and information constraints, a context extensively documented in PPC-specific cognitive-bias research for confirmation bias (evaluating the revised schedule by seeking evidence it will work rather than actively testing it), bounded rationality (settling on a workable revision under time constraints), correlation bias (linking the delay to an unrelated metric based on coincidental co-occurrence), conservatism bias (underweighting the delay's actual severity relative to established planning assumptions), imaginability bias (scenario planning constrained by easily imagined disruption types), and ostrich effect (avoiding a costly, disruptive full replan by not fully engaging with the delay's implications). All six mechanisms map cleanly onto distinct stages of the PPC revision workflow. [publica.fraunhofer](https://publica.fraunhofer.de/entities/publication/401d3758-03ca-42a7-aac8-51811bb9c028)
- **Primary CTA scenario:** Revising the production programme after a supplier delay, drawing on incomplete data and established planning heuristics; confirmation bias in evaluating the revised schedule, bounded rationality in the time-constrained revision, correlation bias in linking the delay to an unrelated metric, conservatism bias in underweighting the delay's severity, imaginability bias in scenario planning, ostrich effect in avoiding a costly full replan.
- **Triggering event:** A PPC analyst learns of a supplier delay affecting a key raw material with only partial information about its duration and severity; a full replan would be costly and disruptive, and the analyst must revise the production programme within a tight timeframe.
- **Decision episodes:**
  1. Initial assessment of the supplier delay's likely severity, informed by an observed but possibly coincidental correlation with an unrelated recent metric.
  2. Generation of a revised schedule based on easily imagined disruption scenarios, given limited time to consider the full range of possibilities.
  3. Evaluation of the revised schedule, seeking confirming evidence that it will adequately address the delay rather than actively stress-testing it.
  4. Final decision on whether the partial revision is sufficient or whether a full, more disruptive replan is genuinely warranted.
- **Available cues and evidence:** The supplier's delay notification and its stated (uncertain) duration, the unrelated metric's coincidental timing, established planning assumptions about typical delay severity, the revised schedule's projected performance, the cost and disruption of a full replan.
- **Competing interpretations:** The unrelated metric's coincidental timing indicates a genuine connection to the delay vs. is unrelated coincidence; established planning assumptions adequately capture this delay's severity vs. underweight the delay relative to its actual, more severe impact; the partial revision adequately addresses the disruption vs. a full replan is genuinely warranted despite its cost.
- **Plausible actions:** Implement the partial revision as the final schedule; commission a full replan despite the cost and disruption; seek additional supplier information to resolve the delay's actual severity before finalizing; actively stress-test the revised schedule against a wider range of disruption scenarios.
- **Constraints and pressures:** The revision deadline, the cost and disruption of a full replan, limited real-time information about the supplier delay's actual severity, established planning heuristics from past similar disruptions.
- **Consequences of error:** An inadequate partial revision that fails to prevent downstream production shortfalls, or an unnecessarily costly full replan triggered by an overestimated delay severity.
- **Counterfactual causal variable:** Actual severity and duration of the supplier delay (later found to be substantially more severe than the partial revision accounted for).
- **Expected interview structure:** Opening (PPC analyst role context), Episode 1 (severity assessment), Episode 2 (scenario generation), Episode 3 (revised-schedule evaluation), Episode 4 (final revision-vs-replan decision), Closing (reflection on the six-mechanism reasoning process).
- **Natural biases:** Confirmation Bias, Bounded Rationality, Correlation Bias, Conservatism Bias, Imaginability Bias, Ostrich Effect.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four distinct episodes to avoid compression into a single decision point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Production Planner (overlaps with Interview 1; bounded rationality already assigned there in a routine-scheduling rather than disruption-response context).
- **Rejected alternative occupation 2:** Quality Assurance Analyst (overlaps with Interview 2; correlation bias and conservatism bias already assigned there in a statistical-process rather than supply-chain-planning context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Primacy Effect, Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect, Bandwagon Effect, Recency Effect
- **Selected occupation:** Process/Manufacturing Engineer (Process Selection)
- **Role and setting:** Technical engineering role responsible for selecting and validating manufacturing processes for new product lines; evaluates vendor demonstrations, conducts trial runs, and coordinates with peer engineers and production teams to finalize a process selection. [fem.put.poznan](https://fem.put.poznan.pl/sites/default/files/inline-files/Obrony_doktoratow/Fredrick_Mumali/doktorat_Fredrick_Mumali.pdf)
- **Why this occupation fits the bias list:** Process engineers select manufacturing processes through a sequence of vendor demonstrations, trial runs, and peer consultation, a context well-documented in manufacturing-process-selection literature for primacy effect (the first vendor demonstration disproportionately shaping the engineer's overall impression), fundamental attribution bias (explaining a colleague's process failure as a competence issue rather than a process-design flaw), gambler's fallacy (expecting the next trial run to succeed because recent trials have failed, independent of the underlying failure-rate distribution), illusion of control (overestimating the selected process's predictability), ambiguity effect (avoiding an unfamiliar process option despite potentially superior performance, in favor of a better-understood but inferior option), bandwagon effect (peer engineers' process preference influencing the engineer's own choice), and recency effect (the most recent trial run being weighted more heavily than the fuller trial history). Bandwagon effect requires an explicit peer-preference cue kept distinct from the primacy-effect mechanism (the vendor demonstration) to remain separable. [fem.put.poznan](https://fem.put.poznan.pl/sites/default/files/inline-files/Obrony_doktoratow/Fredrick_Mumali/doktorat_Fredrick_Mumali.pdf)
- **Primary CTA scenario:** Selecting a manufacturing process for a new product line after an initial vendor demonstration and a string of recent minor process failures; primacy effect from the first vendor demonstration, fundamental attribution bias in explaining a colleague's process failure, gambler's fallacy in expecting the next trial to succeed, illusion of control in the selected process's predictability, ambiguity effect in avoiding an unfamiliar but potentially superior process, bandwagon effect from peer engineers' process preference, recency effect in weighting the most recent trial run.
- **Triggering event:** A process engineer is selecting between two candidate manufacturing processes for a new product line; the first vendor's demonstration was impressive and shapes the engineer's ongoing preference, several peer engineers have independently expressed a preference for the same familiar process type, a colleague's recent trial run with the unfamiliar alternative process failed (attributed by the team to the colleague's setup rather than the process itself), and the most recent trial run with the preferred process succeeded after two earlier failures.
- **Decision episodes:**
  1. Initial vendor demonstration and formation of a lasting impression of the preferred process.
  2. Observation of the colleague's failed trial with the unfamiliar alternative and explanation of its cause.
  3. Sequence of trial runs with the preferred process, including two failures followed by a recent success, and expectation-setting about the next trial.
  4. Final process-selection decision, informed by peer engineers' expressed preference and the process's perceived predictability.
- **Available cues and evidence:** The first vendor demonstration's specific claims and conditions, the colleague's failed trial and its actual cause (setup error vs. process limitation), the full trial-run history for the preferred process (including the two earlier failures), peer engineers' stated preferences and their basis, the unfamiliar alternative process's actual performance data where available.
- **Competing interpretations:** The first vendor demonstration accurately represents the process's typical performance vs. was an especially favorable, non-representative showing; the colleague's failure reflects a setup error vs. a genuine limitation of the unfamiliar process; the most recent successful trial indicates the preferred process is now reliable vs. the two earlier failures are equally informative about its true failure rate; peer engineers' preference reflects sound independent judgment vs. shared, unexamined bias toward the familiar process; the unfamiliar process's greater uncertainty makes it a real risk vs. its actual performance data may be comparable or superior once properly evaluated.
- **Plausible actions:** Select the preferred, familiar process based on the vendor demonstration and recent trial success; select the unfamiliar alternative after re-examining the colleague's trial failure's actual cause; commission additional trials for both processes before deciding; explicitly solicit an independent, first-time evaluation of the unfamiliar process's actual performance data.
- **Constraints and pressures:** Project timeline for process selection, peer engineers' visible preference and its social influence, the vendor demonstration's lasting impression, limited trial runs for the unfamiliar alternative.
- **Consequences of error:** Selection of a familiar but ultimately less suitable process due to primacy, bandwagon, and gambler's-fallacy-driven overconfidence in its recent success, or rejection of a genuinely superior unfamiliar process due to ambiguity aversion and a misattributed trial failure.
- **Counterfactual causal variable:** Actual cause of the colleague's failed trial with the unfamiliar process (later found to be a genuine process limitation rather than a setup error, contrary to the team's attribution).
- **Expected interview structure:** Opening (process engineer role context), Episode 1 (vendor demonstration and impression), Episode 2 (colleague's trial and attribution), Episode 3 (trial-run sequence and expectation), Episode 4 (final selection with peer input), Closing (reflection on the seven-mechanism reasoning process).
- **Natural biases:** Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect, Recency Effect.
- **Plausible but difficult biases:** Primacy Effect (requires the first vendor demonstration's lasting influence to be explicit and distinguishable from ongoing, cumulative evidence), Bandwagon Effect (requires an explicit peer-preference cue — the engineer's own choice shifting toward the peer consensus — distinct from the primacy-effect mechanism).
- **Biases that should not be forced:** None outright, but Bandwagon Effect must be grounded in an explicit peer-influence moment separate from the vendor-demonstration-driven primacy effect.
- **Rejected alternative occupation 1:** Maintenance Reliability Engineer (overlaps with Interview 4; fundamental attribution bias and gambler's fallacy already assigned there in a failure-investigation rather than process-selection context).
- **Rejected alternative occupation 2:** Plant Manager (overlaps with Interview 5; bandwagon effect and recency effect already assigned there in a senior-approval rather than technical-selection context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Bandwagon Effect requires an explicit peer-preference cue distinct from the vendor-demonstration-driven Primacy Effect)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (production planner, QA analyst, safety compliance officer, reliability engineer, plant manager, PPC analyst, process engineer) | None | None | None | None needed |
| Work setting | Planning/office-floor interface (1, 6), Data-heavy analytical (2), Regulatory/documentation-heavy (3), Technical/troubleshooting (4), Senior management (5), Technical/creative design (7) | Planning (2/7: 1, 6) | Planning | Field/outdoor, public-facing | None critical; Interviews 1 and 6 differ materially in scope (routine weekly schedule vs. six-bias disruption-response revision) and reflect the domain's genuine planning-intensive character |
| Decision type | Resource allocation/scheduling (1), Diagnosis/interpretation (2), Risk assessment (3), Diagnosis/attribution (4), Resource allocation/approval (5), Planning/troubleshooting (6), Design/creative judgment (7) | None significant | None | Negotiation, Personnel management | None critical; strong spread across scheduling, diagnosis, risk assessment, approval, and design |
| Information environment | Time-constrained/multi-constraint (1), Data-heavy/quantified (2), Documentation-heavy/ambiguous (3), Data-heavy/technical (4), Cross-departmental/socially-mediated (5), Data-heavy/software-mediated (6), Technical/socially-mediated (7) | Data-heavy (4/7: 2, 4, 6, 7) | Data-heavy | Rich/structured as sole driver | None critical; reflects the domain's genuinely data-intensive character across quality, maintenance, planning, and process-engineering functions |
| Time pressure | High (1), Moderate (2, 3), Moderate-high (4), Moderate (5), High (6), Moderate-high (7) | Moderate (2/7) | Balanced | Very low | None critical |
| Consequence of error | Operational/schedule (1), Quality/financial (2), Safety/regulatory (3), Safety/operational (4), Financial/operational (5), Operational continuity (6), Financial/quality (7) | None significant | None | Environmental, educational | None critical; reflects the domain's genuine mix of quality, safety, and operational-continuity consequence profiles |
| Expertise level | Independent professional (1, 2), Specialist (3, 4), Decision authority (5), Specialist/independent (6, 7) | Specialist (4/7: 3, 4, 6, 7) | Specialist | Developing practitioner | None critical; reflects that consequential bias-rich decisions in this domain often sit with technically specialized roles, with Interview 5 providing senior-authority contrast |
| Stakeholder pattern | Individual with tools (1, 2, 6), Individual with organizational stakes (3), Individual with team interface (4), Cross-departmental (5), Individual with peer influence (7) | Individual with tools (3/7: 1, 2, 6) | Individual with tools | Multi-party negotiation, public-facing | None critical; Interviews 5 and 7 provide the needed team/peer-influence contrast |
| Scenario archetype | Schedule finalization (1), Control-chart interpretation (2), Risk-report review (3), Failure investigation (4), Proposal approval (5), Schedule revision (6), Process selection (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Material-shortage severity (1), Temperature-defect causal link (2), Hazard-pathway relevance (3), Technician-error cause (4), Sister-facility comparability (5), Supplier-delay severity (6), Trial-failure cause (7) | None significant | None | Equipment/technical hardware failure as primary variable (present but secondary) | None critical; all seven turn on a distinct, plausible causal fact appropriate to the domain |

**Overall assessment:** Strong diversity across occupations, settings, and decision types, spanning production scheduling, statistical quality analysis, safety compliance, reliability engineering, senior plant management, production planning and control, and process engineering. Data-heavy information environments and specialist expertise levels recur across several interviews, which is expected given the domain's genuinely technical and data-driven industrial character, but each instance differs materially in function, hazard type, and causal structure. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Bounded Rationality (clear mechanism: satisficing under time/cognitive constraints) | None | None | None | None | None | Show the planner explicitly weighing whether to continue searching versus finalize; probe the time/cognitive constraint explicitly, not just that the schedule later had a conflict |
| 2 | Correlation Bias (causal inference from co-trending variables), Conservatism Bias (underweighting new data vs. established limits) | Correlation Bias and Confirmation Bias (both involve favoring a particular interpretation, though correlation bias specifically concerns inferring causation from co-occurrence) | None | None | None | None | Show the two variables' co-trending pattern explicitly and the analyst's causal inference from it; separate the specification-limit reliance (conservatism) from the correlation-based hypothesis as distinct reasoning steps |
| 3 | Imaginability Bias (scenario generation limited by ease of imagining), Ostrich Effect (avoidance of uncomfortable data), Primacy Effect (first-report anchoring) | Ostrich Effect and Ambiguity Effect (both can involve avoiding engagement with unclear information, though ostrich effect specifically concerns avoiding known, uncomfortable information) | None | None | Ostrich Effect (must show active avoidance, not merely a reasonable prioritization decision) | Ostrich Effect | Show the officer explicitly choosing not to investigate the uncomfortable data despite its availability, distinct from a reasoned resource-prioritization decision; separate the original report's lasting influence (primacy) from the scenario-generation limitation (imaginability) |
| 4 | Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect (four distinct) | Fundamental Attribution Bias and ordinary performance evaluation (must show a specific situational factor being overlooked, not merely an accurate competence assessment) | None | None | None | None | Show the systemic factor (workload, procedure clarity) explicitly as an unexplored alternative to the competence attribution; separate the elapsed-time reasoning (gambler's fallacy) from the maintenance-schedule confidence (illusion of control) as distinct episodes |
| 5 | Bandwagon Effect, Recency Effect, Overconfidence Bias, Availability Heuristic, Anchoring Bias (five distinct) | Availability Heuristic and Anchoring Bias (both involve a specific salient reference point, though availability concerns ease of recall of a vivid example, anchoring concerns the first numerical figure received), Bandwagon Effect and Availability Heuristic (both involve social/vivid influence) | None | None | None | None | Show the department heads' early support explicitly as distinct from the proposal's initial figures (anchoring); separate the vivid sister-facility story's influence (availability) from the department heads' social endorsement (bandwagon) as distinct cues |
| 6 | Confirmation Bias, Bounded Rationality, Correlation Bias, Conservatism Bias, Imaginability Bias, Ostrich Effect (six distinct mechanisms across planning phases) | Bounded Rationality and Satisficing-adjacent Confirmation Bias (both involve stopping short of full evaluation, though confirmation bias specifically concerns selective evidence-seeking for the chosen option), Conservatism Bias and Ostrich Effect (both involve underweighting/avoiding new information) | None | None | Ostrich Effect (must show active avoidance of the full replan's implications, not merely a reasonable cost-benefit decision) | Ostrich Effect | Distribute the six biases across the four distinct episodes; separate the delay-severity correlation reasoning from the confirmation-biased schedule evaluation as distinct steps; show explicit avoidance behavior for Ostrich Effect distinct from a reasoned cost-based decision against a full replan |
| 7 | Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, Ambiguity Effect, Recency Effect (five cleanly distinguishable); Primacy Effect, Bandwagon Effect (require explicit distinct cues) | Primacy Effect and Bandwagon Effect (both involve an external influence shaping the engineer's preference, though primacy concerns the first vendor demonstration's lasting impression, bandwagon concerns peer engineers' concurrent preference), Gambler's Fallacy and Recency Effect (both involve overweighting recent trial outcomes, though for different underlying reasoning errors) | None | None | Primacy Effect (must show the first demonstration's lasting influence explicitly, distinct from cumulative trial evidence), Bandwagon Effect (must show an explicit peer-preference-driven shift) | Primacy Effect, Bandwagon Effect | Show the first vendor demonstration's specific, lasting impression explicitly, separate from the later trial-run evidence; show the peer engineers' preference as an explicit, distinct social-influence moment rather than conflating it with the vendor-demonstration-driven primacy effect |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 7, generate Primacy Effect and Bandwagon Effect as two explicit, temporally distinct influence events (the initial vendor demonstration versus the later peer-preference discussion) rather than blending them into a single "the engineer liked the familiar option" narrative. For Interviews 3 and 6, ground Ostrich Effect in explicit, described avoidance behavior rather than a reasonable resource-prioritization decision. For Interview 6, distribute all six biases across the four distinct planning episodes rather than compressing them into a single revision moment.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Availability Heuristic/Anchoring Bias and Bandwagon Effect/Availability Heuristic in Interview 5; Primacy Effect/Bandwagon Effect and Gambler's Fallacy/Recency Effect in Interview 7; Conservatism Bias/Ostrich Effect in Interview 6). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
