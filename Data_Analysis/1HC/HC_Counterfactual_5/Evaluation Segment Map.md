"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "clinical_evidence_assessment",
        "raw_interview_anchor": "Week-eight assessment: 78% quadriceps index, threshold cited at 80-85%, no pain or swelling, and good movement.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Objective near-threshold data and asymptomatic status provide a plausible clinical basis for caution without independently manifesting a hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "progression_decision_rationale",
        "raw_interview_anchor": "The prior graft-failure case 'stuck with me'; the PT held progression, said the memory colored the current case, and said it would have tipped the decision even without deadline pressure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The unrelated vivid prior case was treated as the decisive risk input over the current patient's near-threshold, symptom-free data."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "test_scheduling_context",
        "raw_interview_anchor": "Three clean hopping sessions had occurred; the dynamometer was booked, available only two days weekly, and slots went quickly regardless of authorization.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This establishes legitimate resource and scheduling constraints but does not itself express the streak-based prediction used to delay testing."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "streak_based_prediction",
        "raw_interview_anchor": "The PT felt that three good sessions meant they were 'due for something to give,' delayed the test, acknowledged no clinical red flags, and said the delay was purely about the streak.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "A short run of successful sessions was treated as making a decline due despite no fatigue, swelling, PROM decline, or authorization urgency."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "ambiguous_option_evaluation",
        "raw_interview_anchor": "At week twelve, approximately 85% of interim milestones were met; the routine case-manager check-in asked about clinic visits versus a home program, and either path was supportable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an ambiguous decision boundary and neutral option assessment before the framing choice."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "recommendation_framing",
        "raw_interview_anchor": "The PT led with the risk of losing strength gains, gave little attention to home-program gains, said the loss language drove continued clinic care, and denied insurance pressure as the driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "Loss-framed presentation measurably tilted the clinic-versus-home recommendation despite ambiguous data and no deadline pressure."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "prognosis_and_clearance",
        "raw_interview_anchor": "With 88% hop symmetry and 91% quadriceps index, the PT said the patient was very likely to return injury-free, acknowledged the confidence exceeded the scores, and chose full clearance.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "The PT converted favorable individual scores and personal caseload comparison into an overly confident individual prognosis and unqualified clearance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "risk_communication",
        "raw_interview_anchor": "When asked about re-injury chances, the PT answered only with the patient's own numbers, omitted general athlete re-injury rates, and acknowledged having time to provide fuller context.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "Relevant population-level risk information was available but omitted in favor of individual data."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_causal_reflection",
        "raw_interview_anchor": "The PT said a hard visit cap might have increased stress about the dynamometer delay but would not have changed the core reasoning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual causal reflection rather than a new hidden bias manifestation."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "closing_reflection",
        "raw_interview_anchor": "The PT advised checking whether a call is driven by the patient or by something carried in from elsewhere.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "General reflective advice does not add a distinct decision-point manifestation."
      }
    ]
  }
