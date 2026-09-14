"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "decision_alternatives",
        "raw_interview_anchor": "I did a visual first: no obvious damage, no standing water in the case, gasket looked a little worn but nothing dramatic. At that point I had two ways I could go. I could sit and watch the signal through another cycle or two to see if the drop repeated in a way I could actually observe, or I could go straight into bench testing the track circuit and relay to start ruling things in or out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Options considered after inspection; no bias instance is intended."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "choice_rationale",
        "raw_interview_anchor": "I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Choice justified by the movement deadline and value of measurements."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "confidence_and_evidence_comparison",
        "raw_interview_anchor": "Fairly confident, but I'll be honest, it wasn't a slam dunk either way. Watching it might've told me more about the actual pattern — whether it was tied to a specific type of train movement, say. But testing gets me hard numbers right away, and with the clock running, I leaned that way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Weighs information value against time and states uncertainty."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "That's where it got murkier. I ran three insulation resistance cycles. Two came back within normal tolerance, one came back marginally low — not a fail, just lower than I'd like to see. No single component gave me a clean, readable fault. So now I've got a relay and wiring that's original to a fifteen-year-old installation, and one reading out of three that's a little off.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Mixed readings and old equipment are interpreted as ambiguous."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_alternatives",
        "raw_interview_anchor": "Whether to just replace the relay and that wiring segment right there, using the marginal reading as my justification, or hold off and run more cycles to see if a real pattern showed up before committing to a replacement.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States two options following mixed results."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "choice_rationale",
        "raw_interview_anchor": "I ran more cycles instead of replacing on the spot. One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions. I gave it a fourth cycle after some extra drying time, and that one came back normal.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Defers replacement based on one marginal reading, alternatives, and a follow-up test."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "Not entirely. It made the moisture explanation more plausible, but it didn't rule out the wiring either — a marginal insulation reading can come and go for more than one reason, so I still didn't have a clean answer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retains both plausible causal explanations."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "resource_tradeoff",
        "raw_interview_anchor": "The gasket on the cabinet was showing some wear, and the marginal reading lined up with timing not long after that earlier rain. So I had a lower-cost option: dry everything out, clean the connections, reseal the case, and monitor. Or I could go straight to a full replacement of the wiring segment, which would take a lot longer and eat into overtime I'd need approval to extend.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Compares weather-linked interim repair with longer overtime-consuming replacement."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "causal_attribution_and_choice_rationale",
        "raw_interview_anchor": "The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Selects a plausible testable hypothesis while retaining the competing explanation."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "post_intervention_evidence_assessment",
        "raw_interview_anchor": "Readings stayed stable through two more monitored cycles after the drying and resealing. Which was encouraging, but two clean cycles after a marginal one doesn't fully prove the wiring's fine — it's consistent with the fix working, and it's also consistent with the marginal reading just being a one-off that would've cleared up on its own.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Treats post-fix evidence as encouraging but inconclusive."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "restoration_decision_context",
        "raw_interview_anchor": "Right, by that point I had two stable cycles, the next scheduled movement was coming up, and I still didn't have a confirmed root cause — could've been the moisture issue resolved, could've been a quiet wiring problem that just hadn't shown itself again yet. My options were to restore automatic service on the strength of those two stable readings, or keep it under manual block protection for the rest of the shift and take another look in daylight.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States evidence, deadline, unresolved cause, and restoration alternatives."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "restoration_choice_rationale",
        "raw_interview_anchor": "I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there. But I did flag it for a follow-up inspection rather than calling it closed, because I knew I hadn't actually nailed down which explanation was right.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Restores service as an operational trade-off with continued uncertainty and follow-up."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "outcome_interpretation",
        "raw_interview_anchor": "Yeah, ran clean through the rest of the shift. But I want to be clear, that doesn't tell me for certain I got the diagnosis right — it just means nothing happened on my watch that night.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Does not treat clean outcome as diagnostic proof."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "Almost certainly, yeah. Two marginal readings out of four would've pushed me toward the full replacement instead of the interim fix — that's a different pattern than what I actually saw.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Predicts different response to a different test pattern."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "counterfactual_resource_sensitivity",
        "raw_interview_anchor": "Honestly, I might have leaned toward the full wiring replacement regardless, just to close the loop completely instead of leaving it on an interim fix. The time and approval limits were part of what made the cheaper option attractive.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Says expanded overtime would change cost-benefit choice."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "information_need",
        "raw_interview_anchor": "I'd still like a cleaner way to separate a moisture-related reading from an early-stage wiring issue on that generation of cabinet. Right now both look the same on my meter, and that's the part of this call I'm least settled on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Identifies unresolved information need between two plausible causes."
      }
    ]
  }
