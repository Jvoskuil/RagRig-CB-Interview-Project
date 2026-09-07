This confirms the bias cluster (contextual bias, confirmation bias, coherence-based reasoning) is strongly associated with forensic examination roles specifically. This grounds several occupation choices.

## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Patrol Officer (Field Response) | Responding to a domestic disturbance call where the initial dispatch description omits a key detail present at the scene; feature positive effect in weighting presented cues over absent ones | 100% | 3 | High | Adds field-based, individual rapid-response, low-procedural-structure context | APPROVED |
| 2 | 2 | Latent Fingerprint Examiner | Comparing a latent print to a suspect exemplar after being told the suspect confessed; contextual bias from case information, coherence-based reasoning explaining away discrepancies | 100% | 6 | High | Adds forensic laboratory, technical/perceptual comparison, individual analytic context | APPROVED |
| 3 | 3 | Homicide Detective | Reviewing a cold case file years later and reassessing the original suspect theory with a squad review board; cognitive dissonance after committing to a theory, recency effects from the most recent tip, groupthink in review board consensus | 100% | 9 | High | Adds long-horizon investigation, team review, moderate-structure context | APPROVED |
| 4 | 4 | DNA Forensic Analyst | Interpreting a low-template/mixed DNA profile after being told the case involves a high-profile suspect; confirmation bias and asymmetrical skepticism toward supporting vs. contradicting data, feature positive effect in allele call weighting, contextual bias from case information, coherence-based reasoning in profile interpretation | 100% | 12 | High | Adds forensic laboratory, data-heavy/quantified, individual technical context | APPROVED |
| 5 | 5 | Internal Affairs Investigator | Investigating a use-of-force complaint against a colleague after publicly stating an initial assessment; cognitive dissonance in defending the stated position, recency effects from the most recent witness statement, groupthink in unit consensus, confirmation bias and asymmetrical skepticism toward the officer's account vs. complainant's account | 100% | 15 | High | Adds internal accountability, one-to-one interview, organizational/political-pressure context | APPROVED |
| 6 | 6 | Polygraph Examiner / Interview Specialist | Assessing a suspect's truthfulness in an interrogation after reviewing a case file suggesting guilt; contextual bias from file information, coherence-based reasoning in interpreting responses, cognitive dissonance after committing to a guilt assessment, feature positive effect in reading presented behavioral cues, groupthink in debrief with investigating team (duplicate Groupthink treated as single mechanism) | 100% | 18 | High | Adds one-to-one interview, socially-mediated/perceptual, individual-with-team-debrief context | APPROVED_WITH_CAVEATS (duplicate Groupthink in list requires single-instance handling) |
| 7 | 7 | Crime Scene Investigator (CSI) / Forensic Scene Examiner | Processing a crime scene after being briefed on the responding officers' working theory of what happened; feature positive effect in evidence documentation, contextual bias from officer briefing, coherence-based reasoning in scene narrative construction, cognitive dissonance after committing to initial scene interpretation, recency effects from the last item processed, confirmation bias and asymmetrical skepticism toward theory-supporting vs. contradicting evidence (duplicate treated as single mechanism across two episodes) | 86% | 19 | Moderate-High | Adds field forensic, technical/perceptual, individual-in-team-context, evidence-chain consequence profile | APPROVED_WITH_CAVEATS (duplicate Confirmation Bias/Asymmetrical Skepticism requires two-episode separation) |

***

## 2. Candidate occupation matrix

### Interview 1 (Feature Positive Effect)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Patrol Officer (Field Response) | 1 (Feature Positive Effect) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (rapid multi-phase field response) | High (change presence/absence of the omitted detail) | High | High (adds field-based, individual, low-procedure context) | 0.88 |
| Latent Fingerprint Examiner | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.58 |
| Crime Scene Investigator | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Low (overlaps with Interview 7) | 0.72 |
| Homicide Detective | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.55 |
| DNA Forensic Analyst | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.52 |

**Selected:** Patrol Officer (Field Response) (best coverage, distinctness, diversity fit; reserves the forensic feature-positive mechanism for Interview 7's more complex scenario).

***

### Interview 2 (Contextual Bias, Coherence-based Reasoning/Rationalisation)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Latent Fingerprint Examiner | 2 (Contextual, Coherence-based) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (comparison phases, verification) | High (change case information provided) | High | High (adds forensic lab, technical comparison role) | 0.90 |
| DNA Forensic Analyst | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 4) | 0.72 |
| Homicide Detective | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.65 |
| Crime Scene Investigator | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 7) | 0.62 |
| Patrol Officer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.48 |

**Selected:** Latent Fingerprint Examiner (best coverage, distinctness, diversity fit; grounded directly in forensic-science bias literature). [assets.publishing.service.gov](https://assets.publishing.service.gov.uk/media/5f4fc26ce90e074695f80977/217_FSR-G-217_Cognitive_bias_appendix_Issue_2.pdf)

***

### Interview 3 (Cognitive Dissonance, Recency Effects, Groupthink)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Homicide Detective | 3 (Cognitive Dissonance, Recency, Groupthink) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (cold-case review phases, team review) | High (change accuracy of the recent tip) | High | High (adds long-horizon investigation, team review context) | 0.92 |
| Internal Affairs Investigator | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| Polygraph Examiner | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.68 |
| Patrol Officer | 1 | 1 | 1 | 0 | 67% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 1) | 0.55 |
| DNA Forensic Analyst | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.58 |

**Selected:** Homicide Detective (best coverage, distinctness, diversity fit).

***

