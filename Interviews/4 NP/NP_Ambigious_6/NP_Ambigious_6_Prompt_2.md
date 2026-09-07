You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Ambigious_6",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Reactor Operator (NRC-licensed)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Anomalous Feedwater Temperature Drift During Power Ascension — Ambiguous Control",
    "scenario_summary_internal": "This is the ambiguous-control pairing for NP_Biased_6. The same PWR power-ascension incident is reconstructed: a licensed Reactor Operator notices a slow, small upward drift in feedwater heater 1B outlet temperature during a post-refueling ascension test while a redundant train reads normal, and must reason through the same four sequential junctures — initial interpretation of the drift, whether to escalate to the STA, how to weigh a maintenance technician's conflicting field report, and whether to proceed with the final ascension step. Unlike the biased condition, the operator's reasoning at each point remains genuinely underdetermined: the available evidence supports more than one defensible reading, the operator raises and partially investigates competing hypotheses, and consequences remain ambiguous. No named cognitive bias is intentionally instantiated; the interview should read as a competent but imperfectly informed operator navigating real uncertainty, with plausible non-bias explanations available for every choice.",
    "occupational_realism": {
      "objective": "Safely complete a scheduled power ascension from 90% to 100% reactor thermal power following a refueling outage, meeting a grid-dispatch commitment window without violating any Technical Specification limit.",
      "setting": "Main control room of a pressurized water reactor (PWR) plant during a daytime shift, several hours into a power-ascension test sequence with STA, Shift Manager, and I&C/maintenance support available by phone or in person.",
      "constraints": [
        "Technical Specification limits on feedwater heater outlet temperature and associated reactivity/power limits",
        "Grid dispatch commitment creating time pressure to reach 100% power by a fixed window",
        "Limited direct instrumentation redundancy on the affected feedwater train",
        "Need for STA concurrence before certain procedural steps",
        "Fatigue/workload from a multi-hour ascension test already in progress"
      ],
      "stakeholders": [
        "Licensed Reactor Operator (primary interviewee)",
        "Shift Technical Advisor (STA)",
        "Shift Manager",
        "Maintenance/I&C technician",
        "Balance-of-plant operator monitoring feedwater system"
      ],
      "technical_terms_to_use": [
        "feedwater heater outlet temperature",
        "power ascension test",
        "Technical Specification limit",
        "trend recorder",
        "redundant train",
        "STA concurrence",
        "reactivity management",
        "work order",
        "instrument drift",
        "heat exchanger fouling"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "salience bias",
        "similarity bias",
        "bounded rationality",
        "imperfect rationality",
        "heuristic",
        "cognitive bias",
        "anchoring"
      ],
      "notes_on_realism": "All four decision points mirror the paired biased scenario's structure and stakes, but each decision must be written so that the operator visibly considers, and partially acts on, more than one hypothesis or evidence source, leaving the reasoning genuinely underdetermined rather than resolved by a one-sided shortcut."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Feedwater heater 1B outlet temperature has risen 3°F over 20 minutes on the trend recorder",
          "Redundant train 1A shows stable, normal temperature",
          "A calibration deviation on the same sensor was logged and closed out during the prior operating cycle",
          "No alarm has actuated; value remains within Tech Spec limits"
        ],
        "alternatives": [
          "Treat the drift as most likely a recurrence of the prior calibration issue, while noting it is not yet confirmed",
          "Treat the drift as an open question requiring a quick independent cross-check before assuming a cause"
        ],
        "intended_action": "RO notes the resemblance to the prior calibration event but explicitly flags that the match is not confirmed, and requests a short cross-reference of the current pattern against the closed-out fault report before deciding how to log it, ultimately logging it as 'probable but unconfirmed calibration recurrence' pending that check.",
        "new_information_after_decision": [
          "The cross-reference shows partial but incomplete similarity — the timing and magnitude of the rise resemble the prior event, but one data point (rate of onset) is not clearly comparable because the prior log did not record it consistently"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Continued shallow upward trend on 1B",
          "Partial but inconclusive match to the prior calibration signature",
          "STA is available in the control room and has not yet been briefed on the drift",
          "Ascension procedure has a discretionary hold point allowing the RO to pause and consult before the next power increase step",
          "Grid dispatch window requires reaching 100% power within the next two hours"
        ],
        "alternatives": [
          "Brief the STA now given the inconclusive cross-reference, even though no limit is threatened",
          "Continue trending a while longer to gather more data before deciding whether a briefing is warranted"
        ],
        "intended_action": "RO weighs the inconclusive cross-check against the available schedule margin and decides to continue trending for a defined additional interval (rather than either briefing immediately or deferring indefinitely), explicitly reasoning that more data would make either a briefing or a stand-down decision better supported.",
        "new_information_after_decision": [
          "A maintenance technician performing an unrelated walkdown radios in that the 1B heater shell shows a slightly higher-than-usual skin temperature by hand-held infrared reading"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Technician's infrared reading suggests possible localized heating, which could indicate fouling but could also be consistent with a warm calibration-drifted sensor location",
          "Control-room trend data still shows a smooth, gradual rise",
          "Technician has hands-on familiarity with heat exchanger degradation modes but has not previously flagged a false positive with this equipment",
          "No Tech Spec limit has been approached"
        ],
        "alternatives": [
          "Request that the technician repeat the scan or provide a comparison reading to help disambiguate the finding",
          "Rely on the existing trend recorder data as the primary basis while treating the field reading as a secondary, unresolved input pending the repeat scan"
        ],
        "intended_action": "RO asks the technician to take a second reading and report the scan conditions, treating both the trend and the field report as incomplete evidence until the repeat scan comes back, and explicitly withholds a final classification of the drift's cause pending that additional data point.",
        "new_information_after_decision": [
          "The repeat scan technician provides is taken quickly and shows a similar but not identical reading; the technician notes that scan conditions were not perfectly controlled either time, leaving the comparison inconclusive",
          "Trend recorder shows the rate of temperature rise beginning to flatten slightly as the ascension nears the final step"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flattening trend on 1B temperature",
          "Inconclusive repeat infrared scan",
          "Time remaining before the grid dispatch window is tightening",
          "No procedural or Tech Spec basis currently exists to halt the ascension",
          "STA has not been formally engaged on this specific trend, though the RO has kept a written log of the open items"
        ],
        "alternatives": [
          "Proceed with the final ascension step, given the flattening trend and absence of a Tech Spec basis to hold, while flagging the open items for follow-up",
          "Request a brief hold at current power specifically to resolve the inconclusive infrared comparison before the final step"
        ],
        "intended_action": "RO proceeds with the final ascension step but explicitly documents the unresolved infrared comparison as an open item for the oncoming shift and initiates a maintenance follow-up request, treating the flattening trend as sufficient for the immediate step without treating it as fully resolving the earlier uncertainty.",
        "new_information_after_decision": [
          "Ascension completes without exceeding any limit; a routine end-of-shift work order is later written recommending inspection of the 1B feedwater heater, which subsequently reveals early-stage fouling unrelated to the prior calibration issue"
        ]
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when you first noticed the feedwater heater 1B temperature trend.",
        "What was your overall goal during this shift, and what pressures were you managing?"
      ],
      "timeline_reconstruction": [
        "What did the trend recorder show at each point, and how often were you checking it?",
        "When did the technician's report come in relative to your other observations?",
        "What did you know about the prior cycle's calibration issue, and how did you first recall it?"
      ],
      "decision_point_probes": [
        "What information sources did you rely on when you first interpreted the drift, and why those sources?",
        "What made you decide to check the cross-reference before logging a cause?",
        "How did you decide how long to keep trending before considering a briefing?",
        "How did you weigh the technician's infrared reading against the control-room trend data, and what led you to ask for a repeat scan?",
        "What made you comfortable proceeding with the final ascension step given the unresolved comparison?"
      ],
      "goals_and_alternatives": [
        "At each point, what other options did you have available, and why did you rule them out or keep them open?",
        "Was reaching the grid dispatch window part of your reasoning at any of these steps?"
      ],
      "decision_basis": [
        "What single piece of evidence mattered most to you at each decision, and why?",
        "Was there a point where you felt the evidence genuinely didn't point clearly one way or the other?"
      ],
      "prior_experience": [
        "Had you seen a similar temperature trend before, and how did that shape your interpretation this time?",
        "How did the prior cycle's calibration history influence your response to this new trend, given it wasn't a perfect match?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the dispatch schedule weigh on your decisions?",
        "At what point, if any, did you feel most uncertain about what was actually happening with the heater, and what would have resolved that uncertainty?"
      ],
      "closing_hypotheticals": [
        "What single piece of information would have changed your decision at the technician's-report stage?",
        "If the repeat scan had come back clearly confirming localized heating, what would you have done differently at the final step?",
        "Looking back, is there a point where you wish you'd had better information, even if your decision was reasonable at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "NP_Biased_6",
      "features_to_match": [
        "Same occupational domain, role, setting, and objective (PWR power ascension, licensed RO, dispatch-window pressure)",
        "Same four-decision-point structure and same underlying factual anchors (heater 1B drift, prior calibration history, technician infrared report, flattening trend, final ascension step)",
        "Same stakeholders (STA, Shift Manager, maintenance technician, BOP operator)",
        "Same technical vocabulary, difficulty level, and emotional tone (measured, professional, mild but present time pressure)",
        "Same ambiguous, non-diagnostic consequence structure (successful ascension, later work order revealing unrelated early-stage fouling)"
      ],
      "features_to_remove_or_change": [
        "Remove selective, one-sided interpretation of the prior calibration match; replace with explicit acknowledgment of partial, inconclusive similarity",
        "Remove deferral of STA briefing based on an informal, non-systematic gut check; replace with a reasoned, time-bounded decision to gather more data before choosing between briefing and standing down",
        "Remove asymmetric discounting of the technician's report based on evidence format or source identity; replace with a request for corroborating data (repeat scan) that treats both sources as incomplete",
        "Remove the final-step decision to proceed without revisiting open uncertainty; replace with an explicit decision to proceed while formally logging the unresolved item for follow-up",
        "Remove any framing that ties source credibility to role similarity or shared operator identity"
      ],
      "ambiguity_boundary": "Each decision point must leave a genuinely open question that a careful reader cannot resolve as clearly biased or clearly optimal: the cross-reference in decision 1 is partial, the additional trending interval in decision 2 is a defensible middle path rather than a clear deferral, the repeat scan in decision 3 is itself inconclusive, and the final decision in decision 4 combines proceeding with explicit unresolved-item documentation rather than either ignoring or fully resolving the uncertainty. No decision should collapse into a clean example of any of the five target biases, but each should remain the kind of judgment call where a domain expert could defensibly disagree with the operator's choice."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and numbered 1-4",
      "Confirm zero intended instances of Confirmation Bias, Imperfect Rationality, Salience Bias, Similarity Bias, and Bounded Rationality are embedded",
      "Confirm no bias name, definition, or psychological term appears in the public interview text",
      "Confirm each decision point contains a genuinely underdetermined element with a stated plausible non-bias explanation, not a resolved or one-sided judgment",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points and probe plan density",
      "Confirm the scenario matches NP_Biased_6 in domain, role, setting, actors, vocabulary, tone, and four-decision structure",
      "Confirm consequences (successful ascension, later work order revealing fouling) remain ambiguous and do not diagnostically prove any reasoning pattern",
      "Confirm no exaggerated or artificially neutral dialogue is used to signal the control condition",
      "Confirm probe_plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals, including at least one 'what information would have changed the decision' and one 'what if a key feature had been different' probe"
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
