"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "diagnostic_choice_and_rationale",
        "raw_interview_anchor": "I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The targeted profiling choice is a reasonable diagnostic narrowing based on deployment timing; no hidden bias instance is manifested."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "resource_allocation_choice_and_rationale",
        "raw_interview_anchor": "I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it... Ripping it out after all that felt like it would waste the specialized knowledge we'd built up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ie_01"
        ],
        "ground_truth_rationale": "The decision to continue patching is justified primarily by sunk engineering effort, specialized expertise, and reluctance to waste prior investment rather than by a forward-looking comparison with the mature alternative."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "personnel_assignment_choice_and_rationale",
        "raw_interview_anchor": "I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh... Marcus hadn't had an incident like that, so it felt like the safer bet.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "nb_01"
        ],
        "ground_truth_rationale": "A single vivid recent outage is given disproportionate weight over Dev's strong eighteen-month record and Marcus's more diffuse pattern of missed deadlines."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "status_communication_choice_and_rationale",
        "raw_interview_anchor": "I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Transparent status reporting with mitigation and monitoring is the specified defensible, non-biased choice."
      }
    ]
  }
