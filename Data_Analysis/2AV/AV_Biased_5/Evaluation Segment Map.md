"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "maintenance_decision_reasoning",
        "raw_interview_anchor": "No fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A procedural/MEL-based dispatch rationale without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "risk_trend_interpretation",
        "raw_interview_anchor": "This was probably a nuisance signal that would settle down on its own... I didn't see it as a trend that was going anywhere serious.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "The participant projects a benign trajectory despite increasing caution duration and chooses monitoring over deeper isolation."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "case_pattern_matching",
        "raw_interview_anchor": "It felt like we already had the answer... it just felt like the same animal.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rh_01"
        ],
        "ground_truth_rationale": "The prior in-house case is treated as matching without checking flight hours or component-batch differences."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "expert_evidence_weighting",
        "raw_interview_anchor": "The OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ab_01"
        ],
        "ground_truth_rationale": "The informal OEM representative's status and experience are weighted over the senior engineer's formal procedural recommendation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "repair_scope_decision",
        "raw_interview_anchor": "We'd sunk real hours into the path we were on... the seal fix looked like it would close it out without starting over.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "scf_01"
        ],
        "ground_truth_rationale": "Prior labor and component investment materially support continuing the incremental plan despite new leak evidence."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "confidence_calibration",
        "raw_interview_anchor": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition... but I didn't see a reason to hold the airplane.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ocb_01"
        ],
        "ground_truth_rationale": "The participant expresses strong certainty while acknowledging that ground testing did not reproduce the relevant in-flight condition."
      }
    ]
  }
