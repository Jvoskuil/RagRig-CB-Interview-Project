"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_communication_goal",
        "raw_interview_anchor": "Overview of the Riverside fire, PIO responsibilities, and objective to protect people without causing panic or issuing statements that would need to be withdrawn.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive communication objective, but no intentionally embedded bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_warning_choice",
        "raw_interview_anchor": "With wind toward the neighborhood, odor reports, and no confirmed hazard identity, the participant recommends a precautionary shelter-in-place advisory rather than waiting for the manifest.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an uncertainty-sensitive precautionary decision; the generation specification assigns no bias instance to decision point 1."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "post_update_reassessment",
        "raw_interview_anchor": "After the manifest and wind update ease the risk picture, the participant still judges the initial advisory correct given the information available at the time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A hindsight-aware reassessment of the initial precaution; no hidden bias is planned here."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "operational_constraint_and_misinformation_response",
        "raw_interview_anchor": "The participant describes incomplete air monitoring, competing stakeholder demands, and spending response capacity correcting inaccurate chemical-explosion speculation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive prioritization and coordination context without an embedded target bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "channel_selection_rationale",
        "raw_interview_anchor": "The participant compares reverse-911's block-level geotargeting with CAN's five years of drill and incident use, then selects CAN because it is familiar, trusted, and known to work despite its countywide reach.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["meb_01"],
        "ground_truth_rationale": "Decision point 2 contains the single Mere Exposure instance: repeated familiarity with CAN drives selection over a more targeted unfamiliar option."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "severity_assessment_and_escalation",
        "raw_interview_anchor": "While advisory-range sensor readings remain open, the participant says the viral black-smoke photograph looks bad, drafts evacuation language, and keeps returning to the image until the health officer pushes back.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["pse_01"],
        "ground_truth_rationale": "Decision point 3 contains the single Picture Superiority instance: the vivid image disproportionately shapes severity judgment relative to contemporaneous sensor data."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "hindsight_evidence_reconciliation",
        "raw_interview_anchor": "Follow-up readings remain stable and the participant explains that the black smoke came from packaging material, so the visual appearance was not supported by the air data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is later counterevidence and retrospective reconciliation, not a new hidden occurrence."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "all_clear_action",
        "raw_interview_anchor": "With suppression nearly complete, parents at the reunification point, residual odor reports, and health-officer guidance, the participant chooses a phased message over an immediate full all-clear.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is intentionally non-biased and follows the health officer's staged recommendation."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "cautious_message_justification",
        "raw_interview_anchor": "The participant defends the staged message as more defensible than a blanket all-clear because odor reports remained, despite residents finding it confusing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A cautious, evidence-linked communication rationale with no hidden target instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "channel_counterfactual",
        "raw_interview_anchor": "The participant says prior successful live use of reverse-911 would probably have increased trust enough to change the channel choice.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a closing counterfactual about the existing channel decision, not a separate manifested occurrence."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "escalation_counterfactual",
        "raw_interview_anchor": "The participant predicts the escalation discussion would have been calmer and would likely have stayed at shelter-in-place without the photo.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This counterfactual supports the already mapped photo episode but does not create a second Picture Superiority occurrence."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "retrospective_lesson",
        "raw_interview_anchor": "The participant recommends stating the data source before reacting to visually striking information and verifying reverse-911 before defaulting to CAN, while judging the original calls reasonable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective corrective lessons refer back to the two existing episodes and are not additional hidden occurrences."
      }
    ]
  }
