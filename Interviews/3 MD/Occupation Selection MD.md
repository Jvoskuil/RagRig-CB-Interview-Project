## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Intelligence Analyst (All-Source) | Post-strike assessment showing extreme success followed by回归 to average performance; analyst misattributes regression to tactical changes | 100% | 3 | High | Adds office-based analytical, individual decision-making, intelligence assessment context | APPROVED |
| 2 | 2 | Military Police Investigator / Criminal Investigations Division (CID) Special Agent | Investigating friendly fire incident; illusory correlation between unit ethnicity and incident rates; negative rejection of contradictory evidence | 100% | 6 | High | Adds law enforcement/investigative, field-based, one-to-one interaction, legal/regulatory consequences | APPROVED |
| 3 | 3 | Joint Operations Center (JOC) Watch Officer / Battle Captain | Rapidly developing crisis requiring course-of-action selection; retrievability of recent exercises, search set bias in intel databases, imaginability of worst-case scenarios | 100% | 9 | High | Adds command post, team coordination, high time pressure, operational continuity consequences | APPROVED |
| 4 | 4 | Fire Support Officer (FSO) / Joint Fires Observer | Planning close air support mission; gambler's fallacy in weather patterns, in-group bias toward own unit's capabilities, optimism in mission success, base-rate neglect of historical abort rates | 100% | 12 | High | Adds field combat support, human-machine collaboration, safety/operational consequences | APPROVED |
| 5 | 5 | Battalion Operations Officer (S3) | Planning major offensive operation; authority bias from higher HQ, hindsight bias in after-action review, representativeness in enemy COA prediction, status quo in force allocation, groupthink in staff planning | 100% | 15 | High | Adds staff planning, team decision-making, moderate time pressure, multi-stakeholder dynamics | APPROVED |
| 6 | 6 | Unmanned Aircraft System (UAS) Operator / Sensor Operator | Extended ISR mission with mixed target identification results; overconfidence in platform capabilities, availability of recent successes, anchoring on initial target assessment, confirmation in pattern analysis, regression to mean misattribution, illusory correlation in target patterns | 100% | 18 | High | Adds remote operations, human-machine collaboration, individual work with tools, intelligence/operational consequences | APPROVED |
| 7 | 7 | Special Operations Forces (SOF) Team Leader / Troop Commander | Planning high-risk direct action mission; negative rejection of dissenting intel, retrievability of past successful missions, search set bias in threat databases, imaginability of worst-case scenarios, gambler's fallacy in mission timing, in-group bias toward team capabilities, optimism in mission success | 86% | 19 | Moderate-High | Adds special operations, field-based, high consequence, team leadership, mixed information sources | APPROVED_WITH_CAVEATS (Gambler's Fallacy requires careful design) |

***

## 2. Candidate occupation matrix

### Interview 1 (Failure to recognize regression to the mean)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Intelligence Analyst (All-Source) | 1 (Regression to mean) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (multiple assessment phases) | High (change actual performance data) | High | High (adds analytical, individual role) | 0.88 |
| UAS Operator | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.78 |
| Fire Support Officer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Medium | 0.58 |
| Battalion S3 | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.62 |
| Logistics Officer (J4) | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Low | 0.42 |

**Selected:** Intelligence Analyst (best coverage, distinctness, diversity fit).

***

### Interview 2 (Illusory Correlation, Negative Rejection Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Military Police Investigator / CID Special Agent | 2 (Illusory Correlation, Negative Rejection) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (investigation phases, evidence evaluation) | High (change evidence reliability) | High | High (adds law enforcement, investigative role) | 0.90 |
| Intelligence Analyst | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Medium (overlaps with Interview 1) | 0.75 |
| Battalion S3 | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Medium | 0.70 |
| JOC Watch Officer | 1 | 0 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low | 0.55 |
| UAS Operator | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low | 0.52 |

**Selected:** Military Police Investigator / CID (best coverage, distinctness, diversity fit).

***

### Interview 3 (Retrievability Bias, Search set Bias, Imaginability Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Joint Operations Center (JOC) Watch Officer / Battle Captain | 3 (Retrievability, Search set, Imaginability) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (rapid decision phases, multiple information sources) | High (change intel database completeness) | High | High (adds command post, team coordination) | 0.92 |
| Intelligence Analyst | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 1) | 0.80 |
| Battalion S3 | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Medium | 0.76 |
| Fire Support Officer | 1 | 2 | 0 | 0 | 83% | Moderate | Moderate | Moderate | High | Medium | 0.68 |
| Logistics Officer (J4) | 1 | 1 | 1 | 0 | 67% | Moderate | Moderate | Moderate | High | Low | 0.58 |

**Selected:** JOC Watch Officer / Battle Captain (best coverage, distinctness, diversity fit).

***

### Interview 4 (Gambler's Fallacy, In-group bias, Optimism bias, Base-rate neglect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Fire Support Officer (FSO) / Joint Fires Observer | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (mission planning phases, weather, coordination) | High (change weather pattern data) | High | High (adds field combat support, fires role) | 0.94 |
| Battalion S3 | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 5) | 0.82 |
| SOF Team Leader | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.80 |
| JOC Watch Officer | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Intelligence Analyst | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low | 0.68 |

**Selected:** Fire Support Officer (best coverage, distinctness, diversity fit).

***

### Interview 5 (Authority Bias, Hindsight Bias, Representativeness, Status Quo Bias, Groupthink)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Battalion Operations Officer (S3) | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (staff planning phases, multiple stakeholders) | High (change higher HQ guidance accuracy) | High | High (adds staff planning, team decision-making) | 0.95 |
| JOC Watch Officer | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 3) | 0.82 |
| SOF Team Leader | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.80 |
| Intelligence Analyst | 3 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 1) | 0.74 |
| Logistics Officer (J4) | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Medium | 0.72 |

**Selected:** Battalion S3 (best coverage, distinctness, scenario richness).

***

