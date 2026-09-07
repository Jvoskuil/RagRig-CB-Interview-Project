## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Fire Inspector (Building Code Compliance) | Conducting a compliance inspection where the facility manager is a respected long-standing contact; courtesy bias in softening findings during the verbal exit briefing | 100% | 3 | High | Adds public-facing, one-to-one, compliance-inspection context | APPROVED |
| 2 | 2 | Fire Investigator (Origin and Cause) | Reconstructing a fire's origin and cause weeks after the scene has been altered, relying on witness interviews and a familiar-looking burn pattern; false memory in witness statement reliance, familiarity bias in pattern-matching to a past case | 100% | 6 | High | Adds forensic/investigative, evidence-based, retrospective context | APPROVED |
| 3 | 3 | Fire Protection System Designer (Sprinkler/Suppression Design Engineer) | Selecting a suppression system design for a new warehouse under a fixed client budget and timeline; incentive bias in favoring the client-preferred cheaper system, satisficing in stopping at the first code-compliant option, stereotyping in assuming occupancy-type risk profile | 100% | 9 | High | Adds design/engineering, client-relationship, resource-constrained context | APPROVED |
| 4 | 4 | Structural Fire Engineer (Performance-Based Design) | Reviewing a widely-cited fire-resistance test report while deciding whether to act immediately on a suspected design flaw in an active project; illusion of truth effect from repeated exposure to the test claim, action bias in immediate intervention, affect bias in emotional reaction to potential failure, default bias in following the standard design approach | 100% | 12 | High | Adds technical/data-heavy, high-consequence design review, individual analytical context | APPROVED |
| 5 | 5 | Process Safety Engineer (Chemical/Industrial Facility) | Participating in a hazard review team meeting for a new process unit where the team converges quickly on a risk rating; group polarization in team risk-rating discussion, Dunning-Kruger effect in a junior member's confident assessment, risk aversion bias in recommending excessive safeguards, in-group bias favoring the design team's own risk model, halo effect from a senior engineer's reputation | 100% | 15 | High | Adds team-based hazard analysis, cross-functional, high-consequence industrial context | APPROVED |
| 6 | 6 | Building/Fire Code Official (Plan Review and Permitting) | Reviewing a building permit application where several unrelated code-compliance indicators appear together, alongside base-rate data on similar building types; clustering illusion in seeing a pattern in the compliance indicators, probability neglect in a rare-hazard provision, optimism bias in construction-timeline compliance, ambiguity effect in an unclear code provision, authority bias toward a senior official's precedent ruling, hindsight bias in reviewing a past approval after an unrelated incident | 100% | 18 | High | Adds regulatory/administrative, documentation-heavy, individual-with-precedent context | APPROVED |
| 7 | 7 | Emergency Response/Incident Commander (Industrial Fire Brigade) | Commanding response to an industrial fire where the initial fire pattern resembles a familiar past incident, and the team must decide whether to continue an interior attack after significant resource commitment; representative heuristic in pattern-matching to the past incident, sunk cost bias in continuing given resources committed, status quo bias in maintaining the initial tactical plan, framing effect in how risk is communicated over radio, bandwagon effect from other units' actions, groupthink in command team consensus, recency effect in weighting the most recent radio report | 86% | 19 | Moderate-High | Adds high-time-pressure field command, team coordination, industrial fire-brigade context | APPROVED_WITH_CAVEATS (Bandwagon Effect and Groupthink require careful separation) |

***

## 2. Candidate occupation matrix

### Interview 1 (Courtesy Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Fire Inspector (Building Code Compliance) | 1 (Courtesy Bias) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (inspection, briefing, report phases) | High (change actual compliance severity) | High | High (adds public-facing, one-to-one context) | 0.88 |
| Fire Investigator | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.58 |
| Building/Fire Code Official | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| Process Safety Engineer | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.55 |
| Fire Protection System Designer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 3) | 0.48 |

**Selected:** Fire Inspector (best coverage, distinctness, diversity fit; courtesy bias is the natural core mechanism of the recurring inspector-facility-owner relationship). [iccsafe](https://www.iccsafe.org/wp-content/uploads/ICC_Careers_in_Codes.pdf)

***

### Interview 2 (False Memory, Familiarity Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Fire Investigator (Origin and Cause) | 2 (False Memory, Familiarity Bias) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (witness interview, pattern analysis phases) | High (change scene evidence reliability) | High | High (adds forensic/investigative, retrospective context) | 0.90 |
| Fire Inspector | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 1) | 0.68 |
| Structural Fire Engineer | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.65 |
| Process Safety Engineer | 0 | 1 | 1 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.52 |
| Incident Commander | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.55 |

**Selected:** Fire Investigator (best coverage, distinctness, diversity fit; grounded directly in the domain's designated forensic-investigation career path). [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)

***

### Interview 3 (Incentive Bias, Satisficing, Stereotyping)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Fire Protection System Designer | 3 (Incentive, Satisficing, Stereotyping) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (design, budget negotiation, occupancy assessment phases) | High (change actual occupancy risk profile) | High | High (adds design/engineering, client-relationship, resource-constrained context) | 0.92 |
| Fire Inspector | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 1) | 0.62 |
| Structural Fire Engineer | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.72 |
| Building/Fire Code Official | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.58 |
| Process Safety Engineer | 1 | 2 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.68 |

**Selected:** Fire Protection System Designer (best coverage, distinctness, diversity fit; grounded directly in fire-protection engineering's building/facility design pathway). [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)

***

### Interview 4 (Illusion of Truth Effect, Action Bias, Affect Bias, Default Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Structural Fire Engineer (Performance-Based Design) | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (test-report review, design decision phases) | High (change test report's actual validity) | High | High (adds technical/data-heavy, high-consequence design review context) | 0.94 |
| Fire Protection System Designer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 3) | 0.80 |
| Process Safety Engineer | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 5) | 0.72 |
| Building/Fire Code Official | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.65 |
| Incident Commander | 1 | 2 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.60 |

