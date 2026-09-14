You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down for this. This is a voluntary debrief for our operational learning file, not disciplinary. Can you tell me your role that shift and what the plan was?

Participant: Sure. I was Control Room Supervisor on dayshift. We were about five days past a refueling outage, running a scheduled ascension from 45 up to a 75 percent hold point. Standard evolution — controlled rod withdrawals, watching secondary parameters track along. Management wanted us at the hold point that day for a grid commitment, so there was a schedule to keep, but nothing forcing anyone's hand. Turnover wasn't a factor — I was only a few hours into the shift, still had most of it ahead of me.

Interviewer: What was your general read on plant status as the shift moved into the middle stretch?

Participant: Pretty routine. Ascensions like this usually throw a couple small things at you — nothing alarming, just things worth tracking. That's what happened here.

Interviewer: Walk me through the incident as it unfolded.

Participant: About two hours in, the reactor operator flagged that feedwater pump 1B's discharge pressure had a slow upward oscillation — vibration monitor ticking up too, still well within the normal band, no alarm. I had him log it and bump up the monitoring interval rather than pulling in the system engineer right away, since nothing was abnormal enough yet to justify an operability call. About forty minutes later, during a rod withdrawal, we got a brief blip in steam generator B's narrow range level — auto control caught it in seconds. Small thing, but two developing items at once gets your attention. I called our on-call reactor engineer, walked him through it, and he said it looked consistent with known control response at that power level. Level stayed stable after that.

Then, later in the shift, the pump vibration had crept up again — now sitting in the upper third of its normal band. Still no tech spec limit reached, no alarm. But it had been trending the same direction for a while, and I was pulling together materials for a surveillance test pre-brief due in about forty-five minutes, on top of the ascension schedule. I told the crew to keep it on the standard continue-and-monitor watch we use for that kind of trend, and we carried on toward the next hold point. During the pre-brief itself, the test coordinator asked an unrelated procedural question that happened to touch on the vibration item, and I mentioned it in passing without going into detail. About ninety minutes after that, the pump ended up on a formal close-monitoring action under a tech spec statement — the trend kept climbing. I pulled the historical comparison myself later that shift, once the pre-brief wrapped up.

Interviewer: Let's go through that in order. First, the pump reading forty minutes in — what informed logging it and increasing monitoring instead of calling the engineer immediately?

Participant: There wasn't much to react to yet — within the band, no real trend history to speak of. Calling the engineer for every early wobble creates noise. Tightening the interval was the right first move; escalate if it keeps climbing.

Interviewer: And the level blip — what made you check with the on-call engineer rather than rely on your own read?

Participant: Auto control handled it fine, so it wasn't urgent operationally. But two things trending at once during an ascension makes you want a second opinion, especially something with a control-system explanation I wanted verified rather than assumed.

Interviewer: Now the point where vibration crossed into the upper third of the band while you were assembling pre-brief materials. What options did you weigh, and what pushed you toward the standard response?

Participant: That's the one I've turned over the most. I had three things going — the pump, the pre-brief prep, and the ascension clock. The continue-and-monitor approach is what we've used for trends like this before, and it's worked, so that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could've done — the data was right there — but between the pre-brief materials and the schedule, it didn't feel necessary in that window. It wasn't that I decided the comparison was pointless, I just didn't work it in.

Interviewer: Did you consider holding the ascension until the engineer completed a documented review?

Participant: Briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before. So I went with what I knew rather than stopping to build a fuller comparison right then.

Interviewer: How much did the upcoming pre-brief shape that, compared to if nothing else had been due?

Participant: Some. When you're building out pre-brief materials and tracking an ascension schedule at the same time, you lean on what's familiar instead of starting fresh on every item. If I'd had a totally open stretch, I probably would've poked at the historical data just out of curiosity. In hindsight, the rate of rise on that trend was a bit different from the earlier cases I was drawing on, but I didn't do the side-by-side to notice that at the time.

