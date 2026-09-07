You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Biased_3",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
