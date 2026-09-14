You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal analytic training purposes only, not for any evaluation of your performance. Is that alright with you?

Participant: Yes, that's fine. I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your role and your relationship to this particular account?

Participant: I'm a strategic all-source analyst. I've owned the border garrison account for a little over three years now, alongside six other accounts. It's one of those long-running files where the judgment hasn't moved much — low activity, defensive posture, nothing indicating an offensive buildup. That's been the analytic line since before I inherited it.

Interviewer: Let's start with a general account of the incident we're here to discuss. What happened?

Participant: Over about two weeks, we started getting a handful of reports that didn't fit neatly into the existing picture. First was an imagery report — earth-moving equipment and some new foundation work near a motor pool that had been inactive for as long as anyone could remember. Then a SIGINT analyst flagged an intercept referencing something called "phase two" in the garrison's comms, which nobody could immediately place. And then our liaison partner reported unusual convoy movement at night, three nights running. All of this came in while I was prepping for the quarterly warning board, where I'd need to either sustain or revise the standing assessment.

Interviewer: What was your objective during this period?

Participant: Get it right without overreacting. We've had cycles before where a single ambiguous report triggers a scramble, collection gets retasked away from higher-priority theaters, and it turns out to be nothing. I didn't want to cry wolf on an account that's been stable for three assessment cycles. At the same time, obviously, if something real was changing, I needed to catch it before the board, not after.

Interviewer: What constraints were you working under?

Participant: The usual ones — collection assets are shared across theaters that are ranked higher priority than this one, so tasking anything extra takes justification. I had my other six accounts competing for the same hours in the day. And the liaison service that reported the convoys has a mixed track record — historically maybe six in ten of their reports pan out. So I had to weigh all of that against a board deadline that was about ten days out.

Interviewer: Let's reconstruct the timeline in order. What came in first?

Participant: The imagery report came first, maybe twelve days before the board. Then the SIGINT intercept about five days after that. The liaison convoy reporting came in over the last three nights before the board prep really kicked into gear, so maybe four to six days out.

Interviewer: How did each of those get logged or routed when they arrived?

Participant: The imagery went into the case file as an update — it gets reviewed at the next scheduled cycle unless something flags it for early attention. The intercept got filed under the existing account entry. The convoy reporting got an annotation from me once I looked at it. None of them got kicked upstairs individually; they came to me first since I own the account.

Interviewer: Let's go through the imagery report specifically. What stood out to you, and what did you decide to do?

Participant: The equipment and foundation work were new, that's true — no anomalies like that in the imagery for at least eighteen months. But construction near a motor pool isn't inherently alarming; garrisons refurbish infrastructure for all kinds of reasons, maintenance, logistics upgrades. Given three straight years of assessments concluding no material change, I logged it as a routine update rather than flagging it as a deviation from baseline. I didn't task follow-on collection immediately — the next available window was about ten days out anyway.

Interviewer: What alternatives did you consider at that point?

Participant: I thought about pushing for immediate follow-on imagery, and I thought about flagging it to my branch chief right then for an out-of-cycle conversation. But collection is scarce, and a single unexplained construction indicator didn't feel like enough to justify jumping the queue ahead of higher-priority theaters.

Interviewer: How confident were you in that call?

Participant: Reasonably. Not fully — there's always some uncertainty with a single indicator. But nothing about it screamed urgent.

Interviewer: Moving to the SIGINT intercept. Walk me through your reasoning there.

Participant: The SIGINT analyst brought me the "phase two" reference and asked whether it should be treated as a new indicator. I looked at the broader communications pattern, and outside that one phrase, everything else matched historical baselines — same frequency, same general traffic volume. So I characterized it as ambiguous, non-actionable language, consistent with how this garrison's comms have looked for years.

Interviewer: Did you compare it against the imagery report from a few days earlier?

Participant: Not directly, no. They came from different collection disciplines and different analysts brought them to me separately. At the time it didn't occur to me to sit them side by side — the intercept read as ambiguous on its own terms, so I treated it that way.

