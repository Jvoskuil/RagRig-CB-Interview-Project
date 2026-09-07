You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Just to confirm, this conversation is being used to understand how decisions get made during unusual shifts — not to evaluate your performance. Is that okay with you?

Participant: Yeah, that's fine. I've done these debriefs before after incidents, so no problem.

Interviewer: Great. Can you start by telling me your role and what made this particular night shift nonroutine?

Participant: Sure. I'm the yardmaster on the night shift at the hump yard. That night was messy from the start — one of our two hump leads was down for signal maintenance, so we were running everything through a single lead. On top of that, we were short two carmen because of storm callouts, and it was raining hard enough that the retarders weren't behaving predictably on wet rail. We also had an SLA connection window we needed to hit for an outbound customer train, so there was real pressure to keep things moving.

Interviewer: Walk me through how the shift actually unfolded.

Participant: When I came on, the relief briefing was rushed — the prior yardmaster was trying to get out before the worst of the storm hit, so he gave me the switch list verbally: 38 cars, expected to have the cut classified by 2200. That was my starting point for the night. Then the inbound train came in about 40 minutes late, and when we actually counted, it was 41 cars, not 38. The retarders were also cycling slower than normal because of the wet rail. So already things were behind where the paperwork said they'd be.

A while into classification, the hot-box detector flagged one car, GATX 88213, with a temperature reading that was elevated but still within tolerance — borderline, not a clear alarm. That detector's given us false positives before in wet weather. But we'd had a derailment at this yard about three weeks earlier from an overheated bearing on a similar car, and that was fresh in my mind. I made the call to pull the whole eleven-car cut it was sitting in for inspection, not just that one car.

Two carmen inspected it. One found a hairline mark near the knuckle, unrelated to the bearing issue. The other inspected independently and cleared it, no defect found. There was also an old repair entry on that car from two inspection cycles back, already closed out. I ended up treating it as still suspect and asked for a third pass. That ate more time. By the end, we were running about 55 minutes behind, with the SLA window closing in 40. I set that car out and dispatched the rest of the train.

Interviewer: Let's slow down and go through each of those moments. Starting with the ready-time estimate — you had 38 cars and a 2200 target from the handoff, then learned it was 41 cars with slower cycling. What went through your mind?

Participant: Honestly, I kept 2200 as my working target. I nudged it a little in my head, but I didn't sit down and recalculate from the new numbers. Part of it was trust — the relief yardmaster's been doing this longer than me, and his estimates are usually solid. Part of it was just not wanting to move the target this early and cause confusion down the line for the dispatcher.

Interviewer: What alternatives did you consider at that point?

Participant: I could've recalculated from scratch with the actual count and the cycle speed we were seeing. Or radioed the hump conductor for his read on pace before locking anything in. I didn't do either right away — I just carried the number forward.

Interviewer: What would have made you recalculate immediately instead of adjusting slightly?

Participant: Probably if the discrepancy had been bigger — if it'd been 50 cars instead of 41, I think I'd have thrown the original number out completely. Three extra cars didn't feel like enough to abandon the plan.

Interviewer: Now the hot-box alert. The reading was borderline, and you know that detector throws false positives in wet weather. What drove the decision to pull the full eleven-car cut instead of just the flagged car?

Participant: The derailment three weeks back was still sitting with me. That one started exactly this way — a reading that didn't look dramatic at first. I didn't want a repeat, so I went bigger than the book probably called for. Standard procedure would've been to isolate just GATX 88213 for a manual check. I pulled the whole cut.

Interviewer: Did you weigh the detector's false-positive history in that moment?

Participant: I knew about it, yeah. But it didn't carry the same weight as the derailment did. That one's the thing that comes to mind first when a hot-box alert comes in here, even though logically the wet-weather false positives happen a lot more often.

Interviewer: Then you had two conflicting carman reports — one found a hairline mark, the other cleared the car. How did you resolve that?

Participant: I leaned toward Carman A's finding. There was also that old repair entry on the car, even though it was closed out and unrelated to the bearing concern. Between the mark and that history, it felt like enough to keep the car flagged. I asked for a third inspection rather than accepting Carman B's clearance.

