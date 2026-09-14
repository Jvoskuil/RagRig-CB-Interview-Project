You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for talking with me. This is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not go into. Can you tell me about your role and how the Meridian Tower conversion came to you?

Participant: Happy to. I'm a plan review official in the building and fire division—permitting and life-safety sign-off, mainly. Meridian Tower was an adaptive reuse, a 22-story former office tower going to mixed-use residential and retail. The complication was the atrium, a large central void running most of the building height. It didn't fit the prescriptive smoke control provisions in our code, so the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the review done correctly within our statutory window. We had a 30-day clock, the department was short-staffed that quarter, and there was pressure from the city to keep housing projects moving. All of that mattered, but the core job was still making sure the building would actually perform the way the code intends if there's a fire.

Interviewer: Walk me through what happened, from the start.

Participant: The engineer of record was Halkirk & Vance, a regional firm with a lot of atrium experience—dozens of approved performance-based designs, and a neighboring jurisdiction had approved something similar from them the year before. They submitted a CFD-based smoke control model in place of the prescriptive system. We didn't have budget for an outside peer review that cycle, so I went through the documentation myself. One assumption stood out—how the model handled stack effect if a door were left partially open during an event—and I wasn't satisfied it was addressed clearly enough, so I sent that back to them in writing before finalizing anything. After that we moved into commissioning planning, where we had to choose between two verification protocols. Construction got underway, and about six weeks in, our inspector flagged fire-rated door deficiencies on three floors. Later, as we were approaching occupancy, the developer requested an early certificate before full integration testing was complete. Near the end of construction there was a small trash-chute fire—sprinklers handled it, no injuries—which led us to take another look at the atrium system, though it turned out to be a separate issue.

Interviewer: Let's put the order together more precisely. What did you know before the first major decision, and what came in after?

Participant: Before approving the design, I had the CFD report, the firm's general track record, and the neighboring jurisdiction's approval. After I sent back the question on the stack-effect assumption, they responded with additional documentation, and I approved based on that exchange. Then came the commissioning protocol decision. After that, construction started, and the door issue came up. The occupancy request was near the end, and the trash-chute fire happened after that decision was made, not before.

Interviewer: Let's take the first decision—approving the performance-based design. What carried the most weight?

Participant: The firm's documentation carried real weight, and so did the neighboring jurisdiction's approval—that told me the overall modeling approach had held up under scrutiny elsewhere. But I still went through the assumptions myself, and the stack-effect piece wasn't fully addressed for our specific geometry. I asked for a written clarification on that point specifically rather than taking the package at face value or sending the whole thing out for a full outside review, which would have added about three weeks.

Interviewer: Was a full peer review ever seriously on the table?

Participant: It was one of the options, yes. I decided a targeted clarification on the one assumption that mattered most for egress got me most of the benefit without the full delay.

Interviewer: Second decision—the commissioning protocol. What were you weighing?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's geometry according to the guidance, but its thresholds were only partly and qualitatively defined. Option B was the older prescriptive smoke test—clean binary pass-fail, but less sensitive to some of the failure modes this atrium could actually have.

Interviewer: Which did you choose, and why?

Participant: Option A, but not without addressing the enforcement problem. I built in defined interim checkpoints and documentation standards so the qualitative thresholds would still be auditable if anyone questioned the sign-off later. I didn't want to trade technical fit for administrative convenience, but I also didn't want a protocol I couldn't defend.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: The inspector found bad fire-door installations on floors 8, 11, and 14. My first instinct was to wonder if we had a specific crew problem. But crews were rotated randomly across the building, and it was three deficiencies out of roughly 150 doors checked at that point—which is within the range you'd expect from ordinary variation on a project this size. So I kept the original random-sample inspection plan across all floors rather than concentrating just on those three.

Interviewer: What did the rest of the inspection show?

Participant: The building-wide sample came back with a defect rate consistent with what we'd already seen—nothing suggesting those three floors were actually worse than the rest.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still about three weeks out. The contractor had a good record on other city jobs, and a colleague mentioned a nearby building that had gotten early partial occupancy without incident. But our own five-year data show something like a 15 percent rework rate on these atrium integration tests citywide, and that number is specific to the exact system we hadn't tested yet. So I granted occupancy only for the floors that didn't depend on the untested atrium system, and held back the rest until testing was done.

Interviewer: What would have made you grant broader occupancy at that point?

Participant: A completed, passed integration test, basically. Nothing short of that for the floors relying on that system.

Interviewer: How much uncertainty did you feel across these decisions?

Participant: Fairly consistent, honestly. The door situation had some ambiguity until the wider sample came back. The occupancy call had the most riding on it, which is part of why I drew the line where I did rather than treating the contractor's general history as settling the question.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It held up fine, as it turned out—the fire was in the chute enclosure, unrelated to the atrium system. If anything, it reinforced that the clarification I'd asked for on the stack-effect assumption was worth pursuing at the time, though I wouldn't say the fire proved anything either way about that decision.

Interviewer: If you had to make the temporary occupancy call again with the same information, would you do anything differently?

Participant: No, I think I'd draw the same line. The rework rate was too specific to ignore just because of a good general track record elsewhere.

Interviewer: Last question—what would you tell a newer reviewer facing a similar submittal?

Participant: Don't let a strong firm's name stand in for checking the one assumption that actually matters for your building, and don't let a small pattern in early data override what a proper sample tells you.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Clustering illusion",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Probability neglect or Base-Rate Neglect",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Optimism bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      }
    ],
    "target_bias_names": [
      "Clustering illusion",
      "Probability neglect or Base-Rate Neglect",
      "Optimism bias",
      "Ambiguity effect",
      "Authority Bias",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Clustering illusion", "requested_occurrences": 0 },
      { "bias": "Probability neglect or Base-Rate Neglect", "requested_occurrences": 0 },
      { "bias": "Optimism bias", "requested_occurrences": 0 },
      { "bias": "Ambiguity effect", "requested_occurrences": 0 },
      { "bias": "Authority Bias", "requested_occurrences": 0 },
      { "bias": "Hindsight bias", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HE_Biased_6",
    "counterfactual_variable": {
      "name": "engineering_firm_reputation",
      "original_state": "Nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "changed_state": "Not applicable in this generation run; condition is vocabulary_control, not counterfactual",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "All four decision points and their topical sequence"
      ]
    },
    "scenario_id": "HE_Vocab_Control_6",
    "domain_id": "HE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition mandates zero intended bias instances for every bias in the paired target set, overriding the occurrence counts listed in the input manifest. Decision-point topics were matched one-to-one against HE_Biased_6's four decision points to preserve structure while each was rewritten with an evidence-consistent, non-biased justification.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Occupational setting and stakeholders",
      "Four-decision-point structure and topical sequence",
      "Difficulty level and narrative complexity",
      "Emotional tone and overall word count",
      "Dialogue format (Interviewer/Participant turns)"
    ],
    "generation_warnings": [
      "The input occurrence manifest listed 1 occurrence for each of the six named biases; per the vocabulary_control condition rule, all occurrence counts were overridden to 0 in this generation, and the manifest above records that override explicitly rather than silently omitting the originally supplied counts."
    ]
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
