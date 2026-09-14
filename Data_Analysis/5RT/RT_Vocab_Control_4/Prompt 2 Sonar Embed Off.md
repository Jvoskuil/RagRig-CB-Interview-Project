You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is being recorded for internal process review, not a performance evaluation — I'm interested in how you worked through the situation. Okay to proceed?

Participant: Sure, no problem.

Interviewer: Can you tell me your role and how long you've been in it?

Participant: Division Superintendent, six years in this role, twenty years on the railroad overall, most of it on this same subdivision as a trainmaster and roadmaster before that.

Interviewer: Walk me through what first came to your attention that morning regarding milepost 214.

Participant: Our track inspector called around 7 a.m. He'd run the ultrasonic test on the curve as part of the regular cycle, and it came back at 4 millimeters on an internal transverse defect. That same spot had been logged at 2 millimeters three weeks earlier. He called me directly instead of just filing the report because the jump stood out to him.

Interviewer: What was your objective for the shift once that came in?

Participant: Keep the operation safe, but also be realistic about the schedule. We had Q-119, one of our priority intermodal trains, due through that territory later in the day, and there's a contractual on-time window — past two hours late and we take a penalty. On top of that we had a cold front coming that night, about a 25-degree drop, which matters for rail integrity on continuous welded rail. So I'm weighing the defect information against the operational picture, not just one or the other.

Interviewer: What happened right after the ultrasonic results came in?

Participant: I pulled the defect history for that curve. There'd been small flaws there before, mostly on bolted rail nearby, that had stayed flat and never developed into anything. But what stood out this time wasn't just the 4-millimeter reading, it was the rate — doubling in three weeks is faster than anything in that log. I treated that rate as the key new piece of information. Instead of keeping the standard two-week retest, I moved it to an elevated-monitor status with a one-week retest.

Interviewer: What made you decide the growth rate itself should change the interval?

Participant: Two millimeters isn't much on its own, but the speed of the change is what a static reading doesn't tell you. If it had gone from 2 to 2.5, I'd probably have left the interval alone. Doubling in three weeks felt like something that needed a closer look sooner.

Interviewer: What information did you have at the moment you made that call?

Participant: The two readings, the inspector's comparison to the historical log, the current 60 mile-an-hour track class rating, and his statement that the rate was faster than what we'd typically seen. Nothing pointed to imminent failure, but the trend was enough to justify tightening the interval.

Interviewer: Let's move to later that morning. What led into the next decision?

Participant: The inspector called back to flag that this stretch is continuous welded rail, laid about five years ago, different from most of the bolted-rail spots in our comparison cases. He also mentioned tonnage on that curve is up around 15 percent year over year. Both came up before I made the next call.

Interviewer: How did you weigh those details against what you'd seen in similar cases before?

Participant: I've handled a lot of flaw reports over the years, and my instinct was that this looked like ones that had resolved fine. But the inspector's point about the CWR and tonnage was legitimate — those aren't small distinctions, especially with the cold snap coming. So rather than going with full track speed because it reminded me of past cases, or swinging all the way to a full slow order, I put a targeted, moderate speed restriction on that curve specifically, to hold until the one-week retest.

Interviewer: What alternatives did you rule out there, and why?

Participant: Full track speed leaned too much on pattern-matching without accounting for the differences the inspector raised. A full slow order across the segment felt heavier than the data supported — we didn't have evidence of anything beyond the flagged growth rate. The moderate restriction on just that curve matched the actual risk picture.

Interviewer: Let's go to the afternoon call about Q-119.

Participant: As we got closer to Q-119's window, the chief dispatcher, trainmaster, and road foreman got on a call with me to decide whether to release the train through 214 under the interim restriction, hold it for a reroute, or wait for more data.

Interviewer: What was everyone's position going in?

Participant: The trainmaster had texted beforehand that it was probably fine but he was a little nervous. The road foreman said he was leaning toward releasing it but wouldn't mind a slow order. So there was some caution on the table already.

