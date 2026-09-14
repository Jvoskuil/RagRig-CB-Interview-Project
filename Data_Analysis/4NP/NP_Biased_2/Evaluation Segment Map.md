"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_hypothesis_weighting",
        "raw_interview_anchor": "I-131 peak interpreted through the prior fuel-defect event while the recent recalibration explanation was acknowledged but parked.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sb_01"
        ],
        "ground_truth_rationale": "The participant explicitly overweighted a personally experienced prior fuel-defect event relative to the objectively relevant recent recalibration."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "confirmatory_evidence_interpretation",
        "raw_interview_anchor": "The repeat count was treated as a real signal rather than noise, with plant-transient explanations deprioritized.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is evidence interpretation and exclusion of a plant-transient explanation, without a hidden manifested bias instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "pattern_based_causal_attribution",
        "raw_interview_anchor": "The current spectrum was treated as a resin-intrusion-type issue because it resembled an older case before pathway confirmation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sim_01"
        ],
        "ground_truth_rationale": "The participant favored a causal attribution from superficial spectral resemblance despite distinct sample points and absent pathway confirmation."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "counterevidence_interpretation",
        "raw_interview_anchor": "The mismatched demineralizer ratio and absence of valve work orders were recognized as complications.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant incorporated counterevidence; this segment contains no hidden target instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "escalation_framing",
        "raw_interview_anchor": "The supervisor was given a preliminary early-fuel-defect framing while reporting urgency shaped the escalation timing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest contains no anchoring instance at the escalation point."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "final_reporting_decision",
        "raw_interview_anchor": "The final report used ranked causes and increased sampling because the evidence was not definitive.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant updated toward uncertainty and a ranked report; no hidden target instance is located here."
      }
    ]
  }
