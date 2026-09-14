 "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "role_and_intervention_rationale",
        "raw_interview_anchor": "Standard revenue sector. I'm there to evaluate his technical handling and CRM for the recurrent check, intervening only if there's a safety need.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Defines the participant's evaluation objective and intervention threshold; no hidden bias instance is planned in this zero-bias control."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "dispatch_evidence_weighting",
        "raw_interview_anchor": "There were two things pulling in different directions. On one hand, maintenance had physically done something — replaced a part — not just signed a form. That counts for something. On the other hand, their own test didn't confirm a fault, so the replacement was really a guess about what might have caused it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly weighs supporting and countervailing evidence; the control specification requires no bias instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "maintenance_information_choice",
        "raw_interview_anchor": "I thought about asking whether they'd tested the replaced connector under load, not just visually. I didn't end up asking. Partly schedule, partly that it felt like it might not have changed anything practical — if they said yes, fine, if they said no, we'd probably still have gone.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains a contemplated information-gathering action and competing practical considerations without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "dispatch_threshold_reflection",
        "raw_interview_anchor": "Honestly, I go back and forth on that. If the write-up had said 'fault confirmed, unresolved,' that's different. What we had was murkier — inspected, not confirmed, acted on anyway. I can see an argument for going and an argument for waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States a conditional threshold and preserves competing interpretations; no hidden instance exists."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "climb_symptom_differentiation",
        "raw_interview_anchor": "I remember specifically noting to the captain that this wasn't the same wording as the previous flight's write-up — different system behavior, not obviously connected. That mattered to me because I didn't want either of us assuming it was 'the same thing again' when it might not be.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Distinguishes current and prior symptoms and guards against an unsupported assumption; no hidden bias instance is planned."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "climb_action_choice",
        "raw_interview_anchor": "Leveling off to watch a couple more parameters before continuing. I considered it. In the end the absence of a checklist trigger carried more weight, but I wouldn't say it was an easy call — an ADIRU-adjacent caution always has some amount of 'we don't fully know what's behind this' to it, regardless of how it presents.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Weighs an alternative against checklist evidence while retaining uncertainty; candidate cand_001 localizes here but the hidden control has no positive instance."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "confidence_and_communication",
        "raw_interview_anchor": "Moderately. Not fully confident, not dismissive either. I flagged the uncertainty out loud rather than treating it as settled.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Expresses calibrated confidence and an uncertainty disclosure; no hidden instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "checkride_grading_rationale",
        "raw_interview_anchor": "He explained his reasoning to the FO — the item doesn't affect flight safety, he'd come back to it, and he did. The checklist itself allows some latitude on sequencing non-critical items. So there's a real basis for calling that acceptable. At the same time, a stricter reading of the manual might say any deferral should be flagged differently regardless of the rationale. I noted both readings in the report rather than picking one as obviously correct.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Gives a dual-basis evaluation and records the stricter alternative; no hidden bias occurrence is present."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "seniority_counterfactual",
        "raw_interview_anchor": "I've genuinely thought about that and I don't have a settled answer. Possibly yes, because the rationale and outcome would be identical. Possibly not, if I'd want to see more explicit checklist referencing from someone earlier in their career. I can argue it either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Considers whether seniority would alter grading but does not endorse a distortion; candidate cand_002 localizes here and remains a false alarm at the candidate threshold."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "peer_challenge_response",
        "raw_interview_anchor": "I told him it was a fair question and I wasn't sure. I've had mixed views on this myself across different checks — sometimes I think the standard should be identical regardless of who's flying, other times I think context legitimately matters. I suggested we bring it up at the next standardization meeting rather than me just deciding it on the spot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Responds to a process challenge by acknowledging uncertainty and escalating for standardization; no hidden instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "outcome_counterfactual_reflection",
        "raw_interview_anchor": "If the connector issue had turned out to be confirmed and unresolved, the dispatch call looks different in hindsight. If the deferred checklist item had caused any downstream problem, that grading looks different too. But neither of those things happened, so I'm left without a clean answer on which reading was right.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly frames adverse outcomes as counterfactual and withholds a definitive conclusion; candidate cand_003 localizes here but no hidden instance exists."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "repeat_flight_change_choice",
        "raw_interview_anchor": "I might ask maintenance control the load-test question next time, mostly for the record. Beyond that, I honestly don't know that I'd change the calls themselves. I can see reasonable people landing on either side of each one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Identifies a modest process change while preserving ambiguity about the substantive calls; no hidden instance."
      }
    ]
  }
