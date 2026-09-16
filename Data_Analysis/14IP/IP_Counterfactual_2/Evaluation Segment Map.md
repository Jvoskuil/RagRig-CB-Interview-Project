"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "signal_observation_and_interpretation",
        "raw_interview_anchor": "Participant: I'm the QA analyst covering statistical process control ... Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant interprets the chart pattern and distinguishes a mean shift from increased within-subgroup variability, but no hidden bias instance is manifested."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "signal_assessment",
        "raw_interview_anchor": "Participant: Honestly, at 62% through the shift's quota ... I didn't have an obvious explanation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant gives a reasonable Western Electric assessment of a warning-zone point and trend without committing to an unsupported cause."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "sampling_and_measurement_validation",
        "raw_interview_anchor": "Participant: I tightened up sampling instead of pulling the trigger on a full stop ... I knew it was real.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant uses increased sampling and a manual spot check as proportionate process-control actions; neither is a hidden bias occurrence."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "first_decision_action_rationale",
        "raw_interview_anchor": "Participant: I could have shut it down right there ... Increasing sampling was the middle path — get more data fast without committing to downtime.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The alternatives and the moderate sampling choice are the intended non-bias response at decision point 1."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "root_cause_information_gathering",
        "raw_interview_anchor": "Participant: I pulled up everything I had access to in real time ... this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This segment records the available temperature, lot, tool-wear, and engineer information; the hidden correlation occurrence is localized to the subsequent choice to favor temperature and defer the lot test."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "causal_attribution_and_evidence_selection",
        "raw_interview_anchor": "Participant: The timing just lined up so cleanly on its own ... I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["corrbias_01"],
        "ground_truth_rationale": "The participant treats temporal co-occurrence as sufficient support for the temperature explanation and does not test the comparably available material-lot hypothesis with equivalent rigor, despite lacking engineer precedent."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "tool_wear_update_and_intervention_choice",
        "raw_interview_anchor": "Participant: The tool wear sensor data finally came through ... Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["consbias_01"],
        "ground_truth_rationale": "The participant acknowledges strong 78% tool-wear evidence but remains influenced by the recently-serviced-tool assumption and chooses only a small offset rather than a tool change."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "post_adjustment_assessment",
        "raw_interview_anchor": "Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding ... a cue I obviously didn't have access to until after the handoff.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a consequence and information-availability update after the offset decision, not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "final_corrective_action_rationale",
        "raw_interview_anchor": "Participant: By the end, several parts were near or slightly under the lower spec limit ... a deviation report was required regardless of what I concluded about the cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The final recommendation is the intended accurate tool-change and deviation-report response at decision point 4."
      }
    ]
  }
