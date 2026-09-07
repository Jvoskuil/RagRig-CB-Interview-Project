This confirms the analytic-workflow bias taxonomy maps cleanly onto stages: capture requirements, plan analytic response, obtain data, process data, interpret outputs, communicate conclusions — directly useful for grounding each interview's decision episodes. Now I'll build the full allocation.

## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | All-Source Intelligence Analyst (Strategic) | Monitoring a slow-developing foreign military buildup where nothing has escalated for months; complacency bias in downgrading the priority of the account | 100% | 3 | High | Adds strategic/long-horizon monitoring, individual analytical work context | APPROVED |
| 2 | 2 | Signals Intelligence (SIGINT) Analyst | Interpreting intercepted communications using a familiar analytic technique; explanation bias in imagining a scenario that then feels more likely, fluency effects favoring familiar source/technique | 100% | 6 | High | Adds technical/perceptual signal interpretation, individual work with raw data context | APPROVED |
| 3 | 3 | Imagery/GEOINT Analyst | Interpreting satellite imagery of a foreign facility using a Western operational template; mirror imaging in inferring intent, order effects in image sequence review, perceptual bias in ambiguous imagery interpretation | 100% | 9 | High | Adds visual/perceptual analytic work, technical tools, individual interpretation context | APPROVED |
| 4 | 4 | Financial Crime/Threat Intelligence Analyst | Assessing likelihood and timeline of a sanctions-evasion scheme becoming operational; wishful thinking about disruption success, belief bias in evaluating argument plausibility, selective attention to confirming transaction patterns, planning fallacy in disruption-operation timeline | 100% | 12 | High | Adds financial/regulatory information environment, cross-agency stakeholder context | APPROVED |
| 5 | 5 | Counterterrorism Analyst (Team Lead, Fusion Center) | Leading a rapid assessment briefing to senior decision-makers on an emerging threat; authority bias toward senior officer's framing, framing effects in threat presentation, groupthink in team assessment, overconfidence in threat level, anchoring on first threat report | 100% | 15 | High | Adds team coordination, briefing/communication stage, multi-stakeholder, high-consequence context | APPROVED |
| 6 | 6 | Cyber Threat Intelligence Analyst | Attributing a network intrusion to a known threat actor using a familiar analytic technique under time pressure; confirmation bias in attribution, complacency in recurring alert triage, explanation bias in attack narrative, fluency effects favoring familiar actor profile, mirror imaging in attacker motive, order effects in log review sequence | 100% | 18 | High | Adds data-heavy/software-mediated technical environment, rapidly changing information context | APPROVED |
| 7 | 7 | Human Intelligence (HUMINT) Collection Manager/Reports Officer | Evaluating a source's reporting on an impending event and deciding whether to task further collection; perceptual bias in interpreting ambiguous source reporting, wishful thinking about source reliability, belief bias in argument evaluation, selective attention to corroborating details, planning fallacy in tasking timeline, authority bias toward senior handler's assessment, framing effects in reporting write-up | 86% | 19 | Moderate-High | Adds human-source/socially-mediated information environment, one-to-one source relationship context | APPROVED_WITH_CAVEATS (Authority Bias requires clear organizational hierarchy cue; Planning Fallacy requires distinct tasking-timeline episode) |

***

## 2. Candidate occupation matrix

### Interview 1 (Complacency Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| All-Source Intelligence Analyst (Strategic) | 1 (Complacency) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (long-horizon monitoring phases) | High (change actual threat trajectory) | High | High (adds long-horizon, individual monitoring context) | 0.88 |
| Cyber Threat Intelligence Analyst | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 6) | 0.76 |
| HUMINT Reports Officer | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.60 |
| GEOINT Analyst | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 3) | 0.55 |
| Financial Crime Analyst | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Medium | 0.45 |

**Selected:** All-Source Intelligence Analyst (Strategic) (best coverage, distinctness, diversity fit).

***

### Interview 2 (Explanation Bias, Fluency Effects)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Signals Intelligence (SIGINT) Analyst | 2 (Explanation, Fluency) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (intercept interpretation phases) | High (change intercept content ambiguity) | High | High (adds technical/perceptual signal role) | 0.90 |
| All-Source Analyst | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| Cyber Threat Intelligence Analyst | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.66 |
| GEOINT Analyst | 1 | 0 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 3) | 0.52 |
| HUMINT Reports Officer | 0 | 1 | 1 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 7) | 0.50 |

**Selected:** SIGINT Analyst (best coverage, distinctness, diversity fit).

***

### Interview 3 (Mirror Imaging Bias, Order Effects, Perceptual Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Imagery/GEOINT Analyst | 3 (Mirror Imaging, Order Effects, Perceptual) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (imagery interpretation phases) | High (change actual facility function) | High | High (adds visual/perceptual analytic role) | 0.92 |
| All-Source Analyst | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 1) | 0.76 |
| SIGINT Analyst | 1 | 1 | 1 | 0 | 67% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.60 |
| Cyber Threat Intelligence Analyst | 1 | 2 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.66 |
| Counterterrorism Analyst | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.68 |

**Selected:** Imagery/GEOINT Analyst (best coverage, distinctness, diversity fit).

***

