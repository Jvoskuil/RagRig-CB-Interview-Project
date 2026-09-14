You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, no problem. It's a good one to talk through.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, so we had a fixed obligation deadline. Miss it, and part of that funding is at risk.

Interviewer: What made this project different from others you'd run?

Participant: Live revenue service running through the work zone, so limited possession windows at night and weekends. A fixed-price design-build contract, which makes change orders painful. And that federal clock running the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We set a baseline schedule and budget up front. During early design we had a utility-survey question — the corridor's underground records were old — and we decided to commission an updated survey before locking the schedule. That survey came back mostly clean, but it flagged one segment where the position data had a stated tolerance, meaning the utility was there but not pinned down precisely. We handled that finding a certain way. Mid-construction, crews still hit a conduit conflict in that exact segment, and we had a shorter safety stand-down than you'd get from a totally unknown strike, but a stand-down all the same. Contractor followed with a risk report on the cost and schedule impact. Then near the end we had to decide how to run systems integration testing against the deadline. We got through commissioning, the system passed, and we hit the funding deadline, but it was tight.

Interviewer: Let's start with the baseline schedule. What information did you have?

Participant: The contractor's proposal assumed efficient crew productivity — their best-case numbers. We also had data from peer agencies that had done similar interlocking swaps, running 28 to 34 months typically. Leadership wanted visible progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh those two data points?

Participant: I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.

Interviewer: Once the survey added three weeks up front, how did that affect the schedule?

Participant: We didn't push the overall target out. We absorbed those three weeks by tightening later construction phases so the external date stayed at 24 months.

Interviewer: Let's go to the survey itself. What did the results tell you, and what did you do with them?

Participant: Utility maps had been over five years old, so we commissioned the updated survey — about $150,000 and three weeks. It came back solid overall, but one segment near the bore path came with a stated tolerance, something like two feet of uncertainty on exact position, because the underlying municipal records for that block were poor to begin with.

Interviewer: What were your options once you saw that tolerance note?

Participant: We could fund extra contingency time and budget specifically for that segment, or rely on our normal process — weekly risk reviews plus the field crew's verification work during excavation — to handle it as it came up.

Interviewer: Which way did you go, and why?

Participant: We didn't add contingency. Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice. I knew that verification would really only confirm the actual position once we were mobilized inside that possession window — so if something was off, we'd find out on the clock, not ahead of it — but that still felt like enough to keep the segment on plan. Two feet isn't a huge miss, and I didn't see it as something that needed separate budget.

Interviewer: What happened once construction reached that segment?

Participant: Crews still caught a conduit edge that was outside where the drawing showed it, inside that same flagged area. Shorter stand-down than a full unknown-utility strike would cause — a few days, not weeks — but it did stop work on that segment.

Interviewer: Looking back on that now, how foreseeable does it feel?

Participant: Honestly, the survey told us that segment was uncertain. So in hindsight, of course something was going to be slightly off there — it's almost obvious once you say it that way.

Interviewer: At the time, though, how was that segment actually rated?

Participant: Our risk register logged it as low residual risk once the survey came back. We treated the tolerance note as basically resolved by process, not as an open risk.

Interviewer: Let's move to the contractor's risk report. What did that process look like?

Participant: It came in projecting around a 6 percent cost overrun and about four weeks of schedule impact from the segment conflict. Those numbers weren't something I wanted to sit with heading into board season, honestly — reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature. I had five business days to sign off, and that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads without asking for a real readout on what it actually showed, and told the team to keep monitoring. I didn't escalate to the grant administrator during that window.

Interviewer: Did the picture change in the following weeks?

Participant: It crept up a bit before we brought it into focus and eventually asked the grant side for a smaller schedule accommodation than we would have needed with a full unmapped strike.

Interviewer: Now the testing decision near the end. What was the situation?

Participant: Six weeks left before the grant deadline. Standard systems integration testing runs eight weeks. Our engineering lead wanted the full eight, no shortcuts. Grants officer was clear that missing the milestone risked about $4 million of funding we already had secured.

Interviewer: What alternatives did you weigh?

Participant: Request a formal extension and keep the full eight weeks, or compress to five weeks, trimming some redundant verification cycles, to hit the date.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.

Interviewer: If that $4 million had instead been potential new funding you could gain by finishing on time, rather than money you already had, would the call have gone differently?