Interviewer: What sources did you consult before making that call?

Participant: Mainly the SIGINT analyst's write-up and the historical comms baseline in our database. I didn't pull the imagery file back up at that point.

Interviewer: Let's talk about the convoy reporting. What was your process there?

Participant: My branch chief asked for a preliminary read ahead of the board. I looked at the liaison's track record — about sixty percent corroboration historically — and given that base rate, I annotated the report as uncorroborated and consistent with the liaison's usual noise level. I didn't request independent verification from our own overhead assets against those specific nights.

Interviewer: What alternatives were available to you there?

Participant: I could have tasked an independent asset to check those nights specifically, or I could have flagged it as an open item requiring resolution before the board instead of discounting it outright. Given the timeline and the asset competition, I leaned on the liaison's reliability history as the main basis for how much weight to give it.

Interviewer: Did you connect the convoy reporting with the imagery or the intercept at that stage?

Participant: Not really — each one got assessed against its own history and its own source reliability. It wasn't until later, when I sat down to draft the board summary, that I had all three in front of me together.

Interviewer: Tell me about that moment — pulling the recommendation together for the board.

Participant: With about forty-eight hours left, I had the construction indicator, the intercept, and the convoy reporting all in the case file at once, which was actually the first time I'd looked at them side by side rather than one at a time. My recommendation was to sustain the existing steady-state judgment, with a caveat flagging the three items for continued monitoring. My reasoning was that we've had three consecutive years of stable assessments, and each of these three items, taken on its own, fell within the kind of noise this account has produced before. That track record carried a lot of weight in how much additional verification effort I felt was warranted before finalizing the call.

Interviewer: Did you consider treating the three together as a potential pattern rather than as separate items?

Participant: I noted them together in the write-up, but I didn't reframe the overall confidence level because of it. The account's history of stability was the anchor point for the recommendation.

Interviewer: What happened after the board?

Participant: The board accepted the sustained judgment with the caveats noted. About three weeks later, additional reporting came in that suggested the garrison's posture might actually have shifted, which triggered a retrospective look back at the quarterly call. That review is still ongoing, so I can't tell you definitively yet whether the original read was wrong or whether this new reporting is its own separate development.

Interviewer: If the imagery report had come in on a brand-new account with no track record behind it, do you think you'd have handled it differently?

Participant: Probably, yes. Without three years of stable assessments sitting behind it, I think a single unexplained construction indicator would have gotten more immediate scrutiny, maybe an earlier push for follow-on collection.

Interviewer: What information, if it had arrived earlier, would have changed your recommendation at the board?

Participant: If I'd had independent confirmation on the convoy nights, or if the SIGINT and imagery had been flagged together earlier instead of separately, that combination might have shifted my confidence level enough to recommend an upgrade rather than a caveat.

Interviewer: Looking back, what would you tell a junior analyst handling a similar long-running low-threat account?

