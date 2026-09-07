This confirms strong grounding for framing effect, anchoring, confirmation bias, and bias blind spot specifically in crisis/emergency management decision-making literature, and normalcy/normality bias is well-documented in disaster preparedness contexts. Now building the full allocation.

## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Emergency Management Training Officer | Designing a public evacuation briefing after years of technical expertise, unintentionally omitting steps that seem obvious; curse of knowledge in assuming audience shares the officer's background understanding | 100% | 3 | High | Adds instructional/communication design, individual work, public-facing context | APPROVED |
| 2 | 2 | Public Information Officer (Emergency/Crisis Communications) | Selecting a warning graphic and repeated message format for a public alert campaign; mere exposure in favoring a familiar visual template, picture superiority in choosing image-based over text-based warnings | 100% | 6 | High | Adds visual/communication design, public-facing, media-relations context | APPROVED |
| 3 | 3 | Local Emergency Manager (County/Municipal Level) | Reviewing the jurisdiction's hazard mitigation plan years after the last major event; bias blind spot in reviewing peer jurisdictions' plans more critically than one's own, normality bias in underestimating recurrence likelihood, planning fallacy in timeline/resource estimates for plan implementation | 100% | 9 | High | Adds long-horizon planning, moderate procedural structure, individual-with-organizational-context | APPROVED |
| 4 | 4 | Meteorological Hazard Forecaster (Emergency Support Function) | Issuing a severe weather warning based on a limited ensemble model run and a directive from a senior forecaster; illusion of validity in trusting the coherent-looking forecast pattern, insensitivity to sample size in the small ensemble, authority bias toward the senior forecaster's call, bandwagon effect from other forecast offices' matching warnings | 100% | 12 | High | Adds technical/data-heavy forecasting, individual-with-team-hierarchy, rapidly changing information context | APPROVED |
| 5 | 5 | Incident Commander (Structural Fire/Hazmat Response) | Making a go/no-go decision on interior attack during an active structural fire based on initial size-up information; framing effect in how risk is presented over radio, hindsight bias in after-action review, bandwagon effect from other units' actions, anchoring bias on the initial size-up report, confirmation bias in interpreting subsequent radio traffic | 100% | 15 | High | Adds high-time-pressure field command, team coordination, immediate safety-consequence context | APPROVED |
| 6 | 6 | Emergency Preparedness Curriculum Designer / Exercise Planner | Designing a full-scale disaster exercise scenario after years of specialized expertise, drawing heavily on familiar past exercise formats and vivid past-incident imagery; curse of knowledge in scenario complexity, mere exposure in reusing familiar exercise formats, picture superiority in scenario materials, bias blind spot in self-assessing objectivity, normality bias in underestimating the exercise's realistic severity, planning fallacy in exercise timeline | 100% | 18 | High | Adds instructional design, long-horizon planning, moderate time pressure, individual-with-organizational-review context | APPROVED |
| 7 | 7 | Emergency Operations Center (EOC) Situation Unit Analyst | Compiling a real-time situational assessment during an unfolding multi-hazard event from a limited, vivid set of field reports; illusion of validity in the coherent-seeming picture, insensitivity to sample size in the limited field reports, authority bias toward a senior official's framing, availability bias from vivid recent reports (duplicate treated as single mechanism), framing effect in the situation report's presentation, hindsight bias in the after-action review | 86% | 19 | Moderate-High | Adds data-heavy/rapidly-changing information environment, team coordination, high-consequence operational context | APPROVED_WITH_CAVEATS (duplicate Availability Bias requires single-instance handling) |

***

## 2. Candidate occupation matrix

### Interview 1 (Curse of Knowledge)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Emergency Management Training Officer | 1 (Curse of Knowledge) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (briefing design phases) | High (change audience's actual background knowledge) | High | High (adds instructional design, public-facing context) | 0.88 |
| Local Emergency Manager | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.58 |
| Public Information Officer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.55 |
| Incident Commander | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.52 |
| Meteorological Forecaster | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Low (overlaps with Interview 4) | 0.42 |

**Selected:** Emergency Management Training Officer (best coverage, distinctness, diversity fit; curse of knowledge is the natural core mechanism of expert-to-novice instructional design).

***

### Interview 2 (Mere Exposure, Picture Superiority)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Public Information Officer (Emergency/Crisis Communications) | 2 (Mere Exposure, Picture Superiority) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (campaign design phases) | High (change warning message effectiveness data) | High | High (adds visual/communication design, public-facing context) | 0.90 |
| Training Officer | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| Exercise Planner | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.65 |
| Local Emergency Manager | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 3) | 0.50 |
| EOC Situation Analyst | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 7) | 0.48 |

**Selected:** Public Information Officer (best coverage, distinctness, diversity fit).

***

### Interview 3 (Bias Blind Spot, Normality Bias, Planning Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Local Emergency Manager (County/Municipal) | 3 (Bias Blind Spot, Normality Bias, Planning Fallacy) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (long-horizon plan review phases) | High (change actual recurrence likelihood data) | High | High (adds long-horizon planning, organizational-context) | 0.92 |
| Exercise Planner | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 6) | 0.76 |
| Incident Commander | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.60 |
| Training Officer | 1 | 1 | 1 | 0 | 67% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.55 |
| Meteorological Forecaster | 0 | 1 | 2 | 0 | 33% | Low | High | High | High | Low (overlaps with Interview 4) | 0.42 |

