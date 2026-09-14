"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_clinical_impression",
        "raw_interview_anchor": "Recognized five prior panic-attack-coded visits and described the presentation as classic on the surface.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Initial impression and chart recognition are background framing here; the hidden occurrence is assigned narrowly to the later ambiguous-vital-sign interpretation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "protocol_action_rationale",
        "raw_interview_anchor": "“Chest pain protocol doesn't care about history” and ECG was obtained within the protocol window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Protocol adherence regardless of psychiatric history; no hidden bias mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "triage_choice_rationale",
        "raw_interview_anchor": "Chose full chest-pain protocol rather than lowering acuity because of the anxiety history.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly evidence- and protocol-consistent triage choice."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "ambiguous_evidence_interpretation",
        "raw_interview_anchor": "“My read at the time was that this looked like her usual picture” and he gave an anxiolytic with reassessment instead of immediate D-dimer/CT.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant interpreted borderline tachycardia and SpO2 through the chart-derived expectation of recurrent anxiety and deferred PE testing."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_update_and_workup",
        "raw_interview_anchor": "New calf tenderness and swelling did not fit the prior pattern; he calculated Wells score and ordered D-dimer and CT angiography.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Evidence-driven updating and escalation after new information."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "disposition_rationale",
        "raw_interview_anchor": "Held the patient in a monitored bed rather than admitting before imaging because she was stable and CT was pending.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Disposition decision based on uncertainty and clinical stability, not the hidden bias."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "Reported the greatest uncertainty after the elevated D-dimer while imaging was pending.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicit uncertainty tolerance; no hidden bias mechanism."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_adjustment",
        "raw_interview_anchor": "“I'd probably weigh the sats a little more heavily on their own” in retrospect.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective corrective reflection, not an additional hidden occurrence."
      }
    ]
  }
