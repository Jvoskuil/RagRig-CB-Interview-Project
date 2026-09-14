"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "pre_departure_dispatch_reasoning",
        "raw_interview_anchor": "Two prior flights, same fault, both cleared themselves... My read was, this is a known quantity... So there wasn't a strong pull toward digging further.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant treats repeated self-clearing fault history and MEL disposition as evidence that further inspection is unnecessary for dispatch."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "in_flight_predictive_reasoning",
        "raw_interview_anchor": "My first thought honestly was, there it is again, exactly like the tech log said... keep the climb going... at the time it felt like a clear pattern rather than a limited sample.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The participant predicts benign future fault behavior with high confidence from a brief, small-sample pattern."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "performance_evaluation_reasoning",
        "raw_interview_anchor": "I weighted his extensive time on type... more heavily than a step-by-step review of the QRH sequence... With him, the track record does a lot of the work.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The participant grades the captain more favorably because of seniority and track record instead of independently verifying procedural compliance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_flight_self_assessment",
        "raw_interview_anchor": "I told him I didn't think that applied to me... that kind of thing is more of a risk for someone earlier in their check-airman career... For me, I trust the process I've built.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "The participant dismisses a peer's critique of his own judgment while attributing similar susceptibility to less experienced evaluators."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "retrospective_outcome_reasoning",
        "raw_interview_anchor": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything... none of this proves anything one way or the other about the calls I made.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive retrospective reflection, but outcome bias is not part of the exhaustive hidden manifest."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "closing_counterfactual_reasoning",
        "raw_interview_anchor": "Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains what he would change under the same information; no additional hidden instance is manifested."
      }
    ]
  }
