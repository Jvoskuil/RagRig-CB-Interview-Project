"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_clinical_interpretation",
        "raw_interview_anchor": "Clinically, it's a fairly textbook SIRS picture without a clear source yet... a handful of things.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive differential-diagnosis and severity interpretation without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "imaging_decision_and_rationale",
        "raw_interview_anchor": "It reminded me a lot of a patient I had maybe three weeks earlier... I ordered a CT of the torso pretty much right away... it felt like the responsible thing given what I'd just been through.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ah_01"
        ],
        "ground_truth_rationale": "A vivid recent adverse case emotionally elevated perceived soft-tissue risk and drove urgent imaging despite absent focal findings."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "workup_alternatives",
        "raw_interview_anchor": "I could've done a more stepwise workup... Both were reasonable. I just didn't feel comfortable waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicit comparison of reasonable workup alternatives without an additional hidden instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "antibiotic_bundle_selection",
        "raw_interview_anchor": "Seeing it sitting there next to the standard bundle made the standard one look like the obviously sensible choice... So that's what I went with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "de_01"
        ],
        "ground_truth_rationale": "The dominated extended option made the standard bundle appear preferable by comparison rather than through independent severity-based derivation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "monitoring_order_confirmation",
        "raw_interview_anchor": "I signed off on them as they were configured... I didn't sit down and re-derive whether five days was still appropriate. It's just what comes up when you open the pathway.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "db_01"
        ],
        "ground_truth_rationale": "Preconfigured telemetry and catheter defaults were accepted without active reassessment despite clinical improvement and nursing input."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "rounds_diagnostic_updating",
        "raw_interview_anchor": "That was the first thing said about the case, and honestly that framing kind of stuck for the group... the conversation kept circling back to the urosepsis framing for a while.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pb_01"
        ],
        "ground_truth_rationale": "The first diagnostic framing continued to dominate discussion despite negative urine culture and blood-culture evidence favoring another source."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "time_pressure_context",
        "raw_interview_anchor": "Constant, honestly. ED wanted the bed, rounds have a hard start time, and you're juggling four or five other patients too.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive contextual explanation of time pressure, without a hidden bias instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_learning",
        "raw_interview_anchor": "I'd force myself to write down the actual severity-based reasoning... build in a habit of re-checking defaults once the patient's status changes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective improvement plan and uncertainty statement, not a new intended occurrence."
      }
    ]
  }