### Interview 4 (Wishful Thinking, Belief Bias, Selective Attention Bias, Planning Fallacy)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Financial Crime/Threat Intelligence Analyst | 4 (Wishful Thinking, Belief Bias, Selective Attention, Planning Fallacy) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (case-building phases, cross-agency coordination) | High (change transaction pattern accuracy) | High | High (adds financial/regulatory information environment) | 0.94 |
| HUMINT Reports Officer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.80 |
| Counterterrorism Analyst | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| All-Source Analyst | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| Cyber Threat Intelligence Analyst | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 6) | 0.65 |

**Selected:** Financial Crime/Threat Intelligence Analyst (best coverage, distinctness, diversity fit — introduces financial-sector information environment not otherwise represented).

***

### Interview 5 (Authority Bias, Framing Effects, Groupthink, Overconfidence Bias, Anchoring Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Counterterrorism Analyst (Team Lead, Fusion Center) | 5 (all) | 0 | 0 | 0 | 100% | High (five distinct mechanisms) | High (briefing phases, team dynamics) | High (change initial threat report accuracy) | High | High (adds team leadership, briefing/communication context) | 0.95 |
| All-Source Analyst | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 1) | 0.80 |
| Financial Crime Analyst | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 4) | 0.74 |
| GEOINT Analyst | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.68 |
| SIGINT Analyst | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.66 |

**Selected:** Counterterrorism Analyst (Team Lead) (best coverage, distinctness, scenario richness).

***

### Interview 6 (Confirmation Bias, Complacency Bias, Explanation Bias, Fluency Effects, Mirror Imaging Bias, Order Effects)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Cyber Threat Intelligence Analyst | 6 (all) | 0 | 0 | 0 | 100% | High (six distinct mechanisms, all mappable to distinct workflow stages) | High (attribution phases, multiple decision points) | High (change log/attribution data accuracy) | High | High (adds data-heavy, rapidly-changing technical environment) | 0.96 |
| SIGINT Analyst | 5 | 1 | 0 | 0 | 92% | High | High | High | High | Low (overlaps with Interview 2) | 0.82 |
| GEOINT Analyst | 4 | 2 | 0 | 0 | 83% | High | High | High | High | Low (overlaps with Interview 3) | 0.76 |
| All-Source Analyst | 4 | 1 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| Counterterrorism Analyst | 3 | 2 | 1 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.68 |

**Selected:** Cyber Threat Intelligence Analyst (best coverage, distinctness, diversity fit; all six biases map cleanly onto distinct stages of the malware/log analysis workflow).

***

### Interview 7 (Perceptual Bias, Wishful Thinking, Belief Bias, Selective Attention Bias, Planning Fallacy, Authority Bias, Framing Effects)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Human Intelligence (HUMINT) Collection Manager/Reports Officer | 5 (Perceptual, Wishful Thinking, Belief Bias, Selective Attention, Framing) | 2 (Planning Fallacy, Authority Bias) | 0 | 0 | 100% | Moderate-High (Planning Fallacy and Authority Bias require distinct episodes) | High (source reporting phases, tasking decision) | High (change source reliability data) | High | High (adds human-source, socially-mediated information environment) | 0.88 |
| Counterterrorism Analyst | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.80 |
| Financial Crime Analyst | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.76 |
| GEOINT Analyst | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.74 |
| SIGINT Analyst | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 2) | 0.72 |

