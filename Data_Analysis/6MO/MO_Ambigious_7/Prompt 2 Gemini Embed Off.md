You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making the time. This is a confidential debrief on the cargo transfer job alongside the platform, purely to understand the reasoning behind decisions on the day — not a disciplinary review. Comfortable proceeding?

Participant: Yes, go ahead.

Interviewer: Can you start with your role that day?

Participant: I was DPO on watch, running DP2 station-keeping during a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normal job in most respects. Hold position off the leg, crane operator takes the lifts, we maintain the watch circle.

Interviewer: What made this one non-routine?

Participant: The forecast weather was closing in a bit faster than the morning brief suggested. Roughly a four-hour window before sea state would exceed the platform crane's limit. So there was schedule pressure, but nothing outside what we train for.

Interviewer: Walk me through what happened, start to finish.

Participant: On final approach I picked up a 1.7-meter discrepancy between HPR and the two DGPS units, which were agreeing with each other closely. The system had auto-weighted the DGPS pair and was showing green. I also remembered that HPR had an intermittent fault logged from a previous voyage — cleared, but never formally re-certified after that. Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach. We got alongside, transfer went smoothly through the first several lifts. About halfway — 55% of cargo across — Thruster 3 raised a yellow caution, reduced power available. Consequence analysis still showed adequate capability, but with less margin than we'd started with. I also knew that switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn't have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace. On the second-to-last lift, there was a wind shift that changed the footprint recommendation on the DP plot. I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately. The Master noticed the vessel's attitude shift a short time after and flagged it. For the final lift, OIM asked whether we could finish or should stand off. I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish. Partway through, our separation closed faster than either figure had suggested it would, and we suspended early and backed off. No contact, stayed inside the watch circle, but it was closer than planned.

Interviewer: Let's go back through that in order. What were you tracking at each stage?

Participant: Early on, reference systems and DP status, which is standard for closing distance. Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks. During the final lift specifically, the crane display gets priority per procedure, and whoever's free on the bridge picks up secondary monitoring — that shifted around a bit depending on what else was happening at the time.

Interviewer: On the reference discrepancy — talk me through the reasoning there.

Participant: DGPS1 and DGPS2 agreed tightly. HPR was off by 1.7 meters, and it had that fault history from a prior voyage — nothing currently logged against it, but nothing re-certifying it as fully sound either. Given a choice between two fresh, agreeing units and one with an open question mark over it, I leaned toward the DGPS pair. I didn't call it settled — I noted it as something to keep an eye on rather than a solved problem.

Interviewer: Did you consider pausing to pull HPR's diagnostic log before continuing?

Participant: I thought about it. It would have meant holding the approach for a few minutes with no clear guarantee it would tell us anything conclusive, since the fault history was intermittent by nature. I judged the DGPS agreement plus HPR's own track record gave enough basis to proceed, but I'll be honest, it wasn't a fully closed question either way.

Interviewer: Now the thruster caution — what went into continuing there?

Participant: The consequence analysis still cleared us, just with a smaller cushion than before. I also had a rough number for what a mode change would cost us time-wise against a window that was already tight. It came down to margin against time cost, and the margin figure won out. I can see an argument either way on that one.

Interviewer: Did the amount of cargo already moved factor into it?

Participant: No — the cargo already across was just where we happened to be in the sequence, not something I weighed. The actual comparison was the consequence-analysis margin against the projected delay from reconfiguring, and the margin held up well enough to justify continuing at that point.

Interviewer: Move to the final lift and the footprint change. What was happening with attention at that point?

Participant: Standard procedure has the crane display as priority during an active lift. My co-operator was tied up confirming rigging on the radio for the next lift, which is a legitimate concurrent task, not something either of us could have dropped without creating a different problem. So the footprint change sat for a short while before either of us caught it.

Interviewer: Would reassigning that monitoring in the moment have been realistic?

Participant: Possibly, but it would have meant interrupting a rigging confirmation that also affects safety on the next lift. It's a genuine trade-off, not an obvious call either way.

Interviewer: Last one — the OIM's question about the final lift.

Participant: I looked at both numbers I had — time to finish and the current separation and capability readout — and both supported finishing at that moment. The margin just closed faster than either had indicated it would once we were actually maneuvering.

Interviewer: If the margin readout had shown a tighter number at that moment, would that have changed your answer?

