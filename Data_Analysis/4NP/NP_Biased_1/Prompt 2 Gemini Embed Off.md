You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operational learning file, not a disciplinary review — anything you share helps us understand decision-making under real shift conditions. Can you start by telling me your role that shift and what the overall plan was?

Participant: Sure. I was the Control Room Supervisor on dayshift. We were about five days past a refueling outage, doing a scheduled ascension from 45 percent up to a 75 percent hold point. Standard stuff — controlled rod withdrawals, watching turbine and secondary parameters track along with it. Management wanted us at the hold point by end of shift because of a grid commitment, so there was a real schedule to keep, but nothing that should've forced anyone's hand.

Interviewer: What was your general sense of plant status as the shift moved into the middle stretch?

Participant: Pretty routine, honestly. Ascensions like this usually throw a couple of small things at you — nothing alarming, just things worth tracking. That's basically what happened.

Interviewer: Walk me through the incident as it unfolded.

Participant: About two hours in, the reactor operator flagged that feedwater pump 1B's discharge pressure had a slow upward oscillation going on — vibration monitor was ticking up too, still well within the normal band, no alarm. I had him log it and bump up the monitoring interval rather than pulling in the system engineer right away, since there was nothing abnormal enough to justify an operability call yet. About forty minutes later, during a rod withdrawal, we got a brief blip in steam generator B's narrow range level — auto control caught it in seconds. Small thing, but two developing items at once gets your attention. I called our on-call reactor engineer, walked him through it, and he said it looked consistent with known control response at that power level. Level stayed stable after that.

Then, closer to the end of the shift — turnover was maybe forty-five minutes out and I was drafting the brief — the pump vibration had crept up again, now sitting in the upper third of its normal band. Still no tech spec limit reached, no alarm. But it had been trending the same direction for a while now, and I was juggling the turnover paperwork, the ascension schedule, and this pump at the same time. I told the crew to keep it on the standard continue-and-monitor watch we use for that kind of trend and we carried on toward the next hold point. About ninety minutes after I left, I heard they ended up putting the pump on a formal close-monitoring action under a tech spec statement — the trend kept climbing. When I handed over, I'd mentioned the vibration item but didn't flag it as something the oncoming crew needed to dig into specifically.

Interviewer: Let's go back through that in order. First, the pump reading forty minutes in — what informed the choice to just log it and increase monitoring instead of contacting the engineer immediately?

Participant: At that point there wasn't much to react to — it was within the band, no trend history yet to speak of. Calling the engineer for every early wobble would just create noise. Tightening the monitoring interval was the appropriate first move; if it kept climbing, that's when you escalate.

Interviewer: And the steam generator level blip — what made you decide to check with the on-call engineer rather than rely on your own read of it?

Participant: The auto control handled it fine, so operationally it wasn't urgent. But two things trending at once during an ascension makes you want a second opinion, especially on something with a control-system explanation I wanted verified rather than assumed. That's just good practice at that stage — get an independent read before you write it off.

Interviewer: Now the point where the vibration crossed into the upper third of the band, forty-five minutes before turnover, while you were writing the brief. What options did you weigh, and what pushed you toward the standard monitoring response?

Participant: Honestly, that's the one I've turned over the most since. I had three things going — the pump, the turnover brief, and the schedule to the next hold point. The continue-and-monitor approach is what we've used for trends like this in the past, and it's worked. So that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could have done — the data was sitting right there — but between the paperwork and the ascension clock, it didn't feel necessary at the time. It wasn't that I decided the comparison wouldn't be useful, I just didn't work it into what I was doing in that window.

Interviewer: Did you consider holding the ascension at that point until the engineer completed a documented review?

Participant: I thought about it briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before without issue. So I went with what I knew rather than stopping to build out a fuller comparison right then.

Interviewer: How much do you think the approaching turnover shaped that choice?

Participant: Some, for sure. When you're consolidating a brief and tracking an ascension schedule at the same time, you lean on what's familiar rather than starting from scratch on every item. In hindsight, the rate of rise on that trend was a bit different from the earlier cases I was drawing on, but I didn't do the side-by-side at the time to notice that.

Interviewer: Last decision point — writing the turnover note itself. What determined how much detail you included on the vibration trend?

