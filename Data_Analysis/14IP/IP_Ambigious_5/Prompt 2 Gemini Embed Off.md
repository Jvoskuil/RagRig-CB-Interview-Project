You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Conservative, mechanism-first evaluation of the participant's production-problem reasoning. No RAG retrieval context was supplied, so no occurrence was classified using retrieved corpus support."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Action bias",
        "alternative_labels": ["Action bias", "urgency effect"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision point two: borderline wear reading under closing press-down window",
        "supporting_interview_quote": "So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.",
        "plausible_mechanism": "A closing operational window and uncertainty may have created a preference for immediate, higher-intensity intervention despite ambiguous diagnostic evidence.",
        "why_not_identified": "The transcript gives explicit scheduling and risk-management reasons for the insert swap, without affirmatively showing a distinct cognitive distortion beyond time-constrained decision-making."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Social proof",
        "alternative_labels": ["Bandwagon effect", "Social proof"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision point three: adopting sister-plant cooling-time reduction protocol",
        "supporting_interview_quote": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.",
        "plausible_mechanism": "Adoption by similar plants could have exerted social influence on the participant's decision to adopt the protocol despite incomplete transferability evidence.",
        "why_not_identified": "The participant explicitly acknowledged the transferability problem, relied on partial local validation and corporate quality input, and weighed the trade-offs; the transcript does not demonstrate that social proof actually distorted the final reasoning operation."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "Recency bias",
        "alternative_labels": ["Recency effect"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision point four: rollout decision for Lines 4 and 6",
        "supporting_interview_quote": "By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability.",
        "plausible_mechanism": "The recent single-shift improvement could have been overweighted relative to the broader mixed trend when deciding whether to expand the fix.",
        "why_not_identified": "The participant stated explicitly that the last shift was treated as one data point rather than the whole answer, and approved only a limited pilot rather than a full rollout; the reasoning does not affirmatively demonstrate recency-based distortion."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No scientific retrieval context was supplied, so corpus support could not be used to validate candidate mechanisms.",
      "Analysis is limited to the single interview transcript and cannot directly observe internal cognitive processes.",
      "The participant's self-reported reasoning may omit or reconstruct details, though the analysis relies on what was disclosed.",
      "Time pressure and operational constraints are present throughout, but were not treated as biases without distinct distortion mechanisms."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Ambigious_5_Gemini_off",
  "interview_id": "IP_Ambigious_5",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
