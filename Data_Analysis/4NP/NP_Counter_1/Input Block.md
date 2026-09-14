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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
