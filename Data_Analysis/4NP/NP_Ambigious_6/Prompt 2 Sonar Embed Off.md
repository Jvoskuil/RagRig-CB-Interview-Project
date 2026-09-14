You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is a routine cognitive task analysis interview — I want to understand how you actually worked through the feedwater heater trend during the ascension test, not evaluate your performance. It'll be de-identified for training and procedure review. Okay with you?

Participant: Sure, no problem.

Interviewer: Let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend?

Participant: We were about three hours into the ascension test, sitting around 90 percent power, working toward a dispatch commitment at end of shift. I was doing my normal rounds on the trend recorders and caught that heater 1B outlet temperature had come up about three degrees over maybe twenty minutes. Train 1A was steady, no alarm, nothing outside our Tech Spec limit. My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched.

Interviewer: What was going through your head in terms of goals and pressures?

Participant: Getting to a hundred percent within the dispatch window, with about two hours of slack at that point. I wasn't rushed, but I was aware of the clock. At the same time, I didn't want to just label the drift and move on without checking whether it actually fit.

Interviewer: Let's reconstruct the timeline before we get into the decisions. What happened after you noticed the drift?

Participant: I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. I asked him to take a second reading. Shortly after that the trend recorder started flattening as we came up on the final ascension step.

Interviewer: Okay, let's go through this decision by decision. First: when you noticed the drift, what alternatives did you actually weigh?

Participant: Either treat it as the same calibration issue from last cycle, or treat it as an open question and get an independent check before assuming anything. I ended up somewhere in between — I pulled up the old fault log to see how closely the pattern matched.

Interviewer: What did that comparison tell you?

Participant: Honestly, it was partial. The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had.

Interviewer: Did that ambiguity bother you?

Participant: A little. I would've liked a cleaner match one way or the other. But I didn't think it was worth pulling I&C off other work for a value that was still well inside limits.

Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available to brief the STA before continuing. What went into that call?

Participant: That one I thought about for a bit. The STA was right there. Part of me thought, with the comparison being inconclusive, maybe I should just brief him now and let him weigh in. But I also didn't have much to brief him with yet — just an unconfirmed resemblance to an old fault. So I decided to keep trending for a defined stretch, I think I gave it another fifteen minutes in my head, with the idea that either the data would firm up enough to justify a briefing, or it would settle down and not need one.

Interviewer: Was the schedule part of that?

Participant: A bit, sure. But it wasn't the deciding factor — I genuinely thought waiting a short, bounded amount of time would give me better information either way.

Interviewer: Right after that, the technician's infrared call came in. How did you weigh that against the trend recorder?

Participant: That's the one where I felt most uncertain. His reading suggested localized heating, which could point to fouling, but it could also just be a warm spot from wherever that drifted sensor sits — I honestly wasn't sure which. The trend recorder showed a smooth rise, which didn't obviously rule either explanation in or out. Rather than pick one, I asked him to take a second reading and tell me what the scan conditions were, since I wanted something to compare against rather than deciding off one data point.

Interviewer: What came back?

Participant: A similar but not identical reading. He mentioned the scan angle and surface conditions weren't perfectly controlled either time, so even the comparison didn't fully resolve it. At that point I had two data sources that each pointed somewhere, but neither one closed the question.

Interviewer: How did you feel about leaving it open like that?

Participant: A little uneasy, if I'm honest. Usually you want a cleaner answer before you keep moving. But nothing in front of me demanded an immediate call, so I didn't force one.

Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed?

Participant: The flattening helped, but I didn't treat it as proof the earlier question was settled. I still had that inconclusive infrared comparison sitting unresolved. What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point.

Interviewer: Did you consider holding anyway, just to close out the comparison first?

Participant: I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call.

Interviewer: What single piece of information would have changed that decision?

Participant: If the repeat scan had come back clean and consistent — clearly showing localized heating with good scan conditions both times — I think I would've held and gotten the STA involved before the final step.

Interviewer: And if the trend had kept climbing instead of flattening?

Participant: Then the flattening wouldn't have been there to lean on, and I think the open item alone would've been enough to justify a hold.

Interviewer: Looking back, is there a point where you wish you'd had better information, even if the decision felt reasonable at the time?

Participant: The infrared piece, definitely. I'd have liked a way to get a controlled comparison reading rather than two scans taken under different conditions. That's really where most of my uncertainty sat the whole time.

Interviewer: One last thing for the record, unrelated to how you reasoned through it at the time — a maintenance work order filed after your shift ended found early-stage fouling on the 1B heater, separate from the old calibration issue. That wasn't information you had available during the ascension, so I'm just noting it for the file.

Participant: Understood — that's good to have documented either way.

