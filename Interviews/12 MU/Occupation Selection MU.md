## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Underground Shift Supervisor / Mine Captain | Explaining a sudden equipment failure to management by constructing a plausible causal story that ties together unrelated recent events; narrative fallacy in the after-incident account | 100% | 3 | High | Adds field supervisory, team leadership, retrospective-narrative context | APPROVED |
| 2 | 2 | Geotechnical Engineer / Ground Control Specialist | Interpreting a rock-mass monitoring anomaly and attributing its cause after a minor fall-of-ground incident; attribution bias in explaining the incident's cause, illusion of validity in trusting a coherent-looking geotechnical model | 100% | 6 | High | Adds technical/data-heavy analysis, individual-with-instruments context | APPROVED |
| 3 | 3 | Drill and Blast Engineer | Designing a blast pattern for a new rock type using a long-used design template; experience bias in relying on past blast patterns, status quo bias in resisting design changes, overconfidence bias in predicted fragmentation outcome | 100% | 9 | High | Adds technical/creative design, individual-with-tools, moderate procedural structure context | APPROVED |
| 4 | 4 | Mine Ventilation Engineer | Assessing whether a gas-monitoring alarm pattern indicates a genuine ventilation deficiency or a sensor artifact after a memorable prior incident; availability bias from the memorable past incident, anchoring bias on the initial alarm reading, confirmation bias in interpreting subsequent readings, narrative fallacy in constructing an explanatory account | 100% | 12 | High | Adds technical/safety-critical, data-heavy monitoring, individual-with-instruments context | APPROVED |
| 5 | 5 | Mine Planning Engineer | Revising the short-term mine plan after a grade-control geologist's data conflicts with the engineer's established sequencing approach; attribution bias in explaining the data discrepancy, illusion of validity in the plan's internal coherence, experience bias in relying on past sequencing decisions, status quo bias in resisting plan revision, overconfidence bias in production forecasts | 100% | 15 | High | Adds planning/scheduling, cross-disciplinary coordination, resource allocation context | APPROVED |
| 6 | 6 | Mine Safety/Health & Safety Officer | Investigating a near-miss incident and compiling the official incident report after forming an early causal theory; availability bias from a recent similar incident, experience bias in pattern-matching to past investigations, confirmation bias in evidence selection, narrative fallacy in report construction, attribution bias in assigning cause, illusion of validity in the completed investigation | 100% | 18 | High | Adds investigative, documentation-heavy, individual-with-organizational-stakes context | APPROVED |
| 7 | 7 | Underground Mine Manager / Assistant Mine Manager | Deciding whether to halt production in a section after conflicting reports on ground conditions, weighing an initial inspection report against subsequent crew feedback; anchoring bias on the initial inspection report, status quo bias in continuing production, overconfidence bias in the section's safety margin, availability bias from a recent unrelated incident, confirmation bias in evaluating crew feedback | 86% | 19 | Moderate-High | Adds senior decision authority, high-consequence, multi-source information environment | APPROVED_WITH_CAVEATS (duplicate Anchoring Bias and duplicate Confirmation Bias require single-instance handling) |

***

## 2. Candidate occupation matrix

### Interview 1 (Narrative Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Underground Shift Supervisor / Mine Captain | 1 (Narrative Fallacy) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multi-phase incident account construction) | High (change actual root cause of the failure) | High | High (adds field supervisory, retrospective-narrative context) | 0.88 |
| Mine Safety Officer | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.76 |
| Ventilation Engineer | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.58 |
| Geotechnical Engineer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.55 |
| Mine Planning Engineer | 0 | 0 | 1 | 0 | 25% | Low | High | High | High | Low (overlaps with Interview 5) | 0.42 |

**Selected:** Underground Shift Supervisor / Mine Captain (best coverage, distinctness, diversity fit; narrative fallacy is the natural core mechanism of retrospective incident storytelling).

***

### Interview 2 (Attribution Bias, Illusion of Validity)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Geotechnical Engineer / Ground Control Specialist | 2 (Attribution, Illusion of Validity) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (monitoring interpretation, model-building phases) | High (change monitoring data reliability) | High | High (adds technical/data-heavy analysis context) | 0.90 |
| Mine Planning Engineer | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 5) | 0.70 |
| Mine Safety Officer | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.65 |
| Ventilation Engineer | 1 | 0 | 1 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.55 |
| Drill and Blast Engineer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 3) | 0.50 |

**Selected:** Geotechnical Engineer / Ground Control Specialist (best coverage, distinctness, diversity fit).

***

### Interview 3 (Experience Bias, Status Quo Bias, Overconfidence Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Drill and Blast Engineer | 3 (Experience, Status Quo, Overconfidence) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (blast design, pattern selection, outcome prediction phases) | High (change actual rock-type fragmentation behavior) | High | High (adds technical/creative design, individual-with-tools context) | 0.92 |
| Mine Planning Engineer | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 5) | 0.76 |
| Underground Mine Manager | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 7) | 0.70 |
| Shift Supervisor | 1 | 2 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.65 |
| Geotechnical Engineer | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.58 |