**Selected:** Local Emergency Manager (best coverage, distinctness, diversity fit; grounded directly in disaster-preparedness bias literature on normalcy/normalization bias). [preventionweb](https://www.preventionweb.net/hubs/disaster-risk-communication-hub/understand/cognitive-biases)

***

### Interview 4 (Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Bandwagon Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Meteorological Hazard Forecaster (Emergency Support Function) | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (forecast/warning decision phases) | High (change ensemble model sample validity) | High | High (adds technical/data-heavy forecasting, hierarchy context) | 0.94 |
| EOC Situation Analyst | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Incident Commander | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 5) | 0.70 |
| Local Emergency Manager | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.62 |
| Public Information Officer | 1 | 2 | 1 | 0 | 75% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.55 |

**Selected:** Meteorological Hazard Forecaster (best coverage, distinctness, diversity fit; well-grounded in probabilistic-forecasting bias literature).

***

### Interview 5 (Framing Effect, Hindsight Bias, Bandwagon Effect, Anchoring Bias, Confirmation Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Incident Commander (Structural Fire/Hazmat Response) | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (rapid field command phases) | High (change initial size-up accuracy) | High | High (adds high-time-pressure field command, team coordination context) | 0.95 |
| EOC Situation Analyst | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.82 |
| Meteorological Forecaster | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 4) | 0.74 |
| Local Emergency Manager | 2 | 2 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.65 |
| Public Information Officer | 2 | 1 | 2 | 0 | 60% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.52 |

**Selected:** Incident Commander (best coverage, distinctness, scenario richness; directly grounded in crisis decision-making bias research on framing, anchoring, and confirmation bias). [pure.tudelft](https://pure.tudelft.nl/ws/files/134568595/1_s2.0_S2212420922005982_main.pdf)

***

### Interview 6 (Curse of Knowledge, Mere Exposure, Picture Superiority, Bias Blind Spot, Normality Bias, Planning Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Emergency Preparedness Curriculum Designer / Exercise Planner | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms across design phases) | High (exercise design, materials creation, timeline phases) | High (change scenario severity realism data) | High | High (adds instructional design, long-horizon planning context) | 0.96 |
| Training Officer | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 1) | 0.82 |
| Local Emergency Manager | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 3) | 0.74 |
| Public Information Officer | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.68 |
| Incident Commander | 2 | 2 | 2 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.58 |

**Selected:** Emergency Preparedness Curriculum Designer / Exercise Planner (best coverage, distinctness, diversity fit; all six biases map cleanly onto distinct stages of the exercise-design workflow).

***

### Interview 7 (Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Availability Bias x2, Framing Effect, Hindsight Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Emergency Operations Center (EOC) Situation Unit Analyst | 5 (Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Availability Bias, Framing Effect) | 1 (Hindsight Bias) | 0 | 0 | 100% | Moderate-High (duplicate Availability Bias treated as one mechanism) | High (real-time situational assessment phases) | High (change field report representativeness) | High | High (adds data-heavy/rapidly-changing, team-coordination context) | 0.88 |
| Meteorological Forecaster | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.78 |
| Incident Commander | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.76 |
| Local Emergency Manager | 3 | 2 | 1 | 0 | 71% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.68 |
| Public Information Officer | 3 | 2 | 1 | 0 | 71% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.64 |

**Selected:** EOC Situation Unit Analyst (best diversity fit, adds real-time information-synthesis role; duplicate Availability Bias requires single-instance handling).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Curse of Knowledge
- **Selected occupation:** Emergency Management Training Officer
- **Role and setting:** Instructional design role within a fire department, county emergency management agency, or state training academy; develops public-facing evacuation briefings, training materials, and community preparedness guidance, drawing on years of technical hazard expertise.
- **Why this occupation fits the bias list:** Training officers with deep technical expertise routinely design communications for lay audiences. Curse of knowledge — the difficulty of imagining what it is like not to know something one already knows, leading to omission of steps that feel "obvious" — is a natural and distinct mechanism when translating expert hazard knowledge into a public evacuation briefing.
- **Primary CTA scenario:** Designing a public evacuation briefing after years of technical expertise, unintentionally omitting steps that seem obvious; curse of knowledge in assuming audience shares the officer's background understanding.
- **Triggering event:** A training officer is asked to revise the county's flood evacuation briefing script after a post-exercise survey reveals residents were confused about which routes to use, despite the officer having delivered this briefing dozens of times using terminology and assumptions that feel self-evident.
- **Decision episodes:**
  1. Initial draft of the briefing script based on the officer's established mental model of the evacuation process.
  2. Review of the confused survey responses and consideration of what may have been unclear.
  3. Attempt to identify which steps or terms were assumed rather than explained.
  4. Final revision decision and script sign-off.
