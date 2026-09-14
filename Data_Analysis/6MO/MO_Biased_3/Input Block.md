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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
