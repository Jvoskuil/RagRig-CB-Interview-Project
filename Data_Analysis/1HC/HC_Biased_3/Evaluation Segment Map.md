"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_diagnostic_interpretation",
        "raw_interview_anchor": "Reproducible tenderness was described as classic for costochondritis, and the furniture-moving history was said to fit.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a plausible initial clinical interpretation without the required hidden-bias manifestation by itself."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "diagnostic_evidence_weighting_and_closure",
        "raw_interview_anchor": "The chest wall tenderness was the dominant finding; the flight and calf symptom felt like background noise; the participant did not chase it further and considered the case basically settled.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pc_01"
        ],
        "ground_truth_rationale": "The participant settles on a musculoskeletal explanation after a salient finding, dismisses unresolved PE-risk cues, and stops further differential consideration."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "alternative_management_analysis",
        "raw_interview_anchor": "The participant described either redoing risk stratification with Wells/PERC or obtaining CTPA immediately.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly articulates competing options and their relevant diagnostic implications; the bias manifestation occurs in the subsequent choice rationale."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "immediate_action_choice_and_resource_allocation",
        "raw_interview_anchor": "The participant sent the patient straight for CTPA, citing the queue, boarding pressure, handoff deadline, and the desire to get a real answer and make the decisive move.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ab_01"
        ],
        "ground_truth_rationale": "The participant favors immediate imaging over rescoring or observation and frames the decision around decisiveness and resolving ambiguity under pressure."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "test_consequence_assessment",
        "raw_interview_anchor": "The negative CTPA was reassuring, but the incidental nodule and mild contrast reaction required follow-up and monitoring and consumed additional time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an assessment of consequences after the decision, not an intended hidden bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_third_party_decision_evaluation",
        "raw_interview_anchor": "Dr. B's decision was initially called clearly right because nothing bad happened; the participant later acknowledged reacting to the good outcome rather than what Dr. B knew going in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "The initial evaluation of Dr. B's decision is based primarily on the favorable outcome before process information is known, with later reflection confirming that mechanism."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "final_disposition_reasoning",
        "raw_interview_anchor": "The participant went back and forth about admission versus discharge, then discharged because the patient was stable, PE was excluded, outpatient follow-up was arranged, and admission would not change overnight management.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The disposition decision is explicitly uncertain, clinically reasoned, and intentionally neutral in the hidden specification."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_uncertainty_reflection",
        "raw_interview_anchor": "The participant identified the D-dimer moment as the point where they moved fastest and might have paused longer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective reflection on uncertainty and pacing, not a separate hidden instance."
      }
    ]
  }
