You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a review of decision-making processes during watch operations, not for any disciplinary purpose. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me a bit about your role and what you were responsible for monitoring that evening?

Participant: Sure. I was on console for the approach channel, so my job was traffic separation through the narrows — sequencing inbound and outbound vessels, keeping an eye on anything that didn't fit the normal pattern, and coordinating with pilots on larger transits. That evening we had a crude tanker inbound under pilotage, and it was right around dusk, so visibility was starting to get patchy with some fog banks rolling through. My main objective was just making sure the tanker had a clean run through the bend within its tidal window, since that channel doesn't give you much room to maneuver once you're committed.

Interviewer: Okay. Walk me through what happened, from when things started to become unusual.

Participant: About forty minutes before the tanker was due at the bend, I picked up a small contact near there — slow track, kind of wandering. AIS class B tagged it as a local fishing vessel, one that's licensed to work that area, so my first read was that it was probably setting or hauling gear. That's a pretty common sight in that spot, especially in the evening. The radar was showing some inconsistent course data on it, near-zero speed at some points, but with the sea state kicking up a bit of clutter, small-target tracking isn't always clean, so I didn't put much weight on that at first. No distress call, nothing on the radio suggesting trouble, so I logged it as routine and kept my main attention on the tanker's progress.

Interviewer: What happened after that?

Participant: About ten minutes later I noticed the track had drifted a bit further toward the centerline than I'd expect from a boat working gear in that area, and there was a short burst on the radio from around that frequency, but it was garbled — couldn't make out any content. Around then my shift supervisor came on for handover and looked at the display with me. He'd worked that stretch for years and said straight off that this looked typical for that vessel, that he'd seen this exact drift pattern before with boats working that bend. My colleague on the next console glanced over and mentioned the track looked a little off to her, but didn't push it further, and we moved on with finishing the handover log. Then, as the tanker got closer to the tidal cutoff, the supervisor turned to me and framed it as, essentially, are we going to lose the tide window over this or not. I proceeded with the transit as scheduled. Afterward, once the tanker had cleared and things settled, we found the fishing vessel was completely stationary and not answering hails, so I put out a general advisory. Turned out later it had a fouled propeller and needed a tow.

Interviewer: Let's reconstruct that a bit more carefully. Starting with your very first read on the contact — what specific cues led you to call it routine fishing activity?

Participant: Mainly the AIS tag. It came up as a class B unit registered to a fishing vessel we see in that area fairly often, so that matched what I'd expect to see there at that hour. I did notice the COG data wasn't fully consistent with active maneuvering, but I chalked that up to the clutter — that channel gets noisy on radar with any chop, and small targets bounce around in the plot all the time.

Interviewer: Did you go back and check the COG pattern again once you'd made that initial call?

Participant: Not specifically, no. Once I had a plausible explanation for it, my attention went back to the tanker's progress, since that was the higher-priority track at that point.

Interviewer: What alternatives did you consider at that moment?

Participant: I could have hailed the vessel directly on VHF to check status, or just flagged it for tighter radar tracking without contacting them. I didn't do either right away — with no distress call and the AIS type matching, it didn't seem urgent enough to prioritize over the tanker sequencing.

Interviewer: Moving to the handover — tell me more about that conversation with your supervisor and colleague.

Participant: He came on, looked at the plot, and said it looked like the same pattern he'd seen from that boat before — kind of a lazy drift while gear's out. He said it with a lot of confidence, and honestly that matched my own initial read too, so it didn't feel like there was much to question. My colleague said something like "that track looks a little odd" but didn't really elaborate, and nobody asked her to say more. We closed out the handover log with a "no action required" note on that contact.

Interviewer: Did anyone suggest getting an independent re-plot or double-checking the radar data before finalizing that note?

Participant: No, not really. It felt like a fairly settled read at that point, given his experience with that specific vessel.

Interviewer: When the tanker was about fifteen minutes from the bend, how did the decision to proceed take shape?

