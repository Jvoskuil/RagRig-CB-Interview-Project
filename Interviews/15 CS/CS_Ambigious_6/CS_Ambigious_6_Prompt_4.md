You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Recency", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Availability Frequency", "occurrences": 0, "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit." },
      { "bias": "Exposure to limited alternatives", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Loss Framing", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 0, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Recency",
      "Availability Frequency",
      "Exposure to limited alternatives",
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency", "requested_occurrences": 0 },
      { "bias": "Availability Frequency", "requested_occurrences": 0 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 0 },
      { "bias": "Loss Framing", "requested_occurrences": 0 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "CS_Biased_6",
    "counterfactual_variable": {
      "name": "Not applicable in this condition",
      "original_state": "Not applicable",
      "changed_state": "Not applicable",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Analyst role, staffing, and tooling"
      ]
    },
    "scenario_id": "CS_Ambigious_6",
    "domain_id": "CS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No occurrences requested; ambiguous_control condition requires zero intended instances of all named target biases. Decision points were instead constructed to preserve genuine ambiguity and plausible non-bias justifications at each of the four decision points, mirroring the structural positions used for bias instances in the paired biased scenario (CS_Biased_6) without instantiating any bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "CVE technical details and CVSS score",
      "Backlog composition and the older database finding",
      "48-hour compliance deadline",
      "Analyst role, staffing, and tooling",
      "Four-decision-point structure and domain vocabulary matching CS_Biased_6"
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