Interviewer: That's really helpful, thank you.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Ambigious_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 0,
        "mechanism_constraint": "No intended instance; operator must explicitly treat the prior-calibration match as partial and unconfirmed rather than selectively accepted."
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 0,
        "mechanism_constraint": "No intended instance; the escalation decision at decision point 2 must reflect a reasoned, time-bounded data-gathering choice rather than an informal, non-systematic satisficing judgment."
      },
      {
        "bias": "Salience Bias",
        "occurrences": 0,
        "mechanism_constraint": "No intended instance; evidence weighting at decision point 3 must not be driven by visual prominence of the trend display over the verbal field report."
      },
      {
        "bias": "Similarity Bias",
        "occurrences": 0,
        "mechanism_constraint": "No intended instance; source-credibility reasoning must not discount the technician based on role dissimilarity or shared operator identity."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 0,
        "mechanism_constraint": "No intended instance; the final decision must explicitly document the unresolved item rather than proceeding on a restricted information set without acknowledgment."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Imperfect Rationality",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 0 },
      { "bias": "Imperfect Rationality", "requested_occurrences": 0 },
      { "bias": "Salience Bias", "requested_occurrences": 0 },
      { "bias": "Similarity Bias", "requested_occurrences": 0 },
      { "bias": "Bounded Rationality", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "NP_Biased_6",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Ambigious_6",
    "domain_id": "NP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable — this is an ambiguous_control scenario with a zero-occurrence manifest for all five target biases named in the paired biased scenario (NP_Biased_6). No allocation across decision points was performed since no bias instances are intentionally planned. Instead, each of the four decision points (matched one-to-one to the biased scenario's decision points) was redesigned so that the specific reasoning pattern that constituted each bias instance in NP_Biased_6 is replaced with an explicitly underdetermined, dual-hypothesis, or corroboration-seeking judgment that resists classification as any named bias while remaining a defensible point of expert disagreement.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (PWR licensed Reactor Operator)",
      "Setting and operational objective (power ascension test toward 100% power within a dispatch window)",
      "Four-decision-point structure and their sequential relationship to the same underlying incident (initial drift interpretation, escalation/hold-point choice, weighing technician field report, final ascension go-decision)",
      "Core factual anchors (heater 1B outlet temperature drift, redundant train 1A stability, prior-cycle calibration history, technician infrared report, flattening trend, post-hoc work order revealing fouling)",
      "Stakeholders, vocabulary level, difficulty, and overall emotional tone",
      "Ambiguous, non-diagnostic consequence structure"
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
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The participant compares the drift with the prior calibration issue, considers an independent check, and logs it as probable but unconfirmed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden zero-occurrence manifest requires treating the prior-event resemblance as partial and unconfirmed."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The participant weighs briefing the STA against keeping the trend under observation for a defined additional interval to obtain better information.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The choice is explicitly time-bounded and information-seeking rather than an unstructured satisficing judgment."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The participant treats the infrared reading and trend recorder as incomplete evidence, requests a repeat scan, and withholds a final classification.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant does not privilege the visually prominent trend or discount the technician by role; both sources remain unresolved."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The participant proceeds after the trend flattens, documents the unresolved infrared comparison, hands it off, and considers but rejects an additional hold.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The unresolved item is explicitly documented and assigned for follow-up, satisfying the zero-bias control requirement."
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
      "analysis_scope_note": "No retrieved scientific-paper corpus passages were available in the provided context. The analysis therefore uses conservative, general cognitive-science knowledge and does not cite corpus evidence."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "availability heuristic",
        "alternative_labels": [
          "availability bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial interpretation of heater 1B outlet temperature drift",
        "supporting_interview_quote": "My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched.",
        "plausible_mechanism": "A salient prior calibration event came easily to mind and may have shaped the initial hypothesis, potentially making the old calibration explanation more mentally available than other possible causes.",
        "why_not_identified": "The participant explicitly recognized the memory was incomplete, did not treat the prior event as a confirmed match, and sought objective comparison with the closed-out fault report. There is insufficient affirmative evidence that ease of recall distorted a probability judgment or subsequent decision."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "confirmation bias",
        "alternative_labels": [
          "confirmatory bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Comparison of current drift with prior calibration fault log",
        "supporting_interview_quote": "The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had.",
        "plausible_mechanism": "The participant may have given somewhat more weight to features consistent with the initial calibration hypothesis, logging a probable recurrence despite an inconclusive onset-rate comparison.",
        "why_not_identified": "The participant acknowledged the missing diagnostic information and labeled the recurrence as unconfirmed. There is no clear evidence of selective search, discounting of disconfirming information, or avoidance of alternative explanations."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No scientific-paper corpus passages were available for retrieval, so bias labels and mechanisms could not be verified against corpus definitions.",
      "The interview is a retrospective self-report; although no affirmative bias mechanism was identified, memory and self-presentation could affect the account.",
      "The later maintenance finding of early-stage fouling was not available to the participant during the ascension test and was not treated as evidence of biased reasoning."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Ambigious_6_Sonar_off",
  "interview_id": "NP_Ambigious_6",
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