**Selected:** HUMINT Collection Manager/Reports Officer (best diversity fit, adds human-source information environment; Planning Fallacy and Authority Bias require careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Complacency Bias
- **Selected occupation:** All-Source Intelligence Analyst (Strategic)
- **Role and setting:** Office-based analytic role in a national or defense intelligence organization; monitors a long-standing account (e.g., a foreign military capability or political situation) over months or years, integrating multiple source types into periodic assessments for policy or military customers. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Why this occupation fits the bias list:** Strategic analysts often track "steady state" accounts where nothing dramatic happens for extended periods. Complacency bias (reduced vigilance and prioritization after prolonged absence of change) is a natural mechanism when an analyst has watched an indicator remain stable for many reporting cycles and begins deprioritizing routine checks. This is well-documented in analytic tradecraft literature on sustained monitoring accounts. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Primary CTA scenario:** Monitoring a slow-developing foreign military buildup where nothing has escalated for months; complacency bias in downgrading the priority of the account.
- **Triggering event:** After eight months of unchanging indicators on a foreign military modernization account, a new but modest-looking satellite pass shows a minor change that the analyst must decide whether to flag for closer review or file as routine.
- **Decision episodes:**
  1. Initial routine review of the new data against the long-stable baseline.
  2. Prioritization decision: does this account still warrant the same review cadence and depth?
  3. Comparison of the minor change against historical noise/variation in past reporting cycles.
  4. Final decision on whether to escalate, request additional collection, or note as routine and move to other higher-priority accounts.
- **Available cues and evidence:** Historical baseline imagery/reporting, the new indicator, collection tasking history, competing account workload, prior false-alarm rate on this account.
- **Competing interpretations:** The change is noise consistent with eight months of stability vs. the change is an early signal of a shift; the account's low historical activity justifies reduced scrutiny vs. warrants the same rigor as any active account.
- **Plausible actions:** File as routine with no further action; request follow-up collection; flag for a colleague's second look; elevate to a special report.
- **Constraints and pressures:** Competing workload from higher-priority accounts, limited collection resources, customer expectations for account-specific reporting cadence, lack of recent negative feedback reinforcing current review depth.
- **Consequences of error:** Missed early warning of a genuine shift vs. unnecessary escalation diverting scarce collection resources from active crises.
- **Counterfactual causal variable:** Actual significance of the minor change (later found that it was the first visible indicator of a program that accelerated significantly in subsequent months).
- **Expected interview structure:** Opening (analyst role and account context), Episode 1 (routine review), Episode 2 (prioritization reasoning), Episode 3 (comparison and decision), Closing (reflection on vigilance and workload trade-offs).
- **Natural biases:** Complacency Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Cyber Threat Intelligence Analyst (would overlap with Interview 6; less natural for long-horizon complacency given faster-moving cyber timelines).
- **Rejected alternative occupation 2:** HUMINT Reports Officer (overlaps with Interview 7; complacency less central to source-handling work than to steady-state account monitoring).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Explanation Bias, Fluency Effects
- **Selected occupation:** Signals Intelligence (SIGINT) Analyst
- **Role and setting:** Technical analytic role; processes and interprets intercepted communications (voice, text, or metadata), applies established analytic techniques to characterize intent and activity, works largely individually with specialized tools before contributing to broader reporting. [armyprt](https://www.armyprt.com/mos/35-series-mos/)
- **Why this occupation fits the bias list:** SIGINT analysts routinely construct explanatory narratives from fragmentary intercepts and rely on familiar analytic techniques and trusted source types. Explanation bias (imagining how an event could occur, making it seem more likely) occurs naturally during the "interpret outputs" stage, and fluency effects (preferring familiar, easily processed information or techniques) occur naturally during the "plan analytic response" and "obtain data" stages, per the analytic workflow model. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Primary CTA scenario:** Interpreting intercepted communications using a familiar analytic technique; explanation bias in imagining a scenario that then feels more likely, fluency effects favoring familiar source/technique.
- **Triggering event:** SIGINT analyst receives a batch of intercepts referencing an ambiguous planning activity; the analyst begins by using the same analytic technique and trusted source category used successfully on a similar account months earlier.
- **Decision episodes:**
  1. Initial technique selection based on past familiarity and ease of use.
  2. Construction of a plausible explanatory scenario for the ambiguous intercept content.
  3. Evaluation of the scenario's likelihood after having articulated it.
  4. Final assessment and decision on how confidently to report the interpretation.
- **Available cues and evidence:** Raw intercept content, metadata, historical pattern from the similar prior account, alternative less-familiar analytic techniques available but unused, source reliability ratings.
- **Competing interpretations:** The imagined scenario is the most likely explanation vs. one of several equally plausible explanations; the familiar technique is appropriate here vs. a different technique would surface different evidence.
- **Plausible actions:** Report the imagined scenario as the primary assessment; explicitly present multiple competing scenarios; request additional collection using an alternative technique; flag low confidence pending more data.
- **Constraints and pressures:** Reporting deadlines, limited time to explore alternative techniques, customer expectations for a clear assessment, tool/technique familiarity from training and past use.
- **Consequences of error:** Reporting an incorrect scenario as more likely than warranted, potentially misdirecting customer expectations or downstream collection priorities.
- **Counterfactual causal variable:** Actual meaning of the intercept content (later found that an alternative, initially unconsidered, explanation was correct).
- **Expected interview structure:** Opening (SIGINT analyst role context), Episode 1 (technique selection), Episode 2 (scenario construction), Episode 3 (likelihood evaluation and reporting decision), Closing (reflection on technique and scenario choice).
- **Natural biases:** Explanation Bias, Fluency Effects.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** All-Source Analyst (overlaps with Interview 1; less naturally tied to the specific technique-familiarity mechanism of fluency effects in raw signal processing).
- **Rejected alternative occupation 2:** Cyber Threat Intelligence Analyst (overlaps with Interview 6; risks conflating fluency effects with the confirmation/complacency mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Mirror Imaging Bias, Order Effects, Perceptual Bias
- **Selected occupation:** Imagery/GEOINT Analyst
- **Role and setting:** Visual analytic role; exploits and interprets satellite, aerial, or full-motion video imagery to identify and characterize objects, facilities, and activities; works largely individually with imagery exploitation tools, often reviewing sequential image sets over time. [dami.army.pentagon](https://www.dami.army.pentagon.mil/offices/dami-cp/guidance/aogs/132_st/part_II.asp)
- **Why this occupation fits the bias list:** Imagery analysts interpret inherently ambiguous visual data and often reason about foreign facilities or activities using familiar operational templates from their own military/organizational background. Mirror imaging bias (assuming a foreign actor will behave according to one's own operational logic) is a classic and well-documented mechanism in imagery interpretation of foreign facilities. Order effects (the sequence in which images or reports are reviewed affecting weight given to information) and perceptual bias (interpretation of genuinely ambiguous visual data shaped by expectation) are both natural in the "obtain data" and "interpret outputs" stages of imagery work. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Primary CTA scenario:** Interpreting satellite imagery of a foreign facility using a Western operational template; mirror imaging in inferring intent, order effects in image sequence review, perceptual bias in ambiguous imagery interpretation.
- **Triggering event:** GEOINT analyst reviews a new set of satellite images showing configuration changes at a foreign facility; the images are reviewed in the order received, with the clearest image arriving first and more ambiguous images arriving afterward.
- **Decision episodes:**
  1. Initial review of the first (clearest) image and formation of an interpretive hypothesis.
  2. Review of subsequent, more ambiguous images in the order received.
  3. Application of a familiar operational template to infer the facility's likely function and intent.
  4. Final characterization and confidence assessment for the report.
- **Available cues and evidence:** Sequential satellite images of varying clarity, facility layout changes, comparison imagery of similar facilities (including from analyst's own country's doctrine), collateral reporting, historical activity at the site.
- **Competing interpretations:** The facility serves the same function it would in the analyst's own military doctrine vs. a different function reflecting different operational logic; the first, clearest image is most representative vs. later images should carry more weight; the ambiguous features indicate one activity vs. another equally plausible activity.
- **Plausible actions:** Report facility function based on the operational-template inference; explicitly flag alternative functions and request additional collateral; re-order review to weight all images equally; consult a subject-matter expert on the foreign military's actual doctrine.
- **Constraints and pressures:** Reporting deadlines, image sequence delivery order, limited collateral information on the specific foreign doctrine, customer urgency for facility characterization.
- **Consequences of error:** Misidentifying facility function based on an inapplicable operational template, leading to miscalibrated threat assessment or misdirected further collection.
- **Counterfactual causal variable:** Actual doctrine and operational logic governing the foreign facility (later found to differ substantially from the analyst's own military's approach to a similarly configured facility).
- **Expected interview structure:** Opening (GEOINT analyst role context), Episode 1 (first image review), Episode 2 (sequential review of ambiguous images), Episode 3 (template application and characterization), Closing (reflection on interpretive assumptions).
- **Natural biases:** Mirror Imaging Bias, Order Effects, Perceptual Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** All-Source Analyst (overlaps with Interview 1; less naturally tied to the visual/perceptual mechanism specific to imagery interpretation).
- **Rejected alternative occupation 2:** Counterterrorism Analyst (overlaps with Interview 5; mirror imaging is plausible but order effects and perceptual bias are less naturally tied to briefing-focused work).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Wishful Thinking, Belief Bias, Selective Attention Bias, Planning Fallacy
- **Selected occupation:** Financial Crime/Threat Intelligence Analyst
- **Role and setting:** Analytic role in a financial intelligence unit, bank, or regulatory body; investigates suspicious transaction patterns and financial networks to assess sanctions evasion, money laundering, or terrorist financing risk; interfaces with compliance, law enforcement, and international partners on disruption operations. [tandfonline](https://www.tandfonline.com/doi/full/10.1080/02684527.2012.746415)
- **Why this occupation fits the bias list:** Financial crime analysts build cases and plan disruption operations against evasive financial networks with genuinely incomplete data. Wishful thinking (hoping a disruption operation will succeed and interpreting ambiguous signs accordingly), belief bias (evaluating an argument's strength by whether the conclusion feels plausible rather than its logical structure), selective attention bias (focusing on transaction data that confirms an existing hypothesis about the network), and planning fallacy (underestimating the time and complexity of executing a disruption operation) are all well-documented in financial-crime analytic work.
- **Primary CTA scenario:** Assessing likelihood and timeline of a sanctions-evasion scheme becoming operational; wishful thinking about disruption success, belief bias in evaluating argument plausibility, selective attention to confirming transaction patterns, planning fallacy in disruption-operation timeline.
- **Triggering event:** Financial crime analyst identifies a pattern of transactions suggestive of an emerging sanctions-evasion network and is tasked with assessing how quickly the network could become fully operational and recommending a disruption timeline.
- **Decision episodes:**
  1. Initial pattern identification and hypothesis formation about the network's structure.
  2. Evidence gathering, with attention drawn disproportionately to transactions that fit the initial hypothesis.
  3. Argument construction for the case file, evaluated partly by how plausible the overall conclusion feels.
  4. Timeline and resource estimation for the recommended disruption operation.
- **Available cues and evidence:** Transaction records, entity relationship data, prior similar case outcomes, partner agency input, sanctions list data, operational resource constraints.
- **Competing interpretations:** The transaction pattern reflects a coordinated evasion scheme vs. unrelated legitimate activity; the case argument is logically sound vs. merely plausible-sounding; the disruption timeline is realistic vs. underestimates coordination complexity.
- **Plausible actions:** Recommend immediate disruption action; recommend continued monitoring to build a stronger case; request additional partner-agency data; revise the timeline estimate upward.
- **Constraints and pressures:** Legal evidentiary thresholds, cross-agency coordination requirements, resource availability for disruption operations, reporting deadlines, desire for a successful case outcome.
- **Consequences of error:** Premature or failed disruption operation damaging future case-building vs. delayed action allowing the network to become fully operational.
- **Counterfactual causal variable:** Actual complexity of the network's operational structure (later found to involve additional layers not accounted for in the original timeline estimate).
- **Expected interview structure:** Opening (analyst role context), Episode 1 (pattern identification), Episode 2 (evidence gathering), Episode 3 (case argument and timeline estimation), Closing (reflection on case-building process).
- **Natural biases:** Wishful Thinking, Belief Bias, Selective Attention Bias, Planning Fallacy.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** HUMINT Reports Officer (overlaps with Interview 7; belief bias and selective attention are plausible but wishful thinking about disruption is more naturally tied to operational case-building than source handling).
- **Rejected alternative occupation 2:** Counterterrorism Analyst (overlaps with Interview 5; would create redundancy in briefing-style scenario pattern).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Authority Bias or Authority Obedience, Framing Effects, Groupthink, Overconfidence Bias, Anchoring Bias
- **Selected occupation:** Counterterrorism Analyst (Team Lead, Fusion Center)
- **Role and setting:** Team leadership role in a multi-agency fusion center; leads a small analytic team assessing an emerging threat, synthesizes team input into a briefing for senior decision-makers, operates under significant time pressure and organizational hierarchy. [tandfonline](https://www.tandfonline.com/doi/full/10.1080/02684527.2012.746415)
- **Why this occupation fits the bias list:** Team leads in fusion-center settings brief senior officials and work within organizational hierarchies where authority bias (deferring to a senior officer's framing of the threat), framing effects (how the threat is presented shaping risk perception), groupthink (team consensus suppressing dissenting views under time pressure), overconfidence bias (in the certainty of the threat assessment), and anchoring bias (on the initial threat report) are all well-documented mechanisms in intelligence briefing and team-assessment contexts. [ikn.army](https://www.ikn.army.mil/apps/MIPBW/MIPB_Features/Kwoun.pdf)
- **Primary CTA scenario:** Leading a rapid assessment briefing to senior decision-makers on an emerging threat; authority bias toward senior officer's framing, framing effects in threat presentation, groupthink in team assessment, overconfidence in threat level, anchoring on first threat report.
- **Triggering event:** A fusion-center team lead receives an initial threat report rated as high-confidence by a senior officer and must lead the team's rapid assessment before a same-day briefing to senior decision-makers.
- **Decision episodes:**
  1. Initial team review anchored to the senior officer's high-confidence framing of the first report.
  2. Team discussion incorporating additional, partially conflicting information.
  3. Consensus-building under time pressure for the briefing.
  4. Final briefing delivery, including framing of risk and expressed confidence level.
- **Available cues and evidence:** Initial threat report and senior officer's assessment, additional partial corroborating and conflicting reporting, team members' individual assessments, briefing time constraints, historical base rate for similar threat reports.
- **Competing interpretations:** The senior officer's initial framing is correct and should anchor the team's assessment vs. new information warrants revising the framing; team consensus reflects genuine agreement vs. suppressed dissent under time pressure; the threat level is as certain as the team's confidence suggests vs. warrants more caveated language.
- **Plausible actions:** Brief the threat as originally framed by the senior officer; revise the framing based on team discussion; explicitly present dissenting views and lower confidence; request additional time before briefing.
- **Constraints and pressures:** Same-day briefing deadline, organizational hierarchy and deference norms, team cohesion pressure, senior decision-maker expectations for clear, confident assessments.
- **Consequences of error:** Overstated threat framing leading to disproportionate policy response vs. understated framing leaving decision-makers unprepared for a genuine threat.
- **Counterfactual causal variable:** Actual reliability of the senior officer's initial high-confidence report (later found to have been based on a single, uncorroborated source).
- **Expected interview structure:** Opening (team lead role context), Episode 1 (initial anchored review), Episode 2 (team discussion), Episode 3 (consensus-building and briefing decision), Closing (reflection on hierarchy, framing, and confidence).
- **Natural biases:** Authority Bias or Authority Obedience, Framing Effects, Groupthink, Overconfidence Bias, Anchoring Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** All-Source Analyst (overlaps with Interview 1; lacks the team-leadership and briefing-hierarchy elements needed for authority bias and groupthink).
- **Rejected alternative occupation 2:** Financial Crime Analyst (overlaps with Interview 4; less naturally tied to same-day briefing hierarchy dynamics).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Confirmation Bias, Complacency Bias, Explanation Bias, Fluency Effects, Mirror Imaging Bias, Order Effects
- **Selected occupation:** Cyber Threat Intelligence Analyst
- **Role and setting:** Technical analytic role in a security operations center or cyber threat intelligence unit; investigates network intrusions, correlates indicators of compromise, and attributes attacks to known threat actors using log data, malware analysis, and historical actor profiles; works individually with data-heavy tools under rapidly changing conditions. [armyprt](https://www.armyprt.com/mos/35-series-mos/)
- **Why this occupation fits the bias list:** Cyber threat analysts triage a high volume of recurring alerts (creating complacency risk), rely on familiar attacker profiles and analytic tools (fluency effects), construct attack narratives that then feel more probable once articulated (explanation bias), search for and interpret evidence favoring an initial attribution hypothesis (confirmation bias), infer attacker motive and behavior based on how the analyst's own organization would operate (mirror imaging), and review logs in a sequence that weights early or late entries disproportionately (order effects). All six mechanisms map cleanly onto distinct stages of the attribution workflow. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Primary CTA scenario:** Attributing a network intrusion to a known threat actor using a familiar analytic technique under time pressure; confirmation bias in attribution, complacency in recurring alert triage, explanation bias in attack narrative, fluency effects favoring familiar actor profile, mirror imaging in attacker motive, order effects in log review sequence.
- **Triggering event:** A cyber threat analyst is triaging a new alert that resembles a recurring low-severity pattern seen dozens of times before, but a closer log review reveals timeline anomalies suggesting a more sophisticated, unfamiliar actor.
- **Decision episodes:**
  1. Initial alert triage, informed by the recurring pattern and habitual review depth.
  2. Log review in the order captured, with early entries shaping the initial hypothesis.
  3. Attribution hypothesis formation based on a familiar, previously-encountered threat actor profile.
  4. Search for and interpretation of additional evidence, and construction of the final attack narrative for the incident report.
- **Available cues and evidence:** Historical alert pattern and triage outcomes, sequential log entries, indicators of compromise, known threat-actor behavioral profiles, timeline anomalies in the current incident, alternative less-familiar actor profiles not initially considered.
- **Competing interpretations:** The alert is consistent with the recurring low-severity pattern vs. represents a genuinely different, more capable actor; the familiar actor profile explains the behavior vs. an unfamiliar actor with different motives is responsible; early log entries are most diagnostic vs. later entries reveal the more significant anomaly.
- **Plausible actions:** Close the alert as a routine recurring pattern; escalate for deeper investigation; attribute to the familiar actor profile without further verification; explicitly test the attribution against an alternative actor profile.
- **Constraints and pressures:** High alert volume and limited time per case, established triage procedures reinforcing habitual depth of review, deadline for incident report, organizational reliance on the analyst's individual judgment.
- **Consequences of error:** Missed identification of a more sophisticated actor allowing continued compromise vs. unnecessary escalation consuming scarce investigative resources.
- **Counterfactual causal variable:** Actual identity and behavior pattern of the threat actor (later found to be a different, more capable actor mimicking the familiar low-severity pattern to avoid detection).
- **Expected interview structure:** Opening (cyber analyst role context), Episode 1 (initial triage), Episode 2 (log review sequence), Episode 3 (attribution hypothesis and evidence search), Closing (reflection on the six-stage reasoning process).
- **Natural biases:** Confirmation Bias, Complacency Bias, Explanation Bias, Fluency Effects, Mirror Imaging Bias, Order Effects.
- **Plausible but difficult biases:** None outright, but six biases require distribution across the four distinct decision episodes to avoid compression into a single point.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** SIGINT Analyst (overlaps with Interview 2; would create redundancy in the fluency-effects/explanation-bias mechanism already assigned there).
- **Rejected alternative occupation 2:** GEOINT Analyst (overlaps with Interview 3; would create redundancy in the mirror-imaging/order-effects mechanisms already assigned there).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Perceptual Bias, Wishful Thinking, Belief Bias, Selective Attention Bias, Planning Fallacy, Authority Bias or Authority Obedience, Framing Effects
- **Selected occupation:** Human Intelligence (HUMINT) Collection Manager/Reports Officer
- **Role and setting:** Analytic-operational role managing human source reporting; evaluates incoming source reports for reliability and significance, decides on follow-up tasking, and writes up assessments for downstream analysts and decision-makers; operates in a socially-mediated information environment shaped by source relationships and organizational hierarchy. [armyprt](https://www.armyprt.com/mos/35-series-mos/)
- **Why this occupation fits the bias list:** HUMINT reports officers interpret inherently ambiguous and socially-mediated source reporting, often want a valuable source's information to be reliable (wishful thinking), and must decide on tasking timelines. Perceptual bias (interpreting ambiguous source reporting through an expected lens), wishful thinking (about source reliability), belief bias (evaluating the source's argument by conclusion plausibility), selective attention bias (focusing on corroborating details), authority bias (deferring to a senior handler's assessment of the source), and framing effects (how the write-up presents the reporting) are all plausible in this context. Planning fallacy (underestimating the time needed to task and receive follow-up collection) is plausible but requires a distinct tasking-timeline episode to avoid feeling forced. [strathprints.strath.ac](https://strathprints.strath.ac.uk/76840/1/Belton_Dhami_RHBR_2020_Cognitive_biases_and_debiasing_in_intelligence_analysis.pdf)
- **Primary CTA scenario:** Evaluating a source's reporting on an impending event and deciding whether to task further collection; perceptual bias in interpreting ambiguous source reporting, wishful thinking about source reliability, belief bias in argument evaluation, selective attention to corroborating details, planning fallacy in tasking timeline, authority bias toward senior handler's assessment, framing effects in reporting write-up.
- **Triggering event:** A reports officer receives ambiguous reporting from a long-standing but recently less-productive source describing a possible impending event, alongside a senior handler's assessment vouching strongly for the source's continued reliability.
- **Decision episodes:**
  1. Initial interpretation of the ambiguous source reporting.
  2. Evaluation of source reliability, influenced by hope that the valuable relationship remains productive and by the senior handler's vouching assessment.
  3. Selective gathering of corroborating details from other reporting to support the write-up.
  4. Final write-up framing and tasking decision, including timeline estimate for follow-up collection.
- **Available cues and evidence:** The source's raw reporting, source reliability history, senior handler's assessment, partially corroborating and partially conflicting other reporting, organizational tasking procedures and typical turnaround times.
- **Competing interpretations:** The source's ambiguous reporting indicates a genuine impending event vs. is consistent with the source's recent decline in reliability; the senior handler's vouching assessment is well-founded vs. reflects handler attachment to a long-standing source; the tasking timeline is realistic vs. underestimates coordination and source-access constraints.
- **Plausible actions:** Write up the report with high confidence in the source; write up with explicit reliability caveats; task immediate follow-up collection; request an independent reliability review before further action.
- **Constraints and pressures:** Reporting deadlines, organizational deference to senior handlers, source-access limitations, downstream customer expectations for actionable reporting.
- **Consequences of error:** Overstated confidence in unreliable source reporting misdirecting downstream analysis vs. dismissing a genuinely significant report due to excessive caution.
- **Counterfactual causal variable:** Actual current reliability of the source (later found to have been compromised or coerced, contrary to the senior handler's assessment).
- **Expected interview structure:** Opening (reports officer role context), Episode 1 (initial interpretation), Episode 2 (reliability evaluation), Episode 3 (corroboration and write-up), Episode 4 (tasking timeline decision), Closing (reflection on source relationship and hierarchy).
- **Natural biases:** Perceptual Bias, Wishful Thinking, Belief Bias, Selective Attention Bias, Framing Effects.
- **Plausible but difficult biases:** Planning Fallacy (requires a distinct tasking-timeline episode), Authority Bias or Authority Obedience (requires a clear organizational hierarchy cue distinguishing it from simple trust in a colleague).
- **Biases that should not be forced:** None outright, but Authority Bias must be clearly tied to hierarchical deference rather than mere reliance on the handler's more direct source access (which would be legitimate information use, not bias).
- **Rejected alternative occupation 1:** Counterterrorism Analyst (overlaps with Interview 5; authority bias and framing effects already assigned there in a briefing context, risking mechanism duplication).
- **Rejected alternative occupation 2:** Financial Crime Analyst (overlaps with Interview 4; wishful thinking and planning fallacy already assigned there in a case-building context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (Authority Bias requires a clear organizational hierarchy cue distinct from Interview 5's team-lead/senior-officer dynamic; Planning Fallacy requires a distinct tasking-timeline episode to avoid feeling compressed into the reliability-evaluation episode)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations (strategic all-source, SIGINT, GEOINT, financial crime, counterterrorism team lead, cyber threat, HUMINT) | None | None | None | None needed |
| Work setting | Office-based individual analytic (1, 2, 3), Office-based cross-agency (4), Team/briefing (5), Data-heavy technical (6), Socially-mediated source relationship (7) | Office-based individual (3/7) | Office-based individual work | Field-based, public-facing | None critical; reflects the genuinely office/desk-bound nature of most intelligence analysis roles, though HUMINT (7) introduces a socially-mediated, relationship-based dimension not purely deskbound |
| Decision type | Monitoring/prioritization (1), Diagnosis/interpretation (2, 3), Case-building/forecasting (4), Risk assessment/team management (5), Diagnosis/attribution (6), Diagnosis/resource-tasking (7) | Diagnosis-type (4/7: 2, 3, 6, 7) | Diagnosis/interpretation | Negotiation, Design/creative judgment | None critical; diagnosis-type reasoning is the natural core of analytic work, but decision context (monitoring, case-building, team briefing, attribution, tasking) differs materially across each |
| Information environment | Rich/structured but sparse-signal (1), Perceptual/technical (2, 3), Data-heavy/regulated (4), Socially-mediated/team (5), Rapidly-changing/data-heavy (6), Socially-mediated/human-source (7) | Perceptual/technical (2/7) | Balanced | Conflicting-across-sources as primary driver | None critical |
| Time pressure | Low/moderate (1), Moderate (2, 3, 4), High (5, 6), Moderate (7) | Moderate (4/7) | Moderate | Very high/emergency | None critical; matches the generally non-emergency pace of analytic work outside crisis briefings |
| Consequence of error | Strategic/missed warning (1), Reporting accuracy (2, 3), Legal/operational disruption (4), Policy/reputational (5), Operational/cyber defense (6), Source/operational security (7) | None significant | None | Purely financial-only, purely environmental | None critical; good spread across strategic, legal, policy, operational, and security consequence types |
| Expertise level | Senior practitioner (1), Independent professional (2, 3, 6), Specialist (4), Supervisor/team lead (5), Independent/specialist (7) | Independent professional (3/7) | Independent professional | Developing practitioner | None critical; reflects the specialist nature of most named analytic disciplines |
| Stakeholder pattern | Individual work (1, 2, 3, 6), Cross-agency (4), Team/hierarchy (5), One-to-one source relationship (7) | Individual work (4/7) | Individual work | Multi-party negotiation | None critical; individual analytic work is the ecologically valid default for most named roles, with Interview 5 (team) and Interview 7 (source relationship) providing needed contrast |
| Scenario archetype | Steady-state monitoring (1), Intercept interpretation (2), Imagery interpretation (3), Case-building/disruption (4), Threat briefing (5), Intrusion attribution (6), Source evaluation/tasking (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Significance of a minor change (1), Correct intercept meaning (2), Foreign facility's actual doctrine (3), Network operational complexity (4), Reliability of initial report (5), Actual threat actor identity (6), Actual source reliability (7) | None significant | None | Equipment/technical failure as primary variable | None critical; all seven turn on a distinct, plausible causal fact |

**Overall assessment:** Strong diversity across occupations, decision types, information environments, and consequence profiles. All seven roles are grounded in real intelligence-community and adjacent (financial crime, cyber) disciplines rather than generic titles. Diagnosis/interpretation-type reasoning is common across four interviews, which is expected given the domain's inherent focus on interpreting ambiguous information, but each interview differs materially in information environment, stakeholder configuration, and causal structure. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Complacency Bias (clear mechanism: reduced vigilance after prolonged stability) | None | Complacency Bias (risk of being read as simply "a bad outcome after inaction") | None | None | None | Ensure the decision reasoning (workload trade-off, historical stability) is explicit and precedes the outcome; probe the analyst's stated rationale at the time, not just the result |
| 2 | Explanation Bias (imagining scenario increases perceived likelihood), Fluency Effects (preference for familiar technique/source) | Explanation Bias and Confirmation Bias (both involve favoring a constructed hypothesis) | None | None | None | None | Show the analyst explicitly considering the scenario before judging it more likely; show technique/source choice driven by familiarity, not merely by appropriateness |
| 3 | Mirror Imaging Bias (own-doctrine template), Order Effects (sequence-driven weighting), Perceptual Bias (ambiguity-driven interpretation) | Mirror Imaging and Perceptual Bias (both involve interpretation of ambiguous visual data) | None | None | Order Effects (sequence cue must be explicit, not incidental) | Order Effects | Make the review order and its influence on weighting explicit in the transcript; separate the doctrine-template reasoning (mirror imaging) from the general ambiguity-interpretation reasoning (perceptual bias) |
| 4 | Wishful Thinking (hope-driven interpretation), Belief Bias (plausibility-based argument evaluation), Selective Attention Bias (confirming-data focus), Planning Fallacy (timeline underestimation) | Wishful Thinking and Selective Attention (both involve favoring a preferred outcome), Belief Bias and Confirmation Bias (both involve evaluating evidence favorably) | None | None | None | None | Separate the desire for disruption success (wishful thinking) from the mechanics of evidence-gathering (selective attention); ensure planning fallacy is tied to a specific, quantifiable timeline estimate |
| 5 | Authority Bias, Framing Effects, Groupthink, Overconfidence Bias, Anchoring Bias (five distinct mechanisms) | Authority Bias and Groupthink (both involve social/hierarchical influence), Anchoring Bias and Authority Bias (both involve the first report's influence) | None | None | Groupthink (dissent-suppression must be explicit, not just consensus) | Groupthink | Show at least one team member's dissenting view being suppressed or discounted to distinguish groupthink from ordinary consensus; distinguish anchoring on the report's content from authority-based deference to the officer who delivered it |
| 6 | Confirmation Bias, Complacency Bias, Explanation Bias, Fluency Effects, Mirror Imaging Bias, Order Effects (six distinct mechanisms mapped to distinct workflow stages) | Complacency and Fluency Effects (both involve reduced scrutiny of familiar patterns), Confirmation Bias and Explanation Bias (both involve favoring a constructed hypothesis), Mirror Imaging and Confirmation Bias (both involve favoring an expected interpretation) | None | None | Complacency Bias (must be tied to the recurring-alert history, not just current inattention) | Mirror Imaging Bias (needs explicit own-organization behavioral comparison) | Distribute the six biases across the four decision episodes rather than compressing them into the attribution step alone; explicitly show the recurring-alert history for complacency and an explicit own-organization comparison for mirror imaging |
| 7 | Perceptual Bias, Wishful Thinking, Belief Bias, Selective Attention Bias, Framing Effects (five cleanly distinguishable) | Wishful Thinking and Selective Attention (both involve favoring source reliability), Authority Bias and legitimate reliance on handler's direct access (risk of conflating bias with reasonable information use), Planning Fallacy and ordinary uncertainty about tasking timelines | None | None | Authority Bias (must be tied to hierarchical deference, not mere trust in better-positioned information), Planning Fallacy (needs a distinct, quantifiable timeline estimate episode) | Authority Bias, Planning Fallacy | Add a clear cue that the officer defers to the handler's rank/seniority rather than the handler's superior access to source-specific information; add a distinct tasking-timeline estimation episode separate from the reliability evaluation to isolate Planning Fallacy |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interview 6, ensure all six biases are distributed across distinct decision episodes rather than compressed into a single attribution moment. For Interview 7, add an explicit hierarchical-deference cue for Authority Bias and a separate, quantifiable tasking-timeline episode for Planning Fallacy so neither bias is inferred merely from ambiguous trust or ordinary scheduling uncertainty. For Interview 5, ensure Groupthink includes an explicit suppressed dissenting view, distinguishing it from ordinary team agreement.
- **Prompt 2 (annotation):** Require annotators to cite the specific decision episode and observable cue for each coded bias, particularly for neighboring pairs (Complacency/Fluency in Interview 6; Wishful Thinking/Selective Attention in Interviews 4 and 7; Anchoring/Authority Bias in Interview 5). Flag any bias supported by only outcome knowledge (a bad result) rather than an articulated in-the-moment reasoning pattern, per the bias evaluation rules.