- **Available cues and evidence:** The original briefing script, the confused survey responses and specific points of confusion, the officer's own technical understanding of the evacuation zones and terminology, a colleague's unfamiliar-audience read-through (if solicited).
- **Competing interpretations:** The confusion reflects genuinely unclear or assumed-knowledge content in the script vs. reflects inattentive audience members unrelated to script clarity; the officer's technical framing is accessible to a general audience vs. relies on background knowledge the audience does not share.
- **Plausible actions:** Revise the script to explicitly define previously assumed terms and steps; leave the script unchanged and attribute confusion to audience attentiveness; pilot-test a revised script with a naive reader before finalizing; add supplementary visual aids without changing the core script.
- **Constraints and pressures:** Publication deadline for the updated briefing materials, limited access to genuinely naive test audiences, the officer's confidence in their own established communication approach.
- **Consequences of error:** Continued public confusion during a real evacuation, potentially delaying compliance or causing residents to take incorrect routes.
- **Counterfactual causal variable:** Actual point of confusion in the original script (later found to be a specific technical term the officer had never considered unclear, rather than the audience's general inattentiveness).
- **Expected interview structure:** Opening (training officer role context), Episode 1 (initial draft), Episode 2 (survey review), Episode 3 (gap identification), Closing (reflection on the assumption of shared understanding).
- **Natural biases:** Curse of Knowledge.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Exercise Planner (would overlap with Interview 6; curse of knowledge is plausible there but reserved for the more complex six-bias exercise-design scenario).
- **Rejected alternative occupation 2:** Local Emergency Manager (less naturally isolated from the plan-review mechanisms already assigned to that role in Interview 3).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Mere Exposure, Picture Superiority
- **Selected occupation:** Public Information Officer (Emergency/Crisis Communications)
- **Role and setting:** Communications role within an emergency management agency; designs public warning messages, selects visual and textual formats for alerts, coordinates with media outlets, works under recurring campaign cycles for seasonal hazards.
- **Why this occupation fits the bias list:** Public information officers repeatedly select and reuse warning templates and visual formats across campaigns. Mere exposure — favoring a familiar visual template or message format simply because of repeated past use, independent of its actual effectiveness — and picture superiority — choosing image-based warnings over text-based ones because images are more memorable, even when a text format might convey the specific risk more accurately — are both natural, distinct mechanisms in this recurring communications-design context.
- **Primary CTA scenario:** Selecting a warning graphic and repeated message format for a public alert campaign; mere exposure in favoring a familiar visual template, picture superiority in choosing image-based over text-based warnings.
- **Triggering event:** Ahead of hurricane season, a public information officer must finalize the warning graphic and message format for this year's evacuation alert campaign, choosing between the agency's long-used graphic template and a newly proposed, more precise but less visually striking text-based format.
- **Decision episodes:**
  1. Initial review of the long-used graphic template and the newly proposed text-based alternative.
  2. Consideration of which format has historically felt more effective, based on familiarity with the existing template.
  3. Evaluation of which format is more memorable versus which conveys the specific risk information more precisely.
  4. Final selection and sign-off for the campaign.
- **Available cues and evidence:** The long-used graphic template and its history of repeated use, the newly proposed text-based format and its more precise risk information, any available data on past campaign recall or compliance, stakeholder preferences.
- **Competing interpretations:** The familiar template is preferred because it is genuinely more effective vs. simply because of repeated past exposure; the image-based format is more memorable and thus more effective vs. the text-based format's greater precision better serves the actual warning purpose.
- **Plausible actions:** Retain the long-used graphic template; adopt the new text-based format; combine elements of both; commission a comparative test before deciding.
- **Constraints and pressures:** Campaign launch deadline, limited testing budget, media partner familiarity with the existing template, agency branding consistency expectations.
- **Consequences of error:** A warning format that is memorable but imprecise, leading to inadequate public understanding of the specific required action, or a precise but unmemorable format that fails to capture attention.
- **Counterfactual causal variable:** Actual comparative effectiveness of the two formats in prompting correct evacuation behavior (later found that the less visually memorable text format produced measurably better compliance due to its specificity).
- **Expected interview structure:** Opening (PIO role context), Episode 1 (initial format review), Episode 2 (familiarity consideration), Episode 3 (memorability vs. precision evaluation), Closing (reflection on the basis for the final selection).
- **Natural biases:** Mere Exposure, Picture Superiority.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Training Officer (overlaps with Interview 1; picture superiority is plausible in materials design but mere exposure is less naturally tied to a one-off briefing-revision task).
- **Rejected alternative occupation 2:** Exercise Planner (overlaps with Interview 6; both mechanisms already assigned there in a more complex six-bias scenario-design context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Bias Blind Spot, Normality Bias, Planning Fallacy
- **Selected occupation:** Local Emergency Manager (County/Municipal Level)
- **Role and setting:** Jurisdictional emergency management role; maintains and periodically updates the county or municipal hazard mitigation and response plan, coordinates with multiple agencies, works on multi-year planning cycles between major events.
- **Why this occupation fits the bias list:** Emergency managers periodically review long-standing hazard plans during quiet periods between major events, a context well-documented in disaster-preparedness literature for underestimating recurrence likelihood (normality bias — the tendency to believe things will continue functioning the way they normally have, underestimating disaster likelihood and impact) and for underestimating timeline and resource needs (planning fallacy). Bias blind spot (perceiving one's own judgment as less biased than others') is naturally embedded when the manager evaluates a peer jurisdiction's plan more critically than their own. [preventionweb](https://www.preventionweb.net/hubs/disaster-risk-communication-hub/understand/cognitive-biases)
- **Primary CTA scenario:** Reviewing the jurisdiction's hazard mitigation plan years after the last major event; bias blind spot in reviewing peer jurisdictions' plans more critically than one's own, normality bias in underestimating recurrence likelihood, planning fallacy in timeline/resource estimates for plan implementation.
- **Triggering event:** Ten years after the county's last major flood, the emergency manager conducts the mandated five-year plan update, drawing comparisons with a neighboring county's recently revised plan while estimating the timeline and resources needed to implement updated mitigation measures.
- **Decision episodes:**
  1. Initial review of the current plan against the long quiet period since the last major event.
  2. Comparative review of the neighboring county's plan, evaluating its assumptions and gaps.
  3. Estimation of the timeline and resources required to implement proposed updates to the local plan.
  4. Final plan revision decision and submission for approval.
- **Available cues and evidence:** The current plan's assumptions and last-updated risk estimates, ten years of relatively quiet hazard activity, the neighboring county's plan and its stated assumptions, historical timeline data from past mitigation projects, budget and staffing constraints.
- **Competing interpretations:** The ten-year quiet period indicates genuinely reduced risk vs. reflects normal variability that does not change the underlying hazard probability; the neighboring county's plan has notable gaps vs. the manager's own plan may share similar, unexamined gaps; the proposed implementation timeline is realistic vs. underestimates the coordination and approval steps historically required.
- **Plausible actions:** Maintain current risk estimates and mitigation priorities; revise risk estimates upward despite the quiet period; adopt a longer, more conservative implementation timeline; commission an independent review of the local plan's own assumptions.
- **Constraints and pressures:** Mandated review deadline, budget cycle for mitigation funding, political pressure to avoid alarming risk revisions without recent events, staffing limitations.
- **Consequences of error:** Continued underestimation of hazard likelihood leaving the jurisdiction under-prepared, or an unrealistic implementation timeline delaying actual mitigation work once approved.
- **Counterfactual causal variable:** Actual underlying hazard recurrence probability (later found, through updated hydrological modeling, to be unchanged or higher despite the ten quiet years).
- **Expected interview structure:** Opening (emergency manager role context), Episode 1 (current plan review), Episode 2 (peer comparison), Episode 3 (timeline estimation), Closing (reflection on how the quiet period and peer comparison shaped the review).
- **Natural biases:** Bias Blind Spot, Normality Bias, Planning Fallacy.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Exercise Planner (overlaps with Interview 6; normality bias and planning fallacy already assigned there in a scenario-design rather than plan-review context).
- **Rejected alternative occupation 2:** Incident Commander (overlaps with Interview 5; bias blind spot is plausible in after-action contexts but less naturally tied to a multi-year planning cycle).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Bandwagon Effect
- **Selected occupation:** Meteorological Hazard Forecaster (Emergency Support Function)
- **Role and setting:** Technical forecasting role supporting emergency management operations; interprets weather model output (including ensemble forecasts) to issue or recommend severe weather warnings, works within a forecast-office hierarchy and coordinates with neighboring offices.
- **Why this occupation fits the bias list:** Forecasters interpret probabilistic model output where illusion of validity (a small ensemble producing a coherent-looking pattern that feels more reliable than its actual statistical basis warrants) and insensitivity to sample size (treating a small ensemble run with the same confidence as a larger one) are well-documented statistical-reasoning mechanisms. Authority bias (deferring to a senior forecaster's call despite independent data) and bandwagon effect (matching a warning because neighboring forecast offices have issued similar warnings) are both natural in the hierarchical, coordinated structure of operational forecasting.
- **Primary CTA scenario:** Issuing a severe weather warning based on a limited ensemble model run and a directive from a senior forecaster; illusion of validity in trusting the coherent-looking forecast pattern, insensitivity to sample size in the small ensemble, authority bias toward the senior forecaster's call, bandwagon effect from other forecast offices' matching warnings.
- **Triggering event:** A forecaster reviews a small, six-member ensemble model run that shows a coherent, consistent severe-weather track; a senior forecaster has already indicated they favor issuing a warning, and two neighboring forecast offices have just issued similar warnings for adjacent areas.
- **Decision episodes:**
  1. Initial review of the ensemble output and its apparent coherence.
  2. Consideration of the ensemble's actual sample size and statistical reliability.
  3. Weighing the senior forecaster's stated preference against independent analysis.
  4. Final warning decision, informed also by the neighboring offices' matching warnings.
- **Available cues and evidence:** The six-member ensemble run and its member-to-member agreement, the ensemble's actual statistical confidence interval, the senior forecaster's stated preference, the neighboring offices' warning decisions and their independent basis, historical false-alarm rate for this pattern type.
- **Competing interpretations:** The ensemble's coherence indicates a reliable forecast vs. is an artifact of a small sample that could differ substantially with more members; the senior forecaster's call reflects superior judgment vs. should be independently verified; the neighboring offices' warnings indicate a genuine regional threat vs. reflect their own independent (and possibly also biased) analyses.
- **Plausible actions:** Issue the warning consistent with the ensemble, senior forecaster, and neighboring offices; request a larger ensemble run before deciding; issue a lower-confidence advisory instead of a full warning; independently verify against additional data sources.
- **Constraints and pressures:** Time pressure to issue warnings ahead of the approaching system, deference norms within the forecast-office hierarchy, coordination expectations with neighboring offices, public safety stakes of over- or under-warning.
- **Consequences of error:** A false-alarm warning eroding public trust and future compliance, or a missed/delayed warning for a genuine severe-weather threat.
- **Counterfactual causal variable:** Actual statistical reliability of the six-member ensemble (later found that a full 30-member ensemble run, available shortly after, showed a much less consistent track).
- **Expected interview structure:** Opening (forecaster role context), Episode 1 (ensemble review), Episode 2 (sample size consideration), Episode 3 (hierarchy and peer-office weighing), Closing (reflection on the basis for the final warning decision).
- **Natural biases:** Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Bandwagon Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** EOC Situation Analyst (overlaps with Interview 7; illusion of validity and insensitivity to sample size already assigned there in a field-report rather than model-ensemble context).
- **Rejected alternative occupation 2:** Incident Commander (overlaps with Interview 5; authority bias and bandwagon effect already assigned there in a field-command rather than forecasting context).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Framing Effect, Hindsight Bias, Bandwagon Effect, Anchoring Bias, Confirmation Bias
- **Selected occupation:** Incident Commander (Structural Fire/Hazmat Response)
- **Role and setting:** Field command role at the scene of an active structural fire or hazmat incident; makes rapid tactical decisions (interior attack, defensive posture, evacuation) based on initial size-up and evolving radio reports, holds ultimate on-scene decision authority, operates under extreme time pressure.
- **Why this occupation fits the bias list:** Incident commanders make rapid go/no-go decisions under severe time pressure and incomplete information, a context extensively documented in crisis decision-making bias research for anchoring bias (the initial size-up report disproportionately shaping subsequent judgment), confirmation bias (interpreting ambiguous subsequent radio traffic as consistent with the initial assessment), framing effect (how risk is verbally framed over the radio affecting the perceived urgency of the decision), bandwagon effect (other units' actions influencing the commander's own tactical choice), and hindsight bias (in the after-action review of the decision once the outcome is known). [pure.tudelft](https://pure.tudelft.nl/ws/files/134568595/1_s2.0_S2212420922005982_main.pdf)
- **Primary CTA scenario:** Making a go/no-go decision on interior attack during an active structural fire based on initial size-up information; framing effect in how risk is presented over radio, hindsight bias in after-action review, bandwagon effect from other units' actions, anchoring bias on the initial size-up report, confirmation bias in interpreting subsequent radio traffic.
- **Triggering event:** An incident commander arrives at a structural fire and receives an initial size-up report from the first-arriving officer describing "moderate smoke, contained to one room"; minutes later, additional units begin an interior attack based on this framing, and subsequent radio traffic includes an ambiguous report that could indicate either a contained situation or a developing structural hazard.
- **Decision episodes:**
  1. Initial size-up report and formation of the commander's working mental model of the fire's severity.
  2. Observation of other units beginning interior attack, and the commander's own tactical decision in that context.
  3. Interpretation of the ambiguous subsequent radio report in light of the initial size-up.
  4. Final tactical decision (continue interior attack, order withdrawal, or reassess) and later after-action review of the decision.
- **Available cues and evidence:** The initial size-up report and its specific framing language, other units' observed actions, the ambiguous subsequent radio report, smoke and structural conditions visible from the command post, historical patterns for similar-sounding incidents.
- **Competing interpretations:** The initial size-up accurately reflects the fire's severity vs. was an early, incomplete assessment that should be revised; other units' interior attack indicates it is safe to continue vs. reflects their own anchoring on the same initial report; the ambiguous radio report confirms the situation is contained vs. indicates a developing hazard that contradicts the initial framing.
- **Plausible actions:** Continue the interior attack as initially framed; order an immediate withdrawal pending clarification; request additional size-up information before deciding; escalate to defensive operations.
- **Constraints and pressures:** Extreme time pressure, firefighter safety stakes, incomplete and rapidly evolving information, the visible commitment of other units already engaged in interior attack.
- **Consequences of error:** Continued interior attack into a genuinely developing structural collapse or flashover hazard, or an unnecessary withdrawal from a situation that was in fact contained, delaying suppression and increasing property loss.
- **Counterfactual causal variable:** Actual structural condition at the time of the decision (later found, through post-incident analysis, to have already been deteriorating in a way not evident from the size-up report or the ambiguous radio traffic).
- **Expected interview structure:** Opening (commander role context), Episode 1 (initial size-up and anchor), Episode 2 (other units' actions), Episode 3 (ambiguous report interpretation), Episode 4 (final decision), Closing (reflection during after-action review).
- **Natural biases:** Framing Effect, Bandwagon Effect, Anchoring Bias, Confirmation Bias.
- **Plausible but difficult biases:** Hindsight Bias (requires the after-action review to be a clearly separate, later episode distinct from the in-the-moment decision, to avoid the bias being read simply as "the outcome was bad").
- **Biases that should not be forced:** None outright, but Hindsight Bias must be embedded in an explicit later review episode, not inferred from the outcome itself.
- **Rejected alternative occupation 1:** EOC Situation Analyst (overlaps with Interview 7; framing effect and hindsight bias already assigned there in a strategic rather than tactical field-command context).
- **Rejected alternative occupation 2:** Meteorological Forecaster (overlaps with Interview 4; bandwagon effect and authority-adjacent mechanisms already assigned there in a forecasting rather than field-command context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Curse of Knowledge, Mere Exposure, Picture Superiority, Bias Blind Spot, Normality Bias, Planning Fallacy
- **Selected occupation:** Emergency Preparedness Curriculum Designer / Exercise Planner
- **Role and setting:** Specialized instructional and planning role within an emergency management training division; designs full-scale disaster exercises and training curricula, drawing on both technical expertise and prior exercise materials, works on long design cycles with organizational review and approval.
- **Role and setting (continued):** Coordinates with multiple participating agencies and evaluates exercise realism against past incident data.
- **Why this occupation fits the bias list:** Exercise planners combine deep technical expertise (curse of knowledge in designing scenario complexity that assumes participant background knowledge), reuse of familiar formats (mere exposure in defaulting to past exercise structures), reliance on vivid incident imagery (picture superiority in scenario materials), self-assessment of design objectivity (bias blind spot), assumptions about disaster severity based on organizational routine (normality bias in underestimating how severe a realistic exercise scenario should be), and long-cycle scheduling (planning fallacy in exercise timeline estimation). All six mechanisms map cleanly onto distinct stages of the exercise-design workflow.
- **Primary CTA scenario:** Designing a full-scale disaster exercise scenario after years of specialized expertise, drawing heavily on familiar past exercise formats and vivid past-incident imagery; curse of knowledge in scenario complexity, mere exposure in reusing familiar exercise formats, picture superiority in scenario materials, bias blind spot in self-assessing objectivity, normality bias in underestimating the exercise's realistic severity, planning fallacy in exercise timeline.
- **Triggering event:** An exercise planner begins designing next year's full-scale regional disaster exercise, drawing on the same basic exercise format used for the past five years, illustrated with vivid imagery from a past real incident, while estimating a timeline for design and stakeholder approval that mirrors past cycles.
- **Decision episodes:**
  1. Initial scenario complexity design, drawing on the planner's own technical expertise.
  2. Selection of the exercise format, defaulting to the familiar structure used in prior years.
  3. Selection of scenario materials, favoring vivid imagery from a memorable past incident over less visually striking but more representative data.
  4. Self-assessment of the design's objectivity and severity realism, and estimation of the design-to-approval timeline.
- **Available cues and evidence:** The planner's technical expertise and its assumptions about participant background knowledge, the five years of prior exercise formats and their outcomes, the vivid past-incident imagery and its actual representativeness of likely future scenarios, historical design-to-approval timelines, peer planners' independent assessments (if solicited).
- **Competing interpretations:** The scenario complexity is appropriately calibrated for participants vs. assumes background knowledge participants do not have; the familiar exercise format remains the best choice vs. is simply the most repeated one; the vivid imagery accurately represents realistic severity vs. is memorable but statistically unrepresentative; the planner's own design is appropriately objective vs. shares the same blind spots the planner would readily identify in a peer's design; the estimated timeline is realistic vs. underestimates coordination and approval steps.
- **Plausible actions:** Proceed with the familiar format and current scenario complexity; commission an independent review of the scenario's assumptions and severity calibration; select scenario materials based on statistical representativeness rather than visual memorability; build a longer timeline buffer based on past actual (versus estimated) cycles.
- **Constraints and pressures:** Multi-agency coordination requirements, budget and scheduling constraints, the planner's professional investment in established formats, organizational expectations for exercise realism.
- **Consequences of error:** An exercise that fails to adequately challenge or prepare participants due to unexamined assumptions, unrepresentative severity calibration, or an unrealistic timeline delaying the exercise's actual execution.
- **Counterfactual causal variable:** Actual representativeness of the vivid past-incident imagery relative to the range of plausible future scenarios (later found to substantially underrepresent a more statistically likely but less memorable scenario type).
- **Expected interview structure:** Opening (exercise planner role context), Episode 1 (scenario complexity design), Episode 2 (format selection), Episode 3 (materials selection), Episode 4 (self-assessment and timeline estimation), Closing (reflection on the six-mechanism design process).
- **Natural biases:** Curse of Knowledge, Mere Exposure, Picture Superiority, Normality Bias, Planning Fallacy.
- **Plausible but difficult biases:** Bias Blind Spot (requires an explicit meta-cognitive comparison point — the planner assessing a peer's design more critically than their own — to avoid feeling merely asserted).
- **Biases that should not be forced:** None outright, but Bias Blind Spot must be grounded in an explicit comparative self-assessment moment.
- **Rejected alternative occupation 1:** Training Officer (overlaps with Interview 1; curse of knowledge already assigned there in a briefing-revision rather than exercise-design context).
- **Rejected alternative occupation 2:** Local Emergency Manager (overlaps with Interview 3; bias blind spot, normality bias, and planning fallacy already assigned there in a plan-review rather than exercise-design context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Availability Bias, Framing Effect, Hindsight Bias, Availability Bias
- **Selected occupation:** Emergency Operations Center (EOC) Situation Unit Analyst
- **Role and setting:** Information-synthesis role within an Emergency Operations Center; compiles real-time situational assessments from field reports, sensor data, and agency inputs during an unfolding multi-hazard event, briefs incident command and senior officials, works under rapidly changing, high-volume information conditions.
- **Why this occupation fits the bias list:** Situation unit analysts synthesize a limited, often vivid set of field reports into a coherent operational picture under time pressure — a context extensively documented in crisis information-management bias research for illusion of validity (a coherent-seeming picture from limited data feeling more reliable than warranted), insensitivity to sample size (treating a handful of field reports as representative of the full affected area), authority bias (deferring to a senior official's framing of the situation), availability bias (vivid, recent reports disproportionately shaping the assessment — the duplicate entry is treated as one mechanism, not two), framing effect (how the situation report is presented shaping downstream decisions), and hindsight bias (in the after-action review). [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC8938164/)
- **Primary CTA scenario:** Compiling a real-time situational assessment during an unfolding multi-hazard event from a limited, vivid set of field reports; illusion of validity in the coherent-seeming picture, insensitivity to sample size in the limited field reports, authority bias toward a senior official's framing, availability bias from vivid recent reports, framing effect in the situation report's presentation, hindsight bias in the after-action review.
- **Triggering event:** During an unfolding regional flooding event, an EOC situation analyst receives a handful of vivid, detailed field reports from one hard-hit area while most of the affected region remains unreported due to communications outages; a senior official has already suggested the situation is "under control," and the analyst must compile the situation report for the next command briefing.
- **Decision episodes:**
  1. Initial compilation of the available field reports into a working picture of the event.
  2. Consideration of how representative the vivid, available reports are of the full affected area.
  3. Reconciliation of the senior official's stated framing with the analyst's own read of the incoming data.
  4. Final situation report drafting and presentation, followed by later after-action review.
- **Available cues and evidence:** The available vivid field reports, the known extent of communications outages in unreported areas, the senior official's stated framing, historical patterns for similar-sounding events, any indirect indicators (e.g., satellite or sensor data) about the unreported areas.
- **Competing interpretations:** The available reports accurately represent the overall situation vs. reflect only the most severely affected, most vividly reported area while other areas remain unknown; the coherent picture assembled from limited data is reliable vs. an artifact of a small, non-representative sample; the senior official's framing reflects accurate situational awareness vs. should be independently verified against the analyst's own data read.
- **Plausible actions:** Present the situation report consistent with the vivid reports and senior official's framing; explicitly flag the unreported areas and the report's limited representativeness; seek additional indirect data sources before finalizing; present multiple scenarios reflecting the uncertainty.
- **Constraints and pressures:** Time pressure ahead of the command briefing, deference norms toward the senior official, communications outages limiting data availability, downstream reliance by incident command on the situation report.
- **Consequences of error:** A situation report that understates the severity or extent of the event in unreported areas, delaying appropriate resource allocation, or an overstated report based on unrepresentative vivid data causing resource misallocation.
- **Counterfactual causal variable:** Actual conditions in the unreported areas (later found, once communications were restored, to be substantially worse than the vivid but unrepresentative available reports suggested).
- **Expected interview structure:** Opening (situation analyst role context), Episode 1 (initial compilation), Episode 2 (representativeness consideration), Episode 3 (reconciliation with senior framing), Episode 4 (report drafting and later review), Closing (reflection on the six-mechanism reasoning process).
- **Natural biases:** Illusion of Validity, Insensitivity to Sample Size, Availability Bias, Framing Effect.
- **Plausible but difficult biases:** Authority Bias (requires an explicit hierarchical-deference cue distinct from simply agreeing with an accurate assessment), Hindsight Bias (requires a clearly separate, later after-action episode).
- **Biases that should not be forced:** A second, independent instance of Availability Bias (the list's duplicate should not be coded as two separate mechanisms).
- **Rejected alternative occupation 1:** Meteorological Forecaster (overlaps with Interview 4; illusion of validity and insensitivity to sample size already assigned there in a model-ensemble rather than field-report context).
- **Rejected alternative occupation 2:** Incident Commander (overlaps with Interview 5; framing effect and hindsight bias already assigned there in a tactical field-command rather than strategic situational-assessment context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (duplicate Availability Bias must be coded as one mechanism; Authority Bias and Hindsight Bias require explicit, distinct cues to avoid feeling forced)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (training officer, public information officer, local emergency manager, meteorological forecaster, incident commander, exercise planner, EOC situation analyst) | None | None | None | None needed |
| Work setting | Instructional/office (1, 6), Communications/public-facing (2), Long-horizon planning/office (3), Technical forecasting (4), Field command (5), EOC/office (7) | Instructional design (2/7: 1, 6) | Instructional design | Field/outdoor as primary, industrial/technical | None critical; Interviews 1 and 6 differ materially in scope (single briefing vs. full exercise) and bias complexity |
| Decision type | Communication/design (1, 2), Planning/risk assessment (3), Forecasting/warning issuance (4), Emergency response/command (5), Design/planning (6), Monitoring/situational assessment (7) | Design-type (3/7: 1, 2, 6) | Design/communication | Negotiation, Personnel management | None critical; reflects the domain's genuine emphasis on preparedness communication and design, balanced by field command (5) and technical forecasting (4) |
| Information environment | Perceptual/experiential (1, 2), Regulated/long-horizon (3), Data-heavy/probabilistic (4), Rapidly-changing/socially-mediated (5), Perceptual/organizational (6), Data-heavy/rapidly-changing (7) | Rapidly-changing (2/7: 5, 7) | Balanced | Rich/structured as primary driver | None critical; reflects the domain's inherent mix of quiet-period planning and acute-crisis information environments |
| Time pressure | Low/moderate (1, 3, 6), Moderate (2), High (4), Extreme (5), High (7) | Moderate (3/7) | Balanced | Very low | None critical; strong spread from low (plan review) to extreme (interior attack decision) |
| Consequence of error | Public understanding/safety (1, 2), Preparedness/resource (3), Public safety/warning accuracy (4), Immediate life-safety (5), Preparedness quality (6), Operational/resource allocation (7) | None significant | None | Financial-only, environmental | None critical; reflects the domain's inherent public-safety consequence profile at varying time horizons |
| Expertise level | Independent professional (1, 2), Senior practitioner/decision authority (3), Specialist/technical (4), Decision authority (5), Specialist/senior practitioner (6), Independent/specialist (7) | Senior practitioner (3/7: 3, 5, 6) | Senior practitioner | Developing practitioner | None critical; reflects that consequential bias-rich decisions in this domain often sit with experienced roles |
| Stakeholder pattern | Individual with public audience (1, 2), Individual with organizational context (3), Individual with hierarchy (4), Individual with team/command authority (5), Individual with organizational review (6), Individual with hierarchy/team (7) | None significant | None | Multi-party negotiation, one-to-one client | None critical |
| Scenario archetype | Briefing design (1), Warning-format selection (2), Plan review (3), Forecast/warning issuance (4), Interior-attack decision (5), Exercise design (6), Situational assessment (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Audience knowledge gap (1), Format effectiveness (2), Recurrence probability (3), Ensemble reliability (4), Structural condition (5), Scenario representativeness (6), Unreported-area conditions (7) | None significant | None | Equipment/technical hardware failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact appropriate to the domain |

**Overall assessment:** Strong diversity across occupations, settings, decision types, and time horizons, spanning quiet-period planning and design work (1, 2, 3, 6) through acute technical forecasting (4) and extreme-time-pressure field command (5) to real-time situational synthesis (7). Design/communication-type decisions recur across three interviews, which is expected given the domain's genuine emphasis on preparedness and public communication, but each instance differs materially in artifact, audience, and bias complexity. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Curse of Knowledge (clear mechanism: difficulty imagining audience's lack of background knowledge) | None | None | None | None | None | Show the officer's specific unexamined assumption explicitly; probe why the term/step felt self-evident, not just that confusion occurred |
| 2 | Mere Exposure (familiarity-driven preference), Picture Superiority (image-over-text preference) | Mere Exposure and Status Quo Bias (both involve preference for the familiar/existing option, though mere exposure specifically concerns repeated passive exposure) | None | None | None | None | Show the officer's reasoning citing familiarity itself as a justification, distinct from a reasoned effectiveness argument; separate the image/text memorability judgment from the format-familiarity judgment |
| 3 | Bias Blind Spot (self vs. peer double standard), Normality Bias (recurrence underestimation), Planning Fallacy (timeline underestimation) | Normality Bias and Optimism Bias (closely related; normality bias specifically concerns assuming continuity of normal conditions rather than general positive outlook) | None | None | Bias Blind Spot (must show an explicit self-vs-peer comparison, not just confidence in one's own judgment) | Bias Blind Spot | Show the manager explicitly critiquing the neighboring county's plan for a flaw shared by their own, unexamined plan; separate the quiet-period reasoning (normality bias) from the timeline estimation (planning fallacy) as distinct episodes |
| 4 | Illusion of Validity, Insensitivity to Sample Size, Authority Bias, Bandwagon Effect (four distinct) | Illusion of Validity and Insensitivity to Sample Size (closely related — illusion of validity concerns the subjective feeling of reliability from a coherent pattern, insensitivity to sample size concerns the specific statistical reasoning error) | None | None | None | None | Show the ensemble's coherence explicitly as the source of confidence, separate from an explicit (mis)statement or disregard of the sample size; separate authority-deference from peer-office bandwagon as distinct cues |
| 5 | Framing Effect, Bandwagon Effect, Anchoring Bias, Confirmation Bias (four distinct); Hindsight Bias (requires separate later episode) | Anchoring Bias and Confirmation Bias (closely related — anchoring sets the initial reference point, confirmation bias is the subsequent selective interpretation), Hindsight Bias and outcome bias (must be separated from the outcome itself) | Hindsight Bias | Hindsight Bias | None | Hindsight Bias | Ensure the after-action review is a distinct, later episode with the commander reflecting knowing the outcome, separate from the in-the-moment decision episodes; show the initial size-up's specific framing language distinctly from the later ambiguous-report interpretation |
| 6 | Curse of Knowledge, Mere Exposure, Picture Superiority, Normality Bias, Planning Fallacy (five distinct); Bias Blind Spot (requires explicit comparative moment) | Mere Exposure and Status Quo Bias (as in Interview 2), Curse of Knowledge and Illusion of Understanding (both involve overestimating shared/accurate understanding, though curse of knowledge specifically concerns the communicator's inability to un-know something) | None | None | Bias Blind Spot (must show explicit self-vs-peer comparison, as in Interview 3, but in a design rather than plan-review context) | Bias Blind Spot | Distribute the six biases across the four distinct design episodes; show the planner explicitly comparing their own design's objectivity favorably against a peer's design to ground Bias Blind Spot |
| 7 | Illusion of Validity, Insensitivity to Sample Size, Availability Bias, Framing Effect (four cleanly distinguishable); Authority Bias, Hindsight Bias (require explicit distinct cues) | Illusion of Validity and Insensitivity to Sample Size (as in Interview 4), Availability Bias and Illusion of Validity (both involve overweighting vivid, available information as more reliable than warranted) | Hindsight Bias | Hindsight Bias | Authority Bias (must show explicit deference to the official's rank/position, not just agreement with an accurate framing) | Authority Bias, Hindsight Bias | Treat the duplicate Availability Bias entry as one mechanism; show the analyst's explicit deference to the senior official's framing based on rank rather than independent verification; ensure the after-action review is a distinct, later episode for Hindsight Bias |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interviews 3 and 6, ground Bias Blind Spot in an explicit, comparative self-vs-peer moment rather than mere confidence in one's own judgment. For Interviews 5 and 7, ensure Hindsight Bias is embedded in a clearly separate, later after-action-review episode, distinct from the in-the-moment decision, to avoid being read as ordinary outcome bias. For Interview 7, generate exactly one underlying Availability Bias mechanism despite the duplicate list entry, and ground Authority Bias in explicit rank-based deference rather than simple agreement with an accurate assessment.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing closely related neighboring pairs identified above (Illusion of Validity/Insensitivity to Sample Size in Interviews 4 and 7; Anchoring/Confirmation Bias in Interview 5; Mere Exposure/Status Quo Bias in Interviews 2 and 6). Flag any bias supported only by the case's ultimate outcome rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
