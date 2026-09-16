<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is a cognitive task analysis interview — I want to understand how you actually worked through a specific production problem, including what you knew at each point and why you chose what you did. There are no right answers I'm grading you against. Okay to start?

Participant: Sure, no problem. I've got a decent example — the Line 3 flash issue before our Meridian shipment a few weeks back.

Interviewer: Great, let's use that. Can you describe the overall situation and what you were trying to accomplish?

Participant: We had a 72-hour window to ship a Meridian order off Line 3 — interior clips, tight tolerances. Partway through a night shift, scrap jumped from about 1.8% to 6.4%, mostly flash, some short shots. My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway.

Interviewer: What were the first signs something was wrong?

Participant: Quality flagged the scrap numbers, and the SPC chart showed cavity pressure drifting starting mid-shift. That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction.

Interviewer: Did anything from past experience come to mind?

Participant: We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring.

Interviewer: So what did you do with that uncertainty?

Participant: I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other.

Interviewer: What came back?

Participant: Humidity logs were normal. Tooling data showed moderate wear had built up. So the wear side turned out to be the real thread, but I couldn't have known that going in — it really could have gone either way based on what we had.

Interviewer: Let's reconstruct the next couple of days. What happened once wear was confirmed?

Participant: That's decision point two. Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on.

Interviewer: How did you resolve that?

Participant: We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.

Interviewer: Did that resolve things?

Participant: Partially. Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which.

Interviewer: Take me to the third point — the call with the sister plant.

Participant: Right, this was day two, when my quality engineer was out sick, so I had less support than usual. I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.

Interviewer: What did you know about how well it would apply to your line specifically?

Participant: My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet.

Interviewer: So what did you decide?

Participant: I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one.

Interviewer: What happened after?

Participant: Short-term, flash defects dropped. Then two shifts later we got a new warping issue on some parts, cause not yet clear. Might be related to the cooling change, might not.

Interviewer: Last decision point — the rollout call.

Participant: Right. By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability. Corporate quality asked if we should roll the fix to Lines 4 and 6.

Interviewer: What made that decision hard?

Participant: Lines 4 and 6 have different tooling age profiles than Line 3, so I couldn't just assume the fix would transfer cleanly either way. Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down.

Interviewer: So what did you approve?

Participant: A limited pilot on one line with extra monitoring, rather than pushing it to both. I said as much to corporate — that the data didn't support going all-in yet, but doing nothing wasn't realistic either.

Interviewer: What came of the pilot?

Participant: Initial improvement, then a new tooling alarm showed up on that line that we hadn't seen before. A fuller week-long review later suggested the underlying wear issue was only partly addressed.

Interviewer: What information would have made these calls easier?

Participant: Faster wear measurements at decision two, and full geometry validation before decision three. Those were the two spots where I felt like I was deciding on incomplete information out of necessity, not preference.

Interviewer: If the last shift's numbers had come in worse instead of better, would decision four have gone differently?

Participant: Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer.

Interviewer: Anything you'd do differently if this happened again?

Participant: Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants. Otherwise, honestly, most of these calls I'd probably make the same way again given the same constraints.

Interviewer: This has been really helpful, thank you.

