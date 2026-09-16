You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operational learning file, not a disciplinary review — you can decline any question. Can you state your role and how long you've been in it?

Participant: Sure. I'm shift captain on nights, been supervising underground crews about nine years, this site for four. Before that I was a ground control tech, so I came up through that side.

Interviewer: Good. Let's start broad — walk me through what you knew at the start of the shift, before anything unusual happened.

Participant: Standard handover. Day shift left a note that there'd been a small seismic event overnight near Panel 3, magnitude around 1.1, logged as minor, within normal range for that ground. They also flagged some wet ground near the access drift — more seepage than usual, nothing alarming on its own. Production schedule had us blasting Panel 3 within the first couple hours, and mucking and haulage after that. That was the plan.

Interviewer: What was the main objective for the night?

Participant: Keep Panel 3 on schedule. We were behind for the week, so there was some pressure from the surface to not lose another shift. Safety first, obviously, but the blast cycle was already tight.

Interviewer: Take me through the incident itself, in order.

Participant: Okay. First couple hours were the blast — I authorized it after the ground control tech did a visual pass, no visible loose rock, so we went ahead as scheduled. Didn't call for an instrumented convergence check, just a visual scaling look, because the seismic event had been small and logged as normal range. Blast went fine, mucking started.

A while after that, microseismic monitoring started showing a cluster of small events near the panel next to our old mined-out area — not bigger events, just more of them, more frequent. Haul trucks run a road that passes under part of that adjacent panel, so I had to decide whether to keep hauling that route. Ventilation was reading normal across the circuit, no gas issues reported, so I let haulage continue as-is.

About fifteen minutes after trucks started moving again, a methane sensor near that haul intersection logged a brief spike, then went back to baseline. Ventilation officer logged it as transient, no recurrence, didn't think much of it at the time — that kind of blip happens.

Then we got the fall of ground. Small one, near the haul intersection, damaged a section of mesh, no injuries, but it needed re-support before we could keep running trucks through there.

Interviewer: When that happened, what did you think was going on?

Participant: Honestly, by that point it felt pretty clear. You had the seismic event overnight, the wet ground, then the seismic cluster building up near the old workings, plus the blast vibration from our own cycle — it all lined up. Stress transfer off the old mined-out panel, aggravated by the water getting into the joints and then our blast adding vibration on top. Once you saw it laid out like that, it made sense — it was almost the story you'd expect given that ground history.

Interviewer: And the methane spike from earlier?

Participant: That I set aside. It didn't fit with a ground stability event — different system, different sensor, and it hadn't recurred. Ventilation had already called it transient. I didn't loop back on it specifically once we had a ground explanation that accounted for everything else.

Interviewer: Let's go back through each decision point one at a time. Starting with the blast authorization — what alternatives did you weigh?

Participant: Three options really. Go ahead with just the visual check, delay and call for an instrumented geotech inspection, or go ahead but scale back charge size and add scaling time as a buffer. I went with the first. The seismic event was classified minor, the tech didn't see loose rock, and we were already behind schedule.

Interviewer: What cues mattered most there?

Participant: The classification on the seismic log, mostly. "Minor, within normal range" carries weight — that's the geotech team's own threshold, not something I'm second-guessing casually.

Interviewer: Any uncertainty at that point?

Participant: Some. The wet ground note nagged at me a little, but on its own it's common enough that shift.

Interviewer: Second decision — continuing haulage under the adjacent panel despite the seismic cluster.

Participant: I considered rerouting the trucks, or halting until the geotech engineer looked at the cluster. But it was frequency increasing, not magnitude — that pattern is something I've seen before near old workings settling out. Ventilation was clean. Given the schedule pressure, I let it continue.

Interviewer: Whose input did you lean on there, and whose didn't you seek?

Participant: Leaned on the ventilation officer's readings. Didn't call the on-call geotech engineer — he's not on-site overnight, and I judged the cluster wasn't urgent enough to wake him for.

Interviewer: Third — the fall of ground and the remediation decision. What alternatives existed?

Participant: I could've treated the cause as undetermined and ordered an instrumented investigation of both the ground and the gas anomaly before deciding on re-support. Or gotten the geotech engineer's real-time input before committing to any explanation. Instead I went with the stress-transfer account and had the crew re-support directly on that basis.

Interviewer: What made that explanation feel solid enough to act on without waiting for engineering input?

