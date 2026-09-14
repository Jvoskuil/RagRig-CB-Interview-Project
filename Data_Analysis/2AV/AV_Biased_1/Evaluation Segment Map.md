"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "role_and_threshold_reasoning",
        "raw_interview_anchor": "Monitoring repetitive write-ups and deciding when a case crosses from normal noise into formal corrective action.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive decision criterion without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_escalation_reasoning",
        "raw_interview_anchor": "The third write-up was unusual, but fleet-wide removal remained within MTBUR; the participant opened a focused review rather than declaring a fleet issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Evidence-weighted escalation decision without a hidden bias."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_integration",
        "raw_interview_anchor": "A second tail showed a similar complaint; difficult bench testing suggested an intermittent fault, and both tails shared a valve lot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Working-hypothesis update from new evidence without a hidden bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "interim_action_rationale",
        "raw_interview_anchor": "Repeated MEL carryover was a flag, but grounding was unsupported by the evidence; the participant imposed a one-leg MEL limit and opened an investigation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Balanced operational restriction without a hidden bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "root_cause_evidence_assessment",
        "raw_interview_anchor": "Vendor documentation and in-house teardown both pointed to the same seal-material cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Assessment of convergent existing evidence before the assay decision."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "evidence_selection_and_submission_timing",
        "raw_interview_anchor": "The participant already regarded lot-bounded replacement as settled, nevertheless commissioned a three-week external assay for thoroughness, and held the submission despite knowing the assay could not change the recommendation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["ib_01"],
        "ground_truth_rationale": "The sole hidden Information bias instance: non-decision-relevant additional data was sought for reassurance or perceived thoroughness, causing a deadline miss."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "final_corrective_action_rationale",
        "raw_interview_anchor": "The participant chose replacement limited to the identified vendor lot rather than a fleet-wide swap or deferral.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Scope selection followed lot-specific evidence."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_reasoning",
        "raw_interview_anchor": "In hindsight, the participant said the lot-based request should have been submitted on the original timeline without waiting for the assay.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective reconsideration of the already mapped occurrence, not a second occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_follow_up_reasoning",
        "raw_interview_anchor": "A different assay result would have triggered a follow-up investigation, not delayed the original submission.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual response without an additional bias instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "prospective_process_reasoning",
        "raw_interview_anchor": "For a future case, the participant would ask whether extra data could change the recommendation or merely improve the file.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Prospective process adjustment without a new manifested occurrence."
      }
    ]
  }
