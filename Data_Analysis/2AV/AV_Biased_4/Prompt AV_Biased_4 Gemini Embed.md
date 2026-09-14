You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The transcript was assessed for affirmative, mechanism-grounded evidence of cognitive bias in the participant TRE's pre-departure reasoning, in-flight evaluation, and debrief reflections. Retrieved aviation human-factors passages were used where directly relevant."
  },
  "identified_bias_summary": [
    {
      "bias_label": "bias_blind_spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo_effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation_bias",
      "alternative_labels": [
        "expectation_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms one's existing mental model or hypothesis while discounting contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-departure and climb interpretation of intermittent ADIRU fault",
      "decision_point_description": "Whether to treat the recurring ADIRU flag as benign and continue the climb rather than leveling off, consulting maintenance, or running the full non-normal procedure.",
      "affected_reasoning_operation": "Interpretation of ambiguous fault indications and risk assessment",
      "bias_specific_mechanism": "The participant formed a mental model from two prior self-clearing write-ups that the ADIRU fault was benign and self-contained. When the fault recurred in flight, he interpreted the transient EICAS flag and later display disagreement as confirming that model, used the limited prior history as justification to continue, and downgraded the possibility that an airborne recurrence was disconfirming evidence of an unresolved intermittent fault.",
      "manifestation_in_interview": "The participant describes the pre-departure history as making further inspection unnecessary and then describes the climb flag as 'there it is again, exactly like the tech log said.' Later he states the three brief occurrences felt like a clear pattern rather than a limited sample.",
      "effect_on_reasoning_or_decision": "Reduced vigilance and led to continuing the climb rather than pausing or running the non-normal checklist; the interim interpretation was treated as confirmation of a benign pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.",
          "evidence_explanation": "Shows the formation of a benign prior belief from limited prior events and a reduced inclination to seek disconfirming maintenance evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.",
          "evidence_explanation": "Directly demonstrates assimilation of an ambiguous in-flight fault into the prior benign pattern and a decision to continue based on that interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.",
          "evidence_explanation": "Confirms the confidence arose from subjective pattern perception rather than statistically or diagnostically robust evidence."
        }
      ],
      "correction_or_counterevidence": "Maintenance had previously cleared the aircraft under the MEL, no checklist auto-triggered, and the participant did consider leveling off and consulting maintenance. These are legitimate operational factors and create a partial non-bias explanation. Later maintenance found an intermittent connector fault, but this was unknown at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved aviation-focused paper directly describes confirmation bias in cockpit events as interpretation of available cues as supporting the crew's mental model and ignoring evidence that would contradict the aircraft state.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam OConnor",
          "publication_year": null,
          "retrieved_passage_or_finding": "the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "Confirmation bias operates by using cues consistent with an existing mental model and ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "The participant similarly interpreted the recurring ADIRU fault cues as consistent with his benign mental model and discounted the possibility that the airborne fault was contradictory evidence of an unresolved problem."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo_effect",
      "alternative_labels": [
        "halo_error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A global positive impression of a person influences judgments about specific, unrelated attributes or behaviors.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of captain's handling of in-flight ADIRU disagreement",
      "decision_point_description": "Whether to grade the captain's non-QRH standby-instrument response as satisfactory despite incomplete procedural verification.",
      "affected_reasoning_operation": "Performance evaluation and grading of technical/procedural behavior",
      "bias_specific_mechanism": "The participant's broad favorable impression of the captain's experience and track record generalized to the specific evaluation of procedural compliance. He explicitly weighted the captain's time on type and calm behavior more heavily than a step-by-step verification of the QRH, and stated that the same performance by a junior captain would be graded less generously.",
      "manifestation_in_interview": "The participant graded the captain satisfactory after he bypassed the QRH in favor of standby instruments from memory, saying the captain's track record does a lot of the work and that a first-year captain would not have received the same grade.",
      "effect_on_reasoning_or_decision": "Produced a person-dependent evaluative standard and likely lenient grade for a specific procedural deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either.",
          "evidence_explanation": "Establishes the specific behavioral target: the captain did not follow the QRH procedure in order."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I weighted his extensive time on type and the real-time standby cross-check he ran more heavily than a step-by-step review of the QRH sequence afterward. I didn't go back and verify each item had technically been hit in order.",
          "evidence_explanation": "Shows that the global experience factor outweighed object-level procedural verification in the evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.",
          "evidence_explanation": "Directly demonstrates differential grading based on a global impression of the captain rather than identical performance."
        }
      ],
      "correction_or_counterevidence": "Expert pilots sometimes use memory-based cross-checks efficiently, and the fault resolved; however, the participant's own contrast with a junior captain indicates the standard was influenced by person-level reputation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly validated the halo effect. The classification relies on established general cognitive-science knowledge of the halo effect as an evaluation bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bias_blind_spot",
      "alternative_labels": [
        "bias_blindness"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others while failing to recognize one's own susceptibility to the same or similar biases.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to colleague's debrief feedback",
      "decision_point_description": "Whether to accept or reject the suggestion that his evaluations were shaped by the crew's clean history and his prior beliefs.",
      "affected_reasoning_operation": "Self-assessment of bias susceptibility and integration of peer feedback",
      "bias_specific_mechanism": "In response to peer feedback, the participant exempted himself from cognitive bias by citing his structured process and long record of no incidents, while attributing the same kind of bias risk to less experienced check-airmen. This self-other asymmetry is the defining mechanism of the bias blind spot.",
      "manifestation_in_interview": "He says the suggestion did not apply to him, that such bias is more of a risk for someone earlier in their check-airman career, and that he trusts the process he has built.",
      "effect_on_reasoning_or_decision": "Foreclosed corrective reflection and reduced the likelihood that peer feedback would update his evaluation standard.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.",
          "evidence_explanation": "Directly shows self-exemption from bias and attribution of bias susceptibility to a less experienced group, without engaging with the specific evidence."
        }
      ],
      "correction_or_counterevidence": "A structured process and extensive experience may reduce some errors, but they do not confer immunity; the use of a clean record as proof of objectivity is part of the biased reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly validated the bias blind spot. The classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome_bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retrospective reassessment of the same-day decisions",
      "supporting_interview_quote": "If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.",
      "plausible_mechanism": "The participant's willingness to revise his evaluation appears partly contingent on a severe outcome—complete failure—rather than solely on the quality of the in-the-moment decision process.",
      "why_not_identified": "The participant also states that the ambiguous outcome does not prove the calls were right, so the evidence is mixed and insufficient to establish outcome bias affirmatively."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is self-reported and retrospective, so the analysis relies on the participant's description of his own cognition.",
    "Some retrieved passages concern aviation accident and incident reports rather than check-airman evaluation, so generalization to this evaluation context is indirect.",
    "The corpus provides direct support for confirmation bias, but support for halo effect and bias blind spot is absent and relies on established general cognitive-science knowledge.",
    "The boundaries between confirmation bias, expectation bias, and normalcy/plan-continuation bias overlap; a conservative separation was used to avoid over-counting."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_4_Gemini_on",
  "interview_id": "AV_Biased_4",
  "system_prompt_id": "Gemini",
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
