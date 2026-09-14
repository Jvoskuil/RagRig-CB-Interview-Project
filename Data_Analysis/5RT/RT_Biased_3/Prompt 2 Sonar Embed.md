You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm, this conversation is being used to understand how decisions get made during unusual shifts — not to evaluate your performance. Is that okay with you?

Participant: Yeah, that's fine. I've done these debriefs before after incidents, so no problem.

Interviewer: Great. Can you start by telling me your role and what made this particular night shift nonroutine?

Participant: Sure. I'm the yardmaster on the night shift at the hump yard. That night was messy from the start — one of our two hump leads was down for signal maintenance, so we were running everything through a single lead. On top of that, we were short two carmen because of storm callouts, and it was raining hard enough that the retarders weren't behaving predictably on wet rail. We also had an SLA connection window we needed to hit for an outbound customer train, so there was real pressure to keep things moving.

Interviewer: Walk me through how the shift actually unfolded.

Participant: When I came on, the relief briefing was rushed — the prior yardmaster was trying to get out before the worst of the storm hit, so he gave me the switch list verbally: 38 cars, expected to have the cut classified by 2200. That was my starting point for the night. Then the inbound train came in about 40 minutes late, and when we actually counted, it was 41 cars, not 38. The retarders were also cycling slower than normal because of the wet rail. So already things were behind where the paperwork said they'd be.

A while into classification, the hot-box detector flagged one car, GATX 88213, with a temperature reading that was elevated but still within tolerance — borderline, not a clear alarm. That detector's given us false positives before in wet weather. But we'd had a derailment at this yard about three weeks earlier from an overheated bearing on a similar car, and that was fresh in my mind. I made the call to pull the whole eleven-car cut it was sitting in for inspection, not just that one car.

Two carmen inspected it. One found a hairline mark near the knuckle, unrelated to the bearing issue. The other inspected independently and cleared it, no defect found. There was also an old repair entry on that car from two inspection cycles back, already closed out. I ended up treating it as still suspect and asked for a third pass. That ate more time. By the end, we were running about 55 minutes behind, with the SLA window closing in 40. I set that car out and dispatched the rest of the train.

Interviewer: Let's slow down and go through each of those moments. Starting with the ready-time estimate — you had 38 cars and a 2200 target from the handoff, then learned it was 41 cars with slower cycling. What went through your mind?

Participant: Honestly, I kept 2200 as my working target. I nudged it a little in my head, but I didn't sit down and recalculate from the new numbers. Part of it was trust — the relief yardmaster's been doing this longer than me, and his estimates are usually solid. Part of it was just not wanting to move the target this early and cause confusion down the line for the dispatcher.

Interviewer: What alternatives did you consider at that point?

Participant: I could've recalculated from scratch with the actual count and the cycle speed we were seeing. Or radioed the hump conductor for his read on pace before locking anything in. I didn't do either right away — I just carried the number forward.

Interviewer: What would have made you recalculate immediately instead of adjusting slightly?

Participant: Probably if the discrepancy had been bigger — if it'd been 50 cars instead of 41, I think I'd have thrown the original number out completely. Three extra cars didn't feel like enough to abandon the plan.

Interviewer: Now the hot-box alert. The reading was borderline, and you know that detector throws false positives in wet weather. What drove the decision to pull the full eleven-car cut instead of just the flagged car?

Participant: The derailment three weeks back was still sitting with me. That one started exactly this way — a reading that didn't look dramatic at first. I didn't want a repeat, so I went bigger than the book probably called for. Standard procedure would've been to isolate just GATX 88213 for a manual check. I pulled the whole cut.

Interviewer: Did you weigh the detector's false-positive history in that moment?

Participant: I knew about it, yeah. But it didn't carry the same weight as the derailment did. That one's the thing that comes to mind first when a hot-box alert comes in here, even though logically the wet-weather false positives happen a lot more often.

Interviewer: Then you had two conflicting carman reports — one found a hairline mark, the other cleared the car. How did you resolve that?

Participant: I leaned toward Carman A's finding. There was also that old repair entry on the car, even though it was closed out and unrelated to the bearing concern. Between the mark and that history, it felt like enough to keep the car flagged. I asked for a third inspection rather than accepting Carman B's clearance.

Interviewer: What made Carman A's report and the old repair note feel more convincing than Carman B's clearance?