Participant: I'd say don't let a good track record become the reason you stop cross-checking new reporting against everything else that's come in recently. It's easy to evaluate each report against its own history in isolation. I'd tell them to make a habit of pulling related indicators together sooner, not just when you're already sitting down to write the board summary.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_1",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "All-Source Intelligence Analyst (Strategic)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Steady State: Reassessing a Long-Dormant Border Garrison",
    "scenario_summary_internal": "A senior strategic all-source analyst has monitored a foreign border garrison for three years under a standing assessment of 'low activity, defensive posture only.' New multi-INT indicators (satellite imagery showing engineering equipment, a signals intercept referencing 'phase two,' and a liaison report of unusual night convoys) begin arriving over a two-week period. The analyst must decide whether to escalate, reframe, or fold the new data into the existing steady-state narrative before a quarterly strategic warning board. The incident tests whether long-standing threat assessments are re-examined with appropriate rigor when disconfirming evidence begins to accumulate, or whether the existing 'nothing changes here' judgment is preserved through reduced vigilance and routinized handling of new inputs.",
    "occupational_realism": {
      "objective": "Determine whether the garrison's new activity indicators warrant an upgraded threat assessment and formal warning notification before the quarterly board, without triggering an unnecessary alert fatigue cycle.",
      "setting": "A strategic intelligence fusion cell supporting a regional command, three years into monitoring a border garrison previously assessed as low-threat and defensively postured.",
      "constraints": [
        "Quarterly warning board convenes in 10 days; assessment must be finalized 48 hours prior",
        "Collection assets are shared across higher-priority theaters, limiting tasking flexibility",
        "Analyst carries a portfolio of six other accounts alongside this one",
        "Liaison reporting from the partner service has a mixed reliability history",
        "Prior three annual assessments all concluded 'no material change'"
      ],
      "stakeholders": [
        "Strategic all-source analyst (interviewee)",
        "Branch chief responsible for the quarterly warning board briefing",
        "Imagery analyst providing the engineering-activity report",
        "SIGINT analyst flagging the 'phase two' intercept",
        "Partner-nation liaison officer reporting convoy activity",
        "Regional command watch officer"
      ],
      "technical_terms_to_use": [
        "steady-state assessment",
        "indications and warning (I&W)",
        "multi-INT fusion",
        "collection tasking",
        "confidence level",
        "warning board",
        "baseline deviation",
        "analytic line"
      ],
      "technical_terms_to_avoid": [
        "complacency bias",
        "cognitive bias",
        "anchoring",
        "status quo bias",
        "normalcy bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three consecutive annual assessments rated the garrison as low-activity, defensive-only",
          "New satellite imagery shows earth-moving equipment and new foundation work near a previously inactive motor pool",
          "No prior imagery anomalies had been reported in over 18 months"
        ],
        "new_information_after_decision": [
          "The imagery analyst's report is logged as a routine update rather than a baseline-deviation flag",
          "No follow-on collection is tasked against the site for another 10 days"
        ],
        "alternatives": [
          "Task immediate follow-on imagery collection to confirm whether construction indicates a capability change",
          "Log the report as a minor update consistent with the existing steady-state judgment and revisit at the next scheduled review",
          "Flag the discrepancy to the branch chief for an out-of-cycle discussion"
        ],
        "intended_action": "Analyst logs the new construction activity as a routine update within the existing steady-state file, citing three years of consistent low-activity assessments, and does not escalate or retask collection."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIGINT intercept references an unidentified 'phase two' in a garrison communications channel",
          "The garrison's communications patterns have otherwise matched historical baselines",
          "The SIGINT analyst requests analytic input on whether 'phase two' should be treated as a new indicator"
        ],
        "new_information_after_decision": [
          "The intercept is filed under the existing account without a new indicator code",
          "No cross-reference is made against the earlier imagery report from Phase 1"
        ],
        "alternatives": [
          "Cross-reference the intercept against the recent imagery findings to test for a converging pattern",
          "Request additional SIGINT collection to clarify the meaning of 'phase two'",
          "Treat the intercept as ambiguous background noise consistent with historical low-threat communications"
        ],
        "intended_action": "Analyst characterizes the intercept as ambiguous and non-actionable, consistent with the garrison's historical communications pattern, without cross-referencing it against the imagery indicator from Phase 1."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Partner-nation liaison reports unusual night convoy movements near the garrison over three consecutive nights",
          "Liaison service has a mixed reliability history, with roughly 60% of past reports corroborated",
          "The branch chief asks the analyst for a preliminary read ahead of the warning board"
        ],
        "new_information_after_decision": [
          "The convoy report is annotated as 'uncorroborated, consistent with liaison's historical noise level'",
          "The analyst does not request independent verification against available overhead assets"
        ],
        "alternatives": [
          "Request tasking of an independent collection asset to verify or refute the convoy reporting",
          "Weight the convoy report cautiously but flag it as a data point requiring resolution before the board",
          "Discount the report primarily on the basis of the liaison's historical reliability record"
        ],
        "intended_action": "Analyst discounts the convoy reporting largely on the liaison's historical reliability record, without independently verifying it, and does not integrate it with the imagery and SIGINT indicators already on file."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All three indicators (construction, intercept, convoys) are now visible together in the case file for the first time as the analyst drafts the warning board summary",
          "The branch chief expects a recommendation: sustain the existing assessment or propose an upgrade",
          "Time remaining before the assessment is due: approximately 48 hours"
        ],
        "new_information_after_decision": [
          "The warning board accepts the sustained low-activity judgment with minor caveats noted for future monitoring",
          "Three weeks later, additional reporting suggests the garrison's posture may have changed, prompting a retrospective review of the quarterly assessment"
        ],
        "alternatives": [
          "Synthesize the three indicators as a potential converging pattern and recommend an upgraded confidence level or formal warning",
          "Sustain the existing steady-state judgment with a caveat noting the indicators for future monitoring",
          "Request a short extension to task confirmatory collection before finalizing the recommendation"
        ],
        "intended_action": "Analyst sustains the existing steady-state judgment for the warning board, treating each indicator individually as within historical noise levels rather than synthesizing them as a potential converging signal, citing the multi-year track record of stability as the primary basis for confidence."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how you first became involved in monitoring this garrison account?",
        "What was your understanding of the account's threat status going into this period?"
      ],
      "timeline_reconstruction": [
        "Walk me through, in order, how each new piece of reporting came in over the two-week period.",
        "At what point did you first see the imagery, the intercept, and the convoy reporting?",
        "How did each report get logged or routed once it arrived?"
      ],
      "decision_point_probes": [
        "What specific cues in the imagery report stood out to you, if any?",
        "What sources did you consult before deciding how to characterize the intercept?",
        "What alternatives did you consider for handling the convoy reporting?",
        "What was your main basis for the recommendation you brought to the warning board?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in each judgment at the time you made it?",
        "What prior experience with this account shaped how you interpreted the new reporting?"
      ],
      "closing_hypotheticals": [
        "If the imagery report had arrived without the account's three-year track record behind it, how might you have handled it differently?",
        "If you had unlimited collection assets, what would you have tasked differently across this period?",
        "Looking back, what would you tell a junior analyst about how to handle a long-running low-threat account when new indicators start to appear?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "decision_point": 4,
        "mechanism": "Analyst relies on the multi-year track record of a stable, low-threat judgment as the primary justification for sustaining the existing assessment, treating newly converging multi-INT indicators as individually explainable rather than triggering a full re-evaluation of vigilance or verification effort at the synthesis stage.",
        "affected_reasoning_operation": "Evidence synthesis and confidence calibration at the point of final judgment formation",
        "evidence_available_at_time": [
          "Imagery indicator of new construction from Phase 1",
          "SIGINT 'phase two' intercept from Phase 2",
          "Liaison convoy reporting from Phase 3",
          "Three years of prior steady-state assessments"
        ],
        "required_textual_manifestation": "In responding to the closing decision-point probe, the analyst should explicitly cite the account's long track record of stability as the reason for not escalating verification effort, while acknowledging the three indicators were seen together for the first time without prompting a corresponding increase in scrutiny.",
        "plausible_nonbias_interpretation": "The analyst could reasonably conclude that each indicator was individually weak and that base-rate stability legitimately supports a cautious, non-alarmist recommendation given resource constraints.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "complacency",
          "cognitive bias",
          "vigilance decrement",
          "reduced scrutiny due to routine"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario requested for this generation."
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
      "Confirm the interview contains exactly four decision points, each with at least two plausible alternatives.",
      "Confirm exactly one Complacency Bias instance is embedded, located at decision point 4, with no repetition or reinforcement of the same judgment elsewhere.",
      "Confirm decision points 1-3 contain plausible, non-bias-labeled analyst reasoning that sets up the evidentiary basis for the Phase 4 instance without themselves being scored as bias instances.",
      "Confirm no bias terminology, labels, or psychological explanations appear anywhere in the interview text.",
      "Confirm total word count falls between 1,215 and 1,485 words, targeting 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm the outcome (retrospective review three weeks later) does not mechanically confirm or deny whether the Phase 4 judgment was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Complacency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Complacency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Complacency Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "mechanism": "Reliance on a long track record of stability to justify sustained low vigilance and forgone verification effort at the point of synthesizing newly converging multi-INT indicators, rather than treating the convergence itself as a trigger for renewed scrutiny.",
        "affected_reasoning_operation": "Evidence synthesis and confidence calibration during final judgment formation for the warning board",
        "evidence_source": "Combined imagery (Phase 1), SIGINT (Phase 2), and liaison convoy (Phase 3) indicators viewed together for the first time in Phase 4, against the backdrop of three years of prior steady-state assessments",
        "distinctiveness_requirement": "This is the only planned Complacency Bias instance; it must be identifiable specifically at the synthesis/final-judgment stage and must not be a restatement of the individual handling decisions in Phases 1-3, which are evidentiary setup rather than counted instances."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
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
    "scenario_id": "IA_Biased_1",
    "domain_id": "IA",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the strongest mechanism fit and narrative realism: the final synthesis/recommendation decision (Phase 4), where prior track-record reliance most plausibly suppresses appropriate re-evaluation of newly converging evidence. Phases 1-3 were designed to supply the necessary evidentiary buildup without themselves constituting counted instances, per the exact-occurrence rule limiting the bias to one independently identifiable manifestation.",
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
        "segment_type": "objective_and_rationale",
        "raw_interview_anchor": "Get it right without overreacting… didn't want to cry wolf… catch it before the board.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "constraints_and_evidence_weighting",
        "raw_interview_anchor": "Collection assets are shared… liaison reports historically maybe six in ten… weigh all of that against a board deadline.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "imagery_interpretation_and_action",
        "raw_interview_anchor": "Construction… isn't inherently alarming… Given three straight years… logged it as a routine update… didn't task follow-on collection.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "imagery_alternatives_and_resource_rationale",
        "raw_interview_anchor": "Thought about immediate follow-on imagery and flagging it… collection is scarce… a single indicator didn't feel like enough.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "imagery_confidence_assessment",
        "raw_interview_anchor": "Reasonably. Not fully… uncertainty with a single indicator. Nothing… screamed urgent.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "sigint_interpretation",
        "raw_interview_anchor": "Outside that one phrase, everything else matched historical baselines… characterized it as ambiguous, non-actionable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "cross_source_comparison_choice",
        "raw_interview_anchor": "Not directly… didn't occur to me to sit them side by side… intercept read as ambiguous on its own terms.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the Phase 2 decision not to compare reports; the manifest designates Phases 1–3 as setup, not scored instances."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "information_search_choice",
        "raw_interview_anchor": "Mainly the SIGINT analyst's write-up and historical comms baseline. I didn't pull the imagery file back up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "liaison_report_weighting",
        "raw_interview_anchor": "Given that base rate, I annotated the report as uncorroborated… didn't request independent verification.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "convoy_alternatives_and_resource_rationale",
        "raw_interview_anchor": "Could have tasked an independent asset or flagged an open item… leaned on reliability history.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "indicator_integration_process",
        "raw_interview_anchor": "Each one got assessed against its own history and source reliability… later… all three in front of me together.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive reasoning or evidence weighting, but it is outside the sole Phase 4 target specified in the manifest."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "board_recommendation_and_synthesis_rationale",
        "raw_interview_anchor": "All three… at once… recommend sustain… each item… within historical noise… track record carried a lot of weight in verification effort.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The final synthesis treats all three indicators individually as historical noise and lets the multi-year stability record drive verification effort and the recommendation; this is the one planned Complacency Bias instance."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "board_confidence_reframing",
        "raw_interview_anchor": "Noted them together… didn't reframe confidence… history of stability was the anchor point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant explicitly declines to reframe confidence after considering the indicators together because the stability history anchors the recommendation; this is the same single instance."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "closing_counterfactual",
        "raw_interview_anchor": "Without three years of stable assessments… construction… would have gotten more immediate scrutiny.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective hypothetical about Phase 1, not an additional contemporaneous manifestation."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "counterfactual_information_value",
        "raw_interview_anchor": "Independent convoy confirmation or SIGINT and imagery flagged together earlier… might have shifted confidence.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is counterfactual or retrospective reasoning, not an additional manifested instance."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "retrospective_advice",
        "raw_interview_anchor": "Don't let a good track record become the reason you stop cross-checking… pull related indicators together sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is counterfactual or retrospective reasoning, not an additional manifested instance."
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
    "analysis_scope_note": "Conservative mechanism-first analysis of the analyst's self-reported reasoning. Operational constraints and source-reliability vetting were considered as alternative explanations, and only bias mechanisms affirmatively evidenced by the transcript were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which an initial reference point or prior judgment exerts disproportionate influence on subsequent estimates, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Quarterly board assessment of newly reported garrison indicators",
      "decision_point_description": "Whether to sustain the standing steady-state judgment or escalate collection/verification in response to the imagery, SIGINT, and liaison convoy reports.",
      "affected_reasoning_operation": "Integration and weighting of new evidence against a standing analytic baseline",
      "bias_specific_mechanism": "The three-year standing assessment functioned as an anchor; each anomalous report was evaluated relative to that stable baseline and discounted as routine or noise, with insufficient adjustment away from the anchor even when three indicators were available together.",
      "manifestation_in_interview": "The participant repeatedly used the account's long-term stability as the reference for current reports, logged the first novel construction indicator as routine, and explicitly stated that the account's history of stability was the anchor point for the board recommendation.",
      "effect_on_reasoning_or_decision": "The prior stable baseline suppressed escalation to follow-on collection or an upgraded warning-board recommendation; the standing judgment was sustained with only continued-monitoring caveats.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given three straight years of assessments concluding no material change, I logged it as a routine update rather than flagging it as a deviation from baseline.",
          "evidence_explanation": "Shows the prior baseline directly shaped interpretation and action for the first novel imagery indicator, rather than the indicator's intrinsic diagnostic value."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My reasoning was that we've had three consecutive years of stable assessments, and each of these three items, taken on its own, fell within the kind of noise this account has produced before.",
          "evidence_explanation": "Demonstrates the prior baseline was the dominant comparator; the three new items were partitioned into historical noise, leaving the anchor substantially unadjusted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The account's history of stability was the anchor point for the recommendation.",
          "evidence_explanation": "Explicitly identifies the standing historical judgment as the cognitive anchor guiding the board recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. Without three years of stable assessments sitting behind it, I think a single unexplained construction indicator would have gotten more immediate scrutiny, maybe an earlier push for follow-on collection.",
          "evidence_explanation": "Counterfactual statement that the account's track record, rather than the indicator's features, drove the decision not to scrutinize or collect."
        }
      ],
      "correction_or_counterevidence": "The participant did not ignore the indicators entirely: he flagged all three for continued monitoring, acknowledged uncertainty about the imagery call, and described an ongoing retrospective review after later reporting. However, no debiasing occurred before the board decision; the safeguards were partial and did not alter the sustaining recommendation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieval provided background on anchoring-and-adjustment; the passage is from an AI-assisted decision-making study rather than this exact intelligence-account setting, but it supports the general heuristic mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment heuristic: judgments remain tied to an initial reference value unless conditions allow sufficient adjustment.",
          "relevance_to_this_occurrence": "Supports the anchoring-and-adjustment mechanism visible in the participant's continued reliance on the prior stable assessment when weighing new indicators."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory bias",
        "Hypothesis persistence"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or weigh evidence in ways that uphold an existing hypothesis or prior expectation, and to discount ambiguous or disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "SIGINT and liaison report interpretation prior to board",
      "decision_point_description": "Whether the 'phase two' intercept and nighttime convoy reports should be treated as potentially meaningful new indicators or as historical noise.",
      "affected_reasoning_operation": "Interpretation and corroboration of ambiguous reports relative to an existing account judgment",
      "bias_specific_mechanism": "The participant assimilated ambiguous evidence into the standing no-material-change hypothesis: an intercept was read as non-actionable and consistent with historical communications, convoy reporting as consistent with the liaison's usual noise, and each indicator was evaluated against its own history rather than jointly as a potential pattern, preserving the prior judgment.",
      "manifestation_in_interview": "The participant did not directly compare the SIGINT report with the earlier imagery report, characterized the intercept as ambiguous and non-actionable because it matched historical baselines, and discounted the liaison convoy report based on source reliability without requesting independent verification.",
      "effect_on_reasoning_or_decision": "Reduced the likelihood that three convergent anomalous indicators would be treated as a potential pattern, contributing to sustaining the standing assessment and avoiding tasking of additional verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I characterized it as ambiguous, non-actionable language, consistent with how this garrison's comms have looked for years.",
          "evidence_explanation": "Shows ambiguous information being resolved in favor of the pre-existing hypothesis that nothing had changed, rather than treated as a potentially disconfirming anomaly."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly, no. They came from different collection disciplines and different analysts brought them to me separately. At the time it didn't occur to me to sit them side by side — the intercept read as ambiguous on its own terms, so I treated it that way.",
          "evidence_explanation": "Demonstrates failure to seek or integrate potentially pattern-forming evidence, consistent with a confirmatory mode of evaluating the current report against the existing view."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "given that base rate, I annotated the report as uncorroborated and consistent with the liaison's usual noise level. I didn't request independent verification from our own overhead assets against those specific nights.",
          "evidence_explanation": "Uses source history to categorize the report as noise, excluding independent disconfirmation even though verification was possible."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really — each one got assessed against its own history and its own source reliability. It wasn't until later, when I sat down to draft the board summary, that I had all three in front of me together.",
          "evidence_explanation": "Explicitly describes isolated evaluation of each indicator, which prevented pattern recognition and preserved the standing judgment."
        }
      ],
      "correction_or_counterevidence": "The participant eventually placed all three indicators side by side in the board summary and recommended continued monitoring. Legitimate resource constraints and the liaison's mixed track record provide plausible competing contributors, so confidence is moderate rather than high.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved intelligence-analysis paper supports confirmation bias as a documented analyst bias, though it does not provide a direct task-specific diagnosis; it is used for mechanism grounding.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human factors of the confirmation bias in intelligence analysis: decision support from graphical evidence layouts",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "The goals for this study were to document the extent of the conﬁrmation bias exhibited by analysts working the initial steps of a problem and to investigate the efﬁcacy of two new bias-reducing techniques.",
          "mechanism_supported_by_source": "Confirmation bias in intelligence analysis: analysts exhibit confirmatory evidence selection and interpretation during initial problem steps.",
          "relevance_to_this_occurrence": "The participant was working the initial steps of account assessment and displayed a confirmatory interpretation and prioritization pattern consistent with the source's documented analyst confirmation bias."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report, so recall and self-presentation may affect the evidence.",
    "Retrieved corpus passages are sparse and from adjacent domains such as intelligence analysis and AI-assisted decision making, providing conceptual rather than context-specific grounding.",
    "The analyst faced real operational constraints, including collection scarcity and competing accounts, which complicate isolation of cognitive bias from resource-based decision making."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_1_Sonnet_on",
  "interview_id": "IA_Biased_1",
  "system_prompt_id": "Sonnet",
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