### Interview 4 (Confirmation Bias/Asymmetrical Skepticism, Feature Positive Effect, Contextual Bias, Coherence-based Reasoning)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| DNA Forensic Analyst | 4 (all) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (profile interpretation phases, quantified data) | High (change case information/suspect identity disclosure) | High | High (adds data-heavy, quantified, technical role) | 0.94 |
| Latent Fingerprint Examiner | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 2) | 0.78 |
| Crime Scene Investigator | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.76 |
| Homicide Detective | 2 | 2 | 0 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.68 |
| Polygraph Examiner | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.62 |

**Selected:** DNA Forensic Analyst (best coverage, distinctness, diversity fit; four biases map cleanly onto distinct stages of DNA profile interpretation with quantified, structured data unlike the more perceptual fingerprint role). [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319185/)

***

### Interview 5 (Cognitive Dissonance, Recency Effects x2, Groupthink, Confirmation Bias/Asymmetrical Skepticism)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Internal Affairs Investigator | 4 (Cognitive Dissonance, Recency, Groupthink, Confirmation/Asymmetrical Skepticism) | 0 | 0 | 0 | 100% | High (four distinct mechanisms; duplicate Recency treated as one) | High (interview phases, public-statement pressure) | High (change accuracy of most recent witness statement) | High | High (adds internal accountability, organizational-pressure context) | 0.94 |
| Homicide Detective | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 3) | 0.80 |
| Polygraph Examiner | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 6) | 0.76 |
| DNA Forensic Analyst | 2 | 2 | 0 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.68 |
| Crime Scene Investigator | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.62 |

**Selected:** Internal Affairs Investigator (best coverage, distinctness, diversity fit; unique organizational/political-pressure and public-commitment dynamic not represented elsewhere).

***

### Interview 6 (Contextual Bias, Coherence-based Reasoning, Cognitive Dissonance, Feature Positive Effect, Groupthink x2)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Polygraph Examiner / Interview Specialist | 5 (Contextual, Coherence-based, Cognitive Dissonance, Feature Positive, Groupthink) | 0 | 0 | 0 | 100% | High (five distinct mechanisms; duplicate Groupthink treated as one) | High (interrogation phases, team debrief) | High (change case file guilt-suggestion accuracy) | High | High (adds one-to-one interview, socially-mediated role) | 0.92 |
| Homicide Detective | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 3) | 0.80 |
| Internal Affairs Investigator | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 5) | 0.76 |
| Crime Scene Investigator | 3 | 2 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 7) | 0.70 |
| Latent Fingerprint Examiner | 3 | 1 | 1 | 0 | 80% | Moderate-High | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.65 |

**Selected:** Polygraph Examiner / Interview Specialist (best coverage, distinctness, diversity fit; introduces a socially-mediated, one-to-one interview role not otherwise represented).

***

### Interview 7 (Feature Positive Effect, Contextual Bias, Coherence-based Reasoning, Cognitive Dissonance, Recency Effects, Confirmation Bias/Asymmetrical Skepticism x2)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Crime Scene Investigator (CSI) / Forensic Scene Examiner | 5 (Feature Positive, Contextual, Coherence-based, Cognitive Dissonance, Confirmation/Asymmetrical Skepticism) | 1 (Recency) | 0 | 0 | 100% | Moderate-High (six nominal biases from a five-item deduplicated set; requires episode separation) | High (scene processing phases, evidence sequence) | High (change officer briefing accuracy) | High | High (adds field forensic, technical/perceptual, evidence-chain role) | 0.88 |
| DNA Forensic Analyst | 5 | 1 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.80 |
| Latent Fingerprint Examiner | 4 | 2 | 0 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.76 |
| Homicide Detective | 4 | 2 | 0 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.72 |
| Polygraph Examiner | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.70 |

**Selected:** Crime Scene Investigator (CSI) (best diversity fit, adds field forensic evidence-chain context; six-item list requires deduplication and careful episode separation).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Feature Positive Effect
- **Selected occupation:** Patrol Officer (Field Response)
- **Role and setting:** Field-based first-response role; responds to dispatched calls, makes rapid on-scene assessments with limited information, exercises significant individual discretion under time pressure, works with minimal procedural scripting for ambiguous situations.
- **Why this occupation fits the bias list:** Patrol officers respond to calls where dispatch information is necessarily incomplete, and on-scene cues that are present and salient (a raised voice, visible injury, a weapon in view) are naturally weighted more heavily than equally relevant absent cues (the lack of a weapon, the absence of visible injury, a calm demeanor that contradicts the dispatch description). The feature positive effect — the tendency for the presence of a feature to be more readily detected and weighted than its absence — is a natural and distinct mechanism in this rapid-assessment context, without requiring instrument-based technical scrutiny.
- **Primary CTA scenario:** Responding to a domestic disturbance call where the initial dispatch description omits a key detail present at the scene; feature positive effect in weighting presented cues over absent ones.
- **Triggering event:** Officer is dispatched to a "verbal domestic disturbance, no weapons mentioned" call; upon arrival, one party is visibly agitated and gesturing, while the other party is calm and silent, and no dispatch information addressed prior incidents at the address.
- **Decision episodes:**
  1. Initial approach and rapid scene assessment based on visible/audible cues.
  2. Formation of a working account of "what happened" based on presented behavior.
  3. Consideration of whether absence of certain cues (no visible injury, no weapon) changes the assessment.
  4. Final decision on arrest, separation, or de-escalation without further action.
