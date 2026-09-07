You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Conservatism Bias", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 1 must show proportionate updating on new growth-rate evidence instead." },
      { "bias": "Experience Bias", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 2 must show experience weighed alongside explicit contextual differences instead." },
      { "bias": "Group Polarization", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 3 must show group convergence consistent with individual pre-call positions instead." },
      { "bias": "Groupthink", "occurrences": 0, "mechanism_constraint": "Zero intended instances; decision point 4 must show inclusion of the dissenting stakeholder and documented open follow-up instead of rapid unanimous closure." }
    ],
    "target_bias_names": ["Conservatism Bias", "Experience Bias", "Group Polarization", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Conservatism Bias", "requested_occurrences": 0 },
      { "bias": "Experience Bias", "requested_occurrences": 0 },
      { "bias": "Group Polarization", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "RT_Biased_4",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Vocab_Control_4",
    "domain_id": "RT",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition requires zero intended occurrences of all named biases across all four decision points. No allocation was performed; instead, each decision point that hosted a target bias mechanism in the paired biased scenario (RT_Biased_4) was redesigned with an evidence-proportionate, non-biased counterpart reasoning pattern occupying the same structural position.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and setting (90-mile subdivision, milepost 214 curve, cold snap)",
      "Actors and their roles",
      "Four-decision-point chronological structure",
      "Technical vocabulary and terminology level",
      "Difficulty level (moderate)",
      "Emotional tone (measured, professional, mild pressure)",
      "Approximate word count and dialogue format"
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
