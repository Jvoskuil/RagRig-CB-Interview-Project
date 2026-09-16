"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "schedule_context_reasoning",
        "raw_interview_anchor": "It was a compressed week. We had four things converging... the contract had liquidated damages tied to the occupancy date, so everything landed at once.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive explanation of schedule convergence and commercial pressure, but no hidden bias mechanism is manifested in this span."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_decision",
        "raw_interview_anchor": "Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence... It felt corroborated...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["he4_iot_01"],
        "ground_truth_rationale": "The participant attributes increased credibility to repeated identical claims and does not check whether the documents share one underlying test."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "action_inaction_decision",
        "raw_interview_anchor": "I authorized the commissioning to proceed... holding the whole phase for a re-run felt like it would stall the entire program... I treated the re-run as something that could happen in parallel rather than as a gate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["he4_ab_01"],
        "ground_truth_rationale": "The active commissioning step is preferred over waiting for a recommended safety re-run primarily to maintain momentum under uncertainty and deadline pressure."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "risk_prioritization_decision",
        "raw_interview_anchor": "There'd been that apartment-tower fire overseas about two weeks earlier... It stuck with me... I put the remaining time into re-inspecting the cladding fire-stopping.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["he4_afb_01"],
        "ground_truth_rationale": "A vivid unrelated recent fire drives the cladding priority despite a different, documented system and an unresolved pressurization deficiency."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "default_parameter_selection",
        "raw_interview_anchor": "We didn't, in the end... The defaults are the standard starting point in that software, so I kept them for the final compliance run.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["he4_db_01"],
        "ground_truth_rationale": "The participant retains generic defaults over available project-specific data, acknowledging the mismatch and citing effort and complication rather than technical superiority."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A retrospective counterfactual about the glazing decision supports the earlier occurrence but is not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "The CFD re-run probably would've been a hard hold point rather than something running in parallel. Without the schedule squeeze, I don't think I'd have authorized commissioning ahead of it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A counterfactual prediction about schedule pressure is evidence about the prior decision, not a separate manifested bias instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "If that overseas fire hadn't been in the news right before my punch-list decision, do you think the priority would have looked different? Possibly...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A qualified counterfactual about the news event is supporting reflection on the punch-list decision, not a new hidden occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "If recalibrating the egress model had taken less effort, would you have used the survey data? Probably, yes...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A counterfactual about effort and the egress parameters supports the prior decision but does not add another hidden occurrence."
      }
    ]
  }
