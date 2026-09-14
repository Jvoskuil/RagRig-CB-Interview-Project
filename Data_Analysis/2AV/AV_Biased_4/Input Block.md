<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay?

Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE.

Interviewer: What was the flight supposed to accomplish, and what was your role exactly?

Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it.

Interviewer: Take me through what actually happened, from the start.

Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing.

Interviewer: And afterward?

Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground.

Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries?

Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.

Interviewer: Did you consider asking for another maintenance look before departure?

Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going.

Interviewer: What would have had to be different on paper for you to hold the flight?

Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than "checked, no fault found," that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.

Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically.

Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.

Interviewer: What alternative did you weigh at that point?

Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting.

Interviewer: How confident were you in that read at the time?

Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.

Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it?

Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either.

Interviewer: How did you grade that?

Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.

Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same?

Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.

Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that?

Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.

Interviewer: Is there anything that would change your mind about that day, looking back?

Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.

Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently?

Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_4",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Check Airman / Type Rating Instructor (TRI/TRE)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "ADIRU Miscompare During Line Check: A Check Airman's Judgment Under Layered Uncertainty",
    "scenario_summary_internal": "A veteran Type Rating Examiner (TRE) conducts a scheduled Line Check/OPC on a senior widebody captain during a revenue flight. A previously logged, self-clearing ADIRU (Air Data Inertial Reference Unit) miscompare fault resurfaces intermittently during climb and cruise, layering real system ambiguity on top of the TRE's evaluative duties. The TRE must decide whether to accept the aircraft at dispatch, how to respond to a transient instrument disagreement flag in climb, how to grade the captain's nonstandard resolution technique in cruise, and how to interpret feedback on his own judgment during post-flight debrief. The incident resolves without an accident, but maintenance later finds an intermittent connector fault, leaving the quality of each judgment call genuinely ambiguous.",
    "occupational_realism": {
      "objective": "Complete a scheduled Line Check / Operator Proficiency Check (OPC) on a type-rated captain while maintaining safe operation of the aircraft, correctly grading crew performance, and responding appropriately to an emergent avionics anomaly.",
      "setting": "Flight deck of a twin-aisle commercial aircraft during a scheduled passenger revenue flight, TRE occupying the observer/jump seat with check-ride authority, captain as Pilot Flying under evaluation, first officer as Pilot Monitoring.",
      "constraints": [
        "Fixed check-ride syllabus with limited time to complete required evaluation items",
        "Dispatch reliability and schedule pressure from operations control",
        "MEL (Minimum Equipment List) sign-off already completed by maintenance before the flight",
        "TRE must both fly/observe and simultaneously grade CRM and technical performance",
        "Limited real-time diagnostic data on an intermittent avionics fault",
        "Passengers and revenue schedule create incentive to avoid unnecessary diversion or turnback"
      ],
      "stakeholders": [
        "Type Rating Examiner (TRE) / Check Airman",
        "Line Captain under evaluation",
        "First Officer (Pilot Monitoring)",
        "Maintenance Control",
        "Operations Control / Dispatch",
        "Fellow Check Airman (peer, post-flight)"
      ],
      "technical_terms_to_use": [
        "ADIRU", "miscompare", "EICAS", "QRH", "MEL", "OPC", "Line Check",
        "CRM", "cross-check", "non-normal checklist", "tech log", "PF/PM",
        "V1", "memory items", "dispatch release"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias", "heuristic", "anchoring", "overconfidence",
        "blind spot", "normalcy bias", "illusion of validity", "expert intuition bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tech log shows two prior flights with ADIRU 2 miscompare messages that self-cleared",
          "Maintenance signed off the aircraft per MEL with no further action required",
          "Aircraft is on schedule with a full passenger load"
        ],
        "new_information_after_decision": [
          "The fault recurs briefly during climb (Phase 2), suggesting it was not fully resolved"
        ],
        "alternatives": [
          "Accept the aircraft as dispatched, relying on the MEL sign-off and the fault's history of self-clearing",
          "Request an additional maintenance inspection or hold the flight pending further troubleshooting before departure"
        ],
        "intended_action": "TRE and captain jointly accept the aircraft as dispatched without requesting further inspection, treating the repeated self-clearing pattern as evidence the fault is inconsequential."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Brief ADIRU disagree flag appears on EICAS during climb through FL250 and clears within about 10 seconds",
          "No corresponding QRH non-normal checklist is triggered by the system",
          "TRE recalls the tech log history from Phase 1"
        ],
        "new_information_after_decision": [
          "In cruise, the disagreement reappears in a more complex form, this time affecting altitude/airspeed cross-check displayed to the crew"
        ],
        "alternatives": [
          "Continue the climb to cruise altitude as planned, judging the flicker as consistent with the known benign pattern",
          "Level off, run the full non-normal checklist, and contact maintenance control or dispatch for guidance before proceeding"
        ],
        "intended_action": "TRE advises continuing the climb, expressing confidence that the transient flag matches the previously observed benign pattern and does not warrant a full non-normal response."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "In cruise, airspeed/altitude indications briefly disagree between the captain's and first officer's displays",
          "The captain, a 20,000+ hour veteran, resolves the disagreement by referencing standby instruments from memory and continuing manual cross-check rather than working the QRH disagreement procedure in its published sequence",
          "First Officer defers to the captain's method without objection"
        ],
        "new_information_after_decision": [
          "The indications stabilize and the remainder of the flight proceeds uneventfully"
        ],
        "alternatives": [
          "Grade the captain's handling as satisfactory based on the captain's seniority and demonstrated calm command of the aircraft, without independently verifying each QRH step was completed in sequence",
          "Pause the evaluation to independently verify against the QRH disagreement procedure step-by-step before assigning a grade, regardless of the captain's experience level"
        ],
        "intended_action": "TRE grades the captain's nonstandard resolution as satisfactory, primarily on the basis of the captain's seniority and composed demeanor, without independently cross-checking the QRH sequence."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flight lands uneventfully; TRE begins writing the check report",
          "A fellow TRE, reviewing the report informally, suggests the sign-off decisions may have been shaped by the crew's history of prior uneventful flights with the same aircraft",
          "TRE has a long personal track record of check rides without a reported incident"
        ],
        "new_information_after_decision": [
          "Maintenance later finds an intermittent connector fault in the ADIRU wiring, requiring component replacement, without confirming whether any specific in-flight judgment was sound or flawed"
        ],
        "alternatives": [
          "Acknowledge that his own judgment could be subject to the same evaluative pressures he screens for in others and revisit the report language accordingly",
          "Dismiss the peer's suggestion, citing his systematic process and experience as evidence that his own judgment is not subject to the same distortions that affect other check airmen"
        ],
        "intended_action": "TRE dismisses the peer's concern, asserting that his structured evaluation process and experience make him personally immune to the kind of bias he is trained to watch for in the pilots he checks."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this flight was supposed to accomplish and your role in it?",
        "What was your initial impression of the aircraft and crew before departure?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you notice at each stage of the flight?",
        "What information did you have in front of you at each point, and where did it come from?",
        "What changed between what you expected and what actually occurred?"
      ],
      "decision_point_probes": [
        "What cues led you to accept/continue/grade the situation the way you did at this point?",
        "What information sources did you rely on, and were there others you could have consulted?",
        "What were you trying to achieve at that moment, and did that goal compete with anything else?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the basis for your decision — what specifically tipped it one way?",
        "Had you seen something like this before, and how did that shape your response?",
        "How much time pressure did you feel, and did that affect how you gathered information?",
        "How confident were you in your read of the situation at the time, versus in hindsight?",
        "If the fault history had been different, or if a different pilot had been flying, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If you had to do this flight again with the same information, what would you do differently, if anything?",
        "If a less experienced captain had made the same call in Phase 3, would you have graded it the same way?",
        "How do you think other check airmen might have handled the same sequence of events?",
        "What would it take to convince you that one of your calls that day was influenced by something other than the facts on hand?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Normalcy Bias",
        "decision_point": 1,
        "mechanism": "Repeated prior instances of a fault self-clearing are used to treat the current, unresolved recurrence as inherently non-threatening, despite no new diagnostic confirmation that the underlying cause has been fixed.",
        "affected_reasoning_operation": "Risk assessment of dispatch acceptance based on fault history",
        "evidence_available_at_time": [
          "Tech log entries showing two prior self-clearing ADIRU miscompares",
          "MEL sign-off from maintenance",
          "Schedule and passenger load pressures"
        ],
        "required_textual_manifestation": "TRE explicitly reasons that because the fault has 'always cleared itself before,' there is no need for further inspection, treating repetition of a benign outcome as proof of continued safety.",
        "plausible_nonbias_interpretation": "Accepting an MEL-cleared aircraft with a documented and dispositioned history is standard, defensible practice consistent with maintenance authority and dispatch procedure.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy bias", "bias", "heuristic"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of validity",
        "decision_point": 2,
        "mechanism": "TRE expresses high confidence that a brief, ambiguous instrument flag matches a known 'benign pattern' and predicts its future behavior, based on a small, self-selected set of past observations rather than validated diagnostic data.",
        "affected_reasoning_operation": "Predictive judgment about fault trajectory used to justify continuing the climb",
        "evidence_available_at_time": [
          "Brief ADIRU disagree flag during climb, cleared in ~10 seconds",
          "No triggered non-normal checklist",
          "TRE's recollection of two prior self-clearing occurrences"
        ],
        "required_textual_manifestation": "TRE states strong personal confidence ('I could tell exactly what this was going to do') in predicting the fault's future behavior from a short pattern, treating a small sample as a reliable signal.",
        "plausible_nonbias_interpretation": "A transient flag with no checklist trigger is a legitimate basis for continuing normal operations pending further developments.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "bias", "overconfidence"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Experience Bias or Trusting expert intuition",
        "decision_point": 3,
        "mechanism": "TRE substitutes the captain's seniority and composed demeanor for independent verification of procedural compliance, grading a nonstandard checklist deviation as satisfactory primarily because an experienced pilot performed it confidently.",
        "affected_reasoning_operation": "Evaluative judgment/grading of crew performance against procedural standard",
        "evidence_available_at_time": [
          "Captain's out-of-sequence handling of the QRH disagreement procedure",
          "Captain's 20,000+ hour experience level",
          "First Officer's silent deference"
        ],
        "required_textual_manifestation": "TRE explains the passing grade largely in terms of the captain's experience and calm command ('a pilot with his hours knows what he's doing') rather than a step-by-step procedural check.",
        "plausible_nonbias_interpretation": "Deferring to a demonstrably skilled captain's judgment under CRM principles can be a reasonable evaluative shortcut when outcomes are satisfactory.",
        "strength": "subtle",
        "do_not_make_explicit": ["expert intuition bias", "experience bias", "bias"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "decision_point": 4,
        "mechanism": "When a peer raises the possibility that the TRE's own judgments were shaped by the crew's flight history, the TRE dismisses the concern by citing his systematic process and experience as proof that he personally is not subject to the distortions he is trained to detect in others.",
        "affected_reasoning_operation": "Self-assessment of one's own evaluative objectivity in response to external feedback",
        "evidence_available_at_time": [
          "Peer TRE's informal suggestion about possible influence from prior uneventful flights",
          "TRE's personal track record of incident-free check rides",
          "TRE's stated systematic evaluation process"
        ],
        "required_textual_manifestation": "TRE responds to the peer's suggestion by asserting that his process and experience make his own judgment reliable, while readily acknowledging that other, less experienced check airmen could be susceptible to such influences.",
        "plausible_nonbias_interpretation": "A confident, experienced evaluator defending a documented process against an unsubstantiated critique is a normal professional response.",
        "strength": "moderate",
        "do_not_make_explicit": ["bias blind spot", "bias", "self-awareness"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable; no counterfactual condition requested for this generation.",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, one per requested bias instance",
      "Each decision point offers at least two plausible alternatives",
      "Each bias instance is tied to a distinct evidence trace and reasoning operation, not a repeated restatement",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative",
      "Consequences (successful landing, later maintenance finding) do not confirm or refute whether any single decision was biased",
      "Target word count 1,215-1,485 words achievable given 4 timeline phases plus probe responses without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dismissal of a peer's specific critique of the TRE's own judgment, contrasted with willingness to attribute similar susceptibility to other check airmen."
      },
      {
        "bias": "Normalcy Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispatch-acceptance reasoning based on prior self-clearing fault history rather than new diagnostic confirmation."
      },
      {
        "bias": "Experience Bias or Trusting expert intuition",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as grading a nonstandard procedural deviation as satisfactory primarily on the basis of the performer's seniority/experience rather than independent verification."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as stated high confidence in predicting fault behavior from a small, self-selected pattern of past observations."
      }
    ],
    "target_bias_names": [
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of validity"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bias Blind Spot", "requested_occurrences": 1 },
      { "bias": "Normalcy Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 1 },
      { "bias": "Illusion of validity", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias" },
      { "instance_id": "cb_02", "bias": "Illusion of validity" },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition" },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of validity", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Normalcy Bias",
        "mechanism": "Treats repeated self-clearing of an ADIRU fault as proof of continued safety absent new diagnostic confirmation, used to justify accepting the aircraft at dispatch.",
        "affected_reasoning_operation": "Risk assessment / dispatch-acceptance judgment",
        "evidence_source": "Tech log history of two prior self-clearing occurrences plus MEL sign-off",
        "distinctiveness_requirement": "Must be tied specifically to the pre-departure dispatch decision, not to the in-flight fault recurrence in cb_02."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of validity",
        "mechanism": "Expresses unwarranted confidence in predicting the fault's future behavior from a brief, small-sample pattern rather than validated diagnostic data.",
        "affected_reasoning_operation": "Predictive judgment about fault trajectory to justify continuing climb",
        "evidence_source": "Transient EICAS ADIRU disagree flag during climb, no checklist trigger",
        "distinctiveness_requirement": "Must center on predictive confidence in a specific in-flight moment, distinct from the dispatch-history reasoning in cb_01 and the evaluative grading in cb_03."
      },
      {
        "instance_id": "cb_03",
        "bias": "Experience Bias or Trusting expert intuition",
        "mechanism": "Substitutes captain's seniority/demeanor for independent procedural verification when grading a nonstandard checklist deviation.",
        "affected_reasoning_operation": "Evaluative grading of crew performance against procedural standard",
        "evidence_source": "Captain's out-of-sequence QRH handling and stated experience level",
        "distinctiveness_requirement": "Must be an evaluative/grading act tied to the captain's actions, distinct from the TRE's own predictive or self-assessment reasoning in cb_02 and cb_04."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "mechanism": "Dismisses a peer's specific critique of the TRE's own judgment while affirming that other check airmen could be susceptible to the same influence.",
        "affected_reasoning_operation": "Self-assessment of personal evaluative objectivity in response to external feedback",
        "evidence_source": "Peer TRE's informal comment during report writing plus TRE's stated track record",
        "distinctiveness_requirement": "Must be a post-flight self-referential reflection, distinct from the in-flight operational judgments in cb_01-cb_03."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of validity", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_4",
    "domain_id": "AV",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per named bias assigned to a distinct decision point (DP1-Normalcy Bias, DP2-Illusion of validity, DP3-Experience Bias, DP4-Bias Blind Spot), chosen for mechanism fit: dispatch-history reasoning at DP1, in-flight predictive confidence at DP2, evaluative grading of another's action at DP3, and post-flight self-referential reflection at DP4. No bias shares a decision point with another occurrence of itself, satisfying spread and distinctiveness rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
        "segment_type": "pre_departure_dispatch_reasoning",
        "raw_interview_anchor": "Two prior flights, same fault, both cleared themselves... My read was, this is a known quantity... So there wasn't a strong pull toward digging further.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant treats repeated self-clearing fault history and MEL disposition as evidence that further inspection is unnecessary for dispatch."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "in_flight_predictive_reasoning",
        "raw_interview_anchor": "My first thought honestly was, there it is again, exactly like the tech log said... keep the climb going... at the time it felt like a clear pattern rather than a limited sample.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The participant predicts benign future fault behavior with high confidence from a brief, small-sample pattern."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "performance_evaluation_reasoning",
        "raw_interview_anchor": "I weighted his extensive time on type... more heavily than a step-by-step review of the QRH sequence... With him, the track record does a lot of the work.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The participant grades the captain more favorably because of seniority and track record instead of independently verifying procedural compliance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_flight_self_assessment",
        "raw_interview_anchor": "I told him I didn't think that applied to me... that kind of thing is more of a risk for someone earlier in their check-airman career... For me, I trust the process I've built.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "The participant dismisses a peer's critique of his own judgment while attributing similar susceptibility to less experienced evaluators."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "retrospective_outcome_reasoning",
        "raw_interview_anchor": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything... none of this proves anything one way or the other about the calls I made.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive retrospective reflection, but outcome bias is not part of the exhaustive hidden manifest."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "closing_counterfactual_reasoning",
        "raw_interview_anchor": "Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains what he would change under the same information; no additional hidden instance is manifested."
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
    "analysis_scope_note": "No retrieved scientific-paper passages were supplied. All labels and mechanisms are assigned from general cognitive-science knowledge and grounded in the interview evidence only."
  },
  "identified_bias_summary": [
    {
      "bias_label": "bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["sample-size neglect", "belief in the law of small numbers"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability or future behavior of an outcome by how representative it seems of a small, observed pattern rather than by using sample-size and base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure review of ADIRU write-up history",
      "decision_point_description": "Deciding whether to request additional maintenance inquiry before accepting the aircraft.",
      "affected_reasoning_operation": "Probabilistic inference about the future behavior of an intermittent fault from limited historical evidence",
      "bias_specific_mechanism": "The participant treated two self-cleared prior write-ups as a stable, representative pattern and inferred that the fault was a known, non-escalating quantity, even though the sample was too small to support that inference.",
      "manifestation_in_interview": "He described the fault history as a 'known quantity' and 'the history itself felt like the justification for going,' then later acknowledged that three brief occurrences were too few to know what an intermittent wiring fault would do next.",
      "effect_on_reasoning_or_decision": "Reduced the perceived need for further pre-departure maintenance investigation and made departure feel justified because the limited historical sample appeared to form a consistent pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening.",
          "evidence_explanation": "Shows that two prior self-clearing events were treated as a stable behavioral profile of the fault rather than as a limited sample."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.",
          "evidence_explanation": "Demonstrates that the recurrence pattern was used to infer low risk, which is the core representativeness inference from a small sample."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "Explicitly contrasts the inference he made at the time with the limited-sample problem, which is the precise mechanism behind representativeness-based generalization."
        }
      ],
      "correction_or_counterevidence": "He considered requesting another maintenance look and said a hard fault or specific maintenance flag would have changed his decision; later in the interview he acknowledged that the sample was limited.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or strengthen one's existing beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Climb-time ADIRU disagree indication",
      "decision_point_description": "Deciding whether to continue climb or level off and run the full non-normal procedure.",
      "affected_reasoning_operation": "Interpretation of new ambiguous safety information under uncertainty",
      "bias_specific_mechanism": "When a new ADIRU disagree flag appeared during climb, the participant immediately categorized it as another instance of the already-known benign pattern and used that classification to dismiss the alternative of pausing and running the non-normal procedure as overreaction.",
      "manifestation_in_interview": "He stated that his first thought was 'there it is again, exactly like the tech log said,' instructed the captain to keep the climb going, and described the alternative safety action as overreacting.",
      "effect_on_reasoning_or_decision": "The new fault evidence was interpreted as confirmatory rather than as potentially disconfirming; this led to the operational decision to continue climb without running the full non-normal procedure.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears.",
          "evidence_explanation": "This shows immediate assimilation of new ambiguous evidence into the prior benign pattern, rather than treating it as independent evidence requiring renewed evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "The prior belief was treated as decisive for a safety-relevant operational decision, which is the key effect of confirmation-bias reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "pausing the climb over a ten-second flicker felt like overreacting.",
          "evidence_explanation": "The alternative safety action was dismissed as disproportionate, showing that the confirmatory interpretation suppressed serious consideration of a competing hypothesis."
        }
      ],
      "correction_or_counterevidence": "He did consider leveling off and running the non-normal procedure, and the system did not auto-trigger a checklist. Later he acknowledged that the underlying inference was based on limited evidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": ["halo error", "experience halo"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a global positive impression of a person to influence judgments about their specific attributes or behaviors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Cruise evaluation of captain's response to instrument disagreement",
      "decision_point_description": "Assigning a grade to the captain's non-normal handling after a QRH-order deviation.",
      "affected_reasoning_operation": "Performance evaluation of a specific technical procedure",
      "bias_specific_mechanism": "The evaluator's positive global impression of the captain's extensive experience and calm demeanor spilled over into the evaluation of a specific checklist-compliance deviation; he explicitly weighted seniority and track record over the missed step-by-step QRH sequence.",
      "manifestation_in_interview": "The captain did not reach for the QRH procedure in order, but the participant graded the handling satisfactory. He said the captain's experience and calmness 'tells you something' and admitted he would not grade a first-year captain the same way.",
      "effect_on_reasoning_or_decision": "The specific procedural deviation was graded leniently because of the captain's general experience and track record, producing differential grading based on seniority rather than the observed behavior alone.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved.",
          "evidence_explanation": "Establishes the specific procedural deviation that should have been the focus of the technical evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward.",
          "evidence_explanation": "Shows that a global impression of the captain's seniority and calmness was allowed to outweigh the specific checklist-sequencing deficiency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "Directly demonstrates differential grading based on the captain's seniority and track record, which is the hallmark halo-effect influence."
        }
      ],
      "correction_or_counterevidence": "The participant could point to the captain's real-time standby cross-check, calm CRM, and the first officer's lack of objection as legitimate evidence in favor of the grade; however, the explicit differential grading by first-year captain remains direct evidence of a halo effect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bias blind spot",
      "alternative_labels": ["blind spot bias", "asymmetric bias awareness"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in other people more readily than in oneself.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-flight peer conversation about potential bias",
      "decision_point_description": "Deciding whether to accept or reject a colleague's suggestion that the crew's clean history may have shaped the check-ride calls.",
      "affected_reasoning_operation": "Self-assessment of personal susceptibility to cognitive bias",
      "bias_specific_mechanism": "The participant recognized the general risk of history-based bias in less experienced check airmen but exempted himself, citing his structured process and long record without incidents as evidence that the bias did not apply to him.",
      "manifestation_in_interview": "He rejected his colleague's challenge, saying he did not think the bias applied to him, and projected the risk onto less experienced check airmen instead.",
      "effect_on_reasoning_or_decision": "The participant dismissed peer feedback and maintained confidence that his own evaluations were objective, reducing the likelihood of correcting the earlier biased judgments.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me.",
          "evidence_explanation": "Directly denies personal susceptibility to the bias raised by the colleague."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I've got a structured process I follow on every check, and a long run of check rides without an incident.",
          "evidence_explanation": "Uses a formal process and a clean personal record as evidence of objectivity, which is a common justification in bias blind spot reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "Projects the vulnerability onto others while exempting himself, illustrating asymmetric bias awareness."
        }
      ],
      "correction_or_counterevidence": "Earlier in the interview he acknowledged the sample-size limitation in hindsight, suggesting some capacity for reflection; however, during this specific peer-feedback exchange he did not correct or reconsider his claim of personal immunity.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so corpus evidence arrays are empty and labels rely on general cognitive-science knowledge.",
    "Some decision points involve operational constraints, such as MEL disposition and lack of an automatic checklist trigger, which could also support non-bias explanations; findings are limited to bias-specific interpretive mechanisms evidenced in the participant's own statements."
  ]
}
</RAG_ANALYSIS_OUTPUT>
