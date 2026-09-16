"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "goal_statement",
        "raw_interview_anchor": "Participant: Mainly to see whether adopting something pre-built could shortcut months of remediation work, given the timeline.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states a time-constrained evaluation goal without a manifested cognitive-bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_review_and_scope_basis",
        "raw_interview_anchor": "Participant: Rather than take that at face value, I asked for their contrast-ratio spec sheet... it only covered default, unthemed values... our actual implementation would always be themed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant seeks direct evidence and identifies the limits of the available spec before deciding scope."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "pilot_scoping_decision",
        "raw_interview_anchor": "Participant: I scoped the pilot narrowly — just the token categories tied directly to our compliance gap... since the spec sheet could not tell me how the tokens would hold up once themed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The narrow pilot is explicitly tied to an evidence gap and the compliance need."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_separation",
        "raw_interview_anchor": "Participant: The demo was impressive, but impressive motion design on one component does not tell you much about contrast behavior on a different set of tokens, so I kept those separate in my head.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly separates component-level motion evidence from token contrast evidence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "licensing_tier_decision",
        "raw_interview_anchor": "Participant: I mapped what the narrow pilot actually needed against each tier’s component list... Team actually covered our confirmed needs... I recommended Team.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The tier choice is based on confirmed component requirements and comparison against each tier."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "rollout_timeline_decision",
        "raw_interview_anchor": "Participant: I asked both squad leads directly what their earliest realistic integration window was... One could start in three weeks, the other in five. I set the rollout date to the later window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The date is set from both squads’ stated feasible windows rather than an unsupported internal assumption."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "recommendation_reflection",
        "raw_interview_anchor": "Participant: Checking actual needs against the tier list and getting real calendar commitments from both squads is basically what I would do again.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant restates an evidence-based decision process; no bias instance is intended or manifested."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "audit_status_and_disclosure",
        "raw_interview_anchor": "Participant: I had told the VP and both squad leads earlier that the defaults tested well... but I had also flagged at the time that full-scale testing was still pending.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports both the preliminary result and its pending-testing caveat."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "diagnostic_retest_decision",
        "raw_interview_anchor": "Participant: I wanted to know whether the failure was in our theming layer or in the vendor’s own default tokens, so I requested an independent retest... I did not want to guess at the cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The retest is a diagnostic step to distinguish competing causal explanations."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "selective_reversion_decision",
        "raw_interview_anchor": "Participant: Once the retest pointed at the vendor defaults specifically, I reverted just the three affected components... and left the rest... in place, since those had tested clean.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant takes a selective action keyed to retest evidence and component-level test results."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "final_option_comparison_and_recommendation",
        "raw_interview_anchor": "Participant: The hybrid matched what the evidence actually showed — keep what tested clean, source internally what did not... I documented the retest findings, expected migration effort, and compliance risk for each option.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The final recommendation compares alternatives using test evidence, migration effort, and compliance risk."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "retrospective_improvement",
        "raw_interview_anchor": "Participant: I would keep asking for direct evidence... The one thing I would tighten up is flagging the pending full-scale testing caveat more visibly in written updates.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies a communication improvement while retaining evidence-seeking practices."
      }
    ]
  }