**Selected:** Structural Fire Engineer (best coverage, distinctness, scenario richness; grounded in performance-based fire engineering's reliance on published test data and standard design defaults). [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)

***

### Interview 5 (Group Polarization, Dunning-Kruger Effect, Risk Aversion Bias, In-group Bias, Halo Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Process Safety Engineer (Chemical/Industrial Facility) | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (hazard review team meeting phases) | High (change actual hazard severity data) | High | High (adds team-based hazard analysis, cross-functional context) | 0.95 |
| Structural Fire Engineer | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 4) | 0.80 |
| Building/Fire Code Official | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| Fire Protection System Designer | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.68 |
| Incident Commander | 3 | 2 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 7) | 0.70 |

**Selected:** Process Safety Engineer (best coverage, distinctness, diversity fit; grounded in the domain's process-safety hazard-review discipline, a well-recognized risk-engineering role). [risk-engineering](https://risk-engineering.org/careers/)

***

### Interview 6 (Clustering Illusion, Probability Neglect/Base-Rate Neglect, Optimism Bias, Ambiguity Effect, Authority Bias, Hindsight Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Building/Fire Code Official (Plan Review and Permitting) | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across review phases) | High (permit review, precedent-consultation phases) | High (change actual compliance pattern significance) | High | High (adds regulatory/administrative, documentation-heavy context) | 0.96 |
| Fire Inspector | 4 | 2 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 1) | 0.80 |
| Fire Protection System Designer | 3 | 2 | 1 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Process Safety Engineer | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.70 |
| Structural Fire Engineer | 2 | 2 | 2 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.60 |