Participant: It tied together everything we'd seen that night in one line — the timing worked, the location worked, the mechanism was one I understood from my ground control days. When it clicks together that cleanly, you don't feel like you're guessing anymore.

Interviewer: Did anything not fit that account?

Participant: The methane spike, technically. But it was a single blip, different monitoring system, already logged as transient. It didn't feel like it belonged in the same picture as a ground support issue.

Interviewer: Fourth decision — resuming production after re-support.

Participant: Re-support was done, no new seismic or gas readings since the FOG, and we were losing more schedule the longer we sat. I could've resumed limited production with continued monitoring, or suspended the panel until formal sign-off. I resumed full production. The explanation held together and the repair was solid, so I didn't see a reason to hold back further.

Interviewer: How confident were you in the cause at that point, on reflection?

Participant: Pretty confident in the moment. Looking back, I'll admit the geotech engineer wanted the raw seismic and gas data before he'd sign off on it as the definitive cause — he mentioned it could also be a localized joint failure or even sensor drift, unrelated to the stress-transfer idea entirely.

Interviewer: What information, if you'd had it earlier, might have changed your read?

Participant: Probably the engineer's data review itself, before we committed to re-support. If that had flagged the methane sensor as a calibration issue right away, or ruled out joint failure, I'd have felt more sure. Without it, I was working off what fit together in front of me.

Interviewer: If the methane spike had recurred a second time that night, would that have changed anything?

Participant: Yeah, I think so. A repeat would've been harder to wave off as unrelated. One blip is easy to set aside; two starts looking like its own problem.

Interviewer: Looking back, what part of your explanation are you least sure about now?

Participant: Whether the stress transfer story was really the whole cause, or just the part that was easiest to see. The pieces fit together well enough that I didn't push hard on what didn't fit.

Interviewer: What would you tell a newer supervisor facing a similar sequence?

