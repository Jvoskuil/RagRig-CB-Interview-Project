"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "schedule_assessment",
        "raw_interview_anchor": "Actually pretty comfortable, for once. We had six weeks from kickoff to permit submission... I wasn't fighting the calendar the way I sometimes am.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly characterizes the schedule as comfortable and non-constraining; this is contextual reasoning and contains no hidden bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "commodity_classification_and_information_search",
        "raw_interview_anchor": "There wasn't really a schedule reason it had to happen that week... I'd done two other jobs for similar 3PL operators... I went with Class III based on that pattern and moved on... I went with that pattern instead of waiting on their list.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["st_01"],
        "ground_truth_rationale": "The classification was inferred from a tenant-type category and two prior exemplars instead of tenant-specific packaging data, despite feasible time to obtain it."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "hydraulic_density_area_selection",
        "raw_interview_anchor": "Several density and area points would have satisfied code minimum... I took the first point that cleared the minimum... I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["sf_01"],
        "ground_truth_rationale": "The participant stopped at the first technically acceptable design point without comparing configuration-specific alternatives, although several weeks remained."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "value_engineering_risk_communication",
        "raw_interview_anchor": "Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him... so I recommended pulling the allowance to hit his number... I framed the removal as a reasonable trade rather than spelling out how much margin we'd be giving up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["ib_01"],
        "ground_truth_rationale": "The recommendation and selective framing were shaped by preserving an ongoing owner relationship while reducing a known safety margin."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "commissioning_testing_decision",
        "raw_interview_anchor": "The AHJ requires the witnessed flow test regardless, and with days to spare before move-in, there wasn't a reason to cut corners. I did the full test.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant followed the required full testing process with adequate schedule slack; the generation specification embeds no bias at Decision Point 4."
      }
    ]
  }
