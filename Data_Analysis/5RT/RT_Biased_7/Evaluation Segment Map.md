"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_operational_constraints",
        "raw_interview_anchor": "Get it done safe, get it done in the window. Those two things are supposed to line up, but this one had some tension in it — rain was forecast within about 48 hours, which cuts into ballast curing time, and we only had one tamper and one ballast regulator, shared with the gang working the adjacent territory. So there wasn't a lot of slack.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant balances safety and schedule while identifying real weather and equipment constraints; this is ordinary operational framing."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "duration_and_scope_estimation",
        "raw_interview_anchor": "I used our standard production rate for a 500-foot renewal — so many ties an hour with a full crew — and built a 60-hour schedule off that, plus the fair rating. We mobilized that afternoon.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_02"
        ],
        "ground_truth_rationale": "The supervisor commits to the standard-rate duration without adjusting for the deterioration signal, expressing the hidden Planning Fallacy."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "analogical_case_use_in_method_selection",
        "raw_interview_anchor": "One of the inspectors mentioned a similar-looking curve we'd worked three years back that came in light on tie count too, and it held up fine long-term. That gave the room some confidence, and we went with the faster method.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_04"
        ],
        "ground_truth_rationale": "The prior curve's favorable result reassures the group. Later, the participant says MP 47.3's drainage was worse and the contrary report was not revisited, establishing the hidden Experience Bias in this decision."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_selection_before_scope_commitment",
        "raw_interview_anchor": "Honestly, the fair rating was the most recent data point I had, and the production table's what we use on every job like this — it's not something I second-guess unless there's a specific reason to. There is a longer defect history on that segment in our system, going back five years, that tracks flaw growth over time. I didn't pull it. At the time it felt like it'd just slow down getting the crew mobilized, and the two-week-old inspection seemed current enough to plan against.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_01"
        ],
        "ground_truth_rationale": "The accessible five-year history was not retrieved before commitment, and the supervisor preferred the recent rating. This is the hidden Ostrich Effect."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "collective_risk_judgment",
        "raw_interview_anchor": "By the end, everybody was more on board with running fast than any one of us had been at the start of that meeting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_03"
        ],
        "ground_truth_rationale": "The group's confidence in the accelerated method increased beyond members' initial positions during discussion, expressing Group Polarization."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "causal_attribution_in_status_reporting",
        "raw_interview_anchor": "I told him we'd had a late ballast delivery and lost some hours to a rain delay overnight, which was true, both happened. For the segments that were tracking on pace, I credited the crew's execution and the call to add the extra tamper pass. He signed off on keeping the existing timeline.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_05"
        ],
        "ground_truth_rationale": "The report attributes slippage to external causes, credits progress to crew execution and the participant's choices, and omits the initial scope estimate. The later admission confirms that estimate contributed to slippage."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "gain_loss_weighting_in_go_no_go",
        "raw_interview_anchor": "The penalty clause was the thing sitting heaviest on me at that point. Missing that window meant a real financial hit to the region, and I didn't want to be the reason for that. I knew the geometry car would give us a continuous read across the whole segment that manual checks just can't match, but with that loss already sitting right in front of us and the verification still open-ended, avoiding the hit was what drove the call more than anything else.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_06"
        ],
        "ground_truth_rationale": "The participant centers the choice on avoiding the contract penalty despite knowing the higher-fidelity verification remained incomplete, expressing Loss Aversion/Loss Framing."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "risk_control_judgment",
        "raw_interview_anchor": "We'd done manual gauge spot-checks across the segment and they came back clean, and I'd set up extra hand-inspection rounds plus a pilot train running the curve at reduced speed before we opened it to normal traffic. The roadmaster pointed out that the hand rounds and the pilot train wouldn't give us the same continuous profile the car would, but I figured between what we already had and those extra rounds, we'd catch anything that mattered. Between those, I felt like we had the risk covered well enough to lift the slow order without waiting on the geometry car.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rt7_07"
        ],
        "ground_truth_rationale": "The supervisor treats the checks as sufficient substitutes for the missing profile despite a warning that they are not equivalent, expressing Illusion of Control. The composite RAG finding is assigned to the separate penalty-weighting segment under one-to-one matching."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "post_decision_outcome_assessment",
        "raw_interview_anchor": "It ran the next day and came back within tolerance. So the track was fine. But I'll say that doesn't necessarily tell you whether lifting it early that morning was the right call or just the way it worked out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant separates the favorable outcome from the quality of the earlier decision; this is sound retrospective reasoning."
      }
    ]
  }
