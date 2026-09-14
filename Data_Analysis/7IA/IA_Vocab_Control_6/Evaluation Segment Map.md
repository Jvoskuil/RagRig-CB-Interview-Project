"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_triage_reasoning",
        "raw_interview_anchor": "After the Low score, I did a quick scan of the alert summary fields — parent process, any flagged child processes, whether the trading-support role tag showed anything unusual. Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would have run fifteen to twenty minutes, but I noted it to revisit if anything else came in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The control specification marks phase 1 as a proportionate verification and resource trade-off; the participant checks the automated score, does not accept it outright, and plans to revisit on a new signal."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "attribution_reasoning",
        "raw_interview_anchor": "The registry-key match was strong — I had documented that artifact myself in an earlier report, so I trusted it as a data point. But I did not want to treat it as decisive on its own, because two things cut against it: the C2 domain registration profile did not match GreyFalcon’s usual infrastructure, and the target — an HR database — was not something GreyFalcon has gone after in anything I had tracked. So I called it moderate confidence rather than high, and flagged both mismatches explicitly as things the hunt would need to test.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The control specification requires balanced attribution: the registry match is weighed with both discordant signals and confidence is kept moderate."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "hunt_scope_reasoning",
        "raw_interview_anchor": "The bulletin listed five IOCs — the protocol signature and two file hashes among them, not really ranked by the vendor in any stated order. I started with the two file hashes first, since they were more specific and carried a lower false-positive risk technically, and treated the protocol signature as a second pass to expand into if the first pass did not resolve things. It was not about which one stood out most on the page — it was about which ones would tell me the most per unit of hunt effort.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The control specification describes diagnosticity-driven two-pass scoping and explicitly rejects list order or prominence as the basis for sequencing."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "containment_reasoning",
        "raw_interview_anchor": "I did not pick one over the other outright. The vendor bulletin was well-formatted and specific; the colleague’s notes were hedged but, as far as I could tell, accurate. I checked specific claims from both against the telemetry I had — did the timestamps line up, did the described behavior match what we actually saw — and both held up partially.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The control specification requires cross-checking both sources against telemetry and blending corroborated elements, rather than preferring presentation style."
      }
    ]
  }
