"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial interpretation",
        "raw_interview_anchor": "The participant interprets the pressure trend as more likely an instrumentation quirk than a reaction problem because temperature remains in band.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A plausible initial technical interpretation is expressed, but no hidden bias manifestation is required in this span."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "group-influenced decision rationale",
        "raw_interview_anchor": "The participant describes entering the control-room discussion unsure, becoming more confident after others converged on the prior sensor-issue interpretation, and using that shared read to continue monitoring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gp_01"
        ],
        "ground_truth_rationale": "The group discussion amplifies confidence beyond the participant's initial uncertainty and supports continuing monitoring rather than independently interrupting or escalating."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "causal diagnosis",
        "raw_interview_anchor": "After the relief-valve lift, the participant quickly concludes that the event is the familiar sensor-drift pattern, acknowledges the new catalyst lot, but says he did not weight that difference heavily and did not wait for the fuller review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "dk_01"
        ],
        "ground_truth_rationale": "The participant treats surface similarity and prior familiarity as sufficient for a confident causal conclusion despite an unreviewed catalyst-lot variable and incomplete diagnostic picture."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "mitigation option selection",
        "raw_interview_anchor": "The participant recommends retaining the manual response procedure because operators know it, the interlock is unfamiliar, and the known system feels safer despite the contractor's documented margin reduction.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ra_01"
        ],
        "ground_truth_rationale": "The small unfamiliarity risk of the interlock is weighted more heavily than the documented safety-margin risk that the interlock would address."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "MOC evidence weighting and closure",
        "raw_interview_anchor": "In the MOC meeting, the participant sides with the senior in-house engineer, citing the original team, long unit experience, excellent safety record, and the contractor's status as an outside read, then closes the MOC without the kinetics review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ig_01",
          "he_01"
        ],
        "ground_truth_rationale": "This span contains both affiliation-based discounting of the outside contractor and transfer of the senior colleague's general safety reputation to a specific unverified technical claim."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective rationale",
        "raw_interview_anchor": "The participant identifies shift-changeover time pressure as influential in the root-cause call and MOC closure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Time pressure is contextual information and is not itself a hidden bias manifestation."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "counterfactual information-order assessment",
        "raw_interview_anchor": "The participant says receiving the contractor report before the control-room discussion might have slowed convergence and that order mattered.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective counterfactual and does not create an additional hidden instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "future corrective action",
        "raw_interview_anchor": "For a future deviation with a new catalyst lot, the participant would flag the lot change early and treat the case independently rather than pattern-match to prior events.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a corrective reflection on future practice, not a separate biased decision in the incident."
      }
    ]
  }