Participant: That's when my supervisor turned it into a scheduling question — asked whether holding for this would cost us the tide window. Once he framed it that way, the conversation was mostly about whether the delay was worth it, since missing that window would push the tanker's transit back a full cycle. Holding to confirm the fishing vessel's status would almost certainly have meant losing the window.

Interviewer: Was there a point where you weighed the safety margin on its own, separate from the schedule question?

Participant: I think I mostly folded it into the same conversation — the tide window was the thing driving the urgency, so that's the lens I was looking at it through. In hindsight I can see how that shaped which options felt realistic.

Interviewer: What alternatives were on the table there?

Participant: Holding the tanker outside the channel, advising the pilot to slow down and open up the CPA a bit while still proceeding, or just going ahead as scheduled. I went with proceeding as scheduled, given the tide constraint.

Interviewer: And the final decision, after the tanker had cleared and the fishing vessel was found stationary and not responding — how did you land on issuing the advisory?

Participant: At that point the immediate encounter was already resolved, but there was another inbound vessel due within the hour, so I weighed that residual risk against the fact that the current situation had cleared without incident. I decided the advisory was worth it given the upcoming traffic, even though nothing bad had actually happened yet.

Interviewer: How much time pressure did you feel across these decisions?

Participant: The tide window created real pressure during that middle stretch. The final advisory call felt calmer, more like a standard judgment call with time to think it through.

Interviewer: If you'd gotten a clean, confirmed COG reading right at the start, would anything have changed?

Participant: Probably — if it had clearly shown no active movement at all, I likely would've tried to raise them on the radio much earlier instead of letting it ride.

Interviewer: Looking back, if your colleague had pushed harder on that "looks odd" comment, do you think it would have changed the outcome?

Participant: Possibly. If she'd said more specifically what she was seeing, it might have prompted another look at the plot before we closed the handover.

Interviewer: And if the tide-window question had been framed differently — say, purely as a safety check rather than a scheduling one — do you think you'd have weighed the options differently?

Participant: That's a fair point. I might have leaned more toward slowing the pilot down or holding briefly, if the conversation had started from the risk side rather than the schedule side.

Interviewer: Anything you'd want to do differently if this came up again?