Participant: Looking back, I'm not entirely sure I can justify that cleanly. Carman B followed the same protocol, same timeframe. I think once I already suspected the car, the mark and the repair history just fit what I expected to find. Carman B's "all clear" almost read to me like it needed double-checking, when really it should've carried equal weight.

Interviewer: What would have changed that call — if anything?

Participant: If Carman B's report had come in first, before Carman A's, I might have closed it out right there. Order mattered more than it should have, probably.

Interviewer: Last decision — the SLA deadline was closing in, and the car was still unresolved. What did you decide?

Participant: I set the car out and dispatched the rest of the train. Holding the whole consist for one car wasn't going to help anyone, and the dispatcher confirmed we'd only eat a partial penalty instead of a full one if we released the rest on time. That one felt like a straightforward trade-off, not a hard call.

Interviewer: How did things turn out?

Participant: The third inspection came back clean — no defect on GATX 88213. The train made it out with a partial penalty instead of the full one.

Interviewer: If the derailment three weeks earlier had never happened, do you think the hot-box call goes differently?

Participant: Probably, yeah. I think I isolate just the one car and keep moving.

Interviewer: And if you ran this same shift again tomorrow, what would you do differently?

Participant: I'd probably push back harder on the initial time estimate instead of just carrying it forward, and I'd try to look at both carmen's reports side by side instead of one at a time. Other than that, given what I knew in the moment, I'd probably land in a similar place.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_3",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Yardmaster / Rail Yard Supervisor",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Night Shift Hump Yard Congestion and Suspected Hot Bearing",
    "scenario_summary_internal": "During a night shift with only one working hump lead (the other closed for signal maintenance) and a carman shortage aggravated by a storm, the yardmaster must classify and release a mixed freight train to meet a customer SLA connection window. A prior-shift switch list gives an initial car-count and ready-time estimate. A wheel-bearing hot-box detector flags a car in the cut at a borderline reading, evoking memory of a derailment three weeks earlier at the same yard caused by an overheated bearing. The yardmaster forms a working hypothesis that a specific car has a coupler/mechanical defect and selectively weighs subsequent carman reports before making a final dispatch call under time pressure.",
    "occupational_realism": {
      "objective": "Classify and safely dispatch an inbound mixed freight cut through the hump yard in time to meet an outbound connection with a contractual SLA penalty, without compromising mechanical safety.",
      "setting": "Class I railroad classification (hump) yard control tower, night shift, moderate rain reducing visibility, one of two hump leads closed for signal maintenance.",
      "constraints": [
        "Only one working hump lead available",
        "Carman crew reduced by two due to storm callouts",
        "Outbound connection deadline with customer SLA penalty",
        "Wet rail reducing retarder braking predictability",
        "Prior-shift paperwork handed off verbally during a rushed relief briefing"
      ],
      "stakeholders": [
        "Yardmaster (interviewee)",
        "Relief yardmaster (prior shift)",
        "Two carmen (car inspectors)",
        "Hump conductor / switchman crew",
        "Train dispatcher (network control)",
        "Customer service desk (SLA owner)"
      ],
      "technical_terms_to_use": [
        "hump lead",
        "bad order",
        "switch list",
        "hot-box detector",
        "knuckle",
        "retarder",
        "cut of cars",
        "bowl track",
        "consist",
        "SLA connection window"
      ],
      "technical_terms_to_avoid": [
        "anchoring effect",
        "availability heuristic",
        "confirmation bias",
        "cognitive bias",
        "heuristic",
        "base rate"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Prior shift's switch list states 38 cars, estimated classification-complete by 2200",
          "Relief briefing was rushed due to shift-change storm delays",
          "Inbound train reported running 40 minutes late by the road crew"
        ],
        "new_information_after_decision": [
          "Actual car count on arrival is 41, three more than the switch list indicated",
          "Storm has slowed retarder cycle times, extending classification beyond normal pace"
        ],
        "alternatives": [
          "Recalculate the ready-time estimate from scratch using current car count and observed retarder cycle speed",
          "Keep the 2200 target from the switch list and only make minor mental adjustments",
          "Request an updated estimate directly from the hump conductor before committing to a target"
        ],
        "intended_action": "Yardmaster keeps the 2200 figure as the working target, adjusting only slightly despite the higher car count and slower cycle time."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Hot-box detector flags car GATX 88213 at a borderline temperature reading, within tolerance but elevated",
          "Detector history at this location has produced false positives in wet weather",
          "Three weeks earlier, an overheated bearing on a similar car caused a derailment at this yard"
        ],
        "new_information_after_decision": [
          "A full cut-pull inspection of eleven cars is ordered, consuming crew time already short due to storm callouts",
          "The carman assigned reports the reading is consistent with normal wet-rail sensor variance"
        ],
        "alternatives": [
          "Flag only the single indicated car for a standard visual and manual temperature check per procedure",
          "Pull the entire eleven-car cut for inspection out of caution",
          "Continue classification and reassess the detector reading at the next scheduled pass"
        ],
        "intended_action": "Yardmaster orders the full cut pulled for inspection, citing the earlier derailment, well beyond what the borderline reading and detector history would typically warrant."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Carman A reports a hairline mark near the coupler knuckle on GATX 88213, unrelated to the bearing alarm",
          "Carman B, inspecting the same car independently, reports no defect found and clears the car",
          "A paperwork discrepancy shows GATX 88213 was flagged for a minor repair two inspection cycles ago, now closed"
        ],
        "new_information_after_decision": [
          "Yardmaster logs the car as suspect and requests a third inspection pass, delaying the cut further",
          "Carman B's clearance is not recorded in the shift log as a factor in the decision"
        ],
        "alternatives": [
          "Weigh both carmen's reports equally and default to the standard resolution procedure for conflicting inspections",
          "Accept Carman B's clearance since it followed the same protocol and timeframe as Carman A's mark",
          "Escalate the conflicting reports to the car foreman for an independent tie-breaking inspection"
        ],
        "intended_action": "Yardmaster treats Carman A's hairline-mark report and the old repair-history entry as confirming a defect, while discounting Carman B's clearance as insufficiently thorough."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Classification is now running roughly 55 minutes behind the original target",
          "The SLA connection window closes in 40 minutes",
          "GATX 88213 has been set aside pending the third inspection pass; the rest of the cut is ready"
        ],
        "new_information_after_decision": [
          "Dispatcher confirms the outbound train can depart without GATX 88213, incurring a partial rather than full SLA penalty",
          "The third inspection later clears GATX 88213 with no defect found"
        ],
        "alternatives": [
          "Hold the entire train until GATX 88213's status is resolved",
          "Set out GATX 88213 and dispatch the remainder of the cut to partially meet the SLA window",
          "Request a short extension from the dispatcher to complete the third inspection before departure"
        ],
        "intended_action": "Yardmaster sets out GATX 88213 and dispatches the rest of the train, a judgment call balanced against genuine competing constraints rather than a biased inference."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this shift's objective was and what made it nonroutine?",
        "What information did you have at the very start of the shift, and where did it come from?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events in the order they happened.",
        "At each stage, what changed compared to what you expected going in?"
      ],
      "decision_point_probes": [
        "What options did you consider at that moment, and why did you choose the one you did?",
        "What specific piece of information most influenced that call?",
        "Did anything from earlier in the shift, or from past experience, shape how you read this situation?",
        "How did you weigh the different reports or data points you received?",
        "Looking back, was there information you didn't use as much as you could have?"
      ],
      "closing_hypotheticals": [
        "If the hot-box detector had never triggered, how do you think the shift would have gone?",
        "If Carman B's clearance had come in before Carman A's report, would that have changed your decision?",
        "How much did the earlier derailment weigh on you during this shift, if at all?",
        "If you had to make the same set of decisions again tomorrow, what would you do differently, if anything?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "decision_point": 1,
        "mechanism": "Initial numeric/time estimate from the prior shift's switch list (2200 ready-time, 38 cars) is insufficiently adjusted despite new, materially different information (41 cars, slower retarder cycling in the rain).",
        "affected_reasoning_operation": "Estimation and revision of a target completion time under new evidence",
        "evidence_available_at_time": [
          "Switch list stating 38 cars / 2200 target",
          "Actual arrival count of 41 cars",
          "Observed slower retarder cycle time due to wet rail"
        ],
        "required_textual_manifestation": "Yardmaster explicitly references sticking with the 2200 figure or making only a small mental tweak to it, rather than recalculating from the new car count and cycle speed.",
        "plausible_nonbias_interpretation": "Could be read as reasonable trust in a handoff estimate from an experienced relief yardmaster under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "anchoring",
          "initial estimate bias",
          "insufficient adjustment"
        ]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "The vivid, emotionally salient memory of a recent derailment caused by an overheated bearing disproportionately drives the probability/severity assessment of a borderline, statistically unremarkable hot-box reading, overriding the known false-positive rate of the detector in wet conditions.",
        "affected_reasoning_operation": "Risk assessment and response-scaling to a sensor alert",
        "evidence_available_at_time": [
          "Borderline hot-box detector reading",
          "Known history of false positives at this detector location in wet weather",
          "Recent memory of a derailment three weeks earlier involving a similar defect"
        ],
        "required_textual_manifestation": "Yardmaster's stated rationale for pulling the full eleven-car cut explicitly invokes the recent derailment memory as the driving reason, disproportionate to the borderline/ordinary nature of the reading.",
        "plausible_nonbias_interpretation": "Could be read as appropriately cautious safety margin-setting by an experienced supervisor.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "availability bias",
          "recency of memory",
          "salience"
        ]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "After forming a working hypothesis that the car is defective, the yardmaster selectively weights Carman A's ambiguous mark and an unrelated closed repair-history entry as corroborating evidence, while discounting Carman B's independent clearance that followed the same protocol.",
        "affected_reasoning_operation": "Evaluation and integration of conflicting evidence sources against a pre-existing hypothesis",
        "evidence_available_at_time": [
          "Carman A's report of a hairline mark near the knuckle",
          "Carman B's independent clearance finding no defect",
          "A closed, unrelated repair-history entry for the same car"
        ],
        "required_textual_manifestation": "Yardmaster explains treating Carman A's report and the old repair note as confirming the suspicion while characterizing Carman B's clearance as less credible or incomplete, without a stated procedural justification for the asymmetry.",
        "plausible_nonbias_interpretation": "Could be read as a defensible safety-first tie-breaking judgment favoring the more cautious of two conflicting reports.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "confirmation bias",
          "selective weighting",
          "discounting disconfirming evidence"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased', not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two alternatives.",
      "Exactly 3 intended bias instances planned (an_01, av_01, cb_01), matching the manifest total of 3.",
      "Each bias instance occupies its own decision point (1, 2, 3 respectively); decision point 4 is deliberately bias-free to serve as a genuine multi-constraint trade-off.",
      "No bias labels or psychological terminology appear in technical_terms_to_use, probe_plan, or timeline entries.",
      "Each instance has a plausible non-bias interpretation to avoid mechanically proving bias from outcome alone.",
      "Target word count (1,215-1,485 words) is achievable given 4 decision points with moderate probe depth and no repetitive exposition.",
      "Consequences (SLA penalty avoided partially, GATX 88213 later cleared) do not conclusively prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Anchoring Effect",
        "occurrences": 1,
        "mechanism_constraint": "Insufficient adjustment from a handed-off numeric/time estimate despite materially different new information."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Overweighting a vivid recent memory of an incident over calibrated base-rate/detector-history information."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Selective weighting of evidence corroborating a pre-existing hypothesis while discounting disconfirming evidence of comparable procedural credibility."
      }
    ],
    "target_bias_names": [
      "Anchoring Effect",
      "Availability Bias",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Anchoring Effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Availability Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Confirmation Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "decision_point": 1
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "mechanism": "Insufficient adjustment away from the prior shift's 2200/38-car estimate despite new information (41 cars, slower cycle time).",
        "affected_reasoning_operation": "Time-target estimation and revision",
        "evidence_source": "Prior-shift switch list vs. current arrival count and observed cycle speed",
        "distinctiveness_requirement": "Must be the only instance where a numeric/time target from a handoff document is under-adjusted; not to be repeated at any other decision point."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recent derailment memory disproportionately inflates the perceived risk of a borderline, statistically ordinary detector reading, overriding known false-positive base rate.",
        "affected_reasoning_operation": "Risk/severity assessment of a sensor alert",
        "evidence_source": "Hot-box detector reading and detector false-positive history vs. recalled derailment incident",
        "distinctiveness_requirement": "Must be the sole instance tied to recalled-incident-driven risk inflation; must not reappear as justification in decision points 3 or 4."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective acceptance of evidence (Carman A's mark, old repair note) that supports an existing defect hypothesis, paired with discounting of procedurally equivalent disconfirming evidence (Carman B's clearance).",
        "affected_reasoning_operation": "Integration and weighting of conflicting inspection evidence",
        "evidence_source": "Carman A report and repair-history entry vs. Carman B's independent clearance",
        "distinctiveness_requirement": "Must be the only instance involving asymmetric weighting of two competing carman reports; not to be conflated with the availability-driven risk framing at decision point 2."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "strength": "subtle"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_3",
    "domain_id": "RT",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per bias assigned to its own distinct decision point (1, 2, 3) based on mechanism fit: anchoring to the initial numeric estimate revision, availability to the sensor-risk assessment invoking a recalled incident, confirmation to the conflicting-evidence integration step. Decision point 4 deliberately left bias-free to preserve a genuine, non-mechanical trade-off and satisfy the exactly-4-decision-point requirement without introducing unrequested instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
        "segment_type": "estimate_revision_rationale",
        "raw_interview_anchor": "I kept 2200 as my working target. I nudged it a little in my head, but I didn't sit down and recalculate from the new numbers.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "an_01"
        ],
        "ground_truth_rationale": "The participant retained the handed-off 2200 target and made only a small adjustment despite learning the actual count and cycle conditions had changed. This is the primary manifestation of the single planned anchoring instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "alternative_action_and_estimate_choice",
        "raw_interview_anchor": "I could've recalculated from scratch ... Or radioed the hump conductor ... I didn't do either right away — I just carried the number forward.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "an_01"
        ],
        "ground_truth_rationale": "This is a separate articulation of the same estimate-revision decision: the participant identifies recalculation and consultation as alternatives but carries the initial target forward. It is not an additional planned occurrence."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "estimate_revision_threshold",
        "raw_interview_anchor": "Probably if the discrepancy had been bigger ... if it'd been 50 cars ... Three extra cars didn't feel like enough to abandon the plan.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "an_01"
        ],
        "ground_truth_rationale": "The participant describes a threshold for abandoning the initial target and treats the actual discrepancy as insufficient to do so. This is a repeated manifestation of the same planned anchoring instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "sensor_alert_action_rationale",
        "raw_interview_anchor": "We'd had a derailment at this yard about three weeks earlier ... and that was fresh in my mind. I made the call to pull the whole eleven-car cut.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "The recent derailment is explicitly connected to the choice to pull the full cut after a borderline alert. This is an initial articulation of the single planned availability-bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "sensor_alert_response_scaling",
        "raw_interview_anchor": "The derailment three weeks back was still sitting with me ... I didn't want a repeat, so I went bigger than the book probably called for.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "The vivid recent event drives a response beyond standard procedure for the borderline reading. This repeats the same planned availability-bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_for_sensor_risk",
        "raw_interview_anchor": "It didn't carry the same weight as the derailment ... even though logically the wet-weather false positives happen a lot more often.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "The participant explicitly says the recalled derailment outweighed the more frequent wet-weather false positives. This is the clearest articulation of the planned availability-bias mechanism."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "conflicting_inspection_action_rationale",
        "raw_interview_anchor": "One found a hairline mark ... The other inspected independently and cleared it ... There was also an old repair entry ... I ended up treating it as still suspect and asked for a third pass.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant describes treating the car as suspect after receiving both a mark and an independent clearance, while also mentioning the old repair entry. This is an initial articulation of the single planned confirmation-bias instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "conflicting_evidence_choice",
        "raw_interview_anchor": "I leaned toward Carman A's finding ... Between the mark and that history, it felt like enough to keep the car flagged. I asked for a third inspection rather than accepting Carman B's clearance.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant favors evidence supporting suspicion and rejects the independent clearance, using the old unrelated repair entry as supporting context. This repeats the same planned confirmation-bias instance."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "conflicting_evidence_interpretation",
        "raw_interview_anchor": "Once I already suspected the car, the mark and the repair history just fit what I expected to find. Carman B's 'all clear' almost read to me like it needed double-checking.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant directly describes a prior suspicion shaping interpretation of supporting evidence and discounting a procedurally equivalent clearance. This is the clearest articulation of the planned confirmation-bias instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "report_order_counterfactual",
        "raw_interview_anchor": "If Carman B's report had come in first ... I might have closed it out right there. Order mattered more than it should have, probably.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective counterfactual about report order. The hidden manifest contains no primacy-effect instance, and this statement does not establish the defined confirmation-bias mechanism of selectively weighting evidence according to a prior defect hypothesis."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "dispatch_resource_tradeoff",
        "raw_interview_anchor": "I set the car out and dispatched the rest of the train. Holding the whole consist for one car wasn't going to help anyone ... we'd only eat a partial penalty instead of a full one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The specification explicitly designates this as a genuine trade-off under competing constraints rather than a biased inference. The participant weighs the unresolved car against the SLA consequences of holding the consist."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "incident_counterfactual",
        "raw_interview_anchor": "If the derailment three weeks earlier had never happened ... I think I isolate just the one car and keep moving.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective counterfactual, not an additional decision-time manifestation. The planned availability instance is mapped to the actual sensor-risk decision and its contemporaneous reasoning."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "prospective_estimate_revision",
        "raw_interview_anchor": "I'd probably push back harder on the initial time estimate instead of just carrying it forward.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a proposed future correction during retrospective reflection, not a separate manifested bias occurrence."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "prospective_evidence_review",
        "raw_interview_anchor": "I'd try to look at both carmen's reports side by side instead of one at a time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a proposed future method for reviewing reports, not a separate manifested bias occurrence."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of a single interview transcript for cognitive biases. Retrieved corpus passages were used where they supported a specific mechanism; general knowledge was used only where retrieved support was unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment heuristic",
      "alternative_labels": [
        "anchoring bias",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which people form estimates by starting from an initial value or anchor and then adjust insufficiently from that anchor when new information becomes available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial ready-time estimate after discovering actual car count and retarder speed differed from the handoff",
      "decision_point_description": "Whether to recalculate the 2200 classification target from scratch after learning the cut had 41 cars rather than 38 and the retarders were cycling slower than normal.",
      "affected_reasoning_operation": "Numerical time and planning estimate revision",
      "bias_specific_mechanism": "The participant used the relief yardmaster's 38-car, 2200-target handoff as an initial anchor. After learning the count was 41 cars and the cycle speed was slower, he made only a slight mental adjustment and did not recalculate from the new numbers, consistent with insufficient adjustment from an anchor.",
      "manifestation_in_interview": "The participant explicitly says he kept 2200 as the working target, nudged it slightly, and did not recalculate even though the actual car count and retarder behavior differed from the handoff.",
      "effect_on_reasoning_or_decision": "The original target was carried forward despite material changes in conditions, contributing to the shift being behind schedule.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I kept 2200 as my working target. I nudged it a little in my head, but I didn't sit down and recalculate from the new numbers.",
          "evidence_explanation": "This directly describes insufficient adjustment from the initial 2200/38-car anchor rather than full recalculation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably if the discrepancy had been bigger — if it'd been 50 cars instead of 41, I think I'd have thrown the original number out completely. Three extra cars didn't feel like enough to abandon the plan.",
          "evidence_explanation": "This shows the anchor persisted until a much larger discrepancy threshold was reached, a hallmark of anchoring-and-adjustment."
        }
      ],
      "correction_or_counterevidence": "No in-the-moment correction occurred. In hindsight, the participant said he would push back harder on the initial time estimate.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages from space-flight verification and AI-assisted decision-making describe anchoring-and-adjustment as a process in which initial values produce insufficient subsequent adjustments.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The passage describes anchoring and adjustment: people make estimates based on an initial answer and adjust from there based on additional information; Tversky and Kahneman stated that adjustments are typically insufficient.",
          "mechanism_supported_by_source": "Initial values serve as anchors, and later adjustments from additional information are often insufficient.",
          "relevance_to_this_occurrence": "The participant treated the handoff estimate as the starting value and made only a small adjustment despite new information about car count and retarder speed."
        },
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "The study found that participants' likelihood of sufficiently adjusting away from an incorrect AI prediction increased as the time allocated increased, supporting the anchoring-and-adjustment heuristic as a resource-rational trade-off between time and accuracy.",
          "mechanism_supported_by_source": "Insufficient adjustment away from an initial prediction is characteristic of anchoring-and-adjustment.",
          "relevance_to_this_occurrence": "The participant adjusted away from the initial prediction only slightly and did not sufficiently revise the plan."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which judgments of frequency or risk are influenced by how easily examples come to mind, often making recent, vivid, or emotionally salient events disproportionately influential.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hot-box detector response: whether to isolate only the flagged car or pull the full eleven-car cut for inspection",
      "decision_point_description": "Response to a borderline elevated hot-box temperature on GATX 88213 in wet-weather conditions with a known false-positive history and a recent derailment memory.",
      "affected_reasoning_operation": "Risk judgment and inspection scope decision",
      "bias_specific_mechanism": "The recent derailment was highly vivid and easily recalled, so it dominated the participant's risk assessment of the hot-box alert even though he knew wet-weather false positives were more frequent.",
      "manifestation_in_interview": "The participant explicitly says the recent derailment comes to mind first and outweighed the detector's false-positive history.",
      "effect_on_reasoning_or_decision": "He pulled the entire eleven-car cut for inspection instead of isolating just the flagged car, consuming additional time and contributing to schedule delay.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The derailment three weeks back was still sitting with me. That one started exactly this way — a reading that didn't look dramatic at first. I didn't want a repeat, so I went bigger than the book probably called for.",
          "evidence_explanation": "The recent vivid derailment drives the decision to exceed normal procedure for a borderline reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew about it, yeah. But it didn't carry the same weight as the derailment did. That one's the thing that comes to mind first when a hot-box alert comes in here, even though logically the wet-weather false positives happen a lot more often.",
          "evidence_explanation": "This explicitly shows the more available recent event outweighing better information about the frequency of false positives."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. I think I isolate just the one car and keep moving.",
          "evidence_explanation": "The participant's counterfactual confirms that the derailment memory specifically changed the hot-box decision, supporting availability rather than a purely operational rationale."
        }
      ],
      "correction_or_counterevidence": "The participant knew about the false-positive history but discounted it in the moment. The later third inspection was clean.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic was unavailable; the label is applied from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "biased assimilation",
        "confirmation seeking",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs or hypotheses, while giving less weight to evidence that contradicts them.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Resolution of conflicting carman inspection reports for suspected car GATX 88213",
      "decision_point_description": "Whether to accept the clean inspection report or keep the car flagged and request a third inspection after receiving conflicting carman reports.",
      "affected_reasoning_operation": "Evaluation and weighing of confirmatory versus disconfirmatory evidence",
      "bias_specific_mechanism": "After forming a suspicion about the car, the participant favored the report and repair history that matched his suspicion and discounted the independent clean report as needing double-checking.",
      "manifestation_in_interview": "The participant explicitly says the mark and repair history fit what he expected to find, while Carman B's all-clear felt like it needed double-checking even though it should have carried equal weight.",
      "effect_on_reasoning_or_decision": "He requested a third inspection and kept the car flagged, causing additional delay.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned toward Carman A's finding. There was also that old repair entry on the car, even though it was closed out and unrelated to the bearing concern. Between the mark and that history, it felt like enough to keep the car flagged.",
          "evidence_explanation": "Shows preferential weighting of evidence consistent with suspicion, including an irrelevant closed repair entry."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think once I already suspected the car, the mark and the repair history just fit what I expected to find. Carman B's 'all clear' almost read to me like it needed double-checking, when really it should've carried equal weight.",
          "evidence_explanation": "This is an explicit description of biased interpretation and differential weighting of disconfirmatory evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If Carman B's report had come in first, before Carman A's, I might have closed it out right there. Order mattered more than it should have, probably.",
          "evidence_explanation": "Shows that the initial evidence shaped the hypothesis and subsequent evaluation, consistent with confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that Carman B followed the same protocol and that the reports should have carried equal weight. The third inspection was clean. No contemporaneous correction occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation cockpit source supports confirmation bias as a contributing factor in maintaining an initial interpretation despite contradictory cues, though it does not provide a formal definition. The definition above relies on general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "ACA759 had mistakenly lined up with taxiway Charlie instead of 28R, and despite multiple cues available to the crew... a go-around was not initiated... The confirmation bias as contributing fact.",
          "mechanism_supported_by_source": "Confirmation bias can lead operators to maintain an initial interpretation despite multiple contradictory cues.",
          "relevance_to_this_occurrence": "Similarly, the participant maintained suspicion about the car and discounted the clean report even though the contradictory evidence should have had equal weight."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support for the availability heuristic was unavailable; that label was applied from general cognitive-science knowledge.",
    "The possible order effect in the conflicting carman reports was considered but subsumed under confirmation bias rather than reported as a separate occurrence.",
    "The analysis is based on a single interview without independent performance data or objective benchmarks.",
    "Some statements are retrospective and may reflect after-the-fact reconstruction rather than in-the-moment cognition."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_3_Sonar_on",
  "interview_id": "RT_Biased_3",
  "system_prompt_id": "Sonar",
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