Participant: Probably, yes — if the readout itself had been less favorable I'd have told him to stand off. The issue wasn't which number I used, it's that the number moved faster than expected.

Interviewer: Looking back at the whole sequence, does it seem like there were earlier signs of how close things got, or does it read that way mainly because of how it ended?

Participant: Honestly, I go back and forth on that. Individually, none of those things — the discrepancy, the caution, the workload split — crossed a line that demanded a different call. Whether they add up to something predictable in hindsight, or whether it just came together unluckily at the end, I'm genuinely not sure.

Interviewer: What would you tell a newer DPO facing something similar?

Participant: Don't treat any single reading in isolation, and keep checking whether your trade-offs still hold as conditions shift, not just at the point you first made them.

Interviewer: Anything you'd do differently?

Participant: Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady. Otherwise I think the calls were reasonable given what was in front of me at each point.

Interviewer: Appreciate you walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Ambigious_7",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Dynamic Positioning Operator (Offshore Support Vessel)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Reference Drift During Cargo Transfer at North Sea Platform (Ambiguous Control)",
    "scenario_summary_internal": "Paired ambiguous-control counterpart to MO_Biased_7. A DPO aboard the same class of DP2 offshore support vessel conducts a scheduled cargo transfer alongside a fixed platform under a closing weather window, encountering the same four structural decision points: a reference-system discrepancy on approach, a thruster caution mid-transfer, a late environmental cue during the final lift, and an OIM query about finishing the last lift. In this version, each decision is genuinely underdetermined: the available evidence supports more than one reasonable course of action, the DPO's stated reasoning references defensible operational heuristics and workload constraints, and no decision is driven by selective evidence weighting, automated deference, attentional fixation, sunk-cost justification, default preservation, or a skewed decision frame. The incident still ends as a near-miss with an early suspension of the final lift, preserving outcome ambiguity so that the sequence cannot be judged biased or unbiased purely from its result.",
    "occupational_realism": {
      "objective": "Complete a scheduled cargo transfer of deck cargo and bulk material from the OSV to a fixed offshore platform under DP2 station-keeping, within a forecast weather window, without breaching safe approach distance or DP capability limits.",
      "setting": "North Sea fixed platform, DP2-class offshore support vessel on standby/cargo-transfer duty, daylight, forecast deteriorating sea state (rising from 2.5m to 3.5m Hs) over a 4-hour window, cargo crane operations alongside the platform leg.",
      "constraints": [
        "Closing weather window before conditions exceed platform crane operating limits",
        "Limited remaining vessel time on charter before transit to next location",
        "DP2 redundancy requirement (loss of one reference system must not compromise position-keeping)",
        "Crew fatigue from an extended shift",
        "Communication lag between crane operator, platform OIM, and bridge team"
      ],
      "stakeholders": [
        "Dynamic Positioning Operator (interviewee)",
        "Master / DP2 co-operator",
        "Platform Installation Manager (OIM)",
        "Crane operator",
        "Vessel superintendent (shore-based, schedule pressure)"
      ],
      "technical_terms_to_use": [
        "DP2 redundancy concept",
        "reference system (DGPS, HPR, laser/Fanbeam)",
        "footprint plot",
        "consequence analysis",
        "thruster caution alarm",
        "green/yellow/red DP status",
        "safe working envelope",
        "watch circle",
        "weather window"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "automation bias",
        "inattentional blindness",
        "hindsight bias",
        "sunk cost",
        "status quo bias",
        "framing effect",
        "any explicit bias or heuristic terminology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "DGPS1 and HPR show a 1.7m position discrepancy during final approach",
          "DGPS2 agrees closely with DGPS1",
          "DP system auto-selected DGPS1/DGPS2 as the weighted reference pair, showing overall GREEN status",
          "HPR has a minor, previously logged intermittent fault history from a prior voyage, since cleared but not re-certified"
        ],
        "new_information_after_decision": [
          "HPR discrepancy is later attributed to a plausible combination of the prior intermittent fault history and structural multipath near the platform, with no single definitive cause identified",
          "The discrepancy trend remains within the DP2 alert threshold throughout the approach"
        ],
        "alternatives": [
          "Accept the DP system's auto-weighted reference pair, noting HPR's own uncertain fault history as a reason to deprioritize it",
          "Pause briefly to manually query HPR's fault log and current diagnostic state before closing distance"
        ],
        "intended_action": "DPO cross-references HPR's known intermittent fault history against the current discrepancy, reasonably concludes that a previously flagged reference carries more uncertainty than two freshly agreeing units, and proceeds while noting the ambiguity for the log rather than treating it as fully resolved."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Approximately 55% of cargo has been transferred; two lifts remain",
          "Thruster 3 shows a yellow caution for reduced power availability",
          "DP consequence analysis shows adequate capability with the caution active, but with reduced margin compared to the start of the job",
          "Weather forecast confirms Hs will exceed platform crane limits within roughly 70 minutes",
          "A conservative mode change would add an estimated 20-25 minutes to remaining completion time"
        ],
        "new_information_after_decision": [
          "Thruster 3 caution persists at a stable but unresolved severity through the remaining transfer",
          "The added time cost of a conservative mode change is later confirmed to have been a reasonable estimate, making the original trade-off assessment defensible in retrospect"
        ],
        "alternatives": [
          "Suspend the transfer, move to standby distance, and reassess DP capability before continuing",
          "Switch to a more conservative operating mode at the cost of additional time within the closing weather window",
          "Continue the transfer at the current pace, citing the consequence analysis and the time cost of switching modes"
        ],
        "intended_action": "DPO weighs the consequence analysis result against the time cost of switching to a more conservative mode within the specific closing weather window, and continues at current pace, explicitly citing the capability margin rather than the amount of cargo already completed as the deciding factor."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "DPO's attention is concentrated on the crane boom position display during the final lift, per the vessel's standard lift-monitoring procedure",
          "A new wind-shift alert changes the vessel's heading/footprint recommendation on the DP plot",
          "The environmental sensor trend line has shifted for roughly 90 seconds prior to the lift's completion",
          "The co-operator is occupied at that moment with a separate radio exchange confirming the next lift's rigging status"
        ],
        "new_information_after_decision": [
          "The wind shift is confirmed moments later by the Master, who notices the vessel's heel/attitude change",
          "Review shows both the crane task and the radio exchange were legitimate concurrent demands on the two-person bridge team at that moment"
        ],
        "alternatives": [
          "Interrupt the co-operator's radio exchange to reassign footprint monitoring during the final lift",
          "Rely on the standard procedure of prioritizing crane-boom monitoring during an active lift, with footprint checks resuming immediately after",
          "Pause the lift briefly to allow a full instrument scan before continuing"
        ],
        "intended_action": "DPO follows the standard procedure of prioritizing crane-boom monitoring during the active lift while the co-operator is legitimately occupied with a concurrent rigging confirmation, resulting in a short delay before the wind shift is registered, consistent with normal two-person workload division rather than a fixed or evidence-driven pattern."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "One final, smaller lift remains, estimated at 8-10 minutes",
          "Wind and swell have increased since Phase 3, narrowing the safe working envelope",
          "Thruster 3 caution and the earlier reference discrepancy are both still present but not escalated to red/alarm status",
          "OIM asks whether the vessel can finish the last lift or should stand off",
          "DPO has both the time estimate and the current separation/capability readout available on adjacent display panels"
        ],
        "new_information_after_decision": [
          "The vessel's separation from the platform decreases more than expected during the final maneuvering, prompting an early suspension of the lift",
          "Post-event review shows the margin readout and the time estimate were both consulted, but the margin trend accelerated faster than either figure had indicated at the moment of decision"
        ],
        "alternatives": [
          "Suspend the final lift now given the narrowing envelope",
          "Complete the final lift after checking both the time estimate and the current margin readout, judging the margin still adequate for the estimated duration"
        ],
        "intended_action": "DPO reviews both the completion-time estimate and the current separation/capability readout, judges the margin adequate for the short remaining duration, and elects to proceed with the final lift before conditions force an early suspension when the margin narrows faster than anticipated."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities during this cargo transfer operation.",
        "Walk me through what a routine transfer alongside this platform normally looks like."
      ],
      "timeline_reconstruction": [
        "Take me through the operation from approach to the final lift, in the order things happened.",
        "What were you monitoring at each stage, and how did that change as the job progressed?"
      ],
      "decision_point_probes": [
        "At the point where the reference systems disagreed, what information did you use to decide which was correct?",
        "What made you comfortable continuing the transfer once the thruster caution appeared?",
        "What were you focused on during the final lift, and how did you become aware of the wind shift?",
        "When the OIM asked about finishing the last lift, what factors did you weigh in your answer?",
        "What alternatives did you consider at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If the HPR discrepancy had appeared without any prior fault history, would your approach have differed?",
        "Looking back, do you think there were earlier indications of the eventual close approach to the platform, or does it look that way mainly because of how it ended?",
        "If you were advising a newer DPO facing a similar sequence, what would you tell them to watch for?",
        "What, if anything, would you do differently if this situation arose again?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MO_Biased_7",
      "features_to_match": [
        "Same DP2 vessel class, platform setting, and closing weather window",
        "Same four-decision-point chronology: reference discrepancy, thruster caution, missed footprint cue, OIM final-lift query",
        "Same stakeholders, technical vocabulary, difficulty, and near-miss outcome structure",
        "Same emotional tone (measured, professional, moderate time pressure) and interview probe structure"
      ],
      "features_to_remove_or_change": [
        "Remove selective reliance on agreeing references as confirmation of a pre-existing view; replace with an explicit, defensible fault-history-based justification for deprioritizing HPR",
        "Remove deference to automated GREEN status alone as the stated reason for inaction; replace with reasoning that references the underlying diagnostic data directly",
        "Remove reliance on cargo/time already invested as the stated reason to continue after the thruster caution; replace with a forward-looking capability-versus-time-cost trade-off",
        "Remove default retention of configuration without comparison; replace with an explicit, reasoned comparison that still results in continuing",
        "Remove attentional fixation on the crane display as an unexplained default; replace with a stated, procedure-based workload allocation between two occupied bridge personnel",
        "Remove framing of the final decision purely around time; replace with an account showing both time and margin figures were consulted",
        "Remove retrospective overstatement of foreseeability; replace with a hypothetical answer that explicitly questions whether the pattern was really foreseeable at the time or only appears so in retrospect"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the DPO's account should show real information gaps, competing legitimate priorities, or reasonable trade-offs, such that a reader cannot confidently classify the reasoning as biased or as optimally rational. Do not resolve the ambiguity toward either a clearly biased pattern or an artificially perfect textbook decision process; avoid contrived neutrality where the DPO recites all alternatives mechanically without genuine trade-off tension."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable - ambiguous_control condition does not implement a counterfactual manipulation",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm zero intended bias instances of any of the seven named biases",
      "Confirm each decision point contains genuine underdetermination with a stated non-bias justification that is at least as plausible as any bias-consistent reading",
      "Confirm no bias terminology, labels, or explanations appear in the public interview text",
      "Confirm structural parity with MO_Biased_7: same stakeholders, vocabulary, four-phase chronology, near-miss outcome ambiguity, and interview probe structure",
      "Confirm final word count falls between 1,215 and 1,485 words",
      "Confirm consequences described (near-approach, suspension) do not mechanically prove the presence or absence of biased reasoning",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm the closing hypothetical explicitly surfaces the foreseeability question without the participant resolving it toward an inflated retrospective certainty"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {"bias": "Confirmation Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; reference-preference decision must be justified by an independent fault-history rationale rather than motivated dismissal of disconfirming evidence"},
      {"bias": "Automation Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; any reliance on system status must be paired with reference to underlying diagnostic data, not deference to the status indicator alone"},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 0, "mechanism_constraint": "Must not manifest; delayed registration of the footprint cue must be explained by a legitimate concurrent workload allocation, not an unexplained attentional default"},
      {"bias": "Hindsight Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; retrospective reflection must explicitly question foreseeability rather than assert it was obvious"},
      {"bias": "Sunk cost bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; continuation rationale must reference forward-looking capability and time trade-offs, not completed cargo or elapsed effort"},
      {"bias": "Status Quo Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; configuration retention must follow from an explicit stated comparison of alternatives, not default preservation"},
      {"bias": "Framing Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; final-lift rationale must reference both time and margin information as jointly consulted, not one framing displacing the other"}
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias",
      "Sunk cost bias",
      "Status Quo Bias",
      "Framing Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Confirmation Bias", "requested_occurrences": 0},
      {"bias": "Automation Bias", "requested_occurrences": 0},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 0},
      {"bias": "Hindsight Bias", "requested_occurrences": 0},
      {"bias": "Sunk cost bias", "requested_occurrences": 0},
      {"bias": "Status Quo Bias", "requested_occurrences": 0},
      {"bias": "Framing Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MO_Biased_7",
    "counterfactual_variable": {
      "name": "N/A",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Ambigious_7",
    "domain_id": "MO",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: ambiguous_control condition requires zero intended bias occurrences across all four decision points. Each decision point that hosted a bias mechanism in the paired MO_Biased_7 scenario (reference discrepancy, thruster caution, footprint cue, OIM final-lift query) is instead constructed with an explicit, independently defensible non-bias rationale of comparable narrative weight and complexity, preserving structural and vocabulary parity without instantiating any named mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Vessel class and DP2 operating mode",
      "Platform setting and weather-window premise",
      "Four-decision-point chronology and sequence",
      "Stakeholder roles (Master, OIM, crane operator, superintendent)",
      "Technical vocabulary and terminology list",
      "Difficulty level and near-miss outcome ambiguity",
      "Interview probe structure and approximate word count"
    ],
    "generation_warnings": []
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
        "segment_type": "Final approach reference discrepancy",
        "raw_interview_anchor": "On final approach I picked up a 1.7-meter discrepancy... treated the DGPS pair as the more trustworthy read... continued the approach.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest is zero-bias; the reference choice is explicitly supported by two agreeing DGPS units and HPR's prior intermittent fault history, with the discrepancy logged as unresolved."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "Thruster caution continuation decision",
        "raw_interview_anchor": "About halfway... Thruster 3 raised a yellow caution... I weighed that against the capability numbers and kept going at the same pace.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The continuation rationale explicitly compares forward-looking capability margin with the projected delay and does not rely on completed cargo."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "Footprint-monitoring workload allocation",
        "raw_interview_anchor": "On the second-to-last lift... I was on the crane boom display... my co-operator was mid-exchange... neither of us picked up the footprint change immediately.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The delayed cue registration is explained by the stated standard lift procedure and a legitimate concurrent rigging-radio task; no hidden selective-attention instance exists."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "Final-lift completion decision",
        "raw_interview_anchor": "For the final lift, OIM asked whether we could finish... I checked both the time estimate... and the separation and capability readout... and told him we could finish.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The decision jointly consults the time estimate and current separation/capability readout; the hidden manifest contains no framing or other bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "Monitoring priorities across phases",
        "raw_interview_anchor": "Early on, reference systems and DP status... Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a procedural description of changing monitoring priorities, with no hidden bias occurrence."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "Reference-system evidence weighting",
        "raw_interview_anchor": "DGPS1 and DGPS2 agreed tightly... Given a choice between two fresh, agreeing units and one with an open question mark... I leaned toward the DGPS pair.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant gives an independent reliability-weighted rationale and keeps the discrepancy open; the control manifest specifies zero confirmation or automation-bias occurrences."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "Diagnostic-pause alternative",
        "raw_interview_anchor": "I thought about it... holding the approach for a few minutes with no clear guarantee... I judged the DGPS agreement plus HPR's own track record gave enough basis to proceed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A pause was considered and rejected on an explicit information-value and operational-basis comparison, with uncertainty acknowledged."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "Consequence-margin versus mode-change time",
        "raw_interview_anchor": "The consequence analysis still cleared us, just with a smaller cushion... It came down to margin against time cost, and the margin figure won out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The stated comparison is between capability margin and projected time cost, not sunk effort or default preservation."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "Cargo-progress factor clarification",
        "raw_interview_anchor": "No \u2014 the cargo already across was just where we happened to be in the sequence... The actual comparison was the consequence-analysis margin against the projected delay.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant expressly disclaims cargo-progress weighting and identifies the forward-looking comparison used."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "Final-lift attention priority",
        "raw_interview_anchor": "Standard procedure has the crane display as priority during an active lift... my co-operator was tied up confirming rigging on the radio.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The attention allocation is attributed to standard procedure and a legitimate concurrent safety task."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "Monitoring reassignment trade-off",
        "raw_interview_anchor": "Possibly, but it would have meant interrupting a rigging confirmation... It's a genuine trade-off, not an obvious call either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant considers reassignment and explains the competing safety cost without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "Final-lift information check",
        "raw_interview_anchor": "I looked at both numbers I had \u2014 time to finish and the current separation and capability readout \u2014 and both supported finishing at that moment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Both information sources were consulted as required by the hidden control rationale; the later closure acceleration is not hindsight proof of bias."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "Counterfactual tighter-readout response",
        "raw_interview_anchor": "Probably, yes \u2014 if the readout itself had been less favorable I'd have told him to stand off.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hypothetical shows a conditional decision rule tied to the readout, without asserting a biased mechanism."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "Retrospective foreseeability assessment",
        "raw_interview_anchor": "Honestly, I go back and forth on that... Whether they add up to something predictable in hindsight... I'm genuinely not sure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly questions foreseeability rather than asserting that the outcome was obvious."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "Proposed fixed margin re-check",
        "raw_interview_anchor": "Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a concrete prospective improvement and does not instantiate any hidden bias."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": [
        "Interviewer",
        "Participant"
      ],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "No retrieved corpus passages were supplied; the analysis therefore relied on a conservative, mechanism-first reading of the transcript alone. Several plausible but unconfirmed bias patterns are recorded as candidates rather than identified occurrences."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "confirmation bias",
        "alternative_labels": [
          "confirmatory search",
          "selective information weighting"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant (DPO)",
        "possible_decision_episode_label": "Reference-sensor discrepancy during final approach",
        "supporting_interview_quote": "Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach.",
        "plausible_mechanism": "A preexisting belief that HPR was unreliable may have led the participant to selectively favor the agreeing DGPS units and to avoid diagnostic testing of HPR.",
        "why_not_identified": "The participant explicitly recorded the discrepancy as unresolved, considered pausing for diagnostics, and gave a legitimate engineering rationale based on two agreeing DGPS units and an uncertified intermittent fault history, so the transcript does not affirmatively demonstrate biased evaluation."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "plan continuation bias",
        "alternative_labels": [
          "get-there-itis",
          "plan continuation error"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant (DPO)",
        "possible_decision_episode_label": "Thruster 3 caution during cargo transfer",
        "supporting_interview_quote": "Switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn't have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace.",
        "plausible_mechanism": "Schedule pressure and commitment to the original transfer plan may have caused the participant to discount the reduced capability margin and continue the existing plan.",
        "why_not_identified": "The participant reports an explicit trade-off between capability margin and time cost, with consequence analysis still showing adequate capability; the transcript therefore does not clearly show biased discounting rather than a permissible operational judgment."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "inattentional blindness",
        "alternative_labels": [
          "attentional tunneling",
          "change blindness"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant (DPO) and co-operator",
        "possible_decision_episode_label": "Missed DP footprint change on second-to-last lift",
        "supporting_interview_quote": "I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately.",
        "plausible_mechanism": "Focused attention on the crane display and a concurrent radio task may have prevented detection of a safety-relevant environmental change.",
        "why_not_identified": "The monitoring allocation followed standard procedure and involved a concurrent safety-relevant task; this may represent a bounded attentional resource or task conflict rather than a distinct cognitive bias."
      },
      {
        "candidate_id": "cand_004",
        "classification_status": "candidate",
        "proposed_bias_label": "overconfidence effect",
        "alternative_labels": [
          "optimism bias",
          "planning fallacy"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant (DPO)",
        "possible_decision_episode_label": "Final lift go/no-go decision",
        "supporting_interview_quote": "I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish.",
        "plausible_mechanism": "The participant may have been overconfident in the stability of the current margin and time estimate, underestimating possible variance in separation or closure rate.",
        "why_not_identified": "The participant used available instrument data and stated that a less favorable readout would have led to a stand-off; the later rapid closure appears attributable to unanticipated environmental dynamics rather than clearly biased subjective confidence."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved corpus passages were supplied, so labels and mechanisms rely on general cognitive-science knowledge rather than corpus-grounded evidence.",
      "Analysis is based solely on self-reported reasoning in a debrief; no objective sensor, eye-tracking, workload, or behavioral data were available.",
      "Several plausible bias patterns could not be confirmed because the participant provided explicit alternative justifications and standard procedural explanations that act as credible non-bias accounts."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Ambigious_7_Gemini_off",
  "interview_id": "MO_Ambigious_7",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
