You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the full interview transcript for cognitive bias occurrences. No retrieved scientific-paper passages were supplied in the RAG context."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Premature closure",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Salience bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Expectation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in ways that confirm pre-existing beliefs or expectations while underweighting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Valve lineup verification after turnover mention of added isolation valve",
      "decision_point_description": "Deciding whether to stop and consult the work order attachment or proceed with the routine lineup sequence",
      "affected_reasoning_operation": "Information search and verification judgment",
      "bias_specific_mechanism": "The operator's strong pre-existing routine expectation about the standard valve lineup led him to treat the changed configuration as ordinary and not seek the disconfirming updated work order attachment.",
      "manifestation_in_interview": "The participant reported proceeding through the lineup the same way he always did and not pulling the work order attachment despite being told about an added downstream isolation valve; he described the verbal mention as registering but not breaking the pattern.",
      "effect_on_reasoning_or_decision": "The valve lineup was not verified against the updated paperwork, and the lineup was later found not to match the updated configuration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd done this exact lineup more times than I can count, so I started working through it the way I always do, valve by valve, left side first, then across to the discharge header.",
          "evidence_explanation": "Shows a strong pre-existing routine expectation guiding the verification sequence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up.",
          "evidence_explanation": "Demonstrates that information inconsistent with the routine was not used to alter search behavior; the prior expectation persisted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I got near where that valve should've been, I didn't stop to pull the work order attachment and check it — I just verified it looked roughly right and kept going.",
          "evidence_explanation": "Specific failure to seek potentially disconfirming updated documentation, consistent with confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The participant had occasionally handled added or modified valves before when turnover clearly flagged them, and the verbal mention here was brief. The behavior may also be partly explained by routine automaticity rather than deliberate confirmation seeking.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or nature of a current event by the ease with which similar instances come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of slightly elevated bearing temperature RTD during pump startup",
      "decision_point_description": "Deciding whether to pull trend data or escalate the RTD reading versus assuming it was instrumentation again",
      "affected_reasoning_operation": "Probability judgment and causal attribution",
      "bias_specific_mechanism": "A recent, salient false alarm involving another pump's RTD came easily to mind, so the participant judged the current elevated RTD as probably another wiring/instrumentation issue and did not seek contemporaneous trend data.",
      "manifestation_in_interview": "The participant explicitly recalled the prior week's wiring fault and inferred that the current RTD was probably the same kind of issue.",
      "effect_on_reasoning_or_decision": "He did not pull the 15-minute trend or escalate initially; the bearing later required unplanned maintenance for degrading lubrication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault, nothing physically wrong with the pump. So I figured this was probably the same kind of thing and didn't pull up the trend data right then.",
          "evidence_explanation": "Direct evidence of a salient recent memory dominating causal judgment and reducing information search."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I relied more on remembering that other pump's issue from the week before.",
          "evidence_explanation": "Shows the judgment was supported by recall rather than current data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I might have pulled the trend sooner instead of assuming it was the same story.",
          "evidence_explanation": "Counterfactual statement supports the causal role of the available memory."
        }
      ],
      "correction_or_counterevidence": "The RTD was only slightly above normal and not alarming, so a non-bias explanation is that it was initially treated as low urgency. The participant also said he was not certain.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Salience bias",
      "alternative_labels": [
        "Attentional bias",
        "Salience effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to focus on perceptually or emotionally salient cues while underweighting less prominent but potentially diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reporting abnormal pump cues after noticing noise, temperature drift, and odor during rounds",
      "decision_point_description": "Deciding which abnormal cues to prioritize when communicating with the control room",
      "affected_reasoning_operation": "Attention allocation and cue prioritization",
      "bias_specific_mechanism": "The loud, rhythmic knocking noise was highly salient, so it dominated attention and reporting; the smaller temperature drift and faint odor were underweighted even though they could be diagnostically important.",
      "manifestation_in_interview": "The participant centered the report on the noise and described the other two cues as brief footnotes.",
      "effect_on_reasoning_or_decision": "The control room received a report led by the noise, with the temperature and odor cues minimized, potentially shaping subsequent diagnostic focus.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The noise was what stood out, so that's what I focused on and what I called up to the control room about.",
          "evidence_explanation": "Explicit statement that salience directed focus and reporting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's just impossible to ignore, it's loud, it's rhythmic, it sounds mechanical and wrong. The temperature drift was smaller and only visible if you were looking right at the local gauge, and the odor was faint enough that I almost second-guessed whether I was smelling anything at all. So naturally the noise is what I led with on the radio.",
          "evidence_explanation": "Contrasts highly salient noise with less salient cues and explains unequal cue weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mentioned the other two, but briefly, more like a footnote to the noise call.",
          "evidence_explanation": "Demonstrates that the report was shaped by salience-weighted attention."
        }
      ],
      "correction_or_counterevidence": "The participant did mention the other cues briefly, so the information was not entirely suppressed. Preferentially reporting the loudest cue may be a natural and sometimes appropriate diagnostic heuristic.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Premature closure",
      "alternative_labels": [
        "Premature diagnostic closure"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Stopping information gathering once a plausible conclusion or course of action has been reached, before adequately testing disconfirming possibilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final decision to continue running Pump Train B rather than trip or swap trains",
      "decision_point_description": "Deciding whether the available partial information was sufficient to continue running the train within the surveillance window",
      "affected_reasoning_operation": "Information search and course-of-action decision under uncertainty",
      "bias_specific_mechanism": "After assembling a partial picture, the participant treated it as sufficient and did not initiate further checks or ask whether a quicker check could fit within the window.",
      "manifestation_in_interview": "The participant acknowledged that a fast local vibration reading or radio consultation might have been possible, but he did not ask about it in the moment and decided the situation was workable.",
      "effect_on_reasoning_or_decision": "The train remained running with degraded bearing lubrication; a quicker diagnostic check that could have helped distinguish the loose coupling guard from a developing bearing issue was not pursued.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I put together what I had, decided it was workable, and kept the train running to finish the test on schedule.",
          "evidence_explanation": "Indicates closure on a plausible course of action based on partial information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, yeah, there probably was. A quick local vibration check wouldn't have taken long, and I could have gotten someone on the radio to sanity-check what I was seeing. I didn't actually ask whether that was doable in the moment — once I had the pieces I'd already gathered, it felt like enough to keep going, so I didn't stop to find out if a faster check could have fit inside the window.",
          "evidence_explanation": "Shows termination of information search after reaching a plausible decision, despite later recognizing an available disconfirming check."
        }
      ],
      "correction_or_counterevidence": "Strong situational factors, including less than 30 minutes left in the surveillance window, coordination burden, and the Shift Technical Advisor being tied up, may explain the decision without invoking bias. This alternative is why confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus was provided; bias labels and mechanisms rely on general cognitive-science knowledge and are disclosed accordingly.",
    "The transcript is a retrospective self-report after the outcome was known, which can introduce recall and hindsight effects, but no separate hindsight-bias occurrence was affirmatively identified.",
    "Time pressure and procedural constraints are present as competing explanations, particularly for the final decision."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_4_Sonar_off",
  "interview_id": "NP_Biased_4",
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
