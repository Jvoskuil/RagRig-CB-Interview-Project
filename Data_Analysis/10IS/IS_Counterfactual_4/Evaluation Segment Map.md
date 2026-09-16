"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "vendor_selection_reasoning",
        "raw_interview_anchor": "Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it. ... that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant lets the near-priced inferior full-service option frame Vendor C and does not independently assess whether Vendor A meets the three-flow scope, despite ample time."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "contractor_selection_reasoning",
        "raw_interview_anchor": "Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. ... I extended trust from the visual work to the rest of it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant generalizes prestige and visual polish to unverified documentation and communication abilities, despite the other candidate's directly relevant process evidence and available trial task."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "rules_engine_causal_interpretation",
        "raw_interview_anchor": "Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it. ... we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant attributes an underpowered, confounded uptick to their own manual rule changes and acts on that attribution despite the Analytics Lead's warning and schedule slack."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_test_uncertainty_update",
        "raw_interview_anchor": "Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This later uncertainty update acknowledges reversal and unresolved causality; it contains no hidden manifested bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "legacy_component_continuation_reasoning",
        "raw_interview_anchor": "Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare. ... Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Past effort is used to justify continuation even though the forward-looking one-sprint migration estimate is better and remaining runway is sufficient."
      }
    ]
  }
