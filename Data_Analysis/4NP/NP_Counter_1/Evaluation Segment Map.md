"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial monitoring decision rationale",
        "raw_interview_anchor": "There wasn't much to react to yet — within the band, no real trend history to speak of. Calling the engineer for every early wobble creates noise. Tightening the interval was the right first move; escalate if it keeps climbing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A within-band early wobble is logged and monitored more frequently; the participant gives a plausible escalation threshold and no hidden bias is embedded here."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "second-opinion decision rationale",
        "raw_interview_anchor": "Auto control handled it fine, so it wasn't urgent operationally. But two things trending at once during an ascension makes you want a second opinion, especially something with a control-system explanation I wanted verified rather than assumed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant seeks an engineer check because two items trend concurrently and the control-system explanation should be verified; this is ordinary cautious reasoning."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "continue-or-hold decision under competing workload",
        "raw_interview_anchor": "That's the one I've turned over the most. I had three things going — the pump, the pre-brief prep, and the ascension clock. The continue-and-monitor approach is what we've used for trends like this before, and it's worked, so that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could've done — the data was right there — but between the pre-brief materials and the schedule, it didn't feel necessary in that window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ir_cf_01"
        ],
        "ground_truth_rationale": "Under concurrent non-handoff workload and ascension pressure, the participant chooses a familiar satisfactory response and consciously defers accessible comparative data, which is the hidden Imperfect Rationality manifestation."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "pre-brief communication choice",
        "raw_interview_anchor": "I mentioned it in passing when the coordinator's question happened to touch on it — kept it brief since it wasn't the topic of that meeting and it was already framed as a monitor-and-continue item in my head.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant makes a communication-scope choice during an unrelated pre-brief; no additional hidden bias instance is specified."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "post-pre-brief resource-allocation rationale",
        "raw_interview_anchor": "Once the pre-brief wrapped, it was one of the first things on my list — nobody was waiting on me to hand it off, but it had been nagging at me a bit. The comparison showed the rate of climb didn't quite match the earlier benign cases.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "After the competing task ends, the participant independently retrieves the comparison; this follow-up contains no separate hidden instance."
      }
    ]
  }
