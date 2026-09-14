"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_tradeoff_reasoning",
        "raw_interview_anchor": "Keep the railroad safe, obviously, but also keep things moving; Q-119's on-time window and the cold snap.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant frames competing safety, schedule, and weather considerations without a manifested target bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_classification_rationale",
        "raw_interview_anchor": "Similar small flaws that just sat there; my first read was, this looks like the kind of thing we've seen.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the initial assessment based on historical cases, before the inspector's explicit comparison of the growth rate with prior cases. The generation specification documents a plausible non-bias interpretation for a monitor classification at this size."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_decision",
        "raw_interview_anchor": "Doubling in three weeks is quicker ... still a small number in absolute terms. It didn't strike me as enough to change the call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant recognizes the faster growth evidence but discounts it as insufficient to change the existing monitor classification, matching the hidden Conservatism Bias instance at decision point 1."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "Nothing in front of me suggested immediate failure, just a number that had gone up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "This explanation again minimizes the significance of the increase despite the known readings and growth comparison. It is evidence from the same hidden decision-point-1 occurrence, not a separate occurrence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_explanation",
        "raw_interview_anchor": "I just didn't weigh the rate itself as the deciding factor. I was weighing it against 'we've handled dozens of these,' and none of them ever became anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant explicitly gives prior non-events greater weight than the reliable growth-rate evidence, further expressing the same under-updating instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "analogical_reasoning",
        "raw_interview_anchor": "Three specific cases ... where we had a flaw that size ... it never amounted to anything. That's twenty years of pattern.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant relies on specific personally recalled cases as the basis for expecting the present flaw to resolve similarly, despite the material context differences raised by the inspector."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "Those three cases felt close enough ... We held off on any interim slow order ... it felt like overkill.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant rejects a slow order by relying on the recalled cases as sufficiently similar, continuing the same hidden decision-point-2 occurrence."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "group_decision_reasoning",
        "raw_interview_anchor": "Everybody's confidence built on everybody else's ... more decisive than where any of us individually started.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gp_01"
        ],
        "ground_truth_rationale": "The participant reports that group discussion shifted initially cautious positions toward the more extreme risk-tolerant decision to release at full speed, matching Group Polarization."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "consensus_interpretation",
        "raw_interview_anchor": "The whole call took maybe six minutes. Nobody raised an objection ... there wasn't a sense we needed to slow down and hash it out further.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gp_01"
        ],
        "ground_truth_rationale": "The short call and absence of voiced dissent are part of the same hidden group-polarization episode; they do not constitute a separate occurrence."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "stakeholder_inclusion_reasoning",
        "raw_interview_anchor": "The assistant engineer ... wanted to raise concerns ... he wasn't looped in beforehand ... nobody was especially eager to reopen that discussion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The group excludes a known dissenting stakeholder in part to avoid reopening the disputed classification, matching part of the hidden Groupthink instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "debrief_evidence_interpretation",
        "raw_interview_anchor": "Agreed pretty quickly it was unrelated ... didn't get into re-examining the retest interval or walking back through the earlier classification call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The group rapidly dismisses ambiguous evidence and avoids reviewing the earlier decision, matching part of the hidden Groupthink instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "consensus_recording",
        "raw_interview_anchor": "Everybody agreed it was a non-event. The minutes just note we concluded the process worked as intended.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The participant describes unanimous closure and a record that the process worked as intended without a dissenting view, part of the same hidden Groupthink instance."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "alternative_review_rationale",
        "raw_interview_anchor": "We could have pulled the assistant engineer in ... or kicked it up ... Given how it played out ... it didn't feel necessary.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The participant acknowledges independent review options but dismisses them based on the group's benign interpretation of the sound, continuing the same hidden debrief instance."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "retrospective_reflection",
        "raw_interview_anchor": "Probably the debrief. He was asking to be included for a reason ... Might've been worth five more minutes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective recognition that dissent might have been useful, not a new biased decision or an additional hidden occurrence."
      }
    ]
  }
