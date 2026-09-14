"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "monitoring_strategy",
        "raw_interview_anchor": "checking the plot, cross-referencing with a visual sweep every few minutes since I know some of these wooden boats don't paint well on radar",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Independent visual cross-checking is a sensible monitoring strategy and is not an intentionally biased instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_prioritization",
        "raw_interview_anchor": "It was converging, but slowly, and ARPA still wasn't holding a firm track ... I logged it mentally as one to watch rather than something urgent.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the initial low-urgency assessment before the hidden Automation Bias decision point; the specification assigns no planned bias here."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "attention_allocation",
        "raw_interview_anchor": "I went with splitting attention — mostly trusting the system's target list but throwing in visual checks specifically because I've been burned before by small wooden hulls not showing up well.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The response describes a mixed ARPA and visual monitoring plan at Decision Point 1, which is explicitly non-biased in the hidden specification."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_escalation",
        "raw_interview_anchor": "The lookout said the boat seemed to be zigzagging ... But ARPA's overall ranking still had nothing above the alarm threshold ... I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything was critical yet.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ab_01"
        ],
        "ground_truth_rationale": "The decision defers to ARPA's aggregate ranking and non-alarm state despite the conflicting lookout report, delaying independent plotting or avoidance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "risk_estimation_and_attention_allocation",
        "raw_interview_anchor": "this loose cluster showed up right at the spot from the bulletin, and my first thought honestly was 'this is the same setup as that near-miss' ... I started orienting my planning toward the cluster",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "The vivid recalled bulletin drives the estimated danger and attention allocation despite the cluster's weaker plotted risk relative to the bulk carrier."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "comparative_attention_correction",
        "raw_interview_anchor": "The bulk carrier was actually the one with the tightening CPA on the numbers ... for a bit my attention was more on the cluster ... later ... realized that was the one needing the firmer action.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a later recognition and correction within the same episode; the hidden instance is mapped to the earlier salience-driven judgment in seg_005."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "communication_and_resource_recommendation",
        "raw_interview_anchor": "I recommended posting an extra lookout for the rest of the transit ... based on what we'd actually observed that watch, not tied to any one incident.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The post-watch recommendation is an evidence-based precaution and Decision Point 4 contains no planned bias instance."
      }
    ]
  }
