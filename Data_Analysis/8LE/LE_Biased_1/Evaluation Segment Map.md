"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_observation_reasoning",
        "raw_interview_anchor": "Watching first just gives me information without giving up the advantage.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 1 is not the hidden positive instance; the officer chooses distance-based observation from vague dispatch information and recent break-ins."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "pat_down_evidence_weighting_reasoning",
        "raw_interview_anchor": "They didn't really go on the same scale for me, if I'm honest. The bulge was a fact I could point to—something's there, I don't know what. Him being relaxed about it, answering fine, not flinching—yeah, in hindsight that probably should've counted for something on the other side. Normally in an uncertain stop like that, somebody being that calm and cooperative does ease things off for me a notch, gives me a little more room to slow down. But here, once I clocked the bulge, that easing just didn't happen—the calm didn't really buy him anything against the pocket.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fpe_01"
        ],
        "ground_truth_rationale": "The hidden instance is at decision point 2: the present pocket bulge is weighted heavily while the absent nervous/evasive cues and calm cooperation are discounted in the same pat-down judgment."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "post_pat_down_detention_reasoning",
        "raw_interview_anchor": "Holding him a few extra minutes to get dispatch confirmation felt like the reasonable middle ground—not cutting him loose on an unverified story, but not escalating into an arrest either.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 3 is outside the single hidden instance; the officer holds briefly for independent verification after a clean pat-down."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "stop_closure_reasoning",
        "raw_interview_anchor": "Once dispatch confirmed the account and the employee showed up right after, there wasn't anything left to hang a citation on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is outside the hidden instance; verified delivery information and the employee’s arrival support release and documentation."
      }
    ]
  }
