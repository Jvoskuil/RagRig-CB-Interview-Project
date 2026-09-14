You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is just a debrief for training purposes — we're looking at how you worked through the call, not grading the outcome. Okay to go ahead?

Participant: Yeah, that's fine.

Interviewer: Can you tell me your role and set the scene for that evening?

Participant: I'm a signal maintainer covering the territory that includes the Marlow interlocking, out on the secondary main line. I got paged out in the evening after a track crew reported the signal dropping to a more restrictive aspect twice during their shift, then clearing back to normal on its own both times. It had rained earlier that day, so everything out there was still damp. My job was to figure out what was going on and get the signal back to reliable automatic operation before the next scheduled train movement, without stringing the possession out longer than it needed to be.

Interviewer: Walk me through what you found and what you did first.

Participant: When I got to the cabinet, there was no fault code logged at the interlocking — nothing tripped that would point me straight at a component. No history of this signal giving trouble before, either, so it wasn't a repeat offender. I did a visual first: no obvious damage, no standing water in the case, gasket looked a little worn but nothing dramatic. At that point I had two ways I could go. I could sit and watch the signal through another cycle or two to see if the drop repeated in a way I could actually observe, or I could go straight into bench testing the track circuit and relay to start ruling things in or out.

Interviewer: Which way did you go?

Participant: I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me.

Interviewer: How confident were you that testing first was the better call?

Participant: Fairly confident, but I'll be honest, it wasn't a slam dunk either way. Watching it might've told me more about the actual pattern — whether it was tied to a specific type of train movement, say. But testing gets me hard numbers right away, and with the clock running, I leaned that way.

Interviewer: What did the testing show?

Participant: That's where it got murkier. I ran three insulation resistance cycles. Two came back within normal tolerance, one came back marginally low — not a fail, just lower than I'd like to see. No single component gave me a clean, readable fault. So now I've got a relay and wiring that's original to a fifteen-year-old installation, and one reading out of three that's a little off.

Interviewer: What were you weighing at that point?

Participant: Whether to just replace the relay and that wiring segment right there, using the marginal reading as my justification, or hold off and run more cycles to see if a real pattern showed up before committing to a replacement.

Interviewer: What did you decide?

Participant: I ran more cycles instead of replacing on the spot. One marginal reading against two normal ones didn't feel like enough to hang a full replacement on — it could've been the wiring starting to go, or it could've been a temporary moisture effect given the damp conditions. I gave it a fourth cycle after some extra drying time, and that one came back normal.

Interviewer: Did that resolve it for you?

Participant: Not entirely. It made the moisture explanation more plausible, but it didn't rule out the wiring either — a marginal insulation reading can come and go for more than one reason, so I still didn't have a clean answer.

Interviewer: That brings us to the next call — what were the options once you had that pattern of readings?

Participant: The gasket on the cabinet was showing some wear, and the marginal reading lined up with timing not long after that earlier rain. So I had a lower-cost option: dry everything out, clean the connections, reseal the case, and monitor. Or I could go straight to a full replacement of the wiring segment, which would take a lot longer and eat into overtime I'd need approval to extend.

Interviewer: What tipped it for you?

Participant: The timing with the rain was a real data point, not just a guess — it's a known failure mode on older cabinets with worn gaskets. That gave me a specific, testable explanation I hadn't ruled out yet, so trying the cheaper fix first and watching the results made sense to me before committing the extra hours to a full swap.

Interviewer: How did that play out?

Participant: Readings stayed stable through two more monitored cycles after the drying and resealing. Which was encouraging, but two clean cycles after a marginal one doesn't fully prove the wiring's fine — it's consistent with the fix working, and it's also consistent with the marginal reading just being a one-off that would've cleared up on its own.

Interviewer: Last decision — putting the signal back in service.

