You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. This is for an internal review of decision-making during admissions, and I may ask follow-up questions as we go. Are you comfortable with that?

Participant: Yes, that's fine.

Interviewer: Can you tell me your role on the team during this admission?

Participant: I was the attending on the general medicine service, with a resident rotating through. We picked this patient up on day one after she came in for an unrelated complaint and the monitor flagged something new.

Interviewer: What was your overall goal for her care during the stay?

Participant: To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue.

Interviewer: Walk me through what happened, from the diagnosis to discharge.

Participant: The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own. Pharmacy checked for interactions with the DOAC we'd typically use and didn't find any, though they flagged her renal function was sitting at the low end of normal and wanted it monitored. The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down.

Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on. The formal assessment came back borderline — not clearly low, not clearly high. I also asked cardiology for a curbside opinion on timing anticoagulation after an unexplained pre-fall symptom, and their answer was honestly that the literature doesn't give a clean threshold for a case like this.

On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially. That took a day to sort out.

By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating. Discharge was set for the next morning. I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old.

On day four, right before discharge, she had a small bruise where blood had been drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for.

Interviewer: Let's go through each of those points in more detail. At the first one — right after diagnosis — what stood out most?

Participant: The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor.

Interviewer: What alternatives did you weigh?

Participant: Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose in the meantime. I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.

Interviewer: At the second point, with the comparator patient — what were you trying to do there?

Participant: Give the daughter an accurate answer instead of a reassuring guess. Without knowing the other patient's renal function or medications, I couldn't tell her anything meaningful, so I had the resident check before we talked further.

Interviewer: How much time pressure did that add?

Participant: Some — it pushed the conversation back a day, which mattered given discharge planning. But answering her with an unverified comparison seemed worse than the delay.

Interviewer: At the third point, after the comparison was clarified and fall risk was still borderline — what was the reasoning behind getting another renal check?

Participant: Her creatinine on admission was borderline, and dosing a DOAC on stale numbers, especially this close to discharge, didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct.

Interviewer: Had a similar situation come up for you before?

Participant: Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little.

Interviewer: At the fourth point, the bruise at discharge — how did that factor in?

Participant: It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result. We noted the bruise for the outpatient team and moved on.

Interviewer: If the fall-risk assessment had come back clearly low instead of borderline, would you have decided differently?

Participant: Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point.

Interviewer: If the comparator patient's chart details had been available immediately, do you think the outcome would have changed?

Participant: Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate.

Interviewer: Looking back, what would you tell a colleague facing something similar?

Participant: Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details. Beyond that, I think reasonable people could have made different calls at almost every step here.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Impact Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero intended occurrences for this control."
      },
      {
        "bias": "Omission Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero intended occurrences for this control."
      }
    ],
    "target_bias_names": ["Impact Bias", "Omission Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Impact Bias", "requested_occurrences": 0},
      {"bias": "Omission Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HC_Biased_2",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Ambigious_2",
    "domain_id": "HC",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: ambiguous_control condition requires zero intended occurrences of all named target biases; each of the four decision points was instead designed with a genuinely sufficient non-bias rationale (incomplete symptom workup, incomplete comparator data, pending renal check, pending lab result) that intentionally avoids instantiating the act-versus-omission blame mechanism or the disproportionate-imagined-impact mechanism from the paired biased scenario.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and setting",
      "Attending physician role and stakeholder roster",
      "Four-decision-point chronology and sequencing",
      "Core clinical facts: atrial fibrillation diagnosis, CHA2DS2-VASc of 4, HAS-BLED of 2",
      "Emotional tone and discharge time pressure",
      "Technical vocabulary and difficulty level"
    ],
    "generation_warnings": []}}

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
