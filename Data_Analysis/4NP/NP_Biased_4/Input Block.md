<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift?

Participant: Sure, no problem. I'm a field equipment operator, been doing this about eleven years now, mostly auxiliary systems. That shift I was assigned to restore AFW Pump Train B to service after maintenance had a check valve out for repair. Goal was straightforward: get the lineup verified, start the pump, run the post-maintenance test, and get it inside the surveillance window before the LCO clock ran out.

Interviewer: Can you walk me through what happened, from the beginning?

Participant: I got to the pump room after grabbing the surveillance procedure and the routine lineup checklist. I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header. Somewhere in there, the prior shift had mentioned during turnover that maintenance added an isolation valve downstream of the check valve for the repair, but it was just a quick verbal mention in passing, not something we sat down and reviewed. I kept moving through my normal sequence. When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going. Found out afterward, when control room called down, that it wasn't lined up the way the updated paperwork called for.

After we sorted that out, I started the pump. On startup, the bearing temperature RTD came up slightly above the normal band, not alarming, but above where I usually see it. My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then. I just kept an eye on it informally and moved on with startup.

A little later, doing my rounds near the pump coupling, I heard a pretty loud, intermittent knocking sound. That got my attention immediately, it's the kind of noise that makes you stop. I also noticed, if I think back on it, the temperature had drifted up a bit more on the local gauge, and there was a faint odor near the oil reservoir. But the noise was what stood out, so that's what I focused on and what I called up to the control room about.

Interviewer: Let's slow down and go through the sequence again. What was the first point where you noticed something outside the routine?

Participant: Really it was the turnover mention of the added valve, though at the time it didn't register as a big deal. Then the RTD reading on startup was the next thing. Then the noise during rounds. Then it all came together near the end when we had to decide whether to keep running or trip the train, with the surveillance window closing in under half an hour.

Interviewer: Let's go through each of those decisions in more detail. Starting with the valve lineup — what information did you have in front of you at that point?

Participant: I had the standard checklist, the verbal mention from turnover about the new valve, and technically the work order attachment was available if I'd gone looking for it.

Interviewer: What made you proceed with the standard sequence instead of stopping to check the attachment?

Participant: Honestly, it's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up.

Interviewer: Had you handled an added or modified valve in a lineup before?

Participant: Occasionally, yeah, and usually turnover flags it clearly enough that I stop. This time it came up quick, almost an afterthought, and I didn't treat it any differently than a normal round.

Interviewer: Moving to the bearing temperature reading — what sources of information did you check, and which did you not check?

Participant: I checked the immediate RTD reading, which was slightly elevated. I did not pull the fifteen-minute trend from the plant computer, even though it was right there available. I relied more on remembering that other pump's issue from the week before.

Interviewer: How confident were you that this was the same kind of issue?

Participant: Confident enough to not escalate it right away, but not certain. If you'd asked me right then, I'd have said probably instrumentation again, but I couldn't have shown you data to back that up.

Interviewer: Let's talk about the noise, temperature drift, and odor. What made you center your report on the noise?

Participant: It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio.

Interviewer: Did you weigh the three cues equally before reporting?

Participant: Not really equally, no. I mentioned the other two, but briefly, more like a footnote to the noise call.

Interviewer: Now the final decision — continue running or trip and swap trains. What did that look like?

Participant: We had maybe under thirty minutes left in the window. I had a partial picture — noise that turned out later to be a loose coupling guard, a temperature that had crept up some more, and that odor still there. Swapping trains meant coordination, paperwork, and possibly missing the window entirely. The Shift Technical Advisor was tied up on another issue. I put together what I had, decided it was workable, and kept the train running to finish the test on schedule.

Interviewer: Did you consider pulling a full vibration spectrum or an oil sample before deciding?

Participant: I thought about it, yeah. There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check.

Interviewer: Was there a quicker option available — say, a fast local vibration reading or a quick radio consultation with someone in the control room — that might have told you within a few minutes whether this was the loose guard or something developing in the bearing itself?

Participant: Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window.

Interviewer: If the work order attachment had been physically handed to you at turnover instead of just mentioned, do you think anything would have changed?

Participant: Probably. If it's in my hand, I'm looking at it. Verbal mentions in a busy turnover just don't stick the same way.

