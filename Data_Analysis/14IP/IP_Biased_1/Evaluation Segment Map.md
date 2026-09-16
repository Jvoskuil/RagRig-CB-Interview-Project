"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "dp_01_technician_assignment",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The planner considered the tighter packaging slot and selected Order A using an explicit production rule; the generation specification treats this as plausible domain reasoning, not an intentional bias instance."
      },
      {
        "segment_id": "dp_02_line3_alarm_overflow",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "br_01"
        ],
        "ground_truth_rationale": "This is the planned Bounded Rationality instance: under concurrent demands, the planner accepted the first workable assessment and did not check the readily available Order C dependency before committing Line 3."
      },
      {
        "segment_id": "dp_03_qa_buffer_plan",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The planner made a reversible provisional plan under uncertain QA timing and explicitly planned to adjust if QA flagged an issue; this is treated as reasonable operational planning."
      },
      {
        "segment_id": "dp_04_rework_shipment",
        "speaker": "Participant",
        "segment_type": "decision_episode",
        "raw_interview_anchor": "Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The planner explicitly weighed overtime, partial shipment, and renegotiation, then made a documented cost and customer-service trade-off; the generation specification does not mark this as biased."
      }
    ]
  }
