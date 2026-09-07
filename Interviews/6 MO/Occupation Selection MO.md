## 1. Dataset allocation summary

| Interview | Requested bias count | Selected occupation | Primary scenario | Coverage | Raw overlap | Distinctness | Diversity contribution | Overall recommendation |
|-----------|----------------------|---------------------|------------------|----------|-------------|--------------|------------------------|------------------------|
| 1 | 1 | Harbor Pilot / Marine Pilot | Boarding a vessel for pilotage with an initial draft/tide estimate that later proves inaccurate; anchoring on first passage plan figure | 100% | 3 | High | Adds one-to-one advisory, high-autonomy, embodied navigation context | APPROVED |
| 2 | 2 | Third Officer / Watchkeeping Officer (Bridge Watch) | Monitoring ECDIS/radar during night watch in traffic separation scheme with automation alerts and limited recent contact history; automation bias in trusting ECDIS route check, availability bias from recent uneventful watches | 100% | 6 | High | Adds solitary watchkeeping, human-machine collaboration, night/low-visibility context | APPROVED |
| 3 | 3 | Vessel Traffic Service (VTS) Operator | Coordinating multiple vessel movements in congested channel with a developing conflict; confirmation bias in traffic prioritization, framing bias in risk communication, groupthink in control room team | 100% | 9 | High | Adds control room, team coordination, regulatory/safety context | APPROVED |
| 4 | 4 | Ship Master / Vessel Captain | Post-grounding review of anchorage decision during storm approach; hindsight bias in after-action review, inattentional blindness to weather cues, overconfidence in vessel handling, status quo bias in maintaining anchorage | 100% | 12 | High | Adds command authority, high-consequence, single-decision-maker context | APPROVED |
| 5 | 5 | Chief Engineer (Marine Engineering) | Deciding whether to continue running degraded main engine vs. shutting down for repair mid-voyage; sunk cost in prior repair investment, automation bias in engine monitoring system, inattentional blindness to secondary alarms, hindsight bias in past decisions | 100% | 15 | High | Adds engine room, technical/mechanical, individual work with automated systems context | APPROVED |
| 6 | 6 | Port Captain / Terminal Operations Manager | Deciding whether to maintain existing berthing schedule despite emerging weather risk; status quo bias in schedule adherence, framing bias in risk presentation, groupthink in operations meeting, overconfidence in weather forecast reliability, anchoring on original schedule | 100% | 18 | High | Adds shore-based management, multi-stakeholder, resource allocation context | APPROVED |
| 7 | 7 | Dynamic Positioning Operator (Offshore Support Vessel) | Managing DP system fault during critical offshore operation alongside platform; confirmation bias in fault diagnosis, automation bias in DP system trust, inattentional blindness to secondary indicators, hindsight bias in review, sunk cost in continuing operation, status quo bias in maintaining position mode, framing bias in risk communication to bridge team | 86% | 19 | Moderate-High | Adds specialized technical operator, human-machine collaboration, high-consequence offshore context | APPROVED_WITH_CAVEATS (duplicate Overconfidence in Interview 6 list requires handling; DP role fits Interview 7 well) |

***

## 2. Candidate occupation matrix

### Interview 1 (Anchoring Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Harbor Pilot / Marine Pilot | 1 (Anchoring) | 0 | 0 | 0 | 100% | High (single bias, clear mechanism) | High (passage planning phases) | High (change tide/draft data accuracy) | High | High (adds one-to-one advisory, embodied navigation) | 0.88 |
| Ship Master | 1 | 0 | 0 | 0 | 100% | High | High | High | High | Medium (overlaps with Interview 4) | 0.76 |
| VTS Operator | 0 | 1 | 0 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 3) | 0.60 |
| Watchkeeping Officer | 0 | 1 | 0 | 0 | 50% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.56 |
| Chief Engineer | 0 | 0 | 1 | 0 | 25% | Low | Moderate | Moderate | High | Medium | 0.45 |

**Selected:** Harbor Pilot / Marine Pilot (best coverage, distinctness, diversity fit).

***

### Interview 2 (Automation Bias, Availability Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Third Officer / Watchkeeping Officer | 2 (Automation, Availability) | 0 | 0 | 0 | 100% | High (two distinct mechanisms) | High (watch phases, ECDIS/radar monitoring) | High (change ECDIS alert accuracy) | High | High (adds solitary watchkeeping, human-machine role) | 0.90 |
| VTS Operator | 1 | 1 | 0 | 0 | 75% | High | High | High | High | Medium (overlaps with Interview 3) | 0.76 |
| Dynamic Positioning Operator | 1 | 1 | 0 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 7) | 0.68 |
| Chief Engineer | 1 | 0 | 1 | 0 | 50% | Moderate | High | High | High | Low (overlaps with Interview 5) | 0.55 |
| Ship Master | 0 | 1 | 1 | 0 | 50% | Moderate | High | High | High | Low | 0.52 |

**Selected:** Third Officer / Watchkeeping Officer (best coverage, distinctness, diversity fit).

***

