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
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "\"I leaned harder on the contractor's numbers. The peer projects weren't identical \u2014 different vendors, different corridor layouts \u2014 so the comparison felt soft. We went with 24 months.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "Baseline schedule selection contains the hidden planning-forecasting instance: the PM favors best-case contractor productivity and discounts the available peer duration range."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "\"Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02",
            "cb_03"
          ],
          "ground_truth_rationale": "The post-survey resource-allocation reasoning contains Illusion of Control, while the later reflection that the conflict was obvious contains Hindsight Bias."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "\"Those numbers weren't something I wanted to sit with heading into board season, honestly \u2014 reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "Handling of the quantified contractor risk report contains the hidden information-avoidance/Ostrich Effect instance."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "\"We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "The final testing choice contains the explicit loss-versus-equivalent-gain framing that defines the hidden Loss Aversion/Loss Framing instance."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