Participant: That a clean-sounding explanation isn't the same as a confirmed one — get the data checked even when the story already feels complete.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_1",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Underground Shift Supervisor / Mine Captain",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Panel 3 Fall of Ground: A Story That Fit Too Well",
    "scenario_summary_internal": "During a night production shift at an underground hard-rock mine, a shift supervisor manages a sequence of nonroutine signals — a minor overnight seismic event, wet ground conditions reported by the outgoing crew, elevated microseismic activity near an adjacent stope, and eventually a small fall of ground (FOG) near a haul route. The supervisor, under time and production pressure, assembles these signals into a single fluent causal narrative ('stress transfer from the old mined-out panel, aggravated by water and blast vibration') that feels complete and inevitable in hindsight. This coherent story shapes the remediation decision and causes a discordant methane sensor reading to be treated as an unrelated nuisance rather than independently investigated. The interview reconstructs the shift chronologically through four decision points, probing cues, evidence sources, alternatives considered, and the supervisor's confidence in the causal story after the fact.",
    "occupational_realism": {
      "objective": "Maintain safe, on-schedule ore production from Panel 3 while responding appropriately to evolving ground-control and gas-monitoring signals during a single night shift.",
      "setting": "A underground hard-rock mine (base-metal, room-and-pillar with adjacent mined-out panels), approximately 650m level, during a scheduled night production shift with a blast cycle and ore haulage in progress.",
      "constraints": [
        "Production quota tied to the shift's blast-and-muck cycle",
        "Limited geotechnical engineer availability (on-call, not on-site overnight)",
        "Ventilation and gas monitoring shared across multiple panels",
        "Historical mined-out area adjacent to active panel creates known but poorly quantified stress-transfer risk",
        "Crew fatigue near end of a run of night shifts",
        "Radio/telemetry lag between panel sensors and surface control room"
      ],
      "stakeholders": [
        "Underground Shift Supervisor / Mine Captain (interviewee)",
        "On-call geotechnical engineer",
        "Ventilation officer",
        "Haul truck operators",
        "Ground control / rock mechanics technician",
        "Mine control room dispatcher"
      ],
      "technical_terms_to_use": [
        "fall of ground (FOG)",
        "microseismic monitoring",
        "stress transfer",
        "rock bolts and mesh",
        "shotcrete",
        "ground support",
        "stope",
        "panel",
        "pillar",
        "backfill",
        "haul road",
        "blast vibration",
        "methane sensor / gas monitoring station",
        "ventilation circuit",
        "seismic event magnitude",
        "scaling (loose rock removal)"
      ],
      "technical_terms_to_avoid": [
        "narrative fallacy",
        "cognitive bias",
        "hindsight bias",
        "heuristic",
        "confirmation bias",
        "storytelling bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Outgoing day-shift report notes a magnitude-1.1 microseismic event near Panel 3 overnight, classified as 'minor, within normal range'",
          "Outgoing crew notes increased seepage/wet ground near the Panel 3 access drift",
          "Production schedule calls for a blast cycle in Panel 3 within the first two hours of shift",
          "No formal geotechnical inspection has been logged since the seismic event"
        ],
        "new_information_after_decision": [
          "Ground control technician does a visual scaling pass and finds no visible loose rock, but does not run instrumented convergence checks",
          "Blast proceeds as scheduled"
        ],
        "alternatives": [
          "Proceed with the scheduled blast after a brief visual check",
          "Delay the blast and request an instrumented geotechnical inspection before proceeding",
          "Proceed with blast but reduce charge size and add extra scaling time as a precaution"
        ],
        "intended_action": "Supervisor authorizes the blast after a visual-only check, prioritizing schedule continuity."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Microseismic monitoring shows a cluster of small events in the panel adjacent to the historical mined-out area, rising in frequency but not magnitude",
          "Haul trucks are routed along a haul road passing beneath a section of that adjacent panel",
          "Ventilation officer reports normal air quality readings across the circuit",
          "No FOG or damage has yet occurred"
        ],
        "new_information_after_decision": [
          "Haulage continues on schedule; no immediate ground issue observed",
          "A methane sensor near the haul road intersection logs a brief, unexplained spike about 15 minutes after trucking resumes, then returns to baseline"
        ],
        "alternatives": [
          "Continue haulage on the existing route without change",
          "Temporarily reroute haul trucks away from beneath the adjacent panel pending review",
          "Halt haulage entirely until the seismic cluster is assessed by the on-call geotechnical engineer"
        ],
        "intended_action": "Supervisor allows haulage to continue on the existing route, treating the seismic cluster as background activity typical of the adjacent worked-out ground."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A small fall of ground occurs near the Panel 3 haul intersection, damaging a length of ground support (mesh partially detached, no injuries)",
          "Supervisor now has, in sequence: the overnight seismic event, the wet ground note, the seismic cluster near the old mined-out panel, the blast schedule, and the earlier unexplained methane sensor spike",
          "The methane spike has not been independently investigated; the ventilation officer's log lists it as 'transient, no recurrence'",
          "Rock mechanics technician has not yet completed an instrumented assessment of the FOG area"
        ],
        "new_information_after_decision": [
          "Remediation crew re-supports the damaged section based on the supervisor's stated cause",
          "The geotechnical engineer, contacted afterward, requests raw seismic and gas data for independent review, noting the sequence could also be consistent with unrelated causes (e.g., localized joint failure, sensor drift)"
        ],
        "alternatives": [
          "Treat the FOG as explained by the stress-transfer/blast-vibration/water sequence and proceed directly to re-support based on that explanation",
          "Treat the cause as undetermined, order an instrumented investigation of both ground and gas anomalies before re-support planning, and flag the methane spike for separate review",
          "Request the on-call geotechnical engineer's real-time input before committing to any explanation or remediation plan"
        ],
        "intended_action": "Supervisor confidently attributes the FOG to a single continuous causal chain — the overnight seismic event triggering stress transfer from the old mined-out panel, worsened by water infiltration and blast vibration — and directs re-support on that basis, describing the sequence as something that 'all fit together' and 'made sense once you saw it,' while setting the earlier methane spike aside as unrelated background noise."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Re-support work is complete on the damaged section",
          "The geotechnical engineer's later data review is still pending and has not yet confirmed or refuted the supervisor's causal account",
          "Shift is approaching its scheduled end; production targets remain unmet for Panel 3",
          "No new seismic or gas anomalies have occurred since the FOG"
        ],
        "new_information_after_decision": [
          "Production resumes in Panel 3 for the remainder of the shift",
          "The following day's engineering review later finds the seismic cluster and the FOG statistically plausible but inconclusive as a single cause, and separately flags the methane sensor for calibration checking"
        ],
        "alternatives": [
          "Resume full production in Panel 3 immediately based on the completed re-support and the supervisor's causal explanation",
          "Resume limited production with continued monitoring pending the geotechnical engineer's independent review",
          "Suspend Panel 3 production for the remainder of the shift until formal sign-off is received"
        ],
        "intended_action": "Supervisor resumes full production, citing the completed re-support and the coherence of the explained cause as sufficient assurance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew at the very start of the shift, before anything unusual happened.",
        "What was your main objective for Panel 3 that night?"
      ],
      "timeline_reconstruction": [
        "What happened next, in the order it happened?",
        "At what point did you first notice something that felt different from a normal shift?",
        "What information came in after each event, and from which source?"
      ],
      "decision_point_probes": [
        "What options did you consider at that point, and why did you choose the one you did?",
        "What cues or data points stood out to you most at that moment?",
        "Whose input did you rely on, and whose did you not seek out or weigh heavily?",
        "How much time pressure did you feel, and did that affect what you checked or didn't check?",
        "How confident were you in your explanation at the time, and what would have changed that confidence?",
        "Was there any information that didn't fit your understanding of what was happening? How did you handle it?",
        "Had you seen a similar sequence of events before? How did that shape your read of this one?"
      ],
      "closing_hypotheticals": [
        "If the methane spike had happened twice instead of once, would that have changed your explanation?",
        "If you'd gotten the geotechnical engineer's data review before re-support, do you think your account of the cause would have looked different?",
        "Looking back, what part of your explanation are you least sure about now?",
        "What would you tell a newer supervisor to watch for in a similar sequence of events?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "decision_point": 3,
        "mechanism": "Post-hoc construction of a single, fluent, and seemingly inevitable causal chain that links several temporally sequenced but only loosely connected signals (overnight seismic event, wet ground, adjacent-panel seismic cluster, blast vibration) into one coherent explanation for the FOG, expressed with a sense that the sequence 'made sense' or 'fit together' once viewed together — while a discordant data point (the methane spike) is folded out of the story as irrelevant rather than genuinely investigated.",
        "affected_reasoning_operation": "Retrospective causal attribution / explanation construction",
        "evidence_available_at_time": [
          "Overnight seismic event log (magnitude ~1.1, classified minor)",
          "Wet ground note from outgoing crew",
          "Adjacent-panel microseismic cluster observed in phase 2",
          "Blast schedule and vibration exposure",
          "Unexplained transient methane sensor spike from phase 2",
          "Absence of completed instrumented geotechnical assessment"
        ],
        "required_textual_manifestation": "The supervisor's account at this decision point must present the cause as a single, smooth, and complete story told with notably higher confidence than the incomplete evidence supports, explicitly describing the pieces as fitting together or making the event feel expected/inevitable in hindsight, and must treat the methane spike as unrelated background without describing any actual investigation of it.",
        "plausible_nonbias_interpretation": "An experienced supervisor pattern-matching from genuine geotechnical training could legitimately propose stress transfer as one reasonable hypothesis among several; this is only a bias instance if the interview shows unwarranted certainty, absence of acknowledged alternative explanations, and dismissal of the discordant methane reading without genuine follow-up, rather than a tentative, evidence-qualified hypothesis.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "narrative fallacy",
          "cognitive bias",
          "storytelling",
          "hindsight",
          "coherence bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable — this is a biased-condition scenario with no paired control specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Confirm exactly one Narrative Fallacy instance is embedded, at decision point 3 only.",
      "Confirm no other decision point contains language that could independently satisfy the Narrative Fallacy mechanism.",
      "Confirm the methane spike is introduced neutrally at phase 2 and only becomes bias-relevant through its treatment at phase 3.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm the interview contains exactly four decision points with at least two alternatives each.",
      "Confirm word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm the outcome (successful re-support, resumed production) does not mechanically confirm or refute whether the causal account was correct.",
      "Confirm technical mining vocabulary is used consistently and avoided-term list is respected."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Narrative Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a post-hoc fluent causal chain linking prior disparate signals into one coherent, high-confidence explanation at decision point 3, with the discordant methane reading dismissed rather than investigated."
      }
    ],
    "target_bias_names": ["Narrative Fallacy"],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Narrative Fallacy",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Post-hoc construction of a single coherent causal chain (seismic event + wet ground + adjacent seismic cluster + blast vibration) explaining the FOG, expressed with unwarranted confidence and completeness, while the discordant methane spike is excluded from the story without genuine investigation.",
        "affected_reasoning_operation": "Retrospective causal attribution / explanation construction",
        "evidence_source": "Cross-phase synthesis of seismic log, ground condition note, microseismic cluster data, blast schedule, and the phase-2 methane sensor spike",
        "distinctiveness_requirement": "Only instance of this bias in the interview; must not be duplicated via restated examples, the phase 4 resumption decision, or the closing hypotheticals — those turns may reference the same explanation but must not introduce a new independently identifiable manifestation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_1",
    "domain_id": "MU",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point (phase 3) offering the strongest mechanism fit and narrative realism — the moment a multi-signal incident (FOG) demands causal explanation under time and production pressure, immediately after a discordant data point (methane spike) has been introduced in phase 2 but left unresolved.",
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
        "segment_type": "initial operational objective and plan",
        "raw_interview_anchor": "Standard handover; wet ground was described as more seepage than usual but not alarming on its own, and the blast, mucking, and haulage plan was stated.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is initial situational assessment and plan description. It does not independently manifest the hidden post-hoc causal-chain instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "blast authorization",
        "raw_interview_anchor": "I authorized the blast after a visual pass and did not call for an instrumented convergence check because the event was small and classified as normal range.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A substantive blast decision and rationale, but not the hidden Narrative Fallacy mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "haulage continuation",
        "raw_interview_anchor": "The microseismic cluster was increasing in frequency rather than magnitude; ventilation was normal, so haulage continued as-is.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a distinct operational continuation decision. The hidden manifest assigns no bias instance to this episode."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "methane-spike interpretation",
        "raw_interview_anchor": "The brief methane spike returned to baseline; it was logged as transient with no recurrence and was not considered significant at the time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification introduces this as a neutral phase-2 signal. It becomes bias-relevant only through its later treatment in the post-FOG explanation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "post-FOG causal explanation and discordant-cue dismissal",
        "raw_interview_anchor": "The seismic event, wet ground, adjacent-panel cluster, and blast vibration 'all lined up'; the participant formed a stress-transfer explanation, said it made sense, and then set aside the methane spike because it did not fit and was not investigated.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["nf_01"],
        "ground_truth_rationale": "This is the sole hidden instance: a fluent, seemingly complete post-hoc causal chain linking disparate signals into an expected-looking explanation for the FOG while excluding the discordant methane reading without genuine follow-up."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "blast alternatives and cue weighting",
        "raw_interview_anchor": "The participant considered visual-only, instrumented inspection, and reduced-charge options; the seismic classification carried the most weight and wet ground created only limited uncertainty.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This elaborates the blast decision and contains no independent hidden occurrence."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "haulage alternatives and input selection",
        "raw_interview_anchor": "The participant considered rerouting or halting, relied on ventilation readings, and did not call the on-call geotechnical engineer because the cluster did not seem urgent enough.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a follow-up rationale for the phase-2 haulage decision; the hidden specification does not assign an instance here."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "FOG remediation commitment",
        "raw_interview_anchor": "The participant acknowledged an undetermined-cause investigation and real-time engineering input as alternatives, but chose the stress-transfer account and direct re-support; later described why the explanation felt solid and why the methane spike did not fit.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an adjacent elaboration of the same decision-point episode. The single hidden instance is localized to seg_005, where the full chain construction and dismissal are expressed together; these later probes do not create a second occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "production resumption and retrospective evidence review",
        "raw_interview_anchor": "After re-support, full production resumed; the participant later acknowledged that engineering review and alternative explanations were still needed before the cause could be considered definitive.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification explicitly prevents phase-4 resumption and later engineering review from being treated as a new independent Narrative Fallacy occurrence."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual and retrospective reflection",
        "raw_interview_anchor": "A repeated methane spike would have been harder to dismiss; the participant said the stress-transfer story might not have been the whole cause and that the pieces fit well enough that he did not push hard on what did not fit.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "These are retrospective and counterfactual reflections on the same episode, not a second independently identifiable manifestation."
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
    "analysis_scope_note": "Evidence-first review of the single interview transcript; no RAG corpus passages were supplied, so bias classifications rely on established cognitive-science knowledge rather than retrieved literature."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect",
        "creeping determinism"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive an outcome as having been more predictable after it has occurred than it actually was, often by reconstructing prior cues into a coherent causal narrative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-fall causal interpretation",
      "decision_point_description": "After the fall of ground, the participant had to interpret the observed sequence and assign a likely cause before deciding on remediation and production resumption.",
      "affected_reasoning_operation": "retrospective causal attribution and predictability judgment",
      "bias_specific_mechanism": "After the outcome occurred, the participant used outcome knowledge to organize preceding cues into a coherent causal sequence and judged that sequence as expectable, increasing subjective certainty about the cause.",
      "manifestation_in_interview": "The participant described the fall as feeling 'pretty clear' and the stress-transfer account as 'almost the story you'd expect' after the fact.",
      "effect_on_reasoning_or_decision": "Increased subjective certainty in the stress-transfer explanation, reducing perceived need to treat the cause as undetermined before proceeding with re-support and resuming production.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, by that point it felt pretty clear. You had the seismic event overnight, the wet ground, then the seismic cluster building up near the old workings, plus the blast vibration from our own cycle — it all lined up. Stress transfer off the old mined-out panel, aggravated by the water getting into the joints and then our blast adding vibration on top. Once you saw it laid out like that, it made sense — it was almost the story you'd expect given that ground history.",
          "evidence_explanation": "This is a post-outcome statement of retrospective clarity and expectedness: the participant treats the event as an almost predictable causal story after it has occurred, which is the signature of hindsight bias."
        }
      ],
      "correction_or_counterevidence": "Later in the interview the participant acknowledges that the geotech engineer wanted raw seismic and gas data before sign-off and that alternative causes such as localized joint failure or sensor drift were possible; he also says the stress-transfer story may have been 'the part that was easiest to see.'",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this classification uses established cognitive-science knowledge of hindsight bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs or hypotheses, while discounting disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-fall cause determination and re-support decision",
      "decision_point_description": "Whether to accept the stress-transfer explanation as sufficient and proceed directly to re-support, or to order further instrumented/geotechnical investigation including the methane anomaly.",
      "affected_reasoning_operation": "evidence weighting and hypothesis evaluation",
      "bias_specific_mechanism": "Once the participant adopted the stress-transfer hypothesis, he favored cues that fit that story and discounted the methane spike as unrelated because it did not belong to the ground-stability picture. This downplayed an unresolved disconfirmatory signal and reduced perceived need for independent engineering review.",
      "manifestation_in_interview": "The participant explicitly set aside the methane spike and later stated that the pieces fit together well enough that he did not push hard on what did not fit.",
      "effect_on_reasoning_or_decision": "He committed to the stress-transfer account and re-supported the area without an instrumented/geotechnical review, reducing the chance of detecting alternative or compounding causes before production resumed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That I set aside. It didn't fit with a ground stability event — different system, different sensor, and it hadn't recurred. Ventilation had already called it transient. I didn't loop back on it specifically once we had a ground explanation that accounted for everything else.",
          "evidence_explanation": "Direct admission that a non-fitting observation was set aside after a ground explanation was available; this is selective discounting of disconfirmatory evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It tied together everything we'd seen that night in one line — the timing worked, the location worked, the mechanism was one I understood from my ground control days. When it clicks together that cleanly, you don't feel like you're guessing anymore.",
          "evidence_explanation": "Shows that the subjective coherence of the story increased confidence; coherence was used as a proxy for confirmation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pieces fit together well enough that I didn't push hard on what didn't fit.",
          "evidence_explanation": "Reflective admission of under-investigating contradictory information, a hallmark of confirmation-biased evaluation."
        }
      ],
      "correction_or_counterevidence": "The participant later notes the geotech engineer's alternative explanations and says a repeat methane spike would have been harder to dismiss; however, this recognition occurred retrospectively and did not prevent the initial biased commitment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this classification uses established cognitive-science knowledge of confirmation bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy bias",
      "alternative_labels": [
        "automation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Blast authorization after minor seismic event and wet ground note",
      "supporting_interview_quote": "The classification on the seismic log, mostly. 'Minor, within normal range' carries weight — that's the geotech team's own threshold, not something I'm second-guessing casually.",
      "plausible_mechanism": "Could reflect overreliance on a 'minor/normal' classification and routine practice, downweighting low-level cues such as wet ground and a prior seismic event that might have warranted instrumented checking.",
      "why_not_identified": "The behavior is substantially explained by legitimate reliance on specialized geotechnical classification and standard site procedure; there is insufficient affirmative evidence of a distinct distortion rather than a bounded rational judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so corpus support availability is absent and labels rely on general cognitive-science knowledge.",
    "Single-interview transcript limits inference of internal cognitive processes; no direct pre-outcome probability elicitation was available for assessing hindsight bias.",
    "Some bias mechanisms overlap and may share quotations, making clean separation between hindsight bias and confirmation bias difficult.",
    "The participant's retrospective account may itself be affected by self-presentation or memory, but analysis is limited to transcript-level evidence."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_1_Gemini_off",
  "interview_id": "MU_Biased_1",
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
