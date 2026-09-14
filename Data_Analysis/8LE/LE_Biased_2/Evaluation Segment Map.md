"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "intake_information_handling",
        "raw_interview_anchor": "Detective supplies confession and prior-conviction information; examiner logs it and notes that the lab normally receives such context without blind review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is substantive intake information handling, but the hidden contextual-bias instance is localized to the later ambiguous-detail interpretation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "intake_choice_under_deadline",
        "raw_interview_anchor": "Examiner considers a fresh look or supervisor flag, then proceeds because reassignment would delay the case and the confession does not change the print.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The intake choice is explained by turnaround constraints and the examiner's view of print evidence; no hidden instance is assigned here."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "latent_quality_and_sufficiency_assessment",
        "raw_interview_anchor": "Examiner assesses a partial, smudged latent with peripheral distortion and ten clear minutiae.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive technical assessment of print quality and sufficiency without the hidden context-to-ambiguous-detail shift."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "ambiguous_detail_interpretation",
        "raw_interview_anchor": "Examiner compares the distorted peripheral region, says the confession made it feel like confirmation, and resolves it as consistent for individualization.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ctx_01"
        ],
        "ground_truth_rationale": "The phase-2 comparison response contains the hidden contextual-bias mechanism: case context enters interpretation of genuinely ambiguous ridge detail."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "verification_routing_choice",
        "raw_interview_anchor": "Examiner sends the full worksheet and conclusion, acknowledging blind verification as cleaner but choosing the standard route under staffing and deadline pressure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The routing decision is a negative segment; standard practice, staffing, and deadline explain the non-blind packet."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "discrepancy_reconciliation_and_belief_update",
        "raw_interview_anchor": "After the verifier flags the peripheral region, examiner searches for a distortion explanation, considers inconclusive and non-match alternatives, discounts the non-match, and keeps individualization.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "coh_01"
        ],
        "ground_truth_rationale": "The phase-4 reconciliation response contains the hidden coherence-based reasoning/rationalisation mechanism: post-hoc distortion explanation preserves the standing conclusion after disconfirming feedback."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "confidence_assessment",
        "raw_interview_anchor": "Examiner rates the peripheral read six or seven out of ten alone but feels solid overall because of the ten clear minutiae.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an explicit uncertainty and evidence-weighting reflection; it is not a separate hidden bias instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "prior_experience_heuristic",
        "raw_interview_anchor": "Examiner says textured tool surfaces are a known headache and that strong core detail usually keeps a rough edge from derailing the call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The professional heuristic is a negative segment because the hidden contextual instance specifically concerns confession/prior-record context, not prior tool-surface experience."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_context_reflection",
        "raw_interview_anchor": "Examiner says the read might have differed without the confession or priors and cannot rule out extra confidence doing work.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective counterfactual reflection, not an additional manifested instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual_verification_reflection",
        "raw_interview_anchor": "Examiner says an earlier verifier discrepancy might have led to an indeterminate treatment from the start.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective process reasoning about sequencing and is not an additional hidden instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "process_improvement_counterfactual",
        "raw_interview_anchor": "With no deadline, examiner would request a fresh lift or enhanced imaging and a blind second look.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive improvement recommendation, but it is not a new bias occurrence."
      }
    ]
  }