- **Available cues and evidence:** Visible demeanor of both parties, audible statements, physical environment, dispatch call notes, absence of visible injury or weapon, absence of prior-incident flag in dispatch notes.
- **Competing interpretations:** The agitated party is the aggressor vs. is reacting to provocation not yet visible; the calm party's silence indicates victimhood vs. indicates the calm party is actually the primary aggressor masking behavior.
- **Plausible actions:** Arrest the visibly agitated party; separate both parties and interview individually; take no enforcement action; request additional units or a supervisor.
- **Constraints and pressures:** Time pressure to resolve the call and clear for other dispatches, incomplete dispatch information, safety considerations, mandatory-arrest statutes in some jurisdictions for domestic incidents.
- **Consequences of error:** Wrongful arrest of the actual victim, or failure to protect a victim whose injuries or history were not visibly presented at the scene.
- **Counterfactual causal variable:** Actual presence of a prior incident history at the address (later found that the calm party had a documented history of coercive control not visible in the moment).
- **Expected interview structure:** Opening (patrol officer role context), Episode 1 (initial approach), Episode 2 (working account formation), Episode 3 (absence-cue consideration and decision), Closing (reflection on what was and wasn't visible).
- **Natural biases:** Feature Positive Effect.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Crime Scene Investigator (would create redundancy with Interview 7's more technical evidence-documentation use of the same mechanism).
- **Rejected alternative occupation 2:** Latent Fingerprint Examiner (overlaps with Interview 2; feature positive effect is plausible but less naturally isolated from contextual/confirmation mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Contextual Bias, Coherence-based Reasoning or Rationalisation
- **Selected occupation:** Latent Fingerprint Examiner
- **Role and setting:** Forensic laboratory role; compares latent prints recovered from a crime scene against exemplar prints from a suspect or database candidate, applies structured comparison methodology (analysis, comparison, evaluation), often works with case submission forms that may include extraneous case information.
- **Why this occupation fits the bias list:** Fingerprint examination is one of the most extensively documented forensic disciplines for contextual bias — where task-irrelevant case information (e.g., a confession, prior record) influences the examiner's interpretation of ambiguous print features — and coherence-based reasoning/rationalisation, where an examiner constructs an internally consistent narrative that explains away discrepancies once a match hypothesis is formed. [assets.publishing.service.gov](https://assets.publishing.service.gov.uk/media/5f4fc26ce90e074695f80977/217_FSR-G-217_Cognitive_bias_appendix_Issue_2.pdf)
- **Primary CTA scenario:** Comparing a latent print to a suspect exemplar after being told the suspect confessed; contextual bias from case information, coherence-based reasoning explaining away discrepancies.
- **Triggering event:** Examiner receives a latent print submission accompanied by a case note stating the suspect has confessed; the latent print is of moderate quality with several corresponding features but two areas of apparent discrepancy with the suspect's exemplar.
- **Decision episodes:**
  1. Initial analysis of the latent print's inherent quality and features, prior to comparison.
  2. Comparison against the suspect exemplar, informed by awareness of the confession.
  3. Evaluation of the two discrepant areas and construction of an explanation for them.
  4. Final conclusion (identification, exclusion, or inconclusive) and documentation.
- **Available cues and evidence:** Latent print image and features, suspect exemplar print, case submission note referencing the confession, the two discrepant feature areas, laboratory comparison standards.
- **Competing interpretations:** The discrepant areas reflect natural print distortion consistent with the same source vs. indicate a genuine non-match; the confession should have no bearing on the technical comparison vs. provides context that appropriately informs interpretation.
- **Plausible actions:** Conclude identification, explaining discrepancies as distortion; conclude inconclusive pending additional analysis; conclude exclusion; request a blind verification by a second examiner.
- **Constraints and pressures:** Case backlog and reporting deadlines, laboratory verification procedures, awareness of the confession's apparent weight, professional expectations for definitive conclusions.
- **Consequences of error:** Wrongful identification supporting a false confession or coerced statement, or wrongful exclusion delaying case resolution.
- **Counterfactual causal variable:** Actual reliability of the confession (later found to have been false or coerced, unrelated to the print's true source).
- **Expected interview structure:** Opening (examiner role context), Episode 1 (initial analysis), Episode 2 (comparison with case context), Episode 3 (discrepancy evaluation), Closing (reflection on the role of the case note).
- **Natural biases:** Contextual Bias, Coherence-based Reasoning or Rationalisation.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** DNA Forensic Analyst (overlaps with Interview 4; contextual bias and coherence-based reasoning are plausible there but reserved for the more quantified DNA context to preserve information-environment diversity).
- **Rejected alternative occupation 2:** Homicide Detective (overlaps with Interview 3; coherence-based reasoning is plausible in narrative case-building but less naturally tied to a discrete technical comparison task).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Cognitive Dissonance, Recency Effects, Groupthink
- **Selected occupation:** Homicide Detective
- **Role and setting:** Lead investigative role on a major-crimes squad; manages long-running cases, develops and tests suspect theories over months or years, presents case status to a squad review board or supervisor panel, exercises substantial individual discretion within a team-oversight structure.
- **Why this occupation fits the bias list:** Homicide detectives commit publicly and professionally to a suspect theory early in an investigation, creating conditions for cognitive dissonance when later evidence conflicts with that commitment. Recency effects (a new tip or piece of evidence disproportionately influencing the assessment relative to older, potentially stronger evidence) and groupthink (a squad review board converging on a shared theory without adequately probing dissenting views) are both well-documented mechanisms in cold-case and major-case review contexts.
- **Primary CTA scenario:** Reviewing a cold case file years later and reassessing the original suspect theory with a squad review board; cognitive dissonance after committing to a theory, recency effects from the most recent tip, groupthink in review board consensus.
- **Triggering event:** A cold case detective reopens a homicide file after a new anonymous tip arrives, years after the detective's own original theory (developed early in the case and defended in prior reviews) named a different individual as the primary suspect.
- **Decision episodes:**
  1. Initial review of the case file and the detective's own prior theory and public statements about it.
  2. Assessment of the new tip's content and credibility relative to the older case evidence.
  3. Presentation to and discussion with the squad review board.
  4. Final decision on whether to reopen the investigation toward a new suspect or maintain the original theory.
- **Available cues and evidence:** Original case file and evidence, the detective's prior public/internal statements committing to the original theory, the new tip's content and source credibility, review board members' reactions and discussion, older evidence that may have been underweighted.
- **Competing interpretations:** The original theory remains the best-supported explanation vs. the new tip reveals it was mistaken; the new tip is more credible because it is recent vs. older evidence was actually stronger; the review board's consensus reflects sound collective judgment vs. reflects deference to the detective's prior public commitment.
- **Plausible actions:** Reopen the investigation toward the new lead; maintain the original theory and treat the tip as unreliable; request additional forensic testing to adjudicate between theories; escalate to a fresh, independent review team.
- **Constraints and pressures:** Reputational stake in the original theory, limited remaining physical evidence for retesting, review board time constraints, family and public pressure for resolution.
- **Consequences of error:** Continued wrongful focus on an innocent original suspect vs. premature abandonment of a correct original theory based on an unreliable new tip.
- **Counterfactual causal variable:** Actual credibility of the new tip (later found to be unreliable, while the original theory's discounted evidence proves accurate — or vice versa).
- **Expected interview structure:** Opening (detective role context), Episode 1 (file review and prior commitment), Episode 2 (new tip assessment), Episode 3 (review board discussion and decision), Closing (reflection on holding versus revising the original theory).
- **Natural biases:** Cognitive Dissonance, Recency Effects, Groupthink.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Internal Affairs Investigator (overlaps with Interview 5; cognitive dissonance and groupthink are plausible there but reserved to preserve the organizational-accountability distinction from case-investigation work).
- **Rejected alternative occupation 2:** Polygraph Examiner (overlaps with Interview 6; recency effects plausible in sequential interview responses but groupthink is less naturally embedded in a largely one-to-one role).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Confirmation Bias and Asymmetrical Skepticism, Feature Positive Effect, Contextual Bias, Coherence-based Reasoning or Rationalisation
- **Selected occupation:** DNA Forensic Analyst
- **Role and setting:** Forensic laboratory role; interprets DNA profiles (including complex mixtures or low-template samples) against reference samples, applies statistical and comparative methodology, often receives case submission information alongside physical samples.
- **Why this occupation fits the bias list:** DNA analysis of low-template or mixed profiles involves genuine interpretive judgment calls (which peaks to call as alleles, how to weight a partial match), making it a well-documented site for confirmation bias and asymmetrical skepticism (applying a lower evidentiary bar to data supporting a suspect theory and a higher bar to data contradicting it), feature positive effect (weighting the presence of matching alleles more than the absence of expected ones), contextual bias (case information about a high-profile suspect shaping interpretation), and coherence-based reasoning (constructing an internally consistent account of an ambiguous profile). [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319185/)
- **Primary CTA scenario:** Interpreting a low-template/mixed DNA profile after being told the case involves a high-profile suspect; confirmation bias and asymmetrical skepticism toward supporting vs. contradicting data, feature positive effect in allele call weighting, contextual bias from case information, coherence-based reasoning in profile interpretation.
- **Triggering event:** Analyst receives a low-template, mixed DNA profile from a high-profile case, accompanied by case notes identifying a specific suspect; the profile shows some alleles consistent with the suspect and some ambiguous peaks near the detection threshold.
- **Decision episodes:**
  1. Initial profile quality assessment prior to suspect comparison.
  2. Allele calling and peak interpretation, informed by awareness of the suspect's profile and case prominence.
  3. Application of differential scrutiny to matching versus non-matching or ambiguous peaks.
  4. Final statistical interpretation and conclusion (inclusion, exclusion, inconclusive).
- **Available cues and evidence:** Raw electropherogram data, suspect reference profile, case notes on suspect identity and case prominence, ambiguous near-threshold peaks, laboratory validation thresholds for allele calling.
- **Competing interpretations:** Ambiguous peaks near threshold should be called as alleles consistent with the suspect vs. treated as noise; the profile provides strong support for inclusion vs. is genuinely inconclusive given profile quality.
- **Plausible actions:** Report a statistically supported inclusion; report inconclusive due to profile quality; request additional testing or a second sample; submit for blind independent review.
- **Constraints and pressures:** Case prominence and public attention, laboratory turnaround expectations, validated statistical thresholds, professional standards for peer review.
- **Consequences of error:** Wrongful inclusion of an innocent high-profile suspect due to differential scrutiny of ambiguous data, or wrongful exclusion of the true source due to overly conservative interpretation.
- **Counterfactual causal variable:** Actual composition of the DNA mixture (later found to include a third, unaccounted-for contributor that explains the ambiguous peaks independent of the suspect).
- **Expected interview structure:** Opening (analyst role context), Episode 1 (initial quality assessment), Episode 2 (allele calling with case context), Episode 3 (differential scrutiny and conclusion), Closing (reflection on how case prominence shaped interpretation).
- **Natural biases:** Confirmation Bias and Asymmetrical Skepticism, Feature Positive Effect, Contextual Bias, Coherence-based Reasoning or Rationalisation.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Latent Fingerprint Examiner (overlaps with Interview 2; would create redundancy in the contextual-bias/coherence-based-reasoning mechanism already assigned there).
- **Rejected alternative occupation 2:** Crime Scene Investigator (overlaps with Interview 7; feature positive effect and contextual bias are plausible there but reserved for the more integrative, multi-episode scene-processing scenario).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Cognitive Dissonance, Recency Effects, Groupthink, Confirmation Bias and Asymmetrical Skepticism, Recency Effects
- **Selected occupation:** Internal Affairs Investigator
- **Role and setting:** Internal accountability role within a law enforcement agency; investigates complaints and allegations against fellow officers, conducts interviews with complainants, witnesses, and the subject officer, often operates under organizational and political pressure with a duty to reach a defensible finding.
- **Why this occupation fits the bias list:** Internal affairs investigators frequently make and publicly communicate preliminary assessments (e.g., to command staff) before an investigation is complete, creating conditions for cognitive dissonance when subsequent evidence conflicts with that stated position. Recency effects (the most recently obtained witness statement disproportionately shaping the final assessment — the duplicate listing is treated as one mechanism appearing at two points in the investigation), groupthink (unit consensus around a colleague-protective or colleague-critical narrative), and confirmation bias with asymmetrical skepticism (applying different evidentiary standards to the officer's account versus the complainant's account) are all well-documented in internal investigation contexts.
- **Primary CTA scenario:** Investigating a use-of-force complaint against a colleague after publicly stating an initial assessment; cognitive dissonance in defending the stated position, recency effects from the most recent witness statement, groupthink in unit consensus, confirmation bias and asymmetrical skepticism toward the officer's account vs. complainant's account.
- **Triggering event:** An internal affairs investigator states an initial preliminary assessment to command staff early in a use-of-force investigation; a newly located witness comes forward late in the investigation with an account that conflicts with both the officer's statement and the investigator's stated preliminary assessment.
- **Decision episodes:**
  1. Initial evidence review and formation of the preliminary assessment communicated to command.
  2. Interviews with the subject officer and original complainant, applying differing standards of scrutiny to each account.
  3. Arrival of the new witness statement late in the investigation and its weighting against earlier, more extensive evidence.
  4. Final finding and unit-level discussion before submission.
- **Available cues and evidence:** Body-worn camera footage, subject officer's statement, complainant's statement, the new witness's late statement, unit colleagues' reactions and discussion, the investigator's own prior stated preliminary assessment.
- **Competing interpretations:** The officer's account should be given greater credence based on training and experience vs. should be scrutinized equally to the complainant's; the new witness statement is more reliable because it is most recent vs. the earlier, more extensive evidence remains stronger; unit consensus reflects genuine agreement vs. reflects pressure to protect the original preliminary assessment.
- **Plausible actions:** Sustain the complaint based on the new evidence; maintain the original preliminary finding; request additional investigation before concluding; escalate for independent civilian review.
- **Constraints and pressures:** Command staff awareness of the preliminary statement, union and departmental political dynamics, unit cohesion pressures, statutory investigation deadlines.
- **Consequences of error:** Wrongful exoneration of misconduct damaging public trust, or wrongful sustained finding against an officer based on an unreliable late statement.
- **Counterfactual causal variable:** Actual reliability of the new witness's late statement (later found to be inconsistent with physical evidence, or conversely fully corroborated by it).
- **Expected interview structure:** Opening (investigator role context), Episode 1 (preliminary assessment), Episode 2 (differential interview scrutiny), Episode 3 (new statement weighting), Closing (reflection on unit discussion and final finding).
- **Natural biases:** Cognitive Dissonance, Recency Effects, Groupthink, Confirmation Bias and Asymmetrical Skepticism.
- **Plausible but difficult biases:** None (the duplicate Recency Effects entry is treated as a single mechanism, not two).
- **Biases that should not be forced:** A second, independent instance of Recency Effects (the list's duplicate should not be coded as two separate mechanisms).
- **Rejected alternative occupation 1:** Homicide Detective (overlaps with Interview 3; would create redundancy in the cognitive-dissonance/groupthink mechanism already assigned there in a similar review-board structure).
- **Rejected alternative occupation 2:** Polygraph Examiner (overlaps with Interview 6; confirmation bias and asymmetrical skepticism are plausible there but reserved for the more perceptual interrogation-response context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Contextual Bias, Coherence-based Reasoning or Rationalisation, Cognitive Dissonance, Feature Positive Effect, Groupthink, Groupthink
- **Selected occupation:** Polygraph Examiner / Interview Specialist
- **Role and setting:** Specialized interview role; conducts structured interviews and polygraph examinations of suspects or witnesses, interprets physiological and behavioral responses, often briefed on case file information beforehand, and debriefs findings with the investigating team afterward.
- **Why this occupation fits the bias list:** Polygraph examiners and interview specialists are typically briefed on case context before an interview (contextual bias), construct an internally coherent narrative of the subject's truthfulness that explains away ambiguous responses (coherence-based reasoning), commit to an assessment during the interview that becomes harder to revise afterward (cognitive dissonance), naturally attend more to presented behavioral cues (fidgeting, gaze aversion) than to their absence (feature positive effect), and debrief with the investigating team in a way that can converge toward consensus (groupthink — the duplicate entry is treated as one mechanism, not two).
- **Primary CTA scenario:** Assessing a suspect's truthfulness in an interrogation after reviewing a case file suggesting guilt; contextual bias from file information, coherence-based reasoning in interpreting responses, cognitive dissonance after committing to a guilt assessment, feature positive effect in reading presented behavioral cues, groupthink in debrief with investigating team.
- **Triggering event:** Examiner reviews a case file strongly suggesting the suspect's guilt before conducting a polygraph and behavioral interview; during the interview, the subject displays some behaviors consistent with the file's suggestion and others that are ambiguous or contrary.
- **Decision episodes:**
  1. Pre-interview case file review and formation of an expectation.
  2. Interview conduct and observation of behavioral and physiological responses.
  3. Real-time interpretation of ambiguous responses and construction of a coherent truthfulness assessment.
  4. Post-interview debrief with the investigating team and finalization of the report.
- **Available cues and evidence:** Case file content, physiological response data (if polygraph), observed behavioral cues during interview, absent or contrary behavioral cues, investigating team's reactions during debrief.
- **Competing interpretations:** The observed behaviors indicate deception consistent with the file vs. reflect normal stress unrelated to guilt; the coherent narrative constructed during the interview accurately reflects truthfulness vs. explains away genuinely disconfirming responses; team debrief consensus reflects sound collective judgment vs. reinforces the examiner's initial expectation.
- **Plausible actions:** Report the subject as deceptive/likely guilty; report as inconclusive; report as consistent with truthfulness; request a second examiner's independent review.
- **Constraints and pressures:** Case file's pre-existing suggestion of guilt, time constraints on the interview, team expectations following debrief, professional standards for polygraph/interview reporting.
- **Consequences of error:** Wrongful deceptive finding contributing to a false accusation, or wrongful truthful finding allowing a genuinely deceptive account to stand.
- **Counterfactual causal variable:** Actual cause of the ambiguous behavioral responses (later found to reflect an unrelated stressor, such as an unrelated legal matter, rather than deception about the case).
- **Expected interview structure:** Opening (examiner role context), Episode 1 (pre-interview file review), Episode 2 (interview and observation), Episode 3 (interpretation and coherent narrative construction), Episode 4 (team debrief), Closing (reflection on file influence and team dynamics).
- **Natural biases:** Contextual Bias, Coherence-based Reasoning or Rationalisation, Cognitive Dissonance, Feature Positive Effect, Groupthink.
- **Plausible but difficult biases:** None outright, but the duplicate Groupthink entry must be treated as a single mechanism rather than forced into two distinct instances.
- **Biases that should not be forced:** A second, independent instance of Groupthink (the list's duplicate should not be coded as two separate mechanisms).
- **Rejected alternative occupation 1:** Homicide Detective (overlaps with Interview 3; cognitive dissonance and groupthink already assigned there in a review-board rather than interview-debrief structure).
- **Rejected alternative occupation 2:** Internal Affairs Investigator (overlaps with Interview 5; confirmation bias and cognitive dissonance already assigned there in a differential-scrutiny rather than interview-interpretation structure).
- **Recommendation status:** APPROVED_WITH_CAVEATS (duplicate Groupthink in the requested list must be coded as one mechanism, not two independent instances)

***

### Interview 7

- **Requested biases:** Feature Positive Effect, Contextual Bias, Coherence-based Reasoning or Rationalisation, Cognitive Dissonance, Recency Effects, Confirmation Bias and Asymmetrical Skepticism, Confirmation Bias and Asymmetrical Skepticism
- **Selected occupation:** Crime Scene Investigator (CSI) / Forensic Scene Examiner
- **Role and setting:** Field forensic role; processes crime scenes to document, collect, and preserve physical evidence, often works alongside or is briefed by responding officers and detectives with a working theory of events, documents findings that feed into the broader case narrative.
- **Why this occupation fits the bias list:** Crime scene investigators are routinely briefed on responding officers' working theories before processing a scene (contextual bias), document presented physical evidence more readily than the absence of expected evidence (feature positive effect), construct a coherent scene narrative that explains away inconsistent items (coherence-based reasoning), commit to an initial scene interpretation that becomes resistant to revision as processing continues (cognitive dissonance), weight the last-processed item more heavily in their overall impression (recency effects), and apply differential scrutiny to evidence supporting versus contradicting the working theory (confirmation bias and asymmetrical skepticism — the duplicate entry is treated as one mechanism appearing across two distinct evidence-handling episodes rather than two independent biases).
- **Primary CTA scenario:** Processing a crime scene after being briefed on the responding officers' working theory of what happened; feature positive effect in evidence documentation, contextual bias from officer briefing, coherence-based reasoning in scene narrative construction, cognitive dissonance after committing to initial scene interpretation, recency effects from the last item processed, confirmation bias and asymmetrical skepticism toward theory-supporting vs. contradicting evidence.
- **Triggering event:** CSI arrives at a scene and is briefed by responding officers on their working theory of what occurred; early in processing, several items are found consistent with the theory, and the CSI documents a preliminary scene narrative before finishing the full search, after which a late-found item appears inconsistent with that narrative.
- **Decision episodes:**
  1. Pre-processing briefing from officers and formation of an initial working theory.
  2. Early evidence collection, with theory-consistent items readily documented and their presence emphasized over the absence of theory-inconsistent items.
  3. Mid-processing commitment to a preliminary scene narrative, applying differential scrutiny to subsequent theory-supporting versus theory-contradicting items.
  4. Discovery and handling of a late, theory-inconsistent item, weighted heavily due to its recency, and final scene report.
- **Available cues and evidence:** Officer briefing content, physical evidence items found throughout processing (in sequence), absence of expected items, the late-found theory-inconsistent item, scene photographs and documentation standards.
- **Competing interpretations:** The scene supports the officers' working theory vs. the late item indicates a different sequence of events; theory-supporting evidence was documented because it was genuinely more probative vs. because it fit the expected narrative; the late item's recency makes it most significant vs. it should be weighted no more than earlier evidence.
- **Plausible actions:** Finalize the scene report consistent with the original working theory, treating the late item as an anomaly; revise the scene narrative to accommodate the late item; flag the inconsistency for the investigating detective without resolving it; request additional scene processing time.
- **Constraints and pressures:** Scene processing time limits, officer briefing's apparent authority, chain-of-custody and documentation standards, downstream reliance by detectives and prosecutors on the scene report.
- **Consequences of error:** A scene report that reinforces an incorrect working theory, misdirecting the investigation, or an unwarranted late revision destabilizing an otherwise sound narrative.
- **Counterfactual causal variable:** Actual sequence and origin of the late-found item (later found to be unrelated to the incident, or conversely the single most probative piece of evidence at the scene).
- **Expected interview structure:** Opening (CSI role context), Episode 1 (briefing and initial theory), Episode 2 (early evidence documentation), Episode 3 (mid-processing commitment and differential scrutiny), Episode 4 (late item and final report), Closing (reflection on briefing influence and evidence sequencing).
- **Natural biases:** Feature Positive Effect, Contextual Bias, Coherence-based Reasoning or Rationalisation, Recency Effects.
- **Plausible but difficult biases:** Cognitive Dissonance (requires a clear, articulated commitment point mid-processing to distinguish it from ordinary evidence weighing), Confirmation Bias and Asymmetrical Skepticism (the duplicate entry requires two distinct episodes — early documentation and late-item handling — to avoid being coded as a single instance when the list nominally requests two).
- **Biases that should not be forced:** A second, fully independent instance of Confirmation Bias and Asymmetrical Skepticism beyond the two-episode treatment described above.
- **Rejected alternative occupation 1:** DNA Forensic Analyst (overlaps with Interview 4; would create redundancy in the confirmation-bias/feature-positive-effect mechanism already assigned there in a lab rather than field context).
- **Rejected alternative occupation 2:** Latent Fingerprint Examiner (overlaps with Interview 2; contextual bias and coherence-based reasoning already assigned there in a discrete comparison rather than integrative scene-processing structure).
- **Recommendation status:** APPROVED_WITH_CAVEATS (duplicate Confirmation Bias/Asymmetrical Skepticism entry requires explicit two-episode separation; Cognitive Dissonance requires a clearly marked commitment point)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (patrol officer, fingerprint examiner, homicide detective, DNA analyst, internal affairs investigator, polygraph examiner, CSI) | None | None | None | None needed |
| Work setting | Field/individual (1, 7), Forensic laboratory (2, 4), Team/office investigative (3, 5), One-to-one interview (6) | Forensic laboratory (2/7) | Balanced | Public-facing/service-oriented, Remote/digital | None critical; law enforcement domain is inherently field/lab/office weighted |
| Decision type | Emergency response/classification (1), Diagnosis/comparison (2, 4), Investigation/review (3), Compliance/adjudication (5), Interrogation/assessment (6), Evidence collection/narrative-building (7) | Diagnosis-type (2/7: 2, 4) | Diagnosis/comparison | Negotiation, Resource allocation | None critical; diagnosis-type reasoning is core to forensic work, but contexts (fingerprint vs. DNA) differ materially in information structure |
| Information environment | Perceptual/rapid (1), Technical/perceptual (2), Socially-mediated/team (3), Data-heavy/quantified (4), Socially-mediated/organizational (5), Socially-mediated/perceptual (6), Technical/perceptual/sequential (7) | Socially-mediated (3/7: 3, 5, 6) | Socially-mediated | Rich/structured as primary driver | None critical; reflects law enforcement's inherently interpersonal and organizational information flows |
| Time pressure | High (1), Low/moderate (2, 4), Moderate (3), Moderate-high (5), Moderate (6), Moderate-high (7) | Moderate (4/7) | Moderate | Very low | None critical |
| Consequence of error | Safety/legal (1), Legal/wrongful conviction (2, 4), Legal/investigative (3), Legal/organizational-reputational (5), Legal/reputational (6), Legal/investigative (7) | Legal (7/7 as secondary) | Legal (expected given domain) | Financial, Environmental | None critical; the entire domain is legal-consequence-anchored by nature, but primary consequence differs (safety in 1, wrongful conviction in 2/4, organizational in 5) |
| Expertise level | Developing/independent (1), Specialist (2, 4), Senior practitioner (3), Independent/specialist (5), Specialist (6), Independent/specialist (7) | Specialist (4/7) | Specialist | Strategist/decision authority | None critical |
| Stakeholder pattern | Individual/public-facing (1), Individual technical (2, 4), Team/review board (3), One-to-one interview (5, 6), Individual-in-team-context (7) | Individual technical (2/7) | Balanced | Multi-party negotiation | None critical |
| Scenario archetype | Rapid field assessment (1), Forensic comparison (2, 4), Cold-case review (3), Internal complaint investigation (5), Interrogation assessment (6), Scene processing narrative (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Presence of unseen history (1), Confession reliability (2), Tip credibility (3), Mixture composition (4), Witness statement reliability (5), Behavioral response cause (6), Late item origin (7) | None significant | None | Equipment/instrument failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact |

**Overall assessment:** Strong diversity across occupations, settings, and decision types, with the domain's inherent legal-consequence and socially-mediated character appropriately reflected rather than artificially diluted. Two forensic laboratory roles (fingerprint, DNA) are both included because they differ materially in information environment (perceptual/qualitative vs. quantified/statistical) and were required to preserve valid, distinct embeddings for four-bias and single-bias-pair lists respectively. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Feature Positive Effect (clear mechanism: presence weighted over absence) | None | Feature Positive Effect (risk of being read as simply "missed a clue") | None | None | None | Explicitly present both a salient cue and an equally relevant absent cue; probe why the absence wasn't weighted, not just the outcome |
| 2 | Contextual Bias (case information influence), Coherence-based Reasoning (discrepancy explaining-away) | Contextual Bias and Confirmation Bias (contextual bias is the trigger; coherence-based reasoning is the mechanism that follows)  [datafield](https://datafield.dev/forensic-science/part-06/chapter-31/) | None | None | None | None | Show the case note explicitly and the examiner's awareness of it before comparison; show explicit reasoning that explains away each discrepancy rather than merely stating a conclusion |
| 3 | Cognitive Dissonance (commitment-defense), Recency Effects (recent-tip weighting), Groupthink (board consensus) | Cognitive Dissonance and Confirmation Bias (both involve resistance to disconfirming evidence) | None | None | Groupthink (dissent-suppression must be explicit, not just agreement) | Groupthink | Show the detective's prior public/internal commitment explicitly; show at least one board member's view being discounted to distinguish groupthink from ordinary consensus |
| 4 | Confirmation Bias/Asymmetrical Skepticism (differential scrutiny), Feature Positive Effect (allele presence weighting), Contextual Bias (case prominence), Coherence-based Reasoning (ambiguous profile narrative) | Confirmation Bias/Asymmetrical Skepticism and Contextual Bias (contextual bias supplies the expectation; confirmation bias is the differential-scrutiny mechanism)  [datafield](https://datafield.dev/forensic-science/part-06/chapter-31/) | None | None | None | None | Show explicit differential treatment of matching vs. non-matching peaks (different scrutiny standards applied), not just a single conclusion; separate the case-prominence cue from the differential-scrutiny behavior |
| 5 | Cognitive Dissonance, Groupthink, Confirmation Bias/Asymmetrical Skepticism (three distinct); Recency Effects (duplicate, single mechanism) | Cognitive Dissonance and Confirmation Bias/Asymmetrical Skepticism (both involve resistance to disconfirming evidence after a stated position) | None | None | Groupthink (unit dissent-suppression must be explicit) | Groupthink | Treat the duplicate Recency Effects entry as one mechanism; show explicit differential interview scrutiny of officer vs. complainant accounts; show the investigator's prior stated preliminary assessment explicitly |
| 6 | Contextual Bias, Coherence-based Reasoning, Cognitive Dissonance, Feature Positive Effect (four distinct); Groupthink (duplicate, single mechanism) | Contextual Bias and Coherence-based Reasoning (trigger/mechanism pair, as in Interview 2)  [datafield](https://datafield.dev/forensic-science/part-06/chapter-31/), Cognitive Dissonance and Coherence-based Reasoning (both involve maintaining a consistent narrative) | None | None | Feature Positive Effect (behavioral-cue presence must be explicit and contrasted with absent cues) | Feature Positive Effect | Treat the duplicate Groupthink entry as one mechanism; show the pre-interview file explicitly and its influence on expectation separately from the in-interview coherent-narrative construction |
| 7 | Feature Positive Effect, Contextual Bias, Coherence-based Reasoning, Recency Effects (four distinct); Cognitive Dissonance (requires explicit commitment point); Confirmation Bias/Asymmetrical Skepticism (duplicate, requires two-episode separation) | Contextual Bias and Coherence-based Reasoning (trigger/mechanism pair)  [datafield](https://datafield.dev/forensic-science/part-06/chapter-31/), Cognitive Dissonance and Confirmation Bias/Asymmetrical Skepticism (both involve resistance to disconfirming evidence post-commitment), Recency Effects and the late-item handling (must be distinguished from ordinary evidence weighing) | None | None | Cognitive Dissonance (commitment point must be explicit, not inferred) | Cognitive Dissonance, Confirmation Bias/Asymmetrical Skepticism (two-episode version) | Mark an explicit, articulated mid-processing commitment point for Cognitive Dissonance; design two clearly separated evidence-handling episodes (early and late) for Confirmation Bias/Asymmetrical Skepticism rather than treating the duplicate as license for a third mechanism |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For all interviews with duplicate bias labels (5: Recency Effects; 6: Groupthink; 7: Confirmation Bias/Asymmetrical Skepticism), generate exactly one underlying mechanism per duplicate pair, optionally manifesting at two distinct points in the narrative, rather than inventing two independent biases. For Interviews 2, 4, 6, and 7, explicitly separate the contextual-bias trigger (the outside information) from the confirmation/coherence-based-reasoning mechanism (what the practitioner does with it), consistent with the forensic-science literature's trigger/engine framing. [datafield](https://datafield.dev/forensic-science/part-06/chapter-31/)
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, with particular attention to distinguishing Contextual Bias (the presence of outside information) from Confirmation Bias/Coherence-based Reasoning (the practitioner's differential handling of evidence in light of that information) as two separable but related mechanisms. Flag any bias supported only by the case's ultimate outcome (e.g., "the analyst was wrong") rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
