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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