Interviewer: What made Carman A's report and the old repair note feel more convincing than Carman B's clearance?

Participant: Looking back, I'm not entirely sure I can justify that cleanly. Carman B followed the same protocol, same timeframe. I think once I already suspected the car, the mark and the repair history just fit what I expected to find. Carman B's "all clear" almost read to me like it needed double-checking, when really it should've carried equal weight.

Interviewer: What would have changed that call — if anything?

Participant: If Carman B's report had come in first, before Carman A's, I might have closed it out right there. Order mattered more than it should have, probably.

Interviewer: Last decision — the SLA deadline was closing in, and the car was still unresolved. What did you decide?

Participant: I set the car out and dispatched the rest of the train. Holding the whole consist for one car wasn't going to help anyone, and the dispatcher confirmed we'd only eat a partial penalty instead of a full one if we released the rest on time. That one felt like a straightforward trade-off, not a hard call.

Interviewer: How did things turn out?

Participant: The third inspection came back clean — no defect on GATX 88213. The train made it out with a partial penalty instead of the full one.

Interviewer: If the derailment three weeks earlier had never happened, do you think the hot-box call goes differently?

Participant: Probably, yeah. I think I isolate just the one car and keep moving.

Interviewer: And if you ran this same shift again tomorrow, what would you do differently?

Participant: I'd probably push back harder on the initial time estimate instead of just carrying it forward, and I'd try to look at both carmen's reports side by side instead of one at a time. Other than that, given what I knew in the moment, I'd probably land in a similar place.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Anchoring Effect",
        "occurrences": 1,
        "mechanism_constraint": "Insufficient adjustment from a handed-off numeric/time estimate despite materially different new information."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Overweighting a vivid recent memory of an incident over calibrated base-rate/detector-history information."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Selective weighting of evidence corroborating a pre-existing hypothesis while discounting disconfirming evidence of comparable procedural credibility."
      }
    ],
    "target_bias_names": [
      "Anchoring Effect",
      "Availability Bias",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Anchoring Effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Availability Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Confirmation Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "decision_point": 1
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "mechanism": "Insufficient adjustment away from the prior shift's 2200/38-car estimate despite new information (41 cars, slower cycle time).",
        "affected_reasoning_operation": "Time-target estimation and revision",
        "evidence_source": "Prior-shift switch list vs. current arrival count and observed cycle speed",
        "distinctiveness_requirement": "Must be the only instance where a numeric/time target from a handoff document is under-adjusted; not to be repeated at any other decision point."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recent derailment memory disproportionately inflates the perceived risk of a borderline, statistically ordinary detector reading, overriding known false-positive base rate.",
        "affected_reasoning_operation": "Risk/severity assessment of a sensor alert",
        "evidence_source": "Hot-box detector reading and detector false-positive history vs. recalled derailment incident",
        "distinctiveness_requirement": "Must be the sole instance tied to recalled-incident-driven risk inflation; must not reappear as justification in decision points 3 or 4."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective acceptance of evidence (Carman A's mark, old repair note) that supports an existing defect hypothesis, paired with discounting of procedurally equivalent disconfirming evidence (Carman B's clearance).",
        "affected_reasoning_operation": "Integration and weighting of conflicting inspection evidence",
        "evidence_source": "Carman A report and repair-history entry vs. Carman B's independent clearance",
        "distinctiveness_requirement": "Must be the only instance involving asymmetric weighting of two competing carman reports; not to be conflated with the availability-driven risk framing at decision point 2."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "strength": "subtle"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_3",
    "domain_id": "RT",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per bias assigned to its own distinct decision point (1, 2, 3) based on mechanism fit: anchoring to the initial numeric estimate revision, availability to the sensor-risk assessment invoking a recalled incident, confirmation to the conflicting-evidence integration step. Decision point 4 deliberately left bias-free to preserve a genuine, non-mechanical trade-off and satisfy the exactly-4-decision-point requirement without introducing unrequested instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