Participant: I mentioned it as an ongoing watch item, consistent with how I'd been treating it all shift. I didn't specifically ask the oncoming crew to pull the historical comparison — it was already framed as monitor-and-continue in my head, so that's how it went into the notes.

Interviewer: The oncoming supervisor apparently asked about it directly and requested that comparison be done. What do you make of that?

Participant: Fair question on their part — fresh eyes on a trend that's been running a while will do that. The comparison afterward showed the rate of climb didn't quite match the earlier benign cases. That's useful information; I just hadn't had it in front of me during my shift.

Interviewer: If you'd had another hour before turnover, would you have handled the vibration trend differently?

Participant: Probably would've pulled the historical comparison myself rather than leaving it for the next crew. An hour changes what feels worth doing versus what feels like it can wait.

Interviewer: If that comparison data had been sitting in front of you at the moment the trend crossed into the upper third of the band, do you think it would have changed your decision?

Participant: Possibly. If it had shown the rate of rise was outside what we'd seen before, I'd have leaned toward holding rather than continuing. But at the time I was working off what had worked previously, not off that specific comparison.

Interviewer: What would you tell a newer supervisor about handling a trending-but-not-alarming parameter close to turnover?

Participant: That the workload right before turnover can quietly narrow what you actually look at. The item that ends up mattering most isn't always the one making noise — sometimes it's the one you've already decided you understand.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_1",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Shift Supervisor / Control Room Supervisor (Nuclear)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Feedwater Pump Vibration Trend During Power Ascension at Shift Turnover",
    "scenario_summary_internal": "During a post-refueling power ascension, the Control Room Supervisor (CRS) manages a developing feedwater pump vibration trend alongside a minor steam generator level control anomaly, while under time pressure from an approaching shift turnover and a management-driven ascension schedule. Cognitive load from tracking multiple concurrent, moderately abnormal parameters leads the CRS to select a familiar, procedurally 'good enough' response at one decision point rather than fully working through the available trend data and alternative hypotheses, illustrating bounded/imperfect rationality rather than a knowledge gap or willful risk-taking.",
    "occupational_realism": {
      "objective": "Safely complete a scheduled power ascension from 45% to 75% reactor power following a refueling outage while maintaining all technical specification limits and equipment operability.",
      "setting": "Main control room of a pressurized water reactor unit, mid-shift during a multi-hour power ascension, approximately 45 minutes before scheduled shift turnover.",
      "constraints": [
        "Ascension schedule set by plant management with grid commitment pressure",
        "Limited on-shift technical staff (one reactor engineer available by phone, not on-site)",
        "Shift turnover approaching, requiring status consolidation and handoff",
        "Technical specification action statements with defined time clocks",
        "Concurrent minor anomalies competing for supervisory attention"
      ],
      "stakeholders": [
        "Control Room Supervisor (interviewee)",
        "Reactor Operator at the controls",
        "Balance-of-Plant Operator",
        "Shift Technical Advisor",
        "Oncoming shift crew",
        "System Engineer (feedwater), on-call",
        "Plant Operations Manager"
      ],
      "technical_terms_to_use": [
        "feedwater pump discharge pressure",
        "vibration trend",
        "technical specification action statement",
        "steam generator narrow range level",
        "power ascension rate",
        "control room log",
        "shift turnover brief",
        "operability determination"
      ],
      "technical_terms_to_avoid": [
        "bounded rationality",
        "satisficing",
        "cognitive bias",
        "heuristic",
        "imperfect rationality"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Feedwater pump 1B discharge pressure showing a slow upward oscillation over the last 40 minutes",
          "Vibration monitor reading within normal band but trending upward",
          "No alarm has actuated; parameter is within technical specification limits"
        ],
        "new_information_after_decision": [
          "Vibration continues a shallow upward trend over the next hour without alarming",
          "Reactor Operator notes the trend during a routine log entry"
        ],
        "alternatives": [
          "Log the trend and continue routine monitoring at current interval",
          "Increase monitoring frequency and request an early vibration data pull from the plant computer",
          "Contact the feedwater system engineer immediately for a preliminary assessment"
        ],
        "intended_action": "CRS directs increased monitoring frequency and logs the trend, deferring engineer contact pending further data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Steam generator 'B' narrow range level shows a brief, minor oscillation during a routine rod movement",
          "Level control system compensates automatically within seconds",
          "No technical specification limit approached"
        ],
        "new_information_after_decision": [
          "Level stabilizes and no further oscillation occurs during the next two rod movements",
          "Reactor Engineer, contacted by phone, states the oscillation is consistent with known control system response characteristics at this power level"
        ],
        "alternatives": [
          "Treat the oscillation as expected control system behavior and continue ascension",
          "Pause ascension briefly to review control system response with the on-call engineer before continuing",
          "Request the Shift Technical Advisor perform an independent operability review before continuing"
        ],
        "intended_action": "CRS pauses briefly, confers with the on-call engineer by phone, and resumes ascension after receiving a verbal assessment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Feedwater pump 1B vibration has now crossed into the upper third of the normal operating band, continuing its earlier trend",
          "Steam generator level control has remained stable since Phase 2",
          "Shift turnover is 45 minutes away and the CRS is simultaneously drafting the turnover brief",
          "Technical specification limit for the vibration parameter has not been reached; no alarm is active",
          "The ascension schedule calls for continuing to the next power hold point within the hour"
        ],
        "new_information_after_decision": [
          "Approximately 90 minutes later, vibration trend continues rising and the pump is placed on close monitoring per a separate technical specification action",
          "Post-event review shows the vibration data pattern was distinguishable from prior similar events on the plant computer, had it been pulled and compared at Phase 3"
        ],
        "alternatives": [
          "Apply the standard 'continue and monitor' checklist response used for prior minor vibration trends, without pulling comparative historical data",
          "Pull and compare the current vibration signature against the plant computer's historical trend library before deciding whether to continue ascension",
          "Hold the ascension at the current power level until the feedwater system engineer completes a documented review"
        ],
        "intended_action": "CRS applies the familiar checklist-based 'continue and monitor' response used successfully in past similar-looking events, without pulling the fuller comparative trend data, in order to keep pace with the ascension schedule and finish the turnover brief on time."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vibration trend has been logged as 'continue and monitor' status in the CRS's draft turnover notes",
          "Oncoming CRS is arriving in 10 minutes",
          "No new alarms or technical specification entries exist at this point"
        ],
        "new_information_after_decision": [
          "Oncoming CRS asks a clarifying question about the vibration trend during turnover and requests the historical comparison be pulled that shift",
          "Comparison later shows the trend pattern differed from prior benign cases in rate of rise"
        ],
        "alternatives": [
          "Hand over the vibration trend as a routine monitoring item with minimal elaboration",
          "Explicitly flag the trend as unresolved and request the oncoming crew prioritize a historical data comparison",
          "Delay turnover briefly to complete the comparison personally before handing over"
        ],
        "intended_action": "CRS hands over the item as a routine monitoring note, briefly mentioning the trend without flagging it as needing a specific follow-up comparison."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were responsible for that shift and what the plan was for the power ascension?",
        "What was your overall mental picture of plant status heading into the middle of the shift?"
      ],
      "timeline_reconstruction": [
        "What happened first with the feedwater pump readings, and when did you first notice it?",
        "Walk me through what happened with the steam generator level oscillation and how that unfolded.",
        "What was going on around the time the vibration trend crossed into the upper part of its normal band?",
        "What did the last part of the shift look like as you prepared the turnover?"
      ],
      "decision_point_probes": [
        "At the point you decided to just increase monitoring rather than call the engineer right away, what informed that choice?",
        "When you paused to call the on-call engineer about the level oscillation, what made you decide to check with him rather than continue on your own judgment?",
        "When the vibration trend crossed into the upper third of the band while you were also drafting the turnover brief, what options did you consider, and what made you choose to continue with the standard monitoring response?",
        "When you were writing the turnover note, what determined how much detail you included about the vibration trend?"
      ],
      "decision_basis": [
        "What specifically made the 'continue and monitor' response feel like the right call at that moment?",
        "Did you consider pulling the historical trend comparison data before continuing ascension? Why or why not?"
      ],
      "information_sources": [
        "What data sources did you have available on the plant computer at that time?",
        "Who did you talk to before making each of these calls, and what did they tell you?"
      ],
      "goals_and_alternatives": [
        "What competing priorities were you juggling at that point in the shift?",
        "Looking back, what other options were realistically available to you at that moment?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the approaching shift turnover affect how you handled the vibration trend?",
        "How confident were you in the vibration data at the time, and what would have increased that confidence?"
      ],
      "prior_experience": [
        "Had you seen a similar vibration trend before, and how did that experience shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If you'd had another hour before turnover, would you have handled the vibration trend differently?",
        "If the historical comparison data had been sitting right in front of you at that moment, do you think it would have changed your decision?",
        "What would you tell a newer supervisor about handling a trending-but-not-yet-alarming parameter near shift turnover?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3,
        "mechanism": "Under concurrent cognitive load (drafting turnover brief while tracking a slowly rising vibration trend, with an ascension schedule to maintain), the CRS selects a familiar, previously successful checklist response ('continue and monitor') without fully retrieving or integrating available comparative evidence (plant computer historical trend library), settling for a satisfactory rather than fully evaluated option.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_available_at_time": [
          "Vibration trend crossing into upper third of normal band",
          "Plant computer historical trend library accessible but not consulted",
          "Ascension schedule and turnover deadline creating competing demands",
          "Prior similar-looking events resolved benignly using the same checklist response"
        ],
        "required_textual_manifestation": "CRS explicitly states they applied the standard/familiar monitoring response because it had worked before and time was limited, and did not pull or compare the historical vibration signature before continuing ascension, despite acknowledging in the interview that the comparison was accessible.",
        "plausible_nonbias_interpretation": "A reasonable supervisor might legitimately deprioritize a non-alarming, within-limits parameter to meet real scheduling and staffing constraints; the response only counts as an instance because the interview must also show that full evaluation was feasible and consciously foregone rather than genuinely impossible.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "bounded rationality",
          "satisficing",
          "cognitive bias",
          "imperfect rationality",
          "heuristic"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition scenario; no paired control scenario was requested."
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
      "Exactly four decision points are present, each with at least two alternatives.",
      "Exactly one Imperfect Rationality instance is embedded, located at decision point 3.",
      "No bias-name vocabulary or psychological terminology appears in probes or intended interview content.",
      "Decision points 1, 2, and 4 contain no intentionally embedded instance of Imperfect Rationality or any other named bias.",
      "The Phase 3 manifestation is distinguishable from ordinary time-pressure prioritization by explicit acknowledgment that fuller comparative evidence was accessible but not consulted.",
      "Consequences (later vibration rise, later flagged by oncoming CRS) do not conclusively prove bias; they remain consistent with a defensible, if suboptimal, judgment call.",
      "Target interview length 1,350 words (range 1,215-1,485) is achievable given four decision points and the probe plan without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Imperfect Rationality",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Under concurrent cognitive load and time pressure at shift turnover, CRS selects a familiar 'good enough' checklist response over full evaluation of accessible comparative vibration trend data, satisficing rather than optimizing the continue/hold decision.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_source": "Plant computer historical vibration trend library (accessible but not consulted) versus prior similar-event checklist experience",
        "distinctiveness_requirement": "Must show that full evaluation was feasible (data accessible) and consciously foregone in favor of a familiar heuristic response, distinguishing it from mere reasonable time-constrained prioritization."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_1",
    "domain_id": "NP",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point offering the strongest mechanism fit and narrative realism: decision point 3, where concurrent cognitive load (turnover brief drafting), schedule pressure, and accessible-but-unused comparative evidence jointly support a distinguishable bounded-rationality manifestation, per allocation rules 2 and 3.",
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
          "segment_type": "plant-status interpretation",
          "raw_interview_anchor": "Pretty routine, honestly. Ascensions like this usually throw a couple of small things at you — nothing alarming, just things worth tracking.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Routine framing is not sufficient to establish the hidden Imperfect Rationality instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "initial monitoring decision",
          "raw_interview_anchor": "I had him log it and bump up the monitoring interval rather than pulling in the system engineer right away.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The initial within-limits monitoring decision is an intended non-bias decision point."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "engineering consultation decision",
          "raw_interview_anchor": "Two developing items at once gets your attention. I called our on-call reactor engineer.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Seeking an independent assessment for the level oscillation is an intended non-bias decision point."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "continue-or-hold decision",
          "raw_interview_anchor": "The continue-and-monitor approach is what we've used for trends like this in the past, and it's worked. ... Pulling the historical vibration comparison ... didn't feel necessary at the time.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ir_01"
          ],
          "ground_truth_rationale": "At decision point 3, the participant explicitly chose a familiar good-enough response while accessible comparative data was available but not consulted amid workload and turnover pressure."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "ascension-hold consideration",
          "raw_interview_anchor": "I thought about it briefly, but the trend hadn't broken any limit ... So I went with what I knew rather than stopping to build out a fuller comparison.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ir_01"
          ],
          "ground_truth_rationale": "This is part of the same phase-3 evidence-integration and option-evaluation episode."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "turnover communication decision",
          "raw_interview_anchor": "I mentioned it as an ongoing watch item ... I didn't specifically ask the oncoming crew to pull the historical comparison.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden occurrence is assigned to phase 3; the phase-4 handover choice is an intended non-bias decision point."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "reflection on fresh review",
          "raw_interview_anchor": "Fair question on their part — fresh eyes on a trend that's been running a while will do that.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a retrospective interpretation of the oncoming supervisor's request, without a separate hidden instance."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "time-counterfactual",
          "raw_interview_anchor": "If you'd had another hour before turnover, would you have handled the vibration trend differently? Probably would've pulled the historical comparison myself.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The counterfactual does not add a new hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "information-counterfactual",
          "raw_interview_anchor": "If it had shown the rate of rise was outside what we'd seen before, I'd have leaned toward holding rather than continuing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an unadopted counterfactual about information that was not available in the decision moment."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "closing guidance",
          "raw_interview_anchor": "The workload right before turnover can quietly narrow what you actually look at.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "General advice summarizes the episode but is not a separate hidden instance."
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
    "analysis_scope_note": "Single-interview transcript analyzed without supplied retrieved corpus passages; classifications rely on established cognitive-science criteria and are grounded solely in interview evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which the perceived likelihood or importance of an event is influenced by how easily similar instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Feedwater pump 1B vibration trending into upper third of normal band near shift turnover",
      "decision_point_description": "Whether to continue standard monitoring versus pull historical vibration comparison or hold the ascension when pump vibration reached the upper third of its normal band.",
      "affected_reasoning_operation": "Risk estimation and choice of monitoring/escalation response",
      "bias_specific_mechanism": "The supervisor relied on readily recalled prior cases where continue-and-monitor had succeeded, using ease and salience of those past outcomes as a substitute for retrieving and comparing the current trend's rate-of-rise data.",
      "manifestation_in_interview": "He explicitly reported choosing continue-and-monitor because similar past situations had worked and said he was working from what had worked previously rather than from the current specific comparison.",
      "effect_on_reasoning_or_decision": "The available historical comparison was not pulled, the trend was treated as a known monitoring item, and the ascension continued; post-shift comparison showed the rate of rise differed from prior benign cases.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The continue-and-monitor approach is what we've used for trends like this in the past, and it's worked. So that's the direction I went.",
          "evidence_explanation": "This directly states that recalled past success, not current diagnostic comparison, drove the monitoring decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time I was working off what had worked previously, not off that specific comparison.",
          "evidence_explanation": "This confirms the substitution of remembered outcomes for available current data, the core availability-heuristic mechanism."
        }
      ],
      "correction_or_counterevidence": "The vibration remained within normal band and below tech-spec limits, and standard monitoring was an established practice; these contextual factors support a non-bias contribution, so occurrence is moderate rather than high.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages were not supplied in the retrieval context; classification uses established cognitive-science criteria only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability that a current instance belongs to a category based on similarity to a prototype, often ignoring baseline rates or diagnostic features.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classification of vibration trend as benign based on apparent resemblance to earlier cases",
      "decision_point_description": "Whether the current feedwater pump vibration trend was sufficiently similar to prior benign cases to justify the same monitor-and-continue response.",
      "affected_reasoning_operation": "Diagnostic classification/probability judgment of equipment condition",
      "bias_specific_mechanism": "The supervisor classified the current trend as benign because it matched a stored prototype of previously encountered similar-looking pump vibration situations, without checking the diagnostic feature—the rate of rise—that distinguished this trend.",
      "manifestation_in_interview": "He used the phrase 'similar-looking situations before without issue' and later acknowledged the rate of rise was 'a bit different' from earlier cases, but he had not performed the side-by-side comparison.",
      "effect_on_reasoning_or_decision": "The category judgment of the trend as a benign monitoring item blocked a more specific comparison and contributed to continuing the ascension.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before without issue.",
          "evidence_explanation": "This shows the probability of a benign course was judged by surface similarity to remembered prior situations, a representativeness heuristic cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, the rate of rise on that trend was a bit different from the earlier cases I was drawing on, but I didn't do the side-by-side at the time to notice that.",
          "evidence_explanation": "This reveals that an important diagnostic feature was neglected while similarity to earlier cases drove the judgment."
        }
      ],
      "correction_or_counterevidence": "No alarm or tech-spec limit was exceeded, and many operational decisions reasonably rely on similarity to prior events; the bias is identified because the specific diagnostic comparison was available and would have differentiated the case.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages were not supplied in the retrieval context; classification uses established cognitive-science criteria only.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Anchoring effect",
      "alternative_labels": [
        "Anchoring bias",
        "Assessment anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency for an initial assessment or value to exert disproportionate influence on later judgments or communications.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Turnover brief preparation and handoff note content",
      "decision_point_description": "What level of specificity and escalation emphasis to give the pump vibration trend in the written or verbal shift handoff.",
      "affected_reasoning_operation": "Handoff communication and escalation framing",
      "bias_specific_mechanism": "The earlier monitor-and-continue assessment served as an anchor; when writing the turnover note, the supervisor carried that frame forward and did not adjust the note to request a historical comparison or specific investigation.",
      "manifestation_in_interview": "He stated the item went into the notes as an ongoing watch item because it was already framed as monitor-and-continue in his head.",
      "effect_on_reasoning_or_decision": "The oncoming crew received a generic watch item rather than a specific prompt to compare historical vibration data; the oncoming supervisor later had to request the comparison directly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I mentioned it as an ongoing watch item, consistent with how I'd been treating it all shift.",
          "evidence_explanation": "This shows the handoff content followed the earlier assessment rather than an independent re-evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't specifically ask the oncoming crew to pull the historical comparison — it was already framed as monitor-and-continue in my head, so that's how it went into the notes.",
          "evidence_explanation": "This explicitly identifies the earlier frame as the anchor that limited adjustment in the handoff communication."
        }
      ],
      "correction_or_counterevidence": "The vibration item was still documented as an ongoing watch item, so key information was not wholly absent. Retrospective self-report may emphasize causal consistency; this occurs at low confidence because ordinary consistency and legitimate continuity could partially explain the note wording.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages were not supplied in the retrieval context; classification uses established cognitive-science criteria only.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis",
        "Plan continuation error"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision not to pause the ascension despite a slowly worsening pump vibration trend",
      "supporting_interview_quote": "Management wanted us at the hold point by end of shift because of a grid commitment, so there was a real schedule to keep... I had three things going — the pump, the turnover brief, and the schedule to the next hold point.",
      "plausible_mechanism": "Schedule goal and commitment to the ascension may have biased the supervisor toward continuing the planned power ascension rather than pausing to investigate.",
      "why_not_identified": "The transcript does not provide sufficient evidence that the schedule goal, rather than the availability or representativeness heuristic or legitimate monitoring criteria, caused the continuation decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Late-shift treatment of pump vibration as a known monitor-and-continue item",
      "supporting_interview_quote": "sometimes it's the one you've already decided you understand.",
      "plausible_mechanism": "Once the vibration was framed as an understood monitoring item, the supervisor may have downplayed information that would challenge that frame and failed to seek disconfirming comparative data.",
      "why_not_identified": "The omission of the comparison is better explained by reliance on prior similar cases and workload; no evidence shows selective weighting or dismissal of disconfirming information."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were not supplied; therefore no corpus metadata or retrieved passage support is reported.",
    "Analysis is based on a retrospective interview; recall and self-presentation may influence reported cognition.",
    "The identified mechanisms overlap partially and share practical consequences; occurrence separation is based on distinct inferred mechanisms rather than wholly separate actions.",
    "The low-confidence anchoring occurrence is included because the participant explicitly described the frame transfer, but it is less certain as a distinct bias."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_1_Gemini_off",
  "interview_id": "NP_Biased_1",
  "system_prompt_id": "Gemini",
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