Participant: Right, by that point I had two stable cycles, the next scheduled movement was coming up, and I still didn't have a confirmed root cause — could've been the moisture issue resolved, could've been a quiet wiring problem that just hadn't shown itself again yet. My options were to restore automatic service on the strength of those two stable readings, or keep it under manual block protection for the rest of the shift and take another look in daylight.

Interviewer: What did you go with, and why?

Participant: I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there. But I did flag it for a follow-up inspection rather than calling it closed, because I knew I hadn't actually nailed down which explanation was right.

Interviewer: Did it hold up?

Participant: Yeah, ran clean through the rest of the shift. But I want to be clear, that doesn't tell me for certain I got the diagnosis right — it just means nothing happened on my watch that night.

Interviewer: If that fourth test cycle had come back marginal again instead of normal, would you have done something different?

Participant: Almost certainly, yeah. Two marginal readings out of four would've pushed me toward the full replacement instead of the interim fix — that's a different pattern than what I actually saw.

Interviewer: And if you'd had open-ended overtime approval that night?

Participant: Honestly, I might have leaned toward the full wiring replacement regardless, just to close the loop completely instead of leaving it on an interim fix. The time and approval limits were part of what made the cheaper option attractive.

Interviewer: Looking back, is there anything you'd want more information on, even now?