Interviewer: During the pre-brief, what determined how much you said about the vibration trend?

Participant: I mentioned it in passing when the coordinator's question happened to touch on it — kept it brief since it wasn't the topic of that meeting and it was already framed as a monitor-and-continue item in my head. I figured I'd circle back to it once we were done.

Interviewer: You mentioned pulling the historical comparison yourself afterward. What prompted that, given there was no handoff forcing your hand?

Participant: Once the pre-brief wrapped, it was one of the first things on my list — nobody was waiting on me to hand it off, but it had been nagging at me a bit. The comparison showed the rate of climb didn't quite match the earlier benign cases.

Interviewer: If nothing else had been competing for your attention at that moment on the ascension, would you have handled the vibration trend differently?

Participant: Probably would've pulled the comparison right then instead of after the pre-brief. Having one clear task instead of two changes what feels worth doing in the moment versus what can wait.

Interviewer: If that comparison data had been sitting in front of you right when the trend crossed into the upper third of the band, do you think it would have changed your decision?

Participant: Possibly. If it had shown the rate of rise was outside what we'd seen before, I'd have leaned toward holding rather than continuing. But at the time I was working off what had worked previously, not off that specific comparison.

Interviewer: What would you tell a newer supervisor about handling a trending-but-not-alarming parameter when something else, even something unrelated, is pulling at your attention?

