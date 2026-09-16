"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial threat assessment and escalation decision",
        "raw_interview_anchor": "Initial flash flood watch discussion: the participant cites fifteen years of benign gauge history, downweights the duty forecaster's atypicality call, and keeps the EOC at routine monitoring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["nb_01"],
        "ground_truth_rationale": "The participant discounts an explicit atypicality signal in favor of historical benign outcomes at the initial threat-assessment decision."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evacuation duration estimation and plan selection",
        "raw_interview_anchor": "Evacuation discussion: the participant bases the timeline on the fastest prior evacuation and later acknowledges insufficient adjustment for nighttime conditions, skeleton staffing, and residents without vehicles.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["pf_01"],
        "ground_truth_rationale": "The participant uses a best-case precedent for duration estimation while failing to incorporate known aggravating conditions."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "shelter routing decision",
        "raw_interview_anchor": "Shelter and mutual-aid discussion: the participant routes most evacuees to shelter A based on initial capacity numbers despite live overflow warnings.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 3 is a neutral/control point in the hidden manifest; the occurrence manifest is exhaustive."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "mutual aid timing decision",
        "raw_interview_anchor": "Shelter and mutual-aid discussion: the participant delays the mutual-aid request until capacity is confirmed despite the reported risk that the access road may close within the hour.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive resource-timing rationale but no hidden bias instance is assigned to decision point 3."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "after-action attribution of colleague judgment",
        "raw_interview_anchor": "After-action review discussion: the participant characterizes the Sheriff's watch commander's reliance on the historical pattern as a judgment failure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The colleague critique alone is not the hidden Bias Blind Spot occurrence; the occurrence requires the subsequent self/other asymmetry."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective self-comparison and causal attribution",
        "raw_interview_anchor": "After-action self-comparison: the participant acknowledges a similar timing gap and best-case estimate in their own decisions but still describes their own decisions as sound and declines to place them in the same category as the colleague.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["bbs_01"],
        "ground_truth_rationale": "The participant applies a critical standard to the colleague while resisting the same interpretation for analogous decisions in their own decision log."
      }
    ]
  }
