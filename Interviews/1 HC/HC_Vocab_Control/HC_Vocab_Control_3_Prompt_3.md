You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time. Just to confirm, this conversation is voluntary and for internal review of decision-making, not a formal chart audit. Okay to proceed?

Participant: Yeah, that's fine.

Interviewer: Can you set the scene—what was going on in the department that evening?

Participant: It was a Thursday night, pretty rough. We had four boarders in hallway beds waiting on inpatient rooms, so our effective capacity was well below normal. I was covering two other acute patients—a possible stroke and a kid with a fracture—when this chest pain patient came in. My second-year resident saw him first and then brought me in.

Interviewer: What was your first impression once you got involved?

Participant: 52-year-old man, generally healthy, pleuritic chest pain that was worse with deep breaths. Vitals were reassuring, sat 97%, heart rate 88. On exam I found reproducible tenderness over the chest wall, which does suggest something musculoskeletal, and he told me he'd been moving furniture two days earlier. That's a coherent story by itself. But he also mentioned, almost in passing, a 10-hour flight home from a trip about a week before, and a mild calf ache nobody had actually examined yet.

Interviewer: How did you weigh those pieces against each other?

Participant: The chest wall tenderness was a legitimate finding, so I wasn't going to dismiss it, but the flight and the calf comment gave me pause. Immobility plus a leg symptom is exactly the combination you don't want to explain away just because there's a tidier story sitting right in front of you. So I told the resident we'd hold off on a final impression until we actually looked at the leg directly.

Interviewer: What happened after that?

Participant: About twenty minutes later, the nurse rechecked him and confirmed mild swelling in the left calf, matching what he'd described. Around the same time, the resident came back with the D-dimer result—it had already been sent per our chest pain protocol—and it was mildly elevated, just above the assay cutoff.

Interviewer: Walk me through your thinking once you had that result.

Participant: A borderline D-dimer doesn't mean much on its own; it depends on the pretest probability going in. With the calf swelling now confirmed, I sat with the resident and we recalculated the Wells score properly, incorporating the leg finding this time rather than just the original picture. That pushed him into a range where imaging felt genuinely warranted, not just a reaction to one number.

Interviewer: How much did the scanner queue or bed pressure factor into that?

Participant: It was there in the background—40-minute queue behind trauma, charge nurse pushing to free up beds—but I didn't let that skip the reassessment step. I wanted the score redone first. Once that supported imaging, the practical pressure just meant asking radiology to prioritize him within their existing queue.

Interviewer: Tell me about the conversation regarding Dr. B's earlier patient.

Participant: While we were waiting on the CTPA, the charge nurse mentioned Dr. B had a similar-looking patient the week before—same kind of pleuritic pain—and discharged him without imaging. She said the patient did fine afterward.

Interviewer: What was your reaction to hearing that?

Participant: Honestly, my first thought was that I didn't know enough to judge it either way. Did he do a formal Wells score? Was it PERC-negative? A good outcome doesn't tell you whether the underlying reasoning was sound—some borderline calls work out fine by chance. I asked the resident to pull the chart before forming any real opinion.

Interviewer: What did you find?

Participant: Dr. B had documented a formal low-risk Wells score and a negative PERC before discharging that patient. So there was actual structure behind the decision, not just a guess that happened to land well.

Interviewer: Did that change your view?

Participant: It confirmed what I suspected—that it was a reasonable, defensible call given what he knew. If it had gone badly instead, with the same documented workup, I'd still call it reasonable. The outcome doesn't really tell you much about the quality of the reasoning behind it.

Interviewer: Let's get to the end of your shift. What was the situation with your patient by then?

Participant: PE was ruled out on the CTPA, though it picked up a small lung nodule needing outpatient follow-up, and he'd had a mild contrast reaction that took about 45 minutes to settle. By the time all that resolved, he was stable, but the visit had gotten more complicated than expected. The hospitalist I called wasn't eager to admit someone with a negative PE workup, and the patient and his wife were anxious to leave. Handoff was closing in.

Interviewer: How did you decide between admitting and discharging?

Participant: I genuinely went back and forth. Part of the pull toward admission was that the visit had been eventful—the reaction, the nodule—but eventful isn't the same as unsafe. Clinically, admission wouldn't have changed anything overnight; the nodule needed outpatient pulmonology, not inpatient care. I discharged him with a follow-up scheduled within the week and clear return precautions, but I told the resident honestly it could have gone either way.

Interviewer: What tipped it toward discharge in the end?

Participant: Mostly that nothing about his overnight risk profile had changed, and we had a real follow-up plan arranged quickly. The boarding pressure was present in the background, but I don't think it drove the decision. If anything, I spent more time on that disposition than I'd have liked given how busy we were.

Interviewer: What information, if it had been available earlier, would have changed how you handled the D-dimer result?

Participant: If the calf swelling had been documented at triage instead of found later, I probably would have gone straight to a formal risk score without the intermediate step of waiting on the nurse's recheck. It would have saved some time, though I don't think it would have changed the ultimate decision to image him.

Interviewer: If the department had been quiet that night, would you have handled things differently?

Participant: Not fundamentally—I still would have wanted the leg exam and the recalculated score before deciding on imaging. Busy or not, that step felt necessary once the calf came into the picture.

Interviewer: And if you'd learned about Dr. B's Wells score at the same time as the outcome, rather than afterward, would your reaction have been different?

Participant: No, I think I'd have asked the same question regardless of order—what did he actually know when he made the call. The outcome was almost beside the point for me.

Interviewer: Looking back, is there a moment you'd have handled differently?

Participant: Maybe I could have pushed radiology harder given how backed up we were. But on the clinical reasoning itself, I wouldn't change much. The disposition at the end is probably where I sat longest and still feel least certain—it was a genuinely close call, not an obvious one.
}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Premature Closure",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
      },
      {
        "bias": "Outcome Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
      },
      {
        "bias": "Action Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
      }
    ],
    "target_bias_names": [
      "Premature Closure",
      "Outcome Bias",
      "Action Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Premature Closure",
        "requested_occurrences": 0
      },
      {
        "bias": "Outcome Bias",
        "requested_occurrences": 0
      },
      {
        "bias": "Action Bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HC_Biased_3",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Vocab_Control_3",
    "domain_id": "HC",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control forces zero intended instances of all named target biases regardless of the caller-supplied manifest, which here identifies the paired target bias set (Premature Closure, Outcome Bias, Action Bias) rather than a nonzero request for this condition.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Setting, constraints, and time pressure profile",
      "Actor roster and roles",
      "Emotional tone",
      "Four-decision-point structure and sequencing",
      "Difficulty level"
    ],
    "generation_warnings": [
      "Caller-supplied manifest listed occurrences of 1 for each of three biases, matching the paired biased scenario's manifest; per condition rules for vocabulary_control, this was treated as the target bias identification for pairing purposes only, and all occurrences were overridden to 0 for this control scenario."
    ]}}}

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