### Interview 6 (Overconfidence, Availability Bias, Anchoring Bias, Confirmation Bias, Failure to recognize regression to the mean, Illusory Correlation)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Unmanned Aircraft System (UAS) Operator / Sensor Operator | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms) | High (extended ISR mission, multiple decision phases) | High (change target identification data accuracy) | High | High (adds remote operations, human-machine collaboration) | 0.96 |
| Intelligence Analyst | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Medium (overlaps with Interview 1) | 0.86 |
| JOC Watch Officer | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Medium | 0.78 |
| Fire Support Officer | 4 | 1 | 1 | 0 | 83% | Moderate-High | Moderate | Moderate | High | Medium | 0.72 |
| Battalion S3 | 3 | 2 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.68 |

**Selected:** UAS Operator / Sensor Operator (best coverage, distinctness, diversity fit).

***

### Interview 7 (Negative Rejection Bias, Retrievability Bias, Search set Bias, Imaginability Bias, Gambler's Fallacy, In-group bias, Optimism bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Special Operations Forces (SOF) Team Leader / Troop Commander | 5 (Negative Rejection, Retrievability, Search set, In-group, Optimism) | 2 (Imaginability, Gambler's Fallacy) | 0 | 0 | 100% | Moderate-High (Gambler's Fallacy requires careful design) | High (mission planning phases, team dynamics) | High (change threat intelligence accuracy) | High | High (adds special operations, field-based, team leadership) | 0.88 |
| Battalion S3 | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.80 |
| Fire Support Officer | 4 | 2 | 1 | 0 | 86% | Moderate-High | Moderate | Moderate | High | Medium | 0.75 |
| JOC Watch Officer | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.76 |
| Military Police Investigator | 3 | 2 | 2 | 0 | 71% | Moderate | Moderate | Moderate | High | Low | 0.65 |

