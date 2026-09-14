"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "The system's been solid for us on this fleet for as long as I've used it, so I issued the ALI to the ramp pretty much as generated.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "au_01"
        ],
        "ground_truth_rationale": "The participant accepted an automated instruction for atypical cargo without the available manual cross-check, relying on the system's general reliability."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I logged it and kept moving, because we still had the last-minute change to deal with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a continuation decision under time pressure, without a hidden bias instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I looked at the total weight and it was basically in line with the LMCs we'd been getting all week on this route... So I cleared it on that basis.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sub_01"
        ],
        "ground_truth_rationale": "The participant used aggregate weight similarity instead of evaluating the placement-specific index impact of the aft hold assignment."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "Two in a row felt like enough to say something was going on with how this rotation was trending that day, so I built in a forward shift.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ap_01"
        ],
        "ground_truth_rationale": "The participant inferred a recurring causal rotation pattern from two unrelated prior events and overrode the current flight's own computed index."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification leaves this operational tradeoff neutral and professionally defensible."
      }
    ]
  }
