You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Biased_1",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Rail Traffic Controller / Train Dispatcher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Falcon Bank Nuisance Trip",
    "scenario_summary_internal": "Overnight, a Rail Traffic Controller manages handback of a single-track branch section (Falcon Bank) from engineering possession to traffic. An intermittent track circuit occupancy indication appears shortly after handback. The controller, drawing on a history of nuisance trips on this same circuit caused by rain and leaf-fall, treats the ambiguous indication as resolved/explained rather than genuinely uncertain, and authorizes a freight train into the section without independent verification. Subsequent events (a garbled foreman readback, worsening weather affecting a passenger train's routing, and a recurrence of the anomaly once the freight train is already in the section) force the controller through three further decisions, none of which mechanically prove whether the original call was biased or simply an unlucky but reasonable judgment.",
    "occupational_realism": {
      "objective": "Safely resume normal train working on a single-line branch after an engineering possession, minimizing delay to a following freight and a late-running passenger service while preserving safe separation between trains.",
      "setting": "A regional signalling control center overseeing a rural single-track branch (Falcon Bank block section) during the 23:30-01:00 overnight window, immediately after an engineering gang has handed back possession.",
      "constraints": [
        "Single line section with no parallel track for overtaking or bidirectional running",
        "Only one train may occupy the block section at a time under normal absolute block rules",
        "Worsening rain forecast affecting signal and track circuit reliability",
        "A late-running passenger service (2T19) needs to traverse the same section within the hour",
        "Pilotman working is available but takes 12-15 minutes to arrange and further delays both trains",
        "Trackside telephone confirmation from the gang foreman is the only independent verification method besides pilotman working",
        "Controller is solo on shift with a supervisor reachable only by phone"
      ],
      "stakeholders": [
        "Rail Traffic Controller (interviewee)",
        "Engineering gang foreman (possession handback)",
        "Freight train driver (6M42)",
        "Passenger train driver/guard (2T19)",
        "Signalling maintenance technician (on-call)",
        "Shift supervisor"
      ],
      "technical_terms_to_use": [
        "track circuit",
        "block section",
        "absolute block working",
        "possession handback",
        "single line working",
        "pilotman",
        "trackside telephone",
        "nuisance trip",
        "right of time",
        "signal box/control panel",
        "occupied/clear indication"
      ],
      "technical_terms_to_avoid": [
        "PTC (positive train control, US-specific)",
        "CTC (centralized traffic control, US-specific)",
        "generic 'red light' language without block terminology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineering gang foreman handed back Falcon Bank section as clear at 23:40",
          "Track circuit briefly displayed 'occupied' for approximately 4 seconds, then cleared, twice within 10 minutes",
          "Maintenance log shows three prior nuisance trips on this same circuit over the past 8 months, all attributed to rain ingress or leaf-fall on the rail",
          "Light rain has just begun in the area",
          "Freight 6M42 is standing ready at the section's entry signal awaiting authority to proceed"
        ],
        "alternatives": [
          "Authorize 6M42 to enter under normal absolute block working, treating the flickers as a known nuisance-trip pattern",
          "Call the gang foreman on the trackside telephone to reconfirm the line is physically clear before authorizing any movement",
          "Request the on-call signalling technician to inspect or test the circuit before resuming normal working",
          "Implement single line working with a pilotman as a precaution until the circuit behavior is explained"
        ],
        "intended_action": "Controller classifies the intermittent indication as a familiar nuisance trip based on the maintenance log pattern and authorizes 6M42 into the section without further verification.",
        "new_information_after_decision": [
          "6M42 departs and enters Falcon Bank section under normal working",
          "No further track circuit flicker is observed for several minutes afterward, giving the appearance the call was correct"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "6M42 is now inside the block section",
          "Gang foreman's radio readback confirming all personnel and equipment clear was partially garbled by static, audible words include 'clear' and 'trolley' but the phrase is incomplete",
          "Foreman is not immediately reachable again as the gang has begun moving to their next worksite",
          "No rule violation has occurred yet; possession was formally handed back before the transmission"
        ],
        "alternatives": [
          "Accept the partial readback as sufficient given the formal handback already received",
          "Halt further movements and attempt to re-contact the foreman for a full readback before allowing 2T19 to approach",
          "Escalate to the shift supervisor for a second opinion on whether the partial transmission is adequate"
        ],
        "intended_action": "Controller logs the partial transmission as adequate confirmation and proceeds with normal planning for 2T19's approach, reasoning that the earlier formal handback already covers clearance.",
        "new_information_after_decision": []
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Rain has intensified; a separate signal at the branch junction is reporting intermittent 'signal failure' warnings unrelated to Falcon Bank",
          "2T19 (passenger, running 18 minutes late) is approaching the junction and needs a routing decision within the next few minutes",
          "An alternate loop line adds 6 minutes to 2T19's journey but avoids the affected junction signal entirely",
          "6M42 is still progressing through Falcon Bank with no further anomalies reported"
        ],
        "alternatives": [
          "Route 2T19 via the affected junction signal, relying on backup indication and driver caution",
          "Divert 2T19 via the alternate loop line to avoid the junction signal issue entirely",
          "Hold 2T19 at the previous station until the junction signal issue is diagnosed"
        ],
        "intended_action": "Controller diverts 2T19 via the loop line as a precaution, accepting the schedule delay to avoid relying on the unreliable junction signal.",
        "new_information_after_decision": [
          "2T19 proceeds via the loop with an additional 6-minute delay",
          "Junction signal issue is later found to be a separate, unrelated relay fault"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Falcon Bank track circuit flickers again, this time while 6M42 is confirmed to still be inside the section",
          "The on-call signalling technician, now reached, states the circuit's wiring has a known moisture-sensitivity issue that has not yet been fully diagnosed",
          "6M42's driver reports no visual obstruction and normal progress",
          "2T19 is now close behind on the same route, having rejoined the main line after the loop diversion"
        ],
        "alternatives": [
          "Continue normal working and allow 2T19 to follow 6M42 into Falcon Bank once clear, treating the second flicker as confirmation of the same known nuisance pattern",
          "Suspend normal working and implement single line working with a pilotman for all further movements through Falcon Bank until the fault is properly diagnosed",
          "Hold 2T19 short of the section and request the technician physically inspect the circuit before any further movement"
        ],
        "intended_action": "Controller implements single line working with a pilotman for 2T19 and future movements, while documenting the recurring flicker for the maintenance team.",
        "new_information_after_decision": [
          "Technician later confirms a genuine intermittent short in the track circuit cabling, aggravated by rain, consistent with but not identical to the earlier nuisance-trip pattern",
          "No safety incident occurred, but the fault is flagged for priority repair"
        ]
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what a normal possession handback looks like on a section like Falcon Bank?",
        "What was your overall objective that night, given the freight and the late passenger service?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the handback at 23:40 through to the pilotman working decision.",
        "At what point did you first notice something unusual with the track circuit?",
        "What did you know about this circuit's history before that night?"
      ],
      "decision_point_probes": [
        "At the moment the flicker first appeared, what cues made you interpret it the way you did?",
        "What information sources did you have available, and which ones did you use or not use?",
        "What were you trying to achieve at that moment, and what alternatives did you consider?",
        "What was the basis for choosing to proceed rather than verify independently?",
        "Had you seen this kind of situation before, and how did that experience shape your response?",
        "How much time pressure did you feel you were under when you made that call?",
        "How confident were you that the indication was genuinely a nuisance trip versus something else?",
        "If the maintenance log had shown no prior nuisance trips on this circuit, would you have acted differently?"
      ],
      "closing_hypotheticals": [
        "If you could redo the initial decision with the benefit of hindsight, what would you change?",
        "What would need to be different about the tools or procedures for you to verify ambiguous indications faster?",
        "How do you think other controllers on your team would have handled the same flicker?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "decision_point": 1,
        "mechanism": "Controller encounters a genuinely ambiguous, intermittent signal (4-second occupancy flicker) and, rather than tolerating or investigating the uncertainty, forcibly resolves it into a certain, familiar category (past nuisance trips) that requires no further action, then acts on that resolved certainty without seeking the available independent verification.",
        "affected_reasoning_operation": "Evidence interpretation and decision to seek (or forgo) verification under ambiguity",
        "evidence_available_at_time": [
          "Intermittent 4-second occupied indication occurring twice in 10 minutes",
          "Maintenance log of three prior similar nuisance trips linked to rain/leaf-fall",
          "Onset of light rain at the same time",
          "Availability of trackside telephone confirmation and pilotman working as verification options"
        ],
        "required_textual_manifestation": "The controller's account should explicitly state that the flicker was treated as 'basically explained' or 'not worth chasing further' because of the prior pattern, and should describe skipping the telephone/pilotman verification step specifically because the uncertainty felt already resolved by the pattern-match, not because verification was impossible or procedurally unnecessary.",
        "plausible_nonbias_interpretation": "A controller could reasonably use base-rate pattern-matching from maintenance history as a legitimate operational heuristic under time pressure, especially if verification always takes 12-15 minutes and causes further delay; this alone would not indicate bias unless the account shows the controller treating residual uncertainty as fully eliminated rather than merely reduced.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "Do not name 'uncertainty rejection bias' or any bias term",
          "Do not have the controller say 'I ignored the uncertainty' in clinical/psychological language",
          "Do not have the narrator or interviewer label the reasoning as flawed"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no control scenario requested for this generation pass."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the controller sought independent verification (trackside telephone confirmation) of the intermittent track circuit indication before authorizing 6M42 into Falcon Bank",
      "original_state": "Controller does not seek verification; treats the flicker as an explained nuisance trip and authorizes movement immediately",
      "counterfactual_state": "Controller calls the trackside telephone to reconfirm the gang has fully cleared the section before authorizing movement, delaying 6M42 by several minutes but obtaining direct confirmation",
      "variables_to_hold_constant": [
        "Weather onset and progression",
        "Maintenance log history of the circuit",
        "Timing and content of the garbled foreman readback",
        "Junction signal fault affecting 2T19",
        "Final technician diagnosis of the genuine intermittent short"
      ],
      "expected_causal_difference": "In the counterfactual, the controller's later decisions (partial readback acceptance, loop diversion, final pilotman decision) would likely be made with a documented verification step already on record, altering how the recurring flicker in phase 4 is interpreted (as an escalation of a partly-verified issue rather than a repeat of an unverified assumption), but consequences would remain non-diagnostic of bias absent this manipulation.",
      "causal_test_question": "Does explicitly seeking trackside verification at decision point 1 change how confidently the controller commits to the nuisance-trip interpretation in decision point 4, independent of the eventual outcome?"
    },
    "generation_checks": [
      "Exactly one instance of Uncertainty Rejection Bias is planned, at decision point 1 only",
      "No other decision point contains an intentional instance of the named bias",
      "Decision points 2 and 3 use different reasoning failures (partial-information acceptance, precautionary diversion) that must not be coded as instances of the named bias",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given four decision points with probes and one embedded bias instance, without repetitive exposition",
      "Consequences at each decision point are ambiguous with respect to whether the decision was well- or poorly-founded",
      "Technical vocabulary matches UK/Commonwealth-style single-line block working terminology consistently"
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
