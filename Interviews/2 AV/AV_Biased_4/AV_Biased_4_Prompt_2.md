You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{ "scenario_id": "AV_Biased_4",
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
