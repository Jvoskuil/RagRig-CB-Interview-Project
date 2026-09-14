"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "choice_and_action_rationale",
        "raw_interview_anchor": "I recommended we not overreact with a full cordon-and-search ... we did push more ISR onto two suspected cache routes and stood up a limited checkpoint pilot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Measured response rationale based on limited confirmation and uncertainty."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_action_rationale",
        "raw_interview_anchor": "Mainly time pressure and thin confirmation. We only had eight weeks of data total ... I didn't want to overcorrect off one bad week.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains a cautious response to sparse data and command pressure."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "causal_attribution_and_alternative_explanation_weighting",
        "raw_interview_anchor": "I told them Steady Watch was working. The numbers backed it up ... That's a big swing ... I treated those as secondary color ... I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rtm_01"
        ],
        "ground_truth_rationale": "The participant attributes the decline primarily to Steady Watch while failing to consider natural reversion after an extreme spike."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "resource_allocation_recommendation",
        "raw_interview_anchor": "Given what I'd just seen in District X, I recommended rolling Steady Watch out to District Y too, expecting a similar sharp drop.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest contains no independent instance at this downstream decision point."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "alternative_analysis_and_decision_rationale",
        "raw_interview_anchor": "I considered it, but time was short and District X felt like a validated model ... The Y handler did mention their spike had a different, still-unresolved driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification excludes an independent hidden instance here."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "forecast_and_communication_choice",
        "raw_interview_anchor": "I presented a forecast of continued low attack tempo ... I could have given a wider range ... but the trend line looked clean and the commander wanted something decisive.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No separate hidden bias instance is planned for this forecast decision."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "retrospective_reasoning_reflection",
        "raw_interview_anchor": "Eleven against a baseline of three is a huge jump, and huge jumps like that don't usually stay huge. I focused on what we did in response rather than on how unusual that single week was.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This retrospective reflection is not a second hidden occurrence."
      }
    ]
  }