### Interview 3 (Confirmation Bias, Framing Bias, Groupthink)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Vessel Traffic Service (VTS) Operator | 3 (Confirmation, Framing, Groupthink) | 0 | 0 | 0 | 100% | High (three distinct mechanisms) | High (control room phases, team coordination) | High (change traffic conflict data accuracy) | High | High (adds control room, team decision-making role) | 0.92 |
| Port Captain | 2 | 1 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 6) | 0.78 |
| Ship Master | 2 | 1 | 0 | 0 | 83% | Moderate-High | High | High | High | Low (overlaps with Interview 4) | 0.70 |
| DP Operator | 2 | 1 | 0 | 0 | 83% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.68 |
| Watchkeeping Officer | 1 | 2 | 0 | 0 | 75% | Moderate | Moderate | Moderate | High | Low (overlaps with Interview 2) | 0.60 |

**Selected:** VTS Operator (best coverage, distinctness, diversity fit).

***

### Interview 4 (Hindsight Bias, Inattentional Blindness, Overconfidence Bias, Status Quo Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Ship Master / Vessel Captain | 4 (Hindsight, Inattentional Blindness, Overconfidence, Status Quo) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (command decision phases, high stakes) | High (change weather forecast accuracy) | High | High (adds command authority, single-decision-maker role) | 0.94 |
| Harbor Pilot | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 1) | 0.80 |
| Chief Engineer | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium | 0.78 |
| Port Captain | 2 | 2 | 0 | 0 | 80% | High | High | High | High | Low (overlaps with Interview 6) | 0.72 |
| VTS Operator | 2 | 1 | 1 | 0 | 75% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.65 |

**Selected:** Ship Master / Vessel Captain (best coverage, distinctness, scenario richness).

***

### Interview 5 (Sunk Cost Bias, Automation Bias, Inattentional Blindness, Hindsight Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Chief Engineer (Marine Engineering) | 4 (Sunk Cost, Automation, Inattentional Blindness, Hindsight) | 0 | 0 | 0 | 100% | High (four distinct mechanisms) | High (engine room monitoring, repair decision phases) | High (change engine sensor data accuracy) | High | High (adds engine room, technical/mechanical role) | 0.94 |
| Ship Master | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 4) | 0.82 |
| DP Operator | 3 | 1 | 0 | 0 | 90% | High | High | High | High | Low (overlaps with Interview 7) | 0.76 |
| Watchkeeping Officer | 2 | 2 | 0 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.68 |
| Port Captain | 2 | 1 | 1 | 0 | 75% | Moderate | High | High | High | Low (overlaps with Interview 6) | 0.62 |

**Selected:** Chief Engineer (best coverage, distinctness, diversity fit).

***

### Interview 6 (Status Quo Bias, Framing Bias, Groupthink, Overconfidence Bias x2, Anchoring Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Port Captain / Terminal Operations Manager | 5 (Status Quo, Framing, Groupthink, Overconfidence x2, Anchoring) | 0 | 0 | 0 | 100% | High (five distinct mechanisms; Overconfidence appears twice but embeddable in separate episodes) | High (scheduling meeting phases, multi-stakeholder) | High (change weather forecast accuracy) | High | High (adds shore-based management, resource allocation role) | 0.94 |
| VTS Operator | 4 | 1 | 0 | 0 | 90% | High | High | High | High | Medium (overlaps with Interview 3) | 0.82 |
| Ship Master | 3 | 2 | 0 | 0 | 83% | High | High | High | High | Medium (overlaps with Interview 4) | 0.75 |
| Harbor Pilot | 3 | 1 | 1 | 0 | 80% | Moderate-High | High | High | High | Low (overlaps with Interview 1) | 0.70 |
| DP Operator | 2 | 2 | 1 | 0 | 80% | Moderate | High | High | High | Low (overlaps with Interview 7) | 0.65 |

**Selected:** Port Captain / Terminal Operations Manager (best coverage, distinctness, diversity fit).

***

### Interview 7 (Confirmation Bias, Automation Bias, Inattentional Blindness, Hindsight Bias, Sunk Cost Bias, Status Quo Bias, Framing Bias)

| Candidate occupation | Natural matches | Plausible matches | Weak matches | Unsuitable matches | Coverage score | Distinctness | Scenario richness | Counterfactual suitability | Realism | Diversity fit | Composite score |
|----------------------|-----------------|-------------------|--------------|---------------------|----------------|--------------|-------------------|---------------------------|---------|---------------|-----------------|
| Dynamic Positioning Operator (Offshore Support Vessel) | 5 (Confirmation, Automation, Inattentional Blindness, Hindsight, Framing) | 2 (Sunk Cost, Status Quo) | 0 | 0 | 100% | Moderate-High (seven mechanisms; requires careful episode separation) | High (DP fault management phases, multiple decision points) | High (change DP sensor/reference data accuracy) | High | High (adds specialized technical operator, human-machine role) | 0.88 |
| Chief Engineer | 5 | 2 | 0 | 0 | 100% | Moderate-High | High | High | High | Low (overlaps with Interview 5) | 0.78 |
| Watchkeeping Officer | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 2) | 0.72 |
| VTS Operator | 4 | 2 | 1 | 0 | 86% | Moderate-High | High | High | High | Low (overlaps with Interview 3) | 0.74 |
| Ship Master | 4 | 2 | 1 | 0 | 86% | Moderate | High | High | High | Low (overlaps with Interview 4) | 0.70 |