Participant: Anytime.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Ambigious_5",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Plant/Industrial Production Manager",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Line 3 Flash Defect Spike Before the Meridian Shipment (Ambiguous Variant)",
    "scenario_summary_internal": "A plant manager at a mid-size injection molding facility must diagnose and correct a sudden rise in flash/short-shot defects on Line 3 in the four days before a large customer (Meridian Automotive) shipment deadline. The manager faces the same operational objective, constraints, stakeholders, and four decision points as the paired biased scenario (IP_Biased_5), but at each decision point the available evidence is genuinely incomplete or conflicting, so the manager's choices remain defensible under multiple reasonable interpretations. No decision is driven by a fixed prior anchor, vivid recall, social consensus, recency-weighting, or miscalibrated certainty; each choice reflects reasonable, resource-constrained judgment under authentic uncertainty.",
    "occupational_realism": {
      "objective": "Restore Line 3 output to spec-compliant quality (scrap rate back under 2%) in time to fulfill the Meridian shipment without triggering a full line shutdown or missing the ship date.",
      "setting": "A 24/7 mid-size automotive-parts injection molding plant running three shifts, with a quality lab, a maintenance/tooling team, and a corporate quality network linking four sister plants.",
      "constraints": [
        "72-hour window before the Meridian shipment must ship",
        "Limited access to the sister plant's full defect log, only a summary shared in a call",
        "Tooling change requires a scheduled press-down window shared with two other product runs",
        "Quality engineer is out sick during the second day, reducing statistical support",
        "Corporate directive discourages full-line shutdowns without VP sign-off"
      ],
      "stakeholders": [
        "Plant/Industrial Production Manager (interviewee)",
        "Shift supervisors (Shift A, B, C)",
        "Quality engineer",
        "Tooling/maintenance lead",
        "Sister-plant production manager (peer)",
        "Corporate quality director",
        "Meridian Automotive account representative"
      ],
      "technical_terms_to_use": [
        "flash defect",
        "short shot",
        "cycle time",
        "scrap rate",
        "mold cavity pressure",
        "resin lot",
        "tooling wear",
        "SPC chart",
        "press-down window",
        "hold pressure"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "anchoring",
        "availability heuristic",
        "bandwagon",
        "overconfidence",
        "recency effect",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scrap rate on Line 3 jumped from 1.8% to 6.4% over the last 12-hour shift",
          "SPC chart shows a cavity-pressure drift starting mid-shift, but the drift magnitude is within a range that has previously been linked to both humidity and early-stage tooling wear",
          "A similar defect pattern six months earlier was traced to humidity, but that plant configuration has since changed (new dehumidifier installed), making direct comparison uncertain",
          "Tooling wear data has not yet been pulled and would take roughly the same time to retrieve as humidity logs"
        ],
        "new_information_after_decision": [
          "Humidity logs come back normal",
          "Tooling wear data, pulled shortly after, shows moderate wear accumulation"
        ],
        "alternatives": [
          "Check humidity/drying conditions first, given the historical precedent",
          "Check tooling wear first, given the equally plausible connection to pressure drift",
          "Request both checks be run in parallel using two available technicians"
        ],
        "intended_action": "Manager decides to run the humidity check and the tooling-wear pull in parallel using two available technicians, explicitly noting that either cause is plausible and that sequencing one before the other could not be justified from the data alone; both come back within a similar timeframe."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tooling wear confirmed as a contributing factor; wear severity readings are borderline between the plant's threshold for a minor hold-pressure adjustment and the threshold for a full insert swap",
          "Two candidate fixes exist: incremental hold-pressure adjustment (lower risk, slower to validate) or a full mold-insert swap (faster perceived fix, requires press-down window)",
          "The tooling lead and the shift supervisor disagree on whether the wear reading is closer to the adjustment threshold or the swap threshold",
          "The press-down window, if used now, will not be available again for five days"
        ],
        "new_information_after_decision": [
          "The insert swap is completed within the available press-down window",
          "Early results show partial improvement but scrap rate does not fully return to baseline, which is consistent with either an correctly-diagnosed-but-incomplete fix or a secondary contributing factor not yet identified"
        ],
        "alternatives": [
          "Choose the insert swap now, given the closing press-down window and borderline wear reading",
          "Choose the incremental hold-pressure adjustment and monitor over several cycles, accepting slower validation",
          "Request a second wear measurement to resolve the disagreement before deciding, at the cost of losing the press-down window"
        ],
        "intended_action": "Manager weighs the disagreement between the tooling lead and shift supervisor, notes that the window will close before a second measurement could realistically change the threshold classification, and selects the insert swap primarily citing the closing window and the borderline reading rather than a settled diagnosis."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A call with the sister-plant manager reveals that three of the four sister plants adopted a cooling-time reduction protocol, but two of those three plants run a different resin lot and slightly different cavity geometry than Line 3",
          "The plant's own quality engineer has partially validated the protocol against Line 3's resin lot but has not completed testing against the specific cavity geometry due to being out sick part of the day",
          "Corporate quality director notes the protocol is showing promising but not yet conclusive results network-wide"
        ],
        "new_information_after_decision": [
          "Applying the cooling-time reduction produces a short-term drop in flash defects",
          "A new, unrelated warping issue emerges on a subset of parts two shifts later, with cause not yet determined"
        ],
        "alternatives": [
          "Adopt the cooling-time reduction protocol based on the partial validation already completed",
          "Wait for the quality engineer to complete geometry-specific validation before adopting",
          "Adopt a modified, more conservative version of the protocol pending full validation"
        ],
        "intended_action": "Manager adopts the protocol after the partial validation, explicitly weighing the incomplete geometry testing against the shipment deadline, and acknowledges in the account that the decision could reasonably have gone either way given the partial data."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The most recent shift (last 8 hours) shows scrap rate down to 1.5%, the best reading in four days",
          "The full four-day trend, including the warping issue from phase 3, is more mixed and shows only 2.9% average improvement with unresolved variability",
          "Meridian shipment must be finalized within hours, and the corporate quality director is asking whether the fix should be rolled out to Lines 4 and 6",
          "Lines 4 and 6 have different tooling age profiles than Line 3, making direct extrapolation uncertain in either direction"
        ],
        "new_information_after_decision": [
          "Lines 4 and 6 initially show improvement, but one line later reports a new tooling alarm not previously seen",
          "A fuller week-long data review shows the underlying wear-related root cause was only partially addressed"
        ],
        "alternatives": [
          "Approve immediate rollout to Lines 4 and 6, citing the deadline and the latest positive shift",
          "Request one more full day of Line 3 data across all shifts before recommending rollout",
          "Approve a limited pilot rollout to one additional line with added monitoring"
        ],
        "intended_action": "Manager approves a limited pilot rollout to one line with added monitoring rather than a full rollout to both lines, explicitly stating that the mixed four-day trend and differing tooling profiles on Lines 4 and 6 made a full rollout premature, while also noting the deadline pressure made some rollout decision unavoidable."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first indicated something was wrong on Line 3?",
        "What was your primary objective when you were first notified?"
      ],
      "timeline_reconstruction": [
        "What happened right after you were told about the scrap rate spike?",
        "Walk me through the sequence of checks, calls, and decisions over the four days.",
        "What information came in after each major decision, and how did it change things?"
      ],
      "decision_point_probes": [
        "At that moment, what options did you consider, and why did you rule the others out?",
        "What evidence or past experience were you drawing on when you made that call?",
        "Who else was involved, and how much did their input shape your decision?",
        "Looking back, what information did you have available that you didn't use, or used less than others?",
        "What information would have changed your decision at that point?"
      ],
      "closing_hypotheticals": [
        "If the sister plants had not shared their protocol, would your approach have been different?",
        "If the last shift's numbers had looked worse instead of better, would you have made the same rollout call?",
        "What would you do differently if a similar defect spike happened again next quarter?",
        "How much uncertainty did you feel you were operating under at each stage, in hindsight?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IP_Biased_5",
      "features_to_match": [
        "Same operational objective, setting, constraints, and stakeholders as IP_Biased_5",
        "Same four decision points in the same sequence and narrative role (diagnosis, fix selection, protocol adoption, rollout decision)",
        "Same technical vocabulary and level of domain detail",
        "Same overall difficulty, emotional tone, and time pressure",
        "Same probe structure and coverage (cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, hypotheticals)"
      ],
      "features_to_remove_or_change": [
        "Remove the fixed anchor to the six-month-old humidity case; introduce a changed plant configuration that makes the historical parallel genuinely uncertain",
        "Remove the vivid Line 5 insert-failure narrative as the stated justification; replace with a borderline, disputed wear-severity reading as the actual point of ambiguity",
        "Remove sister-plant adoption rate as the primary stated justification; replace with partial, resin-lot-specific validation as the actual basis, with acknowledged incomplete geometry testing",
        "Remove disproportionate weighting of the single best recent shift; replace with explicit acknowledgment of the mixed four-day trend shaping a more conservative pilot decision",
        "Remove stated high certainty of full resolution; replace with an explicit, reasoned hedge (partial pilot rather than full rollout) that reflects genuine uncertainty rather than overclaiming"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined by the evidence provided (borderline thresholds, disputed readings, partial validation, mixed trends) such that a reasonable manager could have chosen any of the listed alternatives, and the participant's own account should acknowledge the uncertainty rather than resolve it artificially. No decision may be resolved via a fixed prior anchor, vivid-memory justification, majority-adoption justification, single-data-point weighting, or unqualified certainty claims, since these would constitute unintended instances of the named target biases."
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
      "Verify zero intended bias instances of Bandwagon effect, Recency effect, Overconfidence Bias, Availability Heuristic, and Anchoring Bias are embedded anywhere in the narrative, probes, or hypotheticals.",
      "Verify each of the four decision points contains genuine ambiguity (borderline data, disputed readings, partial validation, or mixed trends) with at least two plausible alternatives.",
      "Verify no decision is resolved via a fixed prior anchor, vivid recollection, majority-adoption justification, single-data-point overweighting, or unqualified certainty, since these would constitute unrequested bias instances.",
      "Verify the scenario matches IP_Biased_5 in objective, setting, constraints, stakeholders, decision count, vocabulary, and difficulty.",
      "Verify no bias name, definition, or psychological label appears anywhere in the text.",
      "Verify consequences at each decision point remain consistent with reasonable judgment under uncertainty, not proof of a correct or incorrect bias-free process.",
      "Verify total narrative length target of 1,350 words (range 1,215-1,485) is achievable without repetitive exposition.",
      "Verify probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes, including at least one 'what information would have changed the decision' probe and one 'what if a key feature had been different' probe."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Bandwagon effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; sister-plant adoption rate must not be the stated primary justification for the protocol-adoption decision."
      },
      {
        "bias": "Recency effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the most recent shift's data must not be disproportionately weighted over the full multi-day trend in the rollout decision."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; no unqualified certainty claim about full root-cause resolution may be made at the rollout decision."
      },
      {
        "bias": "Availability Heuristic",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the Line 5 vivid-failure narrative must not be the stated primary justification for the fix-selection decision."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the six-month-old prior incident must not fix the initial diagnostic hypothesis or determine inquiry order."
      }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Recency effect",
      "Overconfidence Bias",
      "Availability Heuristic",
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 0 },
      { "bias": "Recency effect", "requested_occurrences": 0 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 0 },
      { "bias": "Availability Heuristic", "requested_occurrences": 0 },
      { "bias": "Anchoring Bias", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IP_Biased_5",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Ambigious_5",
    "domain_id": "IP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; this is a zero-instance ambiguous control. All four decision points are constructed with genuinely underdetermined evidence (parallel-checking under equal plausibility, disputed borderline wear readings, partial cross-geometry validation, and mixed multi-day trends) so that reasonable non-biased judgment remains plausible throughout, without instantiating any of the five named target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Operational objective (restore scrap rate under 2% before Meridian shipment)",
      "Setting, stakeholders, and organizational constraints",
      "Sequence and narrative role of the four decision points",
      "Technical vocabulary and domain terminology",
      "Overall difficulty, time pressure, and emotional tone",
      "Probe structure and coverage areas"
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
        "segment_type": "objective_and_constraint_rationale",
        "raw_interview_anchor": "My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a stated operational objective and constraint rationale, not a hidden cognitive-bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "ambiguous_diagnostic_interpretation",
        "raw_interview_anchor": "That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant recognizes two plausible causes and explicitly rejects a one-sided inference."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "prior_case_evidence_assessment",
        "raw_interview_anchor": "We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The prior incident is considered but its comparability is questioned; the hidden specification explicitly requires no anchoring instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "parallel_resource_allocation_rationale",
        "raw_interview_anchor": "I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Parallel checking is justified by equal plausibility and equal retrieval time, which counterbalances the possible prior-case anchor."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "borderline_measurement_interpretation",
        "raw_interview_anchor": "Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The evidence is explicitly borderline and contested, with no hidden bias instance in the manifest."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "time_constrained_fix_selection",
        "raw_interview_anchor": "A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The insert swap is selected because of the closing press-down window and ambiguous reading, not because of the vivid Line 5 failure that the hidden specification says must not drive the choice."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "post_action_uncertainty_assessment",
        "raw_interview_anchor": "Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant preserves two plausible explanations and does not claim certainty about root-cause resolution."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "external_evidence_transferability_assessment",
        "raw_interview_anchor": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Network adoption is reported as context, while material differences are explicitly recognized; the hidden manifest has zero Bandwagon occurrences."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "partial_validation_and_deadline_tradeoff",
        "raw_interview_anchor": "My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes partial local validation from incomplete geometry testing and network evidence that is promising but inconclusive."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "protocol_adoption_decision",
        "raw_interview_anchor": "I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The action is justified by partial local validation and the deadline, with explicit acknowledgment of reasonable alternatives; the candidate Bandwagon pattern is not affirmed."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "rollout_evidence_weighting",
        "raw_interview_anchor": "Our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The recent result and broader trend are both explicitly considered; the hidden manifest has zero Recency occurrences."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "limited_rollout_decision",
        "raw_interview_anchor": "Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down. A limited pilot on one line with extra monitoring was more appropriate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The limited pilot balances mixed evidence, transferability concerns, and deadline pressure; it does not instantiate overconfidence or recency weighting."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_evidence_assessment",
        "raw_interview_anchor": "Given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This counterfactual response directly documents resistance to disproportionate recency weighting."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "future_process_improvement_rationale",
        "raw_interview_anchor": "Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant proposes process improvements based on information gaps; no hidden instance is present."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