Participant: That divided attention narrows what you actually look at, even without a handoff involved. The item that ends up mattering isn't always the one making noise — sometimes it's the one you've already decided you understand.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Counterfactual_1",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Shift Supervisor / Control Room Supervisor (Nuclear)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Feedwater Pump Vibration Trend During Power Ascension Under Generic Mid-Shift Workload (No Imminent Turnover)",
    "scenario_summary_internal": "This is a causal counterfactual paired with NP_Biased_1. The same feedwater pump vibration trend and steam generator level oscillation occur during the same power ascension, but the shift-turnover deadline that created competing demands at decision point 3 is replaced with an equivalent-magnitude, non-handoff competing task (coordinating a time-boxed pre-brief for an unrelated scheduled surveillance test). Total workload and time pressure at decision point 3 are held constant; only the specific presence of an imminent handoff obligation is removed. The single Imperfect Rationality instance is preserved at the same decision point and mechanism, testing whether the earlier scenario's bounded-rationality response depended specifically on turnover-driven urgency or persisted under generic competing-task pressure.",
    "occupational_realism": {
      "objective": "Safely complete a scheduled power ascension from 45% to 75% reactor power following a refueling outage while maintaining all technical specification limits and equipment operability.",
      "setting": "Main control room of a pressurized water reactor unit, mid-shift during a multi-hour power ascension. Shift turnover is approximately 4 hours away (not imminent); a scheduled surveillance test briefing is due in about 45 minutes.",
      "constraints": [
        "Ascension schedule set by plant management with grid commitment pressure",
        "Limited on-shift technical staff (one reactor engineer available by phone, not on-site)",
        "A time-boxed pre-brief for an unrelated scheduled surveillance test is due in ~45 minutes, requiring preparatory documentation",
        "Technical specification action statements with defined time clocks",
        "Concurrent minor anomalies competing for supervisory attention"
      ],
      "stakeholders": [
        "Control Room Supervisor (interviewee)",
        "Reactor Operator at the controls",
        "Balance-of-Plant Operator",
        "Shift Technical Advisor",
        "Surveillance test coordinator (arriving for pre-brief)",
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
        "surveillance test pre-brief",
        "operability determination"
      ],
      "technical_terms_to_avoid": [
        "bounded rationality",
        "satisficing",
        "cognitive bias",
        "heuristic",
        "imperfect rationality",
        "shift turnover"
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
          "A surveillance test pre-brief is due in ~45 minutes and the CRS is simultaneously assembling the pre-brief materials; shift turnover is roughly 4 hours away and not an immediate factor",
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
        "intended_action": "CRS applies the familiar checklist-based 'continue and monitor' response used successfully in past similar-looking events, without pulling the fuller comparative trend data, in order to keep pace with the ascension schedule and finish the surveillance pre-brief materials on time."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vibration trend has been logged as 'continue and monitor' status in the CRS's pre-brief notes",
          "Surveillance test coordinator is arriving in 10 minutes for the pre-brief",
          "No new alarms or technical specification entries exist at this point",
          "No handoff to another supervisor is pending; the CRS remains on shift for several more hours"
        ],
        "new_information_after_decision": [
          "During the pre-brief, the test coordinator asks an unrelated procedural question that briefly surfaces the vibration item, and the CRS mentions it only in passing",
          "Later that shift, the CRS independently revisits the item and pulls the historical comparison after the pre-brief concludes"
        ],
        "alternatives": [
          "Mention the vibration trend only in passing during the pre-brief and return to it later without a specific plan",
          "Set aside a fixed time after the pre-brief to personally pull and review the historical comparison",
          "Delegate the historical comparison to the Balance-of-Plant Operator immediately, in parallel with the pre-brief"
        ],
        "intended_action": "CRS mentions the trend briefly during the pre-brief and privately resolves to pull the historical comparison personally once the pre-brief is finished, since no handoff obligation forces an immediate decision either way."
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
        "What did the period right before the surveillance test pre-brief look like?"
      ],
      "decision_point_probes": [
        "At the point you decided to just increase monitoring rather than call the engineer right away, what informed that choice?",
        "When you paused to call the on-call engineer about the level oscillation, what made you decide to check with him rather than continue on your own judgment?",
        "When the vibration trend crossed into the upper third of the band while you were also preparing the surveillance pre-brief, what options did you consider, and what made you choose to continue with the standard monitoring response?",
        "During the pre-brief itself, what determined how much you said about the vibration trend?"
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
        "How much did the upcoming surveillance test pre-brief affect how you handled the vibration trend, compared to if nothing else had been due?",
        "How confident were you in the vibration data at the time, and what would have increased that confidence?"
      ],
      "prior_experience": [
        "Had you seen a similar vibration trend before, and how did that experience shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If nothing else had been competing for your attention at that moment, would you have handled the vibration trend differently?",
        "If the historical comparison data had been sitting right in front of you at that moment, do you think it would have changed your decision?",
        "What would you tell a newer supervisor about handling a trending-but-not-yet-alarming parameter when another task is pulling at your attention, even without a handoff involved?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3,
        "mechanism": "Under concurrent cognitive load from an unrelated but comparably demanding competing task (surveillance test pre-brief preparation, not a handoff), and with an ascension schedule to maintain, the CRS selects a familiar, previously successful checklist response ('continue and monitor') without fully retrieving or integrating available comparative evidence (plant computer historical trend library), settling for a satisfactory rather than fully evaluated option.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_available_at_time": [
          "Vibration trend crossing into upper third of normal band",
          "Plant computer historical trend library accessible but not consulted",
          "Ascension schedule and surveillance pre-brief deadline creating competing demands",
          "Prior similar-looking events resolved benignly using the same checklist response"
        ],
        "required_textual_manifestation": "CRS explicitly states they applied the standard/familiar monitoring response because it had worked before and attention was divided by the pre-brief preparation, and did not pull or compare the historical vibration signature before continuing ascension, despite acknowledging the comparison was accessible.",
        "plausible_nonbias_interpretation": "A reasonable supervisor might legitimately deprioritize a non-alarming, within-limits parameter to meet real scheduling and preparatory constraints; the response only counts as an instance because the interview must also show that full evaluation was feasible and consciously foregone rather than genuinely impossible.",
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
      "paired_scenario_id": "NP_Biased_1",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual specification, not a zero-bias control."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence of an imminent shift-turnover handoff obligation at decision point 3",
      "original_state": "Shift turnover approaching in ~45 minutes, requiring the CRS to draft and finalize a turnover brief for the oncoming crew concurrently with monitoring the vibration trend.",
      "counterfactual_state": "No shift turnover during this window (turnover ~4 hours away); instead, the CRS is preparing a time-boxed pre-brief for an unrelated scheduled surveillance test due in ~45 minutes, producing an equivalent-magnitude competing-task deadline without any handoff or crew-continuity obligation.",
      "variables_to_hold_constant": [
        "Feedwater pump 1B vibration trend magnitude and timing",
        "Steam generator level oscillation event and its resolution",
        "Ascension schedule and power hold-point timing",
        "Staffing levels and on-call engineer availability",
        "Accessibility of the plant computer historical trend library",
        "Alternatives available at all four decision points",
        "Imperfect Rationality occurrence count (1), decision point (3), mechanism, and strength"
      ],
      "expected_causal_difference": "If the earlier satisficing response was driven specifically by handoff-related urgency (needing to finalize a brief for another person), removing the handoff obligation while preserving equivalent generic workload should be tested for whether the same 'continue and monitor' response, and the same omission of the historical comparison, still occurs, and whether Phase 4 behavior (no handoff pressure) differs from the original turnover handoff behavior.",
      "causal_test_question": "Does the imperfect-rationality response at decision point 3 persist when the competing task is a non-handoff deadline of equivalent magnitude, or was it specifically produced by the impending crew turnover?"
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two alternatives, mirroring NP_Biased_1's structure.",
      "Exactly one Imperfect Rationality instance is embedded, located at decision point 3, matching the base scenario's occurrence count.",
      "Only the causal variable (imminent handoff obligation vs. equivalent non-handoff deadline) differs materially from NP_Biased_1; all other facts, magnitudes, and timings are held constant.",
      "Phase 4 no longer involves a turnover handoff, consistent with the removed causal variable, while preserving a comparable decision structure and no additional bias instance.",
      "No bias-name vocabulary or psychological terminology appears in probes or intended interview content.",
      "Decision points 1, 2, and 4 contain no intentionally embedded instance of Imperfect Rationality or any other named bias.",
      "The Phase 3 manifestation remains distinguishable from ordinary competing-task prioritization by explicit acknowledgment that fuller comparative evidence was accessible but not consulted.",
      "Consequences do not conclusively prove bias; they remain consistent with a defensible, if suboptimal, judgment call.",
      "Target interview length 1,350 words (range 1,215-1,485) is achievable given four decision points and the probe plan without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
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
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Under concurrent cognitive load from a non-handoff competing task (surveillance pre-brief preparation) and ascension schedule pressure, CRS selects a familiar 'good enough' checklist response over full evaluation of accessible comparative vibration trend data, satisficing rather than optimizing the continue/hold decision.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_source": "Plant computer historical vibration trend library (accessible but not consulted) versus prior similar-event checklist experience",
        "distinctiveness_requirement": "Must show that full evaluation was feasible (data accessible) and consciously foregone in favor of a familiar heuristic response, and that this occurs even absent a handoff obligation, distinguishing it from mere reasonable time-constrained prioritization tied specifically to turnover."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "NP_Biased_1",
    "counterfactual_variable": {
      "name": "Presence of an imminent shift-turnover handoff obligation at decision point 3",
      "original_state": "Shift turnover approaching in ~45 minutes, requiring the CRS to draft and finalize a turnover brief for the oncoming crew concurrently with monitoring the vibration trend.",
      "changed_state": "No shift turnover during this window (turnover ~4 hours away); CRS instead prepares a time-boxed pre-brief for an unrelated scheduled surveillance test due in ~45 minutes, producing an equivalent-magnitude competing-task deadline without a handoff obligation.",
      "variables_to_hold_constant": [
        "Feedwater pump 1B vibration trend magnitude and timing",
        "Steam generator level oscillation event and its resolution",
        "Ascension schedule and power hold-point timing",
        "Staffing levels and on-call engineer availability",
        "Accessibility of the plant computer historical trend library",
        "Alternatives available at all four decision points",
        "Imperfect Rationality occurrence count, decision point, mechanism, and strength"
      ]
    },
    "scenario_id": "NP_Counterfactual_1",
    "domain_id": "NP",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to decision point 3, identical to the paired base scenario NP_Biased_1, per allocation rules 2 and 3, to isolate the effect of the counterfactual causal variable while holding the bias mechanism, decision point, and strength constant.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Feedwater pump 1B vibration trend magnitude and timing",
      "Steam generator level oscillation event and its resolution",
      "Ascension schedule and power hold-point timing",
      "Staffing levels and on-call engineer availability",
      "Accessibility of the plant computer historical trend library",
      "Alternatives available at all four decision points",
      "Imperfect Rationality occurrence count (1), decision point (3), mechanism, and strength"
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
          "segment_type": "initial monitoring decision rationale",
          "raw_interview_anchor": "There wasn't much to react to yet — within the band, no real trend history to speak of. Calling the engineer for every early wobble creates noise. Tightening the interval was the right first move; escalate if it keeps climbing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A within-band early wobble is logged and monitored more frequently; the participant gives a plausible escalation threshold and no hidden bias is embedded here."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "second-opinion decision rationale",
          "raw_interview_anchor": "Auto control handled it fine, so it wasn't urgent operationally. But two things trending at once during an ascension makes you want a second opinion, especially something with a control-system explanation I wanted verified rather than assumed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant seeks an engineer check because two items trend concurrently and the control-system explanation should be verified; this is ordinary cautious reasoning."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "continue-or-hold decision under competing workload",
          "raw_interview_anchor": "That's the one I've turned over the most. I had three things going — the pump, the pre-brief prep, and the ascension clock. The continue-and-monitor approach is what we've used for trends like this before, and it's worked, so that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could've done — the data was right there — but between the pre-brief materials and the schedule, it didn't feel necessary in that window.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ir_cf_01"
          ],
          "ground_truth_rationale": "Under concurrent non-handoff workload and ascension pressure, the participant chooses a familiar satisfactory response and consciously defers accessible comparative data, which is the hidden Imperfect Rationality manifestation."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "pre-brief communication choice",
          "raw_interview_anchor": "I mentioned it in passing when the coordinator's question happened to touch on it — kept it brief since it wasn't the topic of that meeting and it was already framed as a monitor-and-continue item in my head.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant makes a communication-scope choice during an unrelated pre-brief; no additional hidden bias instance is specified."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "post-pre-brief resource-allocation rationale",
          "raw_interview_anchor": "Once the pre-brief wrapped, it was one of the first things on my list — nobody was waiting on me to hand it off, but it had been nagging at me a bit. The comparison showed the rate of climb didn't quite match the earlier benign cases.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "After the competing task ends, the participant independently retrieves the comparison; this follow-up contains no separate hidden instance."
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
    "analysis_scope_note": "Mechanism-first review of a single operational debrief narrative. One occurrence of insufficiently adjusted reference-based reasoning was identified with moderate confidence; a possible plan-continuation bias was noted only as a candidate."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": [
        "Anchoring heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A reasoning heuristic in which a judgment or plan is grounded in an initial reference point, and later adjustment from that reference is insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Managing the rising 1B feedwater pump vibration trend during ascension and pre-brief preparation",
      "decision_point_description": "When pump vibration entered the upper third of its normal band while the participant was preparing pre-brief materials, he chose the standard continue-and-monitor path rather than pulling historical comparison data or holding the ascension.",
      "affected_reasoning_operation": "Updating an operational/diagnostic assessment in response to a developing trend and selecting the appropriate investigative or conservative action.",
      "bias_specific_mechanism": "The participant initially interpreted the pump vibration as a familiar 'continue-and-monitor' item. That initial reference point remained dominant as later upward trend information emerged, so his adjustment to the changing trend was insufficient: he proceeded from the familiar prior response rather than building a current, specific comparison.",
      "manifestation_in_interview": "The participant explicitly described leaning on earlier benign cases and the standard checklist response instead of pulling available plant-computer historical data. He later observed that the rate of rise differed from the earlier cases he had been drawing on.",
      "effect_on_reasoning_or_decision": "He did not retrieve already available historical comparison data at the time and did not hold the ascension, continuing the existing monitoring path and delaying recognition of a different rate-of-rise trend until after the pre-brief.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The continue-and-monitor approach is what we've used for trends like this before, and it's worked, so that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could've done — the data was right there — but between the pre-brief materials and the schedule, it didn't feel necessary in that window. It wasn't that I decided the comparison was pointless, I just didn't work it in.",
          "evidence_explanation": "Shows the familiar prior response serving as the reference path and the decision not to pull disambiguating data based on that initial frame."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before. So I went with what I knew rather than stopping to build a fuller comparison right then.",
          "evidence_explanation": "Indicates reliance on prior similar situations and 'what I knew' rather than constructing a current, trend-specific comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When you're building out pre-brief materials and tracking an ascension schedule at the same time, you lean on what's familiar instead of starting fresh on every item. If I'd had a totally open stretch, I probably would've poked at the historical data just out of curiosity. In hindsight, the rate of rise on that trend was a bit different from the earlier cases I was drawing on, but I didn't do the side-by-side to notice that at the time.",
          "evidence_explanation": "Confirms the use of a familiar reference class and absent side-by-side comparison; the participant himself identifies that the actual trend differed from the earlier cases he had drawn on."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time I was working off what had worked previously, not off that specific comparison.",
          "evidence_explanation": "Directly states that the decision was driven by prior successful cases rather than current specific comparison, which is the anchoring-and-insufficient-adjustment pattern."
        }
      ],
      "correction_or_counterevidence": "The parameter remained within its normal band with no alarm or tech-spec limit exceeded at the time; the standard continue-and-monitor response had covered similar-looking situations before; pre-brief and ascension schedule created a plausible time-pressure/efficiency explanation; and the participant later self-initiated the historical comparison after the pre-brief, allowing him to detect the differing rate of rise.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by the retrieved engineering-cognitive-bias passage on anchoring and adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, \"adjustments are typically insufficient.\" ... Although the phenomenon was initially described in ... anchoring on initial values when arriving at numerical estimates, the results have been found to hold in more general cases. One arena in engineering where this can be seen is in the use of socalled \"heritage\". ... the initial idea people have in mind when they first consider a problem can dominate the entire development process.",
          "mechanism_supported_by_source": "Judgments become tied to an initial reference point, and later adjustment from that reference is typically insufficient; this can appear in engineering settings when an initial familiar or legacy idea dominates subsequent reasoning.",
          "relevance_to_this_occurrence": "The participant's initial familiar monitor-and-continue interpretation of the pump vibration appears to have dominated later reasoning despite an upward trend, matching the passage's description of insufficient adjustment from an engineering reference."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis",
        "Plan continuation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Deciding whether to hold the ascension while the pump vibration trend was rising",
      "supporting_interview_quote": "Briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before. So I went with what I knew rather than stopping to build a fuller comparison right then.",
      "plausible_mechanism": "A tendency to continue an original plan or operational sequence despite emerging cues that might warrant pausing or revising the plan.",
      "why_not_identified": "The continuation was supported by the parameter remaining within limits and by an explicit standard response. The evidence also overlaps substantially with the anchoring-and-adjustment mechanism, so an independent plan-continuation bias could not be isolated with sufficient confidence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrospective self-report may be influenced by hindsight or post-event rationalization.",
    "No normative benchmark for the operational decision was available; the parameter remained within limits, so a non-bias efficiency/threshold-based explanation remains plausible.",
    "The retrieved corpus provides general support for anchoring-and-adjustment in engineering, but not a direct experimental analogue to control-room trend monitoring."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Counterfactual_1_Sonar_on",
  "interview_id": "NP_Counterfactual_1",
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
