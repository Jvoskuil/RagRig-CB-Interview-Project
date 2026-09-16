"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "signal_detection",
        "raw_interview_anchor": "Participant describes three subgroup means creeping downward, the latest point in the warning zone, and a stable range chart.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is factual signal interpretation and process monitoring, without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_interpretation",
        "raw_interview_anchor": "Participant weighs quota progress and Western Electric rules, distinguishing one warning-zone point from a meaningful three-point pattern.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The reasoning is a documented, plausible SPC interpretation and is not a hidden instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "sampling_and_measurement_check",
        "raw_interview_anchor": "Participant increases sampling, waits for confirmation, then uses a hand micrometer to rule out a gauge artifact.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a reasonable moderate response and measurement-validation action."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "alternative_weighing",
        "raw_interview_anchor": "Participant compares stopping, ignoring the signal, and increasing sampling, choosing a middle path to obtain more data without downtime.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The choice is explicitly justified as an operational trade-off and is not a planted bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "cause_investigation",
        "raw_interview_anchor": "Participant reviews temperature, material-lot, and unavailable tool-wear information and consults the process engineer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This segment establishes the evidence available before the causal-attribution decision."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "causal_attribution_and_hypothesis_testing",
        "raw_interview_anchor": "Participant favors temperature because its timing lined up with the dimensional drift, cites the engineer's prior experience, and does not prioritize a hardness test of the new lot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["corrbias_01"],
        "ground_truth_rationale": "The participant infers causality from temporal co-movement and leaves a comparably available material-lot hypothesis untested with equivalent rigor."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "new_evidence_interpretation",
        "raw_interview_anchor": "Participant receives the 78% tool-life reading and recognizes the undersize drift as a classic tool-wear signature.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This establishes strong new evidence but does not alone contain the insufficient belief revision that defines the hidden instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "belief_updating_and_corrective_action",
        "raw_interview_anchor": "Participant acknowledges the tool-wear reading but says the recently serviced mental model is hard to shake, then chooses a small offset instead of a tool change under time pressure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["consbias_01"],
        "ground_truth_rationale": "Strong quantitative evidence and a matching wear signature produce only a marginal update toward corrective action because the earlier recent-tool belief remains influential."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "post_adjustment_monitoring",
        "raw_interview_anchor": "Participant reports that the next sample still approached the lower specification limit and that the incoming operator later noticed a different tool sound.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is subsequent evidence and a handoff cue, not an additional hidden bias instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "final_escalation_and_reporting",
        "raw_interview_anchor": "Participant uses near-limit parts, 91% tool life, and the Cpk drop to recommend a tool change, center-line update, and deviation report.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification treats this as an accurate final corrective action, not a second conservatism instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "outcome_and_causal_closure",
        "raw_interview_anchor": "Participant reports that the tool change restored baseline dimensions and that the new lot was later confirmed within hardness specification.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective outcome information and causal closure, explicitly not a new occurrence."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "retrospective_process_improvement",
        "raw_interview_anchor": "Participant says the lot sample could have been pulled earlier to close off an unexamined hypothesis.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is hindsight process improvement, not an additional bias manifestation."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "retrospective_time_pressure_explanation",
        "raw_interview_anchor": "Participant explains that approaching changeover made a full stop less appealing and contributed to choosing the smaller offset first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a plausible operational explanation of the already-mapped tool decision, not a separate hidden occurrence."
      }
    ]
  }
