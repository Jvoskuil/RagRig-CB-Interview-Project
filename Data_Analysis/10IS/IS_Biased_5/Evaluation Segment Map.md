"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "operational_constraint_reasoning",
        "raw_interview_anchor": "Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A substantive continuity and availability constraint supporting the decision, without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "architecture_choice_reasoning",
        "raw_interview_anchor": "We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant explicitly gives the familiar existing system extra weight and does not comparatively evaluate the migration alternative, matching Status Quo Bias."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "risk_estimation_and_urgency_reasoning",
        "raw_interview_anchor": "That breach a peer firm had a couple years back ... was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically. ... I used that story more than the actual advisory language when I was framing the urgency internally.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "A vivid recalled peer ransomware incident was given more weight than the current advisory when communicating risk, matching Availability Bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "comparative_vendor_evaluation",
        "raw_interview_anchor": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The participant preferred statistically equivalent information because of its positive versus negative wording, matching Framing Bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "peer_evidence_weighting",
        "raw_interview_anchor": "Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint ... I figured if that many peers were comfortable, the risk was manageable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "Peer-adoption volume substituted for independent compatibility verification, matching the Bandwagon effect."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "staffing_constraint_reasoning",
        "raw_interview_anchor": "We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A genuine staffing-based operational rationale; the hidden Overconfidence instance is mapped to the separate generalization from prior cutovers."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "cutover_risk_mitigation_reasoning",
        "raw_interview_anchor": "I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable ... those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_05"],
        "ground_truth_rationale": "The participant generalized from prior successes to a materially different architecture and compressed a recommended safety margin, matching Overconfidence Bias."
      }
    ]
  }
