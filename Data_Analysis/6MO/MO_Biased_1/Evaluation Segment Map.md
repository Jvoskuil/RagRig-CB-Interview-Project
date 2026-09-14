"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "environmental_assessment",
        "raw_interview_anchor": "The forecast weather was closing in a bit faster than the morning brief suggested. Roughly a four-hour window before sea state would exceed the platform crane’s limit. So there was schedule pressure, but nothing outside what we train for.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Interprets the weather window as schedule pressure while judging the conditions within training."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "reference_system_decision",
        "raw_interview_anchor": "On final approach I picked up a 1.7-meter discrepancy between HPR and the two DGPS units, which were agreeing with each other closely. The system had auto-weighted the DGPS pair and was showing green. I also remembered that HPR had an intermittent fault logged from a previous voyage — cleared, but never formally re-certified after that. Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies a fault-history-based reliability rationale, preserved uncertainty, and no automation or confirmation mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "continuation_decision",
        "raw_interview_anchor": "About halfway — 55% of cargo across — Thruster 3 raised a yellow caution, reduced power available. Consequence analysis still showed adequate capability, but with less margin than we’d started with. I also knew that switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn’t have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies a forward-looking comparison of consequence-analysis margin and time cost; cargo completion is not the stated basis."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "attention_and_workload_episode",
        "raw_interview_anchor": "On the second-to-last lift, there was a wind shift that changed the footprint recommendation on the DP plot. I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest explains delayed registration through standard procedure and legitimate concurrent tasks."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "final_lift_decision",
        "raw_interview_anchor": "For the final lift, OIM asked whether we could finish or should stand off. I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish. Partway through, our separation closed faster than either figure had suggested it would, and we suspended early and backed off.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies that both time and margin were consulted; the later near-approach does not establish biased reasoning."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "monitoring_allocation_rationale",
        "raw_interview_anchor": "Early on, reference systems and DP status, which is standard for closing distance. Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks. During the final lift specifically, the crane display gets priority per procedure, and whoever’s free on the bridge picks up secondary monitoring — that shifted around a bit depending on what else was happening at the time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explains procedure-based monitoring priorities and secondary-monitor allocation as workload changes."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "reference_evidence_weighting",
        "raw_interview_anchor": "DGPS1 and DGPS2 agreed tightly. HPR was off by 1.7 meters, and it had that fault history from a prior voyage — nothing currently logged against it, but nothing re-certifying it as fully sound either. Given a choice between two fresh, agreeing units and one with an open question mark over it, I leaned toward the DGPS pair. I didn’t call it settled — I noted it as something to keep an eye on rather than a solved problem.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The participant cites underlying reference data and fault history, and keeps the discrepancy unresolved."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "diagnostic_pause_decision",
        "raw_interview_anchor": "I thought about it. It would have meant holding the approach for a few minutes with no clear guarantee it would tell us anything conclusive, since the fault history was intermittent by nature. I judged the DGPS agreement plus HPR’s own track record gave enough basis to proceed, but I’ll be honest, it wasn’t a fully closed question either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly weighs a diagnostic pause against its uncertain value and preserves uncertainty."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "capability_time_tradeoff",
        "raw_interview_anchor": "The consequence analysis still cleared us, just with a smaller cushion than before. I also had a rough number for what a mode change would cost us time-wise against a window that was already tight. It came down to margin against time cost, and the margin figure won out. I can see an argument either way on that one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly states the comparison between capability margin and projected time cost."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "cargo_completion_influence",
        "raw_interview_anchor": "No — the cargo already across was just where we happened to be in the sequence, not something I weighed. The actual comparison was the consequence-analysis margin against the projected delay from reconfiguring, and the margin held up well enough to justify continuing at that point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly rejects completed cargo as a reason and restates the forward-looking trade-off."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "attention_allocation_explanation",
        "raw_interview_anchor": "Standard procedure has the crane display as priority during an active lift. My co-operator was tied up confirming rigging on the radio for the next lift, which is a legitimate concurrent task, not something either of us could have dropped without creating a different problem. So the footprint change sat for a short while before either of us caught it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Provides a procedure and concurrent-workload explanation for the missed cue."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "monitoring_reassignment_tradeoff",
        "raw_interview_anchor": "Possibly, but it would have meant interrupting a rigging confirmation that also affects safety on the next lift. It’s a genuine trade-off, not an obvious call either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Weighs reassignment against another safety-relevant task."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "final_lift_evidence_weighing",
        "raw_interview_anchor": "I looked at both numbers I had — time to finish and the current separation and capability readout — and both supported finishing at that moment. The margin just closed faster than either had indicated it would once we were actually maneuvering.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. States that both time and margin information informed the decision and attributes the outcome to faster-than-expected closure."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "conditional_decision_prediction",
        "raw_interview_anchor": "Probably, yes — if the readout itself had been less favorable I’d have told him to stand off. The issue wasn’t which number I used, it’s that the number moved faster than expected.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Conditionally predicts a different action if the readout were less favorable."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "retrospective_foreseeability_assessment",
        "raw_interview_anchor": "Honestly, I go back and forth on that. Individually, none of those things — the discrepancy, the caution, the workload split — crossed a line that demanded a different call. Whether they add up to something predictable in hindsight, or whether it just came together unluckily at the end, I’m genuinely not sure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly remains uncertain about foreseeability rather than asserting the outcome was obvious."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "prospective_recheck_rationale",
        "raw_interview_anchor": "Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady. Otherwise I think the calls were reasonable given what was in front of me at each point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Identifies a possible future re-check practice and explains it in light of changing margin."
      }
    ]
  }