Interviewer: How did the group's view compare to where people started?

Participant: It didn't move much, honestly. We talked through the restriction already in place, the penalty exposure if we held the train, and the retest timeline, and the road foreman asked partway through whether the restriction we had was enough given the CWR concern. We talked that through for a minute before agreeing to release under the existing restriction rather than removing it. The call ran close to fifteen minutes.

Interviewer: Did anyone push for a more extreme option, either direction?

Participant: Not really. Nobody argued for pulling the restriction, and nobody argued for a full reroute either. We landed close to where people already were.

Interviewer: After Q-119 went through, what happened?

Participant: A following local crew radioed in an unusual sound at the wheel-rail interface near that stretch — no visible damage, nothing measurable. That triggered a debrief before shift change.

Interviewer: Who was in that debrief?

Participant: Myself, the trainmaster, and the chief dispatcher initially. Our assistant engineer from track engineering asked to join to raise concerns about the classification and the speed decision. The meeting was originally set for fifteen minutes before shift change, but the chief dispatcher pushed it back to bring him in once we heard he wanted to weigh in.

Interviewer: What was discussed once he joined?

Participant: We went through the wheel-rail sound — the read was that it was probably unrelated, likely debris or a joint bar, but nobody stated that with certainty. We confirmed we'd keep the interim restriction in place until the retest, and we logged his specific concerns to revisit at that retest rather than closing them out.

Interviewer: Was there any disagreement in the room?

Participant: A bit. He wasn't fully convinced the sound was unrelated, and he wanted the retest moved up further. We didn't move the date, but we agreed to note his concern formally and treat it as open rather than resolved.

Interviewer: What alternatives did you consider in that meeting?

Participant: Closing it out quickly without him, which is basically what almost happened before the schedule got adjusted. Or escalating straight to the chief engineer that same day. We didn't think escalation was warranted yet, but documenting it as open with a defined follow-up felt like the right middle ground.

Interviewer: How much time pressure did you feel across these four moments?

Participant: The release call and the debrief were the tightest, tied to the two-hour window and the shift change. The morning classification had more room — that was mainly me and the inspector working through the numbers.

Interviewer: If the retest interval had stayed at two weeks, would anything about your classification have changed?

Participant: If it had stayed at two weeks, we'd have been relying longer on a single fast-growth data point without a closer check, which is part of why I didn't want to leave it standard.

Interviewer: If the assistant engineer had been on the original conference call, do you think the release decision would have gone differently?

Participant: Maybe the discussion would have taken a bit longer, but I don't think the restriction itself would have changed much, since we'd already built it in based on his earlier input about the CWR and tonnage.

Interviewer: Looking back, anything about the debrief you'd have handled differently given the time constraints?

Participant: I'd have looped him in before the meeting was even scheduled, rather than adjusting on the fly once he asked.

Interviewer: Last one — if this flaw had shown up on a curve you hadn't worked before, would your approach have been different?

Participant: Probably similar, since the restriction came out of the specific data points rather than familiarity with the location. I might have leaned on the inspector's judgment even more, since I wouldn't have my own history with that curve to cross-check against.

Interviewer: That's very helpful, thank you.

