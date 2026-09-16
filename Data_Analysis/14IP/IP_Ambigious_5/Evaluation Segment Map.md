"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_constraint_rationale",
        "raw_interview_anchor": "My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a stated operational objective and constraint rationale, not a hidden cognitive-bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "ambiguous_diagnostic_interpretation",
        "raw_interview_anchor": "That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant recognizes two plausible causes and explicitly rejects a one-sided inference."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "prior_case_evidence_assessment",
        "raw_interview_anchor": "We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The prior incident is considered but its comparability is questioned; the hidden specification explicitly requires no anchoring instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "parallel_resource_allocation_rationale",
        "raw_interview_anchor": "I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Parallel checking is justified by equal plausibility and equal retrieval time, which counterbalances the possible prior-case anchor."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "borderline_measurement_interpretation",
        "raw_interview_anchor": "Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The evidence is explicitly borderline and contested, with no hidden bias instance in the manifest."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "time_constrained_fix_selection",
        "raw_interview_anchor": "A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The insert swap is selected because of the closing press-down window and ambiguous reading, not because of the vivid Line 5 failure that the hidden specification says must not drive the choice."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "post_action_uncertainty_assessment",
        "raw_interview_anchor": "Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant preserves two plausible explanations and does not claim certainty about root-cause resolution."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "external_evidence_transferability_assessment",
        "raw_interview_anchor": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Network adoption is reported as context, while material differences are explicitly recognized; the hidden manifest has zero Bandwagon occurrences."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "partial_validation_and_deadline_tradeoff",
        "raw_interview_anchor": "My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes partial local validation from incomplete geometry testing and network evidence that is promising but inconclusive."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "protocol_adoption_decision",
        "raw_interview_anchor": "I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The action is justified by partial local validation and the deadline, with explicit acknowledgment of reasonable alternatives; the candidate Bandwagon pattern is not affirmed."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "rollout_evidence_weighting",
        "raw_interview_anchor": "Our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The recent result and broader trend are both explicitly considered; the hidden manifest has zero Recency occurrences."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "limited_rollout_decision",
        "raw_interview_anchor": "Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down. A limited pilot on one line with extra monitoring was more appropriate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The limited pilot balances mixed evidence, transferability concerns, and deadline pressure; it does not instantiate overconfidence or recency weighting."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_evidence_assessment",
        "raw_interview_anchor": "Given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This counterfactual response directly documents resistance to disproportionate recency weighting."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "future_process_improvement_rationale",
        "raw_interview_anchor": "Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant proposes process improvements based on information gaps; no hidden instance is present."
      }
    ]
  }
