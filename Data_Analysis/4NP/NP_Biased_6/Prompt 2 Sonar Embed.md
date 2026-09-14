You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay?

Participant: Yeah, that's fine. I figured this was coming after the work order got written up.

Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend?

Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, "here we go again" — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.

Interviewer: What was going through your head at that point, in terms of goals and pressures?

Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again.

Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next?

Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step.

Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider?

Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first.

Interviewer: What made you settle on that one?

Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.

Interviewer: Did you consider what it would take to rule that explanation out?

Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw "same sensor, same shape" and moved on, since I was already treating it as the same event.

Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call?

Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it "felt manageable" — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.

Interviewer: Was the dispatch window part of that calculation?

Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.

Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder.

Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said.

Interviewer: How did you end up weighting the two?

Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.

Interviewer: Did anything about that reasoning give you pause?

Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words.

Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold?

Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.

Interviewer: Did you consider requesting a hold for independent verification before that step?

Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time.

Interviewer: How much uncertainty did you feel across all of this?

Participant: Some, especially after the tech's call. But nothing that crossed into "this violates a limit" territory, so it stayed more like background noise than something driving the decisions.

Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently?

Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise.

Interviewer: And if the trend had kept climbing instead of flattening near the final step?

Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding.

Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call?

Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further.

Interviewer: That's helpful, thank you. I think that covers everything I needed.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 2,
        "mechanism_constraint": "One instance at initial ambiguous-evidence interpretation (decision point 1); one instance at discounting new disconfirming field evidence (decision point 3). Must use distinct evidence sources."
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as a non-systematic, satisficing escalation decision at decision point 2, not as an outcome failure."
      },
      {
        "bias": "Salience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as overweighting the visually prominent trend recorder over a verbally reported field observation at decision point 3."
      },
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as discounting a source based on dissimilar role/background rather than content, at decision point 3."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as an incomplete-information final integrative decision under time/cognitive constraints at decision point 4."
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
      { "bias": "Confirmation Bias", "requested_occurrences": 2 },
      { "bias": "Imperfect Rationality", "requested_occurrences": 1 },
      { "bias": "Salience Bias", "requested_occurrences": 1 },
      { "bias": "Similarity Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "cb_02", "bias": "Confirmation Bias" },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality" },
      { "instance_id": "sb_01", "bias": "Salience Bias" },
      { "instance_id": "sim_01", "bias": "Similarity Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Confirmation Bias", "decision_point": 3 },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality", "decision_point": 2 },
      { "instance_id": "sb_01", "bias": "Salience Bias", "decision_point": 3 },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 3 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective interpretation of ambiguous drift as matching a known prior-cycle belief, without seeking disconfirming checks",
        "affected_reasoning_operation": "Initial hypothesis selection",
        "evidence_source": "trend recorder drift plus prior-cycle calibration log",
        "distinctiveness_requirement": "Occurs at initial evidence interpretation before any conflicting data exists; distinct from cb_02 which involves discounting new conflicting data"
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "mechanism": "Reinterpreting new disconfirming field evidence (infrared reading) as noise to preserve the pre-existing calibration-drift belief",
        "affected_reasoning_operation": "Belief updating in response to new conflicting evidence",
        "evidence_source": "technician's infrared handheld reading",
        "distinctiveness_requirement": "Occurs after new disconfirming evidence arrives, at a different decision point and evidence source than cb_01"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Non-exhaustive, satisficing weighing of escalation criteria under time and information constraints, rather than systematic evaluation",
        "affected_reasoning_operation": "Escalation/deferral decision-making",
        "evidence_source": "trend continuation, hold-point procedure, dispatch schedule",
        "distinctiveness_requirement": "Distinct from bounded rationality instance (br_01) by focusing on the escalation judgment process itself rather than integration of multiple data sources at the final step"
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "mechanism": "Overweighting the continuously visible trend graph relative to a verbally reported one-time field observation",
        "affected_reasoning_operation": "Evidence source weighting",
        "evidence_source": "trend recorder display versus radioed verbal report",
        "distinctiveness_requirement": "Distinct from cb_02 by focusing on visual prominence/attention capture rather than belief-preservation motive"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Discounting technician's report based on dissimilarity of role/training rather than content of the observation",
        "affected_reasoning_operation": "Source credibility assessment",
        "evidence_source": "technician's background/role as stated in the report",
        "distinctiveness_requirement": "Distinct from sb_01 and cb_02 by grounding the discounting in source identity/similarity rather than evidence format or belief consistency"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Using a limited subset of available information for the final go decision due to cognitive/time constraints, without revisiting unresolved uncertainty",
        "affected_reasoning_operation": "Final integrative go/no-go judgment",
        "evidence_source": "flattening trend, prior precedent, unresolved technician report",
        "distinctiveness_requirement": "Distinct from ir_01 by occurring at the final integrative decision point and reflecting information-processing capacity limits rather than escalation-judgment style"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality", "strength": "subtle" },
      { "instance_id": "sb_01", "bias": "Salience Bias", "strength": "subtle" },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_6",
    "domain_id": "NP",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit: decision point 1 received one confirmation-bias instance (initial interpretation); decision point 2 received the imperfect-rationality instance (escalation judgment); decision point 3 received three instances (second confirmation-bias occurrence, salience bias, similarity bias), each tied to a distinct evidence source or reasoning operation (belief-preservation vs. visual prominence vs. source-identity discounting) per the multi-occurrence-per-point rule; decision point 4 received the bounded-rationality instance (final integrative judgment). No bias exceeded two instances at a single decision point, and no two instances at the same decision point shared an evidence source or reasoning operation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": [
      "Decision point 3 carries three distinct bias instances (cb_02, sb_01, sim_01) to satisfy mechanism-fit requirements, since the technician-report conflict is the most natural location for confirmation, salience, and similarity biases to jointly manifest through different evidence-processing routes; each instance is documented with a distinct evidence source and reasoning operation to preserve independent identifiability and avoid redundancy."
    ]
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
          "segment_type": "initial_hypothesis_selection_and_verification_choice",
          "raw_interview_anchor": "Initial observation of the 1B outlet-temperature drift, recall of the prior calibration deviation, selection of the calibration explanation, and decision not to request an independent sensor check.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The participant interprets ambiguous new drift as recurrence of a known prior issue and does not seek a disconfirming check."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "escalation_and_hold_point_decision",
          "raw_interview_anchor": "Decision to continue through the discretionary hold point without briefing the STA, using a quick gut check and schedule/momentum considerations instead of formally working through the hold-point criteria.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ir_01"
          ],
          "ground_truth_rationale": "The escalation decision is non-exhaustive and satisficing under time and information constraints."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "conflicting_evidence_weighting",
          "raw_interview_anchor": "Evaluation of the technician's infrared report against the continuously visible trend, including dismissal as handheld noise and discounting based on the technician's different role and background.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02",
            "sb_01",
            "sim_01"
          ],
          "ground_truth_rationale": "The participant preserves the prior explanation when new field evidence conflicts, overweights the visually prominent trend, and discounts the technician partly because of role dissimilarity."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "final_integrative_go_decision",
          "raw_interview_anchor": "Decision to proceed with the final ascension step based on the flattening trend, prior history, and tightening schedule without revisiting the unresolved technician report or requesting independent verification.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "The final go decision uses a limited subset of available information under time and cognitive constraints."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "retrospective_alternative_reflection",
          "raw_interview_anchor": "Looking back, the participant says the earlier STA briefing might have been a better choice and describes the benefit of another set of eyes.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a retrospective alternative and is not itself a manifested hidden bias occurrence."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single cognitive task analysis interview about reasoning during a feedwater heater temperature trend in an ascension test."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring bias",
        "Anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The anchoring and adjustment heuristic: people form an estimate or interpretation based on an initial value or explanation, and subsequent adjustments from that anchor are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial classification of heater 1B outlet temperature drift",
      "decision_point_description": "Choosing whether to interpret the drift as a known calibration issue versus treating it as something new and requesting an independent instrument check.",
      "affected_reasoning_operation": "Differential diagnosis / classification under uncertainty",
      "bias_specific_mechanism": "The prior-cycle calibration issue served as an available initial interpretation and anchor for the new temperature drift; the participant then compared only superficial features such as 'same sensor, same shape' and did not sufficiently adjust or verify that anchor.",
      "manifestation_in_interview": "The participant immediately categorized the drift as the same calibration deviation from the prior cycle, treated the pattern match as sufficient, and explicitly acknowledged not checking whether the prior fault signature actually matched the current trend.",
      "effect_on_reasoning_or_decision": "The participant selected the known-calibration explanation, logged the drift as consistent with the prior pattern, and did not call for an independent I&C check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly was, 'here we go again' — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.",
          "evidence_explanation": "This shows the prior calibration event immediately becoming the initial interpretation for the new drift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.",
          "evidence_explanation": "The participant treats superficial pattern match with a known cause as sufficient and does not actively seek evidence that would rule that explanation out."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw 'same sensor, same shape' and moved on, since I was already treating it as the same event.",
          "evidence_explanation": "This explicitly demonstrates insufficient adjustment away from the initial calibration anchor, even though the diagnostic signature had not been verified."
        }
      ],
      "correction_or_counterevidence": "Later in the interview, the participant acknowledged that he could have briefed the STA early and gotten another set of eyes, but this was retrospective and did not correct the initial classification.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by a retrieved passage on anchoring and adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974 ... In brief, it has been obser people make estimates based on an initial answer, and adjustments from there based on additional information ... 'adjustments are typic insufficient.'",
          "mechanism_supported_by_source": "People form estimates based on an initial answer or anchor and subsequently adjust insufficiently from that anchor.",
          "relevance_to_this_occurrence": "The participant's initial calibration diagnosis anchored his reading of the new trend, and he made only a superficial comparison rather than sufficiently adjusting or verifying that initial interpretation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Plan continuation error",
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original course of action despite changing conditions or cues that suggest the plan should be reassessed or slowed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Discretionary hold-point and final ascension step decisions",
      "decision_point_description": "Choosing whether to brief or hold for STA review as the trend continued and later flattened before the final power ascension step.",
      "affected_reasoning_operation": "Go/no-go continuation decision under uncertainty",
      "bias_specific_mechanism": "Commitment to reaching 100 percent power within the dispatch window, plus the momentum of the ascension sequence, led the participant to assess anomalous cues as manageable and to bypass formal hold-point review rather than reassessing the plan.",
      "manifestation_in_interview": "The participant described the situation as 'manageable,' did not formally work through hold-point criteria, and cited schedule pressure and the flattening trend as reasons to continue without looping back to the earlier conflicting infrared report.",
      "effect_on_reasoning_or_decision": "The participant did not brief the STA at the discretionary hold point and did not request a hold for independent verification before the final ascension step.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered.",
          "evidence_explanation": "This establishes the original plan and schedule commitment that later influenced continuation decisions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it 'felt manageable' — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.",
          "evidence_explanation": "The participant used a quick gut check instead of formal hold-point criteria and explicitly chose to maintain momentum rather than stop for review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.",
          "evidence_explanation": "This directly links the dispatch window and pace preservation to the decision not to stop."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.",
          "evidence_explanation": "The participant continued the original ascension plan and did not reassess the conflicting field report as time pressure increased."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The flattening is honestly what let me feel okay proceeding.",
          "evidence_explanation": "The participant used the flattening trend as sufficient justification to proceed rather than applying a formal hold decision."
        }
      ],
      "correction_or_counterevidence": "The participant stated that if the trend had kept climbing near the final step, he would have held and called the STA in properly, and he retrospectively acknowledged he could have briefed the STA early.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentioned plan continuation as a bias in operational incidents but did not provide a sufficient definition or mechanism; the label is used from general cognitive-science and aviation-human-factors knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Expectation bias",
        "Selective information processing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior belief or hypothesis, while giving less weight to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of maintenance technician's infrared field report",
      "decision_point_description": "Deciding whether the infrared reading changed the working diagnosis of sensor calibration drift.",
      "affected_reasoning_operation": "Evidence interpretation and information weighting",
      "bias_specific_mechanism": "The participant gave greater weight to the continuously observed trend recorder data that fit the calibration hypothesis and discounted a conflicting field-specialist report as likely noise without checking it, thereby preserving the existing interpretation.",
      "manifestation_in_interview": "The participant contrasted the technician's reading unfavorably with the trend recorder, attributed the field reading to ambient heat or scan-angle inconsistency, and did not request a second scan or re-check his own trend interpretation.",
      "effect_on_reasoning_or_decision": "The infrared evidence did not change the participant's working diagnosis or prompt independent verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue.",
          "evidence_explanation": "The participant recognized the conflicting information but immediately contrasted it with trend data that confirmed his prior calibration hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said.",
          "evidence_explanation": "The participant's attention and trust remained with the confirming trend display, while the disconfirming field report was not mentally retained or weighted equally."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.",
          "evidence_explanation": "This shows one-sided skeptical treatment of the disconfirming field report while the confirming trend interpretation was not subjected to the same scrutiny."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the technician's specialty was probably more relevant to shell heating and that a report from another licensed operator would likely have been taken more seriously, but this awareness did not correct the in-the-moment information weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not provide a sufficient definition or mechanism for confirmation bias; the label is used from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Only one interview transcript was analyzed; no independent outcome or procedure data were available.",
    "The retrieved scientific passages were sparse for some labels, especially plan continuation bias and confirmation bias, so those labels rely on general cognitive-science and human-factors knowledge.",
    "The interview is retrospective and de-identified; it may omit contextual details that would affect interpretation of the reasoning."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_6_Sonar_on",
  "interview_id": "NP_Biased_6",
  "system_prompt_id": "Sonar",
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