**Selected:** Building/Fire Code Official (best coverage, distinctness, diversity fit; all six biases map cleanly onto distinct stages of the permit-review and precedent-consultation workflow). [iccsafe](https://www.iccsafe.org/wp-content/uploads/ICC_Careers_in_Codes.pdf)

***

### Interview 7 (Representative Heuristic, Sunk Cost Bias, Status Quo Bias, Framing Effect, Bandwagon Effect, Groupthink, Modality/Recency Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Emergency Response/Incident Commander (Industrial Fire Brigade) | 5 (Representative Heuristic, Sunk Cost, Status Quo, Framing, Recency) | 2 (Bandwagon, Groupthink) | 0 | 0 | 100% | Moderate-High (Bandwagon and Groupthink require careful separation) | High (rapid field command phases, multiple decision points) | High (change actual fire behavior/structural risk) | High | High (adds high-time-pressure field command, team coordination context) | 0.88 |
| Process Safety Engineer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| Structural Fire Engineer | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.76 |
| Fire Investigator | 3 | 2 | 1 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.68 |
| Building/Fire Code Official | 3 | 2 | 1 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.66 |

**Selected:** Emergency Response/Incident Commander (Industrial Fire Brigade) (best diversity fit, adds high-time-pressure field-command context; Bandwagon Effect and Groupthink require careful design to remain separable).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Courtesy Bias
- **Selected occupation:** Fire Inspector (Building Code Compliance)
- **Role and setting:** Municipal or fire-department-based inspection role; conducts routine and complaint-driven fire-safety and code-compliance inspections of commercial and industrial buildings, delivers findings verbally to facility representatives before issuing a formal written report. [iccsafe](https://www.iccsafe.org/wp-content/uploads/ICC_Careers_in_Codes.pdf)
- **Why this occupation fits the bias list:** Fire inspectors conduct repeated inspections at the same facilities over years, developing ongoing professional relationships with facility managers. Courtesy bias — softening or downplaying negative findings during in-person interactions to preserve a cordial relationship or avoid confrontation — is a natural, distinct mechanism in this recurring, socially-mediated inspection context.
- **Primary CTA scenario:** Conducting a compliance inspection where the facility manager is a respected long-standing contact; courtesy bias in softening findings during the verbal exit briefing.
- **Triggering event:** During a routine annual inspection of a warehouse the inspector has visited for the past six years, the inspector identifies a moderately serious violation (a partially blocked emergency exit) while the facility manager, with whom the inspector has a cordial working relationship, walks alongside during the inspection.
- **Decision episodes:**
  1. Initial identification of the violation during the walkthrough.
  2. Consideration of how to characterize the finding during the verbal exit briefing with the facility manager present.
  3. Delivery of the verbal briefing, including the specific language and framing used to describe the violation's severity.
  4. Final decision on how the violation is documented in the formal written report relative to how it was verbally characterized.
- **Available cues and evidence:** The physical condition of the blocked exit, applicable code provisions and severity classifications, the facility's inspection history and the manager's typical responsiveness to past findings, the inspector's own working relationship with the manager.
- **Competing interpretations:** The violation warrants a serious/urgent classification based on its actual life-safety risk vs. a softer characterization consistent with the cordial relationship and the facility's generally good compliance history; the verbal briefing should match the eventual written report's severity vs. can be softened without affecting the formal documentation.
- **Plausible actions:** Verbally characterize the violation with its full severity and require immediate correction; verbally soften the characterization while still documenting it accurately in the written report; verbally soften and correspondingly under-document the severity in the written report; escalate to a supervisor for a second opinion on classification.
- **Constraints and pressures:** The ongoing professional relationship with the facility manager, the manager's generally cooperative compliance history, time constraints of the inspection visit, departmental expectations for consistent code enforcement.
- **Consequences of error:** A softened characterization leading to delayed correction of a genuine life-safety hazard, or an inconsistency between the verbal and written findings undermining the inspection's enforceability.
- **Counterfactual causal variable:** Actual life-safety risk posed by the blocked exit under a plausible fire scenario (later found, through a subsequent incident elsewhere, to be more severe than the softened verbal characterization suggested).
- **Expected interview structure:** Opening (inspector role context), Episode 1 (violation identification), Episode 2 (briefing-language consideration), Episode 3 (verbal delivery), Closing (reflection on the gap between verbal and written characterization).
- **Natural biases:** Courtesy Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Building/Fire Code Official (would overlap with Interview 6; courtesy bias is plausible in permit-review interactions but reserved for the more complex six-bias plan-review scenario).
- **Rejected alternative occupation 2:** Fire Investigator (less naturally tied to courtesy bias, which depends on an ongoing recurring relationship rather than a one-time post-incident investigation).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** False Memory, Familiarity Bias
- **Selected occupation:** Fire Investigator (Origin and Cause)
- **Role and setting:** Forensic investigative role within a fire department, insurance company, or independent consulting firm; determines the origin and cause of fires through scene examination, witness interviews, and pattern analysis, often working weeks after the event once the scene has been disturbed by suppression and cleanup activity. [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)
- **Why this occupation fits the bias list:** Fire investigators rely heavily on witness recollection, which can be distorted over time (false memory — a witness's account, and the investigator's own recollection of early scene observations, becoming inaccurately reconstructed rather than accurately retrieved), and on visual pattern recognition informed by past cases (familiarity bias — a burn pattern resembling a past, familiar case leading to premature confidence in a similar cause), both well-documented mechanisms in fire forensic literature.
- **Primary CTA scenario:** Reconstructing a fire's origin and cause weeks after the scene has been altered, relying on witness interviews and a familiar-looking burn pattern; false memory in witness statement reliance, familiarity bias in pattern-matching to a past case.
- **Triggering event:** A fire investigator is called in several weeks after a commercial fire, after suppression and partial cleanup have altered the scene; the investigator interviews a witness whose account of the fire's early development has shifted subtly since their initial statement to responding firefighters, and the remaining burn pattern closely resembles a case the investigator handled two years earlier that was ultimately traced to a specific electrical fault.
- **Decision episodes:**
  1. Initial witness interview and comparison against the witness's earlier statement to first responders.
  2. Scene examination and identification of the burn pattern's resemblance to the past, familiar case.
  3. Formation of a working origin-and-cause hypothesis based on the witness account and pattern resemblance.
  4. Final determination and report, including the confidence level assigned to the conclusion.
- **Available cues and evidence:** The witness's current and earlier statements and their specific discrepancies, the remaining burn pattern and its degree of actual similarity to the past case, physical evidence (wiring, appliances) available for direct examination, the altered/disturbed condition of the scene limiting fresh physical evidence.
- **Competing interpretations:** The witness's current account accurately reflects what they observed vs. has been reconstructed and altered by post-event information and the passage of time; the burn pattern's resemblance to the past case indicates a similar electrical-fault cause vs. is a superficial similarity masking a different actual cause.
- **Plausible actions:** Determine cause consistent with the past case's electrical-fault pattern; pursue additional physical evidence examination before concluding; treat the witness's current account with reduced weight and rely primarily on physical evidence; document the determination as provisional pending further investigation.
- **Constraints and pressures:** The disturbed scene limiting fresh physical evidence, reporting deadlines for insurance or legal proceedings, the investigator's professional confidence from the past similar case, the passage of time since the fire.
- **Consequences of error:** A misattributed cause based on a coincidental pattern resemblance and a reconstructed witness account, potentially affecting insurance claims, legal liability, or future fire-prevention measures.
- **Counterfactual causal variable:** Actual origin and cause of the fire (later found, through detailed forensic analysis, to differ from the electrical-fault pattern the burn resembled).
- **Expected interview structure:** Opening (investigator role context), Episode 1 (witness interview), Episode 2 (pattern comparison), Episode 3 (hypothesis formation), Closing (reflection on the basis for the final determination).
- **Natural biases:** False Memory, Familiarity Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Structural Fire Engineer (overlaps with Interview 4; familiarity bias is plausible in design review but less naturally tied to witness-memory reconstruction).
- **Rejected alternative occupation 2:** Incident Commander (overlaps with Interview 7; familiarity/representative-pattern mechanisms already assigned there in a real-time rather than retrospective-investigative context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Incentive Bias, Satisficing, Stereotyping
- **Selected occupation:** Fire Protection System Designer (Sprinkler/Suppression Design Engineer)
- **Role and setting:** Building/facility design role within a fire protection engineering or consulting firm; designs fire detection and suppression systems for new construction projects, works directly with clients under budget and schedule constraints, ensures code compliance while managing client cost expectations. [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)
- **Why this occupation fits the bias list:** Fire protection designers work within a client-relationship structure where budget pressure creates incentive bias (favoring the client-preferred, cheaper suppression system over a more robust but costlier alternative), satisficing (stopping the design search at the first code-compliant option rather than continuing to seek an optimal one), and stereotyping (assuming a general risk profile based on the building's occupancy classification rather than examining its specific characteristics) are all natural, distinct mechanisms in this design-under-constraint context.
- **Primary CTA scenario:** Selecting a suppression system design for a new warehouse under a fixed client budget and timeline; incentive bias in favoring the client-preferred cheaper system, satisficing in stopping at the first code-compliant option, stereotyping in assuming occupancy-type risk profile.
- **Triggering event:** A designer is tasked with specifying a sprinkler system for a new warehouse; the client has expressed a strong budget preference for a less expensive standard wet-pipe system, the project timeline is tight, and the designer's initial assessment of the warehouse's occupancy classification suggests a standard, low-hazard risk profile similar to most warehouses the designer has worked on.
- **Decision episodes:**
  1. Initial occupancy classification and risk-profile assessment based on the building type.
  2. Identification of a first code-compliant suppression system option meeting minimum requirements.
  3. Consideration of the client's budget preference relative to more robust alternative designs.
  4. Final system selection and specification sign-off.
- **Available cues and evidence:** The building's specific intended contents and storage configuration (which may differ from a typical warehouse), the minimum code-compliant system option, alternative system designs offering greater protection margin, the client's stated budget and timeline constraints, the designer's fee structure and relationship with the client.
- **Competing interpretations:** The warehouse's occupancy classification accurately reflects its actual risk profile vs. the specific storage configuration presents a higher hazard than the general classification assumes; the first code-compliant option is adequate vs. a more thorough search would reveal a better-suited design; the client's budget preference should be accommodated vs. should not override a more protective design recommendation.
- **Plausible actions:** Specify the client-preferred, minimum-compliant system; recommend a more robust system despite the budget preference; conduct a more detailed hazard assessment of the specific storage configuration before finalizing; present the client with a cost-risk tradeoff for both options.
- **Constraints and pressures:** Client budget and timeline pressure, the designer's fee and ongoing client relationship, code minimum requirements as a compliance floor, professional liability considerations.
- **Consequences of error:** An undersized or mismatched suppression system inadequate for the warehouse's actual stored-goods hazard, or unnecessary cost imposed on the client if a more robust system was not actually warranted.
- **Counterfactual causal variable:** Actual hazard classification of the warehouse's specific storage configuration (later found, through a detailed commodity classification review, to be a higher-hazard category than the general occupancy assumption suggested).
- **Expected interview structure:** Opening (designer role context), Episode 1 (occupancy assessment), Episode 2 (compliant-option identification), Episode 3 (budget consideration), Closing (reflection on the basis for the final specification).
- **Natural biases:** Incentive Bias, Satisficing, Stereotyping.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Structural Fire Engineer (overlaps with Interview 4; satisficing and stereotyping are plausible there but reserved for the more complex four-bias performance-design scenario).
- **Rejected alternative occupation 2:** Process Safety Engineer (overlaps with Interview 5; incentive bias is plausible in industrial contexts but less naturally tied to a client-facing design-specification role).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Illusion of Truth Effect, Action Bias, Affect Bias, Default Bias
- **Selected occupation:** Structural Fire Engineer (Performance-Based Design)
- **Role and setting:** Specialized engineering role responsible for performance-based fire safety design of complex structures; evaluates fire-resistance test data, models fire behavior and structural response, decides whether standard prescriptive defaults or custom performance-based solutions are warranted for a given project. [eng.umd](https://eng.umd.edu/fire-protection-engineering-careers)
- **Why this occupation fits the bias list:** Structural fire engineers rely on published test reports and industry-standard defaults, making illusion of truth effect (a widely-cited fire-resistance test claim seeming more credible simply through repeated exposure across the literature) and default bias (following the standard prescriptive design approach rather than a custom performance-based analysis) natural mechanisms. Action bias (feeling compelled to intervene immediately upon suspecting a design flaw, even before full analysis) and affect bias (an emotional reaction to the potential consequences of failure coloring the technical judgment) are both well-documented in high-consequence engineering decision-making.
- **Primary CTA scenario:** Reviewing a widely-cited fire-resistance test report while deciding whether to act immediately on a suspected design flaw in an active project; illusion of truth effect from repeated exposure to the test claim, action bias in immediate intervention, affect bias in emotional reaction to potential failure, default bias in following the standard design approach.
- **Triggering event:** While finalizing the fire-resistance design for a high-rise atrium, the engineer notices a specific structural detail resembles a case where a widely-cited industry test report's rating claim has been referenced in dozens of design guides and papers over the years; a nagging concern arises that the test conditions may not fully represent this project's actual geometry, prompting an urge to immediately halt and revise the design.
- **Decision episodes:**
  1. Initial reliance on the widely-cited test report's rating claim as an established, credible basis for the design.
  2. Emergence of a specific concern about the test's applicability to this project's actual geometry, and an emotional reaction to the potential consequences of an undetected flaw.
  3. Impulse toward immediate design revision before completing a full applicability analysis.
  4. Final decision on whether to follow the standard default design approach, halt for revision, or conduct a more targeted analysis first.
- **Available cues and evidence:** The widely-cited test report and its specific test conditions, the atrium's actual geometry and how it differs from the tested configuration, the standard prescriptive default design approach and its general acceptance, the engineer's own emotional response to the potential failure consequence, project timeline pressure.
- **Competing interpretations:** The test report's widespread citation indicates it is well-validated and applicable vs. its frequent citation does not establish its applicability to this project's specific geometry; the standard default approach is appropriate here vs. this project's unusual geometry warrants a custom performance-based analysis; immediate design revision is the responsible course vs. a targeted analysis before acting would better serve the project.
- **Plausible actions:** Proceed with the standard default design relying on the widely-cited test report; immediately halt and revise the design based on the emerging concern; commission a targeted applicability analysis before deciding either way; consult a peer reviewer on the test's applicability.
- **Constraints and pressures:** Project timeline and budget, the engineer's professional standing and the emotional weight of a potential high-consequence failure, the widespread industry acceptance of the cited test report, client expectations for design certainty.
- **Consequences of error:** An undetected design flaw due to unwarranted reliance on the test report's applicability, or costly, unnecessary design revision triggered by an unanalyzed concern that a targeted analysis would have resolved.
- **Counterfactual causal variable:** Actual applicability of the cited test report's conditions to the atrium's specific geometry (later found, through a targeted analysis, to differ in a way that materially affected the fire-resistance rating).
- **Expected interview structure:** Opening (engineer role context), Episode 1 (test report reliance), Episode 2 (concern emergence and emotional reaction), Episode 3 (action impulse), Closing (reflection on the basis for the final decision).
- **Natural biases:** Illusion of Truth Effect, Action Bias, Affect Bias, Default Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Fire Protection System Designer (overlaps with Interview 3; default bias is plausible there but reserved for the more focused three-bias client-relationship scenario).
- **Rejected alternative occupation 2:** Process Safety Engineer (overlaps with Interview 5; affect bias is plausible in high-consequence hazard review but less naturally tied to an individual technical-analysis role).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Group Polarization, Dunning-Kruger Effect or Illusion of Understanding, Risk Aversion Bias, In-group Bias, Halo Effect
- **Selected occupation:** Process Safety Engineer (Chemical/Industrial Facility)
- **Role and setting:** Risk-engineering role within a chemical, petrochemical, or industrial processing facility; participates in and leads hazard and operability (HAZOP) reviews and risk assessments for new or modified process units, works within a cross-functional team including operations, engineering, and safety representatives. [risk-engineering](https://risk-engineering.org/careers/)
- **Why this occupation fits the bias list:** Process safety hazard reviews are conducted by structured teams, making group polarization (the team's risk-rating discussion converging toward a more extreme position than individual members initially held), Dunning-Kruger effect (a less experienced team member's confident but poorly calibrated risk assessment), risk aversion bias (the team recommending excessive, costly safeguards beyond what the actual risk warrants), in-group bias (favoring the design team's own risk model over an external or differing assessment), and halo effect (a senior engineer's general reputation lending unwarranted credibility to a specific risk judgment) all well-documented, distinct mechanisms in team-based hazard analysis.
- **Primary CTA scenario:** Participating in a hazard review team meeting for a new process unit where the team converges quickly on a risk rating; group polarization in team risk-rating discussion, Dunning-Kruger effect in a junior member's confident assessment, risk aversion bias in recommending excessive safeguards, in-group bias favoring the design team's own risk model, halo effect from a senior engineer's reputation.
- **Triggering event:** A process safety engineer leads a HAZOP review for a new reactor unit; a junior team member confidently asserts a specific failure-mode risk rating, a well-regarded senior engineer's supportive comment lends the assessment added weight, and the team's discussion progressively converges toward recommending a more extensive (and costly) set of safeguards than any individual member initially proposed.
- **Decision episodes:**
  1. Initial individual risk-rating proposals from team members, including the junior member's confident assessment.
  2. Team discussion, with the senior engineer's supportive comment influencing how the assessment is received.
  3. Progressive convergence of the group discussion toward a more extreme, more conservative risk rating.
  4. Final safeguard recommendation, including its cost and operational impact.
- **Available cues and evidence:** Individual team members' initial risk-rating proposals, the junior member's stated confidence level relative to their actual analytical basis, the senior engineer's specific comment and its influence on the discussion, the design team's own risk model versus an external benchmark, the final safeguard recommendation's cost and complexity relative to the actual risk reduction achieved.
- **Competing interpretations:** The junior member's confident assessment reflects genuine analytical insight vs. overestimates their own understanding of the failure mode's complexity; the senior engineer's supportive comment reflects sound technical judgment vs. lends unwarranted credibility based on reputation alone; the team's converged, more extreme recommendation reflects genuinely warranted caution vs. reflects group-discussion dynamics rather than a proportionate risk-based assessment; the design team's own risk model is well-calibrated vs. is being favored over an external model without adequate justification.
- **Plausible actions:** Adopt the team's converged, more extensive safeguard recommendation; request an independent, external risk-model comparison before finalizing; explicitly probe the junior member's basis for their confident assessment; scale the safeguard recommendation to a more risk-proportionate level.
- **Constraints and pressures:** Meeting time constraints, team dynamics and deference to the senior engineer, capital cost implications of the safeguard recommendation, regulatory documentation requirements for the HAZOP review.
- **Consequences of error:** Excessive, costly safeguards disproportionate to the actual risk, or, conversely, an underestimated risk if the junior member's confident but poorly calibrated assessment had instead been dismissed without proper scrutiny in either direction.
- **Counterfactual causal variable:** Actual failure-mode risk level for the reactor unit (later found, through an independent quantitative risk assessment, to be substantially lower than the team's converged rating).
- **Expected interview structure:** Opening (process safety engineer role context), Episode 1 (individual proposals), Episode 2 (senior engineer's influence), Episode 3 (group convergence), Closing (reflection on the basis for the final recommendation).
- **Natural biases:** Group Polarization, Dunning-Kruger Effect or Illusion of Understanding, Risk Aversion Bias, In-group Bias, Halo Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Structural Fire Engineer (overlaps with Interview 4; halo effect is plausible there but reserved for the more focused four-bias individual-analysis scenario).
- **Rejected alternative occupation 2:** Building/Fire Code Official (overlaps with Interview 6; authority bias is closely related to halo effect but reserved for the more complex six-bias regulatory scenario).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Clustering Illusion, Probability Neglect or Base-Rate Neglect, Optimism Bias, Ambiguity Effect, Authority Bias, Hindsight Bias
- **Selected occupation:** Building/Fire Code Official (Plan Review and Permitting)
- **Role and setting:** Regulatory administrative role within a municipal building/fire department; reviews construction plans and permit applications for code compliance, interprets ambiguous code provisions, consults precedent rulings, and issues approvals or requires modifications. [iccsafe](https://www.iccsafe.org/wp-content/uploads/ICC_Careers_in_Codes.pdf)
- **Why this occupation fits the bias list:** Code officials review documentation-heavy permit applications where clustering illusion (perceiving a meaningful pattern in several unrelated compliance indicators appearing together), probability/base-rate neglect (underweighting the low base rate of a rare hazard provision relative to a specific case's salient features), optimism bias (in assessing whether construction will meet compliance timelines), ambiguity effect (avoiding a clear ruling on an ambiguous code provision in favor of a safer, more conservative default interpretation), authority bias (deferring to a senior official's past precedent ruling), and hindsight bias (in reviewing a past approval after an unrelated incident elsewhere prompts scrutiny) are all well-documented mechanisms in regulatory decision-making. All six map cleanly onto distinct stages of the plan-review workflow.
- **Primary CTA scenario:** Reviewing a building permit application where several unrelated code-compliance indicators appear together, alongside base-rate data on similar building types; clustering illusion in seeing a pattern in the compliance indicators, probability neglect in a rare-hazard provision, optimism bias in construction-timeline compliance, ambiguity effect in an unclear code provision, authority bias toward a senior official's precedent ruling, hindsight bias in reviewing a past approval after an unrelated incident.
- **Triggering event:** A code official reviews a permit application for a mixed-use building where three unrelated minor compliance indicators happen to appear together (a slightly undersized stairwell, a nonstandard door swing, and a delayed sprinkler submittal), coinciding with a rare, low-probability hazard provision in the code and an ambiguous provision about egress lighting; a senior official's past precedent ruling on a similar ambiguous case is available for reference, and shortly afterward an unrelated fire incident elsewhere prompts the official to revisit a previously approved, similar permit.
- **Decision episodes:**
  1. Initial review of the three compliance indicators and consideration of whether their co-occurrence suggests a broader systemic issue with the application.
  2. Assessment of the rare-hazard provision's applicability given the building's actual, low base-rate risk profile.
  3. Interpretation of the ambiguous egress-lighting provision, informed by the senior official's past precedent ruling, and assessment of construction-timeline compliance likelihood.
  4. Final permit decision, followed later by a hindsight-informed review of a previously approved similar permit after the unrelated incident.
- **Available cues and evidence:** The three compliance indicators and their independent significance, the rare-hazard provision's actual statistical base rate for this building type, the ambiguous code provision's text and the senior official's past precedent ruling, the applicant's construction timeline, the unrelated incident's actual relevance to the previously approved permit.
- **Competing interpretations:** The three compliance indicators' co-occurrence reflects a genuinely systemic application-quality issue vs. is coincidental and each should be assessed independently; the rare-hazard provision's low base rate means it can be reasonably deprioritized vs. still warrants full compliance regardless of rarity; the senior official's precedent ruling is directly applicable vs. was based on materially different circumstances; the previously approved permit was reasonable given information available at the time vs. should have identified the same risk that the unrelated incident later highlighted.
- **Plausible actions:** Approve the permit with standard conditions; require additional review given the co-occurring indicators; apply the senior official's precedent ruling directly to the ambiguous provision; commission an independent review of the previously approved permit rather than relying on hindsight-informed judgment alone.
- **Constraints and pressures:** Permit processing deadlines, deference norms toward senior officials' precedent, applicant pressure for timely approval, public and departmental scrutiny following the unrelated incident.
- **Consequences of error:** Approval of a permit application with a genuine, overlooked systemic issue, or unwarranted rejection/delay based on a coincidental clustering of unrelated minor indicators; an unfair hindsight-informed judgment against a reasonable past approval.
- **Counterfactual causal variable:** Actual relationship between the three compliance indicators (later found to be entirely coincidental and unrelated to any systemic application-quality issue).
- **Expected interview structure:** Opening (code official role context), Episode 1 (indicator co-occurrence review), Episode 2 (rare-hazard provision assessment), Episode 3 (ambiguous provision interpretation), Episode 4 (later hindsight-informed review), Closing (reflection on the six-mechanism reasoning process).
- **Natural biases:** Clustering Illusion, Probability Neglect or Base-Rate Neglect, Optimism Bias, Ambiguity Effect, Authority Bias, Hindsight Bias.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four distinct episodes to avoid compression into a single decision point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Fire Inspector (overlaps with Interview 1; courtesy-adjacent authority dynamics already assigned there in a field-inspection rather than plan-review context).
- **Rejected alternative occupation 2:** Process Safety Engineer (overlaps with Interview 5; halo effect and authority bias are closely related but reserved for the team-based rather than individual-regulatory context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Representative Heuristic, Sunk Cost Bias, Status Quo Bias, Framing Effect, Bandwagon Effect, Groupthink, Modality Effect or Recency Effect
- **Selected occupation:** Emergency Response/Incident Commander (Industrial Fire Brigade)
- **Role and setting:** Field command role within an industrial or facility fire brigade; commands response to fires and hazardous incidents at industrial facilities, coordinates a response team, makes rapid tactical decisions under time pressure and incomplete information, holds on-scene decision authority.
- **Why this occupation fits the bias list:** Industrial fire brigade incident commanders make rapid tactical decisions under severe time pressure, a context where representative heuristic (pattern-matching the current fire's early signs to a familiar past incident type), sunk cost bias (continuing an interior attack because of resources already committed), status quo bias (maintaining the initial tactical plan despite new information), framing effect (how risk is communicated over radio affecting perceived urgency), bandwagon effect (other units' visible actions influencing the commander's own tactical choice), groupthink (the command team converging on consensus without adequately probing dissent), and recency effect (the most recent radio report being weighted more heavily than earlier, potentially more diagnostic reports) are all plausible, though bandwagon effect and groupthink require careful separation to remain distinguishable as individual-level versus group-level mechanisms.
- **Primary CTA scenario:** Commanding response to an industrial fire where the initial fire pattern resembles a familiar past incident, and the team must decide whether to continue an interior attack after significant resource commitment; representative heuristic in pattern-matching to the past incident, sunk cost bias in continuing given resources committed, status quo bias in maintaining the initial tactical plan, framing effect in how risk is communicated over radio, bandwagon effect from other units' actions, groupthink in command team consensus, recency effect in weighting the most recent radio report.
- **Triggering event:** An industrial fire brigade incident commander responds to a fire in a chemical storage area whose early smoke and flame pattern closely resembles a well-known past incident type the commander has trained extensively for; significant resources are committed to an interior attack based on this initial pattern-match, other units begin similar interior tactics, and a series of radio reports arrive, with the most recent one suggesting a possible change in conditions that contradicts an earlier, more detailed report.
- **Decision episodes:**
  1. Initial fire assessment and pattern-matching to the familiar past incident type, shaping the tactical plan.
  2. Commitment of significant resources to an interior attack consistent with that initial plan.
  3. Observation of other units' similar tactical actions and the command team's discussion converging on continuing the current approach.
  4. Interpretation of the most recent, contradictory radio report relative to the earlier, more detailed report, and final decision on continuing, modifying, or withdrawing.
- **Available cues and evidence:** The early fire pattern and its degree of actual similarity to the familiar past incident type, the resources already committed to the interior attack, other units' observed tactical actions, the sequence of radio reports and their relative detail and reliability, the command team's internal discussion dynamics.
- **Competing interpretations:** The current fire genuinely matches the familiar past incident type vs. shares only superficial similarities while differing in a critical respect; continuing the interior attack is justified by the situation vs. by the resources already committed; other units' similar actions indicate a sound consensus vs. reflect the same initial pattern-match bias rather than independent confirmation; the most recent radio report is most reliable because it is most current vs. the earlier, more detailed report should carry more weight; the command team's agreement reflects genuine consensus vs. suppressed dissent.
- **Plausible actions:** Continue the interior attack consistent with the initial plan; order an immediate withdrawal based on the contradictory recent report; request additional reconnaissance before deciding; explicitly solicit dissenting views from the command team before finalizing.
- **Constraints and pressures:** Extreme time pressure, firefighter safety stakes, the visible commitment of resources and other units already engaged, radio communication reliability and information lag.
- **Consequences of error:** Continued interior attack into a genuinely deteriorating hazardous-materials situation not captured by the familiar pattern-match, or an unnecessary withdrawal from a situation that was in fact consistent with the original, correct assessment.
- **Counterfactual causal variable:** Actual current hazard condition in the chemical storage area (later found to differ materially from the familiar past incident type in a way the most recent radio report was beginning to reveal).
- **Expected interview structure:** Opening (incident commander role context), Episode 1 (initial pattern-match), Episode 2 (resource commitment), Episode 3 (other units and team consensus), Episode 4 (contradictory report and final decision), Closing (reflection on the seven-mechanism reasoning process).
- **Natural biases:** Representative Heuristic, Sunk Cost Bias, Status Quo Bias, Framing Effect, Recency Effect.
- **Plausible but difficult biases:** Bandwagon Effect (requires an explicit individual-level cue — the commander's own tactical choice being influenced by observing other units — distinct from the team-level consensus), Groupthink (requires an explicit group-level dissent-suppression cue distinct from Bandwagon Effect).
- **Biases that should not be forced:** None outright, but Bandwagon Effect and Groupthink must be grounded in clearly distinct cues (individual imitation of others' visible actions vs. group-level suppression of dissent within the command team) to avoid being conflated as a single mechanism.
- **Rejected alternative occupation 1:** Process Safety Engineer (overlaps with Interview 5; group polarization and groupthink-adjacent mechanisms already assigned there in a deliberative-meeting rather than real-time field-command context).
- **Rejected alternative occupation 2:** Structural Fire Engineer (overlaps with Interview 4; default bias and status-quo-adjacent mechanisms already assigned there in a design-review rather than field-command context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Bandwagon Effect and Groupthink require explicit, distinct cues — individual imitation versus group-level dissent suppression — to remain separable)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (fire inspector, fire investigator, fire protection system designer, structural fire engineer, process safety engineer, building/fire code official, incident commander) | None | None | None | None needed |
| Work setting | Public-facing/field (1), Forensic/retrospective (2), Design/client-facing (3), Technical/individual analysis (4), Team-based industrial (5), Regulatory/administrative (6), High-time-pressure field command (7) | None significant | None | Remote/digital | None critical; strong spread across public-facing, forensic, design, technical, team, regulatory, and emergency-response settings |
| Decision type | Compliance/adjudication (1), Diagnosis/investigation (2), Design/resource allocation (3), Design/technical judgment (4), Risk assessment/team (5), Compliance/adjudication (6), Emergency response (7) | Compliance/adjudication (2/7: 1, 6) | Compliance/adjudication | Negotiation | None critical; Interviews 1 and 6 differ materially in scope (single inspection interaction vs. multi-stage regulatory review with six biases) |
| Information environment | Socially-mediated/one-to-one (1), Evidence-based/retrospective (2), Client-relationship/resource-constrained (3), Data-heavy/technical (4), Team/socially-mediated (5), Documentation-heavy/regulated (6), Rapidly-changing/socially-mediated (7) | Socially-mediated (3/7: 1, 5, 7) | Balanced | Rich/structured as sole driver | None critical; reflects the domain's genuine mix of interpersonal, technical, and regulatory information environments |
| Time pressure | Moderate (1, 3), Low/moderate (2, 6), Moderate-high (4), Moderate (5), Extreme (7) | Moderate (4/7) | Moderate | Very low | None critical; strong spread from low (retrospective investigation) to extreme (interior fire attack) |
| Consequence of error | Life-safety/enforcement (1), Legal/insurance (2), Life-safety/financial (3), High-consequence structural failure (4), Industrial safety/financial (5), Regulatory/legal (6), Immediate life-safety (7) | None significant | None | Environmental, educational | None critical; reflects the domain's inherent safety- and consequence-critical profile at varying time horizons |
| Expertise level | Independent professional (1, 2), Specialist (3, 4), Specialist/team (5), Senior practitioner/decision authority (6), Decision authority (7) | Specialist (3/7: 3, 4, 5) | Specialist | Developing practitioner | None critical; reflects that consequential bias-rich decisions in this domain often sit with technically specialized or senior roles |
| Stakeholder pattern | One-to-one (1), Individual with witnesses (2), Individual with client (3), Individual with tools (4), Team (5), Individual with precedent/hierarchy (6), Team with command authority (7) | Individual (3/7: 2, 3, 4) | Individual | Multi-party negotiation | None critical; Interviews 5 and 7 provide the needed team-based contrast |
| Scenario archetype | Inspection briefing (1), Origin-and-cause investigation (2), System design (3), Design review (4), Hazard review meeting (5), Permit/plan review (6), Interior-attack decision (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Actual hazard severity (1), Actual fire cause (2), Actual occupancy risk (3), Test-report applicability (4), Actual failure-mode risk (5), Indicator co-occurrence significance (6), Actual hazard condition (7) | None significant | None | Equipment/technical hardware failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact appropriate to the domain |

**Overall assessment:** Strong diversity across occupations, settings, decision types, and time horizons, spanning public-facing compliance work, forensic investigation, client-facing design, individual technical analysis, team-based industrial risk assessment, regulatory administration, and high-time-pressure field command. Compliance/adjudication-type decisions recur across two interviews, which is expected given the domain's regulatory character, but Interviews 1 and 6 differ materially in scope, bias complexity, and stakeholder configuration. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Courtesy Bias (clear mechanism: relationship-driven softening of findings) | None | None | None | None | None | Show the explicit gap between the verbal briefing's language and the written report's severity; probe why the softer language was chosen, not just that the violation existed |
| 2 | False Memory (reconstructed recollection), Familiarity Bias (pattern-resemblance confidence) | False Memory and ordinary witness unreliability (must show active reconstruction, not simply an inaccurate initial account) | None | None | False Memory (must show a specific, demonstrable shift in the witness's account over time) | False Memory | Show the witness's earlier and current statements explicitly, with a specific, demonstrable discrepancy; separate the pattern-resemblance judgment (familiarity bias) from the witness-account reliance (false memory) as distinct cues |
| 3 | Incentive Bias (budget-driven preference), Satisficing (first-adequate-option stopping), Stereotyping (occupancy-based generalization) | Incentive Bias and Satisficing (both can involve settling for a less thorough analysis, though incentive bias specifically concerns the client-budget motivation) | None | None | None | None | Show the designer explicitly citing the client's budget preference as a factor, distinct from a pure code-minimum satisficing stop; separate the occupancy-classification generalization from the specific storage-configuration examination that was skipped |
| 4 | Illusion of Truth Effect (repeated-citation credibility), Action Bias (immediate-intervention impulse), Affect Bias (emotion-colored judgment), Default Bias (standard-approach reliance) | Illusion of Truth Effect and Default Bias (both involve unwarranted confidence in an established, widely-used reference point) | None | None | Affect Bias (must show an explicit emotional reaction, not just professional concern) | Affect Bias | Show the test report's widespread citation explicitly as the basis for confidence, separate from the standard-approach reliance; show the engineer's explicit emotional reaction (e.g., described anxiety about failure consequences) rather than inferring affect bias from ordinary professional caution |
| 5 | Group Polarization, Dunning-Kruger Effect, Risk Aversion Bias, In-group Bias, Halo Effect (five distinct) | Halo Effect and Authority Bias (closely related; halo effect specifically concerns general reputation, authority bias concerns positional/hierarchical deference), Group Polarization and Groupthink (both involve group-level convergence, though not both present in this list) | None | None | Dunning-Kruger Effect (must show an explicit gap between the junior member's confidence and their actual analytical basis) | Dunning-Kruger Effect | Show the junior member's confidence level explicitly alongside a specific, limited analytical basis; separate the senior engineer's reputation-based influence (halo effect) from the design team's own-model preference (in-group bias) as distinct cues |
| 6 | Clustering Illusion, Probability Neglect/Base-Rate Neglect, Optimism Bias, Ambiguity Effect, Authority Bias, Hindsight Bias (six distinct mechanisms across review phases) | Clustering Illusion and Probability Neglect (both involve misjudging statistical significance, though clustering illusion concerns perceiving a pattern in co-occurring items, base-rate neglect concerns underweighting rarity), Authority Bias and Halo Effect (as in Interview 5) | Hindsight Bias | Hindsight Bias | None | None | Distribute the six biases across the four distinct episodes; ensure the hindsight-informed review is a clearly separate, later episode explicitly triggered by the unrelated incident, not inferred from the prior approval's outcome alone |
| 7 | Representative Heuristic, Sunk Cost Bias, Status Quo Bias, Framing Effect, Recency Effect (five cleanly distinguishable); Bandwagon Effect, Groupthink (require explicit distinct cues) | Bandwagon Effect and Groupthink (both involve social influence on the decision, though bandwagon concerns individual imitation of others' visible actions, groupthink concerns group-level dissent suppression), Sunk Cost Bias and Status Quo Bias (both involve resistance to changing course, though for different underlying reasons) | None | None | Bandwagon Effect (must show the commander's own tactical choice, not just observation of other units), Groupthink (must show explicit dissent-suppression within the command team) | Bandwagon Effect, Groupthink | Show the commander explicitly adjusting their own tactical choice based on observing other units (bandwagon), distinct from the command team's internal discussion suppressing a dissenting view (groupthink); separate the resource-investment justification (sunk cost) from the plan-inertia justification (status quo) as distinct reasoning statements |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 7, generate Bandwagon Effect as an individual-level mechanism (the commander's own choice shaped by observing other units) and Groupthink as a distinct group-level mechanism (an explicit dissenting view suppressed within the command team) — do not conflate the two. For Interview 6, ensure the hindsight-informed review episode is clearly triggered by the unrelated incident as a distinct, later event, not inferred from the prior approval's outcome. For Interview 4, ground Affect Bias in an explicit, described emotional reaction rather than ordinary professional caution.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Halo Effect/Authority Bias in Interviews 5 and 6; Clustering Illusion/Base-Rate Neglect in Interview 6; Sunk Cost/Status Quo Bias in Interview 7). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
