You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a post-event learning review, not for disciplinary purposes, and you're free to skip anything you're not comfortable discussing. Can you start by telling me your role and what you were assigned that shift?

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

Hidden generation specification:
{{"hidden_validation_specification": {
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

The hidden specification may include:
- condition;
- exact occurrence manifest;
- target bias names;
- requested occurrence count for each bias;
- planned instance IDs;
- intended decision points;
- intended mechanisms;
- intended strength;
- paired scenario ID;
- counterfactual variable.

Do not treat the hidden specification as evidence that a bias exists. It is a test plan only. The interview text is the evidence. If the specification and interview conflict, report the conflict.

CORE OCCURRENCE DEFINITIONS

A supported occurrence requires all of the following:
1. A distinct decision, inference, evidence-selection act, memory retrieval, prediction, causal attribution, or response to a probe.
2. Evidence showing how the participant processed, weighted, ignored, recalled, interpreted, or updated information.
3. A mechanism consistent with the named bias.
4. Enough context to distinguish the mechanism from a justified domain judgment or an ordinary mistake.

A single occurrence may span several adjacent sentences or one answer turn. Do not count repeated wording about the same reasoning episode as multiple occurrences. Count two occurrences separately only when they have distinct evidence traces, decision moments, evidence sources, or reasoning operations.

VALIDATION TASKS

1. Identify the domain, participant role, operational objective, and incident type.
2. Reconstruct the chronology and identify the decision points. Report whether exactly four decision points are present.
3. For every target bias in the hidden occurrence manifest, independently assess each requested occurrence.
4. Identify additional candidate biases not present in the target manifest.
5. Identify apparent bias cues that should not be labeled as bias.
6. Audit causal claims and counterfactual logic.
7. Evaluate interview quality and control fidelity.
8. Produce precise revision guidance when the interview does not satisfy its occurrence requirements.

FOR EACH REQUESTED OCCURRENCE, CLASSIFY IT AS ONE OF:

- supported: a distinct, textually supported instance is present;
- weak: a possible instance is present, but evidence or mechanism is insufficient;
- absent: no defensible instance is present;
- merged: the intended instance appears to be indistinguishable from another intended occurrence of the
  same bias or from another bias;
- accidental: an unintended instance appears outside the planned occurrence map;
- misclassified: the text supports a different bias or a non-bias explanation instead.

REVISION PRINCIPLES

If a requested occurrence is absent, weak, merged, or misclassified:
- Do not recommend simply repeating the bias label.
- Do not recommend adding an obvious textbook explanation.
- Specify the minimum local narrative or dialogue change needed to make that occurrence independently identifiable.
- Preserve the occupational setting, participant role, chronology, vocabulary, approximate length, and other intended bias occurrences.
- Do not create a new occurrence elsewhere merely to compensate.
- Do not strengthen every occurrence. Revise only the affected occurrence unless the evidence shows a broader structural problem.
- If strengthening the missing occurrence would make the interview too obvious, recommend a subtle evidence change rather than explicit labeling.
- If the requested occurrence is not plausible in the scenario, recommend changing the scenario or the target occurrence manifest rather than forcing implausible behavior.
- For controls, never recommend adding a target bias. If a control contains a defensible bias, recommend neutralizing or replacing the relevant reasoning episode.
- For a counterfactual, preserve the original and changed causal variables and do not introduce a second causal change while repairing bias evidence.

REVISION TYPES

Use one or more of these revision types:
- `none`: occurrence is adequately supported;
- `local_evidence_addition`: add or alter one cue, evidence source, or participant response;
- `local_reasoning_revision`: revise how the participant interprets or weighs evidence;
- `probe_revision`: change an interviewer question or hypothetical so the existing reasoning becomes independently observable;
- `decision_point_revision`: revise one decision point while preserving the rest;
- `remove_accidental_occurrence`: neutralize an unintended additional manifestation;
- `separate_merged_occurrences`: make two intended episodes distinct;
- `reclassify_bias`: change the target label or mechanism because the current label is not defensible;
- `scenario_revision`: revise the occupational situation because the requested occurrence is implausible.

REVISION SPECIFICITY

Each revision recommendation must include:
- the affected instance ID or `additional_candidate`;
- decision point and approximate turn or paragraph location;
- current status;
- evidence currently present, or `none`;
- precise defect;
- recommended revision type;
- minimal change instruction;
- what must remain unchanged;
- a warning against creating additional unintended occurrences;
- expected post-revision status.

Do not rewrite the complete interview. Provide revision instructions only. The generation system will apply
the instructions in a separate revision step.

OUTPUT

Return valid JSON only:
{
  "validator_version": "2.0",
  "interview_id": "...",
  "condition": "biased|vocabulary_control|ambiguous_control|counterfactual|unknown",
  "domain_assessment": {
    "domain": "...",
    "role": "...",
    "objective": "...",
    "incident_type": "...",
    "confidence": 0
  },
  "structure_audit": {
    "estimated_word_count": 0,
    "within_target_range": true,
    "decision_point_count": 0,
    "decision_points": [
      {
        "id": 1,
        "summary": "...",
        "evidence_before": [],
        "evidence_after": [],
        "goals_constraints": [],
        "alternatives": [],
        "decision_basis": "...",
        "time_pressure": "...",
        "uncertainty": "..."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "...",
      "bias": "...",
      "requested_occurrences_for_bias": 0,
      "status": "supported|weak|absent|merged|accidental|misclassified",
      "decision_point": 1,
      "supporting_quote": "...",
      "evidence_location": "...",
      "mechanism": "...",
      "strength": "absent|weak|moderate|strong",
      "confidence": 0,
      "plausible_nonbias_explanation": "...",
      "additional_evidence_needed": "...",
      "revision_needed": true,
      "revision": {
        "revision_type": "none|local_evidence_addition|local_reasoning_revision|probe_revision|decision_point_revision|remove_accidental_occurrence|separate_merged_occurrences|reclassify_bias|scenario_revision",
        "location": "...",
        "current_defect": "...",
        "minimal_change_instruction": "...",
        "preserve": [],
        "avoid_creating": [],
        "expected_post_revision_status": "supported|weak|absent|merged|accidental|misclassified"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "...",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "...",
      "decision_point": 1,
      "supporting_quote": "...",
      "mechanism": "...",
      "confidence": 0,
      "status": "candidate|supported|weak|rejected",
      "plausible_nonbias_explanation": "...",
      "revision_recommendation": "none|remove_or_neutralize|consider_adding_to_manifest"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "...",
      "location": "...",
      "why_not_bias": "..."
    }
  ],
  "causal_audit": {
    "causal_claims": [],
    "correlation_causation_risks": [],
    "counterfactual_present": false,
    "changed_variable": "...",
    "held_constant": [],
    "causal_coherence": "not_applicable|weak|moderate|strong",
    "explanation": "..."
  },
  "quality_scores": {
    "occupational_realism": 0,
    "cta_fidelity": 0,
    "bias_separability": 0,
    "bias_subtlety": 0,
    "control_fidelity": 0,
    "counterfactual_fidelity": 0,
    "narrative_coherence": 0,
    "naturalness": 0,
    "hidden_label_integrity": 0,
    "overall_quality": 0
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none|low|medium|high|reject",
    "recommended_action": "accept|revise|regenerate|reject",
    "global_revision_constraints": [],
    "revision_order": []
  },
  "failure_flags": []
}

COUNTING RULES FOR THE SUMMARY
- `supported_occurrence_total` counts only occurrences with status `supported`.
- `missing_occurrence_total` counts `weak`, `absent`, `merged`, and `misclassified` requested occurrences.
- `accidental_occurrence_total` counts unintended instances that should be removed or separately labeled.
- Set `recommended_action` to `accept` only when all requested occurrences are supported, no unacceptable accidental occurrences exist, and quality is adequate.
- Set it to `revise` when local changes can repair the interview without changing the scenario.
- Set it to `regenerate` when the scenario, decision structure, or several occurrences are fundamentally unsuitable.
- Set it to `reject` for severe incoherence, contaminated controls, or unrepairable causal confounding.

Return JSON only. Do not return a revised interview.
