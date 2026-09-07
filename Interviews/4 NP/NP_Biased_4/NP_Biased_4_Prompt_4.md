You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift?

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

Interviewer: If the work order attachment had been physically handed to you at turnover instead of just mentioned, do you think anything would have changed?

Participant: Probably. If it's in my hand, I'm looking at it. Verbal mentions in a busy turnover just don't stick the same way.

Interviewer: If that other pump's false alarm hadn't happened the week before, would you have responded to the RTD differently?

Participant: That's a fair question. I think I might have pulled the trend sooner instead of assuming it was the same story.

Interviewer: If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention?

Participant: Probably, yeah. It's hard not to chase the loudest thing in the room first.

Interviewer: Looking back, is there anything you'd do differently with the same information you had at the time?

Participant: I'd probably slow down at the valve lineup regardless of how routine it feels, and I'd pull the trend data earlier instead of leaning on what happened last week. The bearing ended up needing unplanned maintenance for degrading lubrication, so there was more going on than I gave it credit for in the moment.}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "NP_Biased_4_unlabeled",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Nuclear-plant auxiliary feedwater operations and post-maintenance surveillance testing",
    "role": "Field equipment operator",
    "objective": "Restore AFW Pump Train B after check-valve maintenance, verify the modified lineup, complete the post-maintenance test, and meet the LCO surveillance deadline",
    "incident_type": "Post-maintenance configuration error followed by potentially degraded pump-condition triage and a continue-versus-trip operational decision",
    "confidence": 0.98
  },
  "structure_audit": {
    "estimated_word_count": 1260,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The operator proceeds through the familiar valve-lineup sequence rather than interrupting the routine to consult available modified-work documentation about a newly added isolation valve.",
        "evidence_before": [
          "Standard lineup checklist",
          "Brief verbal turnover mention that maintenance added an isolation valve downstream of the check valve",
          "Available but unreviewed work-order attachment"
        ],
        "evidence_after": [
          "Control room reports that the lineup does not match the updated paperwork"
        ],
        "goals_constraints": [
          "Restore AFW Pump Train B",
          "Verify the lineup accurately",
          "Complete surveillance before the LCO clock expires",
          "Manage a busy turnover with incomplete direct documentation"
        ],
        "alternatives": [
          "Pause the routine sequence and review the work-order attachment",
          "Seek clarification from turnover personnel or maintenance",
          "Continue using the standard checklist and familiar valve sequence"
        ],
        "decision_basis": "The participant reports that the familiar sequence was second nature and that the turnover mention did not trigger a departure from the learned pattern.",
        "time_pressure": "Present as part of the surveillance deadline, though not described as acute at this precise moment.",
        "uncertainty": "The operator knew a modification existed but did not verify its precise configuration before acting."
      },
      {
        "id": 2,
        "summary": "The operator interprets a slightly elevated bearing-temperature RTD as probably another instrumentation issue, based primarily on a similar false alarm on another pump the prior week, without reviewing available trend data.",
        "evidence_before": [
          "Current RTD slightly above the normal band",
          "Memory of a similar RTD reading on another pump the prior week that was attributed to wiring",
          "Available fifteen-minute plant-computer trend data"
        ],
        "evidence_after": [
          "The temperature later drifts higher",
          "The bearing ultimately requires unplanned maintenance for degrading lubrication"
        ],
        "goals_constraints": [
          "Start and monitor the restored pump",
          "Distinguish an instrumentation issue from an emerging mechanical condition",
          "Avoid unnecessary escalation while completing surveillance"
        ],
        "alternatives": [
          "Pull and assess the current fifteen-minute trend",
          "Escalate the elevated reading for additional evaluation",
          "Treat it as probably similar to the recent false-alarm event and observe informally"
        ],
        "decision_basis": "A recent, superficially similar event is used as the principal interpretive frame despite the availability of current trend evidence.",
        "time_pressure": "Moderate operational time pressure is present, but the participant does not state that obtaining the trend was infeasible.",
        "uncertainty": "The participant explicitly says they were not certain and could not provide data supporting the instrumentation interpretation."
      },
      {
        "id": 3,
        "summary": "The operator reports and prioritizes loud intermittent knocking while giving substantially less weight to a rising temperature and faint oil odor observed in the same period.",
        "evidence_before": [
          "Loud, intermittent, rhythmic knocking near the coupling",
          "Further local temperature drift",
          "Faint odor near the oil reservoir"
        ],
        "evidence_after": [
          "The noise is later attributed to a loose coupling guard",
          "Lubrication degradation is identified as requiring unplanned bearing maintenance"
        ],
        "goals_constraints": [
          "Rapidly communicate equipment condition to the control room",
          "Identify whether the train can safely continue operating",
          "Triage multiple partially diagnostic cues"
        ],
        "alternatives": [
          "Report and evaluate the noise, temperature trend, and odor with comparable prominence",
          "Prioritize the loud noise while treating other cues as secondary",
          "Pause operations for broader condition assessment"
        ],
        "decision_basis": "The perceptual intensity and mechanical character of the noise capture attention and dominate the radio report.",
        "time_pressure": "Operationally relevant but not quantified at this moment.",
        "uncertainty": "The odor is weak and the temperature change is modest, making both cues less immediately compelling but still potentially diagnostic."
      },
      {
        "id": 4,
        "summary": "With less than thirty minutes before the surveillance window closes, the operator decides to continue running the train rather than trip and swap trains or pursue further diagnostics.",
        "evidence_before": [
          "Partial evidence: knocking, increasing temperature, and persistent odor",
          "Subsequent understanding that the noise came from a loose coupling guard",
          "Potentially available vibration-spectrum and oil-sample diagnostics",
          "A Shift Technical Advisor occupied with another issue",
          "Coordination and paperwork burden associated with swapping trains"
        ],
        "evidence_after": [
          "The test is completed on schedule",
          "The bearing later requires unplanned maintenance for degrading lubrication"
        ],
        "goals_constraints": [
          "Finish the surveillance within the LCO window",
          "Maintain train availability",
          "Avoid a potentially disruptive train swap",
          "Make a safety-relevant judgment with incomplete information and limited support"
        ],
        "alternatives": [
          "Continue operating to complete the test",
          "Trip the train and coordinate a swap",
          "Obtain targeted diagnostics before deciding"
        ],
        "decision_basis": "The participant describes choosing a workable path using the evidence already assembled instead of pursuing further possible checks.",
        "time_pressure": "High: fewer than thirty minutes remained, and a swap could have caused a missed surveillance window.",
        "uncertainty": "The evidentiary picture was incomplete, but the interview does not establish whether feasible diagnostics would materially have changed the go/no-go decision within the available time."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "hi_01",
      "bias": "Habit Intrusion",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“It's just the sequence I run every time, it's second nature at this point. The mention at turnover registered, but it didn't trigger me to break from the pattern. I've done that lineup so many times the same way, my hands almost know it before my head catches up.”",
      "evidence_location": "Valve-lineup follow-up, participant response explaining why the work-order attachment was not checked",
      "mechanism": "A highly practiced procedural sequence continues to govern execution despite a known non-routine modification and the availability of documentation needed to verify that modification.",
      "strength": "moderate",
      "confidence": 0.96,
      "plausible_nonbias_explanation": "The turnover communication may genuinely have been insufficiently clear or actionable. However, the participant does not merely report missing information; they explicitly describe the normal sequence as overriding the need to interrupt and verify the modification.",
      "additional_evidence_needed": "None required for the requested occurrence. A precise description of the incorrect valve position would improve operational specificity but is not necessary to establish the procedural-intrusion mechanism.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, valve-lineup explanation",
        "current_defect": "None material. The evidence identifies a distinct procedural-execution episode and directly contrasts the automatic routine with the modified-documentation requirement.",
        "minimal_change_instruction": "No change required.",
        "preserve": [
          "The verbal turnover mention",
          "The availability of the work-order attachment",
          "The participant's description of the routine as second nature",
          "The separation from the later instrument-interpretation episode"
        ],
        "avoid_creating": [
          "A second habitual-memory episode at the RTD decision point",
          "An explicit bias label in the participant's speech"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "rb_01",
      "bias": "Recency Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“My first thought honestly went back to the week before — we'd had a similar RTD on another pump throw a high reading that turned out to be a wiring fault... So I figured this was probably the same kind of thing and didn't pull up the trend data right then.”",
      "evidence_location": "Startup-temperature account and follow-up regarding unreviewed fifteen-minute trend data",
      "mechanism": "A recently experienced false alarm is given disproportionate diagnostic influence over current evidence, leading the operator to treat the present elevation as probably instrumental rather than consult readily available current trend information.",
      "strength": "moderate",
      "confidence": 0.94,
      "plausible_nonbias_explanation": "The previous event could be a legitimate analog if the pumps, instrumentation paths, and symptom patterns were materially comparable. The interview, however, provides no comparative evidence supporting that transfer and records the participant's unsupported reliance on recency.",
      "additional_evidence_needed": "None required for support. It would be useful, but not essential, to state whether the prior event involved the same RTD type or comparable wiring arrangement.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, bearing-temperature interpretation",
        "current_defect": "None material. The remembered event is temporally specified, is used to interpret the current reading, and is contrasted with unreviewed current data.",
        "minimal_change_instruction": "No change required.",
        "preserve": [
          "The prior week's false-alarm event",
          "The current slightly elevated RTD",
          "The unreviewed current trend",
          "The participant's stated lack of certainty"
        ],
        "avoid_creating": [
          "A generic availability or confirmation-bias explanation that obscures the explicitly recent-event mechanism",
          "A second recency episode elsewhere in the interview"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sb_01",
      "bias": "Salience Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“But the noise was what stood out, so that's what I focused on and what I called up to the control room about.” “I mentioned the other two, but briefly, more like a footnote to the noise call.”",
      "evidence_location": "Multi-cue rounds account and probe asking whether the three cues were weighed equally",
      "mechanism": "The loud, rhythmic, perceptually vivid knocking disproportionately captures attention and reporting, while quieter but potentially diagnostic temperature and odor cues receive less weight.",
      "strength": "moderate",
      "confidence": 0.95,
      "plausible_nonbias_explanation": "A loud mechanical noise can appropriately warrant immediate attention. The bias inference rests not on attention to noise alone, but on the participant's explicit comparative downweighting of simultaneously available temperature and odor evidence without an articulated diagnostic rationale.",
      "additional_evidence_needed": "None required. The interview already documents simultaneous cues, comparative weighting, and the report-selection consequence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, report of noise, temperature drift, and odor",
        "current_defect": "None material. The evidence is distinct from the earlier memory-based interpretation and from the later final go/no-go judgment.",
        "minimal_change_instruction": "No change required.",
        "preserve": [
          "The simultaneity of the three cues",
          "The description of the noise as loud and rhythmic",
          "The comparatively muted reporting of temperature and odor",
          "The later clarification that the noise was due to a loose guard"
        ],
        "avoid_creating": [
          "A claim that salience alone proves the final operational decision was wrong",
          "A second salience occurrence based solely on the deadline or noise outcome"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "ir_01",
      "bias": "Imperfect Rationality",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 4,
      "supporting_quote": "“There probably was time if I'd pushed for it, but between the clock and coordinating with everyone else, I went with what I already had rather than chasing every possible check.”",
      "evidence_location": "Final continue-versus-trip decision and follow-up regarding vibration-spectrum and oil-sample diagnostics",
      "mechanism": "The text suggests satisficing under bounded time and coordination resources: the participant accepts a workable partial-evidence picture rather than seek additional information. However, it does not establish that a targeted additional diagnostic was both feasible and decision-relevant before the deadline, or that the decision process omitted a reasonable minimum evaluation.",
      "strength": "weak",
      "confidence": 0.74,
      "plausible_nonbias_explanation": "Continuing may have been a defensible risk-managed decision under an LCO deadline, coordination burden, limited advisory support, and uncertain cue significance. A choice not to perform every possible diagnostic is not itself evidence of imperfect rationality.",
      "additional_evidence_needed": "Evidence that the operator could have requested one specific, rapid, decision-relevant diagnostic or consultation; knew it would be available before the deadline; and chose not to determine whether it would resolve the lubrication concern because the current evidence felt sufficient.",
      "revision_needed": true,
      "revision": {
        "revision_type": "probe_revision",
        "location": "Decision point 4, immediately after the question about obtaining a vibration spectrum or oil sample",
        "current_defect": "The current wording conflates possible bounded rationality with justified operational triage. It says there was “probably” time if the operator pushed, but does not establish that a feasible additional check would have materially informed the decision or that the operator declined a minimally adequate review.",
        "minimal_change_instruction": "Add one narrowly focused probe and response establishing that a specific rapid check or control-room consultation could have been obtained before the surveillance deadline and would have distinguished the loose-guard explanation from a lubrication concern. Have the participant state that they did not ask whether that check could be arranged because completing the test with the existing partial picture seemed workable. Do not add an explicit bias label or portray the operator as ignoring every available check.",
        "preserve": [
          "The under-thirty-minute surveillance pressure",
          "The existing personnel and Shift Technical Advisor constraint",
          "The same continue-versus-trip decision",
          "The prior three decision points and their separate mechanisms",
          "The possibility that swapping trains could miss the window"
        ],
        "avoid_creating": [
          "A new confirmation-bias episode based on defending the loose-coupling-guard explanation",
          "A second salience episode by making the loud noise the sole basis for the final decision",
          "A causal claim that the missed diagnostic necessarily would have prevented the later maintenance outcome"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Recency Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Habit Intrusion",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Imperfect Rationality",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Salience Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Confirmation Bias",
      "decision_point": 2,
      "supporting_quote": "“So I figured this was probably the same kind of thing and didn't pull up the trend data right then.”",
      "mechanism": "The participant does not seek current trend evidence after forming an instrumentation explanation.",
      "confidence": 0.56,
      "status": "weak",
      "plausible_nonbias_explanation": "The lack of trend review is already the evidentiary consequence of the explicitly recent-event-based interpretation. The text does not show selective search for confirming evidence, active discounting of disconfirming evidence, or defense of the initial hypothesis independent of recency.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Anchoring",
      "decision_point": 2,
      "supporting_quote": "“My first thought honestly went back to the week before.”",
      "mechanism": "The prior false-alarm event serves as an initial interpretive anchor for the current RTD reading.",
      "confidence": 0.48,
      "status": "rejected",
      "plausible_nonbias_explanation": "The temporal specificity and centrality of the previous week's event make Recency Bias the more precise classification. Relabeling the same evidence as anchoring would duplicate rather than identify a distinct occurrence.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Attentional Tunneling",
      "decision_point": 3,
      "supporting_quote": "“The noise was what stood out, so that's what I focused on.”",
      "mechanism": "Attention narrows around the loud noise while other cues receive reduced reporting emphasis.",
      "confidence": 0.46,
      "status": "rejected",
      "plausible_nonbias_explanation": "This is not independently traceable from the intended Salience Bias occurrence; it describes the same comparative perceptual-weighting mechanism.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Eleven years of experience and use of a familiar lineup sequence",
      "location": "Opening role description and valve-lineup account",
      "why_not_bias": "Experience and routine execution are not biases by themselves. The relevant supported bias arises only because the participant explicitly reports that the overlearned routine displaced verification of a known modification."
    },
    {
      "cue": "Incomplete verbal turnover and an available but unprovided work-order attachment",
      "location": "Decision point 1",
      "why_not_bias": "This is an organizational-information-quality and handover-design constraint. It supports context for Habit Intrusion but does not itself demonstrate faulty cognition."
    },
    {
      "cue": "The LCO deadline, coordination burden, and unavailable Shift Technical Advisor",
      "location": "Decision point 4",
      "why_not_bias": "These are real resource and organizational constraints. They may rationally limit diagnostic options and cannot alone establish imperfect rationality."
    },
    {
      "cue": "The loudness and mechanical character of the knocking sound",
      "location": "Decision point 3",
      "why_not_bias": "A loud abnormal sound may appropriately deserve immediate operational attention. Salience Bias is supported only by the demonstrated disproportionate weighting of that cue relative to temperature and odor."
    },
    {
      "cue": "The later finding of degrading lubrication and unplanned maintenance",
      "location": "Final participant reflection",
      "why_not_bias": "An adverse later outcome does not retrospectively prove that the earlier reasoning was biased or unreasonable. It only provides outcome context."
    },
    {
      "cue": "The participant's retrospective statement that they would pull trend data earlier",
      "location": "Closing reflection",
      "why_not_bias": "This is a hindsight-informed learning statement. It corroborates the earlier self-described process but should not be counted as a new decision episode or a separate bias occurrence."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "The familiar routine contributed to failure to verify the added isolation valve against updated documentation.",
        "support": "The participant explicitly states that the routine sequence did not trigger a break from pattern despite the turnover mention and available attachment.",
        "assessment": "Moderately supported as a self-reported proximal process, though incomplete handover quality is a co-contributor."
      },
      {
        "claim": "The prior week's false alarm contributed to delayed review of current RTD trend information.",
        "support": "The participant directly links the remembered event to treating the current reading as probably instrumentation and not pulling the trend.",
        "assessment": "Strongly supported as a reported decision-process claim; it does not establish that earlier trend review would necessarily have changed the outcome."
      },
      {
        "claim": "The loud noise caused reduced attention to temperature and odor cues.",
        "support": "The participant reports that the noise stood out, was the focus of the radio report, and rendered the other cues footnotes.",
        "assessment": "Moderately supported as a comparative attentional-weighting claim."
      },
      {
        "claim": "Degrading lubrication caused the bearing to require unplanned maintenance.",
        "support": "The participant reports this as the eventual maintenance finding.",
        "assessment": "Plausible but weakly evidenced within the interview because no maintenance diagnosis, inspection finding, or technical record is described."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The later lubrication finding could be used to imply that the earlier temperature increase and odor conclusively signaled lubrication degradation.",
        "why": "The interview does not provide diagnostic specificity, timing, or maintenance evidence sufficient to establish that causal chain."
      },
      {
        "risk": "The fact that the noise was later identified as a loose coupling guard could be used to conclude that the noise had no operational relevance at the time.",
        "why": "Later diagnosis does not show that treating the noise as initially important was unreasonable; it only shows that the noise and lubrication issue may have had different sources."
      },
      {
        "risk": "The missed work-order verification could be attributed solely to Habit Intrusion.",
        "why": "The incomplete verbal turnover and lack of direct attachment handoff are plausible organizational contributors and should remain in the causal account."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "The interview contains three retrospective hypothetical probes: direct physical provision of the work-order attachment rather than a verbal turnover mention; absence of the prior week's false-alarm event; and lower perceptual intensity of the knocking noise. These do not implement the hidden specification's single bundled counterfactual of directly providing both the written work-order attachment and printed trend summary before lineup.",
    "held_constant": [
      "Operational objective and surveillance deadline are implicitly held constant in the participant's answers",
      "Personnel and plant configuration are not expressly re-specified in the interview's hypothetical probes",
      "The sequence of decision points remains unchanged in the interview narrative"
    ],
    "causal_coherence": "moderate",
    "explanation": "The probes improve mechanism observability: the participant predicts that direct documentation would alter valve verification, that removal of the recent false alarm might prompt earlier trend review, and that reduced noise salience might increase attention to temperature. They are plausible self-reported counterfactuals, but they are retrospective and not a controlled paired scenario. The hidden counterfactual variable is only partially represented because no printed trend summary is directly supplied in the interview, and the interview changes three different variables across separate probes."
  },
  "quality_scores": {
    "occupational_realism": 91,
    "cta_fidelity": 89,
    "bias_separability": 91,
    "bias_subtlety": 84,
    "control_fidelity": 100,
    "counterfactual_fidelity": 58,
    "narrative_coherence": 93,
    "naturalness": 88,
    "hidden_label_integrity": 94,
    "overall_quality": 85
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 3,
    "requested_occurrence_total": 4,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Retain the four-decision-point chronology and one-target-bias-per-decision-point allocation.",
      "Do not treat the later lubrication outcome as proof that every earlier decision was biased.",
      "Preserve the distinction between organizational constraints, such as incomplete turnover and LCO pressure, and the participant's reasoning process.",
      "Repair only the final imperfect-rationality episode; the other three target occurrences are already independently supported.",
      "Do not introduce the hidden bias labels into the dialogue.",
      "If counterfactual fidelity is a separate requirement, align the counterfactual probe with direct provision of both the work-order attachment and the trend summary while holding deadline, personnel, equipment configuration, and time pressure constant."
    ],
    "revision_order": [
      "Revise ir_01 at decision point 4 through a narrowly targeted probe establishing a feasible, decision-relevant minimum additional check that the participant chose not to pursue.",
      "If paired-counterfactual compliance is required, revise the existing handover hypothetical so it tests the specified combined documentation-and-trend-summary intervention without modifying other causal variables.",
      "Re-audit to ensure the final revision remains a bounded-evidence integration episode and does not create a separate confirmation, salience, or hindsight occurrence."
    ]
  },
  "failure_flags": [
    {
      "flag": "IR_01_JUSTIFICATION_AMBIGUITY",
      "severity": "medium",
      "detail": "The final decision may represent rational operational triage under genuine time and coordination constraints rather than imperfect rationality. The interview does not yet establish that the participant declined a feasible and decision-relevant minimum diagnostic process."
    },
    {
      "flag": "COUNTERFACTUAL_SPEC_PARTIAL_MISMATCH",
      "severity": "low",
      "detail": "The hidden counterfactual specifies direct provision of both the written work-order attachment and a printed trend summary. The interview tests direct attachment provision, prior-event removal, and reduced noise intensity in separate retrospective probes, but does not implement the specified bundled documentation intervention."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
