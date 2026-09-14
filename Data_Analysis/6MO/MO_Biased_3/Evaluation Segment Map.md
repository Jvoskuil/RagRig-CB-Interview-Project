"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "goal_setting",
        "raw_interview_anchor": "My main objective was just making sure the tanker had a clean run through the bend within its tidal window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive operational goal and constraint, but no manifested cognitive-bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Mainly the AIS tag... I did notice the COG data wasn't fully consistent with active maneuvering, but I chalked that up to the clutter.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant formed a routine-fishing hypothesis from AIS and discounted conflicting COG/SOG evidence without verification."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "team_decision_reasoning",
        "raw_interview_anchor": "He said it with a lot of confidence... My colleague said something like 'that track looks a little odd' but didn't really elaborate... We closed out the handover log with a 'no action required' note.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The team adopted the supervisor's assessment without pursuing the colleague's dissent or requesting independent verification."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "That's when my supervisor turned it into a scheduling question... I went with proceeding as scheduled, given the tide constraint.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fb_01"
        ],
        "ground_truth_rationale": "The operator evaluated the unresolved safety issue primarily through the schedule and tidal-window frame."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "post_event_judgment",
        "raw_interview_anchor": "At that point the immediate encounter was already resolved... I decided the advisory was worth it given the upcoming traffic.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a neutral residual-risk judgment with explicit consideration of upcoming traffic and no intended hidden bias instance."
      }
    ]
  }