**Selected:** Drill and Blast Engineer (best coverage, distinctness, diversity fit; grounded directly in blast-design workflow well-documented in mining occupation literature). [thiess](https://thiess.com/uploads/Thiess-AZ-of-mining-jobs.pdf)

***

### Interview 4 (Availability Bias, Anchoring Bias, Confirmation Bias, Narrative Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Mine Ventilation Engineer | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (alarm interpretation, monitoring phases) | High (change alarm cause accuracy) | High | High (adds technical/safety-critical, data-heavy monitoring context) | 0.94 |
| Mine Safety Officer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 6) | 0.80 |
| Underground Mine Manager | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 7) | 0.72 |
| Geotechnical Engineer | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.65 |
| Shift Supervisor | 1 | 2 | 1 | 0 | 75% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.58 |

**Selected:** Mine Ventilation Engineer (best coverage, distinctness, diversity fit; well-grounded in the domain's designated ventilation-specialist role). [msha](https://www.msha.gov/sites/default/files/events/Mining-Occupations-and-Methods-vertical.pdf)

***

### Interview 5 (Attribution Bias, Illusion of Validity, Experience Bias, Status Quo Bias, Overconfidence Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Mine Planning Engineer | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (sequencing, forecasting, cross-disciplinary phases) | High (change grade-control data accuracy) | High | High (adds planning/scheduling, cross-disciplinary coordination context) | 0.95 |
| Drill and Blast Engineer | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 3) | 0.80 |
| Underground Mine Manager | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 7) | 0.74 |
| Geotechnical Engineer | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.68 |
| Shift Supervisor | 2 | 2 | 1 | 0 | 80% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.62 |

**Selected:** Mine Planning Engineer (best coverage, distinctness, scenario richness; grounded directly in mine-planning-engineer role description involving sequencing, blending, and reconciliation). [realzambiajobs](https://www.realzambiajobs.com/detail/1530)

***

### Interview 6 (Availability Bias, Experience Bias, Confirmation Bias, Narrative Fallacy, Attribution Bias, Illusion of Validity)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Mine Safety/Health & Safety Officer | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across investigation phases) | High (incident investigation, evidence review, report phases) | High (change actual root cause of the near-miss) | High | High (adds investigative, documentation-heavy context) | 0.96 |
| Underground Mine Manager | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 7) | 0.82 |
| Geotechnical Engineer | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 2) | 0.74 |
| Ventilation Engineer | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.70 |
| Shift Supervisor | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.66 |

