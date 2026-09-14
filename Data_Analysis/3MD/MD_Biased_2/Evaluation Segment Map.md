"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "investigative_action",
        "raw_interview_anchor": "Pulling the fuel reconciliation report, cross-referencing the duty roster, and consulting the motor pool NCOIC to narrow the pool",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes an ordinary initial evidence-gathering sequence without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "cue_interpretation",
        "raw_interview_anchor": "The NCOIC's description of Doyle's motorcycle, tattoos, and rougher crowd is called color commentary",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports the salient cue but has not yet expressed the hidden distortion."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "suspect_prioritization",
        "raw_interview_anchor": "Selecting PFC Doyle first because of the NCOIC's remark, gut feeling, and who seemed like the type before completing the matrix",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ic_01"
        ],
        "ground_truth_rationale": "This is decision point 1: an irrelevant salient off-duty trait is linked to theft likelihood and drives early suspect prioritization."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "Acknowledging that a full overlap matrix would be cleaner but choosing to start somewhere because time was tight",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This supplies a plausible time-pressure explanation but is not itself an additional hidden occurrence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_update",
        "raw_interview_anchor": "After the matrix, recognizing that Doyle matched only two dates while two unremarkable soldiers matched more",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant updates on later shift-overlap data; the hidden manifest contains no additional instance here."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "evidence_review",
        "raw_interview_anchor": "Reviewing irregular key-control sign-outs, inconsistent odometer mileage, and the absence of fingerprints",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a factual evidence review without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "anomaly_handling",
        "raw_interview_anchor": "Logging the odometer issue as unresolved, considering both theft and administrative explanations, and requesting maintenance records",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly preserves an alternative explanation and defers interpretation pending corroboration."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "evidence_revision",
        "raw_interview_anchor": "Accepting that documented maintenance testing explained the extra mileage and noting the benefit of not building it into the narrative",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a later correction and cautious evidence handling, not a hidden target instance."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "disconfirming_evidence_evaluation",
        "raw_interview_anchor": "Skepticism toward the dispatcher's sworn alibi, attributing it to convenient timing or coworker cover, seeking extra corroboration, and keeping the existing focus",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "nrb_01"
        ],
        "ground_truth_rationale": "This is decision point 3: a credible disconfirming witness statement is discounted because it conflicts with the developing case narrative."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "retrospective_correction",
        "raw_interview_anchor": "Learning that phone records confirmed the call and acknowledging that the alibi was not handled as carefully as it should have been",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant recognizes the later corroboration and error retrospectively; this does not add a second hidden occurrence."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "case_closure",
        "raw_interview_anchor": "Choosing referral on the original track before the inspection deadline while flagging the fourth soldier's unresolved fuel-card anomaly for follow-up",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a deadline-driven closure choice; the hidden manifest contains no bias at decision point 4."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "counterfactual_reflection",
        "raw_interview_anchor": "Saying an earlier alibi would have prompted a return to the full personnel matrix",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an adopted counterfactual reflection, not a new hidden occurrence."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_reflection",
        "raw_interview_anchor": "Saying that without the command deadline the fourth soldier's anomaly would have been pursued, and revisiting the initial Doyle and alibi decisions",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This closing reflection is not credited as a separate occurrence because the hidden manifest is exhaustive and the instances are already localized."
      }
    ]
  }