**Selected:** SOF Team Leader (best diversity fit, adds special operations context; Gambler's Fallacy is plausible with careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Failure to recognize regression to the mean
- **Selected occupation:** Intelligence Analyst (All-Source)
- **Role and setting:** Office-based analytical role within intelligence unit; synthesizes multiple intelligence sources (SIGINT, HUMINT, IMINT, OSINT) to produce assessments for command decision-making.
- **Why this occupation fits the bias list:** Intelligence analysts routinely assess patterns in enemy activity, friendly force effectiveness, and operational outcomes. Failure to recognize regression to the mean is well-documented in intelligence analysis when extreme performance (e.g., highly successful strike) is followed by average performance, and analysts misattribute the regression to tactical changes rather than statistical inevitability. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Post-strike assessment showing extreme success followed by回归 to average performance; analyst misattributes regression to tactical changes.
- **Triggering event:** Intelligence analyst receives post-strike assessment data showing initial strike achieved 95% target destruction, followed by subsequent strikes achieving only 60-65% destruction rates.
- **Decision episodes:**
  1. Initial assessment of strike effectiveness data.
  2. Comparison with historical baseline performance.
  3. Attribution analysis (tactical changes vs. statistical regression).
  4. Recommendation on future strike planning and resource allocation.
- **Available cues and evidence:** Strike assessment reports, historical performance data, enemy adaptation indicators, weather and environmental factors, intelligence collection quality metrics.
- **Competing interpretations:** Performance decline due to enemy adaptation/tactical changes vs. statistical regression to mean; need for tactical adjustment vs. maintain current approach.
- **Plausible actions:** Recommend tactical modifications; recommend maintaining current approach; recommend additional intelligence collection on enemy adaptations.
- **Constraints and pressures:** Command expectations for continued high performance, time pressure for assessment, limited historical data, conflicting intelligence sources.
- **Consequences of error:** Unnecessary tactical changes wasting resources vs. failure to adapt to genuine enemy changes leading to reduced effectiveness.
- **Counterfactual causal variable:** Actual enemy tactical changes (later found that enemy made no significant adaptations; regression was purely statistical).
- **Expected interview structure:** Opening (analyst role context), Episode 1 (initial data review), Episode 2 (historical comparison), Episode 3 (attribution and recommendation), Closing (reflection on assessment process).
- **Natural biases:** Failure to recognize regression to the mean.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** UAS Operator (would overlap with Interview 6; less natural for regression analysis in intelligence context).
- **Rejected alternative occupation 2:** Fire Support Officer (less natural for regression to mean in strike assessment context).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Illusory Correlation, Negative Rejection Bias
- **Selected occupation:** Military Police Investigator / Criminal Investigations Division (CID) Special Agent
- **Role and setting:** Law enforcement/investigative role within military police; investigates crimes, incidents, and violations within military jurisdiction, including friendly fire incidents, fraud, and misconduct.
- **Why this occupation fits the bias list:** Military investigators routinely evaluate evidence, witness testimony, and incident patterns. Illusory correlation (perceiving relationships between variables that don't exist, e.g., unit ethnicity and incident rates) and negative rejection bias (dismissing contradictory evidence) are well-documented in investigative contexts where pattern recognition and evidence evaluation are critical. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Investigating friendly fire incident; illusory correlation between unit ethnicity and incident rates; negative rejection of contradictory evidence.
- **Triggering event:** CID special agent assigned to investigate friendly fire incident involving two units from different ethnic/regional backgrounds.
- **Decision episodes:**
  1. Initial evidence collection and witness interviews.
  2. Pattern analysis of similar incidents across units.
  3. Evaluation of contradictory evidence (e.g., training records, equipment status).
  4. Final determination and recommendation on charges or administrative action.
- **Available cues and evidence:** Incident reports, witness statements, training records, equipment maintenance logs, historical incident data by unit, demographic information.
- **Competing interpretations:** Incident pattern reflects genuine correlation with unit characteristics vs. random variation; contradictory evidence is reliable vs. unreliable.
- **Plausible actions:** Recommend charges against specific individuals/units; recommend administrative action; recommend no further action pending additional evidence.
- **Constraints and pressures:** Command pressure for resolution, time pressure for investigation, political sensitivity of inter-unit relations, legal standards for evidence.
- **Consequences of error:** Unjust charges against innocent personnel vs. failure to hold accountable those responsible; inter-unit tension escalation.
- **Counterfactual causal variable:** Actual correlation between unit characteristics and incident rates (later found that incident distribution was random; no genuine correlation existed).
- **Expected interview structure:** Opening (investigator role context), Episode 1 (evidence collection), Episode 2 (pattern analysis), Episode 3 (evaluation and determination), Closing (reflection on investigative process).
- **Natural biases:** Illusory Correlation, Negative Rejection Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Intelligence Analyst (overlaps with Interview 1; less natural for negative rejection in investigative context).
- **Rejected alternative occupation 2:** Battalion S3 (overlaps with Interview 5; less natural for illusory correlation in law enforcement context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Retrievability Bias, Search set Bias, Imaginability Bias
- **Selected occupation:** Joint Operations Center (JOC) Watch Officer / Battle Captain
- **Role and setting:** Command post operations; monitors and coordinates ongoing operations, manages information flow between command and subordinate units, makes rapid decisions during crisis situations.
- **Why this occupation fits the bias list:** Watch officers operate in high-tempo, information-rich environments where rapid decisions are required. Retrievability bias (relying on easily recalled examples), search set bias (limited search of information databases), and imaginability bias (overweighting vividly imaginable scenarios) are all natural in this context where time pressure and information overload are common. [armyupress.army](https://www.armyupress.army.mil/Portals/7/military-review/Archives/English/MilitaryReview_20120630MC_art011.pdf)
- **Primary CTA scenario:** Rapidly developing crisis requiring course-of-action selection; retrievability of recent exercises, search set bias in intel databases, imaginability of worst-case scenarios.
- **Triggering event:** JOC watch officer receives multiple reports of potential enemy movement near friendly force positions; situation developing rapidly with incomplete information.
- **Decision episodes:**
  1. Initial situation assessment and information gathering.
  2. Course-of-action development and evaluation.
  3. Coordination with higher HQ and subordinate units.
  4. Final recommendation to commander on force posture and actions.
- **Available cues and evidence:** Intelligence reports, unit status reports, recent exercise scenarios, terrain and weather data, historical enemy patterns, communications from subordinate units.
- **Competing interpretations:** Enemy movement is preparatory to attack vs. routine repositioning; worst-case scenario is likely vs. unlikely; information search is complete vs. incomplete.
- **Plausible actions:** Recommend force protection posture; recommend pre-emptive action; recommend continued monitoring with enhanced intelligence collection.
- **Constraints and pressures:** Time pressure for decision, incomplete information, command expectations, subordinate unit safety, coordination with higher HQ.
- **Consequences of error:** Unnecessary force protection reducing operational effectiveness vs. failure to protect forces leading to casualties; escalation of tension.
- **Counterfactual causal variable:** Actual enemy intent and capabilities (later found that enemy movement was routine repositioning; no attack planned).
- **Expected interview structure:** Opening (watch officer role context), Episode 1 (initial assessment), Episode 2 (COA development), Episode 3 (coordination and recommendation), Closing (reflection on decision process).
- **Natural biases:** Retrievability Bias, Search set Bias, Imaginability Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Intelligence Analyst (overlaps with Interview 1; less natural for retrievability in rapid decision context).
- **Rejected alternative occupation 2:** Battalion S3 (overlaps with Interview 5; less natural for imaginability in crisis context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Gambler's Fallacy, In-group bias, Optimism bias, Base-rate neglect
- **Selected occupation:** Fire Support Officer (FSO) / Joint Fires Observer
- **Role and setting:** Field combat support role; plans and coordinates close air support, artillery, and naval gunfire support for maneuver units; operates in forward areas with direct exposure to combat operations.
- **Why this occupation fits the bias list:** Fire support officers make critical decisions about weapon system employment, target prioritization, and risk assessment under time pressure. Gambler's fallacy (expecting weather patterns to "balance out"), in-group bias (favoring own unit's capabilities), optimism bias (overestimating mission success), and base-rate neglect (ignoring historical abort rates) are all well-documented in military planning and execution contexts. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Planning close air support mission; gambler's fallacy in weather patterns, in-group bias toward own unit's capabilities, optimism in mission success, base-rate neglect of historical abort rates.
- **Triggering event:** FSO tasked to plan close air support mission for upcoming offensive operation; weather forecasts show marginal conditions, historical abort rates are significant.
- **Decision episodes:**
  1. Initial mission planning and weather assessment.
  2. Asset availability and capability evaluation.
  3. Risk assessment and mitigation planning.
  4. Final mission recommendation and coordination with air assets.
- **Available cues and evidence:** Weather forecasts, historical abort rates, asset availability, unit capabilities, enemy air defense threats, terrain and target data, higher HQ guidance.
- **Competing interpretations:** Weather will improve based on recent patterns vs. weather will remain marginal; own unit's capabilities are sufficient vs. additional assets needed; historical abort rates are applicable vs. not applicable to current conditions.
- **Plausible actions:** Recommend mission proceed as planned; recommend mission delay pending better weather; recommend additional assets or alternative weapon systems.
- **Constraints and pressures:** Operational timeline, higher HQ expectations, subordinate unit requirements, asset availability, weather constraints, enemy threat.
- **Consequences of error:** Unnecessary mission delay reducing operational momentum vs. mission abort or failure with tactical implications; resource misallocation.
- **Counterfactual causal variable:** Actual weather pattern behavior (later found that weather did not improve as expected; gambler's fallacy led to incorrect expectation).
- **Expected interview structure:** Opening (FSO role context), Episode 1 (mission planning), Episode 2 (risk assessment), Episode 3 (recommendation and coordination), Closing (reflection on planning process).
- **Natural biases:** Gambler's Fallacy, In-group bias, Optimism bias, Base-rate neglect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Battalion S3 (overlaps with Interview 5; less natural for gambler's fallacy in weather context).
- **Rejected alternative occupation 2:** SOF Team Leader (overlaps with Interview 7; less natural for base-rate neglect in fires context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Authority Bias or Higher-level prioritization Bias, Hindsight Bias, Representativeness, Status Quo Bias, Groupthink
- **Selected occupation:** Battalion Operations Officer (S3)
- **Role and setting:** Staff planning role within battalion headquarters; responsible for operations planning, training, and coordination of battalion activities; works closely with commander and other staff sections (S1, S2, S4, etc.).
- **Why this occupation fits the bias list:** Battalion S3s operate in staff planning environments where authority from higher HQ, group dynamics, and planning processes create fertile ground for these biases. Authority bias (deferring to higher HQ guidance), hindsight bias (in after-action reviews), representativeness (predicting enemy COA based on similarity to past patterns), status quo bias (maintaining current force allocation), and groupthink (staff planning consensus) are all well-documented in military staff planning contexts. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Planning major offensive operation; authority bias from higher HQ, hindsight bias in after-action review, representativeness in enemy COA prediction, status quo in force allocation, groupthink in staff planning.
- **Triggering event:** Battalion S3 tasked to develop operations plan for upcoming offensive operation; higher HQ provides initial guidance, staff begins planning process.
- **Decision episodes:**
  1. Initial planning guidance review and staff coordination.
  2. Enemy COA development and wargaming.
  3. Force allocation and resource planning.
  4. Final plan development and commander brief.
- **Available cues and evidence:** Higher HQ guidance, intelligence estimates, historical enemy patterns, unit capabilities, resource availability, terrain and weather data, staff input and recommendations.
- **Competing interpretations:** Higher HQ guidance is optimal vs. requires modification; enemy COA predictions are accurate vs. incomplete; force allocation is appropriate vs. requires adjustment; staff consensus reflects best analysis vs. groupthink.
- **Plausible actions:** Recommend plan as developed; recommend modifications to higher HQ guidance; recommend additional planning or wargaming; recommend alternative force allocation.
- **Constraints and pressures:** Higher HQ expectations, operational timeline, resource limitations, staff dynamics, commander preferences, subordinate unit requirements.
- **Consequences of error:** Plan failure leading to operational setbacks vs. unnecessary plan modifications delaying operation; resource misallocation affecting mission success.
- **Counterfactual causal variable:** Accuracy of higher HQ guidance and enemy COA predictions (later found that higher HQ guidance was based on outdated intelligence; enemy COA differed significantly from predictions).
- **Expected interview structure:** Opening (S3 role context), Episode 1 (planning guidance review), Episode 2 (enemy COA development), Episode 3 (force allocation and plan development), Closing (reflection on planning process).
- **Natural biases:** Authority Bias, Hindsight Bias, Representativeness, Status Quo Bias, Groupthink.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** JOC Watch Officer (overlaps with Interview 3; less natural for authority bias in staff planning context).
- **Rejected alternative occupation 2:** Logistics Officer (J4) (less natural for representativeness and groupthink in logistics context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Overconfidence, Availability Bias, Anchoring Bias, Confirmation Bias, Failure to recognize regression to the mean, Illusory Correlation
- **Selected occupation:** Unmanned Aircraft System (UAS) Operator / Sensor Operator
- **Role and setting:** Remote operations role; operates unmanned aircraft systems for ISR missions, target acquisition, and battle damage assessment; works in ground control stations with human-machine collaboration.
- **Why this occupation fits the bias list:** UAS operators work in information-rich, technology-mediated environments where pattern recognition, target identification, and assessment decisions are critical. Overconfidence (in platform capabilities), availability (recent successes), anchoring (initial target assessment), confirmation (seeking data supporting assessment), regression to mean (misattributing performance changes), and illusory correlation (seeing patterns in target data) are all natural in this context where extended missions generate large volumes of data. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Extended ISR mission with mixed target identification results; overconfidence in platform capabilities, availability of recent successes, anchoring on initial target assessment, confirmation in pattern analysis, regression to mean misattribution, illusory correlation in target patterns.
- **Triggering event:** UAS operator conducting extended ISR mission; initial target identification highly successful, followed by mixed results with increasing false positives/negatives.
- **Decision episodes:**
  1. Initial target identification and assessment.
  2. Pattern analysis and correlation with other intelligence sources.
  3. Confidence assessment and recommendation on target validity.
  4. Mission adjustment and resource allocation decisions.
- **Available cues and evidence:** Sensor data (video, IR, etc.), historical target data, intelligence reports, platform performance metrics, environmental conditions, communications with intelligence analysts.
- **Competing interpretations:** Target patterns are genuine vs. random variation; platform performance is degrading vs. target characteristics are changing; initial assessment is accurate vs. requires revision.
- **Plausible actions:** Recommend target engagement; recommend additional intelligence collection; recommend mission adjustment or platform repositioning; recommend no further action on certain targets.
- **Constraints and pressures:** Mission timeline, platform limitations, bandwidth constraints, command expectations, coordination with other assets, environmental conditions.
- **Consequences of error:** False target engagement wasting resources vs. missed target opportunities; platform misallocation reducing operational effectiveness.
- **Counterfactual causal variable:** Actual target pattern validity (later found that target patterns were random variation; no genuine correlation existed).
- **Expected interview structure:** Opening (UAS operator role context), Episode 1 (initial target assessment), Episode 2 (pattern analysis), Episode 3 (confidence assessment and recommendation), Closing (reflection on assessment process).
- **Natural biases:** Overconfidence, Availability Bias, Anchoring Bias, Confirmation Bias, Failure to recognize regression to the mean, Illusory Correlation.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Intelligence Analyst (overlaps with Interview 1; less natural for overconfidence in platform context).
- **Rejected alternative occupation 2:** JOC Watch Officer (overlaps with Interview 3; less natural for anchoring in target identification context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Negative Rejection Bias, Retrievability Bias, Search set Bias, Imaginability Bias, Gambler's Fallacy, In-group bias, Optimism bias
- **Selected occupation:** Special Operations Forces (SOF) Team Leader / Troop Commander
- **Role and setting:** Special operations field leadership; plans and executes high-risk direct action missions, special reconnaissance, and other special operations; leads small teams in austere environments with high autonomy.
- **Why this occupation fits the bias list:** SOF team leaders operate in high-stakes, information-limited environments where mission planning and execution require rapid decisions with incomplete information. Negative rejection (dismissing dissenting intelligence), retrievability (past successful missions), search set (limited threat databases), imaginability (worst-case scenarios), gambler's fallacy (mission timing based on recent patterns), in-group bias (team capabilities), and optimism (mission success) are all plausible, though gambler's fallacy requires careful design to avoid feeling artificial. [apps.dtic](https://apps.dtic.mil/sti/tr/pdf/ADA493560.pdf)
- **Primary CTA scenario:** Planning high-risk direct action mission; negative rejection of dissenting intel, retrievability of past successful missions, search set bias in threat databases, imaginability of worst-case scenarios, gambler's fallacy in mission timing, in-group bias toward team capabilities, optimism in mission success.
- **Triggering event:** SOF team leader tasked to plan high-risk direct action mission; intelligence reports conflicting threat assessments, recent mission success rate is high.
- **Decision episodes:**
  1. Initial mission planning and intelligence review.
  2. Threat assessment and risk mitigation planning.
  3. Team capability evaluation and resource allocation.
  4. Final mission recommendation and go/no-go decision.
- **Available cues and evidence:** Intelligence reports, historical mission data, threat databases, team performance records, environmental conditions, higher HQ guidance, communications with intelligence analysts.
- **Competing interpretations:** Threat assessments are accurate vs. exaggerated; mission timing is optimal vs. suboptimal; team capabilities are sufficient vs. require augmentation; dissenting intelligence is reliable vs. unreliable.
- **Plausible actions:** Recommend mission proceed as planned; recommend mission delay or modification; recommend additional intelligence collection or team augmentation; recommend mission cancellation.
- **Constraints and pressures:** Operational timeline, higher HQ expectations, team safety, mission objectives, environmental conditions, intelligence limitations.
- **Consequences of error:** Mission failure with casualties vs. unnecessary mission delay reducing operational momentum; resource misallocation affecting other missions.
- **Counterfactual causal variable:** Actual threat level and mission timing optimality (later found that dissenting intelligence was accurate; threat level was higher than assessed).
- **Expected interview structure:** Opening (SOF team leader role context), Episode 1 (mission planning), Episode 2 (threat assessment), Episode 3 (team capability and recommendation), Closing (reflection on planning process).
- **Natural biases:** Negative Rejection Bias, Retrievability Bias, Search set Bias, In-group bias, Optimism bias.
- **Plausible but difficult biases:** Imaginability Bias, Gambler's Fallacy.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Battalion S3 (overlaps with Interview 5; less natural for negative rejection in special operations context).
- **Rejected alternative occupation 2:** Fire Support Officer (overlaps with Interview 4; less natural for retrievability in SOF context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Gambler's Fallacy requires careful design to avoid feeling artificial)

***

## 4. Bias-by-occupation compatibility matrix

| Occupation | Failure to recognize regression to the mean | Illusory Correlation | Negative Rejection Bias | Retrievability Bias | Search set Bias | Imaginability Bias | Gambler's Fallacy | In-group bias | Optimism bias | Base-rate neglect | Authority Bias | Hindsight Bias | Representativeness | Status Quo Bias | Groupthink | Overconfidence | Availability Bias | Anchoring Bias | Confirmation Bias |
|------------|---------------------------------------------|----------------------|-------------------------|---------------------|-----------------|---------------------|-------------------|---------------|---------------|-------------------|----------------|----------------|--------------------|-----------------|------------|----------------|-------------------|----------------|-------------------|
| Intelligence Analyst (All-Source) | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | WEAK | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | WEAK | PLAUSIBLE | NATURAL | NATURAL | NATURAL |
| Military Police Investigator / CID | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | WEAK | WEAK | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | WEAK | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL |
| JOC Watch Officer / Battle Captain | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL |
| Fire Support Officer (FSO) | PLAUSIBLE | PLAUSIBLE | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | PLAUSIBLE | NATURAL | PLAUSIBLE |
| Battalion Operations Officer (S3) | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL |
| UAS Operator / Sensor Operator | NATURAL | NATURAL | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | WEAK | WEAK | NATURAL | PLAUSIBLE | WEAK | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | WEAK | NATURAL | NATURAL | NATURAL | NATURAL |
| SOF Team Leader / Troop Commander | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | NATURAL | NATURAL | PLAUSIBLE | NATURAL |

**Explanations for non-NATURAL cells:**
- **PLAUSIBLE:** Bias can be embedded with moderate scenario design effort (e.g., Negative Rejection in Intelligence Analyst role requires careful evidence presentation).
- **WEAK:** Bias mechanism is possible but would require careful scenario design to avoid feeling artificial (e.g., Gambler's Fallacy in Intelligence Analyst role is less natural as analysts typically work with statistical data).

***

## 5. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations | None | None | None | None needed |
| Work setting | Office (1, 6), Command post (3), Field (2, 4, 7), Staff headquarters (5) | Field-based (3/7), Office-based (2/7) | Field-based | Clinical/care-oriented, Industrial/technical | None critical; reflects military operations nature |
| Decision type | Assessment (1, 6), Investigation (2), Crisis response (3), Planning (4, 5, 7) | Planning (3/7), Assessment (2/7) | Planning | Diagnosis, Emergency response | None critical; planning is natural for military |
| Information environment | Data-heavy (1, 3, 6), Conflicting sources (1, 2, 5, 7), Incomplete (3, 4, 7), Regulated (2, 5) | Data-heavy (3/7), Conflicting (4/7) | Conflicting sources, Data-heavy | Rich/structured, Socially mediated | None critical; reflects military information complexity |
| Time pressure | Moderate (1, 2, 5, 6), High (3, 4, 7) | Moderate (4/7) | Moderate | Low | None needed |
| Consequence of error | Safety (3, 4, 7), Operational (1, 3, 4, 5, 7), Legal/regulatory (2), Intelligence (1, 6) | Operational (5/7), Safety (3/7) | Operational, Safety | Financial, Environmental, Educational | None critical; reflects military consequence profile |
| Expertise level | Independent professional (2, 3, 6), Senior practitioner (1, 4, 7), Supervisor/manager (5) | Independent professional (3/7), Senior practitioner (3/7) | Independent professional, Senior practitioner | Developing practitioner, Strategist | None needed |
| Stakeholder pattern | Individual (1, 6), Team (3, 5, 7), One-to-one (2), Multi-party (4) | Team (3/7) | Team | One-to-one, Public interaction | None critical |
| Scenario archetype | Assessment (1, 6), Investigation (2), Crisis response (3), Planning (4, 5, 7) | Planning (3/7), Assessment (2/7) | Planning | Emergency response, Negotiation | None critical |
| Causal-counterfactual structure | Data accuracy (1, 6), Evidence reliability (2), Intent/capabilities (3, 7), Weather/patterns (4), Guidance accuracy (5) | Data/intent (4/7) | Data/intent accuracy | Equipment failure, Human performance | None critical; reflects military causal structure |

**Overall assessment:** Good diversity across occupations, settings, decision types, and consequence profiles. Planning scenarios are slightly overrepresented (3/7), but this reflects the nature of military decision-making where planning is prominent. Field-based and office-based roles are well-balanced. No critical substitutions needed.

***

## 6. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Failure to recognize regression to the mean (clear mechanism: statistical misattribution) | None | None | None | None | None | Ensure clear statistical baseline data; probe attribution reasoning explicitly |
| 2 | Illusory Correlation (pattern perception), Negative Rejection (evidence dismissal) | None | None | None | None | None | Provide clear contradictory evidence; probe evidence evaluation process |
| 3 | Retrievability (memory-based), Search set (database search), Imaginability (vivid scenarios) | Retrievability and Imaginability (both involve memory/vividness) | None | None | Imaginability (vividness cues may be subtle) | Imaginability | Provide explicit vivid scenario cues; separate memory retrieval from imagination |
| 4 | Gambler's Fallacy (pattern expectation), In-group bias (favoritism), Optimism (success overestimation), Base-rate neglect (ignoring statistics) | Optimism and Base-rate neglect (both involve probability misjudgment) | None | None | Gambler's Fallacy (pattern cues may be subtle) | Gambler's Fallacy | Provide clear pattern data; separate in-group favoritism from optimism |
| 5 | Authority Bias (deference), Hindsight Bias (outcome knowledge), Representativeness (pattern matching), Status Quo (maintenance), Groupthink (consensus) | Hindsight Bias and outcome bias (both involve outcome knowledge), Authority Bias and Groupthink (both involve social influence) | Hindsight Bias | Hindsight Bias | Groupthink (consensus cues may be subtle) | Groupthink, Hindsight Bias | Separate outcome knowledge from decision process; probe authority influence explicitly |
| 6 | Overconfidence, Availability, Anchoring, Confirmation, Regression to mean, Illusory Correlation (all distinct) | Availability and Retrievability (both involve memory), Anchoring and Confirmation (both involve initial information), Regression and Illusory Correlation (both involve pattern perception) | None | None | Regression to mean (statistical cues may be subtle), Illusory Correlation (pattern cues may be subtle) | Regression to mean, Illusory Correlation | Provide clear statistical baseline; separate initial anchor from subsequent information |
| 7 | Negative Rejection, Retrievability, Search set, In-group, Optimism (distinct); Imaginability, Gambler's Fallacy (require careful design) | Retrievability and Imaginability (both involve memory/vividness), In-group and Optimism (both involve positive bias) | None | None | Gambler's Fallacy (pattern cues may be subtle), Imaginability (vividness cues may be subtle) | Gambler's Fallacy, Imaginability | Provide clear pattern data; separate memory retrieval from imagination |

**Overall safeguards:**
- **Prompt 1 (interview generation):** Ensure each bias has distinct cues and decision episodes; avoid conflating memory-based biases (Retrievability, Imaginability) with pattern-based biases (Gambler's Fallacy, Illusory Correlation).
- **Prompt 2 (annotation):** Provide clear bias definitions and decision episode boundaries; require annotators to identify specific cues for each bias.

***

## 7. Final generation handoff blocks

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
1

SELECTED OCCUPATION:
Intelligence Analyst (All-Source)

ROLE AND SETTING:
Office-based analytical role within intelligence unit; synthesizes multiple intelligence sources (SIGINT, HUMINT, IMINT, OSINT) to produce assessments for command decision-making.

REQUESTED BIASES:
Failure to recognize regression to the mean

PRIMARY SCENARIO:
Post-strike assessment showing extreme success followed by回归 to average performance; analyst misattributes regression to tactical changes.

DECISION EPISODES:
1. Initial assessment of strike effectiveness data.
2. Comparison with historical baseline performance.
3. Attribution analysis (tactical changes vs. statistical regression).
4. Recommendation on future strike planning and resource allocation.

AVAILABLE INFORMATION AND CUES:
Strike assessment reports, historical performance data, enemy adaptation indicators, weather and environmental factors, intelligence collection quality metrics.

COMPETING INTERPRETATIONS:
Performance decline due to enemy adaptation/tactical changes vs. statistical regression to mean; need for tactical adjustment vs. maintain current approach.

CONSTRAINTS AND PRESSURES:
Command expectations for continued high performance, time pressure for assessment, limited historical data, conflicting intelligence sources.

CONSEQUENCES:
Unnecessary tactical changes wasting resources vs. failure to adapt to genuine enemy changes leading to reduced effectiveness.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual enemy tactical changes (later found that enemy made no significant adaptations; regression was purely statistical).

BIAS-SPECIFIC DESIGN NOTES:
Failure to recognize regression to the mean should manifest as misattributing performance decline to tactical changes rather than statistical inevitability. Analyst should expect continued high performance based on initial extreme success.

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
Military and defense operations

INTERVIEW ID:
2

SELECTED OCCUPATION:
Military Police Investigator / Criminal Investigations Division (CID) Special Agent

ROLE AND SETTING:
Law enforcement/investigative role within military police; investigates crimes, incidents, and violations within military jurisdiction, including friendly fire incidents, fraud, and misconduct.

REQUESTED BIASES:
Illusory Correlation, Negative Rejection Bias

PRIMARY SCENARIO:
Investigating friendly fire incident; illusory correlation between unit ethnicity and incident rates; negative rejection of contradictory evidence.

DECISION EPISODES:
1. Initial evidence collection and witness interviews.
2. Pattern analysis of similar incidents across units.
3. Evaluation of contradictory evidence (e.g., training records, equipment status).
4. Final determination and recommendation on charges or administrative action.

AVAILABLE INFORMATION AND CUES:
Incident reports, witness statements, training records, equipment maintenance logs, historical incident data by unit, demographic information.

COMPETING INTERPRETATIONS:
Incident pattern reflects genuine correlation with unit characteristics vs. random variation; contradictory evidence is reliable vs. unreliable.

CONSTRAINTS AND PRESSURES:
Command pressure for resolution, time pressure for investigation, political sensitivity of inter-unit relations, legal standards for evidence.

CONSEQUENCES:
Unjust charges against innocent personnel vs. failure to hold accountable those responsible; inter-unit tension escalation.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual correlation between unit characteristics and incident rates (later found that incident distribution was random; no genuine correlation existed).

BIAS-SPECIFIC DESIGN NOTES:
Illusory Correlation should manifest as perceiving relationships between unit ethnicity and incident rates that don't exist. Negative Rejection Bias should manifest as dismissing contradictory evidence (e.g., training records showing no differences).

BIAS PAIRS TO KEEP SEPARATE:
Illusory Correlation and Negative Rejection Bias (distinct mechanisms: one involves pattern perception, the other involves evidence evaluation).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
3

SELECTED OCCUPATION:
Joint Operations Center (JOC) Watch Officer / Battle Captain

ROLE AND SETTING:
Command post operations; monitors and coordinates ongoing operations, manages information flow between command and subordinate units, makes rapid decisions during crisis situations.

REQUESTED BIASES:
Retrievability Bias, Search set Bias, Imaginability Bias

PRIMARY SCENARIO:
Rapidly developing crisis requiring course-of-action selection; retrievability of recent exercises, search set bias in intel databases, imaginability of worst-case scenarios.

DECISION EPISODES:
1. Initial situation assessment and information gathering.
2. Course-of-action development and evaluation.
3. Coordination with higher HQ and subordinate units.
4. Final recommendation to commander on force posture and actions.

AVAILABLE INFORMATION AND CUES:
Intelligence reports, unit status reports, recent exercise scenarios, terrain and weather data, historical enemy patterns, communications from subordinate units.

COMPETING INTERPRETATIONS:
Enemy movement is preparatory to attack vs. routine repositioning; worst-case scenario is likely vs. unlikely; information search is complete vs. incomplete.

CONSTRAINTS AND PRESSURES:
Time pressure for decision, incomplete information, command expectations, subordinate unit safety, coordination with higher HQ.

CONSEQUENCES:
Unnecessary force protection reducing operational effectiveness vs. failure to protect forces leading to casualties; escalation of tension.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual enemy intent and capabilities (later found that enemy movement was routine repositioning; no attack planned).

BIAS-SPECIFIC DESIGN NOTES:
Retrievability Bias should manifest as relying on easily recalled examples (e.g., recent exercises). Search set Bias should manifest as limited search of information databases. Imaginability Bias should manifest as overweighting vividly imaginable scenarios (worst-case).

BIAS PAIRS TO KEEP SEPARATE:
Retrievability and Imaginability (distinct mechanisms: one involves memory retrieval, the other involves vividness).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
4

SELECTED OCCUPATION:
Fire Support Officer (FSO) / Joint Fires Observer

ROLE AND SETTING:
Field combat support role; plans and coordinates close air support, artillery, and naval gunfire support for maneuver units; operates in forward areas with direct exposure to combat operations.

REQUESTED BIASES:
Gambler's Fallacy, In-group bias, Optimism bias, Base-rate neglect

PRIMARY SCENARIO:
Planning close air support mission; gambler's fallacy in weather patterns, in-group bias toward own unit's capabilities, optimism in mission success, base-rate neglect of historical abort rates.

DECISION EPISODES:
1. Initial mission planning and weather assessment.
2. Asset availability and capability evaluation.
3. Risk assessment and mitigation planning.
4. Final mission recommendation and coordination with air assets.

AVAILABLE INFORMATION AND CUES:
Weather forecasts, historical abort rates, asset availability, unit capabilities, enemy air defense threats, terrain and target data, higher HQ guidance.

COMPETING INTERPRETATIONS:
Weather will improve based on recent patterns vs. weather will remain marginal; own unit's capabilities are sufficient vs. additional assets needed; historical abort rates are applicable vs. not applicable to current conditions.

CONSTRAINTS AND PRESSURES:
Operational timeline, higher HQ expectations, subordinate unit requirements, asset availability, weather constraints, enemy threat.

CONSEQUENCES:
Unnecessary mission delay reducing operational momentum vs. mission abort or failure with tactical implications; resource misallocation.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual weather pattern behavior (later found that weather did not improve as expected; gambler's fallacy led to incorrect expectation).

BIAS-SPECIFIC DESIGN NOTES:
Gambler's Fallacy should manifest as expecting weather patterns to "balance out" based on recent patterns. In-group bias should manifest as favoring own unit's capabilities over objective assessment. Optimism bias should manifest as overestimating mission success. Base-rate neglect should manifest as ignoring historical abort rates.

BIAS PAIRS TO KEEP SEPARATE:
Optimism and Base-rate neglect (distinct mechanisms: one involves success overestimation, the other involves statistical neglect).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
5

SELECTED OCCUPATION:
Battalion Operations Officer (S3)

ROLE AND SETTING:
Staff planning role within battalion headquarters; responsible for operations planning, training, and coordination of battalion activities; works closely with commander and other staff sections (S1, S2, S4, etc.).

REQUESTED BIASES:
Authority Bias or Higher-level prioritization Bias, Hindsight Bias, Representativeness, Status Quo Bias, Groupthink

PRIMARY SCENARIO:
Planning major offensive operation; authority bias from higher HQ, hindsight bias in after-action review, representativeness in enemy COA prediction, status quo in force allocation, groupthink in staff planning.

DECISION EPISODES:
1. Initial planning guidance review and staff coordination.
2. Enemy COA development and wargaming.
3. Force allocation and resource planning.
4. Final plan development and commander brief.

AVAILABLE INFORMATION AND CUES:
Higher HQ guidance, intelligence estimates, historical enemy patterns, unit capabilities, resource availability, terrain and weather data, staff input and recommendations.

COMPETING INTERPRETATIONS:
Higher HQ guidance is optimal vs. requires modification; enemy COA predictions are accurate vs. incomplete; force allocation is appropriate vs. requires adjustment; staff consensus reflects best analysis vs. groupthink.

CONSTRAINTS AND PRESSURES:
Higher HQ expectations, operational timeline, resource limitations, staff dynamics, commander preferences, subordinate unit requirements.

CONSEQUENCES:
Plan failure leading to operational setbacks vs. unnecessary plan modifications delaying operation; resource misallocation affecting mission success.

COUNTERFACTUAL CAUSAL VARIABLE:
Accuracy of higher HQ guidance and enemy COA predictions (later found that higher HQ guidance was based on outdated intelligence; enemy COA differed significantly from predictions).

BIAS-SPECIFIC DESIGN NOTES:
Authority Bias should manifest as deferring to higher HQ guidance without critical evaluation. Hindsight Bias should manifest in after-action review (outcome knowledge affecting judgment). Representativeness should manifest as predicting enemy COA based on similarity to past patterns. Status Quo Bias should manifest as maintaining current force allocation. Groupthink should manifest as staff planning consensus without critical evaluation.

BIAS PAIRS TO KEEP SEPARATE:
Authority Bias and Groupthink (distinct mechanisms: one involves hierarchical deference, the other involves group consensus); Hindsight Bias and outcome bias (distinct mechanisms: one involves outcome knowledge, the other involves outcome evaluation).

BIAS MECHANISMS NOT TO FORCE:
Hindsight Bias (requires careful separation from outcome knowledge).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
6

SELECTED OCCUPATION:
Unmanned Aircraft System (UAS) Operator / Sensor Operator

ROLE AND SETTING:
Remote operations role; operates unmanned aircraft systems for ISR missions, target acquisition, and battle damage assessment; works in ground control stations with human-machine collaboration.

REQUESTED BIASES:
Overconfidence, Availability Bias, Anchoring Bias, Confirmation Bias, Failure to recognize regression to the mean, Illusory Correlation

PRIMARY SCENARIO:
Extended ISR mission with mixed target identification results; overconfidence in platform capabilities, availability of recent successes, anchoring on initial target assessment, confirmation in pattern analysis, regression to mean misattribution, illusory correlation in target patterns.

DECISION EPISODES:
1. Initial target identification and assessment.
2. Pattern analysis and correlation with other intelligence sources.
3. Confidence assessment and recommendation on target validity.
4. Mission adjustment and resource allocation decisions.

AVAILABLE INFORMATION AND CUES:
Sensor data (video, IR, etc.), historical target data, intelligence reports, platform performance metrics, environmental conditions, communications with intelligence analysts.

COMPETING INTERPRETATIONS:
Target patterns are genuine vs. random variation; platform performance is degrading vs. target characteristics are changing; initial assessment is accurate vs. requires revision.

CONSTRAINTS AND PRESSURES:
Mission timeline, platform limitations, bandwidth constraints, command expectations, coordination with other assets, environmental conditions.

CONSEQUENCES:
False target engagement wasting resources vs. missed target opportunities; platform misallocation reducing operational effectiveness.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual target pattern validity (later found that target patterns were random variation; no genuine correlation existed).

BIAS-SPECIFIC DESIGN NOTES:
Overconfidence should manifest as confidence in platform capabilities beyond objective performance. Availability Bias should manifest as reliance on recent successes. Anchoring Bias should manifest as reliance on initial target assessment. Confirmation Bias should manifest as seeking data supporting assessment. Failure to recognize regression to the mean should manifest as misattributing performance changes. Illusory Correlation should manifest as seeing patterns in target data that don't exist.

BIAS PAIRS TO KEEP SEPARATE:
Availability and Anchoring (distinct mechanisms: one involves memory, the other involves initial information); Regression to mean and Illusory Correlation (distinct mechanisms: one involves statistical misattribution, the other involves pattern perception).

BIAS MECHANISMS NOT TO FORCE:
None.

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

```text
OCCUPATIONAL DOMAIN:
Military and defense operations

INTERVIEW ID:
7

SELECTED OCCUPATION:
Special Operations Forces (SOF) Team Leader / Troop Commander

ROLE AND SETTING:
Special operations field leadership; plans and executes high-risk direct action missions, special reconnaissance, and other special operations; leads small teams in austere environments with high autonomy.

REQUESTED BIASES:
Negative Rejection Bias, Retrievability Bias, Search set Bias, Imaginability Bias, Gambler's Fallacy, Ingroup Preference bias/In-group bias, Optimism bias

PRIMARY SCENARIO:
Planning high-risk direct action mission; negative rejection of dissenting intel, retrievability of past successful missions, search set bias in threat databases, imaginability of worst-case scenarios, gambler's fallacy in mission timing, in-group bias toward team capabilities, optimism in mission success.

DECISION EPISODES:
1. Initial mission planning and intelligence review.
2. Threat assessment and risk mitigation planning.
3. Team capability evaluation and resource allocation.
4. Final mission recommendation and go/no-go decision.

AVAILABLE INFORMATION AND CUES:
Intelligence reports, historical mission data, threat databases, team performance records, environmental conditions, higher HQ guidance, communications with intelligence analysts.

COMPETING INTERPRETATIONS:
Threat assessments are accurate vs. exaggerated; mission timing is optimal vs. suboptimal; team capabilities are sufficient vs. require augmentation; dissenting intelligence is reliable vs. unreliable.

CONSTRAINTS AND PRESSURES:
Operational timeline, higher HQ expectations, team safety, mission objectives, environmental conditions, intelligence limitations.

CONSEQUENCES:
Mission failure with casualties vs. unnecessary mission delay reducing operational momentum; resource misallocation affecting other missions.

COUNTERFACTUAL CAUSAL VARIABLE:
Actual threat level and mission timing optimality (later found that dissenting intelligence was accurate; threat level was higher than assessed).

BIAS-SPECIFIC DESIGN NOTES:
Negative Rejection Bias should manifest as dismissing dissenting intelligence. Retrievability Bias should manifest as relying on past successful missions. Search set Bias should manifest as limited search of threat databases. Imaginability Bias should manifest as overweighting worst-case scenarios. Gambler's Fallacy should manifest as expecting mission timing to "balance out" based on recent patterns. In-group bias should manifest as favoring team capabilities over objective assessment. Optimism bias should manifest as overestimating mission success.

BIAS PAIRS TO KEEP SEPARATE:
Retrievability and Imaginability (distinct mechanisms: one involves memory retrieval, the other involves vividness); In-group and Optimism (distinct mechanisms: one involves group favoritism, the other involves success overestimation).

BIAS MECHANISMS NOT TO FORCE:
Gambler's Fallacy (requires careful design to avoid feeling artificial).

TARGET INTERVIEW LENGTH:
Approximately 1,350 words.

INTERVIEW CONDITION:
BIAS_INJECTED
```

***

## 8. Machine-readable JSON

Removed to .json fil