Participant: I'd still like a cleaner way to separate a moisture-related reading from an early-stage wiring issue on that generation of cabinet. Right now both look the same on my meter, and that's the part of this call I'm least settled on.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "RT_Ambigious_2",
    "domain_id": "RT",
    "domain": "Rail Transportation",
    "role": "Signal Maintainer / Signal Technician",
    "condition": "ambiguous_control",
    "generation_specification": {
      "scenario_title_internal": "Intermittent Signal Drop at the Marlow Interlocking",
      "scenario_summary_internal": "A signal maintainer is called out to an interlocking after crews report a signal intermittently displaying a more restrictive aspect than expected. Test readings are inconsistent across cycles, weather conditions complicate root-cause attribution, and the maintainer must sequence four decisions about testing, component replacement, and restoring the signal to service before the next traffic window, all under incomplete and genuinely ambiguous diagnostic information.",
      "occupational_realism": {
        "objective": "Diagnose and resolve an intermittent signal malfunction at an interlocking and restore reliable, safe operation before the next scheduled traffic window, without unnecessarily extending the out-of-service period.",
        "setting": "Evening call-out to the Marlow interlocking on a secondary main line; damp weather following an earlier rain shower; one signal maintainer on site with phone access to a signal supervisor.",
        "constraints": [
          "The interlocking must be either fully restored or protected by a manual block/flag arrangement before the next scheduled train movement",
          "Test equipment readings vary somewhat between successive test cycles, some within tolerance and some marginal",
          "Damp conditions from earlier rain could plausibly affect insulation resistance readings on aging wiring",
          "A relay cabinet component is old enough to be a plausible failure point but shows no definitive fault indication",
          "Limited overtime authorization; extending the call-out past a certain point requires supervisor approval"
        ],
        "stakeholders": [
          "Signal maintainer (interviewee)",
          "Signal supervisor (phone contact)",
          "Train dispatcher for the territory",
          "Track crew who reported the original anomaly",
          "Next scheduled train crew"
        ],
        "technical_terms_to_use": [
          "track circuit",
          "relay cabinet",
          "insulation resistance test",
          "signal aspect",
          "interlocking",
          "block occupancy",
          "megger reading",
          "manual block protection"
        ],
        "technical_terms_to_avoid": [
          "zero-risk bias",
          "ambiguity aversion",
          "cognitive bias",
          "heuristic",
          "known versus unknown probability"
        ]
      },
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Track crew reports the signal dropped to a more restrictive aspect twice during their shift, then returned to normal on its own",
            "No fault code was logged at the interlocking cabinet",
            "The signal has shown no prior history of similar reports in maintenance records"
          ],
          "new_information_after_decision": [
            "Initial visual inspection of the relay cabinet shows no obvious physical damage or moisture intrusion"
          ],
          "alternatives": [
            "Begin immediate bench testing of the suspect track circuit and relay before drawing conclusions",
            "Observe the signal through one or two more operating cycles before opening the cabinet, to see if the pattern repeats"
          ],
          "intended_action": "Maintainer opts to begin testing immediately rather than waiting for further occurrences, citing the need to have a diagnosis before the next scheduled train movement."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Insulation resistance readings across three test cycles come back inconsistent: two within normal tolerance, one marginally low",
            "Wiring in the cabinet is original to a 15-year-old installation",
            "No single component shows a readable, unambiguous fault"
          ],
          "new_information_after_decision": [
            "A fourth test cycle, run after additional drying time, returns a normal reading"
          ],
          "alternatives": [
            "Replace the aging relay and suspect wiring segment now, using the marginal reading as justification",
            "Continue monitoring across additional test cycles and hold replacement until a clearer pattern emerges"
          ],
          "intended_action": "Maintainer chooses to run additional test cycles rather than replace the component immediately, reasoning that a single marginal reading amid otherwise normal ones does not yet point clearly to the wiring versus a transient moisture effect."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "The marginal reading occurred shortly after an earlier rain shower, and the cabinet gasket shows minor wear",
            "Drying and cleaning the cabinet connections is a lower-cost, faster interim step",
            "A full wiring segment replacement would take significantly longer and use limited overtime hours"
          ],
          "new_information_after_decision": [
            "Readings remain stable after drying and cleaning, through two more monitored cycles"
          ],
          "alternatives": [
            "Dry, clean, and reseal the cabinet connections as an interim measure and monitor for recurrence",
            "Proceed directly to full replacement of the wiring segment despite the added time and cost"
          ],
          "intended_action": "Maintainer selects the drying-and-resealing approach, noting that the timing correlation with the rain shower offers a plausible, lower-cost explanation that has not yet been ruled out."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "Readings have been stable for two consecutive cycles since the interim repair",
            "The next scheduled train movement is approaching, and manual block protection would need to be arranged if the signal is not restored",
            "Root cause remains unconfirmed as either resolved moisture intrusion or a coincidentally quiet marginal wiring issue"
          ],
          "new_information_after_decision": [
            "The signal operates normally through the next several movements without further incident that shift"
          ],
          "alternatives": [
            "Restore the signal to automatic service, given two stable readings, and schedule a follow-up inspection",
            "Keep the signal under manual block protection for the remainder of the shift and reassess in daylight"
          ],
          "intended_action": "Maintainer restores the signal to automatic service after weighing the stable recent readings against the cost of extended manual protection, while flagging the unresolved uncertainty for a follow-up inspection."
        }
      ],
      "probe_plan": {
        "opening": [
          "Can you describe your role and what the call-out looked like when you arrived?",
          "What was your main objective going into this job?"
        ],
        "timeline_reconstruction": [
          "What did you find when you first got to the cabinet, and what did you do right after?",
          "What new information came in after each step that you didn't have going in?"
        ],
        "decision_point_probes": [
          "What options did you weigh at that point, and what made you lean one way?",
          "What specific reading or observation mattered most to you there?",
          "How much time pressure were you under at that moment?",
          "How sure were you about what was actually causing the issue?",
          "Had you seen a similar pattern before, and did that shape your call?"
        ],
        "closing_hypotheticals": [
          "If the marginal reading had shown up again on that fourth test, would you have done something different?",
          "If the overtime authorization had been open-ended, would that have changed your approach?",
          "Looking back, is there a point where you'd want more information before deciding, even now?"
        ]
      },
      "occurrence_embedding_plan_internal": [],
      "control_specification": {
        "paired_scenario_id": "RT_Biased_2",
        "features_to_match": [
          "Four decision points with at least two plausible alternatives each",
          "Subtle difficulty level and comparable narrative complexity",
          "Single frontline technical operator managing incomplete information under moderate time pressure",
          "Similar occupational register, sentence rhythm, and interview probe structure",
          "Comparable proportion of neutral, well-justified reasoning versus open uncertainty",
          "Consequences that do not conclusively prove any decision right or wrong"
        ],
        "features_to_remove_or_change": [
          "Remove the disproportionate risk-elimination framing used in the paired scenario's routing decision",
          "Remove the ambiguity-driven default-to-known-protocol framing used in the paired scenario's hazard-report decision",
          "Change role from dispatcher to signal maintainer and change the operational domain from train movement sequencing to signal/track-circuit diagnostics",
          "Change the specific incident type from multi-train corridor management to single-site fault diagnosis"
        ],
        "ambiguity_boundary": "Genuine diagnostic ambiguity is preserved throughout (inconsistent test readings, an unconfirmed root cause, and a correlation with weather that is plausible but not proven). The maintainer's reasoning at each point remains explicable by ordinary evidence-weighing, cost-benefit judgment, or conservative safety practice, with no point where a described preference is disproportionate to the evidence or driven specifically by discomfort with unspecified information as its stated cause."
      },
      "counterfactual_specification": {
        "causal_variable": "Recent weather exposure of the relay cabinet (dry versus recently rained-on)",
        "original_state": "The marginal insulation reading occurs shortly after a rain shower, with a worn cabinet gasket offering a plausible moisture-related explanation",
        "counterfactual_state": "The same marginal reading occurs during a stretch of consistently dry weather with no recent precipitation, removing the moisture explanation as a candidate cause",
        "variables_to_hold_constant": [
          "The pattern of inconsistent test readings across cycles",
          "The age and condition of the wiring and relay",
          "The interim drying-and-resealing decision structure",
          "The end-of-shift restoration decision and its timing pressure"
        ],
        "expected_causal_difference": "Without the weather-based explanation available, the maintainer's choice between interim measures and full replacement would need to rest on a different justification, which would help distinguish whether the original decision was driven by the specific moisture evidence or by a more general reluctance to commit to a costlier repair.",
        "causal_test_question": "Does removing the plausible weather explanation for the marginal reading change whether the maintainer chooses an interim fix or a full component replacement?"
      },
      "generation_checks": [
        "Confirm exactly 4 decision points are present in the timeline",
        "Confirm no named-bias mechanism from the manifest is intentionally embedded at any decision point",
        "Confirm each decision point contains genuine, textually supported ambiguity with at least one plausible non-bias explanation already built into the surrounding facts",
        "Confirm technical vocabulary and narrative complexity are comparable to the paired scenario RT_Biased_2",
        "Confirm no bias terminology or psychological labels appear in interview text",
        "Confirm each decision point offers at least two plausible alternatives",
        "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
        "Confirm final word count falls between 1215 and 1485 words",
        "Confirm consequences described do not conclusively prove any decision correct, incorrect, or biased"
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "ambiguous_control",
      "exact_occurrence_manifest": [
        {
          "bias": "Zero-Risk Bias",
          "occurrences": 0,
          "mechanism_constraint": "No intended instance; ambiguous_control overrides the caller-supplied manifest count to zero per condition rules."
        },
        {
          "bias": "Ambiguity effect",
          "occurrences": 0,
          "mechanism_constraint": "No intended instance; ambiguous_control overrides the caller-supplied manifest count to zero per condition rules."
        }
      ],
      "target_bias_names": ["Zero-Risk Bias", "Ambiguity effect"],
      "requested_occurrence_count_for_each_bias": [
        { "bias": "Zero-Risk Bias", "requested_occurrences": 0 },
        { "bias": "Ambiguity effect", "requested_occurrences": 0 }
      ],
      "planned_instance_ids": [],
      "intended_decision_points": [],
      "intended_mechanisms": [],
      "intended_strength": [],
      "paired_scenario_id": "RT_Biased_2",
      "counterfactual_variable": {
        "name": "Recent weather exposure of the relay cabinet (dry versus recently rained-on)",
        "original_state": "The marginal insulation reading occurs shortly after a rain shower, with a worn cabinet gasket offering a plausible moisture-related explanation",
        "changed_state": "The same marginal reading occurs during consistently dry weather with no recent precipitation, removing the moisture explanation as a candidate cause",
        "variables_to_hold_constant": [
          "The pattern of inconsistent test readings across cycles",
          "The age and condition of the wiring and relay",
          "The interim drying-and-resealing decision structure",
          "The end-of-shift restoration decision and its timing pressure"
        ]
      },
      "scenario_id": "RT_Ambigious_2",
      "domain_id": "RT",
      "total_requested_occurrences": 0,
      "total_planned_occurrences": 0,
      "allocation_rule_used": "Not applicable; condition rules for ambiguous_control require zero intended occurrences of all named target biases regardless of the caller-supplied manifest, so no decision-point allocation of bias instances was performed. Genuine, non-bias-attributable ambiguity was instead distributed across all four decision points to match the paired scenario's structure.",
      "control_zero_bias_requirement": true,
      "variables_to_hold_constant": [
        "Four-decision-point structure matching the paired scenario",
        "Subtle difficulty level and interview probe structure",
        "Occupational register and time-pressure framing",
        "Proportion of justified reasoning versus open uncertainty"
      ],
      "generation_warnings": [
        "The caller-supplied occurrence manifest listed 1 occurrence each for Zero-Risk Bias and Ambiguity effect, but the specified condition is ambiguous_control, whose condition rule mandates zero intended instances of all named biases. Per the condition rules (which take precedence over manifest counts for control conditions), this specification implements zero intended occurrences for both biases and documents the override here for audit purposes."
      ]
    }
  }
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
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

