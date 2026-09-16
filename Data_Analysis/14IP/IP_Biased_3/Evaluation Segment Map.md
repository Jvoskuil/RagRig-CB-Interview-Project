"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "role_and_objective",
        "raw_interview_anchor": "I own air permit compliance for the whole site... figure out what actually happened, decide what needed to be reported to the state, and keep production moving if I could justify it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states role responsibilities and operational objectives without a manifested hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_hypothesis_and_evidence_interpretation",
        "raw_interview_anchor": "My first read was that it was probably drift again... once I had that in my head... I read them as consistent with drift rather than as a red flag on their own.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The early drift hypothesis is explicitly described as shaping interpretation of later ambiguous handheld readings, matching the Primacy Effect instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "operational_constraint_and_shutdown_tradeoff",
        "raw_interview_anchor": "The readings he brought back were elevated, but not dramatically... We were also mid-batch on a large customer order due in two days, so a shutdown wasn't something anyone wanted to trigger without good reason.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This expresses ambiguous evidence and legitimate production constraints, but does not by itself establish a hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "information_seeking_and_deferral",
        "raw_interview_anchor": "I decided to hold off on pulling the full continuous emissions monitoring data... If it had come back showing an exceedance, we'd have been on a 24-hour reporting clock... So I told myself the grey-zone readings weren't conclusive enough.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The participant acknowledges the more diagnostic step and links deferral partly to the unwelcome reporting consequence, matching the Ostrich effect instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "causal_narrative_and_inspection_prioritization",
        "raw_interview_anchor": "Gasket seep... is genuinely our most common issue... But the Ohio valve failure was just very present for me... the valve scenario is what I wrote down and what I asked maintenance to check first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "A vivid recent valve-failure narrative displaced the statistically common gasket explanation in the initial causal framing, matching Imaginability Bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "reporting_methodology_decision",
        "raw_interview_anchor": "Once the gasket was confirmed, I had two methodologies I could reasonably apply... picked the one I felt was most defensible given how our last few audits went.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification deliberately leaves decision point 4 as an undetermined judgment call without intended bias instrumentation."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "retrospective_uncertainty_and_decision_calibration",
        "raw_interview_anchor": "Early on, fairly confident it was drift—maybe too confident... If the field readings that first morning had been sharper... that would have changed how much weight I put on the drift explanation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective confidence calibration and a counterfactual about evidence sharpness; it does not introduce a separate hidden instance."
      }
    ]
  }
