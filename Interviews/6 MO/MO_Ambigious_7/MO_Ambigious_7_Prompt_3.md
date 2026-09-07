You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making the time. This is a confidential debrief on the cargo transfer job alongside the platform, purely to understand the reasoning behind decisions on the day — not a disciplinary review. Comfortable proceeding?

Participant: Yes, go ahead.

Interviewer: Can you start with your role that day?

Participant: I was DPO on watch, running DP2 station-keeping during a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normal job in most respects. Hold position off the leg, crane operator takes the lifts, we maintain the watch circle.

Interviewer: What made this one non-routine?

Participant: The forecast weather was closing in a bit faster than the morning brief suggested. Roughly a four-hour window before sea state would exceed the platform crane's limit. So there was schedule pressure, but nothing outside what we train for.

Interviewer: Walk me through what happened, start to finish.

Participant: On final approach I picked up a 1.7-meter discrepancy between HPR and the two DGPS units, which were agreeing with each other closely. The system had auto-weighted the DGPS pair and was showing green. I also remembered that HPR had an intermittent fault logged from a previous voyage — cleared, but never formally re-certified after that. Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach. We got alongside, transfer went smoothly through the first several lifts. About halfway — 55% of cargo across — Thruster 3 raised a yellow caution, reduced power available. Consequence analysis still showed adequate capability, but with less margin than we'd started with. I also knew that switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn't have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace. On the second-to-last lift, there was a wind shift that changed the footprint recommendation on the DP plot. I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately. The Master noticed the vessel's attitude shift a short time after and flagged it. For the final lift, OIM asked whether we could finish or should stand off. I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish. Partway through, our separation closed faster than either figure had suggested it would, and we suspended early and backed off. No contact, stayed inside the watch circle, but it was closer than planned.

Interviewer: Let's go back through that in order. What were you tracking at each stage?

Participant: Early on, reference systems and DP status, which is standard for closing distance. Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks. During the final lift specifically, the crane display gets priority per procedure, and whoever's free on the bridge picks up secondary monitoring — that shifted around a bit depending on what else was happening at the time.

Interviewer: On the reference discrepancy — talk me through the reasoning there.

Participant: DGPS1 and DGPS2 agreed tightly. HPR was off by 1.7 meters, and it had that fault history from a prior voyage — nothing currently logged against it, but nothing re-certifying it as fully sound either. Given a choice between two fresh, agreeing units and one with an open question mark over it, I leaned toward the DGPS pair. I didn't call it settled — I noted it as something to keep an eye on rather than a solved problem.

Interviewer: Did you consider pausing to pull HPR's diagnostic log before continuing?

Participant: I thought about it. It would have meant holding the approach for a few minutes with no clear guarantee it would tell us anything conclusive, since the fault history was intermittent by nature. I judged the DGPS agreement plus HPR's own track record gave enough basis to proceed, but I'll be honest, it wasn't a fully closed question either way.

Interviewer: Now the thruster caution — what went into continuing there?

Participant: The consequence analysis still cleared us, just with a smaller cushion than before. I also had a rough number for what a mode change would cost us time-wise against a window that was already tight. It came down to margin against time cost, and the margin figure won out. I can see an argument either way on that one.

Interviewer: Did the amount of cargo already moved factor into it?

Participant: Not as the reason, no — it was really the capability number and the time trade-off. Though I won't pretend having half the job done didn't make continuing feel like the more natural direction.

Interviewer: Move to the final lift and the footprint change. What was happening with attention at that point?

Participant: Standard procedure has the crane display as priority during an active lift. My co-operator was tied up confirming rigging on the radio for the next lift, which is a legitimate concurrent task, not something either of us could have dropped without creating a different problem. So the footprint change sat for a short while before either of us caught it.

Interviewer: Would reassigning that monitoring in the moment have been realistic?

Participant: Possibly, but it would have meant interrupting a rigging confirmation that also affects safety on the next lift. It's a genuine trade-off, not an obvious call either way.

Interviewer: Last one — the OIM's question about the final lift.

Participant: I looked at both numbers I had — time to finish and the current separation and capability readout — and both supported finishing at that moment. The margin just closed faster than either had indicated it would once we were actually maneuvering.

Interviewer: If the margin readout had shown a tighter number at that moment, would that have changed your answer?

Participant: Probably, yes — if the readout itself had been less favorable I'd have told him to stand off. The issue wasn't which number I used, it's that the number moved faster than expected.

Interviewer: Looking back at the whole sequence, does it seem like there were earlier signs of how close things got, or does it read that way mainly because of how it ended?

Participant: Honestly, I go back and forth on that. Individually, none of those things — the discrepancy, the caution, the workload split — crossed a line that demanded a different call. Whether they add up to something predictable in hindsight, or whether it just came together unluckily at the end, I'm genuinely not sure.

Interviewer: What would you tell a newer DPO facing something similar?

Participant: Don't treat any single reading in isolation, and keep checking whether your trade-offs still hold as conditions shift, not just at the point you first made them.

Interviewer: Anything you'd do differently?

Participant: Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady. Otherwise I think the calls were reasonable given what was in front of me at each point.

Interviewer: Appreciate you walking through this in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {"bias": "Confirmation Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; reference-preference decision must be justified by an independent fault-history rationale rather than motivated dismissal of disconfirming evidence"},
      {"bias": "Automation Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; any reliance on system status must be paired with reference to underlying diagnostic data, not deference to the status indicator alone"},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 0, "mechanism_constraint": "Must not manifest; delayed registration of the footprint cue must be explained by a legitimate concurrent workload allocation, not an unexplained attentional default"},
      {"bias": "Hindsight Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; retrospective reflection must explicitly question foreseeability rather than assert it was obvious"},
      {"bias": "Sunk cost bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; continuation rationale must reference forward-looking capability and time trade-offs, not completed cargo or elapsed effort"},
      {"bias": "Status Quo Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; configuration retention must follow from an explicit stated comparison of alternatives, not default preservation"},
      {"bias": "Framing Bias", "occurrences": 0, "mechanism_constraint": "Must not manifest; final-lift rationale must reference both time and margin information as jointly consulted, not one framing displacing the other"}
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias",
      "Sunk cost bias",
      "Status Quo Bias",
      "Framing Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Confirmation Bias", "requested_occurrences": 0},
      {"bias": "Automation Bias", "requested_occurrences": 0},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 0},
      {"bias": "Hindsight Bias", "requested_occurrences": 0},
      {"bias": "Sunk cost bias", "requested_occurrences": 0},
      {"bias": "Status Quo Bias", "requested_occurrences": 0},
      {"bias": "Framing Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MO_Biased_7",
    "counterfactual_variable": {
      "name": "N/A",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Ambigious_7",
    "domain_id": "MO",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: ambiguous_control condition requires zero intended bias occurrences across all four decision points. Each decision point that hosted a bias mechanism in the paired MO_Biased_7 scenario (reference discrepancy, thruster caution, footprint cue, OIM final-lift query) is instead constructed with an explicit, independently defensible non-bias rationale of comparable narrative weight and complexity, preserving structural and vocabulary parity without instantiating any named mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Vessel class and DP2 operating mode",
      "Platform setting and weather-window premise",
      "Four-decision-point chronology and sequence",
      "Stakeholder roles (Master, OIM, crane operator, superintendent)",
      "Technical vocabulary and terminology list",
      "Difficulty level and near-miss outcome ambiguity",
      "Interview probe structure and approximate word count"
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
