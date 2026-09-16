"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_dp1",
        "speaker": "Participant",
        "segment_type": "decision_point_1_initial_placement_hold",
        "raw_interview_anchor": "My first instinct was just to trust the transcript ... so I asked my chair if we could hold off a few days and get a diagnostic test done.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The teacher recognizes uncertainty in the transcript and deliberately gathers more evidence; the generation specification marks this as a reasonable, non-biased data-gathering decision."
      },
      {
        "segment_id": "seg_dp2",
        "speaker": "Participant",
        "segment_type": "decision_point_2_composite_placement_score",
        "raw_interview_anchor": "I converted everything to the same 100-point scale and averaged the four together. That gave me a composite right around 79, which cleared our department's cutoff of 75.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "avg_01"
        ],
        "ground_truth_rationale": "The teacher applies an unweighted arithmetic mean to heterogeneous inputs with materially different reliability and comparability, directly forming the placement decision."
      },
      {
        "segment_id": "seg_dp3",
        "speaker": "Participant",
        "segment_type": "decision_point_3_first_unit_test_monitoring",
        "raw_interview_anchor": "That was concerning, but not alarming yet ... I chose the second option and set up twice-weekly tutoring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The teacher acknowledges the low score, considers reassignment, and chooses support while monitoring under genuine uncertainty; this is explicitly non-biased in the generation specification."
      },
      {
        "segment_id": "seg_dp4",
        "speaker": "Participant",
        "segment_type": "decision_point_4_quarter_end_retention",
        "raw_interview_anchor": "The recent trend mattered a lot to me ... keeping him in with continued support seemed like the right call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retention is supported by the improving trend, tutoring response, transcript continuity, and parent input; the specification treats this as a defensible judgment rather than a named bias."
      }
    ]
  }
