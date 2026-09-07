You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Recency Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Habit Intrusion", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Salience Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Similarity Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Bounded Rationality", "occurrences": 0, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Recency Bias",
      "Habit Intrusion",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 0 },
      { "bias": "Recency Bias", "requested_occurrences": 0 },
      { "bias": "Habit Intrusion", "requested_occurrences": 0 },
      { "bias": "Salience Bias", "requested_occurrences": 0 },
      { "bias": "Similarity Bias", "requested_occurrences": 0 },
      { "bias": "Bounded Rationality", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "NP_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Vocab_Control_7",
    "domain_id": "NP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No bias occurrences are planned or allocated; this is a vocabulary-matched zero-bias control paired to NP_Biased_7. All four decision points are constructed to mirror the paired scenario's structure, phase order, actors, constraints, and vocabulary, with each decision resolved through active, evidence-weighing reasoning rather than any shortcut mechanism associated with the six target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational setting (catalytic reforming unit control room)",
      "Participant role and seniority",
      "Four-decision-point chronological structure",
      "Stakeholders (night operator, field operator, shift supervisor, process engineer)",
      "Core constraints (6-hour regeneration window, alarm nuisance history, limited field-verification availability, proxy-sensor limitation)",
      "Surface incident facts (alarm, pressure-differential trend, handover report, older drift note, heat shimmer, surge and tube-rupture precedents, closing checklist decision)",
      "Emotional tone and escalating time pressure",
      "Interview format, probe categories, and approximate word count"
    ],
    "generation_warnings": []
  }}}
- Validation report: {{VALIDATION_REPORT}}

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