**Selected:** Mine Safety/Health & Safety Officer (best coverage, distinctness, diversity fit; grounded directly in the mine safety-officer role's investigative function). [procrestafrica](https://procrestafrica.com/open-positions/)

***

### Interview 7 (Anchoring Bias x2, Status Quo Bias, Overconfidence Bias, Availability Bias, Confirmation Bias x2)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Underground Mine Manager / Assistant Mine Manager | 5 (Status Quo, Overconfidence, Availability, Anchoring, Confirmation) | 2 (duplicate Anchoring and Confirmation entries) | 0 | 0 | 100% | Moderate-High (duplicate Anchoring and Confirmation Bias entries treated as single mechanisms each) | High (production-halt decision phases, multi-source information) | High (change actual ground-condition severity) | High | High (adds senior decision authority, high-consequence context) | 0.88 |
| Mine Planning Engineer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| Mine Safety Officer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.76 |
| Geotechnical Engineer | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.72 |
| Drill and Blast Engineer | 3 | 2 | 2 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.65 |

**Selected:** Underground Mine Manager / Assistant Mine Manager (best diversity fit, adds senior decision-authority context; duplicate Anchoring Bias and duplicate Confirmation Bias require single-instance handling).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Narrative Fallacy
- **Selected occupation:** Underground Shift Supervisor / Mine Captain
- **Role and setting:** Field supervisory role in an underground mine; leads shift crews, oversees daily production and safety compliance, reports incidents and equipment issues to mine management, coordinates between crew, maintenance, and engineering.
- **Why this occupation fits the bias list:** Shift supervisors are routinely required to explain equipment failures or operational disruptions to management, often shortly after the event and with incomplete information. Narrative fallacy — constructing a coherent, plausible-sounding causal story that connects a sequence of events more tightly than the evidence actually warrants — is a natural and distinct mechanism in this retrospective, explanation-under-pressure context.
- **Primary CTA scenario:** Explaining a sudden equipment failure to management by constructing a plausible causal story that ties together unrelated recent events; narrative fallacy in the after-incident account.
- **Triggering event:** A critical piece of loading equipment fails unexpectedly mid-shift, and the shift supervisor is asked by management, within hours, to explain what happened; the supervisor recalls a maintenance delay from the previous week and a minor operator complaint from two days earlier, weaving them into a single explanatory narrative.
- **Decision episodes:**
  1. Initial gathering of available facts immediately after the failure.
  2. Recall of recent, loosely related prior events (the maintenance delay, the operator complaint).
  3. Construction of a single coherent narrative linking these events to the failure for the management report.
  4. Final report delivery and decision on what corrective actions to recommend based on that narrative.
- **Available cues and evidence:** Equipment failure log and technical readouts, maintenance records from the prior week, the operator's earlier complaint, crew statements from the shift, absence of a definitive root-cause test at the time of reporting.
- **Competing interpretations:** The prior maintenance delay and operator complaint are genuinely causally linked to the failure vs. are coincidental, unrelated events that happen to precede it; the constructed narrative reflects the actual causal chain vs. a plausible-sounding story built from convenient, available facts.
- **Plausible actions:** Report the narrative as the likely cause and recommend corrective action based on it; report the failure as currently unexplained pending formal root-cause analysis; recommend an independent technical investigation before attributing cause; flag the maintenance delay and complaint as separate, unconfirmed factors rather than a unified story.
- **Constraints and pressures:** Management's expectation for a prompt explanation, incomplete technical diagnostic time before the report is due, the supervisor's own desire to appear in command of the situation, production pressure to resume operations quickly.
- **Consequences of error:** A misattributed cause leading to ineffective corrective action while the actual fault recurs, or unwarranted blame placed on maintenance or an operator based on a coincidental sequence.
- **Counterfactual causal variable:** Actual root cause of the equipment failure (later found, through formal investigation, to be an unrelated manufacturing defect with no connection to the maintenance delay or complaint).
- **Expected interview structure:** Opening (supervisor role context), Episode 1 (fact-gathering), Episode 2 (recall of prior events), Episode 3 (narrative construction), Closing (reflection on how the story was assembled under time pressure).
- **Natural biases:** Narrative Fallacy.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Mine Safety Officer (would overlap with Interview 6; narrative fallacy is plausible there but reserved for the more complex six-bias investigation scenario).
- **Rejected alternative occupation 2:** Mine Ventilation Engineer (overlaps with Interview 4; narrative fallacy is less naturally isolated from the three other mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Attribution Bias, Illusion of Validity
- **Selected occupation:** Geotechnical Engineer / Ground Control Specialist
- **Role and setting:** Technical specialist role responsible for rock-mass monitoring, geotechnical modeling, and ground support design in underground operations; interprets instrumentation data (extensometers, seismic monitoring) to assess stability risk, works individually with technical models before reporting to mine management.
- **Why this occupation fits the bias list:** Geotechnical engineers interpret complex monitoring data to explain ground behavior and predict stability. Attribution bias (attributing the cause of a minor fall-of-ground incident to a specific factor, such as blasting vibration, rather than a more complex or unclear multi-factor cause) and illusion of validity (a coherent-looking geotechnical model producing a false sense of confidence in its predictive reliability) are both natural, distinct mechanisms in this technical-interpretation context. [goldindustrygroup.com](https://www.goldindustrygroup.com.au/news/2023/9/7/10-types-of-engineers-youll-find-on-a-mine-site)
- **Primary CTA scenario:** Interpreting a rock-mass monitoring anomaly and attributing its cause after a minor fall-of-ground incident; attribution bias in explaining the incident's cause, illusion of validity in trusting a coherent-looking geotechnical model.
- **Triggering event:** A minor fall-of-ground incident occurs in a development heading shortly after a nearby blast; the geotechnical engineer's monitoring model, which has consistently produced coherent-looking stability predictions over recent months, is used to attribute the incident's likely cause.
- **Decision episodes:**
  1. Initial review of monitoring data and the model's pre-incident predictions.
  2. Attribution of the incident's cause to the most salient recent factor (the nearby blast).
  3. Assessment of the model's overall reliability based on its historical coherence.
  4. Final technical report and recommendation on ground support adjustments.
- **Available cues and evidence:** Extensometer and seismic monitoring data, the model's recent prediction history, the blast timing and proximity, alternative contributing factors (rock mass weathering, undetected structural discontinuities), historical incident data for similar headings.
- **Competing interpretations:** The blast is the primary cause of the incident vs. one of several contributing factors, including undetected geological structure; the model's consistent coherence over recent months indicates genuine predictive validity vs. reflects a stable period that does not test the model's limits.
- **Plausible actions:** Attribute the incident primarily to blast vibration and adjust blast parameters; commission additional geological mapping to identify undetected structural factors; recommend enhanced ground support without a definitive single-cause attribution; independently validate the model against an expanded dataset.
- **Constraints and pressures:** Reporting deadline following the incident, production pressure to resume the heading, the engineer's professional investment in the monitoring model's track record, limited time for additional geological investigation.
- **Consequences of error:** Inadequate corrective action if the true cause (e.g., an undetected structural discontinuity) is misattributed to the blast, or unwarranted operational restrictions if the blast is wrongly implicated.
- **Counterfactual causal variable:** Actual cause of the fall-of-ground incident (later found, through detailed geological mapping, to be an undetected fault plane unrelated to the blast timing).
- **Expected interview structure:** Opening (geotechnical engineer role context), Episode 1 (monitoring data review), Episode 2 (cause attribution), Episode 3 (model reliability assessment), Closing (reflection on the basis for the final report).
- **Natural biases:** Attribution Bias, Illusion of Validity.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Mine Planning Engineer (overlaps with Interview 5; both mechanisms are plausible there but reserved for the more complex five-bias planning scenario).
- **Rejected alternative occupation 2:** Mine Safety Officer (overlaps with Interview 6; attribution bias and illusion of validity already assigned there in an investigative rather than technical-modeling context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Experience Bias, Status Quo Bias, Overconfidence Bias
- **Selected occupation:** Drill and Blast Engineer
- **Role and setting:** Technical design role responsible for planning drill patterns, explosive charging, and blast sequencing; designs blast patterns for varying rock conditions, coordinates with mine planning and shot-firing crews, works within established design templates and safety regulations. [thiess](https://thiess.com/uploads/Thiess-AZ-of-mining-jobs.pdf)
- **Why this occupation fits the bias list:** Drill and blast engineers frequently apply established blast-design templates across varying rock conditions. Experience bias (relying on patterns that worked well in the past rock type), status quo bias (resisting a design change even when a new rock type may warrant one), and overconfidence bias (in the predicted fragmentation outcome, based on the engineer's design experience) are all natural, distinct mechanisms in this technical design context.
- **Primary CTA scenario:** Designing a blast pattern for a new rock type using a long-used design template; experience bias in relying on past blast patterns, status quo bias in resisting design changes, overconfidence bias in predicted fragmentation outcome.
- **Triggering event:** A drill and blast engineer is tasked with designing a blast pattern for a newly encountered rock zone with different structural characteristics than the rock the engineer's standard template was developed for; the engineer must decide whether to apply the established template or design a new pattern.
- **Decision episodes:**
  1. Initial review of the new rock zone's geological characteristics against the established template's original design basis.
  2. Consideration of whether the standard template remains appropriate or requires modification.
  3. Prediction of the expected fragmentation outcome based on design experience.
  4. Final blast design decision and submission for approval.
- **Available cues and evidence:** Geological characterization of the new rock zone, the standard template's design parameters and historical performance record, any available test-blast data for similar rock types, the engineer's own experience with the template across past projects.
- **Competing interpretations:** The standard template remains appropriate because it has worked well historically vs. the new rock's different characteristics require a modified design; the predicted fragmentation outcome is reliable based on experience vs. is overconfident given the untested rock type.
- **Plausible actions:** Apply the standard template unmodified; design a new, modified pattern specific to the new rock zone; commission a small test blast before full-scale application; consult a geotechnical specialist on the rock's fragmentation behavior.
- **Constraints and pressures:** Production schedule pressure to proceed with blasting, the engineer's confidence in a template with a strong historical track record, limited time or budget for a dedicated test blast, safety regulations governing blast design approval.
- **Consequences of error:** Poor fragmentation (oversize or excessive fines) requiring costly secondary breakage or reprocessing, or unnecessary redesign effort if the standard template would have performed adequately.
- **Counterfactual causal variable:** Actual fragmentation behavior of the new rock type under the standard template (later found to differ substantially from the engineer's experience-based prediction due to previously unrecognized structural characteristics).
- **Expected interview structure:** Opening (engineer role context), Episode 1 (geological review), Episode 2 (template appropriateness consideration), Episode 3 (fragmentation prediction), Closing (reflection on the basis for the final design decision).
- **Natural biases:** Experience Bias, Status Quo Bias, Overconfidence Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Mine Planning Engineer (overlaps with Interview 5; experience bias and status quo bias already assigned there in a sequencing rather than blast-design context).
- **Rejected alternative occupation 2:** Underground Mine Manager (overlaps with Interview 7; overconfidence bias already assigned there in a production-halt rather than technical-design context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Availability Bias, Anchoring Bias, Confirmation Bias, Narrative Fallacy
- **Selected occupation:** Mine Ventilation Engineer
- **Role and setting:** Technical safety role responsible for designing and maintaining mine ventilation systems; monitors airflow and gas concentration data, adjusts fans and regulators, responds to gas-monitoring alarms, works individually with instrumentation and periodically with maintenance crews. [msha](https://www.msha.gov/sites/default/files/events/Mining-Occupations-and-Methods-vertical.pdf)
- **Why this occupation fits the bias list:** Ventilation engineers respond to gas-monitoring alarms where availability bias (a memorable past incident disproportionately shaping the interpretation of a new alarm), anchoring bias (the initial alarm reading setting a reference point for subsequent interpretation), confirmation bias (interpreting subsequent readings as consistent with the initial anchor), and narrative fallacy (constructing an explanatory account of the alarm pattern that feels more coherent than the underlying data supports) are all well-documented in safety-critical monitoring and coal-miner cognitive-bias literature. [rcis](https://www.rcis.ro/images/documente/rcis61_01.pdf)
- **Primary CTA scenario:** Assessing whether a gas-monitoring alarm pattern indicates a genuine ventilation deficiency or a sensor artifact after a memorable prior incident; availability bias from the memorable past incident, anchoring bias on the initial alarm reading, confirmation bias in interpreting subsequent readings, narrative fallacy in constructing an explanatory account.
- **Triggering event:** A gas sensor in a remote section of the mine registers an elevated methane reading; the ventilation engineer recalls a memorable incident two years earlier involving a genuine ventilation deficiency in a similar section, and the initial reading anchors the engineer's interpretation of subsequent, more ambiguous sensor data.
- **Decision episodes:**
  1. Initial alarm reading and recall of the memorable past incident.
  2. Formation of a working hypothesis anchored to the initial reading and the recalled incident.
  3. Interpretation of subsequent, more ambiguous sensor readings in light of that anchor.
  4. Construction of an explanatory account for the alarm pattern and final decision on ventilation adjustment or section evacuation.
- **Available cues and evidence:** The initial and subsequent sensor readings, airflow data for the section, the memorable past incident's specific circumstances and how closely they actually match the current situation, sensor calibration and maintenance history, alternative explanations (e.g., a sensor drift or a localized, non-hazardous gas pocket).
- **Competing interpretations:** The elevated reading indicates a genuine ventilation deficiency similar to the past incident vs. a sensor artifact or localized, non-hazardous condition; the subsequent readings confirm the initial anchor vs. are being selectively interpreted to fit it; the constructed narrative reflects the actual situation vs. a plausible story built from the memorable past incident and available data.
- **Plausible actions:** Order section evacuation and full ventilation investigation; adjust ventilation as a precaution while continuing operations; recalibrate or replace the sensor and continue monitoring; consult an independent second reading before deciding.
- **Constraints and pressures:** Immediate worker safety stakes, production pressure to avoid unnecessary evacuation, the vividness of the past incident, limited time to gather additional confirmatory data.
- **Consequences of error:** Continued operation in a genuinely hazardous ventilation deficiency, or unnecessary evacuation and production loss due to a misread sensor artifact.
- **Counterfactual causal variable:** Actual cause of the elevated reading (later found to be a sensor calibration drift unrelated to any genuine ventilation deficiency).
- **Expected interview structure:** Opening (ventilation engineer role context), Episode 1 (initial reading and recall), Episode 2 (anchor formation), Episode 3 (subsequent reading interpretation), Episode 4 (narrative construction and decision), Closing (reflection on the four-mechanism reasoning process).
- **Natural biases:** Availability Bias, Anchoring Bias, Confirmation Bias, Narrative Fallacy.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Mine Safety Officer (overlaps with Interview 6; availability bias and confirmation bias already assigned there in a post-incident investigative rather than real-time monitoring context).
- **Rejected alternative occupation 2:** Underground Mine Manager (overlaps with Interview 7; anchoring bias and availability bias already assigned there in a production-halt rather than technical-monitoring context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Attribution Bias, Illusion of Validity, Experience Bias, Status Quo Bias, Overconfidence Bias
- **Selected occupation:** Mine Planning Engineer
- **Role and setting:** Planning and scheduling role responsible for short- to mid-term mine sequencing, blast scheduling, blending, and stockpile management; coordinates with grade-control geologists, surveyors, and operations to maintain production targets against the mine plan. [realzambiajobs](https://www.realzambiajobs.com/detail/1530)
- **Why this occupation fits the bias list:** Mine planning engineers maintain an established sequencing approach across production periods, making attribution bias (attributing a data discrepancy from the grade-control geologist to a specific, convenient cause), illusion of validity (the plan's internal coherence producing unwarranted confidence in its accuracy), experience bias (relying on past sequencing decisions), status quo bias (resisting plan revision despite conflicting data), and overconfidence bias (in production forecasts) all well-documented and distinct mechanisms across the planning workflow.
- **Primary CTA scenario:** Revising the short-term mine plan after a grade-control geologist's data conflicts with the engineer's established sequencing approach; attribution bias in explaining the data discrepancy, illusion of validity in the plan's internal coherence, experience bias in relying on past sequencing decisions, status quo bias in resisting plan revision, overconfidence bias in production forecasts.
- **Triggering event:** A grade-control geologist reports ore-grade data for the next scheduled block that conflicts with the mine planning engineer's established sequencing approach, which has produced a coherent, internally consistent production schedule based on assumptions from past periods.
- **Decision episodes:**
  1. Initial review of the grade-control data against the existing plan's assumptions.
  2. Attribution of the discrepancy to a specific cause (e.g., sampling error) rather than a genuine geological change.
  3. Assessment of the plan's overall reliability based on its internal coherence and past performance.
  4. Final decision on whether to revise the sequencing, and production forecast confidence for the revised or retained plan.
- **Available cues and evidence:** The grade-control geologist's new data, the existing plan's assumptions and historical accuracy, past sequencing decisions and their outcomes, alternative explanations for the data discrepancy (genuine geological variability, sampling methodology differences), production targets and stakeholder expectations.
- **Competing interpretations:** The discrepancy reflects a sampling or measurement error vs. a genuine geological change requiring plan revision; the plan's internal coherence indicates it is reliable vs. reflects assumptions that have not been tested against this new data; past sequencing success justifies continuing the current approach vs. the new data warrants a different approach; the production forecast is well-calibrated vs. overconfident given the unresolved discrepancy.
- **Plausible actions:** Retain the current plan, attributing the discrepancy to a data issue; revise the sequencing to accommodate the new grade-control data; request additional sampling to resolve the discrepancy before deciding; present both scenarios to management with revised confidence intervals.
- **Constraints and pressures:** Production reporting deadlines, the engineer's investment in the existing plan's coherence, cross-disciplinary coordination requirements with geology and operations, budget cycle implications of a plan revision.
- **Consequences of error:** Continued production against an outdated plan leading to grade or tonnage shortfalls, or an unnecessary plan revision based on a data issue that did not reflect a genuine geological change.
- **Counterfactual causal variable:** Actual cause of the grade-control discrepancy (later found to reflect a genuine, previously unmapped geological variation rather than a sampling error).
- **Expected interview structure:** Opening (planning engineer role context), Episode 1 (data review), Episode 2 (discrepancy attribution), Episode 3 (plan reliability assessment), Episode 4 (revision decision and forecast), Closing (reflection on the five-mechanism reasoning process).
- **Natural biases:** Attribution Bias, Illusion of Validity, Experience Bias, Status Quo Bias, Overconfidence Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Drill and Blast Engineer (overlaps with Interview 3; experience bias and status quo bias already assigned there in a blast-design rather than sequencing context).
- **Rejected alternative occupation 2:** Underground Mine Manager (overlaps with Interview 7; overconfidence bias already assigned there in a production-halt rather than planning context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Availability Bias, Experience Bias, Confirmation Bias, Narrative Fallacy, Attribution Bias, Illusion of Validity
- **Selected occupation:** Mine Safety/Health & Safety Officer
- **Role and setting:** Investigative and compliance role responsible for near-miss and incident investigation, safety protocol enforcement, and regulatory reporting; conducts evidence-based investigations and compiles official incident reports for management and regulatory bodies. [procrestafrica](https://procrestafrica.com/open-positions/)
- **Why this occupation fits the bias list:** Safety officers conduct formal investigations that combine evidence review with pattern-matching to past cases, a context where availability bias (a recent, similar incident shaping the interpretation of the new one), experience bias (pattern-matching to past investigations rather than fresh analysis), confirmation bias (selectively gathering evidence supporting an early causal theory), narrative fallacy (constructing a coherent report narrative), attribution bias (assigning cause to a specific factor or individual), and illusion of validity (unwarranted confidence in the completed investigation's coherence) are all well-documented and map cleanly onto distinct stages of the investigation workflow. [rcis](https://www.rcis.ro/images/documente/rcis61_01.pdf)
- **Primary CTA scenario:** Investigating a near-miss incident and compiling the official incident report after forming an early causal theory; availability bias from a recent similar incident, experience bias in pattern-matching to past investigations, confirmation bias in evidence selection, narrative fallacy in report construction, attribution bias in assigning cause, illusion of validity in the completed investigation.
- **Triggering event:** A near-miss occurs when a piece of mobile equipment narrowly avoids striking a worker; the safety officer, who investigated a similar near-miss two months earlier, begins the investigation with an early theory based on that recent case.
- **Decision episodes:**
  1. Initial site visit and recall of the recent similar near-miss, shaping an early causal theory.
  2. Pattern-matching the current incident against the officer's experience with past investigations.
  3. Evidence collection, focused on details that support the early theory.
  4. Construction of the final report narrative, attribution of cause, and confidence assessment of the completed investigation.
- **Available cues and evidence:** Physical scene evidence, equipment operator and witness statements, the recent similar near-miss's specific circumstances and how closely they actually match, records of past similar investigations, alternative contributing factors not yet fully explored (e.g., a specific blind-spot hazard unique to this location).
- **Competing interpretations:** The current incident shares the same cause as the recent similar case vs. has a materially different underlying cause; evidence supporting the early theory is representative vs. selectively gathered; the officer's experience with similar past cases provides valid pattern recognition vs. inappropriately substitutes for fresh, case-specific analysis; the completed report's coherence indicates a valid investigation vs. reflects confidence not warranted by the actual evidence base.
- **Plausible actions:** Finalize the report attributing cause consistent with the early theory; broaden the evidence review to actively seek disconfirming information; consult an independent second investigator before finalizing; explicitly flag remaining uncertainty in the report rather than presenting a single definitive cause.
- **Constraints and pressures:** Regulatory reporting deadlines, management and workforce expectations for a clear explanation, the officer's professional experience and confidence in pattern recognition, limited time and resources for exhaustive investigation.
- **Consequences of error:** A misattributed cause leading to corrective action that fails to address the actual underlying hazard, allowing a similar or worse incident to recur.
- **Counterfactual causal variable:** Actual cause of the near-miss (later found, through a broader review, to involve a location-specific blind-spot hazard unrelated to the recent similar case's cause).
- **Expected interview structure:** Opening (safety officer role context), Episode 1 (initial theory formation), Episode 2 (pattern-matching), Episode 3 (evidence collection), Episode 4 (report construction and attribution), Closing (reflection on the six-mechanism investigation process).
- **Natural biases:** Availability Bias, Experience Bias, Confirmation Bias, Narrative Fallacy, Attribution Bias, Illusion of Validity.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four distinct investigation phases to avoid compression into a single point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Underground Mine Manager (overlaps with Interview 7; availability bias and confirmation bias already assigned there in a production-decision rather than investigative context).
- **Rejected alternative occupation 2:** Geotechnical Engineer (overlaps with Interview 2; attribution bias and illusion of validity already assigned there in a technical-modeling rather than investigative context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Anchoring Bias, Status Quo Bias, Overconfidence Bias, Availability Bias, Anchoring Bias, Confirmation Bias, Confirmation Bias
- **Selected occupation:** Underground Mine Manager / Assistant Mine Manager
- **Role and setting:** Senior operational decision-authority role responsible for overall underground mine operations; makes production-continuation or halt decisions based on safety and operational information from multiple sources (geotechnical, supervisory, crew), balances production targets against safety risk, works under significant organizational and regulatory accountability. [procrestafrica](https://procrestafrica.com/open-positions/)
- **Why this occupation fits the bias list:** Mine managers make high-consequence continue/halt decisions synthesizing multiple, sometimes conflicting information sources under time pressure — a context where anchoring bias (the initial inspection report setting a reference point — the duplicate entry is treated as one mechanism), status quo bias (preferring to continue production), overconfidence bias (in the section's safety margin), availability bias (a recent, memorable unrelated incident shaping risk perception), and confirmation bias (evaluating subsequent crew feedback in light of the initial anchor — the duplicate entry is treated as one mechanism) are all well-documented in crisis and operational decision-making literature.
- **Primary CTA scenario:** Deciding whether to halt production in a section after conflicting reports on ground conditions, weighing an initial inspection report against subsequent crew feedback; anchoring bias on the initial inspection report, status quo bias in continuing production, overconfidence bias in the section's safety margin, availability bias from a recent unrelated incident, confirmation bias in evaluating crew feedback.
- **Triggering event:** An initial ground-condition inspection report describes a section as "stable with minor, expected deformation"; production continues on this basis, but a crew reports unusual noise and minor debris shortly afterward, while the manager also recalls a recent, memorable but unrelated incident at another mine that heightens general risk sensitivity.
- **Decision episodes:**
  1. Initial inspection report review and formation of the manager's working assessment of the section's safety.
  2. Continuation of production consistent with that initial assessment.
  3. Receipt of the crew's subsequent report of unusual noise and debris, interpreted in light of the initial assessment and the recalled unrelated incident.
  4. Final decision on whether to halt production, continue with enhanced monitoring, or order a fresh independent inspection.
- **Available cues and evidence:** The initial inspection report and its specific findings, the crew's subsequent report of noise and debris, the recalled unrelated incident's actual relevance to this section's conditions, the section's historical stability record, availability of an independent second inspection.
- **Competing interpretations:** The initial "stable" assessment remains accurate vs. the subsequent crew report indicates a genuine change in conditions; continuing production reflects sound confidence in the section's safety margin vs. unwarranted overconfidence; the recalled unrelated incident is a relevant risk signal vs. an emotionally vivid but non-representative anchor; the crew's report confirms the initial assessment's benign framing vs. is being selectively interpreted to fit it.
- **Plausible actions:** Continue production with no change; halt production pending a fresh independent inspection; continue with enhanced monitoring and a lower evacuation threshold; convene an immediate review with the geotechnical engineer before deciding.
- **Constraints and pressures:** Production targets and schedule pressure, worker safety stakes, the manager's confidence in the initial inspection's competence, time pressure to respond to the crew's report promptly.
- **Consequences of error:** Continued production into a genuinely deteriorating ground condition risking a fall-of-ground incident, or an unnecessary production halt based on a benign noise/debris report unrelated to any real safety change.
- **Counterfactual causal variable:** Actual ground condition at the time of the decision (later found, through the crew's report and subsequent investigation, to have already begun deteriorating in a way not captured by the initial inspection).
- **Expected interview structure:** Opening (mine manager role context), Episode 1 (initial report and anchor), Episode 2 (continued production), Episode 3 (crew report and confirmation-biased interpretation), Episode 4 (final decision), Closing (reflection on the five-mechanism decision process).
- **Natural biases:** Status Quo Bias, Overconfidence Bias, Availability Bias.
- **Plausible but difficult biases:** Anchoring Bias (the duplicate entry must be treated as one mechanism, manifesting once at the initial-report stage), Confirmation Bias (the duplicate entry must be treated as one mechanism, manifesting once at the crew-report interpretation stage).
- **Biases that should not be forced:** A second, independent instance of Anchoring Bias and a second, independent instance of Confirmation Bias (the list's duplicates should not be coded as two separate mechanisms each).
- **Rejected alternative occupation 1:** Mine Planning Engineer (overlaps with Interview 5; overconfidence bias and status quo bias already assigned there in a sequencing rather than production-halt context).
- **Rejected alternative occupation 2:** Mine Safety Officer (overlaps with Interview 6; availability bias and confirmation bias already assigned there in a post-incident investigative rather than real-time operational-decision context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (duplicate Anchoring Bias and duplicate Confirmation Bias entries must each be coded as a single mechanism, not two independent instances)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (shift supervisor, geotechnical engineer, drill and blast engineer, ventilation engineer, mine planning engineer, safety officer, mine manager) | None | None | None | None needed |
| Work setting | Field supervisory (1), Technical/instrument-based (2, 4), Technical/creative design (3), Planning/office-field interface (5), Investigative (6), Senior operational authority (7) | Technical/instrument-based (2/7: 2, 4) | Technical | Public-facing, remote/digital | None critical; reflects the domain's inherently technical and field-based nature, and Interviews 2 and 4 differ materially in hazard type (ground stability vs. gas/ventilation) |
| Decision type | Retrospective narrative/reporting (1), Diagnosis/attribution (2), Design/creative judgment (3), Monitoring/anomaly detection (4), Planning/resource allocation (5), Investigation/compliance (6), Risk assessment/emergency response (7) | None significant | None | Negotiation, Personnel management | None critical; strong spread across decision types |
| Information environment | Retrospective/socially-mediated (1), Data-heavy/technical (2, 4), Technical/creative (3), Data-heavy/cross-disciplinary (5), Evidence-based/investigative (6), Multi-source/conflicting (7) | Data-heavy (2/7: 2, 4, 5) | Data-heavy | Rich/structured as primary driver | None critical; reflects the domain's genuine reliance on instrumentation and monitoring data |
| Time pressure | Moderate (1, 3), High (2, 4), Moderate (5, 6), High (7) | Moderate (3/7) | Balanced | Low | None critical |
| Consequence of error | Reputational/organizational (1), Safety/structural (2), Operational/financial (3), Safety/life-critical (4), Financial/production (5), Safety/regulatory (6), Safety/life-critical (7) | Safety (3/7: 2, 4, 7) | Safety | Environmental, educational | None critical; reflects the domain's inherent safety-criticality, balanced by financial/operational consequences in 1, 3, 5 |
| Expertise level | Independent professional/supervisor (1), Specialist (2, 3, 4), Specialist/senior practitioner (5), Independent/specialist (6), Decision authority (7) | Specialist (4/7: 2, 3, 4, 5) | Specialist | Developing practitioner | None critical; reflects that consequential, bias-rich decisions in this domain often sit with technically specialized roles, with Interview 7 providing senior-authority contrast |
| Stakeholder pattern | Individual with management reporting (1), Individual with instruments (2, 4), Individual with tools (3), Individual with cross-disciplinary coordination (5), Individual with organizational stakes (6), Individual with multi-source team input (7) | None significant | None | Multi-party negotiation, public-facing | None critical |
| Scenario archetype | Incident explanation (1), Ground-condition attribution (2), Blast design (3), Gas-alarm interpretation (4), Plan revision (5), Near-miss investigation (6), Production-halt decision (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Equipment failure root cause (1), Fall-of-ground cause (2), Rock fragmentation behavior (3), Sensor/ventilation cause (4), Grade-control discrepancy cause (5), Near-miss root cause (6), Ground-condition deterioration (7) | None significant | None | Equipment/technical hardware failure as primary variable (present but secondary in most) | None critical; all seven turn on a distinct, plausible causal fact appropriate to the domain |

**Overall assessment:** Strong diversity across occupations, settings, and decision types, spanning field supervision, technical specialist analysis (geotechnical, ventilation), creative technical design (blast engineering), cross-disciplinary planning, investigative compliance work, and senior operational decision authority. Specialist-level technical roles recur across several interviews, which is expected given mining's genuinely technical occupational structure, but each instance differs materially in hazard type, information source, and causal structure. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Narrative Fallacy (clear mechanism: coherent story built from loosely connected events) | None | Narrative Fallacy (risk of being read as simply "gave a wrong explanation") | None | None | None | Show the supervisor explicitly weaving together the two prior events into a single story; probe why the connection felt compelling, not just that the explanation was later found wrong |
| 2 | Attribution Bias (cause assignment to salient factor), Illusion of Validity (model-coherence confidence) | Attribution Bias and Narrative Fallacy (both involve constructing a causal account, though attribution bias specifically concerns assigning cause to a particular factor) | None | None | None | None | Show the engineer explicitly favoring the blast as the cause over an unexplored alternative; separate the model's historical coherence from its actual out-of-sample reliability |
| 3 | Experience Bias (past-pattern reliance), Status Quo Bias (resistance to design change), Overconfidence Bias (fragmentation prediction confidence) | Experience Bias and Status Quo Bias (closely related; experience bias concerns relying on past patterns as a cognitive shortcut, status quo bias concerns preference for the existing approach independent of its track record) | None | None | None | None | Show the engineer explicitly citing "this template has always worked" as distinct from a reasoned case-specific evaluation; separate the fragmentation-prediction confidence episode from the template-selection episode |
| 4 | Availability Bias (memorable-incident recall), Anchoring Bias (initial-reading reference point), Confirmation Bias (subsequent-reading interpretation), Narrative Fallacy (explanatory account construction) | Availability Bias and Anchoring Bias (both involve a specific reference point shaping judgment, though availability concerns ease of recall and anchoring concerns the first numerical/informational value received) | None | None | None | None | Show the memorable past incident explicitly and its specific (imperfect) match to the current situation; separate the initial-reading anchor from the subsequent selective interpretation of later readings |
| 5 | Attribution Bias, Illusion of Validity, Experience Bias, Status Quo Bias, Overconfidence Bias (five distinct) | Illusion of Validity and Overconfidence Bias (both involve unwarranted confidence, though illusion of validity concerns the plan's internal coherence specifically), Experience Bias and Status Quo Bias (as in Interview 3) | None | None | None | None | Distribute the five biases across the four distinct episodes; separate the plan's coherence-based confidence (illusion of validity) from the forecast-specific confidence (overconfidence bias) as distinct cues |
| 6 | Availability Bias, Experience Bias, Confirmation Bias, Narrative Fallacy, Attribution Bias, Illusion of Validity (six distinct mechanisms across investigation phases) | Availability Bias and Experience Bias (both involve reliance on past cases, though availability concerns recency/vividness and experience bias concerns general pattern-matching), Confirmation Bias and Narrative Fallacy (both involve shaping the account toward a preferred conclusion) | None | None | None | None | Distribute the six biases across the four distinct investigation phases; separate the recent-case recall (availability) from the general pattern-matching to past investigations (experience bias) as distinct cues |
| 7 | Status Quo Bias, Overconfidence Bias, Availability Bias (three cleanly distinguishable); Anchoring Bias, Confirmation Bias (each require single-instance treatment despite duplicate list entries) | Anchoring Bias (duplicate) and Status Quo Bias (both involve resistance to updating from an initial/current state), Confirmation Bias (duplicate) and Availability Bias (both involve selective interpretation shaped by a salient prior reference) | None | None | Anchoring Bias, Confirmation Bias (duplicate entries risk being forced into two separate instances each) | Anchoring Bias, Confirmation Bias | Treat each duplicate entry as one mechanism; show the initial inspection report as the sole anchoring event and the crew-report interpretation as the sole confirmation-bias event, rather than manufacturing two independent instances of either |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 7, generate exactly one Anchoring Bias mechanism (at the initial-report stage) and one Confirmation Bias mechanism (at the crew-report interpretation stage) despite the duplicate list entries; do not manufacture two independent instances of either. For Interviews 3 and 5, keep Experience Bias and Status Quo Bias distinct by showing the specific reasoning pattern (past-pattern reliance vs. preference for the current approach) rather than a single blended justification. For Interview 6, distribute all six biases across the four distinct investigation phases rather than compressing them into a single causal-attribution moment.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Availability Bias/Anchoring Bias in Interview 4; Availability Bias/Experience Bias in Interview 6; Illusion of Validity/Overconfidence Bias in Interview 5). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules. For Interview 7, explicitly confirm in the annotation key that only one instance each of Anchoring Bias and Confirmation Bias is coded, consistent with the duplicate-handling guidance.
