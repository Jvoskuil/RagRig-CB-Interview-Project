You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Biased_6",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Reactor Operator (NRC-licensed)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Anomalous Feedwater Temperature Drift During Power Ascension",
    "scenario_summary_internal": "During a post-refueling power ascension test on a PWR, the licensed Reactor Operator (RO) at the controls notices a slow, small upward drift in feedwater heater outlet temperature on one train while simultaneously a redundant train shows normal readings. The RO must decide whether the drift reflects a known, previously logged sensor calibration issue (from the prior cycle) or an emerging heat-exchanger fouling condition, while balancing schedule pressure to reach 100% power before a grid-dispatch window closes. Over roughly 90 minutes, the RO makes four sequential decisions: (1) how to interpret the initial temperature drift, (2) whether to escalate to the Shift Technical Advisor (STA) or continue trending, (3) how to weigh a maintenance technician's report against control-room trend data when they conflict, and (4) whether to proceed with the final power ascension step. The incident resolves ambiguously: the ascension is completed without an immediate trip, but a work order is later generated for feedwater heater inspection, meaning the interview can probe reasoning quality independent of outcome.",
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
        "heuristic",
        "cognitive bias",
        "anchoring"
      ],
      "notes_on_realism": "All four decision points are grounded in ordinary control-room practice (trend monitoring, STA consultation, cross-checking maintenance input, procedural go/no-go for ascension) so that biased reasoning is expressed through operational judgment calls rather than explicit psychological language."
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
          "Interpret the drift as a recurrence of the previously known calibration issue and continue trending without further action",
          "Treat the drift as a new, unexplained condition and immediately request an independent sensor cross-check or I&C walkdown"
        ],
        "intended_action": "RO logs the drift as 'consistent with prior calibration history' and continues the ascension sequence without requesting an independent check.",
        "new_information_after_decision": [
          "Temperature continues a shallow upward trend over the next 15 minutes, still within limits"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Continued shallow upward trend on 1B",
          "STA is available in the control room and has not yet been briefed on the drift",
          "Ascension procedure has a discretionary hold point allowing the RO to pause and consult before the next power increase step",
          "Grid dispatch window requires reaching 100% power within the next two hours"
        ],
        "alternatives": [
          "Proactively brief the STA now and request formal review before proceeding further",
          "Continue the ascension on schedule and mention the trend to the STA at the next routine shift briefing"
        ],
        "intended_action": "RO defers formal STA briefing, reasoning that the trend fits the pattern already seen last cycle and does not yet warrant interrupting the schedule.",
        "new_information_after_decision": [
          "A maintenance technician performing an unrelated walkdown radios in that the 1B heater shell shows a slightly higher-than-usual skin temperature by hand-held infrared reading"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Technician's infrared reading suggests possible localized heating inconsistent with a simple sensor calibration error",
          "Control-room trend data still shows a smooth, gradual rise resembling the historical calibration signature",
          "Technician has less control-room instrumentation experience than the RO but has direct hands-on familiarity with heat exchanger degradation modes",
          "No Tech Spec limit has been approached"
        ],
        "alternatives": [
          "Weigh the technician's field observation as an independent data point that may indicate fouling rather than calibration drift",
          "Discount the field reading because it comes from an infrared scan rather than the calibrated plant instrumentation the RO trusts"
        ],
        "intended_action": "RO gives limited weight to the technician's field reading, favoring the smooth control-room trend and the technician's comparatively lower instrumentation-reading experience, and reclassifies the report as likely measurement noise from the handheld device.",
        "new_information_after_decision": [
          "Trend recorder shows the rate of temperature rise beginning to flatten slightly as the ascension nears the final step"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flattening trend on 1B temperature",
          "Time remaining before the grid dispatch window is tightening",
          "No procedural or Tech Spec basis currently exists to halt the ascension",
          "STA has not been formally engaged on this specific trend"
        ],
        "alternatives": [
          "Proceed with the final ascension step to 100% power as scheduled, monitoring the trend continuously",
          "Request a brief hold at current power to allow an independent instrument verification before taking the final step"
        ],
        "intended_action": "RO proceeds with the final ascension step, citing the flattening trend and the historical calibration precedent as sufficient justification, without requesting the independent verification.",
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
        "What alternatives did you consider before deciding not to brief the STA immediately?",
        "How did you weigh the technician's infrared reading against the control-room trend data?",
        "What made you confident enough to proceed with the final ascension step?"
      ],
      "goals_and_alternatives": [
        "At each point, what other options did you have available, and why did you rule them out?",
        "Was reaching the grid dispatch window part of your reasoning at any of these steps?"
      ],
      "decision_basis": [
        "What single piece of evidence mattered most to you at each decision, and why?",
        "Did anything you already believed about this system affect how you read the new data?"
      ],
      "prior_experience": [
        "Had you seen a similar temperature trend before, and how did that shape your interpretation this time?",
        "How did the prior cycle's calibration history influence your response to this new trend?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the dispatch schedule weigh on your decisions?",
        "At what point, if any, did you feel uncertain about what was actually happening with the heater?"
      ],
      "closing_hypotheticals": [
        "If the technician's report had come from another licensed operator instead, would you have weighed it differently?",
        "If the trend had continued rising instead of flattening, what would you have done differently?",
        "Looking back, is there a point where you would have made a different call with the same information?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "RO selectively interprets the ambiguous early temperature drift as matching a known prior-cycle calibration issue, without seeking disconfirming cross-check evidence, because that interpretation fits a pre-existing belief.",
        "affected_reasoning_operation": "Initial evidence interpretation and hypothesis selection",
        "evidence_available_at_time": [
          "3°F rise over 20 minutes on trend recorder",
          "stable redundant train 1A",
          "logged prior-cycle calibration deviation on same sensor"
        ],
        "required_textual_manifestation": "RO states the drift 'had to be' the same calibration issue as last cycle and did not consider requesting an independent sensor check, framing the prior incident as sufficient explanation without checking alternative causes.",
        "plausible_nonbias_interpretation": "A reasonable operator may legitimately treat a documented recurring instrument issue as the most probable explanation for a small drift within limits.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "belief-consistent evidence", "selective interpretation"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "RO discounts the technician's independent infrared field reading because it conflicts with the RO's already-formed calibration-drift belief, actively reinterpreting new disconfirming evidence as noise rather than updating the hypothesis.",
        "affected_reasoning_operation": "Evidence weighting and belief updating when new, potentially disconfirming data arrives",
        "evidence_available_at_time": [
          "technician's infrared skin-temperature reading",
          "smooth control-room trend consistent with calibration-drift hypothesis",
          "RO's established belief that this is a calibration issue"
        ],
        "required_textual_manifestation": "RO explains reclassifying the infrared reading as 'probably just handheld device noise' specifically because it did not match the trend recorder pattern already believed to be the calibration signature.",
        "plausible_nonbias_interpretation": "Calibrated plant instrumentation is legitimately more reliable than a handheld scan, so discounting it could reflect sound instrument-hierarchy judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "disconfirming evidence", "belief updating"]
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 2,
        "mechanism": "RO's decision to defer STA briefing is driven by a mix of schedule concern and pattern-matching rather than a fully systematic weighing of procedural discretion, Tech Spec margin, and risk, reflecting a satisfactory-but-not-optimal reasoning process.",
        "affected_reasoning_operation": "Decision to escalate versus defer, under partial information and multiple competing considerations",
        "evidence_available_at_time": [
          "continued shallow upward trend",
          "available discretionary hold point",
          "dispatch window two hours away",
          "STA present but unbriefed"
        ],
        "required_textual_manifestation": "RO describes weighing the decision quickly using a rough sense that things 'felt manageable' and the schedule 'still had room,' rather than systematically working through the hold-point criteria, resulting in a plausible but non-exhaustive justification for deferring.",
        "plausible_nonbias_interpretation": "Operators often use efficient, experience-based shortcuts under time constraints that are not irrational, only imperfectly systematic.",
        "strength": "subtle",
        "do_not_make_explicit": ["imperfect rationality", "bounded reasoning", "satisficing"]
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 3,
        "mechanism": "RO gives outsized weight to the smooth, easily visible trend-recorder graph (a highly salient visual cue) over the technician's verbally reported, less visually prominent infrared reading, even though both are legitimate data points.",
        "affected_reasoning_operation": "Selection and weighting of competing evidence sources",
        "evidence_available_at_time": [
          "continuously displayed trend recorder graph in the RO's direct field of view",
          "technician's verbal radio report of a one-time handheld reading"
        ],
        "required_textual_manifestation": "RO explains that the trend graph was 'right there in front of me the whole time' and easier to trust than a one-off spoken report, emphasizing visual immediacy as the deciding factor.",
        "plausible_nonbias_interpretation": "Continuous instrumentation data is often objectively more reliable than a single spot-check, so preferring it could be a defensible technical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["salience bias", "visual prominence", "attention-driven weighting"]
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "decision_point": 3,
        "mechanism": "RO discounts the maintenance technician's assessment partly because the technician's background and instrument-reading experience differ from the RO's own licensed-operator training, treating the dissimilar source as less credible independent of the actual content of the observation.",
        "affected_reasoning_operation": "Source credibility assessment",
        "evidence_available_at_time": [
          "technician's field experience and background differing from RO's control-room training",
          "the specific content of the infrared reading itself"
        ],
        "required_textual_manifestation": "RO notes that the technician 'doesn't read control-room trends the way we do' as a reason for weighting the report lower, tying credibility to the technician's dissimilar role rather than solely to the substance of the observation.",
        "plausible_nonbias_interpretation": "Differences in training could legitimately affect how much technical weight a report deserves, independent of any bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity bias", "in-group", "shared background"]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 4,
        "mechanism": "RO makes the final ascension go-decision using a limited subset of available information (flattening trend, prior calibration precedent) rather than exhaustively integrating all available data (technician report, uncertainty about heater fouling), reflecting cognitive and time limits on full information processing.",
        "affected_reasoning_operation": "Final integrative go/no-go judgment under limited processing capacity and time constraint",
        "evidence_available_at_time": [
          "flattening temperature trend",
          "tightening dispatch schedule",
          "unresolved technician report from earlier",
          "no formal STA engagement on this specific trend"
        ],
        "required_textual_manifestation": "RO describes deciding to proceed based on 'the trend leveling off and the history we had' without revisiting the technician's report or the unresolved uncertainty, citing limited time and mental bandwidth to reconsider every input before the step.",
        "plausible_nonbias_interpretation": "Under genuine time constraints, no operator can re-evaluate every data point before every step, so this could reflect a reasonable triage rather than a bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["bounded rationality", "cognitive limits", "satisficing", "limited information processing"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased condition with no paired control specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable — no counterfactual condition requested; field retained as null per AUTOSELECT default with no action taken",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and numbered 1-4",
      "Confirm exactly 6 total bias instances are embedded: 2 confirmation bias, 1 imperfect rationality, 1 salience bias, 1 similarity bias, 1 bounded rationality",
      "Confirm no bias name, definition, or psychological term appears in the public interview text",
      "Confirm each of the two confirmation bias instances uses a distinct evidence source and decision point (phase 1 initial interpretation vs phase 3 discounting new field evidence)",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points and probe plan density",
      "Confirm consequences (successful ascension, later work order revealing fouling) do not conclusively prove bias, preserving the ambiguity requirement",
      "Confirm each instance has a plausible non-bias interpretation documented",
      "Confirm probe_plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals"
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