Participant: Probably, yeah. If it were more like a bonus on the table instead of something already secured, I think we hold the full eight weeks. Losing money we already had in hand felt different from missing out on the same amount.

Interviewer: How did testing play out?

Participant: Finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether the trimmed verification cycles matter down the line, I honestly don't know yet.

Interviewer: What additional information about that tolerance zone would have changed your decision not to add contingency?

Participant: If the survey firm had given us a tighter confidence range, or flagged that segment as a priority-verify area rather than routine, I think we'd have budgeted differently.

Interviewer: Looking back, was the conflict something the team could have anticipated?

Participant: The information was there. We just read the tolerance note as already handled rather than as a live risk.

Interviewer: What would you tell a peer facing a similar project?

Participant: Get your survey done early, but don't stop there — treat any flagged uncertainty as an open item with its own budget line, not something your normal process automatically covers. And build real slack against the funding clock before you're forced into testing-scope decisions at the end.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Counterfactual_5",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Project Manager / Capital Projects Manager (Rail Infrastructure)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Corridor Interlocking Replacement: Schedule, Survey Commissioned, and Grant-Deadline Pressure (Counterfactual)",
    "scenario_summary_internal": "Paired counterfactual to RT_Biased_5. The Capital Projects Manager oversees the same design-build interlocking replacement on the same commuter corridor, under the same federal grant obligation deadline. The single causal variable changed is that the PM commissions an updated utility/geotechnical survey before finalizing the baseline schedule (rather than skipping it). The survey reduces but does not eliminate downstream risk: it flags one segment with a stated position tolerance rather than a fully unknown conduit. The PM still absorbs the added survey time by compressing later phases, still treats the survey's residual tolerance caveat as adequately managed by field inspection process rather than contingency, still underreacts to the contractor's subsequent risk report, and still compresses systems-integration testing under the funding deadline. All other material facts, actors, and the four-decision-point structure are held constant relative to RT_Biased_5.",
    "occupational_realism": {
      "objective": "Deliver a signal/interlocking replacement on a commuter rail corridor on schedule and within the federal grant's obligation window, while maintaining safety-critical testing standards.",
      "setting": "Mid-size regional commuter rail agency; design-build capital project; corridor with active revenue service requiring possession/outage windows for construction.",
      "constraints": [
        "Fixed federal grant obligation deadline with risk of partial defunding on slippage",
        "Limited track possession/outage windows shared with revenue operations",
        "Fixed-price design-build contract with limited change-order flexibility",
        "Aging corridor with a legacy utility survey that carries a stated position tolerance in at least one segment",
        "PM's competing obligations to board reporting, grant compliance officer, and field operations"
      ],
      "stakeholders": [
        "Capital Projects Manager (interviewee)",
        "Design-build contractor project manager",
        "Agency chief engineer",
        "Signal/systems integration engineering lead",
        "Grants and compliance officer",
        "Rail operations/dispatch department",
        "Utility survey firm",
        "Federal grant administrator"
      ],
      "technical_terms_to_use": [
        "interlocking replacement",
        "signal cutover",
        "positive train control (PTC) interface",
        "utility/geotechnical survey",
        "position tolerance zone",
        "pothole/field verification",
        "fixed-price design-build contract",
        "systems integration testing",
        "possession window",
        "change order",
        "risk register",
        "grant obligation deadline",
        "commissioning protocol"
      ],
      "technical_terms_to_avoid": [
        "aviation-specific terminology",
        "maritime terminology",
        "unrelated software engineering jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Grant obligation deadline is 30 months from project initiation",
          "Comparable interlocking replacement projects at peer agencies took 28-34 months historically",
          "Contractor's proposal assumes best-case crew productivity rates",
          "Agency leadership wants visible grant utilization progress reported to the board"
        ],
        "new_information_after_decision": [
          "Actual crew productivity later trails the plan, consistent with the historical range the PM had access to at baseline",
          "The added survey time from phase 2 is absorbed by compressing later construction phases rather than extending the external target date"
        ],
        "alternatives": [
          "Adopt an aggressive 24-month baseline schedule to build political margin",
          "Adopt a 30-month baseline schedule anchored to historical analogous project durations"
        ],
        "intended_action": "PM selects the aggressive 24-month schedule, anchoring on the contractor's best-case estimate and discounting historical overrun patterns on comparable projects."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing utility maps for the corridor are over five years old",
          "Contractor flags several uncertain conduit locations near the planned bore path",
          "An updated survey would cost $150K and add three weeks to baseline",
          "PM has established a weekly risk-review and change-order tracking process"
        ],
        "new_information_after_decision": [
          "The commissioned survey identifies most conduit locations but reports a stated horizontal position tolerance of about two feet in one segment due to poor legacy municipal records",
          "PM's team treats the tolerance caveat as adequately covered by field verification during excavation rather than allocating contingency budget or schedule for that segment",
          "Mid-construction, crews still encounter a conduit conflict within the tolerance-flagged segment, triggering a shorter safety stand-down than an entirely unmapped strike would cause"
        ],
        "alternatives": [
          "Commission the updated survey and additionally fund contingency/extra field-verification time for any segment reported with position tolerance",
          "Commission the updated survey and rely on the existing weekly risk-review cadence and field crews to resolve any reported tolerance issues as they arise"
        ],
        "intended_action": "PM commissions the survey but, on seeing the tolerance caveat, elects not to add contingency budget or schedule for that segment, judging that inspection and field-verification practice already in place will resolve any residual placement uncertainty."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor delivers a risk/cost report following the tolerance-zone conflict, projecting roughly a 6 percent cost overrun and about four weeks of schedule impact",
          "Report requires PM sign-off within five business days",
          "PM's calendar is consumed by quarterly board preparation"
        ],
        "new_information_after_decision": [
          "The overrun risk compounds modestly over the following weeks before it is escalated",
          "The agency later requests a smaller schedule accommodation from the grant administrator than in the fully unmapped-strike scenario"
        ],
        "alternatives": [
          "Block dedicated time to fully review the report and convene a risk workshop with the engineering lead",
          "Skim the executive summary, delegate detailed review, and continue the existing reporting cadence without escalating"
        ],
        "intended_action": "PM defers detailed engagement with the report's underlying analysis because the figures are unwelcome heading into board season, delegates review without requesting a substantive readout, and does not escalate to leadership or the grant administrator during the sign-off window."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Six weeks remain before the grant obligation deadline",
          "Systems integration testing normally requires an eight-week protocol",
          "Signal engineering lead recommends the full eight-week test window",
          "Grants officer states a milestone slip risks roughly $4M in partial defunding"
        ],
        "new_information_after_decision": [
          "Testing completes within the compressed window and the system passes, but with fewer redundant verification cycles; funding is preserved but long-term reliability implications are not yet known at interview time"
        ],
        "alternatives": [
          "Request a formal deadline extension from the grant administrator while completing the full eight-week protocol",
          "Compress testing to five weeks, cutting some redundant verification cycles, to preserve the funding"
        ],
        "intended_action": "PM frames the decision around not losing the already-secured $4M and compresses the testing timeline, indicating the choice would likely have gone the other way if the same amount had been an unrealized upside rather than funding already in hand."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role on this project and what the corridor interlocking replacement was meant to achieve.",
        "What made this project nonroutine compared to prior capital projects you've managed?"
      ],
      "timeline_reconstruction": [
        "Walk me through the project chronologically from initiation to commissioning.",
        "What cues or signals prompted you to move from one phase to the next?",
        "At what point did you first sense the project might not go as planned?"
      ],
      "decision_point_probes": [
        "What information did you have available when you set the baseline schedule, and how did you weigh it?",
        "Once you had the survey results, what did you do with the tolerance-zone finding?",
        "When the contractor's risk report came in, what was your process for reviewing it and deciding next steps?",
        "How did you weigh the testing protocol recommendation against the grant deadline pressure?",
        "How much time pressure did you feel at each of these moments, and how did that affect your options?",
        "What was your level of uncertainty at each decision, and how did you handle it?",
        "Had you faced a similar situation before? How did that experience shape your choice this time?"
      ],
      "closing_hypotheticals": [
        "What additional information about the tolerance zone would have changed your decision not to add contingency?",
        "If the $4 million had been an upside you might gain rather than funding you already had, would the testing decision have changed?",
        "Looking back, was the tolerance-zone conflict something the team could have anticipated at the time?",
        "What would you tell a peer facing a similar fixed-price, fixed-deadline project?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "PM anchors the baseline schedule on the contractor's best-case productivity estimate while discounting the distribution of durations from comparable historical projects that were available at the time.",
        "affected_reasoning_operation": "Estimation/forecasting of project duration",
        "evidence_available_at_time": [
          "Contractor's optimistic productivity-based proposal",
          "Historical duration range (28-34 months) from peer agency projects"
        ],
        "required_textual_manifestation": "PM explains choosing the 24-month schedule primarily by citing the contractor's proposal and board pressure, while acknowledging but setting aside the historical range as not fully comparable, and later absorbs the survey's added three weeks by compressing later phases rather than revising the external target.",
        "plausible_nonbias_interpretation": "PM could argue the peer projects had different scope or team composition, making the shorter estimate a reasonable domain judgment rather than a forecasting error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "decision_point": 2,
        "mechanism": "Having commissioned the survey, PM substitutes confidence in field-verification/inspection practice for actually reducing the residual, explicitly stated position-tolerance uncertainty in one segment, treating routine process as equivalent to control over an acknowledged data limitation.",
        "affected_reasoning_operation": "Risk evaluation and resource allocation in response to a qualified (not absent) data source",
        "evidence_available_at_time": [
          "Survey report showing most conduits located but one segment with a stated ~2-foot position tolerance",
          "Existence of PM's weekly risk-review and field-inspection process",
          "Availability of an option to fund contingency/extra field verification for that segment"
        ],
        "required_textual_manifestation": "PM states that the tolerance caveat did not warrant added contingency because field crews would verify positions during excavation as a matter of course, framing standard inspection practice as sufficient to resolve a known, quantified uncertainty rather than as one imperfect mitigation among others.",
        "plausible_nonbias_interpretation": "PM could argue that a two-foot tolerance is a minor, routine finding not warranting special budget, making the choice an ordinary risk-tolerance judgment rather than an overestimate of control.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence in process"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "decision_point": 2,
        "mechanism": "In a retrospective probe about the tolerance-zone conflict, PM recalls the conflict as obviously predictable given that the survey itself flagged the tolerance, which is inconsistent with the team's contemporaneous risk register that had rated that segment as low residual risk once surveyed.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction of past uncertainty",
        "evidence_available_at_time": [
          "Contemporaneous risk-register entry rating the tolerance-flagged segment as low residual risk",
          "Post-hoc knowledge of the actual conduit conflict"
        ],
        "required_textual_manifestation": "When asked to reflect on the conflict, PM says something like the survey literally told them that segment was uncertain, so of course something turned up there, which contradicts the low-residual-risk rating the team itself assigned after receiving the survey.",
        "plausible_nonbias_interpretation": "PM could be expressing legitimate updated risk literacy about tolerance zones for future projects rather than misremembering the foreseeability of this specific outcome.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "decision_point": 3,
        "mechanism": "Facing an unfavorable, quantified risk/cost report, PM avoids engaging with its underlying data because the figures are unwelcome ahead of board season, skims the summary, delegates without requesting a substantive readout, and does not escalate within the required review window.",
        "affected_reasoning_operation": "Information-seeking and evidence engagement under threat of unfavorable news",
        "evidence_available_at_time": [
          "Contractor risk/cost report projecting a 6 percent overrun and roughly four-week delay",
          "Five-business-day sign-off window",
          "PM's own calendar constraints"
        ],
        "required_textual_manifestation": "PM states that the figures were unwelcome enough that reviewing and escalating them before the next monitoring update felt premature, describes reading only the executive summary, delegating without requesting a detailed readout, and not escalating during the window.",
        "plausible_nonbias_interpretation": "PM could argue that delegation and awaiting the next monitoring cycle reflected legitimate workload triage given competing board-reporting duties, not avoidance of bad news.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "avoidance of negative information"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "PM frames the testing-schedule decision around avoiding the loss of already-secured $4M in grant funding, and when probed with an equivalent-gain framing, indicates the decision would likely differ if the same amount were an unrealized upside rather than funding already in hand, revealing asymmetric weighting rather than a symmetric cost-benefit calculation.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and safety/reliability protocol completeness",
        "evidence_available_at_time": [
          "Grants officer's statement that a slip risks ~$4M defunding of already-committed money",
          "Signal engineering lead's recommendation for the full eight-week protocol",
          "Six weeks remaining before the deadline"
        ],
        "required_textual_manifestation": "PM explicitly states the decision was driven by not wanting to lose funding already secured, and in response to a probe about an equivalent potential gain, states the full protocol would probably have been kept in that scenario, showing the loss framing rather than the dollar amount alone drove the choice.",
        "plausible_nonbias_interpretation": "PM could argue the compressed protocol still met minimum safety-certification requirements, making this a defensible resource-constrained engineering tradeoff rather than a framing-driven distortion.",
        "strength": "moderate",
        "do_not_make_explicit": ["loss aversion", "loss framing", "prospect theory"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "RT_Biased_5",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the counterfactual condition, not a zero-bias control."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the Capital Projects Manager commissions an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "In the paired scenario (RT_Biased_5), the survey is not commissioned; the schedule is finalized using outdated (5+ year old) utility maps",
      "counterfactual_state": "The survey is commissioned; it identifies most utility locations but reports a stated position tolerance in one segment, which the PM treats as adequately managed by field-verification practice rather than by allocating contingency",
      "variables_to_hold_constant": [
        "Grant obligation deadline (30 months) and $4M defunding risk",
        "Contractor identity and fixed-price contract structure",
        "Agency staffing and PM's role/authority",
        "Corridor location and general utility-age profile",
        "Occurrence of a utility-related disruption at decision point 2, though at reduced magnitude",
        "Presence of the contractor risk report at decision point 3 and the testing-compression decision at decision point 4"
      ],
      "expected_causal_difference": "Commissioning the survey reduces the severity of the mid-construction disruption (a shorter stand-down tied to a flagged tolerance zone rather than a fully unmapped strike) and correspondingly scales down the contractor's subsequent risk/cost report, but it does not eliminate the underlying risk-management gap, the report-handling avoidance, or the funding-driven testing compression, because those depend on separate decisions rather than on survey commissioning alone.",
      "causal_test_question": "Does commissioning the utility survey primarily change the magnitude and character of the downstream disruption, while leaving the risk-report handling and testing-compression decisions structurally similar to the paired scenario?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and each has at least two plausible alternatives.",
      "Confirm each of the 5 planned instances is tied to a single, identifiable decision/inference/probe response with distinguishable evidence.",
      "Confirm no bias term, definition, or explicit psychological label appears in the drafted interview text.",
      "Confirm cb_02 and cb_03 at decision point 2 use different reasoning operations (in-the-moment resource-allocation judgment vs. retrospective causal attribution) and different evidence traces.",
      "Confirm the survey is explicitly commissioned in this scenario and that this is the only material fact changed relative to RT_Biased_5's survey decision.",
      "Confirm the interview does not imply the survey deterministically prevented all disruption; only that it changed the disruption's severity and character.",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, probe plan, and 5 embedded instances without repetitive exposition.",
      "Confirm consequences at each decision point are consistent with either a biased or a reasonable-judgment account (non-mechanical proof of bias).",
      "Confirm cb_04 and cb_05 include enough explicit contrast (threat-motivated deferral language; equivalent-gain probe and response) to be independently identifiable without naming the bias."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Illusion of Control", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Aversion or Loss Framing effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Ostrich Effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Planning Fallacy", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Hindsight Bias",
      "Illusion of Control",
      "Loss Aversion or Loss Framing effect",
      "Ostrich Effect",
      "Planning Fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of Control", "requested_occurrences": 1 },
      { "bias": "Loss Aversion or Loss Framing effect", "requested_occurrences": 1 },
      { "bias": "Ostrich Effect", "requested_occurrences": 1 },
      { "bias": "Planning Fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy" },
      { "instance_id": "cb_02", "bias": "Illusion of Control" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring baseline schedule on contractor's best-case estimate while discounting available historical duration data, and later absorbing added survey time via phase compression rather than revising the external target.",
        "affected_reasoning_operation": "Duration estimation/forecasting",
        "evidence_source": "Contractor proposal vs. historical peer-agency project durations",
        "distinctiveness_requirement": "Occurs at initiation/baseline-setting; involves forward-looking forecasting, not the in-the-moment resource-allocation judgment at decision point 2 or the retrospective judgment tied to it."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "mechanism": "Treating routine field-inspection/verification practice as sufficient to resolve an explicitly quantified residual position-tolerance uncertainty in the survey, rather than allocating contingency for it.",
        "affected_reasoning_operation": "Risk evaluation and resource allocation in response to a qualified (not absent) data source at the moment of the survey decision",
        "evidence_source": "Survey report's stated tolerance finding vs. PM's description of relying on field-verification process",
        "distinctiveness_requirement": "Occurs in-the-moment at the post-survey resource-allocation decision, distinct from the later retrospective recall at the same decision point (cb_03)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively characterizing the tolerance-zone conflict as obviously foreseeable because the survey flagged it, inconsistent with the team's contemporaneous low-residual-risk rating for that segment.",
        "affected_reasoning_operation": "Post-hoc causal attribution / memory reconstruction in response to a reflection probe",
        "evidence_source": "Contemporaneous risk-register rating vs. post-outcome recollection",
        "distinctiveness_requirement": "Occurs only in a later reflective probe response about decision point 2's outcome, not in the original in-the-moment decision (cb_02)."
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "mechanism": "Avoiding direct engagement with an unfavorable, quantified risk/cost report because the figures are unwelcome, by skimming the summary, delegating without requesting a substantive readout, and not escalating within the required review window.",
        "affected_reasoning_operation": "Information engagement/evidence-seeking under threat of unfavorable news",
        "evidence_source": "Contractor's risk/cost report and PM's described review behavior, including an explicit statement that the figures were unwelcome ahead of board season",
        "distinctiveness_requirement": "Confined to decision point 3's report-handling behavior; not a repetition of cb_02's resource-allocation judgment or cb_01's forecasting."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Framing the testing-schedule tradeoff around avoiding loss of already-secured funding, with an explicit equivalent-gain probe response showing the decision would likely differ if the same amount were an unrealized upside.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and protocol completeness",
        "evidence_source": "Grants officer's loss framing, engineering lead's full-protocol recommendation, and PM's response to the equivalent-gain probe",
        "distinctiveness_requirement": "Occurs at the final decision point only, tied to explicit loss-framed language and the gain-framing contrast, distinct from all prior instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "strength": "moderate" }
    ],
    "paired_scenario_id": "RT_Biased_5",
    "counterfactual_variable": {
      "name": "Commissioning of an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Not commissioned in the paired scenario (RT_Biased_5); baseline finalized using outdated utility maps",
      "changed_state": "Commissioned in this scenario; survey identifies most utility locations but reports a stated position tolerance in one segment, which the PM manages via field-verification process rather than added contingency",
      "variables_to_hold_constant": [
        "30-month grant obligation deadline and ~$4M defunding risk",
        "Contractor identity and fixed-price contract terms",
        "PM's role, authority, and team composition",
        "Corridor location and utility-age profile",
        "Occurrence of a utility-related disruption at decision point 2, at reduced magnitude",
        "Presence of the contractor risk report and testing-compression decision at decision points 3 and 4"
      ]
    },
    "scenario_id": "RT_Counterfactual_5",
    "domain_id": "RT",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with mechanism-fit prioritization; decision point 2 hosts two distinct biases (Illusion of Control at the moment of the post-survey resource-allocation decision, Hindsight Bias in a later reflective probe about that decision's outcome), using different reasoning operations and evidence sources, mirroring the paired scenario's allocation while adapting the evidence content to the changed causal variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "30-month grant obligation deadline and ~$4M defunding risk",
      "Contractor identity and fixed-price contract terms",
      "PM's role, authority, and team composition",
      "Corridor location and utility-age profile",
      "Occurrence of a utility-related disruption at decision point 2, at reduced magnitude",
      "Presence of the contractor risk report and testing-compression decision at decision points 3 and 4"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first evaluation of the interview transcript for affirmatively evidenced cognitive biases. Retrieved corpus passages were used for theoretical grounding where available; other classifications rely on established cognitive-science knowledge and are noted accordingly."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "information avoidance",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring-and-adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or estimate and to make insufficient adjustments from that anchor when forming a judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Baseline schedule commitment",
      "decision_point_description": "Choosing the project baseline schedule using contractor proposal estimates versus peer agency historical durations.",
      "affected_reasoning_operation": "Schedule estimation under uncertainty",
      "bias_specific_mechanism": "The contractor's best-case proposal served as a salient initial anchor; the participant discounted peer historical durations as soft and adjusted insufficiently toward the 28-34 month base-rate, selecting a 24-month schedule below the peer benchmark.",
      "manifestation_in_interview": "The participant reported leaning harder on contractor numbers and treating non-identical peer projects as less informative, then committing to 24 months.",
      "effect_on_reasoning_or_decision": "Produced an aggressive baseline schedule below comparable historical durations, later requiring absorption of added survey time by tightening construction phases rather than extending the completion date.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The contractor's proposal assumed efficient crew productivity — their best-case numbers. We also had data from peer agencies that had done similar interlocking swaps, running 28 to 34 months typically.",
          "evidence_explanation": "This quote establishes that both a specific contractor anchor and a relevant historical base-rate were available at the time of schedule setting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.",
          "evidence_explanation": "The participant explicitly reports overweighting the contractor estimate and discounting peer base-rate data, resulting in a schedule below the lower peer benchmark."
        }
      ],
      "correction_or_counterevidence": "Peer projects were not identical, so some discounting of the base rate could be a legitimate domain judgment; however, choosing below the lower peer bound while relying on best-case contractor assumptions indicates a distinct under-adjustment consistent with anchoring.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) passage directly discusses anchoring-and-adjustment in decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source validates the anchoring-and-adjustment heuristic as a cognitive mechanism in which adjustment away from an initial estimate can be insufficient.",
          "relevance_to_this_occurrence": "Supports classifying the schedule choice as an anchoring-and-adjustment process, although the interview setting is project management rather than AI-assisted decision-making."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmation bias in evidence interpretation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, or recall information in ways that confirm or support one's existing beliefs, hypotheses, or plans.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-survey risk handling for flagged utility tolerance",
      "decision_point_description": "Deciding whether to add contingency budget or schedule time after the survey flagged tolerance uncertainty near the bore path.",
      "affected_reasoning_operation": "Risk assessment and interpretation of uncertainty evidence",
      "bias_specific_mechanism": "The participant interpreted the flagged tolerance uncertainty as already handled by routine field-verification practice, preserving the existing plan and a low risk-register rating rather than treating the new information as an open, specific risk.",
      "manifestation_in_interview": "The participant did not add contingency and logged the segment as low residual risk because field crews verify positions as a matter of course. The participant knew verification would occur only inside the possession window but still judged that sufficient.",
      "effect_on_reasoning_or_decision": "The uncertain segment remained without targeted contingency, and construction later hit a conduit conflict in that exact segment, causing a short stand-down and schedule/cost impact.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice.",
          "evidence_explanation": "This shows the interpretative move in which new risk information was assimilated into the existing plan rather than treated as contradictory evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew that verification would really only confirm the actual position once we were mobilized inside that possession window — so if something was off, we'd find out on the clock, not ahead of it — but that still felt like enough to keep the segment on plan. Two feet isn't a huge miss, and I didn't see it as something that needed separate budget.",
          "evidence_explanation": "The participant explicitly recognized that the risk would only be resolved later, yet rationalized maintaining the existing plan and no contingency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We treated the tolerance note as basically resolved by process, not as an open risk.",
          "evidence_explanation": "This is an explicit admission that the uncertain information was interpreted as already handled, consistent with confirmation bias in risk interpretation."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the survey had given a warning. Routine verification is a real safety practice, but rating the segment as low residual risk despite known two-foot uncertainty indicates that the existing plan was favored over contradictory risk evidence.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Cook & Smallman (2008) source provides empirical evidence for confirmation bias in evidence selection and interpretation during analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents a strong confirmation bias in evidence selection and prioritization during analytical judgment.",
          "relevance_to_this_occurrence": "Validates confirmation bias as a plausible mechanism in interpreting flagged uncertainty as consistent with the existing plan rather than as contradictory evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "information avoidance",
      "alternative_labels": ["ostrich effect", "motivated inattention"],
      "taxonomy_status": "established_label",
      "bias_definition": "The motivated avoidance of potentially threatening or unpleasant information that could require unwanted action or emotional discomfort.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Review and sign-off of contractor risk report after conduit conflict",
      "decision_point_description": "Deciding how to review and escalate the contractor's cost and schedule impact report within the sign-off window.",
      "affected_reasoning_operation": "Information search, review, and escalation",
      "bias_specific_mechanism": "Aversive cost and schedule impact numbers triggered avoidance: the participant read only the executive summary, delegated detailed analysis without obtaining a substantive readout, and did not escalate during the sign-off window despite having five business days to act.",
      "manifestation_in_interview": "The participant said the numbers were not something he wanted to sit with before board season, then limited review and did not seek detailed analysis. The risk report was held and monitored rather than escalated before the next cycle.",
      "effect_on_reasoning_or_decision": "Reduced substantive review and delayed escalation; the project did not ask the grant administrator for a schedule accommodation until after the reported impact had increased.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Those numbers weren't something I wanted to sit with heading into board season, honestly — reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature.",
          "evidence_explanation": "This statement reveals motivational avoidance of unpleasant financial and schedule information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I read the executive summary, delegated the detailed analysis to one of my leads without asking for a real readout on what it actually showed, and told the team to keep monitoring. I didn't escalate to the grant administrator during that window.",
          "evidence_explanation": "This demonstrates reduced information processing and delayed escalation resulting from avoidance rather than substantive review."
        }
      ],
      "correction_or_counterevidence": "Time pressure and board preparation were real constraints; however, the participant had five business days and explicitly framed the avoidance as not wanting to sit with the numbers, indicating a motivational information-avoidance mechanism rather than only resource limitation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus did not include a source on information avoidance; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "loss aversion",
      "alternative_labels": ["loss aversion bias", "tendency to prefer avoiding losses over acquiring equivalent gains"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for losses to have a greater psychological impact than equivalent gains, leading decision-makers to avoid losses even at the expense of higher expected value or risk.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Systems integration testing window versus grant deadline",
      "decision_point_description": "Choosing between a formal extension with full eight-week testing and compressed five-week testing to protect already-secured grant funding.",
      "affected_reasoning_operation": "Decision under risk and schedule-scope tradeoff",
      "bias_specific_mechanism": "The framing of the $4 million as a sure loss from missing the milestone, rather than as a foregone gain, made avoiding that loss the dominant factor. The participant confirmed that the identical amount framed as new potential funding would not have driven the same decision.",
      "manifestation_in_interview": "The participant chose compressed testing because the funding was already secured, and said the engineering case for full testing was solid. In the hypothetical gain-framed alternative, the participant would have held the full eight weeks.",
      "effect_on_reasoning_or_decision": "The project accepted a shortened systems integration testing window, trimming redundant verification cycles, to avoid losing secured $4 million despite a strong engineering argument for full testing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.",
          "evidence_explanation": "This shows loss framing dominating the decision over the engineering risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. If it were more like a bonus on the table instead of something already secured, I think we hold the full eight weeks. Losing money we already had in hand felt different from missing out on the same amount.",
          "evidence_explanation": "This explicit gain-loss comparison demonstrates the asymmetric weighting of losses and gains that defines loss aversion."
        }
      ],
      "correction_or_counterevidence": "The compressed testing window succeeded and the system passed; however, the decision was influenced by loss framing independent of engineering risk, and the participant acknowledges uncertainty about whether trimmed verification cycles matter later.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus did not include a source on loss aversion; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "planning fallacy",
      "alternative_labels": ["optimism bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Baseline schedule commitment",
      "supporting_interview_quote": "I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.",
      "plausible_mechanism": "Possible underestimation of project duration despite historical base-rate data, consistent with planning fallacy or optimistic forecasting.",
      "why_not_identified": "The transcript more directly evidences anchoring on the contractor's proposal and adjustment away from peer data. Planning fallacy is plausible but cannot be reliably separated from legitimate case-specific judgment, so it remains a candidate."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieval context includes only a small subset of bias-related sources; classifications for information avoidance and loss aversion rely on established general cognitive-science knowledge rather than retrieved corpus support.",
    "The analysis is based on a single interview transcript and self-report, so causal inference about internal mechanisms is limited.",
    "The first occurrence is rated low confidence because peer projects were not identical, which introduces a credible non-bias explanation for discounting the historical base rate."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Counterfactual_5_Gemini_on",
  "interview_id": "RT_Counterfactual_5",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