Participant: Sure thing.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Vocab_Control_4",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Division Superintendent / Operations Manager",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Milepost 214 Rail Flaw and the Q-119 Release Decision (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A division superintendent manages the same evolving situation as the paired biased scenario: an ultrasonic test flags a growing internal rail flaw on a curve near milepost 214 just as a winter cold front approaches and a high-priority intermodal train (Q-119) is due through the territory. Over several hours, the superintendent interprets updated defect data, decides whether to impose a slow order, consults with a small operations group by conference call about releasing Q-119, and runs a post-incident debrief after a minor wheel-rail anomaly is reported downstream. Unlike the paired scenario, every decision in this version is supported by proportionate evidence-weighting, explicit consideration of contextual differences, a group discussion that converges without amplifying individual positions into an extreme, and a debrief that includes the dissenting engineering voice and revisits open questions. The scenario is designed to match the biased scenario's domain vocabulary, structure, actors, emotional tone, and decision count while containing zero intended instances of any named bias.",
    "occupational_realism": {
      "objective": "Maintain safe train operations across the subdivision while minimizing unnecessary delay to a contractual priority intermodal service during a developing rail-defect and weather situation.",
      "setting": "Division dispatch office and territory covering a 90-mile freight subdivision with a curved, high-tonnage segment near milepost 214, during a forecast overnight temperature drop of 25°F.",
      "constraints": [
        "Only one qualified track inspector available for re-testing before Q-119's scheduled window",
        "Contractual on-time performance penalty if Q-119 is delayed beyond a two-hour window",
        "Falling temperatures increase risk of rail contraction breaks in continuous welded rail (CWR)",
        "Limited extra-board crew availability for a potential reroute",
        "Communication only by phone/radio conference call, no in-person meeting possible before the decision window closes"
      ],
      "stakeholders": [
        "Division Superintendent (interviewee)",
        "Track Inspector",
        "Chief Dispatcher",
        "Trainmaster",
        "Road Foreman of Engines",
        "Assistant Engineer (track engineering)",
        "Intermodal customer service desk"
      ],
      "technical_terms_to_use": [
        "ultrasonic rail flaw detection",
        "continuous welded rail (CWR)",
        "slow order",
        "FRA Track Safety Standards / track class",
        "wheel-rail interface",
        "cold weather rail break risk",
        "extra board crew",
        "priority intermodal train",
        "on-time performance (OTP) metric",
        "defect growth rate"
      ],
      "technical_terms_to_avoid": [
        "conservatism bias",
        "experience bias",
        "group polarization",
        "groupthink",
        "anchoring",
        "cognitive bias",
        "heuristic",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Morning ultrasonic test flags a 4mm internal transverse defect near milepost 214, previously logged at 2mm three weeks earlier",
          "Track is currently classified for 60 mph freight operation",
          "Historical defect log shows this curve has had similar small flaws in the past that stabilized without incident",
          "Overnight low forecast to drop 25°F by evening"
        ],
        "new_information_after_decision": [
          "Track inspector notes the growth rate (2mm to 4mm in three weeks) is faster than the prior flaws referenced in the log",
          "Superintendent reclassifies the defect to an elevated-monitor status and moves the retest interval up to one week rather than the standard two, citing the faster growth rate as the deciding factor"
        ],
        "alternatives": [
          "Retain the standard 'monitor, retest in two weeks' classification per historical pattern",
          "Move to an elevated-monitor status with a shortened one-week retest given the faster growth rate",
          "Request emergency inspection support from an adjoining division"
        ],
        "intended_action": "Superintendent explicitly treats the faster growth rate as new, decision-relevant information and proportionately tightens the retest interval, without over- or under-reacting to the single data point."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track inspector raises concern that this segment is CWR laid five years ago, unlike the bolted-rail segments where most prior 'stabilized' flaws were found",
          "Current tonnage on the curve has increased roughly 15% year-over-year",
          "Superintendent has handled dozens of similar-looking flaw reports over a 20-year career on this subdivision",
          "One-week retest interval from decision point 1 is now in effect"
        ],
        "new_information_after_decision": [
          "Superintendent weighs the recalled past cases against the inspector's stated CWR and tonnage distinctions and concludes the differences are material enough to warrant a temporary, targeted response",
          "Decision is made to impose a modest interim speed restriction for the curve until the one-week retest, rather than either full track speed or a blanket slow order"
        ],
        "alternatives": [
          "Keep full track speed based on similarity to past resolved cases",
          "Impose a full slow order across the segment pending retest",
          "Impose a targeted, moderate interim speed restriction reflecting the CWR/tonnage distinctions while awaiting the retest"
        ],
        "intended_action": "Superintendent uses personal experience as one input among several, explicitly reasons about why the current case differs from prior ones (construction type, tonnage, timing), and selects a proportionate middle option rather than defaulting to the remembered pattern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Dispatcher, Trainmaster, and Road Foreman join a short conference call to decide whether to release Q-119 through milepost 214 under the interim restriction, hold it for a reroute, or seek further data",
          "Individually, each participant has expressed mild caution beforehand: Trainmaster texted 'probably fine but a little nervous,' Road Foreman said 'leaning toward yes but wouldn't mind a slow order'",
          "The customer service desk has flagged the two-hour delay penalty as a live financial consequence"
        ],
        "new_information_after_decision": [
          "During the call, participants raise and weigh the interim restriction already in place, the penalty exposure, and the one-week retest timeline, and the group settles on releasing Q-119 under the existing interim restriction rather than adopting a more extreme position in either direction",
          "The call runs about fifteen minutes and includes at least one explicit question about whether the restriction is sufficient before consensus is reached"
        ],
        "alternatives": [
          "Release Q-119 under the interim restriction already in place",
          "Remove the restriction and release at full track speed",
          "Hold Q-119 for a reroute via the adjoining subdivision"
        ],
        "intended_action": "The group discussion converges on a position that is consistent with, rather than more extreme than, the individual pre-call positions, incorporating the existing interim restriction and explicit verification before reaching consensus."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "After Q-119 passes under the interim restriction, a following local crew reports a minor unusual wheel-rail sound near milepost 214 but no measurable damage",
          "Assistant Engineer, not on the earlier call, requests to join the debrief to raise concerns about the defect classification and speed decision",
          "Debrief meeting is scheduled for 15 minutes before shift change but is extended by the Chief Dispatcher once the Assistant Engineer's request is relayed"
        ],
        "new_information_after_decision": [
          "The debrief group, including the Assistant Engineer, discusses the wheel-rail sound alongside the interim restriction and the upcoming one-week retest, and agrees to keep the restriction in place and confirm the retest date rather than closing the matter outright",
          "Minutes record the Assistant Engineer's concern as logged and scheduled for follow-up at the retest, alongside the provisional read that the sound was likely unrelated"
        ],
        "alternatives": [
          "Close the debrief quickly without including the Assistant Engineer's input",
          "Extend the debrief to include the Assistant Engineer's concerns and confirm the retest and restriction plan, as occurred",
          "Escalate immediately to the chief engineer for an independent review"
        ],
        "intended_action": "The debrief group extends the meeting to incorporate a dissenting perspective, documents open questions rather than declaring closure, and ties the outcome to the already-scheduled retest rather than treating the quick agreement as proof the process was fully resolved."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what first came to your attention that morning regarding milepost 214.",
        "What was your overall objective for the shift once the flaw report came in?"
      ],
      "timeline_reconstruction": [
        "What happened right after the ultrasonic test results came in?",
        "What led up to the conference call about Q-119?",
        "What happened between the call ending and the debrief meeting?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided on the retest interval?",
        "How did you weigh what you'd seen before against what was different about this case?",
        "How did the group's view compare with where people started before the call?",
        "What was discussed in the debrief, and how was the Assistant Engineer's input handled?",
        "What alternatives did you weigh at each of these points, and why did you rule the others out?",
        "How much time pressure did you feel at each of these moments?",
        "How certain were you about the defect's growth rate at the time you made the classification?"
      ],
      "closing_hypotheticals": [
        "If the retest interval had stayed at two weeks instead of one, would anything about your classification have changed?",
        "If the Assistant Engineer had been on the original conference call, do you think the release decision would have gone differently?",
        "Looking back, is there anything about the debrief you'd have wanted to handle differently given the time constraints?",
        "If this same flaw had appeared on a curve you hadn't worked before, would your approach have changed?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "RT_Biased_4",
      "features_to_match": [
        "Domain vocabulary: ultrasonic rail flaw detection, CWR, slow order, track class, wheel-rail interface, cold weather rail break risk, extra board crew, priority intermodal train, OTP metric, defect growth rate",
        "Setting: 90-mile subdivision, milepost 214 curve, overnight 25°F cold snap, Q-119 priority intermodal train",
        "Actors: Division Superintendent (interviewee), Track Inspector, Chief Dispatcher, Trainmaster, Road Foreman, Assistant Engineer, customer service desk",
        "Structure: four decision points in the same chronological order (classification, speed/slow-order decision, group release call, post-incident debrief)",
        "Difficulty: moderate, with genuine competing goals (safety vs. on-time performance vs. cost of delay)",
        "Emotional tone: measured, professional, mild background pressure without dramatization",
        "Decision count: exactly four, matching the paired scenario"
      ],
      "features_to_remove_or_change": [
        "Replace under-adjustment of the initial classification with an explicit, proportionate tightening of the retest interval in response to the new growth-rate evidence",
        "Replace over-reliance on personally recalled cases with an explicit weighing of experience against stated contextual differences (CWR, tonnage) and a proportionate middle-ground action",
        "Replace the group's shift to a more extreme release position with a group discussion that converges on a position consistent with individual pre-call views and includes explicit verification",
        "Replace the debrief's rapid, dissent-excluding closure with an extended debrief that includes the dissenting stakeholder and documents open follow-up items"
      ],
      "ambiguity_boundary": "Not applicable for population of intended bias instances: this is a zero-bias vocabulary control. Genuine domain uncertainty (e.g., whether the wheel-rail sound is related to the flaw) may remain unresolved, but no reasoning pattern should manifest a named bias mechanism."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable: condition is 'vocabulary_control', not 'counterfactual'; no counterfactual variable is instantiated for this generation.",
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives, mirroring the paired scenario's structure.",
      "Zero named-bias instances are intentionally embedded anywhere in the interview.",
      "Domain vocabulary, setting, actors, decision count, and emotional tone match the paired biased scenario (RT_Biased_4).",
      "Each decision point shows evidence-proportionate reasoning: new evidence is weighed and acted on, experience is checked against contextual differences, group discussion does not amplify individual positions, and dissent is incorporated rather than excluded.",
      "Consequences (minor wheel-rail sound, no measurable damage) remain genuinely ambiguous and do not mechanically prove the process was correct or incorrect.",
      "No bias name, definition, or psychological label appears anywhere in the interview.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable via four decision-point narrations plus probes without repetitive exposition.",
      "Technical vocabulary reflects rail operations terminology consistent with a Division Superintendent role, matching the paired scenario's technical_terms_to_use list."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Conservatism Bias", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 1 must show proportionate updating on new growth-rate evidence instead." },
      { "bias": "Experience Bias", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 2 must show experience weighed alongside explicit contextual differences instead." },
      { "bias": "Group Polarization", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 3 must show group convergence consistent with individual pre-call positions instead." },
      { "bias": "Groupthink", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 4 must show inclusion of the dissenting stakeholder and documented open follow-up instead of rapid unanimous closure." }
    ],
    "target_bias_names": ["Conservatism Bias", "Experience Bias", "Group Polarization", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Conservatism Bias", "requested_occurrences": 0 },
      { "bias": "Experience Bias", "requested_occurrences": 0 },
      { "bias": "Group Polarization", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "RT_Biased_4",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Vocab_Control_4",
    "domain_id": "RT",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition requires zero intended occurrences of all named biases across all four decision points. No allocation was performed; instead, each decision point that hosted a target bias mechanism in the paired biased scenario (RT_Biased_4) was redesigned with an evidence-proportionate, non-biased counterpart reasoning pattern occupying the same structural position.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and setting (90-mile subdivision, milepost 214 curve, cold snap)",
      "Actors and their roles",
      "Four-decision-point chronological structure",
      "Technical vocabulary and terminology level",
      "Difficulty level (moderate)",
      "Emotional tone (measured, professional, mild pressure)",
      "Approximate word count and dialogue format"
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
        "segment_type": "objective_and_tradeoff",
        "raw_interview_anchor": "Keep the operation safe, but also be realistic about the schedule. We had Q-119, one of our priority intermodal trains, due through that territory later in the day, and there's a contractual on-time window — past two hours late and we take a penalty. On top of that we had a cold front coming that night, about a 25-degree drop, which matters for rail integrity on continuous welded rail. So I'm weighing the defect information against the operational picture, not just one or the other.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly weighs safety, schedule, and cold-weather context; no distorted weighting is manifested."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "I pulled the defect history for that curve. There'd been small flaws there before, mostly on bolted rail nearby, that had stayed flat and never developed into anything. But what stood out this time wasn't just the 4-millimeter reading, it was the rate — doubling in three weeks is faster than anything in that log. I treated that rate as the key new piece of information. Instead of keeping the standard two-week retest, I moved it to an elevated-monitor status with a one-week retest.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The faster growth is treated as new decision-relevant evidence and leads to proportionate retesting, per the control specification."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_threshold_reasoning",
        "raw_interview_anchor": "Two millimeters isn't much on its own, but the speed of the change is what a static reading doesn't tell you. If it had gone from 2 to 2.5, I'd probably have left the interval alone. Doubling in three weeks felt like something that needed a closer look sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains a rate-based evidentiary threshold, not a bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_weighting",
        "raw_interview_anchor": "The two readings, the inspector's comparison to the historical log, the current 60 mile-an-hour track class rating, and his statement that the rate was faster than what we'd typically seen. Nothing pointed to imminent failure, but the trend was enough to justify tightening the interval.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Absence of imminent-failure evidence is distinguished from a trend that justifies a shorter retest."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "I've handled a lot of flaw reports over the years, and my instinct was that this looked like ones that had resolved fine. But the inspector's point about the CWR and tonnage was legitimate — those aren't small distinctions, especially with the cold snap coming. So rather than going with full track speed because it reminded me of past cases, or swinging all the way to a full slow order, I put a targeted, moderate speed restriction on that curve specifically, to hold until the one-week retest.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Experience is weighed against relevant case differences and does not override them. Candidate cand_001's quotation is valid here, but the complete reasoning negates a manifested experience or representativeness bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "alternative_comparison",
        "raw_interview_anchor": "Full track speed leaned too much on pattern-matching without accounting for the differences the inspector raised. A full slow order across the segment felt heavier than the data supported — we didn't have evidence of anything beyond the flagged growth rate. The moderate restriction on just that curve matched the actual risk picture.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Both extremes are rejected for stated evidentiary reasons; the selected restriction is proportionate."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "group_decision_rationale",
        "raw_interview_anchor": "It didn't move much, honestly. We talked through the restriction already in place, the penalty exposure if we held the train, and the retest timeline, and the road foreman asked partway through whether the restriction we had was enough given the CWR concern. We talked that through for a minute before agreeing to release under the existing restriction rather than removing it. The call ran close to fifteen minutes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The group reviews relevant factors and an explicit concern before reaching a position consistent with initial views. Candidate cand_002 quotes this segment, but stable consensus alone does not show anchoring."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "group_convergence_reflection",
        "raw_interview_anchor": "Not really. Nobody argued for pulling the restriction, and nobody argued for a full reroute either. We landed close to where people already were.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes a non-extreme result consistent with starting positions; no polarization or groupthink is manifested."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "response_to_new_cue",
        "raw_interview_anchor": "A following local crew radioed in an unusual sound at the wheel-rail interface near that stretch — no visible damage, nothing measurable. That triggered a debrief before shift change.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A debrief is initiated in response to an unusual report despite no measurable damage."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "meeting_inclusion_decision",
        "raw_interview_anchor": "Myself, the trainmaster, and the chief dispatcher initially. Our assistant engineer from track engineering asked to join to raise concerns about the classification and the speed decision. The meeting was originally set for fifteen minutes before shift change, but the chief dispatcher pushed it back to bring him in once we heard he wanted to weigh in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The schedule is adjusted to include an engineering voice, rather than excluding dissent."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "debrief_evidence_and_followup",
        "raw_interview_anchor": "We went through the wheel-rail sound — the read was that it was probably unrelated, likely debris or a joint bar, but nobody stated that with certainty. We confirmed we'd keep the interim restriction in place until the retest, and we logged his specific concerns to revisit at that retest rather than closing them out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The attribution remains explicitly uncertain and concerns are recorded for later review."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "dissent_handling",
        "raw_interview_anchor": "A bit. He wasn't fully convinced the sound was unrelated, and he wanted the retest moved up further. We didn't move the date, but we agreed to note his concern formally and treat it as open rather than resolved.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Disagreement is retained as an open issue, not erased by apparent consensus."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "alternative_comparison",
        "raw_interview_anchor": "Closing it out quickly without him, which is basically what almost happened before the schedule got adjusted. Or escalating straight to the chief engineer that same day. We didn't think escalation was warranted yet, but documenting it as open with a defined follow-up felt like the right middle ground.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant compares exclusion and immediate escalation and chooses documented follow-up."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "time_pressure_reflection",
        "raw_interview_anchor": "The release call and the debrief were the tightest, tied to the two-hour window and the shift change. The morning classification had more room — that was mainly me and the inspector working through the numbers.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A descriptive assessment of pressure across decision points; pressure alone is not a bias."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "If it had stayed at two weeks, we'd have been relying longer on a single fast-growth data point without a closer check, which is part of why I didn't want to leave it standard.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains the shorter retest using evidence available at the decision."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "Maybe the discussion would have taken a bit longer, but I don't think the restriction itself would have changed much, since we'd already built it in based on his earlier input about the CWR and tonnage.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The engineer's relevant input had already informed the restriction; the hypothetical does not indicate dissent suppression."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "retrospective_process_reflection",
        "raw_interview_anchor": "I'd have looped him in before the meeting was even scheduled, rather than adjusting on the fly once he asked.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This proposes a process improvement for earlier inclusion."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Probably similar, since the restriction came out of the specific data points rather than familiarity with the location. I might have leaned on the inspector's judgment even more, since I wouldn't have my own history with that curve to cross-check against.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hypothetical prioritizes specific data and inspector judgment over familiarity."
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
      "analysis_scope_note": "Analysis of a single interview transcript concerning a railroad defect-management incident. No retrieved scientific-passage RAG context was supplied, so no corpus-supported bias labels or mechanisms could be applied. Findings were assessed conservatively against widely established cognitive-science definitions from general knowledge."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Representativeness heuristic",
        "alternative_labels": [
          "Pattern-matching heuristic",
          "Representativeness bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Mid-morning decision on interim speed restriction for milepost 214",
        "supporting_interview_quote": "I've handled a lot of flaw reports over the years, and my instinct was that this looked like ones that had resolved fine.",
        "plausible_mechanism": "The participant initially assessed the new defect by its similarity to remembered prior defects, which can overweight resemblance and underweight distinctive base-rate or diagnostic information.",
        "why_not_identified": "The participant explicitly recognized the pattern-matching inclination, incorporated the differentiating CWR and tonnage information, and chose a moderate restriction rather than full track speed. There is no affirmative evidence that the initial similarity judgement materially biased the final decision."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved corpus passages were provided for this analysis, so corpus-supported bias labels or mechanisms could not be applied.",
      "The transcript is a retrospective self-report, so real-time reasoning is only approximated and some bias mechanisms may be hidden or reconstructed.",
      "The participant often described considering and rejecting more biased options; such descriptions alone are insufficient to establish that those mechanisms materially affected a decision."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Vocab_Control_4_Sonar_off",
  "interview_id": "RT_Vocab_Control_4",
  "system_prompt_id": "Sonar",
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