</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Mechanism-first review of a signal maintainer debrief covering diagnostic testing, interim repair, and restoration decisions. Operational constraints and explicit uncertainty management were not treated as bias unless a distinct bias-specific mechanism was affirmatively evidenced."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Action bias",
        "alternative_labels": ["bias for action"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Choosing immediate bench testing over passive observation",
        "supporting_interview_quote": "I went straight into testing. Waiting around for it to happen again felt like it could burn time I didn't have if the next train was going to need a clear signal, and testing gets me actual numbers instead of just watching and hoping it repeats on a schedule that suits me.",
        "plausible_mechanism": "A motivational tendency to prefer active intervention over waiting under uncertainty, possibly to reduce discomfort or feel that progress is being made.",
        "why_not_identified": "The transcript shows an explicit time-pressure and information-value rationale, and the participant later acknowledges that watching could have been informative; there is insufficient affirmative evidence that an affect- or motivation-driven action preference outweighed a clearly superior waiting strategy."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Plan continuation bias",
        "alternative_labels": ["get-there-itis"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Restoring automatic service despite unresolved root cause",
        "supporting_interview_quote": "I restored it to automatic service. Two consecutive normal readings after the interim fix was enough for me to move forward, and keeping manual protection running all night has its own cost — it ties up a dispatcher's attention and slows things down for every movement through there.",
        "plausible_mechanism": "A tendency to continue with the planned restoration and scheduled movement despite unresolved causal uncertainty and a recent marginal reading.",
        "why_not_identified": "The decision is presented as an explicit cost-benefit trade-off with a follow-up inspection and clear acknowledgment that the root cause was not confirmed; the transcript does not provide affirmative evidence of a bias-specific plan-adherence mechanism."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "Retrieved corpus passages were largely from aviation and automation domains and offered limited direct support for rail maintenance diagnostic reasoning.",
      "The analysis is based on a retrospective self-report debrief, which may not fully capture automatic or implicit cognitive processes present during the live decision events."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Ambigious_2_Sonnet_on",
  "interview_id": "RT_Ambigious_2",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