Participant: I'd probably push for a direct radio check earlier, before letting an initial read sit unchallenged for too long.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_3",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Vessel Traffic Service (VTS) Operator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Erratic Contact in the Narrows: A Fishing Vessel Anomaly During Tanker Transit",
    "scenario_summary_internal": "During a moderate-traffic evening watch in a narrow, current-affected approach channel, a VTS operator monitors an inbound crude tanker under pilotage while a small fishing vessel exhibits an irregular track near a channel bend. The operator must interpret ambiguous sensor data, coordinate with a shift supervisor and colleague in the ops room, decide how to sequence the tanker relative to the anomalous contact, and ultimately issue (or withhold) a traffic advisory. The incident resolves without collision, but the fishing vessel is later found adrift with a fouled propeller, and the tanker experiences a minor schedule delay it could plausibly have avoided with an earlier query. Nothing in the outcome definitively proves any decision was biased; the interview must be reconstructable as either sound judgment under uncertainty or bias-influenced reasoning, since only the interior evidence trail (not the outcome) can distinguish these.",
    "occupational_realism": {
      "objective": "Maintain safe separation and orderly sequencing of vessel traffic through a narrow channel while correctly classifying and responding to an unidentified anomalous contact.",
      "setting": "A regional VTS center overlooking a narrow tidal channel and port approach, moderate visibility with patchy fog banks, dusk transition, radar/AIS fused display, two operators and one shift supervisor on duty.",
      "constraints": [
        "Fixed channel width limiting overtaking or side-by-side passage",
        "Tidal current window constraining the tanker's safe transit time",
        "Radar clutter from sea state degrading small-target tracking",
        "AIS class B unit on the fishing vessel with intermittent reporting",
        "Limited VHF bandwidth shared across multiple concurrent traffic calls",
        "Shift handover occurring roughly midway through the incident"
      ],
      "stakeholders": [
        "VTS Operator (primary interviewee)",
        "Shift Supervisor",
        "Second VTS Operator (colleague on adjacent console)",
        "Harbor Pilot aboard the inbound tanker",
        "Master of the fishing vessel",
        "Port Authority duty manager (informed after the fact)"
      ],
      "technical_terms_to_use": [
        "COG/SOG",
        "closest point of approach (CPA)",
        "traffic separation scheme",
        "AIS class B",
        "radar clutter",
        "pilotage",
        "traffic advisory",
        "channel transit window",
        "fouled propeller",
        "shift handover log"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "groupthink",
        "framing effect",
        "cognitive bias",
        "heuristic",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fishing vessel contact appears near the channel bend with a slow, wandering track",
          "AIS class B tag identifies it as a licensed local fishing vessel",
          "Radar COG data intermittently shows near-zero or inconsistent course, inconsistent with active fishing maneuvering",
          "No distress call received",
          "Inbound tanker is 40 minutes from the bend, within its tidal transit window"
        ],
        "new_information_after_decision": [
          "Ten minutes later the fishing vessel's track shows continued drift toward the channel centerline",
          "A brief, unreadable VHF transmission is logged from the vessel's frequency"
        ],
        "alternatives": [
          "Log the contact as routine fishing activity and continue standard monitoring",
          "Attempt a direct VHF call to the fishing vessel to verify status",
          "Flag the contact for closer radar tracking without immediate outreach"
        ],
        "intended_action": "Operator classifies the contact as routine fishing behavior based on the AIS vessel-type tag, without reconciling the anomalous COG/SOG pattern."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shift supervisor joins the console during handover and reviews the display",
          "Supervisor states confidently that this pattern is 'typical for that vessel, seen it before'",
          "Second operator briefly notes the drift trend but does not elaborate",
          "Tanker's pilot has not yet been informed of any anomaly"
        ],
        "new_information_after_decision": [
          "Handover log is completed with the contact marked 'no action required'",
          "The fishing vessel's track continues drifting closer to the tanker's projected transit line"
        ],
        "alternatives": [
          "Second operator raises the inconsistent COG data explicitly for team discussion",
          "Supervisor requests an independent radar re-plot before closing the handover note",
          "Team defers to the supervisor's initial read and finalizes the handover as-is"
        ],
        "intended_action": "The team adopts the supervisor's initial assessment without independently re-examining the conflicting radar trend; the second operator's noted concern is not pursued further."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tanker is now 15 minutes from the bend and approaching the tidal cutoff for safe transit",
          "Supervisor frames the emerging question to the operator as 'will this cost us the tide window or not', emphasizing schedule impact",
          "The fishing vessel remains uncontacted and continues its slow drift",
          "Rerouting the tanker to hold outside the channel would likely miss the tidal window by at least one cycle"
        ],
        "new_information_after_decision": [
          "The tanker proceeds into the bend as scheduled",
          "The fishing vessel's CPA with the tanker narrows to a smaller-than-typical margin before both vessels clear each other"
        ],
        "alternatives": [
          "Hold the tanker outside the channel until the fishing vessel's status is confirmed",
          "Advise the pilot to reduce speed and increase CPA margin while proceeding",
          "Proceed with the transit as originally scheduled without modification"
        ],
        "intended_action": "Operator weighs the decision primarily around whether delaying the tanker is worth the schedule cost, framed by the supervisor's question, rather than independently re-evaluating the safety margin as the primary criterion."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tanker has cleared the bend without incident",
          "Fishing vessel is now stationary and unresponsive to two VHF hailing attempts",
          "Weather and current conditions are stable",
          "A second inbound vessel is approaching the same channel section within the hour"
        ],
        "new_information_after_decision": [
          "A general traffic advisory is broadcast noting a stationary vessel in the channel",
          "The fishing vessel is later confirmed to have a fouled propeller and is taken under tow"
        ],
        "alternatives": [
          "Issue a formal traffic advisory to all inbound/outbound vessels about the stationary contact",
          "Continue monitoring without a formal advisory since the immediate transit has cleared",
          "Request an inshore patrol vessel be dispatched immediately"
        ],
        "intended_action": "Operator issues a traffic advisory after weighing the residual risk to the next inbound vessel against the now-resolved immediate encounter; this decision point is designed as a neutral judgment call with genuine, defensible trade-offs and no intended bias instance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were monitoring at the start of this watch?",
        "What was your overall objective for the channel during this period?"
      ],
      "timeline_reconstruction": [
        "What did you see on the display when you first noticed the fishing vessel?",
        "Talk me through what happened after the shift supervisor arrived.",
        "What was communicated during the handover discussion?",
        "How did the situation change as the tanker approached the bend?",
        "What happened after the tanker cleared the bend?"
      ],
      "decision_point_probes": [
        "What specific cues led you to classify the contact the way you did at that point?",
        "What information sources did you check, and which ones did you not check or revisit?",
        "What were your goals at that moment, and did any of them compete with each other?",
        "What alternative actions did you consider, and why did you rule them out?",
        "What was the main basis for your final call at each of these points?",
        "Had you seen a similar pattern before, and did that experience shape your read of the situation?",
        "How much time pressure did you feel at each of these moments?",
        "How confident were you in your assessment, and what uncertainty remained?",
        "If you had gotten a clearer radar or AIS signal at that moment, would your decision have changed?"
      ],
      "closing_hypotheticals": [
        "If the second operator had spoken up more directly about the drift pattern, do you think the outcome would have changed?",
        "If the supervisor had framed the tanker question differently, would you have weighed the options differently?",
        "Looking back, is there a point where you'd want additional information before deciding again?",
        "What would you do differently if this situation happened again next week?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "Operator forms an early hypothesis ('routine fishing activity') from the AIS vessel-type tag and then selectively treats that single data point as sufficient, while the conflicting COG/SOG radar trend is noted but not pursued or reconciled.",
        "affected_reasoning_operation": "Evidence selection and weighting during initial contact classification",
        "evidence_available_at_time": [
          "AIS class B tag identifying vessel type as fishing vessel",
          "Radar COG/SOG data intermittently inconsistent with active fishing movement",
          "No distress signal received"
        ],
        "required_textual_manifestation": "The operator should describe checking/citing the AIS tag as the reason for classification, and should mention noticing the odd COG/SOG pattern but explain it away or set it aside without independent verification, rather than describing a deliberate, reasoned decision to defer verification due to workload or protocol.",
        "plausible_nonbias_interpretation": "Reasonable operators commonly deprioritize ambiguous small-target tracks when higher-priority tanker traffic demands attention; this alone would be a justified heuristic if the operator can articulate a resource-tradeoff rationale rather than an evidentiary dismissal.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "confirmation bias",
          "selective evidence weighting",
          "hypothesis-first reasoning"
        ]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "The supervisor's confidently stated prior assessment is adopted by the team without independent re-examination; the second operator's tentative observation of the drift trend is voiced but not pressed, and no one requests a re-plot before finalizing the handover.",
        "affected_reasoning_operation": "Team-level consensus formation and suppression of dissenting evidence during handover",
        "evidence_available_at_time": [
          "Supervisor's verbal assessment based on past experience with the vessel",
          "Second operator's brief mention of the drift trend",
          "Uncontested handover log entry marking 'no action required'"
        ],
        "required_textual_manifestation": "The interviewee should describe the handover conversation in a way that shows the team converging quickly around the supervisor's view, with the second operator's observation being mentioned but not escalated, and no one calling for independent verification, framed as a natural deference to seniority/experience rather than a structured challenge process.",
        "plausible_nonbias_interpretation": "Deferring to a supervisor's greater experience with a specific local vessel is a legitimate expertise-based heuristic if the operator can show the deference was based on a reasoned assessment of the supervisor's track record rather than social pressure to avoid dissent.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "groupthink",
          "consensus pressure",
          "suppressed dissent"
        ]
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "decision_point": 3,
        "mechanism": "The supervisor's question framed the decision primarily around schedule/tidal-window cost ('will this cost us the tide') rather than safety margin, and the operator's subsequent reasoning about alternatives is anchored to that delay-cost frame rather than to an independent safety-first framing.",
        "affected_reasoning_operation": "Option evaluation and trade-off weighting at the reroute-vs-proceed decision",
        "evidence_available_at_time": [
          "Tidal transit window closing in 15 minutes",
          "Supervisor's delay-framed question",
          "Unresolved status of the fishing vessel's drift",
          "Narrowing CPA margin"
        ],
        "required_textual_manifestation": "The interviewee should explain the decision largely in terms of the schedule/tide-window consequences of holding versus proceeding, echoing the supervisor's framing, rather than independently re-stating the decision as a safety-margin question first and a scheduling question second.",
        "plausible_nonbias_interpretation": "Tidal transit windows are a genuine, safety-relevant operational constraint, so weighing schedule impact is legitimate; this would not count as biased if the operator shows the safety margin was assessed on its own terms before schedule considerations were introduced.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "framing effect",
          "anchored framing",
          "reference-point shift"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition specification and no paired control scenario ID was supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "Timing of independent verification of the fishing vessel's status (queried early at decision point 1 vs. deferred until after decision point 3)",
      "original_state": "Verification of the anomalous contact is deferred until after the tanker has already transited the bend",
      "counterfactual_state": "Verification (direct VHF contact or dedicated re-plot) is attempted immediately at decision point 1, before the handover and before the tanker approaches the tidal cutoff",
      "variables_to_hold_constant": [
        "Channel geometry and tidal window",
        "Weather and visibility conditions",
        "Presence and timing of shift handover",
        "Tanker's original schedule and pilotage arrangement",
        "Fishing vessel's actual mechanical failure (fouled propeller)"
      ],
      "expected_causal_difference": "Earlier independent verification would likely surface the inconsistent COG/SOG pattern before the supervisor's framing and the schedule-cost question arise, potentially preventing both the groupthink convergence at decision point 2 and the delay-framed trade-off at decision point 3.",
      "causal_test_question": "Does moving the verification step earlier in the timeline change whether the team converges on an unverified assessment and whether the reroute decision is framed around schedule versus safety?"
    },
    "generation_checks": [
      "Confirm the interview contains exactly one identifiable Confirmation Bias instance tied to decision point 1 and no other confirmation-bias-like moments elsewhere.",
      "Confirm the interview contains exactly one identifiable Groupthink instance tied to decision point 2 and no other groupthink-like moments elsewhere.",
      "Confirm the interview contains exactly one identifiable Framing Bias instance tied to decision point 3 and no other framing-bias-like moments elsewhere.",
      "Confirm decision point 4 contains no intentionally embedded bias instance.",
      "Confirm no bias name, definition, or psychological label appears in interview text.",
      "Confirm word count falls between 1215 and 1485 words.",
      "Confirm exactly four decision points are present with at least two alternatives each.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm the outcome (fouled propeller, minor delay) does not mechanically prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective reliance on the AIS vessel-type tag while dismissing/ignoring the conflicting radar COG/SOG trend at decision point 1 only."
      },
      {
        "bias": "Framing Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as the operator's reasoning being anchored to the supervisor's schedule/tide-window framing rather than an independent safety-margin framing, at decision point 3 only."
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as rapid team convergence on the supervisor's assessment with suppression/non-escalation of the second operator's dissenting observation, at decision point 2 only."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Framing Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Framing Bias", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "fb_01", "bias": "Framing Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 },
      { "instance_id": "fb_01", "bias": "Framing Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective reliance on AIS vessel-type tag as confirming evidence while conflicting radar COG/SOG data is noted but not investigated",
        "affected_reasoning_operation": "Evidence selection and weighting during initial contact classification",
        "evidence_source": "AIS class B tag vs. radar COG/SOG track",
        "distinctiveness_requirement": "Must be the only confirmation-bias-coded moment in the transcript; distinguished from gt_01 and fb_01 by occurring solely within the solo classification act at decision point 1, before any team discussion or framing occurs."
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Rapid team convergence on supervisor's confident prior assessment; dissenting observation from second operator is voiced but not escalated or independently verified",
        "affected_reasoning_operation": "Team-level consensus formation and suppression of dissent during handover",
        "evidence_source": "Supervisor's verbal assessment and second operator's brief drift-trend observation",
        "distinctiveness_requirement": "Must be the only groupthink-coded moment, located specifically in the multi-person handover conversation at decision point 2, distinct from the solo reasoning in cb_01 and the schedule-framed trade-off in fb_01."
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "mechanism": "Operator's evaluation of reroute-vs-proceed alternatives is anchored to the supervisor's delay-cost framing rather than an independently stated safety-margin framing",
        "affected_reasoning_operation": "Option evaluation and trade-off weighting at the reroute decision",
        "evidence_source": "Supervisor's delay-framed question and tidal transit window constraint",
        "distinctiveness_requirement": "Must be the only framing-bias-coded moment, located specifically at the reroute-vs-proceed trade-off in decision point 3, distinct from the earlier classification (cb_01) and the handover consensus (gt_01)."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "fb_01", "bias": "Framing Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Timing of independent verification of the fishing vessel's status",
      "original_state": "Verification deferred until after the tanker transits the bend",
      "changed_state": "Verification attempted immediately at decision point 1",
      "variables_to_hold_constant": [
        "Channel geometry and tidal window",
        "Weather and visibility conditions",
        "Presence and timing of shift handover",
        "Tanker's original schedule and pilotage arrangement",
        "Fishing vessel's actual mechanical failure (fouled propeller)"
      ]
    },
    "scenario_id": "MO_Biased_3",
    "domain_id": "MO",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Automatic allocation: each bias assigned to the single distinct decision point offering the best mechanism fit and narrative realism (Confirmation Bias -> solo initial classification at DP1; Groupthink -> multi-person handover discussion at DP2; Framing Bias -> reroute trade-off evaluation at DP3), with no bias sharing a decision point and DP4 left intentionally neutral.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Channel geometry and tidal window",
      "Weather and visibility conditions",
      "Cast of stakeholders (operator, supervisor, second operator, pilot, fishing vessel master)",
      "Sequence and number of decision points (4)",
      "Outcome facts (fouled propeller, minor tanker delay, no collision)"
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
          "segment_type": "goal_setting",
          "raw_interview_anchor": "My main objective was just making sure the tanker had a clean run through the bend within its tidal window.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive operational goal and constraint, but no manifested cognitive-bias instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Mainly the AIS tag... I did notice the COG data wasn't fully consistent with active maneuvering, but I chalked that up to the clutter.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The participant formed a routine-fishing hypothesis from AIS and discounted conflicting COG/SOG evidence without verification."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "team_decision_reasoning",
          "raw_interview_anchor": "He said it with a lot of confidence... My colleague said something like 'that track looks a little odd' but didn't really elaborate... We closed out the handover log with a 'no action required' note.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "The team adopted the supervisor's assessment without pursuing the colleague's dissent or requesting independent verification."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "That's when my supervisor turned it into a scheduling question... I went with proceeding as scheduled, given the tide constraint.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fb_01"
          ],
          "ground_truth_rationale": "The operator evaluated the unresolved safety issue primarily through the schedule and tidal-window frame."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "post_event_judgment",
          "raw_interview_anchor": "At that point the immediate encounter was already resolved... I decided the advisory was worth it given the upcoming traffic.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a neutral residual-risk judgment with explicit consideration of upcoming traffic and no intended hidden bias instance."
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
    "analysis_scope_note": "Analysis covers the participant's reported decision-making during the watch operation. Third-party statements are available only through the participant's report, and no retrieved corpus passages were supplied."
  },
  "identified_bias_summary": [
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias", "hypothesis confirmation", "premature closure"],
      "taxonomy_status": "established_label",
      "bias_definition": "Confirmation bias is the tendency to search for, interpret, or favor information in ways that confirm an initial expectation or hypothesis, while underweighting or explaining away disconfirming cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial classification of radar/AIS contact as routine fishing activity",
      "decision_point_description": "The moment when inconsistent COG data was noticed and the participant selected a plausible routine-fishing explanation without re-checking the contact.",
      "affected_reasoning_operation": "Cue interpretation and hypothesis evaluation",
      "bias_specific_mechanism": "The AIS class B fishing-vessel tag primed a routine fishing interpretation; subsequent inconsistent COG/radar cues were then assimilated to that plausible schema as clutter/noise and not re-examined.",
      "manifestation_in_interview": "The participant noticed inconsistent course-over-ground data and near-zero speed, but attributed these cues to sea clutter and small-target tracking limitations. After forming a plausible explanation, the participant did not re-check the COG pattern, hail the vessel, or flag it for tighter tracking at that stage.",
      "effect_on_reasoning_or_decision": "The contact was logged as routine and remained low priority; direct VHF hail or tighter radar tracking was delayed until after the tanker cleared and the vessel was later found stationary.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "AIS class B tagged it as a local fishing vessel, one that's licensed to work that area, so my first read was that it was probably setting or hauling gear.",
          "evidence_explanation": "This shows an initial category-based hypothesis about the contact's activity, which becomes the framework for later interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The radar was showing some inconsistent course data on it, near-zero speed at some points, but with the sea state kicking up a bit of clutter, small-target tracking isn't always clean, so I didn't put much weight on that at first.",
          "evidence_explanation": "A potentially disconfirming cue was present but was explained away as clutter/noise, consistent with confirmation-biased interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not specifically, no. Once I had a plausible explanation for it, my attention went back to the tanker's progress, since that was the higher-priority track at that point.",
          "evidence_explanation": "The participant explicitly reports not returning to re-check the inconsistent COG data after adopting a plausible explanation, demonstrating the narrowing effect of confirmation bias."
        }
      ],
      "correction_or_counterevidence": "There were legitimate non-bias factors: the AIS type matched a known local fishing vessel, small-target radar clutter was plausible, no distress call was received, and the tanker was a higher-priority track. These could partly explain the initial interpretation. However, the explicit failure to re-examine the COG after a plausible explanation was formed supports a confirmation mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the input; the label and mechanism rely on general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "authority bias",
      "alternative_labels": ["authority heuristic", "social proof"],
      "taxonomy_status": "established_label",
      "bias_definition": "Authority bias is the tendency to overweight the opinion or judgment of a perceived authority or experienced figure, reducing independent scrutiny and giving less weight to dissenting or uncertain input from others.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handover review and 'no action required' annotation",
      "decision_point_description": "The handover discussion in which the supervisor and colleague offered differing views and the contact was logged as requiring no action.",
      "affected_reasoning_operation": "Social verification and independent re-assessment of contact status",
      "bias_specific_mechanism": "The supervisor's confident experience-based statement that the drift was typical for that vessel was treated as authoritative; the colleague's less detailed concern was not pursued, and no independent re-plot or double-check was requested.",
      "manifestation_in_interview": "During the handover, the supervisor said the pattern looked typical, and the participant reported that the supervisor's confidence, plus his history with the area, made the read feel settled. The colleague's comment that the track looked odd was not elaborated, and the handover log closed with 'no action required.'",
      "effect_on_reasoning_or_decision": "The contact remained de-prioritized and the handover log recorded a no-action decision; the colleague's disagreement did not trigger further verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He said it with a lot of confidence, and honestly that matched my own initial read too, so it didn't feel like there was much to question.",
          "evidence_explanation": "The participant describes confidence and agreement as a reason not to question the supervisor's assessment, consistent with authority-based or social-validation closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My colleague said something like 'that track looks a little odd' but didn't really elaborate, and nobody asked her to say more. We closed out the handover log with a 'no action required' note on that contact.",
          "evidence_explanation": "The dissenting observation was underweighted and not explored, while the group finalized a no-action log entry."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not really. It felt like a fairly settled read at that point, given his experience with that specific vessel.",
          "evidence_explanation": "The participant explicitly anchors the settled judgment to the supervisor's experience, supporting the authority-bias mechanism."
        }
      ],
      "correction_or_counterevidence": "The supervisor's local knowledge and experience were highly relevant and could justify the assessment; the colleague's comment was admittedly vague. This is a competing non-bias explanation for relying on the supervisor. The evidence for authority bias is therefore indirect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the input; the label and mechanism rely on general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": ["framing bias", "reference frame effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Framing effect is the tendency for decisions to change when the same problem is presented or mentally represented with different reference points, such as schedule loss versus safety risk.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision whether to proceed with tanker transit or hold for status check",
      "decision_point_description": "The moment when holding the tanker was reframed as risking the tide window and the participant chose to proceed as scheduled.",
      "affected_reasoning_operation": "Option evaluation and risk-benefit weighing",
      "bias_specific_mechanism": "The supervisor recast the decision as a scheduling/tide-window loss question; the participant then evaluated options mainly through the schedule frame, folding safety verification into whether a delay was acceptable.",
      "manifestation_in_interview": "The participant described the tide window as the lens driving urgency, acknowledged that the framing shaped which options felt realistic, and later indicated that a safety-first framing might have led to slowing or holding.",
      "effect_on_reasoning_or_decision": "The participant selected proceeding as scheduled rather than holding the tanker or advising the pilot to slow and open the CPA, partly because the options were evaluated as delay-versus-schedule rather than purely safety-versus-uncertainty.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That's when my supervisor turned it into a scheduling question — asked whether holding for this would cost us the tide window.",
          "evidence_explanation": "This directly identifies the reframing of the decision around schedule loss rather than safety verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once he framed it that way, the conversation was mostly about whether the delay was worth it, since missing that window would push the tanker's transit back a full cycle.",
          "evidence_explanation": "The participant reports that the frame narrowed the conversation to delay worthiness, a hallmark of framing effects on option evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I mostly folded it into the same conversation — the tide window was the thing driving the urgency, so that's the lens I was looking at it through. In hindsight I can see how that shaped which options felt realistic.",
          "evidence_explanation": "This is an explicit retrospective acknowledgment that the framing influenced the perceived realism of options."
        }
      ],
      "correction_or_counterevidence": "The tide window was an objective operational constraint, and holding could have imposed a full-cycle delay. However, the participant's own account indicates that the schedule frame changed which options felt realistic, which goes beyond the objective constraint and supports a framing-specific effect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the input; the label and mechanism rely on general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so corpus_support_note reflects general cognitive-science knowledge rather than retrieval.",
    "Third-party statements, including the supervisor's and colleague's comments, are available only through the participant's report.",
    "The transcript does not independently verify whether the supervisor's experience-based assessment or the radar interpretation was factually correct."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_3_Sonnet_off",
  "interview_id": "MO_Biased_3",
  "system_prompt_id": "Sonnet",
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