**Selected:** Dynamic Positioning Operator (best diversity fit, adds specialized technical role; seven-bias list requires careful design).

***

## 3. Final occupation and scenario recommendations

### Interview 1

- **Requested biases:** Anchoring Bias
- **Selected occupation:** Harbor Pilot / Marine Pilot
- **Role and setting:** Licensed maritime pilot boarding vessels to guide navigation through harbors, channels, and confined waters; advises the master, does not have command authority, works in short high-intensity engagements per vessel.
- **Why this occupation fits the bias list:** Pilots form an initial mental model of a passage (tide, draft clearance, traffic) before boarding, based on the latest available data. Anchoring bias (over-reliance on this initial figure despite subsequent updates) is a well-documented mechanism in pilotage error analysis, particularly around under-keel clearance and berth approach speed. [abs.gov](https://www.abs.gov.au/book/export/42669/print)
- **Primary CTA scenario:** Boarding a vessel for pilotage with an initial draft/tide estimate that later proves inaccurate; anchoring on first passage plan figure.
- **Triggering event:** Pilot boards a vessel using a pre-arrival draft and tide estimate; shortly before the critical channel transit, updated tide data becomes available showing less under-keel clearance than originally planned.
- **Decision episodes:**
  1. Initial passage plan review and draft/tide estimate before boarding.
  2. Bridge team briefing and confirmation of initial figures.
  3. Updated tide/draft data received during transit approach.
  4. Final decision on proceeding, adjusting speed, or delaying transit.
- **Available cues and evidence:** Pre-arrival draft survey, tide tables, updated tide gauge readings, vessel's actual draft on arrival, under-keel clearance calculations, master's input.
- **Competing interpretations:** Initial estimate remains valid vs. updated data requires plan revision; margin is sufficient vs. margin has eroded.
- **Plausible actions:** Proceed as originally planned; adjust speed or timing based on updated tide; delay transit to next suitable tide window; request additional under-keel clearance survey.
- **Constraints and pressures:** Tide window timing, vessel schedule commitments, berth availability, port traffic coordination, safety margins required by port authority.
- **Consequences of error:** Grounding or contact risk if margin is overestimated vs. unnecessary delay and cost if overly conservative.
- **Counterfactual causal variable:** Actual under-keel clearance at time of transit (later found that clearance was tighter than either estimate suggested due to localized siltation).
- **Expected interview structure:** Opening (pilot role context), Episode 1 (initial estimate), Episode 2 (bridge briefing), Episode 3 (updated data and decision), Closing (reflection on estimate revision).
- **Natural biases:** Anchoring Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Ship Master (would overlap with Interview 4; less natural for anchoring in single-transit advisory context).
- **Rejected alternative occupation 2:** VTS Operator (overlaps with Interview 3; less natural for anchoring in individual passage-planning context).
- **Recommendation status:** APPROVED

***

### Interview 2

- **Requested biases:** Automation Bias, Availability Bias
- **Selected occupation:** Third Officer / Watchkeeping Officer (Bridge Watch)
- **Role and setting:** Bridge watchkeeping role on merchant vessel; maintains solitary or lightly-assisted watch using ECDIS, radar/ARPA, AIS, and lookout, responsible for collision avoidance and route monitoring during assigned watch period.
- **Why this occupation fits the bias list:** Watchkeeping officers rely heavily on ECDIS route-checking alerts and radar/ARPA target tracking. Automation bias (over-trusting automated route-check or CPA/TCPA alerts) and availability bias (judging risk based on recent uneventful watches) are well-documented mechanisms in bridge resource management literature. [research.chalmers](https://research.chalmers.se/publication/501540/file/501540_Fulltext.pdf)
- **Primary CTA scenario:** Monitoring ECDIS/radar during night watch in traffic separation scheme with automation alerts and limited recent contact history; automation bias in trusting ECDIS route check, availability bias from recent uneventful watches.
- **Triggering event:** Third officer stands night watch in a traffic separation scheme; ECDIS has flagged no route conflicts, and the past several watches have been uneventful, but a crossing vessel's AIS data is inconsistent with its radar-tracked course.
- **Decision episodes:**
  1. Initial watch handover and situational assessment.
  2. ECDIS/radar monitoring and alert interpretation.
  3. Evaluation of AIS-radar discrepancy for the crossing vessel.
  4. Final decision on collision avoidance action or continued monitoring.
- **Available cues and evidence:** ECDIS route-check status, radar/ARPA tracked course and CPA/TCPA, AIS reported course and speed, visual lookout observations, recent watch history, weather and visibility conditions.
- **Competing interpretations:** ECDIS "no conflict" status is reliable vs. requires independent verification; AIS discrepancy is a data error vs. genuine course change; recent uneventful watches support continued routine monitoring vs. current situation is different.
- **Plausible actions:** Continue monitoring per ECDIS guidance; take early avoiding action based on radar; contact vessel via VHF to clarify intentions; call master to bridge.
- **Constraints and pressures:** Solitary watch workload, fatigue, low visibility conditions, radio communication reliability, company/master expectations for autonomous watchkeeping competence.
- **Consequences of error:** Unnecessary early avoiding action affecting schedule vs. delayed recognition of genuine collision risk.
- **Counterfactual causal variable:** Actual cause of AIS-radar discrepancy (later found that the crossing vessel's AIS was misconfigured; radar track was accurate and indicated closing risk).
- **Expected interview structure:** Opening (watchkeeper role context), Episode 1 (watch handover), Episode 2 (monitoring and alert interpretation), Episode 3 (discrepancy evaluation and action), Closing (reflection on reliance on automation and recent experience).
- **Natural biases:** Automation Bias, Availability Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** VTS Operator (overlaps with Interview 3; less natural for automation bias in individual bridge watch context).
- **Rejected alternative occupation 2:** DP Operator (overlaps with Interview 7; less natural for availability bias in DP-specific context).
- **Recommendation status:** APPROVED

***

### Interview 3

- **Requested biases:** Confirmation Bias, Framing Bias, Groupthink
- **Selected occupation:** Vessel Traffic Service (VTS) Operator
- **Role and setting:** Shore-based control room role; monitors and coordinates vessel movements within a port or harbor area using radar, AIS, CCTV, and VHF; works as part of a VTS team, communicates with pilots, masters, and port stakeholders. [portskillsandsafety.co](https://www.portskillsandsafety.co.uk/knowledge-hub/vessel-traffic-services-operations-nos/)
- **Why this occupation fits the bias list:** VTS operators work in team-based control rooms making real-time traffic prioritization decisions with radio communication. Confirmation bias (seeking data supporting initial traffic plan), framing bias (how risk is communicated to vessels or supervisors), and groupthink (control room team consensus without challenge) are all well-documented mechanisms in VTS and bridge team literature. [safety4sea](https://safety4sea.com/wp-content/uploads/2019/09/CHIRP-Making-critical-decisions-at-sea-2019_09.pdf)
- **Primary CTA scenario:** Coordinating multiple vessel movements in congested channel with a developing conflict; confirmation bias in traffic prioritization, framing bias in risk communication, groupthink in control room team.
- **Triggering event:** VTS operator is managing three vessels approaching a narrow channel simultaneously; the operator's initial traffic sequencing plan is challenged by a late-arriving report of reduced visibility from one vessel.
- **Decision episodes:**
  1. Initial traffic sequencing plan development.
  2. Monitoring for confirming or disconfirming information as vessels approach.
  3. Team discussion in control room on sequencing risk and possible changes.
  4. Final decision on maintaining or revising sequencing and communication to vessels.
- **Available cues and evidence:** Radar/AIS vessel tracks, VHF reports from vessels, visibility reports, colleague input in control room, port traffic rules, historical channel transit patterns.
- **Competing interpretations:** Original sequencing plan remains safe vs. requires revision due to visibility; team consensus reflects sound judgment vs. groupthink suppressing dissent; risk framing to vessels is appropriately cautious vs. downplayed.
- **Plausible actions:** Maintain original sequencing; revise sequencing and issue new instructions; hold one vessel outside the channel; escalate to supervisor for a second opinion.
- **Constraints and pressures:** Channel capacity constraints, vessel schedule pressures, team workload, regulatory reporting requirements, safety margins mandated by port authority.
- **Consequences of error:** Unnecessary vessel delays affecting port throughput vs. increased collision or grounding risk in the channel.
- **Counterfactual causal variable:** Actual visibility conditions at time of transit (later found that visibility was more degraded than the late report suggested, and original sequencing carried higher risk than assessed).
- **Expected interview structure:** Opening (VTS operator role context), Episode 1 (initial sequencing), Episode 2 (monitoring for new information), Episode 3 (team discussion and decision), Closing (reflection on team dynamics and information use).
- **Natural biases:** Confirmation Bias, Framing Bias, Groupthink.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Port Captain (overlaps with Interview 6; less natural for confirmation bias in real-time traffic control context).
- **Rejected alternative occupation 2:** Ship Master (overlaps with Interview 4; less natural for groupthink in shore-based team context).
- **Recommendation status:** APPROVED

***

### Interview 4

- **Requested biases:** Hindsight Bias, Selective Attention Bias or Inattentional Blindness, Overconfidence Bias, Status Quo Bias
- **Selected occupation:** Ship Master / Vessel Captain
- **Role and setting:** Command role aboard a merchant vessel; holds ultimate authority and responsibility for vessel safety, navigation decisions, and crew; makes high-consequence decisions often alone or with limited real-time external consultation.
- **Why this occupation fits the bias list:** Ship masters exercise sole command authority and are subject to intense post-incident scrutiny. Hindsight bias (in after-action reviews of anchorage decisions), inattentional blindness (missing weather cues while focused on other tasks), overconfidence bias (in vessel handling capability), and status quo bias (maintaining current anchorage despite deteriorating conditions) are all well-documented in maritime casualty investigations. [nap.nationalacademies](https://nap.nationalacademies.org/read/2055/chapter/9)
- **Primary CTA scenario:** Post-grounding review of anchorage decision during storm approach; hindsight bias in after-action review, inattentional blindness to weather cues, overconfidence in vessel handling, status quo bias in maintaining anchorage.
- **Triggering event:** Master decides to remain at anchorage as a storm approaches, based on holding ground assessment and vessel's engine readiness; conditions deteriorate faster than forecast.
- **Decision episodes:**
  1. Initial anchorage risk assessment as storm forecast develops.
  2. Monitoring of weather and vessel position with competing demands on attention (cargo operations, crew management).
  3. Re-assessment as conditions worsen and consideration of weighing anchor.
  4. Final decision to remain at anchor vs. get underway, and subsequent review after grounding/near-miss.
- **Available cues and evidence:** Weather forecasts and updates, anchor holding ground data, engine readiness status, vessel drift indicators, crew reports, similar past anchorage experiences.
- **Competing interpretations:** Current anchorage remains safe vs. requires relocation; vessel's handling capability is sufficient to manage conditions vs. requires early departure; forecast deterioration is gradual vs. accelerating faster than models predict.
- **Plausible actions:** Remain at anchor with increased monitoring; weigh anchor and seek sea room; request tug assistance; relocate to more sheltered anchorage.
- **Constraints and pressures:** Engine readiness time, crew fatigue, cargo operation commitments, other vessels in anchorage, communication with port authority.
- **Consequences of error:** Unnecessary early departure affecting schedule and cargo operations vs. grounding, anchor dragging, or collision with other vessels in deteriorating conditions.
- **Counterfactual causal variable:** Actual rate of weather deterioration (later found that the storm intensified faster than any available forecast indicated, though certain visual cues were present earlier).
- **Expected interview structure:** Opening (master role context), Episode 1 (initial risk assessment), Episode 2 (monitoring amid competing demands), Episode 3 (re-assessment and decision), Closing (reflection on post-incident review process).
- **Natural biases:** Hindsight Bias, Selective Attention Bias or Inattentional Blindness, Overconfidence Bias, Status Quo Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Harbor Pilot (overlaps with Interview 1; less natural for status quo bias given pilots' short engagement per vessel).
- **Rejected alternative occupation 2:** Chief Engineer (overlaps with Interview 5; less natural for command-level anchorage decision authority).
- **Recommendation status:** APPROVED

***

### Interview 5

- **Requested biases:** Sunk Cost Bias, Automation Bias, Selective Attention Bias or Inattentional Blindness, Hindsight Bias
- **Selected occupation:** Chief Engineer (Marine Engineering)
- **Role and setting:** Senior technical role in the engine room; responsible for main engine, auxiliary machinery, and technical systems; makes maintenance and operational continuity decisions often under time and resource constraints mid-voyage.
- **Why this occupation fits the bias list:** Chief engineers make continue-vs-repair decisions on machinery with prior maintenance investment, automated monitoring systems, and competing alarm priorities. Sunk cost bias (continuing operation due to prior repair investment), automation bias (over-trusting engine monitoring/alarm systems), inattentional blindness (missing secondary alarms while focused on primary fault), and hindsight bias (in reviewing past decisions) are all well-documented in marine engineering incident analysis. [research.chalmers](https://research.chalmers.se/publication/501540/file/501540_Fulltext.pdf)
- **Primary CTA scenario:** Deciding whether to continue running degraded main engine vs. shutting down for repair mid-voyage; sunk cost in prior repair investment, automation bias in engine monitoring system, inattentional blindness to secondary alarms, hindsight bias in past decisions.
- **Triggering event:** Chief engineer detects abnormal readings on the main engine following a recent repair; engine monitoring system shows parameters within acceptable range, but a secondary alarm for a different subsystem is also active.
- **Decision episodes:**
  1. Initial abnormal reading assessment and monitoring system review.
  2. Consideration of recent repair investment and its expected effect.
  3. Attention allocation between primary engine parameters and secondary alarm.
  4. Final decision on continuing operation, reducing load, or shutting down for repair.
- **Available cues and evidence:** Engine monitoring system readouts, alarm log, recent repair records and cost, vessel schedule and position, weather conditions, spare parts availability, past similar incidents.
- **Competing interpretations:** Abnormal readings are within monitoring system's acceptable tolerance vs. indicate developing failure; recent repair investment justifies continued operation vs. sunk cost should not influence current decision; secondary alarm is unrelated vs. connected to primary issue.
- **Plausible actions:** Continue operation at current load; reduce engine load and continue monitoring; shut down for immediate repair; divert to nearest port for repair.
- **Constraints and pressures:** Voyage schedule, repair cost already incurred, spare parts and repair facility availability, weather and sea conditions, crew fatigue, safety requirements.
- **Consequences of error:** Unnecessary shutdown causing schedule delay and cost vs. continued operation leading to engine failure or more severe damage.
- **Counterfactual causal variable:** Actual relationship between the secondary alarm and the primary engine issue (later found that the secondary alarm indicated a developing fault directly connected to the abnormal primary readings).
- **Expected interview structure:** Opening (chief engineer role context), Episode 1 (initial assessment), Episode 2 (repair investment consideration), Episode 3 (attention allocation and decision), Closing (reflection on decision process and review).
- **Natural biases:** Sunk Cost Bias, Automation Bias, Selective Attention Bias or Inattentional Blindness, Hindsight Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** None.
- **Rejected alternative occupation 1:** Ship Master (overlaps with Interview 4; less natural for sunk cost in technical repair-investment context).
- **Rejected alternative occupation 2:** DP Operator (overlaps with Interview 7; less natural for hindsight bias in engine-specific maintenance context).
- **Recommendation status:** APPROVED

***

### Interview 6

- **Requested biases:** Status Quo Bias, Framing Bias, Groupthink, Overconfidence Bias, Overconfidence Bias, Anchoring Bias
- **Selected occupation:** Port Captain / Terminal Operations Manager
- **Role and setting:** Shore-based management role overseeing port/terminal operations; coordinates berthing schedules, liaises with shipping lines, pilots, and terminal staff; leads operational planning meetings with multiple stakeholders.
- **Why this occupation fits the bias list:** Port captains lead scheduling and risk meetings involving multiple stakeholders with competing priorities. Status quo bias (maintaining existing schedule), framing bias (how weather risk is presented), groupthink (team consensus in operations meetings), overconfidence bias (in forecast reliability, appearing twice in the list and embeddable in two distinct episodes — forecast confidence and schedule-adherence confidence), and anchoring bias (on the original schedule) are all well-documented in port operations management. Note: the requested list contains "Overconfidence Bias" twice; this is treated as one bias with two potential manifestation points rather than two separate biases, per the duplicate-handling guidance.
- **Primary CTA scenario:** Deciding whether to maintain existing berthing schedule despite emerging weather risk; status quo bias in schedule adherence, framing bias in risk presentation, groupthink in operations meeting, overconfidence in weather forecast reliability, anchoring on original schedule.
- **Triggering event:** Port captain holds a daily operations meeting; a marginal weather deterioration forecast for the following day threatens the existing berthing schedule for several vessels, but the schedule was set a week in advance and stakeholders have made downstream commitments.
- **Decision episodes:**
  1. Initial schedule review anchored to the original weekly plan.
  2. Weather forecast presentation and risk framing in the operations meeting.
  3. Team discussion and consensus-building on schedule adherence.
  4. Final decision on maintaining, adjusting, or delaying the berthing schedule.
- **Available cues and evidence:** Original berthing schedule, updated weather forecast, historical forecast accuracy, stakeholder commitments (shipping lines, terminal, pilots), team input in meeting, past experience with similar forecasts.
- **Competing interpretations:** Original schedule remains appropriate vs. requires revision; forecast is reliable enough to act on vs. too uncertain to justify disruption; team consensus reflects genuine agreement vs. groupthink suppressing concerns.
- **Plausible actions:** Maintain schedule as planned; adjust berthing sequence or timing; delay specific vessel operations; request additional weather routing advice.
- **Constraints and pressures:** Stakeholder commitments and contractual penalties, terminal capacity, pilot and tug availability, safety margins required by port authority, meeting time constraints.
- **Consequences of error:** Unnecessary schedule disruption causing financial and reputational cost vs. proceeding into hazardous conditions leading to vessel or terminal damage.
- **Counterfactual causal variable:** Actual weather severity at the scheduled time (later found that conditions were more severe than forecast, and the original schedule carried more risk than the team assessed).
- **Expected interview structure:** Opening (port captain role context), Episode 1 (schedule review), Episode 2 (risk presentation), Episode 3 (team discussion and decision), Closing (reflection on schedule adherence and forecast trust).
- **Natural biases:** Status Quo Bias, Framing Bias, Groupthink, Overconfidence Bias, Anchoring Bias.
- **Plausible but difficult biases:** None.
- **Biases that should not be forced:** A second, independent instance of Overconfidence Bias (the list's duplicate should not be treated as a distinct sixth bias; see integrity audit).
- **Rejected alternative occupation 1:** VTS Operator (overlaps with Interview 3; less natural for schedule-level status quo bias).
- **Rejected alternative occupation 2:** Ship Master (overlaps with Interview 4; less natural for multi-stakeholder scheduling context).
- **Recommendation status:** APPROVED

***

### Interview 7

- **Requested biases:** Confirmation Bias, Automation Bias, Selective Attention Bias or Inattentional Blindness, Hindsight Bias, Sunk Cost Bias, Status Quo Bias, Framing Bias
- **Selected occupation:** Dynamic Positioning Operator (Offshore Support Vessel)
- **Role and setting:** Specialized technical bridge role on offshore support/supply vessels; operates the Dynamic Positioning (DP) system to maintain vessel position and heading during operations alongside platforms or other vessels; works in close human-machine collaboration with high consequence of error.
- **Why this occupation fits the bias list:** DP operators manage a highly automated system with multiple reference sensors and must diagnose faults in real time while maintaining position near valuable and hazardous infrastructure. Confirmation bias (in fault diagnosis), automation bias (trusting the DP system's automatic reference-checking), inattentional blindness (missing secondary indicators), hindsight bias (in post-incident review), sunk cost bias (continuing operation given time/resources already invested), status quo bias (maintaining current position-keeping mode), and framing bias (in risk communication to the bridge team) are all well-documented in DP incident investigations, though seven mechanisms require careful separation into distinct episodes. [research.chalmers](https://research.chalmers.se/publication/501540/file/501540_Fulltext.pdf)
- **Primary CTA scenario:** Managing DP system fault during critical offshore operation alongside platform; confirmation bias in fault diagnosis, automation bias in DP system trust, inattentional blindness to secondary indicators, hindsight bias in review, sunk cost in continuing operation, status quo bias in maintaining position mode, framing bias in risk communication to bridge team.
- **Triggering event:** DP operator is holding position alongside an offshore platform during a critical cargo transfer when one position reference system begins showing a discrepancy with the others; the operation is partway through and stopping would require re-establishing position later.
- **Decision episodes:**
  1. Initial fault indication and reference system discrepancy assessment.
  2. Diagnosis process weighing which reference systems to trust.
  3. Consideration of operation progress and cost of aborting versus continuing.
  4. Final decision on continuing, switching reference systems, or aborting and communication to bridge team and platform.
- **Available cues and evidence:** DP system reference sensor readings (DGPS, taut wire, HPR), consequence model outputs, weather and current data, operation progress status, bridge team input, platform communications, past similar fault experiences.
- **Competing interpretations:** Discrepancy reflects a genuine reference system fault requiring action vs. transient sensor noise; current operation should continue given progress made vs. should be aborted given fault uncertainty; DP system's automatic weighting of references is reliable vs. requires manual override.
- **Plausible actions:** Continue operation on remaining reliable references; switch primary reference system; reduce operational tempo and increase monitoring; abort operation and move off station.
- **Constraints and pressures:** Operation time pressure, proximity to platform structure, weather and current conditions, cost of aborting and re-establishing position, bridge team workload, regulatory DP operational limits.
- **Consequences of error:** Unnecessary operation abort causing schedule and cost impact vs. loss of position control leading to collision with platform or dropped load.
- **Counterfactual causal variable:** Actual cause of the reference discrepancy (later found that one reference system had a genuine positioning error that, combined with the automatic weighting algorithm, produced a blended position estimate that was subtly wrong).
- **Expected interview structure:** Opening (DP operator role context), Episode 1 (fault indication), Episode 2 (diagnosis and reference evaluation), Episode 3 (continue/abort decision and communication), Closing (reflection on decision process and post-incident review).
- **Natural biases:** Confirmation Bias, Automation Bias, Selective Attention Bias or Inattentional Blindness, Framing Bias.
- **Plausible but difficult biases:** Hindsight Bias, Sunk Cost Bias, Status Quo Bias (all plausible but require careful separation from the fault-diagnosis episode to avoid conflation).
- **Biases that should not be forced:** None outright, but the seven-bias list requires distributing mechanisms across distinct sub-episodes rather than compressing all into one decision point.
- **Rejected alternative occupation 1:** Chief Engineer (overlaps with Interview 5; less natural for confirmation bias in real-time positioning context).
- **Rejected alternative occupation 2:** Ship Master (overlaps with Interview 4; less natural for automation bias in DP-specific technical context).
- **Recommendation status:** APPROVED_WITH_CAVEATS (seven-bias list requires careful episode separation; risk of conflating Sunk Cost, Status Quo, and Hindsight if not designed carefully)

***

## 4. Cross-interview diversity audit

| Dimension | Variation across interviews | Repetitions | Overrepresented categories | Underrepresented categories | Recommended substitutions |
|-----------|-----------------------------|-------------|---------------------------|-----------------------------|---------------------------|
| Occupation | 7 distinct occupations | None | None | None | None needed |
| Work setting | Embodied/on-vessel advisory (1), Bridge watch (2), Shore control room (3), Command bridge (4), Engine room (5), Shore office/meeting (6), Offshore bridge/technical (7) | None significant | None | Purely office-based analytical | None critical; good spread across afloat/ashore/technical |
| Decision type | Planning/anchoring (1), Monitoring (2), Coordination (3), Risk assessment/command (4), Troubleshooting/repair (5), Planning/scheduling (6), Fault diagnosis/emergency (7) | None significant | None | Negotiation, Personnel management | None critical |
| Information environment | Rich/structured (1), Data-heavy/software-mediated (2, 7), Socially mediated/team (3, 6), Perceptual/experiential (4), Technical/instrumented (5) | Data-heavy (3/7) | Data-heavy | Regulated/documentation-heavy as primary | None critical; reflects maritime information mix |
| Time pressure | Moderate (1, 5, 6), High (2, 3, 4, 7) | High (4/7) | High time pressure | Low time pressure | None critical; maritime operations are inherently time-sensitive |
| Consequence of error | Safety (1, 2, 3, 4, 7), Operational (5, 6), Financial (6), Environmental (1, 4, 7) | Safety (5/7) | Safety | Educational, Purely reputational | None critical; reflects maritime consequence profile |
| Expertise level | Specialist/licensed (1, 7), Independent professional (2), Senior practitioner (3), Decision authority (4), Specialist technical (5), Supervisor/manager (6) | None significant | None | Developing practitioner | None needed |
| Stakeholder pattern | One-to-one advisory (1), Individual with tools (2, 5), Team coordination (3, 7), Sole command (4), Multi-party (6) | None significant | None | Public-facing interaction | None critical |
| Scenario archetype | Passage-plan revision (1), Watch monitoring (2), Traffic sequencing (3), Anchorage/storm (4), Engine continue/repair (5), Schedule/weather (6), DP fault (7) | None significant | None | Negotiation-driven | None critical |
| Causal-counterfactual structure | Tide/draft data (1), AIS/radar discrepancy (2), Visibility report (3), Weather deterioration rate (4), Alarm-fault linkage (5), Weather severity (6), Reference sensor fault (7) | Weather-related (2/7: 4, 6) | Weather | Human performance/fatigue as primary variable | None critical |

**Overall assessment:** Strong diversity across occupations, settings, decision types, and consequence profiles. The set spans embodied advisory work, solitary watchkeeping, shore-based team coordination, sole command authority, technical engineering, management, and specialized offshore operations — avoiding overconcentration in any single professional type or setting. No critical substitutions needed.

***

## 5. Bias-integrity audit

| Interview | Biases independently distinguishable | Bias pairs risking conflation | Biases risking outcome bias | Biases risking hindsight bias | Biases with weak cues | Biases requiring stronger scenario | Recommended safeguards |
|-----------|-------------------------------------|-------------------------------|-----------------------------|-------------------------------|-----------------------|-----------------------------------|------------------------|
| 1 | Anchoring Bias (clear mechanism: initial estimate persistence) | None | None | None | None | None | Ensure updated data clearly contradicts initial estimate; probe reasoning behind not revising |
| 2 | Automation Bias (trust in ECDIS/alerts), Availability Bias (recent uneventful watches) | None | None | None | None | None | Provide clear automated alert and a distinct recent-experience cue; separate the two triggers |
| 3 | Confirmation Bias (selective evidence-seeking), Framing Bias (risk presentation), Groupthink (team consensus) | Framing and Confirmation (both involve information handling) | None | None | Groupthink (dissent-suppression cues may be subtle) | Groupthink | Provide explicit dissenting input that is overridden; separate framing from evidence-seeking |
| 4 | Hindsight Bias (outcome knowledge), Inattentional Blindness (missed cue), Overconfidence Bias (capability judgment), Status Quo Bias (maintaining anchorage) | Hindsight Bias and outcome bias (both involve outcome knowledge), Overconfidence and Status Quo (both involve confidence in current state) | Hindsight Bias | Hindsight Bias | Inattentional Blindness (missed cue must be clearly present but unattended) | Hindsight Bias, Inattentional Blindness | Separate outcome knowledge from in-the-moment reasoning; ensure missed cue was genuinely available |
| 5 | Sunk Cost Bias (repair investment), Automation Bias (monitoring system trust), Inattentional Blindness (secondary alarm), Hindsight Bias (past decision review) | Sunk Cost and Status Quo (not both present, but note for future overlap), Automation and Inattentional Blindness (both involve system/attention interaction) | None | Hindsight Bias | Inattentional Blindness (secondary alarm must be genuinely perceivable) | Inattentional Blindness | Ensure secondary alarm is clearly logged/available; separate repair-cost reasoning from monitoring trust |
| 6 | Status Quo Bias, Framing Bias, Groupthink, Overconfidence Bias, Anchoring Bias (five distinct; duplicate Overconfidence treated as one bias) | Status Quo and Anchoring (both involve resistance to change from a reference point), Overconfidence (duplicate entry — must not be double-counted as two separate biases) | None | None | Groupthink (dissent-suppression cues may be subtle) | Groupthink | Treat duplicate Overconfidence Bias as one bias with two possible manifestation points, not two mechanisms; flag to Prompt 2 annotators to avoid double-coding |
| 7 | Confirmation Bias, Automation Bias, Inattentional Blindness, Framing Bias (four cleanly distinguishable); Hindsight Bias, Sunk Cost Bias, Status Quo Bias (three requiring careful separation) | Sunk Cost and Status Quo (both involve resistance to changing course), Hindsight and outcome bias, Confirmation and Automation (both involve trust in system output) | Hindsight Bias | Hindsight Bias | Status Quo Bias (position-mode maintenance cue may overlap with Sunk Cost) | Hindsight Bias, Sunk Cost Bias, Status Quo Bias | Split the seven biases across at least three distinct sub-episodes (fault detection, continue/abort deliberation, post-incident review); explicitly separate cost-based reasoning (Sunk Cost) from default-inertia reasoning (Status Quo) |

**Overall safeguards:**
- **Prompt 1 (interview generation):** For Interviews 6 and 7, explicitly flag duplicate/overlapping bias labels so the generator does not attempt to manufacture two independent instances of the same mechanism (Interview 6's repeated Overconfidence Bias) or compress too many mechanisms into a single decision point (Interview 7's seven biases). Ensure hindsight-prone interviews (4, 5, 7) clearly separate the in-the-moment reasoning from the after-the-fact review framing.
- **Prompt 2 (annotation):** Require annotators to code Interview 6's duplicate Overconfidence Bias as a single bias instance unless two clearly separable manifestation points are present in the final transcript. Require explicit cue-tagging for Inattentional Blindness (must show the missed cue was genuinely available) and for Sunk Cost vs. Status Quo Bias in Interview 7 (must show cost-based justification vs. default-inertia justification separately).