Interviewer: If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently?

Participant: That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story.

Interviewer: If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention?

Participant: Probably, yeah. It's hard not to chase the loudest thing in the room first.

Interviewer: Looking back, is there anything you'd do differently with the same information you had at the time?

Participant: I'd probably slow down at the valve lineup regardless of how routine it feels, and I'd pull the trend data earlier instead of leaning on what happened last week. The bearing ended up needing unplanned maintenance for degrading lubrication, so there was more going on than I gave it credit for in the moment.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_4",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Field Operator / Equipment Operator (Nuclear)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Post-Maintenance AFW Train Realignment and Escalating Bearing Anomaly",
    "scenario_summary_internal": "A field operator returns Auxiliary Feedwater (AFW) Pump Train B to service following planned maintenance on a discharge check valve. During the post-maintenance walkdown, startup, and monitoring rounds, the operator must verify valve lineup against a modified procedure, interpret an elevated bearing temperature reading in light of a recent unrelated instrument glitch, triage multiple simultaneous abnormal cues of different vividness, and finally decide whether to continue running the train or initiate a trip and swap to the redundant train under time pressure before a required surveillance window closes.",
    "occupational_realism": {
      "objective": "Restore AFW Pump Train B to operable status after maintenance and complete required post-maintenance testing before the surveillance deadline, without introducing a plant transient or violating technical specifications.",
      "setting": "Nuclear power plant auxiliary building, AFW pump room, mid-shift during a scheduled maintenance outage window, field operator working with a control room operator via radio",
      "constraints": [
        "Fixed surveillance test window (Tech Spec LCO) closing in under two hours",
        "Radiological and industrial safety requirements limiting time in the pump room",
        "Only one other AFW train available as backup, creating pressure to avoid unnecessary trips",
        "Recent history of a nuisance/spurious alarm on a similar instrument loop",
        "Communication lag between field operator and control room during radio traffic congestion"
      ],
      "stakeholders": [
        "Field Operator (interviewee)",
        "Control Room Supervisor",
        "Maintenance technician who performed the check valve work",
        "Shift Technical Advisor",
        "Oncoming shift crew"
      ],
      "technical_terms_to_use": [
        "Auxiliary Feedwater (AFW)",
        "check valve",
        "valve lineup",
        "post-maintenance testing (PMT)",
        "bearing temperature",
        "vibration monitoring",
        "Tech Spec LCO",
        "surveillance window",
        "local control station",
        "trending",
        "RTD (resistance temperature detector)"
      ],
      "technical_terms_to_avoid": [
        "recency bias",
        "habit intrusion",
        "bounded rationality",
        "salience bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Standard AFW valve lineup checklist from the routine surveillance procedure",
          "A maintenance work order note stating an additional isolation valve was installed downstream of the check valve for the repair",
          "Verbal handover from the prior shift mentioning the valve change only in passing"
        ],
        "new_information_after_decision": [
          "The added isolation valve is found mid-lineup in a non-standard position",
          "Control room later confirms the valve should have been verified open per the updated work order attachment"
        ],
        "alternatives": [
          "Follow the familiar routine lineup sequence from memory as done hundreds of times before",
          "Stop and cross-check the current valve lineup against the specific post-maintenance work order attachment before proceeding"
        ],
        "intended_action": "Operator begins the lineup using the well-practiced routine sequence, walking past the new valve position without pausing to verify it against the modified paperwork."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Bearing temperature RTD reads slightly above normal band on pump start",
          "One week earlier, an unrelated RTD on a similar pump gave a false high reading traced to a wiring fault, later corrected",
          "Current trend data from the plant computer showing a slow but steady rise over the last 15 minutes is available on request"
        ],
        "new_information_after_decision": [
          "The trend data, if pulled, would show the rise is steeper and more sustained than the earlier false-alarm case",
          "Maintenance later confirms the RTD wiring on this pump was inspected and found intact, meaning the reading was likely real"
        ],
        "alternatives": [
          "Treat the elevated reading as most likely another instrument glitch similar to the recent case and continue monitoring informally",
          "Pull the full trend history and request an independent verification reading before proceeding further"
        ],
        "intended_action": "Operator attributes the reading primarily to the recently experienced false-alarm pattern and defers a full trend review, continuing the startup sequence."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A loud, intermittent mechanical knocking noise from the pump coupling area, clearly audible over the room's ambient noise",
          "A less noticeable but continuous upward drift in the bearing temperature trend visible only on the local gauge",
          "A faint, easily overlooked odor near the oil reservoir consistent with early seal degradation"
        ],
        "new_information_after_decision": [
          "The knocking noise is later attributed to a loose coupling guard, unrelated to the developing problem",
          "The bearing temperature and oil condition, once checked afterward, show the more diagnostic combination the operator initially set aside"
        ],
        "alternatives": [
          "Focus attention and the radio report on the loud knocking noise as the primary concern",
          "Systematically check all three cues (noise, temperature trend, odor) with equal weight before reporting anything"
        ],
        "intended_action": "Operator's attention and radio report to the control room center almost entirely on the loud knocking sound, mentioning the temperature and odor only briefly and without emphasis."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Surveillance window closing in under 30 minutes",
          "Partial, somewhat conflicting data on noise, temperature, and odor gathered across the shift",
          "Backup AFW train available but swapping trains requires additional coordination and paperwork",
          "Shift Technical Advisor available by radio but currently occupied with another issue"
        ],
        "new_information_after_decision": [
          "Post-event review shows a more complete data pull (full trend, vibration spectrum, oil sample) was feasible in the time available but was not fully pursued",
          "The train is later found to have degrading bearing lubrication requiring unplanned maintenance"
        ],
        "alternatives": [
          "Take the extra time to gather complete diagnostic data before deciding, even if it risks missing the surveillance window",
          "Make a quick judgment call based on the readily available partial information to keep the schedule on track"
        ],
        "intended_action": "Operator settles on a workable-enough combination of the partial cues gathered, decides to continue running the train to complete the surveillance on time, without exhaustively weighing all available diagnostic options."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were asked to do at the start of this shift?",
        "What was your understanding of the operational goal before you began the lineup?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do immediately after?",
        "At what point did you first notice something might be different from a routine lineup or startup?",
        "How did the sequence of events unfold from the pump start to the final decision?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at that moment?",
        "What alternatives did you consider before acting?",
        "Why did you choose that option over the other one?",
        "Had you handled a similar situation before? How did that shape your response?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the information you were using?",
        "What sources of information did you check, and which ones did you not check?"
      ],
      "closing_hypotheticals": [
        "If the maintenance work order attachment had been handed to you directly instead of mentioned verbally, would anything have changed?",
        "If the earlier false-alarm instrument event had not happened the week before, would you have responded differently to the temperature reading?",
        "If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention?",
        "Looking back, is there anything you would do differently with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "decision_point": 1,
        "mechanism": "Operator executes the highly familiar, frequently-practiced routine valve lineup sequence from memory, and this overlearned pattern intrudes over the need to consult the modified, non-routine work order documentation for the newly added valve.",
        "affected_reasoning_operation": "Procedural execution / lineup verification",
        "evidence_available_at_time": [
          "Routine lineup checklist",
          "Work order note mentioning an added valve",
          "Brief verbal shift handover"
        ],
        "required_textual_manifestation": "Operator describes proceeding through the lineup 'the way I always do it' or similar, walking past or handling the new valve using the standard sequence rather than pausing to check the modified paperwork, later realizing the valve was not verified per the updated attachment.",
        "plausible_nonbias_interpretation": "The operator could argue the verbal handover was sufficient and time constraints justified relying on the standard sequence.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "habit intrusion",
          "automaticity",
          "overlearned behavior"
        ]
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "decision_point": 2,
        "mechanism": "Operator's interpretation of the elevated bearing temperature is disproportionately anchored on the most recently experienced similar event (last week's false-alarm RTD) rather than on the full available trend data or base rate of real versus spurious readings.",
        "affected_reasoning_operation": "Diagnostic interpretation of an instrument reading",
        "evidence_available_at_time": [
          "Current RTD reading slightly above normal",
          "Memory of last week's unrelated false-alarm RTD event",
          "Available but unpulled 15-minute trend data"
        ],
        "required_textual_manifestation": "Operator explicitly connects the current reading to the recent false-alarm case as the primary basis for downplaying it, without describing having reviewed the actual trend data at that time.",
        "plausible_nonbias_interpretation": "The operator could argue pattern-matching to a recent, verified false alarm was a reasonable time-saving judgment given workload.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "recency bias",
          "recent event weighting",
          "availability of memory"
        ]
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 3,
        "mechanism": "Operator's attention and reporting are captured disproportionately by the most perceptually vivid and attention-grabbing cue (loud knocking noise) while the less vivid but more diagnostically relevant cues (temperature trend, odor) receive minimal attention or reporting.",
        "affected_reasoning_operation": "Cue selection and triage / information reporting",
        "evidence_available_at_time": [
          "Loud intermittent knocking noise",
          "Continuous but visually subtle bearing temperature drift",
          "Faint oil odor"
        ],
        "required_textual_manifestation": "Operator's account of the radio report and personal focus centers heavily on the noise, with the temperature and odor mentioned only in passing or as an afterthought, despite all three being observable at the time.",
        "plausible_nonbias_interpretation": "The operator could argue the noise posed an immediate mechanical safety concern warranting priority attention.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "salience bias",
          "vividness",
          "attention capture"
        ]
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 4,
        "mechanism": "Under time pressure and incomplete information, the operator settles for a workable, 'good-enough' combination of partially gathered cues to reach a decision, rather than systematically pursuing available additional diagnostics (full trend, vibration spectrum, oil sample) that were feasible within the remaining time.",
        "affected_reasoning_operation": "Final go/no-go judgment integrating multiple partial evidence streams",
        "evidence_available_at_time": [
          "Partial, somewhat conflicting cues from noise, temperature, and odor",
          "Time remaining before surveillance window closes",
          "Availability of a backup train and of the Shift Technical Advisor"
        ],
        "required_textual_manifestation": "Operator describes stopping short of a full systematic evaluation of all available diagnostic options, instead combining the readily-at-hand partial information into a workable judgment to keep the train running and meet the schedule.",
        "plausible_nonbias_interpretation": "The operator could argue that pursuing every diagnostic option was operationally impractical given genuine time constraints.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "bounded rationality",
          "satisficing",
          "imperfect rationality"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Completeness of shift handover documentation regarding the added isolation valve and prior instrument trend history",
      "original_state": "Handover was verbal and incomplete; the work order attachment and full trend history were not proactively provided to the field operator",
      "counterfactual_state": "Handover includes the written work order attachment for the added valve and a printed trend summary for the RTD, both handed directly to the field operator before the lineup begins",
      "variables_to_hold_constant": [
        "Operational objective and surveillance deadline",
        "Personnel involved (same field operator, control room supervisor, maintenance technician)",
        "Physical plant conditions and equipment configuration",
        "Sequence of the four decision points",
        "Time pressure magnitude"
      ],
      "expected_causal_difference": "With complete documentation provided upfront, the habit-intrusion and recency-bias manifestations at decision points 1 and 2 would be expected to diminish, since the operator would have direct, salient documentary cues correcting reliance on routine memory and recent-event pattern-matching.",
      "causal_test_question": "Does providing complete written handover documentation (valve change order and trend summary) reduce reliance on routine memory and recent-event pattern-matching at the lineup and diagnostic-interpretation decision points?"
    },
    "generation_checks": [
      "Confirm exactly four decision points are present and sequential.",
      "Confirm exactly one instance each of Recency Bias, Habit Intrusion, Imperfect Rationality, and Salience Bias is embedded, each at a distinct decision point.",
      "Confirm the Habit Intrusion instance textually reflects the mechanism_constraint (familiar, frequently-occurring behavioral pattern).",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each decision point offers at least two plausible alternatives with before/after information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 (acceptable 1,215–1,485) is achievable without repeating any single bias manifestation.",
      "Confirm consequences described do not deterministically prove any decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Recency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Habit Intrusion",
        "occurrences": 1,
        "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences."
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Salience Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Recency Bias",
      "Habit Intrusion",
      "Imperfect Rationality",
      "Salience Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Recency Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Habit Intrusion",
        "requested_occurrences": 1
      },
      {
        "bias": "Imperfect Rationality",
        "requested_occurrences": 1
      },
      {
        "bias": "Salience Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion"
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias"
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "decision_point": 1
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "decision_point": 2
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 3
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "mechanism": "Overlearned, frequently-practiced routine lineup sequence intrudes over the need to consult modified, non-routine documentation for a newly added valve.",
        "affected_reasoning_operation": "Procedural execution / lineup verification",
        "evidence_source": "Routine checklist versus work order attachment describing the added valve",
        "distinctiveness_requirement": "Must be tied to execution of a well-practiced procedural sequence at decision point 1, not to memory-based interpretation of an instrument reading (which is reserved for rb_01)."
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "mechanism": "Interpretation of the current bearing temperature reading is anchored on the most recently experienced similar false-alarm event rather than on available trend data or base rates.",
        "affected_reasoning_operation": "Diagnostic interpretation of an instrument reading",
        "evidence_source": "Memory of last week's false-alarm RTD event versus unpulled current trend data",
        "distinctiveness_requirement": "Must be tied specifically to recency of a remembered event at decision point 2, distinct from the habitual procedural pattern in hi_01 and distinct from the attentional capture in sb_01."
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "mechanism": "Attention and reporting disproportionately capture by the most perceptually vivid cue (loud knocking) over less vivid but diagnostically relevant cues (temperature trend, odor).",
        "affected_reasoning_operation": "Cue selection and triage / information reporting",
        "evidence_source": "Simultaneous noise, temperature trend, and odor cues at decision point 3",
        "distinctiveness_requirement": "Must be tied to comparative attentional weighting among simultaneously available cues, distinct from the temporal/memory basis of rb_01 and the outcome-integration basis of ir_01."
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Under time pressure, settles for a workable combination of partial evidence rather than systematically pursuing feasible additional diagnostics before the final go/no-go judgment.",
        "affected_reasoning_operation": "Final go/no-go judgment integrating multiple partial evidence streams",
        "evidence_source": "Partially gathered cues plus time and resource constraints at decision point 4",
        "distinctiveness_requirement": "Must be tied to the integrative final decision under bounded resources, distinct from the earlier single-cue-processing biases (hi_01, rb_01, sb_01)."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "strength": "moderate"
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "strength": "subtle"
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Completeness of shift handover documentation regarding the added isolation valve and prior instrument trend history",
      "original_state": "Verbal, incomplete handover; no direct provision of work order attachment or trend summary",
      "changed_state": "Written work order attachment and printed trend summary provided directly to the field operator before lineup",
      "variables_to_hold_constant": [
        "Operational objective and surveillance deadline",
        "Personnel involved",
        "Physical plant conditions and equipment configuration",
        "Sequence of the four decision points",
        "Time pressure magnitude"
      ]
    },
    "scenario_id": "NP_Biased_4",
    "domain_id": "NP",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per bias assigned to a distinct decision point, selected by mechanism fit and narrative realism: Habit Intrusion at the procedural lineup stage (DP1), Recency Bias at the memory-anchored instrument interpretation stage (DP2), Salience Bias at the multi-cue attentional triage stage (DP3), and Imperfect Rationality at the final integrative go/no-go judgment under time pressure (DP4). No bias shares a decision point, satisfying the maximum-two-per-point and distinct-evidence-source rules trivially.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Operational objective and surveillance deadline",
      "Personnel involved",
      "Physical plant conditions and equipment configuration",
      "Sequence of the four decision points",
      "Time pressure magnitude"
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
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "Routine valve lineup proceeded without checking the modified work-order attachment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["hi_01"],
          "ground_truth_rationale": "A familiar lineup routine intruded over verification of modified documentation."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "Recent false-alarm memory drove interpretation of the elevated RTD and the trend was not pulled.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["rb_01"],
          "ground_truth_rationale": "The current reading was anchored on the most recent similar event."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "The loud knocking dominated attention and reporting while temperature drift and odor were mentioned only briefly.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["sb_01"],
          "ground_truth_rationale": "A vivid cue was weighted over less vivid diagnostic cues."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_rationale",
          "raw_interview_anchor": "The partial picture was deemed workable and feasible quick diagnostics were not pursued before continuing the test.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["ir_01"],
          "ground_truth_rationale": "The operator settled for partial evidence under time pressure."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
